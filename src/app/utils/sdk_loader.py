#!/usr/bin/env python3
from __future__ import annotations
################################################################################
## AI-Building-Blocks-Agent/scripts/utils/sdk_loader.py
## Copyright (c) 2025 Jeff Teeter
## Cisco Systems, Inc.
## Licensed under the Apache License, Version 2.0 (see LICENSE)
## Distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND.
################################################################################
 

import importlib
import inspect
from types import ModuleType
from typing import Type, Any

# src/app/utils/sdk_loader.py

import importlib
import inspect
from types import ModuleType
from typing import Type, Any


def load_client(module_name: str) -> Type[Any]:
    """
    Dynamically import *module_name* and return the SDK's main entry-point class.

    This function uses a two-stage strategy to ensure accuracy:
    1.  **Platform-Specific Checks:** For complex SDKs with known, unique structures
        (like Intersight), an explicit check is performed first.
    2.  **Generic Fallback:** If no specific rule matches, it falls back to a
        generic search based on common class name suffixes.
    """
    mod: ModuleType = importlib.import_module(module_name)

    # --- STRATEGY 1: EXPLICIT CHECKS FOR KNOWN PLATFORMS ---
    # This is the most reliable method and should be used for any SDK
    # that doesn't follow a simple naming convention.

    if module_name == "intersight":
        # The Intersight SDK's main entry point is the `ApiClient` class.
        if hasattr(mod, "ApiClient"):
            return getattr(mod, "ApiClient")
        else:
            # If the module is 'intersight' but ApiClient is missing,
            # something is fundamentally wrong with the SDK installation.
            raise RuntimeError("Intersight SDK is imported but the ApiClient class is missing.")
    
    if module_name == "catalystwan.session":
        # SD-WAN uses a different pattern - return a dummy class
        # The actual session creation happens in the generated client
        class SDWANSessionPlaceholder:
            """Placeholder for SD-WAN session - actual session created in client __init__"""
            pass
        return SDWANSessionPlaceholder


    # --- STRATEGY 2: GENERIC SUFFIX-BASED FALLBACK ---
    # This works for simpler SDKs like Meraki, Catalyst, etc.

    for attr in dir(mod):
        obj = getattr(mod, attr)
        if not inspect.isclass(obj):
            continue

        lower_name = attr.lower()
        # Check for suffixes in order of preference
        if lower_name.endswith("dashboardapi"): return obj
        if lower_name.endswith("client"): return obj
        if lower_name.endswith("api"): return obj
        if lower_name.endswith("session"): return obj

    raise RuntimeError(f"No recognized SDK client class found in {module_name!r}")