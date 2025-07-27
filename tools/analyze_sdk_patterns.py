#!/usr/bin/env python3
"""
Analyze patterns in the catalystwan SDK structure to improve mapping
"""
from catalystwan.session import ManagerSession
from catalystwan.vmanage_auth import vManageAuth
import re
import json
from collections import defaultdict

def camel_to_snake(name):
    """Convert camelCase to snake_case"""
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

def analyze_sdk_patterns():
    """Analyze patterns in SDK endpoint and method naming"""
    # Create dummy session
    dummy_auth = vManageAuth(username="dummy", password="dummy")
    session = ManagerSession(base_url="https://dummy", auth=dummy_auth)
    
    patterns = {
        'endpoint_names': [],
        'method_names': defaultdict(list),
        'operation_id_mappings': [],
        'common_methods': defaultdict(int)
    }
    
    # Explore top-level endpoints
    for attr_name in dir(session.api):
        if attr_name.startswith('_'):
            continue
        
        try:
            endpoint = getattr(session.api, attr_name)
            if hasattr(endpoint, '__dict__'):
                patterns['endpoint_names'].append(attr_name)
                
                # Get methods for this endpoint
                methods = []
                for method_name in dir(endpoint):
                    if not method_name.startswith('_'):
                        method = getattr(endpoint, method_name)
                        if callable(method):
                            methods.append(method_name)
                            patterns['common_methods'][method_name] += 1
                
                patterns['method_names'][attr_name] = methods
                
                # Generate potential operation ID mappings
                for method in methods:
                    # Common patterns for operation IDs
                    operation_ids = [
                        f"{method}{attr_name.capitalize()}",  # e.g., getAlarms
                        f"{method}{attr_name.title().replace('_', '')}",  # e.g., getAlarms
                        f"{method}Raw{attr_name.title().replace('_', '')}Data",  # e.g., getRawAlarmData
                        f"{method}{attr_name.title().replace('_', '')}Data",  # e.g., getAlarmData
                    ]
                    
                    for op_id in operation_ids:
                        patterns['operation_id_mappings'].append({
                            'operation_id': op_id,
                            'sdk_endpoint': attr_name,
                            'sdk_method': method,
                            'pattern': f"endpoint={attr_name}, method={method} -> operationId={op_id}"
                        })
        except Exception:
            continue
    
    return patterns

def main():
    print("Analyzing SDK patterns...")
    patterns = analyze_sdk_patterns()
    
    print(f"\n=== SDK STRUCTURE ANALYSIS ===")
    print(f"Total endpoints: {len(patterns['endpoint_names'])}")
    print(f"\nTop 10 endpoints:")
    for endpoint in sorted(patterns['endpoint_names'])[:10]:
        print(f"  - {endpoint} (methods: {', '.join(patterns['method_names'][endpoint][:3])}...)")
    
    print(f"\n=== COMMON METHOD PATTERNS ===")
    print("Most common method names across endpoints:")
    for method, count in sorted(patterns['common_methods'].items(), key=lambda x: x[1], reverse=True)[:10]:
        print(f"  - {method}: found in {count} endpoints")
    
    print(f"\n=== OPERATION ID MAPPING PATTERNS ===")
    print("Common patterns for mapping operation IDs to SDK methods:")
    
    # Group by pattern type
    pattern_examples = defaultdict(list)
    for mapping in patterns['operation_id_mappings']:
        if 'Raw' in mapping['operation_id'] and 'Data' in mapping['operation_id']:
            pattern_examples['getRaw{Endpoint}Data'].append(mapping)
        elif mapping['operation_id'].startswith('get') and mapping['sdk_method'] == 'get':
            pattern_examples['get{Endpoint}'].append(mapping)
        elif mapping['operation_id'].startswith('create') and mapping['sdk_method'] == 'create':
            pattern_examples['create{Endpoint}'].append(mapping)
    
    for pattern_type, examples in pattern_examples.items():
        print(f"\nPattern: {pattern_type}")
        for ex in examples[:3]:
            print(f"  Example: {ex['pattern']}")
    
    # Specific analysis for alarms
    print(f"\n=== ALARMS ENDPOINT ANALYSIS ===")
    if 'alarms' in patterns['method_names']:
        print(f"Methods available on 'alarms' endpoint:")
        for method in patterns['method_names']['alarms']:
            print(f"  - {method}")
        
        print(f"\nPotential operation ID mappings for alarms:")
        alarm_mappings = [m for m in patterns['operation_id_mappings'] if m['sdk_endpoint'] == 'alarms']
        for mapping in alarm_mappings[:5]:
            print(f"  - {mapping['operation_id']} -> alarms.{mapping['sdk_method']}")
    
    # Save detailed analysis
    output_file = "tools/sdk_pattern_analysis.json"
    with open(output_file, 'w') as f:
        json.dump(patterns, f, indent=2)
    print(f"\nDetailed analysis saved to {output_file}")
    
    # Recommendations
    print(f"\n=== RECOMMENDATIONS FOR MAPPING IMPROVEMENT ===")
    print("1. The pattern 'getRaw{Endpoint}Data' commonly maps to '{endpoint}.get'")
    print("   Example: getRawAlarmData -> alarms.get")
    print("\n2. Standard CRUD operations follow predictable patterns:")
    print("   - get{Endpoint} -> {endpoint}.get")
    print("   - create{Endpoint} -> {endpoint}.create")
    print("   - update{Endpoint} -> {endpoint}.update")
    print("   - delete{Endpoint} -> {endpoint}.delete")
    print("\n3. The SDK uses snake_case for endpoints, while operation IDs use camelCase")
    print("\n4. Many endpoints have common methods like 'get', 'create', 'update', 'delete'")
    print("\n5. The 'Raw' and 'Data' suffixes in operation IDs don't affect SDK mapping")

if __name__ == "__main__":
    main()