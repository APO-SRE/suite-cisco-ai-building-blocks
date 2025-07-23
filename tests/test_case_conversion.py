#!/usr/bin/env python3
"""
Test case conversion in the function dispatcher.
"""

import sys
from pathlib import Path

# Add the src directory to the path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

def test_case_conversions():
    """Test various case conversions."""
    
    test_cases = [
        ("get_compute_physical_summary_list", "GetComputePhysicalSummaryList"),
        ("get_compute_rack_unit_list", "GetComputeRackUnitList"),
        ("get_device_list", "GetDeviceList"),
        ("get_all_interfaces", "GetAllInterfaces"),
        ("list_servers", "ListServers"),
        ("getAllDeviceStatus", "GetAllDeviceStatus"),  # Already camelCase
    ]
    
    print("Testing case conversions:")
    print("=" * 60)
    
    for snake_case, expected_pascal in test_cases:
        # Convert snake_case to PascalCase
        pascal_name = ''.join(word.capitalize() for word in snake_case.split('_'))
        
        print(f"Input: {snake_case:40} -> {pascal_name}")
        if pascal_name == expected_pascal:
            print(f"✅ Correct: {expected_pascal}")
        else:
            print(f"❌ Expected: {expected_pascal}, Got: {pascal_name}")
        print("-" * 60)


def test_dispatcher_conversion():
    """Test the actual dispatcher with mock functions."""
    from app.llm.function_dispatcher import dispatch_function_call, register, _registry
    
    # Register a test function with PascalCase
    @register("GetTestFunction")
    def get_test_function(**kwargs):
        return {"success": True, "function": "GetTestFunction", "args": kwargs}
    
    print("\nTesting dispatcher conversion:")
    print("=" * 60)
    
    # Test 1: Direct PascalCase call
    try:
        result = dispatch_function_call("GetTestFunction", {"param": "value"})
        print("✅ Direct PascalCase call succeeded:", result)
    except Exception as e:
        print("❌ Direct PascalCase call failed:", e)
    
    # Test 2: snake_case call (should be converted)
    try:
        result = dispatch_function_call("get_test_function", {"param": "value"})
        print("✅ snake_case conversion succeeded:", result)
    except Exception as e:
        print("❌ snake_case conversion failed:", e)
    
    # Test 3: Check registry contents
    print("\nRegistry contents:")
    for key in sorted(_registry.keys()):
        if "Test" in key:
            print(f"  - {key}")


if __name__ == "__main__":
    test_case_conversions()
    test_dispatcher_conversion()