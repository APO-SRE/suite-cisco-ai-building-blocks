#!/usr/bin/env python3
from __future__ import annotations
################################################################################
## AI-Building-Blocks-Agent/scripts/utils/sdk_loader.py
## Copyright (c) 2025 Jeff Teeter
## Cisco Systems, Inc.
## Licensed under the Apache License, Version 2.0 (see LICENSE)
## Distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND.
################################################################################

"""
Utility to locate the main *client* class in a vendor SDK so that the scaffolder
can wrap it automatically.

Matching rules — in order of preference — are:

1.  Class name ends with **DashboardAPI**        (e.g. ``DashboardAPI``)
2.  Class name ends with **Client**              (e.g. ``MerakiClient``)
3.  Class name ends with **API**                 (e.g. ``DNACenterAPI``)

The comparison is case-insensitive.  The first match encountered is returned.
"""

import importlib
import inspect
from types import ModuleType
from typing import Type, Any


def load_client(module_name: str) -> Type[Any]:
    """
    Dynamically import *module_name* and return the first class that looks like
    an SDK entry-point according to the rules above.

    Parameters
    ----------
    module_name : str
        The fully-qualified name of the SDK module, e.g. ``"meraki"``,
        ``"dnacentersdk"``.

    Raises
    ------
    RuntimeError
        If no suitable client class is found.

    Examples
    --------
    >>> load_client("meraki").__name__
    'DashboardAPI'
    >>> load_client("dnacentersdk").__name__
    'DNACenterAPI'
    """
    mod: ModuleType = importlib.import_module(module_name)

    for attr in dir(mod):
        obj = getattr(mod, attr)
        if not inspect.isclass(obj):
            continue

        lower_name = attr.lower()
        if lower_name.endswith("dashboardapi") or lower_name.endswith("client") or lower_name.endswith("api"):
            return obj

    raise RuntimeError(f"No SDK client found in {module_name!r}")
