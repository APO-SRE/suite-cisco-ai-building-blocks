#!/usr/bin/env python3
from __future__ import annotations
################################################################################
## suite-cisco-ai-building-blocks/src/app/user_commands/start_telemetry_stack.py
## Spins up Tempo / Prometheus / Grafana with docker compose and shows status
################################################################################

import subprocess
import sys
from pathlib import Path
from rich.console import Console
from rich.panel import Panel

console = Console()


def main() -> None:
    # Clear the terminal screen
    console.clear()

    # 1) Figure out where the repo root is:
    repo_root = Path(__file__).resolve().parents[3]

    # 2) Compose file lives at "<repo_root>/docker/docker-compose.yaml"
    compose_file = repo_root / "docker" / "docker-compose.yaml"
    if not compose_file.exists():
        console.print(
            Panel(
                f"[red]Error:[/red] Could not find docker-compose file at:\n"
                f"    {compose_file}\n",
                border_style="red",
            )
        )
        sys.exit(1)

    console.print(Panel(f"⏳ Bringing up telemetry stack using:\n  [white]{compose_file}[/white]", style="cyan"))

    # 3) Run: docker compose -f <compose_file> up -d
    try:
        result_up = subprocess.run(
            ["docker", "compose", "-f", str(compose_file), "up", "-d"],
            cwd=str(repo_root),
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
    except FileNotFoundError:
        console.print(
            Panel(
                "[red]Error:[/red] `docker compose` command not found. "
                "Make sure Docker Compose plugin is installed and in your PATH.",
                border_style="red",
            )
        )
        sys.exit(1)
    except subprocess.CalledProcessError as exc:
        console.print(
            Panel(
                f"[red]docker compose failed (exit code {exc.returncode}):[/red]\n"
                f"{exc.stderr}",
                border_style="red",
            )
        )
        sys.exit(exc.returncode)

    # 4) On success, print the output of the up command
    console.print(Panel(f"[green]✅ Telemetry stack started[/green]\n{result_up.stdout}", border_style="green"))

    # 5) Display current container status using the same compose file
    try:
        result_ps = subprocess.run(
            ["docker", "compose", "-f", str(compose_file), "ps"],
            cwd=str(repo_root),
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        console.print(Panel(f"📋 Current stack status:\n{result_ps.stdout}", border_style="blue"))
    except subprocess.CalledProcessError as exc:
        console.print(
            Panel(
                f"[yellow]Warning:[/yellow] Could not fetch stack status (exit code {exc.returncode}).\n"
                f"{exc.stderr}",
                border_style="yellow",
            )
        )


if __name__ == "__main__":
    main()
