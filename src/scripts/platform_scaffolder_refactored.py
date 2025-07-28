#!/usr/bin/env python3
"""
Platform Scaffolder - Refactored Version

This script generates LLM-friendly function definitions and client wrappers
for Cisco platform SDKs. It processes OpenAPI specifications and creates:

1. Function definition schemas for LLMs
2. Client wrappers with authentication
3. Unified service interfaces

The refactored version breaks functionality into focused modules for better
maintainability and readability.
"""

import argparse
import json
import logging
import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Set

# Add project root to path
ROOT = Path(__file__).parent.parent.parent
sys.path.insert(0, str(ROOT))

# Import utilities
from app.utils.openapi_loader import load_spec
from app.utils.sdk_loader import load_client
from app.utils.dietify import dietify_schema
from app.utils.sdk_initialization import SDKInitializer
from app.utils.registry_io import load_registry

# Import platform customizations
from platform_customizations import PLATFORM_OVERRIDES, INJECTION_CONFIG, generate_aliases
from platform_customizations.platform_auth import get_platform_auth
from platform_scaffolder_utilities.scaffolder_helpers import (
    write_json, make_python_identifier, emit_org_injection, drop_dynamic_cache
)
from platform_scaffolder_utilities.sdk_processing import (
    perform_sdk_introspection, filter_operations_by_sdk, write_coverage_report
)
from platform_scaffolder_utilities.client_generator import emit_client_stub
from platform_scaffolder_utilities.unified_service_generator import (
    regenerate_unified_service_init, emit_unified_service
)

# Try to import enhanced SDK introspection
try:
    from app.utils.sdk_introspection import (
        SDKIntrospector, SDKOpenAPIFilter, SDKPattern
    )
    ENHANCED_INTROSPECTION = True
except ImportError:
    ENHANCED_INTROSPECTION = False

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger("scaffolder")

# Constants
LLM_DIR = ROOT / "src/app/llm"
OUT_DIRS = {
    "schemas": LLM_DIR / "platform_function_schemas",
    "dynamic": LLM_DIR / "platform_dynamic_cache",
    "client": LLM_DIR / "cisco_clients",
    "cisco": LLM_DIR / "cisco",
}

ALWAYS_KEEP_TAGS = {"devices", "inventory"}
DEFAULT_DYNAMIC_CACHE = LLM_DIR / "platform_dynamic_cache"


