#!/usr/bin/env python3
from __future__ import annotations
################################################################################
## suite-cisco-ai-building-blocks/src/app/user_commands/create_platform_index.py
## Copyright (c) 2025 Jeff Teeter
## Cisco Systems, Inc.
## Licensed under the Apache License, Version 2.0 (see LICENSE)
## Distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND.
################################################################################

"""
╔════════════════════════ Platform Indexer Wizard ═════════════════════════════════╗
║ A polished step-by-step CLI to run the index_functions script without the flags. ║
║ Hover over links or type '?' at prompts for examples.                            ║
║                                                                                  ║
║ FEATURES                                                                          ║
║   • Select a single existing platform, index ALL platforms, or exit              ║
║   • Automatically configures PYTHONPATH                                            ║
║   • Shows the SDK module behind each platform                                      ║
║   • Displays current vector-store collections and actual indexed platforms         ║
║   • Reads FASTAPI_* environment settings from .env                                 ║
║   • Highlights the active backend first                                           ║
║   • Shows the exact command in a copyable block                                   ║
"""
 

import os
import sys
import shlex
import requests
import subprocess
import json
from pathlib import Path
from typing import List, Optional
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table
from rich.markdown import Markdown
from rich import box
from rich.traceback import install
from app.retrievers.azure_search_retriever import AzureSearchRetriever
from app.utils.paths import ensure_abs_env, REPO_ROOT as UTIL_REPO_ROOT
from app.user_commands.update_platform_registry import load_registry  # <— new import
from dotenv import load_dotenv

load_dotenv()

# ── directory layout fixup ─────────────────────────────────────────────────────
REPO_ROOT   = UTIL_REPO_ROOT
SRC_ROOT    = ensure_abs_env("SRC_ROOT", "src")
AGENT_ROOT  = ensure_abs_env("AGENT_ROOT", "src/app")

# load registry & build sdk_map
registry = load_registry()
sdk_map  = { name: entry.get("sdk_module", "<unknown>") for name, entry in registry.items() }

LLM_DEF_DIR    = ensure_abs_env(
    "PLATFORM_LLM_DEF_DIR",
    "src/app/llm/function_definitions"
)
INDEXER_SCRIPT = ensure_abs_env(
    "INDEXER_PATH",
    "src/scripts/index_functions.py"
)

if str(AGENT_ROOT) not in sys.path:
    sys.path.insert(0, str(AGENT_ROOT))

install()
console = Console()


def clear_screen() -> None:
    if sys.stdout.isatty():
        os.system("cls" if os.name == "nt" else "clear")


def list_definitions() -> List[str]:
    return sorted(fp.stem for fp in LLM_DEF_DIR.glob("*.json"))


def ask_choice(prompt: str, default: Optional[str] = None) -> str:
    return Prompt.ask(f"[cyan]?[/cyan] [bold]{prompt}[/bold]", default=default).strip()


def build_command(platform: Optional[str]) -> List[str]:
    if platform:
        return [sys.executable, str(INDEXER_SCRIPT), "--platform", platform]
    return [sys.executable, str(INDEXER_SCRIPT), "--all"]


def azure_list_platforms() -> List[str]:
    idx = os.getenv("FASTAPI_AZURE_PLATFORM_INDEX", "")
    endpoint = os.getenv("FASTAPI_AZURE_ENDPOINT", "")
    api_ver = os.getenv("FASTAPI_AZURE_API_VERSION", "2024-11-01-preview")
    key = os.getenv("FASTAPI_AZURE_KEY", "")

    if not idx or not endpoint or not key:
        return []

    url = f"{endpoint}/indexes/{idx}/docs/search?api-version={api_ver}"
    payload = {"search": "*", "facets": ["platform,count:1000"], "top": 0}
    try:
        resp = requests.post(
            url,
            headers={"api-key": key, "Content-Type": "application/json"},
            json=payload,
            timeout=30,
        )
        resp.raise_for_status()
        facets = resp.json().get("@search.facets", {}).get("platform", [])
        return sorted(f["value"] for f in facets if f.get("value"))
    except Exception:
        return []


