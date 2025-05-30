#!/usr/bin/env python3
from __future__ import annotations
#####################################################################################################
## suite-cisco-ai-building-blocks/src/app/user_commands/convert_swagger2_to_openapi3.py
## Copyright (c) 2025 Jeff Teeter, Ph.D.
## Cisco Systems, Inc.
## Licensed under the Apache License, Version 2.0 (see LICENSE)
## Distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND.
#####################################################################################################


"""
╔═══════════════════════════ Swagger-2 to OpenAPI-3 Converter ══════════════════════════════════╗
║ A CLI tool to batch-convert Swagger-2 specs into OpenAPI-3 format via `swagger2openapi`.       ║
║ • Lists all Swagger-2 files under db_scripts/source_swagger-2                                   ║
║ • Prompts for selection, performs conversion with `npx swagger2openapi`                         ║
║ • Writes output into src/source_open_api with original filenames                                 ║
║ • Includes a clear-screen helper and polished Rich UI                                          ║
╚═════════════════════════════════════════════════════════════════════════════════════════════════╝
"""

import os
import re
import sys
import subprocess
import tempfile
from pathlib import Path

from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt
from rich.traceback import install

install()
console = Console()


def clear_screen() -> None:
    """Clear the terminal screen if running in a TTY."""
    if sys.stdout.isatty():
        os.system("cls" if os.name == "nt" else "clear")


def main() -> None:
    clear_screen()
    # Determine project directories
    repo_root = Path(__file__).resolve().parents[3]
    src_root = repo_root / "src"
    swagger_dir = src_root / "db_scripts" / "source_swagger-2"
    output_dir = src_root / "source_open_api"

    # Gather Swagger-2 files
    try:
        swagger_files = sorted(
            p for p in swagger_dir.iterdir()
            if p.is_file() and p.suffix.lower() in {".json", ".yaml", ".yml"}
        )
    except FileNotFoundError:
        console.print(f"[red]Directory not found: {swagger_dir}[/red]")
        sys.exit(1)

    if not swagger_files:
        console.print(f"[red]No Swagger-2 files found in {swagger_dir}[/red]")
        sys.exit(1)

    # Display menu
    table = Table(title="Available Swagger-2 files", show_lines=True)
    table.add_column("#", style="bold cyan", no_wrap=True)
    table.add_column("File")
    for idx, path in enumerate(swagger_files, start=1):
        table.add_row(str(idx), path.name)
    table.add_row("0", "Exit")
    console.print(table)

    choice = Prompt.ask(f"Select file to convert [0-{len(swagger_files)}]", default="0").strip()
    if not choice.isdigit():
        console.print("[red]Invalid input. Exiting.[/red]")
        sys.exit(1)
    num = int(choice)
    if num == 0:
        console.print("Exiting.")
        sys.exit(0)
    if not (1 <= num <= len(swagger_files)):
        console.print("[red]Selection out of range. Exiting.[/red]")
        sys.exit(1)

    # Source & destination paths
    src = swagger_files[num - 1]
    dst = output_dir / src.name
    output_dir.mkdir(parents=True, exist_ok=True)

    console.print(Panel(
        f"Converting [bold]{src.name}[/bold] → [bold]{dst}[/bold]",
        title="Conversion",
        border_style="cyan"
    ))

    # ─────────── Pre‐patch path templates in Swagger-2 ───────────
    # turn any "/:param" into "/{param}" so generators accept it
    text = src.read_text(encoding="utf-8")
    patched = re.sub(r"/:([A-Za-z0-9_]+)", r"/{\1}", text)
    tmp = tempfile.NamedTemporaryFile("w+", delete=False, encoding="utf-8")
    tmp.write(patched)
    tmp.flush()
    tmp_path = Path(tmp.name)
    tmp.close()
    src = tmp_path  # point conversion at the patched temp file

    # Run swagger2openapi
    try:
        subprocess.run(
            [
                "npx", "swagger2openapi",
                str(src),
                "--targetVersion", "3.0.0",
                "--outfile", str(dst),
                "--patch",
            ],
            check=True,
        )
        console.print(f"[green]✓ Conversion successful: {dst}[/green]")
    except subprocess.CalledProcessError as e:
        console.print(f"[red]Conversion failed (exit code {e.returncode})[/red]")
        sys.exit(e.returncode)
    finally:
        # clean up temp file
        try:
            tmp_path.unlink()
        except Exception:
            pass


if __name__ == "__main__":
    main()
