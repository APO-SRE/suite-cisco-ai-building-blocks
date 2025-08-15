#!/usr/bin/env python3
"""
================================================================================
 suite-cisco-ai-building-blocks/src/app/user_commands/list_platform_registry.py
 Copyright (c) 2025 Jeff Teeter, Ph.D.
 Cisco Systems, Inc.
 Licensed under the Apache License, Version 2.0 (see LICENSE)
 Distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND.
================================================================================

A **read‑only** CLI tool that prints the contents of `platform_registry.json` in the
same polished Rich UI used by *update_platform_registry.py*.

Usage:
  $ list_platform_registry.py
"""
from __future__ import annotations

import sys
import os
import json
from pathlib import Path
from datetime import datetime

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table
from rich import box
from rich.traceback import install

install()
console = Console()

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
# Current file lives at: suite-cisco-ai-building-blocks/src/app/user_commands/
AGENT_ROOT = Path(__file__).resolve().parents[1]
PROJECT_ROOT = Path(__file__).resolve().parents[3]
REGISTRY_FILE = AGENT_ROOT / "llm" / "platform_registry.json"
SPEC_DIR = PROJECT_ROOT / "src" / "source_open_api"

# ---------------------------------------------------------------------------
# Helpers (borrowed from update_platform_registry.py)
# ---------------------------------------------------------------------------

def clear_screen() -> None:
    if sys.stdout.isatty():
        os.system("cls" if os.name == "nt" else "clear")

def load_registry() -> dict:
    """Load registry or return empty dict when missing/invalid."""
    if not REGISTRY_FILE.exists():
        return {}
    try:
        return json.loads(REGISTRY_FILE.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        console.print(f"[red]Error:[/red] Failed to parse {REGISTRY_FILE}.")
        sys.exit(1)


def display_registry(registry: dict) -> None:
    """Pretty‑print the registry in a table."""
    table = Table(box=box.SIMPLE_HEAVY, show_lines=True)
    table.add_column("#", style="bold cyan", justify="right")
    table.add_column("Short Name", style="bold green")
    table.add_column("OpenAPI Name")
    table.add_column("SDK Module")
    table.add_column("SDK Class")
    table.add_column("Auth Type")
    table.add_column("Created", justify="center")
    table.add_column("Installed", justify="center")
    table.add_column("Route", justify="center")
    for idx, key in enumerate(sorted(registry.keys()), start=1):
        entry = registry[key]
        auth_type = entry.get("auth_config", {}).get("type", "")
        table.add_row(
            str(idx),
            key,
            entry.get("openapi_name", ""),
            entry.get("sdk_module", ""),
            entry.get("sdk_class", ""),
            auth_type,
            "✔" if entry.get("created_by_us", False) else "✖",
            "✔" if entry.get("installed", False) else "✖",
            "✔" if entry.get("route", False) else "✖",
        )
    if registry:
        console.print(Panel(table, title="Platform Registry", border_style="magenta"))
    else:
        console.print(
            Panel(
                "[grey italic]No entries in platform_registry.json[/grey italic]",
                title="Platform Registry",
                border_style="magenta",
            )
        )

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    clear_screen()
    console.print(Panel.fit("📖 List Platform Registry", style="green"))

    # Load & display
    registry = load_registry()
    display_registry(registry)

    # Optionally pause in TTY so the table doesn't disappear when run via double‑click
    if sys.stdout.isatty():
        Prompt.ask("Press [enter] to exit", default="")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[red]Interrupted by user.[/red]")
