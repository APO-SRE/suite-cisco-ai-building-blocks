#!/usr/bin/env python3
from __future__ import annotations
################################################################################
## suite-cisco-ai-building-blocks/src/app/scripts/observability_setup.py
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

import os, subprocess

# 1. Define the content for Dockerfile (FastAPI app image)
dockerfile_content = """\
FROM python:3.11-slim
WORKDIR /app
# Install FastAPI app dependencies (including opentelemetry and prometheus)
RUN pip install fastapi uvicorn[standard] prometheus-fastapi-instrumentator prometheus-client \\
    opentelemetry-sdk opentelemetry-exporter-otlp-proto-http \\
    opentelemetry-instrumentation-fastapi
COPY . .
ENV OTEL_EXPORTER_OTLP_ENDPOINT=${OTEL_EXPORTER_OTLP_ENDPOINT:-http://tempo:4318}
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
"""

# 2. Define docker-compose.yaml content with FastAPI app, Prometheus, Tempo, Grafana
compose_content = """\
services:
  fastapi-app:
    build: .
    container_name: fastapi-app
    ports:
      - "8001:8000"
    environment:
      - OTEL_EXPORTER_OTLP_ENDPOINT=http://tempo:4318
      - OTEL_SERVICE_NAME=fastapi-app
    depends_on:
      - tempo

  prometheus:
    image: prom/prometheus:latest
    container_name: prometheus
    ports:
      - "9090:9090"
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml:ro
    # <— removed depends_on here

  tempo:
    image: grafana/tempo:latest
    container_name: tempo
    command:
      - "-config.file=/etc/tempo.yaml"
    volumes:
      - ./tempo.yaml:/etc/tempo.yaml:ro
    ports:
      - "3200:3200"
      - "4318:4318"
    depends_on:
      - prometheus

  grafana:
    image: grafana/grafana:latest
    container_name: grafana
    ports:
      - "3000:3000"
    volumes:
      - ./grafana-datasources.yml:/etc/grafana/provisioning/datasources/datasources.yml:ro
    depends_on:
      - prometheus
      - tempo
"""

# 3. Prometheus configuration to scrape FastAPI and Tempo
prom_config = """\
global:
  scrape_interval: 5s
scrape_configs:
  - job_name: 'fastapi-app'
    scrape_interval: 5s
    static_configs:
      - targets: ['fastapi-app:8000']
  - job_name: 'tempo'
    scrape_interval: 15s
    static_configs:
      - targets: ['tempo:3200']
"""

# 4. Tempo configuration (OTLP receiver, in-memory storage)
tempo_config = """\
# tempo.yaml — Tempo v2.7+ all-in-one
target: all

server:
  http_listen_port: 3200   # Grafana queries this
  grpc_listen_port: 9095   # internal gRPC (won’t conflict)

# ── Add this back so Tempo will talk OTLP on 4317/4318 ───────────────────────
receivers:
  otlp:
    protocols:
      grpc:
        endpoint: "0.0.0.0:4317"
      http:
        endpoint: "0.0.0.0:4318"

distributor:
  receivers:
    otlp:
      protocols:
        grpc: {}
        http: {}

ingester:
  lifecycler:
    ring:
      kvstore:
        store: inmemory
      replication_factor: 1

storage:
  trace:
    backend: local
    local:
      path: /tmp/tempo/traces
"""


# 5. Grafana data sources provisioning (Prometheus & Tempo)
grafana_datasources = """\
apiVersion: 1
datasources:
- name: Prometheus
  type: prometheus
  access: proxy
  url: http://prometheus:9090
  isDefault: true
- name: Tempo
  type: tempo
  access: proxy
  url: http://tempo:3200
  isDefault: false
"""
# This provisioning file tells Grafana to automatically add Prometheus and Tempo as data sources.

# Create the files in the current directory
with open("Dockerfile", "w") as f:
    f.write(dockerfile_content)
with open("docker-compose.yaml", "w") as f:
    f.write(compose_content)
with open("prometheus.yml", "w") as f:
    f.write(prom_config)
with open("tempo.yaml", "w") as f:
    f.write(tempo_config)
with open("grafana-datasources.yml", "w") as f:
    f.write(grafana_datasources)

# 6. Build and start all containers using Docker Compose
subprocess.run(["docker", "compose", "up", "-d"], check=True)
print("Docker Compose services are up and running.")
