#!/usr/bin/env python3
from __future__ import annotations
#######################################################################################
## suite-cisco-ai-building-blocks/src/app/user_commands/create_sdk.py
## Copyright (c) 2025 Jeff Teeter, Ph.D.
## Cisco Systems, Inc.
## Licensed under the Apache License, Version 2.0 (see LICENSE)
## Distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND.
#######################################################################################

import os
import sys
import subprocess
from pathlib import Path
from typing import List, Dict, Optional
import json
import re
import shutil
import tomllib
import yaml

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table
from rich.tree import Tree
from rich.markdown import Markdown
from rich import box
from rich.traceback import install

# ─────────────────────────────────────────────────────────────────────────────
install()
console = Console()

# ──────────────────────────── Paths / constants
PROJECT_ROOT = Path(__file__).resolve().parents[3]
SOURCE_DIR   = PROJECT_ROOT / "src" / "source_open_api"
OUTPUT_BASE  = PROJECT_ROOT / "src" / "db_scripts" / "output_sdk"

# We will *call into* the bulk generator, so import it lazily
GENERATOR_MOD = "db_scripts.scripts.generate_openapi_sdks"

# ──────────────────────────── Helper utilities
def clear_screen() -> None:
    if sys.stdout.isatty():
        os.system("cls" if os.name == "nt" else "clear")


def list_specs() -> List[Path]:
    return sorted(
        p for p in SOURCE_DIR.iterdir()
        if p.is_file() and p.suffix.lower() in {".json", ".yaml", ".yml"}
    )


def list_existing_sdks() -> List[str]:
    return sorted(p.name for p in OUTPUT_BASE.iterdir() if p.is_dir()) if OUTPUT_BASE.exists() else []


def ask(prompt: str, default: str | None = None) -> str:
    return Prompt.ask(f"[cyan]?[/cyan] [bold]{prompt}[/bold]", default=default or "").strip()


def sanitize_folder(name: str) -> str:
    out = re.sub(r"[^0-9a-zA-Z_]+", "_", name).lower()
    return re.sub(r"_+", "_", out).strip("_") or "sdk"


# ──────────────────────────── Main CLI
def main() -> None:
    clear_screen()
    console.print(Panel.fit("🚀 OpenAPI SDK Generation Wizard", style="green"))

    # Show already‑generated SDKs
    console.print(
        Panel(
            ", ".join(list_existing_sdks()) or "(none)",
            title="Existing SDKs in output_sdk/",
            border_style="magenta",
        )
    )

    specs = list_specs()
    if not specs:
        console.print(f"[red]No OpenAPI documents found in {SOURCE_DIR}[/red]")
        sys.exit(1)

    # Step 1 – choose spec
    table = Table(box=box.SIMPLE_HEAVY, show_lines=False)
    table.add_column("#", style="bold cyan", width=4)
    table.add_column("OpenAPI document")
    for i, sp in enumerate(specs, 1):
        table.add_row(str(i), sp.name)
    table.add_row("0", "Exit")
    console.print(Panel(table, title="Select an OpenAPI spec", border_style="cyan"))

    choice = ask(f"Enter number [1‑{len(specs)}]", "")
    if choice == "0":
        console.print("[green]Bye![/green]")
        sys.exit(0)
    if not choice.isdigit() or not (1 <= int(choice) <= len(specs)):
        console.print("[red]Invalid selection[/red]")
        sys.exit(1)

    spec_path: Path = specs[int(choice) - 1]
    console.print(f":white_check_mark: Selected [bold]{spec_path.name}[/bold]\n")

    # Step 2 – folder / package name
    sdk_folder_raw = ask("Enter folder name for the SDK (will live under output_sdk/)", spec_path.stem)
    sdk_folder     = sanitize_folder(sdk_folder_raw)
    console.print(f":white_check_mark: Folder will be [bold]{sdk_folder}[/bold]\n")

    # Confirm
    if ask("Proceed with SDK generation? (Y/n)", "Y").lower().startswith("n"):
        console.print("[yellow]Aborted by user[/yellow]")
        sys.exit(0)

    # ----------------------------------------------------------------------
    # DELEGATE to the bulk generator
    # We run it in a *sub‑process* so that its interactive prompts can be
    # faked with stdin.  We provide our two answers (spec index + folder).
    # ----------------------------------------------------------------------
    import importlib.util

    # 1. Build the command that resolves to the proper entry‑point script
    generator_entry = Path(importlib.util.find_spec(GENERATOR_MOD).origin)

    cmd = [
        sys.executable,
        str(generator_entry),
    ]

    # 2. Pre‑feed answers to the generator over stdin
    #
    #   • First prompt  → choose the single spec index
    #   • Second prompt → folder name
    #
    answers = f"{choice}\n{sdk_folder}\n"
    result = subprocess.run(cmd, input=answers.encode(), cwd=PROJECT_ROOT)
    if result.returncode != 0:
        console.print(f"[red]Generator script failed (exit {result.returncode})[/red]")
        sys.exit(1)

    # ----------------------------------------------------------------------
    # Post‑generation: install editable package (same as before)
    # ----------------------------------------------------------------------
    edit_path = OUTPUT_BASE / sdk_folder
    console.print(Panel.fit("📦 Installing SDK in editable mode…", style="cyan"))
    subprocess.run([sys.executable, "-m", "pip", "install", "-e", str(edit_path)])

    # Show tree
    tree = Tree(f"[bold]{OUTPUT_BASE.name}[/bold]")
    for d in sorted(OUTPUT_BASE.iterdir()):
        if d.is_dir():
            br = tree.add(d.name)
            for c in sorted(d.iterdir()):
                br.add(c.name)
    console.print(tree)

    # Usage hint
    # Guess the package dir from pyproject.toml
    pyproject = edit_path / "pyproject.toml"
    pkg_name  = sdk_folder
    if pyproject.exists():
        data = tomllib.loads(pyproject.read_text("utf-8"))
        pkg_name = (
            data.get("project", {}).get("name")
            or data.get("tool", {}).get("poetry", {}).get("name")
            or sdk_folder
        ).replace("-", "_")

    console.print(
        Panel.fit(
            Markdown(f"```python\nfrom {pkg_name}.client import Client\n```"),
            title="✅ SDK ready to import",
            border_style="green",
        )
    )


# ────────────────────────────
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[red]Interrupted[/red]")
        sys.exit(1)
