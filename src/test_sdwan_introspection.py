#!/usr/bin/env python3
"""Test SD-WAN SDK introspection"""
import sys
sys.path.insert(0, '.')

from app.utils.sdk_introspection import SDKIntrospector

def test_sdwan_introspection():
    print("Testing SD-WAN SDK introspection...")
    introspector = SDKIntrospector('sdwan_mngr', 'catalystwan')
    methods = introspector.discover_methods()
    
    print(f"\nDiscovered {len(methods)} methods")
    
    # Show first 10 methods
    print("\nFirst 10 methods discovered:")
    for i, (name, method) in enumerate(list(methods.items())[:10]):
        print(f"  {i+1}. {name} (from {method.parent_class})")
        if method.sub_client:
            print(f"     Sub-client: {method.sub_client}")
    
    # Check for some expected methods
    print("\nChecking for specific method patterns:")
    get_methods = [name for name in methods if 'get' in name.lower()]
    print(f"  - Methods containing 'get': {len(get_methods)}")
    
    device_methods = [name for name in methods if 'device' in name.lower()]
    print(f"  - Methods containing 'device': {len(device_methods)}")
    
    return len(methods) > 100  # Expect many methods

if __name__ == "__main__":
    success = test_sdwan_introspection()
    print(f"\nTest {'PASSED' if success else 'FAILED'}")
    sys.exit(0 if success else 1)