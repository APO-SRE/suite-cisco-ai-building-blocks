# app/llm/platform_clients/catalyst_client.py
# Auto-generated – DO NOT EDIT
import dnacentersdk as _sdk
import re, importlib
from functools import partial
import inspect
from typing import get_origin, get_args, Any
import os

# camel→snake splitter
_CAMEL_TO_SNAKE = re.compile(r'(?<!^)(?=[A-Z])')
# Package root of the generated SDK (e.g. "nexus_hyperfabric")
_SDK_PKG = _sdk.__name__

class CatalystClient:
    """Thin wrapper around `DNACenterAPI` with camel→snake fallback."""

    def __init__(self, **kwargs):
        username = os.getenv('DNACENTER_USERNAME')
        password = os.getenv('DNACENTER_PASSWORD')
        base_url = os.getenv('DNACENTER_BASE_URL')
        if not username or not password or not base_url:
            raise ValueError('Missing DNACENTER_USERNAME, DNACENTER_PASSWORD, or DNACENTER_BASE_URL')
        kwargs['username'] = username
        kwargs['password'] = password
        kwargs['base_url']  = base_url
        version = os.getenv('DNACENTER_VERSION', '2.3.7.6')
        verify_env = os.getenv('DNACENTER_VERIFY_SSL','true').lower() in ('true','1','yes')
        kwargs['verify'] = verify_env
        kwargs['version']   = version
        
        self._sdk = _sdk.DNACenterAPI(**kwargs)

    
    @staticmethod
    def _unwrap_model(annotation):
        """
        Return the concrete model class if *annotation* is Optional[T],
        Union[T, None], etc.  Otherwise return the annotation itself.
        """
        origin = get_origin(annotation)
        if origin is None:
            return annotation
        if origin is list:           # body=None edge‑case, keep original
            return annotation
        # Union / Optional
        args = [a for a in get_args(annotation) if a is not type(None)]  # noqa: E721
        return args[0] if args else annotation
    
    # ──────────────────────────────────────────────────────────────
    #  DYNAMIC OPERATION‑ID RESOLUTION
    # ──────────────────────────────────────────────────────────────
    def _resolve(self, name: str):
        """
        Locate <operationId> and return a callable. This method attempts multiple
        strategies to support different SDK architectures.
    
        Scheme (in order):
        1. Direct attr on ApiClient (e.g., PascalCase or snake_case).
        2. Attr on any nested sub-client (for Meraki-style SDKs).
        3. Standalone module function (for openapi-python-client SDKs like Nexus Hyperfabric).
        4. Class-based API tag handler (for Intersight-style SDKs).
        5. Suffix match as a final fallback.
        """
        snake = _CAMEL_TO_SNAKE.sub('_', name).lower()
    
        # Strategy 1: Direct attribute on the SDK client
        if hasattr(self._sdk, name):
            return getattr(self._sdk, name)
        if hasattr(self._sdk, snake):
            return getattr(self._sdk, snake)
    
        # Strategy 2: Look inside nested sub-clients (for Meraki)
        for sub_name in dir(self._sdk):
            if sub_name.startswith('_'):
                continue
            sub = getattr(self._sdk, sub_name)
            for cand in (name, snake):
                if hasattr(sub, cand):
                    return getattr(sub, cand)
    
        # Strategy 3: Handle openapi-python-client's standalone function pattern (for Nexus Hyperfabric)
        # Tries to import a module like: nexus_hyperfabric.api.fabrics.fabrics_get_all_fabrics
        parts = snake.split('_')
        if parts:
            tag = parts[0]
            func_module_name = snake
            try:
                module_path = f"{_SDK_PKG}.api.{tag}.{func_module_name}"
                mod = importlib.import_module(module_path)
                if hasattr(mod, 'sync'):
                    # Wrap the `sync` function to pre-fill the `client` argument
                    return partial(mod.sync, client=self._sdk)
            except (ImportError, AttributeError):
                pass  # If this fails, it's not this architecture; proceed to the next strategy.
    
        # Strategy 4: Class-based API tag handler (for Intersight)
        # Tries to import a class like intersight.api.compute_api.ComputeApi
        if parts:
            # For Intersight, we need to handle get_/post_/patch_/delete_ prefixes
            # get_compute_physical_summary_list -> compute_api.ComputeApi
            if parts[0] in ['get', 'post', 'patch', 'delete', 'put']:
                # Skip the HTTP method prefix for API class detection
                api_parts = parts[1:]
            else:
                api_parts = parts
    
            # This loop logic is important for Intersight's naming conventions
            for i in range(len(api_parts), 0, -1):
                tag = '_'.join(api_parts[:i])
                try:
                    cls_mod = importlib.import_module(f"{_SDK_PKG}.api.{tag}_api")
                    class_name = f"{''.join(p.capitalize() for p in tag.split('_'))}Api"
                    if hasattr(cls_mod, class_name):
                        cls = getattr(cls_mod, class_name)
                        inst = cls(self._sdk)
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
        print(f"[{self.__class__.__name__}] Attempting to resolve function: '{name}'") # <-- ADD THIS LINE
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
                body = model_cls.from_dict(body) if hasattr(model_cls, "from_dict") else model_cls(**body)
            if body_param:
                return target(body=body, **kwargs)
            return target(**kwargs)
        return wrapper
    
