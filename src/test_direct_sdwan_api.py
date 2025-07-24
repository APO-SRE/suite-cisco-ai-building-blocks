#!/usr/bin/env python3
"""Test SD-WAN API calls directly through the dispatcher"""
import os
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent))

# Import the dispatcher
from app.llm.function_dispatcher import dispatch_function_call

print("Testing SD-WAN Operations Directly...")
print("="*60)

# Test operations that should work
test_operations = [
    ("findUsers_1", {}),
    ("listAllDevices", {}),
    ("getAaaConfig", {}),
    ("getAllDeviceStatus", {}),
]

for op_name, params in test_operations:
    print(f"\nTesting {op_name}...")
    try:
        result = dispatch_function_call(op_name, params)
        print(f"✓ Success!")
        if isinstance(result, dict) and 'error' in result:
            print(f"  Error response: {result['error']}")
            if 'available' in result:
                print(f"  Available: {result['available']}")
        elif isinstance(result, list):
            print(f"  Got {len(result)} items")
        else:
            print(f"  Result type: {type(result)}")
            print(f"  Result preview: {str(result)[:100]}...")
    except Exception as e:
        print(f"✗ Error: {e}")
        import traceback
        traceback.print_exc()

print("\n" + "="*60)