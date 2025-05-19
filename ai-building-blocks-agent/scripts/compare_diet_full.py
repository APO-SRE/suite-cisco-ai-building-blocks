#!/usr/bin/env python3
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
