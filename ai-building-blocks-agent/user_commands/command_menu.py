#!/usr/bin/env python3
from __future__ import annotations
################################################################################
## suite-cisco-ai-building-blocks/ai-building-blocks-agent/user_commands/command_menu.py
## Copyright (c) 2025 Jeff Teeter, Ph.D.
## Cisco Systems, Inc.
## Licensed under the Apache License, Version 2.0 (see LICENSE)
## Distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND.
################################################################################

"""
╔═════════════════════════ Command Launcher Wizard ═════════════════════════╗
║ A CLI tool to run common AI agent utilities with a polished UX.         ║
║ Press [cyan]i<n>[/cyan] (e.g. i2) to learn more about command <n>.      ║
║ Enter the number to execute, or the exit option to quit.                ║
╚════════════════════════════════════════════════════════════════════════════╝
"""

import os
import sys
import subprocess
import shlex
from pathlib import Path

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt
from rich import box
from rich.traceback import install
from rich.markdown import Markdown

install()
console = Console()

# clear screen helper
def clear_screen() -> None:
    if sys.stdout.isatty():
        os.system("cls" if os.name == "nt" else "clear")

# Available commands with short and detailed descriptions
COMMANDS: list[dict[str, str]] = [
    {
        "script": "create_platform.py",
        "short": "Scaffold a new platform",
        "long": (
            "`create_platform.py` gathers platform name, SDK module, OpenAPI spec, "
            "HTTP verbs, and regex filters, and generates the LLM artifacts (function defs, "
            "OpenAPI specs, client stubs, dispatchers, and services)."
        ),
    },
    {
        "script": "create_platform_index.py",
        "short": "Index platform functions",
        "long": (
            "`create_platform_index.py` lets you pick a platform's function definitions, "
            "then embeds and indexes them into your vector database."
        ),
    },
    {
        "script": "create_sdk.py",
        "short": "Generate an OpenAPI-based SDK",
        "long": (
            "`create_sdk.py` prompts for an OpenAPI spec and uses the OpenAPI client generator "
            "to produce a Python SDK package for that API."
        ),
    },
    {
        "script": "reset_platform.py",
        "short": "Reset platform artifacts",
        "long": (
            "`reset_platform.py` removes auto-generated LLM folders for a chosen platform, "
            "or recreates them empty, supporting a dry-run mode."
        ),
    },
    {
        "script": "create_domain_demo_index.py",
        "short": "Index a demo domain sample",
        "long": (
            "`create_domain_demo_index.py` lists domain_samples folders, lets you pick one, "
            "and runs `process_domain.py` to chunk, embed, and index that domain's data."
        ),
    },
]


def main() -> None:
    clear_screen()
    console.print(Panel.fit("🛠 Command Launcher Wizard", style="green"))

    AGENT_ROOT = Path(__file__).resolve().parents[1]
    UCMD_DIR = AGENT_ROOT / "user_commands"

    exit_idx = len(COMMANDS) + 1
    while True:
        # display commands
        table = Table(box=box.SIMPLE)
        table.add_column("#", style="bold cyan", no_wrap=True)
        table.add_column("Script")
        table.add_column("Description")
        for idx, cmd in enumerate(COMMANDS, start=1):
            table.add_row(str(idx), cmd["script"], cmd["short"])
        table.add_row(str(exit_idx), "Exit", "Quit the wizard")
        console.print(Panel(table, title="Select or Inspect Command", border_style="cyan"))

        choice = Prompt.ask("Enter number to run, or 'i<n>' for info (e.g. i2)")
        choice = choice.strip()

        # Info branch
        if choice.lower().startswith("i"):
            num = choice[1:]
            if num.isdigit() and 1 <= (i := int(num)) <= len(COMMANDS):
                detail = COMMANDS[i-1]["long"]
                console.print(
                    Panel(
                        Markdown(detail),
                        title=f"Info: {COMMANDS[i-1]['script']}",
                        border_style="magenta",
                    )
                )
                Prompt.ask("Press Enter to return")
                clear_screen()
                continue
            console.print(f"[red]Invalid info request: {choice}[/red]")
            continue

        # Exit branch
        if choice.isdigit() and int(choice) == exit_idx:
            console.print("[green]Goodbye![/green]")
            sys.exit(0)

        # Run branch
        if choice.isdigit() and 1 <= (sel := int(choice)) <= len(COMMANDS):
            script_name = COMMANDS[sel-1]["script"]
            script_path = UCMD_DIR / script_name
            if not script_path.exists():
                console.print(f"[red]Script not found: {script_path}[/red]")
                sys.exit(1)
            clear_screen()
            console.print(Panel.fit(f"🚀 Running {script_name}...", style="cyan"))
            subprocess.run([sys.executable, str(script_path)], check=True, cwd=str(AGENT_ROOT))
            console.print(Panel.fit(":white_check_mark: Done!", style="green"))
            return

        console.print(f"[red]Invalid selection: {choice}[/red]")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()
        sys.exit(1)
