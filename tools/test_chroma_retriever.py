#!/usr/bin/env python3
###########################################################################################
## suite-cisco-ai-building-blocks/tools/test_chroma_retriever.py
## Copyright (c) 2025 Jeff Teeter, Ph.D.
## Cisco Systems, Inc.
## Licensed under the Apache License, Version 2.0 (see LICENSE)
## Distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND.
###########################################################################################
from __future__ import annotations

"""
Smoke-test the Chroma **FunctionRetriever**.

It works from any directory: the script locates the repo root, fixes
`FASTAPI_CHROMA_DB_PATH` (turning a relative value into an absolute path),
then runs one or two demo searches and prints the distance-sorted results.

CLI flags
---------
--term        search term for the vector query        (default: "organization")
--platform    restrict results to a single platform   (omit for no filter)
--top-k       how many hits to show                   (default: 5)

Example usage
-------------
# ── launch from the tools/ folder ──────────────────────────────────────
python3 test_chroma_retriever.py                       # default: term="organization"
python3 test_chroma_retriever.py --term client --top-k 10
python3 test_chroma_retriever.py --term site --platform meraki

# ── launch from the repo root (or anywhere) using -m ───────────────────
python -m ai_building_blocks_agent.tools.test_chroma_retriever \
       --term site --platform meraki
"""

import argparse
import os
import sys
from pathlib import Path

# ── ensure repo root is importable ─────────────────────────────────────────
REPO_ROOT = Path(__file__).resolve().parents[1]          # …/ai-building-blocks-agent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

# ── canonicalise Chroma DB path (relative → absolute) ─────────────────────
from scripts.utils.paths import ensure_abs_env
ensure_abs_env("FASTAPI_CHROMA_DB_PATH", "chroma_dbs/fastapi")

from app.retrievers.chroma_retriever import FunctionRetriever


def print_results(results: list[dict]) -> None:
    for i, r in enumerate(results, 1):
        print(f"  {i:>2}. "
              f"name={r.get('name'):<60} "
              f"platform={r.get('platform'):<10} "
              f"distance={r.get('distance'):.4f}")


def main() -> None:
    # ── CLI flags ─────────────────────────────────────────────────────────
    ap = argparse.ArgumentParser(description="Quick query against Chroma.")
    ap.add_argument("--term",      default="organization",
                    help="vector query term (default: 'organization')")
    ap.add_argument("--platform",  default=None,
                    help="platform filter, e.g. meraki (omit for no filter)")
    ap.add_argument("--top-k",     type=int, default=5,
                    help="how many top hits to display (default: 5)")
    args = ap.parse_args()

    collection = os.getenv("FASTAPI_CHROMA_COLLECTION_PLATFORM",
                           "function-definitions-index")
    print(f"\nInitializing FunctionRetriever against collection "
          f"'{collection}' …\n")
    retriever = FunctionRetriever(collection_name=collection)

    # ── query without platform filter ─────────────────────────────────────
    print(f"1) Top-{args.top_k} schemas for query '{args.term}':")
    hits = retriever.query(args.term, k=args.top_k)
    print_results(hits)
    print(f"  → Retrieved {len(hits)} entries\n")

    # ── optional platform-specific query ──────────────────────────────────
    if args.platform:
        print(f"2) Top-{args.top_k} schemas for '{args.term}' "
              f"on platform '{args.platform}':")
        hits = retriever.query(
            args.term,
            k=args.top_k,
            filter={"platform": {"$in": [args.platform]}}
        )
        print_results(hits)
        print(f"  → Retrieved {len(hits)} entries\n")


if __name__ == "__main__":
    main()
