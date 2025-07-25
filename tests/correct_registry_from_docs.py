# correct_registry_from_docs.py
import os
import json
import re
from pathlib import Path
from dotenv import load_dotenv
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
# IMPORTANT: Save the documentation you provided into this file
SDK_DOCS_PATH = Path(__file__).parent / "sdk_documentation.md" 

def parse_sdk_docs(filepath: Path) -> dict:
    """Parses the SDK documentation markdown file into a mapping."""
    if not filepath.exists():
        raise FileNotFoundError(f"SDK documentation file not found at: {filepath}")

    content = filepath.read_text()
    # Regex to capture the API path and the SDK method path
    # Example: | POST /admin/resourcegroup | ... | [**AdministrationUserAndGroup.create_resource_group**](...) |
    pattern = re.compile(r"\|\s*(?:POST|GET|PUT|DELETE)\s+([/\w{}?=&]+)\s*\|.*?\|.*?\[\*\*([\w.]+)\*\*\]")
    
    path_to_sdk_map = {}
    for match in pattern.finditer(content):
        api_path = match.group(1).strip()
        sdk_full_path = match.group(2).strip()
        
        # The API path in the docs might have query params, remove them for matching
        api_path_base = api_path.split('?')[0]
        
        path_to_sdk_map[api_path_base] = sdk_full_path
        
    return path_to_sdk_map

def correct_sdwan_registry():
    """
    Programmatically corrects the SD-WAN operation registry using the
    authoritative SDK documentation markdown file.
    """
    try:
        # 1. Parse the SDK documentation to create our "answer key"
        console.print(f"📖 Parsing SDK documentation from: [cyan]{SDK_DOCS_PATH.name}[/cyan]")
        sdk_map = parse_sdk_docs(SDK_DOCS_PATH)
        console.print(f"✅ Created a map of {len(sdk_map)} API paths to SDK methods.")

        # 2. Load the broken registry
        console.print(f"📖 Loading broken registry from: [cyan]{INPUT_REGISTRY_PATH.name}[/cyan]")
        with open(INPUT_REGISTRY_PATH, 'r') as f:
            registry = json.load(f)
        operations = registry.get("operations", {})
        console.print(f"✅ Found {len(operations)} operations to process.")

        # 3. --- CORE CORRECTION LOGIC ---
        corrected_operations = {}
        fixed_count = 0
        unfixable_count = 0

        for op_name, op_info in operations.items():
            api_path = op_info.get("path")
            new_op_info = op_info.copy()

            if api_path and api_path in sdk_map:
                sdk_full_path = sdk_map[api_path]
                
                # The SDK path is like 'ClassName.method_name'
                # We need to find the endpoint object name, which is usually a snake_case
                # version of the class name, minus 'Configuration'.
                parts = sdk_full_path.split('.')
                class_name = parts[0]
                sdk_method = parts[1]

                # Convert ClassName to snake_case endpoint name
                # e.g., ConfigurationPolicySiteList -> policy_site_list
                # e.g., MonitoringDeviceDetails -> monitoring_device_details
                endpoint_name = re.sub(r'(?<!^)(?=[A-Z])', '_', class_name).lower()
                endpoint_name = endpoint_name.replace("configuration_", "") # Remove common prefix

                # This is a heuristic, but a good one. We need to map the class
                # to the actual attribute name on `session.api`.
                # Let's create a mapping from our known good endpoints.
                # From your previous script run, we know the available endpoints.
                real_endpoints = ['admin_tech', 'administration_settings', 'alarms', 'cluster_management', 'config_device_inventory_api', 'config_group', 'dashboard', 'device_state', 'devices', 'logs', 'lxcsoftware', 'omp', 'packet_capture', 'partition', 'policy', 'repository', 'resource_groups', 'resource_pool', 'sd_routing_feature_profiles', 'sessions', 'software', 'speedtest', 'templates', 'tenant_backup', 'tenant_management', 'tenant_migration', 'user_groups', 'users']
                
                # Find the real endpoint that matches our generated name
                final_endpoint = None
                for real_ep in real_endpoints:
                    if endpoint_name.endswith(real_ep):
                        final_endpoint = real_ep
                        break
                # A special case for policies, which are nested
                if 'policy' in endpoint_name and not final_endpoint:
                    final_endpoint = 'policy'

                if final_endpoint:
                    new_op_info['sdk_endpoint'] = final_endpoint
                    new_op_info['sdk_method'] = sdk_method
                    corrected_operations[op_name] = new_op_info
                    fixed_count += 1
                else:
                    new_op_info['sdk_endpoint'] = f"!!!_COULD_NOT_MAP_{endpoint_name}_!!!"
                    unfixable_count += 1
            else:
                new_op_info['sdk_endpoint'] = "!!!_API_PATH_NOT_IN_DOCS_!!!"
                unfixable_count += 1
        
        # 4. Save the new, corrected registry file
        new_registry_data = {"operations": corrected_operations}
        with open(OUTPUT_REGISTRY_PATH, 'w') as f:
            json.dump(new_registry_data, f, indent=2)

        console.print("\n" + "="*80)
        console.print("  CORRECTION REPORT V2  ".center(80))
        console.print("="*80)
        console.print(f"✅ [bold green]Automatically corrected {fixed_count} entries.[/bold green]")
        console.print(f"⚠️ [bold yellow]Could not determine endpoint for {unfixable_count} entries.[/bold yellow]")
        console.print(f"💾 New, corrected registry saved to: [cyan]{OUTPUT_REGISTRY_PATH.name}[/cyan]")
        console.print("\n[bold]Next Steps:[/bold]")
        console.print(f"1. Rename '{OUTPUT_REGISTRY_PATH.name}' to '{INPUT_REGISTRY_PATH.name}'.")
        console.print("2. Manually review any entries marked with '!!!'.")
        console.print("3. Restart your FastAPI application.")

    except Exception as e:
        console.print(f"\n❌ An unexpected error occurred: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    correct_sdwan_registry()