"""
Helper functions for the platform scaffolder.
This module contains utility functions to keep the main scaffolder cleaner.
"""

import json
import logging
import re
from pathlib import Path
from typing import Dict, Any

log = logging.getLogger("scaffolder")


def write_json(p: Path, obj: Any, *, pretty: bool = False) -> None:
    """Write JSON to file with optional pretty printing."""
    p.parent.mkdir(parents=True, exist_ok=True)
    indent = 2 if pretty else None
    p.write_text(json.dumps(obj, indent=indent) + '\n')
    log.info("✍  wrote %s (%d bytes)", p.name, p.stat().st_size)


def make_python_identifier(raw: str, seen: Dict[str, int]) -> str:
    """Convert a raw string to a valid Python identifier, handling duplicates."""
    # Basic sanitization
    clean = re.sub(r"[^a-zA-Z0-9_]", "_", raw.strip())
    if clean and clean[0].isdigit():
        clean = f"fn_{clean}"
    
    # Handle duplicates
    if clean in seen:
        seen[clean] += 1
        return f"{clean}_{seen[clean]}"
    else:
        seen[clean] = 1
        return clean


def emit_org_injection(platform: str, non_body_keys: list[str], injection_config: dict) -> list[str]:
    """
    Generates the dispatcher code for parameter injection based on the
    central injection configuration dictionary.
    """
    lines: list[str] = []
    config = injection_config.get(platform.lower())
    
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


def drop_dynamic_cache(cache_root: Path) -> None:
    """Remove the dynamic cache file if it exists."""
    cache_file = cache_root / "full_schemas.json"
    if cache_file.exists():
        try:
            cache_file.unlink()
            log.info("🗑  dropped %s", cache_file.name)
        except Exception as exc:
            log.warning("could not drop cache %s: %s", cache_file, exc)