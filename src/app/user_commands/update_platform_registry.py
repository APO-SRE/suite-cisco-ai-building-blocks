#!/usr/bin/env python3
"""
================================================================================
 suite-cisco-ai-building-blocks/src/app/user_commands/update_platform_registry.py
 Copyright (c) 2025 Jeff Teeter, Ph.D.
 Cisco Systems, Inc.
 Licensed under the Apache License, Version 2.0 (see LICENSE)
 Distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND.
================================================================================

A CLI tool to view, add, edit, or delete entries in platform_registry.json.
Each entry has:
  • short name (key)
  • openapi_name (must be one of the specs already in src/source_open_api)
  • sdk_module
  • created_by_us (boolean, managed only by create_sdk.py)
  • installed (boolean, auto-detected based on generated artifacts)

Usage:
  $ update_platform_registry.py
"""
from __future__ import annotations
import sys
import os
import json
import importlib.util
import re
from pathlib import Path
from datetime import datetime

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt
from rich import box
from rich.traceback import install

install()
console = Console()

# -------------------------------------------------------------------------------
# Paths
# -------------------------------------------------------------------------------
# This script lives at: suite-cisco-ai-building-blocks/src/app/user_commands/update_platform_registry.py
# AGENT_ROOT points to suite-cisco-ai-building-blocks/src/app
AGENT_ROOT = Path(__file__).resolve().parents[1]
# PROJECT_ROOT points to suite-cisco-ai-building-blocks/
PROJECT_ROOT = Path(__file__).resolve().parents[3]
REGISTRY_FILE = AGENT_ROOT / "llm" / "platform_registry.json"
SPEC_DIR = PROJECT_ROOT / "src" / "source_open_api"
ROUTERS_DIR = PROJECT_ROOT / "src" / "app" / "routers"

# Directories to check for generated scaffolding
SCAFFOLD_DIRS = {
    "platform_clients": AGENT_ROOT / "llm" / "platform_clients",
    "function_definitions": AGENT_ROOT / "llm" / "function_definitions",
    "function_dispatcher": AGENT_ROOT / "llm" / "function_dispatcher",
    "unified_service": AGENT_ROOT / "llm" / "unified_service",
}

# Validation for short-name (same as create_platform)
VALID_PLATFORM_RX = re.compile(r"^[a-z][a-z0-9_]*$")


# -------------------------------------------------------------------------------
# Helpers
# -------------------------------------------------------------------------------
def clear_screen() -> None:
    if sys.stdout.isatty():
        os.system("cls" if os.name == "nt" else "clear")


def check_route_exists(short_name: str) -> bool:
    return (ROUTERS_DIR / f"{short_name}_routes.py").exists()

