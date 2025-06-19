#!/usr/bin/env python3
from __future__ import annotations
################################################################################
## suite-cisco-ai-building-blocks/src/app/user_commands/create_platform_route.py
## Copyright (c) 2025 Jeff Teeter, Ph.D.
## Cisco Systems, Inc.
## Licensed under the Apache License, Version 2.0 (see LICENSE)
################################################################################

"""
╔═══════════════════════ Create Platform Route Wizard ═══════════════════════╗
║ 1. Select a scaffolded platform                                            ║
║ 2. Define a URL prefix (defaults to /<platform>)                           ║
║ 3. Preview & confirm                                                        ║
║ 4. Generate <platform>_routes.py, update routers/__init__.py,              ║
║    and set `route = true` in platform_registry.json                        ║
╚════════════════════════════════════════════════════════════════════════════╝
"""
import os
import sys
import json
from pathlib import Path

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt
from rich import box
from rich.traceback import install

install()
console = Console()

# ── paths -------------------------------------------------------------------
# This script lives in: repo/src/app/user_commands/create_platform_route.py
# We need to locate the registry at repo/src/app/llm/platform_registry.json

REPO_ROOT      = Path(__file__).resolve().parents[3]      # …/suite-cisco-ai-building-blocks
LLM_DIR        = REPO_ROOT / "src" / "app" / "llm"
DEF_DIR        = LLM_DIR / "function_definitions"
ROUTER_DIR     = REPO_ROOT / "src" / "app" / "routers"
REGISTRY_PATH  = LLM_DIR / "platform_registry.json"

# ── registry flag helper ----------------------------------------------------
def set_route_flag(short_name: str, present: bool) -> None:
    """
    Directly load the JSON at REGISTRY_PATH, set 'route' to <present> for <short_name>,
    then save. If the key is missing, create a stub entry so we don't lose data.
    """
    if not REGISTRY_PATH.exists():
        # If the file doesn't exist, start with an empty dict
        registry: dict = {}
    else:
        try:
            registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            console.print(f"[red]Error:[/red] Failed to parse {REGISTRY_PATH}.")
            sys.exit(1)

    # If the platform key doesn't exist, create a minimal stub
    if short_name not in registry:
        registry[short_name] = {
            "openapi_name": "",
            "sdk_module": "",
            "created_by_us": False,
            "installed": False,
            # We will add "route" below
        }

    # Set the route flag
    registry[short_name]["route"] = present

    # Write back to disk
    REGISTRY_PATH.parent.mkdir(parents=True, exist_ok=True)
    REGISTRY_PATH.write_text(json.dumps(registry, indent=2), encoding="utf-8")

    console.print(f"[grey]→ Wrote 'route': {present} for '{short_name}' into {REGISTRY_PATH}[/grey]")


# ── util --------------------------------------------------------------------
def clear_screen() -> None:
    if sys.stdout.isatty():
        os.system("cls" if os.name == "nt" else "clear")

def list_definitions() -> list[str]:
    """
    Return a sorted list of all <platform>.json files under app/llm/function_definitions.
    Each name is the platform short name (i.e., filename without .json).
    """
    if not DEF_DIR.exists():
        return []
    return sorted(fp.stem for fp in DEF_DIR.glob("*.json"))


# ── main --------------------------------------------------------------------
def main() -> None:
    clear_screen()
    console.print(Panel.fit("🚀 Create Platform Route Wizard", style="green"))

    # 1) pick platform -------------------------------------------------------
    platforms = list_definitions()
    if not platforms:
        console.print("[red]No scaffolded platforms found.[/red]")
        sys.exit(1)

    tbl = Table(box=box.SIMPLE_HEAVY)
    tbl.add_column("#", style="bold cyan")
    tbl.add_column("Platform")
    for i, name in enumerate(platforms, 1):
        tbl.add_row(str(i), name)
    exit_idx = len(platforms) + 1
    tbl.add_row(str(exit_idx), "Exit")
    console.print(Panel(tbl, title="Step 1/3 – Select Platform", border_style="cyan"))

    choice = Prompt.ask(f"Enter number [1-{exit_idx}]", default=str(exit_idx)).strip()
    if not choice.isdigit():
        console.print("[yellow]Aborted.[/yellow]")
        sys.exit(0)
    idx = int(choice)
    if idx == exit_idx:
        console.print("[yellow]Aborted.[/yellow]")
        sys.exit(0)
    if not (1 <= idx <= len(platforms)):
        console.print("[red]Invalid selection.[/red]")
        sys.exit(1)
    platform = platforms[idx - 1]
    console.print(f":white_check_mark: Selected [bold]{platform}[/bold]\n")

    # 2) URL prefix ----------------------------------------------------------
    console.print(Panel.fit("🔧 Step 2/3 – Define URL Prefix", border_style="cyan"))
    default_prefix = f"/{platform}"
    prefix = Prompt.ask("Route URL prefix", default=default_prefix).strip()
    console.print(f":white_check_mark: Prefix set to [bold]{prefix}[/bold]\n")

    # 3) preview & confirm ---------------------------------------------------
    filename = f"{platform}_routes.py"
    target   = ROUTER_DIR / filename
    stub = (
        "from fastapi import APIRouter\n"
        "from app.llm.unified_service import UnifiedService\n\n"
        f'router = APIRouter(prefix="{prefix}", tags=["{platform}"])\n\n'
        "@router.get(\"/\")\n"
        f"async def get_{platform}_info():\n"
        f"    return UnifiedService.{platform}_info()\n"
    )
    console.print(
        Panel(
            f"Will create:\n[white]{target}[/white]\n\nStub:\n{stub}",
            title="Step 3/3 – Preview",
            border_style="cyan",
        )
    )
    if Prompt.ask("Proceed? (Y/n)", default="Y").lower().startswith("n"):
        console.print("[yellow]Aborted.[/yellow]")
        sys.exit(0)

    # 4) generate route file ------------------------------------------------
    ROUTER_DIR.mkdir(parents=True, exist_ok=True)
    target.write_text(stub, encoding="utf-8")
    console.print(f"[green]Created {target}[/green]")

    # 5) toggle registry flag ------------------------------------------------
    set_route_flag(platform, True)


    # 6) update routers/__init__.py (wrap import in try/except) -------------
    init_py = ROUTER_DIR / "__init__.py"
    safe_import = (
        f"try:\n"
        f"    from .{platform}_routes import router as {platform}_router\n"
        f"except ImportError:\n"
        f"    pass\n"
    )

    if not init_py.exists():
        init_py.write_text(safe_import, encoding="utf-8")
    else:
        lines = init_py.read_text(encoding="utf-8").splitlines(keepends=True)
        # If an import block for this platform is already present, skip
        marker = f"from .{platform}_routes import router as {platform}_router"
        if not any(marker in ln for ln in lines):
            # Append our try/except block at the end
            if lines:
                if not lines[-1].endswith("\n"):
                    lines[-1] += "\n"
            lines.append(safe_import)
            init_py.write_text("".join(lines), encoding="utf-8")
    console.print(f"[green]Updated {init_py}[/green]")
 
    console.print(Panel.fit(":white_check_mark: Done!", style="green"))

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[red]Interrupted.[/red]")
        sys.exit(1)
