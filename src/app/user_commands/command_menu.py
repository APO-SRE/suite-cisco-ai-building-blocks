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
import chromadb  
import logging
from dotenv import load_dotenv  
from pathlib import Path
from rich.console import Console, Group
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt
from rich.text import Text
from rich.align import Align
from rich import box
from rich.traceback import install
from rich.markdown import Markdown
from rich.table import Table as GridTable
from .create_platform_index import azure_list_platforms
from chromadb.config import Settings
from app.utils.paths import ensure_abs_env

load_dotenv() 
install()
console = Console()
logging.basicConfig(
    filename="chroma_debug.log",
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s",
)
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
    {   # 1
        "script":   "start_cisco_platform_ai.py",
        "function": "Start Cisco Platform AI",
        "short":    "Run FastAPI (hot-reload)",
        "long": (
            "`start_platform_agent.py` launches `uvicorn app.main:app --reload`, writes the "
            "PID to `.run/agent.pid`, and streams logs so you can hit `http://localhost:8000/docs`."
        ),
    },
    {   # 2
        "script":   "stop_cisco_platform_ai.py",
        "function": "Stop Cisco Platform AI",
        "short":    "Terminate FastAPI server",
        "long": (
            "`stop_platform_agent.py` reads `.run/agent.pid` and sends SIGTERM to stop the dev server.",
        ),
    },
    {   # 3
        "script":   "start_telemetry_stack.py",
        "function": "Start Telemetry Stack",
        "short":    "Bring up Tempo/Prometheus/Grafana via Docker Compose",
        "long": (
            "`start_telemetry_stack.py` will locate `docker/docker-compose.yaml` and run:\n\n"
            "```bash\n"
            "docker compose -f <repo_root>/docker/docker-compose.yaml up -d\n"
            "```\n\n"
            "This spins up Tempo (OTLP listener on port 4318), Prometheus (9090), and Grafana (3000) "
            "so your locally running FastAPI app can export traces and metrics. "
            "Use this when you need the full telemetry stack available."
        ),
    },
    {   # 4
        "script":   "stop_telemetry_stack.py",
        "function": "Stop Telemetry Stack",
        "short":    "Tear down Tempo/Prometheus/Grafana via Docker Compose",
        "long": (
            "`stop_telemetry_stack.py` will locate `docker/docker-compose.yaml` and run:\n\n"
            "```bash\n"
            "docker compose -f <repo_root>/docker/docker-compose.yaml down\n"
            "```\n\n"
            "This stops and removes the containers for Tempo, Prometheus, and Grafana. "
            "Use this when you want to free up ports or reset your telemetry stack."
        ),
        },
        {   # 5
            "script":   "status_application.py",
            "function": "Application Status",
            "short":    "Show FastAPI & telemetry stack status",
            "long": (
                "`status_application.py` clears your terminal and then:\n\n"
                "1. Checks if FastAPI is listening on port 8000 via `lsof`.\n"
                "2. Runs `docker compose -f <repo_root>/docker/docker-compose.yaml ps` to show the current status\n"
                "   of Tempo, Prometheus, and Grafana.\n\n"
                "Use this to quickly verify that both your API and telemetry components are up and running."
            ),
        },
    {   # 6
        "script":   "create_platform.py",
        "function": "Create Platform",
        "short":    "Scaffold a new platform",
        "long": (
            "`create_platform.py` guides you through naming a platform, selecting its SDK module and "
            "OpenAPI spec, configuring HTTP methods and operation-ID filters, then generates all LLM "
            "artifacts: function definitions, full OpenAPI specs, client stubs, dispatchers, and services."
        ),
    },
    {   # 7
        "script":   "reset_platform.py",
        "function": "Delete Platform",
        "short":    "Delete platform artifacts",
        "long": (
            "`reset_platform.py` deletes or cleans all auto-generated LLM folders for a chosen platform—"
            "function definitions, OpenAPI specs, client code, dispatchers, and services—with an optional "
            "dry-run mode to preview."
        ),
    },
    {   # 8
        "script":   "create_sdk.py",
        "function": "Create SDK",
        "short":    "Generate an OpenAPI-based SDK",
        "long": (
            "`create_sdk.py` prompts for an OpenAPI spec and folder name, runs `openapi-python-client` "
            "to build a Python SDK package, and updates `platform_registry.json` so you can import it."
        ),
    },
    {   # 9
        "script":   "delete_sdk.py",
        "function": "Delete SDK",
        "short":    "Remove a generated SDK",
        "long": (
            "`delete_sdk.py` removes a specified SDK folder from `db_scripts/output_sdk/` and cleans up "
            "its entry in `platform_registry.json`."
        ),
    },
    {   # 10
        "script":   "create_platform_index.py",
        "function": "Create Platform Index",
        "short":    "Index platform functions",
        "long": (
            "`create_platform_index.py` lets you choose a platform’s function definitions and then embeds "
            "and indexes them into your active vector store (Chroma, Azure Search, or Elasticsearch) for retrieval."
        ),
    },
    {   # 11
        "script":   "create_domain_demo_index.py",
        "function": "Create Domain Demo Index",
        "short":    "Index a demo domain sample",
        "long": (
            "`create_domain_demo_index.py` lists the available `domain_samples`, processes the chosen sample "
            "(chunking, embedding), and indexes it into your vector store for domain-level demos."
        ),
    },
    {   # 12
        "script":   "create_events_index.py",
        "function": "Create Events Index",
        "short":    "Index an events JSON sample",
        "long": (
            "`create_events_index.py` lists available event JSON files in `src/db_scripts/events`, sets "
            "`EVENTS_SAMPLES_DIR`, and invokes `db_scripts.process_events` to embed and index them."
        ),
    },
    {   # 13
        "script":   "create_platform_route.py",
        "function": "Create Platform Route",
        "short":    "Add new FastAPI platform routes",
        "long": "`create_platform_route.py` walks you through creating and registering new platform routes in `app/routers`.",
    },
    {   # 14
        "script":   "delete_platform_routes.py",
        "function": "Delete Platform Routes",
        "short":    "Remove FastAPI routes for a platform",
        "long": "`delete_platform_routes.py` lists all route files under `src/app/routers/` and lets you remove the ones you choose.",
    },
    {   # 15
        "script":   "list_platform_registry.py",
        "function": "List Platform Registry",
        "short":    "Show Platform Registry",
        "long": (
            "`list_platform_registry.py` presents the current contents of `platform_registry.json` in "
            "a read-only Rich table, including icons indicating whether each platform was generated "
            "in-house and whether its scaffolding is detected in the repo."
        ),
    },
    {   # 16  
        "script":   "update_platform_registry.py",
        "function": "Update Platform Registry",
        "short":    "Add / edit platform entries",
        "long": (
            "`update_platform_registry.py` opens an interactive wizard to add, edit, or delete records in "
            "`platform_registry.json`, and auto-detects whether each platform’s scaffolding is installed."
        ),
    },
    {   # 17
        "script":   "sync_registry_with_scaffold.py",
        "function": "Sync Platform Registry",
        "short":    "Reconcile registry with files",
        "long": (
            "`sync_registry_with_scaffold.py` scans the four scaffold folders "
            "(`function_definitions`, `platform_clients`, `function_dispatcher`, "
            "`unified_service`) and then:\n"
            " • flips each platform’s **installed** flag to ✔ or ✖ to match what’s on disk;\n"
            " • adds a *stub* entry for any newly-found platform that isn’t yet in "
            "`platform_registry.json`.\n\n"
            "Run it after manual file deletions, bulk imports, or any time you’re unsure "
            "the registry reflects reality."
        ),
    },
    {   # 18
        "script":   "convert_swagger2_to_openapi3.py",
        "function": "Convert Swagger v2",
        "short":    "Convert Swagger 2.0 spec → OpenAPI 3",
        "long": (
            "`convert_swagger2_to_openapi3.py` scans `db_scripts/source_swagger-2` for Swagger v2 files, lets you pick one, "
            "and invokes `swagger2openapi` to emit a valid OpenAPI 3 file into `src/source_open_api/`."
        ),
    },
    {   # 19
    "script":   "manage_.env.py",
    "function": "Manage .env File",
    "short":    "Edit Environment Variables",
    "long": (
        "`manage_.env.py` launches an interactive editor for your `.env` file, allowing you to "
        "view, add, edit, and delete environment variables—including their allowed‐values comments—"
        "while masking any secret keys or tokens."
        ),
    },
    {   # 20
        "script":   "cisco_api_docs.py",
        "function": "Cisco API Docs",
        "short":    "Open Cisco API docs in browser",
        "long": (
            "`cisco_api_docs.py` presents an interactive list of Cisco API doc hubs "
            "(DevNet catalog, Meraki, Webex, Catalyst Center, Umbrella, SecureX, etc.). "
            "Enter a number to launch that page in your default browser, or type "
            "`i<n>` (e.g. i2) for a detailed description without opening a link."
        ),
    },
]


 


