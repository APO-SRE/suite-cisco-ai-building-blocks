#!/usr/bin/env python3
"""
Unified Platform Scaffolder – phase-1
AUTO-GENERATES:

* app/llm/function_definitions/<platform>.json
* app/llm/openapi_specs/full_<platform>.json
* app/llm/platform_clients/<platform>_client.py
* app/llm/function_dispatcher/<platform>_dispatcher.py
* app/llm/unified_service/<platform>_service.py
"""
from __future__ import annotations

import argparse
import json
import logging
import re
import textwrap
from pathlib import Path
from typing import Dict, List

from dotenv import load_dotenv

# ───────── helpers ─────────────────────────────────────────────────────
from .utils.openapi_loader import load_spec          # type: ignore
from .utils.sdk_loader import load_client            # type: ignore
from .utils.dietify import dietify_schema            # type: ignore

# ───────── constants ───────────────────────────────────────────────────
load_dotenv()

ROOT = Path(__file__).resolve().parents[1]           # repo root
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

# ╭─────────────────────────────────────────────────────────────────────╮
# │ 1 ─ package initialisation helpers                                 │
# ╰─────────────────────────────────────────────────────────────────────╯
DISPATCHER_INIT = OUT_DIRS["disp"] / "__init__.py"
FUNCS_INIT = OUT_DIRS["diet"] / "__init__.py"

# 1-a  dispatcher registry (smart Meraki fallback)
if not DISPATCHER_INIT.exists():
    DISPATCHER_INIT.write_text(textwrap.dedent("""\
        \"\"\"
        Decorator-based dispatcher registry **plus** smart Meraki fallback.
        AUTO-GENERATED – DO NOT EDIT MANUALLY.
        \"\"\"
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
            api_key = os.getenv('MERAKI_DASHBOARD_API_KEY')
            if not api_key:
                raise ValueError('Meraki dispatch failed: missing MERAKI_DASHBOARD_API_KEY')

            dash = DashboardAPI(api_key=api_key,
                                suppress_logging=True,
                                print_console=False)

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
    """), encoding="utf-8")
    log.info("✓ %s", DISPATCHER_INIT.relative_to(ROOT))

# 1-b  function-definitions loader
if not FUNCS_INIT.exists():
    FUNCS_INIT.write_text(textwrap.dedent(f"""\
        # Auto-generated – DO NOT EDIT
        # {FUNCS_INIT.relative_to(ROOT)}
        \"\"\"
        Loads every *.json in this folder into FUNCTION_DEFINITIONS
            {{ '<platform>': [{{…}}, … ] , … }}
        \"\"\"
        from __future__ import annotations
        import json
        from pathlib import Path
        from typing import Dict, List, Any

        _DIR = Path(__file__).parent
        FUNCTION_DEFINITIONS: Dict[str, List[Dict[str, Any]]] = {{}}

        for _fp in _DIR.glob('*.json'):
            try:
                FUNCTION_DEFINITIONS[_fp.stem] = json.loads(_fp.read_text(encoding='utf-8'))
            except Exception as exc:
                print(f'[function_definitions] ⚠️  skipped {{_fp.name}}: {{exc}}')

        __all__ = ['FUNCTION_DEFINITIONS']
    """), encoding="utf-8")
    log.info("✓ %s", FUNCS_INIT.relative_to(ROOT))

