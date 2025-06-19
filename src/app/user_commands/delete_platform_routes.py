#!/usr/bin/env python3
from __future__ import annotations
################################################################################
## suite-cisco-ai-building-blocks/src/app/user_commands/delete_platform_route.py
## Copyright (c) 2025 Jeff Teeter
## Cisco Systems, Inc.
## Licensed under the Apache License, Version 2.0 (see LICENSE)
################################################################################
"""
CLI utility that deletes a `<platform>_routes.py` file **and** clears the
`"route": false` flag in ``platform_registry.json``.

Because `routers/__init__.py` is now self‑discovering, no edit is required
there – removing the file is enough.
"""
import json
import sys
from pathlib import Path

from rich import box
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table
from rich.traceback import install

install()
console = Console()

# ──────────────────────────────────────────────────────────────────────────────
APP_DIR      = Path(__file__).resolve().parents[1]       # …/src/app
ROUTERS_DIR  = APP_DIR / "routers"
REGISTRY     = APP_DIR / "llm" / "platform_registry.json"
# ──────────────────────────────────────────────────────────────────────────────


def _routes() -> list[Path]:
    return sorted(ROUTERS_DIR.glob("*_routes.py"))


def _clear_flag(short: str) -> None:
    if not REGISTRY.exists():
        return

    try:
        data = json.loads(REGISTRY.read_text("utf-8"))
    except json.JSONDecodeError:
        console.print(f"[yellow]⚠ Cannot update registry – it is invalid JSON.[/yellow]")
        return

    if short in data:
        data[short]["route"] = False
        REGISTRY.write_text(json.dumps(data, indent=2), "utf-8")
        console.print(f"[grey]→ flag cleared for '{short}'[/grey]")


def main() -> None:
    console.print(Panel.fit("🗑️  Delete Platform Route", style="red"))

    files = _routes()
    if not files:
        console.print("[yellow]No *_routes.py files found.[/yellow]")
        sys.exit(0)

    tbl = Table(box=box.SIMPLE)
    tbl.add_column("#", style="bold cyan", no_wrap=True)
    tbl.add_column("File")
    for n, f in enumerate(files, 1):
        tbl.add_row(str(n), f.name)
    tbl.add_row(str(len(files) + 1), "Exit")
    console.print(Panel(tbl, title="Select file", border_style="red"))

    c = Prompt.ask("Choice", default=str(len(files) + 1)).strip()
    if not c.isdigit() or int(c) == len(files) + 1:
        console.print("[green]Aborted.[/green]")
        sys.exit(0)

    target = files[int(c) - 1]
    if Prompt.ask(f"Delete [bold]{target.name}[/bold]?", choices=["y", "n"], default="n") != "y":
        console.print("[green]Aborted.[/green]")
        sys.exit(0)

    try:
        target.unlink()
        console.print(f"[green]✔ Removed {target.name}[/green]")
        _clear_flag(target.stem.replace("_routes", ""))
    except Exception as exc:  # noqa: BLE001
        console.print(f"[red]✖ {exc}[/red]")
        sys.exit(1)


if __name__ == "__main__":  # pragma: no cover
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[red]Interrupted.[/red]")
        sys.exit(1)
