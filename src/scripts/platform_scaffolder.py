#!/usr/bin/env python3
from __future__ import annotations
################################################################################
## src/scripts/platform_scaffolder.py
## Copyright (c) 2025 Jeff Teeter
## Cisco Systems, Inc.
## Licensed under the Apache License, Version 2.0 (see LICENSE)
## Distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND.
################################################################################
"""
DISCLAIMER: USE AT YOUR OWN RISK

This software is provided "as is", without any express or implied warranties, including, but not limited to,
the implied warranties of merchantability and fitness for a particular purpose. In no event shall the authors or
contributors be liable for any direct, indirect, incidental, special, exemplary, or consequential damages
(including, but not limited to, procurement of substitute goods or services; loss of use, data, or profits;
or business interruption) however caused and on any theory of liability, whether in contract, strict liability,
or tort (including negligence or otherwise) arising in any way out of the use of this software.

This script is provided for demonstration and development purposes only and is not intended for use in production
environments. You are solely responsible for any modifications or adaptations made for your specific use case.

By using this code, you agree that you have read, understood, and accept these terms.
"""
"""
Unified Platform Scaffolder – phase-1 with Enhanced SDK Integration
AUTO-GENERATES:

* app/llm/function_definitions/<platform>.json
* app/llm/openapi_specs/full_<platform>.json
* app/llm/platform_clients/<platform>_client.py
* app/llm/function_dispatcher/<platform>_dispatcher.py
* app/llm/unified_service/<platform>_service.py
* app/llm/sdk_coverage/<platform>_coverage.json (NEW)
"""
import sys
import os
from pathlib import Path
import argparse
import json
import logging
import re
import textwrap
from typing import Dict, List, Set, Tuple, Optional
import keyword
from dotenv import load_dotenv
from functools import partial

# ───────── helpers ─────────────────────────────────────────────────────
from app.utils.openapi_loader import load_spec
from app.utils.sdk_loader     import load_client
from app.utils.dietify        import dietify_schema
from app.utils.sdk_initialization import SDKInitializer
from app.utils.registry_io import load_registry

# Import platform customizations
from platform_customizations import PLATFORM_OVERRIDES, INJECTION_CONFIG, generate_aliases

# Import function customizations directly
import importlib.util
spec = importlib.util.spec_from_file_location(
    "function_customizations", 
    Path(__file__).parent / "platform_scaffolder_utilities" / "function_customizations.py"
)
function_customizations = importlib.util.module_from_spec(spec)
spec.loader.exec_module(function_customizations)
get_function_customization = function_customizations.get_function_customization

# Import the enhanced SDK introspection
try:
    from app.utils.sdk_introspection import (
        SDKIntrospector,
        SDKOpenAPIFilter,
        SDKPattern
    )
    ENHANCED_INTROSPECTION = True
except ImportError:
    # Fall back to original introspection if enhanced not available
    from app.utils.sdk_introspection import (
        discover_sdk_methods,
        discover_sdk_methods_from_client,
        filter_openapi_by_sdk,
        check_operation_id_availability
    )
    ENHANCED_INTROSPECTION = False

# ───────── constants ───────────────────────────────────────────────────
load_dotenv()
NAME_ALLOWED_RX = re.compile(r'[^a-zA-Z0-9_.-]')          # OpenAI rule
MAX_NAME_LEN    = 64
ROOT = Path(__file__).resolve().parents[1]
LLM_DIR = ROOT / "app" / "llm"

OUT_DIRS = {
    "diet":    LLM_DIR / "function_definitions",
    "full":    LLM_DIR / "openapi_specs",
    "client":  LLM_DIR / "platform_clients",
    "disp":    LLM_DIR / "function_dispatcher",
    "service": LLM_DIR / "unified_service",
    "coverage": LLM_DIR / "sdk_coverage",  # NEW: Coverage reports
}
for p in OUT_DIRS.values():
    p.mkdir(parents=True, exist_ok=True)

logging.basicConfig(level=logging.INFO, format="%(levelname)s | %(message)s")
log = logging.getLogger("scaffolder")

# Section 0
#################################################################################################################
# Platform overrides have been moved to the platform_customizations module
# The PLATFORM_OVERRIDES dictionary is imported from platform_customizations/platform_overrides.py

# Parameter injection configurations have been moved to the platform_customizations module
# See platform_customizations/injection_config.py for the INJECTION_CONFIG dictionary


ALWAYS_KEEP_TAGS = {"devices", "inventory"}

DEFAULT_DYNAMIC_CACHE = LLM_DIR / "platform_dynamic_cache"

def _drop_dynamic_cache() -> None:
    cache_root = Path(
        os.getenv("PLATFORM_DYNAMIC_CACHE_PATH", DEFAULT_DYNAMIC_CACHE.as_posix())
    ).resolve()
    cache_file = cache_root / "full_schemas.json"
    if cache_file.exists():
        try:
            cache_file.unlink()
            log.info("🗑  dropped %s", cache_file.relative_to(ROOT))
        except Exception as exc:
            log.warning("could not drop cache %s: %s", cache_file, exc)



def _emit_org_injection(platform: str, non_body_keys: list[str]) -> list[str]:
    """
    Generates the dispatcher code for parameter injection based on the
    central INJECTION_CONFIG dictionary.
    """
    lines: list[str] = []
    config = INJECTION_CONFIG.get(platform.lower())
    
    if not config:
        return lines

    env_var = config["env_var"]
    params_to_inject = config["params"]

    lines.append(f"    # ── auto-inject {env_var} ─────────────────")
    lines.append(f"    env_val = os.getenv('{env_var}')")
    lines.append("    if env_val:")
    
    for param_name, value_template in params_to_inject.items():
        final_template = value_template.replace('{value}', '{env_val}')
        formatted_value = f'f"""{final_template}"""'
  
        lines.extend([
            f"        if '{param_name}' in {non_body_keys} and '{param_name}' not in final_kwargs:",
            f"            final_kwargs['{param_name}'] = {formatted_value}",
        ])
    lines.append("")
    return lines

