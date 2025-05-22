#!/usr/bin/env python3
from __future__ import annotations
################################################################################
## AI-Building-Blocks-Agent/tools/create_platform.py
## Copyright (c) 2025 Jeff Teeter
## Cisco Systems, Inc.
## Licensed under the Apache License, Version 2.0 (see LICENSE)
## Distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND.
################################################################################

"""
╔════════════════════════ Unified Platform Scaffolder Wizard ════════════════════════╗
║ A step-by-step CLI tool to generate AI agent scaffolding with a polished UX.      ║
║ Hover over links or type '?' at prompts for examples.                             ║
║                                                                                   ║
║ OUTPUT                                                                            ║
║   • app/llm/function_definitions/<platform>.json                                  ║
║   • app/llm/openapi_specs/full_<platform>.json                                    ║
║   • app/llm/platform_clients/<platform>_client.py                                 ║
║   • app/llm/function_dispatcher/<platform>_dispatcher.py                          ║
║   • app/llm/unified_service/<platform>_service.py                                 ║
║                                                                                   ║
║ PREREQUISITES                                                                     ║
║   • Install SDK (pip) or ensure PYTHONPATH includes your SDK module.               ║
║   • Provide a valid JSON/YAML OpenAPI spec.                                       ║
║   • If a workflow diagram exists, it will open externally for review.              ║
╚═══════════════════════════════════════════════════════════════════════════════════╝
"""

import argparse
import subprocess
import sys
import os
import re
import webbrowser
import shlex
import json
from datetime import datetime
from pathlib import Path
from itertools import chain
from typing import List, Optional, Tuple

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt
from rich.markdown import Markdown
from rich import box
from rich.traceback import install

install()
console = Console()

# Paths
AGENT_ROOT = Path(__file__).resolve().parents[1]
SPEC_DIR = AGENT_ROOT.parent / "ai-building-blocks-database" / "source_open_api"
if str(AGENT_ROOT) not in sys.path:
    sys.path.insert(0, str(AGENT_ROOT))

# SDK list file for platform choices
SDK_LIST_FILE = AGENT_ROOT / "app" / "llm" / "sdk_list.json"
try:
    sdk_list = json.loads(SDK_LIST_FILE.read_text(encoding="utf-8"))
except Exception:
    sdk_list = []

# Validation patterns
VALID_PLATFORM_RX = re.compile(r"^[a-z][a-z0-9_]*$")
VALID_VERBS = {"GET","POST","PUT","PATCH","DELETE","HEAD","OPTIONS"}

# Example links and diagram
EXAMPLE_LINK = "https://example.com/create-platform-examples"
DIAGRAM_PATH = AGENT_ROOT / "docs" / "create_platform_flow.png"

# Helpers

def clear_screen() -> None:
    if sys.stdout.isatty():
        os.system("cls" if os.name == "nt" else "clear")


def ask(prompt: str, default: Optional[str] = None) -> str:
    """Prompt user; '?' shows examples link. Accepts blank if default is provided."""
    while True:
        resp = Prompt.ask(f"[cyan]?[/cyan] [bold]{prompt}[/bold]", default=default)
        if resp.strip() == "?":
            console.print(Markdown(f"[See examples here]({EXAMPLE_LINK})"))
            try:
                webbrowser.open(EXAMPLE_LINK)
            except Exception:
                pass
            continue
        val = resp.strip()
        if default is not None:
            return val
        if val:
            return val
        console.print("[red]→ Please enter a value.[/red]\n")


