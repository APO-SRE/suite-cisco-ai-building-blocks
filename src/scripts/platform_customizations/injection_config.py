#!/usr/bin/env python3
#src/scripts/platform_customizations/injection_config.py
"""
Parameter injection configuration for platforms.

This module defines all parameters that are automatically injected by the
dispatcher. By listing them here, we can ensure they are marked as optional
for the LLM, allowing the injection logic to work seamlessly.

HOW IT WORKS:
1. When you add a parameter to INJECTION_CONFIG below, the platform_scaffolder.py
   automatically modifies the OpenAPI schema during scaffolding.
   
2. The scaffolder (at lines 944-954 in platform_scaffolder.py) will:
   - Read the parameter names from this config for each platform
   - Remove these parameters from the 'required' list in the function schema
   - This makes the parameters optional for the LLM
   
3. At runtime, the dispatcher will inject these values from environment variables,
   so the LLM doesn't need to provide them.

EXAMPLE:
If you add "org_id" to the meraki config below, any function that requires
"org_id" will have it made optional during scaffolding, and the dispatcher
will automatically inject the value from MERAKI_ORG_ID env var.
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