# ╭─────────────────────────────────────────────────────────────────────╮
# │ 1 ─ package initialisation helpers                                 │
# ╰─────────────────────────────────────────────────────────────────────╯
DISPATCHER_INIT = OUT_DIRS["disp"] / "__init__.py"
FUNCS_INIT      = OUT_DIRS["diet"] / "__init__.py"

# 1-a  dispatcher registry (smart Meraki fallback)
if not DISPATCHER_INIT.exists():
    DISPATCHER_INIT.write_text(textwrap.dedent('''\
        """
        Decorator-based dispatcher registry **plus** smart Meraki fallback.
        AUTO-GENERATED – DO NOT EDIT MANUALLY.
        """
        from __future__ import annotations
        import importlib
        import os
        from pathlib import Path
        from typing import Any, Callable, Dict
        from meraki import DashboardAPI

        _registry: Dict[str, Callable[..., Any]] = {}

        def register(name: str):
            def _decorator(fn: Callable[..., Any]):
                _registry[name] = fn
                return fn
            return _decorator

        # auto-import sub-dispatchers so their @register executes
        _pkg_path = Path(__file__).parent
        for _p in _pkg_path.glob('*_dispatcher.py'):
            if _p.name != '__init__.py':
                importlib.import_module(f'{__name__}.{_p.stem}')

        # Meraki SDK fallback
        def _call_meraki(fname: str, kwargs: Dict[str, Any]):
            api_key = os.getenv('CISCO_MERAKI_API_KEY')
            if not api_key:
                raise ValueError('Meraki dispatch failed: missing CISCO_MERAKI_API_KEY')

            dash = DashboardAPI(api_key=api_key,
                                suppress_logging=True,
                                print_console=True)

            if hasattr(dash, fname):
                return getattr(dash, fname)(**kwargs)

            for attr in dir(dash):
                if attr.startswith('_'):
                    continue
                sub = getattr(dash, attr)
                if hasattr(sub, fname):
                    return getattr(sub, fname)(**kwargs)

            raise AttributeError(f'No Meraki SDK method {fname!r} found')

        def dispatch_function_call(name: str, arguments: Dict[str, Any]):
            if name in _registry:
                return _registry[name](**arguments)
            return _call_meraki(name, arguments)

        __all__ = ['dispatch_function_call', 'register']
    '''), encoding="utf-8")
    log.info("✓ %s", DISPATCHER_INIT.relative_to(ROOT))

# 1-b  function-definitions loader
if not FUNCS_INIT.exists():
    FUNCS_INIT.write_text(textwrap.dedent('''\
        # Auto-generated – DO NOT EDIT
        # {FUNCS_INIT.relative_to(ROOT)}
        """
        Loads every *.json in this folder into FUNCTION_DEFINITIONS
            { '<platform>': [{…}, … ] , … }
        """
        from __future__ import annotations
        import json
        from pathlib import Path
        from typing import Dict, List, Any

        _DIR = Path(__file__).parent
        FUNCTION_DEFINITIONS: Dict[str, List[Dict[str, Any]]] = {}

        for _fp in _DIR.glob('*.json'):
            try:
                FUNCTION_DEFINITIONS[_fp.stem] = json.loads(_fp.read_text(encoding='utf-8'))
            except Exception as exc:
                print(f'[function_definitions] ⚠️  skipped {_fp.name}: {exc}')

        __all__ = ['FUNCTION_DEFINITIONS']
    '''), encoding="utf-8")
    log.info("✓ %s", FUNCS_INIT.relative_to(ROOT))


# ╭─────────────────────────────────────────────────────────────────────╮
# │ 2 ─ utility functions                                              │
# ╰─────────────────────────────────────────────────────────────────────╯
def _write_json(p: Path, obj, *, pretty: bool = False):
    p.write_text(
        json.dumps(obj, indent=2 if pretty else None, separators=(",", ":")),
        encoding="utf-8",
    )
    log.info("✓ %s", p.relative_to(ROOT))

_identifier_rx = re.compile(r"[^0-9A-Za-z_]")
def _py_identifier(raw: str, seen: Dict[str, int]) -> str:
    ident = _identifier_rx.sub("_", raw)
    if ident and ident[0].isdigit():
        ident = f"op_{ident}"
    if ident in seen:
        seen[ident] += 1
        ident = f"{ident}_{seen[ident]}"
    else:
        seen[ident] = 0
    return ident


# ── helpers ────────────────────────────────────────────────────────────────
 



