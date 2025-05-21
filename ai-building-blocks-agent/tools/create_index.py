#!/usr/bin/env python3
from __future__ import annotations
################################################################################
## suite-cisco-ai-building-blocks/ai-building-blocks-agent/tools/create_index.py
## Copyright (c) 2025 Jeff Teeter
## Cisco Systems, Inc.
## Licensed under the Apache License, Version 2.0 (see LICENSE)
## Distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND.
################################################################################

"""
╭────────────────────── Platform Indexer (wizard) ───────────────────────╮
│ Helps you run `scripts/index_functions.py` without remembering flags.  │
│                                                                       │
│  • Pick ONE platform               ── or ──   Index **ALL** platforms │
│  • Handles PYTHONPATH for you so it works from any directory           │
│  • Shows the exact command before running (⇧-C to copy if you like)    │
╰────────────────────────────────────────────────────────────────────────╯
"""

# ── stdlib ────────────────────────────────────────────────────────────────
import argparse
import os
import shlex
import subprocess
import sys
from pathlib import Path
from typing import List, Tuple
# ── colour (optional) ─────────────────────────────────────────────────────
try:
    from colorama import Fore, Style, init as _cinit

    _cinit()
    BOLD = Style.BRIGHT
    CYAN = Fore.CYAN + Style.BRIGHT
    GREEN = Fore.GREEN + Style.BRIGHT
    YELLOW = Fore.YELLOW
    RED = Fore.RED + Style.BRIGHT
    RESET = Style.RESET_ALL
except ImportError:
    BOLD = CYAN = GREEN = YELLOW = RED = RESET = ""


# ───────────────────────────── repo paths ─────────────────────────────────
AGENT_ROOT = Path(__file__).resolve().parents[1]          # …/ai-building-blocks-agent
LLM_DEF_DIR = AGENT_ROOT / "app" / "llm" / "function_definitions"
INDEXER_SCRIPT = AGENT_ROOT / "scripts" / "index_functions.py"

if str(AGENT_ROOT) not in sys.path:                       # for internal imports
    sys.path.insert(0, str(AGENT_ROOT))


# ───────────────────────────── helpers ────────────────────────────────────
def _clear() -> None:
    if sys.stdout.isatty():
        os.system("cls" if os.name == "nt" else "clear")


def _ask(prompt: str, default: str | None = None) -> str:
    suffix = f" {YELLOW}[{default}]{RESET}" if default else ""
    while True:
        val = input(f"{BOLD}?{RESET} {prompt}{suffix}: ").strip()
        if val:
            return val
        if default is not None:
            return default
        print(f"{RED}Please enter a value.{RESET}")


def _list_platforms() -> List[Tuple[int, str]]:
    plats = sorted(p.stem for p in LLM_DEF_DIR.glob("*.json"))
    if not plats:
        return []
    print(f"\n{CYAN}Available platforms (diet JSONs found):{RESET}")
    for idx, name in enumerate(plats, 1):
        print(f"  {idx:>2}. {name}")
    print("  0. All platforms\n")
    return list(enumerate(plats, 1))


def _build_cmd(platform: str | None) -> List[str]:
    if platform:
        return [sys.executable, str(INDEXER_SCRIPT), "--platform", platform]
    return [sys.executable, str(INDEXER_SCRIPT), "--all"]


# ───────────────────────────── wizard ─────────────────────────────────────
def main() -> None:
    _clear()
    print(f"{GREEN}🛠  Platform Indexer (wizard){RESET}\n")

    # --- list *.json files -------------------------------------------------
    listing = _list_platforms()
    if not listing:
        print(f"{RED}No diet JSON files found in {LLM_DEF_DIR}{RESET}")
        sys.exit(1)

    choice = _ask("Choose by number, or 0 for ALL", "0")
    platform = None
    if choice != "0":
        try:
            idx = int(choice)
            platform = next(name for n, name in listing if n == idx)
        except (ValueError, StopIteration):
            print(f"{RED}Invalid selection.{RESET}")
            sys.exit(1)

    # --- build command -----------------------------------------------------
    cmd_parts = _build_cmd(platform)
    cmd_str = " ".join(shlex.quote(p) for p in cmd_parts)

    print(f"\n{CYAN}Command to run{RESET}\n  {cmd_str}\n")
    if _ask("Proceed? (Y/n)", "Y").lower().startswith("n"):
        print("Aborted.")
        return

    # --- ensure repo on PYTHONPATH for child process -----------------------
    env = os.environ.copy()
    env["PYTHONPATH"] = f"{AGENT_ROOT}:{env.get('PYTHONPATH', '')}"

    subprocess.run(cmd_parts, check=True, env=env)
    print(f"\n{GREEN}✅  Indexing complete.{RESET}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{RED}Aborted by user.{RESET}")
