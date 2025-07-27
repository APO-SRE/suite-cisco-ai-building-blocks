#!/usr/bin/env python3
"""
Test script to understand how the catalystwan SDK handles authentication
"""
import os
from dotenv import load_dotenv
from catalystwan.session import create_manager_session
import urllib3

# Load environment variables
load_dotenv()

# Disable SSL warnings for testing
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def explore_session_auth():
    """Explore the session authentication mechanisms"""
    
    # Get credentials from environment
    url = os.getenv('CISCO_SD_WAN_BASE_URL')
    username = os.getenv('CISCO_SD_WAN_USERNAME')
    password = os.getenv('CISCO_SD_WAN_PASSWORD')
    
    if not all([url, username, password]):
        print("Error: Missing SD-WAN credentials in environment")
        return
    
    print(f"Creating session to {url}...")
    
    try:
        # Create session
        session = create_manager_session(
            url=url,
            username=username,
            password=password
        )
        
        print("\n=== Session Object ===")
        print(f"Session type: {type(session)}")
        print(f"Session: {session}")
        
        print("\n=== Session Attributes ===")
        # Check for auth attribute
        if hasattr(session, 'auth'):
            print(f"session.auth: {session.auth}")
            print(f"session.auth type: {type(session.auth)}")
        
        if hasattr(session, '_auth'):
            print(f"session._auth: {session._auth}")
            print(f"session._auth type: {type(session._auth)}")
            
            # Check auth attributes
            if hasattr(session._auth, 'xsrftoken'):
                print(f"XSRF Token: {session._auth.xsrftoken}")
            
            if hasattr(session._auth, 'jsessionid'):
                print(f"JSESSIONID: {session._auth.jsessionid}")
            
            if hasattr(session._auth, 'cookies'):
                print(f"Auth cookies: {session._auth.cookies}")
        
        print("\n=== Session Headers ===")
        if hasattr(session, 'headers'):
            print(f"Session headers: {dict(session.headers)}")
        
        print("\n=== Session Cookies ===")
        if hasattr(session, 'cookies'):
            print(f"Session cookies: {session.cookies}")
            for cookie in session.cookies:
                print(f"  {cookie.name}: {cookie.value}")
        
        print("\n=== Making a Test Request ===")
        # Try to make a simple request to see the headers
        response = session.get('/dataservice/client/about')
        print(f"Response status: {response.status_code}")
        
        # Check the request that was sent
        if hasattr(response, 'request'):
            print(f"\nRequest headers: {dict(response.request.headers)}")
        
        print("\n=== Direct Access to Auth Headers ===")
        # Try to prepare a request to see headers
        from requests import Request
        req = Request('GET', f"{session.base_url}/dataservice/test")
        prepared = session.prepare_request(req)
        print(f"Prepared request headers: {dict(prepared.headers)}")
        
        # Close session
        session.close()
        
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    explore_session_auth()