def _emit_client_stub(platform: str, sdk_module: str) -> None:
    """
    Write app/llm/platform_clients/<platform>_client.py
    with module-level _CAMEL_TO_SNAKE and in-class camel→snake fallback.
    """
    sdk_cls = load_client(sdk_module)

    # universal camel→snake imports
    extra_imports = [
    "import re, importlib",
    "from functools import partial",
    "import inspect",
    "from typing import get_origin, get_args, Any",
]
   
    extra_init, extra_methods = [], []

    # common in-class methods (no duplicate _CAMEL_TO_SNAKE here)
        # common in‑class methods (no duplicate _CAMEL_TO_SNAKE here)
    common_helpers = textwrap.dedent('''
        @staticmethod
        def _unwrap_model(annotation):
            """
            Return the concrete model class if *annotation* is Optional[T],
            Union[T, None], etc.  Otherwise return the annotation itself.
            """
            origin = get_origin(annotation)
            if origin is None:
                return annotation
            if origin is list:           # body=None edge‑case, keep original
                return annotation
            # Union / Optional
            args = [a for a in get_args(annotation) if a is not type(None)]  # noqa: E721
            return args[0] if args else annotation

        # ──────────────────────────────────────────────────────────────
        #  DYNAMIC OPERATION‑ID RESOLUTION
        # ──────────────────────────────────────────────────────────────
        def _resolve(self, name: str):
            """
            Locate <operationId> and return a callable. This method attempts multiple
            strategies to support different SDK architectures.

            Scheme (in order):
            1. Direct attr on ApiClient (e.g., PascalCase or snake_case).
            2. Attr on any nested sub-client (for Meraki-style SDKs).
            3. Standalone module function (for openapi-python-client SDKs like Nexus Hyperfabric).
            4. Class-based API tag handler (for Intersight-style SDKs).
            5. Suffix match as a final fallback.
            """
            snake = _CAMEL_TO_SNAKE.sub('_', name).lower()

            # Strategy 1: Direct attribute on the SDK client
            if hasattr(self._sdk, name):
                return getattr(self._sdk, name)
            if hasattr(self._sdk, snake):
                return getattr(self._sdk, snake)

            # Strategy 2: Look inside nested sub-clients (for Meraki)
            for sub_name in dir(self._sdk):
                if sub_name.startswith('_'):
                    continue
                sub = getattr(self._sdk, sub_name)
                for cand in (name, snake):
                    if hasattr(sub, cand):
                        return getattr(sub, cand)

            # Strategy 3: Handle openapi-python-client's standalone function pattern (for Nexus Hyperfabric)
            # Tries to import a module like: nexus_hyperfabric.api.fabrics.fabrics_get_all_fabrics
            parts = snake.split('_')
            if parts:
                tag = parts[0]
                func_module_name = snake
                try:
                    module_path = f"{_SDK_PKG}.api.{tag}.{func_module_name}"
                    mod = importlib.import_module(module_path)
                    if hasattr(mod, 'sync'):
                        # Wrap the `sync` function to pre-fill the `client` argument
                        return partial(mod.sync, client=self._sdk)
                except (ImportError, AttributeError):
                    pass  # If this fails, it's not this architecture; proceed to the next strategy.

            # Strategy 4: Class-based API tag handler (for Intersight)
            # Tries to import a class like intersight.api.compute_api.ComputeApi
            if parts:
                # For Intersight, we need to handle get_/post_/patch_/delete_ prefixes
                # get_compute_physical_summary_list -> compute_api.ComputeApi
                if parts[0] in ['get', 'post', 'patch', 'delete', 'put']:
                    # Skip the HTTP method prefix for API class detection
                    api_parts = parts[1:]
                else:
                    api_parts = parts
                
                # This loop logic is important for Intersight's naming conventions
                for i in range(len(api_parts), 0, -1):
                    tag = '_'.join(api_parts[:i])
                    try:
                        cls_mod = importlib.import_module(f"{_SDK_PKG}.api.{tag}_api")
                        class_name = f"{''.join(p.capitalize() for p in tag.split('_'))}Api"
                        if hasattr(cls_mod, class_name):
                            cls = getattr(cls_mod, class_name)
                            inst = cls(self._sdk)
                            if hasattr(inst, snake):
                                return getattr(inst, snake)
                    except (ImportError, AttributeError):
                        continue

            # Strategy 5: Suffix match as a last resort
            for cand in (name, snake):
                for attr in dir(self._sdk):
                    if attr.endswith('_' + cand):
                        return getattr(self._sdk, attr)

            raise AttributeError(f"{self.__class__.__name__} could not resolve attribute {name!r}")
                                     



        # expose everything through __getattr__
        def __getattr__(self, name: str):
            print(f"[{self.__class__.__name__}] Attempting to resolve function: '{name}'") # <-- ADD THIS LINE
            target = self._resolve(name)
            if callable(target):
                return self._wrap_method(target)
            return target
 

        def _wrap_method(self, target):
            """
            Wrap SDK call so that a plain dict passed as *body* is automatically
            converted into the expected pydantic/model class.
            """
            sig        = inspect.signature(target)
            body_param = sig.parameters.get("body")
            model_cls  = self._unwrap_model(body_param.annotation) if body_param else None

            def wrapper(body=None, **kwargs):
                if model_cls and isinstance(body, dict):
                    body = model_cls.from_dict(body) if hasattr(model_cls, "from_dict") else model_cls(**body)
                if body_param:
                    return target(body=body, **kwargs)
                return target(**kwargs)
            return wrapper
    ''')


# Import platform authorization configurations
    from platform_customizations.platform_auth import get_platform_auth
    
    # Get platform-specific auth configuration
    auth_config = get_platform_auth(platform, sdk_module)
    extra_imports.extend(auth_config['extra_imports'])
    extra_init.extend(auth_config['extra_init'])
    extra_methods.extend(auth_config['extra_methods'])
    
    # Handle custom common_helpers for specific platforms (like SD-WAN)
    if auth_config['common_helpers']:
        common_helpers = auth_config['common_helpers']
    # inject common methods
    # For SD-WAN, common_helpers was already defined with custom methods
    if platform.lower() != "sdwan_mngr":
        extra_methods.extend(f"    {l}" for l in common_helpers.split('\n'))
    else:
        # SD-WAN already has its custom common_helpers defined above
        extra_methods.extend(f"    {l}" for l in common_helpers.split('\n'))

    # assemble client file:
    lines: list[str] = [
        f"# {(OUT_DIRS['client'] / f'{platform}_client.py').relative_to(ROOT)}",
        "# Auto-generated – DO NOT EDIT",
        f"import {sdk_module} as _sdk",
        *extra_imports,
        "",
        "# camel→snake splitter",
        "_CAMEL_TO_SNAKE = re.compile(r'(?<!^)(?=[A-Z])')",
        "# Package root of the generated SDK (e.g. \"nexus_hyperfabric\")",
        "_SDK_PKG = _sdk.__name__",
        "",
        f"class {platform.capitalize()}Client:",
        f'    """Thin wrapper around `{sdk_cls.__name__}` with camel→snake fallback."""',
        "",
        "    def __init__(self, **kwargs):",
        *[f"        {l}" for l in extra_init],
    ]
    
    # Only add the SDK instantiation line if it's not SD-WAN
    # (SD-WAN creates the session in extra_init)
    if platform.lower() != "sdwan_mngr":
        lines.append(f"        self._sdk = _sdk.{sdk_cls.__name__}(**kwargs)")
    
    lines.extend([
        "",
        *extra_methods,
        "",
    ])

    fp = OUT_DIRS["client"] / f"{platform}_client.py"
    fp.write_text("\n".join(lines), encoding="utf-8")
    log.info("✓ %s", fp.relative_to(ROOT))


