#!/usr/bin/env python3
from __future__ import annotations
################################################################################
## ai-building-blocks-agent/app/llm/dynamic.py
## Copyright (c) 2025 Jeff Teeter, Ph.D.
## Cisco Systems, Inc.
## Licensed under the Apache License, Version 2.0 (see LICENSE)
## Distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND.
################################################################################
 
"""
DISCLAIMER: USE AT YOUR OWN RISK

This software is provided "as is", without any express or implied warranties, including, but not limited to,
the implied warranties of merchantability and fitness for a particular purpose. In no event shall the authors or
contributors be liable for any direct, indirect, incidental, special, exemplary, or consequential damages
(including, but not limited to, procurement of substitute goods or services; loss of use, data, or profits;
or business interruption) however caused and on any theory of liability, whether in contract, strict liability,
or tort (including negligence or otherwise) arising in any way out of the use of this software.

This script is provided for demonstration and development purposes only and is not intended for use in production
environments. You are solely responsible for any modifications or adaptations made for your specific use case.

By using this code, you agree that you have read, understood, and accept these terms.
"""

"""
Dynamic helper that chooses the correct vector-search retriever and
builds the diet-function list the LLM receives.

* Never raises AttributeError if a given retriever class name is missing.
* Supports Chroma, Azure Cognitive Search and Elastic back-ends out-of-the-box.
* Falls back to the first “SomethingRetriever” class it can find, so adding new
  back-ends later is zero-touch.

ENV VARS
--------
FASTAPI_VECTOR_BACKEND          chroma | azure | elastic   (default: chroma)
FASTAPI_CHROMA_COLLECTION_PLATFORM  override Chroma collection name
"""
import importlib
import inspect
import json
import os
from pathlib import Path
from typing import Any, Dict, List

# ─────────────────────────────────────────────────────────────────────────────
# 1.  Pick retriever backend
# ─────────────────────────────────────────────────────────────────────────────
BACKEND = os.getenv("FASTAPI_VECTOR_BACKEND", "chroma").lower()

RETRIEVER_MODULES: dict[str, str] = {
    "chroma":  "retrievers.chroma_retriever",
    "azure":   "retrievers.azure_search_retriever",
    "elastic": "retrievers.elastic_retriever",
}
if BACKEND not in RETRIEVER_MODULES:
    raise ValueError(
        f"Unsupported FASTAPI_VECTOR_BACKEND={BACKEND!r}. "
        f"Expected one of: {', '.join(RETRIEVER_MODULES)}"
    )

mod = importlib.import_module(RETRIEVER_MODULES[BACKEND])

# Try the common names first, then fall back to “any *Retriever class”
Retriever = (
    getattr(mod, "FunctionRetriever", None)
    or getattr(mod, "ChromaRetriever", None)
    or getattr(mod, "AzureSearchRetriever", None)
    or getattr(mod, "ElasticRetriever", None)
)

if Retriever is None:
    for attr in dir(mod):
        obj = getattr(mod, attr)
        if inspect.isclass(obj) and attr.endswith("Retriever"):
            Retriever = obj
            break

if Retriever is None:  # still nothing?  bail out clearly.
    raise ImportError(
        f"No retriever class found in module {RETRIEVER_MODULES[BACKEND]}"
    )

# ─────────────────────────────────────────────────────────────────────────────
# 2.  Instantiate a singleton
# ─────────────────────────────────────────────────────────────────────────────
if BACKEND == "chroma":
    retriever = Retriever(
        collection_name=os.getenv(
            "FASTAPI_CHROMA_COLLECTION_PLATFORM",
            "platform-summaries-index",
        )
    )
    # honour dynamic override if the Chroma client exposes helpers
    custom_col = os.getenv(
        "FASTAPI_CHROMA_COLLECTION_PLATFORM",
        "platform-summaries-index",
    )
    if hasattr(retriever, "set_collection"):
        retriever.set_collection(custom_col)
    elif hasattr(retriever, "collection_name"):
        setattr(retriever, "collection_name", custom_col)
else:  # Azure / Elastic (both accept layer kwarg)
    retriever = Retriever(layer="FASTAPI")

# ─────────────────────────────────────────────────────────────────────────────
# 3.  Full-schema KV (lazy build + cache)
# ─────────────────────────────────────────────────────────────────────────────

