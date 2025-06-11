#!/usr/bin/env python3
from __future__ import annotations
################################################################################
## AI-Building-Blocks-Agent/scripts/utils/paths.py
## Copyright (c) 2025 Jeff Teeter
## Cisco Systems, Inc.
## Licensed under the Apache License, Version 2.0 (see LICENSE)
## Distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND.
################################################################################
# suite-cisco-ai-building-blocks/src/app/utils/paths.py
from pathlib import Path
import os
from typing import Final

REPO_ROOT: Final[Path] = Path(__file__).resolve().parents[3]

def ensure_abs_env(var: str, default_rel: str) -> Path:
    raw = os.getenv(var, default_rel)
    p = Path(raw).expanduser()
    if not p.is_absolute():
        p = (REPO_ROOT / p).resolve()
    os.environ[var] = str(p)
    return p