def pick_spec() -> str:
    console.print(Panel.fit("Step 2/4: Choose OpenAPI spec", style="cyan"))
    specs = sorted(chain(SPEC_DIR.glob("*.json"), SPEC_DIR.glob("*.yaml"), SPEC_DIR.glob("*.yml")))
    table = Table(box=box.SIMPLE_HEAVY)
    table.add_column("#", style="bold cyan")
    table.add_column("File")
    table.add_column("Size (KB)", justify="right")
    table.add_column("Modified")
    for i, fp in enumerate(specs, 1):
        table.add_row(
            str(i), fp.name,
            str(fp.stat().st_size // 1024),
            datetime.fromtimestamp(fp.stat().st_mtime).strftime("%Y-%m-%d"),
        )
    console.print(table)
    choice = ask("Select spec number", "1")
    if choice.isdigit() and (idx := int(choice)) > 0 and idx <= len(specs):
        return str(specs[idx-1])
    return ask("Enter path to OpenAPI spec", None)


def preview_table(rows: List[Tuple[str, str]]) -> None:
    """Display a preview table with rounded borders."""
    table = Table(box=box.ROUNDED, padding=(0, 1))
    table.add_column(justify="right", style="bold green", no_wrap=True)
    table.add_column()
    for key, value in rows:
        table.add_row(f"{key}:", value)
    console.print(Panel(table, title="Preview Configuration", border_style="cyan"))

# Main flow

def main() -> None:
    clear_screen()
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--dry-run", action="store_true")
    args, _ = parser.parse_known_args()

    console.print(Panel.fit("🛠 Welcome to the Unified Platform Scaffolder Wizard", style="green"))

    # Step 1/4: Platform identifier
    console.print(Panel.fit("Step 1/4: Platform identifier", style="cyan"))
    if sdk_list:
        table = Table(box=box.SIMPLE)
        table.add_column("#", style="bold cyan")
        table.add_column("Platform")
        for i, name in enumerate(sdk_list, start=1):
            table.add_row(str(i), name)
        console.print(table)
        while True:
            choice = ask("Select platform number or enter custom", None)
            if choice.isdigit() and 1 <= (idx := int(choice)) <= len(sdk_list):
                platform = sdk_list[idx-1]
                break
            if not choice.isdigit():
                platform = choice
                break
            console.print("[red]→ Invalid selection.[/red]")
    else:
        platform = ask("Enter platform (e.g., meraki)", None)

    while not VALID_PLATFORM_RX.match(platform):
        console.print("[red]→ Invalid platform. Use lowercase letters, digits, and underscores.[/red]")
        platform = ask("Enter platform (e.g., meraki)", None)
    console.print(f":white_check_mark: Platform set to [bold]{platform}[/bold]\n")
    is_new = platform not in sdk_list

    # Step 1b/4: SDK module import path with choice
    console.print(Panel.fit("Step 1b/4: SDK module import path", style="cyan"))
    options = [platform, f"{platform}.session"]
    table = Table(box=box.SIMPLE)
    table.add_column("#", style="bold cyan")
    table.add_column("Module")
    for i, mod in enumerate(options, start=1):
        table.add_row(str(i), mod)
    console.print(table)
    while True:
        sel = ask("Select module number or enter custom", None)
        if sel.isdigit() and 1 <= (idx := int(sel)) <= len(options):
            sdk_module = options[idx-1]
            break
        if not sel.isdigit():
            sdk_module = sel
            break
        console.print("[red]→ Invalid selection.[/red]")
    console.print(f":white_check_mark: SDK module set to [bold]{sdk_module}[/bold]\n")

    # Step 2/4: OpenAPI spec
    spec_file = pick_spec()
    console.print(f":white_check_mark: Using spec [bold]{Path(spec_file).name}[/bold]\n")

    # Step 3/4: HTTP verbs
    console.print(Panel.fit("Step 3/4: Configure HTTP verbs", style="cyan"))
    verbs = ask("HTTP verbs (comma-separated, blank=ALL)", "GET").upper()
    cleaned = [v.strip() for v in verbs.split(",") if v.strip() in VALID_VERBS]
    console.print(f":white_check_mark: Verbs = [bold]{', '.join(cleaned) or 'ALL'}[/bold]\n")

    # Step 4/4: Regex filter
    console.print(Panel.fit("Step 4/4: Regex filter for operationIds", style="cyan"))
    name_re = ask("Regex filter (blank=none)", "").strip()
    console.print(f":white_check_mark: Regex filter = [bold]{name_re or 'None'}[/bold]\n")

    # Preview all choices
    preview_table([
        ("Platform", platform),
        ("SDK module", sdk_module),
        ("Spec file", Path(spec_file).name),
        ("HTTP verbs", ', '.join(cleaned) or "ALL"),
        ("Name regex", name_re or "None"),
    ])

    if DIAGRAM_PATH.exists():
        console.print(Panel.fit("Workflow diagram available at:", border_style="cyan"))
        console.print(f"[cyan]file://{DIAGRAM_PATH}[/cyan]")

    # Build command to invoke platform_scaffolder
    cmd = [
        sys.executable,
        str(AGENT_ROOT / "scripts" / "platform_scaffolder.py"),
        "--platform", platform,
        "--sdk-module", sdk_module,
        "--openapi-spec", spec_file,
    ]
    if cleaned:
        cmd += ["--include-http-methods", ''.join(cleaned)]
    if name_re:
        cmd += ["--name-pattern", name_re]
    cmd_str = ' '.join(shlex.quote(c) for c in cmd)
    console.print(Panel(Markdown(f"**Command to run**\n```bash\n{cmd_str}\n```"), border_style="cyan"))

    # Confirm and execute
    if args.dry_run or ask("Proceed? (Y/n)", "Y").lower().startswith("n"):
        console.print("[yellow]Aborted by user.[/yellow]")
        return

    console.print(Panel.fit("🚀 Running scaffolder...", style="cyan"))
    env = os.environ.copy()
    env["PYTHONPATH"] = f"{AGENT_ROOT}:{env.get('PYTHONPATH','')}"
    subprocess.run(cmd, check=True, env=env)

    # Append new platform to sdk_list.json
    if is_new:
        try:
            sdk_list.append(platform)
            SDK_LIST_FILE.parent.mkdir(parents=True, exist_ok=True)
            SDK_LIST_FILE.write_text(json.dumps(sdk_list, indent=2), encoding="utf-8")
            console.print(f"[green]Added '{platform}' to SDK list.[/green]")
        except Exception as e:
            console.print(f"[red]Failed to update SDK list: {e}[/red]")

    console.print(Panel.fit(":white_check_mark: Scaffolding complete!", style="green"))

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[red]Interrupted by user.[/red]")
