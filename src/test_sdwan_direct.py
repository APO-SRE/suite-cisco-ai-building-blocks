#!/usr/bin/env python3
"""Test SD-WAN operations directly"""
import os
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent))

from app.llm.platform_clients.sdwan_mngr_client import Sdwan_mngrClient

# Test direct client usage
print("Testing SD-WAN Client Direct Access...")
print("="*60)

try:
    # Create client
    client = Sdwan_mngrClient()
    print("✓ Client created successfully")
    
    # Test registry loading
    registry = client._load_registry()
    print(f"✓ Registry loaded: {len(registry.get('operations', {}))} operations")
    
    # Check if listAllDevices exists
    if 'listAllDevices' in registry.get('operations', {}):
        op_info = registry['operations']['listAllDevices']
        print(f"\n✓ Found listAllDevices operation:")
        print(f"  Path: {op_info['path']}")
        print(f"  Method: {op_info['method']}")
        print(f"  SDK Endpoint: {op_info['sdk_endpoint']}")
        print(f"  SDK Method: {op_info['sdk_method']}")
    
    # Try to call it directly
    print("\nTrying to call listAllDevices...")
    try:
        result = client.listAllDevices()
        print(f"✓ Success! Result type: {type(result)}")
        if isinstance(result, dict) and 'error' in result:
            print(f"  Error: {result['error']}")
            if 'available' in result:
                print(f"  Available endpoints: {result['available']}")
        elif isinstance(result, list):
            print(f"  Got {len(result)} devices")
            if result:
                print(f"  First device: {result[0]}")
        else:
            print(f"  Result: {result}")
    except Exception as e:
        print(f"✗ Error calling listAllDevices: {e}")
    
    # Check what's available on the API
    print("\nChecking available API endpoints...")
    if hasattr(client, '_api'):
        api_attrs = [a for a in dir(client._api) if not a.startswith('_')]
        print(f"API attributes: {api_attrs[:10]}...")
        
        # Check if devices endpoint exists
        if hasattr(client._api, 'devices'):
            print("\n✓ Found 'devices' endpoint")
            devices_api = client._api.devices
            methods = [m for m in dir(devices_api) if not m.startswith('_') and callable(getattr(devices_api, m))]
            print(f"  Available methods: {methods}")
        
        # Try alternate endpoints
        for endpoint in ['device_state', 'configuration', 'monitoring']:
            if hasattr(client._api, endpoint):
                print(f"\n✓ Found '{endpoint}' endpoint")
                ep = getattr(client._api, endpoint)
                methods = [m for m in dir(ep) if not m.startswith('_') and callable(getattr(ep, m))][:5]
                print(f"  Sample methods: {methods}")
    
except Exception as e:
    import traceback
    print(f"\n✗ Error: {e}")
    print(traceback.format_exc())

print("\n" + "="*60)
print("Test complete")