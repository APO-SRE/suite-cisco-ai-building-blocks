""" 
Decorator-based dispatcher registry **plus** smart Meraki fallback.
AUTO-GENERATED – DO NOT EDIT MANUALLY.
""" 
from __future__ import annotations
import importlib
import os
from pathlib import Path
from typing import Any, Callable, Dict
from meraki import DashboardAPI

_registry: Dict[str, Callable[..., Any]] = {}

def register(name: str):
    def _decorator(fn: Callable[..., Any]):
        _registry[name] = fn
        return fn
    return _decorator

# auto-import sub-dispatchers so their @register executes
_pkg_path = Path(__file__).parent
for _p in _pkg_path.glob('*_dispatcher.py'):
    if _p.name != '__init__.py':
        importlib.import_module(f'{__name__}.{_p.stem}')

# Meraki SDK fallback
def _call_meraki(fname: str, kwargs: Dict[str, Any]):
    api_key = os.getenv('CISCO_MERAKI_API_KEY')
    if not api_key:
        raise ValueError('Meraki dispatch failed: missing MERAKI_DASHBOARD_API_KEY')

    dash = DashboardAPI(api_key=api_key,
                        suppress_logging=True,
                        print_console=True)

    if hasattr(dash, fname):
        return getattr(dash, fname)(**kwargs)

    for attr in dir(dash):
        if attr.startswith('_'):
            continue
        sub = getattr(dash, attr)
        if hasattr(sub, fname):
            return getattr(sub, fname)(**kwargs)

    raise AttributeError(f'No Meraki SDK method {fname!r} found')

def dispatch_function_call(name: str, arguments: Dict[str, Any]):
    if name in _registry:
        return _registry[name](**arguments)
    return _call_meraki(name, arguments)

__all__ = ['dispatch_function_call', 'register']
