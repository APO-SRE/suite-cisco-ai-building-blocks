# app/llm/platform_clients/sdwan_mngr_client.py
# Auto-generated – DO NOT EDIT
import catalystwan.session as _sdk
import re, importlib
from functools import partial
import inspect
from typing import get_origin, get_args
import os
from catalystwan.session import create_manager_session
import urllib3
import json
from pathlib import Path

# camel→snake splitter
_CAMEL_TO_SNAKE = re.compile(r'(?<!^)(?=[A-Z])')
# Package root of the generated SDK (e.g. "nexus_hyperfabric")
_SDK_PKG = _sdk.__name__

class Sdwan_mngrClient:
    """Thin wrapper around `SDWANSessionPlaceholder` with camel→snake fallback."""

    def __init__(self, **kwargs):
        # Disable SSL warnings for SD-WAN sandbox
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        
        # SD-WAN requires creating a session, not just instantiating a client
        url = kwargs.get('url') or kwargs.get('base_url') or os.getenv('CISCO_SD_WAN_BASE_URL')
        username = kwargs.get('username') or os.getenv('CISCO_SD_WAN_USERNAME')
        password = kwargs.get('password') or os.getenv('CISCO_SD_WAN_PASSWORD')
        port = kwargs.get('port')
        subdomain = kwargs.get('subdomain')
        
        if not all([url, username, password]):
            raise ValueError(
                'SD-WAN Manager requires url, username, and password. '
                'Set via parameters or environment variables: '
                'CISCO_SD_WAN_BASE_URL, CISCO_SD_WAN_USERNAME, CISCO_SD_WAN_PASSWORD'
            )
        
        # Create the manager session
        self._session = create_manager_session(
            url=url,
            username=username,
            password=password,
            port=port,
            subdomain=subdomain
        )
        self._sdk = self._session  # Store session as _sdk for compatibility
        self._api = self._session.api  # Get the API container


    # Load operation registry on first access
    _operation_registry = None
    
    @classmethod
    def _load_registry(cls):
        """Load the SD-WAN operation registry"""
        if cls._operation_registry is None:
            registry_path = Path(__file__).parent.parent / 'sdwan_operation_registry_full.json'
            if registry_path.exists():
                with open(registry_path) as f:
                    cls._operation_registry = json.load(f)
            else:
                # Fallback to minimal registry
                cls._operation_registry = {
                    'operations': {},
                    'comment': 'Registry file not found'
                }
        return cls._operation_registry
    
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
    
    def _resolve(self, name: str):
        """Custom resolution for SD-WAN operations"""
        # Load the operation registry
        registry = self._load_registry()
    
        # Look up the operation
        op_info = registry.get('operations', {}).get(name)
        if not op_info:
            # Try the default resolution logic first
            return self._default_resolve(name)
    
        # Create a wrapper that makes the actual SDK call
        def sdk_call(**kwargs):
            try:
                # Get the SDK endpoint and method
                endpoint_path = op_info.get('sdk_endpoint', '')
                sdk_method = op_info.get('sdk_method', 'get')
    
                # Navigate to the endpoint
                endpoint = self._api
                for part in endpoint_path.split('.'):
                    if hasattr(endpoint, part):
                        endpoint = getattr(endpoint, part)
                    else:
                        return {
                            'error': f'SDK endpoint {endpoint_path} not found',
                            'available': [a for a in dir(endpoint) if not a.startswith('_')][:10]
                        }
    
                # Get the method
                if hasattr(endpoint, sdk_method):
                    method = getattr(endpoint, sdk_method)
                else:
                    return {
                        'error': f'Method {sdk_method} not found on {endpoint_path}',
                        'available_methods': [m for m in dir(endpoint) if not m.startswith('_') and callable(getattr(endpoint, m))]
                    }
    
                # Handle parameters
                call_params = {}
    
                # Path parameters (like deviceId)
                if op_info.get('needs_id') and op_info.get('path_params'):
                    for param in op_info['path_params']:
                        if param in kwargs:
                            call_params[param] = kwargs.pop(param)
    
                # Query parameters
                if op_info.get('query_params'):
                    for param_info in op_info['query_params']:
                        param_name = param_info['name']
                        if param_name in kwargs:
                            call_params[param_name] = kwargs.pop(param_name)
    
                # Body parameter
                if 'body' in kwargs:
                    call_params['body'] = kwargs.pop('body')
    
                # Add any remaining kwargs
                call_params.update(kwargs)
    
                # Make the actual SDK call
                result = method(**call_params)
    
                # Return the result
                if hasattr(result, 'json'):
                    return result.json()
                elif hasattr(result, 'to_dict'):
                    return result.to_dict()
                elif hasattr(result, '__iter__') and not isinstance(result, (str, bytes)):
                    # Handle DataSequence and other iterables from SD-WAN SDK
                    try:
                        # Convert to list and extract data
                        items = list(result)
                        if not items:
                            return []
    
                        # Check first item to determine conversion method
                        first_item = items[0]
    
                        # Try different serialization methods
                        if hasattr(first_item, 'to_dict'):
                            return [item.to_dict() for item in items]
                        elif hasattr(first_item, 'model_dump'):
                            # Handle pydantic v2 models
                            return [item.model_dump() for item in items]
                        elif hasattr(first_item, '__dict__'):
                            # Handle SD-WAN Device objects and similar
                            def serialize_obj(obj):
                                # Get all non-private attributes
                                data = {}
                                for key, value in obj.__dict__.items():
                                    if not key.startswith('_'):
                                        # Recursively handle nested objects
                                        if hasattr(value, '__dict__') and not isinstance(value, (str, int, float, bool, list, dict)):
                                            data[key] = serialize_obj(value)
                                        else:
                                            data[key] = value
                                return data
    
                            return [serialize_obj(item) for item in items]
                        else:
                            # Return as-is if items are already serializable
                            return items
                    except Exception as e:
                        # Log the error for debugging
                        print(f"Error serializing result: {e}")
                        return str(result)
                elif hasattr(result, '__dict__'):
                    # Handle single SD-WAN objects
                    data = {}
                    for key, value in result.__dict__.items():
                        if not key.startswith('_'):
                            data[key] = value
                    return data
                else:
                    return result
    
            except Exception as e:
                import traceback
                return {
                    'error': str(e),
                    'traceback': traceback.format_exc(),
                    'operation': name,
                    'operation_info': op_info
                }
    
        return sdk_call
    
    def _default_resolve(self, name: str):
        """
        Fallback resolution when operation is not in registry.
        """
        snake = _CAMEL_TO_SNAKE.sub('_', name).lower()
    
        # Try basic attribute lookup
        if hasattr(self._sdk, name):
            return getattr(self._sdk, name)
        if hasattr(self._sdk, snake):
            return getattr(self._sdk, snake)
    
        # Look inside the API container
        if hasattr(self, '_api'):
            for attr_name in dir(self._api):
                if attr_name.startswith('_'):
                    continue
                attr = getattr(self._api, attr_name)
                if hasattr(attr, name):
                    return getattr(attr, name)
                if hasattr(attr, snake):
                    return getattr(attr, snake)
    
        raise AttributeError(f"{self.__class__.__name__} could not resolve attribute {name!r}")
    
    def __getattr__(self, name: str):
        """Dynamic <operationId> lookup, with exception trapping."""
        try:
            return self._resolve(name)
        except Exception as e:
            raise AttributeError(f"{self.__class__.__name__} could not resolve attribute {name!r} ({e})")
    
    def _wrap_method(self, target):
        """
        Wrap SDK call so that a plain dict passed as *body* is automatically
        converted into the expected pydantic/model class.
        """
        sig        = inspect.signature(target)
        body_param = sig.parameters.get("body")
        model_cls  = self._unwrap_model(body_param.annotation) if body_param else None
    
        # no body/model → no conversion
        if model_cls is None or not hasattr(model_cls, "__init__"):
            return target
    
        # wrapper: auto-convert dicts to model_cls
        from functools import wraps
        @wraps(target)
        def wrapper(**kwargs):
            body = kwargs.get("body")
            if body and isinstance(body, dict):
                kwargs["body"] = model_cls(**body)
            return target(**kwargs)
    
        return wrapper
    
