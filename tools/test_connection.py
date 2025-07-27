# tools/test_connection.py
import os
import requests
from dotenv import load_dotenv
from rich.console import Console

# --- Configuration ---
console = Console()
load_dotenv()

def test_vmanage_connection():
    """
    Uses the standard `requests` library to test basic network connectivity
    to the vManage instance.
    """
    try:
        # 1. Get Connection Details from Environment
        url = os.getenv('CISCO_SD_WAN_BASE_URL')
        if not url:
            console.print("❌ [bold red]ERROR: CISCO_SD_WAN_BASE_URL not found in .env file.[/bold red]")
            return

        # We will try to reach the main login page or a common API endpoint
        test_url = f"{url}/dataservice/client/server/ready"
        
        console.print(f"⚡️ Attempting to connect to: [cyan]{test_url}[/cyan]")
        console.print("    (This will use a 30-second timeout)")

        # 2. Make the request with a timeout and SSL verification disabled (like the sandbox needs)
        response = requests.get(
            test_url,
            verify=False,  # The sandbox uses a self-signed certificate
            timeout=30     # Force a timeout after 30 seconds
        )

        # 3. --- REPORT THE RESULTS ---
        console.print("\n" + "="*50)
        console.print("  CONNECTION TEST REPORT  ".center(50))
        console.print("="*50)

        # Check if the request was successful (status code 200-299)
        if response.ok:
            console.print(f"✅ [bold green]SUCCESS! Connected to vManage.[/bold green]")
            console.print(f"Status Code: {response.status_code}")
            try:
                # Try to print the JSON response if it exists
                console.print("\n--- Response Data ---")
                console.print(response.json())
            except requests.exceptions.JSONDecodeError:
                console.print("\n--- Response Text (not JSON) ---")
                console.print(response.text[:200] + "...")
        else:
            console.print(f"❌ [bold red]FAILURE! Could not connect to vManage.[/bold red]")
            console.print(f"Status Code: {response.status_code}")
            console.print(f"Reason: {response.reason}")
            console.print("\nThis indicates a network issue (firewall, proxy, VPN) or an incorrect URL.")

    except requests.exceptions.ConnectionTimeout:
        console.print("\n" + "="*50)
        console.print("  CONNECTION TEST REPORT  ".center(50))
        console.print("="*50)
        console.print("❌ [bold red]FAILURE: Connection Timed Out.[/bold red]")
        console.print("\nThe request took longer than 30 seconds to respond.")
        console.print("This strongly suggests a network issue like a firewall blocking the connection.")

    except Exception as e:
        console.print(f"\n❌ [bold red]An unexpected error occurred:[/bold red] {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_vmanage_connection()