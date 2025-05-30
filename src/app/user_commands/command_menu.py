#!/usr/bin/env python3
from __future__ import annotations
################################################################################
## suite-cisco-ai-building-blocks/src/app/user_commands/command_menu.py
## Copyright (c) 2025 Jeff Teeter, Ph.D.
## Cisco Systems, Inc.
## Licensed under the Apache License, Version 2.0 (see LICENSE)
## Distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND.
################################################################################

"""
╔═════════════════════════ Command Launcher Wizard ═════════════════════════╗
║ A CLI tool to run common AI agent utilities with a polished UX.           ║
║ Press [cyan]i<n>[/cyan] (e.g. i2) to learn more about command <n>.        ║
║ Enter the number to execute, or use the exit option to quit.              ║
╚═══════════════════════════════════════════════════════════════════════════╝
"""

import os
import sys
import subprocess

from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt
from rich import box
from rich.traceback import install
from rich.markdown import Markdown
from rich.table import Table as GridTable
from .create_platform_index import azure_list_platforms




install()
console = Console()

# Paths and imports
AGENT_ROOT = Path(__file__).resolve().parents[1]
# CLI entry scripts live under src/app/user_commands
UCMD_DIR   = AGENT_ROOT / "user_commands"
# SRC_ROOT = <repo>/src
SRC_ROOT   = AGENT_ROOT.parent
# point SDK_DIR at <repo>/src/db_scripts/output_sdk
SDK_DIR    = SRC_ROOT / "db_scripts" / "output_sdk"
 

 

# Available commands
COMMANDS: list[dict[str, str]] = [
    {
        "script":   "create_platform.py",
        "function": "Create Platform",
        "short":    "Scaffold a new platform",
        "long": (
            "`create_platform.py` guides you through naming a platform, selecting its SDK module and OpenAPI spec, "
            "configuring HTTP methods and operation-ID filters, then generates all LLM artifacts: function definitions, "
            "full OpenAPI specs, client stubs, dispatchers, and unified service."
        ),
    },
    {
        "script":   "reset_platform.py",
        "function": "Reset Platform",
        "short":    "Reset platform artifacts",
        "long": (
            "`reset_platform.py` deletes or cleans all auto-generated LLM folders for a chosen platform—function definitions, "
            "OpenAPI specs, client code, dispatchers, and services—with an optional dry-run mode to preview."
        ),
    },
    {
        "script":   "create_sdk.py",
        "function": "Create SDK",
        "short":    "Generate an OpenAPI-based SDK",
        "long": (
            "`create_sdk.py` prompts for an OpenAPI spec and folder name, runs `openapi-python-client` to build a Python SDK package, "
            "and updates `sdk_map.json` so you can import it in your code."
        ),
    },
    {
        "script":   "delete_sdk.py",
        "function": "Delete SDK",
        "short":    "Remove a generated SDK",
        "long": (
            "`delete_sdk.py` removes a specified SDK folder from `db_scripts/output_sdk/` and cleans up its entry in `sdk_map.json`."
        ),
    },
    {
        "script":   "create_platform_index.py",
        "function": "Create Platform Index",
        "short":    "Index platform functions",
        "long": (
            "`create_platform_index.py` lets you choose a platform’s function definitions and then embeds and indexes them "
            "into your active vector store (Chroma, Azure Search, or Elasticsearch) for retrieval."
        ),
    },
    {
        "script":   "create_domain_demo_index.py",
        "function": "Create Domain Demo Index",
        "short":    "Index a demo domain sample",
        "long": (
            "`create_domain_demo_index.py` lists the available `domain_samples`, processes the chosen sample (chunking, embedding), "
            "and indexes it into your vector store for domain-level demos."
        ),
    },
    {
        "script":   "convert_swagger2_to_openapi3.py",
        "function": "Convert Swagger v2",
        "short":    "Convert Swagger 2.0 spec → OpenAPI 3",
        "long": (
            "`convert_swagger2_to_openapi3.py` scans `db_scripts/source_swagger-2` for Swagger v2 files, "
            "lets you pick one, and invokes `swagger2openapi` to emit a valid OpenAPI 3 file into `src/source_open_api/`."
        ),
    },
]




# helpers

def list_existing_sdks() -> list[str]:
    return sorted(p.name for p in SDK_DIR.iterdir() if p.is_dir()) if SDK_DIR.exists() else []

def clear_screen() -> None:
    if sys.stdout.isatty():
        os.system("cls" if os.name == "nt" else "clear")

