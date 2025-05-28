# ai-building-blocks-agent/app/telemetry.py
import os

from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor

from prometheus_fastapi_instrumentator import Instrumentator


def init_telemetry(app):
    """
    Configure OpenTelemetry tracing and Prometheus metrics for a FastAPI app.
    """
    # ── OpenTelemetry tracing setup ────────────────────────────
    otlp_endpoint = os.getenv("OTEL_EXPORTER_OTLP_ENDPOINT", "http://tempo:4318")
    service_name  = os.getenv("OTEL_SERVICE_NAME", "ai-building-blocks-agent")

    resource = Resource.create({"service.name": service_name})
    provider = TracerProvider(resource=resource)
    exporter = OTLPSpanExporter(endpoint=otlp_endpoint)
    exporter = OTLPSpanExporter(
        endpoint=f"{otlp_endpoint.rstrip('/')}/v1/traces",)
    provider.add_span_processor(BatchSpanProcessor(exporter))
    trace.set_tracer_provider(provider)

    # Instrument FastAPI and outgoing HTTP calls
    FastAPIInstrumentor.instrument_app(
        app,
        tracer_provider=provider,
        server_request_hook=lambda span, scope: span.set_attribute("span.kind", "server"),
    )
    RequestsInstrumentor().instrument()

    # ── Prometheus metrics setup ───────────────────────────────
    # This will register /metrics and collect request metrics automatically.
    Instrumentator().instrument(app).expose(app, include_in_schema=False)
