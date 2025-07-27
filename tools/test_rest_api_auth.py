#!/usr/bin/env python3
"""
Test script to verify REST API authentication works correctly
"""
import os
import sys
import json
from dotenv import load_dotenv
import urllib3

# Add parent directory to path to import our modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.app.llm.platform_clients.sdwan_mngr_client import Sdwan_mngrClient

# Load environment variables
load_dotenv()

# Disable SSL warnings for testing
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def test_auth_headers():
    """Test that authentication headers are properly extracted"""
    
    print("=== Testing SD-WAN Authentication Headers ===\n")
    
    try:
        # Create client
        client = Sdwan_mngrClient()
        
        print(f"Session created successfully")
        print(f"Session type: {client._session}")
        print(f"Base URL: {client._base_url}")
        
        print("\n=== Authentication Headers ===")
        headers = client._auth_headers
        for key, value in headers.items():
            if key == "x-xsrf-token":
                print(f"{key}: {value[:20]}... (truncated)")
            elif key == "Cookie":
                print(f"{key}: {value}")
            else:
                print(f"{key}: {value}")
        
        print("\n=== Testing REST API Call ===")
        # Test making a REST API call
        import requests
        
        # Try to get system status
        url = f"{client._base_url}/dataservice/client/about"
        response = requests.get(url, headers=headers, verify=False)
        
        print(f"Request URL: {url}")
        print(f"Response Status: {response.status_code}")
        
        if response.status_code == 200:
            print("✓ Authentication successful!")
            print(f"Response: {json.dumps(response.json(), indent=2)}")
        else:
            print(f"✗ Authentication failed!")
            print(f"Response: {response.text}")
        
        print("\n=== Testing Another Endpoint ===")
        # Try another endpoint
        url2 = f"{client._base_url}/dataservice/system/device/controllers"
        response2 = requests.get(url2, headers=headers, verify=False)
        
        print(f"Request URL: {url2}")
        print(f"Response Status: {response2.status_code}")
        
        if response2.status_code == 200:
            print("✓ Second request successful!")
            data = response2.json()
            if 'data' in data:
                print(f"Found {len(data['data'])} controllers")
        else:
            print(f"Response: {response2.text[:200]}...")
        
        # Close session
        client._session.close()
        
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_auth_headers()