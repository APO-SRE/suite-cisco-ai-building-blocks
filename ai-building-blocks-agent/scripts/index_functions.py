#!/usr/bin/env python3
from __future__ import annotations
################################################################################
# ai-building-blocks-agent/scripts/index_functions.py
################################################################################
"""
Index every *diet* schema (or a single platform) into the vector-store selected
for the FASTAPI layer.  Works with Chroma, Azure AI Search, or Elasticsearch.

Examples
--------
# one platform
python -m scripts.index_functions --platform meraki

# everything under app/llm/function_definitions
python -m scripts.index_functions --all
"""
import argparse
import importlib
import json
import os
from pathlib import Path

from dotenv import load_dotenv

# ════════════════════════════════════════════════════════════════════════
# 0  Environment & basic paths
# ════════════════════════════════════════════════════════════════════════
load_dotenv()

ROOT        = Path(__file__).resolve().parents[1]                # repo root (agent)
LLM_DIR     = ROOT / "app" / "llm"
DIET_DIR    = LLM_DIR / "function_definitions"
FULL_DIR    = LLM_DIR / "openapi_specs"

BACKEND     = os.getenv("FASTAPI_VECTOR_BACKEND", "chroma").lower()

# ════════════════════════════════════════════════════════════════════════
# 1  Pick the proper indexer implementation
# ════════════════════════════════════════════════════════════════════════
INDEXER_MODULES: dict[str, str] = {
    "chroma":  "db_scripts.indexers.chroma_indexer",
    "azure":   "db_scripts.indexers.azure_indexer",
    "elastic": "db_scripts.indexers.elastic_indexer",
}

try:
    mod_name = INDEXER_MODULES[BACKEND]
except KeyError as exc:
    raise RuntimeError(
        f"Unsupported backend '{BACKEND}'. "
        f"Choose from: {', '.join(INDEXER_MODULES)}."
    ) from exc

Indexer = getattr(importlib.import_module(mod_name), "PlatformFunctionIndexer")

# ════════════════════════════════════════════════════════════════════════
# 2  Index a single platform
# ════════════════════════════════════════════════════════════════════════
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

    # collection / index name selected from the env for the chosen backend
    if BACKEND == "chroma":
        index_name = os.getenv("FASTAPI_CHROMA_COLLECTION_PLATFORM",
                               "platform-summaries-index")
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

# ════════════════════════════════════════════════════════════════════════
# 3  CLI entry-point
# ════════════════════════════════════════════════════════════════════════
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
