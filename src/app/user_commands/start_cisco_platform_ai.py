#!/usr/bin/env python3
from __future__ import annotations
################################################################################
## suite-cisco-ai-building-blocks/src/app/user_commands/start_cisco_platform_ai.py
## Start Cisco Platform AI  – interactive FastAPI launcher
################################################################################
"""
╔════════════════════════════════ Start Cisco Platform AI ════════════════════════════════╗
║ This wizard spins up the FastAPI “Cisco Platform AI” service (uvicorn --reload).        ║
║                                                                                        ║
║ You’ll be asked:                                                                       ║
║   • **Port** – the TCP port your browser will open (default 8000).                     ║
║   • **Debug** – verbose logging (`--log-level debug`) helpful while coding.            ║
║   • **Background** – run detached so your SSH window stays free (writes .run/agent.log).║
║   • **OpenTelemetry** – export traces/metrics (sets OTEL_* env vars).                  ║
╚════════════════════════════════════════════════════════════════════════════════════════╝
"""

import os, subprocess, sys, signal
from pathlib import Path
from rich import box
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table
from app.llm.dynamic import DYNAMIC_CACHE_ROOT
from rich.traceback import install
from dotenv import load_dotenv

load_dotenv()

install()
console = Console()

# ── paths ────────────────────────────────────────────────────────────────────
ROOT   = Path(__file__).resolve().parents[3]           # repo root
SRC    = ROOT / "src"
RUNDIR = ROOT / ".run";  RUNDIR.mkdir(exist_ok=True)
PID_FILE = RUNDIR / "agent.pid"
LOG_FILE = RUNDIR / "agent.log"

# ── helpers ──────────────────────────────────────────────────────────────────
def clear_screen() -> None:
    if sys.stdout.isatty():
        os.system("cls" if os.name == "nt" else "clear")

def header() -> None:
    console.print(
        Panel.fit(
            "🚀 [bold cyan]Cisco Platform AI – FastAPI Launcher[/bold cyan]\n"
            "[dim]Type “exit” at any prompt to quit.[/dim]",
            style="green",
        )
    )

def explain(question: str, default: str | None = None) -> str:
    """
    Ask *question* with Rich Prompt.

    • If the user types “exit”, “quit”, “q”, or “x” (case-insensitive) → exit(0)
    • If they hit Enter on an empty question *with a default* → return default
    • Otherwise re-prompt until non-empty text is given
    """
    while True:
        ans = Prompt.ask(f"[cyan]?[/cyan] [bold]{question}[/bold]", default=default)
        if ans is None:
            ans = ""
        ans = ans.strip()

        # ── universal escape hatch ───────────────────────────────────────
        if ans.lower() in {"exit", "quit", "q", "x"}:
            console.print("[yellow]Exiting wizard…[/yellow]")
            sys.exit(0)

        if ans:                       # user typed something non-empty
            return ans
        if default is not None:       # blank but default exists → accept default
            return default

        console.print("[red]→ Please enter a value (or type exit).[/red]")


# ── main flow ────────────────────────────────────────────────────────────────
def main() -> None:
    clear_screen(); header()


    # guard – already running?
    if PID_FILE.exists():
        console.print(
            Panel("[red]An agent is already running.[/red]\n"
                  "Use [bold]Stop Cisco PLatform AI[/bold] first.",
                  border_style="red"))
        sys.exit(0)

    # ── interactive questions ───────────────────────────────────────────────
    console.print()
    port   = explain("Port", default="8000")

    console.print()
    debug  = explain("Enable DEBUG logging? (y/n)",  default="n").lower().startswith("y")

    console.print()
    detach = explain("Run in background? (y/n)",      default="y").lower().startswith("y")

    console.print()
    otel   = explain("Enable OpenTelemetry export? (y/n)", default="n").lower().startswith("y")
    console.print()

    # ── env vars ────────────────────────────────────────────────────────────
    env = os.environ.copy()
    if otel:
        env.setdefault("OTEL_PYTHON_AUTO_INSTRUMENTATION", "1")
        endpoint = env.get("OTEL_EXPORTER_OTLP_ENDPOINT") or \
                   explain("OTEL exporter endpoint", default="http://localhost:4318")
        env["OTEL_EXPORTER_OTLP_ENDPOINT"] = endpoint
    else:
        env.pop("OTEL_PYTHON_AUTO_INSTRUMENTATION", None)
        env.pop("OTEL_EXPORTER_OTLP_ENDPOINT", None)

    # ── build uvicorn command ───────────────────────────────────────────────
    cmd = [sys.executable, "-m", "uvicorn", "app.main:app",
           "--host", "0.0.0.0",
           "--port", port,
           "--reload"]
    if debug:
        cmd += ["--log-level", "debug"]

    # ── launch ──────────────────────────────────────────────────────────────
    console.print(
        Panel.fit(
            f"Starting Cisco Platform AI on http://localhost:{port}/docs …",
            border_style="cyan",
        )
    )

    stdout = stderr = None
    if detach:
        stdout = open(LOG_FILE, "ab", buffering=0)
        stderr = stdout

    proc = subprocess.Popen(cmd, cwd=str(SRC), env=env,
                            stdout=stdout, stderr=stderr)

    PID_FILE.write_text(str(proc.pid))
    console.print(f"[green]PID {proc.pid} written to {PID_FILE}[/green]")

    if detach:
        console.print(
            Panel(
                "🟢 Agent running **detached**.\n"
                f"Tail logs with:\n  [white]tail -f {LOG_FILE}[/white]\n\n"
                "You can stop the service later by selecting\n"
                "[bold]“Stop Cisco Platform AI”[/bold] in the menu, "
                "or manually with:\n"
                "  [white]python -m app.user_commands.stop_cisco_platform_ai[/white]",
                border_style="blue",
            )
        )

        return  # detach → script exits

    # attached mode: stream logs until Ctrl-C
    try:
        proc.wait()
    finally:
        PID_FILE.unlink(missing_ok=True)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[red]Interrupted.[/red]")
