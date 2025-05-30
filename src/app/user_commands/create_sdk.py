#!/usr/bin/env python3
from __future__ import annotations
#######################################################################################
## suite-cisco-ai-building-blocks/src/app/user_commands/create_sdk.py
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
║   • Select a single spec                                                 ║
║   • Option to exit without generating                                     ║
║   • Rename the SDK folder (defaults to spec stem)                         ║
║   • Shows the openapi-python-client command in a copyable block           ║
║   • Lists existing SDKs at startup                                        ║
║   • Updates app/llm/sdk_map.json with any new SDKs                        ║
║   • Displays install instruction and import snippet                       ║
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
from rich.tree import Tree
from rich.markdown import Markdown
from rich import box
from rich.traceback import install

install()
console = Console()

# Repo root is four levels up from this file
PROJECT_ROOT     = Path(__file__).resolve().parents[3]
# Specs now live under top‑level src/source_open_api
SOURCE_DIR       = PROJECT_ROOT / "src" / "source_open_api"
OUTPUT_BASE_DIR  = PROJECT_ROOT / "src" / "db_scripts" / "output_sdk"
SDK_MAP_FILE     = PROJECT_ROOT / "src" / "app" / "llm" / "sdk_map.json"


def clear_screen() -> None:
    if sys.stdout.isatty():
        os.system("cls" if os.name == "nt" else "clear")


def list_existing_sdks() -> List[str]:
    if not OUTPUT_BASE_DIR.exists():
        return []
    return sorted(p.name for p in OUTPUT_BASE_DIR.iterdir() if p.is_dir())


def list_specs() -> List[Path]:
    specs = sorted(
        p for p in SOURCE_DIR.iterdir()
        if p.is_file() and p.suffix.lower() in {".json", ".yaml", ".yml"}
    )
    if not specs:
        console.print(f"[red]No OpenAPI files found in {SOURCE_DIR}[/red]")
        sys.exit(1)
    return specs


def ask_choice(prompt: str, default: str) -> str:
    return Prompt.ask(f"[cyan]?[/cyan] [bold]{prompt}[/bold]", default=default).strip()


def build_command(spec: Path, sdk_name: str) -> List[str]:
    dest = OUTPUT_BASE_DIR / sdk_name
    dest.mkdir(parents=True, exist_ok=True)
    return [
        "openapi-python-client", "generate",
        "--path", str(spec),
        "--output-path", str(dest),
        "--meta", "poetry",
        "--overwrite",
    ]


def main() -> None:
    clear_screen()
    console.print(Panel.fit("🚀 OpenAPI SDK Generation Wizard", style="green"))

    # -- show existing SDKs
    existing = list_existing_sdks()
    console.print(Panel(
        ", ".join(existing) if existing else "(none)",
        title="Existing SDKs in output_sdk/",
        border_style="magenta"
    ))

    # -- step 1: pick spec or exit
    specs = list_specs()
    table = Table(box=box.SIMPLE_HEAVY)
    table.add_column("#", style="bold cyan")
    table.add_column("Spec file")
    for i, p in enumerate(specs, 1):
        table.add_row(str(i), p.name)
    exit_idx = len(specs) + 1
    table.add_row(str(exit_idx), "Exit")
    console.print(Panel(table, title="Step 1/4: Select OpenAPI Spec", border_style="cyan"))

    choice = ask_choice(f"Enter number [1-{exit_idx}]", "")
    if choice.isdigit() and int(choice) == exit_idx:
        console.print("[green]Exiting…[/green]")
        sys.exit(0)
    if not (choice.isdigit() and 1 <= (idx := int(choice)) <= len(specs)):
        console.print("[red]Invalid selection. Exiting.[/red]")
        sys.exit(1)
    spec = specs[idx - 1]
    console.print(f":white_check_mark: Selected [bold]{spec.name}[/bold]\n")

    # -- step 2: choose folder name
    console.print(Panel.fit("🔧 Step 2/4: Name Your SDK Folder", border_style="cyan"))
    default_name = spec.stem
    sdk_name = ask_choice(f"SDK folder name for '{spec.name}'", default_name)
    console.print(":white_check_mark: Name set\n")

    # -- step 3: preview
    cmd = build_command(spec, sdk_name)
    console.print(Panel(
        Markdown(f"**Command to run**\n```bash {' '.join(shlex.quote(p) for p in cmd)} ```"),
        title="Step 3/4: Preview Command",
        border_style="cyan"
    ))
    if ask_choice("Proceed with SDK generation? (Y/n)", "Y").lower().startswith("n"):
        console.print("[yellow]Aborted by user.[/yellow]")
        return

    # -- step 4: run
    console.print(Panel.fit("🛠 Generating SDK…", style="cyan"))
    result = subprocess.run(cmd)
    if result.returncode != 0:
        console.print(f"[red]Generation failed for {spec.name}[/red]")
        sys.exit(1)
    console.print(f"[green]Success for {spec.name} → {sdk_name}[/green]\n")

    # -- show tree
    console.print(Panel.fit("📂 Contents of output_sdk/", style="cyan"))
    tree = Tree(f"[bold]{OUTPUT_BASE_DIR.name}[/bold]")
    for sdk_dir in sorted(OUTPUT_BASE_DIR.iterdir()):
        if not sdk_dir.is_dir():
            continue
        branch = tree.add(sdk_dir.name)
        for child in sorted(sdk_dir.iterdir()):
            branch.add(child.name)
    console.print(tree)

    # -- detect actual package directory for import and mapping
    pkg_dir = next(
        (d.name for d in (OUTPUT_BASE_DIR / sdk_name).iterdir()
         if d.is_dir() and (d / "__init__.py").exists()),
        sdk_name
    )

    # -- update sdk_map.json
    try:
        sdk_map: Dict[str, str] = json.loads(SDK_MAP_FILE.read_text(encoding="utf-8"))
    except Exception:
        sdk_map = {}
    if sdk_name not in sdk_map:
        sdk_map[sdk_name] = pkg_dir
        SDK_MAP_FILE.parent.mkdir(parents=True, exist_ok=True)
        SDK_MAP_FILE.write_text(json.dumps(sdk_map, indent=2), encoding="utf-8")
        console.print(f"[green]Added to SDK map: {sdk_name} → {pkg_dir}[/green]")

    # -- show install instructions
    console.print(Panel.fit("📦 Install into your environment:", style="cyan"))
    abs_dest = (OUTPUT_BASE_DIR / sdk_name).resolve()
    console.print(Markdown(f"```bash pip install -e {abs_dest} ```"))

    # -- usage snippet
    console.print(Panel.fit("👉 Usage in your Python code:", style="cyan"))
    console.print(Markdown(f"```python import {pkg_dir} ```"))

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[red]Interrupted by user.[/red]")
        sys.exit(1)
