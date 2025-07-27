# tools/build_new_registry.py (Final Version)
import json
import yaml
import re
from pathlib import Path
from rich.console import Console
from rich.table import Table
from rich import box

# --- Configuration ---
console = Console()

# The script is in `tools/`, so the project root is its parent directory.
ROOT_DIR = Path(__file__).parent.parent 

# Correctly define paths relative to the project root.
YAML_SPEC_PATH = ROOT_DIR / "src" / "source_open_api" / "cisco_catalyst_sd_wan_manager_api_2_0_0.yaml"
OUTPUT_REGISTRY_PATH = ROOT_DIR / "src" / "app" / "llm" / "sdwan_operation_registry_full.json"

# This is the "brain" that maps a ClassName to the simple session.api attribute.
ENDPOINT_HEURISTICS = {
    'templates': ['template'], 'policy': ['policy'], 'devices': ['device'],
    'alarms': ['alarm'], 'users': ['user', 'administrationuserandgroup'], 'sites': ['site'],
    'segments': ['segment', 'vpn', 'vrf'], 'dashboard': ['dashboard', 'health', 'status'],
    'software': ['software', 'image', 'upgrade'], 'logs': ['log'],
    'real_time': ['real_time', 'monitoring', 'statistics'], 'cluster_management': ['cluster'],
    'config_group': ['config_group'], 'omp': ['omp'], 'sessions': ['session'],
    'tenant_management': ['tenant'], 'client': ['client'], 'resource_groups': ['resource_group'],
    'repository': ['repository'], 'partition': ['partition'], 'packet_capture': ['packet_capture'],
    'lxcsoftware': ['lxc'], 'sd_routing_feature_profiles': ['sd_routing'],
    'tenant_backup': ['tenant_backup'], 'tenant_migration': ['tenant_migration'],
    'user_groups': ['user_group'], 'config_device_inventory_api': ['config_device_inventory'],
}

def load_and_parse_spec(filepath: Path) -> dict:
    """Loads the YAML OpenAPI spec and creates a map from operationId to its details."""
    if not filepath.exists():
        raise FileNotFoundError(f"Authoritative OpenAPI spec file not found at: {filepath}")
    
    with open(filepath, 'r') as f:
        spec = yaml.safe_load(f)
    
    op_id_map = {}
    sdk_operations = spec.get('x-sdk-operations', {})
    
    if sdk_operations:
        console.print("✅ Found 'x-sdk-operations' extension in YAML. Using it as the primary source.")
        for op_id, sdk_info in sdk_operations.items():
            found = False
            for path, path_item in spec.get("paths", {}).items():
                for method, op_details in path_item.items():
                    if op_details.get('operationId') == op_id:
                        op_id_map[op_id] = {
                            "path": path, "method": method.lower(),
                            "description": op_details.get('summary') or op_details.get('description', ''),
                            "sdk_class": sdk_info.get('className'), "sdk_func_name": sdk_info.get('methodName')
                        }
                        found = True
                        break
                if found:
                    break
    else:
        console.print("⚠️ 'x-sdk-operations' not found. This is unexpected. Please check the YAML file.")
        # We will stop here as we cannot reliably build the registry without this mapping.
        return {}
        
    return op_id_map

def find_best_endpoint(class_name: str) -> str | None:
    """Finds the most likely SDK endpoint attribute based on the class name."""
    if not class_name: return None
    class_lower = class_name.lower()
    for endpoint, keywords in ENDPOINT_HEURISTICS.items():
        if any(keyword in class_lower for keyword in keywords):
            return endpoint
    return None

def build_new_registry():
    try:
        console.print(f"📖 Loading authoritative OpenAPI spec from: [cyan]{YAML_SPEC_PATH}[/cyan]")
        spec_map = load_and_parse_spec(YAML_SPEC_PATH)
        if not spec_map:
            console.print("[bold red]Could not build map from YAML spec. Aborting.[/bold red]")
            return
        console.print(f"✅ Parsed {len(spec_map)} real, documented operations from the YAML spec.")

        # --- CORE BUILD LOGIC ---
        new_operations = {}
        successful_mappings = 0
        failed_mappings = []

        for op_id, op_details in spec_map.items():
            sdk_class = op_details.get('sdk_class')
            sdk_func = op_details.get('sdk_func_name')
            
            if sdk_class and sdk_func:
                endpoint = find_best_endpoint(sdk_class)
                
                if endpoint:
                    new_operations[op_id] = {
                        "path": op_details["path"], "method": op_details["method"],
                        "sdk_endpoint": endpoint, "sdk_method": sdk_func,
                        "description": op_details["description"]
                    }
                    successful_mappings += 1
                else:
                    failed_mappings.append(f"Could not map Class '{sdk_class}' to an endpoint for OpID '{op_id}'")
            else:
                failed_mappings.append(f"Missing SDK info for OpID '{op_id}' in x-sdk-operations")

        # Save the new, correct registry file, overwriting the old one
        new_registry_data = {"operations": new_operations}
        with open(OUTPUT_REGISTRY_PATH, 'w') as f:
            json.dump(new_registry_data, f, indent=2)

        console.print("\n" + "="*80)
        console.print("  REGISTRY BUILD REPORT  ".center(80))
        console.print("="*80)
        console.print(f"✅ [bold green]Successfully built a new registry with {successful_mappings} valid entries.[/bold green]")
        if failed_mappings:
            console.print(f"⚠️ [bold yellow]Could not map {len(failed_mappings)} entries. These will be excluded.[/bold yellow]")
        
        console.print(f"💾 New, correct registry has overwritten the old file at: [cyan]{OUTPUT_REGISTRY_PATH}[/cyan]")
        console.print("\n[bold]Next Steps:[/bold]")
        console.print("1. Re-run your `platform_scaffolder.py --platform sdwan_mngr ...`")
        console.print("2. Re-index your database using `create_platform_index.py` (and choose to Recreate).")
        console.print("3. Restart your FastAPI application and test.")

    except Exception as e:
        console.print(f"\n❌ An unexpected error occurred: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    build_new_registry()