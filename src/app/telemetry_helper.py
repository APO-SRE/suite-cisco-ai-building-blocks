#!/usr/bin/env python3
from __future__ import annotations
################################################################################
## AI-Building-Blocks-Agent/app/telemetry.py
## Copyright (c) 2025 Jeff Teeter
## Cisco Systems, Inc.
## Licensed under the Apache License, Version 2.0 (see LICENSE)
## Distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND.
################################################################################

"""
Configure OpenTelemetry tracing and Prometheus metrics for a FastAPI app.
Disables outbound OTLP requests when OTEL_TRACES_EXPORTER is set to "none".
"""
import os

from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from prometheus_fastapi_instrumentator import Instrumentator

# Use the built-in ALWAYS_OFF sampler for disabling traces
from opentelemetry.sdk.trace.sampling import ALWAYS_OFF


def init_telemetry_helper(app):
    """
    Initialize tracing and metrics. Honor OTEL_TRACES_EXPORTER=none to disable tracing exports.
    """
    service_name = os.getenv("OTEL_SERVICE_NAME", "ai-building-blocks")
    resource = Resource.create({"service.name": service_name})

    # Determine if tracing exports should be disabled via environment
    traces_exporter = os.getenv("OTEL_TRACES_EXPORTER", "otlp").lower()
    if traces_exporter == "none":
        # Disable all tracing (no spans recorded or exported)
        provider = TracerProvider(resource=resource, sampler=ALWAYS_OFF)
        trace.set_tracer_provider(provider)
    else:
        # Configure OTLP exporter
        otlp_endpoint = os.getenv("OTEL_EXPORTER_OTLP_ENDPOINT", "http://tempo:4318")
        provider = TracerProvider(resource=resource)
        exporter = OTLPSpanExporter(endpoint=f"{otlp_endpoint.rstrip('/')}/v1/traces")
        provider.add_span_processor(BatchSpanProcessor(exporter))
        trace.set_tracer_provider(provider)

        # Instrument FastAPI and outgoing HTTP calls
        FastAPIInstrumentor.instrument_app(
            app,
            tracer_provider=provider,
            server_request_hook=lambda span, scope: span.set_attribute("span.kind", "server"),
        )
        RequestsInstrumentor().instrument()

    # ── Prometheus metrics setup (always enabled) ───────────────────────────────
    Instrumentator().instrument(app).expose(app, include_in_schema=False)
