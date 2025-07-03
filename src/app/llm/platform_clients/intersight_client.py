# app/llm/platform_clients/intersight_client.py
# Auto-generated – DO NOT EDIT
import intersight as _sdk
import re, importlib
from functools import partial
import inspect
from typing import get_origin, get_args
import os
from pathlib import Path
import intersight

# camel→snake splitter
_CAMEL_TO_SNAKE = re.compile(r'(?<!^)(?=[A-Z])')
# Package root of the generated SDK (e.g. "nexus_hyperfabric")
_SDK_PKG = _sdk.__name__

class IntersightClient:
    """Thin wrapper around `ApiClient` with camel→snake fallback."""

    def __init__(self, **kwargs):
        api_key = os.getenv('INTERSIGHT_API_KEY')
        api_secret = os.getenv('INTERSIGHT_API_SECRET')
        base_url = os.getenv('INTERSIGHT_BASE_URL', 'https://intersight.com')
        if not api_key or not api_secret:
            raise ValueError('Missing INTERSIGHT_API_KEY or INTERSIGHT_API_SECRET environment variable')
        
        # --- resolve secret: treat value as path OR inline key text ---
        key_path = Path(api_secret).expanduser()
        if key_path.is_file():
            secret_content = key_path.read_text()
        else:
            secret_content = api_secret.strip()
        
        if re.search('BEGIN RSA PRIVATE KEY', secret_content):
            signing_algorithm = intersight.signing.ALGORITHM_RSASSA_PKCS1v15
        elif re.search('BEGIN EC PRIVATE KEY', secret_content):
            signing_algorithm = intersight.signing.ALGORITHM_ECDSA_MODE_DETERMINISTIC_RFC6979
        else:
            raise ValueError('INTERSIGHT_API_SECRET is not a valid RSA or EC private key')
        
        config = intersight.Configuration(
            host=base_url,
            signing_info=intersight.signing.HttpSigningConfiguration(
                key_id=api_key,
                private_key_string=secret_content,
                signing_scheme=intersight.signing.SCHEME_HS2019,
                signing_algorithm=signing_algorithm,
                hash_algorithm=intersight.signing.HASH_SHA256,
                signed_headers=[
                    intersight.signing.HEADER_REQUEST_TARGET,
                    intersight.signing.HEADER_HOST,
                    intersight.signing.HEADER_DATE,
                    intersight.signing.HEADER_DIGEST,
                ]
            )
        )
        kwargs['configuration'] = config
        
        self._sdk = _sdk.ApiClient(**kwargs)

    
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
        Locate <operationId> and return a callable.
    
        Scheme (in order):
        1. Direct attr on ApiClient (PascalCase or snake_case)
        2. Attr on any nested sub‑client
        3. openapi‑python‑client free function  *.api.<tag>.<func>.sync
        4. Class‑based handler          *.api.<Tag>Api.<func>
        5. Suffix match fallback        *_<operationId>
        """
        # 1 ─ direct
        if hasattr(self._sdk, name):
            return getattr(self._sdk, name)
        snake = _CAMEL_TO_SNAKE.sub('_', name).lower()
        if hasattr(self._sdk, snake):
            return getattr(self._sdk, snake)
    
        # 2 ─ look inside sub‑clients
        for sub_name in dir(self._sdk):
            if sub_name.startswith('_'):
                continue
            sub = getattr(self._sdk, sub_name)
            for cand in (name, snake):
                if hasattr(sub, cand):
                    return getattr(sub, cand)
    
        # 3 / 4 ─ derive tag + func
        verbs = {'get', 'create', 'update', 'delete', 'post', 'put', 'patch'}
        parts = snake.split('_')
        if parts and parts[0] in verbs:
            parts = parts[1:]
        if not parts:
            raise AttributeError(f"{name!r} could not be resolved")
    
        # try increasing tag length until module import succeeds
        for i in range(len(parts), 0, -1):
            tag = '_'.join(parts[:i])
            func_tail = '_'.join(parts[i:])
            func_name = snake                     # full op id
            # 3‑a  openapi‑python‑client free function
            try:
                mod = importlib.import_module(f"{_SDK_PKG}.api.{tag}")
            except ImportError:
                mod = None
            if mod and hasattr(mod, func_name):
                fn_mod = getattr(mod, func_name)
                return partial(fn_mod.sync, client=self._sdk) if hasattr(fn_mod, 'sync') else fn_mod
    
            # 4 ─ class‑based handler (e.g. OrganizationApi)
            try:
                cls_mod = importlib.import_module(f"{_SDK_PKG}.api.{tag}_api")
                class_name = f"{''.join(p.capitalize() for p in tag.split('_'))}Api"
                cls = getattr(cls_mod, class_name)
                inst = cls(self._sdk)
                if hasattr(inst, func_name):
                    return getattr(inst, func_name)
            except (ImportError, AttributeError):
                pass
    
        # 5 ─ suffix match as last resort
        for cand in (name, snake):
            for attr in dir(self._sdk):
                if attr.endswith('_' + cand):
                    return getattr(self._sdk, attr)
    
        raise AttributeError(f"{self.__class__.__name__} has no attribute {name!r}")
    
    # expose everything through __getattr__
    def __getattr__(self, name: str):
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
