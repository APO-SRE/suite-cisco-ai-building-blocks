#!/usr/bin/env python3
from __future__ import annotations
################################################################################
## suite-cisco-ai-building-blocks/src/app/user_commands/delete_platform_route.py
## Copyright (c) 2025 Your Name
## Cisco Systems, Inc.
## Licensed under the Apache License, Version 2.0 (see LICENSE)
################################################################################

import os
import sys
from pathlib import Path

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt
from rich import box

console = Console()

# locate the app root (src/app) and the routers dir
APP_DIR     = Path(__file__).resolve().parents[1]
ROUTERS_DIR = APP_DIR / "routers"
INIT_FILE   = ROUTERS_DIR / "__init__.py"

def list_route_files() -> list[Path]:
    return sorted(
        p for p in ROUTERS_DIR.iterdir()
        if p.is_file() and p.suffix == ".py" and p.name != "__init__.py"
    )

def remove_import_from_init(module_name: str) -> None:
    if not INIT_FILE.exists():
        return
    lines = INIT_FILE.read_text(encoding="utf-8").splitlines()
    filtered = []
    for l in lines:
        # drop any line that mentions this module
        if module_name in l:
            continue
        filtered.append(l)
    INIT_FILE.write_text("\n".join(filtered) + "\n", encoding="utf-8")

def main() -> None:
    console.print(Panel.fit("🗑️  Delete a FastAPI Route", style="red"))

    routes = list_route_files()
    if not routes:
        console.print("[yellow]No route files found in src/app/routers.[/yellow]")
        sys.exit(0)

    # build selection table
    table = Table(box=box.SIMPLE)
    table.add_column("#", style="bold cyan", no_wrap=True)
    table.add_column("Route file")
    for i, f in enumerate(routes, 1):
        table.add_row(str(i), f.name)
    exit_idx = len(routes) + 1
    table.add_row(str(exit_idx), "Exit without deleting")
    console.print(Panel(table, title="Select a route to delete", border_style="red"))

    choice = Prompt.ask(f"Enter 1–{exit_idx}", default=str(exit_idx)).strip()
    if not choice.isdigit() or int(choice) == exit_idx:
        console.print("[green]Nothing deleted. Exiting.[/green]")
        sys.exit(0)

    idx = int(choice)
    if not (1 <= idx <= len(routes)):
        console.print("[red]Invalid selection. Exiting.[/red]")
        sys.exit(1)

    target = routes[idx - 1]
    confirm = Prompt.ask(f"Delete route [bold]{target.name}[/bold]? (y/N)", choices=["y","n"], default="n")
    if confirm != "y":
        console.print("[green]Aborted. No changes made.[/green]")
        sys.exit(0)

    # delete the file
    try:
        target.unlink()
        # scrub import from __init__.py
        module = target.stem
        remove_import_from_init(module)
    except Exception as e:
        console.print(f"[red]Error deleting {target.name}: {e}[/red]")
        sys.exit(1)

    console.print(f"[green]Deleted {target.name} and cleaned up imports.[/green]")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[red]Interrupted by user.[/red]")
        sys.exit(1)
