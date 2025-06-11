#!/usr/bin/env python3
"""
Synchronise platform_registry.json with scaffolded artefacts.

 • Updates the “installed” flag for every existing registry entry.
 • Updates the “route” flag (✔ if src/app/routers/<short>_routes.py exists).
 • Clears “created_by_us” if the SDK folder has been removed from output_sdk.
 • Adds a stub entry for any scaffolded platform not yet in the registry.
 • Does *not* delete anything else.

Run:
  $ sync_registry_with_scaffold.py        # live update
  $ sync_registry_with_scaffold.py --dry  # preview only
"""
from __future__ import annotations
import argparse
import os
import sys
from pathlib import Path
from typing import Dict, List, Tuple

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import box
from rich.traceback import install

from app.user_commands.update_platform_registry import (
    load_registry, save_registry, check_scaffold_exists,
    SCAFFOLD_DIRS, REGISTRY_FILE,
)

install()
console = Console()

# ───────────────────────── paths ──────────────────────────
PROJECT_ROOT      = Path(__file__).resolve().parents[3]
ROUTERS_DIR       = PROJECT_ROOT / "src" / "app" / "routers"
SDK_OUTPUT_DIR    = PROJECT_ROOT / "src" / "db_scripts" / "output_sdk"


# ───────────────────────── helpers ──────────────────────────

def clear_screen() -> None:
    if sys.stdout.isatty():
        os.system("cls" if os.name == "nt" else "clear")


def check_route_exists(short_name: str) -> bool:
    """Return True if src/app/routers/<short_name>_routes.py exists."""
    return (ROUTERS_DIR / f"{short_name}_routes.py").exists()


def find_scaffolded_platforms() -> set[str]:
    """Return all short names for which a function_definitions/*.json exists."""
    defs_dir = SCAFFOLD_DIRS["function_definitions"]
    return {p.stem for p in defs_dir.glob("*.json")}


def render_registry(reg: Dict[str, Dict]) -> Panel:
    tbl = Table(box=box.SIMPLE_HEAVY, show_lines=True)
    tbl.add_column("#",             style="cyan", justify="right")
    tbl.add_column("Short Name",    style="bold")
    tbl.add_column("OpenAPI Name")
    tbl.add_column("SDK Module")
    tbl.add_column("Installed",     justify="center")
    tbl.add_column("Created By Us", justify="center")
    tbl.add_column("Route",         justify="center")

    for i, key in enumerate(sorted(reg), 1):
        e = reg[key]
        tbl.add_row(
            str(i),
            key,
            e.get("openapi_name", ""),
            e.get("sdk_module", ""),
            "✔" if e.get("installed")      else "✖",
            "✔" if e.get("created_by_us") else "✖",
            "✔" if e.get("route")          else "✖",
        )
    return Panel(tbl, title="Current Platform Registry", border_style="magenta")


def show_changes(changes: List[Tuple[str, str]]) -> None:
    if not changes:
        console.print("[green]✓ Registry already matches disk – nothing to do.[/green]")
        return
    tbl = Table(box=box.SIMPLE_HEAVY)
    tbl.add_column("#", justify="right", style="cyan")
    tbl.add_column("Platform")
    tbl.add_column("Action / Result")
    for i, (plat, msg) in enumerate(changes, 1):
        tbl.add_row(str(i), plat, msg)
    console.print(Panel(tbl, title="Synchronisation Summary", border_style="blue"))


# ───────────────────────── main ──────────────────────────

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry", action="store_true", help="Preview changes only")
    args = ap.parse_args()

    clear_screen()

    registry: Dict[str, Dict] = load_registry()
    console.print(render_registry(registry))

    scaffolded = find_scaffolded_platforms()
    changes: List[Tuple[str, str]] = []

    # 1) Update ‘installed’ and ‘route’ flags -----------------------------------
    for short, entry in registry.items():
        installed_now = check_scaffold_exists(short)
        if installed_now != entry.get("installed", False):
            entry["installed"] = installed_now
            changes.append((short, f"installed → {'✔' if installed_now else '✖'}"))

        route_now = check_route_exists(short)
        if route_now != entry.get("route", False):
            entry["route"] = route_now
            changes.append((short, f"route     → {'✔' if route_now else '✖'}"))

    # 2) Clear 'created_by_us' if SDK folder has been removed -------------------
    for short, entry in registry.items():
        sdk_pkg = entry.get("sdk_module", "")
        if sdk_pkg:
            sdk_folder = SDK_OUTPUT_DIR / sdk_pkg
            if not sdk_folder.exists() and entry.get("created_by_us", False):
                entry["created_by_us"] = False
                changes.append((short, "created_by_us → ✖ (SDK missing)"))

    # 3) Stub missing registry entries for newly scaffolded platforms -----------
    for short in sorted(scaffolded - registry.keys()):
        registry[short] = {
            "openapi_name":  "",
            "sdk_module":   "",
            "created_by_us": False,
            "installed":     True,
            "route":         check_route_exists(short),
        }
        changes.append((short, "added stub entry (installed ✔)"))

    console.print()  # blank line before summary
    show_changes(changes)

    if changes and not args.dry:
        save_registry(registry)
        console.print(f"[green]✓ {Path(REGISTRY_FILE).relative_to(Path.cwd())} updated.[/green]")
    elif changes:
        console.print("[yellow]--dry supplied – no file written.[/yellow]")

    # ── Always re-print the (possibly updated) registry ----------------------
    console.print()  # visual spacer
    console.print(render_registry(registry))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[red]Interrupted by user.[/red]")
