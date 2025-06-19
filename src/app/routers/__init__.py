#!/usr/bin/env python3
from __future__ import annotations
################################################################################
## suite-cisco-ai-building-blocks/src/app/routers/__init__.py
## Copyright (c) 2025 Jeff Teeter, Ph.D.
## Cisco Systems, Inc.
## Licensed under the Apache License, Version 2.0 (see LICENSE)
################################################################################
"""
Dynamic, fault‑tolerant loader for every `*_routes.py` file in this package.

* Each file must expose a FastAPI `router` object.
* A successful import is re‑exported as   `<platform>_router`
  (e.g. `catalyst_router`, `meraki_router`, …).
* If the import fails (or the file is missing), we still create the
  attribute and set it to ``None`` so that `app.routers.<alias>` is always
  defined, avoiding ``AttributeError`` elsewhere in the codebase.
"""
from pathlib import Path
import importlib
import pkgutil
import sys
from types import ModuleType
from typing import Any, List

__all__: List[str] = []                       # will be populated at runtime
_pkg = sys.modules[__name__]                  # shortcut to the current module


def _safe_load(module_name: str) -> None:
    """
    Import `<module_name>`, expose its `router` as `<platform>_router`,
    and update ``__all__``; on *any* exception create a stub alias instead.
    """
    short = module_name.rsplit("_routes", 1)[0]
    alias = f"{short}_router"

    try:
        mod: ModuleType = importlib.import_module(f"{__name__}.{module_name}")
        router = getattr(mod, "router")       # AttributeError ➜ except
        setattr(_pkg, alias, router)
        __all__.append(alias)
    except Exception:                         # noqa: BLE001 (intentional blanket)
        # Always expose the alias, even if None, to keep IDEs & imports happy
        setattr(_pkg, alias, None)


# ── Discover & import every *_routes.py next to this file ──────────────────
for info in pkgutil.iter_modules([Path(__file__).parent]):
    if info.name.endswith("_routes"):         # filter only route modules
        _safe_load(info.name)

del importlib, pkgutil, sys, Path, ModuleType, Any, List, _safe_load, _pkg
################################################################################
