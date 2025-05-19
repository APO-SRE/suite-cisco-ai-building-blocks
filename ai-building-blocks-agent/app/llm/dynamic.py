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

import importlib
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
mod = importlib.import_module(RETRIEVER_MODULES[BACKEND])
Retriever = (
    getattr(mod, "FunctionRetriever", None)
    or getattr(mod, "ChromaRetriever")          # chroma package uses this name
)

# Instantiate once
if BACKEND == "chroma":
    retriever = Retriever(
        collection_name=os.getenv(
            "FASTAPI_CHROMA_COLLECTION_PLATFORM",
            "platform-summaries-index",
        )
    )
    custom_col = os.getenv("FASTAPI_CHROMA_COLLECTION_PLATFORM", "platform-summaries-index")
    if hasattr(retriever, "set_collection"):
        retriever.set_collection(custom_col)
    elif hasattr(retriever, "collection_name"):
        setattr(retriever, "collection_name", custom_col)
else:  # Azure / Elastic
    retriever = Retriever(layer="FASTAPI")

# ─────────────────────────────────────────────────────────────────────────────
# 2.  Full-schema KV (lazy build + cache)
# ─────────────────────────────────────────────────────────────────────────────
DB_ROOT   = Path(os.getenv("CHROMA_DB_ROOT",
                           "../ai-building-blocks-database/chroma_dbs")).resolve()
CACHE_DIR = DB_ROOT / "fastapi"
CACHE_DIR.mkdir(parents=True, exist_ok=True)
CACHE_FILE = CACHE_DIR / "full_schemas.json"

SPEC_DIR = Path(__file__).resolve().parent / "openapi_specs"

def _build_full_kv() -> Dict[str, Any]:
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
# 3.  Public helpers
# ─────────────────────────────────────────────────────────────────────────────
def build_functions_for_llm(
    query: str,
    enabled: list[str],
    *,
    token_budget: int = 16_384,  # 4 × the previous room
    k: int = 50,                 # 🔥 lowered from 300 → 50
) -> List[dict]:
    """
    Return a list of diet-function JSON objects that the LLM will receive.

    1. Start with the *k* nearest-neighbour matches from the vector index.
    2. Run a lexical fallback: pick up any extra diet-functions whose *name*
       literally contains a user token (case-insensitive, plural⇢singular).
       **Lexical matches are prepended so they always survive trimming.**
    3. Trim so that the total JSON payload fits within *token_budget*.
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

    # put lexical hits *first* so they survive trimming
    docs = lex_hits + vec_hits

    # ── 3. unwrap  + schema-sanity  + trimming ──────────────────────────
    size   = 0
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
    return FULL_KV.get(f"{platform}:{name}")
