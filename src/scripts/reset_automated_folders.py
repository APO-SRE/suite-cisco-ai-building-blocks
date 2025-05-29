#!/usr/bin/env python3
from __future__ import annotations
###########################################################################################
## suite-cisco-ai-building-blocks/src/app/tools/reset_automated_folders.py
## Copyright (c) 2025 Jeff Teeter, Ph.D.
## Cisco Systems, Inc.
## Licensed under the Apache License, Version 2.0 (see LICENSE)
## Distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND.
###########################################################################################

"""
DISCLAIMER: USE AT YOUR OWN RISK

This script can either:
1. Wipe and recreate all auto-generated LLM folders (function_definitions, openapi_specs,
   platform_clients, function_dispatcher, unified_service).
2. Remove all artifacts for a single platform across those same folders.

Launch it from anywhere; it always operates on the folders inside the
suite-cisco-ai-building-blocks repo and prints what it deleted / rebuilt.
"""

import sys
import os
import shutil
from pathlib import Path

# ── repo root discovery so script works from any cwd ──────────────────────
REPO_ROOT = Path(__file__).resolve().parents[1]         # …/suite-cisco-ai-building-blocks
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

# ── target folders (absolute paths) ───────────────────────────────────────
FOLDERS_TO_RESET = [
    REPO_ROOT / "app" / "llm" / "function_definitions",
    REPO_ROOT / "app" / "llm" / "openapi_specs",
    REPO_ROOT / "app" / "llm" / "platform_clients",
    REPO_ROOT / "app" / "llm" / "function_dispatcher",
    REPO_ROOT / "app" / "llm" / "unified_service",
]

def reset_folders(paths: list[Path]) -> None:
    """Delete each folder if present, then recreate it empty."""
    for folder in paths:
        if folder.exists():
            print(f"Deleting  → {folder.relative_to(REPO_ROOT)}")
            shutil.rmtree(folder)
        else:
            print(f"Not found  → {folder.relative_to(REPO_ROOT)} (skip delete)")

        folder.mkdir(parents=True, exist_ok=True)
        print(f"Recreated → {folder.relative_to(REPO_ROOT)}\n")


if __name__ == "__main__":
    # Discover available platforms by looking at *_client.py in platform_clients
    clients_dir = REPO_ROOT / "app" / "llm" / "platform_clients"
    platform_files = list(clients_dir.glob("*_client.py"))
    platforms = sorted(
        p.stem[:-len("_client")]
        for p in platform_files
        if p.stem.endswith("_client")
    )

    if not platforms:
        print("No platforms found in platform_clients; resetting all folders.")
        reset_folders(FOLDERS_TO_RESET)
        print("✅ All automated folders have been reset.")
        sys.exit(0)

    # Prompt user for choice
    print("Select platform to reset:")
    for idx, name in enumerate(platforms, start=1):
        print(f"  {idx}. {name}")
    all_option = len(platforms) + 1
    print(f"  {all_option}. All")

    choice = input(f"Select [1-{all_option}]: ").strip()
    try:
        sel = int(choice)
    except ValueError:
        print(f"Invalid selection: {choice}")
        sys.exit(1)

    if sel == all_option:
        # Reset all folders as before
        reset_folders(FOLDERS_TO_RESET)
        print("✅ All automated folders have been reset.")
    elif 1 <= sel <= len(platforms):
        plat = platforms[sel - 1]
        print(f"→ Removing artifacts for platform '{plat}' …\n")
        for folder in FOLDERS_TO_RESET:
            rel = folder.relative_to(REPO_ROOT)
            fn = folder.name
            if fn == "platform_clients":
                target = folder / f"{plat}_client.py"
                if target.exists():
                    print(f"Deleting  → {rel}/{target.name}")
                    target.unlink()
                else:
                    print(f"Not found  → {rel}/{target.name} (skip)")
            elif fn == "function_definitions":
                target = folder / f"{plat}.json"
                if target.exists():
                    print(f"Deleting  → {rel}/{target.name}")
                    target.unlink()
                else:
                    print(f"Not found  → {rel}/{target.name} (skip)")
            elif fn == "openapi_specs":
                for name in (f"{plat}.json", f"full_{plat}.json"):
                    target = folder / name
                    if target.exists():
                        print(f"Deleting  → {rel}/{target.name}")
                        target.unlink()
                    else:
                        print(f"Not found  → {rel}/{target.name} (skip)")
            elif fn == "function_dispatcher":
                target = folder / f"{plat}_dispatcher.py"
                if target.exists():
                    print(f"Deleting  → {rel}/{target.name}")
                    target.unlink()
                else:
                    print(f"Not found  → {rel}/{target.name} (skip)")
            elif fn == "unified_service":
                target = folder / f"{plat}_service.py"
                if target.exists():
                    print(f"Deleting  → {rel}/{target.name}")
                    target.unlink()
                else:
                    print(f"Not found  → {rel}/{target.name} (skip)")
        print(f"\n✅ Platform '{plat}' artifacts have been removed.")
    else:
        print(f"Invalid selection: {choice}")
        sys.exit(1)
