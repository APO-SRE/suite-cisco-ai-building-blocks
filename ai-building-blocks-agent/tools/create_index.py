#!/usr/bin/env python3
from __future__ import annotations
################################################################################
## suite-cisco-ai-building-blocks/ai-building-blocks-agent/tools/create_index.py
## Copyright (c) 2025 Jeff Teeter
## Cisco Systems, Inc.
## Licensed under the Apache License, Version 2.0 (see LICENSE)
## Distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND.
################################################################################

"""
╔════════════════════════ Platform Indexer Wizard ═════════════════════════════════╗
║ A polished step-by-step CLI to run the index_functions script without the flags. ║
║ Hover over links or type '?' at prompts for examples.                            ║
║                                                                                  ║
║ FEATURES                                                                          ║
║   • Select a single platform or index ALL platforms                                ║
║   • Automatically configures PYTHONPATH                                             ║
║   • Shows the exact command in a copyable block                                    ║
╚══════════════════════════════════════════════════════════════════════════════════╝
"""

import argparse
import os
import shlex
import subprocess
import sys
from pathlib import Path
from typing import List, Optional, Tuple

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table
from rich.markdown import Markdown
from rich import box
from rich.traceback import install

install()
console = Console()

# Paths and patterns
AGENT_ROOT = Path(__file__).resolve().parents[1]
INDEXER_SCRIPT = AGENT_ROOT / "scripts" / "index_functions.py"
LLM_DEF_DIR = AGENT_ROOT / "app" / "llm" / "function_definitions"

# Helpers

def clear_screen() -> None:
    if sys.stdout.isatty():
        os.system("cls" if os.name == "nt" else "clear")


def list_platforms() -> List[Tuple[int, str]]:
    plats = sorted(fp.stem for fp in LLM_DEF_DIR.glob("*.json"))
    if not plats:
        console.print("[red]No platform JSON files found.[/red]")
        sys.exit(1)
    table = Table(box=box.SIMPLE_HEAVY)
    table.add_column("#", style="bold cyan")
    table.add_column("Platform")
    for i, name in enumerate(plats, 1):
        table.add_row(str(i), name)
    table.add_row("0", "All platforms")
    console.print(Panel(table, title="Step 1/3: Select Platform", border_style="cyan"))
    return list(enumerate(plats, 1))


def ask_choice(prompt: str, default: Optional[str] = None) -> str:
    resp = Prompt.ask(f"[cyan]?[/cyan] [bold]{prompt}[/bold]", default=default)
    return resp.strip()


def build_command(platform: Optional[str]) -> List[str]:
    if platform and platform.lower() != "all":
        return [sys.executable, str(INDEXER_SCRIPT), "--platform", platform]
    return [sys.executable, str(INDEXER_SCRIPT), "--all"]

# Main

def main() -> None:
    clear_screen()
    console.print(Panel.fit("🛠 Welcome to the Platform Indexer Wizard", style="green"))

    # Step 1: choose platform
    listing = list_platforms()
    choice = ask_choice("Enter number (0 for All)", "0")
    platform: Optional[str]
    if choice == "0":
        platform = None
    else:
        try:
            idx = int(choice)
            platform = next(name for n, name in listing if n == idx)
        except Exception:
            console.print("[red]Invalid selection. Exiting.[/red]")
            sys.exit(1)
    console.print(f":white_check_mark: Selected [bold]{platform or 'All'}[/bold]\n")

    # Step 2: preview command
    cmd_parts = build_command(platform)
    cmd_str = " ".join(shlex.quote(p) for p in cmd_parts)
    console.print(
    Panel(
        Markdown(
            f"**Command to run**\n```bash\n{cmd_str}\n```"
        ),
        border_style="cyan",
        title="Step 2/3: Preview Command"
    )
)

    # Step 3: confirmation
    proceed = ask_choice("Proceed with indexing? (Y/n)", "Y")
    if proceed.lower().startswith("n"):
        console.print("[yellow]Aborted by user.[/yellow]")
        return

    # Execute
    console.print(Panel.fit("🚀 Running indexer...", style="cyan"))
    env = os.environ.copy()
    env["PYTHONPATH"] = f"{AGENT_ROOT}:{env.get('PYTHONPATH','')}"
    subprocess.run(cmd_parts, check=True, env=env)
    console.print(Panel.fit(":white_check_mark: Indexing complete!", style="green"))

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[red]Interrupted by user.[/red]")
