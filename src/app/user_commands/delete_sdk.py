#!/usr/bin/env python3
from __future__ import annotations
#######################################################################################
## suite-cisco-ai-building-blocks/ai-building-blocks-agent/user_commands/delete_sdk.py
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
║   • List existing SDKs                                                      ║
║   • Select one to delete                                                    ║
║   • Confirm and remove SDK directory and update sdk_map.json                 ║
║   • Exit option                                                             ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

import os
import sys
import json
import shutil
from pathlib import Path
from typing import List

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table
from rich.markdown import Markdown
from rich import box
from rich.traceback import install

install()
console = Console()

# Paths
PROJECT_ROOT     = Path(__file__).resolve().parents[2]
SOURCE_DIR       = PROJECT_ROOT / "src" / "db_scripts" / "source_open_api"
OUTPUT_BASE_DIR  = PROJECT_ROOT / "src" / "db_scripts" / "output_sdk"
SDK_MAP_FILE     = PROJECT_ROOT / "src" / "app" / "llm" / "sdk_map.json"


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


def main() -> None:
    clear_screen()
    console.print(Panel.fit("🗑️ OpenAPI SDK Deletion Wizard", style="green"))

    # list existing SDKs
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
    if not ask_choice(f"Really delete '{sdk_name}'? (y/N)", "N").lower().startswith("y"):
        console.print("[yellow]Aborted.[/yellow]")
        return

    # ● BEFORE deleting, detect the actual package folder for uninstall
    sdk_path = OUTPUT_BASE_DIR / sdk_name
    pkg_dir = next(
        (
            d.name
            for d in sdk_path.iterdir()
            if d.is_dir() and (d / "__init__.py").exists()
        ),
        sdk_name,
    )
    dist_name = pkg_dir.replace("_", "-")

    # delete folder
    shutil.rmtree(sdk_path)

    # update sdk_map.json
    try:
        sdk_map = json.loads(SDK_MAP_FILE.read_text(encoding="utf-8"))
        sdk_map.pop(sdk_name, None)
        SDK_MAP_FILE.write_text(json.dumps(sdk_map, indent=2), encoding="utf-8")
    except Exception:
        pass

    console.print(f"[green]Deleted SDK: {sdk_name}[/green]")

    # remind to uninstall
    console.print(Panel.fit("📦 Uninstall from your environment:", style="cyan"))
    console.print(Markdown(f"```bash\npip uninstall -y {dist_name}\n```"))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[red]Interrupted by user.[/red]")
        sys.exit(1)
