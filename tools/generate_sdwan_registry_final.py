#!/usr/bin/env python3
"""
Final improved SD-WAN registry generator with better SDK method mapping
"""

import json
import yaml
import re
from pathlib import Path
from typing import Dict, List, Tuple, Set
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

# Enhanced mapping patterns based on analysis
OPERATION_ID_PATTERNS = {
    # Alarm-specific patterns
    r'getRawAlarmData': ('alarms', 'get'),
    r'postRawAlarmData': ('alarms', 'create'),
    r'clearStaleAlarm': ('alarms', 'clear_stale_alarm'),
    r'getNonViewedActiveAlarmsCount': ('alarms', 'get_non_viewed_active_alarms_count'),
    r'markAllAlarmsAsViewed': ('alarms', 'mark_all_as_viewed'),
    r'markAlarmsAsViewed': ('alarms', 'mark_as_viewed'),
    r'getAlarmDetails': ('alarms', 'get'),
    
    # Generic patterns (regex)
    r'^getRaw(.+?)Data$': lambda m: (camel_to_snake(m.group(1)), 'get'),
    r'^postRaw(.+?)Data$': lambda m: (camel_to_snake(m.group(1)), 'create'),
    r'^get(.+?)List$': lambda m: (camel_to_snake(m.group(1)), 'get'),
    r'^create(.+?)$': lambda m: (camel_to_snake(m.group(1)), 'create'),
    r'^update(.+?)$': lambda m: (camel_to_snake(m.group(1)), 'update'),
    r'^delete(.+?)$': lambda m: (camel_to_snake(m.group(1)), 'delete'),
    r'^get(.+?)$': lambda m: (camel_to_snake(m.group(1)), 'get'),
    r'^post(.+?)$': lambda m: (camel_to_snake(m.group(1)), 'create'),
    r'^put(.+?)$': lambda m: (camel_to_snake(m.group(1)), 'update'),
}

# Path-based endpoint mapping
PATH_TO_ENDPOINT_MAP = {
    '/alarms': 'alarms',
    '/admin': 'administration',
    '/certificate': 'certificate',
    '/client': 'client',
    '/device': 'device',
    '/system/device': 'system.device',
    '/template': 'configuration.policy_template',
    '/dataservice': 'monitoring',
}

def camel_to_snake(name: str) -> str:
    """Convert camelCase to snake_case"""
    # Handle special cases
    name = name.replace('OAuth', 'oauth')
    name = name.replace('AAA', 'aaa')
    name = name.replace('API', 'api')
    name = name.replace('URL', 'url')
    name = name.replace('DNS', 'dns')
    name = name.replace('DHCP', 'dhcp')
    
    # Standard conversion
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    result = re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
    
    # Handle pluralization
    if result.endswith('y'):
        result = result[:-1] + 'ies'
    elif not result.endswith('s'):
        result += 's'
    
    return result

def introspect_sdk_full() -> Dict[str, Set[str]]:
    """
    Full SDK introspection capturing all endpoints and their methods
    Returns: {endpoint_path: {method_names}}
    """
    console.print("🔬 [bold]Deep SDK introspection...[/bold]")
    dummy_auth = vManageAuth(username="", password="")
    session = ManagerSession(base_url="dummy_url", auth=dummy_auth)
    
    endpoints = {}
    visited = set()
    
    def explore(obj, path=""):
        obj_id = id(obj)
        if obj_id in visited:
            return
        visited.add(obj_id)
        
        for attr_name in dir(obj):
            if attr_name.startswith('_'):
                continue
                
            try:
                attr = getattr(obj, attr_name)
                current_path = f"{path}.{attr_name}" if path else attr_name
                
                if callable(attr) and not isinstance(attr, type):
                    # It's a method
                    if path:
                        if path not in endpoints:
                            endpoints[path] = set()
                        endpoints[path].add(attr_name)
                elif hasattr(attr, '__dict__'):
                    # Explore nested objects
                    explore(attr, current_path)
            except:
                pass
    
    explore(session.api)
    
    # Also explore session endpoints directly
    for attr_name in ['api', 'endpoints']:
        if hasattr(session, attr_name):
            explore(getattr(session, attr_name), attr_name)
    
    return endpoints

def find_sdk_method(op_id: str, path: str, method: str, sdk_endpoints: Dict[str, Set[str]]) -> Tuple[str, str, bool]:
    """
    Find SDK method for given operation
    Returns: (endpoint, method_name, found)
    """
    # First try direct pattern matching
    for pattern, mapping in OPERATION_ID_PATTERNS.items():
        if callable(mapping):
            match = re.match(pattern, op_id)
            if match:
                endpoint, method_name = mapping(match)
                # Check if this endpoint.method exists in SDK
                if endpoint in sdk_endpoints and method_name in sdk_endpoints[endpoint]:
                    return endpoint, method_name, True
        else:
            if op_id == pattern:
                endpoint, method_name = mapping
                if endpoint in sdk_endpoints and method_name in sdk_endpoints[endpoint]:
                    return endpoint, method_name, True
    
    # Try path-based mapping
    for path_prefix, endpoint in PATH_TO_ENDPOINT_MAP.items():
        if path.startswith(path_prefix):
            # Try common method names
            method_mappings = {
                'get': ['get', 'list', 'get_all'],
                'post': ['create', 'add', 'post'],
                'put': ['update', 'edit', 'put'],
                'delete': ['delete', 'remove'],
            }
            
            for method_name in method_mappings.get(method, []):
                if endpoint in sdk_endpoints and method_name in sdk_endpoints[endpoint]:
                    return endpoint, method_name, True
    
    # Fallback: try snake_case conversion
    snake_op_id = re.sub(r'(?<!^)(?=[A-Z])', '_', op_id).lower()
    
    # Check all endpoints for this method
    for endpoint, methods in sdk_endpoints.items():
        if snake_op_id in methods:
            return endpoint, snake_op_id, True
        # Try without get/post/put/delete prefix
        for prefix in ['get_', 'post_', 'put_', 'delete_', 'create_', 'update_']:
            if snake_op_id.startswith(prefix):
                method_name = snake_op_id[len(prefix):]
                if method_name in methods:
                    return endpoint, method_name, True
    
    return "", "", False

