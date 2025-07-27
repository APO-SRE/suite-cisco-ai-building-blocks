# tools/build_final_registry.py
import json
import yaml
import re
import inspect
from pathlib import Path
from types import ModuleType
from typing import Set, Dict
from catalystwan.session import ManagerSession
from catalystwan.vmanage_auth import vManageAuth
from rich.console import Console
from rich.table import Table
from rich import box

# --- Configuration ---
console = Console()
# This script is in `tools/`, so the project root is its parent directory.
ROOT_DIR = Path(__file__).parent.parent 
LLM_DIR = ROOT_DIR / "src" / "app" / "llm"
YAML_SPEC_PATH = ROOT_DIR / "src" / "source_open_api" / "cisco_catalyst_sd_wan_manager_api_2_0_0.yaml"
# This will overwrite your old, broken file with a new, correct one.
OUTPUT_REGISTRY_PATH = LLM_DIR / "sdwan_operation_registry_full.json"

def introspect_sdk() -> Dict[str, str]:
    """
    Inspects the installed catalystwan library using the proven local introspection method
    and builds a map of {snake_case_method_name: full.sdk.endpoint.path}.
    """
    console.print("🔬 [bold]Inspecting local `catalystwan` SDK...[/bold]")
    dummy_auth = vManageAuth(username="", password="")
    session = ManagerSession(base_url="dummy_url", auth=dummy_auth)
    
    sdk_map = {}
    visited_ids = set()

    def _explore(obj, path_prefix=""):
        if id(obj) in visited_ids: return
        visited_ids.add(id(obj))

        for attr_name in dir(obj):
            if attr_name.startswith('_'): continue
            try:
                child_obj = getattr(obj, attr_name)
                current_path = f"{path_prefix}.{attr_name}" if path_prefix else attr_name
                if callable(child_obj):
                    # We map the python method name (snake_case) to its parent's path
                    sdk_map[attr_name] = path_prefix
                elif hasattr(child_obj, '__dict__') and not isinstance(child_obj, ModuleType):
                    _explore(child_obj, current_path)
            except Exception:
                continue
    
    _explore(session.api)
    console.print(f"✅ Discovered [green]{len(sdk_map)}[/green] unique high-level SDK methods.")
    return sdk_map

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

def build_final_registry():
    try:
        sdk_method_map = introspect_sdk()

        console.print(f"📖 Loading authoritative OpenAPI spec from: [cyan]{YAML_SPEC_PATH.name}[/cyan]")
        spec_map = load_openapi_spec(YAML_SPEC_PATH)
        console.print(f"✅ Found {len(spec_map)} total operations in the YAML spec.")

        new_operations = {}
        sdk_covered_count = 0
        direct_api_count = 0
        camel_to_snake = re.compile(r'(?<!^)(?=[A-Z])')

        for op_id, op_details in spec_map.items():
            # Convert operationId (e.g., 'getRawAlarmData') to snake_case ('get_raw_alarm_data')
            sdk_func_name = camel_to_snake.sub('_', op_id).lower()
            
            if sdk_func_name in sdk_method_map:
                # This function IS covered by the SDK.
                sdk_endpoint = sdk_method_map[sdk_func_name]
                new_operations[op_id] = {
                    "path": op_details["path"], "method": op_details["method"],
                    "sdk_endpoint": sdk_endpoint, "sdk_method": sdk_func_name,
                    "description": op_details["description"],
                    "use_direct_api": False
                }
                sdk_covered_count += 1
            else:
                # This function is NOT in the SDK. It MUST use a direct API call.
                new_operations[op_id] = {
                    "path": op_details["path"], "method": op_details["method"],
                    "description": op_details["description"],
                    "use_direct_api": True
                }
                direct_api_count += 1
        
        new_registry_data = {"operations": new_operations}
        with open(OUTPUT_REGISTRY_PATH, 'w') as f:
            json.dump(new_registry_data, f, indent=2)

        console.print("\n" + "="*80)
        console.print("  REGISTRY BUILD AND COVERAGE REPORT  ".center(80))
        console.print("="*80)
        table = Table(box=box.HEAVY_HEAD)
        table.add_column("Coverage Type", style="bold")
        table.add_column("Count")
        table.add_row("✅ High-Level SDK Coverage", str(sdk_covered_count), style="green")
        table.add_row("🔧 Direct API Fallback", str(direct_api_count), style="blue")
        console.print(table)
        
        console.print(f"\n💾 New, complete registry has overwritten the old file at: [cyan]{OUTPUT_REGISTRY_PATH}[/cyan]")
        console.print("\n[bold]This is the definitive solution. The registry is now built from the ground up based on the installed SDK code.[/bold]")
        console.print("\n[bold]CRITICAL NEXT STEPS:[/bold]")
        console.print("1. Re-run your `platform_scaffolder.py` to use this new registry.")
        console.print("2. Re-index your database using `create_platform_index.py`.")
        console.print("3. Restart your FastAPI application and test.")

    except Exception as e:
        console.print(f"\n❌ An unexpected error occurred: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    build_final_registry()