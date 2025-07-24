#!/usr/bin/env python3
"""Test coverage report generation with HTTP method breakdown"""
import sys
sys.path.insert(0, '.')
import json
from pathlib import Path

# Test with existing coverage files
coverage_dir = Path("app/llm/sdk_coverage")

print("Checking existing coverage reports...")
for coverage_file in coverage_dir.glob("*_coverage.json"):
    print(f"\n{coverage_file.name}:")
    with open(coverage_file) as f:
        data = json.load(f)
    
    # Check basic fields
    print(f"  Platform: {data.get('platform')}")
    print(f"  Total operations: {data.get('total_operations')}")
    print(f"  Coverage: {data.get('coverage_percentage', 0):.1f}%")
    
    # Check if HTTP method breakdown exists
    if 'http_method_breakdown' in data:
        print("  HTTP method breakdown:")
        for method, count in sorted(data['http_method_breakdown'].items()):
            print(f"    {method}: {count}")
    else:
        print("  ⚠️  No HTTP method breakdown found")

print("\n\nTo test the new functionality, re-run the scaffolder for any platform:")
print("python3 scripts/platform_scaffolder.py --platform sdwan_mngr --include-http-methods GET")
print("\nThen check the generated coverage file at:")
print("app/llm/sdk_coverage/sdwan_mngr_coverage.json")