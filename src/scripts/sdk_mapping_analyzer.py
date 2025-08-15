#!/usr/bin/env python3
"""
SDK Mapping Analyzer
Analyzes OpenAPI specs vs SDK methods to suggest operation_id_map entries

Purpose: Analyzing gaps between OpenAPI specs and SDK implementations to generate mapping recommendations
What it does:

Compares ALL operations in OpenAPI spec against ALL methods in SDK
Uses fuzzy matching to suggest mappings for mismatched names
Generates coverage reports showing what % of API is covered by SDK
Suggests operation_id_map entries to improve coverage
Analysis tool for improving your platform configuration

Output:

Coverage percentages
Lists of unmapped operations
Suggested mappings like "GetComputePhysicalSummaryList": "get_compute_physical_summary_list"




"""
import sys
import json
import re
from pathlib import Path
from typing import Dict, List, Set, Tuple
import importlib
from difflib import SequenceMatcher

from app.utils.sdk_introspection import SDKIntrospector, SDKPattern
from app.utils.paths import REPO_ROOT

scripts_dir = REPO_ROOT / "src" / "scripts"
if str(scripts_dir) not in sys.path:
    sys.path.insert(0, str(scripts_dir))

try:
    from platform_scaffolder import PLATFORM_OVERRIDES as PLATFORM_CONFIG, OUT_DIRS
except ImportError as e:
    print(f"Warning: Could not import platform_scaffolder: {e}")
    PLATFORM_CONFIG = {}
    OUT_DIRS = {}
    
class SDKMappingAnalyzer:
    """Analyzes SDK vs OpenAPI to suggest mappings"""
    
    def __init__(self, platform: str, sdk_module_name: str, openapi_spec_path: Path):
        self.platform = platform
        self.sdk_module_name = sdk_module_name
        self.openapi_spec_path = openapi_spec_path
        
        # Load OpenAPI spec
        with open(openapi_spec_path, 'r') as f:
            self.openapi_spec = json.load(f)
        
        # Introspect SDK
        self.introspector = SDKIntrospector(platform, sdk_module_name)
        self.sdk_methods = self.introspector.discover_methods()
        
    def extract_operation_ids(self) -> Set[str]:
        """Extract all operationIds from OpenAPI spec"""
        operation_ids = set()
        
        for path, path_item in self.openapi_spec.get('paths', {}).items():
            for method, operation in path_item.items():
                if method in ['get', 'post', 'put', 'patch', 'delete', 'head', 'options']:
                    op_id = operation.get('operationId')
                    if op_id:
                        operation_ids.add(op_id)
        
        return operation_ids
    
    def find_similar_methods(self, operation_id: str, threshold: float = 0.6) -> List[Tuple[str, float]]:
        """Find SDK methods similar to an operationId"""
        similar = []
        
        # Normalize operation_id for comparison
        op_normalized = self._normalize_name(operation_id)
        
        for sdk_method_name in self.sdk_methods:
            sdk_normalized = self._normalize_name(sdk_method_name)
            
            # Calculate similarity
            similarity = SequenceMatcher(None, op_normalized, sdk_normalized).ratio()
            
            if similarity >= threshold:
                similar.append((sdk_method_name, similarity))
        
        # Sort by similarity score
        similar.sort(key=lambda x: x[1], reverse=True)
        return similar[:5]  # Top 5 matches
    
    def _normalize_name(self, name: str) -> str:
        """Normalize names for comparison"""
        # Convert to lowercase
        name = name.lower()
        
        # Convert camelCase to snake_case
        name = re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()
        
        # Remove common prefixes/suffixes
        for prefix in ['get_', 'list_', 'create_', 'update_', 'delete_', 'set_']:
            if name.startswith(prefix):
                name = name[len(prefix):]
        
        for suffix in ['_list', '_all', '_by_id']:
            if name.endswith(suffix):
                name = name[:-len(suffix)]
        
        return name
    
    def analyze_unmapped_operations(self) -> Dict[str, List[str]]:
        """Find operations without SDK mappings and suggest matches"""
        operation_ids = self.extract_operation_ids()
        unmapped = {}
        
        # Build set of SDK method names and their variants
        sdk_method_variants = set()
        for method in self.sdk_methods.values():
            sdk_method_variants.update(method.operation_id_variants)
        
        for op_id in operation_ids:
            # Check if this operation is already mappable
            found = False
            for variant in [op_id, op_id.lower(), self._normalize_name(op_id)]:
                if variant in sdk_method_variants:
                    found = True
                    break
            
            if not found:
                # Find similar SDK methods
                similar = self.find_similar_methods(op_id)
                if similar:
                    unmapped[op_id] = [f"{method} (similarity: {score:.2f})" for method, score in similar]
        
        return unmapped
    
    def suggest_operation_id_map(self) -> Dict[str, str]:
        """Generate suggested operation_id_map entries"""
        suggestions = {}
        unmapped = self.analyze_unmapped_operations()
        
        for op_id, similar_methods in unmapped.items():
            if similar_methods:
                # Extract the method name from the first suggestion
                best_match = similar_methods[0].split(' ')[0]
                similarity_score = float(similar_methods[0].split('similarity: ')[1].rstrip(')'))
                
                # Only suggest if similarity is high enough
                if similarity_score >= 0.7:
                    suggestions[op_id] = best_match
        
        return suggestions
    
    def generate_report(self) -> dict:
        """Generate comprehensive analysis report"""
        operation_ids = self.extract_operation_ids()
        unmapped = self.analyze_unmapped_operations()
        suggestions = self.suggest_operation_id_map()
        
        # Calculate coverage
        total_operations = len(operation_ids)
        unmapped_count = len(unmapped)
        coverage = ((total_operations - unmapped_count) / total_operations * 100) if total_operations > 0 else 0
        
        report = {
            "platform": self.platform,
            "sdk_module": self.sdk_module_name,
            "total_operations": total_operations,
            "sdk_methods_found": len(self.sdk_methods),
            "unmapped_operations": unmapped_count,
            "coverage_percentage": coverage,
            "suggested_mappings": suggestions,
            "unmapped_details": unmapped,
            "recommendations": []
        }
        
        # Add recommendations
        if unmapped_count > 0:
            report["recommendations"].append(
                f"Consider adding {unmapped_count} operation_id_map entries to improve coverage"
            )
        
        if coverage < 80:
            report["recommendations"].append(
                "SDK coverage is below 80%. Check if SDK is up-to-date with the API"
            )
        
        # Find operations with no good matches
        no_matches = [op for op, matches in unmapped.items() if not matches]
        if no_matches:
            report["operations_with_no_matches"] = no_matches
            report["recommendations"].append(
                f"{len(no_matches)} operations have no similar SDK methods. These may be missing from the SDK."
            )
        
        return report


