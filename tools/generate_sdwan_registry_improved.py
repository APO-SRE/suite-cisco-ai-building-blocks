# tools/generate_sdwan_registry_improved.py
import json
import yaml
import re
import inspect
from pathlib import Path
from types import ModuleType
from typing import Set, Dict, Tuple, Optional, List
from catalystwan.session import ManagerSession
from catalystwan.vmanage_auth import vManageAuth
from rich.console import Console
from rich.table import Table
from rich import box

console = Console()
ROOT_DIR = Path(__file__).parent.parent 
LLM_DIR = ROOT_DIR / "src" / "app" / "llm"
YAML_SPEC_PATH = ROOT_DIR / "src" / "source_open_api" / "cisco_catalyst_sd_wan_manager_api_2_0_0.yaml"
OUTPUT_REGISTRY_PATH = LLM_DIR / "sdwan_operation_registry_full.json"

def introspect_sdk_improved() -> Dict[str, Tuple[str, str]]:
    """
    Improved SDK introspection that captures full method paths.
    Returns: {full_method_path: (endpoint_path, method_name)}
    Example: {"alarms.get": ("alarms", "get")}
    """
    console.print("🔬 [bold]Inspecting catalystwan SDK with improved method detection...[/bold]")
    dummy_auth = vManageAuth(username="", password="")
    session = ManagerSession(base_url="dummy_url", auth=dummy_auth)
    
    sdk_methods = {}
    visited_ids = set()

    def _explore(obj, path_prefix=""):
        if id(obj) in visited_ids: return
        visited_ids.add(id(obj))

        for attr_name in dir(obj):
            if attr_name.startswith('_'): continue
            try:
                child_obj = getattr(obj, attr_name)
                current_path = f"{path_prefix}.{attr_name}" if path_prefix else attr_name
                
                if callable(child_obj) and not isinstance(child_obj, type):
                    # Store full method path mapping
                    if path_prefix:  # Only store if we have a parent endpoint
                        full_path = f"{path_prefix}.{attr_name}"
                        sdk_methods[full_path] = (path_prefix, attr_name)
                        # Also store just the method name for backward compatibility
                        sdk_methods[attr_name] = (path_prefix, attr_name)
                        
                elif hasattr(child_obj, '__dict__') and not isinstance(child_obj, ModuleType):
                    _explore(child_obj, current_path)
            except Exception:
                continue
    
    _explore(session.api)
    console.print(f"✅ Discovered [green]{len(sdk_methods)}[/green] SDK method mappings.")
    return sdk_methods

def convert_operation_id_to_sdk_pattern(op_id: str) -> List[str]:
    """
    Convert an operationId to possible SDK method patterns.
    Returns a list of patterns to try in order of likelihood.
    """
    patterns = []
    
    # Convert camelCase to snake_case
    snake_case = re.sub(r'(?<!^)(?=[A-Z])', '_', op_id).lower()
    
    # Extract potential endpoint and method from operation ID
    # Common patterns:
    # getRawAlarmData -> alarms.get
    # getAlarmDetails -> alarms.get
    # createAlarmList -> alarms.create
    
    # Pattern 1: Remove common prefixes/suffixes and extract endpoint
    clean_patterns = [
        r'^get_raw_(.+?)_data$',  # getRawXData -> X
        r'^get_(.+?)_data$',       # getXData -> X
        r'^get_(.+?)$',            # getX -> X
        r'^create_(.+?)$',         # createX -> X
        r'^update_(.+?)$',         # updateX -> X
        r'^delete_(.+?)$',         # deleteX -> X
        r'^post_(.+?)$',           # postX -> X
    ]
    
    endpoint = None
    method = None
    
    for pattern in clean_patterns:
        match = re.match(pattern, snake_case)
        if match:
            endpoint_candidate = match.group(1)
            # Determine method based on prefix
            if snake_case.startswith('get_'):
                method = 'get'
            elif snake_case.startswith('create_') or snake_case.startswith('post_'):
                method = 'create'
            elif snake_case.startswith('update_') or snake_case.startswith('put_'):
                method = 'update'
            elif snake_case.startswith('delete_'):
                method = 'delete'
            
            # Handle plural/singular forms
            if endpoint_candidate.endswith('s'):
                patterns.append(f"{endpoint_candidate}.{method}")
                patterns.append(f"{endpoint_candidate[:-1]}.{method}")  # Try singular
            else:
                patterns.append(f"{endpoint_candidate}.{method}")
                patterns.append(f"{endpoint_candidate}s.{method}")  # Try plural
            break
    
    # Pattern 2: Direct snake_case conversion
    patterns.append(snake_case)
    
    # Pattern 3: Try to extract endpoint from operation ID
    # For cases like "getRawAlarmData" -> try "alarm" and "alarms"
    if 'alarm' in snake_case:
        patterns.extend(['alarms.get', 'alarm.get', 'alarms.create', 'alarm.create'])
    
    # Pattern 4: Special cases based on common patterns
    special_mappings = {
        'get_raw_alarm_data': ['alarms.get'],
        'post_raw_alarm_data': ['alarms.create'],
        'get_alarm_details': ['alarms.get'],
        'create_alarm_list': ['alarms.get'],  # Note: Some "create" operations actually use GET
        'get_aggregation_data': ['alarms.get'],
        'post_aggregation_data': ['alarms.create'],
    }
    
    if snake_case in special_mappings:
        patterns = special_mappings[snake_case] + patterns
    
    return patterns

