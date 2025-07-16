#!/usr/bin/env python3
from __future__ import annotations
################################################################################
## src/scripts/index_functions.py
## Copyright (c) 2025 Jeff Teeter
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
Index every *diet* function schema (or a single platform) into the vector-store
selected for the FASTAPI layer.  Supports Chroma, Azure AI Search, and
Elasticsearch.

Examples
--------
# one platform
python -m scripts.index_functions --platform meraki

# everything under app/llm/function_definitions
python -m scripts.index_functions --all
"""
# ── stdlib ────────────────────────────────────────────────────────────────
import argparse
import importlib
import json
import os
import sys
from pathlib import Path
from types import ModuleType
# ── third-party ───────────────────────────────────────────────────────────
from dotenv import load_dotenv
# ── internal ──────────────────────────────────────────────────────────────
from app.utils.paths          import ensure_abs_env

# ══════════════════════════════════════════════════════════════════════════
# 0.  Environment & basic paths
# ══════════════════════════════════════════════════════════════════════════
load_dotenv()

# ── dynamic repo & module paths ────────────────────────────────────────
from app.utils.paths import ensure_abs_env, REPO_ROOT as UTIL_REPO_ROOT

# true repo root (suite-cisco-ai-building-blocks)
REPO_ROOT = UTIL_REPO_ROOT

# LLM folder (override with LLM_DIR in .env if needed)
LLM_DIR  = ensure_abs_env("LLM_DIR", "src/app/llm")

# diet schemas folder (override via DIET_DIR)
DIET_DIR = ensure_abs_env("DIET_DIR", "src/app/llm/function_definitions")

# full OpenAPI specs folder (override via FULL_DIR)
FULL_DIR = ensure_abs_env("FULL_DIR", "src/app/llm/openapi_specs")

 

BACKEND     = os.getenv("FASTAPI_VECTOR_BACKEND", "chroma").lower()

# ── guarantee absolute Chroma path (only when using Chroma) ───────────────
if BACKEND == "chroma":
    # layer-scoped DB path (repo-relative default)
    ensure_abs_env("FASTAPI_CHROMA_DB_PATH", "chroma_dbs/fastapi")
    

# ══════════════════════════════════════════════════════════════════════════
# 1.  Import the correct indexer implementation
# ══════════════════════════════════════════════════════════════════════════
INDEXER_MODULES: dict[str, str] = {
    "chroma":  "db_scripts.indexers.chroma_indexer",
    "azure":   "db_scripts.indexers.azure_indexer",
    "elastic": "db_scripts.indexers.elastic_indexer",
}

try:
    Indexer = getattr(
        importlib.import_module(INDEXER_MODULES[BACKEND]),
        "PlatformFunctionIndexer"
    )
except KeyError as exc:
    raise RuntimeError(
        f"Unsupported backend '{BACKEND}'. "
        f"Choose from: {', '.join(INDEXER_MODULES)}."
    ) from exc

# ══════════════════════════════════════════════════════════════════════════
# 2.  Index a single platform
# ══════════════════════════════════════════════════════════════════════════
def index_one(platform: str) -> None:
    diet_path = DIET_DIR  / f"{platform}.json"
    full_path = FULL_DIR  / f"full_{platform}.json"

    if not diet_path.exists():
        raise FileNotFoundError(f"Missing diet schema: {diet_path}")
    if not full_path.exists():
        raise FileNotFoundError(f"Missing full OpenAPI spec: {full_path}")

    diet_fns  = json.loads(diet_path.read_text())
    full_spec = json.loads(full_path.read_text())

    # Azure OpenAI: function names must be ≤ 64 characters
    for fn in diet_fns:
        if len(fn.get("name", "")) > 64:
            orig = fn["name"]
            fn["name"] = orig[:64]
            print(f"[WARN] Truncated long function name: {orig!r} → {fn['name']!r}")

    # collection / index name selected from env for the chosen backend
    if BACKEND == "chroma":
        index_name = os.getenv("FASTAPI_CHROMA_COLLECTION_PLATFORM",
                               "function-definitions-index")
    elif BACKEND == "azure":
        index_name = os.getenv("FASTAPI_AZURE_PLATFORM_INDEX",
                               "platform-summaries-index")
    else:  # elastic
        index_name = os.getenv("FASTAPI_ELASTIC_PLATFORM_INDEX",
                               "platform-summaries-index")

    indexer = Indexer(index_name=index_name, layer_name="FASTAPI")
    print(f"→ indexing {platform} …", flush=True)
    indexer.index_functions(platform, diet_fns, full_spec)
    print(f"✓ {platform}: {len(diet_fns)} functions indexed via {BACKEND}")

# ══════════════════════════════════════════════════════════════════════════
# 3.  CLI entry-point
# ══════════════════════════════════════════════════════════════════════════
def cli() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--platform", help="meraki, catalyst, …")
    ap.add_argument("--all", action="store_true",
                    help="index every diet_*.json found")
    args = ap.parse_args()

    if args.platform and args.all:
        raise SystemExit("--platform and --all are mutually exclusive")

    if args.all:
        platforms = [p.stem for p in DIET_DIR.glob("*.json")]
    elif args.platform:
        platforms = [args.platform]
    else:
        raise SystemExit("Specify --platform <name> or --all")

    for plat in platforms:
        index_one(plat)

if __name__ == "__main__":
    cli()