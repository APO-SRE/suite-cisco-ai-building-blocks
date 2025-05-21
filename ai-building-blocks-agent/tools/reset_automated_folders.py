#!/usr/bin/env python3
###########################################################################################
## suite-cisco-ai-building-blocks/ai-building-blocks-agent/tools/reset_automated_folders.py
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
Utility to wipe and recreate all auto-generated LLM folders
(app/llm/function_definitions, openapi_specs, …).

Launch it from anywhere; it always operates on the folders inside the
ai-building-blocks-agent repo and prints what it deleted / rebuilt.
"""
from __future__ import annotations

from pathlib import Path
import shutil
import sys
import os

# ── repo root discovery so script works from any cwd ──────────────────────
REPO_ROOT = Path(__file__).resolve().parents[1]         # …/ai-building-blocks-agent
if str(REPO_ROOT) not in sys.path:                      # (not strictly needed here,
    sys.path.insert(0, str(REPO_ROOT))                  #  but matches the pattern)

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
    reset_folders(FOLDERS_TO_RESET)
    print("✅ All automated folders have been reset.")
