#!/usr/bin/env python3
"""
Debug script for SD-WAN alarms API
This script explores the SD-WAN alarms API to understand:
1. Available alarm endpoints
2. Different methods to fetch alarms
3. Structure of returned data
"""

import os
import json
import urllib3
from catalystwan.session import create_manager_session
from datetime import datetime, timedelta
import traceback

# Disable SSL warnings for SD-WAN sandbox
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def print_section(title):
    """Print a section header"""
    print(f"\n{'='*80}")
    print(f"{title}")
    print('='*80)

def create_session():
    """Create SD-WAN session using environment variables"""
    print_section("Creating SD-WAN Session")
    
    url = os.getenv('CISCO_SD_WAN_BASE_URL')
    username = os.getenv('CISCO_SD_WAN_USERNAME')
    password = os.getenv('CISCO_SD_WAN_PASSWORD')
    
    if not all([url, username, password]):
        raise ValueError(
            'SD-WAN Manager requires url, username, and password. '
            'Set via environment variables: '
            'CISCO_SD_WAN_BASE_URL, CISCO_SD_WAN_USERNAME, CISCO_SD_WAN_PASSWORD'
        )
    
    print(f"URL: {url}")
    print(f"Username: {username}")
    print(f"Password: {'*' * len(password)}")
    
    session = create_manager_session(
        url=url,
        username=username,
        password=password
    )
    
    print("✓ Session created successfully!")
    return session

def explore_alarm_endpoints(session):
    """Explore available alarm-related endpoints"""
    print_section("Exploring Alarm-Related Endpoints")
    
    api = session.api
    
    # List all API endpoints and find alarm-related ones
    alarm_endpoints = []
    for attr_name in dir(api):
        if not attr_name.startswith('_'):
            # Check for alarm-related endpoints
            if 'alarm' in attr_name.lower() or 'alert' in attr_name.lower() or 'event' in attr_name.lower():
                attr = getattr(api, attr_name)
                if attr is not None:
                    alarm_endpoints.append((attr_name, attr))
                    print(f"Found: api.{attr_name} - {type(attr).__name__}")
    
    # Also check for monitoring endpoints that might have alarms
    monitoring_endpoints = ['monitoring', 'monitor', 'real_time_monitoring']
    for endpoint_name in monitoring_endpoints:
        if hasattr(api, endpoint_name):
            endpoint = getattr(api, endpoint_name)
            print(f"\nChecking api.{endpoint_name} for alarm methods:")
            for method_name in dir(endpoint):
                if not method_name.startswith('_') and ('alarm' in method_name.lower() or 'alert' in method_name.lower()):
                    print(f"  - {method_name}")
    
    return alarm_endpoints

def explore_endpoint_methods(api, endpoint_name):
    """Explore methods available on an endpoint"""
    print(f"\nMethods on api.{endpoint_name}:")
    
    if not hasattr(api, endpoint_name):
        print(f"  ✗ Endpoint not found")
        return
    
    endpoint = getattr(api, endpoint_name)
    methods = []
    
    for method_name in dir(endpoint):
        if not method_name.startswith('_'):
            method = getattr(endpoint, method_name)
            if callable(method):
                methods.append(method_name)
                # Try to get method signature
                try:
                    import inspect
                    sig = inspect.signature(method)
                    params = list(sig.parameters.keys())
                    print(f"  - {method_name}({', '.join(params)})")
                except:
                    print(f"  - {method_name}(...)")
    
    return methods

