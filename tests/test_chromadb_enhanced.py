#!/usr/bin/env python3
"""
Enhanced ChromaDB test with natural language query preprocessing.
This helps map natural language queries to appropriate function names.

Usage:
    python tests/test_chromadb_enhanced.py --query "list servers" --platform intersight
    python tests/test_chromadb_enhanced.py --query "show all devices" --platform meraki
"""

import argparse
import json
import sys
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple
import re

# Add the src directory to the path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from app.retrievers.chroma_retriever import ChromaRetriever
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.syntax import Syntax
from rich import box

console = Console()

# Natural language to function name mappings
QUERY_MAPPINGS = {
    # Server-related queries
    "list servers": ["GetComputePhysicalSummaryList", "list servers", "server inventory", "compute servers"],
    "show servers": ["GetComputePhysicalSummaryList", "list servers", "server inventory"],
    "get servers": ["GetComputePhysicalSummaryList", "list servers", "server inventory"],
    "server list": ["GetComputePhysicalSummaryList", "list servers"],
    "all servers": ["GetComputePhysicalSummaryList", "list servers"],
    
    # Device-related queries
    "list devices": ["getDeviceList", "getAllDeviceStatus", "getOrganizationDevices", "list devices", "device inventory"],
    "show devices": ["getDeviceList", "getAllDeviceStatus", "getOrganizationDevices", "list devices"],
    "all devices": ["getDeviceList", "getAllDeviceStatus", "getOrganizationDevices", "device inventory"],
    
    # Interface-related queries
    "list interfaces": ["getAllInterfaces", "getInterfaces", "GetVnicEthIfList", "list interfaces", "interface inventory"],
    "show interfaces": ["getAllInterfaces", "getInterfaces", "list interfaces"],
    
    # User-related queries
    "list users": ["getUsers", "getUserList", "GetIamUserList", "list users", "user list"],
    "show users": ["getUsers", "getUserList", "GetIamUserList", "list users"],
    
    # Alert-related queries
    "list alerts": ["GetCondAlarmList", "getSecurityAlerts", "list alerts", "alarm list"],
    "show alerts": ["GetCondAlarmList", "getSecurityAlerts", "list alerts"],
    
    # Network-related queries
    "list networks": ["getNetworks", "getNetworkList", "getOrganizationNetworks", "list networks"],
    "show networks": ["getNetworks", "getNetworkList", "list networks"],
    
    # Health-related queries
    "network health": ["getOverallNetworkHealth", "getSiteHealth", "getDeviceHealthStats", "network health"],
    "device health": ["getDeviceHealthStats", "device health", "health status"],
}

# Semantic keyword mappings
SEMANTIC_KEYWORDS = {
    "servers": ["server", "compute", "physical", "rack", "blade", "node", "machine", "host"],
    "devices": ["device", "equipment", "hardware", "network", "controller", "appliance"],
    "interfaces": ["interface", "port", "ethernet", "adapter", "nic", "network"],
    "users": ["user", "account", "identity", "person", "people", "member"],
    "alerts": ["alert", "alarm", "notification", "event", "warning", "incident"],
    "networks": ["network", "vlan", "subnet", "fabric", "vpc", "segment"],
    "health": ["health", "status", "state", "condition", "monitoring", "performance"],
}