class PlatformScaffolder:
    """Main scaffolder class that orchestrates the generation process."""
    
    def __init__(self):
        self.seen_names: Dict[str, Dict[str, int]] = {}
        self.registry = load_registry()
    
    def scaffold_platform(
        self,
        platform: str,
        sdk_module: str,
        spec: dict,
        include_http: Optional[Set[str]] = None,
        name_re: Optional[re.Pattern] = None,
    ) -> None:
        """
        Scaffold a single platform.
        
        Args:
            platform: Platform name (e.g., "meraki", "catalyst")
            sdk_module: SDK module path
            spec: OpenAPI specification dict
            include_http: Set of HTTP methods to include
            name_re: Regex pattern for filtering operation names
        """
        log.info("🚀 Starting scaffold for %s", platform)
        
        # Get platform configuration
        platform_config = PLATFORM_OVERRIDES.get(platform.lower(), {})
        registry_config = self.registry.get(platform.lower(), {})
        
        # Merge configurations (overrides take precedence)
        full_config = {**registry_config, **platform_config}
        
        # Perform SDK introspection if enabled
        introspection_result = None
        if full_config.get("enable_sdk_filtering", False):
            introspection_result = perform_sdk_introspection(
                platform, full_config, ENHANCED_INTROSPECTION
            )
        
        # Process operations
        operations = self._extract_operations(spec, platform, include_http, name_re)
        
        # Apply SDK filtering if introspection succeeded
        if introspection_result:
            operations = filter_operations_by_sdk(
                operations,
                introspection_result['supported_operations'],
                platform
            )
            # Write coverage report
            write_coverage_report(
                platform,
                introspection_result['coverage_report'],
                OUT_DIRS['schemas']
            )
        
        # Apply platform-specific filtering and enhancements
        operations = self._apply_platform_customizations(operations, full_config, platform)
        
        # Generate function schemas
        self._generate_function_schemas(operations, platform, sdk_module)
        
        # Generate client wrapper
        emit_client_stub(platform, sdk_module, OUT_DIRS['client'])
        
        # Generate unified service
        emit_unified_service(platform, OUT_DIRS['cisco'])
        
        log.info("✅ Completed scaffold for %s", platform)
    
    def _extract_operations(
        self,
        spec: dict,
        platform: str,
        include_http: Optional[Set[str]] = None,
        name_re: Optional[re.Pattern] = None
    ) -> List[dict]:
        """Extract operations from OpenAPI spec."""
        operations = []
        
        for path, path_item in spec.get("paths", {}).items():
            if not isinstance(path_item, dict):
                continue
                
            for method, operation in path_item.items():
                if method in ("parameters", "servers", "$ref"):
                    continue
                    
                if include_http and method.upper() not in include_http:
                    continue
                
                if not isinstance(operation, dict):
                    continue
                    
                op_id = operation.get("operationId", "")
                if not op_id:
                    continue
                    
                if name_re and not name_re.search(op_id):
                    continue
                
                # Create operation entry
                op_entry = {
                    "operationId": op_id,
                    "method": method.upper(),
                    "path": path,
                    "summary": operation.get("summary", ""),
                    "description": operation.get("description", ""),
                    "tags": operation.get("tags", []),
                    "parameters": operation.get("parameters", []),
                    "requestBody": operation.get("requestBody"),
                    "responses": operation.get("responses", {}),
                }
                
                operations.append(op_entry)
        
        log.info("Extracted %d operations for %s", len(operations), platform)
        return operations
    
    def _apply_platform_customizations(
        self,
        operations: List[dict],
        platform_config: dict,
        platform: str
    ) -> List[dict]:
        """Apply platform-specific customizations to operations."""
        blocklist = platform_config.get("blocklist", set())
        descriptions = platform_config.get("descriptions", {})
        
        # Filter out blocked operations
        if blocklist:
            original_count = len(operations)
            operations = [op for op in operations if op["operationId"] not in blocklist]
            blocked_count = original_count - len(operations)
            if blocked_count > 0:
                log.info("Blocked %d operations for %s", blocked_count, platform)
        
        # Apply description overrides
        for op in operations:
            op_id = op["operationId"]
            if op_id in descriptions:
                op["description"] = descriptions[op_id]
        
        return operations
    
    def _generate_function_schemas(
        self,
        operations: List[dict],
        platform: str,
        sdk_module: str
    ) -> None:
        """Generate function definition schemas for LLM consumption."""
        if platform not in self.seen_names:
            self.seen_names[platform] = {}
        
        seen = self.seen_names[platform]
        functions = []
        
        # Get injected parameter names for the platform
        injected_keys = INJECTION_CONFIG.get(platform.lower(), {}).get("params", {}).keys()
        
        for op in operations:
            # Create function definition
            func_def = self._create_function_definition(op, platform, seen, injected_keys)
            if func_def:
                functions.append(func_def)
        
        # Write schemas
        schema_file = OUT_DIRS['schemas'] / f"{platform}_functions.json"
        write_json(schema_file, functions, pretty=True)
        
        # Write dynamic cache
        self._write_dynamic_cache(functions, platform)
        
        log.info("Generated %d function schemas for %s", len(functions), platform)
    
    def _create_function_definition(
        self,
        operation: dict,
        platform: str,
        seen: Dict[str, int],
        injected_keys: Set[str]
    ) -> Optional[dict]:
        """Create a function definition from an operation."""
        op_id = operation["operationId"]
        safe_name = make_python_identifier(op_id, seen)
        
        # Build parameter schema
        properties = {}
        required = []
        non_body_params = []
        
        # Process parameters
        for param in operation.get("parameters", []):
            if isinstance(param, dict) and "$ref" not in param:
                param_name = param.get("name")
                if param_name and param_name not in injected_keys:
                    # Add to schema
                    param_schema = param.get("schema", {"type": "string"})
                    properties[param_name] = {
                        "type": param_schema.get("type", "string"),
                        "description": param.get("description", ""),
                    }
                    if param.get("required"):
                        required.append(param_name)
                    non_body_params.append(param_name)
        
        # Process request body
        if operation.get("requestBody"):
            properties["body"] = {
                "type": "object",
                "description": "Request body",
            }
            if operation["requestBody"].get("required"):
                required.append("body")
        
        # Create function schema
        func_schema = {
            "type": "function",
            "function": {
                "name": safe_name,
                "description": operation.get("description") or operation.get("summary", ""),
                "parameters": {
                    "type": "object",
                    "properties": properties,
                    "required": required,
                },
            },
            "metadata": {
                "platform": platform,
                "operationId": op_id,
                "method": operation["method"],
                "path": operation["path"],
                "tags": operation.get("tags", []),
            },
        }
        
        return func_schema
    
    def _write_dynamic_cache(self, functions: List[dict], platform: str) -> None:
        """Write the dynamic cache file."""
        cache_file = OUT_DIRS['dynamic'] / "full_schemas.json"
        
        # Load existing cache or create new
        if cache_file.exists():
            try:
                cache_data = json.loads(cache_file.read_text())
            except:
                cache_data = {}
        else:
            cache_data = {}
        
        # Update with new functions
        cache_data[platform] = functions
        
        # Write back
        write_json(cache_file, cache_data, pretty=True)


