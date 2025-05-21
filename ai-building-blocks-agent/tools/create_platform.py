#!/usr/bin/env python3
################################################################################
## AI-Building-Blocks-Agent/tools/create_platform.py
## Copyright (c) 2025 Jeff Teeter
## Cisco Systems, Inc.
## Licensed under the Apache License, Version 2.0 (see LICENSE)
## Distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND.
################################################################################
"""
╭────────────────────────── Unified Platform Scaffolder (wizard) ──────────────────────────╮
│ Interactively builds and executes the long scaffolder command.                           │
│                                                                                         │
│ OUTPUT (auto-generated)                                                                  │
│   app/llm/function_definitions/<platform>.json                                           │
│   app/llm/openapi_specs/full_<platform>.json                                             │
│   app/llm/platform_clients/<platform>_client.py                                          │
│   app/llm/function_dispatcher/<platform>_dispatcher.py                                   │
│   app/llm/unified_service/<platform>_service.py                                          │
│                                                                                         │
│ PREREQUISITES                                                                            │
│   • SDK import path you supply must be importable (pip-installed or on PYTHONPATH).      │
│   • OpenAPI spec must be valid JSON.                                                     │
│                                                                                         │
│ EXAMPLE (run from anywhere)                                                              │
│   create-platform                                                                        │
│     ↳ choose platform “meraki”                                                           │
│     ↳ pick /ai-building-blocks-database/source_open_api_json/meraki.json                │
│     ↳ select verbs GET,POST                                                              │
│     ↳ optional regex client$                                                             │
│     ↳ confirms and runs the real scaffolder module                                       │
│                                                                                         │
│ TROUBLESHOOTING                                                                          │
│   • “ModuleNotFoundError” → install the SDK you named (pip install …).                   │
│   • Invalid JSON path   → ensure correct file path; supports absolute & relative.        │
╰───────────────────────────────────────────────────────────────────────────────────────────╯
"""
from __future__ import annotations

import argparse
import importlib
import json
import shlex
import subprocess
import sys
import re
import os
from datetime import datetime
from pathlib import Path
from typing import List, Optional, Tuple
from itertools import chain

# ───────────────────────────── colour support ──────────────────────────────
try:
    from colorama import Fore, Style, init as _color_init

    _color_init()
    BOLD = Style.BRIGHT
    CYAN = Fore.CYAN + Style.BRIGHT
    GREEN = Fore.GREEN + Style.BRIGHT
    YELLOW = Fore.YELLOW
    RED = Fore.RED + Style.BRIGHT
    RESET = Style.RESET_ALL
except ImportError:  # colour optional
    BOLD = CYAN = GREEN = YELLOW = RED = RESET = ""

 
VALID_PLATFORM_RX = re.compile(r"^[a-z][a-z0-9_]*$")
VALID_SDK_RX      = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*(\.[A-Za-z_][A-Za-z0-9_]*)*$")
VALID_VERBS       = {"GET", "POST", "PUT", "PATCH", "DELETE", "HEAD", "OPTIONS"}

# ───────────────────────────── repo paths ──────────────────────────────────
AGENT_ROOT = Path(__file__).resolve().parents[1]
TOP_ROOT = AGENT_ROOT.parent
SPEC_DIR = TOP_ROOT / "ai-building-blocks-database" / "source_open_api"

# Make internal packages importable no matter where we’re launched from
if str(AGENT_ROOT) not in sys.path:
    sys.path.insert(0, str(AGENT_ROOT))


# ───────────────────────────── helpers ─────────────────────────────────────
def _clear_screen() -> None:
    """Clear the terminal if stdout is a TTY (Linux/macOS: ANSI; Windows: cls)."""
    if sys.stdout.isatty():
        os.system("cls" if os.name == "nt" else "clear")

