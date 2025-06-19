#!/usr/bin/env python3
from __future__ import annotations
###########################################################################################
## suite-cisco-ai-building-blocks/src/app/user_commands/create_platform.py
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
║   • Select an existing platform or create a new one                               ║
║   • Option to Exit at any time                                                    ║
║   • Automatically detects SDK module import path                                  ║
║   • Validates platform names and regex filters                                    ║
║   • Polished table previews and workflow diagram link                             ║
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

from app.user_commands.update_platform_registry import display_registry
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt
from rich.markdown import Markdown
from rich import box
from rich.traceback import install

install()
console = Console()

# ─────────────────────────── paths ────────────────────────────────────────────
AGENT_ROOT   = Path(__file__).resolve().parents[1]           # …/src/app
PROJECT_ROOT = Path(__file__).resolve().parents[3]           # repo root
SPEC_DIR     = PROJECT_ROOT / "src" / "source_open_api"
DOTENV_PATH = PROJECT_ROOT / ".env"

# Make AGENT_ROOT import-able for sdk_loader
if str(AGENT_ROOT) not in sys.path:
    sys.path.insert(0, str(AGENT_ROOT))

from app.utils.sdk_loader import load_client
from app.user_commands.update_platform_registry import (
    load_registry,
    save_registry,
    check_scaffold_exists,
)
# ───────────────────── env helpers ───────────────────────────────────────

def ensure_enable_flag_in_env(short: str, default: bool = False) -> None:
    """
    Ensure `.env` contains 'ENABLE_<SHORT>=<true|false>' under section 1.3.
    If missing, insert 'ENABLE_<SHORT>=<default>' just after the last existing
    ENABLE_… line in “1.3) PLATFORM TOGGLE SETTINGS” (or at EOF if not found).
    """
    var_name = f"ENABLE_{short.upper()}"
    toggle_header_rx = re.compile(r"^#\s*1\.3\)\s*PLATFORM\s+TOGGLE\s+SETTINGS", re.IGNORECASE)
    toggle_line_rx   = re.compile(r"^ENABLE_[A-Z0-9_]+\s*=", re.IGNORECASE)
    exists_rx        = re.compile(rf"^{var_name}\s*=", re.IGNORECASE)

    # Create .env if it doesn’t exist
    if not DOTENV_PATH.exists():
        DOTENV_PATH.parent.mkdir(parents=True, exist_ok=True)
        DOTENV_PATH.write_text("", encoding="utf-8")

    lines = DOTENV_PATH.read_text(encoding="utf-8").splitlines()

    # If ENABLE_<SHORT> already exists, do nothing
    for ln in lines:
        if exists_rx.match(ln.strip()):
            return

    # Otherwise, locate “1.3) PLATFORM TOGGLE SETTINGS”
    in_toggle = False
    insert_idx = None
    for idx, ln in enumerate(lines):
        if toggle_header_rx.match(ln):
            in_toggle = True
            insert_idx = idx + 1
            continue
        if in_toggle:
            if toggle_line_rx.match(ln.strip()):
                insert_idx = idx + 1
            else:
                # Once we hit a non-ENABLE_… line, stop scanning
                break

    if insert_idx is None:
        # No “1.3” header found → append at end
        insert_idx = len(lines)

    val = "true" if default else "false"
    new_line = f"{var_name}={val}"
    lines.insert(insert_idx, new_line)

    DOTENV_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"[create_platform] Inserted `{new_line}` into .env (section 1.3) at line {insert_idx+1}.")


def ensure_credentials_in_env(short: str, keys: list[str]) -> None:
    """
    Ensure `.env` contains a placeholder for each credential in `keys` under section 1.4.
    Each missing key (e.g. “DNACENTER_USERNAME”) will be inserted as “KEY=” just after
    the last existing credential in “1.4) PLATFORM SPECIFIC CREDENTIALS” (or at EOF).
    """
    creds_header_rx = re.compile(r"^#\s*1\.4\)\s*PLATFORM\s+SPECIFIC\s+CREDENTIALS", re.IGNORECASE)
    any_k_rx        = re.compile(r"^[A-Z0-9_]+\s*=", re.IGNORECASE)
    key_rxs         = {key: re.compile(rf"^{key}\s*=", re.IGNORECASE) for key in keys}

    # Create .env if it doesn’t exist
    if not DOTENV_PATH.exists():
        DOTENV_PATH.parent.mkdir(parents=True, exist_ok=True)
        DOTENV_PATH.write_text("", encoding="utf-8")

    lines = DOTENV_PATH.read_text(encoding="utf-8").splitlines()

    # Determine which keys are missing
    missing = []
    for key, pat in key_rxs.items():
        found = any(pat.match(ln.strip()) for ln in lines)
        if not found:
            missing.append(key)
    if not missing:
        return  # nothing to do

    # Find “1.4) PLATFORM SPECIFIC CREDENTIALS”
    in_creds = False
    insert_idx = None
    for idx, ln in enumerate(lines):
        if creds_header_rx.match(ln):
            in_creds = True
            insert_idx = idx + 1
            continue
        if in_creds:
            if any_k_rx.match(ln.strip()):
                insert_idx = idx + 1
            else:
                break

    if insert_idx is None:
        # No “1.4” header found → append at end
        insert_idx = len(lines)

    # Insert each missing key=
    for key in missing:
        lines.insert(insert_idx, f"{key}=")
        print(f"[create_platform] Inserted placeholder `{key}=` into .env (section 1.4) at line {insert_idx+1}.")
        insert_idx += 1

    DOTENV_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


