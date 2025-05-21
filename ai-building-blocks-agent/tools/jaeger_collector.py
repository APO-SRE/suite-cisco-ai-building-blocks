#!/usr/bin/env python3
from __future__ import annotations
####################################################################################
## suite-cisco-ai-building-blocks/ai-building-blocks-agent/tools/jaeger_collector.py
## Copyright (c) 2025 Jeff Teeter
## Cisco Systems, Inc.
## Licensed under the Apache License, Version 2.0 (see LICENSE)
## Distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND.
####################################################################################
"""
DISCLAIMER: USE AT YOUR OWN RISK

Utility that ensures a Jaeger all-in-one OpenTelemetry collector is running.
If the container is missing it will be created; if it exists but is stopped
it will be started.  The container is given a restart policy so it survives
host reboots and unexpected exits.

Requires:  pip install docker
"""
from typing import Final
import docker
from docker.errors import NotFound, APIError

CONTAINER_NAME: Final = "jaeger"
IMAGE: Final = "jaegertracing/all-in-one:1.57"
PORTS: Final = {"4317/tcp": 4317, "16686/tcp": 16686}
RESTART_POLICY: Final = {"Name": "unless-stopped"}

def main() -> None:
    client = docker.from_env()

    try:
        container = client.containers.get(CONTAINER_NAME)
        status = container.attrs["State"]["Status"]
        if status != "running":
            print(f"Starting existing container '{CONTAINER_NAME}' (was {status})…")
            container.start()
        else:
            print(f"Container '{CONTAINER_NAME}' is already running.")
    except NotFound:
        print(f"Container '{CONTAINER_NAME}' not found. Creating it…")
        container = client.containers.run(
            IMAGE,
            name=CONTAINER_NAME,
            detach=True,
            ports=PORTS,
            restart_policy=RESTART_POLICY,
        )
        print(f"Started new container '{CONTAINER_NAME}' ({container.short_id}).")
    except APIError as exc:
        print(f"Docker API error: {exc.explanation}")
        raise SystemExit(1)

if __name__ == "__main__":
    main()