# helpers

def list_existing_sdks() -> list[str]:
    return sorted(p.name for p in SDK_DIR.iterdir() if p.is_dir()) if SDK_DIR.exists() else []

def clear_screen() -> None:
    if sys.stdout.isatty():
        os.system("cls" if os.name == "nt" else "clear")


# ─── helper: list which platforms are already in Chroma ─────────────
def chroma_list_platforms() -> list[str]:
    """
    Return a list of distinct `platform` values stored in all Chroma collections
    under FASTAPI_CHROMA_DB_PATH (one folder per collection).
    """
    db_root = ensure_abs_env("FASTAPI_CHROMA_DB_PATH", "chroma_dbs/fastapi")
    found: set[str] = set()

    for coll_dir in db_root.iterdir():
        if not coll_dir.is_dir() or not (coll_dir / "chroma.sqlite3").exists():
            continue

        client = chromadb.PersistentClient(
            path=str(coll_dir),
            settings=Settings(anonymized_telemetry=False),
        )
        try:
            col = client.get_collection(coll_dir.name)
        except (KeyError, ValueError):
            # drop this client and move on
            continue

        metas = col.get(where={}, include=["metadatas"], limit=100_000)["metadatas"]
        for m in metas:
            plat = m.get("platform")
            if plat:
                found.add(plat)

    return sorted(found)
 
 


 

