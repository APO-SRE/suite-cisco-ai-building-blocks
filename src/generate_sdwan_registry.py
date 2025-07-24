#!/usr/bin/env python3
"""Generate a complete SD-WAN operation registry from OpenAPI spec"""
import yaml
import json
import re
from pathlib import Path

# Load the OpenAPI spec
with open('source_open_api/cisco_catalyst_sd_wan_manager_api_2_0_0.yaml') as f:
    spec = yaml.safe_load(f)

# Known SDK endpoint mappings based on path patterns
# Based on SDK documentation: session.api.<endpoint>.method()
PATH_TO_SDK_ENDPOINT = {
    # Administration - Direct endpoint names as per SDK docs
    r'^/admin/user': 'users',
    r'^/admin/usergroup': 'user_groups',
    r'^/admin/aaa': 'administration_settings',
    r'^/admin/radius': 'administration_settings',
    r'^/admin/tacacs': 'administration_settings',
    r'^/admin/settings': 'administration_settings',
    r'^/admin/server': 'administration_settings',
    r'^/admin/cloudservices': 'administration_settings',
    
    # Alarms
    r'^/alarms': 'alarms',
    
    # Device Management
    r'^/device/status': 'device_state',
    r'^/device/monitor': 'device_monitor',
    r'^/device/statistics': 'statistics', 
    r'^/device/health': 'device_health',
    r'^/device/counters': 'device_counters',
    r'^/device/control': 'device_control',
    r'^/device/bfd': 'device_bfd',
    r'^/device/interface': 'device_interface',
    r'^/device/tunnel': 'device_tunnel',
    r'^/device/system': 'device_system',
    r'^/device$': 'devices',
    
    # Templates and Configuration
    r'^/template/device': 'configuration.device_template',
    r'^/template/feature': 'configuration.feature_template',
    r'^/template/policy': 'configuration.policy',
    
    # Certificates
    r'^/certificate/device': 'certificate.device',
    r'^/certificate$': 'certificate.management',
    
    # System
    r'^/system/device': 'system.device',
    r'^/system$': 'system.management',
    
    # Monitoring/Statistics
    r'^/statistics': 'monitoring.statistics',
    r'^/stream': 'monitoring.stream',
    
    # Default v1 APIs
    r'^/v1/': 'v1.',
}

def map_path_to_sdk_endpoint(path):
    """Map an API path to an SDK endpoint"""
    # Try each pattern
    for pattern, endpoint in PATH_TO_SDK_ENDPOINT.items():
        if re.match(pattern, path):
            # For v1 APIs, try to extract the next segment
            if endpoint == 'v1.':
                segments = path.strip('/').split('/')
                if len(segments) > 1:
                    return f"v1.{segments[1].replace('-', '_')}"
            return endpoint
    
    # Fallback: use first two path segments
    segments = path.strip('/').split('/')
    if len(segments) >= 2:
        return f"{segments[0]}.{segments[1].replace('-', '_')}"
    elif segments:
        return segments[0]
    return 'unknown'

def get_sdk_method(http_method):
    """Map HTTP method to SDK method"""
    mapping = {
        'get': 'get',
        'post': 'create',
        'put': 'update', 
        'delete': 'delete',
        'patch': 'update'
    }
    return mapping.get(http_method, 'get')

# Generate the registry
registry = {
    "comment": "Auto-generated SD-WAN Operation Registry",
    "operations": {},
    "statistics": {
        "total_operations": 0,
        "get_operations": 0,
        "mapped_operations": 0,
        "unmapped_operations": []
    }
}

# Process all paths
for path, path_item in spec.get('paths', {}).items():
    for method, operation in path_item.items():
        if method not in ['get', 'post', 'put', 'delete', 'patch']:
            continue
            
        op_id = operation.get('operationId')
        if not op_id:
            continue
            
        # Fix generic operation names
        if op_id.lower() in ['get', 'post', 'put', 'delete', 'patch'] or len(op_id) <= 3:
            # Generate a better name from the path
            path_parts = path.strip('/').split('/')
            # Remove version prefix and parameters
            clean_parts = [p for p in path_parts if not p.startswith('v') and not p.startswith('{')]
            if clean_parts:
                # Create camelCase name
                new_name = method
                for part in clean_parts:
                    words = part.replace('-', '_').split('_')
                    new_name += ''.join(word.capitalize() for word in words)
                op_id = new_name
            else:
                # Fallback: use method + path hash
                import hashlib
                path_hash = hashlib.md5(path.encode()).hexdigest()[:6]
                op_id = f"{method}_{path_hash}"
            
        registry['statistics']['total_operations'] += 1
        if method == 'get':
            registry['statistics']['get_operations'] += 1
        
        # Map to SDK
        sdk_endpoint = map_path_to_sdk_endpoint(path)
        sdk_method = get_sdk_method(method)
        
        # Check if it needs special handling
        needs_id = bool(re.search(r'\{[^}]+\}', path))
        has_query_params = bool(operation.get('parameters', []))
        
        # Create the operation entry
        op_entry = {
            'path': path,
            'method': method,
            'sdk_endpoint': sdk_endpoint,
            'sdk_method': sdk_method,
            'description': operation.get('description', '')[:200]
        }
        
        # Add metadata
        if needs_id:
            op_entry['needs_id'] = True
            # Extract parameter names
            params = re.findall(r'\{([^}]+)\}', path)
            op_entry['path_params'] = params
            
        if has_query_params:
            query_params = []
            for param in operation.get('parameters', []):
                if param.get('in') == 'query':
                    query_params.append({
                        'name': param.get('name'),
                        'type': param.get('schema', {}).get('type', 'string'),
                        'required': param.get('required', False)
                    })
            if query_params:
                op_entry['query_params'] = query_params
        
        # Check if we have a good mapping
        if sdk_endpoint != 'unknown':
            registry['statistics']['mapped_operations'] += 1
        else:
            registry['statistics']['unmapped_operations'].append(op_id)
        
        registry['operations'][op_id] = op_entry

# Save the registry
output_path = Path('app/llm/sdwan_operation_registry_full.json')
output_path.write_text(json.dumps(registry, indent=2))

print(f"Generated SD-WAN operation registry:")
print(f"  Total operations: {registry['statistics']['total_operations']}")
print(f"  GET operations: {registry['statistics']['get_operations']}")
print(f"  Mapped operations: {registry['statistics']['mapped_operations']}")
print(f"  Unmapped operations: {len(registry['statistics']['unmapped_operations'])}")
print(f"\nRegistry saved to: {output_path}")

# Show some examples
print("\nExample mappings:")
examples = ['findUsers_1', 'getAllDeviceStatus', 'getAaaConfig', 'getAlarms', 'listAllDevices']
for ex in examples:
    if ex in registry['operations']:
        op = registry['operations'][ex]
        print(f"  {ex}: {op['method'].upper()} {op['path']} -> {op['sdk_endpoint']}.{op['sdk_method']}()")