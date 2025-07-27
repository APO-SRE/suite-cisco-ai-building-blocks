# tools/verify_registry_paths.py (Final Builder Version)
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

# Correct, verified paths to the input and output files
YAML_SPEC_PATH = ROOT_DIR / "src" / "source_open_api" / "cisco_catalyst_sd_wan_manager_api_2_0_0.yaml"
SDK_DOCS_PATH = ROOT_DIR / "sdk_documentation.md"
OUTPUT_REGISTRY_PATH = ROOT_DIR / "src" / "app" / "llm" / "sdwan_operation_registry_full.json"

# This is the "brain" that maps a ClassName from the SDK to the simple session.api attribute.
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

def parse_sdk_docs(filepath: Path) -> dict:
    """Parses the SDK docs, mapping API Path + HTTP Method -> SDK info."""
    if not filepath.exists():
        raise FileNotFoundError(f"SDK documentation file not found at: {filepath}")
    content = filepath.read_text()
    pattern = re.compile(r"\|\s*(GET|POST|PUT|DELETE)\s+([/\w{}.-]+?)\s*\|.*?\|.*?\[\*\*([\w]+)\.([\w]+)\*\*\]")
    
    path_map = {}
    for match in pattern.finditer(content):
        http_method, api_path, class_name, func_name = [s.strip() for s in match.groups()]
        api_path_base = api_path.split('?')[0]
        path_map[(api_path_base, http_method.lower())] = {
            "class_name": class_name, "sdk_func_name": func_name
        }
    return path_map

def load_openapi_spec(filepath: Path) -> dict:
    """Loads the YAML OpenAPI spec and creates a map from operationId to its details."""
    if not filepath.exists():
        raise FileNotFoundError(f"Authoritative OpenAPI spec file not found at: {filepath}")
    with open(filepath, 'r') as f: spec = yaml.safe_load(f)
    
    op_id_map = {}
    for path, path_item in spec.get("paths", {}).items():
        for method, op_details in path_item.items():
            if 'operationId' in op_details:
                op_id = op_details['operationId']
                op_id_map[op_id] = {
                    "path": path, "method": method.lower(),
                    "description": op_details.get('summary') or op_details.get('description', '')
                }
    return op_id_map

def find_best_endpoint(class_name: str) -> str | None:
    if not class_name: return None
    class_lower = class_name.lower()
    for endpoint, keywords in ENDPOINT_HEURISTICS.items():
        if any(keyword in class_lower for keyword in keywords):
            return endpoint
    return None

def build_new_registry():
    try:
        console.print(f"📖 Loading authoritative OpenAPI spec from: [cyan]{YAML_SPEC_PATH}[/cyan]")
        spec_map = load_openapi_spec(YAML_SPEC_PATH)
        console.print(f"✅ Found {len(spec_map)} real operations in the YAML spec.")

        console.print(f"📖 Parsing SDK documentation from: [cyan]{SDK_DOCS_PATH}[/cyan]")
        sdk_doc_map = parse_sdk_docs(SDK_DOCS_PATH)
        console.print(f"✅ Created map of {len(sdk_doc_map)} functions from SDK docs.")

        # --- CORE BUILD LOGIC ---
        new_operations = {}
        successful_mappings = 0
        failed_mappings = []
        
        for op_id, op_details in spec_map.items():
            api_path = op_details["path"]
            http_method = op_details["method"]
            
            # Find the corresponding SDK info from our documentation map
            sdk_info = sdk_doc_map.get((api_path, http_method))
            
            if sdk_info:
                endpoint = find_best_endpoint(sdk_info['class_name'])
                
                if endpoint:
                    new_operations[op_id] = {
                        "path": op_details["path"],
                        "method": op_details["method"],
                        "sdk_endpoint": endpoint,
                        "sdk_method": sdk_info['sdk_func_name'],
                        "description": op_details["description"]
                    }
                    successful_mappings += 1
                else:
                    failed_mappings.append(f"Could not map Class '{sdk_info['class_name']}' to an endpoint for OpID '{op_id}'")
            else:
                # This operation from the spec is NOT in the SDK documentation, so we skip it.
                pass

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
        console.print("\n[bold]This is the correct approach. The registry is now built from the ground up based on official documentation.[/bold]")
        console.print("\n[bold]CRITICAL NEXT STEPS:[/bold]")
        console.print("1. Re-run your `platform_scaffolder.py --platform sdwan_mngr ...`")
        console.print("2. Re-index your database using `create_platform_index.py` (and choose to Recreate).")
        console.print("3. Restart your FastAPI application and test.")

    except Exception as e:
        console.print(f"\n❌ An unexpected error occurred: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    build_new_registry()