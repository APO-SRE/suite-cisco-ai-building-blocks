# correct_registry.py
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

# Define paths for input and output files
LLM_DIR = Path(__file__).parent.parent / "src" / "app" / "llm"
INPUT_REGISTRY_PATH = LLM_DIR / "sdwan_operation_registry_full.json"
OUTPUT_REGISTRY_PATH = LLM_DIR / "sdwan_operation_registry_CORRECTED.json"

# Keywords to map operationId to a likely SDK endpoint
# This is the "brain" of the corrector. More specific keywords are better.
ENDPOINT_KEYWORDS = {
    'templates': ['template', 'parcel'],
    'policy': ['policy', 'policer', 'acl', 'rule'],
    'devices': ['device', 'vedge', 'cedge', 'vbond', 'vsmart'],
    'alarms': ['alarm', 'alert', 'event'],
    'users': ['user', 'aaa', 'group'],
    'sites': ['site'],
    'segments': ['segment', 'vpn', 'vrf'],
    'dashboard': ['dashboard', 'summary', 'health', 'status'],
    'software': ['software', 'image', 'upgrade'],
    'logs': ['log'],
    'real_time': ['real_time', 'monitoring', 'statistics'],
}

def correct_sdwan_registry():
    """
    Programmatically corrects the SD-WAN operation registry by matching
    operationId keywords to actual SDK endpoints.
    """
    session = None
    try:
        # 1. Load the broken registry
        console.print(f"📖 Loading broken registry from: [cyan]{INPUT_REGISTRY_PATH.name}[/cyan]")
        with open(INPUT_REGISTRY_PATH, 'r') as f:
            registry = json.load(f)
        operations = registry.get("operations", {})
        console.print(f"✅ Found {len(operations)} operations to process.")

        # 2. Get the list of REAL SDK endpoints
        console.print("⚡️ Connecting to vManage to get the list of real SDK endpoints...")
        url, username, password = (os.getenv(k) for k in ['CISCO_SD_WAN_BASE_URL', 'CISCO_SD_WAN_USERNAME', 'CISCO_SD_WAN_PASSWORD'])
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        session = create_manager_session(url=url, username=username, password=password)
        real_endpoints = [attr for attr in dir(session.api) if not attr.startswith('_')]
        console.print(f"✅ Found {len(real_endpoints)} real SDK endpoints.", style="bold green")

        # 3. --- CORE CORRECTION LOGIC ---
        corrected_operations = {}
        fixed_count = 0
        unfixable_count = 0

        for op_name, op_info in operations.items():
            op_name_lower = op_name.lower()
            best_match = None
            
            # Find the best endpoint based on keywords
            for endpoint, keywords in ENDPOINT_KEYWORDS.items():
                if endpoint in real_endpoints and any(keyword in op_name_lower for keyword in keywords):
                    best_match = endpoint
                    break # Take the first match based on the order in our keyword map
            
            # Create a new, corrected entry
            new_op_info = op_info.copy()
            if best_match:
                new_op_info['sdk_endpoint'] = best_match
                # Most simple list operations use the 'get' method
                new_op_info['sdk_method'] = 'get' 
                corrected_operations[op_name] = new_op_info
                fixed_count += 1
            else:
                # If we can't guess, mark it for manual review
                new_op_info['sdk_endpoint'] = "!!!_NEEDS_MANUAL_FIX_!!!"
                corrected_operations[op_name] = new_op_info
                unfixable_count += 1
        
        # 4. Save the new, corrected registry file
        new_registry_data = {"operations": corrected_operations}
        with open(OUTPUT_REGISTRY_PATH, 'w') as f:
            json.dump(new_registry_data, f, indent=2)

        console.print("\n" + "="*80)
        console.print("  CORRECTION REPORT  ".center(80))
        console.print("="*80)
        console.print(f"✅ [bold green]Automatically corrected {fixed_count} entries.[/bold green]")
        console.print(f"⚠️ [bold yellow]Could not determine endpoint for {unfixable_count} entries.[/bold yellow]")
        console.print(f"💾 New, corrected registry saved to: [cyan]{OUTPUT_REGISTRY_PATH.name}[/cyan]")
        console.print("\n[bold]Next Steps:[/bold]")
        console.print(f"1. Rename '{OUTPUT_REGISTRY_PATH.name}' to '{INPUT_REGISTRY_PATH.name}'.")
        console.print("2. Manually review any entries marked with '!!!_NEEDS_MANUAL_FIX_!!!'.")
        console.print("3. Restart your FastAPI application.")

    except Exception as e:
        console.print(f"\n❌ An unexpected error occurred: {e}")
        import traceback
        traceback.print_exc()
    finally:
        if session:
            session.logout()

if __name__ == "__main__":
    correct_sdwan_registry()