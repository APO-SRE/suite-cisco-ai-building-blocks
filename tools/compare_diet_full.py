#!/usr/bin/env python3
###########################################################################################
## suite-cisco-ai-building-blocks/tools/compare_diet_full.py
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
Quick utility for **spot-querying the FASTAPI layer’s Chroma DB**.

Run it when you want to inspect which diet-function records are stored for a
particular pattern (e.g. any function whose name starts with “getOrganization”).
It connects to the collection defined by FASTAPI_CHROMA_DB_PATH /
FASTAPI_CHROMA_COLLECTION_PLATFORM, filters the documents, and dumps the hits
as JSONL right next to this script in suite-cisco-ai-building-blocks/tools/.
"""
import os
import json
from pathlib import Path

# ── 1. Locate your diet file and full spec ───────────────────────────────
ROOT       = Path(__file__).resolve().parents[1]
DIET_PATH  = ROOT / "app" / "llm" / "function_definitions" / "meraki.json"
FULL_PATH  = ROOT / "app" / "llm" / "openapi_specs" / "full_meraki.json"

# ── 2. Load them ─────────────────────────────────────────────────────────
diet      = json.loads(DIET_PATH.read_text(encoding="utf-8"))
full_spec = json.loads(FULL_PATH.read_text(encoding="utf-8"))

# ── 3. Extract operationIds ──────────────────────────────────────────────
diet_ids = {fn["name"] for fn in diet}

full_ids = {
    op["operationId"]
    for path_item in full_spec.get("paths", {}).values()
    for op in path_item.values()
    if "operationId" in op
}

# ── 4. Compute differences ────────────────────────────────────────────────
missing_in_diet = sorted(full_ids - diet_ids)
extra_in_diet   = sorted(diet_ids - full_ids)

report = {
    "missing_in_diet": missing_in_diet,
    "extra_in_diet":   extra_in_diet,
}

# ── 5. Write report to disk ──────────────────────────────────────────────
OUTFILE = "diet_vs_full_report.json"
Path(OUTFILE).write_text(json.dumps(report, indent=2), encoding="utf-8")

print(f"✅ Report written to {OUTFILE}")
print(f" • missing_in_diet: {len(missing_in_diet)} items")
print(f" • extra_in_diet:   {len(extra_in_diet)} items")
