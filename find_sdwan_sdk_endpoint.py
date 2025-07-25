#!/usr/bin/env python3
"""
Fill every "!!!_NEEDS_MANUAL_FIX_!!!" with the best matching Catalyst WAN
SDK endpoint.

Compatible registry layouts
  • list  : ["deviceGet", "siteUpdate", …]
  • map   : {"deviceGet": "!!!…!!!", …}
  • object: {"operations": [ {...}, {...} ]}

If the catalystwan package is unavailable, the script scans *.py files in
./sdk_sources (config_device_inventory_api.py, dashboard_api.py, …) that
ship with your repo.

Outputs
  • src/app/llm/sdwan_operation_registry_UPDATED.json
  • registry_autofill_report.tsv   – audit trail
"""

from __future__ import annotations
import importlib
import inspect
import json
import os
import pkgutil
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Dict, List

# ---------------------------------------------------------------------------
#  Configuration
# ---------------------------------------------------------------------------

PLACEHOLDER = "!!!_NEEDS_MANUAL_FIX_!!!"
REG_PATH = Path("src/app/llm/sdwan_operation_registry_CORRECTED.json")
OUT_PATH = Path("src/app/llm/sdwan_operation_registry_UPDATED.json")
REPORT_PATH = Path("registry_autofill_report.tsv")

# ---------------------------------------------------------------------------
#  Helpers: name conversions
# ---------------------------------------------------------------------------

_camel_pat = re.compile(r"([a-z0-9])([A-Z])")


def camel_to_snake(name: str) -> str:
    return _camel_pat.sub(r"\1_\2", name).lower()


def snake_to_camel(name: str) -> str:
    parts = name.split("_")
    return parts[0] + "".join(p.title() for p in parts[1:])


# ---------------------------------------------------------------------------
#  1. Collect SDK endpoints
# ---------------------------------------------------------------------------

def endpoints_from_catalystwan() -> List[str]:
    """Try to import catalystwan and enumerate public callables."""
    try:
        import catalystwan.endpoints  # noqa: F401
    except Exception as exc:  # ImportError or AttributeError
        sys.stderr.write(f"[warn] catalystwan not importable: {exc}\n")
        return []

    prefix = "catalystwan.endpoints."
    callables: List[str] = []

    for mod in pkgutil.walk_packages(
            catalystwan.endpoints.__path__, prefix=prefix):
        if mod.ispkg:
            continue
        module = importlib.import_module(mod.name)
        pkg_suffix = mod.name[len(prefix):]  # e.g. "configuration.device"

        # top‑level functions
        for fn_name, fn in inspect.getmembers(module, inspect.isfunction):
            if fn.__module__ == mod.name and not fn_name.startswith("_"):
                callables.append(f"session.api.{pkg_suffix}.{fn_name}")

        # methods on classes (e.g. class DeviceApi → def get…)
        for _, cls in inspect.getmembers(module, inspect.isclass):
            if cls.__module__ != mod.name or cls.__name__.startswith("_"):
                continue
            for meth_name, meth in inspect.getmembers(cls, inspect.isfunction):
                if meth.__module__ == mod.name and not meth_name.startswith("_"):
                    callables.append(f"session.api.{pkg_suffix}.{meth_name}")

    return callables


def endpoints_from_repo() -> List[str]:
    """
    Fallback: walk *.py files shipped with the repo (those *_api.py files)
    and harvest `def <name>(self, …)` lines.
    """
    src_dir = Path(__file__).resolve().parent
    pattern = re.compile(r"^\s*def\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*\(")
    callables: List[str] = []

    for py_file in src_dir.rglob("*_api.py"):
        pkg_suffix = py_file.stem  # "device_action_api"
        with py_file.open(encoding="utf-8") as fh:
            for line in fh:
                m = pattern.match(line)
                if m:
                    fn = m.group(1)
                    callables.append(f"session.api.{pkg_suffix}.{fn}")

    if not callables:
        sys.stderr.write("[warn] repo‑scan found no *_api.py symbols\n")
    return callables


def collect_endpoints() -> List[str]:
    eps = endpoints_from_catalystwan()
    if eps:
        return eps
    sys.stderr.write("[info] falling back to local source enumeration\n")
    return endpoints_from_repo()


# ---------------------------------------------------------------------------
#  2. Index endpoints by a set of name variants
# ---------------------------------------------------------------------------

