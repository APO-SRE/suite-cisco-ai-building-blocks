#!/usr/bin/env python3
"""
Test and develop a semantic scoring system for function selection.
This helps understand how to better match user intent with function names.

Usage:
    python tests/test_semantic_scoring.py "list servers"
    python tests/test_semantic_scoring.py "get all devices"
    python tests/test_semantic_scoring.py "show network interfaces"
"""

import argparse
import re
from typing import Dict, List, Tuple, Set
from collections import defaultdict
import json

# Common action verbs and their synonyms
ACTION_VERBS = {
    "list": ["list", "show", "get", "retrieve", "display", "enumerate"],
    "create": ["create", "add", "new", "make", "provision"],
    "update": ["update", "modify", "change", "edit", "patch"],
    "delete": ["delete", "remove", "destroy", "terminate"],
    "search": ["search", "find", "lookup", "query"],
}

# Domain-specific noun mappings
NOUN_MAPPINGS = {
    "servers": {
        "primary": ["server", "compute", "physical", "node", "machine", "host"],
        "secondary": ["rack", "blade", "chassis"],
        "avoid": ["profile", "policy", "disruption", "setting", "config"]
    },
    "devices": {
        "primary": ["device", "equipment", "hardware"],
        "secondary": ["network", "endpoint", "controller"],
        "avoid": ["template", "config", "policy"]
    },
    "interfaces": {
        "primary": ["interface", "port", "nic", "adapter"],
        "secondary": ["network", "ethernet", "vnic"],
        "avoid": ["policy", "template", "profile"]
    },
    "users": {
        "primary": ["user", "account", "identity", "person"],
        "secondary": ["group", "role", "permission"],
        "avoid": ["policy", "setting", "config"]
    },
    "networks": {
        "primary": ["network", "vlan", "subnet", "vpc"],
        "secondary": ["fabric", "segment", "zone"],
        "avoid": ["policy", "template"]
    }
}


class SemanticScorer:
    """Score functions based on semantic relevance to the query."""
    
    def __init__(self):
        self.noun_cache = self._build_noun_cache()
        
    def _build_noun_cache(self) -> Dict[str, str]:
        """Build reverse mapping from terms to primary nouns."""
        cache = {}
        for primary_noun, terms in NOUN_MAPPINGS.items():
            for term in terms["primary"] + terms["secondary"]:
                cache[term.lower()] = primary_noun
        return cache
    
    def extract_intent(self, query: str) -> Tuple[str, str, List[str]]:
        """
        Extract the action verb and target noun from a query.
        Returns: (action, primary_noun, all_relevant_terms)
        """
        query_lower = query.lower()
        tokens = query_lower.split()
        
        # Find action verb
        action = None
        for token in tokens:
            for action_type, synonyms in ACTION_VERBS.items():
                if token in synonyms:
                    action = action_type
                    break
            if action:
                break
        
        # Find primary noun
        primary_noun = None
        relevant_terms = []
        
        for token in tokens:
            if token in self.noun_cache:
                primary_noun = self.noun_cache[token]
                if primary_noun in NOUN_MAPPINGS:
                    relevant_terms = NOUN_MAPPINGS[primary_noun]["primary"]
                break
        
        # If no primary noun found, look for any matching terms
        if not primary_noun:
            for noun, terms in NOUN_MAPPINGS.items():
                for term in terms["primary"]:
                    if term in query_lower:
                        primary_noun = noun
                        relevant_terms = terms["primary"]
                        break
                if primary_noun:
                    break
        
        return action or "get", primary_noun or "", relevant_terms
    
    def score_function(self, function_name: str, query: str, 
                      base_priority: int = 50) -> Tuple[int, Dict[str, any]]:
        """
        Score a function based on semantic relevance to the query.
        Returns: (score, debug_info)
        """
        action, primary_noun, relevant_terms = self.extract_intent(query)
        func_lower = function_name.lower()
        
        score = base_priority
        debug_info = {
            "base": base_priority,
            "action": action,
            "primary_noun": primary_noun,
            "boosts": [],
            "penalties": []
        }
        
        # Action verb scoring
        if action == "list" and any(verb in func_lower for verb in ["list", "get"]):
            score += 10
            debug_info["boosts"].append(("action_match", 10))
        
        # Primary noun scoring
        if primary_noun and primary_noun in NOUN_MAPPINGS:
            noun_config = NOUN_MAPPINGS[primary_noun]
            
            # Strong boost for primary terms
            primary_matches = sum(1 for term in noun_config["primary"] 
                                if term in func_lower)
            if primary_matches > 0:
                boost = primary_matches * 50
                score += boost
                debug_info["boosts"].append(("primary_noun_match", boost))
            
            # Moderate boost for secondary terms
            secondary_matches = sum(1 for term in noun_config["secondary"] 
                                  if term in func_lower)
            if secondary_matches > 0:
                boost = secondary_matches * 20
                score += boost
                debug_info["boosts"].append(("secondary_noun_match", boost))
            
            # Penalty for avoid terms
            avoid_matches = sum(1 for term in noun_config["avoid"] 
                              if term in func_lower)
            if avoid_matches > 0:
                penalty = avoid_matches * 30
                score -= penalty
                debug_info["penalties"].append(("avoid_term_match", penalty))
        
        # Generic patterns to avoid
        if any(term in func_lower for term in ["policy", "template", "config", "setting"]):
            if not any(term in query.lower() for term in ["policy", "template", "config", "setting"]):
                score -= 20
                debug_info["penalties"].append(("generic_config_term", 20))
        
        # Boost for exact substring matches
        query_words = set(query.lower().split())
        func_words = set(re.findall(r'[a-z]+', func_lower))
        common_words = query_words & func_words
        if len(common_words) > 1:  # More than just the action verb
            boost = len(common_words) * 15
            score += boost
            debug_info["boosts"].append(("multiple_word_match", boost))
        
        debug_info["final_score"] = score
        return max(0, score), debug_info
    
    def rank_functions(self, functions: List[str], query: str, 
                      priorities: Dict[str, int] = None) -> List[Tuple[str, int, Dict]]:
        """
        Rank functions by semantic relevance to the query.
        Returns list of (function_name, score, debug_info) tuples.
        """
        if priorities is None:
            priorities = {}
        
        scored = []
        for func in functions:
            base_priority = priorities.get(func, 50)
            score, debug_info = self.score_function(func, query, base_priority)
            scored.append((func, score, debug_info))
        
        # Sort by score descending
        scored.sort(key=lambda x: x[1], reverse=True)
        return scored


