#!/usr/bin/env python3
from __future__ import annotations
##########################################################################################
## suite-cisco-ai-building-blocks/src/app/user_commands/reset_platform.py
## Copyright (c) 2025 Jeff Teeter, Ph.D.
## Cisco Systems, Inc.
## Licensed under the Apache License, Version 2.0 (see LICENSE)
## Distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND.
##########################################################################################

"""
╔════════════════════════ Unified Platform Reset Wizard ═════════════════════════╗
║ A step-by-step CLI to wipe or remove specific platform artifacts in the AI     ║
║ agent's auto-generated LLM folders.                                            ║
║                                                                                ║
║ OPTIONS                                                                        ║
║   • All   → delete all platform artifacts and mark all as uninstalled.         ║
║   • One   → remove a single platform's artifacts and mark it uninstalled.      ║
║   • Exit  → quit without making changes.                                       ║
╚═══════════════════════════════════════════════════════════════════════════════╝
"""
import argparse
import json
import os
import sys
from pathlib import Path
from typing import List

from rich import box
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table
from rich.traceback import install

# ──────────────────────────────────────────────────────────────────────
# rich setup + utils
# ──────────────────────────────────────────────────────────────────────
install()
console = Console()


def clear_screen() -> None:
    if sys.stdout.isatty():
        os.system("cls" if os.name == "nt" else "clear")


# ──────────────────────────────────────────────────────────────────────
# repo bootstrap
# ──────────────────────────────────────────────────────────────────────
AGENT_ROOT = Path(__file__).resolve().parents[1]
if str(AGENT_ROOT) not in sys.path:
    sys.path.insert(0, str(AGENT_ROOT))

from scripts.reset_automated_folders import FOLDERS_TO_RESET, reset_folders  # noqa: E402

# Path to platform_registry.json (the same file create_platform uses)
REGISTRY_PATH = AGENT_ROOT / "llm" / "platform_registry.json"


# ╭─────────────────────────────────────────────────────────────────────╮
# │ 1 ─ dynamic registry rebuild (unified_service/__init__.py)         │
# ╰─────────────────────────────────────────────────────────────────────╯
def _rebuild_service_registry(dry_run: bool = False) -> None:
    """Re-create app/llm/unified_service/__init__.py after deletions."""
    service_dir = AGENT_ROOT / "llm" / "unified_service"
    init_py = service_dir / "__init__.py"

    service_files = sorted(service_dir.glob("*_service.py"))
    imports: List[str] = []
    reg_lines: List[str] = []
    all_exports: List[str] = ["UnifiedService"]

    for fp in service_files:
        plat = fp.stem.replace("_service", "")
        cls = f"{plat.capitalize()}ServiceClient"
        imports.append(f"from .{plat}_service import {cls}")
        reg_lines.append(f"    '{plat}': {cls},")
        all_exports.append(cls)

    # Generate import statements (one per line)
    import_lines = chr(10).join(imports) if imports else ''
    
    init_code = f"""# Auto-generated – DO NOT EDIT
from __future__ import annotations
import sys
{import_lines}

_SERVICE_REGISTRY = {{
{chr(10).join(reg_lines)}
}}

class UnifiedService:  # pylint: disable=too-few-public-methods
    \"\"\"Return the correct *ServiceClient for *platform*.\"\"\"
    def __new__(cls, platform: str, *args, **kwargs):  # noqa: D401
        try:
            impl = _SERVICE_REGISTRY[platform.lower()]
        except KeyError as exc:  # pragma: no cover
            raise ValueError(
                f"Unsupported platform '{{platform}}'. "
                f"Valid options: {{', '.join(_SERVICE_REGISTRY)}}"
            ) from exc
        return impl(*args, **kwargs)

__all__ = {all_exports!r}

# optional top-level alias
sys.modules.setdefault("unified_service", sys.modules[__name__])
"""
    
    # Validate the generated code is valid Python syntax
    try:
        compile(init_code, str(init_py), 'exec')
    except SyntaxError as e:
        console.print(f"[red]Error: Generated code has syntax error at line {e.lineno}:[/red]")
        console.print(f"[red]{e.msg}[/red]")
        console.print("[yellow]Generated code:[/yellow]")
        console.print(init_code)
        raise
    
    if dry_run:
        console.print(f"[yellow]Dry run - would write to {init_py.relative_to(AGENT_ROOT)}:[/yellow]")
        console.print(Panel(init_code, title="Generated Code", border_style="yellow"))
    else:
        init_py.write_text(init_code, encoding="utf-8")
        console.print(f"[green]✓ Rebuilt {init_py.relative_to(AGENT_ROOT)}[/green]")


# ╭─────────────────────────────────────────────────────────────────────╮
# │ 2 ─ registry helpers to clear "installed"                        │
# ╰─────────────────────────────────────────────────────────────────────╯
def _load_registry_dict() -> dict:
    """Load the JSON registry as a Python dict; return empty dict if missing/invalid."""
    if not REGISTRY_PATH.exists():
        return {}
    try:
        return json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        console.print(f"[red]Error:[/red] Failed to parse {REGISTRY_PATH}.")
        sys.exit(1)


def _save_registry_dict(data: dict) -> None:
    """Write the given dict back to platform_registry.json."""
    REGISTRY_PATH.write_text(json.dumps(data, indent=2), encoding="utf-8")


