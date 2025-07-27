# tools/test_api_call.py (Direct API Tester)
import os
import requests
import json
import urllib3
from dotenv import load_dotenv
from rich.console import Console
from rich.pretty import pprint

# --- Configuration ---
console = Console()
load_dotenv()
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def test_direct_api_calls():
    """
    Connects to vManage using `requests` and directly tests several key API endpoints.
    """
    session = None
    try:
        # 1. Get credentials and authenticate
        base_url = os.getenv('CISCO_SD_WAN_BASE_URL')
        username = os.getenv('CISCO_SD_WAN_USERNAME')
        password = os.getenv('CISCO_SD_WAN_PASSWORD')

        if not all([base_url, username, password]):
            console.print("❌ [bold red]ERROR: Missing vManage credentials.[/bold red]")
            return

        console.print(f"⚡️ Authenticating to vManage at {base_url}...")
        session = requests.Session()
        auth_response = session.post(
            f"{base_url}/j_security_check",
            data={'j_username': username, 'j_password': password},
            verify=False,
            timeout=30
        )
        if "<html>" in auth_response.text:
            console.print("❌ [bold red]Authentication failed.[/bold red]")
            return
        console.print("✅ Authentication Successful.")

        # --- Test #1: List All Devices ---
        console.print("\n" + "="*50)
        console.print("  Testing: List All Devices  ".center(50))
        console.print("="*50)
        test_endpoint(session, base_url, "/dataservice/device")

        # --- Test #2: List All Users ---
        console.print("\n" + "="*50)
        console.print("  Testing: List All Users  ".center(50))
        console.print("="*50)
        test_endpoint(session, base_url, "/dataservice/admin/user")

        # --- Test #3: List All Alarms ---
        console.print("\n" + "="*50)
        console.print("  Testing: List All Alarms  ".center(50))
        console.print("="*50)
        test_endpoint(session, base_url, "/dataservice/alarms")

    except Exception as e:
        console.print(f"\n❌ [bold red]An unexpected error occurred:[/bold red] {e}")
        import traceback
        traceback.print_exc()

def test_endpoint(session, base_url, api_path):
    """Helper function to test a single GET endpoint."""
    try:
        target_url = f"{base_url}{api_path}"
        console.print(f"🚀 Making GET request to: [cyan]{target_url}[/cyan]")
        response = session.get(target_url, verify=False, timeout=30)
        response.raise_for_status()
        
        data = response.json()
        data_list = data.get('data', [])
        
        console.print(f"✅ [bold green]SUCCESS! Status: {response.status_code}[/bold green]")
        console.print(f"➡️  Found [bold green]{len(data_list)}[/bold green] items in the 'data' key.")
        
        if data_list:
            console.print("\n--- Data from the first item ---")
            pprint(data_list[0])
        else:
            console.print("✅ API call was successful but returned an empty list.")
            
    except requests.exceptions.HTTPError as e:
        console.print(f"❌ [bold red]HTTP Error:[/bold red] {e.response.status_code} {e.response.reason}")
        console.print(f"   Response Body: {e.response.text[:200]}...")
    except Exception as e:
        console.print(f"❌ [bold red]An error occurred during this test:[/bold red] {e}")


if __name__ == "__main__":
    test_direct_api_calls()