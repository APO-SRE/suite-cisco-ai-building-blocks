#!/usr/bin/env python3
from __future__ import annotations
################################################################################
## suite-cisco-ai-building-blocks/src/app/user_commands/stop_cisco_platform_ai.py
################################################################################
"""
Interactive “Stop Cisco Platform AI” wizard.

• Clears screen, shows status
• Confirms with user (y/N)
• Sends SIGTERM, waits up to 10 s
• If still alive after 10 s, sends SIGKILL
• Prints last 10 log lines
• Removes .run/agent.pid
"""

import os, signal, sys, time
from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.syntax import Syntax
from rich.traceback import install

install()
console = Console()

ROOT     = Path(__file__).resolve().parents[3]
RUNDIR   = ROOT / ".run"
PID_FILE = RUNDIR / "agent.pid"
LOG_FILE = RUNDIR / "agent.log"

# ── helpers ──────────────────────────────────────────────────────────────
def clear_screen() -> None:
    if sys.stdout.isatty():
        os.system("cls" if os.name == "nt" else "clear")

def pid_running(pid: int) -> bool:
    try:
        os.kill(pid, 0)
        return True
    except OSError:
        return False

# ── main flow ────────────────────────────────────────────────────────────
def main() -> None:
    clear_screen()
    console.print(Panel.fit("⏹  [bold cyan]Stop Cisco Platform AI[/bold cyan]", style="green"))

    # 1. Ensure PID file exists
    if not PID_FILE.exists():
        console.print(Panel("[yellow]No running agent found.[/yellow]", border_style="yellow"))
        sys.exit(0)

    pid = int(PID_FILE.read_text().strip())
    console.print(f"Found PID file: [white]{pid}[/white]")

    # 2. Confirm
    if Prompt.ask("Really stop the service?", choices=["y", "n"], default="n") == "n":
        console.print("[green]Aborted.[/green]")
        sys.exit(0)

    # 3. Send SIGTERM
    try:
        os.kill(pid, signal.SIGTERM)
        console.print(f"Sent SIGTERM to PID {pid}. Waiting up to 10 s …")
    except ProcessLookupError:
        console.print("[yellow]Process already exited.[/yellow]")

    # 4. Wait for exit (max 10 s)
    deadline = time.time() + 10
    while time.time() < deadline and pid_running(pid):
        time.sleep(0.5)

    # 5. If still running, send SIGKILL
    if pid_running(pid):
        console.print(Panel("[red]Process did not terminate within 10 s. Sending SIGKILL…[/red]", border_style="red"))
        try:
            os.kill(pid, signal.SIGKILL)
            console.print(f"Sent SIGKILL to PID {pid}.")
        except ProcessLookupError:
            console.print("[yellow]Process exited between checks.[/yellow]")
        # Optional: give a brief moment to let SIGKILL take effect
        time.sleep(0.5)

        # Final check
        if pid_running(pid):
            console.print(Panel("[red]Process still alive after SIGKILL. Giving up.[/red]", border_style="red"))
            sys.exit(1)
        else:
            console.print(Panel("[green]⚡ Process forcefully killed.[/green]", border_style="green"))

    # 6. Show last 10 log lines if available
    if LOG_FILE.exists():
        tail = "\n".join(LOG_FILE.read_text(encoding="utf-8").splitlines()[-10:])
        console.print(Panel(Syntax(tail or "(log empty)", "bash"), title="Last 10 log lines", border_style="blue"))

    # 7. Clean up & report
    PID_FILE.unlink(missing_ok=True)
    console.print(Panel("[green]✅ Cisco Platform AI stopped successfully.[/green]", border_style="green"))

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[red]Interrupted.[/red]")
