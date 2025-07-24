#!/usr/bin/env python3
"""Test SD-WAN function execution and response handling"""
import json
from app.llm.unified_service.sdwan_mngr_service import Sdwan_mngrServiceClient

def test_sdwan_functions():
    """Test various SD-WAN functions to see actual responses"""
    
    # Initialize the SD-WAN client
    print("Initializing SD-WAN client...")
    try:
        client = Sdwan_mngrServiceClient()
        print("✓ Client initialized successfully\n")
    except Exception as e:
        print(f"✗ Failed to initialize client: {e}")
        return
    
    # Test 1: List all devices
    print("Test 1: listAllDevices")
    print("-" * 50)
    try:
        result = client.call('listAllDevices')
        print(f"Type: {type(result)}")
        if isinstance(result, list):
            print(f"Count: {len(result)}")
            if result:
                print("First device:", json.dumps(result[0], indent=2)[:200] + "...")
        else:
            print("Result:", json.dumps(result, indent=2)[:500])
    except Exception as e:
        print(f"Error: {e}")
    
    print("\n" + "="*50 + "\n")
    
    # Test 2: Get all device status
    print("Test 2: getAllDeviceStatus")
    print("-" * 50)
    try:
        result = client.call('getAllDeviceStatus')
        print(f"Type: {type(result)}")
        if isinstance(result, list):
            print(f"Count: {len(result)}")
            if result:
                print("First device status:", json.dumps(result[0], indent=2)[:200] + "...")
        else:
            print("Result:", json.dumps(result, indent=2)[:500])
    except Exception as e:
        print(f"Error: {e}")
    
    print("\n" + "="*50 + "\n")
    
    # Test 3: Get all policy lists
    print("Test 3: getAllPolicyLists")
    print("-" * 50)
    try:
        result = client.call('getAllPolicyLists')
        print(f"Type: {type(result)}")
        if isinstance(result, dict) and 'error' in result:
            print("Error response:", json.dumps(result, indent=2))
        elif isinstance(result, list):
            print(f"Count: {len(result)}")
            if result:
                print("First policy:", json.dumps(result[0], indent=2)[:200] + "...")
        else:
            print("Result:", json.dumps(result, indent=2)[:500])
    except Exception as e:
        print(f"Error: {e}")
    
    print("\n" + "="*50 + "\n")
    
    # Test 4: Get alarms
    print("Test 4: getRawAlarmData")
    print("-" * 50)
    try:
        result = client.call('getRawAlarmData')
        print(f"Type: {type(result)}")
        if isinstance(result, dict):
            print("Keys:", list(result.keys()))
            print("Result preview:", json.dumps(result, indent=2)[:300] + "...")
        elif isinstance(result, list):
            print(f"Count: {len(result)}")
        else:
            print("Result:", result)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_sdwan_functions()