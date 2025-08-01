#!/usr/bin/env python3
#src/scripts/platform_customizations/aliases.py
"""
Alias generation logic for platform functions.

This module contains the logic for generating function aliases to help the LLM
understand and access functions more easily.
"""

def generate_aliases(fn: dict, safe_name: str, platform: str) -> list[str]:
    """
    Generate alias registration code for a given function.
    
    Args:
        fn: Function definition dict
        safe_name: Safe Python function name
        platform: Platform name
        
    Returns:
        List of code lines for alias registration
    """
    lines = []
    
    # 3.a - generic "drop‑tag / singular" aliases
    # This is a generic alias creation that strips the platform tag or makes it singular.
    # Automatically create aliases by stripping the platform tag or making it singular. 
    # For instance add aliases for easier LLM use (e.g. "get_device" → "device_get", OR device) 
    if '_' in fn['name']:
        tag, rest = fn['name'].split('_', 1)
        for alias in {rest, rest.rstrip('s')}:
            if alias and alias != fn['name']:
                lines.extend([
                    "# alias → easier for LLM",
                    f"register('{alias}')(globals()['{safe_name}'])",
                    ""
                ])

    # 3‑b. hand‑crafted aliases for server inventory (INTERSIGHT)
    # maps get_compute_physical_summary_list → get_server_list / servers …
    if fn['name'] == 'get_compute_physical_summary_list' or fn['name'] == 'GetComputePhysicalSummaryList':
        for alias in {'get_server_list', 'server_list', 'servers', 'GetServerList', 'GetServerProfileList'}:
            lines.extend([
                f"register('{alias}')(globals()['{safe_name}'])",
                ""
            ])
    
    # 3-c. hand-crafted aliases for Catalyst interfaces
    # This makes the LLM much more likely to choose the correct function.
    if fn['name'] == 'getAllInterfaces':
        for alias in {'list_interfaces', 'get_interfaces', 'show_interfaces', 'interfaces'}:
            lines.extend([
                f"# alias for {fn['name']} -> {alias}",
                f"register('{alias}')(globals()['{safe_name}'])",
                ""
            ])
    
    # 3-d. hand-crafted aliases for Catalyst system functions
    # Makes system queries more intuitive for the LLM
    if fn['name'] == 'ciscoDNACenterPackagesSummary':
        for alias in {'center_packages_summary','dnac_center_packages_summary','dnac_package_summary','system_summary', 'system_package_summary', 'system_packages', 'package_summary', 'packages_summary', 'packages'}:
            lines.extend([
                f"# alias for {fn['name']} -> {alias}",
                f"register('{alias}')(globals()['{safe_name}'])",
                ""
            ])
    
    if fn['name'] == 'ciscoDNACenterReleaseSummary':
        for alias in {'release_info', 'software_release', 'dnac_release_info', 'system_version', 'dnac_version', 'center_version', 'release_details', 'software_info', 'dnac_software_release', 'current_release'}:
            lines.extend([
                f"# alias for {fn['name']} -> {alias}",
                f"register('{alias}')(globals()['{safe_name}'])",
                ""
            ])
    
    # 3-e. hand-crafted aliases for Catalyst node configuration summary
    if fn['name'] == 'ciscoDNACenterNodesConfigurationSummary':
        for alias in {'config_summary', 'configuration_summary', 'node_config_summary', 'nodes_config', 'dnac_config_summary', 'center_config_summary', 'system_config', 'cluster_config'}:
            lines.extend([
                f"# alias for {fn['name']} -> {alias}",
                f"register('{alias}')(globals()['{safe_name}'])",
                ""
            ])
    
    # 3-f. hand-crafted aliases for Catalyst device health functions
    if fn['name'] == 'getSiteHealth':
        for alias in {'site_health', 'get_site_health', 'show_site_health', 'health_by_site', 'site_health_status'}:
            lines.extend([
                f"# alias for {fn['name']} -> {alias}",
                f"register('{alias}')(globals()['{safe_name}'])",
                ""
            ])
    
    # 3-g. hand-crafted aliases for Catalyst device status functions  
    if fn['name'] == 'getNetworkDevicesCredentialsSyncStatus':
        for alias in {'device_credential_status', 'credential_sync_status', 'device_sync_status', 'credentials_status'}:
            lines.extend([
                f"# alias for {fn['name']} -> {alias}",
                f"register('{alias}')(globals()['{safe_name}'])",
                ""
            ])
    
    # 3-h. hand-crafted aliases for Catalyst device details
    if fn['name'] == 'getDeviceById':
        for alias in {'device_details', 'get_device_details', 'device_info', 'show_device'}:
            lines.extend([
                f"# alias for {fn['name']} -> {alias}",
                f"register('{alias}')(globals()['{safe_name}'])",
                ""
            ])
    
    # 3-i. hand-crafted aliases for SD-WAN operations
    # Makes common queries more intuitive for the LLM
    if platform.lower() == 'sdwan_mngr':
        # ========== Device Management Operations ==========
        if fn['name'] == 'listAllDevices':
            # Lists all devices in the SD-WAN fabric (routers, switches, controllers)
            for alias in {'devices', 'get_devices', 'device_list', 'show_devices', 'sdwan_devices', 'list_devices'}:
                lines.extend([
                    f"# alias for {fn['name']} -> {alias}",
                    f"register('{alias}')(globals()['{safe_name}'])",
                    ""
                ])
        
        # ========== Alarm/Alert Operations ==========
        elif fn['name'] == 'getRawAlarmData':
            # Gets raw/all alarms - complete alarm history without filtering
            # This is the most general alarm function, so it gets the shortest aliases
            for alias in {'alarms', 'all_alarms', 'get_all_alarms', 'alarm_list', 'show_alarms', 'raw_alarms', 'alarm_history'}:
                lines.extend([
                    f"# alias for {fn['name']} -> {alias}",
                    f"register('{alias}')(globals()['{safe_name}'])",
                    ""
                ])
        
        elif fn['name'] == 'getActiveAlarms':
            # Gets only currently active alarms - filtered subset of alarms
            # More specific than getRawAlarmData, so uses qualified aliases
            for alias in {'active_alarms', 'get_active_alarms', 'list_active_alarms', 'show_active_alarms', 'current_alarms', 'open_alarms'}:
                lines.extend([
                    f"# alias for {fn['name']} -> {alias}",
                    f"register('{alias}')(globals()['{safe_name}'])",
                    ""
                ])

        # ========== User Management Operations ==========
        elif fn['name'] == 'findUsers_1':
            # Lists all users configured in the SD-WAN management system
            for alias in {'users', 'get_users', 'user_list', 'show_users', 'sdwan_users', 'list_users'}:
                lines.extend([
                    f"# alias for {fn['name']} -> {alias}",
                    f"register('{alias}')(globals()['{safe_name}'])",
                    ""
                ])
        
        # ========== Site/Location Operations ==========
        elif fn['name'] == 'getSites':
            # Lists all sites in the SD-WAN overlay network (branch offices, data centers, etc.)
            for alias in {'sites', 'get_sites', 'site_list', 'show_sites', 'sdwan_sites', 'list_sites', 'locations'}:
                lines.extend([
                    f"# alias for {fn['name']} -> {alias}",
                    f"register('{alias}')(globals()['{safe_name}'])",
                    ""
                ])
        
        # ========== Policy Management Operations ==========
        elif fn['name'] == 'getAllPolicyLists':
            # Retrieves all configured SD-WAN policies (app-aware routing, security, QoS)
            for alias in {'policies', 'get_policies', 'policy_list', 'sdwan_policies', 'show_policies', 'list_policies'}:
                lines.extend([
                    f"# alias for {fn['name']} -> {alias}",
                    f"register('{alias}')(globals()['{safe_name}'])",
                    ""
                ])
        
        # ========== Health Monitoring Operations ==========
        elif fn['name'] == 'getDevicesHealth':
            # Checks health status of all SD-WAN devices (CPU, memory, tunnel status)
            for alias in {'device_health', 'get_device_health', 'health_check', 'show_device_health', 'health_status', 'check_health'}:
                lines.extend([
                    f"# alias for {fn['name']} -> {alias}",
                    f"register('{alias}')(globals()['{safe_name}'])",
                    ""
                ])
        
        # ========== Software Version Management ==========
        elif fn['name'] == 'findSoftwareVersion':
            # Lists all available software versions in the SD-WAN controller repository
            for alias in {'software_versions', 'get_software_versions', 'version_list', 'show_versions', 'available_versions', 'list_versions'}:
                lines.extend([
                    f"# alias for {fn['name']} -> {alias}",
                    f"register('{alias}')(globals()['{safe_name}'])",
                    ""
                ])
        
        elif fn['name'] == 'findVEdgeSoftwareVersion':
            # Lists software versions specifically for vEdge devices (virtual edge routers)
            for alias in {'vedge_versions', 'get_vedge_versions', 'edge_software_versions', 'vedge_software_list', 'edge_versions'}:
                lines.extend([
                    f"# alias for {fn['name']} -> {alias}",
                    f"register('{alias}')(globals()['{safe_name}'])",
                    ""
                ])
        
        # ========== Network Segmentation Operations ==========
        elif fn['name'] == 'getSegment':
            # Gets network segments/VPNs configured in SD-WAN (VPN 0, VPN 512, service VPNs)
            for alias in {'segments', 'networks', 'get_segments', 'network_segments', 'show_segments', 'vpn_list', 'sdwan_vpns', 'list_vpns'}:
                lines.extend([
                    f"# alias for {fn['name']} -> {alias}",
                    f"register('{alias}')(globals()['{safe_name}'])",
                    ""
                ])
        
        # ========== Device Status Operations ==========
        elif fn['name'] == 'getAllDeviceStatus':
            # Gets current operational status of all SD-WAN devices (reachability, sync status)
            for alias in {'device_status', 'get_device_status', 'all_device_status', 'show_device_status', 'status_all_devices', 'device_states'}:
                lines.extend([
                    f"# alias for {fn['name']} -> {alias}",
                    f"register('{alias}')(globals()['{safe_name}'])",
                    ""
                ])
        

    
    return lines