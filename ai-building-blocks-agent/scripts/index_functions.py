#!/usr/bin/env python3
from __future__ import annotations
################################################################################
## AI-Building-Blocks-Agent/scripts/index_functions.py
## Copyright (c) 2025 Jeff Teeter
## Cisco Systems, Inc.
## Licensed under the Apache License, Version 2.0 (see LICENSE)
## Distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND.
################################################################################
"""
DISCLAIMER: USE AT YOUR OWN RISK

Indexes **diet** schemas for all enabled Cisco platforms into the vector-store
backend configured for the FASTAPI layer (Chroma, Azure AI Search, or
Elasticsearch).

Usage
-----
    # Index one platform
    python -m scripts.index_functions --platform meraki

    # Index every diet_<platform>.json present in app/llm/function_definitions
    python -m scripts.index_functions --all
"""
import argparse
import importlib
import json
import os
import sys
import types
from pathlib import Path

from dotenv import load_dotenv

# ──────────────────────────────────────────────────────────────────────────────
# 0 ▸ environment & repo paths
# ──────────────────────────────────────────────────────────────────────────────
load_dotenv()

ROOT      = Path(__file__).resolve().parents[1]                 # repo root
LLM_DIR   = ROOT / "app" / "llm"
DIET_DIR  = LLM_DIR / "function_definitions"
FULL_DIR  = LLM_DIR / "openapi_specs"

# sibling repo that holds the DB-specific indexers
DB_REPO   = ROOT.parents[0] / "ai-building-blocks-database"
sys.path.append(str(DB_REPO))

# expose db_scripts.* as a pseudo-package so importlib can find it
db_pkg                = types.ModuleType("db_scripts")
db_pkg.__path__       = [str(DB_REPO / "scripts")]
sys.modules["db_scripts"] = db_pkg

BACKEND  = os.getenv("FASTAPI_VECTOR_BACKEND", "chroma").lower()
EMB_PROV = os.getenv("FASTAPI_EMBEDDING_PROVIDER", "azure").lower()

# ──────────────────────────────────────────────────────────────────────────────
# 1 ▸ dynamic import of the correct indexer
# ──────────────────────────────────────────────────────────────────────────────
INDEXER_MODULES = {
    "chroma":  "db_scripts.indexers.chroma_indexer",
    "azure":   "db_scripts.indexers.azure_indexer",
    "elastic": "db_scripts.indexers.elastic_indexer",
}

try:
    mod_name = INDEXER_MODULES[BACKEND]
except KeyError as exc:
    raise RuntimeError(
        f"Unsupported backend '{BACKEND}'. "
        f"Valid options: {', '.join(INDEXER_MODULES)}"
    ) from exc

Indexer = getattr(importlib.import_module(mod_name), "PlatformFunctionIndexer")

# ──────────────────────────────────────────────────────────────────────────────
# 2 ▸ index one platform
# ──────────────────────────────────────────────────────────────────────────────
def index_one(platform: str) -> None:
    diet_path = DIET_DIR  / f"{platform}.json"
    full_path = FULL_DIR  / f"full_{platform}.json"

    if not diet_path.exists():
        raise FileNotFoundError(f"Missing diet schema: {diet_path}")
    if not full_path.exists():
        raise FileNotFoundError(f"Missing full OpenAPI spec: {full_path}")

    diet_fns  = json.loads(diet_path.read_text())
    full_spec = json.loads(full_path.read_text())

    # ── Ensure function names ≤ 64 chars (Azure OpenAI restriction) ──────────
    for fn in diet_fns:
        name = fn.get("name", "")
        if len(name) > 64:
            fn["name"] = name[:64]
            print(f"[WARN] Truncated long function name: {name!r} → {fn['name']!r}")

    # ── Pick index name env var according to backend ─────────────────────────
    if BACKEND == "chroma":
        index_name = os.getenv(
            "FASTAPI_CHROMA_COLLECTION_PLATFORM",
            "platform-summaries-index",
        )
    elif BACKEND == "azure":
        index_name = os.getenv(
            "FASTAPI_AZURE_PLATFORM_INDEX",
            "platform-summaries-index",
        )
    elif BACKEND == "elastic":
        index_name = os.getenv(
            "FASTAPI_ELASTIC_PLATFORM_INDEX",
            "platform-summaries-index",
        )

    indexer = Indexer(index_name=index_name, layer_name="FASTAPI")
    indexer.index_functions(platform, diet_fns, full_spec)
    print(f"✓ {platform}: {len(diet_fns)} functions indexed via {BACKEND}")

# ──────────────────────────────────────────────────────────────────────────────
# 3 ▸ CLI wrapper
# ──────────────────────────────────────────────────────────────────────────────
def cli() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--platform", help="meraki, catalyst, …")
    ap.add_argument("--all", action="store_true", help="index every platform found")
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
