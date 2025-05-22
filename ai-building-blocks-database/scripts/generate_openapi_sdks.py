#!/usr/bin/env python3
from __future__ import annotations
################################################################################
## suite-cisco-ai-building-blocks/ai-building-blocks-database/scripts/generate_openapi_sdks.py
## Copyright (c) 2025 Jeff Teeter
## Cisco Systems, Inc.
## Licensed under the Apache License, Version 2.0 (see LICENSE)
## Distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND.
################################################################################

"""
DISCLAIMER: USE AT YOUR OWN RISK

This script lists OpenAPI v3 schema files in the source directory and invokes
openapi-python-client to generate Python SDK packages into the output directory.
You can choose one file or enter "0" to generate for all files, and for each
selection you may enter a custom SDK folder name (defaulting to the JSON stem).
"""

import subprocess
import sys
from pathlib import Path


def main() -> None:
    # Determine project directories
    script_dir = Path(__file__).resolve().parent
    project_dir = script_dir.parent
    source_dir = project_dir / "source_open_api"
    output_base_dir = project_dir / "output_sdk"

    # Ensure base output dir exists
    output_base_dir.mkdir(parents=True, exist_ok=True)

    # Gather OpenAPI files
    openapi_files = sorted(
        p for p in source_dir.iterdir()
        if p.is_file() and p.suffix.lower() in {".json", ".yaml", ".yml"}
    )

    if not openapi_files:
        print(f"No OpenAPI files found in {source_dir}", file=sys.stderr)
        sys.exit(1)

    # Display choices
    print("Available OpenAPI schema files:")
    for idx, path in enumerate(openapi_files, start=1):
        print(f"  {idx}. {path.name}")
    print("  0. Generate SDK for ALL files")

    # User selection
    choice = input(f"Select [0-{len(openapi_files)}]: ").strip()
    if choice == "0":
        selected_files = openapi_files
    else:
        try:
            i = int(choice)
            if not (1 <= i <= len(openapi_files)):
                raise ValueError
            selected_files = [openapi_files[i - 1]]
        except ValueError:
            print("Invalid selection.", file=sys.stderr)
            sys.exit(1)

    # Process each selected file
    for spec in selected_files:
        # Prompt for custom SDK directory name
        default_name = spec.stem
        user_input = input(f"Enter SDK folder name [{default_name}]: ").strip()
        sdk_name = user_input if user_input else default_name

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
        else:
            print(f"✅ Successfully generated SDK at: {dest_dir}")

    print("\nAll done. Your SDKs live under:")
    print(f"  {output_base_dir}")


if __name__ == "__main__":
    main()
