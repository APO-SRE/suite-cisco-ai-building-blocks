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
import json
from pathlib import Path

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt
from rich import box
from rich.traceback import install

install()
console = Console()

# ──────────────────────────────────────────────────────────────────────
# locate the app root (src/app) and the routers dir
# ──────────────────────────────────────────────────────────────────────
# delete_platform_route.py lives at: repo/src/app/user_commands/delete_platform_route.py
# Therefore, APP_DIR = repo/src/app, and the registry is at repo/src/app/llm/platform_registry.json
APP_DIR     = Path(__file__).resolve().parents[1]
ROUTERS_DIR = APP_DIR / "routers"
INIT_FILE   = ROUTER_DIR = ROUTERS_DIR / "__init__.py"

# Correct registry path (inside src/app/llm)
REGISTRY_PATH = APP_DIR / "llm" / "platform_registry.json"

def list_route_files() -> list[Path]:
    """
    Return a sorted list of all *_routes.py files under src/app/routers.
    """
    return sorted(
        p for p in ROUTERS_DIR.iterdir()
        if p.is_file() and p.name.endswith("_routes.py")
    )

def remove_import_from_init(module_name: str) -> None:
    """
    Remove any import lines in __init__.py that refer to the given module_name.
    e.g., if module_name="catalyst_routes", drop lines importing catalyst_routes.
    """
    if not INIT_FILE.exists():
        return

    lines = INIT_FILE.read_text(encoding="utf-8").splitlines()
    filtered = []
    for l in lines:
        # Drop any line that mentions this module
        if module_name in l:
            continue
        filtered.append(l)
    INIT_FILE.write_text("\n".join(filtered) + "\n", encoding="utf-8")

def clear_route_flag(short_name: str) -> None:
    """
    Load platform_registry.json, set "route": false for this entry, then write back,
    preserving all other keys.
    """
    if not REGISTRY_PATH.exists():
        console.print(f"[yellow]Warning: Registry file not found at {REGISTRY_PATH}. Nothing to update.[/yellow]")
        return

    try:
        registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        console.print(f"[red]Error:[/red] Failed to parse {REGISTRY_PATH}. Aborting registry update.")
        return

    if short_name not in registry:
        console.print(f"[yellow]Warning: '{short_name}' not found in registry. No 'route' flag to clear.[/yellow]")
    else:
        registry[short_name]["route"] = False
        # Write back with indentation
        REGISTRY_PATH.write_text(json.dumps(registry, indent=2), encoding="utf-8")
        console.print(f"[grey]→ Cleared 'route' flag for '{short_name}' in {REGISTRY_PATH}[/grey]")

def main() -> None:
    console.print(Panel.fit("🗑️  Delete a FastAPI Route", style="red"))

    routes = list_route_files()
    if not routes:
        console.print("[yellow]No route files found in src/app/routers.[/yellow]")
        sys.exit(0)

    # Build selection table
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
    confirm = Prompt.ask(
        f"Delete route [bold]{target.name}[/bold]? (y/N)",
        choices=["y", "n"],
        default="n"
    )
    if confirm != "y":
        console.print("[green]Aborted. No changes made.[/green]")
        sys.exit(0)

    # 1) Delete the file itself and remove its import from __init__.py
    try:
        target.unlink()
        module = target.stem  # e.g. "catalyst_routes"
        remove_import_from_init(module)
    except Exception as e:
        console.print(f"[red]Error deleting {target.name}: {e}[/red]")
        sys.exit(1)

    # 2) Update platform_registry.json → clear the "route" flag
    short_name = target.stem.replace("_routes", "")  # e.g. "catalyst"
    clear_route_flag(short_name)

    console.print(f"[green]Deleted {target.name} and cleared route flag for '{short_name}'.[/green]")

if __name__ == "__main__":
    
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[red]Interrupted by user.[/red]")
        sys.exit(1)
