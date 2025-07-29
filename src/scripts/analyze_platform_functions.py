#!/usr/bin/env python3
"""
Analyze function definitions across all platforms to provide parameter statistics.
This helps estimate complexity for LLM fine-tuning.
"""
import json
import statistics
from pathlib import Path
from typing import Dict, List, Tuple
from collections import defaultdict
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box
# Optional visualization imports (commented out if not available)
# import matplotlib.pyplot as plt
# import numpy as np

console = Console()

# Paths
PROJECT_ROOT = Path(__file__).resolve().parents[2]
FUNCTION_DEFS_DIR = PROJECT_ROOT / "src" / "app" / "llm" / "function_definitions"
OPENAPI_SPECS_DIR = PROJECT_ROOT / "src" / "app" / "llm" / "openapi_specs"

def count_parameters(function_def: dict) -> Tuple[int, int, int]:
    """
    Count parameters for a function.
    Returns: (total_params, required_params, optional_params)
    """
    params = function_def.get("parameters", {})
    properties = params.get("properties", {})
    required = params.get("required", [])
    
    total = len(properties)
    required_count = len(required)
    optional_count = total - required_count
    
    return total, required_count, optional_count

def analyze_parameter_complexity(properties: dict) -> dict:
    """
    Analyze the complexity of parameters (nested objects, arrays, etc.)
    """
    complexity = {
        "simple": 0,  # string, number, boolean
        "array": 0,
        "object": 0,
        "nested": 0   # objects with properties
    }
    
    for param_name, param_def in properties.items():
        param_type = param_def.get("type", "string")
        
        if param_type in ["string", "number", "integer", "boolean"]:
            complexity["simple"] += 1
        elif param_type == "array":
            complexity["array"] += 1
        elif param_type == "object":
            complexity["object"] += 1
            # Check if it has nested properties
            if "properties" in param_def:
                complexity["nested"] += 1
                
    return complexity

def analyze_platform(platform_name: str, functions: List[dict]) -> dict:
    """
    Analyze all functions for a platform.
    """
    if not functions:
        return {
            "platform": platform_name,
            "total_functions": 0,
            "total_params": 0,
            "required_params": 0,
            "optional_params": 0,
            "avg_params": 0,
            "min_params": 0,
            "max_params": 0,
            "median_params": 0,
            "std_dev": 0,
            "complexity": {"simple": 0, "array": 0, "object": 0, "nested": 0},
            "param_distribution": {},
        }
    
    param_counts = []
    required_counts = []
    optional_counts = []
    total_complexity = defaultdict(int)
    param_distribution = defaultdict(int)
    
    for func in functions:
        total, required, optional = count_parameters(func)
        param_counts.append(total)
        required_counts.append(required)
        optional_counts.append(optional)
        
        # Track distribution
        param_distribution[total] += 1
        
        # Analyze complexity
        props = func.get("parameters", {}).get("properties", {})
        complexity = analyze_parameter_complexity(props)
        for key, value in complexity.items():
            total_complexity[key] += value
    
    return {
        "platform": platform_name,
        "total_functions": len(functions),
        "total_params": sum(param_counts),
        "required_params": sum(required_counts),
        "optional_params": sum(optional_counts),
        "avg_params": statistics.mean(param_counts) if param_counts else 0,
        "min_params": min(param_counts) if param_counts else 0,
        "max_params": max(param_counts) if param_counts else 0,
        "median_params": statistics.median(param_counts) if param_counts else 0,
        "std_dev": statistics.stdev(param_counts) if len(param_counts) > 1 else 0,
        "complexity": dict(total_complexity),
        "param_distribution": dict(param_distribution),
        "functions_by_param_count": {
            "0-5": sum(1 for c in param_counts if c <= 5),
            "6-10": sum(1 for c in param_counts if 6 <= c <= 10),
            "11-20": sum(1 for c in param_counts if 11 <= c <= 20),
            "21-50": sum(1 for c in param_counts if 21 <= c <= 50),
            "50+": sum(1 for c in param_counts if c > 50),
        }
    }

def analyze_intersight_special(platform_name: str) -> dict:
    """
    Special analysis for Intersight which has different structure.
    Intersight uses operation_id_map and has many generated methods.
    """
    # Try to load the full OpenAPI spec for more accurate analysis
    openapi_path = OPENAPI_SPECS_DIR / f"full_{platform_name}.json"
    if openapi_path.exists():
        with open(openapi_path, 'r') as f:
            spec = json.load(f)
            
        total_operations = 0
        param_counts = []
        
        for path, methods in spec.get("paths", {}).items():
            for method, operation in methods.items():
                if method.lower() in ["get", "post", "put", "patch", "delete"]:
                    total_operations += 1
                    # Count parameters
                    params = operation.get("parameters", [])
                    request_body = 1 if "requestBody" in operation else 0
                    total_params = len(params) + request_body
                    param_counts.append(total_params)
        
        return {
            "platform": platform_name,
            "note": "Intersight analysis based on OpenAPI spec",
            "total_operations": total_operations,
            "avg_params": statistics.mean(param_counts) if param_counts else 0,
            "min_params": min(param_counts) if param_counts else 0,
            "max_params": max(param_counts) if param_counts else 0,
            "median_params": statistics.median(param_counts) if param_counts else 0,
        }
    
    return {
        "platform": platform_name,
        "note": "Intersight requires special handling - OpenAPI spec not found"
    }