def try_alarm_methods(session):
    """Try different methods to fetch alarms"""
    print_section("Trying Different Alarm Fetch Methods")
    
    api = session.api
    results = {}
    
    # Method 1: Direct alarms endpoint
    try:
        print("\n1. Trying api.alarms (if exists)...")
        if hasattr(api, 'alarms'):
            alarms_endpoint = api.alarms
            
            # Try different methods
            if hasattr(alarms_endpoint, 'get'):
                print("   - Trying alarms.get()...")
                result = alarms_endpoint.get()
                results['alarms.get'] = process_result(result)
            
            if hasattr(alarms_endpoint, 'get_alarms'):
                print("   - Trying alarms.get_alarms()...")
                result = alarms_endpoint.get_alarms()
                results['alarms.get_alarms'] = process_result(result)
            
            if hasattr(alarms_endpoint, 'list'):
                print("   - Trying alarms.list()...")
                result = alarms_endpoint.list()
                results['alarms.list'] = process_result(result)
        else:
            print("   ✗ api.alarms not found")
    except Exception as e:
        print(f"   ✗ Error: {str(e)}")
        traceback.print_exc()
    
    # Method 2: Try monitoring endpoints
    try:
        print("\n2. Trying monitoring endpoints...")
        monitoring_names = ['monitoring', 'monitor', 'real_time_monitoring']
        
        for mon_name in monitoring_names:
            if hasattr(api, mon_name):
                mon_endpoint = getattr(api, mon_name)
                print(f"   - Found api.{mon_name}")
                
                # Look for alarm-related methods
                for method_name in ['alarms', 'get_alarms', 'alerts', 'get_alerts']:
                    if hasattr(mon_endpoint, method_name):
                        print(f"     - Trying {mon_name}.{method_name}()...")
                        method = getattr(mon_endpoint, method_name)
                        result = method()
                        results[f'{mon_name}.{method_name}'] = process_result(result)
    except Exception as e:
        print(f"   ✗ Error: {str(e)}")
        traceback.print_exc()
    
    # Method 3: Try event endpoints
    try:
        print("\n3. Trying event endpoints...")
        if hasattr(api, 'event'):
            event_endpoint = api.event
            print("   - Found api.event")
            
            methods_to_try = ['get', 'get_events', 'list']
            for method_name in methods_to_try:
                if hasattr(event_endpoint, method_name):
                    print(f"     - Trying event.{method_name}()...")
                    method = getattr(event_endpoint, method_name)
                    result = method()
                    results[f'event.{method_name}'] = process_result(result)
    except Exception as e:
        print(f"   ✗ Error: {str(e)}")
        traceback.print_exc()
    
    # Method 4: Try direct REST API calls
    try:
        print("\n4. Trying direct REST API calls...")
        # Common alarm endpoints in SD-WAN
        endpoints_to_try = [
            '/dataservice/alarms',
            '/dataservice/alarms/count',
            '/dataservice/alarm/alarms',
            '/dataservice/event',
            '/dataservice/statistics/alarm',
            '/api/alarms',
            '/api/v1/alarms'
        ]
        
        for endpoint in endpoints_to_try:
            try:
                print(f"   - Trying GET {endpoint}...")
                response = session.get(endpoint)
                if response.status_code == 200:
                    data = response.json()
                    results[f'GET {endpoint}'] = {
                        'success': True,
                        'count': len(data) if isinstance(data, list) else 1,
                        'sample': data[:2] if isinstance(data, list) else data
                    }
                    print(f"     ✓ Success! Got {len(data) if isinstance(data, list) else 'data'}")
                else:
                    print(f"     ✗ Status {response.status_code}")
            except Exception as e:
                print(f"     ✗ Error: {str(e)}")
    except Exception as e:
        print(f"   ✗ Error in REST calls: {str(e)}")
    
    return results

def process_result(result):
    """Process and summarize the result from an API call"""
    try:
        if result is None:
            return {'success': False, 'data': None}
        
        # Handle different result types
        if hasattr(result, 'json'):
            data = result.json()
        elif hasattr(result, 'to_dict'):
            data = result.to_dict()
        elif hasattr(result, '__iter__') and not isinstance(result, (str, bytes)):
            # Handle iterables (like DataSequence)
            items = list(result)
            if items and hasattr(items[0], 'to_dict'):
                data = [item.to_dict() for item in items]
            elif items and hasattr(items[0], '__dict__'):
                data = [dict(item.__dict__) for item in items]
            else:
                data = items
        else:
            data = result
        
        # Summarize the data
        summary = {
            'success': True,
            'type': type(data).__name__,
            'count': len(data) if isinstance(data, (list, tuple)) else 1
        }
        
        # Add sample data
        if isinstance(data, list):
            summary['sample'] = data[:2] if data else []
        elif isinstance(data, dict):
            summary['keys'] = list(data.keys())
            summary['sample'] = data
        else:
            summary['sample'] = str(data)[:200]
        
        return summary
    except Exception as e:
        return {'success': False, 'error': str(e)}

def print_results(results):
    """Print the results in a formatted way"""
    print_section("Results Summary")
    
    successful_methods = []
    failed_methods = []
    
    for method, result in results.items():
        if result.get('success'):
            successful_methods.append((method, result))
        else:
            failed_methods.append((method, result))
    
    if successful_methods:
        print("\n✓ Successful methods:")
        for method, result in successful_methods:
            print(f"\n  {method}:")
            print(f"    - Type: {result.get('type')}")
            print(f"    - Count: {result.get('count')}")
            if 'keys' in result:
                print(f"    - Keys: {result['keys']}")
            if 'sample' in result:
                print(f"    - Sample data:")
                print(json.dumps(result['sample'], indent=6, default=str)[:500])
    
    if failed_methods:
        print("\n✗ Failed methods:")
        for method, result in failed_methods:
            print(f"  {method}: {result.get('error', 'Unknown error')}")

def main():
    """Main function"""
    try:
        # Create session
        session = create_session()
        
        # Explore alarm endpoints
        alarm_endpoints = explore_alarm_endpoints(session)
        
        # Explore specific endpoints
        endpoints_to_explore = ['alarms', 'event', 'monitoring', 'monitor']
        for endpoint in endpoints_to_explore:
            explore_endpoint_methods(session.api, endpoint)
        
        # Try different methods to fetch alarms
        results = try_alarm_methods(session)
        
        # Print results
        print_results(results)
        
        # Additional exploration: Look at session methods
        print_section("Session-level Methods")
        print("\nDirect session methods for alarms:")
        for method_name in dir(session):
            if not method_name.startswith('_') and ('alarm' in method_name.lower() or 'alert' in method_name.lower()):
                print(f"  - session.{method_name}")
        
    except Exception as e:
        print(f"\n✗ Fatal error: {str(e)}")
        traceback.print_exc()

if __name__ == "__main__":
    main()