def load_openapi_spec(filepath: Path) -> dict:
    """Loads the YAML OpenAPI spec and creates a map from operationId to its details."""
    if not filepath.exists():
        raise FileNotFoundError(f"OpenAPI spec file not found at: {filepath}")
    with open(filepath, 'r') as f: 
        spec = yaml.safe_load(f)
    
    op_id_map = {}
    for path, path_item in spec.get("paths", {}).items():
        for method, op_details in path_item.items():
            if 'operationId' in op_details:
                op_id = op_details['operationId']
                op_id_map[op_id] = {
                    "path": path, 
                    "method": method.lower(),
                    "description": op_details.get('summary') or op_details.get('description', '')
                }
    return op_id_map

def build_improved_registry():
    try:
        sdk_methods = introspect_sdk_improved()
        
        console.print(f"📖 Loading OpenAPI spec from: [cyan]{YAML_SPEC_PATH.name}[/cyan]")
        spec_map = load_openapi_spec(YAML_SPEC_PATH)
        console.print(f"✅ Found {len(spec_map)} total operations in the YAML spec.")

        new_operations = {}
        sdk_covered_count = 0
        direct_api_count = 0
        pattern_matched_count = 0

        for op_id, op_details in spec_map.items():
            found_sdk_method = False
            
            # Try pattern-based matching first
            patterns = convert_operation_id_to_sdk_pattern(op_id)
            
            for pattern in patterns:
                if pattern in sdk_methods:
                    endpoint, method = sdk_methods[pattern]
                    new_operations[op_id] = {
                        "path": op_details["path"], 
                        "method": op_details["method"],
                        "sdk_endpoint": endpoint, 
                        "sdk_method": method,
                        "description": op_details["description"],
                        "use_direct_api": False
                    }
                    sdk_covered_count += 1
                    pattern_matched_count += 1
                    found_sdk_method = True
                    break
            
            if not found_sdk_method:
                # Fallback: try direct snake_case conversion
                sdk_func_name = re.sub(r'(?<!^)(?=[A-Z])', '_', op_id).lower()
                if sdk_func_name in sdk_methods:
                    endpoint, method = sdk_methods[sdk_func_name]
                    new_operations[op_id] = {
                        "path": op_details["path"], 
                        "method": op_details["method"],
                        "sdk_endpoint": endpoint, 
                        "sdk_method": method,
                        "description": op_details["description"],
                        "use_direct_api": False
                    }
                    sdk_covered_count += 1
                    found_sdk_method = True
            
            if not found_sdk_method:
                # No SDK method found, use direct API
                new_operations[op_id] = {
                    "path": op_details["path"], 
                    "method": op_details["method"],
                    "description": op_details["description"],
                    "use_direct_api": True
                }
                direct_api_count += 1
        
        # Save the registry
        new_registry_data = {"operations": new_operations}
        with open(OUTPUT_REGISTRY_PATH, 'w') as f:
            json.dump(new_registry_data, f, indent=2)

        # Display results
        console.print("\n" + "="*80)
        console.print("  IMPROVED REGISTRY BUILD AND COVERAGE REPORT  ".center(80))
        console.print("="*80)
        
        table = Table(box=box.HEAVY_HEAD)
        table.add_column("Coverage Type", style="bold")
        table.add_column("Count")
        table.add_row("✅ SDK Coverage (Total)", str(sdk_covered_count), style="green")
        table.add_row("  ↳ Pattern Matched", str(pattern_matched_count), style="green")
        table.add_row("  ↳ Direct Match", str(sdk_covered_count - pattern_matched_count), style="green")
        table.add_row("🔧 Direct API Fallback", str(direct_api_count), style="blue")
        table.add_row("📊 Total Operations", str(len(new_operations)), style="yellow")
        console.print(table)
        
        # Show improvement percentage
        improvement_pct = (sdk_covered_count / len(new_operations)) * 100
        console.print(f"\n📈 SDK Coverage: [bold green]{improvement_pct:.1f}%[/bold green]")
        
        console.print(f"\n💾 Registry saved to: [cyan]{OUTPUT_REGISTRY_PATH}[/cyan]")
        
        # Show some examples of pattern matches
        console.print("\n📋 [bold]Sample Pattern Matches:[/bold]")
        examples = []
        for op_id, details in new_operations.items():
            if not details.get("use_direct_api") and "alarm" in op_id.lower():
                examples.append(f"  • {op_id} → {details['sdk_endpoint']}.{details['sdk_method']}")
                if len(examples) >= 5:
                    break
        for ex in examples:
            console.print(ex)

    except Exception as e:
        console.print(f"\n❌ An error occurred: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    build_improved_registry()