def parse_cli() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Generate LLM-friendly function schemas from OpenAPI specs"
    )
    
    parser.add_argument(
        "platforms",
        nargs="+",
        help="Platform(s) to scaffold (e.g., meraki catalyst)",
    )
    
    parser.add_argument(
        "--include-http",
        nargs="+",
        choices=["GET", "POST", "PUT", "PATCH", "DELETE"],
        help="Only include specific HTTP methods",
    )
    
    parser.add_argument(
        "--name-pattern",
        help="Regex pattern to filter operations by name",
    )
    
    parser.add_argument(
        "--sdk-module",
        help="Override SDK module name",
    )
    
    parser.add_argument(
        "--drop-cache",
        action="store_true",
        help="Drop the dynamic cache before scaffolding",
    )
    
    return parser.parse_args()


def main():
    """Main entry point."""
    args = parse_cli()
    
    # Drop cache if requested
    if args.drop_cache:
        cache_root = Path(os.getenv("PLATFORM_DYNAMIC_CACHE_PATH", DEFAULT_DYNAMIC_CACHE.as_posix()))
        drop_dynamic_cache(cache_root)
    
    # Create output directories
    for out_dir in OUT_DIRS.values():
        out_dir.mkdir(parents=True, exist_ok=True)
    
    # Prepare filters
    include_http = set(args.include_http) if args.include_http else None
    name_re = re.compile(args.name_pattern) if args.name_pattern else None
    
    # Create scaffolder
    scaffolder = PlatformScaffolder()
    
    # Process each platform
    for platform in args.platforms:
        try:
            # Load OpenAPI spec
            spec = load_spec(platform)
            if not spec:
                log.error("Could not load spec for %s", platform)
                continue
            
            # Scaffold the platform
            scaffolder.scaffold_platform(
                platform,
                args.sdk_module or platform,
                spec,
                include_http,
                name_re
            )
            
        except Exception as e:
            log.error("Failed to scaffold %s: %s", platform, e)
            continue
    
    # Regenerate unified service init
    regenerate_unified_service_init(OUT_DIRS['cisco'])
    
    log.info("✅ DONE – all artifacts generated")


if __name__ == "__main__":
    main()