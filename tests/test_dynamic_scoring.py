#!/usr/bin/env python3
"""
Test the enhanced semantic scoring in dynamic.py
"""

import sys
from pathlib import Path

# Add the src directory to the path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from app.llm.dynamic import calculate_function_score, extract_query_intent, SEMANTIC_MAPPINGS

def test_scoring():
    """Test various query scenarios with the new scoring."""
    
    test_cases = [
        # (query, platform, function_name, expected_min_score)
        ("list servers", "intersight", "GetComputePhysicalSummaryList", 400),
        ("list servers", "intersight", "GetServerProfileList", 50),
        ("list servers", "intersight", "GetKvmPolicyList", 10),
        ("show interfaces", "catalyst", "getAllInterfaces", 300),
        ("show interfaces", "catalyst", "getInterfaceDetails", 100),
        ("get all devices", "sdwan_mngr", "getAllDeviceStatus", 300),
        ("get all devices", "sdwan_mngr", "listAllDevices", 10),
        ("network health", "catalyst", "getOverallNetworkHealth", 200),
        ("user accounts", "intersight", "GetIamUserList", 200),
    ]
    
    print("Testing Enhanced Semantic Scoring")
    print("=" * 80)
    
    for query, platform, func_name, expected_min in test_cases:
        score = calculate_function_score(func_name, platform, query, False)
        primary_target, _ = extract_query_intent(query)
        
        status = "✓" if score >= expected_min else "✗"
        print(f"{status} Query: '{query}' | Function: {func_name}")
        print(f"  Platform: {platform} | Score: {score} | Expected: >={expected_min}")
        print(f"  Semantic target: '{primary_target}'")
        
        if score < expected_min:
            print(f"  WARNING: Score {score} is below expected minimum {expected_min}")
        print()


def test_semantic_mappings():
    """Test that semantic mappings are working correctly."""
    print("\nTesting Semantic Intent Extraction")
    print("=" * 80)
    
    queries = [
        "list servers",
        "show all devices",
        "get network interfaces",
        "user list",
        "health status",
        "inventory report",
        "alerts and notifications",
    ]
    
    for query in queries:
        primary_target, words = extract_query_intent(query)
        print(f"Query: '{query}'")
        print(f"  Primary target: '{primary_target}'")
        if primary_target and primary_target in SEMANTIC_MAPPINGS:
            config = SEMANTIC_MAPPINGS[primary_target]
            print(f"  Primary functions: {', '.join(config['primary_functions'][:3])}")
        print()


if __name__ == "__main__":
    test_scoring()
    test_semantic_mappings()