#!/usr/bin/env python3
"""Debug SD-WAN device operations mapping"""

import json
from pathlib import Path

# Load the operation registry
registry_path = Path('app/llm/sdwan_operation_registry_full.json')
with open(registry_path) as f:
    registry = json.load(f)

# Find all device-related operations
device_ops = {}
for op_name, op_info in registry['operations'].items():
    if 'device' in op_name.lower() or '/device' in op_info.get('path', ''):
        device_ops[op_name] = op_info

print("=== Device Operations in Registry ===")
print(f"Total device operations: {len(device_ops)}")
print()

# Group by endpoint
by_endpoint = {}
for op_name, op_info in device_ops.items():
    endpoint = op_info.get('sdk_endpoint', 'unknown')
    if endpoint not in by_endpoint:
        by_endpoint[endpoint] = []
    by_endpoint[endpoint].append((op_name, op_info))

# Show operations by endpoint
for endpoint, ops in sorted(by_endpoint.items()):
    print(f"\n=== Endpoint: {endpoint} ({len(ops)} operations) ===")
    for op_name, op_info in sorted(ops)[:5]:  # Show first 5
        print(f"  {op_name}: {op_info.get('path')} - {op_info.get('description', 'N/A')[:60]}")
    if len(ops) > 5:
        print(f"  ... and {len(ops) - 5} more")

# Look specifically for the operations that should list all devices
print("\n=== Operations that should list all devices ===")
list_ops = ['listAllDevices', 'getAllDeviceStatus', 'getDeviceListAsKeyValue', 'getConnectedDevices']
for op_name in list_ops:
    if op_name in registry['operations']:
        op = registry['operations'][op_name]
        print(f"\n{op_name}:")
        print(f"  Path: {op.get('path')}")
        print(f"  SDK Endpoint: {op.get('sdk_endpoint')}")
        print(f"  SDK Method: {op.get('sdk_method')}")
        print(f"  Description: {op.get('description')}")

# Check current mapping
print("\n=== Current Path to SDK Mappings ===")
paths_to_check = ['/device', '/device/status', '/device/list']
for path in paths_to_check:
    # Find operations with this path
    found = False
    for op_name, op_info in registry['operations'].items():
        if op_info.get('path') == path:
            print(f"{path} -> {op_info.get('sdk_endpoint')}")
            found = True
            break
    if not found:
        print(f"{path} -> Not found")