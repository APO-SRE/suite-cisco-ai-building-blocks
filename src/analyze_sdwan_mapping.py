#!/usr/bin/env python3
"""Analyze SD-WAN OpenAPI operations and map them to SDK endpoints"""
import yaml
import json
from collections import defaultdict
from catalystwan.api.api_container import APIContainer

# Load OpenAPI spec
with open('source_open_api/cisco_catalyst_sd_wan_manager_api_2_0_0.yaml') as f:
    spec = yaml.safe_load(f)

# Analyze paths and group by first segment
path_groups = defaultdict(list)
operation_to_path = {}

for path, methods in spec.get('paths', {}).items():
    # Extract first path segment (e.g., /admin/user -> admin)
    segments = path.strip('/').split('/')
    if segments:
        first_segment = segments[0]
        
        for method, operation in methods.items():
            if method in ['get', 'post', 'put', 'delete', 'patch']:
                op_id = operation.get('operationId')
                if op_id:
                    path_groups[first_segment].append({
                        'operationId': op_id,
                        'method': method,
                        'path': path,
                        'description': operation.get('description', '')[:80]
                    })
                    operation_to_path[op_id] = (method, path)

# Show path segments and counts
print("OpenAPI Path Segments (first level):")
for segment, ops in sorted(path_groups.items(), key=lambda x: -len(x[1])):
    print(f"  /{segment}: {len(ops)} operations")
    if len(ops) <= 5:
        for op in ops:
            print(f"    - {op['operationId']} ({op['method'].upper()} {op['path']})")

# Now check what's available in the SDK
print("\n\nSD-WAN SDK API Container attributes:")
api_container = APIContainer(None, None)
api_attrs = []
for attr_name in dir(api_container):
    if not attr_name.startswith('_'):
        attr = getattr(api_container, attr_name, None)
        if attr is not None:
            api_attrs.append(attr_name)
            print(f"  - {attr_name}: {type(attr).__name__}")

# Try to map common patterns
print("\n\nPotential mappings:")
for segment in ['admin', 'device', 'template', 'certificate', 'system']:
    if segment in path_groups:
        # Check if there's a matching API attribute
        potential_matches = [api for api in api_attrs if segment in api.lower()]
        print(f"\n/{segment} ({len(path_groups[segment])} operations):")
        if potential_matches:
            print(f"  Potential SDK matches: {potential_matches}")
        else:
            print(f"  No direct SDK match found")
        
        # Show a few example operations
        for op in path_groups[segment][:3]:
            print(f"    - {op['operationId']}: {op['method'].upper()} {op['path']}")