# app/llm/platform_clients/catalyst_client.py
# Auto-generated – DO NOT EDIT
import dnacentersdk as _sdk
import re, importlib
from functools import partial

# camel→snake splitter
_CAMEL_TO_SNAKE = re.compile(r'(?<!^)(?=[A-Z])')
# Package root of the generated SDK (e.g. "nexus_hyperfabric")
_SDK_PKG = _sdk.__name__

class CatalystClient:
    """Thin wrapper around `DNACenterAPI` with camel→snake fallback."""

    def __init__(self, **kwargs):
        self._sdk = _sdk.DNACenterAPI(**kwargs)

    
    def _resolve(self, name: str):
        """
        Resolve <operationId> to a callable.
    
        ① direct attribute on the AuthenticatedClient
        ② attribute on a sub‑client (camel→snake tried too)
        ③ <sdk>.api.<tag>.<function>.sync  – the pattern used by
        openapi‑python‑client
        """
        if hasattr(self._sdk, name):
            return getattr(self._sdk, name)
        snake = _CAMEL_TO_SNAKE.sub('_', name).lower()
        if hasattr(self._sdk, snake):
            return getattr(self._sdk, snake)
        for sub_name in dir(self._sdk):
            if sub_name.startswith('_'):
                continue
            sub = getattr(self._sdk, sub_name)
            for candidate in (name, snake):
                if hasattr(sub, candidate):
                    return getattr(sub, candidate)
    
        # ---- pattern ③  ----------------------------------------------------
        # e.g. "fabricsGetAllFabrics" → tag="fabrics" func="get_all_fabrics"
        if "_" in snake:
            tag, func = snake.split("_", 1)
            api_mod_path = f"{_SDK_PKG}.api.{tag}"
            try:
                api_mod = importlib.import_module(api_mod_path)
            except ImportError:
                pass
            else:
                # First try lazy export in api.<tag> ( __init__.py re‑exports )
                if hasattr(api_mod, func):
                    func_mod = getattr(api_mod, func)
                else:
                    # Fallback: direct sub‑module import
                    try:
                        func_mod = importlib.import_module(f"{api_mod_path}.{func}")
                    except ImportError:
                        func_mod = None
                if func_mod is not None and hasattr(func_mod, "sync"):
                    # Bind the generated client automatically
                    return partial(func_mod.sync, client=self._sdk)
    
        raise AttributeError(f"{self.__class__.__name__} has no attribute '{name}'")
    
    def __getattr__(self, name: str):
        target = self._resolve(name)
        if callable(target):
            return target
        return target
