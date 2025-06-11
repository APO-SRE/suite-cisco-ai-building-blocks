#!/usr/bin/env python3
from __future__ import annotations
################################################################################
## suite-cisco-ai-building-blocks/src/app/user_commands/status_application.py
## Clears screen and shows status of FastAPI (port 8000) and telemetry stack
################################################################################

import subprocess
import sys
from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()

def check_fastapi() -> Text:
    """
    Checks if FastAPI is listening on port 8000.
    Returns a Rich Text with the status and any listener info.
    """
    try:
        result = subprocess.run(
            ["lsof", "-iTCP:8000", "-sTCP:LISTEN"],
            check=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        if result.stdout.strip():
            return Text.from_markup(f"[green]✅ FastAPI is running:[/green]\n{result.stdout}")
        else:
            return Text.from_markup("[red]❌ FastAPI is not listening on port 8000.[/red]")
    except FileNotFoundError:
        return Text.from_markup(
            "[yellow]⚠️ lsof not found. Cannot check FastAPI port status.[/yellow]"
        )


def check_telemetry(repo_root: Path) -> Text:
    """
    Uses docker compose to show current telemetry stack status.
    """
    compose_file = repo_root / "docker" / "docker-compose.yaml"
    if not compose_file.exists():
        return Text.from_markup(
            f"[red]Error:[/red] Could not find docker-compose file at {compose_file}"
        )
    try:
        result = subprocess.run(
            ["docker", "compose", "-f", str(compose_file), "ps"],
            cwd=str(repo_root),
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        return Text.from_markup(f"[blue]📋 Telemetry stack status:\n[/blue]{result.stdout}")
    except subprocess.CalledProcessError as exc:
        return Text.from_markup(
            f"[red]Failed to get telemetry status (exit {exc.returncode}):[/red]\n{exc.stderr}"
        )
    except FileNotFoundError:
        return Text.from_markup(
            "[yellow]⚠️ docker compose not found. Cannot check telemetry stack status.[/yellow]"
        )


def main() -> None:
    # Clear screen
    console.clear()

    # Determine repo root (three parents up)
    repo_root = Path(__file__).resolve().parents[3]

    # FastAPI status
    fastapi_status = check_fastapi()
    console.print(Panel(fastapi_status, title="FastAPI Status", border_style="green"))

    # Telemetry stack status
    telemetry_status = check_telemetry(repo_root)
    console.print(Panel(telemetry_status, title="Telemetry Stack Status", border_style="blue"))


if __name__ == "__main__":
    main()
