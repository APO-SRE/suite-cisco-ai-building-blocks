#!/usr/bin/env python3
"""Test SD-WAN SDK introspection with logging"""
import sys
sys.path.insert(0, '.')

import logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s | %(message)s")

from app.utils.sdk_introspection import SDKIntrospector

def test_with_logging():
    print("Testing SD-WAN SDK introspection with logging...")
    introspector = SDKIntrospector('sdwan_mngr', 'catalystwan')
    
    print(f"SDK Pattern detected: {introspector.sdk_pattern}")
    
    methods = introspector.discover_methods()
    
    print(f"\nDiscovered {len(methods)} methods")
    
    if len(methods) > 0:
        print("\nFirst 5 methods:")
        for i, (name, method) in enumerate(list(methods.items())[:5]):
            print(f"  {i+1}. {name} (from {method.parent_class})")

if __name__ == "__main__":
    test_with_logging()