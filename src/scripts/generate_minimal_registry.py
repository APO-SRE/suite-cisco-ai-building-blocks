#!/usr/bin/env python3
"""
Generate a minimal SD-WAN registry that only contains SDK mapping info,
without duplicating OpenAPI data that's already in the dispatcher.
"""
import json
from pathlib import Path

def generate_minimal_registry():
    """
    Create a minimal registry that only maps operation IDs to SDK methods.
    REST API calls will get their path/method info from the OpenAPI spec.
    """
    
    # Only store SDK mappings - no path/method duplication
    minimal_registry = {
        "comment": "Minimal SD-WAN Operation Registry - SDK mappings only",
        "sdk_mappings": {
            # Operations that use SDK
            "listAllDevices": {
                "sdk_endpoint": "devices",
                "sdk_method": "get"
            },
            "getAllDeviceStatus": {
                "sdk_endpoint": "devices", 
                "sdk_method": "get"
            },
            "getRawAlarmData": {
                "sdk_endpoint": "alarms",
                "sdk_method": "get"
            },
            "markAllAlarmsAsViewed": {
                "sdk_endpoint": "alarms",
                "sdk_method": "mark_all_as_viewed"
            },
            "findUserGroups": {
                "sdk_endpoint": "admin_tech.session.endpoints.administration_user_and_group",
                "sdk_method": "find_user_groups"
            },
            # Add more SDK mappings as discovered...
        }
    }
    
    # Save the minimal registry
    output_path = Path(__file__).parent.parent / "src" / "app" / "llm" / "sdwan_minimal_registry.json"
    with open(output_path, 'w') as f:
        json.dump(minimal_registry, f, indent=2)
    
    print(f"Generated minimal registry: {output_path}")
    return minimal_registry

if __name__ == "__main__":
    generate_minimal_registry()