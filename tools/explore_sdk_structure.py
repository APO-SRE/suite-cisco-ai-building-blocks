#!/usr/bin/env python3
"""
Explore the catalystwan SDK structure to understand how endpoints and methods are organized.
"""
import inspect
from types import ModuleType
from catalystwan.session import ManagerSession
from catalystwan.vmanage_auth import vManageAuth
import json

def explore_sdk_tree(obj, path="", visited=None, max_depth=5, current_depth=0):
    """
    Recursively explore the SDK object tree and map all callable methods.
    """
    if visited is None:
        visited = set()
    
    if current_depth >= max_depth:
        return {}
    
    # Avoid infinite recursion
    obj_id = id(obj)
    if obj_id in visited:
        return {}
    visited.add(obj_id)
    
    result = {}
    
    # Get all attributes
    for attr_name in dir(obj):
        # Skip private/magic methods
        if attr_name.startswith('_'):
            continue
            
        try:
            attr = getattr(obj, attr_name)
            current_path = f"{path}.{attr_name}" if path else attr_name
            
            # If it's callable, record it
            if callable(attr) and not isinstance(attr, type):
                result[current_path] = {
                    'type': 'method',
                    'doc': inspect.getdoc(attr) or 'No documentation',
                    'signature': str(inspect.signature(attr)) if hasattr(inspect, 'signature') else 'N/A'
                }
            # If it's an object with attributes (not a module), explore deeper
            elif hasattr(attr, '__dict__') and not isinstance(attr, ModuleType):
                # Record this as an endpoint/namespace
                result[current_path] = {
                    'type': 'endpoint',
                    'methods': []
                }
                # Explore its methods
                sub_results = explore_sdk_tree(attr, current_path, visited, max_depth, current_depth + 1)
                result.update(sub_results)
                # Update the methods list for this endpoint
                for sub_path, sub_info in sub_results.items():
                    if sub_info['type'] == 'method' and sub_path.startswith(current_path + '.'):
                        method_name = sub_path[len(current_path) + 1:]
                        if '.' not in method_name:  # Direct child method
                            result[current_path]['methods'].append(method_name)
        except Exception as e:
            # Skip attributes that can't be accessed
            continue
    
    return result

def main():
    print("Creating dummy session to explore SDK structure...")
    
    # Create a dummy session
    dummy_auth = vManageAuth(username="dummy", password="dummy")
    session = ManagerSession(base_url="https://dummy", auth=dummy_auth)
    
    print("\nExploring session.api structure...")
    api_structure = explore_sdk_tree(session.api)
    
    # Filter and organize results
    endpoints = {}
    methods = {}
    
    for path, info in api_structure.items():
        if info['type'] == 'endpoint':
            endpoints[path] = info
        elif info['type'] == 'method':
            methods[path] = info
    
    print(f"\nFound {len(endpoints)} endpoints and {len(methods)} methods")
    
    # Look specifically for alarms
    print("\n=== ALARMS RELATED STRUCTURES ===")
    alarm_items = {k: v for k, v in api_structure.items() if 'alarm' in k.lower()}
    
    for path, info in sorted(alarm_items.items()):
        print(f"\n{path}:")
        print(f"  Type: {info['type']}")
        if info['type'] == 'endpoint' and info.get('methods'):
            print(f"  Methods: {', '.join(info['methods'])}")
        elif info['type'] == 'method':
            print(f"  Signature: {info.get('signature', 'N/A')}")
            print(f"  Doc: {info['doc'][:100]}..." if len(info['doc']) > 100 else f"  Doc: {info['doc']}")
    
    # Show general structure pattern
    print("\n=== TOP-LEVEL ENDPOINTS ===")
    top_level = {k: v for k, v in endpoints.items() if '.' not in k}
    for endpoint in sorted(top_level.keys()):
        print(f"\n{endpoint}:")
        if endpoints[endpoint].get('methods'):
            print(f"  Methods: {', '.join(endpoints[endpoint]['methods'][:5])}")
            if len(endpoints[endpoint]['methods']) > 5:
                print(f"  ... and {len(endpoints[endpoint]['methods']) - 5} more")
    
    # Save full structure to file
    output_file = "tools/sdk_structure_analysis.json"
    with open(output_file, 'w') as f:
        json.dump({
            'endpoints': endpoints,
            'methods': methods,
            'total_endpoints': len(endpoints),
            'total_methods': len(methods)
        }, f, indent=2)
    
    print(f"\nFull structure saved to {output_file}")
    
    # Pattern analysis
    print("\n=== PATTERN ANALYSIS ===")
    print("Common endpoint naming patterns:")
    endpoint_names = [k.split('.')[-1] for k in endpoints.keys() if '.' not in k]
    print(f"  Endpoints: {', '.join(sorted(set(endpoint_names))[:10])}...")
    
    print("\nCommon method naming patterns:")
    method_names = [k.split('.')[-1] for k in methods.keys()]
    method_name_counts = {}
    for name in method_names:
        method_name_counts[name] = method_name_counts.get(name, 0) + 1
    
    print("  Most common method names:")
    for name, count in sorted(method_name_counts.items(), key=lambda x: x[1], reverse=True)[:10]:
        print(f"    {name}: {count} occurrences")

if __name__ == "__main__":
    main()