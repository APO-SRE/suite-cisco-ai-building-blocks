#!/usr/bin/env python3
"""
Test the enhanced build_functions_for_llm function with natural language queries.
"""

import sys
from pathlib import Path

# Add the src directory to the path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from app.llm.dynamic import build_functions_for_llm

def test_natural_language_queries():
    """Test various natural language queries to ensure proper function selection."""
    
    test_cases = [
        {
            "query": "list servers",
            "platforms": ["intersight"],
            "expected_top": "GetComputePhysicalSummaryList",
            "description": "Natural language: list servers"
        },
        {
            "query": "show all servers",
            "platforms": ["intersight"],
            "expected_top": "GetComputePhysicalSummaryList",
            "description": "Natural language: show all servers"
        },
        {
            "query": "GetComputePhysicalSummaryList",
            "platforms": ["intersight"],
            "expected_top": "GetComputePhysicalSummaryList",
            "description": "Exact function name"
        },
        {
            "query": "get server inventory",
            "platforms": ["intersight"],
            "expected_top": "GetComputePhysicalSummaryList",
            "description": "Natural language: server inventory"
        },
        {
            "query": "list all devices",
            "platforms": ["meraki", "catalyst", "sdwan_mngr"],
            "expected_contains": ["getDeviceList", "getAllDeviceStatus", "getOrganizationDevices"],
            "description": "Natural language: list all devices (multi-platform)"
        },
        {
            "query": "network health status",
            "platforms": ["catalyst"],
            "expected_contains": ["getOverallNetworkHealth", "getSiteHealth"],
            "description": "Natural language: network health"
        }
    ]
    
    print("Testing enhanced build_functions_for_llm with natural language queries\n")
    print("=" * 80)
    
    for test in test_cases:
        print(f"\nTest: {test['description']}")
        print(f"Query: '{test['query']}'")
        print(f"Platforms: {test['platforms']}")
        
        try:
            # Call the enhanced function
            functions = build_functions_for_llm(
                test['query'], 
                test['platforms'],
                k=10  # Get top 10 for testing
            )
            
            if not functions:
                print("❌ No functions returned!")
                continue
            
            # Check results
            function_names = [f.get('name', 'Unknown') for f in functions]
            print(f"Top 5 results: {function_names[:5]}")
            
            # Verify expected results
            if 'expected_top' in test:
                if functions[0].get('name') == test['expected_top']:
                    print(f"✅ Expected top function found: {test['expected_top']}")
                else:
                    print(f"❌ Expected {test['expected_top']} as top result, got {functions[0].get('name')}")
            
            if 'expected_contains' in test:
                found = [name for name in test['expected_contains'] if name in function_names[:10]]
                if found:
                    print(f"✅ Found expected functions: {found}")
                else:
                    print(f"❌ None of the expected functions found in top 10")
            
            # Show enhanced descriptions for top results
            print("\nTop 3 function descriptions:")
            for i, func in enumerate(functions[:3], 1):
                desc = func.get('description', 'No description')[:100]
                print(f"  {i}. {func.get('name')}: {desc}...")
                
        except Exception as e:
            print(f"❌ Error: {str(e)}")
            import traceback
            traceback.print_exc()
        
        print("-" * 80)


if __name__ == "__main__":
    test_natural_language_queries()