#!/usr/bin/env python3
import logging
logging.basicConfig(
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    level=logging.DEBUG,
)
from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter

# 1) Hit Tempo's HTTP OTLP endpoint internally on the Docker network
exporter = OTLPSpanExporter(endpoint="http://tempo:4319/v1/traces")

# 2) Immediate delivery
provider = TracerProvider(resource=Resource({"service.name": "docker-http-test"}))
provider.add_span_processor(SimpleSpanProcessor(exporter))
trace.set_tracer_provider(provider)

# 3) Emit a single span
tracer = trace.get_tracer("test_http")
with tracer.start_as_current_span("hello-http-span"):
    print("✔️  started & ended hello-http-span")

# 4) Flush & exit
trace.get_tracer_provider().shutdown()
