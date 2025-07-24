#!/usr/bin/env python3
"""Test SD-WAN operation ID matching"""
import sys
sys.path.insert(0, '.')
import json

# Load the coverage report
with open('app/llm/sdk_coverage/sdwan_mngr_coverage.json') as f:
    coverage = json.load(f)

print(f"Total operations: {coverage['total_operations']}")
print(f"Covered operations: {coverage['covered_operations']}")
print(f"SDK methods count: {coverage.get('sdk_methods_count', 'N/A')}")

# Check a few missing operation IDs
print("\nFirst 10 missing GET operations:")
get_ops = [op for op in coverage['missing_operations'] if op['method'] == 'get']
for i, op in enumerate(get_ops[:10]):
    print(f"  {i+1}. {op['operationId']} - {op['path']}")

# Now let's check what SDK methods were discovered
from app.utils.sdk_introspection import SDKIntrospector

print("\n\nRunning SDK introspection...")
introspector = SDKIntrospector('sdwan_mngr', 'catalystwan')
methods = introspector.discover_methods()

print(f"\nDiscovered {len(methods)} SDK methods")
print("\nFirst 20 SDK methods:")
for i, name in enumerate(list(methods.keys())[:20]):
    print(f"  {i+1}. {name}")

# Check for specific patterns
print("\n\nChecking for common patterns:")
aaa_methods = [m for m in methods if 'aaa' in m.lower()]
print(f"Methods with 'aaa': {len(aaa_methods)}")
if aaa_methods:
    print(f"  Examples: {aaa_methods[:5]}")

get_methods = [m for m in methods if m.startswith('get')]
print(f"Methods starting with 'get': {len(get_methods)}")
if get_methods:
    print(f"  Examples: {get_methods[:5]}")