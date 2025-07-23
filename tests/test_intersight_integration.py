#!/usr/bin/env python3
"""
Integration test for Intersight natural language queries.
Tests the full pipeline from natural language to function execution.

Usage:
    python tests/test_intersight_integration.py
"""

import sys
import os
from pathlib import Path
import json
import argparse

# Add the src directory to the path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from app.llm.dynamic import build_functions_for_llm
from app.llm.function_dispatcher import dispatch_function_call

# Import for testing without actual API calls
from unittest.mock import MagicMock, patch


def test_function_selection(query: str, expected_functions: list[str]):
    """Test that natural language queries select the correct functions."""
    print(f"\n{'='*60}")
    print(f"Testing query: '{query}'")
    print(f"Expected functions: {expected_functions}")
    print('-'*60)
    
    # Build functions for LLM
    functions = build_functions_for_llm(query, ["intersight"], k=10)
    
    if not functions:
        print("❌ No functions returned!")
        return False
    
    # Extract function names
    function_names = [f.get('name', 'Unknown') for f in functions]
    print(f"Top 5 functions returned: {function_names[:5]}")
    
    # Check if expected functions are in the results
    success = True
    for expected in expected_functions:
        if expected in function_names[:5]:  # Check top 5
            print(f"✅ Found expected function: {expected}")
        else:
            print(f"❌ Missing expected function: {expected}")
            success = False
    
    # Display the top function's description
    if functions:
        top_func = functions[0]
        print(f"\nTop function details:")
        print(f"  Name: {top_func.get('name')}")
        print(f"  Description: {top_func.get('description', 'No description')[:100]}...")
    
    return success


def test_dispatcher_resolution(function_name: str, snake_case_name: str):
    """Test that the dispatcher can resolve function names correctly."""
    print(f"\n{'='*60}")
    print(f"Testing dispatcher resolution")
    print(f"Function: {function_name} -> {snake_case_name}")
    print('-'*60)
    
    try:
        # Import the dispatcher module to check if function is registered
        from app.llm.function_dispatcher import _registry
        
        if function_name in _registry:
            print(f"✅ Function '{function_name}' is registered in dispatcher")
            
            # Test if it can handle snake_case call
            with patch('app.llm.platform_clients.intersight_client.IntersightClient') as mock_client:
                # Mock the client method
                mock_instance = MagicMock()
                mock_method = MagicMock(return_value={"success": True, "data": "mocked"})
                setattr(mock_instance, snake_case_name, mock_method)
                mock_client.return_value = mock_instance
                
                # Test dispatch with snake_case
                try:
                    result = dispatch_function_call(snake_case_name, {})
                    print(f"✅ Dispatcher successfully resolved snake_case: {snake_case_name}")
                    return True
                except Exception as e:
                    print(f"❌ Dispatcher failed to resolve snake_case: {e}")
                    return False
        else:
            print(f"❌ Function '{function_name}' not found in dispatcher registry")
            return False
            
    except Exception as e:
        print(f"❌ Error testing dispatcher: {e}")
        return False


def test_intersight_pipeline():
    """Test the complete pipeline for Intersight natural language queries."""
    print("\nTesting Intersight Natural Language Pipeline")
    print("="*80)
    
    # Test cases
    test_cases = [
        {
            "query": "list servers",
            "expected_functions": ["GetComputePhysicalSummaryList"],
            "dispatcher_function": "GetComputePhysicalSummaryList",
            "snake_case": "get_compute_physical_summary_list"
        },
        {
            "query": "show intersight users",
            "expected_functions": ["GetIamUserList"],
            "dispatcher_function": "GetIamUserList", 
            "snake_case": "get_iam_user_list"
        }
    ]
    
    all_passed = True
    
    for test in test_cases:
        print(f"\n{'#'*80}")
        print(f"# Test Case: {test['query']}")
        print(f"{'#'*80}")
        
        # Test 1: Function Selection
        if test_function_selection(test["query"], test["expected_functions"]):
            print("✅ Function selection test passed")
        else:
            print("❌ Function selection test failed")
            all_passed = False
        
        # Test 2: Dispatcher Resolution
        if test_dispatcher_resolution(test["dispatcher_function"], test["snake_case"]):
            print("✅ Dispatcher resolution test passed")
        else:
            print("❌ Dispatcher resolution test failed")
            all_passed = False
    
    # Summary
    print(f"\n{'='*80}")
    print("Test Summary")
    print(f"{'='*80}")
    if all_passed:
        print("✅ All tests passed!")
    else:
        print("❌ Some tests failed")
    
    return all_passed


def test_with_real_api():
    """Test with real API calls (requires valid Intersight credentials)."""
    print("\nTesting with Real API (requires credentials)")
    print("="*80)
    
    # Check if credentials are available
    api_key = os.getenv('INTERSIGHT_API_KEY')
    api_secret = os.getenv('INTERSIGHT_API_SECRET')
    
    if not api_key or not api_secret:
        print("⚠️  Skipping real API tests - no credentials found")
        print("   Set INTERSIGHT_API_KEY and INTERSIGHT_API_SECRET to test with real API")
        return
    
    print("✅ Credentials found - testing with real API")
    
    try:
        # Test list servers
        print("\nTesting 'list servers' with real API...")
        result = dispatch_function_call("GetComputePhysicalSummaryList", {})
        if result:
            print(f"✅ Successfully called API - returned {len(result.get('Results', []))} servers")
        else:
            print("❌ API call returned no results")
            
    except Exception as e:
        print(f"❌ Real API test failed: {e}")


def main():
    parser = argparse.ArgumentParser(description="Test Intersight natural language integration")
    parser.add_argument("--real-api", action="store_true", help="Test with real API calls")
    parser.add_argument("--query", help="Test a specific query")
    args = parser.parse_args()
    
    if args.query:
        # Test a specific query
        test_function_selection(args.query, [])
    else:
        # Run all tests
        test_intersight_pipeline()
        
        if args.real_api:
            test_with_real_api()


if __name__ == "__main__":
    main()