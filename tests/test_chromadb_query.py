#!/usr/bin/env python3
"""
Test script to query ChromaDB and inspect function details.
This helps debug function selection and understand what's stored in ChromaDB.

Usage:
    python tests/test_chromadb_query.py --function GetComputePhysicalSummaryList --platform intersight
    python tests/test_chromadb_query.py --query "list servers" --platform intersight --top 10
    python tests/test_chromadb_query.py --dump-all --platform intersight
"""

import argparse
import json
import sys
from pathlib import Path
from typing import List, Dict, Any, Optional
import os

# Add the src directory to the path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from app.retrievers.chroma_retriever import ChromaRetriever
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.syntax import Syntax
from rich import box

console = Console()


class ChromaDBInspector:
    """Utility class to inspect ChromaDB contents for debugging."""
    
    def __init__(self, collection_name: str = "function-definitions-index"):
        """Initialize the inspector with ChromaDB collection."""
        self.retriever = ChromaRetriever(collection_name=collection_name)
        self.collection = self.retriever.col
        
    def get_function_by_name(self, function_name: str, platform: Optional[str] = None) -> List[Dict[str, Any]]:
        """Get a specific function by exact name match."""
        filter_dict = {}
        if platform:
            filter_dict["platform"] = {"$eq": platform}
            
        # Query with exact function name
        results = self.collection.query(
            query_texts=[function_name],
            n_results=10,
            where=filter_dict
        )
        
        return self._format_results(results)
    
    def search_functions(self, query: str, platform: Optional[str] = None, top_k: int = 10) -> List[Dict[str, Any]]:
        """Search for functions using similarity search."""
        filter_dict = {}
        if platform:
            filter_dict["platform"] = {"$in": [platform]}
            
        results = self.retriever.query(query, k=top_k, filter=filter_dict)
        return results
    
    def get_all_functions(self, platform: Optional[str] = None, limit: int = 100) -> List[Dict[str, Any]]:
        """Get all functions for a platform."""
        filter_dict = {}
        if platform:
            filter_dict["platform"] = {"$eq": platform}
            
        # Get all with empty query
        results = self.collection.query(
            query_texts=[""],
            n_results=limit,
            where=filter_dict
        )
        
        return self._format_results(results)
    
    def _format_results(self, results: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Format ChromaDB results into a consistent structure."""
        formatted = []
        
        if not results or not results.get("ids"):
            return formatted
            
        ids = results.get("ids", [[]])[0] if results.get("ids") else []
        documents = results.get("documents", [[]])[0] if results.get("documents") else []
        metadatas = results.get("metadatas", [[]])[0] if results.get("metadatas") else []
        distances = results.get("distances", [[]])[0] if results.get("distances") else []
        embeddings = results.get("embeddings", [[]])[0] if results.get("embeddings") else [None] * len(ids)
        
        for i in range(len(ids)):
            try:
                # Parse the document content (it's a JSON string)
                doc_content = json.loads(documents[i]) if documents[i] else {}
            except json.JSONDecodeError:
                doc_content = {"error": "Failed to parse document", "raw": documents[i]}
                
            formatted.append({
                "id": ids[i],
                "distance": distances[i] if i < len(distances) else None,
                "metadata": metadatas[i] if i < len(metadatas) else {},
                "content": doc_content,
                "embedding": embeddings[i][:5] if embeddings[i] else None  # First 5 values only
            })
            
        return formatted
    
    def display_function_details(self, function_data: Dict[str, Any]):
        """Display detailed information about a function."""
        content = function_data.get("content", {})
        metadata = function_data.get("metadata", {})
        
        # Create main info table
        info_table = Table(box=box.ROUNDED, show_header=False)
        info_table.add_column("Field", style="cyan")
        info_table.add_column("Value")
        
        info_table.add_row("ID", function_data.get("id", "N/A"))
        info_table.add_row("Platform", metadata.get("platform", "N/A"))
        info_table.add_row("Function Name", content.get("name", metadata.get("name", "N/A")))
        info_table.add_row("Distance/Score", f"{function_data.get('distance', 'N/A'):.4f}" if function_data.get('distance') else "N/A")
        
        console.print(Panel(info_table, title="Function Information", border_style="blue"))
        
        # Display description
        description = content.get("description", "No description available")
        console.print(Panel(description, title="Description", border_style="green"))
        
        # Display parameters
        params = content.get("parameters", {})
        if params:
            param_json = json.dumps(params, indent=2)
            syntax = Syntax(param_json, "json", theme="monokai", line_numbers=True)
            console.print(Panel(syntax, title="Parameters", border_style="yellow"))
        
        # Display raw content if needed
        if console.is_terminal:
            show_raw = console.input("\n[cyan]Show raw content? (y/N): [/cyan]").lower() == 'y'
            if show_raw:
                raw_json = json.dumps(content, indent=2)
                syntax = Syntax(raw_json, "json", theme="monokai", line_numbers=True)
                console.print(Panel(syntax, title="Raw Content", border_style="red"))


def main():
    parser = argparse.ArgumentParser(description="Query ChromaDB to inspect function details")
    parser.add_argument("--function", "-f", help="Search for specific function by name")
    parser.add_argument("--query", "-q", help="Similarity search query")
    parser.add_argument("--platform", "-p", help="Filter by platform (e.g., intersight, meraki)")
    parser.add_argument("--top", "-t", type=int, default=10, help="Number of results to return")
    parser.add_argument("--dump-all", action="store_true", help="Dump all functions for a platform")
    parser.add_argument("--collection", default="function-definitions-index", help="ChromaDB collection name")
    parser.add_argument("--show-stats", action="store_true", help="Show collection statistics")
    
    args = parser.parse_args()
    
    # Initialize inspector
    inspector = ChromaDBInspector(collection_name=args.collection)
    
    # Show collection stats
    if args.show_stats:
        count = inspector.collection.count()
        console.print(Panel(f"Total documents in collection: {count}", title="Collection Stats", border_style="cyan"))
        return
    
    # Handle different query modes
    if args.dump_all:
        console.print(f"\n[cyan]Dumping all functions for platform: {args.platform or 'all'}[/cyan]\n")
        results = inspector.get_all_functions(platform=args.platform, limit=1000)
        
        table = Table(box=box.SIMPLE)
        table.add_column("#", style="dim")
        table.add_column("Platform", style="cyan")
        table.add_column("Function", style="green")
        table.add_column("Description", style="yellow", overflow="fold")
        
        for i, func in enumerate(results, 1):
            content = func.get("content", {})
            metadata = func.get("metadata", {})
            table.add_row(
                str(i),
                metadata.get("platform", "N/A"),
                content.get("name", metadata.get("name", "N/A")),
                content.get("description", "No description")[:80] + "..."
            )
            
        console.print(table)
        
    elif args.function:
        console.print(f"\n[cyan]Searching for function: {args.function}[/cyan]\n")
        results = inspector.get_function_by_name(args.function, platform=args.platform)
        
        if not results:
            console.print("[red]No functions found![/red]")
        else:
            console.print(f"[green]Found {len(results)} result(s)[/green]\n")
            for i, func in enumerate(results):
                if i > 0:
                    console.print("\n" + "="*80 + "\n")
                inspector.display_function_details(func)
                
    elif args.query:
        console.print(f"\n[cyan]Similarity search for: '{args.query}'[/cyan]\n")
        results = inspector.search_functions(args.query, platform=args.platform, top_k=args.top)
        
        if not results:
            console.print("[red]No results found![/red]")
        else:
            table = Table(box=box.SIMPLE_HEAVY)
            table.add_column("#", style="dim")
            table.add_column("Score", style="cyan")
            table.add_column("Platform", style="green")
            table.add_column("Function", style="yellow")
            table.add_column("Description", style="white", overflow="fold")
            
            for i, func in enumerate(results, 1):
                # Results from search are already formatted differently
                metadata = func.get("metadata", {})
                try:
                    content = json.loads(func.get("content", "{}"))
                except:
                    content = {"name": func.get("name", "N/A"), "description": "Parse error"}
                    
                distance = func.get("distance", 0)
                score = 1 - distance if distance else "N/A"  # Convert distance to similarity
                
                table.add_row(
                    str(i),
                    f"{score:.3f}" if isinstance(score, float) else score,
                    metadata.get("platform", "N/A"),
                    content.get("name", func.get("name", "N/A")),
                    content.get("description", "No description")[:60] + "..."
                )
                
            console.print(table)
            
            # Ask if user wants details on any result
            if console.is_terminal:
                choice = console.input("\n[cyan]Enter result number for details (or press Enter to skip): [/cyan]")
                if choice.isdigit() and 1 <= int(choice) <= len(results):
                    console.print("\n" + "="*80 + "\n")
                    selected = results[int(choice) - 1]
                    # Format it properly for display
                    formatted = {
                        "id": selected.get("id", "N/A"),
                        "distance": selected.get("distance"),
                        "metadata": selected.get("metadata", {}),
                        "content": json.loads(selected.get("content", "{}")) if isinstance(selected.get("content"), str) else selected.get("content", {})
                    }
                    inspector.display_function_details(formatted)
    else:
        parser.print_help()
        console.print("\n[yellow]Examples:[/yellow]")
        console.print("  python tests/test_chromadb_query.py --function GetComputePhysicalSummaryList --platform intersight")
        console.print("  python tests/test_chromadb_query.py --query 'list servers' --platform intersight --top 10")
        console.print("  python tests/test_chromadb_query.py --dump-all --platform meraki")
        console.print("  python tests/test_chromadb_query.py --show-stats")


if __name__ == "__main__":
    main()