#!/usr/bin/env python3
"""
Simple test script for Intersight natural language queries.
Shows what functions would be selected for different queries.

Usage:
    python tests/test_intersight_queries.py
    python tests/test_intersight_queries.py --query "your custom query"
"""

import sys
from pathlib import Path
import argparse

# Add the src directory to the path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from app.llm.dynamic import build_functions_for_llm
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box

console = Console()


def test_query(query: str, platform: str = "intersight"):
    """Test what functions are selected for a given query."""
    
    console.print(f"\n[cyan]Query:[/cyan] '{query}'")
    console.print(f"[cyan]Platform:[/cyan] {platform}")
    
    # Build functions
    functions = build_functions_for_llm(query, [platform], k=10)
    
    if not functions:
        console.print("[red]No functions found![/red]")
        return
    
    # Create results table
    table = Table(title=f"Top Functions for '{query}'", box=box.ROUNDED)
    table.add_column("#", style="dim", width=3)
    table.add_column("Function Name", style="green", width=40)
    table.add_column("Description", style="yellow")
    
    for i, func in enumerate(functions[:10], 1):
        name = func.get('name', 'Unknown')
        desc = func.get('description', 'No description')
        # Truncate description
        if len(desc) > 80:
            desc = desc[:77] + "..."
        table.add_row(str(i), name, desc)
    
    console.print(table)
    
    # Show the top function details
    top_func = functions[0]
    console.print(f"\n[bold green]Top Match:[/bold green] {top_func.get('name')}")
    console.print(Panel(top_func.get('description', 'No description'), 
                       title="Full Description", 
                       border_style="green"))


def main():
    parser = argparse.ArgumentParser(description="Test Intersight query function selection")
    parser.add_argument("--query", "-q", help="Custom query to test")
    parser.add_argument("--platform", "-p", default="intersight", help="Platform to test")
    args = parser.parse_args()
    
    if args.query:
        # Test custom query
        test_query(args.query, args.platform)
    else:
        # Test common queries
        console.print("\n[bold cyan]Testing Common Intersight Queries[/bold cyan]")
        console.print("="*60)
        
        common_queries = [
            "list servers",
            "show users",
            "get alarms",
            "list blade servers",
            "show rack servers",
            "list interfaces",
            "show chassis",
            "get server profiles",
            "list storage",
            "show fabric interconnects"
        ]
        
        for query in common_queries:
            test_query(query)
            console.print("\n" + "-"*60)


if __name__ == "__main__":
    main()