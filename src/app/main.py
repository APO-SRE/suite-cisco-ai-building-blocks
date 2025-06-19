#!/usr/bin/env python3
from __future__ import annotations
################################################################################
## suite-cisco-ai-building-blocks/src/app/main.py
## Copyright (c) 2025 Jeff Teeter
## Cisco Systems, Inc.
## Licensed under the Apache License, Version 2.0 (see LICENSE)
## Distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND.
################################################################################

"""
DISCLAIMER: USE AT YOUR OWN RISK

This software is provided "as is", without any express or implied warranties, including, but not limited to,
the implied warranties of merchantability and fitness for a particular purpose. In no event shall the authors or
contributors be liable for any direct, indirect, incidental, special, exemplary, or consequential damages
(including, but not limited to, procurement of substitute goods or services; loss of use, data, or profits;
or business interruption) however caused and on any theory of liability, whether in contract, strict liability,
or tort (including negligence or otherwise) arising in any way out of the use of this software.

This script is provided for demonstration and development purposes only and is not intended for use in production
environments. You are solely responsible for any modifications or adaptations made for your specific use case.

By using this code, you agree that you have read, understood, and accept these terms.
"""
import importlib
from dotenv import load_dotenv
load_dotenv()

import logging
import structlog
import os
from pathlib import Path
from typing import Annotated, Any, Tuple

from fastapi import Depends, FastAPI, HTTPException, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from app.user_commands.update_platform_registry import load_registry
from prometheus_client import Histogram

from app.config import cfg
from app.telemetry_helper import init_telemetry_helper  # <— our helper

# ── structured logging ─────────────────────────────────────────
structlog.configure(
    wrapper_class=structlog.make_filtering_bound_logger(logging.INFO),
    processors=[
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.JSONRenderer(),
    ],
)
log = structlog.get_logger("ai-agent")

# ── Optional retrievers import ─────────────────────────────────
try:
    from app.retrievers.chroma_retriever import ChromaRetriever
except ImportError as exc:
    ChromaRetriever = None
    logging.warning("Chroma retriever unavailable – %s", exc)

try:
    from app.retrievers.azure_search_retriever import AzureSearchRetriever
except ImportError as exc:
    AzureSearchRetriever = None
    logging.warning("Azure Search retriever unavailable – %s", exc)

# ── Logging setup ───────────────────────────────────────────────
logger = logging.getLogger("ai_agent")
logging.basicConfig(
    level=os.getenv("LOG_LEVEL", "INFO"),
    format="%(levelname)s: %(message)s",
)

# ── FastAPI app instantiation ──────────────────────────────────
app = FastAPI(title="AI Building Blocks Agent", version="0.3.0-dev")

# ── Initialize telemetry: tracing + metrics ───────────────────
init_telemetry_helper(app)

# ── Custom histogram: /chat latency ───────────────────────────
request_latency = Histogram(
    "chat_latency_ms",
    "End-to-end latency of /chat route in milliseconds",
)
# ── Check Platform Enabled, Routes, etc.. ───────────────────────────

log = logging.getLogger("uvicorn.error")
registry = load_registry()

def check_credentials(short: str) -> Tuple[bool, str]:
    """
    Return (True, "") if all needed env vars for `short` are non-empty;
    otherwise return (False, reason).
    """
    if short == "ai_defense":
        needed = ["AI_DEFENSE_API_KEY"]
    elif short == "catalyst":
        needed = ["DNACENTER_USERNAME", "DNACENTER_PASSWORD", "DNACENTER_BASE_URL"]
    elif short == "cloudlock":
        needed = ["CLOUDLOCK_API_KEY", "CLOUDLOCK_API_SECRET"]
    elif short == "intersight":
        needed = ["INTERSIGHT_API_KEY", "INTERSIGHT_API_SECRET", "INTERSIGHT_BASE_URL"]
    elif short == "meraki":
        needed = ["CISCO_MERAKI_API_KEY"]
    elif short == "nexus_dashboard":
        needed = ["NEXUS_DASHBOARD_API_KEY", "NEXUS_DASHBOARD_BASE_URL"]
    elif short == "nexus_hyperfabric":
        needed = ["NEXUS_HYPERFABRIC_BEARER_TOKEN",
                  "NEXUS_HYPERFABRIC_BASE_URL"]
    elif short == "sdwan_mngr":
        needed = ["CISCO_SD_WAN_USERNAME",
                  "CISCO_SD_WAN_PASSWORD",
                  "CISCO_SD_WAN_BASE_URL"]
    elif short == "secure_access":
        needed = ["SECURE_ACCESS_CLIENT_ID",
                  "SECURE_ACCESS_CLIENT_SECRET",
                  "SECURE_ACCESS_TOKEN_URL"]
    elif short == "umbrella":
        needed = ["UMBRELLA_API_KEY", "UMBRELLA_API_SECRET"]
    else:
        return True, ""  # no credentials needed

    missing = [k for k in needed if not os.getenv(k)]
    if missing:
        return False, f"missing {', '.join(missing)}"
    return True, ""

