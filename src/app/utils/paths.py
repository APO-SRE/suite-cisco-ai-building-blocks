#!/usr/bin/env python3
from __future__ import annotations
################################################################################
## AI-Building-Blocks-Agent/scripts/utils/paths.py
## Copyright (c) 2025 Jeff Teeter
## Cisco Systems, Inc.
## Licensed under the Apache License, Version 2.0 (see LICENSE)
## Distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND.
################################################################################
"""
Path-handling helpers shared across layers.

* ``ensure_abs_env(var, default_rel)``  
  Makes sure *var* exists and is an **absolute** path, resolving any relative
  value against the repo root (parent of ``suite-cisco-ai-building-blocks``).

* ``get_chroma_root(layer_env: str, default_rel: str = "chroma_dbs")``  
  Returns the absolute path for *this layer’s* Chroma collections, based solely
  on the per-layer env-var (no more legacy ``CHROMA_DB_ROOT``).

* ``get_dynamic_cache_dir()``  
  Ensures and returns the directory pointed to by
  ``PLATFORM_DYNAMIC_CACHE_PATH`` (or its default).
"""

from pathlib import Path
import os
from typing import Final

# ────────────────────────────────────────────────────────────────────────────
REPO_ROOT: Final[Path] = Path(__file__).resolve().parents[2]  # ../../

# ╔═════════════════════════════════════════════════════════════════════════╗
# 1.  Generic helper
# ╚═════════════════════════════════════════════════════════════════════════╝
def ensure_abs_env(var: str, default_rel: str) -> Path:
    raw = os.getenv(var, default_rel)
    p   = Path(raw).expanduser()
    if not p.is_absolute():
        p = (REPO_ROOT / p).resolve()
    os.environ[var] = str(p)
    return p

# ╔═════════════════════════════════════════════════════════════════════════╗
# 2.  Chroma collections (per layer)
# ╚═════════════════════════════════════════════════════════════════════════╝
def get_chroma_root(layer_env: str, default_rel: str = "chroma_dbs") -> Path:
    """
    Resolve the folder that stores *layer-specific* Chroma collections.

    Parameters
    ----------
    layer_env:
        The env-var name, e.g. ``FASTAPI_CHROMA_DB_PATH``.
    default_rel:
        Fallback relative path (resolved under the repo root).

    Returns
    -------
    pathlib.Path
        Absolute path to the collection directory.
    """
    return ensure_abs_env(layer_env, default_rel)

# ╔═════════════════════════════════════════════════════════════════════════╗
# 3.  Platform-function dynamic cache
# ╚═════════════════════════════════════════════════════════════════════════╝
def get_dynamic_cache_dir() -> Path:
    cache = ensure_abs_env(
        "PLATFORM_DYNAMIC_CACHE_PATH",
        "app/llm/platform_dynamic_cache",
    )
    Path(cache).mkdir(parents=True, exist_ok=True)
    return Path(cache)
