#!/usr/bin/env python3
from __future__ import annotations
###########################################################################################
## suite-cisco-ai-building-blocks/ai-building-blocks-agent/user_commands/create_platform.py
## Copyright (c) 2025 Jeff Teeter, Ph.D.
## Cisco Systems, Inc.
## Licensed under the Apache License, Version 2.0 (see LICENSE)
## Distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND.
###########################################################################################

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
║ FEATURES                                                                          ║
║   • Select an existing platform or create a new one                                 ║
║   • Option to Exit at any time                                                     ║
║   • Automatically detects SDK module import path                                    ║
║   • Validates platform names and regex filters                                     ║
║   • Polished table previews and workflow diagram link                              ║
╚═══════════════════════════════════════════════════════════════════════════════════╝
"""

import argparse
import subprocess
import sys
import os
import re
import webbrowser
import json
import shlex
from datetime import datetime
from pathlib import Path
from itertools import chain
from typing import Dict, List, Optional, Tuple

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
# Ensure our agent root is on PYTHONPATH for sdk_loader
if str(AGENT_ROOT) not in sys.path:
    sys.path.insert(0, str(AGENT_ROOT))
SPEC_DIR = PROJECT_ROOT      / "src"                           / "source_open_api"

# Internal loader
from scripts.utils.sdk_loader import load_client

# SDK map for platform → sdk_module
SDK_MAP_FILE = AGENT_ROOT / "app" / "llm" / "sdk_map.json"
try:
    sdk_map: Dict[str, str] = json.loads(SDK_MAP_FILE.read_text(encoding="utf-8"))
except Exception:
    sdk_map = {}

# Validation patterns
VALID_PLATFORM_RX = re.compile(r"^[a-z][a-z0-9_]*$")
VALID_VERBS = {"GET","POST","PUT","PATCH","DELETE","HEAD","OPTIONS"}

# Example links
EXAMPLE_LINK = "https://example.com/create-platform-examples"
DIAGRAM_PATH = AGENT_ROOT / "docs" / "create_platform_flow.png"

# Helpers

def clear_screen() -> None:
    if sys.stdout.isatty():
        os.system("cls" if os.name == "nt" else "clear")


def ask(prompt: str, default: Optional[str] = None) -> str:
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
        if default is not None or val:
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
    if choice.isdigit() and 1 <= (idx := int(choice)) <= len(specs):
        return str(specs[idx-1])
    return ask("Enter path to OpenAPI spec", None)

def preview_table(rows: List[Tuple[str, str]]) -> None:
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

    # Show existing platforms
    existing = set()
    llm_base = AGENT_ROOT / "app" / "llm"
    scan_cfg = {
        "function_definitions": {"ext": ".json", "prefix": "", "suffix": ""},
        "openapi_specs":      {"ext": ".json", "prefix": "full_", "suffix": ""},
        "platform_clients":   {"ext": ".py",   "prefix": "",      "suffix": "_client"},
        "function_dispatcher": {"ext": ".py",   "prefix": "",      "suffix": "_dispatcher"},
        "unified_service":     {"ext": ".py",   "prefix": "",      "suffix": "_service"},
    }
    for folder, cfg in scan_cfg.items():
        path = llm_base / folder
        if not path.exists():
            continue
        for fp in path.glob(f"*{cfg['ext']}"):
            name = fp.stem
            if name == "__init__":
                continue
            if cfg['prefix'] and name.startswith(cfg['prefix']):
                name = name[len(cfg['prefix']):]
            if cfg['suffix'] and name.endswith(cfg['suffix']):
                name = name[:-len(cfg['suffix'])]
            existing.add(name)
    console.print(Panel(
        ", ".join(sorted(existing)) if existing else "None",
        title="Existing Platforms", border_style="magenta"
    ))

    console.print(Panel.fit("🛠 Welcome to the Unified Platform Scaffolder Wizard", style="green"))

    # Step 1/4: Platform identifier
    console.print(Panel.fit("Step 1/4: Platform identifier", style="cyan"))
    if sdk_map:
        table = Table(box=box.SIMPLE)
        table.add_column("#", style="bold cyan")
        table.add_column("Platform Short Name")
        for i, short in enumerate(sorted(sdk_map), 1):
            table.add_row(str(i), short)
        exit_idx = len(sdk_map) + 1
        table.add_row(str(exit_idx), "Exit")
        console.print(table)
        while True:
            choice = ask(f"Select platform number [1-{exit_idx}] or enter new short name (nickname)", None)
            if choice.lower() in ("exit", str(exit_idx)):
                console.print("[yellow]Exiting...[/yellow]")
                sys.exit(0)
            if choice.isdigit() and 1 <= (i := int(choice)) <= len(sdk_map):
                platform = sorted(sdk_map)[i-1]
                break
            if not choice.isdigit() and VALID_PLATFORM_RX.match(choice):
                platform = choice
                break
            console.print("[red]→ Invalid selection.[/red]")
    else:
        val = ask("Enter new platform short name (e.g., meraki) or 'exit' to quit", None)
        if val.lower() == "exit":
            console.print("[yellow]Exiting...[/yellow]")
            sys.exit(0)
        platform = val

    while not VALID_PLATFORM_RX.match(platform):
        console.print("[red]→ Invalid platform. Use lowercase letters, digits, and underscores.[/red]")
        platform = ask("Enter platform short name (e.g., meraki)", None)

    console.print(f":white_check_mark: Platform set to [bold]{platform}[/bold]\n")
    is_new = platform not in sdk_map

    # Step 1b/4: SDK module import path
    console.print(Panel.fit("Step 1b/4: SDK module import path", style="cyan"))
    default_sdk = sdk_map.get(platform, platform)
    base_mod = default_sdk.removesuffix(".session")
    options: List[str] = []
    for guess in (base_mod, f"{base_mod}.session"):
        try:
            load_client(guess)
            options.append(guess)
        except Exception:
            pass
    if not options:
        console.print("[yellow]Warning: no valid SDK module found; showing raw guesses[/yellow]")
        options = [base_mod, f"{base_mod}.session"]
    table = Table(box=box.SIMPLE)
    table.add_column("#", style="bold cyan")
    table.add_column("Module")
    for i, mod in enumerate(options, 1):
        table.add_row(str(i), mod)
    console.print(table)
    while True:
        sel = ask("Select module number or enter custom (or 'exit' to quit)", None)
        if sel.lower() == "exit":
            console.print("[yellow]Exiting...[/yellow]")
            sys.exit(0)
        if sel.isdigit() and 1 <= (j := int(sel)) <= len(options):
            sdk_module = options[j-1]
            break
        if not sel.isdigit() and sel:
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

    # Build and execute scaffolder command
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

    if args.dry_run:
        console.print(Panel(Markdown(f"**DRY RUN**\n```bash {' '.join(shlex.quote(c) for c in cmd)} ```"), border_style="yellow"))
    else:
        console.print(Panel.fit("🚀 Running scaffolder...", style="cyan"))
        env = os.environ.copy()
        env["PYTHONPATH"] = f"{AGENT_ROOT}:{env.get('PYTHONPATH','')}"
        subprocess.run(cmd, check=True, env=env)

    # Update sdk_map.json if new
    if is_new:
        sdk_map[platform] = sdk_module
        SDK_MAP_FILE.write_text(json.dumps(sdk_map, indent=2), encoding="utf-8")
        console.print(f"[green]Added '{platform}' → '{sdk_module}' to SDK map.[/green]")

    console.print(Panel.fit(":white_check_mark: Scaffolding complete!", style="green"))

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[red]Interrupted by user.[/red]")