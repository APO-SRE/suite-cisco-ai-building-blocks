#!/usr/bin/env python3
from __future__ import annotations
################################################################################
## suite-cisco-ai-building-blocks/src/app/user_commands/create_events_index.py
## Copyright (c) 2025 Jeff Teeter, Ph.D.
## Cisco Systems, Inc.
## Licensed under the Apache License, Version 2.0 (see LICENSE)
################################################################################

"""
╔═══════════════════════ Events Indexer Wizard ═══════════════════════════╗
║ A polished CLI to embed & index your events JSON via process_events.    ║
║                                                                         ║
║ FEATURES                                                                ║
║   • Ensures DB & sample directories via .env                            ║
║   • Shows the exact command you’ll run                                  ║
║   • One-click run or exit                                               ║
╚═════════════════════════════════════════════════════════════════════════╝
"""

import os
import sys
import subprocess
from pathlib import Path

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich import box
from rich.table import Table
from rich.traceback import install
from app.utils.paths import ensure_abs_env

install()
console = Console()

def clear_screen() -> None:
    if sys.stdout.isatty():
        os.system("cls" if os.name == "nt" else "clear")

def main() -> None:
    clear_screen()
    console.print(Panel.fit("📅 Events Indexer Wizard", style="green"))

    # ── resolve our scripts root & events folder ──────────────────────────────
    DB_DIR      = ensure_abs_env("DB_SCRIPTS_DIR",       "src/db_scripts")
    EVENTS_DIR  = ensure_abs_env("EVENTS_SAMPLES_DIR",   "src/db_scripts/events")

    if not EVENTS_DIR.exists():
        console.print(f"[red]Events folder not found: {EVENTS_DIR}[/red]")
        sys.exit(1)

    # ── ensure chroma DB path for events ──────────────────────────────────────
    ensure_abs_env("EVENTS_CHROMA_DB_PATH", "chroma_dbs/events")

    # ── build preview command ─────────────────────────────────────────────────
    cmd = [sys.executable, "-m", "db_scripts.process_events"]
    env = os.environ.copy()
    env["EVENTS_SAMPLES_DIR"] = str(EVENTS_DIR)

    preview = (
        f"EVENTS_SAMPLES_DIR={EVENTS_DIR} "
        f"{sys.executable} -m db_scripts.process_events"
    )
    console.print(Panel(preview, title="Command to run", border_style="cyan"))

    # ── confirm & run ─────────────────────────────────────────────────────────
    if not Prompt.ask("Proceed with events indexing? (Y/n)", default="Y").lower().startswith("y"):
        console.print("[yellow]Aborted by user.[/yellow]")
        sys.exit(0)

    console.print(Panel.fit("🚀 Running process_events…", style="cyan"))
    subprocess.run(cmd, check=True, env=env, cwd=str(DB_DIR))
    console.print(Panel.fit(":white_check_mark: Events indexing complete!", style="green"))

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[red]Interrupted by user.[/red]")
        sys.exit(1)
