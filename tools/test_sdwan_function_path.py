# tools/test_sdwan_path.py
import os
import urllib3
from dotenv import load_dotenv
from catalystwan.session import create_manager_session
from rich.console import Console
from rich.pretty import pprint

# --- Configuration ---
console = Console()
load_dotenv()

# The exact SDK path and method we want to test for listing all segments
SDK_ENDPOINT_TO_TEST = "segment"
SDK_METHOD_TO_TEST = "get"

def test_the_path():
    """
    Connects to vManage and tests a specific SDK endpoint path and method.
    """
    session = None
    try:
        # 1. Get Connection Details from Environment
        url = os.getenv('CISCO_SD_WAN_BASE_URL')
        username = os.getenv('CISCO_SD_WAN_USERNAME')
        password = os.getenv('CISCO_SD_WAN_PASSWORD')
        # SSL verification is often disabled for sandboxes
        verify_ssl_env = os.getenv('CISCO_SD_WAN_VERIFY_SSL', 'false').lower()
        verify = verify_ssl_env in ('true', '1', 'yes')

        if not all([url, username, password]):
            console.print("❌ [bold red]ERROR: Missing vManage credentials in .env file.[/bold red]")
            return

        if not verify:
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            console.print("⚠️ SSL verification is disabled.")

        console.print(f"⚡️ Connecting to vManage at {url}...")
        
        # 2. Create the Session
        session = create_manager_session(
            url=url, 
            username=username, 
            password=password,
            # Note: We are not using timeout or verify kwargs as they are not in your SDK version
        )
        console.print("✅ Successfully connected to vManage.")

        # 3. --- THIS IS THE CRITICAL TEST ---
        console.print("\n" + "="*50)
        console.print(f"  Attempting to access SDK endpoint...  ")
        console.print(f"  Path:  [cyan]session.api.{SDK_ENDPOINT_TO_TEST}[/cyan]")
        console.print(f"  Method: [cyan]{SDK_METHOD_TO_TEST}()[/cyan]")
        print("="*50)

        # Navigate the endpoint path part by part
        current_obj = session.api
        for part in SDK_ENDPOINT_TO_TEST.split('.'):
            console.print(f"Navigating to: [yellow]{part}[/yellow]...")
            if not hasattr(current_obj, part):
                raise AttributeError(f"Failed! The object does not have a '{part}' attribute.")
            current_obj = getattr(current_obj, part)
        
        console.print("\n✅ [bold green]Successfully navigated to the final endpoint object.[/bold green]")
        
        # Check if the final method exists
        if not hasattr(current_obj, SDK_METHOD_TO_TEST):
            raise AttributeError(f"The final endpoint object does not have the method '{SDK_METHOD_TO_TEST}'")
        
        method_to_call = getattr(current_obj, SDK_METHOD_TO_TEST)
        console.print(f"✅ [bold green]Method '{SDK_METHOD_TO_TEST}' found. Calling it now...[/bold green]")

        # Call the method
        result = method_to_call()

        # 4. --- REPORT THE RESULTS ---
        console.print("\n" + "="*50)
        console.print("  SUCCESS! SDK CALL RESULT  ".center(50))
        console.print("="*50)
        
        result_list = list(result)
        console.print(f"➡️  Result Type: {type(result)}")
        console.print(f"➡️  Number of segments returned: {len(result_list)}")
        
        if result_list:
            console.print("\n--- Data from the first segment ---")
            # The result items are objects; we can convert them to dicts to see the data
            first_item_data = result_list[0].to_dict()
            pprint(first_item_data)

    except Exception as e:
        console.print(f"\n❌ [bold red]An error occurred:[/bold red] {e}")
        import traceback
        traceback.print_exc()
    finally:
        if session:
            try:
                console.print("\n🔌 Logging out of vManage session.")
                session.logout()
            except Exception:
                pass

if __name__ == "__main__":
    test_the_path()