class EnhancedChromaDBInspector:
    """Enhanced ChromaDB inspector with natural language preprocessing."""
    
    def __init__(self, collection_name: str = "function-definitions-index"):
        """Initialize the inspector with ChromaDB collection."""
        self.retriever = ChromaRetriever(collection_name=collection_name)
        self.collection = self.retriever.col
        
    def preprocess_query(self, query: str) -> Tuple[List[str], List[str]]:
        """
        Preprocess a natural language query to find relevant search terms.
        
        Returns:
            Tuple of (enhanced_queries, detected_keywords)
        """
        query_lower = query.lower().strip()
        enhanced_queries = [query]  # Always include original
        detected_keywords = []
        
        # Check for exact mapping matches
        for pattern, expansions in QUERY_MAPPINGS.items():
            if pattern in query_lower:
                enhanced_queries.extend(expansions)
                detected_keywords.append(pattern)
                console.print(f"[green]Detected pattern: '{pattern}'[/green]")
        
        # Check for semantic keywords
        for category, keywords in SEMANTIC_KEYWORDS.items():
            for keyword in keywords:
                if keyword in query_lower:
                    detected_keywords.append(keyword)
                    # Add the category as a search term
                    enhanced_queries.append(category)
                    # Add related function names from mappings
                    for pattern, expansions in QUERY_MAPPINGS.items():
                        if category in pattern:
                            enhanced_queries.extend(expansions[:2])  # Take first 2 expansions
        
        # Remove duplicates while preserving order
        seen = set()
        unique_queries = []
        for q in enhanced_queries:
            if q not in seen:
                seen.add(q)
                unique_queries.append(q)
        
        return unique_queries, detected_keywords
    
    def search_functions_enhanced(self, query: str, platform: Optional[str] = None, top_k: int = 10) -> List[Dict[str, Any]]:
        """Enhanced search that preprocesses natural language queries."""
        enhanced_queries, keywords = self.preprocess_query(query)
        
        console.print(f"\n[cyan]Original query:[/cyan] '{query}'")
        if keywords:
            console.print(f"[cyan]Detected keywords:[/cyan] {', '.join(keywords)}")
        console.print(f"[cyan]Enhanced searches:[/cyan] {', '.join(enhanced_queries[:5])}{'...' if len(enhanced_queries) > 5 else ''}")
        
        # Aggregate results from all enhanced queries
        all_results = {}
        result_scores = {}
        
        filter_dict = {}
        if platform:
            filter_dict["platform"] = {"$in": [platform]}
        
        # Search with each enhanced query
        for i, eq in enumerate(enhanced_queries[:5]):  # Limit to first 5 to avoid too many queries
            results = self.retriever.query(eq, k=top_k, filter=filter_dict)
            
            for result in results:
                func_name = self._extract_function_name(result)
                if func_name:
                    # Use the best (lowest) distance score
                    if func_name not in all_results or result.get('distance', float('inf')) < result_scores.get(func_name, float('inf')):
                        all_results[func_name] = result
                        result_scores[func_name] = result.get('distance', float('inf'))
                        # Boost score if this was from an early enhanced query
                        if i < 2:  # First two queries get a boost
                            result_scores[func_name] *= 0.8
        
        # Convert back to list and sort by score
        sorted_results = sorted(all_results.values(), key=lambda x: result_scores.get(self._extract_function_name(x), float('inf')))
        
        return sorted_results[:top_k]
    
    def _extract_function_name(self, result: Dict[str, Any]) -> Optional[str]:
        """Extract function name from a search result."""
        try:
            if isinstance(result.get('content'), str):
                content = json.loads(result['content'])
                return content.get('name')
            else:
                return result.get('name')
        except:
            return None
    
    def display_results(self, results: List[Dict[str, Any]], show_details: bool = False):
        """Display search results in a formatted table."""
        if not results:
            console.print("[red]No results found![/red]")
            return
            
        table = Table(box=box.SIMPLE_HEAVY)
        table.add_column("#", style="dim")
        table.add_column("Score", style="cyan")
        table.add_column("Platform", style="green")
        table.add_column("Function", style="yellow")
        table.add_column("Description", style="white", overflow="fold")
        
        for i, result in enumerate(results, 1):
            metadata = result.get("metadata", {})
            try:
                content = json.loads(result.get("content", "{}")) if isinstance(result.get("content"), str) else result.get("content", {})
            except:
                content = {"name": result.get("name", "N/A"), "description": "Parse error"}
            
            distance = result.get("distance", 0)
            score = 1 - distance if distance else "Perfect"
            
            table.add_row(
                str(i),
                f"{score:.3f}" if isinstance(score, float) else score,
                metadata.get("platform", "N/A"),
                content.get("name", result.get("name", "N/A")),
                content.get("description", "No description")[:80] + "..."
            )
        
        console.print(table)
        
        if show_details and console.is_terminal:
            choice = console.input("\n[cyan]Enter result number for details (or press Enter to skip): [/cyan]")
            if choice.isdigit() and 1 <= int(choice) <= len(results):
                selected = results[int(choice) - 1]
                self._display_function_details(selected)
    
    def _display_function_details(self, function_data: Dict[str, Any]):
        """Display detailed information about a function."""
        try:
            content = json.loads(function_data.get("content", "{}")) if isinstance(function_data.get("content"), str) else function_data.get("content", {})
        except:
            content = {}
        
        metadata = function_data.get("metadata", {})
        
        # Create main info table
        info_table = Table(box=box.ROUNDED, show_header=False)
        info_table.add_column("Field", style="cyan")
        info_table.add_column("Value")
        
        info_table.add_row("Function Name", content.get("name", metadata.get("name", "N/A")))
        info_table.add_row("Platform", metadata.get("platform", "N/A"))
        distance = function_data.get("distance", "N/A")
        info_table.add_row("Match Score", f"{1 - distance:.3f}" if isinstance(distance, (int, float)) else "N/A")
        
        console.print(Panel(info_table, title="Function Information", border_style="blue"))
        
        # Display description
        description = content.get("description", "No description available")
        console.print(Panel(description, title="Description", border_style="green"))


def main():
    parser = argparse.ArgumentParser(description="Enhanced ChromaDB query tool with natural language support")
    parser.add_argument("--query", "-q", required=True, help="Natural language query")
    parser.add_argument("--platform", "-p", help="Filter by platform (e.g., intersight, meraki)")
    parser.add_argument("--top", "-t", type=int, default=10, help="Number of results to return")
    parser.add_argument("--collection", default="function-definitions-index", help="ChromaDB collection name")
    parser.add_argument("--details", "-d", action="store_true", help="Show interactive details view")
    parser.add_argument("--show-mappings", action="store_true", help="Show all query mappings")
    
    args = parser.parse_args()
    
    if args.show_mappings:
        console.print("\n[cyan]Query Mappings:[/cyan]")
        for pattern, expansions in QUERY_MAPPINGS.items():
            console.print(f"  [yellow]{pattern}[/yellow] → {', '.join(expansions[:3])}...")
        return
    
    # Initialize inspector
    inspector = EnhancedChromaDBInspector(collection_name=args.collection)
    
    # Perform enhanced search
    results = inspector.search_functions_enhanced(args.query, platform=args.platform, top_k=args.top)
    
    # Display results
    inspector.display_results(results, show_details=args.details)


if __name__ == "__main__":
    main()