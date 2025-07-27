#!/usr/bin/env python3
"""
Enhanced SD-WAN client generation that passes OpenAPI metadata through the call chain.
This eliminates the need for duplicating path/method info in the registry.
"""

import textwrap

def generate_enhanced_sdwan_dispatcher_method(fn_info, safe_name, platform):
    """
    Generate dispatcher method that includes OpenAPI metadata.
    """
    
    # Extract OpenAPI info from function definition
    # This info comes from the OpenAPI spec during scaffolding
    
    lines = [
        f"@register('{fn_info['name']}')",
        f"def {safe_name}({signature}):",
        '    """Auto-generated wrapper with OpenAPI metadata."""',
        "    # OpenAPI metadata from the spec",
        f"    _openapi_info = {{",
        f"        'path': '{path}',",  # From OpenAPI spec
        f"        'method': '{method}',",  # From OpenAPI spec
        f"        'operationId': '{fn_info['name']}'",
        f"    }}",
        "",
        "    # Build kwargs",
        "    final_kwargs = {}",
        # ... parameter handling ...,
        "",
        "    # Pass OpenAPI info along with the call",
        "    client = Sdwan_mngrClient()",
        "    return client.call_operation(",
        f"        operation_id='{fn_info['name']}',",
        "        openapi_info=_openapi_info,",
        "        **final_kwargs",
        "    )",
    ]
    
    return lines

def generate_enhanced_sdwan_client():
    """
    Generate an SD-WAN client that receives OpenAPI info from the dispatcher.
    """
    
    client_code = textwrap.dedent('''
    import json
    from pathlib import Path
    import requests
    from urllib.parse import urljoin
    
    class Sdwan_mngrClient:
        """Enhanced SD-WAN client that uses OpenAPI metadata from dispatcher."""
        
        def __init__(self, **kwargs):
            # ... existing init code ...
            
            # Load minimal SDK mappings (no OpenAPI duplication)
            self._sdk_mappings = self._load_sdk_mappings()
        
        def _load_sdk_mappings(self):
            """Load only SDK endpoint mappings, not full OpenAPI data."""
            registry_path = Path(__file__).parent.parent / 'sdwan_minimal_registry.json'
            if registry_path.exists():
                with open(registry_path) as f:
                    data = json.load(f)
                    return data.get('sdk_mappings', {})
            return {}
        
        def call_operation(self, operation_id: str, openapi_info: dict, **kwargs):
            """
            Execute an operation using either SDK or REST API.
            
            Args:
                operation_id: The operation ID from OpenAPI spec
                openapi_info: Dict with 'path' and 'method' from OpenAPI spec
                **kwargs: Operation parameters
            """
            
            # Check if we have an SDK mapping for this operation
            sdk_mapping = self._sdk_mappings.get(operation_id)
            
            if sdk_mapping:
                # Try SDK first
                try:
                    result = self._call_sdk_method(
                        sdk_mapping['sdk_endpoint'],
                        sdk_mapping['sdk_method'],
                        **kwargs
                    )
                    return self._serialize_recursively(result)
                except Exception as e:
                    # Fall back to REST API
                    pass
            
            # Use REST API (either no SDK mapping or SDK failed)
            return self._make_rest_api_call(
                path=openapi_info['path'],
                method=openapi_info['method'],
                **kwargs
            )
        
        def _call_sdk_method(self, endpoint_path: str, method_name: str, **kwargs):
            """Call SDK method."""
            endpoint = self._api
            for part in endpoint_path.split('.'):
                endpoint = getattr(endpoint, part)
            
            method = getattr(endpoint, method_name)
            return method(**kwargs)
        
        def _make_rest_api_call(self, path: str, method: str, **kwargs):
            """Make REST API call using OpenAPI info."""
            # Implementation similar to before, but using
            # path and method passed from dispatcher
            # ...
    ''')
    
    return client_code