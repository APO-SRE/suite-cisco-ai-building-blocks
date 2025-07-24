#!/usr/bin/env python3
"""Test that other platform SDK introspection still works"""
import sys
sys.path.insert(0, '.')

from app.utils.sdk_introspection import SDKIntrospector

def test_platform(platform, sdk_module):
    print(f"\nTesting {platform} ({sdk_module})...")
    try:
        introspector = SDKIntrospector(platform, sdk_module)
        print(f"  Pattern detected: {introspector.sdk_pattern}")
        methods = introspector.discover_methods()
        print(f"  Methods discovered: {len(methods)}")
        return True
    except Exception as e:
        print(f"  ERROR: {e}")
        return False

def main():
    # Test a few common platforms to ensure they still work
    platforms = [
        ('meraki', 'meraki'),
        ('catalyst_center', 'dnacentersdk'),
        ('intersight', 'intersight'),
    ]
    
    all_passed = True
    for platform, sdk_module in platforms:
        if not test_platform(platform, sdk_module):
            all_passed = False
    
    print(f"\nAll tests {'PASSED' if all_passed else 'FAILED'}")
    return all_passed

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)