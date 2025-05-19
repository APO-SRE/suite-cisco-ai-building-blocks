#!/usr/bin/env python3
import os
import json
from pathlib import Path

import chromadb
from chromadb.config import Settings
from dotenv import load_dotenv

# ── Load environment variables from top-level .env ──
ROOT_DIR = Path(__file__).resolve().parents[2]
load_dotenv(ROOT_DIR / ".env")

# ── Clearly define database paths ──
DB_ROOT = Path(
    os.getenv(
        "FASTAPI_CHROMA_DB_PATH",
        ROOT_DIR / "ai-building-blocks-agent" / "chroma_dbs" / "fastapi"
    )
).expanduser().resolve()

COL_NAME = os.getenv(
    "FASTAPI_CHROMA_COLLECTION_PLATFORM",
    "function-definitions-index"
)
COL_DIR = DB_ROOT / COL_NAME

if not COL_DIR.exists():
    raise FileNotFoundError(f"Collection folder not found: {COL_DIR}")

# ── Initialize Chroma DB ──
client = chromadb.PersistentClient(
    path=str(COL_DIR),
    settings=Settings(anonymized_telemetry=False),
)
col = client.get_or_create_collection(COL_NAME)

print(f"Collection '{COL_NAME}' has {col.count()} vectors")

# ── Retrieve all documents and metadata ──
data = col.get()
ids, docs, metas = data["ids"], data["documents"], data["metadatas"]

# ── Broader Filter (from second script) ──
hits = [
    {
        "id": _id,
        "name": meta.get("name", ""),
        "metadata": meta,
        "schema": json.loads(doc)
    }
    for _id, meta, doc in zip(ids, metas, docs)
    if meta.get("name", "").startswith(("getOrganization", "getOrganizations"))
]

print(f"Found {len(hits)} getOrganization* schemas")

# ── Write clearly to JSONL file ──
outfile = ROOT_DIR / "getOrganization_schemas.jsonl"
with open(outfile, "w", encoding="utf-8") as f:
    for rec in hits:
        f.write(json.dumps(rec) + "\n")

print(f"Wrote {len(hits)} records → {outfile}")