def _regenerate_unified_service_init():
    """
    Scan all files in OUT_DIRS['service'] matching '*_service.py',
    and rebuild unified_service/__init__.py so that it:
      1. Tries to import each <platform>ServiceClient
      2. Safely skips if the module is missing
      3. Populates a guarded _SERVICE_REGISTRY
      4. Defines UnifiedService to dispatch by 'platform'
    """
    service_dir   = OUT_DIRS["service"]
    init_path     = service_dir / "__init__.py"
    service_files = sorted([p for p in service_dir.glob("*_service.py") if p.is_file()])

    lines: List[str] = [
        "# Auto-generated – DO NOT EDIT",
        "# This file was rebuilt by platform_scaffolder.py",
        "",
        "_SERVICE_REGISTRY: dict[str, type] = {}",
        "",
    ]

    for fp in service_files:
        stem       = fp.stem                    # e.g. "catalyst_service"
        platform   = stem.replace("_service", "")  # "catalyst"
        class_name = f"{platform.capitalize()}ServiceClient"

        lines.append("try:")
        lines.append(f"    from .{platform}_service import {class_name}")
        lines.append(f"    _SERVICE_REGISTRY['{platform}'] = {class_name}")
        lines.append("except ImportError:")
        lines.append(f"    {class_name} = None")
        lines.append("")

    lines.extend([
        "class UnifiedService:",
        '    """Return the correct ServiceClient for a given platform"""',
        "",
        "    def __new__(cls, platform: str, *args, **kwargs):",
        "        try:",
        "            impl = _SERVICE_REGISTRY[platform.lower()]",
        "        except KeyError as exc:",
        "            valid = ', '.join(_SERVICE_REGISTRY.keys())",
        "            raise ValueError(",
        "                f\"Unsupported platform '{platform}'. Valid options: {valid}\"",
        "            ) from exc",
        "        return impl(*args, **kwargs)",
        "",
        "__all__ = ['UnifiedService',",
    ])
    for fp in service_files:
        platform = fp.stem.replace("_service", "")
        lines.append(f"    '{platform.capitalize()}ServiceClient',")
    lines.append("]\n")

    init_path.write_text("\n".join(lines), encoding="utf-8")
    log.info("✓ %s", init_path.relative_to(ROOT))


def _emit_unified_service(platform: str):
    code = textwrap.dedent(f"""
        # Auto-generated – DO NOT EDIT
        from app.llm.platform_clients.{platform}_client import {platform.capitalize()}Client

        class {platform.capitalize()}ServiceClient:
            \"\"\"Generic call-through service used by FastAPI.\"\"\"

            def __init__(self, **sdk_kwargs):
                self.client = {platform.capitalize()}Client(**sdk_kwargs)

            def call(self, function_name: str, **kwargs):
                try:
                    method = getattr(self.client, function_name)
                except AttributeError:
                    raise ValueError(
                        f"No such method '{{function_name}}' on {platform.capitalize()}Client"
                    )
                return method(**kwargs)
    """).strip()

    fp = OUT_DIRS["service"] / f"{platform}_service.py"
    fp.write_text(f"# {fp.relative_to(ROOT)}\n\n{code}", encoding="utf-8")
    log.info("✓ %s", fp.relative_to(ROOT))


