# tools/validate_sdwan_coverage.py
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
console = Console()
load_dotenv()

ROOT_DIR = Path(__file__).parent.parent
REGISTRY_PATH = ROOT_DIR / "src" / "app" / "llm" / "sdwan_operation_registry_full.json"
OUTPUT_REPORT_PATH = ROOT_DIR / "tools" / "sdwan_coverage_report.json"

def validate_coverage():
    """
    Connects to vManage and programmatically validates every entry in the
    SD-WAN operation registry to determine SDK coverage.
    """
    session = None
    try:
        # 1. Load the Registry File
        if not REGISTRY_PATH.exists():
            console.print(f"❌ [bold red]ERROR: Registry file not found at:[/bold red] {REGISTRY_PATH}")
            return
        with open(REGISTRY_PATH, 'r') as f:
            registry = json.load(f)
        operations = registry.get("operations", {})
        console.print(f"✅ Loaded {len(operations)} operations from the registry to validate.")

        # 2. Connect to vManage
        url, username, password = (os.getenv(k) for k in ['CISCO_SD_WAN_BASE_URL', 'CISCO_SD_WAN_USERNAME', 'CISCO_SD_WAN_PASSWORD'])
        if not all([url, username, password]):
            console.print("❌ [bold red]ERROR: Missing vManage credentials in .env file.[/bold red]")
            return
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        console.print(f"⚡️ Connecting to vManage at {url}...")
        session = create_manager_session(url=url, username=username, password=password)
        console.print("✅ Successfully connected to vManage.")

        # 3. --- CORE VALIDATION LOOP ---
        console.print("\n🚀 [bold cyan]Starting validation of all registry entries...[/bold cyan]")
        
        results = {
            "valid": [],
            "invalid_mapping": [],
            "not_implemented": []
        }

        for op_name, op_info in operations.items():
            sdk_endpoint_path = op_info.get("sdk_endpoint")
            sdk_method_name = op_info.get("sdk_method")

            # Case 1: Entry is missing the SDK path info. Mark as not implemented.
            if not sdk_endpoint_path or not sdk_method_name:
                results["not_implemented"].append({
                    "operationId": op_name,
                    "reason": "Missing sdk_endpoint or sdk_method in registry."
                })
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
                
                # If we get here, the mapping is valid!
                results["valid"].append(op_name)

            except AttributeError as e:
                # The path or method was wrong. This is an invalid mapping.
                results["invalid_mapping"].append({
                    "operationId": op_name,
                    "sdk_endpoint": sdk_endpoint_path,
                    "sdk_method": sdk_method_name,
                    "reason": str(e)
                })

        # 4. --- REPORT THE RESULTS ---
        console.print("\n" + "="*80)
        console.print("  SDK COVERAGE VALIDATION REPORT  ".center(80))
        console.print("="*80)

        table = Table(box=box.HEAVY_HEAD)
        table.add_column("Status", style="bold")
        table.add_column("Count")
        table.add_column("Description")
        
        table.add_row("✅ Valid", str(len(results["valid"])), "The SDK mapping is correct.", style="green")
        table.add_row("❌ Invalid Mapping", str(len(results["invalid_mapping"])), "The sdk_endpoint or sdk_method is wrong.", style="red")
        table.add_row("⚠️ Not Implemented", str(len(results["not_implemented"])), "The mapping is missing or the function likely has no high-level SDK method.", style="yellow")
        
        console.print(table)
        
        # 5. Save the detailed report to a JSON file
        with open(OUTPUT_REPORT_PATH, 'w') as f:
            json.dump(results, f, indent=2)
        
        console.print(f"\n💾 [bold]Detailed report saved to:[/bold] [cyan]{OUTPUT_REPORT_PATH}[/cyan]")
        console.print("\n[bold]Next Steps:[/bold]")
        console.print(f"1. Open '{OUTPUT_REPORT_PATH.name}' to see the full lists.")
        console.print(f"2. For all functions in 'invalid_mapping' and 'not_implemented', add `\"use_direct_api\": true` to their entry in the main registry file.")
        console.print(f"3. Re-run the scaffolder and re-index the database.")


    except Exception as e:
        console.print(f"\n❌ [bold red]An unexpected error occurred:[/bold red] {e}")
        import traceback
        traceback.print_exc()
    finally:
        if session:
            console.print("\n🔌 Logging out of vManage session.")
            session.logout()

if __name__ == "__main__":
    validate_coverage()