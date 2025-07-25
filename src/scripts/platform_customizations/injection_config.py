#!/usr/bin/env python3
#src/scripts/platform_customizations/injection_config.py
"""
Parameter injection configuration for platforms.

This module defines all parameters that are automatically injected by the
dispatcher. By listing them here, we can ensure they are marked as optional
for the LLM, allowing the injection logic to work seamlessly.
"""

INJECTION_CONFIG = {
    "meraki": {
        "env_var": "MERAKI_ORG_ID",
        "params": {
            # Parameter Name -> Value to Inject
            "organizationId": "{value}",
            "organization_id": "{value}",
            "org_id": "{value}",
        }
    },
    "intersight": {
        "env_var": "INTERSIGHT_ORGANIZATION_MOID",
        "params": {
            "organization_moid": "{value}",
            "$filter": "Organization.Moid eq '{value}'",
            "filter": "Organization.Moid eq '{value}'",
        }
    },
}