def clear_installed_flag(short_name: str) -> None:
    """
    Load platform_registry.json, set 'installed': false for this entry,
    then write back.
    """
    reg = _load_registry_dict()
    if short_name in reg and reg[short_name].get("installed", False):
        reg[short_name]["installed"] = False
        _save_registry_dict(reg)


def clear_all_installed_flags() -> None:
    """
    Set 'installed': false for every entry in platform_registry.json.
    """
    reg = _load_registry_dict()
    changed = False
    for key in reg:
        if reg[key].get("installed", False):
            reg[key]["installed"] = False
            changed = True
    if changed:
        _save_registry_dict(reg)


# ╭─────────────────────────────────────────────────────────────────────╮
# │ 3 ─ helpers for CLI display                                        │
# ╰─────────────────────────────────────────────────────────────────────╯
def get_platforms() -> list[str]:
    """
    Return a sorted list of platforms that have a <platform>_client.py in app/llm/platform_clients.
    """
    clients_dir = AGENT_ROOT / "llm" / "platform_clients"
    return sorted(
        fp.stem[: -len("_client")]
        for fp in clients_dir.glob("*_client.py")
        if fp.stem.endswith("_client")
    )


def display_platforms(platforms: list[str]) -> None:
    """
    Show a table of platforms + “All” + “Exit” for resetting.
    """
    table = Table(box=box.SIMPLE)
    table.add_column("#", style="bold cyan", no_wrap=True)
    table.add_column("Platform")
    for idx, name in enumerate(platforms, start=1):
        table.add_row(str(idx), name)
    table.add_row(str(len(platforms) + 1), "All")
    table.add_row(str(len(platforms) + 2), "Exit")
    console.print(Panel(table, title="Select Platform to Reset", border_style="green"))


# ╭─────────────────────────────────────────────────────────────────────╮
# │ 4 ─ main flow                                                      │
# ╰─────────────────────────────────────────────────────────────────────╯
def main() -> None:
    clear_screen()
    parser = argparse.ArgumentParser(description="Reset AI agent LLM folders.")
    parser.add_argument("--dry-run", action="store_true", help="Show actions only.")
    args = parser.parse_args()

    platforms = get_platforms()
    if not platforms:
        console.print("[yellow]No platforms found. Resetting all folders.[/yellow]")
        if not args.dry_run:
            reset_folders(FOLDERS_TO_RESET)
            _rebuild_service_registry(dry_run=args.dry_run)
            clear_all_installed_flags()
        return

    display_platforms(platforms)

    # allow empty input (just Enter) to exit gracefully
    choice = Prompt.ask(f"Enter choice [1-{len(platforms)+2}]", default="")
    if not choice.strip():
        console.print("[cyan]No selection made. Exiting without changes.[/cyan]")
        sys.exit(0)
    try:
        sel = int(choice)
    except ValueError:
        console.print(f"[red]Invalid selection: {choice}[/red]")
        sys.exit(1)

    # ── Exit ───────────────────────────────────────────────────────
    if sel == len(platforms) + 2:
        console.print("[cyan]Exiting without changes.[/cyan]")
        sys.exit(0)

    # ── Reset ALL ──────────────────────────────────────────────────
    if sel == len(platforms) + 1:
        console.print(Panel.fit("Resetting [bold]ALL[/bold] platform artifacts.", style="cyan"))
        if not args.dry_run:
            reset_folders(FOLDERS_TO_RESET)
            _rebuild_service_registry(dry_run=args.dry_run)
            clear_all_installed_flags()
        else:
            console.print("[yellow]Dry run: no changes applied.[/yellow]")
        return

    # ── Reset ONE ──────────────────────────────────────────────────
    if 1 <= sel <= len(platforms):
        plat = platforms[sel - 1]
        console.print(Panel.fit(f"Removing artifacts for [bold]{plat}[/bold].", style="cyan"))
        if args.dry_run:
            console.print("[yellow]Dry run: no changes applied.[/yellow]")
            return

        # 1) Delete the autogenerated files for this platform
        for folder in FOLDERS_TO_RESET:
            rel = folder.relative_to(AGENT_ROOT)
            name = folder.name

            if name == "platform_clients":
                target_files = [folder / f"{plat}_client.py"]
            elif name == "function_definitions":
                target_files = [folder / f"{plat}.json"]
            elif name == "openapi_specs":
                target_files = [folder / f"{plat}.json", folder / f"full_{plat}.json"]
            elif name == "function_dispatcher":
                target_files = [folder / f"{plat}_dispatcher.py"]
            elif name == "unified_service":
                target_files = [folder / f"{plat}_service.py"]
            else:
                target_files = []

            for target in target_files:
                desc = f"{rel}/{target.name}"
                if target.exists():
                    console.print(f"Deleting → {desc}")
                    target.unlink()
                else:
                    console.print(f"Not found → {desc}")

        # 2) Rebuild __init__.py for unified_service
        _rebuild_service_registry(dry_run=args.dry_run)

        # 3) Clear the 'installed' flag for this single platform
        clear_installed_flag(plat)

        console.print(f"[green]✓ Platform '{plat}' artifacts removed and marked uninstalled.[/green]")
        return

    console.print(f"[red]Selection out of range: {sel}[/red]")
    sys.exit(1)


if __name__ == "__main__":  # pragma: no cover
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[red]Interrupted by user.[/red]")
        sys.exit(1)
