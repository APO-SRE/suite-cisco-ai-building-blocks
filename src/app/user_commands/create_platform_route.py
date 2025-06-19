#!/usr/bin/env python3
from __future__ import annotations
################################################################################
## suite-cisco-ai-building-blocks/src/app/user_commands/create_platform_route.py
## Copyright (c) 2025 Jeff Teeter, Ph.D.
## Cisco Systems, Inc.
## Licensed under the Apache License, Version 2.0 (see LICENSE)
################################################################################
"""
Interactive wizard that

1. lets the user pick a scaffolded platform JSON definition,
2. chooses the URL prefix,
3. writes `<platform>_routes.py`,
4. flips `"route": true` in ``platform_registry.json``.

**No change to   routers/__init__.py   is necessary any more** because that file
is now self‑discovering.  We therefore removed the brittle append logic.
"""
import json
import os
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
REPO_ROOT      = Path(__file__).resolve().parents[3]
LLM_DIR        = REPO_ROOT / "src" / "app" / "llm"
DEF_DIR        = LLM_DIR / "function_definitions"
ROUTER_DIR     = REPO_ROOT / "src" / "app" / "routers"
REGISTRY_PATH  = LLM_DIR / "platform_registry.json"
# ──────────────────────────────────────────────────────────────────────────────


def _set_route_flag(short: str, present: bool) -> None:
    """Toggle ``"route": <bool>`` for *short* in the registry."""
    registry: dict[str, dict] = {}
    if REGISTRY_PATH.exists():
        try:
            registry = json.loads(REGISTRY_PATH.read_text("utf-8"))
        except json.JSONDecodeError:
            console.print(f"[red]✖ {REGISTRY_PATH} is not valid JSON.[/red]")
            sys.exit(1)

    registry.setdefault(short, {
        "openapi_name": "",
        "sdk_module": "",
        "created_by_us": False,
        "installed": False,
    })["route"] = present

    REGISTRY_PATH.write_text(json.dumps(registry, indent=2), "utf-8")
    console.print(f"[grey]→ registry updated ({'enabled' if present else 'disabled'})[/grey]")


def _clear_screen() -> None:
    if sys.stdout.isatty():
        os.system("cls" if os.name == "nt" else "clear")


def _platforms() -> list[str]:
    return sorted(p.stem for p in DEF_DIR.glob("*.json")) if DEF_DIR.exists() else []


# ──────────────────────────────────────────────────────────────────────────────
def main() -> None:  # noqa: C901 (CLI = long is okay)
    _clear_screen()
    console.print(Panel.fit("🚀  Create Platform Route Wizard", style="green"))

    # 1) Select platform ------------------------------------------------------
    platforms = _platforms()
    if not platforms:
        console.print("[yellow]No scaffolded platforms found.[/yellow]")
        sys.exit(0)

    tbl = Table(box=box.SIMPLE_HEAVY)
    tbl.add_column("#", style="bold cyan", no_wrap=True)
    tbl.add_column("Platform")
    for i, name in enumerate(platforms, 1):
        tbl.add_row(str(i), name)
    tbl.add_row(str(len(platforms) + 1), "Exit")
    console.print(Panel(tbl, title="Step 1/3 – Pick platform", border_style="cyan"))

    c = Prompt.ask("Choice", default=str(len(platforms) + 1)).strip()
    if not c.isdigit() or int(c) == len(platforms) + 1:
        console.print("[green]Aborted.[/green]")
        sys.exit(0)

    platform = platforms[int(c) - 1]
    console.print(f":white_check_mark:  [bold]{platform}[/bold] selected\n")

    # 2) URL prefix -----------------------------------------------------------
    console.print(Panel.fit("🔧  Step 2/3 – URL prefix", border_style="cyan"))
    prefix = Prompt.ask("Prefix", default=f"/{platform}").rstrip("/")
    console.print(f":white_check_mark:  Will mount at [bold]{prefix}/…[/bold]\n")

    # 3) Preview --------------------------------------------------------------
    filename = f"{platform}_routes.py"
    target   = ROUTER_DIR / filename
    stub = f"""\"\"\"Auto‑generated FastAPI router for *{platform}* (edit me!).\"\"\"
from fastapi import APIRouter
from app.llm.unified_service import UnifiedService

router = APIRouter(prefix="{prefix}", tags=["{platform}"])

@router.get("/")
async def {platform}_info():
    \"\"\"Return basic information about the platform.\"\"\"
    return UnifiedService.{platform}_info()
"""
    console.print(Panel(stub, title="Step 3/3 – Stub preview", border_style="cyan"))
    if not Prompt.ask("Create file?", choices=["y", "n"], default="y").startswith("y"):
        console.print("[green]Aborted.[/green]")
        sys.exit(0)

    # Write file & update registry -------------------------------------------
    ROUTER_DIR.mkdir(parents=True, exist_ok=True)
    target.write_text(stub, "utf-8")
    console.print(f"[green]✔ Created {target.relative_to(REPO_ROOT)}[/green]")

    _set_route_flag(platform, True)
    console.print(Panel.fit(":white_check_mark:  Done!", style="green"))


if __name__ == "__main__":  # pragma: no cover
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[red]Interrupted.[/red]")
        sys.exit(1)
