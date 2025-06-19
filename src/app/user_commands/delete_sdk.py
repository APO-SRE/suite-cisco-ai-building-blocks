#!/usr/bin/env python3
from __future__ import annotations
#######################################################################################
## suite-cisco-ai-building-blocks/src/app/user_commands/delete_sdk.py
## Copyright (c) 2025 Jeff Teeter, Ph.D.
## Cisco Systems, Inc.
## Licensed under the Apache License, Version 2.0 (see LICENSE)
## Distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND.
#######################################################################################

"""
╔═══════════════════ OpenAPI SDK Deletion Wizard ══════════════════════════════╗
║ A polished CLI to remove generated SDKs from output_sdk.                     ║
║                                                                              ║
║ FEATURES                                                                     ║
║   • List existing SDKs                                                       ║
║   • Select one to delete                                                     ║
║   • Also remove any matching 'sdk_module' entry from platform_registry.json  ║
║   • Exit option                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

import os
import sys
import json
import shutil
from pathlib import Path
from typing import List
import tomllib

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table
from rich.markdown import Markdown
from rich import box
from rich.traceback import install

install()
console = Console()

# ────────────────────────────────────────────────────────────────────────────────
# Paths
# ────────────────────────────────────────────────────────────────────────────────
PROJECT_ROOT        = Path(__file__).resolve().parents[3]
SOURCE_DIR          = PROJECT_ROOT / "src" / "source_open_api"
OUTPUT_BASE_DIR     = PROJECT_ROOT / "src" / "db_scripts" / "output_sdk"
PLATFORM_REGISTRY   = PROJECT_ROOT / "src" / "app" / "llm" / "platform_registry.json"


def clear_screen() -> None:
    if sys.stdout.isatty():
        os.system("cls" if os.name == "nt" else "clear")


def list_existing_sdks() -> List[str]:
    if not OUTPUT_BASE_DIR.exists():
        return []
    return sorted(p.name for p in OUTPUT_BASE_DIR.iterdir() if p.is_dir())


def ask(prompt: str, default: str = "") -> str:
    resp = Prompt.ask(f"[cyan]?[/cyan] [bold]{prompt}[/bold]", default=default)
    return resp.strip()


# alias so existing calls work
ask_choice = ask


def parse_package_dir(dest_dir: Path, fallback: str) -> str:
    pyproject = dest_dir / "pyproject.toml"
    if pyproject.exists():
        try:
            data = tomllib.loads(pyproject.read_text(encoding="utf-8"))
            name = data.get("project", {}).get("name") or \
                   data.get("tool", {}).get("poetry", {}).get("name")
            if name:
                return name.replace("-", "_")
        except Exception:
            pass
    return fallback


def main() -> None:
    clear_screen()
    console.print(Panel.fit("🗑️ OpenAPI SDK Deletion Wizard", style="green"))

    # Step 1: List existing SDK folders
    sdks = list_existing_sdks()
    if not sdks:
        console.print("[yellow]No SDKs to delete.[/yellow]")
        return

    table = Table(box=box.SIMPLE_HEAVY)
    table.add_column("#", style="bold cyan")
    table.add_column("SDK Name")
    for i, name in enumerate(sdks, 1):
        table.add_row(str(i), name)
    exit_idx = len(sdks) + 1
    table.add_row(str(exit_idx), "Exit")
    console.print(Panel(table, title="Select an SDK to delete", border_style="cyan"))

    choice = ask_choice(f"Enter number [1-{exit_idx}]", "")
    if choice.isdigit() and (idx := int(choice)) == exit_idx:
        console.print("[green]Cancelled.[/green]")
        return
    if not (choice.isdigit() and 1 <= (idx := int(choice)) <= len(sdks)):
        console.print("[red]Invalid selection. Exiting.[/red]")
        sys.exit(1)

    sdk_name = sdks[idx - 1]

    # Confirm deletion
    if not ask_choice(f"Really delete '{sdk_name}'? (y/N)", "N").lower().startswith("y"):
        console.print("[yellow]Aborted.[/yellow]")
        return

    # Step 2: Determine the actual module directory name via pyproject.toml
    sdk_path = OUTPUT_BASE_DIR / sdk_name
    pkg_dir = parse_package_dir(sdk_path, sdk_name)
    dist_name = pkg_dir.replace("_", "-")

    # Step 3: Delete the SDK directory
    try:
        shutil.rmtree(sdk_path)
        console.print(f"[green]Deleted SDK directory: {sdk_path.relative_to(PROJECT_ROOT)}[/green]")
    except Exception as e:
        console.print(f"[red]Failed to remove '{sdk_path}': {e}[/red]")
        sys.exit(1)



    # Step 4: Update platform_registry.json (remove any matching "sdk_module" and its "created_by_us" flag)
    try:
        if PLATFORM_REGISTRY.exists():
            registry_data = json.loads(PLATFORM_REGISTRY.read_text(encoding="utf-8"))
            updated = False

            # Iterate over each platform entry and clear fields if "sdk_module" matches pkg_dir
            for platform_key, entry in registry_data.items():
                if entry.get("sdk_module") == pkg_dir:
                    entry.pop("sdk_module", None)
                    entry.pop("created_by_us", None)
                    updated = True

            if updated:
                PLATFORM_REGISTRY.write_text(json.dumps(registry_data, indent=2), encoding="utf-8")
                console.print(f"[green]Removed 'sdk_module: {pkg_dir}' and its 'created_by_us' flag from platform_registry.json[/green]")
            else:
                console.print(f"[yellow]No matching 'sdk_module' found for '{pkg_dir}' in platform_registry.json[/yellow]")
    except Exception as e:
        console.print(f"[yellow]Warning: could not update platform_registry.json: {e}[/yellow]")


    # Step 5: Remind user to uninstall from their environment
    console.print(Panel.fit("📦 To fully remove from your Python environment, run:", style="cyan"))
    console.print(Markdown(f"```bash\npip uninstall -y {dist_name}\n```"))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[red]Interrupted by user.[/red]")
        sys.exit(1)
