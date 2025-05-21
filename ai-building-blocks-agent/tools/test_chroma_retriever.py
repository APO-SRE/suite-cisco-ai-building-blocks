#!/usr/bin/env python3
# ai-building-blocks-agent/scripts/test_chroma_retriever.py


import os
import sys

# ── Ensure project root is on PYTHONPATH so `import retrievers` works ────────────
sys.path.insert(0, os.getcwd())

from retrievers.chroma_retriever import FunctionRetriever

def print_results(results):
    for i, r in enumerate(results, 1):
        name = r.get("name")
        platform = r.get("platform")
        distance = r.get("distance")
        print(f"  {i}. name={name}  platform={platform}  distance={distance:.4f}")

def main():
    collection = "function-definitions-index"
    print(f"Initializing FunctionRetriever against '{collection}'…")
    fr = FunctionRetriever(collection_name=collection)

    # 1) Generic query (no filter)
    print("\n1) Top 5 schemas for query 'organization':")
    results = fr.query("organization", k=5)
    print_results(results)
    print(f"  → Retrieved {len(results)} entries\n")

    # 2) Meraki-only filter
    print("2) Top 5 schemas for 'organization' with meraki filter:")
    results = fr.query(
        "organization",
        k=5,
        filter={"platform": {"$in": ["meraki"]}}
    )
    print_results(results)
    print(f"  → Retrieved {len(results)} entries\n")

if __name__ == "__main__":
    main()