def ask(prompt: str, default: Optional[str] = None) -> str:
    suffix = f" {YELLOW}[{default}]{RESET}" if default else ""
    while True:
        ans = input(f"{BOLD}?{RESET} {prompt}{suffix}: ").strip()
        if ans:
            return ans
        if default is not None:
            return default
        print(f"{RED}Please enter a value.{RESET}")

def list_specs() -> list[tuple[int, Path]]:
    """Return a numbered list of *.json / *.yml / *.yaml files in SPEC_DIR."""
    specs = sorted(
        chain(
            SPEC_DIR.glob("*.json"),
            SPEC_DIR.glob("*.yml"),
            SPEC_DIR.glob("*.yaml"),
        )
    )
    if not specs:
        return []

    print(f"\n{CYAN}Available OpenAPI specs in {SPEC_DIR}:{RESET}")
    for idx, fp in enumerate(specs, 1):
        size_kb = fp.stat().st_size // 1024
        mtime   = datetime.fromtimestamp(fp.stat().st_mtime).strftime("%Y-%m-%d")
        print(f"  {idx:>2}. {fp.name:<35} {size_kb:>6} KB  {mtime}")
    return list(enumerate(specs, 1))

 


def pick_spec_json() -> str:
    listing = list_specs()
    if not listing:
        return ask("Enter full path to your OpenAPI JSON")

    print("  0. Enter a custom path\n")
    while True:
        choice = ask("Choose a file by number", "1")
        if choice == "0":
            return ask("Enter full path to your OpenAPI JSON")
        if choice.isdigit():
            idx = int(choice)
            for n, fp in listing:
                if n == idx:
                    return str(fp)
        print(f"{RED}Invalid selection.{RESET}")


def preview_table(rows: List[Tuple[str, str]]) -> None:
    width = max(len(k) for k, _ in rows) + 2
    for k, v in rows:
        print(f"{BOLD}{k:<{width}}{RESET}{v}")

def build_cmd(
        platform: str,
        sdk: str,
        spec: str,
        verbs: Optional[str],
        regex: Optional[str],
) -> List[str]:
    """Return argv list to invoke platform_scaffolder.py directly."""
    scaffolder_path = AGENT_ROOT / "scripts" / "platform_scaffolder.py"
    cmd = [
        sys.executable,
        str(scaffolder_path),          # ← absolute path instead of -m package
        "--platform", platform,
        "--sdk-module", sdk,
        "--openapi-spec", spec,
    ]
    if verbs:
        cmd += ["--include-http-methods", verbs.upper().replace(" ", "")]
    if regex:
        cmd += ["--name-pattern", regex]
    return cmd



def ask_valid(prompt: str,
              pattern: re.Pattern[str],
              error_msg: str,
              default: Optional[str] = None) -> str:
    while True:
        val = ask(prompt, default)
        if pattern.match(val):
            return val
        print(f"{RED}{error_msg}{RESET}")


