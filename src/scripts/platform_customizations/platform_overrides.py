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
            "getDeviceList": "⭐ PRIMARY function to list all devices in the catalyst network (routers, switches, controllers). Use for queries like 'list devices', 'show devices', 'get devices', 'device list', 'catalyst devices', or 'list all devices'.,To get all devices, call this function with no parameters. You can also filter by a specific 'hostname', 'macAddress', or 'serialNumber'.",
            "getAllInterfaces": "⭐ PRIMARY function to get a list of interfaces for a *specific* network device. You MUST ask the user for a device ID or hostname first, as it is required.",
            "getNotifications": "⭐ PRIMARY function to get notification events from Catalyst Center. IMPORTANT: When user asks for 'catalyst notifications', call this function WITHOUT any parameters. The 'category' parameter is for filtering notification categories (e.g., 'SYSTEM', 'NETWORK', 'APPLICATION') - NOT for platform names like 'catalyst'.",
            "getProject_s_Details": "⭐ PRIMARY function to get details of projects in Catalyst Center. Use for queries like 'project details', 'show projects', 'get projects', 'project list', or 'catalyst projects'.",
            "getPhysicalTopology": "⭐ PRIMARY function to get the physical network topology showing device connections and relationships. Use for queries like 'network topology', 'physical topology', 'show topology', 'device connections', or 'network map'.",
            "getApplicationPolicy": "⭐ PRIMARY function to get application policies configured in Catalyst Center. Use for queries like 'application policies', 'app policies', 'show policies', 'get application policy', or 'policy list'.",
            "getSites": "⭐ PRIMARY function to get all sites configured in Catalyst Center (buildings, floors, areas). Use for queries like 'sites', 'get sites', 'site list', 'show sites', 'catalyst sites', or 'locations'.",
            "getSiteHealth": "⭐ PRIMARY function to get health status of sites in the network. Use for queries like 'site health', 'get site health', 'health status', 'site status', or 'show site health'.",
            "ciscoDNACenterPackagesSummary": "⭐ PRIMARY function to get summary of installed packages and software components in Catalyst Center. Use for queries like 'package summary', 'installed packages', 'software packages', 'system packages', or 'dnac packages'.",
            "ciscoDNACenterReleaseSummary": "⭐ PRIMARY function to get release/version information of Catalyst Center. Use for queries like 'release info', 'version info', 'dnac version', 'catalyst version', 'software release', or 'system version'.",
            "ciscoDNACenterNodesConfigurationSummary": "⭐ PRIMARY function to get configuration summary of Catalyst Center nodes/cluster. Use for queries like 'config summary', 'node configuration', 'cluster config', 'dnac config', 'system configuration', or 'nodes config'."
        },
        # Add any operation_id_map entries needed for Catalyst here
        "operation_id_map": {
            # "getUsersAPI": "get_users", # Example
            "ciscoDNACenterPackagesSummary": "cisco_dna_center_packages_summary",
            "ciscoDNACenterReleaseSummary": "release_summary",
        },
        # Parameter safelist to drastically reduce the number of exposed parameters
        # Only include the most common and reliable parameters for each function
        "parameter_safelist": {
            "getDeviceList": [
                "hostname", "managementIpAddress", "macAddress", 
                "serialNumber", "id", "limit", "offset"
            ],
            "getDeviceByID": ["id"],
            "getNetworkDeviceById": ["id"],
            "getDeviceDetail": ["searchBy", "identifier"],
            "getDeviceInterfaceCount": ["deviceId"],
            "getModules": ["deviceId", "limit", "offset"],
            "getStackDetailsForDevice": ["deviceId"],
            "getAllInterfaces": ["deviceId", "limit", "offset"],
            "getInterfaceDetailsByDeviceIdAndInterfaceName": ["deviceId", "name"],
            "getDeviceConfigById": ["networkDeviceId"],
            "getRunningConfig": ["networkDeviceId"],
            "getNotifications": [
                "eventIds", "startTime", "endTime", "severity", 
                "domain", "subDomain", "source", "offset", "limit", 
                "sortBy", "order", "tags", "namespace", "siteId"
                # Intentionally excluding 'category' and 'type' to avoid confusion
            ],
            # Add more functions and their safelists as needed
        }
    },
    "meraki": {
        # Enable SDK filtering for Meraki (opt-in)
        "enable_sdk_filtering": True,
        "blocklist": set(), # No blocked functions for Meraki yet
        "descriptions": {
            "getOrganizationAssuranceAlerts": "⭐ PRIMARY function to get assurance alerts for the organization. Use for queries like 'alerts', 'get alerts', 'assurance alerts', 'organization alerts', 'meraki alerts', or 'show alerts'.",
            "getOrganizationDevices": "⭐ PRIMARY function to list all devices in the Meraki organization. Use for queries like 'devices', 'list devices', 'get devices', 'organization devices', 'meraki devices', or 'show all devices'.",
            "getOrganizationInventoryDevices": "⭐ PRIMARY function to get inventory of all devices including unclaimed devices. Use for queries like 'inventory', 'device inventory', 'get inventory', 'unclaimed devices', 'all inventory', or 'show inventory'.",
            "getOrganizationPolicyObjects": "⭐ PRIMARY function to get policy objects configured in the organization. Use for queries like 'policy objects', 'get policies', 'organization policies', 'meraki policies', 'policy list', or 'show policies'.",
            "getOrganizationAdmins": "⭐ PRIMARY function to list all administrators in the organization. Use for queries like 'admins', 'administrators', 'get admins', 'organization admins', 'admin list', or 'show admins'.",
            "getAdministeredIdentitiesMe": "⭐ PRIMARY function to get identity information about the current authenticated user. Use for queries like 'my identity', 'who am i', 'current user', 'my info', 'my profile', or 'authenticated user'."
        },
    },
    
    "intersight": {
        "blocklist": {
            # Block this so only the alias version exists
            "GetServerProfileList"
        },
        "descriptions": {
            "GetComputePhysicalSummaryList": "⭐ PRIMARY function to get list of all physical servers (compute nodes) in your infrastructure. Use this to retrieve server inventory, hardware details, and server status. This is the primary function for listing servers, server list, getting all servers, listing compute servers, or listing intersight servers. Keywords: servers, compute, physical, inventory, list servers, intersight servers.",
            "GetServerProfileList": "Get list of server configuration profiles/templates. These are policies applied to servers, NOT the actual physical servers themselves.",
            "GetComputeRackUnitList": "Get list of rack-mounted servers. Use this for rack servers specifically, not blade servers.",
            "GetComputeBladeList": "Get list of blade servers in chassis. Use this for blade servers specifically, not rack servers.",
            "GetCondAlarmList": "⭐ PRIMARY function to get list of condition alarms across the infrastructure. Use for queries like 'alarms', 'get alarms', 'alarm list', 'condition alarms', 'show alarms', or 'infrastructure alarms'.",
            "GetMonitoringHealthStatusList": "⭐ PRIMARY function to get health monitoring status of infrastructure components. Use for queries like 'health status', 'monitoring status', 'infrastructure health', 'system health', 'health check', or 'show health'.",
            "GetHciAlarmList": "⭐ PRIMARY function to get HyperConverged Infrastructure (HCI) specific alarms. Use for queries like 'hci alarms', 'hyperflex alarms', 'hyperconverged alarms', 'hci alerts', or 'show hci alarms'.",
            "GetTechsupportmanagementTechSupportStatusList": "⭐ PRIMARY function to get technical support status and collection information. Use for queries like 'tech support', 'support status', 'techsupport', 'support collection', 'tac status', or 'show tech support'.",
            "GetLicenseLicenseRegistrationStatusList": "⭐ PRIMARY function to get license registration status. Use for queries like 'license status', 'registration status', 'licensing', 'license info', 'show licenses', or 'license registration'.",
            "GetComputeServerSettingList": "⭐ PRIMARY function to get server settings and configurations. Use for queries like 'server settings', 'compute settings', 'server configuration', 'server config', 'show settings', or 'server setup'.",
            "GetNetworkElementList": "⭐ PRIMARY function to get list of network elements (switches, fabric interconnects). Use for queries like 'network elements', 'network devices', 'switches', 'fabric interconnects', 'fi list', or 'network components'.",
            "GetPowerPolicyList": "⭐ PRIMARY function to get power policies configured in the system. Use for queries like 'power policies', 'power settings', 'power configuration', 'energy policies', 'power management', or 'show power policies'.",
            "GetIamUserList": "⭐ PRIMARY function to get list of IAM users in Intersight. Use for queries like 'users', 'user list', 'iam users', 'get users', 'show users', or 'intersight users'."
        },
        # Intersight doesn't need operation_id_map because the SDK follows a consistent
        # PascalCase -> snake_case pattern that's handled automatically by the client
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