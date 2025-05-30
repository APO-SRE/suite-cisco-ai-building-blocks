#!/usr/bin/env python3
from __future__ import annotations
#####################################################################################################
## suite-cisco-ai-building-blocks/src/app/user_commands/create_domain_demo_index.py
## Copyright (c) 2025 Jeff Teeter, Ph.D.
## Cisco Systems, Inc.
## Licensed under the Apache License, Version 2.0 (see LICENSE)
## Distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND.
#####################################################################################################

"""
╔═════════════════════════ Domain Demo Indexer Wizard ═════════════════════════╗
║ A step-by-step CLI to index a sample domain via process_domain.py with a    ║
║ polished UX.                                                                ║
║                                                                              ║
║ FEATURES                                                                     ║
║   • Lists available domain_samples folders                                   ║
║   • Sets DOMAIN_SAMPLES_INDEX_FOLDER_NAME and invokes process_domain.py      ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

import os
import sys
import subprocess
import shlex
from pathlib import Path

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table
from rich import box
from rich.traceback import install

install()
console = Console()

# clear screen helper
def clear_screen() -> None:
    if sys.stdout.isatty():
        os.system("cls" if os.name == "nt" else "clear")


def main() -> None:
    clear_screen()
    console.print(Panel.fit("🛠 Welcome to the Domain Demo Indexer Wizard", style="green"))

    # discover paths
    REPO_ROOT     = Path(__file__).resolve().parents[3]       # …/suite-cisco-ai-building-blocks/
    SRC_ROOT      = REPO_ROOT / "src"                         # …/suite-cisco-ai-building-blocks/src
    AGENT_ROOT    = SRC_ROOT  / "app"                         # …/src/app
    AGENT_ROOT = Path(__file__).resolve().parents[1]
    PROJECT_ROOT = Path(__file__).resolve().parents[3]
    REPO_ROOT = AGENT_ROOT.parent
    DB_DIR = PROJECT_ROOT / "src" / "db_scripts"
    SAMPLES_DIR = DB_DIR / "domain_samples"

    # verify samples directory
    if not SAMPLES_DIR.exists():
        console.print(f"[red]Samples directory not found: {SAMPLES_DIR}[/red]")
        sys.exit(1)

    # list demo domains
    domains = sorted([p.name for p in SAMPLES_DIR.iterdir() if p.is_dir()])
    if not domains:
        console.print(f"[red]No demo domains found in {SAMPLES_DIR}[/red]")
        sys.exit(1)

    table = Table(box=box.SIMPLE)
    table.add_column("#", style="bold cyan", no_wrap=True)
    table.add_column("Domain Sample")
    for idx, name in enumerate(domains, start=1):
        table.add_row(str(idx), name)
    console.print(Panel(table, title="Select Demo Domain to Index", border_style="cyan"))

    # prompt with exit option
    prompt_str = f"Enter number [1-{len(domains)}] or 'exit' to quit"
    choice = Prompt.ask(prompt_str).strip()
    if choice.lower() == 'exit':
        console.print("[cyan]Exiting without indexing.[/cyan]")
        sys.exit(0)

    try:
        idx = int(choice)
        folder = domains[idx - 1]
        console.print(Panel.fit(f"You chose: [bold]{folder}[/bold]", style="cyan"))
    except Exception:
        console.print(f"[red]Invalid selection: {choice}[/red]")
        sys.exit(1)

    # preview command
    cmd = [sys.executable, "-m", "scripts.process_domain"]
    env = os.environ.copy()
    env["DOMAIN_SAMPLES_INDEX_FOLDER_NAME"] = folder
    preview_cmd = f"DOMAIN_SAMPLES_INDEX_FOLDER_NAME={folder} {sys.executable} -m scripts.process_domain"
    console.print(Panel(preview_cmd, title="Command to run", border_style="cyan"))

    # confirm
    confirm = Prompt.ask("Proceed with domain indexing? (Y/n)", default="Y")
    if confirm.strip().lower().startswith("n"):
        console.print("[yellow]Aborted by user.[/yellow]")
        return

    console.print(Panel.fit("🚀 Running process_domain...", style="cyan"))
    subprocess.run(cmd, check=True, env=env, cwd=str(DB_DIR))
    console.print(Panel.fit(":white_check_mark: Domain indexing complete!", style="green"))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()  # newline
        sys.exit(1)
