#!/usr/bin/env python3
"""
Test if the scaffolder properly adds date defaults to getActiveAlarms
"""
import subprocess
import sys

# Run scaffolder for sdwan_mngr
print("Running scaffolder for sdwan_mngr...")
result = subprocess.run([
    sys.executable, 
    "src/scripts/platform_scaffolder.py",
    "--platform", "sdwan_mngr",
    "--sdk-module", "catalystwan", 
    "--openapi-spec", "src/app/llm/openapi_specs/full_sdwan_mngr.json"
], capture_output=True, text=True)

if result.returncode != 0:
    print(f"Scaffolder failed: {result.stderr}")
    sys.exit(1)

# Check if the dispatcher has our customization
print("\nChecking if getActiveAlarms has date defaults...")
with open("src/app/llm/function_dispatcher/sdwan_mngr_dispatcher.py", "r") as f:
    content = f.read()
    
# Look for our customization
if "from datetime import datetime, timedelta" in content:
    print("✓ Import found")
else:
    print("✗ Import NOT found")
    
if "If no dates provided, default to last 24 hours" in content:
    print("✓ Date default logic found")
    
    # Find and print the getActiveAlarms function
    import re
    match = re.search(r'def getActiveAlarms.*?(?=\n@register|\ndef|\Z)', content, re.DOTALL)
    if match:
        print("\ngetActiveAlarms function:")
        print("-" * 50)
        print(match.group(0))
        print("-" * 50)
else:
    print("✗ Date default logic NOT found")