def list_definitions() -> list[str]:
    defs_dir = AGENT_ROOT / "llm" / "function_definitions"
    if not defs_dir.exists():
         return []
    return sorted(p.stem for p in defs_dir.glob("*.json") if p.is_file())
 
 

# ── helper to render header + status ───────────────────────────────────────
def show_status() -> None:
    load_dotenv(override=True)
    clear_screen()

  
    title    = Text("🛠  Cisco Platform AI Agent Menu  🛠", style="bold bright_green")
    subtitle = Text("EXPERIENCE the POWER of CISCO PLATFORMS", style="bright_cyan")
    footer   = Text(
        "Powered by Cisco AI Building Blocks — AI for cloud, hybrid, and on-prem environments",
        style="bright_white"
    )

    header = Panel(
        Group(
            Align.center(title),
            Align.center(subtitle),
            Align.center(footer),
        ),
        border_style="green",
        padding=(1, 2),
    )
    console.print(header)
  
 

    c_coll = os.getenv("FASTAPI_CHROMA_COLLECTION_PLATFORM", "<none>")
    c_db   = os.getenv("FASTAPI_CHROMA_DB_PATH",            "<none>")

    a_idx      = os.getenv("FASTAPI_AZURE_PLATFORM_INDEX",       "<none>")
    a_endpoint = os.getenv("FASTAPI_AZURE_ENDPOINT",             "<none>")
 
    e_idx  = os.getenv("FASTAPI_ELASTIC_PLATFORM_INDEX", "<none>")
    e_host = os.getenv("FASTAPI_ELASTIC_HOST",           "<none>")

    pls  = list_definitions()
    sdks = list_existing_sdks()
    scaffolded = list_definitions()
    vec  = os.getenv("FASTAPI_VECTOR_BACKEND", "<none>")
    embed = os.getenv("FASTAPI_EMBEDDING_PROVIDER", "<none>")
    llm   = os.getenv("FASTAPI_LLM_PROVIDER", "<none>")


  
    indexed_chroma = chroma_list_platforms()  # → "catalyst, meraki"
    indexed_azure  = azure_list_platforms()   # → ["meraki",…]




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
    indexed_elastic = ", ".join(e_pls) or "(none)"
    rel_db = os.path.relpath(c_db, start=Path(__file__).resolve().parents[3])
    grid = GridTable.grid(expand=True)
    grid.add_column(ratio=1)
    grid.add_column(ratio=1)
    grid.add_column(ratio=1)

    # ── HEADER ROW ───────────────────────────────────────────────
    grid.add_row(
        "[bold blue]PLATFORM[/bold blue]",
        "[bold blue]INDEXES[/bold blue]",
        "[bold blue]FASTAPI ACTIVE BACKEND SETTINGS[/bold blue]",
    )
    # ─────────────────────────────────────────────────────────────────


    # Row 1: scaffolded vs indexed vs vector backend
    grid.add_row(
        f"[yellow]Scaffolded[/yellow]:\n{', '.join(scaffolded) or '(none)'}",
        f"[yellow]Chroma Indexed[/yellow]:\n{', '.join(indexed_chroma) or '(none)'}",
        f"[yellow]Active Vector Backend[/yellow]:\n[white]{vec}[/white]"
    )

    # Row 2: SDKs vs Azure indexed vs embedding provider
    grid.add_row(
        f"[yellow]Created SDKs[/yellow]:\n{', '.join(sdks) or '(none)'}",
        f"[yellow]Azure Indexed[/yellow]:\n{', '.join(indexed_azure) or '(none)'}",
        f"[yellow]Active Embedding Provider[/yellow]:\n[white]{embed}[/white]"
    )

 
    # Row 3  →  Elastic Indexed + Active LLM Provider
    grid.add_row(
        "",                                                     # col-1 still blank
        f"[yellow]Elastic Indexed[/yellow]:\n{indexed_elastic}",# col-2
        f"[yellow]Active LLM Provider[/yellow]:\n[white]{llm}[/white]"  # col-3
    )


 

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
        f"[bright_blue]Platforms[/bright_blue]: [white]{', '.join(indexed_chroma) or '(none)'}[/white]\n"
        #f"[bright_blue]DB Path[/bright_blue]: {c_db}\n"
        f"[bright_blue]Concurrency[/bright_blue]: [white]OMP={chroma_omp}, MKL={chroma_mkl}, CPUs={chroma_cpus}, Workers={chroma_workers}[/white]\n"
        f"[bright_blue]Embed Batch Size[/bright_blue]: [white]{c_e_batch}[/white]\n"
        f"[bright_blue]Chunk Size[/bright_blue]: [white]{c_chunk}[/white]\n"
        f"[bright_blue]Chunk Overlap[/bright_blue]: [white]{c_overlap}[/white]\n"
        f"[bright_blue]Recreate Index[/bright_blue]: [white]{c_recreate}[/white]\n"
        f"[bright_blue]Collection Platform[/bright_blue]: [white]{c_coll}[/white]\n"
        f"[bright_blue]Database Path[/bright_blue]: [white]{rel_db}[/white]\n"
        f"[bright_blue]Keyword Type[/bright_blue]: [white]{c_kw_type}[/white]\n"
        f"[bright_blue]Summarizer Type[/bright_blue]: [white]{c_sum_type}[/white]\n"
        f"[bright_blue]Enable Keywords[/bright_blue]: [white]{c_kw_en}[/white]\n"
        f"[bright_blue]Enable Summarization[/bright_blue]: [white]{c_sum_en}[/white]",
        # Azure details
        f"[bright_blue]Index[/bright_blue]: [white]{a_idx}[/white]\n"
        f"[bright_blue]Platforms[/bright_blue]: [white]{', '.join(a_pls) or '(none)'}[/white]\n"
        f"[bright_blue]Endpoint[/bright_blue]: {a_endpoint}\n"
        f"[bright_blue]Concurrency[/bright_blue]: [white]OMP={azure_omp}, MKL={azure_mkl}, CPUs={azure_cpus}, Workers={azure_workers}[/white]\n"
        f"[bright_blue]Embed Batch Size[/bright_blue]: [white]{a_e_batch}[/white]\n"
        f"[bright_blue]Chunk Size[/bright_blue]: [white]{a_chunk}[/white]\n"
        f"[bright_blue]Chunk Overlap[/bright_blue]: [white]{a_overlap}[/white]\n"
        f"[bright_blue]Recreate Index[/bright_blue]: [white]{a_recreate}[/white]\n"
        #f"[bright_blue]Endpoint[/bright_blue]: [white]{a_endpoint}[/white]\n"
        f"[bright_blue]API Version[/bright_blue]: [white]{a_api_ver}[/white]\n"
        f"[bright_blue]Prechunked[/bright_blue]: [white]{a_prechunk}[/white]\n"
        f"[bright_blue]Query Type[/bright_blue]: [white]{a_query}[/white]\n"
        f"[bright_blue]Strictness[/bright_blue]: [white]{a_strict}[/white]\n"
        f"[bright_blue]Enable In Domain[/bright_blue]: [white]{a_dom_en}[/white]\n"
        f"[bright_blue]Semconf[/bright_blue]: [white]{a_semconf}[/white]\n"
        f"[bright_blue]Platform Select[/bright_blue]: [white]{a_plat_sel}[/white]\n", # last line in column needs a comma
        #f"[bright_blue]Vector Columns[/bright_blue]: [white]{a_vec_cols}[/white]\n"
        #f"[bright_blue]Dim[/bright_blue]: [white]{a_dim}[/white]",
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

