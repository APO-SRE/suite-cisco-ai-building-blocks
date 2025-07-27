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
    
    # 3-d. hand-crafted aliases for SD-WAN operations
    # Makes common queries more intuitive for the LLM
    if platform.lower() == 'sdwan_mngr':
        # Device operations
        if fn['name'] == 'listAllDevices':
            for alias in {'devices', 'get_devices', 'device_list', 'show_devices'}:
                lines.extend([
                    f"# alias for {fn['name']} -> {alias}",
                    f"register('{alias}')(globals()['{safe_name}'])",
                    ""
                ])
        
        # Alarm operations
        elif fn['name'] == 'getRawAlarmData':
            for alias in {'alarms', 'get_alarms', 'alarm_list', 'show_alarms'}:
                lines.extend([
                    f"# alias for {fn['name']} -> {alias}",
                    f"register('{alias}')(globals()['{safe_name}'])",
                    ""
                ])
        
        # User operations
        elif fn['name'] == 'findUsers_1':
            for alias in {'users', 'get_users', 'user_list', 'show_users'}:
                lines.extend([
                    f"# alias for {fn['name']} -> {alias}",
                    f"register('{alias}')(globals()['{safe_name}'])",
                    ""
                ])
        
        # Template operations
        elif fn['name'] == 'getAllDeviceTemplates':
            for alias in {'templates', 'get_templates', 'template_list', 'device_templates'}:
                lines.extend([
                    f"# alias for {fn['name']} -> {alias}",
                    f"register('{alias}')(globals()['{safe_name}'])",
                    ""
                ])
        
        # Site operations
        elif fn['name'] == 'getAllSites':
            for alias in {'sites', 'get_sites', 'site_list', 'show_sites'}:
                lines.extend([
                    f"# alias for {fn['name']} -> {alias}",
                    f"register('{alias}')(globals()['{safe_name}'])",
                    ""
                ])
        
        # Policy operations
        elif fn['name'] == 'getAllVedgePolicies':
            for alias in {'policies', 'get_policies', 'policy_list', 'vedge_policies'}:
                lines.extend([
                    f"# alias for {fn['name']} -> {alias}",
                    f"register('{alias}')(globals()['{safe_name}'])",
                    ""
                ])
        
        # Health operations
        elif fn['name'] == 'getSiteHealth':
            for alias in {'site_health', 'get_site_health', 'health_sites', 'show_site_health'}:
                lines.extend([
                    f"# alias for {fn['name']} -> {alias}",
                    f"register('{alias}')(globals()['{safe_name}'])",
                    ""
                ])
        
        elif fn['name'] == 'getDevicesHealth':
            for alias in {'device_health', 'get_device_health', 'health_devices', 'show_device_health'}:
                lines.extend([
                    f"# alias for {fn['name']} -> {alias}",
                    f"register('{alias}')(globals()['{safe_name}'])",
                    ""
                ])
        
        # Network operations
        elif fn['name'] == 'getSegment':
            for alias in {'segment', 'get_segment', 'network_segment', 'show_segment', "get_network","list_network"}:
                lines.extend([
                    f"# alias for {fn['name']} -> {alias}",
                    f"register('{alias}')(globals()['{safe_name}'])",
                    ""
                ])
        
        elif fn['name'] == 'getTopology':
            for alias in {'topology', 'get_topology', 'network_topology', 'show_topology'}:
                lines.extend([
                    f"# alias for {fn['name']} -> {alias}",
                    f"register('{alias}')(globals()['{safe_name}'])",
                    ""
                ])
        
        # Device status operations
        elif fn['name'] == 'getAllDeviceStatus':
            for alias in {'device_status', 'get_device_status', 'status_devices', 'show_device_status'}:
                lines.extend([
                    f"# alias for {fn['name']} -> {alias}",
                    f"register('{alias}')(globals()['{safe_name}'])",
                    ""
                ])
        
        elif fn['name'] == 'getDeviceDetails':
            for alias in {'device_details', 'get_device_details', 'device_info', 'show_device_details'}:
                lines.extend([
                    f"# alias for {fn['name']} -> {alias}",
                    f"register('{alias}')(globals()['{safe_name}'])",
                    ""
                ])
    
    return lines