# ── Enhanced SDK introspection helpers ─────────────────────────────────────
def perform_sdk_introspection(
    platform: str, 
    sdk_module_name: str, 
    openapi_spec: dict
) -> Tuple[dict, dict, dict]:
    """
    Perform enhanced SDK introspection and filter OpenAPI spec.
    
    Returns:
        Tuple of (filtered_spec, operation_mapping, coverage_report)
    """
    platform_config = PLATFORM_OVERRIDES.get(platform.lower(), {})
    
    registry = load_registry()  
    registry_config = registry.get(platform.lower(), {})

    # Check if SDK filtering is enabled (opt-in, disabled by default)
    if not platform_config.get("enable_sdk_filtering", False):
        log.info(f"ℹ️  SDK filtering disabled for {platform} (default behavior)")
        return openapi_spec, {}, {"coverage_percentage": 100, "note": "SDK filtering disabled"}
    
    if ENHANCED_INTROSPECTION:
        try:
            # Use the enhanced introspector
            introspector = SDKIntrospector(platform, sdk_module_name)
            
            # Create the filter
            sdk_filter = SDKOpenAPIFilter(introspector)
            
            # Apply custom operation_id_map if provided
            custom_map = platform_config.get("operation_id_map", {})
            if custom_map:
                log.info(f"Applying custom operation ID mappings: {custom_map}")
                for op_id, sdk_method in custom_map.items():
                    # Create a mock SDK method for the mapping
                    from app.utils.sdk_introspection import SDKMethod
                    sdk_filter.methods[sdk_method] = SDKMethod(
                        name=sdk_method,
                        signature=None,
                        parent_class="Unknown"
                    )
                    sdk_filter.operation_id_map[op_id] = sdk_filter.methods[sdk_method]
            
            # Filter the OpenAPI spec
            filtered_spec, operation_mapping = sdk_filter.filter_openapi_spec(openapi_spec)
            
            # Generate coverage report
            coverage_report = sdk_filter.generate_coverage_report(openapi_spec)
            
            log.info(f"✓ SDK Coverage for {platform}: {coverage_report['coverage_percentage']:.1f}%")
            log.info(f"  - Total operations: {coverage_report['total_operations']}")
            log.info(f"  - Covered: {coverage_report['covered_operations']}")
            log.info(f"  - Missing: {len(coverage_report['missing_operations'])}")
            
            return filtered_spec, operation_mapping, coverage_report
            
        except Exception as e:
            log.warning(f"⚠️  Enhanced SDK introspection failed for {platform}: {e}")
            log.warning("Falling back to original introspection")
            # Fall through to original introspection
    
    # Original introspection logic
    sdk_methods = set()
    log.info(f"🔍 Discovering SDK methods for {platform}...")
    try:
        # Create a temporary client instance to discover methods
        sdk_client_module = load_client(sdk_module_name)
        
        # Try to create a minimal instance for introspection
        temp_client = None
        if platform.lower() == "meraki":
            import os
            api_key = os.getenv('CISCO_MERAKI_API_KEY', 'dummy-key-for-introspection')
            temp_client = sdk_client_module(api_key=api_key, suppress_logging=True)
        elif platform.lower() == "catalyst":
            try:
                temp_client = sdk_client_module()
            except:
                pass
        elif platform.lower() == "intersight":
            import importlib
            intersight_module = importlib.import_module(sdk_module_name)
            sdk_methods = discover_sdk_methods(intersight_module)
            if sdk_methods:
                log.info(f"✓ Discovered {len(sdk_methods)} SDK methods from module introspection")
            else:
                try:
                    temp_client = sdk_client_module()
                except:
                    pass
        else:
            try:
                temp_client = sdk_client_module()
            except:
                pass
        
        if temp_client and not sdk_methods:
            sdk_methods = discover_sdk_methods_from_client(temp_client)
            log.info(f"✓ Discovered {len(sdk_methods)} SDK methods")
        elif not sdk_methods:
            log.warning(f"⚠️  Could not discover SDK methods, proceeding without SDK filtering")
    except Exception as e:
        log.warning(f"⚠️  SDK introspection failed: {e}, proceeding without filtering")
    
    # Filter OpenAPI spec if we have SDK methods
    if sdk_methods:
        log.info("🔧 Filtering OpenAPI spec to match SDK capabilities...")
        filtered_spec = filter_openapi_by_sdk(openapi_spec, sdk_methods)
        log.info(f"✓ Filtered spec: {len(filtered_spec.get('paths', {}))} paths remaining from {len(openapi_spec.get('paths', {}))}")
        
        # Calculate coverage
        total_ops = sum(1 for path in openapi_spec.get('paths', {}).values() 
                       for method in path.values() 
                       if isinstance(method, dict) and 'operationId' in method)
        filtered_ops = sum(1 for path in filtered_spec.get('paths', {}).values() 
                          for method in path.values() 
                          if isinstance(method, dict) and 'operationId' in method)
        coverage = (filtered_ops / total_ops * 100) if total_ops > 0 else 0
        
        coverage_report = {
            "platform": platform,
            "sdk_module": sdk_module_name,
            "total_operations": total_ops,
            "covered_operations": filtered_ops,
            "coverage_percentage": coverage,
            "sdk_methods_count": len(sdk_methods)
        }
        
        return filtered_spec, {}, coverage_report
    
    return openapi_spec, {}, {"coverage_percentage": 100, "note": "No SDK filtering applied"}

def write_coverage_report(platform: str, coverage_report: dict):
    """Write SDK coverage report to file."""
    coverage_file = OUT_DIRS["coverage"] / f"{platform}_coverage.json"
    coverage_file.write_text(
        json.dumps(coverage_report, indent=2),
        encoding="utf-8"
    )
    log.info(f"✓ Coverage report: {coverage_file.relative_to(ROOT)}")


# ╭─────────────────────────────────────────────────────────────────────╮
# │ 3 ─ per-platform scaffolding                                        │
# ╰─────────────────────────────────────────────────────────────────────╯

