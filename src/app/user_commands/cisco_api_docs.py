#!/usr/bin/env python3
"""
Cisco & Splunk API Documentation Launcher
──────────────────────────────────────────
Select a number to open the doc site in your default browser, or type
`i<n>` (e.g. i3) to display a longer description without launching.
"""
from __future__ import annotations
import os
import sys
import webbrowser
from pathlib import Path

from rich.console import Console, Group
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt
from rich.text import Text
from rich import box
from rich.traceback import install

install()
console = Console()

# ── Docs catalogue -----------------------------------------------------------
DOCS: list[dict[str, str]] = [
    {   # 1
        "name": "Cisco DevNet – Docs Home",
        "url":  "https://developer.cisco.com/docs/",
        "desc": "Main DevNet documentation hub covering all Cisco platforms: REST guides, SDKs, samples, and sandboxes.",
    },
    {   # 2
        "name": "Cisco Meraki Dashboard API",
        "url":  "https://developer.cisco.com/meraki/api-v1/",
        "desc": "Interactive reference and examples for the Meraki v1 Dashboard API.",
    },
    {   # 3
        "name": "Cisco Webex REST API",
        "url":  "https://developer.webex.com/docs/api/getting-started",
        "desc": "Webex Messaging / Meetings REST endpoints, OAuth walkthroughs, and SDK links.",
    },
    {   # 4
        "name": "Cisco Catalyst Center Intent API",
        "url":  "https://developer.cisco.com/docs/catalyst-center/",
        "desc": "API reference, workflows, and SDK guides for Catalyst Center (formerly DNAC).",
    },
    {   # 5
        "name": "Cisco Umbrella Reporting & Admin APIs",
        "url":  "https://developer.cisco.com/docs/cloud-security/",
        "desc": "Umbrella Cloud Security API docs: reporting, management, and enforcement.",
    },
    {   # 6
        "name": "Cisco SecureX & Secure Cloud APIs",
        "url":  "https://developer.cisco.com/docs/security/",
        "desc": "SecureX threat-response, Secure Firewall Management Center, Secure Endpoint, etc.",
    },
    # ── Splunk additions (Cisco Observability) --------------------------------
    {   # 7
        "name": "Splunk Enterprise REST API (latest)",
        "url":  "https://docs.splunk.com/Documentation/Splunk/latest/RESTREF/RESTlist",
        "desc": "Authoritative REST reference manual for Splunk Enterprise – auto‑redirects to the current version.",
    },
    {   # 8
        "name": "Splunk Cloud REST API overview",
        "url":  "https://docs.splunk.com/Documentation/SplunkCloud/latest/RESTTUT/RESTandCloud",
        "desc": "Differences and usage guidelines for Splunk Cloud Platform REST endpoints.",
    },
    {   # 9
        "name": "Splunk Developer Portal (Enterprise Apps)",
        "url":  "https://dev.splunk.com/enterprise/docs",
        "desc": "SDKs, modular inputs, and AppInspect resources for building on Splunk Enterprise.",
    },
]

EXIT_ROW = len(DOCS) + 1

# ── helpers -----------------------------------------------------------------

def clear() -> None:
    if sys.stdout.isatty():
        os.system("cls" if os.name == "nt" else "clear")


def show_menu() -> None:
    table = Table(box=box.SIMPLE)
    table.add_column("#", style="bold cyan", no_wrap=True)
    table.add_column("Documentation Hub")
    for idx, d in enumerate(DOCS, 1):
        table.add_row(str(idx), d["name"])
    table.add_row(str(EXIT_ROW), "Exit")
    console.print(Panel(table, title="Select API Documentation", border_style="cyan"))


def main() -> None:
    clear()
    console.print(Panel.fit("📚 Cisco & Splunk API Docs", style="green"))

    while True:
        show_menu()
        choice = Prompt.ask("Enter number or 'i<n>' for info").strip()

        # Info request ------------------------------------------------------
        if choice.lower().startswith("i"):
            num = choice[1:]
            if num.isdigit() and 1 <= (n := int(num)) <= len(DOCS):
                doc = DOCS[n-1]
                console.print(
                    Panel(doc["desc"], title=f"Info: {doc['name']}", border_style="magenta")
                )
                Prompt.ask("Press Enter to return")
            continue

        # Exit --------------------------------------------------------------
        if choice.isdigit() and int(choice) == EXIT_ROW:
            console.print("[green]Goodbye![/green]")
            sys.exit(0)

        # Open URL ----------------------------------------------------------
        if choice.isdigit() and 1 <= (sel := int(choice)) <= len(DOCS):
            url = DOCS[sel-1]["url"]
            console.print(f"[green]Opening {url}…[/green]")
            webbrowser.open_new_tab(url)
            Prompt.ask("Press Enter to return")
            continue

        console.print("[red]Invalid input.[/red]")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()
        sys.exit(1)
