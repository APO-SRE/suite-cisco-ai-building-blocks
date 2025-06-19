# app/llm/platform_clients/meraki_client.py
# Auto-generated – DO NOT EDIT
import meraki as _sdk
import re, importlib
from functools import partial
import os

# camel→snake splitter
_CAMEL_TO_SNAKE = re.compile(r'(?<!^)(?=[A-Z])')
# Package root of the generated SDK (e.g. "nexus_hyperfabric")
_SDK_PKG = _sdk.__name__

class MerakiClient:
    """Thin wrapper around `DashboardAPI` with camel→snake fallback."""

    def __init__(self, **kwargs):
        api_key = os.getenv('CISCO_MERAKI_API_KEY')
        if not api_key:
            raise ValueError('Missing CISCO_MERAKI_API_KEY environment variable')
        kwargs['api_key'] = api_key
        
        self._sdk = _sdk.DashboardAPI(**kwargs)

    
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
        # e.g. 'fabrics_get_all_fabrics'
        if '_' in snake:
            tag, func_tail = snake.split('_', 1)          # tag = 'fabrics'
            api_mod_path = f'{_SDK_PKG}.api.{tag}'        # …api.fabrics
            try:
                api_mod = importlib.import_module(api_mod_path)
            except ImportError:
                pass
            else:
                # 3‑a: function re‑exported by api.<tag>.__init__.py
                if hasattr(api_mod, func_tail):
                    func_mod = getattr(api_mod, func_tail)
                else:
                    # 3‑b: full snake‑name module (fabrics_get_all_fabrics)
                    full_mod_path = f'{api_mod_path}.{snake}'
                    try:
                        func_mod = importlib.import_module(full_mod_path)
                    except ImportError:
                        # 3‑c: legacy name without tag (get_all_fabrics)
                        try:
                            func_mod = importlib.import_module(f'{api_mod_path}.{func_tail}')
                        except ImportError:
                            func_mod = None
                if func_mod is not None and hasattr(func_mod, 'sync'):
                    return partial(func_mod.sync, client=self._sdk)
    
    
        raise AttributeError(f"{self.__class__.__name__} has no attribute '{name}'")
    
    def __getattr__(self, name: str):
        target = self._resolve(name)
        if callable(target):
            return target
        return target
