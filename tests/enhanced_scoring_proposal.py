"""
Enhanced scoring function proposal for dynamic.py

This approach focuses on semantic relevance rather than simple keyword matching.
"""

import re
from typing import Dict, List, Tuple, Set


# Semantic mappings for common query patterns
SEMANTIC_MAPPINGS = {
    # What the user asks for -> what functions should match
    "servers": {
        "boost_terms": ["server", "compute", "physical", "rack", "blade", "node"],
        "avoid_terms": ["profile", "policy", "setting", "disruption"],
        "primary_functions": ["GetComputePhysicalSummaryList", "GetComputeRackUnitList", "GetComputeBladeList"]
    },
    "devices": {
        "boost_terms": ["device", "equipment", "hardware", "network"],
        "avoid_terms": ["template", "policy", "config"],
        "primary_functions": ["getDeviceList", "getAllDeviceStatus", "getOrganizationDevices"]
    },
    "interfaces": {
        "boost_terms": ["interface", "port", "ethernet", "adapter"],
        "avoid_terms": ["policy", "template"],
        "primary_functions": ["getAllInterfaces", "getInterfaces"]
    },
    "users": {
        "boost_terms": ["user", "account", "identity"],
        "avoid_terms": ["policy", "setting"],
        "primary_functions": ["getUsers", "getUserList"]
    },
    "alerts": {
        "boost_terms": ["alert", "alarm", "notification", "event"],
        "avoid_terms": ["policy", "template"],
        "primary_functions": ["GetCondAlarmList", "getSecurityAlerts"]
    },
    "networks": {
        "boost_terms": ["network", "vlan", "subnet", "fabric"],
        "avoid_terms": ["policy"],
        "primary_functions": ["getNetworks", "getNetworkList"]
    }
}


def extract_query_intent(query: str) -> Tuple[str, Set[str]]:
    """
    Extract the primary intent and relevant terms from a query.
    Returns: (primary_target, relevant_terms)
    """
    query_lower = query.lower()
    words = set(query_lower.split())
    
    # Find the primary target (what the user wants)
    primary_target = None
    for target, config in SEMANTIC_MAPPINGS.items():
        if target in query_lower:
            primary_target = target
            break
        # Check if any boost terms are in the query
        for term in config["boost_terms"]:
            if term in query_lower:
                primary_target = target
                break
        if primary_target:
            break
    
    return primary_target, words


def calculate_semantic_score(
    func_name: str,
    platform: str,
    query: str,
    base_priority: int,
    is_lexical_match: bool = False
) -> float:
    """
    Enhanced scoring that considers semantic relevance.
    """
    score = base_priority
    func_name_lower = func_name.lower()
    query_lower = query.lower()
    
    # Extract query intent
    primary_target, query_words = extract_query_intent(query)
    
    # Apply semantic scoring if we identified a target
    if primary_target and primary_target in SEMANTIC_MAPPINGS:
        config = SEMANTIC_MAPPINGS[primary_target]
        
        # Huge boost for primary functions
        if func_name in config["primary_functions"]:
            score += 200
        
        # Boost for matching semantic terms
        for boost_term in config["boost_terms"]:
            if boost_term in func_name_lower:
                score += 50
        
        # Penalty for avoid terms (unless explicitly requested)
        for avoid_term in config["avoid_terms"]:
            if avoid_term in func_name_lower and avoid_term not in query_lower:
                score -= 40
    
    # Multi-word matching bonus
    # Count how many query words appear in the function name
    func_words = set(re.findall(r'[a-z]+', func_name_lower))
    common_words = query_words & func_words
    
    # Filter out common words that don't add meaning
    meaningful_words = common_words - {'get', 'list', 'show', 'all', 'the', 'a', 'an'}
    if len(meaningful_words) >= 2:
        score += len(meaningful_words) * 30
    
    # Lexical match gets moderate boost (not huge)
    if is_lexical_match:
        score += 15  # Reduced from 25
    
    # Platform-specific adjustments
    if platform == "intersight":
        if primary_target == "servers":
            if "physical" in func_name_lower and "summary" in func_name_lower:
                score += 100  # Extra boost for the primary server function
            elif "profile" in func_name_lower and "server" not in query_lower:
                score -= 50  # Penalty for profile functions unless requested
    
    elif platform == "catalyst":
        if primary_target == "interfaces":
            if func_name == "getAllInterfaces":
                score += 100
            elif func_name == "getInterfaces":
                score += 50
    
    elif platform == "sdwan_mngr":
        if primary_target == "devices":
            if func_name == "getAllDeviceStatus":
                score += 100
            elif func_name in ["listAllDevices", "getDevicesList"]:
                score -= 50  # Deprecated/confusing functions
    
    return max(0, score)


# Example of how this would be integrated into dynamic.py:
"""
def calculate_function_score(
    func_name: str,
    platform: str,
    query: str,
    is_lexical_match: bool = False
) -> float:
    # Get base priority from configuration
    platform_priorities = FUNCTION_PRIORITIES.get(platform, {})
    base_score = platform_priorities.get(func_name, 50)
    
    # Use semantic scoring
    return calculate_semantic_score(
        func_name,
        platform,
        query,
        base_score,
        is_lexical_match
    )
"""

# Test the enhanced scoring
if __name__ == "__main__":
    test_cases = [
        # (function_name, platform, query, base_priority)
        ("GetComputePhysicalSummaryList", "intersight", "list servers", 100),
        ("GetServerProfileList", "intersight", "list servers", 40),
        ("GetKvmPolicyList", "intersight", "list servers", 50),
        ("getAllInterfaces", "catalyst", "show interfaces", 90),
        ("getInterfaceDetails", "catalyst", "show interfaces", 50),
        ("getAllDeviceStatus", "sdwan_mngr", "get all devices", 95),
        ("listAllDevices", "sdwan_mngr", "get all devices", 10),
    ]
    
    print("Enhanced Semantic Scoring Results:")
    print("=" * 80)
    
    for func_name, platform, query, base_priority in test_cases:
        score = calculate_semantic_score(func_name, platform, query, base_priority)
        print(f"Query: '{query}' | Function: {func_name}")
        print(f"  Platform: {platform} | Base: {base_priority} | Final Score: {score}")
        print()