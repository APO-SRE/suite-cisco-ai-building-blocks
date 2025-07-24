#!/usr/bin/env python3
"""Test the SD-WAN client to see how it handles alarm queries"""

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.llm.platform_clients.sdwan_mngr_client import Sdwan_mngrClient

def test_alarm_operations():
    """Test various alarm operations"""
    
    print("=== Testing SD-WAN Client Alarm Operations ===\n")
    
    # Create client
    try:
        client = Sdwan_mngrClient()
        print("✓ Client created successfully\n")
    except Exception as e:
        print(f"✗ Failed to create client: {e}")
        return
    
    # Test operations to try
    operations = [
        ("getRawAlarmData", {}),
        ("getRawAlarmData", {"query": "{}"}),  # Empty query for all alarms
        ("getActiveAlarms", {}),
        ("getNonViewedAlarms", {}),
        ("getAlarmDetails", {}),
        # Direct endpoint access
        ("_api.alarms.get", {}),
    ]
    
    for op_name, params in operations:
        print(f"\n--- Testing: {op_name} ---")
        try:
            if op_name.startswith("_api."):
                # Direct API access
                parts = op_name.split('.')[1:]  # Remove _api
                endpoint = client._api
                for part in parts[:-1]:
                    endpoint = getattr(endpoint, part)
                method = getattr(endpoint, parts[-1])
                result = method(**params)
            else:
                # Operation through registry
                operation = getattr(client, op_name)
                result = operation(**params)
            
            # Show result type and sample
            if result is None:
                print("Result: None")
            elif isinstance(result, dict):
                if 'error' in result:
                    print(f"Error: {result['error']}")
                    if 'available' in result:
                        print(f"Available: {result['available']}")
                else:
                    print(f"Result type: dict with {len(result)} keys")
                    print(f"Keys: {list(result.keys())[:5]}")
                    if 'data' in result:
                        data = result['data']
                        if isinstance(data, list):
                            print(f"Data: list with {len(data)} items")
                            if data:
                                print(f"First item: {data[0]}")
            elif isinstance(result, list):
                print(f"Result type: list with {len(result)} items")
                if result:
                    first = result[0]
                    print(f"First item type: {type(first)}")
                    if hasattr(first, '__dict__'):
                        print(f"First item attrs: {list(vars(first).keys())[:10]}")
                    else:
                        print(f"First item: {first}")
            else:
                print(f"Result type: {type(result)}")
                if hasattr(result, '__iter__') and not isinstance(result, str):
                    try:
                        items = list(result)
                        print(f"Iterable with {len(items)} items")
                        if items:
                            print(f"First item: {items[0]}")
                    except:
                        print("Could not iterate")
                        
        except AttributeError as e:
            print(f"AttributeError: {e}")
        except Exception as e:
            print(f"Exception ({type(e).__name__}): {e}")
            import traceback
            traceback.print_exc()

if __name__ == "__main__":
    test_alarm_operations()