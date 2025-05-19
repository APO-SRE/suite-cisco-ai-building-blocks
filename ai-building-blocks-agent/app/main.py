#!/usr/bin/env python3
from __future__ import annotations
################################################################################
## ai-building-blocks-agent/app/main.py
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
import logging, structlog, os
from pathlib import Path
from typing import Annotated, Any

from fastapi import Depends, FastAPI, HTTPException, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from prometheus_client import Histogram, generate_latest
from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from app.config import cfg

# -------- structured logging ---------
structlog.configure(
    wrapper_class=structlog.make_filtering_bound_logger(logging.INFO),
    processors=[
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.JSONRenderer()
    ],
)
log = structlog.get_logger("ai-agent")




# Optional retrievers (import-guarded so the app can start without them)
try:
    from retrievers.chroma_retriever import ChromaRetriever
except ImportError as exc:
    ChromaRetriever = None
    logging.warning("Chroma retriever unavailable – %s", exc)

try:
    from retrievers.azure_search_retriever import AzureSearchRetriever
except ImportError as exc:
    AzureSearchRetriever = None
    logging.warning("Azure Search retriever unavailable – %s", exc)

# ─────────────────────────────────────────────────────────────────────────────
# Logging setup
# ─────────────────────────────────────────────────────────────────────────────
logger = logging.getLogger("ai_agent")
logging.basicConfig(
    level=os.getenv("LOG_LEVEL", "INFO"),
    format="%(levelname)s: %(message)s",
)

# ─────────────────────────────────────────────────────────────────────────────
# FastAPI app + Prometheus metric
# ─────────────────────────────────────────────────────────────────────────────
app = FastAPI(title="AI Building Blocks Agent", version="0.3.0-dev")

# Global histogram – used by chat route to record end-to-end latency
request_latency = Histogram(
    "chat_latency_ms",
    "End-to-end latency of /chat route in milliseconds",
)

@app.get("/metrics")
def metrics() -> Response:
    """
    Prometheus scrape endpoint
    """
    return Response(generate_latest(), media_type="text/plain")

# ---------- OpenTelemetry ------------
if os.getenv("OTEL_EXPORTER_OTLP_ENDPOINT", "http://localhost:4317"):
    tp = TracerProvider(resource=Resource.create({"service.name": "ai-agent"}))
    tp.add_span_processor(
        BatchSpanProcessor(OTLPSpanExporter())
    )
    trace.set_tracer_provider(tp)

tracer = trace.get_tracer(__name__)

# FastAPI / requests auto-instrument
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
# later, right after `app = FastAPI()`:
FastAPIInstrumentor().instrument_app(app)
RequestsInstrumentor().instrument()
# ───────────────────────────────────────────────────────────────────────


# ─────────────────────────────────────────────────────────────────────────────
# Static & assets
# ─────────────────────────────────────────────────────────────────────────────
PROJECT_ROOT = Path(__file__).resolve().parent.parent
STATIC_DIR   = PROJECT_ROOT / "static"
ASSETS_DIR   = PROJECT_ROOT / "app" / "assets"

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
app.mount("/assets", StaticFiles(directory=ASSETS_DIR), name="assets")

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

# ─────────────────────────────────────────────────────────────────────────────
# CORS
# ─────────────────────────────────────────────────────────────────────────────
origins = cfg("CORS_ORIGINS", cast=str, default="*") or "*"
app.add_middleware(
    CORSMiddleware,
    allow_origins=[origins] if origins != "*" else ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ─────────────────────────────────────────────────────────────────────────────
# Startup: choose vector retriever
# ─────────────────────────────────────────────────────────────────────────────
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

    # Honour <LAYER>_VECTOR_ENABLED
    if not cfg("VECTOR_ENABLED", layer=layer, cast=bool, default=True):
        logger.warning("%s: VECTOR layer disabled – using NullRetriever.", layer)
        from retrievers.null_retriever import NullRetriever
        app.state.retriever = NullRetriever()
        return

# ─────────────────────────────────────────────────────────────────────────────
# Dependency injection helper
# ─────────────────────────────────────────────────────────────────────────────
def get_retriever(request: Request):
    r = getattr(request.app.state, "retriever", None)
    if r is None:
        raise HTTPException(404, "Vector retriever not configured.")
    return r

RetrieverDep = Annotated[Any, Depends(get_retriever)]

# ─────────────────────────────────────────────────────────────────────────────
# Sample utility endpoints
# ─────────────────────────────────────────────────────────────────────────────
@app.get("/search")
async def search_endpoint(q: str, retriever: RetrieverDep):
    if hasattr(retriever, "query"):
        return retriever.query(q, k=5)
    return {"error": "Retriever does not implement 'query'."}

@app.get("/health", tags=["meta"])
async def health():
    return {"status": "ok", "layer": cfg("ACTIVE_LAYER", default="FASTAPI")}

# ─────────────────────────────────────────────────────────────────────────────
# Routers
# ─────────────────────────────────────────────────────────────────────────────
try:
    from app.routers import chat_routes          # noqa: WPS433
    app.include_router(chat_routes.router, prefix="/chat")
except ImportError as exc:
    logger.warning("chat_routes not present – skipping (%s).", exc)
try:
    from app.routers.meraki_routes import router as meraki_router
    app.include_router(meraki_router)    # no prefix, since your paths start with /meraki
    logger.info("Mounted Meraki routes")
except ImportError as exc:
    logger.warning("meraki_routes not present – skipping (%s)", exc)