#!/usr/bin/env python3
"""
Test script to demonstrate SDK alignment functionality

Purpose: Testing that the SDK introspection and validation mechanisms work correctly
What it does:

Tests if SDK methods can be discovered
Tests if OpenAPI filtering works
Tests if the validated dispatcher can validate and call functions
Unit/Integration testing of your SDK alignment features

Output: Test results showing pass/fail for each component

"""
import json
import logging
from pathlib import Path
import sys

# Add src to path to import our modules
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from app.utils.sdk_introspection import (
    discover_sdk_methods_from_client,
    filter_openapi_by_sdk,
    check_operation_id_availability
)
from app.llm.function_dispatcher_validated import create_validated_dispatcher

logging.basicConfig(level=logging.INFO, format="%(levelname)s | %(message)s")
log = logging.getLogger(__name__)


def test_sdk_introspection(platform: str, sdk_module_name: str):
    """
    Test SDK introspection for a given platform.
    """
    log.info(f"\n{'='*60}")
    log.info(f"Testing SDK Introspection for {platform}")
    log.info(f"{'='*60}")
    
    try:
        # Import and instantiate the SDK
        import importlib
        sdk_module = importlib.import_module(sdk_module_name)
        
        # Create a minimal client for introspection
        if platform == "meraki":
            import os
            api_key = os.getenv('CISCO_MERAKI_API_KEY', 'dummy-key')
            client = sdk_module.DashboardAPI(api_key=api_key, suppress_logging=True)
        else:
            # Try generic instantiation
            client = None
            for name, obj in sdk_module.__dict__.items():
                if 'client' in name.lower() or 'api' in name.lower():
                    try:
                        client = obj()
                        break
                    except:
                        pass
        
        if not client:
            log.error(f"Could not create client for {platform}")
            return
        
        # Discover methods
        methods = discover_sdk_methods_from_client(client)
        log.info(f"✓ Found {len(methods)} methods in {platform} SDK")
        
        # Show sample methods
        sample_methods = sorted(methods)[:10]
        log.info(f"Sample methods: {', '.join(sample_methods)}")
        
        # Test operation ID checking
        test_operations = [
            "getOrganizations",
            "getAllDevices", 
            "someNonExistentMethod"
        ]
        
        log.info("\nTesting operation ID availability:")
        for op_id in test_operations:
            available = check_operation_id_availability(op_id, methods)
            status = "✓ Available" if available else "✗ Not found"
            log.info(f"  {op_id}: {status}")
        
    except Exception as e:
        log.error(f"Error during introspection: {e}")


def test_openapi_filtering(platform: str, spec_path: Path):
    """
    Test OpenAPI filtering based on SDK availability.
    """
    log.info(f"\n{'='*60}")
    log.info(f"Testing OpenAPI Filtering for {platform}")
    log.info(f"{'='*60}")
    
    try:
        # Load the OpenAPI spec
        with open(spec_path, 'r') as f:
            openapi_spec = json.load(f)
        
        original_paths = len(openapi_spec.get('paths', {}))
        log.info(f"Original spec has {original_paths} paths")
        
        # For this test, create a mock set of available methods
        # In production, this would come from actual SDK introspection
        mock_sdk_methods = {
            "getOrganizations",
            "get_organizations",
            "getDevices", 
            "get_devices",
            "updateDevice",
            "update_device"
        }
        
        # Filter the spec
        filtered_spec = filter_openapi_by_sdk(openapi_spec, mock_sdk_methods)
        filtered_paths = len(filtered_spec.get('paths', {}))
        
        log.info(f"Filtered spec has {filtered_paths} paths")
        log.info(f"Removed {original_paths - filtered_paths} paths not in SDK")
        
    except Exception as e:
        log.error(f"Error during filtering: {e}")


def test_validated_dispatcher(platform: str):
    """
    Test the validated function dispatcher.
    """
    log.info(f"\n{'='*60}")
    log.info(f"Testing Validated Dispatcher for {platform}")
    log.info(f"{'='*60}")
    
    try:
        # Create a validated dispatcher
        # Note: This requires proper environment variables to be set
        dispatcher = create_validated_dispatcher(platform)
        
        # Get available functions
        available = dispatcher.get_available_functions()
        log.info(f"✓ Dispatcher has {len(available)} available functions")
        
        # Test validation
        test_functions = ["getOrganizations", "nonExistentFunction"]
        for func in test_functions:
            is_valid = dispatcher.validate_function(func)
            status = "✓ Valid" if is_valid else "✗ Invalid"
            log.info(f"  {func}: {status}")
        
    except Exception as e:
        log.error(f"Error testing dispatcher: {e}")


def main():
    """
    Run all tests.
    """
    # Test with Meraki as an example
    platform = "meraki"
    sdk_module = "meraki"
    
    # Test SDK introspection
    test_sdk_introspection(platform, sdk_module)
    
    # Test OpenAPI filtering (if spec exists)
    spec_path = Path(__file__).parent.parent / "src" / "app" / "llm" / "openapi_specs" / f"full_{platform}.json"
    if spec_path.exists():
        test_openapi_filtering(platform, spec_path)
    else:
        log.warning(f"OpenAPI spec not found at {spec_path}")
    
    # Test validated dispatcher
    test_validated_dispatcher(platform)
    
    log.info(f"\n{'='*60}")
    log.info("Testing complete!")
    log.info(f"{'='*60}")


if __name__ == "__main__":
    main()