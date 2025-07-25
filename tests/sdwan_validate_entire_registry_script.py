# validate_registry.py
import os
import json
import urllib3
from pathlib import Path
from dotenv import load_dotenv
from catalystwan.session import create_manager_session
from rich.console import Console
from rich.table import Table
from rich import box

# --- Configuration ---
load_dotenv()
console = Console()

# Define the path to your registry file
# Assumes it's in src/app/llm/ based on our previous discussions
REGISTRY_FILE_PATH = Path(__file__).parent.parent / "src" / "app" / "llm" / "sdwan_operation_registry_full.json"

# --- Main Validation Logic ---
def validate_sdwan_registry():
    """
    Connects to vManage and programmatically validates every entry in the
    SD-WAN operation registry file.
    """
    session = None
    try:
        # 1. Load the Registry File
        if not REGISTRY_FILE_PATH.exists():
            console.print(f"❌ [bold red]ERROR: Registry file not found at:[/bold red] {REGISTRY_FILE_PATH}")
            return
            
        with open(REGISTRY_FILE_PATH, 'r') as f:
            registry = json.load(f)
        
        operations = registry.get("operations", {})
        if not operations:
            console.print("⚠️ Registry file is empty or has no 'operations' key.")
            return
            
        console.print(f"✅ Loaded {len(operations)} operations from the registry.")

        # 2. Connect to vManage to get a live SDK session
        url = os.getenv('CISCO_SD_WAN_BASE_URL')
        username = os.getenv('CISCO_SD_WAN_USERNAME')
        password = os.getenv('CISCO_SD_WAN_PASSWORD')

        if not all([url, username, password]):
            console.print("❌ [bold red]ERROR: Missing vManage credentials in .env file.[/bold red]")
            return

        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        console.print(f"⚡️ Connecting to vManage at {url}...")
        session = create_manager_session(url=url, username=username, password=password)
        console.print("✅ Successfully connected to vManage.")

        # 3. --- THIS IS THE CORE VALIDATION LOOP ---
        console.print("\n🚀 [bold cyan]Starting validation of all registry entries...[/bold cyan]")
        
        valid_entries = []
        invalid_entries = []

        for op_name, op_info in operations.items():
            sdk_endpoint_path = op_info.get("sdk_endpoint")
            sdk_method_name = op_info.get("sdk_method")

            if not sdk_endpoint_path or not sdk_method_name:
                invalid_entries.append((op_name, sdk_endpoint_path, sdk_method_name, "Missing endpoint or method"))
                continue

            try:
                # Navigate the endpoint path
                current_obj = session.api
                for part in sdk_endpoint_path.split('.'):
                    if not hasattr(current_obj, part):
                        raise AttributeError(f"Endpoint part '{part}' not found")
                    current_obj = getattr(current_obj, part)
                
                # Check if the final method exists
                if not hasattr(current_obj, sdk_method_name):
                    raise AttributeError(f"Method '{sdk_method_name}' not found on final endpoint")
                
                # If we get here, it's valid!
                valid_entries.append((op_name, sdk_endpoint_path, sdk_method_name))

            except AttributeError as e:
                invalid_entries.append((op_name, sdk_endpoint_path, sdk_method_name, str(e)))

        # 4. --- REPORT THE RESULTS ---
        console.print("\n" + "="*80)
        console.print("  VALIDATION REPORT  ".center(80))
        console.print("="*80)

        # Print Invalid Entries
        if invalid_entries:
            table = Table(title="❌ Invalid Registry Entries", box=box.HEAVY_HEAD, header_style="bold red")
            table.add_column("Operation ID", style="cyan")
            table.add_column("SDK Endpoint Path")
            table.add_column("SDK Method")
            table.add_column("Error Reason", style="red")
            
            for op_name, path, method, reason in invalid_entries:
                table.add_row(op_name, str(path), str(method), reason)
            
            console.print(table)
        else:
            console.print("\n[bold green]✅ All registry entries appear to be valid![/bold green]")
            
        # Optionally print valid entries
        if console.input("\n[cyan]Show all valid entries? (y/N): [/cyan]").lower() == 'y':
            table = Table(title="✅ Valid Registry Entries", box=box.ROUNDED, header_style="bold green")
            table.add_column("Operation ID", style="cyan")
            table.add_column("SDK Endpoint Path")
            table.add_column("SDK Method")
            
            for op_name, path, method in valid_entries:
                table.add_row(op_name, path, method)
            
            console.print(table)

    except Exception as e:
        console.print(f"\n❌ An unexpected error occurred: {e}")
        import traceback
        traceback.print_exc()
    finally:
        if session:
            console.print("\n🔌 Logging out of vManage session.")
            session.logout()

if __name__ == "__main__":
    validate_sdwan_registry()