# ───────────────────── registry helpers ───────────────────────────────────────
registry: Dict[str, Dict[str, str]] = load_registry()

def registry_get_sdk(short: str) -> str | None:
    return registry.get(short, {}).get("sdk_module") or None

def registry_get_spec(short: str) -> str | None:
    return registry.get(short, {}).get("openapi_name") or None

def registry_set(
    short: str,
    sdk_pkg: str,
    openapi_stem: str,
    *,
    created_by_us: bool | None = None,
    installed: bool = False,
) -> None:
    # Preserve any existing "route" flag; default to False if not present
    old_entry = registry.get(short, {})
    route_flag = old_entry.get("route", False)
    if created_by_us is None:
        created_by_us = old_entry.get("created_by_us", False)

    registry[short] = {
        "openapi_name":  openapi_stem,
        "sdk_module":    sdk_pkg,
        "created_by_us": created_by_us,
        "installed":     installed,
        "route":         route_flag,
    }
    save_registry(registry)

# ─────────────────────── validation ───────────────────────────────────────────
VALID_PLATFORM_RX = re.compile(r"^[a-z][a-z0-9_]*$")
VALID_VERBS       = {"GET", "POST", "PUT", "PATCH", "DELETE", "HEAD", "OPTIONS"}

EXAMPLE_LINK  = "https://example.com/create-platform-examples"
DIAGRAM_PATH  = AGENT_ROOT / "docs" / "create_platform_flow.png"

def clear_screen() -> None:
    if sys.stdout.isatty():
        os.system("cls" if os.name == "nt" else "clear")

def preview_table(rows: List[Tuple[str, str]]) -> None:
    """
    Given a list of (key, value) tuples, render a two-column table inside a Panel.
    """
    table = Table(box=box.ROUNDED, padding=(0, 1))
    table.add_column(justify="right", style="bold green", no_wrap=True)
    table.add_column()
    for key, value in rows:
        table.add_row(f"{key}:", value)
    console.print(Panel(table, title="Preview Configuration", border_style="cyan"))

def ask(prompt: str, default: Optional[str] = None) -> str:
    while True:
        resp = Prompt.ask(f"[cyan]?[/cyan] [bold]{prompt}[/bold]", default=default)
        if resp is None:
            resp = ""
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