# 1-c  empty __init__.py for every other folder
for folder in OUT_DIRS.values():
    init_py = folder / "__init__.py"
    if not init_py.exists():
        init_py.write_text(
            f"# Auto-generated – DO NOT EDIT\n# {init_py.relative_to(ROOT)}\n",
            encoding="utf-8",
        )
        log.info("✓ %s", init_py.relative_to(ROOT))

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
    """
    Convert *raw* into a valid Python identifier and guarantee uniqueness
    within a dispatcher file using the *seen* registry.
    """
    ident = _identifier_rx.sub("_", raw)
    if ident[0].isdigit():
        ident = f"op_{ident}"
    # prevent collisions if two different raw names normalise identically
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
    – searches both root *and* first-level sub-clients for attributes.
    """
    sdk_cls = load_client(sdk_module)                # e.g. meraki.DashboardAPI

    # ── Meraki-specific env guard
    extra_imports, extra_init = [], []
    if platform.lower() == "meraki":
        extra_imports.append("import os")
        extra_init.extend([
            "api_key = os.getenv('CISCO_MERAKI_API_KEY')",
            "if not api_key:",
            "    raise ValueError('Missing CISCO_MERAKI_API_KEY environment variable')",
            "kwargs['api_key'] = api_key",
            "",
        ])

    lines: list[str] = [
        f"# {(OUT_DIRS['client'] / f'{platform}_client.py').relative_to(ROOT)}",
        "# Auto-generated – DO NOT EDIT",
        f"import {sdk_module} as _sdk",
        *extra_imports,
        "",
        f"class {platform.capitalize()}Client:",
        f"    \"\"\"Thin wrapper around `{sdk_cls.__name__}` with fuzzy attribute lookup.\"\"\"",
        "",
        "    def __init__(self, **kwargs):",
        *[f"        {l}" for l in extra_init],
        f"        self._sdk = _sdk.{sdk_cls.__name__}(**kwargs)",

        "",
        "    def __getattr__(self, item):",
        "        # ① direct attribute on DashboardAPI",
        "        if hasattr(self._sdk, item):",
        "            return getattr(self._sdk, item)",
        "",
        "        # ② first-level sub-clients (organizations, networks, …)",
        "        for name in dir(self._sdk):",
        "            if name.startswith('_'):",
        "                continue",
        "            sub = getattr(self._sdk, name)",
        "            if hasattr(sub, item):",
        "                return getattr(sub, item)",
        "",
        "        raise AttributeError(f\"{self.__class__.__name__} has no attribute {item!r}\")",
        "",
    ]

    fp = OUT_DIRS['client'] / f'{platform}_client.py'
    fp.write_text('\n'.join(lines), encoding='utf-8')
    log.info('✓ %s', fp.relative_to(ROOT))





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

    _write_json(OUT_DIRS["full"] / f"{platform}.json", full_spec, pretty=True)
    _write_json(OUT_DIRS["full"] / f"full_{platform}.json", full_spec, pretty=True)

    diet_fns: List[dict] = []
    safe_name_seen: Dict[str, int] = {}

    for path, path_item in full_spec.get("paths", {}).items():
        for verb, op in path_item.items():
            if include_http and verb.upper() not in include_http:
                continue

            op_id = op.get("operationId") or f"{verb}_{path}"
            if name_re and not name_re.search(op_id):
                continue

            schema = {
                "name": op_id,
                "description": op.get("summary") or op.get("description", ""),
                "parameters": {"type": "object", "properties": {}, "required": []},
            }
            for p in op.get("parameters", []):
                schema["parameters"]["properties"][p["name"]] = {
                    "type": p.get("schema", {}).get("type", "string"),
                    "description": p.get("description", ""),
                }
                if p.get("required"):
                    schema["parameters"]["required"].append(p["name"])

            diet_fns.append(dietify_schema(schema))

    _write_json(OUT_DIRS["diet"] / f"{platform}.json", diet_fns)

    _emit_client_stub(platform, sdk_module)
    _emit_unified_service(platform)

    disp_fp = OUT_DIRS["disp"] / f"{platform}_dispatcher.py"
    lines: List[str] = [
        f"# {disp_fp.relative_to(ROOT)}",
        "from app.llm.function_dispatcher import register",
        f"from app.llm.platform_clients.{platform}_client import {platform.capitalize()}Client",
        "",
    ]
    for fn in diet_fns:
        safe_name = _py_identifier(fn["name"], safe_name_seen)
        lines.append(
            f"@register('{fn['name']}')\n"
            f"def {safe_name}(**kwargs):\n"
            f"    return {platform.capitalize()}Client().{safe_name}(**kwargs)\n"
        )

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

if __name__ == "__main__":
    main()