def create_visualizations(results: List[dict]):
    """Create visualization charts for the analysis (requires matplotlib)."""
    console.print("[yellow]Visualization skipped (matplotlib not installed)[/yellow]")
    console.print("[dim]To enable visualizations, install matplotlib: pip install matplotlib[/dim]")
    
def main():
    """Main analysis function."""
    console.print(Panel.fit("🔍 Platform Function Analysis", style="bold blue"))
    
    # Load all function definitions
    all_results = []
    
    for json_file in sorted(FUNCTION_DEFS_DIR.glob("*.json")):
        platform_name = json_file.stem
        
        try:
            with open(json_file, 'r') as f:
                functions = json.load(f)
            
            # Special handling for Intersight
            if platform_name.lower() == "intersight":
                result = analyze_intersight_special(platform_name)
            else:
                result = analyze_platform(platform_name, functions)
            
            all_results.append(result)
            
        except Exception as e:
            console.print(f"[red]Error analyzing {platform_name}: {e}[/red]")
    
    # Sort by total functions
    all_results.sort(key=lambda x: x.get("total_functions", 0), reverse=True)
    
    # Create summary table
    table = Table(title="Platform Function Analysis Summary", box=box.ROUNDED)
    table.add_column("Platform", style="cyan", no_wrap=True)
    table.add_column("Functions", justify="right", style="green")
    table.add_column("Avg Params", justify="right")
    table.add_column("Min", justify="right")
    table.add_column("Max", justify="right")
    table.add_column("Median", justify="right")
    table.add_column("Std Dev", justify="right")
    table.add_column("Required", justify="right", style="yellow")
    table.add_column("Optional", justify="right", style="blue")
    
    total_all_functions = 0
    total_all_params = 0
    
    for result in all_results:
        if result.get("note"):  # Special case like Intersight
            table.add_row(
                result["platform"],
                str(result.get("total_operations", "N/A")),
                f"{result.get('avg_params', 0):.1f}",
                str(result.get("min_params", "N/A")),
                str(result.get("max_params", "N/A")),
                f"{result.get('median_params', 0):.1f}",
                "N/A",
                "N/A",
                "N/A"
            )
        else:
            table.add_row(
                result["platform"],
                str(result["total_functions"]),
                f"{result['avg_params']:.1f}",
                str(result["min_params"]),
                str(result["max_params"]),
                f"{result['median_params']:.1f}",
                f"{result['std_dev']:.2f}",
                str(result["required_params"]),
                str(result["optional_params"])
            )
            total_all_functions += result["total_functions"]
            total_all_params += result["total_params"]
    
    console.print(table)
    
    # Overall statistics
    console.print("\n")
    stats_table = Table(title="Overall Statistics", box=box.SIMPLE)
    stats_table.add_column("Metric", style="bold")
    stats_table.add_column("Value", justify="right")
    
    stats_table.add_row("Total Platforms", str(len(all_results)))
    stats_table.add_row("Total Functions", str(total_all_functions))
    stats_table.add_row("Total Parameters", str(total_all_params))
    if total_all_functions > 0:
        stats_table.add_row("Overall Avg Params/Function", f"{total_all_params/total_all_functions:.2f}")
    
    console.print(stats_table)
    
    # Complexity estimates for fine-tuning
    console.print("\n")
    console.print(Panel.fit("🎯 Fine-Tuning Complexity Estimates", style="bold green"))
    
    complexity_table = Table(box=box.SIMPLE)
    complexity_table.add_column("Platform", style="cyan")
    complexity_table.add_column("Complexity", style="yellow")
    complexity_table.add_column("Estimated Training Time", style="green")
    
    for result in all_results:
        if result.get("total_functions", 0) == 0:
            continue
            
        # Calculate complexity score
        avg_params = result.get("avg_params", 0)
        total_funcs = result.get("total_functions", 0)
        
        # Complexity factors
        param_complexity = avg_params / 10  # Normalize to 0-10 scale
        volume_complexity = min(total_funcs / 100, 10)  # Cap at 10
        
        # Check for complex parameters
        complex_param_ratio = 0
        if result.get("complexity"):
            total_complex = sum(result["complexity"].values())
            if total_complex > 0:
                complex_param_ratio = (result["complexity"].get("object", 0) + 
                                     result["complexity"].get("nested", 0)) / total_complex
        
        # Overall complexity score (0-10 scale)
        complexity_score = (param_complexity * 0.4 + 
                          volume_complexity * 0.4 + 
                          complex_param_ratio * 10 * 0.2)
        
        # Estimate training time
        if complexity_score < 2:
            complexity_label = "Low"
            time_estimate = "1-2 hours"
        elif complexity_score < 5:
            complexity_label = "Medium"
            time_estimate = "3-5 hours"
        elif complexity_score < 8:
            complexity_label = "High"
            time_estimate = "6-12 hours"
        else:
            complexity_label = "Very High"
            time_estimate = "12+ hours"
        
        complexity_table.add_row(
            result["platform"],
            f"{complexity_label} ({complexity_score:.1f}/10)",
            time_estimate
        )
    
    console.print(complexity_table)
    
    # Save detailed results
    output_file = PROJECT_ROOT / "platform_function_analysis.json"
    with open(output_file, 'w') as f:
        json.dump(all_results, f, indent=2)
    
    console.print(f"\n[green]✓ Detailed results saved to: {output_file}[/green]")
    
    # Create visualizations
    try:
        create_visualizations(all_results)
    except Exception as e:
        console.print(f"[yellow]Could not create visualizations: {e}[/yellow]")

if __name__ == "__main__":
    main()