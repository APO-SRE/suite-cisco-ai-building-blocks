#!/usr/bin/env python3
from __future__ import annotations
##########################################################################################
## suite-cisco-ai-building-blocks/ai-building-blocks-agent/user_commands/reset_platform.py
## Copyright (c) 2025 Jeff Teeter, Ph.D.
## Cisco Systems, Inc.
## Licensed under the Apache License, Version 2.0 (see LICENSE)
## Distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND.
##########################################################################################

"""
╔════════════════════════ Unified Platform Reset Wizard ═════════════════════════╗
║ A step-by-step CLI to wipe or remove specific platform artifacts in the AI     ║
║ agent's auto-generated LLM folders.                                            ║
║                                                                                ║
║ OPTIONS                                                                        ║
║   • All   → delete all platform artifacts.                                     ║
║   • One   → remove a single platform's artifacts.                              ║
║   • Exit  → quit without making changes.                                       ║
╚═══════════════════════════════════════════════════════════════════════════════╝
"""

import argparse
import sys
import os
from pathlib import Path
import shutil

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt
from rich import box
from rich.traceback import install

# enable rich tracebacks
install()
console = Console()

# clear screen helper
def clear_screen() -> None:
    if sys.stdout.isatty():
        os.system("cls" if os.name == 'nt' else "clear")

# Discover repository root & import reset logic
AGENT_ROOT = Path(__file__).resolve().parents[1]
if str(AGENT_ROOT) not in sys.path:
    sys.path.insert(0, str(AGENT_ROOT))

from scripts.reset_automated_folders import FOLDERS_TO_RESET, reset_folders


def get_platforms() -> list[str]:
    """Scan platform_clients folder for available platforms."""
    clients_dir = AGENT_ROOT / "app" / "llm" / "platform_clients"
    return sorted(
        fp.stem[:-len("_client")]
        for fp in clients_dir.glob("*_client.py")
        if fp.stem.endswith("_client")
    )


def display_platforms(platforms: list[str]) -> None:
    """Show numbered list of platforms plus All and Exit options."""
    table = Table(box=box.SIMPLE)
    table.add_column("#", style="bold cyan", no_wrap=True)
    table.add_column("Platform")
    for idx, name in enumerate(platforms, start=1):
        table.add_row(str(idx), name)
    table.add_row(str(len(platforms) + 1), "All")
    table.add_row(str(len(platforms) + 2), "Exit")
    console.print(Panel(table, title="Select Platform to Reset", border_style="green"))


def main() -> None:
    clear_screen()

    parser = argparse.ArgumentParser(description="Reset AI agent LLM folders for all or one platform.")
    parser.add_argument("--dry-run", dest="dry_run", action="store_true",
                        help="Show what would be done without making changes.")
    args = parser.parse_args()

    platforms = get_platforms()
    if not platforms:
        console.print("[yellow]No platforms found. Resetting all folders.[/yellow]")
        if not args.dry_run:
            reset_folders(FOLDERS_TO_RESET)
        return

    display_platforms(platforms)
    choice = Prompt.ask(f"Enter choice [1-{len(platforms)+2}]")
    try:
        sel = int(choice)
    except ValueError:
        console.print(f"[red]Invalid selection: {choice}[/red]")
        sys.exit(1)

    # Exit option
    if sel == len(platforms) + 2:
        console.print("[cyan]Exiting without changes.[/cyan]")
        sys.exit(0)

    # Option: All platforms
    if sel == len(platforms) + 1:
        console.print(Panel.fit("You chose: [bold]All[/bold] → resetting all folders.", style="cyan"))
        if not args.dry_run:
            reset_folders(FOLDERS_TO_RESET)
        else:
            console.print("[yellow]Dry run: no changes applied.[/yellow]")
        return

    # Option: Single platform
    if 1 <= sel <= len(platforms):
        plat = platforms[sel - 1]
        console.print(Panel.fit(f"You chose: [bold]{plat}[/bold] → removing its artifacts.", style="cyan"))
        if args.dry_run:
            console.print("[yellow]Dry run: no changes applied.[/yellow]")
            return

        for folder in FOLDERS_TO_RESET:
            rel = folder.relative_to(AGENT_ROOT)
            name = folder.name
            if name == "platform_clients":
                target = folder / f"{plat}_client.py"
            elif name == "function_definitions":
                target = folder / f"{plat}.json"
            elif name == "openapi_specs":
                # two files: <plat>.json and full_<plat>.json
                for fn in (f"{plat}.json", f"full_{plat}.json"):
                    target = folder / fn
                    desc = f"{rel}/{fn}"
                    if target.exists():
                        console.print(f"Deleting → {desc}")
                        target.unlink()
                    else:
                        console.print(f"Not found → {desc}")
                continue
            elif name == "function_dispatcher":
                target = folder / f"{plat}_dispatcher.py"
            elif name == "unified_service":
                target = folder / f"{plat}_service.py"
            else:
                continue

            desc = f"{rel}/{target.name}"
            if target.exists():
                console.print(f"Deleting → {desc}")
                target.unlink()
            else:
                console.print(f"Not found → {desc}")

        console.print(f"[green]✓ Platform '{plat}' artifacts removed.[/green]")
        return

    console.print(f"[red]Selection out of range: {sel}[/red]")
    sys.exit(1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[red]Interrupted by user.[/red]")
