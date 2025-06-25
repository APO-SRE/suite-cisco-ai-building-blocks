# app/llm/platform_clients/nexus_hyperfabric_client.py
# Auto-generated – DO NOT EDIT
import cisco_nexus_hyperfabric_rest_api_client as _sdk
import re, importlib
from functools import partial
import inspect
from typing import get_origin, get_args
import os

# camel→snake splitter
_CAMEL_TO_SNAKE = re.compile(r'(?<!^)(?=[A-Z])')
# Package root of the generated SDK (e.g. "nexus_hyperfabric")
_SDK_PKG = _sdk.__name__

class Nexus_hyperfabricClient:
    """Thin wrapper around `AuthenticatedClient` with camel→snake fallback."""

    def __init__(self, **kwargs):
        base_url = os.getenv('NEXUS_HYPERFABRIC_BASE_URL')
        token    = os.getenv('NEXUS_HYPERFABRIC_BEARER_TOKEN')
        if not base_url or not token:
            raise ValueError('Missing NEXUS_HYPERFABRIC_BASE_URL or NEXUS_HYPERFABRIC_BEARER_TOKEN')
        kwargs.setdefault('base_url', base_url)
        kwargs.setdefault('token', token)
        
        self._sdk = _sdk.AuthenticatedClient(**kwargs)

    
    @staticmethod    
    def _unwrap_model(annotation):
        """
        Return the concrete model class if *annotation* is Optional[T],
        Union[T, None], etc.  Otherwise return the annotation itself.
        """
        origin = get_origin(annotation)
        if origin is None:
            return annotation
        if origin is list:      # body=None edge‑case, keep original
            return annotation
        # Union / Optional
        args = [a for a in get_args(annotation) if a is not type(None)]  # noqa: E721
        return args[0] if args else annotation
    
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
    
        # 2) Nested sub‑clients
        for sub_name in dir(self._sdk):
            if sub_name.startswith('_'):
                continue
            sub = getattr(self._sdk, sub_name)
            for candidate in (name, snake):
                if hasattr(sub, candidate):
                    return getattr(sub, candidate)
    
        # 3) openapi‑python‑client pattern
        if '_' in snake:
            tag, func_tail = snake.split('_', 1)
            api_mod_path = f'{_SDK_PKG}.api.{tag}'
            try:
                api_mod = importlib.import_module(api_mod_path)
            except ImportError:
                pass
            else:
                if hasattr(api_mod, func_tail):
                    func_mod = getattr(api_mod, func_tail)
                else:
                    try:
                        func_mod = importlib.import_module(f'{api_mod_path}.{snake}')
                    except ImportError:
                        try:
                            func_mod = importlib.import_module(f'{api_mod_path}.{func_tail}')
                        except ImportError:
                            func_mod = None
                if func_mod is not None and hasattr(func_mod, 'sync'):
                    return partial(func_mod.sync, client=self._sdk)
    
        # 4) Suffix match: alias without tag
        for candidate in (name, snake):
            for attr in dir(self._sdk):
                if attr.endswith("_" + candidate):
                    return getattr(self._sdk, attr)
    
        raise AttributeError(f"{self.__class__.__name__} has no attribute '{name}'")
    
    def __getattr__(self, name: str):
        target = self._resolve(name)
        if callable(target):
            return self._wrap_method(target)
        return target
    
    def _wrap_method(self, target):
        sig        = inspect.signature(target)
        body_param = sig.parameters.get("body")
        model_cls  = self._unwrap_model(body_param.annotation) if body_param else None
        def wrapper(body=None, **kwargs):
            # If SDK expects a model class but we got a plain dict → wrap it
            if model_cls and isinstance(body, dict):
                if hasattr(model_cls, 'from_dict'):
                    body = model_cls.from_dict(body)
                else:
                    body = model_cls(**body)
            if body_param:               # SDK has a 'body' parameter
                return target(body=body, **kwargs)
            return target(**kwargs)      # no body in signature
        return wrapper
