#!/usr/bin/env python3
from __future__ import annotations
##############################################################################################
## suite-cisco-ai-building-blocks/ai-building-blocks-database/scripts/generate_openapi_sdks.py
## Copyright (c) 2025 Jeff Teeter
## Cisco Systems, Inc.
## Licensed under the Apache License, Version 2.0 (see LICENSE)
## Distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND.
##############################################################################################

"""
DISCLAIMER: USE AT YOUR OWN RISK

This script lists OpenAPI v3 schema files in the source directory and invokes
openapi-python-client to generate Python SDK packages into the output directory.
After each successful generation it will also update the agent’s sdk_map.json
with the actual package directory names.
"""

import subprocess
import sys
import json
from pathlib import Path


def main() -> None:
    # --- locate all the relevant directories --------------------------------
    script_dir      = Path(__file__).resolve().parent
    db_root         = script_dir.parent                          # .../ai-building-blocks-database
    source_dir      = db_root / "source_open_api"
    output_base_dir = db_root / "output_sdk"

    # the agent’s sdk_map.json lives alongside user_commands in the ai-building-blocks-agent tree
    agent_root      = db_root.parent / "ai-building-blocks-agent"
    sdk_map_file    = agent_root / "app" / "llm" / "sdk_map.json"

    # ensure our output dir exists
    output_base_dir.mkdir(parents=True, exist_ok=True)

    # load or initialize SDK map
    if sdk_map_file.exists():
        sdk_map = json.loads(sdk_map_file.read_text(encoding="utf-8"))
    else:
        sdk_map = {}

    # --- gather all OpenAPI files -------------------------------------------
    openapi_files = sorted(
        p for p in source_dir.iterdir()
        if p.is_file() and p.suffix.lower() in {".json", ".yaml", ".yml"}
    )
    if not openapi_files:
        print(f"No OpenAPI files found in {source_dir}", file=sys.stderr)
        sys.exit(1)

    # --- user picks one or all -----------------------------------------------
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

    # --- generate and map each one ------------------------------------------
    added_mappings: list[str] = []
    for spec in selected:
        default_name = spec.stem
        user_input   = input(f"Enter SDK folder name [{default_name}]: ").strip()
        sdk_name     = user_input or default_name

        dest_dir = output_base_dir / sdk_name
        dest_dir.mkdir(parents=True, exist_ok=True)

        print(f"\n🔧 Generating SDK for '{spec.name}' → '{dest_dir}'")
        cmd = [
            "openapi-python-client",
            "generate",
            "--path", str(spec),
            "--output-path", str(dest_dir),
            "--meta", "poetry",
            "--overwrite"
        ]
        result = subprocess.run(cmd)
        if result.returncode != 0:
            print(f"❌ Failed for {spec.name}; see details above.", file=sys.stderr)
            continue

        # detect actual Python package directory inside the generated SDK
        pkg_dir = next(
            (d.name for d in dest_dir.iterdir()
             if d.is_dir() and (d / "__init__.py").exists()),
            sdk_name
        )
        print(f"✅ Successfully generated SDK at: {dest_dir} (package '{pkg_dir}')")

        # update sdk_map.json if new
        if sdk_name not in sdk_map or sdk_map[sdk_name] != pkg_dir:
            sdk_map[sdk_name] = pkg_dir
            added_mappings.append(f"{sdk_name} → {pkg_dir}")

    # --- persist any changes to sdk_map.json --------------------------------
    if added_mappings:
        sdk_map_file.parent.mkdir(parents=True, exist_ok=True)
        sdk_map_file.write_text(json.dumps(sdk_map, indent=2), encoding="utf-8")
        print("\n🗺️  Updated SDK map with:")
        for mapping in added_mappings:
            print(f"  {mapping}")

    print("\nAll done. Your SDKs live under:")
    print(f"  {output_base_dir}")


if __name__ == "__main__":
    main()
