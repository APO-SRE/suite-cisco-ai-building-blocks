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
Unified Platform Scaffolder – phase-1
AUTO-GENERATES:

* app/llm/function_definitions/<platform>.json
* app/llm/openapi_specs/full_<platform>.json
* app/llm/platform_clients/<platform>_client.py
* app/llm/function_dispatcher/<platform>_dispatcher.py
* app/llm/unified_service/<platform>_service.py
"""
import sys
import os
from pathlib import Path
import argparse
import json
import logging
import re
import textwrap
from typing import Dict, List
import keyword
from dotenv import load_dotenv
from functools import partial

# ───────── helpers ─────────────────────────────────────────────────────
from app.utils.openapi_loader import load_spec
from app.utils.sdk_loader     import load_client
from app.utils.dietify        import dietify_schema

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
}
for p in OUT_DIRS.values():
    p.mkdir(parents=True, exist_ok=True)

logging.basicConfig(level=logging.INFO, format="%(levelname)s | %(message)s")
log = logging.getLogger("scaffolder")

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
    "from typing import get_origin, get_args",
]
   
    extra_init, extra_methods = [], []

    # common in-class methods (no duplicate _CAMEL_TO_SNAKE here)
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
            if origin is list:      # body=None edge‑case, keep original
                return annotation
            # Union / Optional
            args = [a for a in get_args(annotation) if a is not type(None)]  # noqa: E721
            return args[0] if args else annotation

        def _resolve(self, name: str):
            """
            Resolve <operationId> to a callable.

            ① direct attribute on the AuthenticatedClient
            ② attribute on a sub‑client (camel→snake tried too)
            ③ <sdk>.api.<tag>.<function>.sync  – the pattern used by
               openapi‑python‑client
            """
            if hasattr(self._sdk, name):
                return getattr(self._sdk, name)
            snake = _CAMEL_TO_SNAKE.sub('_', name).lower()
            if hasattr(self._sdk, snake):
                return getattr(self._sdk, snake)

            # 2) Nested sub‑clients
            for sub_name in dir(self._sdk):
                if sub_name.startswith('_'):
                    continue
                sub = getattr(self._sdk, sub_name)
                for candidate in (name, snake):
                    if hasattr(sub, candidate):
                        return getattr(sub, candidate)

            # 3) openapi‑python‑client pattern
            if '_' in snake:
                tag, func_tail = snake.split('_', 1)
                api_mod_path = f'{_SDK_PKG}.api.{tag}'
                try:
                    api_mod = importlib.import_module(api_mod_path)
                except ImportError:
                    pass
                else:
                    if hasattr(api_mod, func_tail):
                        func_mod = getattr(api_mod, func_tail)
                    else:
                        try:
                            func_mod = importlib.import_module(f'{api_mod_path}.{snake}')
                        except ImportError:
                            try:
                                func_mod = importlib.import_module(f'{api_mod_path}.{func_tail}')
                            except ImportError:
                                func_mod = None
                    if func_mod is not None and hasattr(func_mod, 'sync'):
                        return partial(func_mod.sync, client=self._sdk)

            # 4) Suffix match: alias without tag
            for candidate in (name, snake):
                for attr in dir(self._sdk):
                    if attr.endswith("_" + candidate):
                        return getattr(self._sdk, attr)

            raise AttributeError(f"{self.__class__.__name__} has no attribute '{name}'")

        def __getattr__(self, name: str):
            target = self._resolve(name)
            if callable(target):
                return self._wrap_method(target)
            return target

        def _wrap_method(self, target):
            sig        = inspect.signature(target)
            body_param = sig.parameters.get("body")
            model_cls  = self._unwrap_model(body_param.annotation) if body_param else None
            def wrapper(body=None, **kwargs):
                # If SDK expects a model class but we got a plain dict → wrap it
                if model_cls and isinstance(body, dict):
                    if hasattr(model_cls, 'from_dict'):
                        body = model_cls.from_dict(body)
                    else:
                        body = model_cls(**body)
                if body_param:               # SDK has a 'body' parameter
                    return target(body=body, **kwargs)
                return target(**kwargs)      # no body in signature
            return wrapper
    ''').splitlines()


 
    # Meraki-specific injection
    if platform.lower() == "meraki":
        extra_imports.append("import os")
        extra_init.extend([
            "api_key = os.getenv('CISCO_MERAKI_API_KEY')",
            "if not api_key:",
            "    raise ValueError('Missing CISCO_MERAKI_API_KEY environment variable')",
            "kwargs['api_key'] = api_key",
            "",
        ])

    # Nexus auth injection
    if platform.lower() == "nexus_hyperfabric":
        extra_imports.append("import os")
        extra_init.extend([
            "base_url = os.getenv('NEXUS_HYPERFABRIC_BASE_URL')",
            "token    = os.getenv('NEXUS_HYPERFABRIC_BEARER_TOKEN')",
            "if not base_url or not token:",
            "    raise ValueError('Missing NEXUS_HYPERFABRIC_BASE_URL or NEXUS_HYPERFABRIC_BEARER_TOKEN')",
            "kwargs.setdefault('base_url', base_url)",
            "kwargs.setdefault('token', token)",
            "",
        ])

    # inject common methods
    extra_methods.extend(f"    {l}" for l in common_helpers)

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
        f"        self._sdk = _sdk.{sdk_cls.__name__}(**kwargs)",
        "",
        *extra_methods,
        "",
    ]

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


# ╭─────────────────────────────────────────────────────────────────────╮
# │ 3 ─ per-platform scaffolding                                       │
# ╰─────────────────────────────────────────────────────────────────────╯
def scaffold_one(
    platform: str,
    sdk_module: str,
    spec_path: Path,
    include_http: set[str] | None,
    name_re: re.Pattern | None,
) -> None:
    full_spec = load_spec(spec_path)

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
            if include_http and verb.upper() not in include_http:
                continue

            # 👉 robust name sanitisation  (always OpenAI‑safe)
            raw_op_id = op.get("operationId") or f"{verb}_{path}"
            op_id = NAME_ALLOWED_RX.sub('_', raw_op_id)       # illegal → "_"
            op_id = re.sub(r'__+', '_', op_id)                # collapse "___"
            op_id = op_id.lstrip('.-')                        # cannot start with "." | "-"
            if not op_id:                                     # empty after clean‑up
                op_id = f"op_{verb}"
            op_id = op_id[:MAX_NAME_LEN]                      # 1‑64 chars total





            if name_re and not name_re.search(op_id):
                continue
            op_params  = op.get("parameters", [])
            all_params = {p["name"]: p for p in op_params if "name" in p}

            # ─────────────── NEW: pull in JSON requestBody as single “body” param ─────────
            # ─────────────── NEW: Recursive Schema Resolver ─────────
            def resolve_schema(schema_ref, full_spec):
                """Recursively resolve $ref schema references."""
                if '$ref' in schema_ref:
                    ref_path = schema_ref['$ref'].split('/')[1:]  # ["components", "schemas", "SchemaName"]
                    resolved = full_spec
                    for part in ref_path:
                        resolved = resolved.get(part, {})
                    return resolve_schema(resolved, full_spec)
                elif schema_ref.get('type') == 'object':
                    return {
                        "type": "object",
                        "properties": {
                            prop_name: resolve_schema(prop_schema, full_spec)
                            for prop_name, prop_schema in schema_ref.get('properties', {}).items()
                        },
                        "required": schema_ref.get('required', [])
                    }
                elif schema_ref.get('type') == 'array':
                    items_schema = resolve_schema(schema_ref.get('items', {}), full_spec)
                    return {
                        "type": "array",
                        "items": items_schema
                    }
                else:
                    # Base types: string, integer, boolean, etc.
                    return {
                        "type": schema_ref.get('type', 'string'),
                        "description": schema_ref.get('description', '')
                    }

            # ─────────────── UPDATED: Handle requestBody schema ─────────
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
                    properties[prop_name] = prop_entry

                return {
                    "properties": properties,
                    "required": required_fields
                }

            if "requestBody" in op:
                rb = op["requestBody"]
                rb_content = rb.get("content", {}).get("application/json", {})
                rb_schema_ref = rb_content.get("schema", {})
                resolved_schema = resolve_schema(rb_schema_ref, full_spec)

                schema_details = build_properties(resolved_schema, full_spec)

                description = rb.get("description", "Request payload")
                if not description.strip():
                    description = "Request payload"

                all_params["body"] = {
                    "name": "body",
                    "schema": {
                        "type": "object",
                        "properties": schema_details["properties"],  # Ensure explicit properties key
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
            if "_" in op_id:
                _, rest = op_id.split("_", 1)
                for alias in {rest, rest.rstrip("s")}:
                    alias = alias[:MAX_NAME_LEN]
                    if alias and alias not in {f["name"] for f in diet_fns}:
                        s2          = schema.copy()
                        s2["name"]  = alias
                        diet_fns.append(dietify_schema(s2))
 

    _write_json(OUT_DIRS["diet"] / f"{platform}.json",   diet_fns)
    _write_json(ROOT / "scaffold_skip.log", skipped_ops, pretty=True)

    _emit_client_stub(platform,   sdk_module)
    _emit_unified_service(platform)
    _regenerate_unified_service_init()

    disp_fp = OUT_DIRS["disp"] / f"{platform}_dispatcher.py"
    lines = [
        f"# {disp_fp.relative_to(ROOT)}",
        "from typing import Any",                     # <— for fallback
        "from app.llm.function_dispatcher import register",
        f"from app.llm.platform_clients.{platform}_client import {platform.capitalize()}Client",
        "",
    ]

    # map OpenAPI types → Python annotation
    type_mapping: Dict[str, str] = {
        "string":  "str",
        "integer": "int",
        "number":  "float",
        "boolean": "bool",
        "array":   "list",
        "object":  "dict",
    }

    for fn in diet_fns:
        safe_name = _py_identifier(fn["name"], safe_name_seen)
        props     = fn["parameters"]["properties"]
        required  = sorted(fn["parameters"]["required"])
        optional  = sorted(set(props) - set(required))

        props     = fn["parameters"]["properties"]
        required  = sorted(fn["parameters"]["required"])

        # ensure each required key is present in props
        # dietify_schema sometimes drops "body" or other complex objects.
        # Inject a default so lookups never raise KeyError.
        for missing in (set(required) - set(props)):
            props[missing] = {"type": "object"}

        optional  = sorted(set(props) - set(required))

        def sanitize(param: str) -> str:
            ident = _identifier_rx.sub("_", param)
            if keyword.iskeyword(ident):
                ident += "_arg"
            return ident

        sanitized = {p: sanitize(p) for p in props}

        sig_parts  = [f"{sanitized[p]}: {type_mapping.get(props[p]['type'],'Any')}" for p in required]
        if optional:
            sig_parts.append("**kwargs")
 
        call_parts = [f"'{p}': {sanitized[p]}" for p in required]
        if optional:
            call_parts.append("**kwargs")
        

        #
        lines.extend([
            f"@register('{fn['name']}')",
            f"def {safe_name}(body: dict | None = None, **kwargs):",
            '    """Auto‑generated wrapper.',
            '',
            '    If `body` is omitted we wrap all remaining keyword arguments',
            '    into it so the underlying SDK still receives the required',
            '    payload.',
            '    """',
            "    if body is None:",
            "        body = kwargs",
            "        kwargs = {}",
            f"    return {platform.capitalize()}Client().{safe_name}(body=body, **kwargs)",
            "",
        ])
            
 
        

        # ─────────────── NEW: also register aliases for the same callable ────────────────
        if '_' in fn['name']:
            tag, rest = fn['name'].split('_', 1)
            for alias in {rest, rest.rstrip('s')}:
                if alias and alias != fn['name']:
                    lines.extend([
                        f"# alias → easier for LLM",
                        f"register('{alias}')(globals()['{safe_name}'])",
                        ""
                    ])
 



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
        scaffold_one(plat, args.sdk_module, spec, include_http, name_re)

    log.info("✅ DONE – all artefacts generated")
    _drop_dynamic_cache()


if __name__ == "__main__":
    main()
