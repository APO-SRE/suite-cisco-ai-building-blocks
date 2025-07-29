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
            # ========== Device Management Operations ==========
            "listAllDevices": "⭐ PRIMARY function to list all devices in the SD-WAN fabric (routers, switches, controllers). Use for queries like 'list devices', 'show devices', 'get devices', 'device list', 'sdwan devices', or 'list all devices'.",
            "getAllDeviceStatus": "⭐ PRIMARY function to get current operational status of all SD-WAN devices (reachability, sync status). Shows device states, connectivity, and synchronization status.",
            
            # ========== Alarm/Alert Operations ==========
            "getRawAlarmData": "⭐ PRIMARY function to get raw/all alarms - complete alarm history without filtering. This is the most general alarm function. Use for queries like 'alarms', 'all alarms', 'get all alarms', 'alarm list', 'show alarms', 'raw alarms', or 'alarm history'.",
            "getActiveAlarms": "Get only currently active alarms - filtered subset of alarms. More specific than getRawAlarmData. Use for queries like 'active alarms', 'current alarms', 'open alarms', or 'list active alarms'.",
            
            # ========== User Management Operations ==========
            "findUsers_1": "⭐ PRIMARY function to list all users configured in the SD-WAN management system. Use for queries like 'users', 'get users', 'user list', 'show users', 'sdwan users', or 'list users'.",
            
            # ========== Site/Location Operations ==========
            "getSites": "⭐ PRIMARY function to list all sites in the SD-WAN overlay network (branch offices, data centers, etc.). Use for queries like 'sites', 'get sites', 'site list', 'show sites', 'sdwan sites', 'list sites', or 'locations'.",
            
            # ========== Policy Management Operations ==========
            "getAllPolicyLists": "⭐ PRIMARY function to retrieve all configured SD-WAN policies (app-aware routing, security, QoS). Use for queries like 'policies', 'get policies', 'policy list', 'sdwan policies', 'show policies', or 'list policies'.",
            
            # ========== Health Monitoring Operations ==========
            "getDevicesHealth": "⭐ PRIMARY function to check health status of all SD-WAN devices (CPU, memory, tunnel status). Use for queries like 'device health', 'get device health', 'health check', 'show device health', 'health status', or 'check health'.",
            
            # ========== Software Version Management ==========
            "findSoftwareVersion": "⭐ PRIMARY function to list all available software versions in the SD-WAN controller repository. Use for queries like 'software versions', 'get software versions', 'version list', 'show versions', 'available versions', or 'list versions'.",
            "findVEdgeSoftwareVersion": "List software versions specifically for vEdge devices (virtual edge routers). Use for queries like 'vedge versions', 'get vedge versions', 'edge software versions', 'vedge software list', or 'edge versions'.",
            
            # ========== Network Segmentation Operations ==========
            "getSegment": "⭐ PRIMARY function to get network segments/VPNs configured in SD-WAN (VPN 0, VPN 512, service VPNs). Use for queries like 'segments', 'networks', 'get segments', 'network segments', 'show segments', 'vpn list', 'sdwan vpns', or 'list vpns'.",
            
            # --- Additional Operations (not in aliases.py) ---
            "getAllSites": "Alternative function to get all configured sites. See getSites for primary site listing function.",
            
        }
    },
    
    "nexushyperfabric": {
        # SDK filtering is disabled by default (no enable_sdk_filtering specified)
        "blocklist": set(),
        "descriptions": {},
    },
    
    # Add other platforms here as needed
}