def scaffold_one(
    platform: str,
    sdk_module: str,
    spec_path: Path,
    include_http: set[str] | None,
    name_re: re.Pattern | None,
    disable_sdk_filtering: bool = False,
) -> None:
    # Initialize total_spec_operations at function scope
    total_spec_operations = 0
 
    # EXISTING CODE: Get the specific overrides for the current platform from the global config.
    platform_config = PLATFORM_OVERRIDES.get(platform.lower(), {})
    
    # NEW CODE: Load the full registry and merge with overrides
    registry = load_registry()  # This loads your platform_registry.json
    registry_config = registry.get(platform.lower(), {})
    
    # Merge registry config with PLATFORM_OVERRIDES (overrides take precedence)
    full_platform_config = {**registry_config, **platform_config}
    platform_config = full_platform_config
    
    # NEW CODE: Initialize SDK helper only if SDK filtering is enabled (opt-in)
    if platform_config.get("enable_sdk_filtering", False):
        try:
            initializer = SDKInitializer()  # It will auto-find platform_registry.json
        except Exception as e:
            log.warning(f"Failed to initialize SDK helper: {e}")
            # Continue without SDK initialization
    
    # Override sdk_module if specified in registry
    if not sdk_module and platform_config.get("sdk_module"):
        sdk_module = platform_config["sdk_module"]
        log.info(f"Using SDK module from registry: {sdk_module}")
    
    # EXISTING CODE: Load the OpenAPI spec
    full_spec = load_spec(spec_path)
    
    # NEW CODE: Analyze HTTP method breakdown
    http_method_counts = {}
    for path, path_item in full_spec.get("paths", {}).items():
        for verb, op in path_item.items():
            if verb.upper() in {"GET", "POST", "PUT", "PATCH", "DELETE"}:
                http_method_counts[verb.upper()] = http_method_counts.get(verb.upper(), 0) + 1
                total_spec_operations += 1
    
    log.info(f"📊 OpenAPI Spec Analysis for {platform}:")
    log.info(f"  - Total operations: {total_spec_operations}")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        if method in http_method_counts:
            log.info(f"  - {method}: {http_method_counts[method]} operations")
    
    # MODIFIED CODE: Enhanced SDK introspection with registry awareness
    filtered_spec, operation_mapping, coverage_report = perform_sdk_introspection(
        platform, sdk_module, full_spec
    )
    
    # Add HTTP method counts to coverage report
    coverage_report["http_method_breakdown"] = http_method_counts
    
    # EXISTING CODE: Write coverage report
    write_coverage_report(platform, coverage_report)
    
    # Store operation mapping in platform config for later use
    platform_config["_operation_mapping"] = operation_mapping
    
    # EXISTING CODE: Use filtered spec
    full_spec = filtered_spec

    _write_json(OUT_DIRS["full"] / f"{platform}.json",        full_spec, pretty=True)
    _write_json(OUT_DIRS["full"] / f"full_{platform}.json",   full_spec, pretty=True)

    diet_fns       : List[dict] = []
    skipped_ops    : List[dict] = []
    safe_name_seen : Dict[str,int] = {}

    for path, path_item in full_spec.get("paths", {}).items():
        # first collect any path-level parameters (always required)
        path_level_params = {
            param["name"]
            for param in path_item.get("parameters", [])
            if param.get("in") == "path" and "name" in param
        }

        for verb, op in path_item.items():
            # Skip non-HTTP method entries (like 'parameters')
            if verb.upper() not in {"GET", "POST", "PUT", "PATCH", "DELETE", "HEAD", "OPTIONS"}:
                continue
            
            if include_http and verb.upper() not in include_http:
                continue

 
            # Get the raw operationId once to use for platform-specific checks.
            raw_op_id = op.get("operationId")

            # Check against the platform-specific blocklist.
            if raw_op_id in platform_config.get("blocklist", set()):
                log.info(f"🚫  Skipping blocked operationId for '{platform}': {raw_op_id}")
                continue
            
            # Check if operation is available in SDK (already filtered but double-check)
            sdk_methods = set()  # This would come from introspection
            if sdk_methods and raw_op_id:
                # Check custom operation_id_map first
                operation_id_map = platform_config.get("operation_id_map", {})
                if raw_op_id in operation_id_map:
                    # Use the mapped SDK method name
                    sdk_method_name = operation_id_map[raw_op_id]
                    if sdk_method_name not in sdk_methods:
                        log.info(f"⚠️  Skipping {raw_op_id} - mapped method {sdk_method_name} not found in SDK")
                        skipped_ops.append({"op": raw_op_id, "reason": f"mapped SDK method '{sdk_method_name}' not found"})
                        continue
                elif not check_operation_id_availability(raw_op_id, sdk_methods):
                    log.info(f"⚠️  Skipping {raw_op_id} - not found in SDK")
                    skipped_ops.append({"op": raw_op_id, "reason": "not available in SDK"})
                    continue

            # 👉 robust name sanitisation  (always OpenAI‑safe)
            # Use the raw_op_id we already fetched.
            op_id = raw_op_id or f"{verb}_{path}"
            op_id = NAME_ALLOWED_RX.sub('_', op_id)       # illegal → "_"
            op_id = re.sub(r'__+', '_', op_id)                # collapse "___"
            op_id = op_id.lstrip('.-')                        # cannot start with "." | "-"
            if not op_id:                                     # empty after clean‑up
                op_id = f"op_{verb}"
            op_id = op_id[:MAX_NAME_LEN]                      # 1‑64 chars total
            if platform.lower() == "intersight" and op_id.lower().startswith("getview"):
                skipped_ops.append({"op": op_id, "reason": "view endpoint"})
                continue

            if name_re and not name_re.search(op_id):
                continue
            op_params  = op.get("parameters", [])
            all_params = {p["name"]: p for p in op_params if "name" in p}
 
            def resolve_schema(schema_ref, full_spec):
                if '$ref' in schema_ref:
                    ref_path = schema_ref['$ref'].split('/')[1:]
                    resolved = full_spec
                    for part in ref_path:
                        resolved = resolved.get(part, {})
                    return resolved
                return schema_ref
 
            def build_properties(schema, full_spec):
                properties = {}
                required_fields = schema.get('required', [])
                for prop_name, prop_schema in schema.get('properties', {}).items():
                    resolved_prop_schema = resolve_schema(prop_schema, full_spec)
                    prop_type = resolved_prop_schema.get("type", "object")
                    prop_entry = {
                        "type": prop_type,
                        "description": resolved_prop_schema.get("description", "")
                    }
                    if prop_type == "object":
                        prop_entry.update(build_properties(resolved_prop_schema, full_spec))
                    elif prop_type == "array":
                        prop_entry["items"] = build_properties(resolved_prop_schema.get("items", {}), full_spec)
                    properties[prop_name] =  prop_entry

                return {
                    "properties": properties,
                    "required": required_fields
                }

            if "requestBody" in op:
                rb = op["requestBody"]
                # Try different content types
                rb_content = None
                for content_type in ["application/json", "application/x-www-form-urlencoded", "multipart/form-data"]:
                    rb_content = rb.get("content", {}).get(content_type, {})
                    if rb_content:
                        break
                
                rb_schema_ref = rb_content.get("schema", {}) if rb_content else {}
                resolved_schema = resolve_schema(rb_schema_ref, full_spec)

                schema_details = build_properties(resolved_schema, full_spec)

                # For form-encoded data, flatten the properties into main parameters
                if content_type == "application/x-www-form-urlencoded":
                    # Add each property from the request body as a top-level parameter
                    for prop_name, prop_schema in schema_details["properties"].items():
                        all_params[prop_name] = {
                            "name": prop_name,
                            "schema": prop_schema,
                            "description": prop_schema.get("description", ""),
                            "required": prop_name in schema_details["required"],
                        }
                else:
                    # For JSON bodies, keep as nested body parameter
                    description = rb.get("description", "Request payload")
                    if not description.strip():
                        description = "Request payload"

                    all_params["body"] = {
                        "name": "body",
                        "schema": {
                            "type": "object",
                            "properties": schema_details["properties"],
                            "required": schema_details["required"]
                        },
                        "description": description,
                        "required": rb.get("required", False),
                    }

            schema = {
                "name": op_id,
                "description": op.get("summary") or op.get("description", ""),
                "parameters": {
                    "type": "object",
                    "properties": {
                        name: {
                            "type": p.get("schema", {}).get("type", "string"),
                            "description": p.get("description", ""),
                            **({"properties": p["schema"]["properties"]} if "properties" in p["schema"] else {}),
                            **({"items": p["schema"]["items"]} if "items" in p["schema"] else {}),
                        }
                        for name, p in all_params.items()
                    },
                    "required": [
                        name for name, p in all_params.items() if p.get("required", False)
                    ] + list(path_level_params),
                },
            }
            schema['metadata'] = {'platform': platform}
            # Get the set of injected parameter names for the current platform.
            injected_keys = INJECTION_CONFIG.get(platform.lower(), {}).get("params", {}).keys()

            if injected_keys:
                required_params = schema['parameters'].get('required', [])
                new_required = [p for p in required_params if p not in injected_keys]
                
                if len(new_required) < len(required_params):
                    removed_keys = set(required_params) - set(new_required)
                    log.info(f"✓ Making injected keys optional for '{op_id}': {', '.join(removed_keys)}")
                    schema['parameters']['required'] = new_required
 

            # Check for and apply platform-specific description overrides.
            # We use the raw, un-sanitized operationId as the key.
            if raw_op_id in platform_config.get("descriptions", {}):
                schema['description'] = platform_config["descriptions"][raw_op_id]
                log.info(f"✓ Overwrote description for '{platform}': {raw_op_id}")

 


            # ------------------------------------------------------------------
            # Diet‑ify the schema.  If the diet version loses *all* parameters
            # (common for complex requestBody objects) fall back to the full
            # version so the LLM still sees at least the top‑level keys.
            # ------------------------------------------------------------------
            skinny = dietify_schema(schema)
            if not skinny["parameters"]["properties"]:      # nothing left?
                diet_fns.append(schema)                     # keep full
            else:
                diet_fns.append(skinny)





            # ─────────────── NEW: helpful aliases (drop tag prefix, singularise) ───────────
            if "_" in op_id and platform.lower() != "sdwan_mngr":  # Skip aliases for SD-WAN
                _, rest = op_id.split("_", 1)
                # Only create alias if it's not just a number
                if rest and not rest.isdigit():
                    for alias in {rest, rest.rstrip("s")}:
                        alias = alias[:MAX_NAME_LEN]
                        if alias and alias not in {f["name"] for f in diet_fns}:
                            s2          = schema.copy()
                            s2["name"]  = alias
                            diet_fns.append(dietify_schema(s2))
 

    _write_json(OUT_DIRS["diet"] / f"{platform}.json",   diet_fns)
    _write_json(ROOT / "scaffold_skip.log", skipped_ops, pretty=True)
    
 
    log.info(f"📝 Functions actually scaffolded:")
    if include_http:
        log.info(f"  - Filtered to HTTP methods: {', '.join(sorted(include_http))}")
    log.info(f"  - Skipped operations: {len(skipped_ops)}")
    log.info(f"  - Functions written to file: {len(diet_fns)}")
    
   
    if total_spec_operations > 0 and len(diet_fns) < total_spec_operations * 0.9:
        reduction_pct = ((total_spec_operations - len(diet_fns)) / total_spec_operations) * 100
        log.info(f"  - Reduction from spec: {reduction_pct:.1f}% ({total_spec_operations} → {len(diet_fns)})")

    _emit_client_stub(platform,   sdk_module)
    _emit_unified_service(platform)
    _regenerate_unified_service_init()


    disp_fp = OUT_DIRS["disp"] / f"{platform}_dispatcher.py"
    
    # Collect all custom imports needed
    custom_imports = set()
    for fn in diet_fns:
        custom = get_function_customization(platform, fn['name'])
        custom_imports.update(custom.get('imports', []))
    
    lines = [
        f"# {disp_fp.relative_to(ROOT)}",
        "import os",
        "from typing import Any",
        "from app.llm.function_dispatcher import register",
        f"from app.llm.platform_clients.{platform}_client import {platform.capitalize()}Client",
    ]
    
    # Add custom imports
    if custom_imports:
        for imp in sorted(custom_imports):
            lines.append(imp)
    
    lines.append("")

    type_mapping: Dict[str, str] = {
        "string":  "str",
        "integer": "int",
        "number":  "float",
        "boolean": "bool",
        "array":   "list",
        "object":  "dict",
    }
    # Reserved names that would conflict with imports
    RESERVED_NAMES = {'register', 'Any', 'os'}
    
    for fn in diet_fns:
        safe_name = _py_identifier(fn["name"], safe_name_seen)
        
        # Handle reserved name conflicts
        if safe_name in RESERVED_NAMES:
            safe_name = f"{safe_name}_op"
            
        props     = fn["parameters"]["properties"]
        required  = set(fn["parameters"].get("required", []))

        # build signature
        def py_name(p):
            ident = _identifier_rx.sub("_", p)
            return ident + "_arg" if keyword.iskeyword(ident) else ident

        required_params = [p for p in props if p in required]
        optional_params = [p for p in props if p not in required]
        sig_parts = []
        for pname in required_params:
            meta = props[pname]
            sig_parts.append(f"{py_name(pname)}: {type_mapping.get(meta.get('type'), 'Any')}")
        for pname in optional_params:
            meta = props[pname]
            sig_parts.append(f"{py_name(pname)}: {type_mapping.get(meta.get('type'), 'Any')} = None")
        signature = ", ".join(sig_parts)



        # dispatcher body
        non_body_params = {p: py_name(p) for p in props if p != "body"}
        
        # Get function customizations
        custom = get_function_customization(platform, fn['name'])
        
        lines.extend([
            f"@register('{fn['name']}')",
            f"def {safe_name}({signature}):",
            '    """Auto-generated wrapper for clarity and maintainability."""',
        ])
        
        # Add any custom imports at the function level as comments (since we can't import inside function)
        # The imports should be added at module level instead
        
        # Add pre-kwargs customization code
        lines.extend(custom.get('pre_kwargs', []))
        
        lines.extend([
            "    # Explicitly build keyword arguments, excluding None values.",
            "    final_kwargs = {}",
        ])

        # Generate an explicit check for each non-body parameter
        for orig, san in non_body_params.items():
            lines.append(f"    if {san} is not None:")
            lines.append(f"        final_kwargs['{orig}'] = {san}")
        lines.append("")

        # Handle the body payload explicitly if it exists
        if 'body' in props:
            py_body_name = py_name('body')
            lines.extend([
                f"    # The 'body' parameter is handled separately.",
                f"    body_payload = {py_body_name} if {py_body_name} is not None else None",
            ])
        else:
            lines.extend([
                "    # No body parameter for this function.",
                "    body_payload = None",
            ])
        lines.append("")
        
        # Add post-kwargs customization code (after kwargs built, before injection)
        lines.extend(custom.get('post_kwargs', []))

        # insert injection
        non_body_keys = list(non_body_params.keys())
        lines.extend(_emit_org_injection(platform, non_body_keys))

        # finish with a clearer target call
        # Check if we have a mapped SDK method name for this operation
        platform_config = PLATFORM_OVERRIDES.get(platform, {})
        operation_id_map = platform_config.get("operation_id_map", {})
        target_method_name = operation_id_map.get(fn['name'], safe_name)
        
        lines.extend([
            f"    client = {platform.capitalize()}Client()",
            f"    # Use attribute access to trigger __getattr__ for dynamic resolution",
            f"    target = client.{target_method_name}",
            "",
            "    if body_payload is not None:",
            "        return target(body=body_payload, **final_kwargs)",
            "    return target(**final_kwargs)",
            "",
        ])

        


        
        # Generate aliases for the function
        # See platform_customizations/aliases.py for the alias generation logic
        alias_lines = generate_aliases(fn, safe_name, platform)
        lines.extend(alias_lines)
 



    disp_fp.write_text("\n".join(lines), encoding="utf-8")
    log.info("✓ %s", disp_fp.relative_to(ROOT))


