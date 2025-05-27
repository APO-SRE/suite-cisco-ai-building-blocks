#!/usr/bin/env python3
from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter

# 1) Point at the OTLP gRPC receiver on port 4320
exporter = OTLPSpanExporter(
    endpoint="localhost:4320",  # <-- change here
    insecure=True               # plaintext gRPC
)

# 2) Immediate delivery
provider = TracerProvider(resource=Resource({"service.name": "grpc-test"}))
provider.add_span_processor(SimpleSpanProcessor(exporter))
trace.set_tracer_provider(provider)

tracer = trace.get_tracer("test_grpc")

# 3) Fire one span
with tracer.start_as_current_span("hello-grpc-span"):
    print("✔️  started & ended hello-grpc-span")

# 4) Flush
trace.get_tracer_provider().shutdown()