#-------------------------------------------------------------------------------

def main() -> None:
    exit_idx = len(COMMANDS) + 1

    while True:
        # 1) Clear + show full status each time
        show_status()

        # 2) Build & show the menu  ──────────────────────────────────────────
        # Split commands evenly (first col gets the extra if odd)
        total_rows      = len(COMMANDS) + 1           # +1 for Exit
        first_col_rows  = (total_rows + 1) // 2       # → 9 when total_rows = 17
        second_col_rows = total_rows - first_col_rows # → 8

        # Helper that returns a new Rich Table pre-configured
        def _new_col_table() -> Table:
            t = Table(box=box.SIMPLE, pad_edge=False, expand=True)
            t.add_column("#",           style="bold cyan", no_wrap=True)
            t.add_column("Function")
            return t

        left  = _new_col_table()
        right = _new_col_table()

        # Fill the two tables
        for idx in range(1, total_rows + 1):
            if idx == total_rows:  # Exit row
                row = (str(idx), "Exit")
            else:
                cmd = COMMANDS[idx - 1]
                row = (str(idx), cmd["function"])

            (left if idx <= first_col_rows else right).add_row(*row)

        # Wrap both tables in one grid so they share headers
        grid = Table.grid(expand=True)
        grid.add_column(ratio=1)
        grid.add_column(ratio=1)

        # Header row (same for both columns)
        header = ["#", "Function"]
        grid.add_row(
            Table.grid().add_row(*[f"[bold]{h}[/bold]" for h in header]),
            Table.grid().add_row(*[f"[bold]{h}[/bold]" for h in header]),
        )
        grid.add_row(left, right)  # actual tables

        console.print(
            Panel(
                grid,
                title="Select or Inspect Command",
                border_style="cyan",
            )
        )

        # 3) Prompt for choice
        choice = Prompt.ask("Enter number or 'i<n>' for info").strip()

        # 4) Info view
        if choice.lower().startswith("i"):
            num = choice[1:]
            if num.isdigit() and 1 <= (i := int(num)) <= len(COMMANDS):
                console.print(
                    Panel(
                        Markdown(COMMANDS[i-1]["long"]),
                        title=f"Info: {COMMANDS[i-1]['function']}",
                        border_style="magenta",
                    )
                )
                Prompt.ask("Press Enter to return")
            continue  # loop back, will re-print status + menu

        # 5) Exit
        if choice.isdigit() and int(choice) == exit_idx:
            console.print("[green]Goodbye![/green]")
            sys.exit(0)

        # 6) Run a command
        if choice.isdigit() and 1 <= (sel := int(choice)) <= len(COMMANDS):
            script = UCMD_DIR / COMMANDS[sel-1]["script"]
            clear_screen()
            console.print(f"🚀 Running {COMMANDS[sel-1]['function']}…")
            subprocess.run([sys.executable, str(script)], check=True, cwd=str(AGENT_ROOT))
            console.print(":white_check_mark: Done!")
            #show_status()
            action = Prompt.ask("What now? [b]m[/b]enu/[b]e[/b]xit", choices=["m", "e"], default="m")
            if action == "e":
                console.print("[green]Goodbye![/green]")
                sys.exit(0)
            # on "m" we simply continue, which will re-print status + menu

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()
        sys.exit(1)