# ╭─────────────────────────────────────────────────────────────────────╮
# │ 4 ─ CLI                                                            │
# ╰─────────────────────────────────────────────────────────────────────╯
def _parse_cli():
    ap = argparse.ArgumentParser()
    ap.add_argument("--platform")
    ap.add_argument("--sdk-module")
    ap.add_argument("--openapi-spec")
    ap.add_argument("--include-http-methods")
    ap.add_argument("--name-pattern")
    ap.add_argument("--all", action="store_true",
                    help="Scaffold for every full_*.json already present")
    ap.add_argument("--disable-sdk-filtering", action="store_true",
                    help="Disable SDK introspection and filtering (generate all functions from OpenAPI)")
    ap.add_argument("--coverage-only", action="store_true",
                    help="Only generate coverage reports without scaffolding")
    return ap.parse_args()


# ── diet-filter helpers ──────────────────────────────────────────────
def _looks_too_big(op: dict) -> bool:
    tags = {t.lower() for t in op.get("tags", [])}
    if tags & ALWAYS_KEEP_TAGS:
        return False
    if len(op.get("parameters", [])) > 30:
        return True
    if any(p.get("name") in {"perPage", "page"} for p in op.get("parameters", [])):
        return True
    return False


def main():
    args = _parse_cli()
    
    # Add coverage-only mode
    if args.coverage_only:
        log.info("Running in coverage-only mode")
        for platform in PLATFORM_OVERRIDES.keys():
            spec_path = OUT_DIRS["full"] / f"full_{platform}.json"
            if spec_path.exists():
                log.info(f"Generating coverage for {platform}")
                full_spec = json.loads(spec_path.read_text())
                # Look up SDK module from existing logic or config
                sdk_module = None
                # Try to find it from existing generated files or config
                if platform.lower() == "meraki":
                    sdk_module = "meraki"
                elif platform.lower() == "catalyst":
                    sdk_module = "dnacentersdk"
                elif platform.lower() == "intersight":
                    sdk_module = "intersight"
                # Add other platforms as needed
                
                if sdk_module:
                    _, _, coverage = perform_sdk_introspection(
                        platform, 
                        sdk_module, 
                        full_spec
                    )
                    write_coverage_report(platform, coverage)
        return

    if args.all and (args.platform or args.sdk_module or args.openapi_spec):
        raise SystemExit("--all cannot be used with other flags")

    if args.all:
        platforms = [
            p.stem.replace("full_", "") for p in OUT_DIRS["full"].glob("full_*.json")
        ]
    else:
        if not (args.platform and args.sdk_module and args.openapi_spec):
            raise SystemExit("Need --platform, --sdk-module, and --openapi-spec")
        platforms = [args.platform]

    include_http = (
        {m.upper() for m in args.include_http_methods.split(",")}
        if args.include_http_methods
        else None
    )
    name_re = re.compile(args.name_pattern) if args.name_pattern else None

    for plat in platforms:
        spec = (
            Path(args.openapi_spec)
            if args.openapi_spec
            else OUT_DIRS["full"] / f"{plat}.json"
        )
        log.info("⏳ Scaffolding %s …", plat)
        scaffold_one(plat, args.sdk_module or plat, spec, include_http, name_re, args.disable_sdk_filtering)

    log.info("✅ DONE – all artefacts generated")
    _drop_dynamic_cache()


if __name__ == "__main__":
    main()