#!/usr/bin/env python3
from __future__ import annotations
################################################################################
## suite-cisco-ai-building-blocks/src/app/user_commands/create_platform_route.py
## Copyright (c) 2025 Jeff Teeter, Ph.D.
## Cisco Systems, Inc.
## Licensed under the Apache License, Version 2.0 (see LICENSE)
## Distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND.
################################################################################

"""
╔═══════════════════════ Create Platform Route Wizard ═══════════════════════╗
║ A step-by-step CLI to scaffold a new FastAPI route for a platform.        ║
║                                                                         ║
║ STEPS                                                                   ║
║   1. Select a scaffolded platform                                       ║
║   2. Choose a URL prefix                                                ║
║   3. Review & confirm                                                   ║
║   4. Generate route file & update router registry                       ║
╚═════════════════════════════════════════════════════════════════════════╝
"""

import os
import sys
from pathlib import Path
import json

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt
from rich.tree import Tree
from rich import box
from rich.traceback import install

install()
console = Console()

# project roots
env_root = Path(__file__).resolve().parents[3]  # suite-cisco-ai-building-blocks
USER_CMDS = Path(__file__).resolve().parents[1]
ROUTER_DIR = env_root / "src" / "app" / "routers"

# definitions directory (scaffolded platforms)
def list_definitions() -> list[str]:
    defs = env_root / "src" / "app" / "llm" / "function_definitions"
    if not defs.exists():
        return []
    return sorted(p.stem for p in defs.glob("*.json") if p.is_file())


def clear_screen() -> None:
    if sys.stdout.isatty():
        os.system("cls" if os.name == "nt" else "clear")


def main() -> None:
    clear_screen()
    console.print(Panel.fit("🚀 Create Platform Route Wizard", style="green"))

    # Step 1: pick platform or exit
    platforms = list_definitions()
    if not platforms:
        console.print("[red]No scaffolded platforms found under llm/function_definitions[/red]")
        sys.exit(1)
    table = Table(box=box.SIMPLE_HEAVY)
    table.add_column("#", style="bold cyan")
    table.add_column("Platform")
    for i, name in enumerate(platforms, 1):
        table.add_row(str(i), name)
    exit_idx = len(platforms) + 1
    table.add_row(str(exit_idx), "Exit")
    console.print(Panel(table, title="Step 1/3: Select Scaffolded Platform", border_style="cyan"))
    choice = Prompt.ask(f"Enter number [1-{exit_idx}]", default="").strip()
    if choice.isdigit() and int(choice) == exit_idx:
        console.print("[green]Exiting…[/green]")
        sys.exit(0)
    if not (choice.isdigit() and 1 <= (idx := int(choice)) <= len(platforms)):
        console.print("[red]Invalid selection. Exiting.[/red]")
        sys.exit(1)
    platform = platforms[idx-1]
    console.print(f":white_check_mark: Selected platform [bold]{platform}[/bold]\n")

    # Step 2: choose route prefix
    console.print(Panel.fit("🔧 Step 2/3: Define URL Prefix", border_style="cyan"))
    default_prefix = f"/{platform}"
    prefix = Prompt.ask("Route URL prefix", default=default_prefix).strip()
    console.print(f":white_check_mark: URL prefix set to [bold]{prefix}[/bold]\n")

    # Step 3: preview & confirm
    filename = f"{platform}_route.py"
    target = ROUTER_DIR / filename
    stub = (
        f"from fastapi import APIRouter, Depends\n"
        f"from app.llm.unified_service import UnifiedService\n\n"
        f"router = APIRouter(prefix=\"{prefix}\", tags=[\"{platform}\"])\n\n"
        f"@router.get(\"/\")\n"
        f"async def get_{platform}_info():\n"
        f"    return UnifiedService.{platform}_info()\n"
    )
    console.print(Panel(
        f"Will create route file:\n[white]{target}[/white]\n\nStub content:\n{i}{stub}",
        title="Step 3/3: Preview Route", border_style="cyan"
    ))
    proceed = Prompt.ask("Proceed and generate? (Y/n)", default="Y").lower()
    if proceed.startswith("n"):
        console.print("[yellow]Aborted by user.[/yellow]")
        sys.exit(0)

    # generate file
    ROUTER_DIR.mkdir(parents=True, exist_ok=True)
    target.write_text(stub, encoding="utf-8")
    console.print(f"[green]Created route file → {target}[/green]")

    # register in __init__.py
    init_py = ROUTER_DIR / "__init__.py"
    import_line = f"from .{platform}_route import router as {platform}_router\n"
    if not init_py.exists():
        init_py.write_text(import_line, encoding="utf-8")
    else:
        lines = init_py.read_text(encoding="utf-8").splitlines(keepends=True)
        if import_line not in lines:
            lines.append(import_line)
            init_py.write_text("".join(lines), encoding="utf-8")
    console.print(f"[green]Updated router registry → {init_py}[/green]")

    console.print(Panel.fit(":white_check_mark: Done!", style="green"))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[red]Interrupted by user.[/red]")
        sys.exit(1)