def build_index(endpoints: List[str]) -> Dict[str, List[str]]:
    index: Dict[str, List[str]] = defaultdict(list)
    for ep in endpoints:
        short = ep.rsplit(".", 1)[-1]          # e.g. "get_device"
        variants = {
            short,
            short.lower(),
            camel_to_snake(short),
            snake_to_camel(short),
        }
        for v in variants:
            index[v].append(ep)
    return index


# ---------------------------------------------------------------------------
#  3. Load & normalise the registry into a list[dict]
# ---------------------------------------------------------------------------

def load_registry(path: Path) -> List[dict]:
    with path.open(encoding="utf-8") as fh:
        data = json.load(fh)

    # ---- shape detection ---------------------------------------------------
    if isinstance(data, list):  # simple array
        ops = []
        for item in data:
            if isinstance(item, str):
                ops.append({"operationId": item, "sdk_endpoint": PLACEHOLDER})
            elif isinstance(item, dict):
                # guarantee key names
                ops.append({
                    "operationId": item.get("operationId") or item.get("name"),
                    "sdk_endpoint": item.get("sdk_endpoint", PLACEHOLDER),
                    **item
                })
            else:
                raise TypeError(f"Unsupported entry type {type(item)} in list")
        return ops

    if isinstance(data, dict) and "operations" in data:  # object layout
        return data["operations"]

    if isinstance(data, dict):  # map layout
        return [
            {"operationId": k, "sdk_endpoint": v}
            for k, v in data.items()
        ]

    raise ValueError("Unsupported registry format")


# ---------------------------------------------------------------------------
#  4. Auto‑fill placeholders
# ---------------------------------------------------------------------------

def pick_best(op_id: str, candidates: List[str]) -> (str | None, str):
    """Return (choice, reason)."""
    if not candidates:
        return None, "no‑match"
    if len(candidates) == 1:
        return candidates[0], "single"
    # tie‑break: choose shortest FQN – empirically correct most often
    return min(candidates, key=len), "shortest"


def autofill(ops: List[dict], index: Dict[str, List[str]]) -> int:
    updated = 0
    report_rows = []

    for op in ops:
        if op.get("sdk_endpoint") != PLACEHOLDER:
            continue
        op_id = op.get("operationId") or op.get("name")
        if not op_id:
            continue
        cands = (
            index.get(op_id) or
            index.get(camel_to_snake(op_id)) or
            index.get(op_id.lower()) or
            []
        )
        choice, reason = pick_best(op_id, cands)
        report_rows.append((op_id, len(cands), reason, choice or ""))
        if choice:
            op["sdk_endpoint"] = choice
            updated += 1

    # write audit
    with REPORT_PATH.open("w", encoding="utf-8") as rep:
        rep.write("operationId\tcandidates\treason\tchoice\n")
        for r in report_rows:
            rep.write("\t".join(map(str, r)) + "\n")

    return updated


# ---------------------------------------------------------------------------
#  5. Write updated registry in same structure as input
# ---------------------------------------------------------------------------

def write_registry(orig_path: Path, ops: List[dict]) -> None:
    with orig_path.open(encoding="utf-8") as fh:
        data = json.load(fh)

    if isinstance(data, list):
        # preserve simplest format (strings) when no extra metadata
        new_list = [
            op["sdk_endpoint"] if isinstance(item, str)
            else op                   # item was dict; keep dict
            for item, op in zip(data, ops)
        ]
        json_data = new_list
    elif isinstance(data, dict) and "operations" in data:
        data["operations"] = ops
        json_data = data
    else:  # map
        json_data = {op["operationId"]: op["sdk_endpoint"] for op in ops}

    with OUT_PATH.open("w", encoding="utf-8") as out:
        json.dump(json_data, out, indent=2)


# ---------------------------------------------------------------------------
#  Main entry
# ---------------------------------------------------------------------------

def main() -> None:
    if not REG_PATH.exists():
        sys.exit(f"Registry file {REG_PATH} not found")

    print("🔍  enumerating SDK …")
    endpoints = collect_endpoints()
    print(f"   found {len(endpoints):,} callable functions")

    index = build_index(endpoints)
    ops = load_registry(REG_PATH)

    filled = autofill(ops, index)
    print(f"✅  auto‑filled {filled:,} placeholder(s)")
    print(f"📄  audit   → {REPORT_PATH}")
    write_registry(REG_PATH, ops)
    print(f"💾  updated → {OUT_PATH}")


if __name__ == "__main__":
    main()
