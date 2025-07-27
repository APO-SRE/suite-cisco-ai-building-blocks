# SD-WAN (catalystwan) SDK Authentication Documentation

## Overview

The catalystwan SDK handles authentication for REST API calls using a session-based authentication mechanism with JSESSIONID cookies and XSRF tokens.

## Authentication Flow

1. **Session Creation**: When you create a session using `create_manager_session()`, the SDK:
   - Makes a POST request to `/j_security_check` with username/password
   - Receives a JSESSIONID cookie in the response
   - Makes a GET request to `/dataservice/client/token` to get an XSRF token
   - Stores both in the session's auth object

2. **Request Authentication**: For each API request, the SDK:
   - Adds the JSESSIONID cookie to the `Cookie` header
   - Adds the XSRF token to the `x-xsrf-token` header
   - These headers are automatically injected by the auth handler

## Key Components

### ManagerSession Class
- Extends `requests.Session` with SD-WAN specific functionality
- Contains an `auth` property that holds the authentication handler
- The actual auth object is stored in `_auth` (private attribute)

### vManageAuth Class
- Implements the authentication logic
- Stores:
  - `jsessionid`: The session cookie value
  - `xsrftoken`: The XSRF token for CSRF protection
  - `cookies`: RequestsCookieJar containing the session cookie
- Handles automatic re-authentication if session expires

## Accessing Authentication Details

```python
from catalystwan.session import create_manager_session

# Create session
session = create_manager_session(
    url="https://your-vmanage.com",
    username="admin",
    password="password"
)

# Access authentication details
auth = session._auth  # or session.auth

# Get JSESSIONID
jsessionid = auth.jsessionid

# Get XSRF token
xsrf_token = auth.xsrftoken

# Get cookies
cookies = auth.cookies
```

## Making REST API Calls with Authentication

To make direct REST API calls outside the SDK while using the same authentication:

```python
import requests

# Get authentication headers from session
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "User-Agent": "catalystwan/0.40.2",
    "Cookie": f"JSESSIONID={session._auth.jsessionid}",
    "x-xsrf-token": session._auth.xsrftoken
}

# Make REST API call
response = requests.get(
    f"{session.base_url}/dataservice/your/endpoint",
    headers=headers,
    verify=False  # For self-signed certificates
)
```

## Implementation in sdwan_mngr_client.py

The client extracts authentication headers in the `_get_auth_headers()` method:

```python
def _get_auth_headers(self) -> dict:
    """Get authentication headers from the session for REST API calls."""
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "User-Agent": "catalystwan/0.40.2"
    }
    
    # Get authentication from session._auth
    if hasattr(self._session, '_auth'):
        auth = self._session._auth
        
        # Add JSESSIONID cookie
        if hasattr(auth, 'jsessionid') and auth.jsessionid:
            headers["Cookie"] = f"JSESSIONID={auth.jsessionid}"
        
        # Add XSRF token
        if hasattr(auth, 'xsrftoken') and auth.xsrftoken:
            headers["x-xsrf-token"] = auth.xsrftoken
    
    return headers
```

## Important Notes

1. **Session Persistence**: The JSESSIONID and XSRF token remain valid for the session duration
2. **Automatic Re-authentication**: The SDK handles expired sessions automatically
3. **Thread Safety**: The vManageAuth class uses locks for thread-safe authentication
4. **SSL Verification**: Production environments should use `verify=True` for SSL certificate validation

## Testing Authentication

Use the provided test scripts to verify authentication:
- `test_session_auth.py`: Explores session authentication details
- `test_rest_api_auth.py`: Tests making REST API calls with extracted headers