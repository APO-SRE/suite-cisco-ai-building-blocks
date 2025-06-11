#!/usr/bin/env python3
from __future__ import annotations
################################################################################
## suite-cisco-ai-building-blocks/src/app/routers/__init__.py
## Copyright (c) 2025 Jeff Teeter, Ph.D.
## Cisco Systems, Inc.
## Licensed under the Apache License, Version 2.0 (see LICENSE)
## Distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND.
################################################################################

"""
DISCLAIMER: USE AT YOUR OWN RISK

This file is now guarded so that missing route files won’t break import.
"""

# 1) Initialize __all__ so that we can append to it safely:
__all__: list[str] = []

# 2) Wrap each “from .<short>_routes import router as <short>_router” in try/except:
try:
    from .catalyst_routes import router as catalyst_router
    __all__.append("catalyst_routes")
except ImportError:
    catalyst_router = None

try:
    from .chat_routes import router as chat_router
    __all__.append("chat_routes")
except ImportError:
    chat_router = None
try:
    from .chat_routes import router as chat_router
    __all__.append("chat_routes")
except ImportError:
    chat_router = None
try:
    from .meraki_routes import router as meraki_router
    __all__.append("meraki_routes")
except ImportError:
    meraki_router = None

try:
    from .webex_routes import router as webex_router
    __all__.append("webex_routes")
except ImportError:
    webex_router = None

# …repeat the same pattern for any other routers you might have…
try:
    from .ai_defense_routes import router as ai_defense_router
    __all__.append("ai_defense_routes")
except ImportError:
    ai_defense_router = None

try:
    from .intersight_routes import router as intersight_router
    __all__.append("intersight_routes")
except ImportError:
    intersight_router = None

try:
    from .sdwan_mngr_routes import router as sdwan_mngr_router
    __all__.append("sdwan_mngr_routes")
except ImportError:
    sdwan_mngr_router = None
