#!/usr/bin/env python3
from __future__ import annotations
################################################################################
## src/scripts/platform_scaffolder_improved.py
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
Unified Platform Scaffolder – IMPROVED VERSION with hybrid SDK/REST API support
AUTO-GENERATES:

* app/llm/function_definitions/<platform>.json
* app/llm/openapi_specs/full_<platform>.json
* app/llm/platform_clients/<platform>_client.py
* app/llm/function_dispatcher/<platform>_dispatcher.py
* app/llm/unified_service/<platform>_service.py
* app/llm/sdk_coverage/<platform>_coverage.json

IMPROVEMENTS:
- SD-WAN client now handles both SDK calls and direct REST API calls
- Better error handling and fallback mechanisms
- Improved serialization for all response types
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

# Import all existing constants and configurations from the original file
exec(open(Path(__file__).parent / "platform_scaffolder.py").read())

def _emit_sdwan_client_hybrid() -> None:
    """
    Generate a hybrid SD-WAN client that can handle both SDK and REST API calls.
    """
    platform = "sdwan_mngr"
    sdk_module = "catalystwan.session"
    
    lines = [
        f"# app/llm/platform_clients/{platform}_client.py",
        "# Auto-generated – DO NOT EDIT",
        f"import {sdk_module} as _sdk",
        "import re, importlib",
        "from functools import partial",
        "import inspect",
        "from typing import get_origin, get_args, Any, Optional, Dict",
        "import os",
        "from catalystwan.session import create_manager_session",
        "import urllib3",
        "import json",
        "from pathlib import Path",
        "import requests",
        "from urllib.parse import urljoin",
        "",
        "# camel→snake splitter",
        "_CAMEL_TO_SNAKE = re.compile(r'(?<!^)(?=[A-Z])')",
        "# Package root of the generated SDK (e.g. \"catalystwan\")",
        "_SDK_PKG = _sdk.__name__",
        "",
        f"class {platform.capitalize()}Client:",
        '    """Hybrid SD-WAN client supporting both SDK and REST API calls."""',
        "",
        "    def __init__(self, **kwargs):",
        "        # Disable SSL warnings for SD-WAN sandbox",
        "        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)",
        "        ",
        "        # SD-WAN requires creating a session, not just instantiating a client",
        "        url = kwargs.get('url') or kwargs.get('base_url') or os.getenv('CISCO_SD_WAN_BASE_URL')",
        "        username = kwargs.get('username') or os.getenv('CISCO_SD_WAN_USERNAME')",
        "        password = kwargs.get('password') or os.getenv('CISCO_SD_WAN_PASSWORD')",
        "        port = kwargs.get('port')",
        "        subdomain = kwargs.get('subdomain')",
        "        ",
        "        if not all([url, username, password]):",
        "            raise ValueError(",
        "                'SD-WAN Manager requires url, username, and password. '",
        "                'Set via parameters or environment variables: '",
        "                'CISCO_SD_WAN_BASE_URL, CISCO_SD_WAN_USERNAME, CISCO_SD_WAN_PASSWORD'",
        "            )",
        "        ",
        "        # Store base URL for REST API calls",
        "        self._base_url = url",
        "        ",
        "        # Create the manager session",
        "        self._session = create_manager_session(",
        "            url=url,",
        "            username=username,",
        "            password=password,",
        "            port=port,",
        "            subdomain=subdomain",
        "        )",
        "        self._sdk = self._session  # Store session as _sdk for compatibility",
        "        self._api = self._session.api  # Get the API container",
        "        ",
        "        # Get authentication headers for REST API calls",
        "        self._auth_headers = self._get_auth_headers()",
        "",
        "    def _get_auth_headers(self) -> Dict[str, str]:",
        '        """Get authentication headers from the session for REST API calls."""',
        "        headers = {",
        '            "Content-Type": "application/json",',
        '            "Accept": "application/json"',
        "        }",
        "        ",
        "        # Try to get auth token from session",
        "        if hasattr(self._session, 'headers'):",
        "            headers.update(self._session.headers)",
        "        elif hasattr(self._session, 'auth') and hasattr(self._session.auth, 'headers'):",
        "            headers.update(self._session.auth.headers)",
        "        ",
        "        # Try to get JSESSIONID if available",
        "        if hasattr(self._session, 'jsessionid'):",
        '            headers["Cookie"] = f"JSESSIONID={self._session.jsessionid}"',
        "        elif hasattr(self._session, 'cookies'):",
        "            for cookie in self._session.cookies:",
        '                if cookie.name == "JSESSIONID":',
        '                    headers["Cookie"] = f"JSESSIONID={cookie.value}"',
        "                    break",
        "        ",
        "        return headers",
        "",
        "    # Load operation registry on first access",
        "    _operation_registry = None",
        "    ",
        "    @classmethod",
        "    def _load_registry(cls):",
        '        """Load the SD-WAN operation registry"""',
        "        if cls._operation_registry is None:",
        "            registry_path = Path(__file__).parent.parent / 'sdwan_operation_registry_full.json'",
        "            if registry_path.exists():",
        "                with open(registry_path) as f:",
        "                    cls._operation_registry = json.load(f)",
        "            else:",
        "                cls._operation_registry = {'operations': {}, 'comment': 'Registry file not found'}",
        "        return cls._operation_registry",
        "",
        "    def _make_rest_api_call(self, op_info: dict, **kwargs) -> Any:",
        '        """Make a direct REST API call when SDK method is not available."""',
        "        try:",
        "            # Build the URL",
        "            path = op_info['path']",
        "            method = op_info['method'].upper()",
        "            ",
        "            # Replace path parameters",
        "            if op_info.get('path_params'):",
        "                for param in op_info['path_params']:",
        "                    if param in kwargs:",
        "                        path = path.replace(f'{{{param}}}', str(kwargs.pop(param)))",
        "            ",
        "            # Build full URL",
        "            url = urljoin(self._base_url, f'/dataservice{path}')",
        "            ",
        "            # Prepare request parameters",
        "            request_kwargs = {",
        "                'headers': self._auth_headers.copy(),",
        "                'verify': False  # For sandbox environments",
        "            }",
        "            ",
        "            # Handle query parameters",
        "            query_params = {}",
        "            if op_info.get('query_params'):",
        "                for param_info in op_info['query_params']:",
        "                    param_name = param_info['name']",
        "                    if param_name in kwargs:",
        "                        query_params[param_name] = kwargs.pop(param_name)",
        "            ",
        "            if query_params:",
        "                request_kwargs['params'] = query_params",
        "            ",
        "            # Handle request body",
        "            if method in ['POST', 'PUT', 'PATCH']:",
        "                if 'body' in kwargs:",
        "                    request_kwargs['json'] = kwargs.pop('body')",
        "                elif kwargs:",
        "                    request_kwargs['json'] = kwargs",
        "            ",
        "            # Make the request",
        "            response = requests.request(method, url, **request_kwargs)",
        "            ",
        "            # Handle response",
        "            if response.status_code >= 400:",
        "                return {",
        "                    'error': f'HTTP {response.status_code}',",
        "                    'message': response.text,",
        "                    'url': url,",
        "                    'method': method",
        "                }",
        "            ",
        "            # Parse JSON response",
        "            if response.text:",
        "                try:",
        "                    data = response.json()",
        "                    # Handle vManage response format",
        "                    if isinstance(data, dict) and 'data' in data:",
        "                        return data['data']",
        "                    return data",
        "                except json.JSONDecodeError:",
        "                    return response.text",
        "            ",
        "            return {'status': 'success', 'status_code': response.status_code}",
        "            ",
        "        except Exception as e:",
        "            import traceback",
        "            return {",
        "                'error': str(e),",
        "                'traceback': traceback.format_exc(),",
        "                'operation': op_info.get('operationId', 'unknown'),",
        "                'url': url if 'url' in locals() else 'unknown'",
        "            }",
        "",
        "    def _resolve(self, name: str):",
        '        """Custom resolution for SD-WAN operations supporting both SDK and REST API."""',
        "        registry = self._load_registry()",
        "        op_info = registry.get('operations', {}).get(name)",
        "        ",
        "        if not op_info:",
        "            # Try default SDK resolution",
        "            return self._default_resolve(name)",
        "        ",
        "        # Check if we should use direct API",
        "        if op_info.get('use_direct_api', False):",
        "            # Return a wrapper function for REST API call",
        "            def rest_api_call(**kwargs):",
        "                return self._make_rest_api_call(op_info, **kwargs)",
        "            return rest_api_call",
        "        ",
        "        # Use SDK method",
        "        def sdk_call(**kwargs):",
        "            try:",
        "                endpoint_path = op_info.get('sdk_endpoint', '')",
        "                sdk_method = op_info.get('sdk_method', 'get')",
        "                ",
        "                endpoint = self._api",
        "                for part in endpoint_path.split('.'):",
        "                    if not hasattr(endpoint, part):",
        "                        # Fallback to REST API if SDK endpoint not found",
        "                        return self._make_rest_api_call(op_info, **kwargs)",
        "                    endpoint = getattr(endpoint, part)",
        "                ",
        "                if not hasattr(endpoint, sdk_method):",
        "                    # Fallback to REST API if SDK method not found",
        "                    return self._make_rest_api_call(op_info, **kwargs)",
        "                ",
        "                method = getattr(endpoint, sdk_method)",
        "                ",
        "                # Prepare parameters",
        "                call_params = {}",
        "                if op_info.get('path_params'):",
        "                    for param in op_info['path_params']:",
        "                        if param in kwargs:",
        "                            call_params[param] = kwargs.pop(param)",
        "                ",
        "                if op_info.get('query_params'):",
        "                    for param_info in op_info['query_params']:",
        "                        param_name = param_info['name']",
        "                        if param_name in kwargs:",
        "                            call_params[param_name] = kwargs.pop(param_name)",
        "                ",
        "                call_params.update(kwargs)",
        "                ",
        "                result = method(**call_params)",
        "                ",
        "                # Serialize the result",
        "                return self._serialize_recursively(result)",
        "                ",
        "            except Exception as e:",
        "                # Fallback to REST API on any SDK error",
        "                return self._make_rest_api_call(op_info, **kwargs)",
        "        ",
        "        return sdk_call",
        "",
        "    def _serialize_recursively(self, obj):",
        '        """',
        "        Recursively traverses an object and converts it into a JSON-serializable format,",
        "        handling all known catalystwan object types.",
        '        """',
        "        try:",
        "            from pydantic.fields import FieldInfo",
        "        except ImportError:",
        "            FieldInfo = type(None)",
        "        ",
        "        # 1. Handle base cases immediately",
        "        if obj is None or isinstance(obj, (str, int, float, bool)):",
        "            return obj",
        "        ",
        "        # 2. Handle already-serialized formats",
        "        if isinstance(obj, dict):",
        "            return {key: self._serialize_recursively(value) for key, value in obj.items()}",
        "        if isinstance(obj, (list, tuple)):",
        "            return [self._serialize_recursively(item) for item in obj]",
        "        ",
        "        # 3. Handle specific object types with known methods",
        "        if hasattr(obj, 'to_dict') and callable(obj.to_dict):",
        "            return self._serialize_recursively(obj.to_dict())",
        "        if hasattr(obj, 'model_dump') and callable(obj.model_dump):",
        "            return obj.model_dump()  # Already recursive and serializable",
        "        if hasattr(obj, 'dict') and callable(obj.dict):",
        "            return obj.dict()  # Already recursive and serializable",
        "        if hasattr(obj, 'value') and not callable(obj.value):",
        "            return obj.value",
        "        ",
        "        # 4. Handle Pydantic models and other objects with __dict__",
        "        if hasattr(obj, '__dict__'):",
        "            data = {}",
        "            for key, value in obj.__dict__.items():",
        "                if not key.startswith('_') and not isinstance(value, FieldInfo):",
        "                    data[key] = self._serialize_recursively(value)",
        "            if data:  # Only return if we found data",
        "                return data",
        "        ",
        "        # 5. Handle dataclasses (like Device/AlarmData) that don't use __dict__",
        "        data = {}",
        "        public_attrs = [attr for attr in dir(obj) if not attr.startswith('_') and not callable(getattr(obj, attr))]",
        "        for attr in public_attrs:",
        "            data[attr] = self._serialize_recursively(getattr(obj, attr))",
        "        if data:",
        "            return data",
        "        ",
        "        # 6. Final fallback",
        "        return str(obj)",
        "",
        "    def _default_resolve(self, name: str):",
        '        """Fallback resolution when operation is not in registry."""',
        "        snake = _CAMEL_TO_SNAKE.sub('_', name).lower()",
        "        if hasattr(self._sdk, name): return getattr(self._sdk, name)",
        "        if hasattr(self._sdk, snake): return getattr(self._sdk, snake)",
        "        ",
        "        if hasattr(self, '_api'):",
        "            for attr_name in dir(self._api):",
        "                if attr_name.startswith('_'): continue",
        "                attr = getattr(self._api, attr_name)",
        "                if hasattr(attr, name): return getattr(attr, name)",
        "                if hasattr(attr, snake): return getattr(attr, snake)",
        "        ",
        "        raise AttributeError(f\"{self.__class__.__name__} could not resolve attribute {name!r}\")",
        "",
        "    def __getattr__(self, name: str):",
        '        """Dynamic <operationId> lookup, with exception trapping."""',
        "        try:",
        "            return self._resolve(name)",
        "        except Exception as e:",
        "            raise AttributeError(f\"{self.__class__.__name__} could not resolve attribute {name!r} ({e})\")",
        "",
    ]
    
    fp = OUT_DIRS["client"] / f"{platform}_client.py"
    fp.write_text("\n".join(lines), encoding="utf-8")
    log.info("✓ Generated hybrid SD-WAN client: %s", fp.relative_to(ROOT))

# Override the _emit_client_stub function for SD-WAN
original_emit_client_stub = _emit_client_stub

def _emit_client_stub_enhanced(platform: str, sdk_module: str) -> None:
    """Enhanced client stub generation with SD-WAN hybrid support."""
    if platform.lower() == "sdwan_mngr":
        _emit_sdwan_client_hybrid()
    else:
        original_emit_client_stub(platform, sdk_module)

# Replace the original function
_emit_client_stub = _emit_client_stub_enhanced

if __name__ == "__main__":
    # Import and run the main function from the original scaffolder
    from platform_scaffolder import main
    main()