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
    
    sdk_cls = load_client(sdk_module)

    # universal imports for client stub
    extra_imports = [
        "import re, importlib, pkgutil, inspect",
        "from functools import partial"
    ]
    extra_init, extra_methods = [], []

    # Robust resolve and getattr helpers
    common_helpers = textwrap.dedent('''
        def _resolve(self, name: str):
            """Lookup endpoint in various SDK layouts."""
            # 1. Direct attribute
            if hasattr(self._sdk, name):
                return getattr(self._sdk, name)
            snake = _CAMEL_TO_SNAKE.sub('_', name).lower()
            if hasattr(self._sdk, snake):
                return getattr(self._sdk, snake)
            # 2. Nested sub-clients
            for sub_name in dir(self._sdk):
                if sub_name.startswith("_"):
                    continue
                sub = getattr(self._sdk, sub_name)
                for candidate in (name, snake):
                    if hasattr(sub, candidate):
                        return getattr(sub, candidate)
            # 3. Function-based OpenAPI client
            sdk_pkg = self._sdk.__class__.__module__.split('.')[0]
            try:
                api_pkg = importlib.import_module(f"{sdk_pkg}.api")
            except ImportError:
                api_pkg = None
            if api_pkg:
                for _, mod_name, _ in pkgutil.iter_modules(api_pkg.__path__):
                    mod = importlib.import_module(f"{sdk_pkg}.api.{mod_name}")
                    for candidate in (name, snake):
                        if hasattr(mod, candidate):
                            fn = getattr(mod, candidate)
                            return fn
            # 4. Alternate apis.tags layout
            try:
                tags_pkg = importlib.import_module(f"{sdk_pkg}.apis.tags")
            except ImportError:
                tags_pkg = None
            if tags_pkg:
                for _, mod_name, _ in pkgutil.iter_modules(tags_pkg.__path__):
                    mod = importlib.import_module(f"{sdk_pkg}.apis.tags.{mod_name}")
                    for _, cls in inspect.getmembers(mod, inspect.isclass):
                        if cls.__name__.endswith("Api"):
                            inst = cls(self._sdk)
                            for candidate in (name, snake):
                                if hasattr(inst, candidate):
                                    return getattr(inst, candidate)
            raise AttributeError(f"{self.__class__.__name__} has no attribute '{name}'")

        def __getattr__(self, name: str):
            """Dynamically resolve and bind endpoint functions."""
            target = self._resolve(name)
            if callable(target):
                # bind free functions expecting client parameter
                if getattr(target, '__self__', None) is None:
                    return partial(target, client=self._sdk)
                return target
            return target
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



    # assemble client file
    lines: list[str] = [
        f"# {(OUT_DIRS['client'] / f'{platform}_client.py').relative_to(ROOT)}",
        "# Auto-generated – DO NOT EDIT",
        f"import {sdk_module} as _sdk",
        *extra_imports,
        "",
        "# camel→snake splitter",
        "_CAMEL_TO_SNAKE = re.compile(r'(?<!^)(?=[A-Z])')",
        "_SDK_PKG = _sdk.__name__",
        "",
        f"class {platform.capitalize()}Client:",
        f'    """Thin wrapper around `{sdk_cls.__name__}` with flexible resolution."""',
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






def _emit_client_stub(platform: str, sdk_module: str) -> None:
    """
    Write app/llm/platform_clients/<platform>_client.py
    with module-level _CAMEL_TO_SNAKE and in-class camel→snake fallback.
    """
    sdk_cls = load_client(sdk_module)

    # universal camel→snake imports
    extra_imports = ["import re, importlib", "from functools import partial"]
    extra_init, extra_methods = [], []

    # common in-class methods (no duplicate _CAMEL_TO_SNAKE here)
    common_helpers = textwrap.dedent("""
        def _resolve(self, name: str):
            \"\"\"
            Resolve <operationId> to a callable.

            ① direct attribute on the AuthenticatedClient
            ② attribute on a sub‑client (camel→snake tried too)
            ③ <sdk>.api.<tag>.<function>.sync  – the pattern used by
            openapi‑python‑client
            \"\"\"
            if hasattr(self._sdk, name):
                return getattr(self._sdk, name)
            snake = _CAMEL_TO_SNAKE.sub('_', name).lower()
            if hasattr(self._sdk, snake):
                return getattr(self._sdk, snake)
            for sub_name in dir(self._sdk):
                if sub_name.startswith('_'):
                    continue
                sub = getattr(self._sdk, sub_name)
                for candidate in (name, snake):
                    if hasattr(sub, candidate):
                        return getattr(sub, candidate)

            # ---- pattern ③  ----------------------------------------------------
            # e.g. 'fabrics_get_all_fabrics'
            if '_' in snake:
                tag, func_tail = snake.split('_', 1)          # tag = 'fabrics'
                api_mod_path = f'{_SDK_PKG}.api.{tag}'        # …api.fabrics
                try:
                    api_mod = importlib.import_module(api_mod_path)
                except ImportError:
                    pass
                else:
                    # 3‑a: function re‑exported by api.<tag>.__init__.py
                    if hasattr(api_mod, func_tail):
                        func_mod = getattr(api_mod, func_tail)
                    else:
                        # 3‑b: full snake‑name module (fabrics_get_all_fabrics)
                        full_mod_path = f'{api_mod_path}.{snake}'
                        try:
                            func_mod = importlib.import_module(full_mod_path)
                        except ImportError:
                            # 3‑c: legacy name without tag (get_all_fabrics)
                            try:
                                func_mod = importlib.import_module(f'{api_mod_path}.{func_tail}')
                            except ImportError:
                                func_mod = None
                    if func_mod is not None and hasattr(func_mod, 'sync'):
                        return partial(func_mod.sync, client=self._sdk)
                                        

            raise AttributeError(f"{self.__class__.__name__} has no attribute '{name}'")

        def __getattr__(self, name: str):
            target = self._resolve(name)
            if callable(target):
                return target
            return target
    """).splitlines()


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

            op_params = op.get("parameters", [])
            all_params = {p["name"]: p for p in op_params if "name" in p}

            schema = {
                "name": op_id,
                "description": op.get("summary") or op.get("description", ""),
                "parameters": {
                    "type": "object",
                    "properties": {
                        name: {
                            "type": p.get("schema",{}).get("type","string"),
                            "description": p.get("description",""),
                        }
                        for name,p in all_params.items()
                    },
                    "required": [
                        name
                        for name,p in all_params.items()
                        if p.get("required",False)
                    ] + list(path_level_params),
                },
            }
            diet_fns.append(dietify_schema(schema))


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

        lines.extend([
            f"@register('{fn['name']}')",
            f"def {safe_name}({', '.join(sig_parts)}):",
            f"    return {platform.capitalize()}Client().{safe_name}(**{{{', '.join(call_parts)}}})",
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
