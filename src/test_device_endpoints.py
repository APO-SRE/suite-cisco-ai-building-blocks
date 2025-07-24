#!/usr/bin/env python3
"""Test what methods are available on device-related endpoints"""

import os
from dotenv import load_dotenv
load_dotenv()

# Check if we have the necessary credentials
if not all([os.getenv('CISCO_SD_WAN_BASE_URL'), 
            os.getenv('CISCO_SD_WAN_USERNAME'), 
            os.getenv('CISCO_SD_WAN_PASSWORD')]):
    print("SD-WAN credentials not found in environment")
    print("Please set: CISCO_SD_WAN_BASE_URL, CISCO_SD_WAN_USERNAME, CISCO_SD_WAN_PASSWORD")
    exit(1)

try:
    from catalystwan.session import create_manager_session
    import urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    
    # Create session
    session = create_manager_session(
        url=os.getenv('CISCO_SD_WAN_BASE_URL'),
        username=os.getenv('CISCO_SD_WAN_USERNAME'),
        password=os.getenv('CISCO_SD_WAN_PASSWORD')
    )
    
    api = session.api
    
    print("=== SD-WAN API Endpoints ===\n")
    
    # Check what's available on the main API
    print("Main API attributes:")
    for attr in sorted(dir(api)):
        if not attr.startswith('_'):
            print(f"  api.{attr}")
    
    # Check specific endpoints
    endpoints_to_check = ['devices', 'device_state', 'alarms', 'users']
    
    for endpoint_name in endpoints_to_check:
        if hasattr(api, endpoint_name):
            endpoint = getattr(api, endpoint_name)
            print(f"\n=== api.{endpoint_name} methods ===")
            methods = [m for m in dir(endpoint) if not m.startswith('_') and callable(getattr(endpoint, m))]
            for method in sorted(methods):
                print(f"  {method}")
                
    # Try to get devices using different approaches
    print("\n=== Testing device retrieval ===")
    
    # Method 1: api.devices.get()
    try:
        if hasattr(api, 'devices') and hasattr(api.devices, 'get'):
            result = api.devices.get()
            if hasattr(result, '__iter__'):
                devices = list(result)
                print(f"\napi.devices.get() returned {len(devices)} devices")
                if devices:
                    first = devices[0]
                    print(f"First device type: {type(first)}")
                    if hasattr(first, '__dict__'):
                        print(f"Device attributes: {list(vars(first).keys())[:10]}")
            else:
                print(f"\napi.devices.get() returned: {type(result)}")
    except Exception as e:
        print(f"\napi.devices.get() failed: {e}")
        
    # Method 2: Try session.endpoints.monitoring_device_details
    try:
        if hasattr(session, 'endpoints') and hasattr(session.endpoints, 'monitoring_device_details'):
            endpoint = session.endpoints.monitoring_device_details
            print(f"\n=== session.endpoints.monitoring_device_details methods ===")
            methods = [m for m in dir(endpoint) if not m.startswith('_') and callable(getattr(endpoint, m))]
            for method in sorted(methods)[:10]:
                print(f"  {method}")
    except:
        pass
        
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()