# ───────────────────────────── main flow ──────────────────────────────────
def main() -> None:
    _clear_screen()  

    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--dry-run", action="store_true",
                        help="Show command but do not execute")
    args, _ = parser.parse_known_args()

    print(f"\n{GREEN}🛠  Unified Platform Scaffolder (wizard){RESET}\n")

    # 1) Platform identifier (strict validation)
    platform = ask_valid(
        "Platform identifier (lowercase letters, digits, underscore; must start with a letter)",
        VALID_PLATFORM_RX,
        "Invalid platform identifier. Use lowercase letters, digits and '_' only, starting with a letter.",
    )

    # 2) SDK import path (valid dotted-name)
    sdk_mod = ask_valid(
        "Python SDK import path "
        "(fully-qualified module — e.g. 'meraki' or 'catalystwan.session' "
        "if ManagerSession lives in that sub-module)",
        VALID_SDK_RX,
        "Invalid dotted import path. Use valid Python identifiers separated by '.'.",
        platform,              # default = same as platform name
    )

    # 3) Choose / pick spec file ------------------------------------------------
    print(f"\n{CYAN}─ OpenAPI spec ─{RESET}")
    default_spec = SPEC_DIR / f"{platform}.json"
    if default_spec.exists():
        use_default = ask(f"Use {default_spec.name} found in spec folder? (y/N)", "N")
        spec_file = str(default_spec) if use_default.lower().startswith("y") else pick_spec_json()
    else:
        spec_file = pick_spec_json()

    # 4) HTTP verb list (with validation) ---------------------------------------
    while True:
        verbs_raw = ask(
            "\nHTTP verbs to scaffold "
            "(comma-separated — GET, POST, PUT, PATCH, DELETE; leave blank for ALL)\n"
            "Tip: start with GET only if you just need read-only access while prototyping"
        )
        if not verbs_raw:       # blank → ALL (accepted)
            break
        verbs = {v.strip().upper() for v in verbs_raw.split(",")}
        bad   = verbs - VALID_VERBS
        if not bad:
            break
        print(f"{RED}Unrecognised verb(s): {', '.join(sorted(bad))}{RESET}")

    # 5) Optional regex for operationIds
    print ()
    name_re = ask(
    "Regex filter for operationIds (leave blank to include every endpoint).\n"
    "  • Each endpoint in an OpenAPI spec has a unique “operationId” such as\n"
    "    getDeviceHealth, createSite, deleteSiteById, etc.\n"
    "  • Provide a regular-expression to keep only the IDs you care about.\n"
    "    –  Example 1:  ^get                → keep every read-only endpoint\n"
    "    –  Example 2:  (Client|Device)$    → keep IDs ending in Client or Device\n"
    "    –  Example 3:  health|metrics      → any ID containing those words\n"
    "Press <Enter> for no filter → scaffold ALL operationIds.",
    ""
)
   
    print(f"\n{CYAN}…processing your selections, please wait ⏳{RESET}", flush=True)
    # ── sanity checks on spec & SDK ────────────────────────────────────────────
    spec_path = Path(spec_file)
    if not spec_path.is_file():
        print(f"{RED}❌  Spec file not found: {spec_path}{RESET}")
        sys.exit(1)

    from scripts.utils.openapi_loader import load_spec
    try:
        load_spec(spec_path)        # parses JSON or YAML; raises on error
    except Exception as exc:
        print(f"{RED}❌  Spec file is not valid JSON/YAML: {exc}{RESET}")
        sys.exit(1)

    try:
        importlib.import_module(sdk_mod)
    except ModuleNotFoundError:
        print(f"{YELLOW}⚠  SDK module '{sdk_mod}' cannot be imported – "
              f"ensure it’s installed in the venv{RESET}")

    # ── preview table ─────────────────────────────────────────────────────────
    print(f"\n{CYAN}Configuration summary{RESET}")
    preview_table([
        ("Platform",      platform),
        ("SDK module",    sdk_mod),
        ("OpenAPI file",  spec_file),
        ("HTTP verbs",    verbs_raw or "ALL"),
        ("Name regex",    name_re or "–"),
    ])

    # ── build + show command ───────────────────────────────────────────────────
    cmd_parts = build_cmd(
        platform, sdk_mod, spec_file,
        verbs_raw if verbs_raw else None,
        name_re   if name_re   else None,
    )
    cmd_str = " ".join(shlex.quote(p) for p in cmd_parts)
    print(f"\n{CYAN}Command to run{RESET}\n  {cmd_str}\n")

    if args.dry_run:
        print(f"{GREEN}Dry-run mode: command not executed.{RESET}")
        return

    if ask("Proceed? (Y/n)", "Y").lower().startswith("n"):
        print("Aborted.")
        return

    # --- run scaffolder with PYTHONPATH pointing at repo -----------------
    env = os.environ.copy()
    env["PYTHONPATH"] = f"{AGENT_ROOT}:{env.get('PYTHONPATH', '')}"
    subprocess.run(cmd_parts, check=True, env=env)

    print(f"\n{GREEN}✅  Scaffolding complete.{RESET}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{RED}Aborted by user.{RESET}")


