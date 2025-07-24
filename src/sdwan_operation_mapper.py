#!/usr/bin/env python3
"""
SD-WAN Operation Mapper - Maps OpenAPI operation IDs to SDK methods

The SD-WAN SDK (catalystwan) uses a different pattern than the OpenAPI spec:
- OpenAPI: Specific operation IDs like 'findUsers_1', 'getAaaConfig'
- SDK: Generic CRUD methods on API endpoint objects

This mapper translates between the two patterns.
"""
import re
from typing import Dict, Tuple, Optional, Any

class SDWANOperationMapper:
    """Maps OpenAPI operation IDs to SD-WAN SDK API calls"""
    
    # Known mappings from path segments to API endpoints
    PATH_TO_API_ENDPOINT = {
        # Administration
        'admin/user': 'administration.users',
        'admin/usergroup': 'administration.user_groups',
        'admin/aaa': 'administration.aaa',
        'admin/radius': 'administration.radius',
        'admin/tacacs': 'administration.tacacs',
        'admin/server': 'administration.server',
        'admin/settings': 'administration.settings',
        
        # Device management
        'device': 'devices',
        'device/status': 'device_state',
        'device/monitor': 'monitoring_device',
        'device/system': 'real_time_monitoring.system',
        'device/control': 'real_time_monitoring.control',
        'device/bfd': 'real_time_monitoring.bfd',
        'device/interface': 'real_time_monitoring.interface',
        
        # Configuration
        'template/device': 'configuration.device_template',
        'template/feature': 'configuration.feature_template',
        'template/policy': 'configuration.policy',
        
        # Alarms and events
        'alarms': 'alarms',
        'event': 'event',
        'auditlog': 'audit_log',
        
        # Certificates
        'certificate': 'certificate',
        'certificate/device': 'certificate.device',
        'certificate/enterprise': 'certificate.enterprise',
        
        # System
        'system': 'system',
        'system/device': 'system.device',
        'system/backup': 'system.backup',
    }
    
    # HTTP method to SDK method mapping
    HTTP_TO_SDK_METHOD = {
        'get': 'get',
        'post': 'create',
        'put': 'update',
        'delete': 'delete',
        'patch': 'update'
    }
    
    @classmethod
    def map_operation(cls, operation_id: str, http_method: str, path: str) -> Dict[str, Any]:
        """
        Map an OpenAPI operation to an SDK method call
        
        Returns a dict with:
        - api_endpoint: The SDK API endpoint (e.g., 'administration.users')
        - sdk_method: The method to call (e.g., 'get')
        - needs_id: Whether an ID parameter is needed
        - custom_params: Any custom parameter mappings
        """
        # Clean up the path
        clean_path = path.strip('/').split('?')[0]  # Remove query params
        clean_path = re.sub(r'/\{[^}]+\}', '', clean_path)  # Remove path params
        
        # Find the best matching API endpoint
        api_endpoint = None
        for path_pattern, endpoint in cls.PATH_TO_API_ENDPOINT.items():
            if clean_path.startswith(path_pattern):
                api_endpoint = endpoint
                break
        
        if not api_endpoint:
            # Try a generic mapping based on first path segment
            first_segment = clean_path.split('/')[0]
            api_endpoint = cls._guess_api_endpoint(first_segment)
        
        # Determine SDK method
        sdk_method = cls.HTTP_TO_SDK_METHOD.get(http_method, 'get')
        
        # Check if this needs an ID parameter
        needs_id = '{' in path and '}' in path
        
        # Build the mapping
        mapping = {
            'api_endpoint': api_endpoint,
            'sdk_method': sdk_method,
            'needs_id': needs_id,
            'original_path': path,
            'operation_id': operation_id
        }
        
        # Add any operation-specific customizations
        mapping.update(cls._get_custom_params(operation_id, path))
        
        return mapping
    
    @classmethod
    def _guess_api_endpoint(cls, first_segment: str) -> str:
        """Guess API endpoint from first path segment"""
        # Common patterns
        if first_segment == 'v1':
            return 'v1_api'  # Generic v1 API
        elif 'device' in first_segment:
            return 'devices'
        elif 'template' in first_segment:
            return 'configuration.template'
        elif 'policy' in first_segment:
            return 'configuration.policy'
        else:
            # Convert to potential API name
            return first_segment.replace('-', '_')
    
    @classmethod
    def _get_custom_params(cls, operation_id: str, path: str) -> Dict[str, Any]:
        """Get any custom parameters for specific operations"""
        custom = {}
        
        # Handle specific operations that need special treatment
        if operation_id == 'findUsers_1':
            custom['filter_key'] = 'userName'
        elif operation_id == 'getAllDeviceStatus':
            custom['response_key'] = 'data'
        elif 'ByQuery' in operation_id:
            custom['requires_body'] = True
        
        return custom
    
    @classmethod
    def generate_sdk_call(cls, mapping: Dict[str, Any], **kwargs) -> str:
        """Generate the actual SDK call code"""
        api_endpoint = mapping['api_endpoint']
        sdk_method = mapping['sdk_method']
        
        # Build the call
        call_parts = ['session.api']
        for part in api_endpoint.split('.'):
            call_parts.append(part)
        
        # Add the method
        method_call = f".{sdk_method}("
        
        # Add parameters
        params = []
        if mapping.get('needs_id') and 'id' in kwargs:
            params.append(f"id='{kwargs['id']}'")
        
        if mapping.get('requires_body') and 'body' in kwargs:
            params.append(f"body={kwargs['body']}")
        
        # Add any other kwargs
        for key, value in kwargs.items():
            if key not in ['id', 'body']:
                params.append(f"{key}={repr(value)}")
        
        method_call += ', '.join(params) + ')'
        
        return '.'.join(call_parts) + method_call


# Example usage
if __name__ == "__main__":
    # Test some mappings
    test_operations = [
        ('findUsers_1', 'get', '/admin/user'),
        ('getAaaConfig', 'get', '/admin/aaa'),
        ('getAllDeviceStatus', 'get', '/device/status'),
        ('createUser_1', 'post', '/admin/user'),
        ('deleteDevice', 'delete', '/device/{deviceId}'),
    ]
    
    print("SD-WAN Operation Mappings:")
    print("-" * 80)
    
    for op_id, method, path in test_operations:
        mapping = SDWANOperationMapper.map_operation(op_id, method, path)
        sdk_call = SDWANOperationMapper.generate_sdk_call(mapping, id='123')
        
        print(f"\nOperation: {op_id}")
        print(f"  HTTP: {method.upper()} {path}")
        print(f"  SDK Endpoint: {mapping['api_endpoint']}")
        print(f"  SDK Method: {mapping['sdk_method']}")
        print(f"  Example Call: {sdk_call}")