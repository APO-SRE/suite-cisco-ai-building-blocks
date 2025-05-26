#!/usr/bin/env python3
import os
from dotenv import load_dotenv
import docker

# ── 1) Exporter setup ────────────────────────────────────────
os.environ["OTEL_TRACES_EXPORTER"]        = "otlp"
os.environ["OTEL_METRICS_EXPORTER"]       = "none"
os.environ["OTEL_EXPORTER_OTLP_ENDPOINT"] = "http://localhost:4319/v1/traces"
os.environ["OTEL_EXPORTER_OTLP_PROTOCOL"] = "http/protobuf"
os.environ["OTEL_EXPORTER_OTLP_INSECURE"] = "true"
os.environ["OTEL_SERVICE_NAME"]           = "ai-building-blocks-agent"

load_dotenv()  # allow .env overrides

# ── 2) Tempo config ────────────────────────────────
tempo_config = """\
server:
  http_listen_port: 4318
  grpc_listen_port: 4317

distributor:
  receivers:
    otlp:
      protocols:
        http:
          endpoint: 0.0.0.0:4319
        grpc:
          endpoint: 0.0.0.0:4320

ingester:
  trace_idle_period: 10s
  max_block_bytes: 10485760
  lifecycler:
    ring:
      replication_factor: 1

metrics_generator:
  ring:
    kvstore:
      store: memberlist
  processor:
    service_graphs: {}
    span_metrics: {}
  storage:
    path: /var/tempo/metrics-generator/wal
    remote_write:
      - url: http://prometheus:9090/api/v1/write

storage:
  trace:
    backend: local
    local:
      path: /var/tempo/traces

compactor:
  compaction:
    block_retention: 24h

"""

with open("tempo.yaml", "w") as f:
    f.write(tempo_config)

# ── 3) Prometheus & Grafana configs ────────────────
prom_config = """\
global:
  scrape_interval: 15s
scrape_configs:
- job_name: tempo
  static_configs:
  - targets: ['tempo:3200']
- job_name: prometheus
  static_configs:
  - targets: ['localhost:9090']
"""

with open("prometheus.yml", "w") as f:
    f.write(prom_config)

grafana_ds = """\
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
  url: http://tempo:4318
"""
os.makedirs("grafana_provisioning", exist_ok=True)
with open("grafana_provisioning/datasources.yaml", "w") as f:
    f.write(grafana_ds)

# ── 4) Spin up Docker ────────────────────────────────────────
client = docker.from_env()
net = "observability-net"
try:
    client.networks.get(net)
except docker.errors.NotFound:
    client.networks.create(net, driver="bridge")

# Clean up old containers
for name in ("prometheus", "tempo", "grafana"):
    try:
        client.containers.get(name).remove(force=True)
    except docker.errors.NotFound:
        pass

# Prometheus
client.containers.run(
    "prom/prometheus:latest",
    name="prometheus",
    detach=True,
    ports={"9090/tcp": 9090},
    volumes={os.path.abspath("prometheus.yml"): {"bind": "/etc/prometheus/prometheus.yml", "mode": "ro"}},
    command=["--config.file=/etc/prometheus/prometheus.yml", "--web.enable-remote-write-receiver"],
    network=net,
)

# Tempo
client.containers.run(
    "grafana/tempo:2.7.1",
    name="tempo",
    detach=True,
    ports={
      "4318/tcp": 4318,
      "4319/tcp": 4319,
      "14250/tcp": 14250,
      "3200/tcp": 3200,
    },
    volumes={os.path.abspath("tempo.yaml"): {"bind": "/etc/tempo.yaml", "mode": "ro"}},
    command=["-config.file=/etc/tempo.yaml"],
    network=net,
)

# Grafana
client.containers.run(
    "grafana/grafana:latest",
    name="grafana",
    detach=True,
    ports={"3000/tcp": 3000},
    volumes={os.path.abspath("grafana_provisioning"): {"bind": "/etc/grafana/provisioning/datasources", "mode": "ro"}},
    environment={
        "GF_SECURITY_ADMIN_USER":     "admin",
        "GF_SECURITY_ADMIN_PASSWORD": "cisco101",
    },
    network=net,
)

print("✅ telemetry stack started.")
print("  • Prometheus → http://localhost:9090")
print("  • Tempo (OTLP HTTP) → http://localhost:4318/v1/traces")
print("  • Grafana → http://localhost:3000 (admin/cisco101)")