for short, entry in registry.items():
    wants_route = bool(entry.get("route", False))
    sdk_module  = entry.get("sdk_module", "").strip()
    env_flag    = os.getenv(f"ENABLE_{short.upper()}", "false").lower() == "true"
    has_sdk     = False
    reason      = ""

    if not wants_route:
        reason = "route not scaffolded"
    elif not sdk_module:
        reason = "no sdk_module set"
    else:
        try:
            importlib.import_module(sdk_module)
            has_sdk = True
        except Exception as e:
            has_sdk = False
            reason = f"could not import SDK '{sdk_module}' ({e})"

    if not wants_route or not sdk_module or not has_sdk:
        log.info(f"Skipping '{short}': {reason}")
        continue

    if not env_flag:
        log.info(f"Skipping '{short}': ENABLE_{short.upper()} is false or missing")
        continue

    creds_ok, cred_reason = check_credentials(short)
    if not creds_ok:
        log.warning(f"Skipping '{short}': {cred_reason}")
        continue

    # All checks passed → import & mount router
    module_name = f"app.routers.{short}_routes"
    try:
        router_mod = importlib.import_module(module_name)
    except Exception as e:
        log.warning(f"Skipping '{short}': router module not found or error ({e})")
        continue

    if not hasattr(router_mod, "router"):
        log.warning(f"Skipping '{short}': no 'router' attribute in {module_name}")
        continue

    app.include_router(router_mod.router)
    log.info(f"Mounted routes for platform '{short}'")


# ── Static & assets ────────────────────────────────────────────
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# 1) Your UI lives under src/app/static
STATIC_DIR = Path(__file__).resolve().parent / "static"

# 2) Your images (logo, favicon, etc) live under src/app/assets
ASSETS_DIR = Path(__file__).resolve().parent / "assets"

# serve the assets at /assets
app.mount("/assets", StaticFiles(directory=ASSETS_DIR), name="assets")

# serve the rest of the UI under /static
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

 

@app.get("/", tags=["meta"], response_class=HTMLResponse)
async def root() -> HTMLResponse:
    """
    Single-page chat UI (opens *static/index.html*).
    """
    index_path = STATIC_DIR / "index.html"
    if not index_path.exists():
        return HTMLResponse(
            "<h2>index.html not found — did you copy the static folder?</h2>",
            status_code=404,
        )
    return HTMLResponse(index_path.read_text(encoding="utf-8"), status_code=200)

# ── CORS ───────────────────────────────────────────────────────
origins = cfg("CORS_ORIGINS", cast=str, default="*") or "*"
app.add_middleware(
    CORSMiddleware,
    allow_origins=[origins] if origins != "*" else ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── Startup: choose vector retriever ───────────────────────────
@app.on_event("startup")
async def _startup() -> None:
    layer    = cfg("ACTIVE_LAYER", default="FASTAPI").upper()
    backend  = cfg("VECTOR_BACKEND", layer=layer,
                   default=os.getenv("FASTAPI_VECTOR_BACKEND", "chroma")).lower()
    provider = cfg("LLM_PROVIDER", layer=layer,
                   default=os.getenv("FASTAPI_LLM_PROVIDER", "azure"))

    logger.info("=== AI-Agent startup ===")
    logger.info("Layer=%s | VectorBackend=%s | LLM=%s", layer, backend, provider)

    if backend == "chroma":
        if ChromaRetriever is None:
            raise RuntimeError("chromadb not installed but VECTOR_BACKEND='chroma'.")
        app.state.retriever = ChromaRetriever(layer=layer)
    elif backend in {"azure", "azure_search", "azsearch"}:
        if AzureSearchRetriever is None:
            raise RuntimeError("Azure Search retriever dependencies missing.")
        app.state.retriever = AzureSearchRetriever(layer=layer)
    else:
        logger.warning("Unknown VECTOR_BACKEND '%s' – retriever disabled.", backend)
        app.state.retriever = None

    if not cfg("VECTOR_ENABLED", layer=layer, cast=bool, default=True):
        logger.warning("%s: VECTOR layer disabled – using NullRetriever.", layer)
        from app.retrievers.null_retriever import NullRetriever
        app.state.retriever = NullRetriever()
        return

# ── Dependency injection helper ───────────────────────────────
def get_retriever(request: Request):
    r = getattr(request.app.state, "retriever", None)
    if r is None:
        raise HTTPException(404, "Vector retriever not configured.")
    return r

RetrieverDep = Annotated[Any, Depends(get_retriever)]

# ── Sample utility endpoints ─────────────────────────────────
@app.get("/search")
async def search_endpoint(q: str, retriever: RetrieverDep):
    if hasattr(retriever, "query"):
        return retriever.query(q, k=5)
    return {"error": "Retriever does not implement 'query'."}

@app.get("/health", tags=["meta"])
async def health():
    return {"status": "ok", "layer": cfg("ACTIVE_LAYER", default="FASTAPI")}

# ── Routers ───────────────────────────────────────────────────
try:
    from app.routers import chat_routes          # noqa: WPS433
    app.include_router(chat_routes.router, prefix="/chat")
except ImportError as exc:
    logger.warning("chat_routes not present – skipping (%s).", exc)

try:
    from app.routers.meraki_routes import router as meraki_router
    app.include_router(meraki_router)  
    logger.info("Mounted Meraki routes")
except ImportError as exc:
    logger.warning("meraki_routes not present – skipping (%s)", exc)