def load_registry() -> dict:
    """Load the registry JSON or return empty dict if file missing or invalid."""
    if not REGISTRY_FILE.exists():
        return {}
    try:
        return json.loads(REGISTRY_FILE.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        console.print(f"[red]Error:[/red] Failed to parse {REGISTRY_FILE}.")
        sys.exit(1)


def save_registry(registry: dict) -> None:
    """Write the registry back to disk (creating parent dirs if needed)."""
    REGISTRY_FILE.parent.mkdir(parents=True, exist_ok=True)
    REGISTRY_FILE.write_text(json.dumps(registry, indent=2), encoding="utf-8")


def is_installed(pkg_name: str) -> bool:
    """
    Return True if pkg_name (or its top-level segment) can be imported in this env.
    (Still used if you want to verify SDK availability, but not for 'installed' flag here.)
    """
    if importlib.util.find_spec(pkg_name) is not None:
        return True
    root = pkg_name.split(".", 1)[0]
    return importlib.util.find_spec(root) is not None


def check_scaffold_exists(short_name: str) -> bool:
    """
    Determine 'installed' status by checking for generated scaffolding files:
      - platform_clients/<short_name>_client.py
      - function_definitions/<short_name>.json
      - function_dispatcher/<short_name>_dispatcher.py
      - unified_service/<short_name>_service.py
    If any of these exist, return True.
    """
    client_py = SCAFFOLD_DIRS["platform_clients"] / f"{short_name}_client.py"
    func_def = SCAFFOLD_DIRS["function_definitions"] / f"{short_name}.json"
    dispatcher_py = SCAFFOLD_DIRS["function_dispatcher"] / f"{short_name}_dispatcher.py"
    service_py = SCAFFOLD_DIRS["unified_service"] / f"{short_name}_service.py"
    return any(path.exists() for path in (client_py, func_def, dispatcher_py, service_py))

def display_registry(registry: dict) -> None:
    """
    Render platform_registry.json in a Rich table with a Route column.
    """
    table = Table(box=box.SIMPLE_HEAVY, show_lines=True)
    table.add_column("#",             style="bold cyan", justify="right")
    table.add_column("Short Name",    style="bold green")
    table.add_column("OpenAPI Name")
    table.add_column("SDK Module")
    table.add_column("Created By Us", justify="center")
    table.add_column("Installed",     justify="center")
    table.add_column("Route",         justify="center")   # ← NEW

    for idx, key in enumerate(sorted(registry.keys()), start=1):
        entry = registry[key]
        table.add_row(
            str(idx),
            key,
            entry.get("openapi_name", ""),
            entry.get("sdk_module",   ""),
            "✔" if entry.get("created_by_us", False) else "✖",
            "✔" if entry.get("installed",     False) else "✖",
            "✔" if entry.get("route",         False) else "✖",   # ← NEW
        )

    console.print(
        Panel(
            table if registry else "[grey italic]No entries yet.[/grey italic]",
            title="Current Platform Registry",
            border_style="magenta",
        )
    )
 

def select_entry(registry: dict, action: str) -> str | None:
    """
    Let user select an existing short name from the registry for editing or deletion.
    Returns the chosen key, or None if user aborts.
    """
    if not registry:
        console.print("[yellow]No entries available.[/yellow]")
        return None

    keys = sorted(registry.keys())
    table = Table(box=box.SIMPLE)
    table.add_column("#", style="bold cyan", justify="right")
    table.add_column("Short Name", style="bold green")
    for i, key in enumerate(keys, start=1):
        table.add_row(str(i), key)
    exit_idx = len(keys) + 1
    table.add_row(str(exit_idx), "Cancel")
    console.print(Panel(table, title=f"Select entry to {action}", border_style="cyan"))

    while True:
        choice = Prompt.ask(f"[cyan]?[/cyan] Select number [1-{exit_idx}]", default=str(exit_idx))
        if not choice.isdigit():
            console.print("[red]→ Invalid selection. Enter a number.[/red]")
            continue
        idx = int(choice)
        if idx == exit_idx:
            return None
        if 1 <= idx <= len(keys):
            return keys[idx - 1]
        console.print(f"[red]→ Choose a number between 1 and {exit_idx}.[/red]")


def list_specs() -> list[Path]:
    """
    Return a sorted list of all OpenAPI spec files under src/source_open_api/.
    """
    specs = sorted(
        list(SPEC_DIR.glob("*.json")) + list(SPEC_DIR.glob("*.yaml")) + list(SPEC_DIR.glob("*.yml"))
    )
    return specs


def pick_spec() -> str:
    """
    Present a table of available OpenAPI spec filenames and let user pick one.
    Returns the spec file's stem (i.e., filename without extension). Returns "" if canceled.
    """
    specs = list_specs()
    if not specs:
        console.print(f"[red]No OpenAPI specs found in {SPEC_DIR}.[/red]")
        sys.exit(1)

    table = Table(box=box.SIMPLE_HEAVY)
    table.add_column("#", style="bold cyan", justify="right")
    table.add_column("Filename", style="bold")
    table.add_column("Size (KB)", justify="right")
    table.add_column("Last Modified", justify="center")

    for i, fp in enumerate(specs, start=1):
        table.add_row(
            str(i),
            fp.name,
            str(fp.stat().st_size // 1024),
            datetime.fromtimestamp(fp.stat().st_mtime).strftime("%Y-%m-%d"),
        )
    exit_idx = len(specs) + 1
    table.add_row(str(exit_idx), "Cancel", "", "")
    console.print(Panel(table, title="Available OpenAPI Specs", border_style="cyan"))

    while True:
        choice = Prompt.ask(f"[cyan]?[/cyan] Select spec number [1-{exit_idx}]", default=str(exit_idx))
        if not choice.isdigit():
            console.print("[red]→ Invalid selection. Enter a number.[/red]")
            continue
        idx = int(choice)
        if idx == exit_idx:
            return ""  # signal “cancelled”
        if 1 <= idx <= len(specs):
            return specs[idx - 1].stem
        console.print(f"[red]→ Choose a number between 1 and {exit_idx}.[/red]")


# -------------------------------------------------------------------------------
# Main interactive flow
# -------------------------------------------------------------------------------
def main() -> None:
    clear_screen()
    console.print(Panel.fit("🔧 Update Platform Registry Wizard", style="green"))

    registry = load_registry()

    while True:
        # Display current entries
        display_registry(registry)

        # Show main menu
        console.print(
            Panel.fit(
                "[bold]Actions:[/bold]\n"
                "  1. Add new entry\n"
                "  2. Edit existing entry\n"
                "  3. Delete entry\n"
                "  4. Exit",
                border_style="cyan",
            )
        )
        choice = Prompt.ask("[cyan]?[/cyan] Choose action [1-4]", default="4")
        if not choice.isdigit() or not (1 <= (c := int(choice)) <= 4):
            console.print("[red]→ Invalid selection. Enter 1, 2, 3, or 4.[/red]")
            continue

        # === Add new entry ===
        if c == 1:
            console.print(Panel.fit("➕ Add New Entry", style="cyan"))

            # Prompt for short_name
            while True:
                short_name = Prompt.ask("[cyan]?[/cyan] [bold]Short name (nickname)[/bold]")
                short_name = short_name.strip()
                if not short_name:
                    console.print("[red]→ Short name cannot be empty.[/red]")
                    continue
                if not VALID_PLATFORM_RX.match(short_name):
                    console.print(
                        "[red]→ Invalid short name. Use lowercase letters, digits, underscores; must start with a letter.[/red]"
                    )
                    continue
                if short_name in registry:
                    console.print(f"[red]→ '{short_name}' already exists.[/red]")
                    continue
                break

            # Prompt user to pick an existing spec from src/source_open_api
            openapi_stem = pick_spec()
            if not openapi_stem:
                console.print("[yellow]Add cancelled; returning to main menu.[/yellow]")
                continue

            # Prompt for sdk_module (optional; allow "update later")
            sdk_module = Prompt.ask(
                "[cyan]?[/cyan] [bold]Associated SDK module[/bold] "
                "(e.g. dnacentersdk or type 'update later')",
                default="update later",
            ).strip()
            if sdk_module.lower() in {"update later", "later", "skip", "none"}:
                sdk_module = ""          # empty means "set it later"

            # Prompt for sdk_pattern
            sdk_pattern = Prompt.ask(
                "[cyan]?[/cyan] [bold]SDK pattern[/bold] (e.g. catalyst)",
                default=short_name,
            ).strip()

            # Prompt for sdk_class
            sdk_class = Prompt.ask(
                "[cyan]?[/cyan] [bold]SDK class name[/bold] (e.g. DNACenterAPI)",
                default="Client",
            ).strip()

            # Prompt for auth type
            console.print("\n[bold]Authentication types:[/bold]")
            console.print("  1. api_key")
            console.print("  2. api_key_secret")
            console.print("  3. basic_auth")
            console.print("  4. bearer_token")
            console.print("  5. session_based")
            console.print("  6. duo_auth")
            console.print("  7. oauth2")
            console.print("  8. none")
            auth_choice = Prompt.ask("[cyan]?[/cyan] Select auth type [1-8]", default="1")
            auth_types = {
                "1": "api_key",
                "2": "api_key_secret",
                "3": "basic_auth",
                "4": "bearer_token",
                "5": "session_based",
                "6": "duo_auth",
                "7": "oauth2",
                "8": "none"
            }
            auth_type = auth_types.get(auth_choice, "api_key")

            # Ask about sub_clients
            has_sub_clients = Prompt.ask(
                "[cyan]?[/cyan] [bold]Does this SDK have sub-clients?[/bold] [y/N]",
                default="N"
            ).strip().lower() in ("y", "yes")

            # For new entries, leave 'created_by_us' as False (updated later by create_sdk.py)
            created_by_us = False

            # Determine 'installed' by checking for generated scaffolding
            installed = check_scaffold_exists(short_name)

            # Check if route exists
            route = check_route_exists(short_name)

            # Build entry and save
            registry[short_name] = {
                "openapi_name": openapi_stem,
                "sdk_module": sdk_module,
                "sdk_pattern": sdk_pattern,
                "sdk_class": sdk_class,
                "created_by_us": created_by_us,
                "installed": installed,
                "route": route,
                "auth_config": {
                    "type": auth_type,
                    "env_vars": {},
                    "init_params": {
                        "required": [],
                        "optional": []
                    }
                },
                "sub_clients": has_sub_clients,
                "example_init": ""
            }
            save_registry(registry)
            console.print(f"[green]Added '{short_name}' → spec '{openapi_stem}'.[/green]")

        # === Edit existing entry ===
        elif c == 2:
            short_name = select_entry(registry, "edit")
            if short_name is None:
                continue  # back to main menu

            entry = registry[short_name]
            console.print(Panel.fit(f"✏️ Editing '{short_name}'", style="cyan"))

            # Let user pick a new OpenAPI spec (or keep current)
            console.print(f"Current OpenAPI spec: [bold]{entry.get('openapi_name')}[/bold]")
            if Prompt.ask(
                "[cyan]?[/cyan] [bold]Change OpenAPI spec?[/bold] [y/N]", default="N"
            ).strip().lower() in ("y", "yes"):
                new_openapi = pick_spec()
                if not new_openapi:
                    new_openapi = entry.get("openapi_name", "")
                console.print(f":white_check_mark: OpenAPI spec set to [bold]{new_openapi}[/bold]\n")
            else:
                new_openapi = entry.get("openapi_name", "")

            # Prompt new SDK module (type 'update later' to clear it)
            new_sdk = Prompt.ask(
                "[cyan]?[/cyan] [bold]SDK module[/bold]",
                default=entry.get("sdk_module", ""),
            ).strip()
            if new_sdk.lower() in {"update later", "later", "skip", "none"}:
                new_sdk = ""              # clears the field

            # Update SDK pattern
            new_pattern = Prompt.ask(
                "[cyan]?[/cyan] [bold]SDK pattern[/bold]",
                default=entry.get("sdk_pattern", short_name),
            ).strip()

            # Update SDK class
            new_class = Prompt.ask(
                "[cyan]?[/cyan] [bold]SDK class[/bold]",
                default=entry.get("sdk_class", "Client"),
            ).strip()

            # Keep existing auth_config but allow updating auth type
            current_auth = entry.get("auth_config", {}).get("type", "api_key")
            console.print(f"Current auth type: [bold]{current_auth}[/bold]")
            if Prompt.ask(
                "[cyan]?[/cyan] [bold]Change auth type?[/bold] [y/N]", default="N"
            ).strip().lower() in ("y", "yes"):
                console.print("\n[bold]Authentication types:[/bold]")
                console.print("  1. api_key")
                console.print("  2. api_key_secret")
                console.print("  3. basic_auth")
                console.print("  4. bearer_token")
                console.print("  5. session_based")
                console.print("  6. duo_auth")
                console.print("  7. oauth2")
                console.print("  8. none")
                auth_choice = Prompt.ask("[cyan]?[/cyan] Select auth type [1-8]", default="1")
                auth_types = {
                    "1": "api_key",
                    "2": "api_key_secret",
                    "3": "basic_auth",
                    "4": "bearer_token",
                    "5": "session_based",
                    "6": "duo_auth",
                    "7": "oauth2",
                    "8": "none"
                }
                new_auth_type = auth_types.get(auth_choice, current_auth)
            else:
                new_auth_type = current_auth

            # Update sub_clients
            new_sub_clients = Prompt.ask(
                "[cyan]?[/cyan] [bold]Has sub-clients?[/bold] [y/N]",
                default="Y" if entry.get("sub_clients", False) else "N"
            ).strip().lower() in ("y", "yes")

            # Keep 'created_by_us' unchanged
            new_created = entry.get("created_by_us", False)

            # Recompute 'installed' by checking generated scaffolding again
            new_installed = check_scaffold_exists(short_name)

            # Check if route exists
            new_route = check_route_exists(short_name)

            # Update and save, preserving other fields
            updated_entry = entry.copy()
            updated_entry.update({
                "openapi_name": new_openapi,
                "sdk_module": new_sdk,
                "sdk_pattern": new_pattern,
                "sdk_class": new_class,
                "created_by_us": new_created,
                "installed": new_installed,
                "route": new_route,
                "sub_clients": new_sub_clients,
            })
            
            # Update auth type if changed
            if "auth_config" not in updated_entry:
                updated_entry["auth_config"] = {"type": new_auth_type, "env_vars": {}, "init_params": {"required": [], "optional": []}}
            else:
                updated_entry["auth_config"]["type"] = new_auth_type
            
            registry[short_name] = updated_entry
            save_registry(registry)
            console.print(f"[green]Updated '{short_name}'.[/green]")

        # === Delete entry ===
        elif c == 3:
            short_name = select_entry(registry, "delete")
            if short_name is None:
                continue  # back to main menu

            confirm = Prompt.ask(
                f"[cyan]?[/cyan] [bold]Are you sure you want to delete '{short_name}'?[/bold] [y/N]",
                default="N",
            ).strip().lower() in ("y", "yes")
            if confirm:
                registry.pop(short_name, None)
                save_registry(registry)
                console.print(f"[green]Deleted '{short_name}' from registry.[/green]")
            else:
                console.print("[yellow]Deletion cancelled.[/yellow]")

        # === Exit ===
        else:
            console.print("[yellow]Exiting...[/yellow]")
            sys.exit(0)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[red]Interrupted by user.[/red]")
