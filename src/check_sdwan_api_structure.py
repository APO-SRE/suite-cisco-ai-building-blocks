#!/usr/bin/env python3
"""Check the actual structure of SD-WAN API endpoints"""
import os
from catalystwan.session import create_manager_session
from catalystwan.api.api_container import APIContainer
import inspect

# Create a session
print("Creating SD-WAN session...")
session = create_manager_session(
    url=os.getenv('CISCO_SD_WAN_BASE_URL'),
    username=os.getenv('CISCO_SD_WAN_USERNAME'),
    password=os.getenv('CISCO_SD_WAN_PASSWORD')
)

print("Session created successfully!")
print(f"Session type: {type(session)}")

# Get the API container
api = session.api
print(f"\nAPI Container type: {type(api)}")

# List all API endpoints
print("\nAvailable API endpoints:")
endpoints = []
for attr_name in dir(api):
    if not attr_name.startswith('_'):
        attr = getattr(api, attr_name)
        if attr is not None:
            endpoints.append((attr_name, attr))
            print(f"  - api.{attr_name}: {type(attr).__name__}")

# Check methods on a few key endpoints
print("\n\nMethods available on key endpoints:")
for endpoint_name in ['admin', 'device_state', 'config_group', 'alarms']:
    if hasattr(api, endpoint_name):
        endpoint = getattr(api, endpoint_name)
        print(f"\napi.{endpoint_name} methods:")
        methods = []
        for method_name in dir(endpoint):
            if not method_name.startswith('_'):
                method = getattr(endpoint, method_name)
                if callable(method):
                    try:
                        sig = inspect.signature(method)
                        params = list(sig.parameters.keys())
                        print(f"    - {method_name}({', '.join(params)})")
                        methods.append(method_name)
                    except:
                        print(f"    - {method_name}(...)")
        
        # Show if it has generic CRUD methods
        crud_methods = ['get', 'post', 'put', 'delete', 'create', 'update']
        has_crud = [m for m in crud_methods if m in methods]
        if has_crud:
            print(f"    Has CRUD methods: {has_crud}")

# Example: Try to map a specific operation
print("\n\nExample operation mapping:")
print("OpenAPI: findUsers_1 (GET /admin/user)")
print("SDK equivalent: api.administration.users.get()")
print("\nOpenAPI: getAaaConfig (GET /admin/aaa)")  
print("SDK equivalent: api.administration.aaa ???")