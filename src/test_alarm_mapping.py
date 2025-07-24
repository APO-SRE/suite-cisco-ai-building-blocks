#!/usr/bin/env python3
"""Test script to understand SD-WAN alarm data retrieval"""

import json
from pathlib import Path

# Load the operation registry
registry_path = Path(__file__).parent / 'app' / 'llm' / 'sdwan_operation_registry_full.json'
with open(registry_path) as f:
    registry = json.load(f)

# Find all alarm-related operations
alarm_ops = {}
for op_name, op_info in registry['operations'].items():
    if 'alarm' in op_name.lower() or 'alarm' in op_info.get('path', '').lower():
        alarm_ops[op_name] = op_info

print("=== SD-WAN Alarm Operations ===")
print(f"Total alarm operations found: {len(alarm_ops)}")
print()

# Group by method type
by_method = {}
for op_name, op_info in alarm_ops.items():
    method = op_info.get('method', 'unknown')
    if method not in by_method:
        by_method[method] = []
    by_method[method].append((op_name, op_info))

# Show GET operations that should return alarm data
print("=== GET Operations for Alarms ===")
if 'get' in by_method:
    for op_name, op_info in sorted(by_method['get']):
        print(f"\nOperation: {op_name}")
        print(f"  Path: {op_info.get('path')}")
        print(f"  SDK Endpoint: {op_info.get('sdk_endpoint')}")
        print(f"  SDK Method: {op_info.get('sdk_method')}")
        print(f"  Description: {op_info.get('description', 'N/A')}")
        
        # Show parameters if any
        if op_info.get('query_params'):
            print("  Query Parameters:")
            for param in op_info['query_params']:
                req = "required" if param.get('required') else "optional"
                print(f"    - {param['name']} ({param.get('type', 'unknown')}) [{req}]")

# Look for operations that might return full alarm details
print("\n=== Operations that likely return alarm details ===")
detail_keywords = ['data', 'detail', 'info', 'get', 'list', 'view']
for op_name, op_info in alarm_ops.items():
    if any(kw in op_name.lower() for kw in detail_keywords) and op_info.get('method') == 'get':
        print(f"\n{op_name}:")
        print(f"  Path: {op_info.get('path')}")
        print(f"  Description: {op_info.get('description', 'N/A')}")