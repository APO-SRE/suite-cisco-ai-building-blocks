#!/usr/bin/env python3
from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter

# ── 1) Force the right path on Tempo 2.7.x ────────────────────
exporter = OTLPSpanExporter(
    endpoint="http://localhost:4319/v1/traces"
)

# ── 2) Simple processor = immediate delivery ───────────────────
provider = TracerProvider(resource=Resource({"service.name": "otel-test"}))
provider.add_span_processor(SimpleSpanProcessor(exporter))
trace.set_tracer_provider(provider)

tracer = trace.get_tracer("test_otel")

# ── 3) Send one span ───────────────────────────────────────────
with tracer.start_as_current_span("hello-world-span"):
    print("✔️  started & ended hello-world-span")

# ── 4) Flush & shutdown ────────────────────────────────────────
trace.get_tracer_provider().shutdown()
