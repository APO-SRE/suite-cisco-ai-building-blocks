#!/usr/bin/env python3
"""Analyze SDK mapping discrepancies"""

import json
import re
from pathlib import Path
from catalystwan.session import ManagerSession
from catalystwan.vmanage_auth import vManageAuth

def load_sdk_documentation():
    """Load SDK documentation and extract method names"""
    doc_path = Path(__file__).parent.parent / "sdk_documentation.md"
    methods = []
    
    with open(doc_path, 'r') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#'):
                # Extract HTTP method and path
                match = re.match(r'^(GET|POST|PUT|DELETE|PATCH)\s+(.+)$', line)
                if match:
                    methods.append({
                        'http_method': match.group(1),
                        'path': match.group(2)
                    })
    
    return methods

def explore_sdk_endpoints():
    """Explore SDK endpoints in detail"""
    dummy_auth = vManageAuth(username="", password="")
    session = ManagerSession(base_url="dummy_url", auth=dummy_auth)
    
    endpoints = {}
    
    def explore_obj(obj, path=""):
        for attr_name in dir(obj):
            if attr_name.startswith('_'):
                continue
            
            try:
                attr = getattr(obj, attr_name)
                current_path = f"{path}.{attr_name}" if path else attr_name
                
                if callable(attr) and not isinstance(attr, type):
                    # It's a method
                    if path:  # Has a parent endpoint
                        if path not in endpoints:
                            endpoints[path] = []
                        endpoints[path].append(attr_name)
                elif hasattr(attr, '__dict__') and not attr_name.startswith('__'):
                    # It's an endpoint object, explore further
                    explore_obj(attr, current_path)
            except:
                pass
    
    explore_obj(session.api)
    return endpoints

def main():
    print("🔍 Analyzing SDK mapping discrepancies...\n")
    
    # Load SDK documentation
    doc_methods = load_sdk_documentation()
    print(f"📄 Found {len(doc_methods)} methods in sdk_documentation.md")
    
    # Explore actual SDK
    sdk_endpoints = explore_sdk_endpoints()
    total_sdk_methods = sum(len(methods) for methods in sdk_endpoints.values())
    print(f"🔧 Found {total_sdk_methods} methods in actual SDK")
    print(f"📁 Found {len(sdk_endpoints)} endpoint groups\n")
    
    # Show sample endpoints with their methods
    print("📋 Sample SDK endpoints and their methods:")
    for i, (endpoint, methods) in enumerate(sdk_endpoints.items()):
        if i >= 10:  # Show first 10
            break
        print(f"\n  {endpoint}:")
        for method in sorted(methods)[:5]:  # Show first 5 methods
            print(f"    - {method}")
        if len(methods) > 5:
            print(f"    ... and {len(methods) - 5} more")
    
    # Check for alarm-related endpoints
    print("\n\n🚨 Alarm-related endpoints:")
    for endpoint, methods in sdk_endpoints.items():
        if 'alarm' in endpoint.lower():
            print(f"\n  {endpoint}:")
            for method in sorted(methods):
                print(f"    - {method}")
    
    # Save detailed mapping for analysis
    output_path = Path(__file__).parent / "sdk_endpoint_analysis.json"
    with open(output_path, 'w') as f:
        json.dump({
            'endpoints': sdk_endpoints,
            'total_methods': total_sdk_methods,
            'doc_method_count': len(doc_methods)
        }, f, indent=2)
    
    print(f"\n💾 Detailed analysis saved to: {output_path}")

if __name__ == "__main__":
    main()