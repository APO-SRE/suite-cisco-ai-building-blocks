#!/usr/bin/env python3
###########################################################################################
## suite-cisco-ai-building-blocks/ai-building-blocks-agent/tools/list_chroma_collections.py
## Copyright (c) 2025 Jeff Teeter, Ph.D.
## Cisco Systems, Inc.
## Licensed under the Apache License, Version 2.0 (see LICENSE)
## Distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND.
###########################################################################################
from __future__ import annotations

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
Spot-query the FASTAPI layer’s Chroma DB and dump matching diet-function
records to a JSONL file for manual inspection.

CLI flags
---------
--pattern   prefix (or regex) to match against `metadata["name"]`
--platform  restrict to a single platform (omit for all)
--outfile   where to write the JSONL (default: <pattern>_schemas.jsonl)

Example usage
-------------
# (run these from ai-building-blocks-agent/tools)

# 1. Default: find any function whose name starts with “getOrganization”
python3 list_chroma_collections.py --pattern getOrganization

# 2. Same pattern but restrict to the Meraki platform
python3 list_chroma_collections.py --pattern getOrganization --platform meraki

# 3. Look for functions that start with “client”, show all platforms,
#    and write the results to client_funcs.jsonl
python3 list_chroma_collections.py --pattern client --outfile client_funcs.jsonl

"""


# ── standard libs ─────────────────────────────────────────────────────────
import argparse
import json
import os
import re
import sys
from pathlib import Path

# ── repo-root on sys.path so imports work from any cwd ────────────────────
REPO_ROOT = Path(__file__).resolve().parents[1]          # …/ai-building-blocks-agent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

# ── third-party ───────────────────────────────────────────────────────────
from dotenv import load_dotenv
import chromadb
from chromadb.config import Settings

# ── internal helper to canonicalise paths ────────────────────────────────
from scripts.utils.paths import ensure_abs_env

# ╔══════════════════════════════════════════════════════════════════════╗
# 1.  Parse CLI flags
# ╚══════════════════════════════════════════════════════════════════════╝
ap = argparse.ArgumentParser(description="Dump matching diet-function records "
                                         "from the FASTAPI Chroma DB.")
ap.add_argument("--pattern", default="getOrganization",
                help="prefix (or full regex) to match (default: getOrganization)")
ap.add_argument("--platform", default=None,
                help="platform filter (e.g. meraki); omit for all")
ap.add_argument("--outfile", default=None,
                help="output path; default is <pattern>_schemas.jsonl "
                     "in the same folder as this script")
args = ap.parse_args()

# ╔══════════════════════════════════════════════════════════════════════╗
# 2.  Resolve env-vars + open Chroma collection
# ╚══════════════════════════════════════════════════════════════════════╝
load_dotenv(REPO_ROOT.parent / ".env")

DB_ROOT = ensure_abs_env("FASTAPI_CHROMA_DB_PATH", "chroma_dbs/fastapi")
COL_NAME = os.getenv("FASTAPI_CHROMA_COLLECTION_PLATFORM",
                     "function-definitions-index")
COL_DIR = DB_ROOT / COL_NAME
client = chromadb.PersistentClient(
    path=str(COL_DIR),
    settings=Settings(anonymized_telemetry=False),
)
col = client.get_or_create_collection(COL_NAME)
print(f"Collection '{COL_NAME}' has {col.count()} vectors")

# ╔══════════════════════════════════════════════════════════════════════╗
# 3.  Fetch and filter
# ╚══════════════════════════════════════════════════════════════════════╝
regex = re.compile(rf"{args.pattern}")
hits = []

data = col.get()   # pulls all ids/docs/metas
for _id, meta, doc in zip(data["ids"], data["metadatas"], data["documents"]):
    if args.platform and meta.get("platform") != args.platform:
        continue
    name = meta.get("name", "")
    if regex.match(name):
        hits.append({
            "id": _id,
            "name": name,
            "metadata": meta,
            "schema": json.loads(doc),
        })

print(f"Found {len(hits)} matching schemas "
      f"for pattern '{args.pattern}'"
      f"{' in platform ' + args.platform if args.platform else ''}")

# ╔══════════════════════════════════════════════════════════════════════╗
# 4.  Write JSONL next to this script (or custom path)
# ╚══════════════════════════════════════════════════════════════════════╝
script_dir = Path(__file__).parent.resolve()
outfile = Path(args.outfile) if args.outfile else \
          script_dir / f"{args.pattern}_schemas.jsonl"

with outfile.open("w", encoding="utf-8") as fh:
    for rec in hits:
        fh.write(json.dumps(rec) + "\n")

print(f"Wrote {len(hits)} records → {outfile.resolve()}")