def main() -> None:
    clear_screen()
    console.print(Panel.fit("🛠 Welcome to the Platform Indexer Wizard", style="green"))

    backends = ["chroma", "azure", "elastic"]
    active = os.getenv("FASTAPI_VECTOR_BACKEND", "chroma").lower()
    ordered = [active] + [b for b in backends if b != active]

    for be in ordered:
        is_active = (be == active)
        title = f"{be.capitalize()} Backend" + (" (active)" if is_active else "")
        collections: List[str] = []
        indexed:    List[str] = []

        if be == "chroma":
            col = os.getenv("FASTAPI_CHROMA_COLLECTION_PLATFORM", "")
            if col:
                collections.append(col)
                from app.user_commands.update_platform_registry import load_registry as _;
                # reuse registry for chroma listing if needed
                indexed = list_definitions()
        elif be == "azure":
            col = os.getenv("FASTAPI_AZURE_PLATFORM_INDEX", "")
            if col:
                collections.append(col)
                indexed = azure_list_platforms()
        else:
            col = os.getenv("FASTAPI_ELASTIC_PLATFORM_INDEX", "")
            if col:
                collections.append(col)
                indexed = []

        coll_txt = ", ".join(collections) or "(none)"
        idx_txt  = ", ".join(indexed)    or "(none)"
        style    = "yellow" if is_active else "magenta"

        console.print(
            Panel(
                f"[magenta]{coll_txt}[/magenta]\n\n[yellow]Platforms indexed:[/yellow] {idx_txt}",
                title=title,
                border_style=style
            )
        )

    platforms = list_definitions()
    if not platforms:
        console.print("[red]No platform definitions found; please scaffold first.[/red]")
        sys.exit(1)

    menu = Table(box=box.SIMPLE_HEAVY)
    menu.add_column("#", style="bold cyan")
    menu.add_column("Platform")
    menu.add_column("SDK Module")
    for i, name in enumerate(platforms, start=1):
        menu.add_row(str(i), name, sdk_map.get(name, "<unknown>"))

    all_i  = len(platforms) + 1
    exit_i = len(platforms) + 2
    menu.add_row(str(all_i),  "All Platforms", "-")
    menu.add_row(str(exit_i), "Exit",          "-")

    console.print(Panel(menu, title="Step 1/3: Select Platform to Index", border_style="cyan"))

    choice = ask_choice(f"Enter number [1-{exit_i}] (or 'all'/'exit')", "all")
    if choice.lower() in ("all", str(all_i)):
        sel = None
    elif choice.lower() in ("exit", str(exit_i)):
        console.print("[green]Exiting...[/green]")
        sys.exit(0)
    elif choice.isdigit() and 1 <= (n := int(choice)) <= len(platforms):
        sel = platforms[n - 1]
    else:
        console.print(f"[red]Invalid selection: {choice}[/red]")
        sys.exit(1)

    console.print(f":white_check_mark: Selected [bold]{sel or 'All'}[/bold]\n")

    parts = build_command(sel)
    cmd = " ".join(shlex.quote(p) for p in parts)
    console.print(
        Panel(
            Markdown(f"**Command to run**\n```bash\n{cmd}\n```"),
            border_style="cyan",
            title="Step 2/3: Preview Command"
        )
    )
    if ask_choice("Proceed with indexing? (Y/n)", "Y").lower().startswith("n"):
        console.print("[yellow]Aborted by user.[/yellow]")
        return

    console.print(Panel.fit("🚀 Running indexer...", style="cyan"))
    env = os.environ.copy()
    env["PYTHONPATH"] = f"{AGENT_ROOT}:{env.get('PYTHONPATH','')}"
    subprocess.run(parts, check=True, env=env, cwd=str(SRC_ROOT))
    console.print(Panel.fit(":white_check_mark: Indexing complete!", style="green"))

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[red]Interrupted by user.[/red]")
        sys.exit(1)


