#!/usr/bin/env python3
#src/scripts/platform_customizations/platform_overrides.py
"""
Platform-specific overrides and configurations.

This module contains all platform-specific rules and overrides that allow
customization of behavior for individual platforms without affecting others.
"""

PLATFORM_OVERRIDES = {
    "catalyst": {
        # SDK filtering is disabled by default (no enable_sdk_filtering specified)
        "blocklist": {
            # This operationId is ambiguous and unhelpful for Catalyst.
            "getInterfaces",
        },
        "descriptions": {
            # This makes the correct function much more attractive to the LLM.
            "getAllInterfaces": "Crucial for users asking to list, show, or get all network interfaces from all devices. This is the primary tool for interface inventory.",
        },
    },
    "meraki": {
        # Enable SDK filtering for Meraki (opt-in)
        "enable_sdk_filtering": True,
        "blocklist": set(), # No blocked functions for Meraki yet
        "descriptions": {}, # No description overrides for Meraki yet
    },
    
    "intersight": {
        "blocklist": {
            # Block this so only the alias version exists
            "GetServerProfileList"
        },
        "descriptions": {
            "GetComputePhysicalSummaryList": "Get list of all physical servers (compute nodes) in your infrastructure. Use this to retrieve server inventory, hardware details, and server status. This is the primary function for listing servers, server list, getting all servers, listing compute servers, or listing intersight servers. Keywords: servers, compute, physical, inventory, list servers, intersight servers.",
            "GetServerProfileList": "Get list of server configuration profiles/templates. These are policies applied to servers, NOT the actual physical servers themselves.",
            "GetComputeRackUnitList": "Get list of rack-mounted servers. Use this for rack servers specifically, not blade servers.",
            "GetComputeBladeList": "Get list of blade servers in chassis. Use this for blade servers specifically, not rack servers."
        },
        # Map PascalCase operation IDs to snake_case SDK methods
        "operation_id_map": {
            "GetComputePhysicalSummaryList": "get_compute_physical_summary_list",
            "GetComputePhysicalSummaryByMoid": "get_compute_physical_summary_by_moid",
            "GetComputeRackUnitList": "get_compute_rack_unit_list",
            "GetComputeBladeList": "get_compute_blade_list",
        },
        # Enable SDK filtering for Intersight (opt-in)
        "enable_sdk_filtering": True,
    },
    
    
    "sdwan_mngr": {
        "blocklist": set(),
        "descriptions": {
          
            # --- Alarm Operations ---
            "getRawAlarmData": "⭐ PRIMARY function to retrieve a list of all alarms from the SD-WAN system. Use for queries like 'list all alarms', 'show alarms', 'get alarms', or 'alarm list'.",
            "getActiveAlarms": "Get a list of only the currently active alarms.",
            "getAlarmsCount": "Get the total count of alarms, useful for dashboard summaries.",

            # --- Device Operations ---
            "listAllDevices": "⭐ PRIMARY function to get a basic inventory of all devices. Use for queries like 'list all devices', 'show devices', 'get devices', or 'device list'.",
            "getAllDeviceStatus": "⭐ PRIMARY function to get the operational status of all SD-WAN devices (vSmart, vBond, vEdge, cEdge). Shows health, reachability, and status.",
            "getDevicesDetails": "Get detailed configuration and operational information for SD-WAN devices.",
            "getDevicesHealth": "Get detailed health metrics for SD-WAN devices, ideal for troubleshooting.",

            # --- Network Operations ---
            "getSegment": "⭐ PRIMARY function to list all network segments (also known as VPNs or VRFs) in the SD-WAN fabric. Use this for queries like 'list all networks', 'show segments', or 'get all networks'.",

            # --- Policy Operations ---
            "getAllVedgePolicies": "⭐ PRIMARY function to get a list of all vEdge policies. Use for queries like 'list all policies', 'show policies', 'get policies', or 'policy list'.",
            "getApplicationAwareRoutingPolicyList": "Get a list of all Application-Aware Routing (AAR) policies.",
            "getControlPolicyList": "Get a list of all control policies.",

            # --- Site Operations ---
            "getAllSites": "⭐ PRIMARY function to get a list of all configured sites. Use for queries like 'list all sites', 'show sites', 'get sites', or 'site list'.",
            "getSiteHealth": "Get detailed health information for a specific site.",

            # --- Template Operations ---
            "getAllDeviceTemplates": "⭐ PRIMARY function to get a list of all device templates. Use for queries like 'list all templates', 'show templates', 'get templates', or 'device templates'.",
            "getFeatureTemplateList": "Get a list of all available feature templates in the system.",

            # --- User Operations ---
            "findUsers_1": "⭐ PRIMARY function to get a list of all administrative users configured in the SD-WAN system. Use for queries like 'list all users', 'show users', 'get users', or 'user list'.",
            "getAAAUsers": "Get a list of all AAA (Authentication, Authorization, and Accounting) users from a specific device in real-time."
        }
    },
    
    "nexushyperfabric": {
        # SDK filtering is disabled by default (no enable_sdk_filtering specified)
        "blocklist": set(),
        "descriptions": {},
    },
    
    # Add other platforms here as needed
}