def analyze_all_platforms():
    """Analyze all configured platforms"""

    
    reports = {}
    
    for platform, config in PLATFORM_CONFIG.items():
        openapi_path = OUT_DIRS["full"] / f"full_{platform}.json"
        if not openapi_path.exists():
            print(f"Skipping {platform} - no OpenAPI spec found")
            continue
        
        print(f"\nAnalyzing {platform}...")
        
        try:
            analyzer = SDKMappingAnalyzer(
                platform,
                config["sdk_module"],
                openapi_path
            )
            
            report = analyzer.generate_report()
            reports[platform] = report
            
            # Print summary
            print(f"  Coverage: {report['coverage_percentage']:.1f}%")
            print(f"  Unmapped operations: {report['unmapped_operations']}")
            
            if report['suggested_mappings']:
                print(f"  Suggested mappings:")
                for op_id, sdk_method in list(report['suggested_mappings'].items())[:5]:
                    print(f"    '{op_id}': '{sdk_method}',")
            
        except Exception as e:
            print(f"  Error: {e}")
            reports[platform] = {"error": str(e)}
    
    # Write full report
    report_path = OUT_DIRS["coverage"] / "sdk_mapping_analysis.json"
    with open(report_path, 'w') as f:
        json.dump(reports, f, indent=2)
    
    print(f"\nFull report written to: {report_path}")
    
    # Generate operation_id_map suggestions file
    suggestions_path = OUT_DIRS["coverage"] / "operation_id_map_suggestions.py"
    with open(suggestions_path, 'w') as f:
        f.write("# Suggested operation_id_map entries for PLATFORM_CONFIG\n\n")
        
        for platform, report in reports.items():
            if 'suggested_mappings' in report and report['suggested_mappings']:
                f.write(f'    "{platform}": {{\n')
                f.write(f'        "operation_id_map": {{\n')
                for op_id, sdk_method in report['suggested_mappings'].items():
                    f.write(f'            "{op_id}": "{sdk_method}",\n')
                f.write('        }\n')
                f.write('    },\n\n')
    
    print(f"Suggestions written to: {suggestions_path}")


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        # Analyze specific platform
        platform = sys.argv[1]
        sdk_module = sys.argv[2] if len(sys.argv) > 2 else None
        openapi_spec = sys.argv[3] if len(sys.argv) > 3 else f"app/llm/openapi_specs/full_{platform}.json"
        
        if not sdk_module:

 

            sdk_module = PLATFORM_CONFIG.get(platform, {}).get("sdk_module")
        
        if not sdk_module:
            print(f"Error: SDK module not found for platform {platform}")
            sys.exit(1)
        
        analyzer = SDKMappingAnalyzer(platform, sdk_module, Path(openapi_spec))
        report = analyzer.generate_report()
        
        print(json.dumps(report, indent=2))
    else:
        # Analyze all platforms
        analyze_all_platforms()