def test_scoring():
    """Test the semantic scoring with various queries and functions."""
    
    # Test functions from different platforms
    test_functions = [
        # Intersight functions
        "GetComputePhysicalSummaryList",
        "GetServerProfileList",
        "GetComputeRackUnitList",
        "GetKvmPolicyList",
        "GetVnicEthIfList",
        "GetStoragePhysicalDiskList",
        
        # Catalyst functions
        "getDeviceList",
        "getAllInterfaces",
        "getNetworkDeviceList",
        "getInterfaceDetails",
        "getPolicyList",
        
        # Meraki functions
        "getOrganizationDevices",
        "getNetworkClients",
        "getDevices",
        
        # Generic list functions
        "GetSnmpPolicyList",
        "GetSshPolicyList",
        "GetVmediaPolicyList",
    ]
    
    # Test queries
    test_queries = [
        "list servers",
        "get all devices",
        "show interfaces",
        "list users",
        "network devices",
        "server inventory",
        "physical servers",
    ]
    
    # Platform-specific priorities (simplified)
    priorities = {
        "GetComputePhysicalSummaryList": 100,
        "GetComputeRackUnitList": 75,
        "GetServerProfileList": 40,
        "getDeviceList": 95,
        "getAllInterfaces": 90,
        "getOrganizationDevices": 85,
    }
    
    scorer = SemanticScorer()
    
    for query in test_queries:
        print(f"\n{'='*80}")
        print(f"Query: '{query}'")
        print(f"{'='*80}")
        
        action, noun, terms = scorer.extract_intent(query)
        print(f"Intent: action='{action}', target='{noun}', terms={terms}")
        print()
        
        results = scorer.rank_functions(test_functions, query, priorities)
        
        print("Top 10 Results:")
        print(f"{'Rank':<5} {'Score':<7} {'Function':<35} {'Debug Info'}")
        print("-" * 80)
        
        for i, (func, score, debug) in enumerate(results[:10], 1):
            boosts = ', '.join([f"{b[0]}(+{b[1]})" for b in debug['boosts']])
            penalties = ', '.join([f"{p[0]}(-{p[1]})" for p in debug['penalties']])
            debug_str = f"base={debug['base']}"
            if boosts:
                debug_str += f", {boosts}"
            if penalties:
                debug_str += f", {penalties}"
            
            print(f"{i:<5} {score:<7} {func:<35} {debug_str}")


def main():
    parser = argparse.ArgumentParser(description="Test semantic scoring for function selection")
    parser.add_argument("query", nargs="?", help="Query to test")
    parser.add_argument("--functions", "-f", help="Comma-separated list of functions to test")
    parser.add_argument("--test-all", action="store_true", help="Run all test cases")
    
    args = parser.parse_args()
    
    if args.test_all or not args.query:
        test_scoring()
    else:
        scorer = SemanticScorer()
        
        # Default test functions if none provided
        if args.functions:
            functions = [f.strip() for f in args.functions.split(",")]
        else:
            functions = [
                "GetComputePhysicalSummaryList",
                "GetServerProfileList",
                "GetKvmPolicyList",
                "getDeviceList",
                "getAllInterfaces",
            ]
        
        print(f"\nScoring functions for query: '{args.query}'")
        print("=" * 60)
        
        results = scorer.rank_functions(functions, args.query)
        
        for i, (func, score, debug) in enumerate(results, 1):
            print(f"\n{i}. {func} (Score: {score})")
            print(f"   Debug: {json.dumps(debug, indent=2)}")


if __name__ == "__main__":
    main()