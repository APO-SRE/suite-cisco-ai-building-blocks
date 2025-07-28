"""
SDK introspection and processing functions for the platform scaffolder.
"""

import logging
from typing import Optional, Dict, Any, Set
from pathlib import Path

log = logging.getLogger("scaffolder")


def perform_sdk_introspection(
    platform: str,
    platform_config: dict,
    enhanced_introspection: bool
) -> Optional[Dict[str, Any]]:
    """
    Perform SDK introspection if enhanced introspection is available and enabled.
    
    Returns:
        Dictionary with 'supported_operations' and 'coverage_report' if successful,
        None if introspection is disabled or fails.
    """
    if not enhanced_introspection:
        return None
        
    if not platform_config.get("enable_sdk_filtering", False):
        return None
    
    try:
        # Import here to avoid issues if not available
        from app.utils.sdk_introspection import SDKIntrospector
        
        log.info("🔍 Performing SDK introspection for %s...", platform)
        
        # Create introspector for the platform
        introspector = SDKIntrospector(platform=platform)
        
        # Get supported operations
        supported_ops = introspector.get_supported_operations()
        
        if not supported_ops:
            log.warning("SDK introspection found no supported operations")
            return None
        
        log.info("Found %d supported SDK operations", len(supported_ops))
        
        # Generate coverage report
        coverage_report = {
            'total_operations': len(supported_ops),
            'supported_operations': supported_ops,
            'platform': platform,
        }
        
        return {
            'supported_operations': supported_ops,
            'coverage_report': coverage_report
        }
        
    except Exception as e:
        log.warning(f"SDK introspection failed: {e}")
        return None


def filter_operations_by_sdk(
    operations: list,
    supported_operations: Set[str],
    platform: str
) -> list:
    """
    Filter operations to only include those supported by the SDK.
    
    Args:
        operations: List of OpenAPI operations
        supported_operations: Set of operation IDs supported by SDK
        platform: Platform name for logging
        
    Returns:
        Filtered list of operations
    """
    original_count = len(operations)
    filtered_ops = [
        op for op in operations 
        if op.get('operationId') in supported_operations
    ]
    filtered_count = len(filtered_ops)
    
    log.info(
        "SDK filtering for %s: %d/%d operations kept",
        platform, filtered_count, original_count
    )
    
    return filtered_ops


def write_coverage_report(platform: str, coverage_report: dict, out_dir: Path) -> None:
    """Write SDK coverage report to file."""
    coverage_file = out_dir / f"{platform}_sdk_coverage.json"
    
    try:
        import json
        coverage_file.parent.mkdir(parents=True, exist_ok=True)
        
        with open(coverage_file, 'w') as f:
            json.dump(coverage_report, f, indent=2)
            
        log.info("📊 Wrote SDK coverage report to %s", coverage_file.name)
        
    except Exception as e:
        log.warning(f"Failed to write coverage report: {e}")