DYNAMIC_CACHE_ROOT = Path(
    os.getenv(
        "PLATFORM_DYNAMIC_CACHE_PATH",
        # Default: <repo-root>/src/app/llm/platform_dynamic_cache
        (Path(__file__).resolve().parent        / "platform_dynamic_cache").as_posix(),

    )
).resolve()
DYNAMIC_CACHE_ROOT.mkdir(parents=True, exist_ok=True)

CACHE_FILE = DYNAMIC_CACHE_ROOT / "full_schemas.json"
SPEC_DIR   = Path(__file__).resolve().parent / "openapi_specs"


def _build_full_kv() -> Dict[str, Any]:
    """Load `openapi_specs/full_*.json` files into a single lookup table."""
    kv: dict[str, Any] = {}
    for fp in SPEC_DIR.glob("full_*.json"):
        platform = fp.stem.replace("full_", "")
        spec     = json.loads(fp.read_text(encoding="utf-8"))
        for path_item in spec.get("paths", {}).values():
            for op in path_item.values():
                op_id = op.get("operationId")
                if op_id:
                    kv[f"{platform}:{op_id}"] = op
    CACHE_FILE.write_text(json.dumps(kv), encoding="utf-8")
    return kv


FULL_KV: Dict[str, Any] = (
    json.loads(CACHE_FILE.read_text(encoding="utf-8"))
    if CACHE_FILE.exists()
    else _build_full_kv()
)

# ─────────────────────────────────────────────────────────────────────────────
# 4.  Public helpers
# ─────────────────────────────────────────────────────────────────────────────
def build_functions_for_llm(
    query: str,
    enabled: list[str],
    *,
    token_budget: int = int(os.getenv("FASTAPI_FUNCTION_TOKEN_BUDGET", 16_384)),
    k: int = int(os.getenv("FASTAPI_FUNCTION_TOP_K", 50)),
 
) -> List[dict]:
    """
    Return a list of diet-function JSON objects that the LLM will receive.

    1. Top-k vector search over enabled platforms.
    2. Lexical fallback: include any function whose *name* contains a user token
       (case-insensitive, plural⇢singular). Lexical hits are prepended so they
       always survive trimming.
    3. Trim JSON payload to fit within *token_budget*.
    """
    # ── 1. vector search ────────────────────────────────────────────────
    vec_hits: list[dict] = retriever.query(
        query,
        k=k,
        filter={"platform": {"$in": enabled}},
    )
    have: set[str] = {d["name"] for d in vec_hits}

    # ── 2. lexical fallback  ────────────────────────────────────────────
    raw_tokens = [t.lower().strip(".,!?") for t in query.split()]
    tokens: set[str] = set()
    for tok in raw_tokens:
        tokens.add(tok)
        if tok.endswith("s") and len(tok) > 3:
            tokens.add(tok[:-1])

    lex_hits: list[dict] = []
    for platform in enabled:
        every = retriever.query(
            "",                  # empty query returns everything
            k=200,               # 🔥 lowered from 1000 → 200
            filter={"platform": {"$in": [platform]}},
        )
        for d in every:
            if d["name"] in have:
                continue
            if any(tok in d["name"].lower() for tok in tokens):
                lex_hits.append(d)
                have.add(d["name"])

    # lexical hits *first* → they survive trimming
    docs = lex_hits + vec_hits

    # ── 3. unwrap  + schema-sanity  + trimming ─────────────────────────
    size = 0
    out: list[dict] = []

    for d in docs:
        try:
            fn_schema = json.loads(d["content"])
        except (KeyError, json.JSONDecodeError):
            continue

        # fix OpenAI array-schema quirk (missing "items")
        for pschema in fn_schema.get("parameters", {}).get("properties", {}).values():
            if pschema.get("type") == "array" and "items" not in pschema:
                pschema["items"] = {"type": "string"}

        payload = json.dumps(fn_schema, separators=(",", ":"))
        if size + len(payload) > token_budget:
            break

        size += len(payload)
        out.append(fn_schema)

    return out


def full_schema_lookup(platform: str, name: str) -> dict | None:
    """Return the full OpenAPI operation object (or `None` if not found)."""
    return FULL_KV.get(f"{platform}:{name}")

