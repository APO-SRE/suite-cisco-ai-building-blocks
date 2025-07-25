# correct_registry_v3.py
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

LLM_DIR = Path(__file__).parent.parent / "src" / "app" / "llm"
INPUT_REGISTRY_PATH = LLM_DIR / "sdwan_operation_registry_full.json"
OUTPUT_REGISTRY_PATH = LLM_DIR / "sdwan_operation_registry_CORRECTED.json"
SDK_DOCS_PATH = Path(__file__).parent / "sdk_documentation.md"

# This is the "brain" that maps a ClassName to the simple session.api attribute.
# We will build this from the real endpoints.
ENDPOINT_HEURISTICS = {
    'admin_tech': ['admin_tech'],
    'administration_settings': ['administration_settings'],
    'alarms': ['alarm'],
    'cluster_management': ['cluster'],
    'config_device_inventory_api': ['config_device_inventory'],
    'config_group': ['config_group'],
    'dashboard': ['dashboard'],
    'device_state': ['device_state'],
    'devices': ['device'],
    'logs': ['log'],
    'lxcsoftware': ['lxc'],
    'omp': ['omp'],
    'packet_capture': ['packet_capture'],
    'partition': ['partition'],
    'policy': ['policy'],
    'repository': ['repository'],
    'resource_groups': ['resource_group'],
    'resource_pool': ['resource_pool'],
    'sd_routing_feature_profiles': ['sd_routing'],
    'sessions': ['session'],
    'software': ['software'],
    'speedtest': ['speedtest'],
    'templates': ['template'],
    'tenant_backup': ['tenant_backup'],
    'tenant_management': ['tenant'],
    'tenant_migration': ['tenant_migration'],
    'user_groups': ['user_group'],
    'users': ['user', 'administrationuserandgroup'], # Map the long class name directly
    'sdavc_cloud_connector': ['sdavc'],
    'server_info': ['server'],
    'misc': ['misc'],
    # Add more mappings as needed by observing class names
}

def parse_sdk_docs_by_function(filepath: Path) -> dict:
    """Parses the SDK docs, mapping function_name -> {class_name, method}."""
    if not filepath.exists():
        raise FileNotFoundError(f"SDK documentation file not found at: {filepath}")

    content = filepath.read_text()
    pattern = re.compile(r"\|\s*(?:POST|GET|PUT|DELETE)\s+.*?\|\s*.*?\|\s*\[\*\*([\w]+)\.([\w]+)\*\*\]")
    
    func_to_class_map = {}
    for match in pattern.finditer(content):
        class_name = match.group(1).strip()
        func_name = match.group(2).strip()
        func_to_class_map[func_name] = class_name
        
    return func_to_class_map

def find_best_endpoint(class_name: str) -> str | None:
    """Finds the most likely SDK endpoint attribute based on the class name."""
    class_lower = class_name.lower()
    for endpoint, keywords in ENDPOINT_HEURISTICS.items():
        if any(keyword in class_lower for keyword in keywords):
            return endpoint
    return None

def correct_sdwan_registry():
    """Corrects the registry using function name matching against SDK docs."""
    try:
        console.print(f"📖 Parsing SDK documentation from: [cyan]{SDK_DOCS_PATH.name}[/cyan]")
        sdk_func_map = parse_sdk_docs_by_function(SDK_DOCS_PATH)
        console.print(f"✅ Created a map of {len(sdk_func_map)} SDK functions to their classes.")

        console.print(f"📖 Loading broken registry from: [cyan]{INPUT_REGISTRY_PATH.name}[/cyan]")
        with open(INPUT_REGISTRY_PATH, 'r') as f:
            registry = json.load(f)
        operations = registry.get("operations", {})
        console.print(f"✅ Found {len(operations)} operations to process.")

        corrected_operations = {}
        fixed_count = 0
        unfixable_count = 0

        # Pre-compile regex for camel to snake conversion
        camel_to_snake_pattern = re.compile(r'(?<!^)(?=[A-Z])')

        for op_id, op_info in operations.items():
            # Convert operationId (e.g., 'listAllDevices') to snake_case ('list_all_devices')
            sdk_func_name = camel_to_snake_pattern.sub('_', op_id).lower()
            
            new_op_info = op_info.copy()

            if sdk_func_name in sdk_func_map:
                class_name = sdk_func_map[sdk_func_name]
                endpoint = find_best_endpoint(class_name)
                
                if endpoint:
                    new_op_info['sdk_endpoint'] = endpoint
                    new_op_info['sdk_method'] = sdk_func_name
                    corrected_operations[op_id] = new_op_info
                    fixed_count += 1
                else:
                    new_op_info['sdk_endpoint'] = f"!!!_NO_ENDPOINT_FOR_CLASS_{class_name}_!!!"
                    unfixable_count += 1
            else:
                new_op_info['sdk_endpoint'] = "!!!_FUNC_NOT_IN_DOCS_!!!"
                unfixable_count += 1
        
        new_registry_data = {"operations": corrected_operations}
        with open(OUTPUT_REGISTRY_PATH, 'w') as f:
            json.dump(new_registry_data, f, indent=2)

        console.print("\n" + "="*80)
        console.print("  CORRECTION REPORT V3  ".center(80))
        console.print("="*80)
        console.print(f"✅ [bold green]Automatically corrected {fixed_count} entries.[/bold green]")
        console.print(f"⚠️ [bold yellow]Could not determine endpoint for {unfixable_count} entries.[/bold yellow]")
        console.print(f"💾 New, corrected registry saved to: [cyan]{OUTPUT_REGISTRY_PATH.name}[/cyan]")

    except Exception as e:
        console.print(f"\n❌ An unexpected error occurred: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    correct_sdwan_registry()