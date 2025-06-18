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
║ A polished step‑by‑step CLI to run openapi‑python‑client for your specs.  ║
║                                                                           ║
║ FEATURES                                                                  ║
║   • Select a spec                                                         ║
║   • Suggest folder name from platform_registry.json                       ║
║   • Generate the SDK with poetry meta                                     ║
║   • Auto‑populate *sdk_module* in platform_registry.json                  ║
║     (but **does NOT touch the `installed` flag**)                         ║
║   • Show pip‑install instructions & import snippet                        ║
╚═══════════════════════════════════════════════════════════════════════════╝
"""

import os
import sys
import shlex
import subprocess
import json
import re
import tomllib
import shutil
from pathlib import Path
from typing import List, Dict, Optional

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

# ────────────────────────────────────────────────────────────────────────────────
# Constants
# ────────────────────────────────────────────────────────────────────────────────
PROJECT_ROOT           = Path(__file__).resolve().parents[3]  # repo root
SOURCE_DIR             = PROJECT_ROOT / "src" / "source_open_api"           # specs folder
OUTPUT_BASE_DIR        = PROJECT_ROOT / "src" / "db_scripts" / "output_sdk" # generated SDKs
SDK_MAP_FILE           = PROJECT_ROOT / "src" / "app" / "llm" / "sdk_map.json"
PLATFORM_REGISTRY_FILE = PROJECT_ROOT / "src" / "app" / "llm" / "platform_registry.json"

# ────────────────────────────────────────────────────────────────────────────────
# Helpers
# ────────────────────────────────────────────────────────────────────────────────

def clear_screen() -> None:
    if sys.stdout.isatty():
        os.system("cls" if os.name == "nt" else "clear")


def list_existing_sdks() -> List[str]:
    return sorted(p.name for p in OUTPUT_BASE_DIR.iterdir() if p.is_dir()) if OUTPUT_BASE_DIR.exists() else []


def list_specs() -> List[Path]:
    specs = sorted(p for p in SOURCE_DIR.iterdir() if p.is_file() and p.suffix.lower() in {".json", ".yaml", ".yml"})
    if not specs:
        console.print(f"[red]No OpenAPI files found in {SOURCE_DIR}[/red]")
        sys.exit(1)
    return specs


def ask_choice(prompt: str, default: str) -> str:
    return Prompt.ask(f"[cyan]?[/cyan] [bold]{prompt}[/bold]", default=default).strip()


def sanitize_sdk_name(name: str) -> str:
    sanitized = re.sub(r"[^0-9a-zA-Z_]+", "_", name).lower()
    sanitized = re.sub(r"_+", "_", sanitized).strip("_")
    return sanitized or "sdk"


def build_command(spec: Path, sdk_name: str, package_name: str) -> List[str]:
    dest = OUTPUT_BASE_DIR / sdk_name
    dest.mkdir(parents=True, exist_ok=True)
    return [
        "openapi-python-client", "generate",
        "--path", str(spec),
        "--output-path", str(dest),
        "--meta", "poetry",
        "--overwrite",
        "--package-name", package_name,
    ]


def parse_package_dir(dest_dir: Path, fallback: str) -> str:
    pyproject = dest_dir / "pyproject.toml"
    if pyproject.exists():
        try:
            data = tomllib.loads(pyproject.read_text(encoding="utf-8"))
            poetry = data.get("tool", {}).get("poetry", {})
            packages = poetry.get("packages")
            if isinstance(packages, list) and packages:
                inc = packages[0].get("include") if isinstance(packages[0], dict) else None
                if inc:
                    return inc.replace("-", "_")
            name = poetry.get("name") or data.get("project", {}).get("name")
            if isinstance(name, str):
                return name.replace("-", "_")
        except Exception:
            pass
    for p in dest_dir.iterdir():
        if p.is_dir() and (p / "__init__.py").exists():
            return p.name.replace("-", "_")
    return fallback.replace("-", "_")


def load_registry() -> Dict[str, Dict[str, str]]:
    try:
        return json.loads(PLATFORM_REGISTRY_FILE.read_text(encoding="utf-8"))
    except Exception:
        return {}


def save_registry(reg: Dict[str, Dict[str, str]]) -> None:
    PLATFORM_REGISTRY_FILE.parent.mkdir(parents=True, exist_ok=True)
    PLATFORM_REGISTRY_FILE.write_text(json.dumps(reg, indent=2), encoding="utf-8")


def registry_short_name_for_spec(spec: Path, registry: Dict[str, Dict[str, str]]) -> Optional[str]:
    stem = spec.stem.lower()
    for short_name, entry in registry.items():
        if stem == str(entry.get("openapi_name", "")).lower():
            return short_name
    return None

# ────────────────────────────────────────────────────────────────────────────────
# Main CLI
# ────────────────────────────────────────────────────────────────────────────────

def main() -> None:
    if shutil.which("openapi-python-client") is None:
        console.print(
            "[red]`openapi-python-client` is not installed. "
            "Install it with `pip install openapi-python-client` and try again.[/red]"
        )
        sys.exit(1)
    clear_screen()
    console.print(Panel.fit("🚀 OpenAPI SDK Generation Wizard", style="green"))

    # Show existing SDKs
    console.print(Panel(
        ", ".join(list_existing_sdks()) or "(none)",
        title="Existing SDKs in output_sdk/",
        border_style="magenta",
    ))

    # Step 1 – pick spec
    specs = list_specs()
    table = Table(box=box.SIMPLE_HEAVY)
    table.add_column("#", style="bold cyan")
    table.add_column("Spec file")
    for i, path in enumerate(specs, 1):
        table.add_row(str(i), path.name)
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

    # Step 2 – folder name (default from registry if available)
    registry = load_registry()
    default_sdk_name = registry_short_name_for_spec(spec, registry) or ""
    console.print(Panel.fit(
        "🔧 Step 2/4: Name Your SDK Folder" + (f"\n[dim](suggested: {default_sdk_name})[/dim]" if default_sdk_name else ""),
        border_style="cyan",
    ))
    sdk_name = Prompt.ask("[cyan]?[/cyan] [bold]Enter a short SDK folder name[/bold]", default=default_sdk_name).strip()
    if not sdk_name:
        console.print("[red]You must enter a non-empty SDK name. Exiting.[/red]")
        sys.exit(1)
    package_name = sanitize_sdk_name(sdk_name)
    console.print(":white_check_mark: Name set\n")

    # Step 3 – preview command
    cmd = build_command(spec, sdk_name, package_name)
    console.print(Panel(Markdown(f"**Command to run**\n```bash {' '.join(shlex.quote(p) for p in cmd)} ```"), title="Step 3/4: Preview Command", border_style="cyan"))
    if ask_choice("Proceed with SDK generation? (Y/n)", "Y").lower().startswith("n"):
        console.print("[yellow]Aborted by user.[/yellow]")
        return

    # Step 4 – run generator
    console.print(Panel.fit("🛠 Generating SDK…", style="cyan"))
    if subprocess.run(cmd).returncode != 0:
        console.print(f"[red]Generation failed for {spec.name}[/red]")
        sys.exit(1)
    console.print(f"[green]Success for {spec.name} → {sdk_name}[/green]\n")

    # Show tree of output_sdk
    tree = Tree(f"[bold]{OUTPUT_BASE_DIR.name}[/bold]")
    for d in sorted(OUTPUT_BASE_DIR.iterdir()):
        if d.is_dir():
            br = tree.add(d.name)
            for child in sorted(d.iterdir()):
                br.add(child.name)
    console.print(tree)



    # Determine package directory name via pyproject.toml
    pkg_dir = parse_package_dir(OUTPUT_BASE_DIR / sdk_name, sdk_name)



 
    # ---------------------------------------------------------------------
    # Update platform_registry.json (without touching 'installed')
    # ---------------------------------------------------------------------
    short_name = registry_short_name_for_spec(spec, registry) or sdk_name
    entry = registry.get(short_name, {})
    entry["openapi_name"] = spec.stem
    entry["sdk_module"] = pkg_dir
    entry["created_by_us"] = True
    # Note: we intentionally leave the 'installed' flag unchanged.
    registry[short_name] = entry
    save_registry(registry)
    console.print(f"[green]Registry updated: {short_name} → sdk_module={pkg_dir}[/green]")

    # ---------------------------------------------------------------------
    # Show install instructions & usage snippet
    # ---------------------------------------------------------------------
    console.print(Panel.fit("📦 Install into your environment:", style="cyan"))
    abs_dest = (OUTPUT_BASE_DIR / sdk_name).resolve()
    console.print(Markdown(f"```bash pip install -e {abs_dest} ```"))

    console.print(Panel.fit("👉 Usage in your Python code:", style="cyan"))
    console.print(Markdown(f"```python\nimport {pkg_dir} \n```"))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[red]Interrupted by user.[/red]")
        sys.exit(1)