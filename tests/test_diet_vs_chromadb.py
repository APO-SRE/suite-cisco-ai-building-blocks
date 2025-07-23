#!/usr/bin/env python3
"""
Compare diet schema files with what's actually stored in ChromaDB.
This helps identify discrepancies between generated schemas and indexed content.

Usage:
    python tests/test_diet_vs_chromadb.py --platform intersight
    python tests/test_diet_vs_chromadb.py --function GetComputePhysicalSummaryList
    python tests/test_diet_vs_chromadb.py --check-all
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
import difflib

# Add the src directory to the path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from app.retrievers.chroma_retriever import ChromaRetriever
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.syntax import Syntax
from rich import box
from rich.columns import Columns
from rich.text import Text

console = Console()


class SchemaComparator:
    """Compare diet schemas with ChromaDB contents."""
    
    def __init__(self, collection_name: str = "function-definitions-index"):
        """Initialize with paths and ChromaDB."""
        self.retriever = ChromaRetriever(collection_name=collection_name)
        self.collection = self.retriever.col
        self.diet_dir = Path(__file__).parent.parent / "src" / "app" / "llm" / "function_definitions"
        self.overrides_file = Path(__file__).parent.parent / "src" / "scripts" / "platform_scaffolder.py"
        
    def load_diet_schema(self, platform: str) -> Dict[str, Dict[str, Any]]:
        """Load diet schema from file."""
        schema_file = self.diet_dir / f"{platform}.json"
        if not schema_file.exists():
            console.print(f"[red]Diet schema file not found: {schema_file}[/red]")
            return {}
            
        with open(schema_file, 'r') as f:
            functions = json.load(f)
            
        # Index by function name
        return {func["name"]: func for func in functions}
    
    def get_chromadb_functions(self, platform: str) -> Dict[str, Dict[str, Any]]:
        """Get all functions from ChromaDB for a platform."""
        results = self.collection.query(
            query_texts=[""],
            n_results=1000,  # Get all
            where={"platform": {"$eq": platform}}
        )
        
        indexed_funcs = {}
        ids = results.get("ids", [[]])[0]
        documents = results.get("documents", [[]])[0]
        metadatas = results.get("metadatas", [[]])[0]
        
        for i in range(len(ids)):
            try:
                content = json.loads(documents[i])
                func_name = content.get("name", metadatas[i].get("name", "Unknown"))
                indexed_funcs[func_name] = content
            except json.JSONDecodeError:
                console.print(f"[yellow]Warning: Failed to parse document {ids[i]}[/yellow]")
                
        return indexed_funcs
    
    def load_platform_overrides(self) -> Dict[str, Dict[str, Any]]:
        """Load PLATFORM_OVERRIDES from scaffolder script."""
        try:
            with open(self.overrides_file, 'r') as f:
                content = f.read()
                
            # Find PLATFORM_OVERRIDES section
            start = content.find("PLATFORM_OVERRIDES = {")
            if start == -1:
                return {}
                
            # Extract just the dictionary definition
            brace_count = 0
            end = start
            for i, char in enumerate(content[start:], start):
                if char == '{':
                    brace_count += 1
                elif char == '}':
                    brace_count -= 1
                    if brace_count == 0:
                        end = i + 1
                        break
                        
            override_str = content[start:end]
            
            # Create a minimal execution environment
            namespace = {}
            exec(override_str, namespace)
            return namespace.get("PLATFORM_OVERRIDES", {})
            
        except Exception as e:
            console.print(f"[yellow]Warning: Could not load overrides: {e}[/yellow]")
            return {}
    
    def compare_function(self, func_name: str, diet_func: Dict[str, Any], 
                        chromadb_func: Dict[str, Any], overrides: Dict[str, Any]) -> Dict[str, Any]:
        """Compare a single function between diet schema and ChromaDB."""
        diffs = {
            "name": func_name,
            "description_match": diet_func.get("description") == chromadb_func.get("description"),
            "diet_description": diet_func.get("description", ""),
            "chromadb_description": chromadb_func.get("description", ""),
            "override_description": overrides.get("descriptions", {}).get(func_name, ""),
            "parameters_match": json.dumps(diet_func.get("parameters", {}), sort_keys=True) == 
                               json.dumps(chromadb_func.get("parameters", {}), sort_keys=True),
            "in_blocklist": func_name in overrides.get("blocklist", set()),
        }
        
        # Check if override exists but wasn't applied
        if diffs["override_description"] and diffs["override_description"] != diffs["diet_description"]:
            diffs["override_not_applied"] = True
        else:
            diffs["override_not_applied"] = False
            
        return diffs
    
    def display_comparison(self, platform: str, specific_function: Optional[str] = None):
        """Display comparison results."""
        console.print(f"\n[cyan]Comparing diet schemas vs ChromaDB for platform: {platform}[/cyan]\n")
        
        # Load data
        diet_funcs = self.load_diet_schema(platform)
        chromadb_funcs = self.get_chromadb_functions(platform)
        all_overrides = self.load_platform_overrides()
        platform_overrides = all_overrides.get(platform, {})
        
        # Stats
        stats_table = Table(box=box.ROUNDED)
        stats_table.add_column("Source", style="cyan")
        stats_table.add_column("Count", style="green")
        stats_table.add_row("Diet Schema Functions", str(len(diet_funcs)))
        stats_table.add_row("ChromaDB Functions", str(len(chromadb_funcs)))
        stats_table.add_row("Platform Overrides", str(len(platform_overrides.get("descriptions", {}))))
        console.print(Panel(stats_table, title="Overview", border_style="blue"))
        
        # Find differences
        all_func_names = set(diet_funcs.keys()) | set(chromadb_funcs.keys())
        
        if specific_function:
            if specific_function not in all_func_names:
                console.print(f"[red]Function '{specific_function}' not found![/red]")
                return
            all_func_names = {specific_function}
        
        mismatches = []
        missing_in_chromadb = []
        missing_in_diet = []
        
        for func_name in sorted(all_func_names):
            if func_name not in diet_funcs:
                missing_in_diet.append(func_name)
                continue
            if func_name not in chromadb_funcs:
                missing_in_chromadb.append(func_name)
                continue
                
            diff = self.compare_function(
                func_name, 
                diet_funcs[func_name], 
                chromadb_funcs[func_name],
                platform_overrides
            )
            
            if not diff["description_match"] or diff["override_not_applied"]:
                mismatches.append(diff)
        
        # Display results
        if missing_in_chromadb:
            console.print(Panel(
                "\n".join(missing_in_chromadb), 
                title=f"[red]Missing in ChromaDB ({len(missing_in_chromadb)})[/red]",
                border_style="red"
            ))
            
        if missing_in_diet:
            console.print(Panel(
                "\n".join(missing_in_diet), 
                title=f"[yellow]Missing in Diet Schema ({len(missing_in_diet)})[/yellow]",
                border_style="yellow"
            ))
        
        if mismatches:
            console.print(f"\n[red]Found {len(mismatches)} description mismatches:[/red]\n")
            
            for diff in mismatches:
                # Function name
                console.print(f"\n[bold cyan]Function: {diff['name']}[/bold cyan]")
                
                if diff["in_blocklist"]:
                    console.print("[red]⚠️  This function is in the blocklist![/red]")
                
                # Show override if exists
                if diff["override_description"]:
                    console.print("\n[green]Override Definition:[/green]")
                    console.print(Panel(diff["override_description"], border_style="green"))
                    
                    if diff["override_not_applied"]:
                        console.print("[red]❌ Override NOT applied to diet schema![/red]")
                
                # Show diet schema description
                console.print("\n[yellow]Diet Schema:[/yellow]")
                console.print(Panel(diff["diet_description"] or "[No description]", border_style="yellow"))
                
                # Show ChromaDB description
                console.print("\n[blue]ChromaDB:[/blue]")
                console.print(Panel(diff["chromadb_description"] or "[No description]", border_style="blue"))
                
                # Show diff if descriptions don't match
                if diff["diet_description"] != diff["chromadb_description"]:
                    console.print("\n[red]Diff:[/red]")
                    diff_lines = list(difflib.unified_diff(
                        diff["chromadb_description"].splitlines(keepends=True),
                        diff["diet_description"].splitlines(keepends=True),
                        fromfile="ChromaDB",
                        tofile="Diet Schema",
                        n=1
                    ))
                    if diff_lines:
                        syntax = Syntax("".join(diff_lines), "diff", theme="monokai")
                        console.print(syntax)
                
                console.print("\n" + "─" * 80)
        else:
            console.print("[green]✅ All descriptions match between diet schema and ChromaDB![/green]")
    
    def check_all_platforms(self):
        """Check all available platforms."""
        # Find all diet schema files
        platforms = []
        for schema_file in self.diet_dir.glob("*.json"):
            platforms.append(schema_file.stem)
            
        if not platforms:
            console.print("[red]No diet schema files found![/red]")
            return
            
        summary_table = Table(box=box.SIMPLE_HEAVY)
        summary_table.add_column("Platform", style="cyan")
        summary_table.add_column("Diet", style="yellow")
        summary_table.add_column("ChromaDB", style="blue")
        summary_table.add_column("Missing", style="red")
        summary_table.add_column("Mismatches", style="magenta")
        summary_table.add_column("Status", style="green")
        
        for platform in sorted(platforms):
            diet_funcs = self.load_diet_schema(platform)
            chromadb_funcs = self.get_chromadb_functions(platform)
            
            missing_in_chromadb = len(set(diet_funcs.keys()) - set(chromadb_funcs.keys()))
            
            # Count mismatches
            mismatches = 0
            for func_name in set(diet_funcs.keys()) & set(chromadb_funcs.keys()):
                if diet_funcs[func_name].get("description") != chromadb_funcs[func_name].get("description"):
                    mismatches += 1
            
            status = "✅" if missing_in_chromadb == 0 and mismatches == 0 else "❌"
            
            summary_table.add_row(
                platform,
                str(len(diet_funcs)),
                str(len(chromadb_funcs)),
                str(missing_in_chromadb),
                str(mismatches),
                status
            )
            
        console.print(Panel(summary_table, title="Platform Summary", border_style="cyan"))


def main():
    parser = argparse.ArgumentParser(description="Compare diet schemas with ChromaDB content")
    parser.add_argument("--platform", "-p", help="Platform to compare")
    parser.add_argument("--function", "-f", help="Specific function to compare")
    parser.add_argument("--check-all", action="store_true", help="Check all platforms")
    parser.add_argument("--collection", default="function-definitions-index", help="ChromaDB collection name")
    
    args = parser.parse_args()
    
    comparator = SchemaComparator(collection_name=args.collection)
    
    if args.check_all:
        comparator.check_all_platforms()
    elif args.platform or args.function:
        # If function specified without platform, try to find it
        platform = args.platform
        if args.function and not platform:
            # Search all platforms
            for p in ["intersight", "meraki", "catalyst", "sdwan_mngr", "nexus_dashboard"]:
                diet_funcs = comparator.load_diet_schema(p)
                if args.function in diet_funcs:
                    platform = p
                    console.print(f"[green]Found function in platform: {platform}[/green]")
                    break
                    
        if not platform:
            console.print("[red]Platform not specified and function not found in any platform![/red]")
            return
            
        comparator.display_comparison(platform, args.function)
    else:
        parser.print_help()
        console.print("\n[yellow]Examples:[/yellow]")
        console.print("  python tests/test_diet_vs_chromadb.py --platform intersight")
        console.print("  python tests/test_diet_vs_chromadb.py --function GetComputePhysicalSummaryList")
        console.print("  python tests/test_diet_vs_chromadb.py --check-all")


if __name__ == "__main__":
    main()