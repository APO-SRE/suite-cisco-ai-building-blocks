#!/usr/bin/env python3
from __future__ import annotations
#######################################################################################
## suite-cisco-ai-building-blocks/ai-building-blocks-agent/user_commands/create_sdk.py
## Copyright (c) 2025 Jeff Teeter, Ph.D.
## Cisco Systems, Inc.
## Licensed under the Apache License, Version 2.0 (see LICENSE)
## Distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND.
#######################################################################################

"""
╔═══════════════════ OpenAPI SDK Generation Wizard ═════════════════════════╗
║ A polished step-by-step CLI to run openapi-python-client for your specs.  ║
║ Hover over links or type '?' at prompts for examples.                     ║
║                                                                           ║
║ FEATURES                                                                  ║
║   • Select a single spec or generate for ALL specs                        ║
║   • For each spec, optionally rename the SDK folder (defaults to stem)    ║
║   • Shows the exact openapi-python-client commands in a copyable block    ║
║   • At the end, lists the contents of the output_sdk directory            ║
║   • Updates app/llm/sdk_map.json with any new SDK names                  ║
║   • Displays import snippet for each newly generated SDK                 ║
╚═══════════════════════════════════════════════════════════════════════════╝
"""

import os
import sys
import shlex
import subprocess
import json
from pathlib import Path
from typing import List, Dict

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table
from rich.markdown import Markdown
from rich.tree import Tree
from rich import box
from rich.traceback import install

install()
console = Console()

# Locate dirs
AGENT_ROOT = Path(__file__).resolve().parents[1]
DB_ROOT = AGENT_ROOT.parent / "ai-building-blocks-database"
SOURCE_DIR = DB_ROOT / "source_open_api"
OUTPUT_BASE_DIR = DB_ROOT / "output_sdk"
SDK_MAP_FILE = AGENT_ROOT / "app" / "llm" / "sdk_map.json"


def clear_screen() -> None:
    if sys.stdout.isatty():
        os.system("cls" if os.name == "nt" else "clear")


def list_specs() -> List[Path]:
    specs = sorted(
        p for p in SOURCE_DIR.iterdir()
        if p.is_file() and p.suffix.lower() in {".json", ".yaml", ".yml"}
    )
    if not specs:
        console.print(f"[red]No OpenAPI files found in {SOURCE_DIR}[/red]")
        sys.exit(1)

    table = Table(box=box.SIMPLE_HEAVY)
    table.add_column("#", style="bold cyan")
    table.add_column("Spec file")
    for i, p in enumerate(specs, 1):
        table.add_row(str(i), p.name)
    table.add_row("0", "All specs")
    console.print(Panel(table, title="Step 1/4: Select OpenAPI Spec", border_style="cyan"))
    return specs


def ask_choice(prompt: str, default: str) -> str:
    return Prompt.ask(f"[cyan]?[/cyan] [bold]{prompt}[/bold]", default=default).strip()


def build_commands(mapping: Dict[Path, str]) -> List[List[str]]:
    cmds: List[List[str]] = []
    for spec, sdk_name in mapping.items():
        dest = OUTPUT_BASE_DIR / sdk_name
        dest.mkdir(parents=True, exist_ok=True)
        cmd = [
            "openapi-python-client", "generate",
            "--path", str(SOURCE_DIR / spec.name),
            "--output-path", str(dest),
            "--meta", "poetry",
            "--overwrite",
        ]
        cmds.append(cmd)
    return cmds


def main() -> None:
    clear_screen()
    console.print(Panel.fit("🚀 OpenAPI SDK Generation Wizard", style="green"))

    # Step 1: choose spec(s)
    specs = list_specs()
    choice = ask_choice(f"Enter number [0-{len(specs)}]", "0")
    if choice == "0":
        selected = specs
        label = "All specs"
    else:
        try:
            idx = int(choice)
            selected = [specs[idx - 1]]
            label = specs[idx - 1].name
        except Exception:
            console.print("[red]Invalid selection. Exiting.[/red]")
            sys.exit(1)
    console.print(f":white_check_mark: Selected [bold]{label}[/bold]\n")

    # Step 2: optionally rename each SDK folder
    mapping: Dict[Path, str] = {}
    console.print(Panel.fit("🔧 Step 2/4: Name Your SDK Folders", border_style="cyan"))
    for spec in selected:
        default_name = spec.stem
        sdk_name = ask_choice(f"SDK folder name for '{spec.name}'", default_name)
        mapping[spec] = sdk_name
    console.print(":white_check_mark: Names set\n")

    # Step 3: preview commands
    cmds = build_commands(mapping)
    md_blocks = "\n".join(
        "```bash\n" + " ".join(shlex.quote(p) for p in cmd) + "\n```"
        for cmd in cmds
    )
    console.print(
        Panel(
            Markdown(f"**Commands to run**\n{md_blocks}"),
            title="Step 3/4: Preview Commands",
            border_style="cyan",
        )
    )

    proceed = ask_choice("Proceed with SDK generation? (Y/n)", "Y")
    if proceed.lower().startswith("n"):
        console.print("[yellow]Aborted by user.[/yellow]")
        return

    # Step 4: execute
    console.print(Panel.fit("🛠 Generating SDK(s)...", style="cyan"))
    for cmd in cmds:
        console.print(f"> [bold]{' '.join(shlex.quote(p) for p in cmd)}[/bold]")
        result = subprocess.run(cmd)
        if result.returncode != 0:
            console.print(f"[red]Failed for {cmd[-2]}[/red]")
        else:
            console.print(f"[green]Success for {cmd[-2]}[/green]")

    console.print(Panel.fit(":white_check_mark: Generation complete!", style="green"))

    # Final: list contents of output_sdk
    console.print(Panel.fit("📂 Contents of output_sdk/", style="cyan"))
    tree = Tree(f"[bold]{OUTPUT_BASE_DIR.name}[/bold]")
    for sdk_dir in sorted(OUTPUT_BASE_DIR.iterdir()):
        if not sdk_dir.is_dir():
            continue
        branch = tree.add(sdk_dir.name)
        for child in sorted(sdk_dir.iterdir()):
            branch.add(child.name)
    console.print(tree)

    # Update sdk_map.json with new SDK names and show import snippet
    try:
        sdk_map: Dict[str, str] = json.loads(SDK_MAP_FILE.read_text(encoding="utf-8"))
    except Exception:
        sdk_map = {}
    added: List[str] = []
    for sdk_name in mapping.values():
        if sdk_name not in sdk_map:
            sdk_map[sdk_name] = sdk_name
            added.append(sdk_name)
    if added:
        try:
            SDK_MAP_FILE.parent.mkdir(parents=True, exist_ok=True)
            SDK_MAP_FILE.write_text(json.dumps(sdk_map, indent=2), encoding="utf-8")
            console.print(f"[green]Added to SDK map: {', '.join(added)}[/green]")
            # Show import snippet
            console.print(Panel.fit("👉 Usage in your Python code:", style="cyan"))
            for name in added:
                console.print(Markdown(f"```python import {name}```"))
        except Exception as e:
            console.print(f"[red]Failed to update SDK map: {e}[/red]")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[red]Interrupted by user.[/red]")
        sys.exit(1)
