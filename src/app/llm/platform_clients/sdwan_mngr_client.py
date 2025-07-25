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
                cls._operation_registry = {'operations': {}, 'comment': 'Registry file not found'}
        return cls._operation_registry
    
    def _resolve(self, name: str):
        """Custom resolution for SD-WAN operations"""
        registry = self._load_registry()
        op_info = registry.get('operations', {}).get(name)
        if not op_info:
            return self._default_resolve(name)
    
        def sdk_call(**kwargs):
            try:
                # ... (this part of the function is correct and remains the same) ...
    
                result = method(**call_params)
    
                # --- THIS IS THE NEW, BULLETPROOF SERIALIZATION LOGIC ---
                def serialize_item(item):
                    """
                    Serialize a single item from the catalystwan SDK, robustly handling
                    all known object types.
                    """
                    # If it's a basic type, return it immediately.
                    if item is None or isinstance(item, (str, int, float, bool, dict, list)):
                        return item
    
                    # 1. First, try the standard .to_dict() method.
                    if hasattr(item, 'to_dict') and callable(item.to_dict):
                        return item.to_dict()
    
                    # 2. If that fails, build a dictionary from the object's public attributes.
                    #    This handles dataclasses like Device and AlarmData.
                    item_dict = {}
                    # Get attributes that are not private and not methods.
                    public_attrs = [attr for attr in dir(item) if not attr.startswith('_') and not callable(getattr(item, attr))]
    
                    for attr in public_attrs:
                        value = getattr(item, attr)
                        # Handle nested Enum types (like Severity.CRITICAL -> "Critical")
                        if hasattr(value, 'value'):
                            item_dict[attr] = value.value
                        # Handle other basic types
                        elif isinstance(value, (str, int, float, bool, dict, list, type(None))):
                            item_dict[attr] = value
                        # For other nested objects, convert them to a string as a safe fallback
                        else:
                            item_dict[attr] = str(value)
    
                    # Only return the dict if it has content
                    if item_dict:
                        return item_dict
    
                    # If all else fails, return a string representation of the object
                    return str(item)
    
                # Check if the result is iterable (like a list or DataSequence)
                if hasattr(result, '__iter__') and not isinstance(result, (str, bytes, dict)):
                    return [serialize_item(item) for item in result]
    
                # If the result is a single object, serialize it.
                return serialize_item(result)
    
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
    