def list_definitions() -> list[str]:
    defs_dir = AGENT_ROOT / "llm" / "function_definitions"
    if not defs_dir.exists():
         return []
    return sorted(p.stem for p in defs_dir.glob("*.json") if p.is_file())
 
    if not defs_dir.exists():
        return []
    # each JSON file name (minus “.json”) is a platform short-name
    return sorted(p.stem for p in defs_dir.glob("*.json") if p.is_file())

# ── helper to render header + status ───────────────────────────────────────
def show_status() -> None:
    clear_screen()
    show_status()

    # --- STATUS SECTION ---
    pls  = list_definitions()
    sdks = list_existing_sdks()
    vec  = os.getenv("FASTAPI_VECTOR_BACKEND", "<none>")
    embed = os.getenv("FASTAPI_EMBEDDING_PROVIDER", "<none>")
    llm   = os.getenv("FASTAPI_LLM_PROVIDER", "<none>")

    # Concurrency settings
    azure_omp     = os.getenv("FASTAPI_AZURE_OMP_NUM_THREADS", "<none>")
    azure_mkl     = os.getenv("FASTAPI_AZURE_MKL_NUM_THREADS", "<none>")
    azure_cpus    = os.getenv("FASTAPI_AZURE_NUM_CPUS", "<none>")
    azure_workers = os.getenv("FASTAPI_AZURE_RETRIEVER_WORKERS", "<none>")

    chroma_omp     = os.getenv("FASTAPI_CHROMA_OMP_NUM_THREADS", "<none>")
    chroma_mkl     = os.getenv("FASTAPI_CHROMA_MKL_NUM_THREADS", "<none>")
    chroma_cpus    = os.getenv("FASTAPI_CHROMA_NUM_CPUS", "<none>")
    chroma_workers = os.getenv("FASTAPI_CHROMA_RETRIEVER_WORKERS", "<none>")

    elastic_omp     = os.getenv("FASTAPI_ELASTIC_NUM_THREADS", "<none>")
    elastic_mkl     = os.getenv("FASTAPI_ELASTIC_MKL_NUM_THREADS", "<none>")
    elastic_cpus    = os.getenv("FASTAPI_ELASTIC_NUM_CPUS", "<none>")
    elastic_workers = os.getenv("FASTAPI_ELASTIC_RETRIEVER_WORKERS", "<none>")

    # Chroma config
    c_e_batch = os.getenv("FASTAPI_CHROMA_EMBED_BATCH_SIZE", "<none>")
    c_chunk   = os.getenv("FASTAPI_CHROMA_CHUNK_SIZE", "<none>")
    c_overlap = os.getenv("FASTAPI_CHROMA_CHUNK_OVERLAP", "<none>")
    c_recreate= os.getenv("FASTAPI_CHROMA_RECREATE_INDEX", "<none>")
    c_coll    = os.getenv("FASTAPI_CHROMA_COLLECTION_PLATFORM", "<none>")
    c_db      = os.getenv("FASTAPI_CHROMA_DB_PATH", "<none>")
    c_kw_type = os.getenv("FASTAPI_CHROMA_KEYWORD_TYPE", "<none>")
    c_sum_type= os.getenv("FASTAPI_CHROMA_SUMMARIZER_TYPE", "<none>")
    c_kw_en   = os.getenv("FASTAPI_CHROMA_ENABLE_KEYWORDS", "<none>")
    c_sum_en  = os.getenv("FASTAPI_CHROMA_ENABLE_SUMMARIZATION", "<none>")

    # Azure config
    a_e_batch = os.getenv("FASTAPI_AZURE_EMBED_BATCH_SIZE", "<none>")
    a_chunk   = os.getenv("FASTAPI_AZURE_CHUNK_SIZE", "<none>")
    a_overlap = os.getenv("FASTAPI_AZURE_CHUNK_OVERLAP", "<none>")
    a_recreate= os.getenv("FASTAPI_AZURE_RECREATE_INDEX", "<none>")
    a_idx     = os.getenv("FASTAPI_AZURE_PLATFORM_INDEX", "<none>")
    a_endpoint= os.getenv("FASTAPI_AZURE_ENDPOINT", "<none>")
    a_api_ver = os.getenv("FASTAPI_AZURE_API_VERSION", "<none>")
    a_prechunk= os.getenv("FASTAPI_AZURE_INDEX_IS_PRECHUNKED", "<none>")
    a_query   = os.getenv("FASTAPI_AZURE_QUERY_TYPE", "<none>")
    a_strict  = os.getenv("FASTAPI_AZURE_STRICTNESS", "<none>")
    a_dom_en  = os.getenv("FASTAPI_AZURE_ENABLE_IN_DOMAIN", "<none>")
    a_semconf = os.getenv("FASTAPI_AZURE_PLATFORM_SEMCONF", "<none>")
    a_plat_sel= os.getenv("FASTAPI_AZURE_PLATFORM_SELECT", "<none>")
    a_vec_cols= os.getenv("FASTAPI_AZURE_VECTOR_COLUMNS", "<none>")
    a_dim     = os.getenv("FASTAPI_AZURE_DIM", "<none>")
    a_pls     = azure_list_platforms()
   

    # Elastic config
    e_e_batch = os.getenv("FASTAPI_ELASTIC_EMBED_BATCH_SIZE", "<none>")
    e_chunk   = os.getenv("FASTAPI_ELASTIC_CHUNK_SIZE", "<none>")
    e_overlap = os.getenv("FASTAPI_ELASTIC_CHUNK_OVERLAP", "<none>")
    e_recreate= os.getenv("FASTAPI_ELASTIC_RECREATE_INDEX", "<none>")
    e_idx     = os.getenv("FASTAPI_ELASTIC_PLATFORM_INDEX", "<none>")
    e_host    = os.getenv("FASTAPI_ELASTIC_HOST", "<none>")
    e_port    = os.getenv("FASTAPI_ELASTIC_PORT", "<none>")
    e_pls     = []

    grid = GridTable.grid(expand=True)
    grid.add_column(ratio=1)
    grid.add_column(ratio=1)
    grid.add_column(ratio=1)

    # General
    grid.add_row(
        f"[yellow]Existing Platforms[/yellow]:\n{', '.join(pls) or '(none)'}",
        f"[yellow]Created SDKs[/yellow]:\n{', '.join(sdks) or '(none)'}",
        f"[yellow]Active Vector Backend[/yellow]: [white]{vec}[/white]\n[yellow]Active Embedding Provider[/yellow]: [white]{embed}[/white]\n[yellow]Active LLM[/yellow]: [white]{llm}[/white]"
    )

    # blank line
    grid.add_row("", "", "")

    # Chroma
    grid.add_row(
        f"[yellow]Chroma[/yellow]",
        f"[yellow]Azure[/yellow]",
        f"[yellow]Elastic[/yellow]"
    )

    grid.add_row(
        # Chroma details
        f"[bright_blue]Index[/bright_blue]: [white]{c_coll}[/white]\n"
        f"[bright_blue]Platforms[/bright_blue]: [white]{', '.join(pls) or '(none)'}[/white]\n"
        f"[bright_blue]Concurrency[/bright_blue]: [white]OMP={chroma_omp}, MKL={chroma_mkl}, CPUs={chroma_cpus}, Workers={chroma_workers}[/white]\n"
        f"[bright_blue]Embed Batch Size[/bright_blue]: [white]{c_e_batch}[/white]\n"
        f"[bright_blue]Chunk Size[/bright_blue]: [white]{c_chunk}[/white]\n"
        f"[bright_blue]Chunk Overlap[/bright_blue]: [white]{c_overlap}[/white]\n"
        f"[bright_blue]Recreate Index[/bright_blue]: [white]{c_recreate}[/white]\n"
        f"[bright_blue]Collection Platform[/bright_blue]: [white]{c_coll}[/white]\n"
        f"[bright_blue]Database Path[/bright_blue]: [white]{c_db}[/white]\n"
        f"[bright_blue]Keyword Type[/bright_blue]: [white]{c_kw_type}[/white]\n"
        f"[bright_blue]Summarizer Type[/bright_blue]: [white]{c_sum_type}[/white]\n"
        f"[bright_blue]Enable Keywords[/bright_blue]: [white]{c_kw_en}[/white]\n"
        f"[bright_blue]Enable Summarization[/bright_blue]: [white]{c_sum_en}[/white]",
        # Azure details
        f"[bright_blue]Index[/bright_blue]: [white]{a_idx}[/white]\n"
        f"[bright_blue]Platforms[/bright_blue]: [white]{', '.join(a_pls) or '(none)'}[/white]\n"
        f"[bright_blue]Concurrency[/bright_blue]: [white]OMP={azure_omp}, MKL={azure_mkl}, CPUs={azure_cpus}, Workers={azure_workers}[/white]\n"
        f"[bright_blue]Embed Batch Size[/bright_blue]: [white]{a_e_batch}[/white]\n"
        f"[bright_blue]Chunk Size[/bright_blue]: [white]{a_chunk}[/white]\n"
        f"[bright_blue]Chunk Overlap[/bright_blue]: [white]{a_overlap}[/white]\n"
        f"[bright_blue]Recreate Index[/bright_blue]: [white]{a_recreate}[/white]\n"
        f"[bright_blue]Endpoint[/bright_blue]: [white]{a_endpoint}[/white]\n"
        f"[bright_blue]API Version[/bright_blue]: [white]{a_api_ver}[/white]\n"
        f"[bright_blue]Prechunked[/bright_blue]: [white]{a_prechunk}[/white]\n"
        f"[bright_blue]Query Type[/bright_blue]: [white]{a_query}[/white]\n"
        f"[bright_blue]Strictness[/bright_blue]: [white]{a_strict}[/white]\n"
        f"[bright_blue]Enable In Domain[/bright_blue]: [white]{a_dom_en}[/white]\n"
        f"[bright_blue]Semconf[/bright_blue]: [white]{a_semconf}[/white]\n"
        f"[bright_blue]Platform Select[/bright_blue]: [white]{a_plat_sel}[/white]\n"
        f"[bright_blue]Vector Columns[/bright_blue]: [white]{a_vec_cols}[/white]\n"
        f"[bright_blue]Dim[/bright_blue]: [white]{a_dim}[/white]",
        # Elastic details
        f"[bright_blue]Index[/bright_blue]: [white]{e_idx}[/white]\n"
        f"[bright_blue]Platforms[/bright_blue]: [white]{', '.join(e_pls) or '(none)'}[/white]\n"
        f"[bright_blue]Concurrency[/bright_blue]: [white]OMP={elastic_omp}, MKL={elastic_mkl}, CPUs={elastic_cpus}, Workers={elastic_workers}[/white]\n"
        f"[bright_blue]Embed Batch Size[/bright_blue]: [white]{e_e_batch}[/white]\n"
        f"[bright_blue]Chunk Size[/bright_blue]: [white]{e_chunk}[/white]\n"
        f"[bright_blue]Chunk Overlap[/bright_blue]: [white]{e_overlap}[/white]\n"
        f"[bright_blue]Recreate Index[/bright_blue]: [white]{e_recreate}[/white]\n"
        f"[bright_blue]Host[/bright_blue]: [white]{e_host}[/white]\n"
        f"[bright_blue]Port[/bright_blue]: [white]{e_port}[/white]"
    )



    console.print(Panel(grid, title="[bold yellow]Status[/bold yellow]", border_style="blue"))



