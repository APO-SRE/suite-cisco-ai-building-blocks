# app/llm/platform_clients/sdwan_mngr_client.py
# Auto-generated – DO NOT EDIT
import catalystwan.session as _sdk
import re, importlib
from functools import partial
import inspect
from typing import get_origin, get_args
import os
import urllib3
from catalystwan.session import create_manager_session

# camel→snake splitter
_CAMEL_TO_SNAKE = re.compile(r'(?<!^)(?=[A-Z])')
# Package root of the generated SDK (e.g. "nexus_hyperfabric")
_SDK_PKG = _sdk.__name__

class Sdwan_mngrClient:
    """Thin wrapper around `APIEndpointClient` with camel→snake fallback."""

    def __init__(self, **kwargs):
        # disable warnings if you don’t verify the sandbox cert
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        
        base_url   = os.getenv('CISCO_SD_WAN_BASE_URL')
        username   = os.getenv('CISCO_SD_WAN_USERNAME')
        password   = os.getenv('CISCO_SD_WAN_PASSWORD')
        verify_env = os.getenv('CISCO_SD_WAN_VERIFY_SSL','false').lower() in ('true','1','yes')
        
        if not base_url or not username or not password:
            raise ValueError('Missing CISCO_SD_WAN_BASE_URL, CISCO_SD_WAN_USERNAME, or CISCO_SD_WAN_PASSWORD')
        
        # 1. Create the session object first.
        session = create_manager_session(url=base_url, username=username, password=password)
        # 2. Then, set the verify attribute on the created session.
        session.verify = verify_env
        
        self._sdk = session

    @staticmethod
    def _unwrap_model(annotation):
        """
        Return the concrete model class if *annotation* is Optional[T],
        Union[T, None], etc.  Otherwise return the annotation itself.
        """
        origin = get_origin(annotation)
        if origin is None:
            return annotation
        if origin is list:           # body=None edge-case, keep original
            return annotation
        # Union / Optional
        args = [a for a in get_args(annotation) if a is not type(None)]  # noqa: E721
        return args[0] if args else annotation
    
    # ──────────────────────────────────────────────────────────────
    #  DYNAMIC OPERATION-ID RESOLUTION
    # ──────────────────────────────────────────────────────────────
    def _resolve(self, name: str):
        """
        Locate <operationId> and return a callable. This method attempts multiple
        strategies to support different SDK architectures.
        """
        snake = _CAMEL_TO_SNAKE.sub('_', name).lower()
    
        # Strategy 1: Direct attribute on the SDK client
        if hasattr(self._sdk, name):
            return getattr(self._sdk, name)
        if hasattr(self._sdk, snake):
            return getattr(self._sdk, snake)
    
        # Strategy 2: Look inside nested sub-clients (for Meraki, SD-WAN)
        for sub_name in dir(self._sdk):
            if sub_name.startswith('_'):
                continue
            sub = getattr(self._sdk, sub_name)
            for cand in (name, snake):
                if hasattr(sub, cand):
                    return getattr(sub, cand)
    
        # Strategy 3: Handle openapi-python-client's standalone function pattern
        parts = snake.split('_')
        if parts:
            tag = parts[0]
            func_module_name = snake
            try:
                module_path = f"{_SDK_PKG}.api.{tag}.{func_module_name}"
                mod = importlib.import_module(module_path)
                if hasattr(mod, 'sync'):
                    return partial(mod.sync, client=self._sdk)
            except (ImportError, AttributeError):
                pass
    
        # Strategy 4: Class-based API tag handler (for Intersight)
        if parts:
            for i in range(len(parts), 0, -1):
                tag = '_'.join(parts[:i])
                try:
                    cls_mod = importlib.import_module(f"{_SDK_PKG}.api.{tag}_api")
                    class_name = f"{''.join(p.capitalize() for p in tag.split('_'))}Api"
                    if hasattr(cls_mod, class_name):
                        inst = getattr(cls_mod, class_name)(self._sdk)
                        if hasattr(inst, snake):
                            return getattr(inst, snake)
                except (ImportError, AttributeError):
                    continue
    
        # Strategy 5: Suffix match as a last resort
        for cand in (name, snake):
            for attr in dir(self._sdk):
                if attr.endswith('_' + cand):
                    return getattr(self._sdk, attr)
    
        raise AttributeError(f"{self.__class__.__name__} could not resolve attribute {name!r}")
    
    # expose everything through __getattr__
    def __getattr__(self, name: str):
        # print(f"[{self.__class__.__name__}] Attempting to resolve function: '{name}'") # Optional: for debugging
        target = self._resolve(name)
        if callable(target):
            return self._wrap_method(target)
        return target
    
    def _wrap_method(self, target):
        """
        Wrap SDK call so that a plain dict passed as *body* is automatically
        converted into the expected pydantic/model class.
        """
        sig        = inspect.signature(target)
        body_param = sig.parameters.get("body")
        model_cls  = self._unwrap_model(body_param.annotation) if body_param else None
    
        def wrapper(body=None, **kwargs):
            if model_cls and isinstance(body, dict):
                try:
                    if hasattr(model_cls, "from_dict"):
                        body = model_cls.from_dict(body)
                    else:
                        body = model_cls(**body)
                except TypeError:
                    # Skip non-instantiable models (e.g. Protocols)
                    pass
            if body_param:
                return target(body=body, **kwargs)
            return target(**kwargs)
    
        return wrapper
