#!/usr/bin/env python3
"""Debug SD-WAN SDK endpoints"""
import os

# Set environment variables if not already set
os.environ.setdefault('CISCO_SD_WAN_BASE_URL', 'https://sandbox-sdwan-2.cisco.com')
os.environ.setdefault('CISCO_SD_WAN_USERNAME', 'devnetuser')
os.environ.setdefault('CISCO_SD_WAN_PASSWORD', 'RG!_Yw919_83')

from catalystwan.session import create_manager_session

print("Debugging SD-WAN SDK Structure...")
print("="*60)

try:
    # Create session
    session = create_manager_session(
        url=os.getenv('CISCO_SD_WAN_BASE_URL'),
        username=os.getenv('CISCO_SD_WAN_USERNAME'),
        password=os.getenv('CISCO_SD_WAN_PASSWORD')
    )
    print("✓ Session created successfully")
    
    # Check API structure
    api = session.api
    print("\nAPI Container attributes:")
    api_attrs = [a for a in dir(api) if not a.startswith('_')]
    for attr in sorted(api_attrs)[:20]:
        print(f"  - {attr}")
    
    # Check specific endpoints mentioned in errors
    print("\nChecking specific endpoints:")
    
    # Administration
    if hasattr(api, 'administration'):
        print("\n✓ Found 'administration' endpoint")
        admin = api.administration
        admin_attrs = [a for a in dir(admin) if not a.startswith('_')]
        print(f"  Attributes: {admin_attrs}")
        
        if hasattr(admin, 'users'):
            print("  ✓ Has 'users' sub-endpoint")
    
    # Check for users endpoint directly
    if hasattr(api, 'users'):
        print("\n✓ Found direct 'users' endpoint")
        users = api.users
        methods = [m for m in dir(users) if not m.startswith('_') and callable(getattr(users, m))]
        print(f"  Methods: {methods}")
    
    # Check config endpoints
    if hasattr(api, 'config'):
        print("\n✓ Found 'config' endpoint")
        config = api.config
        config_attrs = [a for a in dir(config) if not a.startswith('_')]
        print(f"  Attributes: {config_attrs[:10]}...")
    
    # Try to find user-related endpoints
    print("\nSearching for user-related endpoints:")
    for attr_name in api_attrs:
        if 'user' in attr_name.lower() or 'admin' in attr_name.lower():
            print(f"  - {attr_name}")
            attr = getattr(api, attr_name)
            if hasattr(attr, '__dict__'):
                sub_attrs = [a for a in dir(attr) if not a.startswith('_')][:5]
                print(f"    Sub-attributes: {sub_attrs}")
    
    # Try some direct calls
    print("\nTrying direct API calls:")
    
    # Try to get devices
    if hasattr(api, 'devices'):
        print("\nTrying api.devices.get()...")
        try:
            devices = api.devices.get()
            print(f"  ✓ Success! Got {len(list(devices))} devices")
        except Exception as e:
            print(f"  ✗ Error: {e}")
    
    # Try configuration endpoints
    if hasattr(api, 'configuration'):
        print("\nChecking configuration endpoint...")
        config = api.configuration
        config_attrs = [a for a in dir(config) if not a.startswith('_')]
        print(f"  Attributes: {config_attrs[:10]}...")

except Exception as e:
    import traceback
    print(f"\n✗ Error: {e}")
    print(traceback.format_exc())

print("\n" + "="*60)