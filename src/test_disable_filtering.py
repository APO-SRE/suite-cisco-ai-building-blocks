#!/usr/bin/env python3
"""Test SD-WAN with SDK filtering disabled"""
import sys
sys.path.insert(0, '.')

from scripts.platform_scaffolder import PLATFORM_OVERRIDES

# Check the configuration
sdwan_config = PLATFORM_OVERRIDES.get('sdwan_mngr', {})
print("SD-WAN Configuration:")
print(f"  disable_sdk_filtering: {sdwan_config.get('disable_sdk_filtering', False)}")
print(f"  blocklist: {sdwan_config.get('blocklist', set())}")
print(f"  descriptions: {len(sdwan_config.get('descriptions', {}))} entries")

print("\nWith SDK filtering disabled, the scaffolder should generate ALL operations from the OpenAPI spec.")
print("This means you should get all 2,151 GET operations (not just 18).")

print("\nTo re-run the scaffolder with the new configuration:")
print("python3 scripts/platform_scaffolder.py --platform sdwan_mngr --sdk-module catalystwan --openapi-spec source_open_api/cisco_catalyst_sd_wan_manager_api_2_0_0.yaml --include-http-methods GET")

print("\nOr to get ALL operations (not just GET):")
print("python3 scripts/platform_scaffolder.py --platform sdwan_mngr --sdk-module catalystwan --openapi-spec source_open_api/cisco_catalyst_sd_wan_manager_api_2_0_0.yaml")