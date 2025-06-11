#!/usr/bin/env python3
from __future__ import annotations
################################################################################
## AI-Building-Blocks-Agent/app/telemetry_helper.py              ★ NEW VERSION ★
################################################################################
"""
OpenTelemetry bootstrap for FastAPI **plus** a smart span-callback that
adds `peer.service` based on host or path so the Tempo service-graph
looks friendly.
"""
import os, logging
from urllib.parse import urlparse
from typing import Dict

from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from prometheus_fastapi_instrumentator import Instrumentator
from opentelemetry.sdk.trace.sampling import ALWAYS_OFF

# ------------------------------------------------------------------- #
# 1. Your *routing table* – tweak / extend whenever you add services  #
# ------------------------------------------------------------------- #
_PEER_ROUTE_MAP: Dict[str, str] = {
    # host:port  → peer.service
    "vector-db.internal:9200": "chroma",
    "api.openai.com":          "openai",

    # path-prefix → peer.service
    "/search":                 "retriever",
    "/infer":                  "llm-worker",
    "/metrics":                "prometheus",
}

_DEFAULT_PEER = "external"

def _tag_peer(span, request, response):           # <- used for requests & httpx
    """
    Add   • peer.service
          • http.method & status_code   (nice for trace search)
    """
    try:
        # generic HTTP attributes
        span.set_attribute("http.method", request.method)
        if response is not None:
            span.set_attribute("http.status_code", getattr(response, "status_code", 0))

        # --- decide the logical downstream service -------------------
        url      = urlparse(str(request.url))
        hostport = url.netloc.lower()
        path     = url.path or "/"

        peer = _PEER_ROUTE_MAP.get(hostport)
        if peer is None:                          # try path prefixes
            for prefix, name in _PEER_ROUTE_MAP.items():
                if path.startswith(prefix):
                    peer = name
                    break
        if peer is None:
            peer = _DEFAULT_PEER

        span.set_attribute("peer.service", peer)
    except Exception as exc:                      # never break tracing
        logging.getLogger(__name__).debug("peer-cb error: %s", exc)


# ------------------------------------------------------------------- #
# 2. public helper called from `app/main.py`                           #
# ------------------------------------------------------------------- #
def init_telemetry_helper(app):
    """
    Initialise tracing & Prometheus metrics.  
    Honour **OTEL_TRACES_EXPORTER=none** to disable exporting.
    """
    service_name = os.getenv("OTEL_SERVICE_NAME", "ai-building-blocks")
    resource     = Resource.create({"service.name": service_name})

    traces_exporter = os.getenv("OTEL_TRACES_EXPORTER", "otlp").lower()
    if traces_exporter == "none":
        provider = TracerProvider(resource=resource, sampler=ALWAYS_OFF)
        trace.set_tracer_provider(provider)
    else:
        otlp_endpoint = os.getenv("OTEL_EXPORTER_OTLP_ENDPOINT",
                                   "http://localhost:4318").rstrip("/")
        provider = TracerProvider(resource=resource)
        provider.add_span_processor(
            BatchSpanProcessor(
                OTLPSpanExporter(endpoint=f"{otlp_endpoint}/v1/traces")
            )
        )
        trace.set_tracer_provider(provider)

        # ---- inbound FastAPI ----------------------------------------
        FastAPIInstrumentor.instrument_app(
            app,
            tracer_provider=provider,
            server_request_hook=lambda s, _: s.set_attribute("span.kind", "server"),
        )

        # ---- outbound HTTP (requests + httpx) -----------------------
        RequestsInstrumentor().instrument(span_callback=_tag_peer)

        try:
            from opentelemetry.instrumentation.httpx import (
                HTTPXClientInstrumentor,
            )
            HTTPXClientInstrumentor().instrument(span_callback=_tag_peer)
        except ImportError:
            logging.getLogger(__name__).debug("httpx instr not installed")

    # ---- Prometheus FastAPI metrics ---------------------------------
    Instrumentator().instrument(app).expose(app, include_in_schema=False)