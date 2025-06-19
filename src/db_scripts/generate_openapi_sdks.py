#!/usr/bin/env python3
from __future__ import annotations
##############################################################################################
## suite-cisco-ai-building-blocks/src/db_scripts/scripts/generate_openapi_sdks.py
## Copyright (c) 2025 Jeff Teeter
## Cisco Systems, Inc.
## Licensed under the Apache License, Version 2.0 (see LICENSE)
## Distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND.
##############################################################################################

""" DISCLAIMER: USE AT YOUR OWN RISK

This script lists OpenAPI v3 schema files in the source directory and invokes
openapi-python-client to generate Python SDK packages into the output directory.
After each successful generation it will also update the platform_registry.json
with the sdk_module and mark the SDK as created_by_us.
"""

import subprocess
import sys
import json
import re
import shutil
from pathlib import Path
import tomllib

PROJECT_ROOT = Path(__file__).resolve().parents[2]
SOURCE_DIR = PROJECT_ROOT / "src" / "source_open_api"
OUTPUT_BASE_DIR = PROJECT_ROOT / "src" / "db_scripts" / "output_sdk"
PLATFORM_REGISTRY_FILE = PROJECT_ROOT / "src" / "app" / "llm" / "platform_registry.json"

def load_registry() -> dict:
    if PLATFORM_REGISTRY_FILE.exists():
        try:
            return json.loads(PLATFORM_REGISTRY_FILE.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            print(f"Warning: failed to parse {PLATFORM_REGISTRY_FILE}, starting fresh", file=sys.stderr)
    return {}

def save_registry(registry: dict) -> None:
    PLATFORM_REGISTRY_FILE.parent.mkdir(parents=True, exist_ok=True)
    PLATFORM_REGISTRY_FILE.write_text(json.dumps(registry, indent=2), encoding="utf-8")

def parse_package_dir(dest_dir: Path, fallback: str) -> str:
    pyproject = dest_dir / "pyproject.toml"
    if pyproject.exists():
        try:
            data = tomllib.loads(pyproject.read_text(encoding="utf-8"))
            name = data.get("project", {}).get("name") or data.get("tool", {}).get("poetry", {}).get("name")
            if name:
                return name.replace("-", "_")
        except Exception:
            pass
    return fallback

def _sanitize_version(version: str) -> str:
    match = re.match(
        r"(?P<base>[0-9]+(?:\.[0-9]+)*)-Rev\.(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})\.(?P<build>\d+)",
        version
    )
    if match:
        base = match.group("base")
        return f"{base}.post{match.group('year')}.{match.group('month')}.{match.group('day')}.{match.group('build')}"
    return re.sub(r"[^0-9A-Za-z.]+", ".", version)

def sanitize_pyproject_version(pyproject: Path) -> None:
    if not pyproject.exists():
        return
    data = tomllib.loads(pyproject.read_text(encoding="utf-8"))
    poetry_table = data.get("tool", {}).get("poetry")
    if not poetry_table or "version" not in poetry_table:
        return
    original = poetry_table["version"]
    sanitized = _sanitize_version(original)
    if sanitized != original:
        text = pyproject.read_text(encoding="utf-8")
        text = text.replace(f'version = "{original}"', f'version = "{sanitized}"')
        pyproject.write_text(text, encoding="utf-8")

def main() -> None:
    # Ensure output directory exists
    OUTPUT_BASE_DIR.mkdir(parents=True, exist_ok=True)
    registry = load_registry()

    # Gather OpenAPI files
    openapi_files = sorted(
        p for p in SOURCE_DIR.iterdir()
        if p.is_file() and p.suffix.lower() in {".json", ".yaml", ".yml"}
    )
    if not openapi_files:
        print(f"No OpenAPI files found in {SOURCE_DIR}", file=sys.stderr)
        sys.exit(1)

    # User selection
    print("Available OpenAPI schema files:")
    for idx, path in enumerate(openapi_files, start=1):
        print(f"  {idx}. {path.name}")
    print(f"  0. Generate SDK for ALL files")

    choice = input(f"Select [0-{len(openapi_files)}]: ").strip()
    if choice == "0":
        selected = openapi_files
    else:
        try:
            i = int(choice)
            if not (1 <= i <= len(openapi_files)):
                raise ValueError
            selected = [openapi_files[i-1]]
        except ValueError:
            print("Invalid selection.", file=sys.stderr)
            sys.exit(1)

    updated_entries: list[str] = []
    for spec in selected:
        # Suggest short name if present in registry
        default_short = next((k for k, v in registry.items() if v.get("openapi_name") == spec.stem), None)
        default_name = default_short or spec.stem
        user_input = input(f"Enter SDK folder name [{default_name}]: ").strip()
        sdk_name = user_input or default_name

        dest_dir = OUTPUT_BASE_DIR / sdk_name
        dest_dir.mkdir(parents=True, exist_ok=True)

        # Generate SDK
        print(f"\n🔧 Generating SDK for '{spec.name}' → '{dest_dir}'")
        cmd = [
            "openapi-python-client", "generate",
            "--path", str(spec),
            "--output-path", str(dest_dir),
            "--meta", "poetry", "--overwrite"
        ]
        result = subprocess.run(cmd)
        if result.returncode != 0:
            print(f"❌ Failed for {spec.name}; see details above.", file=sys.stderr)
            continue

        # Sanitize version and detect package
        sanitize_pyproject_version(dest_dir / "pyproject.toml")
        pkg_dir = parse_package_dir(dest_dir, sdk_name)
        print(f"✅ Successfully generated SDK at: {dest_dir} (package '{pkg_dir}')")

        # Ensure api/ package
        api_dir = dest_dir / pkg_dir / "api"
        if not api_dir.exists():
            alt_tags = dest_dir / pkg_dir / "apis" / "tags"
            if alt_tags.exists():
                print("⚠️  consolidating 'apis/tags' into 'api/'")
                api_dir.mkdir(parents=True, exist_ok=True)
                for f in alt_tags.glob("*.py"):
                    shutil.copy(f, api_dir / f.name)
                (api_dir / "__init__.py").write_text("# auto-generated\n", encoding="utf-8")
            else:
                print(f"❌ Missing api/ in SDK '{pkg_dir}'", file=sys.stderr)
                continue
        if not list(api_dir.glob("*.py")):
            print(f"❌ '{pkg_dir}.api' is empty", file=sys.stderr)
            continue

        # Update registry entry
        entry = registry.setdefault(sdk_name, {})
        entry["openapi_name"] = spec.stem
        entry["sdk_module"] = pkg_dir
        entry["created_by_us"] = True
        updated_entries.append(f"{sdk_name} → {pkg_dir}")

    # Persist registry changes
    if updated_entries:
        save_registry(registry)
        print("\n🌐 Updated platform_registry.json with:")
        for m in updated_entries:
            print(f"  {m}")

    print(f"\nAll done. Your SDKs live under: {OUTPUT_BASE_DIR}")

if __name__ == "__main__":
    main()