def load_openapi_spec(filepath: Path) -> dict:
    """Load OpenAPI spec"""
    with open(filepath, 'r') as f:
        spec = yaml.safe_load(f)
    
    op_map = {}
    for path, path_item in spec.get("paths", {}).items():
        for method, details in path_item.items():
            if 'operationId' in details:
                op_id = details['operationId']
                op_map[op_id] = {
                    "path": path,
                    "method": method.lower(),
                    "description": details.get('summary', details.get('description', ''))
                }
    
    return op_map

def build_final_registry():
    """Build the final improved registry"""
    try:
        # Get SDK endpoints
        sdk_endpoints = introspect_sdk_full()
        total_sdk_methods = sum(len(methods) for methods in sdk_endpoints.values())
        console.print(f"✅ Found {len(sdk_endpoints)} SDK endpoints with {total_sdk_methods} total methods")
        
        # Load OpenAPI spec
        console.print(f"📖 Loading OpenAPI spec...")
        spec_map = load_openapi_spec(YAML_SPEC_PATH)
        console.print(f"✅ Found {len(spec_map)} operations in spec")
        
        # Build registry
        operations = {}
        sdk_mapped = 0
        direct_api = 0
        
        # Track mapping types
        pattern_mapped = 0
        path_mapped = 0
        fallback_mapped = 0
        
        for op_id, op_details in spec_map.items():
            endpoint, method_name, found = find_sdk_method(
                op_id, op_details["path"], op_details["method"], sdk_endpoints
            )
            
            if found:
                operations[op_id] = {
                    "path": op_details["path"],
                    "method": op_details["method"],
                    "sdk_endpoint": endpoint,
                    "sdk_method": method_name,
                    "description": op_details["description"],
                    "use_direct_api": False
                }
                sdk_mapped += 1
                
                # Track mapping type
                if op_id in [p for p in OPERATION_ID_PATTERNS if isinstance(p, str)]:
                    pattern_mapped += 1
                elif any(op_details["path"].startswith(p) for p in PATH_TO_ENDPOINT_MAP):
                    path_mapped += 1
                else:
                    fallback_mapped += 1
            else:
                operations[op_id] = {
                    "path": op_details["path"],
                    "method": op_details["method"],
                    "description": op_details["description"],
                    "use_direct_api": True
                }
                direct_api += 1
        
        # Save registry
        registry_data = {
            "comment": "Auto-generated SD-WAN Operation Registry - Final Version",
            "operations": operations,
            "stats": {
                "total_operations": len(operations),
                "sdk_mapped": sdk_mapped,
                "direct_api": direct_api,
                "pattern_mapped": pattern_mapped,
                "path_mapped": path_mapped,
                "fallback_mapped": fallback_mapped
            }
        }
        
        with open(OUTPUT_REGISTRY_PATH, 'w') as f:
            json.dump(registry_data, f, indent=2)
        
        # Display results
        console.print("\n" + "="*80)
        console.print("  FINAL REGISTRY BUILD REPORT  ".center(80))
        console.print("="*80)
        
        table = Table(box=box.HEAVY_HEAD)
        table.add_column("Metric", style="bold")
        table.add_column("Count", justify="right")
        table.add_column("Percentage", justify="right")
        
        table.add_row("Total Operations", str(len(operations)), "100.0%")
        table.add_row("✅ SDK Mapped", str(sdk_mapped), f"{(sdk_mapped/len(operations)*100):.1f}%", style="green")
        table.add_row("  ↳ Pattern Match", str(pattern_mapped), f"{(pattern_mapped/len(operations)*100):.1f}%")
        table.add_row("  ↳ Path Match", str(path_mapped), f"{(path_mapped/len(operations)*100):.1f}%")
        table.add_row("  ↳ Fallback Match", str(fallback_mapped), f"{(fallback_mapped/len(operations)*100):.1f}%")
        table.add_row("🔧 Direct API", str(direct_api), f"{(direct_api/len(operations)*100):.1f}%", style="blue")
        
        console.print(table)
        
        # Show alarm examples
        console.print("\n📋 [bold]Alarm-related mappings:[/bold]")
        alarm_ops = [(op_id, details) for op_id, details in operations.items() 
                     if 'alarm' in op_id.lower()][:10]
        
        for op_id, details in alarm_ops:
            if details.get("use_direct_api"):
                console.print(f"  • {op_id} → [red]Direct API[/red]")
            else:
                console.print(f"  • {op_id} → [green]{details['sdk_endpoint']}.{details['sdk_method']}[/green]")
        
        console.print(f"\n💾 Registry saved to: [cyan]{OUTPUT_REGISTRY_PATH}[/cyan]")
        
        # Compare with SDK documentation
        doc_path = ROOT_DIR / "sdk_documentation.md"
        if doc_path.exists():
            with open(doc_path) as f:
                doc_lines = sum(1 for line in f if line.strip() and not line.startswith('#'))
            console.print(f"\n📊 SDK Documentation shows ~{doc_lines} methods")
            console.print(f"📊 We found {total_sdk_methods} actual SDK methods")
            console.print(f"📊 Mapped {sdk_mapped} operations to SDK methods")
        
    except Exception as e:
        console.print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    build_final_registry()