# —————————————————————————————

# main

def main() -> None:



    # menu loop...
    exit_idx = len(COMMANDS) + 1
    while True:
        table = Table(box=box.SIMPLE)
        table.add_column("#", style="bold cyan", no_wrap=True)
        table.add_column("Function")
        table.add_column("Description")
        for idx, cmd in enumerate(COMMANDS, start=1):
            table.add_row(str(idx), cmd["function"], cmd["short"] )
        table.add_row(str(exit_idx), "Exit", "Quit the wizard")
        console.print(Panel(table, title="Select or Inspect Command", border_style="cyan"))

        choice = Prompt.ask("Enter number to run, or 'i<n>' for info (e.g. i2)")
        choice = choice.strip()

        if choice.lower().startswith("i"):
            num = choice[1:]
            if num.isdigit() and 1 <= (i := int(num)) <= len(COMMANDS):
                detail = COMMANDS[i-1]["long"]
                console.print(Panel(Markdown(detail), title=f"Info: {COMMANDS[i-1]['function']}", border_style="magenta"))
                Prompt.ask("Press Enter to return")
                clear_screen()
                continue
            console.print(f"[red]Invalid info request: {choice}[/red]")
            continue

        if choice.isdigit() and int(choice) == exit_idx:
            console.print("[green]Goodbye![/green]")
            sys.exit(0)

        if choice.isdigit() and 1 <= (sel := int(choice)) <= len(COMMANDS):
            script_name = COMMANDS[sel-1]["script"]
            script_path = UCMD_DIR / script_name
            if not script_path.exists():
                console.print(f"[red]Script not found: {script_path}[/red]")
                sys.exit(1)
            clear_screen()
            console.print(Panel.fit(f"🚀 Running {COMMANDS[sel-1]['function']}...", style="cyan"))
            subprocess.run([sys.executable, str(script_path)], check=True, cwd=str(AGENT_ROOT))
            console.print(Panel.fit(":white_check_mark: Done!", style="green"))

            # --- Ask whether to go back to menu or exit ---
            action = Prompt.ask(
                "\nWhat now? [b]m[/b]enu/[b]e[/b]xit",
                choices=["m", "e"],
                default="m"
            )
            if action == "e":
                console.print("\n[green]Goodbye![/green]")
                sys.exit(0)

            # back to menu: re-show header + status
            show_status()
            continue

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()
        sys.exit(1)

