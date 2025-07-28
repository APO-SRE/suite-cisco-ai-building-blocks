"""
Client file generation for the platform scaffolder.
"""

import logging
import textwrap
from pathlib import Path
from typing import List

from ..platform_customizations.platform_auth import get_platform_auth

log = logging.getLogger("scaffolder")

# Common helper methods for all clients (except SD-WAN which has custom ones)
DEFAULT_COMMON_HELPERS = textwrap.dedent('''
    def _resolve(self, name: str):
        """Dynamic <operationId> lookup with camel→snake fallback."""
        # If it's directly on the SDK object, go with that
        if hasattr(self._sdk, name):
            target = getattr(self._sdk, name)
            # --- decorator-injection logic for nexus_hyperfabric ---
            if hasattr(self, '_dispatcher'):
                import functools
                @functools.wraps(target)
                def wrapper(**kwargs):
                    return self._dispatcher(name, target, kwargs)
                return wrapper
            return target

        # Otherwise, try the snake_case version
        snake = _CAMEL_TO_SNAKE.sub('_', name).lower()
        if hasattr(self._sdk, snake):
            target = getattr(self._sdk, snake)
            # --- decorator-injection logic for nexus_hyperfabric ---
            if hasattr(self, '_dispatcher'):
                import functools
                @functools.wraps(target)
                def wrapper(**kwargs):
                    return self._dispatcher(name, target, kwargs)
                return wrapper
            return target

        raise AttributeError(f"{self.__class__.__name__} could not resolve attribute {name!r}")

    def __getattr__(self, name: str):
        """Dynamic <operationId> lookup, with exception trapping."""
        try:
            return self._resolve(name)
        except Exception as e:
            raise AttributeError(f"{self.__class__.__name__} could not resolve attribute {name!r} ({e})")
    ''')


def emit_client_stub(platform: str, sdk_module: str, out_dir: Path) -> None:
    """
    Generate the <platform>_client.py file that wraps the SDK.
    
    This creates a thin wrapper around the platform's SDK with:
    - Authentication injection from environment variables
    - Dynamic method resolution (camelCase -> snake_case)
    - Platform-specific customizations
    """
    # Get platform-specific configuration
    auth_config = get_platform_auth(platform, sdk_module)
    
    extra_imports = ["import re"]
    extra_imports.extend(auth_config['extra_imports'])
    
    extra_init = auth_config['extra_init']
    extra_methods = auth_config['extra_methods']
    
    # Use custom common_helpers if provided, otherwise use default
    common_helpers = auth_config.get('common_helpers', DEFAULT_COMMON_HELPERS)
    
    # Build the SDK import and class detection
    if sdk_module.startswith("app.llm.cisco_sdks."):
        sdk_import = f"from {sdk_module} import *"
        sdk_init = [
            "",
            "# ── sniff out the SDK's primary API class ─────────",
            f"candidates = [obj for name, obj in globals().items() if isinstance(obj, type) and obj.__module__ == '{sdk_module}']",
            "if not candidates:",
            f"    raise RuntimeError('Could not find SDK class in {sdk_module}')",
            "_SdkCls = candidates[0]",
            f"self._sdk = _SdkCls(**kwargs)",
        ]
    else:
        sdk_import = f"import {sdk_module} as _sdk"
        sdk_init = ["self._sdk = _sdk.ApiClient(**kwargs)"]
    
    extra_init.extend(sdk_init)
    
    # Add common methods
    if platform.lower() != "sdwan_mngr":  # SD-WAN has custom helpers
        extra_methods.extend(f"    {l}" for l in common_helpers.split('\n'))
    else:
        # SD-WAN already has its custom common_helpers defined
        extra_methods.extend(f"    {l}" for l in common_helpers.split('\n'))
    
    # Assemble the client file
    lines: List[str] = [
        f"# {platform}_client.py",
        "# Auto-generated – DO NOT EDIT",
        sdk_import,
        *extra_imports,
        "",
        "# camel→snake splitter",
        "_CAMEL_TO_SNAKE = re.compile(r'(?<!^)(?=[A-Z])')",
        "",
        f"class {platform.capitalize()}Client:",
        f'    """Thin wrapper around {platform} SDK with camel→snake fallback."""',
        "",
        "    def __init__(self, **kwargs):",
        *[f"        {l}" for l in extra_init],
        "",
        *extra_methods,
    ]
    
    # Write the file
    client_file = out_dir / f"{platform}_client.py"
    client_file.parent.mkdir(parents=True, exist_ok=True)
    client_file.write_text('\n'.join(lines) + '\n')
    
    log.info("✍  wrote %s", client_file.name)