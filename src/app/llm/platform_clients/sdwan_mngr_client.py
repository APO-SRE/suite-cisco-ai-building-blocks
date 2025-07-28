# app/llm/platform_clients/sdwan_mngr_client.py
# Auto-generated – DO NOT EDIT
import catalystwan.session as _sdk
import re, importlib
from functools import partial
import inspect
from typing import get_origin, get_args, Any
import os
from catalystwan.session import create_manager_session
import urllib3
from urllib.parse import urljoin
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
        
        # Store base URL for REST API calls
        self._base_url = url
        
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
                cls._operation_registry = {'operations': {}, 'comment': 'Registry file not found'}
        return cls._operation_registry
    
    def _make_rest_api_call(self, op_info: dict, **kwargs):
        """Make a direct REST API call when SDK method is not available."""
        try:
            # Build the URL
            path = op_info['path']
            method = op_info['method'].upper()
    
            # Replace path parameters
            if op_info.get('path_params'):
                for param in op_info['path_params']:
                    if param in kwargs:
                        path = path.replace(f'{{{param}}}', str(kwargs.pop(param)))
    
            # Build full URL
            url = urljoin(self._base_url, f'/dataservice{path}')
    
            # Debug logging (optional - remove in production)
            # print(f"[REST API Debug] URL: {url}")
            # print(f"[REST API Debug] Method: {method}")
    
            # Prepare request parameters
            # The session already has auth configured, so we don't need to manually add headers
            request_kwargs = {
                'verify': False  # For sandbox environments
            }
    
            # Handle query parameters
            query_params = {}
            if op_info.get('query_params'):
                for param_info in op_info['query_params']:
                    param_name = param_info['name']
                    if param_name in kwargs:
                        query_params[param_name] = kwargs.pop(param_name)
    
            if query_params:
                request_kwargs['params'] = query_params
    
            # Handle request body
            if method in ['POST', 'PUT', 'PATCH']:
                if 'body' in kwargs:
                    request_kwargs['json'] = kwargs.pop('body')
                elif kwargs:
                    request_kwargs['json'] = kwargs
    
            # Make the request using the SDK session (which has auth already configured)
            # The SDK session extends requests.Session, so we can use it directly
            response = self._session.request(method, url, **request_kwargs)
    
            # Handle response
            if response.status_code >= 400:
                return {
                    'error': f'HTTP {response.status_code}',
                    'message': response.text,
                    'url': url,
                    'method': method
                }
    
            # Parse JSON response
            if response.text:
                try:
                    data = response.json()
                    # Handle vManage response format
                    if isinstance(data, dict) and 'data' in data:
                        return data['data']
                    return data
                except json.JSONDecodeError:
                    return response.text
    
            return {'status': 'success', 'status_code': response.status_code}
    
        except Exception as e:
            import traceback
            return {
                'error': str(e),
                'traceback': traceback.format_exc(),
                'operation': op_info.get('operationId', 'unknown'),
                'url': url if 'url' in locals() else 'unknown'
            }
    
    def _resolve(self, name: str):
        """Custom resolution for SD-WAN operations supporting both SDK and REST API."""
        registry = self._load_registry()
        op_info = registry.get('operations', {}).get(name)
    
        if not op_info:
            # Try default SDK resolution
            return self._default_resolve(name)
    
        # Special handling for getActiveAlarms to add default dates and count
        if name == 'getActiveAlarms' and op_info.get('use_direct_api', False):
            def active_alarms_wrapper(**kwargs):
                # If no dates provided, default to last 24 hours
                if 'startDate' not in kwargs and 'endDate' not in kwargs:
                    from datetime import datetime, timedelta
                    kwargs['endDate'] = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
                    kwargs['startDate'] = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%dT%H:%M:%S')
                # If no count provided, default to 1000
                if 'count' not in kwargs:
                    kwargs['count'] = 1000
                return self._make_rest_api_call(op_info, **kwargs)
            return active_alarms_wrapper
    
        # Check if we should use direct API
        if op_info.get('use_direct_api', False):
            # Return a wrapper function for REST API call
            def rest_api_call(**kwargs):
                return self._make_rest_api_call(op_info, **kwargs)
            return rest_api_call
    
        # Use SDK method
        def sdk_call(**kwargs):
            try:
                endpoint_path = op_info.get('sdk_endpoint', '')
                sdk_method = op_info.get('sdk_method', 'get')
    
                endpoint = self._api
                for part in endpoint_path.split('.'):
                    if not hasattr(endpoint, part):
                        # Fallback to REST API if SDK endpoint not found
                        return self._make_rest_api_call(op_info, **kwargs)
                    endpoint = getattr(endpoint, part)
    
                if not hasattr(endpoint, sdk_method):
                    # Fallback to REST API if SDK method not found
                    return self._make_rest_api_call(op_info, **kwargs)
    
                method = getattr(endpoint, sdk_method)
    
                call_params = {}
                if op_info.get('path_params'):
                    for param in op_info['path_params']:
                        if param in kwargs:
                            call_params[param] = kwargs.pop(param)
    
                if op_info.get('query_params'):
                    for param_info in op_info['query_params']:
                        param_name = param_info['name']
                        if param_name in kwargs:
                            call_params[param_name] = kwargs.pop(param_name)
    
                call_params.update(kwargs)
    
                result = method(**call_params)
    
                # --- THIS IS THE UNIFIED, BULLETPROOF SERIALIZATION LOGIC ---
                def serialize_recursively(obj):
                    """
                    Recursively traverses an object and converts it into a JSON-serializable format,
                    handling all known catalystwan object types.
                    """
                    try:
                        from pydantic.fields import FieldInfo
                    except ImportError:
                        FieldInfo = type(None)
    
                    # 1. Handle base cases immediately
                    if obj is None or isinstance(obj, (str, int, float, bool)):
                        return obj
    
                    # 2. Handle already-serialized formats
                    if isinstance(obj, dict):
                        return {key: serialize_recursively(value) for key, value in obj.items()}
                    if isinstance(obj, (list, tuple)):
                        return [serialize_recursively(item) for item in obj]
    
                    # 3. Handle specific object types with known methods
                    if hasattr(obj, 'to_dict') and callable(obj.to_dict):
                        return serialize_recursively(obj.to_dict())
                    if hasattr(obj, 'model_dump') and callable(obj.model_dump):
                        return obj.model_dump() # Already recursive and serializable
                    if hasattr(obj, 'dict') and callable(obj.dict):
                        return obj.dict() # Already recursive and serializable
                    if hasattr(obj, 'value') and not callable(obj.value):
                        return obj.value
    
                    # 4. Handle Pydantic models and other objects with __dict__
                    if hasattr(obj, '__dict__'):
                        data = {}
                        for key, value in obj.__dict__.items():
                            if not key.startswith('_') and not isinstance(value, FieldInfo):
                                data[key] = serialize_recursively(value)
                        if data: # Only return if we found data
                            return data
    
                    # 5. Handle dataclasses (like Device/AlarmData) that don't use __dict__
                    data = {}
                    public_attrs = [attr for attr in dir(obj) if not attr.startswith('_') and not callable(getattr(obj, attr))]
                    for attr in public_attrs:
                        data[attr] = serialize_recursively(getattr(obj, attr))
                    if data:
                        return data
    
                    # 6. Final fallback
                    return str(obj)
    
                return serialize_recursively(result)
    
            except Exception as e:
                # Fallback to REST API on any SDK error
                return self._make_rest_api_call(op_info, **kwargs)
    
        return sdk_call
    
    
    def _default_resolve(self, name: str):
        """Fallback resolution when operation is not in registry."""
        snake = _CAMEL_TO_SNAKE.sub('_', name).lower()
        if hasattr(self._sdk, name): return getattr(self._sdk, name)
        if hasattr(self._sdk, snake): return getattr(self._sdk, snake)
    
        if hasattr(self, '_api'):
            for attr_name in dir(self._api):
                if attr_name.startswith('_'): continue
                attr = getattr(self._api, attr_name)
                if hasattr(attr, name): return getattr(attr, name)
                if hasattr(attr, snake): return getattr(attr, snake)
    
        raise AttributeError(f"{self.__class__.__name__} could not resolve attribute {name!r}")
    
    def __getattr__(self, name: str):
        """Dynamic <operationId> lookup, with exception trapping."""
        try:
            return self._resolve(name)
        except Exception as e:
            raise AttributeError(f"{self.__class__.__name__} could not resolve attribute {name!r} ({e})")
    