# ───────────────────────────── main flow ──────────────────────────────────────
def main() -> None:
    clear_screen()
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--dry-run", action="store_true")
    args, _ = parser.parse_known_args()
    
    # Show the registry before anything else
    display_registry(registry)

    # ── show platforms that already have scaffolding ──────────────────────────
    generated = {p.stem for p in (AGENT_ROOT / "llm" / "function_definitions").glob("*.json")}
    console.print(Panel(", ".join(sorted(generated)) or "None", title="Existing Platforms", border_style="magenta"))

    console.print(Panel.fit("🛠 Welcome to the Unified Platform Scaffolder Wizard", style="green"))

    # Step 1/4 — short name (now driven by registry) ───────────────────────────
    console.print(Panel.fit("Step 1/4: Platform identifier", style="cyan"))

    if registry:
        table = Table(box=box.SIMPLE)
        table.add_column("#", style="bold cyan")
        table.add_column("Short Name")
        for i, short in enumerate(sorted(registry), 1):
            table.add_row(str(i), short)
        exit_idx = len(registry) + 1
        table.add_row(str(exit_idx), "Exit")
        console.print(table)

        while True:
            choice = ask(f"Select number [1-{exit_idx}] or enter new name", None)
            if choice.lower() in ("exit", str(exit_idx)):
                console.print("[yellow]Exiting…[/yellow]"); sys.exit(0)
            if choice.isdigit() and 1 <= (i := int(choice)) <= len(registry):
                platform = sorted(registry)[i-1]
                break
            if VALID_PLATFORM_RX.match(choice):
                platform = choice
                break
            console.print("[red]→ Invalid selection.[/red]")
    else:
        val = ask("Enter new platform short name (e.g. meraki) or 'exit' to quit")
        if val.lower() == "exit":
            console.print("[yellow]Exiting…[/yellow]"); sys.exit(0)
        platform = val

    while not VALID_PLATFORM_RX.match(platform):
        console.print("[red]→ Must be lowercase letters, digits, underscores; start with letter.[/red]")
        platform = ask("Enter platform short name", None)

    console.print(f":white_check_mark: Platform = [bold]{platform}[/bold]\n")
    is_new = platform not in registry

    # ── Step 1b/4 — SDK module (prefill from registry) ────────────────────────
    console.print(Panel.fit("Step 1b/4: SDK module import path", style="cyan"))
    default_sdk = registry_get_sdk(platform) or platform
    candidates = []
    if default_sdk:
        candidates.append(default_sdk)
        candidates.append(f"{default_sdk}.session")

    # Deduplicate in case default_sdk == base_mod
    candidates = list(dict.fromkeys(candidates))

    import importlib
    importable: List[str] = []
    loadable: List[str]   = []

    # 1) Which candidates import at all?
    for guess in candidates:
        try:
            importlib.import_module(guess)
            importable.append(guess)
        except ImportError:
            continue

    # 2) Among importable, which also load_client(...) okay?
    for modname in importable:
        try:
            load_client(modname)
            loadable.append(modname)
        except Exception:
            continue

    # Decide which set to show:
    if loadable:
        options = loadable
        default_index = 1  # pick the first loadable by default
    elif importable:
        options = importable
        default_index = 1  # first importable
    else:
        # If nothing even imports, show both guesses so user can type a custom path
        options = candidates
        default_index = 1 if candidates else None
        console.print("[yellow]No candidates imported; you may enter a custom SDK path.[/yellow]")

    # Render the table of possible SDK module names
    table = Table(box=box.SIMPLE)
    table.add_column("#", style="bold cyan")
    table.add_column("Module")
    for i, mod in enumerate(options, 1):
        table.add_row(str(i), mod)
    console.print(table)

    # Prompt user (preselect default_index)
    while True:
        sel_default = str(default_index) if default_index else None
        sel = ask("Select module number or enter custom (or 'exit')", sel_default)
        if sel.lower() == "exit":
            console.print("[yellow]Exiting…[/yellow]")
            sys.exit(0)
        if sel.isdigit() and 1 <= (j := int(sel)) <= len(options):
            sdk_module = options[j-1]
            break
        if sel:
            sdk_module = sel
            break
        console.print("[red]→ Invalid selection.[/red]")

    # Finally, warn if load_client(...) fails for the chosen SDK
    sdk_ok = True
    try:
        load_client(sdk_module)
    except Exception as e:
        console.print(
            f"[yellow]Warning:[/yellow] Imported '{sdk_module}', "
            f"but load_client() failed to find a client-class (details: {e})."
        )
        sdk_ok = False

    console.print(f":white_check_mark: SDK module = [bold]{sdk_module}[/bold]\n")

    # ── Step 2/4 — OpenAPI spec (prefill from registry if available) ─────────
    console.print(Panel.fit("Step 2/4: Choose OpenAPI spec", style="cyan"))
    stored_spec = registry_get_spec(platform)
    specs = sorted(chain(SPEC_DIR.glob("*.json"), SPEC_DIR.glob("*.yaml"), SPEC_DIR.glob("*.yml")))
    stem_to_path = {fp.stem: fp for fp in specs}

    table = Table(box=box.SIMPLE_HEAVY)
    table.add_column("#", style="bold cyan")
    table.add_column("File")
    table.add_column("Size (KB)", justify="right")
    table.add_column("Modified")
    default_spec_index = None
    for i, fp in enumerate(specs, 1):
        table.add_row(
            str(i), fp.name,
            str(fp.stat().st_size // 1024),
            datetime.fromtimestamp(fp.stat().st_mtime).strftime("%Y-%m-%d"),
        )
        if stored_spec and fp.stem == stored_spec:
            default_spec_index = i

    console.print(table)

    if default_spec_index:
        default_spec_prompt = str(default_spec_index)
    else:
        default_spec_prompt = "1"

    choice = ask("Select spec number", default_spec_prompt)
    if choice.isdigit() and 1 <= (idx := int(choice)) <= len(specs):
        spec_file = str(specs[idx-1])
    else:
        spec_file = ask("Enter path to OpenAPI spec", None)

    spec_ok = Path(spec_file).exists()
    if not spec_ok:
        console.print(f"[red]→ Spec file '{spec_file}' not found.[/red]")

    console.print(f":white_check_mark: Spec = [bold]{Path(spec_file).name}[/bold]\n")

    # Step 3/4 — Configure HTTP verbs
    console.print(Panel.fit("Step 3/4: Configure HTTP verbs", style="cyan"))
    verbs   = ask("HTTP verbs (comma-separated, blank=ALL)", "GET").upper()
    cleaned = [v.strip() for v in verbs.split(",") if v.strip() in VALID_VERBS]
    console.print(f":white_check_mark: Verbs = [bold]{', '.join(cleaned) or 'ALL'}[/bold]\n")

    # Step 4/4 — Regex filter for operationIds
    console.print(Panel.fit("Step 4/4: Regex filter for operationIds", style="cyan"))
    name_re = ask("Regex filter (blank=none)", "").strip()
    console.print(f":white_check_mark: Regex = [bold]{name_re or "None"}[/bold]\n")

    # ── Preview & confirm ─────────────────────────────────────────────────────
    preview_table([
        ("Platform",    platform),
        ("SDK module",  sdk_module),
        ("Spec file",   Path(spec_file).name),
        ("HTTP verbs",  ', '.join(cleaned) or "ALL"),
        ("Name regex",  name_re or "None"),
    ])

    if DIAGRAM_PATH.exists():
        console.print(Panel.fit("-----------------------"))
        console.print(f"[cyan]file://{DIAGRAM_PATH}[/cyan]")

    # ── call platform_scaffolder.py ───────────────────────────────────────────
    scaffolder_path = PROJECT_ROOT / "src" / "scripts" / "platform_scaffolder.py"
    cmd = [
        sys.executable, str(scaffolder_path),
        "--platform",      platform,
        "--sdk-module",    sdk_module,
        "--openapi-spec",  spec_file,
    ]
    if cleaned:
        cmd += ["--include-http-methods", ''.join(cleaned)]
    if name_re:
        cmd += ["--name-pattern", name_re]

    # Only mark installed=True if both SDK import and spec exist
    final_installed_flag = sdk_ok and spec_ok

    if args.dry_run:
        console.print(Panel(f"**DRY RUN**\n{' '.join(shlex.quote(c) for c in cmd)}", border_style="yellow"))
    else:
        console.print(Panel.fit("🚀 Running scaffolder…", style="cyan"))
        env = os.environ.copy()
        env["PYTHONPATH"] = f"{AGENT_ROOT}:{env.get('PYTHONPATH','')}"
        try:
            subprocess.run(cmd, check=True, env=env)
        except subprocess.CalledProcessError as e:
            console.print(f"[red]Error: scaffolder failed with exit code {e.returncode}[/red]")
            final_installed_flag = False

    # ── update registry (single source of truth) ──────────────────────────────
    registry_set(
        platform,
        sdk_pkg        = sdk_module,
        openapi_stem   = Path(spec_file).stem,
        installed      = final_installed_flag,
        created_by_us  = None,
    )

    # ── Ensure .env has the toggle & credential placeholders ───────────────────
    ensure_enable_flag_in_env(platform)

    # Decide which credential keys this platform needs:
    if platform == "ai_defense":
        creds = ["AI_DEFENSE_API_KEY"]
    elif platform == "catalyst":
        creds = ["DNACENTER_USERNAME", "DNACENTER_PASSWORD", "DNACENTER_BASE_URL"]
    elif platform == "cloudlock":
        creds = ["CLOUDLOCK_API_KEY", "CLOUDLOCK_API_SECRET"]
    elif platform == "intersight":
        creds = ["INTERSIGHT_API_KEY", "INTERSIGHT_API_SECRET", "INTERSIGHT_BASE_URL"]
    elif platform == "meraki":
        creds = ["CISCO_MERAKI_API_KEY"]
    elif platform == "nexus_dashboard":
        creds = ["NEXUS_DASHBOARD_API_KEY", "NEXUS_DASHBOARD_BASE_URL"]
    elif platform == "nexus_hyperfabric":
        creds = ["NEXUS_HYPERFABRIC_API_KEY",
                 "NEXUS_HYPERFABRIC_API_SECRET",
                 "NEXUS_HYPERFABRIC_BASE_URL"]
    elif platform == "sdwan_mngr":
        creds = ["CISCO_SD_WAN_USERNAME",
                 "CISCO_SD_WAN_PASSWORD",
                 "CISCO_SD_WAN_BASE_URL"]
    elif platform == "secure_access":
        creds = ["SECURE_ACCESS_CLIENT_ID",
                 "SECURE_ACCESS_CLIENT_SECRET",
                 "SECURE_ACCESS_TOKEN_URL"]
    elif platform == "umbrella":
        creds = ["UMBRELLA_API_KEY", "UMBRELLA_API_SECRET"]
    else:
        creds = []

    if creds:
        ensure_credentials_in_env(platform, creds)


    if final_installed_flag:
        console.print(Panel.fit(":white_check_mark: Scaffolding complete!", style="green"))
    else:
        console.print(Panel.fit(
            "[yellow]Warning: Some steps did not complete successfully. "
            "Registry updated with installed=False.[/yellow]",
            style="yellow",
        ))

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[red]Interrupted by user.[/red]")
