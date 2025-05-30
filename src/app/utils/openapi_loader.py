#!/usr/bin/env python3
from __future__ import annotations
################################################################################
## suite-cisco-ai-building-blocks/src/scripts/openaapi_loader.py
## Copyright (c) 2025 Jeff Teeter
## Cisco Systems, Inc.
## Licensed under the Apache License, Version 2.0 (see LICENSE)
## Distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND.
################################################################################
"""
openapi_loader.py

Tiny helper that loads an OpenAPI document into a Python ``dict``.

• Accepts **JSON** (``*.json``) **and YAML** (``*.yml`` / ``*.yaml``).  
• Requires ``PyYAML`` for YAML files – install once with ``pip install pyyaml``.
"""

from pathlib import Path
import json
from typing import Any, Dict


def _load_yaml(text: str) -> Dict[str, Any]:
    try:
        import yaml  # type: ignore
    except ModuleNotFoundError as exc:
        raise RuntimeError(
            "YAML spec detected but PyYAML is not installed.\n"
            "Fix:  pip install pyyaml"
        ) from exc
    return yaml.safe_load(text)


def load_spec(path: Path) -> dict:
    """
    Read *path* and return the parsed OpenAPI spec as a dictionary.

    Parameters
    ----------
    path : pathlib.Path
        File ending in .json, .yaml or .yml.

    Raises
    ------
    FileNotFoundError
        If the path doesn’t exist.
    ValueError
        If the file extension is unrecognised.
    RuntimeError
        If a YAML file is supplied but PyYAML is missing.
    """
    if not path.exists():
        raise FileNotFoundError(path)

    ext = path.suffix.lower()
    text = path.read_text(encoding="utf-8")

    if ext == ".json":
        return json.loads(text)
    if ext in {".yaml", ".yml"}:
        return _load_yaml(text)

    raise ValueError(f"Unsupported file extension {ext!r} for {path}")