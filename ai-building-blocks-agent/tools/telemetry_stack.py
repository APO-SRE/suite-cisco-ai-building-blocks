#!/usr/bin/env python3
import os
from dotenv import load_dotenv
import docker
import subprocess

# ── 0) Load .env overrides first ────────────────────────────
load_dotenv(override=True)

# ── 1) OTEL exporter defaults ───────────────────────────────
# signal-specific HTTP/protobuf traces exporter
os.environ.setdefault("OTEL_TRACES_EXPORTER",        "otlp")
os.environ.setdefault("OTEL_METRICS_EXPORTER",       "none")
os.environ.setdefault("OTEL_EXPORTER_OTLP_ENDPOINT", "http://localhost:4319")
os.environ.setdefault("OTEL_EXPORTER_OTLP_PROTOCOL", "http/protobuf")
os.environ.setdefault("OTEL_EXPORTER_OTLP_INSECURE", "true")
os.environ.setdefault("OTEL_SERVICE_NAME",           "ai-building-blocks-agent")

# ── 1a) Prep host storage dirs ─────────────────────────────
for sub in ("traces", "metrics-generator/traces", "metrics-generator/wal"):
    os.makedirs(f"tempo-data/{sub}", exist_ok=True)

# fix ownership & perms so Tempo can mkdir & write inside container
subprocess.run(["sudo", "chown", "-R", f"{os.getuid()}:{os.getgid()}", "tempo-data"], check=True)
subprocess.run(["chmod", "-R", "777", "tempo-data"], check=True)

# ── 2) Write out tempo.yaml with debug logging ──────────────
tempo_config = """\
server:
  # main HTTP (query, metrics) and gRPC ports
  http_listen_port: 4318
  grpc_listen_port: 4317

  log_level: debug
  log_format: logfmt

  # force‐log *every* HTTP request on the query/metrics server
  http_server_settings:
    log_requests: true

distributor:
  receivers:
    otlp:
      protocols:
        http:
          endpoint: 0.0.0.0:4319
          # force‐log *every* OTLP-HTTP span post
          http_server_settings:
            log_requests: true
        grpc:
          endpoint: 0.0.0.0:4320

ingester:
  lifecycler:
    ring:
      kvstore:
        store: memberlist
      replication_factor: 1

storage:
  trace:
    backend: local
    local:
      path: /var/tempo/traces
"""

with open("tempo.yaml", "w") as f:
    f.write(tempo_config)

# ── 3) Prometheus & Grafana provisioning ────────────────────
prom_config = """\
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: prometheus
    static_configs:
      - targets: ['localhost:9090']

  - job_name: tempo-server
    metrics_path: /metrics
    static_configs:
      - targets: ['tempo:4318']
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
  jsonData:
    serviceGraphDatasource: Prometheus
"""
os.makedirs("grafana_provisioning", exist_ok=True)
with open("grafana_provisioning/datasources.yaml", "w") as f:
    f.write(grafana_ds)

# ── 4) Launch via Docker API ────────────────────────────────
client = docker.from_env()
net = "observability-net"
try:
    client.networks.get(net)
except docker.errors.NotFound:
    client.networks.create(net, driver="bridge")

# tear down old
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

# Tempo v2.7.1 with debug logs
client.containers.run(
    "grafana/tempo:2.7.1",
    name="tempo",
    detach=True,
    network_mode="host",
    volumes={
        os.path.abspath("tempo-debug.yaml"): {"bind": "/etc/tempo.yaml", "mode": "ro"},
        os.path.abspath("tempo-data"):    {"bind": "/var/tempo",         "mode": "rw"},
    },
    command=["-config.file=/etc/tempo.yaml", "--log.level=debug"],
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
print("  • Tempo (OTLP HTTP) → http://localhost:4319/v1/traces")
print("  • Grafana → http://localhost:3000 (admin/cisco101)")
