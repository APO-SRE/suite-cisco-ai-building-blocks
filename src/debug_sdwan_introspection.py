#!/usr/bin/env python3
"""Debug SD-WAN SDK introspection"""
import sys
sys.path.insert(0, '.')

from catalystwan.api.api_container import APIContainer

def debug_api_container():
    print("Creating APIContainer with None values...")
    api_container = APIContainer(None, None)
    
    print("\nAll attributes of APIContainer:")
    for attr_name in sorted(dir(api_container)):
        if not attr_name.startswith('_'):
            try:
                attr = getattr(api_container, attr_name)
                print(f"  - {attr_name}: {type(attr).__name__} = {attr}")
            except Exception as e:
                print(f"  - {attr_name}: ERROR: {e}")
    
    print("\nChecking specific API endpoints...")
    # Try to access some common endpoints
    for endpoint in ['device', 'monitoring', 'configuration', 'admin']:
        try:
            api = getattr(api_container, endpoint, None)
            if api:
                print(f"\n{endpoint} API:")
                print(f"  Type: {type(api)}")
                print(f"  Methods: {[m for m in dir(api) if not m.startswith('_')][:5]}...")
        except Exception as e:
            print(f"\n{endpoint} API: ERROR: {e}")

if __name__ == "__main__":
    debug_api_container()