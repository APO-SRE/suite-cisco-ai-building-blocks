#!/usr/bin/env python3
"""
Test if the alarms.get SDK method exists and works
"""
from catalystwan.session import ManagerSession
from catalystwan.vmanage_auth import vManageAuth
import os

def test_alarms_method():
    """Test if alarms.get exists in the SDK"""
    print("Testing alarms SDK method...")
    
    # Create dummy session
    dummy_auth = vManageAuth(username="dummy", password="dummy")
    session = ManagerSession(base_url="https://dummy", auth=dummy_auth)
    
    # Check if alarms endpoint exists
    if hasattr(session.api, 'alarms'):
        print("✓ session.api.alarms exists")
        alarms_endpoint = session.api.alarms
        
        # Check available methods
        methods = [m for m in dir(alarms_endpoint) if not m.startswith('_') and callable(getattr(alarms_endpoint, m))]
        print(f"✓ Available methods on alarms endpoint: {methods}")
        
        # Check if get method exists
        if hasattr(alarms_endpoint, 'get'):
            print("✓ alarms.get method exists")
            
            # Get method signature
            import inspect
            sig = inspect.signature(alarms_endpoint.get)
            print(f"✓ Method signature: {sig}")
            
            # Check docstring
            doc = inspect.getdoc(alarms_endpoint.get)
            print(f"✓ Method documentation: {doc}")
            
            return True
        else:
            print("✗ alarms.get method NOT found")
            return False
    else:
        print("✗ session.api.alarms NOT found")
        return False

def check_operation_mapping():
    """Check how getRawAlarmData should be mapped"""
    print("\n=== MAPPING ANALYSIS ===")
    print("Operation ID: getRawAlarmData")
    print("OpenAPI path: /alarms")
    print("OpenAPI method: GET")
    print("\nSDK mapping should be:")
    print("  sdk_endpoint: alarms")
    print("  sdk_method: get")
    print("  use_direct_api: false")
    print("\nCurrent registry has:")
    print("  use_direct_api: true (INCORRECT - SDK method exists!)")

if __name__ == "__main__":
    if test_alarms_method():
        check_operation_mapping()
        print("\n✅ The getRawAlarmData operation SHOULD use the SDK method alarms.get")
        print("   The registry needs to be updated to set use_direct_api: false")
    else:
        print("\n✗ No SDK method found - direct API is correct")