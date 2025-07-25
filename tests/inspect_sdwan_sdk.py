# inspect_sdk.py
import os
import urllib3
from dotenv import load_dotenv
from catalystwan.session import create_manager_session
from pprint import pprint

# --- Configuration ---
# This script is designed to be run from the root of your project directory.
# It will load the same .env file as your main application.
print("🔎 Loading environment variables from .env file...")
load_dotenv()

# --- Main Inspection Logic ---
def inspect_sdwan_devices():
    """Connects to vManage and inspects the output of the listAllDevices call."""
    session = None
    try:
        # 1. Get Connection Details from Environment
        url = os.getenv('CISCO_SD_WAN_BASE_URL')
        username = os.getenv('CISCO_SD_WAN_USERNAME')
        password = os.getenv('CISCO_SD_WAN_PASSWORD')

        if not all([url, username, password]):
            print("❌ ERROR: Missing CISCO_SD_WAN_BASE_URL, USERNAME, or PASSWORD in your .env file.")
            return

        # Disable SSL warnings, just like in the app
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        print(f"⚡️ Connecting to vManage at {url}...")

        # 2. Create the Session
        session = create_manager_session(url=url, username=username, password=password)
        print("✅ Successfully connected to vManage.")

        # 3. Make the EXACT SDK call that is failing
        # The 'listAllDevices' operationId maps to session.api.devices.get()
        print("🚀 Calling the SDK function: session.api.devices.get()")
        result = session.api.devices.get()
        
        # 4. --- THIS IS THE CRITICAL INSPECTION PART ---
        print("\n" + "="*50)
        print("  SDK RESULT INSPECTION  ")
        print("="*50)

        print(f"\n➡️ Overall Result Type: {type(result)}")

        # Check if the result is iterable (like a list or DataSequence)
        if hasattr(result, '__iter__') and not isinstance(result, (str, bytes, dict)):
            result_list = list(result)
            print(f"➡️ Result is iterable with {len(result_list)} items.")
            
            if not result_list:
                print("⚠️ The result is an empty list.")
                return

            # Get the first item to inspect its structure
            first_item = result_list[0]
            print(f"➡️ Type of the first item: {type(first_item)}")
            
            print("\n" + "-"*50)
            print("  Attributes of the First Item (vars(item))  ")
            print("-"*50)
            # Use pprint for a clean, readable dictionary view of the object's attributes
            pprint(vars(first_item))

            print("\n" + "-"*50)
            print("  Available Methods & Attributes (dir(item))  ")
            print("-"*50)
            # List all attributes and methods, filtering out the standard "dunder" methods
            available_attrs = [attr for attr in dir(first_item) if not attr.startswith('__')]
            pprint(available_attrs)

        else:
            print("\n⚠️ The result is NOT an iterable list of items. Full result:")
            pprint(result)

    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
        import traceback
        traceback.print_exc()
    finally:
        if session:
            print("\n🔌 Logging out of vManage session.")
            session.logout()

if __name__ == "__main__":
    inspect_sdwan_devices()