# app/llm/function_dispatcher/meraki_dispatcher.py
import os
from typing import Any
from app.llm.function_dispatcher import register
from app.llm.platform_clients.meraki_client import MerakiClient

@register('getAdministeredIdentitiesMe')
def getAdministeredIdentitiesMe():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in [] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in [] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in [] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getAdministeredIdentitiesMe

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getAdministeredIdentitiesMeApiKeys')
def getAdministeredIdentitiesMeApiKeys():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in [] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in [] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in [] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getAdministeredIdentitiesMeApiKeys

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getAdministeredLicensingSubscriptionEntitlements')
def getAdministeredLicensingSubscriptionEntitlements(skus: list = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if skus is not None:
        final_kwargs['skus'] = skus

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['skus'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['skus'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['skus'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getAdministeredLicensingSubscriptionEntitlements

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getAdministeredLicensingSubscriptionSubscriptions')
def getAdministeredLicensingSubscriptionSubscriptions(perPage: int = None, startingAfter: str = None, endingBefore: str = None, subscriptionIds: list = None, organizationIds: list = None, statuses: list = None, productTypes: list = None, name: str = None, startDate: str = None, endDate: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if perPage is not None:
        final_kwargs['perPage'] = perPage
    if startingAfter is not None:
        final_kwargs['startingAfter'] = startingAfter
    if endingBefore is not None:
        final_kwargs['endingBefore'] = endingBefore
    if subscriptionIds is not None:
        final_kwargs['subscriptionIds'] = subscriptionIds
    if organizationIds is not None:
        final_kwargs['organizationIds'] = organizationIds
    if statuses is not None:
        final_kwargs['statuses'] = statuses
    if productTypes is not None:
        final_kwargs['productTypes'] = productTypes
    if name is not None:
        final_kwargs['name'] = name
    if startDate is not None:
        final_kwargs['startDate'] = startDate
    if endDate is not None:
        final_kwargs['endDate'] = endDate

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['perPage', 'startingAfter', 'endingBefore', 'subscriptionIds', 'organizationIds', 'statuses', 'productTypes', 'name', 'startDate', 'endDate'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['perPage', 'startingAfter', 'endingBefore', 'subscriptionIds', 'organizationIds', 'statuses', 'productTypes', 'name', 'startDate', 'endDate'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['perPage', 'startingAfter', 'endingBefore', 'subscriptionIds', 'organizationIds', 'statuses', 'productTypes', 'name', 'startDate', 'endDate'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getAdministeredLicensingSubscriptionSubscriptions

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getAdministeredLicensingSubscriptionSubscriptionsComplianceStatu')
def getAdministeredLicensingSubscriptionSubscriptionsComplianceStatu(organizationIds: list, subscriptionIds: list = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationIds is not None:
        final_kwargs['organizationIds'] = organizationIds
    if subscriptionIds is not None:
        final_kwargs['subscriptionIds'] = subscriptionIds

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationIds', 'subscriptionIds'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationIds', 'subscriptionIds'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationIds', 'subscriptionIds'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getAdministeredLicensingSubscriptionSubscriptionsComplianceStatu

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDevice')
def getDevice(serial: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if serial is not None:
        final_kwargs['serial'] = serial

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['serial'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['serial'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['serial'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getDevice

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceApplianceDhcpSubnets')
def getDeviceApplianceDhcpSubnets(serial: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if serial is not None:
        final_kwargs['serial'] = serial

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['serial'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['serial'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['serial'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getDeviceApplianceDhcpSubnets

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceAppliancePerformance')
def getDeviceAppliancePerformance(serial: str, t0: str = None, t1: str = None, timespan: float = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if serial is not None:
        final_kwargs['serial'] = serial
    if t0 is not None:
        final_kwargs['t0'] = t0
    if t1 is not None:
        final_kwargs['t1'] = t1
    if timespan is not None:
        final_kwargs['timespan'] = timespan

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['serial', 't0', 't1', 'timespan'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['serial', 't0', 't1', 'timespan'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['serial', 't0', 't1', 'timespan'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getDeviceAppliancePerformance

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceAppliancePrefixesDelegated')
def getDeviceAppliancePrefixesDelegated(serial: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if serial is not None:
        final_kwargs['serial'] = serial

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['serial'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['serial'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['serial'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getDeviceAppliancePrefixesDelegated

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceAppliancePrefixesDelegatedVlanAssignments')
def getDeviceAppliancePrefixesDelegatedVlanAssignments(serial: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if serial is not None:
        final_kwargs['serial'] = serial

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['serial'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['serial'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['serial'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getDeviceAppliancePrefixesDelegatedVlanAssignments

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceApplianceRadioSettings')
def getDeviceApplianceRadioSettings(serial: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if serial is not None:
        final_kwargs['serial'] = serial

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['serial'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['serial'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['serial'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getDeviceApplianceRadioSettings

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceApplianceUplinksSettings')
def getDeviceApplianceUplinksSettings(serial: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if serial is not None:
        final_kwargs['serial'] = serial

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['serial'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['serial'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['serial'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getDeviceApplianceUplinksSettings

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceCameraAnalyticsLive')
def getDeviceCameraAnalyticsLive(serial: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if serial is not None:
        final_kwargs['serial'] = serial

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['serial'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['serial'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['serial'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getDeviceCameraAnalyticsLive

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceCameraAnalyticsOverview')
def getDeviceCameraAnalyticsOverview(serial: str, t0: str = None, t1: str = None, timespan: float = None, objectType: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if serial is not None:
        final_kwargs['serial'] = serial
    if t0 is not None:
        final_kwargs['t0'] = t0
    if t1 is not None:
        final_kwargs['t1'] = t1
    if timespan is not None:
        final_kwargs['timespan'] = timespan
    if objectType is not None:
        final_kwargs['objectType'] = objectType

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['serial', 't0', 't1', 'timespan', 'objectType'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['serial', 't0', 't1', 'timespan', 'objectType'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['serial', 't0', 't1', 'timespan', 'objectType'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getDeviceCameraAnalyticsOverview

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceCameraAnalyticsRecent')
def getDeviceCameraAnalyticsRecent(serial: str, objectType: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if serial is not None:
        final_kwargs['serial'] = serial
    if objectType is not None:
        final_kwargs['objectType'] = objectType

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['serial', 'objectType'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['serial', 'objectType'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['serial', 'objectType'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getDeviceCameraAnalyticsRecent

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceCameraAnalyticsZones')
def getDeviceCameraAnalyticsZones(serial: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if serial is not None:
        final_kwargs['serial'] = serial

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['serial'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['serial'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['serial'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getDeviceCameraAnalyticsZones

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceCameraAnalyticsZoneHistory')
def getDeviceCameraAnalyticsZoneHistory(serial: str, zoneId: str, t0: str = None, t1: str = None, timespan: float = None, resolution: int = None, objectType: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if serial is not None:
        final_kwargs['serial'] = serial
    if zoneId is not None:
        final_kwargs['zoneId'] = zoneId
    if t0 is not None:
        final_kwargs['t0'] = t0
    if t1 is not None:
        final_kwargs['t1'] = t1
    if timespan is not None:
        final_kwargs['timespan'] = timespan
    if resolution is not None:
        final_kwargs['resolution'] = resolution
    if objectType is not None:
        final_kwargs['objectType'] = objectType

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['serial', 'zoneId', 't0', 't1', 'timespan', 'resolution', 'objectType'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['serial', 'zoneId', 't0', 't1', 'timespan', 'resolution', 'objectType'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['serial', 'zoneId', 't0', 't1', 'timespan', 'resolution', 'objectType'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getDeviceCameraAnalyticsZoneHistory

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceCameraCustomAnalytics')
def getDeviceCameraCustomAnalytics(serial: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if serial is not None:
        final_kwargs['serial'] = serial

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['serial'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['serial'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['serial'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getDeviceCameraCustomAnalytics

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceCameraQualityAndRetention')
def getDeviceCameraQualityAndRetention(serial: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if serial is not None:
        final_kwargs['serial'] = serial

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['serial'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['serial'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['serial'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getDeviceCameraQualityAndRetention

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceCameraSense')
def getDeviceCameraSense(serial: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if serial is not None:
        final_kwargs['serial'] = serial

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['serial'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['serial'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['serial'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getDeviceCameraSense

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceCameraSenseObjectDetectionModels')
def getDeviceCameraSenseObjectDetectionModels(serial: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if serial is not None:
        final_kwargs['serial'] = serial

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['serial'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['serial'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['serial'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getDeviceCameraSenseObjectDetectionModels

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceCameraVideoSettings')
def getDeviceCameraVideoSettings(serial: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if serial is not None:
        final_kwargs['serial'] = serial

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['serial'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['serial'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['serial'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getDeviceCameraVideoSettings

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceCameraVideoLink')
def getDeviceCameraVideoLink(serial: str, timestamp: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if serial is not None:
        final_kwargs['serial'] = serial
    if timestamp is not None:
        final_kwargs['timestamp'] = timestamp

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['serial', 'timestamp'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['serial', 'timestamp'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['serial', 'timestamp'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getDeviceCameraVideoLink

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceCameraWirelessProfiles')
def getDeviceCameraWirelessProfiles(serial: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if serial is not None:
        final_kwargs['serial'] = serial

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['serial'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['serial'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['serial'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getDeviceCameraWirelessProfiles

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceCellularSims')
def getDeviceCellularSims(serial: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if serial is not None:
        final_kwargs['serial'] = serial

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['serial'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['serial'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['serial'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getDeviceCellularSims

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceCellularGatewayLan')
def getDeviceCellularGatewayLan(serial: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if serial is not None:
        final_kwargs['serial'] = serial

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['serial'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['serial'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['serial'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getDeviceCellularGatewayLan

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceCellularGatewayPortForwardingRules')
def getDeviceCellularGatewayPortForwardingRules(serial: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if serial is not None:
        final_kwargs['serial'] = serial

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['serial'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['serial'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['serial'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getDeviceCellularGatewayPortForwardingRules

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceClients')
def getDeviceClients(serial: str, t0: str = None, timespan: float = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if serial is not None:
        final_kwargs['serial'] = serial
    if t0 is not None:
        final_kwargs['t0'] = t0
    if timespan is not None:
        final_kwargs['timespan'] = timespan

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['serial', 't0', 'timespan'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['serial', 't0', 'timespan'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['serial', 't0', 'timespan'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getDeviceClients

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceLiveToolsArpTable')
def getDeviceLiveToolsArpTable(serial: str, arpTableId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if serial is not None:
        final_kwargs['serial'] = serial
    if arpTableId is not None:
        final_kwargs['arpTableId'] = arpTableId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['serial', 'arpTableId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['serial', 'arpTableId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['serial', 'arpTableId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getDeviceLiveToolsArpTable

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceLiveToolsCableTest')
def getDeviceLiveToolsCableTest(serial: str, id: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if serial is not None:
        final_kwargs['serial'] = serial
    if id is not None:
        final_kwargs['id'] = id

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['serial', 'id'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['serial', 'id'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['serial', 'id'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getDeviceLiveToolsCableTest

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceLiveToolsLedsBlink')
def getDeviceLiveToolsLedsBlink(serial: str, ledsBlinkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if serial is not None:
        final_kwargs['serial'] = serial
    if ledsBlinkId is not None:
        final_kwargs['ledsBlinkId'] = ledsBlinkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['serial', 'ledsBlinkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['serial', 'ledsBlinkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['serial', 'ledsBlinkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getDeviceLiveToolsLedsBlink

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceLiveToolsPing')
def getDeviceLiveToolsPing(serial: str, id: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if serial is not None:
        final_kwargs['serial'] = serial
    if id is not None:
        final_kwargs['id'] = id

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['serial', 'id'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['serial', 'id'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['serial', 'id'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getDeviceLiveToolsPing

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceLiveToolsPingDevice')
def getDeviceLiveToolsPingDevice(serial: str, id: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if serial is not None:
        final_kwargs['serial'] = serial
    if id is not None:
        final_kwargs['id'] = id

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['serial', 'id'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['serial', 'id'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['serial', 'id'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getDeviceLiveToolsPingDevice

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceLiveToolsThroughputTest')
def getDeviceLiveToolsThroughputTest(serial: str, throughputTestId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if serial is not None:
        final_kwargs['serial'] = serial
    if throughputTestId is not None:
        final_kwargs['throughputTestId'] = throughputTestId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['serial', 'throughputTestId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['serial', 'throughputTestId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['serial', 'throughputTestId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getDeviceLiveToolsThroughputTest

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceLiveToolsWakeOnLan')
def getDeviceLiveToolsWakeOnLan(serial: str, wakeOnLanId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if serial is not None:
        final_kwargs['serial'] = serial
    if wakeOnLanId is not None:
        final_kwargs['wakeOnLanId'] = wakeOnLanId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['serial', 'wakeOnLanId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['serial', 'wakeOnLanId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['serial', 'wakeOnLanId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getDeviceLiveToolsWakeOnLan

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceLldpCdp')
def getDeviceLldpCdp(serial: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if serial is not None:
        final_kwargs['serial'] = serial

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['serial'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['serial'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['serial'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getDeviceLldpCdp

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceLossAndLatencyHistory')
def getDeviceLossAndLatencyHistory(serial: str, ip: str, t0: str = None, t1: str = None, timespan: float = None, resolution: int = None, uplink: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if serial is not None:
        final_kwargs['serial'] = serial
    if t0 is not None:
        final_kwargs['t0'] = t0
    if t1 is not None:
        final_kwargs['t1'] = t1
    if timespan is not None:
        final_kwargs['timespan'] = timespan
    if resolution is not None:
        final_kwargs['resolution'] = resolution
    if uplink is not None:
        final_kwargs['uplink'] = uplink
    if ip is not None:
        final_kwargs['ip'] = ip

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['serial', 't0', 't1', 'timespan', 'resolution', 'uplink', 'ip'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['serial', 't0', 't1', 'timespan', 'resolution', 'uplink', 'ip'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['serial', 't0', 't1', 'timespan', 'resolution', 'uplink', 'ip'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getDeviceLossAndLatencyHistory

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceManagementInterface')
def getDeviceManagementInterface(serial: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if serial is not None:
        final_kwargs['serial'] = serial

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['serial'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['serial'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['serial'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getDeviceManagementInterface

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceSensorCommands')
def getDeviceSensorCommands(serial: str, operations: list = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None, sortOrder: str = None, t0: str = None, t1: str = None, timespan: float = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if serial is not None:
        final_kwargs['serial'] = serial
    if operations is not None:
        final_kwargs['operations'] = operations
    if perPage is not None:
        final_kwargs['perPage'] = perPage
    if startingAfter is not None:
        final_kwargs['startingAfter'] = startingAfter
    if endingBefore is not None:
        final_kwargs['endingBefore'] = endingBefore
    if sortOrder is not None:
        final_kwargs['sortOrder'] = sortOrder
    if t0 is not None:
        final_kwargs['t0'] = t0
    if t1 is not None:
        final_kwargs['t1'] = t1
    if timespan is not None:
        final_kwargs['timespan'] = timespan

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['serial', 'operations', 'perPage', 'startingAfter', 'endingBefore', 'sortOrder', 't0', 't1', 'timespan'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['serial', 'operations', 'perPage', 'startingAfter', 'endingBefore', 'sortOrder', 't0', 't1', 'timespan'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['serial', 'operations', 'perPage', 'startingAfter', 'endingBefore', 'sortOrder', 't0', 't1', 'timespan'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getDeviceSensorCommands

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceSensorCommand')
def getDeviceSensorCommand(serial: str, commandId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if serial is not None:
        final_kwargs['serial'] = serial
    if commandId is not None:
        final_kwargs['commandId'] = commandId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['serial', 'commandId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['serial', 'commandId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['serial', 'commandId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getDeviceSensorCommand

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceSensorRelationships')
def getDeviceSensorRelationships(serial: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if serial is not None:
        final_kwargs['serial'] = serial

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['serial'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['serial'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['serial'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getDeviceSensorRelationships

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceSwitchPorts')
def getDeviceSwitchPorts(serial: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if serial is not None:
        final_kwargs['serial'] = serial

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['serial'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['serial'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['serial'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getDeviceSwitchPorts

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceSwitchPortsStatuses')
def getDeviceSwitchPortsStatuses(serial: str, t0: str = None, timespan: float = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if serial is not None:
        final_kwargs['serial'] = serial
    if t0 is not None:
        final_kwargs['t0'] = t0
    if timespan is not None:
        final_kwargs['timespan'] = timespan

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['serial', 't0', 'timespan'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['serial', 't0', 'timespan'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['serial', 't0', 'timespan'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getDeviceSwitchPortsStatuses

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceSwitchPortsStatusesPackets')
def getDeviceSwitchPortsStatusesPackets(serial: str, t0: str = None, timespan: float = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if serial is not None:
        final_kwargs['serial'] = serial
    if t0 is not None:
        final_kwargs['t0'] = t0
    if timespan is not None:
        final_kwargs['timespan'] = timespan

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['serial', 't0', 'timespan'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['serial', 't0', 'timespan'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['serial', 't0', 'timespan'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getDeviceSwitchPortsStatusesPackets

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceSwitchPort')
def getDeviceSwitchPort(serial: str, portId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if serial is not None:
        final_kwargs['serial'] = serial
    if portId is not None:
        final_kwargs['portId'] = portId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['serial', 'portId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['serial', 'portId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['serial', 'portId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getDeviceSwitchPort

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceSwitchRoutingInterfaces')
def getDeviceSwitchRoutingInterfaces(serial: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if serial is not None:
        final_kwargs['serial'] = serial

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['serial'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['serial'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['serial'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getDeviceSwitchRoutingInterfaces

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceSwitchRoutingInterface')
def getDeviceSwitchRoutingInterface(serial: str, interfaceId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if serial is not None:
        final_kwargs['serial'] = serial
    if interfaceId is not None:
        final_kwargs['interfaceId'] = interfaceId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['serial', 'interfaceId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['serial', 'interfaceId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['serial', 'interfaceId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getDeviceSwitchRoutingInterface

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceSwitchRoutingInterfaceDhcp')
def getDeviceSwitchRoutingInterfaceDhcp(serial: str, interfaceId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if serial is not None:
        final_kwargs['serial'] = serial
    if interfaceId is not None:
        final_kwargs['interfaceId'] = interfaceId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['serial', 'interfaceId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['serial', 'interfaceId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['serial', 'interfaceId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getDeviceSwitchRoutingInterfaceDhcp

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceSwitchRoutingStaticRoutes')
def getDeviceSwitchRoutingStaticRoutes(serial: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if serial is not None:
        final_kwargs['serial'] = serial

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['serial'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['serial'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['serial'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getDeviceSwitchRoutingStaticRoutes

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceSwitchRoutingStaticRoute')
def getDeviceSwitchRoutingStaticRoute(serial: str, staticRouteId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if serial is not None:
        final_kwargs['serial'] = serial
    if staticRouteId is not None:
        final_kwargs['staticRouteId'] = staticRouteId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['serial', 'staticRouteId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['serial', 'staticRouteId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['serial', 'staticRouteId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getDeviceSwitchRoutingStaticRoute

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceSwitchWarmSpare')
def getDeviceSwitchWarmSpare(serial: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if serial is not None:
        final_kwargs['serial'] = serial

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['serial'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['serial'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['serial'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getDeviceSwitchWarmSpare

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceWirelessBluetoothSettings')
def getDeviceWirelessBluetoothSettings(serial: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if serial is not None:
        final_kwargs['serial'] = serial

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['serial'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['serial'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['serial'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getDeviceWirelessBluetoothSettings

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceWirelessConnectionStats')
def getDeviceWirelessConnectionStats(serial: str, t0: str = None, t1: str = None, timespan: float = None, band: str = None, ssid: int = None, vlan: int = None, apTag: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if serial is not None:
        final_kwargs['serial'] = serial
    if t0 is not None:
        final_kwargs['t0'] = t0
    if t1 is not None:
        final_kwargs['t1'] = t1
    if timespan is not None:
        final_kwargs['timespan'] = timespan
    if band is not None:
        final_kwargs['band'] = band
    if ssid is not None:
        final_kwargs['ssid'] = ssid
    if vlan is not None:
        final_kwargs['vlan'] = vlan
    if apTag is not None:
        final_kwargs['apTag'] = apTag

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['serial', 't0', 't1', 'timespan', 'band', 'ssid', 'vlan', 'apTag'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['serial', 't0', 't1', 'timespan', 'band', 'ssid', 'vlan', 'apTag'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['serial', 't0', 't1', 'timespan', 'band', 'ssid', 'vlan', 'apTag'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getDeviceWirelessConnectionStats

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceWirelessElectronicShelfLabel')
def getDeviceWirelessElectronicShelfLabel(serial: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if serial is not None:
        final_kwargs['serial'] = serial

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['serial'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['serial'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['serial'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getDeviceWirelessElectronicShelfLabel

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceWirelessLatencyStats')
def getDeviceWirelessLatencyStats(serial: str, t0: str = None, t1: str = None, timespan: float = None, band: str = None, ssid: int = None, vlan: int = None, apTag: str = None, fields: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if serial is not None:
        final_kwargs['serial'] = serial
    if t0 is not None:
        final_kwargs['t0'] = t0
    if t1 is not None:
        final_kwargs['t1'] = t1
    if timespan is not None:
        final_kwargs['timespan'] = timespan
    if band is not None:
        final_kwargs['band'] = band
    if ssid is not None:
        final_kwargs['ssid'] = ssid
    if vlan is not None:
        final_kwargs['vlan'] = vlan
    if apTag is not None:
        final_kwargs['apTag'] = apTag
    if fields is not None:
        final_kwargs['fields'] = fields

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['serial', 't0', 't1', 'timespan', 'band', 'ssid', 'vlan', 'apTag', 'fields'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['serial', 't0', 't1', 'timespan', 'band', 'ssid', 'vlan', 'apTag', 'fields'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['serial', 't0', 't1', 'timespan', 'band', 'ssid', 'vlan', 'apTag', 'fields'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getDeviceWirelessLatencyStats

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceWirelessRadioSettings')
def getDeviceWirelessRadioSettings(serial: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if serial is not None:
        final_kwargs['serial'] = serial

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['serial'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['serial'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['serial'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getDeviceWirelessRadioSettings

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceWirelessStatus')
def getDeviceWirelessStatus(serial: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if serial is not None:
        final_kwargs['serial'] = serial

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['serial'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['serial'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['serial'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getDeviceWirelessStatus

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetwork')
def getNetwork(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetwork

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkAlertsHistory')
def getNetworkAlertsHistory(networkId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if perPage is not None:
        final_kwargs['perPage'] = perPage
    if startingAfter is not None:
        final_kwargs['startingAfter'] = startingAfter
    if endingBefore is not None:
        final_kwargs['endingBefore'] = endingBefore

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'perPage', 'startingAfter', 'endingBefore'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'perPage', 'startingAfter', 'endingBefore'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'perPage', 'startingAfter', 'endingBefore'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkAlertsHistory

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkAlertsSettings')
def getNetworkAlertsSettings(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkAlertsSettings

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkApplianceClientSecurityEvents')
def getNetworkApplianceClientSecurityEvents(networkId: str, clientId: str, t0: str = None, t1: str = None, timespan: float = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None, sortOrder: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if clientId is not None:
        final_kwargs['clientId'] = clientId
    if t0 is not None:
        final_kwargs['t0'] = t0
    if t1 is not None:
        final_kwargs['t1'] = t1
    if timespan is not None:
        final_kwargs['timespan'] = timespan
    if perPage is not None:
        final_kwargs['perPage'] = perPage
    if startingAfter is not None:
        final_kwargs['startingAfter'] = startingAfter
    if endingBefore is not None:
        final_kwargs['endingBefore'] = endingBefore
    if sortOrder is not None:
        final_kwargs['sortOrder'] = sortOrder

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'clientId', 't0', 't1', 'timespan', 'perPage', 'startingAfter', 'endingBefore', 'sortOrder'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'clientId', 't0', 't1', 'timespan', 'perPage', 'startingAfter', 'endingBefore', 'sortOrder'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'clientId', 't0', 't1', 'timespan', 'perPage', 'startingAfter', 'endingBefore', 'sortOrder'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkApplianceClientSecurityEvents

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkApplianceConnectivityMonitoringDestinations')
def getNetworkApplianceConnectivityMonitoringDestinations(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkApplianceConnectivityMonitoringDestinations

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkApplianceContentFiltering')
def getNetworkApplianceContentFiltering(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkApplianceContentFiltering

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkApplianceContentFilteringCategories')
def getNetworkApplianceContentFilteringCategories(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkApplianceContentFilteringCategories

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkApplianceFirewallCellularFirewallRules')
def getNetworkApplianceFirewallCellularFirewallRules(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkApplianceFirewallCellularFirewallRules

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkApplianceFirewallFirewalledServices')
def getNetworkApplianceFirewallFirewalledServices(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkApplianceFirewallFirewalledServices

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkApplianceFirewallFirewalledService')
def getNetworkApplianceFirewallFirewalledService(networkId: str, service: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if service is not None:
        final_kwargs['service'] = service

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'service'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'service'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'service'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkApplianceFirewallFirewalledService

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkApplianceFirewallInboundCellularFirewallRules')
def getNetworkApplianceFirewallInboundCellularFirewallRules(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkApplianceFirewallInboundCellularFirewallRules

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkApplianceFirewallInboundFirewallRules')
def getNetworkApplianceFirewallInboundFirewallRules(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkApplianceFirewallInboundFirewallRules

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkApplianceFirewallL3FirewallRules')
def getNetworkApplianceFirewallL3FirewallRules(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkApplianceFirewallL3FirewallRules

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkApplianceFirewallL7FirewallRules')
def getNetworkApplianceFirewallL7FirewallRules(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkApplianceFirewallL7FirewallRules

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkApplianceFirewallL7FirewallRulesApplicationCategories')
def getNetworkApplianceFirewallL7FirewallRulesApplicationCategories(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkApplianceFirewallL7FirewallRulesApplicationCategories

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkApplianceFirewallOneToManyNatRules')
def getNetworkApplianceFirewallOneToManyNatRules(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkApplianceFirewallOneToManyNatRules

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkApplianceFirewallOneToOneNatRules')
def getNetworkApplianceFirewallOneToOneNatRules(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkApplianceFirewallOneToOneNatRules

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkApplianceFirewallPortForwardingRules')
def getNetworkApplianceFirewallPortForwardingRules(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkApplianceFirewallPortForwardingRules

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkApplianceFirewallSettings')
def getNetworkApplianceFirewallSettings(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkApplianceFirewallSettings

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkAppliancePorts')
def getNetworkAppliancePorts(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkAppliancePorts

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkAppliancePort')
def getNetworkAppliancePort(networkId: str, portId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if portId is not None:
        final_kwargs['portId'] = portId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'portId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'portId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'portId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkAppliancePort

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkAppliancePrefixesDelegatedStatics')
def getNetworkAppliancePrefixesDelegatedStatics(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkAppliancePrefixesDelegatedStatics

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkAppliancePrefixesDelegatedStatic')
def getNetworkAppliancePrefixesDelegatedStatic(networkId: str, staticDelegatedPrefixId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if staticDelegatedPrefixId is not None:
        final_kwargs['staticDelegatedPrefixId'] = staticDelegatedPrefixId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'staticDelegatedPrefixId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'staticDelegatedPrefixId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'staticDelegatedPrefixId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkAppliancePrefixesDelegatedStatic

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkApplianceRfProfiles')
def getNetworkApplianceRfProfiles(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkApplianceRfProfiles

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkApplianceRfProfile')
def getNetworkApplianceRfProfile(networkId: str, rfProfileId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if rfProfileId is not None:
        final_kwargs['rfProfileId'] = rfProfileId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'rfProfileId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'rfProfileId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'rfProfileId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkApplianceRfProfile

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkApplianceSecurityEvents')
def getNetworkApplianceSecurityEvents(networkId: str, t0: str = None, t1: str = None, timespan: float = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None, sortOrder: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if t0 is not None:
        final_kwargs['t0'] = t0
    if t1 is not None:
        final_kwargs['t1'] = t1
    if timespan is not None:
        final_kwargs['timespan'] = timespan
    if perPage is not None:
        final_kwargs['perPage'] = perPage
    if startingAfter is not None:
        final_kwargs['startingAfter'] = startingAfter
    if endingBefore is not None:
        final_kwargs['endingBefore'] = endingBefore
    if sortOrder is not None:
        final_kwargs['sortOrder'] = sortOrder

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 't0', 't1', 'timespan', 'perPage', 'startingAfter', 'endingBefore', 'sortOrder'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 't0', 't1', 'timespan', 'perPage', 'startingAfter', 'endingBefore', 'sortOrder'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 't0', 't1', 'timespan', 'perPage', 'startingAfter', 'endingBefore', 'sortOrder'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkApplianceSecurityEvents

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkApplianceSecurityIntrusion')
def getNetworkApplianceSecurityIntrusion(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkApplianceSecurityIntrusion

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkApplianceSecurityMalware')
def getNetworkApplianceSecurityMalware(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkApplianceSecurityMalware

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkApplianceSettings')
def getNetworkApplianceSettings(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkApplianceSettings

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkApplianceSingleLan')
def getNetworkApplianceSingleLan(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkApplianceSingleLan

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkApplianceSsids')
def getNetworkApplianceSsids(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkApplianceSsids

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkApplianceSsid')
def getNetworkApplianceSsid(networkId: str, number: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if number is not None:
        final_kwargs['number'] = number

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'number'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'number'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'number'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkApplianceSsid

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkApplianceStaticRoutes')
def getNetworkApplianceStaticRoutes(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkApplianceStaticRoutes

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkApplianceStaticRoute')
def getNetworkApplianceStaticRoute(networkId: str, staticRouteId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if staticRouteId is not None:
        final_kwargs['staticRouteId'] = staticRouteId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'staticRouteId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'staticRouteId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'staticRouteId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkApplianceStaticRoute

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkApplianceTrafficShaping')
def getNetworkApplianceTrafficShaping(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkApplianceTrafficShaping

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkApplianceTrafficShapingCustomPerformanceClasses')
def getNetworkApplianceTrafficShapingCustomPerformanceClasses(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkApplianceTrafficShapingCustomPerformanceClasses

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkApplianceTrafficShapingCustomPerformanceClass')
def getNetworkApplianceTrafficShapingCustomPerformanceClass(networkId: str, customPerformanceClassId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if customPerformanceClassId is not None:
        final_kwargs['customPerformanceClassId'] = customPerformanceClassId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'customPerformanceClassId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'customPerformanceClassId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'customPerformanceClassId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkApplianceTrafficShapingCustomPerformanceClass

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkApplianceTrafficShapingRules')
def getNetworkApplianceTrafficShapingRules(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkApplianceTrafficShapingRules

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkApplianceTrafficShapingUplinkBandwidth')
def getNetworkApplianceTrafficShapingUplinkBandwidth(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkApplianceTrafficShapingUplinkBandwidth

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkApplianceTrafficShapingUplinkSelection')
def getNetworkApplianceTrafficShapingUplinkSelection(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkApplianceTrafficShapingUplinkSelection

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkApplianceUplinksUsageHistory')
def getNetworkApplianceUplinksUsageHistory(networkId: str, t0: str = None, t1: str = None, timespan: float = None, resolution: int = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if t0 is not None:
        final_kwargs['t0'] = t0
    if t1 is not None:
        final_kwargs['t1'] = t1
    if timespan is not None:
        final_kwargs['timespan'] = timespan
    if resolution is not None:
        final_kwargs['resolution'] = resolution

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 't0', 't1', 'timespan', 'resolution'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 't0', 't1', 'timespan', 'resolution'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 't0', 't1', 'timespan', 'resolution'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkApplianceUplinksUsageHistory

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkApplianceVlans')
def getNetworkApplianceVlans(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkApplianceVlans

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkApplianceVlansSettings')
def getNetworkApplianceVlansSettings(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkApplianceVlansSettings

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkApplianceVlan')
def getNetworkApplianceVlan(networkId: str, vlanId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if vlanId is not None:
        final_kwargs['vlanId'] = vlanId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'vlanId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'vlanId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'vlanId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkApplianceVlan

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkApplianceVpnBgp')
def getNetworkApplianceVpnBgp(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkApplianceVpnBgp

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkApplianceVpnSiteToSiteVpn')
def getNetworkApplianceVpnSiteToSiteVpn(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkApplianceVpnSiteToSiteVpn

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkApplianceWarmSpare')
def getNetworkApplianceWarmSpare(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkApplianceWarmSpare

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkBluetoothClients')
def getNetworkBluetoothClients(networkId: str, t0: str = None, timespan: float = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None, includeConnectivityHistory: bool = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if t0 is not None:
        final_kwargs['t0'] = t0
    if timespan is not None:
        final_kwargs['timespan'] = timespan
    if perPage is not None:
        final_kwargs['perPage'] = perPage
    if startingAfter is not None:
        final_kwargs['startingAfter'] = startingAfter
    if endingBefore is not None:
        final_kwargs['endingBefore'] = endingBefore
    if includeConnectivityHistory is not None:
        final_kwargs['includeConnectivityHistory'] = includeConnectivityHistory

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 't0', 'timespan', 'perPage', 'startingAfter', 'endingBefore', 'includeConnectivityHistory'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 't0', 'timespan', 'perPage', 'startingAfter', 'endingBefore', 'includeConnectivityHistory'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 't0', 'timespan', 'perPage', 'startingAfter', 'endingBefore', 'includeConnectivityHistory'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkBluetoothClients

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkBluetoothClient')
def getNetworkBluetoothClient(networkId: str, bluetoothClientId: str, includeConnectivityHistory: bool = None, connectivityHistoryTimespan: int = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if bluetoothClientId is not None:
        final_kwargs['bluetoothClientId'] = bluetoothClientId
    if includeConnectivityHistory is not None:
        final_kwargs['includeConnectivityHistory'] = includeConnectivityHistory
    if connectivityHistoryTimespan is not None:
        final_kwargs['connectivityHistoryTimespan'] = connectivityHistoryTimespan

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'bluetoothClientId', 'includeConnectivityHistory', 'connectivityHistoryTimespan'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'bluetoothClientId', 'includeConnectivityHistory', 'connectivityHistoryTimespan'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'bluetoothClientId', 'includeConnectivityHistory', 'connectivityHistoryTimespan'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkBluetoothClient

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkCameraQualityRetentionProfiles')
def getNetworkCameraQualityRetentionProfiles(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkCameraQualityRetentionProfiles

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkCameraQualityRetentionProfile')
def getNetworkCameraQualityRetentionProfile(networkId: str, qualityRetentionProfileId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if qualityRetentionProfileId is not None:
        final_kwargs['qualityRetentionProfileId'] = qualityRetentionProfileId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'qualityRetentionProfileId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'qualityRetentionProfileId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'qualityRetentionProfileId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkCameraQualityRetentionProfile

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkCameraSchedules')
def getNetworkCameraSchedules(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkCameraSchedules

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkCameraWirelessProfiles')
def getNetworkCameraWirelessProfiles(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkCameraWirelessProfiles

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkCameraWirelessProfile')
def getNetworkCameraWirelessProfile(networkId: str, wirelessProfileId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if wirelessProfileId is not None:
        final_kwargs['wirelessProfileId'] = wirelessProfileId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'wirelessProfileId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'wirelessProfileId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'wirelessProfileId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkCameraWirelessProfile

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkCellularGatewayConnectivityMonitoringDestinations')
def getNetworkCellularGatewayConnectivityMonitoringDestinations(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkCellularGatewayConnectivityMonitoringDestinations

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkCellularGatewayDhcp')
def getNetworkCellularGatewayDhcp(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkCellularGatewayDhcp

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkCellularGatewaySubnetPool')
def getNetworkCellularGatewaySubnetPool(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkCellularGatewaySubnetPool

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkCellularGatewayUplink')
def getNetworkCellularGatewayUplink(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkCellularGatewayUplink

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkClients')
def getNetworkClients(networkId: str, t0: str = None, timespan: float = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None, statuses: list = None, ip: str = None, ip6: str = None, ip6Local: str = None, mac: str = None, os: str = None, pskGroup: str = None, description: str = None, vlan: str = None, namedVlan: str = None, recentDeviceConnections: list = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if t0 is not None:
        final_kwargs['t0'] = t0
    if timespan is not None:
        final_kwargs['timespan'] = timespan
    if perPage is not None:
        final_kwargs['perPage'] = perPage
    if startingAfter is not None:
        final_kwargs['startingAfter'] = startingAfter
    if endingBefore is not None:
        final_kwargs['endingBefore'] = endingBefore
    if statuses is not None:
        final_kwargs['statuses'] = statuses
    if ip is not None:
        final_kwargs['ip'] = ip
    if ip6 is not None:
        final_kwargs['ip6'] = ip6
    if ip6Local is not None:
        final_kwargs['ip6Local'] = ip6Local
    if mac is not None:
        final_kwargs['mac'] = mac
    if os is not None:
        final_kwargs['os'] = os
    if pskGroup is not None:
        final_kwargs['pskGroup'] = pskGroup
    if description is not None:
        final_kwargs['description'] = description
    if vlan is not None:
        final_kwargs['vlan'] = vlan
    if namedVlan is not None:
        final_kwargs['namedVlan'] = namedVlan
    if recentDeviceConnections is not None:
        final_kwargs['recentDeviceConnections'] = recentDeviceConnections

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 't0', 'timespan', 'perPage', 'startingAfter', 'endingBefore', 'statuses', 'ip', 'ip6', 'ip6Local', 'mac', 'os', 'pskGroup', 'description', 'vlan', 'namedVlan', 'recentDeviceConnections'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 't0', 'timespan', 'perPage', 'startingAfter', 'endingBefore', 'statuses', 'ip', 'ip6', 'ip6Local', 'mac', 'os', 'pskGroup', 'description', 'vlan', 'namedVlan', 'recentDeviceConnections'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 't0', 'timespan', 'perPage', 'startingAfter', 'endingBefore', 'statuses', 'ip', 'ip6', 'ip6Local', 'mac', 'os', 'pskGroup', 'description', 'vlan', 'namedVlan', 'recentDeviceConnections'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkClients

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkClientsApplicationUsage')
def getNetworkClientsApplicationUsage(networkId: str, clients: str, ssidNumber: int = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None, t0: str = None, t1: str = None, timespan: float = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if clients is not None:
        final_kwargs['clients'] = clients
    if ssidNumber is not None:
        final_kwargs['ssidNumber'] = ssidNumber
    if perPage is not None:
        final_kwargs['perPage'] = perPage
    if startingAfter is not None:
        final_kwargs['startingAfter'] = startingAfter
    if endingBefore is not None:
        final_kwargs['endingBefore'] = endingBefore
    if t0 is not None:
        final_kwargs['t0'] = t0
    if t1 is not None:
        final_kwargs['t1'] = t1
    if timespan is not None:
        final_kwargs['timespan'] = timespan

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'clients', 'ssidNumber', 'perPage', 'startingAfter', 'endingBefore', 't0', 't1', 'timespan'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'clients', 'ssidNumber', 'perPage', 'startingAfter', 'endingBefore', 't0', 't1', 'timespan'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'clients', 'ssidNumber', 'perPage', 'startingAfter', 'endingBefore', 't0', 't1', 'timespan'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkClientsApplicationUsage

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkClientsBandwidthUsageHistory')
def getNetworkClientsBandwidthUsageHistory(networkId: str, t0: str = None, t1: str = None, timespan: float = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if t0 is not None:
        final_kwargs['t0'] = t0
    if t1 is not None:
        final_kwargs['t1'] = t1
    if timespan is not None:
        final_kwargs['timespan'] = timespan
    if perPage is not None:
        final_kwargs['perPage'] = perPage
    if startingAfter is not None:
        final_kwargs['startingAfter'] = startingAfter
    if endingBefore is not None:
        final_kwargs['endingBefore'] = endingBefore

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 't0', 't1', 'timespan', 'perPage', 'startingAfter', 'endingBefore'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 't0', 't1', 'timespan', 'perPage', 'startingAfter', 'endingBefore'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 't0', 't1', 'timespan', 'perPage', 'startingAfter', 'endingBefore'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkClientsBandwidthUsageHistory

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkClientsOverview')
def getNetworkClientsOverview(networkId: str, t0: str = None, t1: str = None, timespan: float = None, resolution: int = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if t0 is not None:
        final_kwargs['t0'] = t0
    if t1 is not None:
        final_kwargs['t1'] = t1
    if timespan is not None:
        final_kwargs['timespan'] = timespan
    if resolution is not None:
        final_kwargs['resolution'] = resolution

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 't0', 't1', 'timespan', 'resolution'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 't0', 't1', 'timespan', 'resolution'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 't0', 't1', 'timespan', 'resolution'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkClientsOverview

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkClientsUsageHistories')
def getNetworkClientsUsageHistories(networkId: str, clients: str, ssidNumber: int = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None, t0: str = None, t1: str = None, timespan: float = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if clients is not None:
        final_kwargs['clients'] = clients
    if ssidNumber is not None:
        final_kwargs['ssidNumber'] = ssidNumber
    if perPage is not None:
        final_kwargs['perPage'] = perPage
    if startingAfter is not None:
        final_kwargs['startingAfter'] = startingAfter
    if endingBefore is not None:
        final_kwargs['endingBefore'] = endingBefore
    if t0 is not None:
        final_kwargs['t0'] = t0
    if t1 is not None:
        final_kwargs['t1'] = t1
    if timespan is not None:
        final_kwargs['timespan'] = timespan

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'clients', 'ssidNumber', 'perPage', 'startingAfter', 'endingBefore', 't0', 't1', 'timespan'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'clients', 'ssidNumber', 'perPage', 'startingAfter', 'endingBefore', 't0', 't1', 'timespan'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'clients', 'ssidNumber', 'perPage', 'startingAfter', 'endingBefore', 't0', 't1', 'timespan'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkClientsUsageHistories

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkClient')
def getNetworkClient(networkId: str, clientId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if clientId is not None:
        final_kwargs['clientId'] = clientId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'clientId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'clientId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'clientId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkClient

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkClientPolicy')
def getNetworkClientPolicy(networkId: str, clientId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if clientId is not None:
        final_kwargs['clientId'] = clientId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'clientId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'clientId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'clientId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkClientPolicy

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkClientSplashAuthorizationStatus')
def getNetworkClientSplashAuthorizationStatus(networkId: str, clientId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if clientId is not None:
        final_kwargs['clientId'] = clientId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'clientId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'clientId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'clientId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkClientSplashAuthorizationStatus

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkClientTrafficHistory')
def getNetworkClientTrafficHistory(networkId: str, clientId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if clientId is not None:
        final_kwargs['clientId'] = clientId
    if perPage is not None:
        final_kwargs['perPage'] = perPage
    if startingAfter is not None:
        final_kwargs['startingAfter'] = startingAfter
    if endingBefore is not None:
        final_kwargs['endingBefore'] = endingBefore

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'clientId', 'perPage', 'startingAfter', 'endingBefore'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'clientId', 'perPage', 'startingAfter', 'endingBefore'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'clientId', 'perPage', 'startingAfter', 'endingBefore'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkClientTrafficHistory

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkClientUsageHistory')
def getNetworkClientUsageHistory(networkId: str, clientId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if clientId is not None:
        final_kwargs['clientId'] = clientId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'clientId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'clientId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'clientId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkClientUsageHistory

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkDevices')
def getNetworkDevices(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkDevices

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkEvents')
def getNetworkEvents(networkId: str, productType: str = None, includedEventTypes: list = None, excludedEventTypes: list = None, deviceMac: str = None, deviceSerial: str = None, deviceName: str = None, clientIp: str = None, clientMac: str = None, clientName: str = None, smDeviceMac: str = None, smDeviceName: str = None, eventDetails: str = None, eventSeverity: str = None, isCatalyst: bool = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if productType is not None:
        final_kwargs['productType'] = productType
    if includedEventTypes is not None:
        final_kwargs['includedEventTypes'] = includedEventTypes
    if excludedEventTypes is not None:
        final_kwargs['excludedEventTypes'] = excludedEventTypes
    if deviceMac is not None:
        final_kwargs['deviceMac'] = deviceMac
    if deviceSerial is not None:
        final_kwargs['deviceSerial'] = deviceSerial
    if deviceName is not None:
        final_kwargs['deviceName'] = deviceName
    if clientIp is not None:
        final_kwargs['clientIp'] = clientIp
    if clientMac is not None:
        final_kwargs['clientMac'] = clientMac
    if clientName is not None:
        final_kwargs['clientName'] = clientName
    if smDeviceMac is not None:
        final_kwargs['smDeviceMac'] = smDeviceMac
    if smDeviceName is not None:
        final_kwargs['smDeviceName'] = smDeviceName
    if eventDetails is not None:
        final_kwargs['eventDetails'] = eventDetails
    if eventSeverity is not None:
        final_kwargs['eventSeverity'] = eventSeverity
    if isCatalyst is not None:
        final_kwargs['isCatalyst'] = isCatalyst
    if perPage is not None:
        final_kwargs['perPage'] = perPage
    if startingAfter is not None:
        final_kwargs['startingAfter'] = startingAfter
    if endingBefore is not None:
        final_kwargs['endingBefore'] = endingBefore

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'productType', 'includedEventTypes', 'excludedEventTypes', 'deviceMac', 'deviceSerial', 'deviceName', 'clientIp', 'clientMac', 'clientName', 'smDeviceMac', 'smDeviceName', 'eventDetails', 'eventSeverity', 'isCatalyst', 'perPage', 'startingAfter', 'endingBefore'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'productType', 'includedEventTypes', 'excludedEventTypes', 'deviceMac', 'deviceSerial', 'deviceName', 'clientIp', 'clientMac', 'clientName', 'smDeviceMac', 'smDeviceName', 'eventDetails', 'eventSeverity', 'isCatalyst', 'perPage', 'startingAfter', 'endingBefore'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'productType', 'includedEventTypes', 'excludedEventTypes', 'deviceMac', 'deviceSerial', 'deviceName', 'clientIp', 'clientMac', 'clientName', 'smDeviceMac', 'smDeviceName', 'eventDetails', 'eventSeverity', 'isCatalyst', 'perPage', 'startingAfter', 'endingBefore'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkEvents

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkEventsEventTypes')
def getNetworkEventsEventTypes(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkEventsEventTypes

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkFirmwareUpgrades')
def getNetworkFirmwareUpgrades(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkFirmwareUpgrades

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkFirmwareUpgradesStagedEvents')
def getNetworkFirmwareUpgradesStagedEvents(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkFirmwareUpgradesStagedEvents

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkFirmwareUpgradesStagedGroups')
def getNetworkFirmwareUpgradesStagedGroups(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkFirmwareUpgradesStagedGroups

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkFirmwareUpgradesStagedGroup')
def getNetworkFirmwareUpgradesStagedGroup(networkId: str, groupId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if groupId is not None:
        final_kwargs['groupId'] = groupId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'groupId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'groupId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'groupId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkFirmwareUpgradesStagedGroup

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkFirmwareUpgradesStagedStages')
def getNetworkFirmwareUpgradesStagedStages(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkFirmwareUpgradesStagedStages

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkFloorPlans')
def getNetworkFloorPlans(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkFloorPlans

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkFloorPlan')
def getNetworkFloorPlan(networkId: str, floorPlanId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if floorPlanId is not None:
        final_kwargs['floorPlanId'] = floorPlanId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'floorPlanId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'floorPlanId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'floorPlanId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkFloorPlan

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkGroupPolicies')
def getNetworkGroupPolicies(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkGroupPolicies

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkGroupPolicy')
def getNetworkGroupPolicy(networkId: str, groupPolicyId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if groupPolicyId is not None:
        final_kwargs['groupPolicyId'] = groupPolicyId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'groupPolicyId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'groupPolicyId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'groupPolicyId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkGroupPolicy

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkHealthAlerts')
def getNetworkHealthAlerts(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkHealthAlerts

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkInsightApplicationHealthByTime')
def getNetworkInsightApplicationHealthByTime(networkId: str, applicationId: str, t0: str = None, t1: str = None, timespan: float = None, resolution: int = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if applicationId is not None:
        final_kwargs['applicationId'] = applicationId
    if t0 is not None:
        final_kwargs['t0'] = t0
    if t1 is not None:
        final_kwargs['t1'] = t1
    if timespan is not None:
        final_kwargs['timespan'] = timespan
    if resolution is not None:
        final_kwargs['resolution'] = resolution

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'applicationId', 't0', 't1', 'timespan', 'resolution'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'applicationId', 't0', 't1', 'timespan', 'resolution'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'applicationId', 't0', 't1', 'timespan', 'resolution'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkInsightApplicationHealthByTime

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkMerakiAuthUsers')
def getNetworkMerakiAuthUsers(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkMerakiAuthUsers

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkMerakiAuthUser')
def getNetworkMerakiAuthUser(networkId: str, merakiAuthUserId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if merakiAuthUserId is not None:
        final_kwargs['merakiAuthUserId'] = merakiAuthUserId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'merakiAuthUserId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'merakiAuthUserId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'merakiAuthUserId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkMerakiAuthUser

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkMqttBrokers')
def getNetworkMqttBrokers(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkMqttBrokers

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkMqttBroker')
def getNetworkMqttBroker(networkId: str, mqttBrokerId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if mqttBrokerId is not None:
        final_kwargs['mqttBrokerId'] = mqttBrokerId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'mqttBrokerId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'mqttBrokerId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'mqttBrokerId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkMqttBroker

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkNetflow')
def getNetworkNetflow(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkNetflow

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkNetworkHealthChannelUtilization')
def getNetworkNetworkHealthChannelUtilization(networkId: str, t0: str = None, t1: str = None, timespan: float = None, resolution: int = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if t0 is not None:
        final_kwargs['t0'] = t0
    if t1 is not None:
        final_kwargs['t1'] = t1
    if timespan is not None:
        final_kwargs['timespan'] = timespan
    if resolution is not None:
        final_kwargs['resolution'] = resolution
    if perPage is not None:
        final_kwargs['perPage'] = perPage
    if startingAfter is not None:
        final_kwargs['startingAfter'] = startingAfter
    if endingBefore is not None:
        final_kwargs['endingBefore'] = endingBefore

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 't0', 't1', 'timespan', 'resolution', 'perPage', 'startingAfter', 'endingBefore'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 't0', 't1', 'timespan', 'resolution', 'perPage', 'startingAfter', 'endingBefore'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 't0', 't1', 'timespan', 'resolution', 'perPage', 'startingAfter', 'endingBefore'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkNetworkHealthChannelUtilization

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkPiiPiiKeys')
def getNetworkPiiPiiKeys(networkId: str, username: str = None, email: str = None, mac: str = None, serial: str = None, imei: str = None, bluetoothMac: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if username is not None:
        final_kwargs['username'] = username
    if email is not None:
        final_kwargs['email'] = email
    if mac is not None:
        final_kwargs['mac'] = mac
    if serial is not None:
        final_kwargs['serial'] = serial
    if imei is not None:
        final_kwargs['imei'] = imei
    if bluetoothMac is not None:
        final_kwargs['bluetoothMac'] = bluetoothMac

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'username', 'email', 'mac', 'serial', 'imei', 'bluetoothMac'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'username', 'email', 'mac', 'serial', 'imei', 'bluetoothMac'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'username', 'email', 'mac', 'serial', 'imei', 'bluetoothMac'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkPiiPiiKeys

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkPiiRequests')
def getNetworkPiiRequests(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkPiiRequests

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkPiiRequest')
def getNetworkPiiRequest(networkId: str, requestId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if requestId is not None:
        final_kwargs['requestId'] = requestId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'requestId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'requestId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'requestId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkPiiRequest

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkPiiSmDevicesForKey')
def getNetworkPiiSmDevicesForKey(networkId: str, username: str = None, email: str = None, mac: str = None, serial: str = None, imei: str = None, bluetoothMac: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if username is not None:
        final_kwargs['username'] = username
    if email is not None:
        final_kwargs['email'] = email
    if mac is not None:
        final_kwargs['mac'] = mac
    if serial is not None:
        final_kwargs['serial'] = serial
    if imei is not None:
        final_kwargs['imei'] = imei
    if bluetoothMac is not None:
        final_kwargs['bluetoothMac'] = bluetoothMac

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'username', 'email', 'mac', 'serial', 'imei', 'bluetoothMac'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'username', 'email', 'mac', 'serial', 'imei', 'bluetoothMac'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'username', 'email', 'mac', 'serial', 'imei', 'bluetoothMac'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkPiiSmDevicesForKey

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkPiiSmOwnersForKey')
def getNetworkPiiSmOwnersForKey(networkId: str, username: str = None, email: str = None, mac: str = None, serial: str = None, imei: str = None, bluetoothMac: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if username is not None:
        final_kwargs['username'] = username
    if email is not None:
        final_kwargs['email'] = email
    if mac is not None:
        final_kwargs['mac'] = mac
    if serial is not None:
        final_kwargs['serial'] = serial
    if imei is not None:
        final_kwargs['imei'] = imei
    if bluetoothMac is not None:
        final_kwargs['bluetoothMac'] = bluetoothMac

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'username', 'email', 'mac', 'serial', 'imei', 'bluetoothMac'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'username', 'email', 'mac', 'serial', 'imei', 'bluetoothMac'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'username', 'email', 'mac', 'serial', 'imei', 'bluetoothMac'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkPiiSmOwnersForKey

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkPoliciesByClient')
def getNetworkPoliciesByClient(networkId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None, t0: str = None, timespan: float = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if perPage is not None:
        final_kwargs['perPage'] = perPage
    if startingAfter is not None:
        final_kwargs['startingAfter'] = startingAfter
    if endingBefore is not None:
        final_kwargs['endingBefore'] = endingBefore
    if t0 is not None:
        final_kwargs['t0'] = t0
    if timespan is not None:
        final_kwargs['timespan'] = timespan

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'perPage', 'startingAfter', 'endingBefore', 't0', 'timespan'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'perPage', 'startingAfter', 'endingBefore', 't0', 'timespan'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'perPage', 'startingAfter', 'endingBefore', 't0', 'timespan'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkPoliciesByClient

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSensorAlertsCurrentOverviewByMetric')
def getNetworkSensorAlertsCurrentOverviewByMetric(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkSensorAlertsCurrentOverviewByMetric

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSensorAlertsOverviewByMetric')
def getNetworkSensorAlertsOverviewByMetric(networkId: str, t0: str = None, t1: str = None, timespan: float = None, interval: int = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if t0 is not None:
        final_kwargs['t0'] = t0
    if t1 is not None:
        final_kwargs['t1'] = t1
    if timespan is not None:
        final_kwargs['timespan'] = timespan
    if interval is not None:
        final_kwargs['interval'] = interval

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 't0', 't1', 'timespan', 'interval'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 't0', 't1', 'timespan', 'interval'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 't0', 't1', 'timespan', 'interval'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkSensorAlertsOverviewByMetric

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSensorAlertsProfiles')
def getNetworkSensorAlertsProfiles(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkSensorAlertsProfiles

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSensorAlertsProfile')
def getNetworkSensorAlertsProfile(networkId: str, id: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if id is not None:
        final_kwargs['id'] = id

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'id'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'id'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'id'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkSensorAlertsProfile

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSensorMqttBrokers')
def getNetworkSensorMqttBrokers(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkSensorMqttBrokers

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSensorMqttBroker')
def getNetworkSensorMqttBroker(networkId: str, mqttBrokerId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if mqttBrokerId is not None:
        final_kwargs['mqttBrokerId'] = mqttBrokerId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'mqttBrokerId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'mqttBrokerId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'mqttBrokerId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkSensorMqttBroker

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSensorRelationships')
def getNetworkSensorRelationships(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkSensorRelationships

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSettings')
def getNetworkSettings(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkSettings

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSmBypassActivationLockAttempt')
def getNetworkSmBypassActivationLockAttempt(networkId: str, attemptId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if attemptId is not None:
        final_kwargs['attemptId'] = attemptId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'attemptId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'attemptId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'attemptId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkSmBypassActivationLockAttempt

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSmDevices')
def getNetworkSmDevices(networkId: str, fields: list = None, wifiMacs: list = None, serials: list = None, ids: list = None, uuids: list = None, systemTypes: list = None, scope: list = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if fields is not None:
        final_kwargs['fields'] = fields
    if wifiMacs is not None:
        final_kwargs['wifiMacs'] = wifiMacs
    if serials is not None:
        final_kwargs['serials'] = serials
    if ids is not None:
        final_kwargs['ids'] = ids
    if uuids is not None:
        final_kwargs['uuids'] = uuids
    if systemTypes is not None:
        final_kwargs['systemTypes'] = systemTypes
    if scope is not None:
        final_kwargs['scope'] = scope
    if perPage is not None:
        final_kwargs['perPage'] = perPage
    if startingAfter is not None:
        final_kwargs['startingAfter'] = startingAfter
    if endingBefore is not None:
        final_kwargs['endingBefore'] = endingBefore

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'fields', 'wifiMacs', 'serials', 'ids', 'uuids', 'systemTypes', 'scope', 'perPage', 'startingAfter', 'endingBefore'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'fields', 'wifiMacs', 'serials', 'ids', 'uuids', 'systemTypes', 'scope', 'perPage', 'startingAfter', 'endingBefore'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'fields', 'wifiMacs', 'serials', 'ids', 'uuids', 'systemTypes', 'scope', 'perPage', 'startingAfter', 'endingBefore'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkSmDevices

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSmDeviceCellularUsageHistory')
def getNetworkSmDeviceCellularUsageHistory(networkId: str, deviceId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if deviceId is not None:
        final_kwargs['deviceId'] = deviceId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'deviceId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'deviceId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'deviceId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkSmDeviceCellularUsageHistory

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSmDeviceCerts')
def getNetworkSmDeviceCerts(networkId: str, deviceId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if deviceId is not None:
        final_kwargs['deviceId'] = deviceId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'deviceId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'deviceId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'deviceId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkSmDeviceCerts

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSmDeviceConnectivity')
def getNetworkSmDeviceConnectivity(networkId: str, deviceId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if deviceId is not None:
        final_kwargs['deviceId'] = deviceId
    if perPage is not None:
        final_kwargs['perPage'] = perPage
    if startingAfter is not None:
        final_kwargs['startingAfter'] = startingAfter
    if endingBefore is not None:
        final_kwargs['endingBefore'] = endingBefore

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'deviceId', 'perPage', 'startingAfter', 'endingBefore'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'deviceId', 'perPage', 'startingAfter', 'endingBefore'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'deviceId', 'perPage', 'startingAfter', 'endingBefore'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkSmDeviceConnectivity

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSmDeviceDesktopLogs')
def getNetworkSmDeviceDesktopLogs(networkId: str, deviceId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if deviceId is not None:
        final_kwargs['deviceId'] = deviceId
    if perPage is not None:
        final_kwargs['perPage'] = perPage
    if startingAfter is not None:
        final_kwargs['startingAfter'] = startingAfter
    if endingBefore is not None:
        final_kwargs['endingBefore'] = endingBefore

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'deviceId', 'perPage', 'startingAfter', 'endingBefore'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'deviceId', 'perPage', 'startingAfter', 'endingBefore'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'deviceId', 'perPage', 'startingAfter', 'endingBefore'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkSmDeviceDesktopLogs

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSmDeviceDeviceCommandLogs')
def getNetworkSmDeviceDeviceCommandLogs(networkId: str, deviceId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if deviceId is not None:
        final_kwargs['deviceId'] = deviceId
    if perPage is not None:
        final_kwargs['perPage'] = perPage
    if startingAfter is not None:
        final_kwargs['startingAfter'] = startingAfter
    if endingBefore is not None:
        final_kwargs['endingBefore'] = endingBefore

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'deviceId', 'perPage', 'startingAfter', 'endingBefore'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'deviceId', 'perPage', 'startingAfter', 'endingBefore'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'deviceId', 'perPage', 'startingAfter', 'endingBefore'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkSmDeviceDeviceCommandLogs

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSmDeviceDeviceProfiles')
def getNetworkSmDeviceDeviceProfiles(networkId: str, deviceId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if deviceId is not None:
        final_kwargs['deviceId'] = deviceId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'deviceId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'deviceId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'deviceId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkSmDeviceDeviceProfiles

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSmDeviceNetworkAdapters')
def getNetworkSmDeviceNetworkAdapters(networkId: str, deviceId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if deviceId is not None:
        final_kwargs['deviceId'] = deviceId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'deviceId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'deviceId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'deviceId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkSmDeviceNetworkAdapters

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSmDevicePerformanceHistory')
def getNetworkSmDevicePerformanceHistory(networkId: str, deviceId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if deviceId is not None:
        final_kwargs['deviceId'] = deviceId
    if perPage is not None:
        final_kwargs['perPage'] = perPage
    if startingAfter is not None:
        final_kwargs['startingAfter'] = startingAfter
    if endingBefore is not None:
        final_kwargs['endingBefore'] = endingBefore

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'deviceId', 'perPage', 'startingAfter', 'endingBefore'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'deviceId', 'perPage', 'startingAfter', 'endingBefore'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'deviceId', 'perPage', 'startingAfter', 'endingBefore'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkSmDevicePerformanceHistory

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSmDeviceRestrictions')
def getNetworkSmDeviceRestrictions(networkId: str, deviceId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if deviceId is not None:
        final_kwargs['deviceId'] = deviceId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'deviceId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'deviceId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'deviceId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkSmDeviceRestrictions

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSmDeviceSecurityCenters')
def getNetworkSmDeviceSecurityCenters(networkId: str, deviceId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if deviceId is not None:
        final_kwargs['deviceId'] = deviceId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'deviceId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'deviceId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'deviceId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkSmDeviceSecurityCenters

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSmDeviceSoftwares')
def getNetworkSmDeviceSoftwares(networkId: str, deviceId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if deviceId is not None:
        final_kwargs['deviceId'] = deviceId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'deviceId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'deviceId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'deviceId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkSmDeviceSoftwares

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSmDeviceWlanLists')
def getNetworkSmDeviceWlanLists(networkId: str, deviceId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if deviceId is not None:
        final_kwargs['deviceId'] = deviceId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'deviceId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'deviceId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'deviceId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkSmDeviceWlanLists

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSmProfiles')
def getNetworkSmProfiles(networkId: str, payloadTypes: list = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if payloadTypes is not None:
        final_kwargs['payloadTypes'] = payloadTypes

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'payloadTypes'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'payloadTypes'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'payloadTypes'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkSmProfiles

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSmTargetGroups')
def getNetworkSmTargetGroups(networkId: str, withDetails: bool = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if withDetails is not None:
        final_kwargs['withDetails'] = withDetails

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'withDetails'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'withDetails'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'withDetails'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkSmTargetGroups

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSmTargetGroup')
def getNetworkSmTargetGroup(networkId: str, targetGroupId: str, withDetails: bool = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if targetGroupId is not None:
        final_kwargs['targetGroupId'] = targetGroupId
    if withDetails is not None:
        final_kwargs['withDetails'] = withDetails

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'targetGroupId', 'withDetails'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'targetGroupId', 'withDetails'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'targetGroupId', 'withDetails'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkSmTargetGroup

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSmTrustedAccessConfigs')
def getNetworkSmTrustedAccessConfigs(networkId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if perPage is not None:
        final_kwargs['perPage'] = perPage
    if startingAfter is not None:
        final_kwargs['startingAfter'] = startingAfter
    if endingBefore is not None:
        final_kwargs['endingBefore'] = endingBefore

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'perPage', 'startingAfter', 'endingBefore'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'perPage', 'startingAfter', 'endingBefore'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'perPage', 'startingAfter', 'endingBefore'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkSmTrustedAccessConfigs

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSmUserAccessDevices')
def getNetworkSmUserAccessDevices(networkId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if perPage is not None:
        final_kwargs['perPage'] = perPage
    if startingAfter is not None:
        final_kwargs['startingAfter'] = startingAfter
    if endingBefore is not None:
        final_kwargs['endingBefore'] = endingBefore

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'perPage', 'startingAfter', 'endingBefore'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'perPage', 'startingAfter', 'endingBefore'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'perPage', 'startingAfter', 'endingBefore'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkSmUserAccessDevices

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSmUsers')
def getNetworkSmUsers(networkId: str, ids: list = None, usernames: list = None, emails: list = None, scope: list = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if ids is not None:
        final_kwargs['ids'] = ids
    if usernames is not None:
        final_kwargs['usernames'] = usernames
    if emails is not None:
        final_kwargs['emails'] = emails
    if scope is not None:
        final_kwargs['scope'] = scope

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'ids', 'usernames', 'emails', 'scope'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'ids', 'usernames', 'emails', 'scope'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'ids', 'usernames', 'emails', 'scope'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkSmUsers

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSmUserDeviceProfiles')
def getNetworkSmUserDeviceProfiles(networkId: str, userId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if userId is not None:
        final_kwargs['userId'] = userId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'userId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'userId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'userId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkSmUserDeviceProfiles

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSmUserSoftwares')
def getNetworkSmUserSoftwares(networkId: str, userId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if userId is not None:
        final_kwargs['userId'] = userId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'userId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'userId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'userId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkSmUserSoftwares

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSnmp')
def getNetworkSnmp(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkSnmp

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSplashLoginAttempts')
def getNetworkSplashLoginAttempts(networkId: str, ssidNumber: int = None, loginIdentifier: str = None, timespan: int = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if ssidNumber is not None:
        final_kwargs['ssidNumber'] = ssidNumber
    if loginIdentifier is not None:
        final_kwargs['loginIdentifier'] = loginIdentifier
    if timespan is not None:
        final_kwargs['timespan'] = timespan

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'ssidNumber', 'loginIdentifier', 'timespan'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'ssidNumber', 'loginIdentifier', 'timespan'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'ssidNumber', 'loginIdentifier', 'timespan'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkSplashLoginAttempts

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSwitchAccessControlLists')
def getNetworkSwitchAccessControlLists(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkSwitchAccessControlLists

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSwitchAccessPolicies')
def getNetworkSwitchAccessPolicies(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkSwitchAccessPolicies

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSwitchAccessPolicy')
def getNetworkSwitchAccessPolicy(networkId: str, accessPolicyNumber: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if accessPolicyNumber is not None:
        final_kwargs['accessPolicyNumber'] = accessPolicyNumber

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'accessPolicyNumber'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'accessPolicyNumber'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'accessPolicyNumber'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkSwitchAccessPolicy

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSwitchAlternateManagementInterface')
def getNetworkSwitchAlternateManagementInterface(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkSwitchAlternateManagementInterface

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSwitchDhcpV4ServersSeen')
def getNetworkSwitchDhcpV4ServersSeen(networkId: str, t0: str = None, timespan: float = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if t0 is not None:
        final_kwargs['t0'] = t0
    if timespan is not None:
        final_kwargs['timespan'] = timespan
    if perPage is not None:
        final_kwargs['perPage'] = perPage
    if startingAfter is not None:
        final_kwargs['startingAfter'] = startingAfter
    if endingBefore is not None:
        final_kwargs['endingBefore'] = endingBefore

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 't0', 'timespan', 'perPage', 'startingAfter', 'endingBefore'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 't0', 'timespan', 'perPage', 'startingAfter', 'endingBefore'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 't0', 'timespan', 'perPage', 'startingAfter', 'endingBefore'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkSwitchDhcpV4ServersSeen

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSwitchDhcpServerPolicy')
def getNetworkSwitchDhcpServerPolicy(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkSwitchDhcpServerPolicy

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers')
def getNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers(networkId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if perPage is not None:
        final_kwargs['perPage'] = perPage
    if startingAfter is not None:
        final_kwargs['startingAfter'] = startingAfter
    if endingBefore is not None:
        final_kwargs['endingBefore'] = endingBefore

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'perPage', 'startingAfter', 'endingBefore'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'perPage', 'startingAfter', 'endingBefore'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'perPage', 'startingAfter', 'endingBefore'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSwitchDhcpServerPolicyArpInspectionWarningsByDevice')
def getNetworkSwitchDhcpServerPolicyArpInspectionWarningsByDevice(networkId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if perPage is not None:
        final_kwargs['perPage'] = perPage
    if startingAfter is not None:
        final_kwargs['startingAfter'] = startingAfter
    if endingBefore is not None:
        final_kwargs['endingBefore'] = endingBefore

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'perPage', 'startingAfter', 'endingBefore'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'perPage', 'startingAfter', 'endingBefore'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'perPage', 'startingAfter', 'endingBefore'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkSwitchDhcpServerPolicyArpInspectionWarningsByDevice

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSwitchDscpToCosMappings')
def getNetworkSwitchDscpToCosMappings(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkSwitchDscpToCosMappings

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSwitchLinkAggregations')
def getNetworkSwitchLinkAggregations(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkSwitchLinkAggregations

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSwitchMtu')
def getNetworkSwitchMtu(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkSwitchMtu

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSwitchPortSchedules')
def getNetworkSwitchPortSchedules(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkSwitchPortSchedules

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSwitchQosRules')
def getNetworkSwitchQosRules(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkSwitchQosRules

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSwitchQosRulesOrder')
def getNetworkSwitchQosRulesOrder(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkSwitchQosRulesOrder

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSwitchQosRule')
def getNetworkSwitchQosRule(networkId: str, qosRuleId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if qosRuleId is not None:
        final_kwargs['qosRuleId'] = qosRuleId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'qosRuleId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'qosRuleId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'qosRuleId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkSwitchQosRule

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSwitchRoutingMulticast')
def getNetworkSwitchRoutingMulticast(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkSwitchRoutingMulticast

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSwitchRoutingMulticastRendezvousPoints')
def getNetworkSwitchRoutingMulticastRendezvousPoints(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkSwitchRoutingMulticastRendezvousPoints

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSwitchRoutingMulticastRendezvousPoint')
def getNetworkSwitchRoutingMulticastRendezvousPoint(networkId: str, rendezvousPointId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if rendezvousPointId is not None:
        final_kwargs['rendezvousPointId'] = rendezvousPointId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'rendezvousPointId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'rendezvousPointId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'rendezvousPointId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkSwitchRoutingMulticastRendezvousPoint

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSwitchRoutingOspf')
def getNetworkSwitchRoutingOspf(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkSwitchRoutingOspf

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSwitchSettings')
def getNetworkSwitchSettings(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkSwitchSettings

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSwitchStacks')
def getNetworkSwitchStacks(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkSwitchStacks

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSwitchStack')
def getNetworkSwitchStack(networkId: str, switchStackId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if switchStackId is not None:
        final_kwargs['switchStackId'] = switchStackId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'switchStackId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'switchStackId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'switchStackId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkSwitchStack

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSwitchStackRoutingInterfaces')
def getNetworkSwitchStackRoutingInterfaces(networkId: str, switchStackId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if switchStackId is not None:
        final_kwargs['switchStackId'] = switchStackId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'switchStackId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'switchStackId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'switchStackId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkSwitchStackRoutingInterfaces

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSwitchStackRoutingInterface')
def getNetworkSwitchStackRoutingInterface(networkId: str, switchStackId: str, interfaceId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if switchStackId is not None:
        final_kwargs['switchStackId'] = switchStackId
    if interfaceId is not None:
        final_kwargs['interfaceId'] = interfaceId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'switchStackId', 'interfaceId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'switchStackId', 'interfaceId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'switchStackId', 'interfaceId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkSwitchStackRoutingInterface

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSwitchStackRoutingInterfaceDhcp')
def getNetworkSwitchStackRoutingInterfaceDhcp(networkId: str, switchStackId: str, interfaceId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if switchStackId is not None:
        final_kwargs['switchStackId'] = switchStackId
    if interfaceId is not None:
        final_kwargs['interfaceId'] = interfaceId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'switchStackId', 'interfaceId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'switchStackId', 'interfaceId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'switchStackId', 'interfaceId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkSwitchStackRoutingInterfaceDhcp

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSwitchStackRoutingStaticRoutes')
def getNetworkSwitchStackRoutingStaticRoutes(networkId: str, switchStackId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if switchStackId is not None:
        final_kwargs['switchStackId'] = switchStackId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'switchStackId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'switchStackId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'switchStackId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkSwitchStackRoutingStaticRoutes

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSwitchStackRoutingStaticRoute')
def getNetworkSwitchStackRoutingStaticRoute(networkId: str, switchStackId: str, staticRouteId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if switchStackId is not None:
        final_kwargs['switchStackId'] = switchStackId
    if staticRouteId is not None:
        final_kwargs['staticRouteId'] = staticRouteId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'switchStackId', 'staticRouteId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'switchStackId', 'staticRouteId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'switchStackId', 'staticRouteId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkSwitchStackRoutingStaticRoute

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSwitchStormControl')
def getNetworkSwitchStormControl(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkSwitchStormControl

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSwitchStp')
def getNetworkSwitchStp(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkSwitchStp

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSyslogServers')
def getNetworkSyslogServers(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkSyslogServers

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkTopologyLinkLayer')
def getNetworkTopologyLinkLayer(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkTopologyLinkLayer

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkTraffic')
def getNetworkTraffic(networkId: str, t0: str = None, timespan: float = None, deviceType: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if t0 is not None:
        final_kwargs['t0'] = t0
    if timespan is not None:
        final_kwargs['timespan'] = timespan
    if deviceType is not None:
        final_kwargs['deviceType'] = deviceType

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 't0', 'timespan', 'deviceType'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 't0', 'timespan', 'deviceType'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 't0', 'timespan', 'deviceType'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkTraffic

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkTrafficAnalysis')
def getNetworkTrafficAnalysis(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkTrafficAnalysis

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkTrafficShapingApplicationCategories')
def getNetworkTrafficShapingApplicationCategories(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkTrafficShapingApplicationCategories

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkTrafficShapingDscpTaggingOptions')
def getNetworkTrafficShapingDscpTaggingOptions(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkTrafficShapingDscpTaggingOptions

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkVlanProfiles')
def getNetworkVlanProfiles(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkVlanProfiles

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkVlanProfilesAssignmentsByDevice')
def getNetworkVlanProfilesAssignmentsByDevice(networkId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None, serials: list = None, productTypes: list = None, stackIds: list = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if perPage is not None:
        final_kwargs['perPage'] = perPage
    if startingAfter is not None:
        final_kwargs['startingAfter'] = startingAfter
    if endingBefore is not None:
        final_kwargs['endingBefore'] = endingBefore
    if serials is not None:
        final_kwargs['serials'] = serials
    if productTypes is not None:
        final_kwargs['productTypes'] = productTypes
    if stackIds is not None:
        final_kwargs['stackIds'] = stackIds

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'perPage', 'startingAfter', 'endingBefore', 'serials', 'productTypes', 'stackIds'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'perPage', 'startingAfter', 'endingBefore', 'serials', 'productTypes', 'stackIds'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'perPage', 'startingAfter', 'endingBefore', 'serials', 'productTypes', 'stackIds'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkVlanProfilesAssignmentsByDevice

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkVlanProfile')
def getNetworkVlanProfile(networkId: str, iname: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if iname is not None:
        final_kwargs['iname'] = iname

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'iname'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'iname'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'iname'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkVlanProfile

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWebhooksHttpServers')
def getNetworkWebhooksHttpServers(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkWebhooksHttpServers

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWebhooksHttpServer')
def getNetworkWebhooksHttpServer(networkId: str, httpServerId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if httpServerId is not None:
        final_kwargs['httpServerId'] = httpServerId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'httpServerId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'httpServerId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'httpServerId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkWebhooksHttpServer

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWebhooksPayloadTemplates')
def getNetworkWebhooksPayloadTemplates(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkWebhooksPayloadTemplates

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWebhooksPayloadTemplate')
def getNetworkWebhooksPayloadTemplate(networkId: str, payloadTemplateId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if payloadTemplateId is not None:
        final_kwargs['payloadTemplateId'] = payloadTemplateId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'payloadTemplateId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'payloadTemplateId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'payloadTemplateId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkWebhooksPayloadTemplate

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWebhooksWebhookTest')
def getNetworkWebhooksWebhookTest(networkId: str, webhookTestId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if webhookTestId is not None:
        final_kwargs['webhookTestId'] = webhookTestId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'webhookTestId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'webhookTestId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'webhookTestId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkWebhooksWebhookTest

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWirelessAirMarshal')
def getNetworkWirelessAirMarshal(networkId: str, t0: str = None, timespan: float = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if t0 is not None:
        final_kwargs['t0'] = t0
    if timespan is not None:
        final_kwargs['timespan'] = timespan

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 't0', 'timespan'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 't0', 'timespan'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 't0', 'timespan'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkWirelessAirMarshal

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWirelessAlternateManagementInterface')
def getNetworkWirelessAlternateManagementInterface(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkWirelessAlternateManagementInterface

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWirelessBilling')
def getNetworkWirelessBilling(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkWirelessBilling

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWirelessBluetoothSettings')
def getNetworkWirelessBluetoothSettings(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkWirelessBluetoothSettings

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWirelessChannelUtilizationHistory')
def getNetworkWirelessChannelUtilizationHistory(networkId: str, t0: str = None, t1: str = None, timespan: float = None, resolution: int = None, autoResolution: bool = None, clientId: str = None, deviceSerial: str = None, apTag: str = None, band: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if t0 is not None:
        final_kwargs['t0'] = t0
    if t1 is not None:
        final_kwargs['t1'] = t1
    if timespan is not None:
        final_kwargs['timespan'] = timespan
    if resolution is not None:
        final_kwargs['resolution'] = resolution
    if autoResolution is not None:
        final_kwargs['autoResolution'] = autoResolution
    if clientId is not None:
        final_kwargs['clientId'] = clientId
    if deviceSerial is not None:
        final_kwargs['deviceSerial'] = deviceSerial
    if apTag is not None:
        final_kwargs['apTag'] = apTag
    if band is not None:
        final_kwargs['band'] = band

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 't0', 't1', 'timespan', 'resolution', 'autoResolution', 'clientId', 'deviceSerial', 'apTag', 'band'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 't0', 't1', 'timespan', 'resolution', 'autoResolution', 'clientId', 'deviceSerial', 'apTag', 'band'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 't0', 't1', 'timespan', 'resolution', 'autoResolution', 'clientId', 'deviceSerial', 'apTag', 'band'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkWirelessChannelUtilizationHistory

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWirelessClientCountHistory')
def getNetworkWirelessClientCountHistory(networkId: str, t0: str = None, t1: str = None, timespan: float = None, resolution: int = None, autoResolution: bool = None, clientId: str = None, deviceSerial: str = None, apTag: str = None, band: str = None, ssid: int = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if t0 is not None:
        final_kwargs['t0'] = t0
    if t1 is not None:
        final_kwargs['t1'] = t1
    if timespan is not None:
        final_kwargs['timespan'] = timespan
    if resolution is not None:
        final_kwargs['resolution'] = resolution
    if autoResolution is not None:
        final_kwargs['autoResolution'] = autoResolution
    if clientId is not None:
        final_kwargs['clientId'] = clientId
    if deviceSerial is not None:
        final_kwargs['deviceSerial'] = deviceSerial
    if apTag is not None:
        final_kwargs['apTag'] = apTag
    if band is not None:
        final_kwargs['band'] = band
    if ssid is not None:
        final_kwargs['ssid'] = ssid

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 't0', 't1', 'timespan', 'resolution', 'autoResolution', 'clientId', 'deviceSerial', 'apTag', 'band', 'ssid'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 't0', 't1', 'timespan', 'resolution', 'autoResolution', 'clientId', 'deviceSerial', 'apTag', 'band', 'ssid'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 't0', 't1', 'timespan', 'resolution', 'autoResolution', 'clientId', 'deviceSerial', 'apTag', 'band', 'ssid'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkWirelessClientCountHistory

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWirelessClientsConnectionStats')
def getNetworkWirelessClientsConnectionStats(networkId: str, t0: str = None, t1: str = None, timespan: float = None, band: str = None, ssid: int = None, vlan: int = None, apTag: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if t0 is not None:
        final_kwargs['t0'] = t0
    if t1 is not None:
        final_kwargs['t1'] = t1
    if timespan is not None:
        final_kwargs['timespan'] = timespan
    if band is not None:
        final_kwargs['band'] = band
    if ssid is not None:
        final_kwargs['ssid'] = ssid
    if vlan is not None:
        final_kwargs['vlan'] = vlan
    if apTag is not None:
        final_kwargs['apTag'] = apTag

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 't0', 't1', 'timespan', 'band', 'ssid', 'vlan', 'apTag'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 't0', 't1', 'timespan', 'band', 'ssid', 'vlan', 'apTag'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 't0', 't1', 'timespan', 'band', 'ssid', 'vlan', 'apTag'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkWirelessClientsConnectionStats

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWirelessClientsLatencyStats')
def getNetworkWirelessClientsLatencyStats(networkId: str, t0: str = None, t1: str = None, timespan: float = None, band: str = None, ssid: int = None, vlan: int = None, apTag: str = None, fields: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if t0 is not None:
        final_kwargs['t0'] = t0
    if t1 is not None:
        final_kwargs['t1'] = t1
    if timespan is not None:
        final_kwargs['timespan'] = timespan
    if band is not None:
        final_kwargs['band'] = band
    if ssid is not None:
        final_kwargs['ssid'] = ssid
    if vlan is not None:
        final_kwargs['vlan'] = vlan
    if apTag is not None:
        final_kwargs['apTag'] = apTag
    if fields is not None:
        final_kwargs['fields'] = fields

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 't0', 't1', 'timespan', 'band', 'ssid', 'vlan', 'apTag', 'fields'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 't0', 't1', 'timespan', 'band', 'ssid', 'vlan', 'apTag', 'fields'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 't0', 't1', 'timespan', 'band', 'ssid', 'vlan', 'apTag', 'fields'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkWirelessClientsLatencyStats

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWirelessClientConnectionStats')
def getNetworkWirelessClientConnectionStats(networkId: str, clientId: str, t0: str = None, t1: str = None, timespan: float = None, band: str = None, ssid: int = None, vlan: int = None, apTag: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if clientId is not None:
        final_kwargs['clientId'] = clientId
    if t0 is not None:
        final_kwargs['t0'] = t0
    if t1 is not None:
        final_kwargs['t1'] = t1
    if timespan is not None:
        final_kwargs['timespan'] = timespan
    if band is not None:
        final_kwargs['band'] = band
    if ssid is not None:
        final_kwargs['ssid'] = ssid
    if vlan is not None:
        final_kwargs['vlan'] = vlan
    if apTag is not None:
        final_kwargs['apTag'] = apTag

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'clientId', 't0', 't1', 'timespan', 'band', 'ssid', 'vlan', 'apTag'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'clientId', 't0', 't1', 'timespan', 'band', 'ssid', 'vlan', 'apTag'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'clientId', 't0', 't1', 'timespan', 'band', 'ssid', 'vlan', 'apTag'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkWirelessClientConnectionStats

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWirelessClientConnectivityEvents')
def getNetworkWirelessClientConnectivityEvents(networkId: str, clientId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None, sortOrder: str = None, t0: str = None, t1: str = None, timespan: float = None, types: list = None, band: str = None, ssidNumber: int = None, includedSeverities: list = None, deviceSerial: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if clientId is not None:
        final_kwargs['clientId'] = clientId
    if perPage is not None:
        final_kwargs['perPage'] = perPage
    if startingAfter is not None:
        final_kwargs['startingAfter'] = startingAfter
    if endingBefore is not None:
        final_kwargs['endingBefore'] = endingBefore
    if sortOrder is not None:
        final_kwargs['sortOrder'] = sortOrder
    if t0 is not None:
        final_kwargs['t0'] = t0
    if t1 is not None:
        final_kwargs['t1'] = t1
    if timespan is not None:
        final_kwargs['timespan'] = timespan
    if types is not None:
        final_kwargs['types'] = types
    if band is not None:
        final_kwargs['band'] = band
    if ssidNumber is not None:
        final_kwargs['ssidNumber'] = ssidNumber
    if includedSeverities is not None:
        final_kwargs['includedSeverities'] = includedSeverities
    if deviceSerial is not None:
        final_kwargs['deviceSerial'] = deviceSerial

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'clientId', 'perPage', 'startingAfter', 'endingBefore', 'sortOrder', 't0', 't1', 'timespan', 'types', 'band', 'ssidNumber', 'includedSeverities', 'deviceSerial'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'clientId', 'perPage', 'startingAfter', 'endingBefore', 'sortOrder', 't0', 't1', 'timespan', 'types', 'band', 'ssidNumber', 'includedSeverities', 'deviceSerial'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'clientId', 'perPage', 'startingAfter', 'endingBefore', 'sortOrder', 't0', 't1', 'timespan', 'types', 'band', 'ssidNumber', 'includedSeverities', 'deviceSerial'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkWirelessClientConnectivityEvents

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWirelessClientLatencyHistory')
def getNetworkWirelessClientLatencyHistory(networkId: str, clientId: str, t0: str = None, t1: str = None, timespan: float = None, resolution: int = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if clientId is not None:
        final_kwargs['clientId'] = clientId
    if t0 is not None:
        final_kwargs['t0'] = t0
    if t1 is not None:
        final_kwargs['t1'] = t1
    if timespan is not None:
        final_kwargs['timespan'] = timespan
    if resolution is not None:
        final_kwargs['resolution'] = resolution

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'clientId', 't0', 't1', 'timespan', 'resolution'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'clientId', 't0', 't1', 'timespan', 'resolution'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'clientId', 't0', 't1', 'timespan', 'resolution'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkWirelessClientLatencyHistory

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWirelessClientLatencyStats')
def getNetworkWirelessClientLatencyStats(networkId: str, clientId: str, t0: str = None, t1: str = None, timespan: float = None, band: str = None, ssid: int = None, vlan: int = None, apTag: str = None, fields: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if clientId is not None:
        final_kwargs['clientId'] = clientId
    if t0 is not None:
        final_kwargs['t0'] = t0
    if t1 is not None:
        final_kwargs['t1'] = t1
    if timespan is not None:
        final_kwargs['timespan'] = timespan
    if band is not None:
        final_kwargs['band'] = band
    if ssid is not None:
        final_kwargs['ssid'] = ssid
    if vlan is not None:
        final_kwargs['vlan'] = vlan
    if apTag is not None:
        final_kwargs['apTag'] = apTag
    if fields is not None:
        final_kwargs['fields'] = fields

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'clientId', 't0', 't1', 'timespan', 'band', 'ssid', 'vlan', 'apTag', 'fields'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'clientId', 't0', 't1', 'timespan', 'band', 'ssid', 'vlan', 'apTag', 'fields'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'clientId', 't0', 't1', 'timespan', 'band', 'ssid', 'vlan', 'apTag', 'fields'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkWirelessClientLatencyStats

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWirelessConnectionStats')
def getNetworkWirelessConnectionStats(networkId: str, t0: str = None, t1: str = None, timespan: float = None, band: str = None, ssid: int = None, vlan: int = None, apTag: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if t0 is not None:
        final_kwargs['t0'] = t0
    if t1 is not None:
        final_kwargs['t1'] = t1
    if timespan is not None:
        final_kwargs['timespan'] = timespan
    if band is not None:
        final_kwargs['band'] = band
    if ssid is not None:
        final_kwargs['ssid'] = ssid
    if vlan is not None:
        final_kwargs['vlan'] = vlan
    if apTag is not None:
        final_kwargs['apTag'] = apTag

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 't0', 't1', 'timespan', 'band', 'ssid', 'vlan', 'apTag'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 't0', 't1', 'timespan', 'band', 'ssid', 'vlan', 'apTag'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 't0', 't1', 'timespan', 'band', 'ssid', 'vlan', 'apTag'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkWirelessConnectionStats

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWirelessDataRateHistory')
def getNetworkWirelessDataRateHistory(networkId: str, t0: str = None, t1: str = None, timespan: float = None, resolution: int = None, autoResolution: bool = None, clientId: str = None, deviceSerial: str = None, apTag: str = None, band: str = None, ssid: int = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if t0 is not None:
        final_kwargs['t0'] = t0
    if t1 is not None:
        final_kwargs['t1'] = t1
    if timespan is not None:
        final_kwargs['timespan'] = timespan
    if resolution is not None:
        final_kwargs['resolution'] = resolution
    if autoResolution is not None:
        final_kwargs['autoResolution'] = autoResolution
    if clientId is not None:
        final_kwargs['clientId'] = clientId
    if deviceSerial is not None:
        final_kwargs['deviceSerial'] = deviceSerial
    if apTag is not None:
        final_kwargs['apTag'] = apTag
    if band is not None:
        final_kwargs['band'] = band
    if ssid is not None:
        final_kwargs['ssid'] = ssid

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 't0', 't1', 'timespan', 'resolution', 'autoResolution', 'clientId', 'deviceSerial', 'apTag', 'band', 'ssid'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 't0', 't1', 'timespan', 'resolution', 'autoResolution', 'clientId', 'deviceSerial', 'apTag', 'band', 'ssid'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 't0', 't1', 'timespan', 'resolution', 'autoResolution', 'clientId', 'deviceSerial', 'apTag', 'band', 'ssid'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkWirelessDataRateHistory

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWirelessDevicesConnectionStats')
def getNetworkWirelessDevicesConnectionStats(networkId: str, t0: str = None, t1: str = None, timespan: float = None, band: str = None, ssid: int = None, vlan: int = None, apTag: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if t0 is not None:
        final_kwargs['t0'] = t0
    if t1 is not None:
        final_kwargs['t1'] = t1
    if timespan is not None:
        final_kwargs['timespan'] = timespan
    if band is not None:
        final_kwargs['band'] = band
    if ssid is not None:
        final_kwargs['ssid'] = ssid
    if vlan is not None:
        final_kwargs['vlan'] = vlan
    if apTag is not None:
        final_kwargs['apTag'] = apTag

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 't0', 't1', 'timespan', 'band', 'ssid', 'vlan', 'apTag'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 't0', 't1', 'timespan', 'band', 'ssid', 'vlan', 'apTag'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 't0', 't1', 'timespan', 'band', 'ssid', 'vlan', 'apTag'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkWirelessDevicesConnectionStats

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWirelessDevicesLatencyStats')
def getNetworkWirelessDevicesLatencyStats(networkId: str, t0: str = None, t1: str = None, timespan: float = None, band: str = None, ssid: int = None, vlan: int = None, apTag: str = None, fields: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if t0 is not None:
        final_kwargs['t0'] = t0
    if t1 is not None:
        final_kwargs['t1'] = t1
    if timespan is not None:
        final_kwargs['timespan'] = timespan
    if band is not None:
        final_kwargs['band'] = band
    if ssid is not None:
        final_kwargs['ssid'] = ssid
    if vlan is not None:
        final_kwargs['vlan'] = vlan
    if apTag is not None:
        final_kwargs['apTag'] = apTag
    if fields is not None:
        final_kwargs['fields'] = fields

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 't0', 't1', 'timespan', 'band', 'ssid', 'vlan', 'apTag', 'fields'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 't0', 't1', 'timespan', 'band', 'ssid', 'vlan', 'apTag', 'fields'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 't0', 't1', 'timespan', 'band', 'ssid', 'vlan', 'apTag', 'fields'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkWirelessDevicesLatencyStats

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWirelessElectronicShelfLabel')
def getNetworkWirelessElectronicShelfLabel(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkWirelessElectronicShelfLabel

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWirelessElectronicShelfLabelConfiguredDevices')
def getNetworkWirelessElectronicShelfLabelConfiguredDevices(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkWirelessElectronicShelfLabelConfiguredDevices

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWirelessEthernetPortsProfiles')
def getNetworkWirelessEthernetPortsProfiles(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkWirelessEthernetPortsProfiles

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWirelessEthernetPortsProfile')
def getNetworkWirelessEthernetPortsProfile(networkId: str, profileId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if profileId is not None:
        final_kwargs['profileId'] = profileId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'profileId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'profileId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'profileId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkWirelessEthernetPortsProfile

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWirelessFailedConnections')
def getNetworkWirelessFailedConnections(networkId: str, t0: str = None, t1: str = None, timespan: float = None, band: str = None, ssid: int = None, vlan: int = None, apTag: str = None, serial: str = None, clientId: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if t0 is not None:
        final_kwargs['t0'] = t0
    if t1 is not None:
        final_kwargs['t1'] = t1
    if timespan is not None:
        final_kwargs['timespan'] = timespan
    if band is not None:
        final_kwargs['band'] = band
    if ssid is not None:
        final_kwargs['ssid'] = ssid
    if vlan is not None:
        final_kwargs['vlan'] = vlan
    if apTag is not None:
        final_kwargs['apTag'] = apTag
    if serial is not None:
        final_kwargs['serial'] = serial
    if clientId is not None:
        final_kwargs['clientId'] = clientId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 't0', 't1', 'timespan', 'band', 'ssid', 'vlan', 'apTag', 'serial', 'clientId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 't0', 't1', 'timespan', 'band', 'ssid', 'vlan', 'apTag', 'serial', 'clientId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 't0', 't1', 'timespan', 'band', 'ssid', 'vlan', 'apTag', 'serial', 'clientId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkWirelessFailedConnections

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWirelessLatencyHistory')
def getNetworkWirelessLatencyHistory(networkId: str, t0: str = None, t1: str = None, timespan: float = None, resolution: int = None, autoResolution: bool = None, clientId: str = None, deviceSerial: str = None, apTag: str = None, band: str = None, ssid: int = None, accessCategory: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if t0 is not None:
        final_kwargs['t0'] = t0
    if t1 is not None:
        final_kwargs['t1'] = t1
    if timespan is not None:
        final_kwargs['timespan'] = timespan
    if resolution is not None:
        final_kwargs['resolution'] = resolution
    if autoResolution is not None:
        final_kwargs['autoResolution'] = autoResolution
    if clientId is not None:
        final_kwargs['clientId'] = clientId
    if deviceSerial is not None:
        final_kwargs['deviceSerial'] = deviceSerial
    if apTag is not None:
        final_kwargs['apTag'] = apTag
    if band is not None:
        final_kwargs['band'] = band
    if ssid is not None:
        final_kwargs['ssid'] = ssid
    if accessCategory is not None:
        final_kwargs['accessCategory'] = accessCategory

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 't0', 't1', 'timespan', 'resolution', 'autoResolution', 'clientId', 'deviceSerial', 'apTag', 'band', 'ssid', 'accessCategory'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 't0', 't1', 'timespan', 'resolution', 'autoResolution', 'clientId', 'deviceSerial', 'apTag', 'band', 'ssid', 'accessCategory'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 't0', 't1', 'timespan', 'resolution', 'autoResolution', 'clientId', 'deviceSerial', 'apTag', 'band', 'ssid', 'accessCategory'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkWirelessLatencyHistory

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWirelessLatencyStats')
def getNetworkWirelessLatencyStats(networkId: str, t0: str = None, t1: str = None, timespan: float = None, band: str = None, ssid: int = None, vlan: int = None, apTag: str = None, fields: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if t0 is not None:
        final_kwargs['t0'] = t0
    if t1 is not None:
        final_kwargs['t1'] = t1
    if timespan is not None:
        final_kwargs['timespan'] = timespan
    if band is not None:
        final_kwargs['band'] = band
    if ssid is not None:
        final_kwargs['ssid'] = ssid
    if vlan is not None:
        final_kwargs['vlan'] = vlan
    if apTag is not None:
        final_kwargs['apTag'] = apTag
    if fields is not None:
        final_kwargs['fields'] = fields

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 't0', 't1', 'timespan', 'band', 'ssid', 'vlan', 'apTag', 'fields'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 't0', 't1', 'timespan', 'band', 'ssid', 'vlan', 'apTag', 'fields'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 't0', 't1', 'timespan', 'band', 'ssid', 'vlan', 'apTag', 'fields'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkWirelessLatencyStats

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWirelessMeshStatuses')
def getNetworkWirelessMeshStatuses(networkId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if perPage is not None:
        final_kwargs['perPage'] = perPage
    if startingAfter is not None:
        final_kwargs['startingAfter'] = startingAfter
    if endingBefore is not None:
        final_kwargs['endingBefore'] = endingBefore

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'perPage', 'startingAfter', 'endingBefore'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'perPage', 'startingAfter', 'endingBefore'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'perPage', 'startingAfter', 'endingBefore'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkWirelessMeshStatuses

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWirelessRfProfiles')
def getNetworkWirelessRfProfiles(networkId: str, includeTemplateProfiles: bool = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if includeTemplateProfiles is not None:
        final_kwargs['includeTemplateProfiles'] = includeTemplateProfiles

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'includeTemplateProfiles'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'includeTemplateProfiles'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'includeTemplateProfiles'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkWirelessRfProfiles

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWirelessRfProfile')
def getNetworkWirelessRfProfile(networkId: str, rfProfileId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if rfProfileId is not None:
        final_kwargs['rfProfileId'] = rfProfileId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'rfProfileId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'rfProfileId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'rfProfileId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkWirelessRfProfile

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWirelessSettings')
def getNetworkWirelessSettings(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkWirelessSettings

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWirelessSignalQualityHistory')
def getNetworkWirelessSignalQualityHistory(networkId: str, t0: str = None, t1: str = None, timespan: float = None, resolution: int = None, autoResolution: bool = None, clientId: str = None, deviceSerial: str = None, apTag: str = None, band: str = None, ssid: int = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if t0 is not None:
        final_kwargs['t0'] = t0
    if t1 is not None:
        final_kwargs['t1'] = t1
    if timespan is not None:
        final_kwargs['timespan'] = timespan
    if resolution is not None:
        final_kwargs['resolution'] = resolution
    if autoResolution is not None:
        final_kwargs['autoResolution'] = autoResolution
    if clientId is not None:
        final_kwargs['clientId'] = clientId
    if deviceSerial is not None:
        final_kwargs['deviceSerial'] = deviceSerial
    if apTag is not None:
        final_kwargs['apTag'] = apTag
    if band is not None:
        final_kwargs['band'] = band
    if ssid is not None:
        final_kwargs['ssid'] = ssid

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 't0', 't1', 'timespan', 'resolution', 'autoResolution', 'clientId', 'deviceSerial', 'apTag', 'band', 'ssid'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 't0', 't1', 'timespan', 'resolution', 'autoResolution', 'clientId', 'deviceSerial', 'apTag', 'band', 'ssid'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 't0', 't1', 'timespan', 'resolution', 'autoResolution', 'clientId', 'deviceSerial', 'apTag', 'band', 'ssid'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkWirelessSignalQualityHistory

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWirelessSsids')
def getNetworkWirelessSsids(networkId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkWirelessSsids

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWirelessSsid')
def getNetworkWirelessSsid(networkId: str, number: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if number is not None:
        final_kwargs['number'] = number

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'number'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'number'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'number'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkWirelessSsid

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWirelessSsidBonjourForwarding')
def getNetworkWirelessSsidBonjourForwarding(networkId: str, number: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if number is not None:
        final_kwargs['number'] = number

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'number'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'number'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'number'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkWirelessSsidBonjourForwarding

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWirelessSsidDeviceTypeGroupPolicies')
def getNetworkWirelessSsidDeviceTypeGroupPolicies(networkId: str, number: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if number is not None:
        final_kwargs['number'] = number

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'number'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'number'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'number'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkWirelessSsidDeviceTypeGroupPolicies

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWirelessSsidEapOverride')
def getNetworkWirelessSsidEapOverride(networkId: str, number: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if number is not None:
        final_kwargs['number'] = number

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'number'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'number'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'number'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkWirelessSsidEapOverride

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWirelessSsidFirewallL3FirewallRules')
def getNetworkWirelessSsidFirewallL3FirewallRules(networkId: str, number: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if number is not None:
        final_kwargs['number'] = number

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'number'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'number'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'number'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkWirelessSsidFirewallL3FirewallRules

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWirelessSsidFirewallL7FirewallRules')
def getNetworkWirelessSsidFirewallL7FirewallRules(networkId: str, number: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if number is not None:
        final_kwargs['number'] = number

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'number'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'number'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'number'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkWirelessSsidFirewallL7FirewallRules

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWirelessSsidHotspot20')
def getNetworkWirelessSsidHotspot20(networkId: str, number: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if number is not None:
        final_kwargs['number'] = number

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'number'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'number'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'number'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkWirelessSsidHotspot20

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWirelessSsidIdentityPsks')
def getNetworkWirelessSsidIdentityPsks(networkId: str, number: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if number is not None:
        final_kwargs['number'] = number

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'number'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'number'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'number'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkWirelessSsidIdentityPsks

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWirelessSsidIdentityPsk')
def getNetworkWirelessSsidIdentityPsk(networkId: str, number: str, identityPskId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if number is not None:
        final_kwargs['number'] = number
    if identityPskId is not None:
        final_kwargs['identityPskId'] = identityPskId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'number', 'identityPskId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'number', 'identityPskId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'number', 'identityPskId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkWirelessSsidIdentityPsk

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWirelessSsidSchedules')
def getNetworkWirelessSsidSchedules(networkId: str, number: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if number is not None:
        final_kwargs['number'] = number

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'number'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'number'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'number'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkWirelessSsidSchedules

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWirelessSsidSplashSettings')
def getNetworkWirelessSsidSplashSettings(networkId: str, number: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if number is not None:
        final_kwargs['number'] = number

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'number'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'number'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'number'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkWirelessSsidSplashSettings

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWirelessSsidTrafficShapingRules')
def getNetworkWirelessSsidTrafficShapingRules(networkId: str, number: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if number is not None:
        final_kwargs['number'] = number

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'number'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'number'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'number'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkWirelessSsidTrafficShapingRules

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWirelessSsidVpn')
def getNetworkWirelessSsidVpn(networkId: str, number: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if number is not None:
        final_kwargs['number'] = number

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 'number'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 'number'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 'number'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkWirelessSsidVpn

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWirelessUsageHistory')
def getNetworkWirelessUsageHistory(networkId: str, t0: str = None, t1: str = None, timespan: float = None, resolution: int = None, autoResolution: bool = None, clientId: str = None, deviceSerial: str = None, apTag: str = None, band: str = None, ssid: int = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if t0 is not None:
        final_kwargs['t0'] = t0
    if t1 is not None:
        final_kwargs['t1'] = t1
    if timespan is not None:
        final_kwargs['timespan'] = timespan
    if resolution is not None:
        final_kwargs['resolution'] = resolution
    if autoResolution is not None:
        final_kwargs['autoResolution'] = autoResolution
    if clientId is not None:
        final_kwargs['clientId'] = clientId
    if deviceSerial is not None:
        final_kwargs['deviceSerial'] = deviceSerial
    if apTag is not None:
        final_kwargs['apTag'] = apTag
    if band is not None:
        final_kwargs['band'] = band
    if ssid is not None:
        final_kwargs['ssid'] = ssid

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['networkId', 't0', 't1', 'timespan', 'resolution', 'autoResolution', 'clientId', 'deviceSerial', 'apTag', 'band', 'ssid'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['networkId', 't0', 't1', 'timespan', 'resolution', 'autoResolution', 'clientId', 'deviceSerial', 'apTag', 'band', 'ssid'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['networkId', 't0', 't1', 'timespan', 'resolution', 'autoResolution', 'clientId', 'deviceSerial', 'apTag', 'band', 'ssid'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkWirelessUsageHistory

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizations')
def getOrganizations(perPage: int = None, startingAfter: str = None, endingBefore: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if perPage is not None:
        final_kwargs['perPage'] = perPage
    if startingAfter is not None:
        final_kwargs['startingAfter'] = startingAfter
    if endingBefore is not None:
        final_kwargs['endingBefore'] = endingBefore

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['perPage', 'startingAfter', 'endingBefore'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['perPage', 'startingAfter', 'endingBefore'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['perPage', 'startingAfter', 'endingBefore'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizations

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganization')
def getOrganization(organizationId: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganization

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationActionBatches')
def getOrganizationActionBatches(organizationId: str = None, status: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if status is not None:
        final_kwargs['status'] = status

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'status'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'status'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'status'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationActionBatches

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationActionBatch')
def getOrganizationActionBatch(actionBatchId: str, organizationId: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if actionBatchId is not None:
        final_kwargs['actionBatchId'] = actionBatchId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'actionBatchId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'actionBatchId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'actionBatchId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationActionBatch

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationAdaptivePolicyAcls')
def getOrganizationAdaptivePolicyAcls(organizationId: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationAdaptivePolicyAcls

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationAdaptivePolicyAcl')
def getOrganizationAdaptivePolicyAcl(aclId: str, organizationId: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if aclId is not None:
        final_kwargs['aclId'] = aclId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'aclId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'aclId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'aclId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationAdaptivePolicyAcl

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationAdaptivePolicyGroups')
def getOrganizationAdaptivePolicyGroups(organizationId: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationAdaptivePolicyGroups

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationAdaptivePolicyGroup')
def getOrganizationAdaptivePolicyGroup(id: str, organizationId: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if id is not None:
        final_kwargs['id'] = id

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'id'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'id'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'id'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationAdaptivePolicyGroup

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationAdaptivePolicyOverview')
def getOrganizationAdaptivePolicyOverview(organizationId: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationAdaptivePolicyOverview

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationAdaptivePolicyPolicies')
def getOrganizationAdaptivePolicyPolicies(organizationId: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationAdaptivePolicyPolicies

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationAdaptivePolicyPolicy')
def getOrganizationAdaptivePolicyPolicy(id: str, organizationId: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if id is not None:
        final_kwargs['id'] = id

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'id'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'id'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'id'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationAdaptivePolicyPolicy

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationAdaptivePolicySettings')
def getOrganizationAdaptivePolicySettings(organizationId: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationAdaptivePolicySettings

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationAdmins')
def getOrganizationAdmins(organizationId: str = None, networkIds: list = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if networkIds is not None:
        final_kwargs['networkIds'] = networkIds

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'networkIds'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'networkIds'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'networkIds'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationAdmins

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationAlertsProfiles')
def getOrganizationAlertsProfiles(organizationId: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationAlertsProfiles

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationApiRequests')
def getOrganizationApiRequests(organizationId: str = None, t0: str = None, t1: str = None, timespan: float = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None, adminId: str = None, path: str = None, method: str = None, responseCode: int = None, sourceIp: str = None, userAgent: str = None, version: int = None, operationIds: list = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if t0 is not None:
        final_kwargs['t0'] = t0
    if t1 is not None:
        final_kwargs['t1'] = t1
    if timespan is not None:
        final_kwargs['timespan'] = timespan
    if perPage is not None:
        final_kwargs['perPage'] = perPage
    if startingAfter is not None:
        final_kwargs['startingAfter'] = startingAfter
    if endingBefore is not None:
        final_kwargs['endingBefore'] = endingBefore
    if adminId is not None:
        final_kwargs['adminId'] = adminId
    if path is not None:
        final_kwargs['path'] = path
    if method is not None:
        final_kwargs['method'] = method
    if responseCode is not None:
        final_kwargs['responseCode'] = responseCode
    if sourceIp is not None:
        final_kwargs['sourceIp'] = sourceIp
    if userAgent is not None:
        final_kwargs['userAgent'] = userAgent
    if version is not None:
        final_kwargs['version'] = version
    if operationIds is not None:
        final_kwargs['operationIds'] = operationIds

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 't0', 't1', 'timespan', 'perPage', 'startingAfter', 'endingBefore', 'adminId', 'path', 'method', 'responseCode', 'sourceIp', 'userAgent', 'version', 'operationIds'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 't0', 't1', 'timespan', 'perPage', 'startingAfter', 'endingBefore', 'adminId', 'path', 'method', 'responseCode', 'sourceIp', 'userAgent', 'version', 'operationIds'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 't0', 't1', 'timespan', 'perPage', 'startingAfter', 'endingBefore', 'adminId', 'path', 'method', 'responseCode', 'sourceIp', 'userAgent', 'version', 'operationIds'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationApiRequests

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationApiRequestsOverview')
def getOrganizationApiRequestsOverview(organizationId: str = None, t0: str = None, t1: str = None, timespan: float = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if t0 is not None:
        final_kwargs['t0'] = t0
    if t1 is not None:
        final_kwargs['t1'] = t1
    if timespan is not None:
        final_kwargs['timespan'] = timespan

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 't0', 't1', 'timespan'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 't0', 't1', 'timespan'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 't0', 't1', 'timespan'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationApiRequestsOverview

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationApiRequestsOverviewResponseCodesByInterval')
def getOrganizationApiRequestsOverviewResponseCodesByInterval(organizationId: str = None, t0: str = None, t1: str = None, timespan: float = None, interval: int = None, version: int = None, operationIds: list = None, sourceIps: list = None, adminIds: list = None, userAgent: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if t0 is not None:
        final_kwargs['t0'] = t0
    if t1 is not None:
        final_kwargs['t1'] = t1
    if timespan is not None:
        final_kwargs['timespan'] = timespan
    if interval is not None:
        final_kwargs['interval'] = interval
    if version is not None:
        final_kwargs['version'] = version
    if operationIds is not None:
        final_kwargs['operationIds'] = operationIds
    if sourceIps is not None:
        final_kwargs['sourceIps'] = sourceIps
    if adminIds is not None:
        final_kwargs['adminIds'] = adminIds
    if userAgent is not None:
        final_kwargs['userAgent'] = userAgent

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 't0', 't1', 'timespan', 'interval', 'version', 'operationIds', 'sourceIps', 'adminIds', 'userAgent'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 't0', 't1', 'timespan', 'interval', 'version', 'operationIds', 'sourceIps', 'adminIds', 'userAgent'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 't0', 't1', 'timespan', 'interval', 'version', 'operationIds', 'sourceIps', 'adminIds', 'userAgent'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationApiRequestsOverviewResponseCodesByInterval

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationApplianceSecurityEvents')
def getOrganizationApplianceSecurityEvents(organizationId: str = None, t0: str = None, t1: str = None, timespan: float = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None, sortOrder: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if t0 is not None:
        final_kwargs['t0'] = t0
    if t1 is not None:
        final_kwargs['t1'] = t1
    if timespan is not None:
        final_kwargs['timespan'] = timespan
    if perPage is not None:
        final_kwargs['perPage'] = perPage
    if startingAfter is not None:
        final_kwargs['startingAfter'] = startingAfter
    if endingBefore is not None:
        final_kwargs['endingBefore'] = endingBefore
    if sortOrder is not None:
        final_kwargs['sortOrder'] = sortOrder

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 't0', 't1', 'timespan', 'perPage', 'startingAfter', 'endingBefore', 'sortOrder'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 't0', 't1', 'timespan', 'perPage', 'startingAfter', 'endingBefore', 'sortOrder'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 't0', 't1', 'timespan', 'perPage', 'startingAfter', 'endingBefore', 'sortOrder'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationApplianceSecurityEvents

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationApplianceSecurityIntrusion')
def getOrganizationApplianceSecurityIntrusion(organizationId: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationApplianceSecurityIntrusion

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationApplianceTrafficShapingVpnExclusionsByNetwork')
def getOrganizationApplianceTrafficShapingVpnExclusionsByNetwork(organizationId: str = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None, networkIds: list = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if perPage is not None:
        final_kwargs['perPage'] = perPage
    if startingAfter is not None:
        final_kwargs['startingAfter'] = startingAfter
    if endingBefore is not None:
        final_kwargs['endingBefore'] = endingBefore
    if networkIds is not None:
        final_kwargs['networkIds'] = networkIds

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'networkIds'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'networkIds'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'networkIds'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationApplianceTrafficShapingVpnExclusionsByNetwork

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationApplianceUplinkStatuses')
def getOrganizationApplianceUplinkStatuses(organizationId: str = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None, networkIds: list = None, serials: list = None, iccids: list = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if perPage is not None:
        final_kwargs['perPage'] = perPage
    if startingAfter is not None:
        final_kwargs['startingAfter'] = startingAfter
    if endingBefore is not None:
        final_kwargs['endingBefore'] = endingBefore
    if networkIds is not None:
        final_kwargs['networkIds'] = networkIds
    if serials is not None:
        final_kwargs['serials'] = serials
    if iccids is not None:
        final_kwargs['iccids'] = iccids

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'networkIds', 'serials', 'iccids'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'networkIds', 'serials', 'iccids'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'networkIds', 'serials', 'iccids'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationApplianceUplinkStatuses

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationApplianceUplinksStatusesOverview')
def getOrganizationApplianceUplinksStatusesOverview(organizationId: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationApplianceUplinksStatusesOverview

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationApplianceUplinksUsageByNetwork')
def getOrganizationApplianceUplinksUsageByNetwork(organizationId: str = None, t0: str = None, t1: str = None, timespan: float = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if t0 is not None:
        final_kwargs['t0'] = t0
    if t1 is not None:
        final_kwargs['t1'] = t1
    if timespan is not None:
        final_kwargs['timespan'] = timespan

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 't0', 't1', 'timespan'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 't0', 't1', 'timespan'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 't0', 't1', 'timespan'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationApplianceUplinksUsageByNetwork

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationApplianceVpnStats')
def getOrganizationApplianceVpnStats(organizationId: str = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None, networkIds: list = None, t0: str = None, t1: str = None, timespan: float = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if perPage is not None:
        final_kwargs['perPage'] = perPage
    if startingAfter is not None:
        final_kwargs['startingAfter'] = startingAfter
    if endingBefore is not None:
        final_kwargs['endingBefore'] = endingBefore
    if networkIds is not None:
        final_kwargs['networkIds'] = networkIds
    if t0 is not None:
        final_kwargs['t0'] = t0
    if t1 is not None:
        final_kwargs['t1'] = t1
    if timespan is not None:
        final_kwargs['timespan'] = timespan

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'networkIds', 't0', 't1', 'timespan'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'networkIds', 't0', 't1', 'timespan'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'networkIds', 't0', 't1', 'timespan'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationApplianceVpnStats

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationApplianceVpnStatuses')
def getOrganizationApplianceVpnStatuses(organizationId: str = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None, networkIds: list = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if perPage is not None:
        final_kwargs['perPage'] = perPage
    if startingAfter is not None:
        final_kwargs['startingAfter'] = startingAfter
    if endingBefore is not None:
        final_kwargs['endingBefore'] = endingBefore
    if networkIds is not None:
        final_kwargs['networkIds'] = networkIds

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'networkIds'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'networkIds'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'networkIds'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationApplianceVpnStatuses

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationApplianceVpnThirdPartyVPNPeers')
def getOrganizationApplianceVpnThirdPartyVPNPeers(organizationId: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationApplianceVpnThirdPartyVPNPeers

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationApplianceVpnVpnFirewallRules')
def getOrganizationApplianceVpnVpnFirewallRules(organizationId: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationApplianceVpnVpnFirewallRules

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationAssuranceAlerts')
def getOrganizationAssuranceAlerts(organizationId: str = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None, sortOrder: str = None, networkId: str = None, severity: str = None, types: list = None, tsStart: str = None, tsEnd: str = None, category: str = None, sortBy: str = None, serials: list = None, deviceTypes: list = None, deviceTags: list = None, active: bool = None, dismissed: bool = None, resolved: bool = None, suppressAlertsForOfflineNodes: bool = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if perPage is not None:
        final_kwargs['perPage'] = perPage
    if startingAfter is not None:
        final_kwargs['startingAfter'] = startingAfter
    if endingBefore is not None:
        final_kwargs['endingBefore'] = endingBefore
    if sortOrder is not None:
        final_kwargs['sortOrder'] = sortOrder
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if severity is not None:
        final_kwargs['severity'] = severity
    if types is not None:
        final_kwargs['types'] = types
    if tsStart is not None:
        final_kwargs['tsStart'] = tsStart
    if tsEnd is not None:
        final_kwargs['tsEnd'] = tsEnd
    if category is not None:
        final_kwargs['category'] = category
    if sortBy is not None:
        final_kwargs['sortBy'] = sortBy
    if serials is not None:
        final_kwargs['serials'] = serials
    if deviceTypes is not None:
        final_kwargs['deviceTypes'] = deviceTypes
    if deviceTags is not None:
        final_kwargs['deviceTags'] = deviceTags
    if active is not None:
        final_kwargs['active'] = active
    if dismissed is not None:
        final_kwargs['dismissed'] = dismissed
    if resolved is not None:
        final_kwargs['resolved'] = resolved
    if suppressAlertsForOfflineNodes is not None:
        final_kwargs['suppressAlertsForOfflineNodes'] = suppressAlertsForOfflineNodes

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'sortOrder', 'networkId', 'severity', 'types', 'tsStart', 'tsEnd', 'category', 'sortBy', 'serials', 'deviceTypes', 'deviceTags', 'active', 'dismissed', 'resolved', 'suppressAlertsForOfflineNodes'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'sortOrder', 'networkId', 'severity', 'types', 'tsStart', 'tsEnd', 'category', 'sortBy', 'serials', 'deviceTypes', 'deviceTags', 'active', 'dismissed', 'resolved', 'suppressAlertsForOfflineNodes'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'sortOrder', 'networkId', 'severity', 'types', 'tsStart', 'tsEnd', 'category', 'sortBy', 'serials', 'deviceTypes', 'deviceTags', 'active', 'dismissed', 'resolved', 'suppressAlertsForOfflineNodes'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationAssuranceAlerts

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationAssuranceAlertsOverview')
def getOrganizationAssuranceAlertsOverview(organizationId: str = None, networkId: str = None, severity: str = None, types: list = None, tsStart: str = None, tsEnd: str = None, category: str = None, serials: list = None, deviceTypes: list = None, deviceTags: list = None, active: bool = None, dismissed: bool = None, resolved: bool = None, suppressAlertsForOfflineNodes: bool = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if severity is not None:
        final_kwargs['severity'] = severity
    if types is not None:
        final_kwargs['types'] = types
    if tsStart is not None:
        final_kwargs['tsStart'] = tsStart
    if tsEnd is not None:
        final_kwargs['tsEnd'] = tsEnd
    if category is not None:
        final_kwargs['category'] = category
    if serials is not None:
        final_kwargs['serials'] = serials
    if deviceTypes is not None:
        final_kwargs['deviceTypes'] = deviceTypes
    if deviceTags is not None:
        final_kwargs['deviceTags'] = deviceTags
    if active is not None:
        final_kwargs['active'] = active
    if dismissed is not None:
        final_kwargs['dismissed'] = dismissed
    if resolved is not None:
        final_kwargs['resolved'] = resolved
    if suppressAlertsForOfflineNodes is not None:
        final_kwargs['suppressAlertsForOfflineNodes'] = suppressAlertsForOfflineNodes

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'networkId', 'severity', 'types', 'tsStart', 'tsEnd', 'category', 'serials', 'deviceTypes', 'deviceTags', 'active', 'dismissed', 'resolved', 'suppressAlertsForOfflineNodes'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'networkId', 'severity', 'types', 'tsStart', 'tsEnd', 'category', 'serials', 'deviceTypes', 'deviceTags', 'active', 'dismissed', 'resolved', 'suppressAlertsForOfflineNodes'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'networkId', 'severity', 'types', 'tsStart', 'tsEnd', 'category', 'serials', 'deviceTypes', 'deviceTags', 'active', 'dismissed', 'resolved', 'suppressAlertsForOfflineNodes'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationAssuranceAlertsOverview

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationAssuranceAlertsOverviewByNetwork')
def getOrganizationAssuranceAlertsOverviewByNetwork(organizationId: str = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None, sortOrder: str = None, networkId: str = None, severity: str = None, types: list = None, tsStart: str = None, tsEnd: str = None, category: str = None, serials: list = None, deviceTypes: list = None, deviceTags: list = None, active: bool = None, dismissed: bool = None, resolved: bool = None, suppressAlertsForOfflineNodes: bool = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if perPage is not None:
        final_kwargs['perPage'] = perPage
    if startingAfter is not None:
        final_kwargs['startingAfter'] = startingAfter
    if endingBefore is not None:
        final_kwargs['endingBefore'] = endingBefore
    if sortOrder is not None:
        final_kwargs['sortOrder'] = sortOrder
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if severity is not None:
        final_kwargs['severity'] = severity
    if types is not None:
        final_kwargs['types'] = types
    if tsStart is not None:
        final_kwargs['tsStart'] = tsStart
    if tsEnd is not None:
        final_kwargs['tsEnd'] = tsEnd
    if category is not None:
        final_kwargs['category'] = category
    if serials is not None:
        final_kwargs['serials'] = serials
    if deviceTypes is not None:
        final_kwargs['deviceTypes'] = deviceTypes
    if deviceTags is not None:
        final_kwargs['deviceTags'] = deviceTags
    if active is not None:
        final_kwargs['active'] = active
    if dismissed is not None:
        final_kwargs['dismissed'] = dismissed
    if resolved is not None:
        final_kwargs['resolved'] = resolved
    if suppressAlertsForOfflineNodes is not None:
        final_kwargs['suppressAlertsForOfflineNodes'] = suppressAlertsForOfflineNodes

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'sortOrder', 'networkId', 'severity', 'types', 'tsStart', 'tsEnd', 'category', 'serials', 'deviceTypes', 'deviceTags', 'active', 'dismissed', 'resolved', 'suppressAlertsForOfflineNodes'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'sortOrder', 'networkId', 'severity', 'types', 'tsStart', 'tsEnd', 'category', 'serials', 'deviceTypes', 'deviceTags', 'active', 'dismissed', 'resolved', 'suppressAlertsForOfflineNodes'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'sortOrder', 'networkId', 'severity', 'types', 'tsStart', 'tsEnd', 'category', 'serials', 'deviceTypes', 'deviceTags', 'active', 'dismissed', 'resolved', 'suppressAlertsForOfflineNodes'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationAssuranceAlertsOverviewByNetwork

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationAssuranceAlertsOverviewByType')
def getOrganizationAssuranceAlertsOverviewByType(organizationId: str = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None, sortOrder: str = None, networkId: str = None, severity: str = None, types: list = None, tsStart: str = None, tsEnd: str = None, category: str = None, sortBy: str = None, serials: list = None, deviceTypes: list = None, deviceTags: list = None, active: bool = None, dismissed: bool = None, resolved: bool = None, suppressAlertsForOfflineNodes: bool = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if perPage is not None:
        final_kwargs['perPage'] = perPage
    if startingAfter is not None:
        final_kwargs['startingAfter'] = startingAfter
    if endingBefore is not None:
        final_kwargs['endingBefore'] = endingBefore
    if sortOrder is not None:
        final_kwargs['sortOrder'] = sortOrder
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if severity is not None:
        final_kwargs['severity'] = severity
    if types is not None:
        final_kwargs['types'] = types
    if tsStart is not None:
        final_kwargs['tsStart'] = tsStart
    if tsEnd is not None:
        final_kwargs['tsEnd'] = tsEnd
    if category is not None:
        final_kwargs['category'] = category
    if sortBy is not None:
        final_kwargs['sortBy'] = sortBy
    if serials is not None:
        final_kwargs['serials'] = serials
    if deviceTypes is not None:
        final_kwargs['deviceTypes'] = deviceTypes
    if deviceTags is not None:
        final_kwargs['deviceTags'] = deviceTags
    if active is not None:
        final_kwargs['active'] = active
    if dismissed is not None:
        final_kwargs['dismissed'] = dismissed
    if resolved is not None:
        final_kwargs['resolved'] = resolved
    if suppressAlertsForOfflineNodes is not None:
        final_kwargs['suppressAlertsForOfflineNodes'] = suppressAlertsForOfflineNodes

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'sortOrder', 'networkId', 'severity', 'types', 'tsStart', 'tsEnd', 'category', 'sortBy', 'serials', 'deviceTypes', 'deviceTags', 'active', 'dismissed', 'resolved', 'suppressAlertsForOfflineNodes'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'sortOrder', 'networkId', 'severity', 'types', 'tsStart', 'tsEnd', 'category', 'sortBy', 'serials', 'deviceTypes', 'deviceTags', 'active', 'dismissed', 'resolved', 'suppressAlertsForOfflineNodes'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'sortOrder', 'networkId', 'severity', 'types', 'tsStart', 'tsEnd', 'category', 'sortBy', 'serials', 'deviceTypes', 'deviceTags', 'active', 'dismissed', 'resolved', 'suppressAlertsForOfflineNodes'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationAssuranceAlertsOverviewByType

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationAssuranceAlertsOverviewHistorical')
def getOrganizationAssuranceAlertsOverviewHistorical(segmentDuration: int, tsStart: str, organizationId: str = None, networkId: str = None, severity: str = None, types: list = None, tsEnd: str = None, category: str = None, serials: list = None, deviceTypes: list = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if segmentDuration is not None:
        final_kwargs['segmentDuration'] = segmentDuration
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if severity is not None:
        final_kwargs['severity'] = severity
    if types is not None:
        final_kwargs['types'] = types
    if tsStart is not None:
        final_kwargs['tsStart'] = tsStart
    if tsEnd is not None:
        final_kwargs['tsEnd'] = tsEnd
    if category is not None:
        final_kwargs['category'] = category
    if serials is not None:
        final_kwargs['serials'] = serials
    if deviceTypes is not None:
        final_kwargs['deviceTypes'] = deviceTypes

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'segmentDuration', 'networkId', 'severity', 'types', 'tsStart', 'tsEnd', 'category', 'serials', 'deviceTypes'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'segmentDuration', 'networkId', 'severity', 'types', 'tsStart', 'tsEnd', 'category', 'serials', 'deviceTypes'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'segmentDuration', 'networkId', 'severity', 'types', 'tsStart', 'tsEnd', 'category', 'serials', 'deviceTypes'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationAssuranceAlertsOverviewHistorical

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationAssuranceAlert')
def getOrganizationAssuranceAlert(id: str, organizationId: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if id is not None:
        final_kwargs['id'] = id

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'id'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'id'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'id'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationAssuranceAlert

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationBrandingPolicies')
def getOrganizationBrandingPolicies(organizationId: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationBrandingPolicies

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationBrandingPoliciesPriorities')
def getOrganizationBrandingPoliciesPriorities(organizationId: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationBrandingPoliciesPriorities

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationBrandingPolicy')
def getOrganizationBrandingPolicy(brandingPolicyId: str, organizationId: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if brandingPolicyId is not None:
        final_kwargs['brandingPolicyId'] = brandingPolicyId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'brandingPolicyId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'brandingPolicyId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'brandingPolicyId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationBrandingPolicy

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationCameraBoundariesAreasByDevice')
def getOrganizationCameraBoundariesAreasByDevice(organizationId: str = None, serials: list = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if serials is not None:
        final_kwargs['serials'] = serials

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'serials'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'serials'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'serials'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationCameraBoundariesAreasByDevice

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationCameraBoundariesLinesByDevice')
def getOrganizationCameraBoundariesLinesByDevice(organizationId: str = None, serials: list = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if serials is not None:
        final_kwargs['serials'] = serials

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'serials'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'serials'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'serials'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationCameraBoundariesLinesByDevice

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationCameraCustomAnalyticsArtifacts')
def getOrganizationCameraCustomAnalyticsArtifacts(organizationId: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationCameraCustomAnalyticsArtifacts

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationCameraCustomAnalyticsArtifact')
def getOrganizationCameraCustomAnalyticsArtifact(artifactId: str, organizationId: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if artifactId is not None:
        final_kwargs['artifactId'] = artifactId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'artifactId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'artifactId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'artifactId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationCameraCustomAnalyticsArtifact

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationCameraDetectionsHistoryByBoundaryByInterval')
def getOrganizationCameraDetectionsHistoryByBoundaryByInterval(boundaryIds: list, ranges: list, organizationId: str = None, duration: int = None, perPage: int = None, boundaryTypes: list = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if boundaryIds is not None:
        final_kwargs['boundaryIds'] = boundaryIds
    if ranges is not None:
        final_kwargs['ranges'] = ranges
    if duration is not None:
        final_kwargs['duration'] = duration
    if perPage is not None:
        final_kwargs['perPage'] = perPage
    if boundaryTypes is not None:
        final_kwargs['boundaryTypes'] = boundaryTypes

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'boundaryIds', 'ranges', 'duration', 'perPage', 'boundaryTypes'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'boundaryIds', 'ranges', 'duration', 'perPage', 'boundaryTypes'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'boundaryIds', 'ranges', 'duration', 'perPage', 'boundaryTypes'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationCameraDetectionsHistoryByBoundaryByInterval

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationCameraOnboardingStatuses')
def getOrganizationCameraOnboardingStatuses(organizationId: str = None, serials: list = None, networkIds: list = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if serials is not None:
        final_kwargs['serials'] = serials
    if networkIds is not None:
        final_kwargs['networkIds'] = networkIds

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'serials', 'networkIds'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'serials', 'networkIds'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'serials', 'networkIds'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationCameraOnboardingStatuses

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationCameraPermissions')
def getOrganizationCameraPermissions(organizationId: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationCameraPermissions

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationCameraPermission')
def getOrganizationCameraPermission(permissionScopeId: str, organizationId: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if permissionScopeId is not None:
        final_kwargs['permissionScopeId'] = permissionScopeId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'permissionScopeId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'permissionScopeId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'permissionScopeId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationCameraPermission

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationCameraRoles')
def getOrganizationCameraRoles(organizationId: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationCameraRoles

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationCameraRole')
def getOrganizationCameraRole(roleId: str, organizationId: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if roleId is not None:
        final_kwargs['roleId'] = roleId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'roleId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'roleId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'roleId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationCameraRole

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationCellularGatewayEsimsInventory')
def getOrganizationCellularGatewayEsimsInventory(organizationId: str = None, eids: list = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if eids is not None:
        final_kwargs['eids'] = eids

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'eids'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'eids'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'eids'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationCellularGatewayEsimsInventory

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationCellularGatewayEsimsServiceProviders')
def getOrganizationCellularGatewayEsimsServiceProviders(organizationId: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationCellularGatewayEsimsServiceProviders

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationCellularGatewayEsimsServiceProvidersAccounts')
def getOrganizationCellularGatewayEsimsServiceProvidersAccounts(organizationId: str = None, accountIds: list = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if accountIds is not None:
        final_kwargs['accountIds'] = accountIds

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'accountIds'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'accountIds'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'accountIds'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationCellularGatewayEsimsServiceProvidersAccounts

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationCellularGatewayEsimsServiceProvidersAccountsCommu')
def getOrganizationCellularGatewayEsimsServiceProvidersAccountsCommu(accountIds: list, organizationId: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if accountIds is not None:
        final_kwargs['accountIds'] = accountIds

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'accountIds'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'accountIds'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'accountIds'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationCellularGatewayEsimsServiceProvidersAccountsCommu

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationCellularGatewayEsimsServiceProvidersAccountsRateP')
def getOrganizationCellularGatewayEsimsServiceProvidersAccountsRateP(accountIds: list, organizationId: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if accountIds is not None:
        final_kwargs['accountIds'] = accountIds

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'accountIds'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'accountIds'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'accountIds'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationCellularGatewayEsimsServiceProvidersAccountsRateP

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationCellularGatewayUplinkStatuses')
def getOrganizationCellularGatewayUplinkStatuses(organizationId: str = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None, networkIds: list = None, serials: list = None, iccids: list = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if perPage is not None:
        final_kwargs['perPage'] = perPage
    if startingAfter is not None:
        final_kwargs['startingAfter'] = startingAfter
    if endingBefore is not None:
        final_kwargs['endingBefore'] = endingBefore
    if networkIds is not None:
        final_kwargs['networkIds'] = networkIds
    if serials is not None:
        final_kwargs['serials'] = serials
    if iccids is not None:
        final_kwargs['iccids'] = iccids

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'networkIds', 'serials', 'iccids'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'networkIds', 'serials', 'iccids'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'networkIds', 'serials', 'iccids'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationCellularGatewayUplinkStatuses

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationClientsBandwidthUsageHistory')
def getOrganizationClientsBandwidthUsageHistory(organizationId: str = None, networkTag: str = None, deviceTag: str = None, ssidName: str = None, usageUplink: str = None, t0: str = None, t1: str = None, timespan: float = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if networkTag is not None:
        final_kwargs['networkTag'] = networkTag
    if deviceTag is not None:
        final_kwargs['deviceTag'] = deviceTag
    if ssidName is not None:
        final_kwargs['ssidName'] = ssidName
    if usageUplink is not None:
        final_kwargs['usageUplink'] = usageUplink
    if t0 is not None:
        final_kwargs['t0'] = t0
    if t1 is not None:
        final_kwargs['t1'] = t1
    if timespan is not None:
        final_kwargs['timespan'] = timespan

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'networkTag', 'deviceTag', 'ssidName', 'usageUplink', 't0', 't1', 'timespan'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'networkTag', 'deviceTag', 'ssidName', 'usageUplink', 't0', 't1', 'timespan'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'networkTag', 'deviceTag', 'ssidName', 'usageUplink', 't0', 't1', 'timespan'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationClientsBandwidthUsageHistory

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationClientsOverview')
def getOrganizationClientsOverview(organizationId: str = None, t0: str = None, t1: str = None, timespan: float = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if t0 is not None:
        final_kwargs['t0'] = t0
    if t1 is not None:
        final_kwargs['t1'] = t1
    if timespan is not None:
        final_kwargs['timespan'] = timespan

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 't0', 't1', 'timespan'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 't0', 't1', 'timespan'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 't0', 't1', 'timespan'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationClientsOverview

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationClientsSearch')
def getOrganizationClientsSearch(mac: str, organizationId: str = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if perPage is not None:
        final_kwargs['perPage'] = perPage
    if startingAfter is not None:
        final_kwargs['startingAfter'] = startingAfter
    if endingBefore is not None:
        final_kwargs['endingBefore'] = endingBefore
    if mac is not None:
        final_kwargs['mac'] = mac

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'mac'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'mac'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'mac'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationClientsSearch

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationConfigTemplates')
def getOrganizationConfigTemplates(organizationId: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationConfigTemplates

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationConfigTemplate')
def getOrganizationConfigTemplate(configTemplateId: str, organizationId: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if configTemplateId is not None:
        final_kwargs['configTemplateId'] = configTemplateId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'configTemplateId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'configTemplateId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'configTemplateId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationConfigTemplate

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationConfigTemplateSwitchProfiles')
def getOrganizationConfigTemplateSwitchProfiles(configTemplateId: str, organizationId: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if configTemplateId is not None:
        final_kwargs['configTemplateId'] = configTemplateId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'configTemplateId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'configTemplateId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'configTemplateId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationConfigTemplateSwitchProfiles

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationConfigTemplateSwitchProfilePorts')
def getOrganizationConfigTemplateSwitchProfilePorts(configTemplateId: str, profileId: str, organizationId: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if configTemplateId is not None:
        final_kwargs['configTemplateId'] = configTemplateId
    if profileId is not None:
        final_kwargs['profileId'] = profileId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'configTemplateId', 'profileId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'configTemplateId', 'profileId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'configTemplateId', 'profileId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationConfigTemplateSwitchProfilePorts

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationConfigTemplateSwitchProfilePort')
def getOrganizationConfigTemplateSwitchProfilePort(configTemplateId: str, profileId: str, portId: str, organizationId: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if configTemplateId is not None:
        final_kwargs['configTemplateId'] = configTemplateId
    if profileId is not None:
        final_kwargs['profileId'] = profileId
    if portId is not None:
        final_kwargs['portId'] = portId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'configTemplateId', 'profileId', 'portId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'configTemplateId', 'profileId', 'portId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'configTemplateId', 'profileId', 'portId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationConfigTemplateSwitchProfilePort

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationConfigurationChanges')
def getOrganizationConfigurationChanges(organizationId: str = None, t0: str = None, t1: str = None, timespan: float = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None, networkId: str = None, adminId: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if t0 is not None:
        final_kwargs['t0'] = t0
    if t1 is not None:
        final_kwargs['t1'] = t1
    if timespan is not None:
        final_kwargs['timespan'] = timespan
    if perPage is not None:
        final_kwargs['perPage'] = perPage
    if startingAfter is not None:
        final_kwargs['startingAfter'] = startingAfter
    if endingBefore is not None:
        final_kwargs['endingBefore'] = endingBefore
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if adminId is not None:
        final_kwargs['adminId'] = adminId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 't0', 't1', 'timespan', 'perPage', 'startingAfter', 'endingBefore', 'networkId', 'adminId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 't0', 't1', 'timespan', 'perPage', 'startingAfter', 'endingBefore', 'networkId', 'adminId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 't0', 't1', 'timespan', 'perPage', 'startingAfter', 'endingBefore', 'networkId', 'adminId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationConfigurationChanges

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationDevices')
def getOrganizationDevices(organizationId: str = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None, configurationUpdatedAfter: str = None, networkIds: list = None, productTypes: list = None, tags: list = None, tagsFilterType: str = None, name: str = None, mac: str = None, serial: str = None, model: str = None, macs: list = None, serials: list = None, sensorMetrics: list = None, sensorAlertProfileIds: list = None, models: list = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if perPage is not None:
        final_kwargs['perPage'] = perPage
    if startingAfter is not None:
        final_kwargs['startingAfter'] = startingAfter
    if endingBefore is not None:
        final_kwargs['endingBefore'] = endingBefore
    if configurationUpdatedAfter is not None:
        final_kwargs['configurationUpdatedAfter'] = configurationUpdatedAfter
    if networkIds is not None:
        final_kwargs['networkIds'] = networkIds
    if productTypes is not None:
        final_kwargs['productTypes'] = productTypes
    if tags is not None:
        final_kwargs['tags'] = tags
    if tagsFilterType is not None:
        final_kwargs['tagsFilterType'] = tagsFilterType
    if name is not None:
        final_kwargs['name'] = name
    if mac is not None:
        final_kwargs['mac'] = mac
    if serial is not None:
        final_kwargs['serial'] = serial
    if model is not None:
        final_kwargs['model'] = model
    if macs is not None:
        final_kwargs['macs'] = macs
    if serials is not None:
        final_kwargs['serials'] = serials
    if sensorMetrics is not None:
        final_kwargs['sensorMetrics'] = sensorMetrics
    if sensorAlertProfileIds is not None:
        final_kwargs['sensorAlertProfileIds'] = sensorAlertProfileIds
    if models is not None:
        final_kwargs['models'] = models

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'configurationUpdatedAfter', 'networkIds', 'productTypes', 'tags', 'tagsFilterType', 'name', 'mac', 'serial', 'model', 'macs', 'serials', 'sensorMetrics', 'sensorAlertProfileIds', 'models'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'configurationUpdatedAfter', 'networkIds', 'productTypes', 'tags', 'tagsFilterType', 'name', 'mac', 'serial', 'model', 'macs', 'serials', 'sensorMetrics', 'sensorAlertProfileIds', 'models'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'configurationUpdatedAfter', 'networkIds', 'productTypes', 'tags', 'tagsFilterType', 'name', 'mac', 'serial', 'model', 'macs', 'serials', 'sensorMetrics', 'sensorAlertProfileIds', 'models'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationDevices

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationDevicesAvailabilities')
def getOrganizationDevicesAvailabilities(organizationId: str = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None, networkIds: list = None, productTypes: list = None, serials: list = None, tags: list = None, tagsFilterType: str = None, statuses: list = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if perPage is not None:
        final_kwargs['perPage'] = perPage
    if startingAfter is not None:
        final_kwargs['startingAfter'] = startingAfter
    if endingBefore is not None:
        final_kwargs['endingBefore'] = endingBefore
    if networkIds is not None:
        final_kwargs['networkIds'] = networkIds
    if productTypes is not None:
        final_kwargs['productTypes'] = productTypes
    if serials is not None:
        final_kwargs['serials'] = serials
    if tags is not None:
        final_kwargs['tags'] = tags
    if tagsFilterType is not None:
        final_kwargs['tagsFilterType'] = tagsFilterType
    if statuses is not None:
        final_kwargs['statuses'] = statuses

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'networkIds', 'productTypes', 'serials', 'tags', 'tagsFilterType', 'statuses'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'networkIds', 'productTypes', 'serials', 'tags', 'tagsFilterType', 'statuses'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'networkIds', 'productTypes', 'serials', 'tags', 'tagsFilterType', 'statuses'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationDevicesAvailabilities

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationDevicesAvailabilitiesChangeHistory')
def getOrganizationDevicesAvailabilitiesChangeHistory(organizationId: str = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None, t0: str = None, t1: str = None, timespan: float = None, serials: list = None, productTypes: list = None, networkIds: list = None, statuses: list = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if perPage is not None:
        final_kwargs['perPage'] = perPage
    if startingAfter is not None:
        final_kwargs['startingAfter'] = startingAfter
    if endingBefore is not None:
        final_kwargs['endingBefore'] = endingBefore
    if t0 is not None:
        final_kwargs['t0'] = t0
    if t1 is not None:
        final_kwargs['t1'] = t1
    if timespan is not None:
        final_kwargs['timespan'] = timespan
    if serials is not None:
        final_kwargs['serials'] = serials
    if productTypes is not None:
        final_kwargs['productTypes'] = productTypes
    if networkIds is not None:
        final_kwargs['networkIds'] = networkIds
    if statuses is not None:
        final_kwargs['statuses'] = statuses

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 't0', 't1', 'timespan', 'serials', 'productTypes', 'networkIds', 'statuses'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 't0', 't1', 'timespan', 'serials', 'productTypes', 'networkIds', 'statuses'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 't0', 't1', 'timespan', 'serials', 'productTypes', 'networkIds', 'statuses'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationDevicesAvailabilitiesChangeHistory

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationDevicesOverviewByModel')
def getOrganizationDevicesOverviewByModel(organizationId: str = None, models: list = None, networkIds: list = None, productTypes: list = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if models is not None:
        final_kwargs['models'] = models
    if networkIds is not None:
        final_kwargs['networkIds'] = networkIds
    if productTypes is not None:
        final_kwargs['productTypes'] = productTypes

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'models', 'networkIds', 'productTypes'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'models', 'networkIds', 'productTypes'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'models', 'networkIds', 'productTypes'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationDevicesOverviewByModel

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationDevicesPowerModulesStatusesByDevice')
def getOrganizationDevicesPowerModulesStatusesByDevice(organizationId: str = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None, networkIds: list = None, productTypes: list = None, serials: list = None, tags: list = None, tagsFilterType: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if perPage is not None:
        final_kwargs['perPage'] = perPage
    if startingAfter is not None:
        final_kwargs['startingAfter'] = startingAfter
    if endingBefore is not None:
        final_kwargs['endingBefore'] = endingBefore
    if networkIds is not None:
        final_kwargs['networkIds'] = networkIds
    if productTypes is not None:
        final_kwargs['productTypes'] = productTypes
    if serials is not None:
        final_kwargs['serials'] = serials
    if tags is not None:
        final_kwargs['tags'] = tags
    if tagsFilterType is not None:
        final_kwargs['tagsFilterType'] = tagsFilterType

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'networkIds', 'productTypes', 'serials', 'tags', 'tagsFilterType'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'networkIds', 'productTypes', 'serials', 'tags', 'tagsFilterType'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'networkIds', 'productTypes', 'serials', 'tags', 'tagsFilterType'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationDevicesPowerModulesStatusesByDevice

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationDevicesProvisioningStatuses')
def getOrganizationDevicesProvisioningStatuses(organizationId: str = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None, networkIds: list = None, productTypes: list = None, serials: list = None, status: str = None, tags: list = None, tagsFilterType: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if perPage is not None:
        final_kwargs['perPage'] = perPage
    if startingAfter is not None:
        final_kwargs['startingAfter'] = startingAfter
    if endingBefore is not None:
        final_kwargs['endingBefore'] = endingBefore
    if networkIds is not None:
        final_kwargs['networkIds'] = networkIds
    if productTypes is not None:
        final_kwargs['productTypes'] = productTypes
    if serials is not None:
        final_kwargs['serials'] = serials
    if status is not None:
        final_kwargs['status'] = status
    if tags is not None:
        final_kwargs['tags'] = tags
    if tagsFilterType is not None:
        final_kwargs['tagsFilterType'] = tagsFilterType

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'networkIds', 'productTypes', 'serials', 'status', 'tags', 'tagsFilterType'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'networkIds', 'productTypes', 'serials', 'status', 'tags', 'tagsFilterType'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'networkIds', 'productTypes', 'serials', 'status', 'tags', 'tagsFilterType'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationDevicesProvisioningStatuses

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationDevicesStatuses')
def getOrganizationDevicesStatuses(organizationId: str = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None, networkIds: list = None, serials: list = None, statuses: list = None, productTypes: list = None, models: list = None, tags: list = None, tagsFilterType: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if perPage is not None:
        final_kwargs['perPage'] = perPage
    if startingAfter is not None:
        final_kwargs['startingAfter'] = startingAfter
    if endingBefore is not None:
        final_kwargs['endingBefore'] = endingBefore
    if networkIds is not None:
        final_kwargs['networkIds'] = networkIds
    if serials is not None:
        final_kwargs['serials'] = serials
    if statuses is not None:
        final_kwargs['statuses'] = statuses
    if productTypes is not None:
        final_kwargs['productTypes'] = productTypes
    if models is not None:
        final_kwargs['models'] = models
    if tags is not None:
        final_kwargs['tags'] = tags
    if tagsFilterType is not None:
        final_kwargs['tagsFilterType'] = tagsFilterType

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'networkIds', 'serials', 'statuses', 'productTypes', 'models', 'tags', 'tagsFilterType'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'networkIds', 'serials', 'statuses', 'productTypes', 'models', 'tags', 'tagsFilterType'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'networkIds', 'serials', 'statuses', 'productTypes', 'models', 'tags', 'tagsFilterType'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationDevicesStatuses

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationDevicesStatusesOverview')
def getOrganizationDevicesStatusesOverview(organizationId: str = None, productTypes: list = None, networkIds: list = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if productTypes is not None:
        final_kwargs['productTypes'] = productTypes
    if networkIds is not None:
        final_kwargs['networkIds'] = networkIds

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'productTypes', 'networkIds'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'productTypes', 'networkIds'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'productTypes', 'networkIds'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationDevicesStatusesOverview

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationDevicesUplinksAddressesByDevice')
def getOrganizationDevicesUplinksAddressesByDevice(organizationId: str = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None, networkIds: list = None, productTypes: list = None, serials: list = None, tags: list = None, tagsFilterType: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if perPage is not None:
        final_kwargs['perPage'] = perPage
    if startingAfter is not None:
        final_kwargs['startingAfter'] = startingAfter
    if endingBefore is not None:
        final_kwargs['endingBefore'] = endingBefore
    if networkIds is not None:
        final_kwargs['networkIds'] = networkIds
    if productTypes is not None:
        final_kwargs['productTypes'] = productTypes
    if serials is not None:
        final_kwargs['serials'] = serials
    if tags is not None:
        final_kwargs['tags'] = tags
    if tagsFilterType is not None:
        final_kwargs['tagsFilterType'] = tagsFilterType

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'networkIds', 'productTypes', 'serials', 'tags', 'tagsFilterType'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'networkIds', 'productTypes', 'serials', 'tags', 'tagsFilterType'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'networkIds', 'productTypes', 'serials', 'tags', 'tagsFilterType'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationDevicesUplinksAddressesByDevice

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationDevicesUplinksLossAndLatency')
def getOrganizationDevicesUplinksLossAndLatency(organizationId: str = None, t0: str = None, t1: str = None, timespan: float = None, uplink: str = None, ip: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if t0 is not None:
        final_kwargs['t0'] = t0
    if t1 is not None:
        final_kwargs['t1'] = t1
    if timespan is not None:
        final_kwargs['timespan'] = timespan
    if uplink is not None:
        final_kwargs['uplink'] = uplink
    if ip is not None:
        final_kwargs['ip'] = ip

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 't0', 't1', 'timespan', 'uplink', 'ip'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 't0', 't1', 'timespan', 'uplink', 'ip'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 't0', 't1', 'timespan', 'uplink', 'ip'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationDevicesUplinksLossAndLatency

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationEarlyAccessFeatures')
def getOrganizationEarlyAccessFeatures(organizationId: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationEarlyAccessFeatures

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationEarlyAccessFeaturesOptIns')
def getOrganizationEarlyAccessFeaturesOptIns(organizationId: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationEarlyAccessFeaturesOptIns

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationEarlyAccessFeaturesOptIn')
def getOrganizationEarlyAccessFeaturesOptIn(optInId: str, organizationId: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if optInId is not None:
        final_kwargs['optInId'] = optInId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'optInId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'optInId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'optInId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationEarlyAccessFeaturesOptIn

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationFirmwareUpgrades')
def getOrganizationFirmwareUpgrades(organizationId: str = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None, status: list = None, productTypes: list = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if perPage is not None:
        final_kwargs['perPage'] = perPage
    if startingAfter is not None:
        final_kwargs['startingAfter'] = startingAfter
    if endingBefore is not None:
        final_kwargs['endingBefore'] = endingBefore
    if status is not None:
        final_kwargs['status'] = status
    if productTypes is not None:
        final_kwargs['productTypes'] = productTypes

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'status', 'productTypes'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'status', 'productTypes'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'status', 'productTypes'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationFirmwareUpgrades

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationFirmwareUpgradesByDevice')
def getOrganizationFirmwareUpgradesByDevice(organizationId: str = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None, networkIds: list = None, serials: list = None, macs: list = None, firmwareUpgradeBatchIds: list = None, upgradeStatuses: list = None, currentUpgradesOnly: bool = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if perPage is not None:
        final_kwargs['perPage'] = perPage
    if startingAfter is not None:
        final_kwargs['startingAfter'] = startingAfter
    if endingBefore is not None:
        final_kwargs['endingBefore'] = endingBefore
    if networkIds is not None:
        final_kwargs['networkIds'] = networkIds
    if serials is not None:
        final_kwargs['serials'] = serials
    if macs is not None:
        final_kwargs['macs'] = macs
    if firmwareUpgradeBatchIds is not None:
        final_kwargs['firmwareUpgradeBatchIds'] = firmwareUpgradeBatchIds
    if upgradeStatuses is not None:
        final_kwargs['upgradeStatuses'] = upgradeStatuses
    if currentUpgradesOnly is not None:
        final_kwargs['currentUpgradesOnly'] = currentUpgradesOnly

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'networkIds', 'serials', 'macs', 'firmwareUpgradeBatchIds', 'upgradeStatuses', 'currentUpgradesOnly'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'networkIds', 'serials', 'macs', 'firmwareUpgradeBatchIds', 'upgradeStatuses', 'currentUpgradesOnly'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'networkIds', 'serials', 'macs', 'firmwareUpgradeBatchIds', 'upgradeStatuses', 'currentUpgradesOnly'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationFirmwareUpgradesByDevice

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationFloorPlansAutoLocateDevices')
def getOrganizationFloorPlansAutoLocateDevices(organizationId: str = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None, networkIds: list = None, floorPlanIds: list = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if perPage is not None:
        final_kwargs['perPage'] = perPage
    if startingAfter is not None:
        final_kwargs['startingAfter'] = startingAfter
    if endingBefore is not None:
        final_kwargs['endingBefore'] = endingBefore
    if networkIds is not None:
        final_kwargs['networkIds'] = networkIds
    if floorPlanIds is not None:
        final_kwargs['floorPlanIds'] = floorPlanIds

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'networkIds', 'floorPlanIds'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'networkIds', 'floorPlanIds'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'networkIds', 'floorPlanIds'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationFloorPlansAutoLocateDevices

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationFloorPlansAutoLocateStatuses')
def getOrganizationFloorPlansAutoLocateStatuses(organizationId: str = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None, networkIds: list = None, floorPlanIds: list = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if perPage is not None:
        final_kwargs['perPage'] = perPage
    if startingAfter is not None:
        final_kwargs['startingAfter'] = startingAfter
    if endingBefore is not None:
        final_kwargs['endingBefore'] = endingBefore
    if networkIds is not None:
        final_kwargs['networkIds'] = networkIds
    if floorPlanIds is not None:
        final_kwargs['floorPlanIds'] = floorPlanIds

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'networkIds', 'floorPlanIds'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'networkIds', 'floorPlanIds'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'networkIds', 'floorPlanIds'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationFloorPlansAutoLocateStatuses

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationInsightApplications')
def getOrganizationInsightApplications(organizationId: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationInsightApplications

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationInsightMonitoredMediaServers')
def getOrganizationInsightMonitoredMediaServers(organizationId: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationInsightMonitoredMediaServers

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationInsightMonitoredMediaServer')
def getOrganizationInsightMonitoredMediaServer(monitoredMediaServerId: str, organizationId: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if monitoredMediaServerId is not None:
        final_kwargs['monitoredMediaServerId'] = monitoredMediaServerId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'monitoredMediaServerId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'monitoredMediaServerId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'monitoredMediaServerId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationInsightMonitoredMediaServer

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationInventoryDevices')
def getOrganizationInventoryDevices(organizationId: str = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None, usedState: str = None, search: str = None, macs: list = None, networkIds: list = None, serials: list = None, models: list = None, orderNumbers: list = None, tags: list = None, tagsFilterType: str = None, productTypes: list = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if perPage is not None:
        final_kwargs['perPage'] = perPage
    if startingAfter is not None:
        final_kwargs['startingAfter'] = startingAfter
    if endingBefore is not None:
        final_kwargs['endingBefore'] = endingBefore
    if usedState is not None:
        final_kwargs['usedState'] = usedState
    if search is not None:
        final_kwargs['search'] = search
    if macs is not None:
        final_kwargs['macs'] = macs
    if networkIds is not None:
        final_kwargs['networkIds'] = networkIds
    if serials is not None:
        final_kwargs['serials'] = serials
    if models is not None:
        final_kwargs['models'] = models
    if orderNumbers is not None:
        final_kwargs['orderNumbers'] = orderNumbers
    if tags is not None:
        final_kwargs['tags'] = tags
    if tagsFilterType is not None:
        final_kwargs['tagsFilterType'] = tagsFilterType
    if productTypes is not None:
        final_kwargs['productTypes'] = productTypes

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'usedState', 'search', 'macs', 'networkIds', 'serials', 'models', 'orderNumbers', 'tags', 'tagsFilterType', 'productTypes'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'usedState', 'search', 'macs', 'networkIds', 'serials', 'models', 'orderNumbers', 'tags', 'tagsFilterType', 'productTypes'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'usedState', 'search', 'macs', 'networkIds', 'serials', 'models', 'orderNumbers', 'tags', 'tagsFilterType', 'productTypes'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationInventoryDevices

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationInventoryDevicesSwapsBulk')
def getOrganizationInventoryDevicesSwapsBulk(id: str, organizationId: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if id is not None:
        final_kwargs['id'] = id

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'id'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'id'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'id'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationInventoryDevicesSwapsBulk

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationInventoryDevice')
def getOrganizationInventoryDevice(serial: str, organizationId: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if serial is not None:
        final_kwargs['serial'] = serial

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'serial'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'serial'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'serial'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationInventoryDevice

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationInventoryOnboardingCloudMonitoringImports')
def getOrganizationInventoryOnboardingCloudMonitoringImports(importIds: list, organizationId: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if importIds is not None:
        final_kwargs['importIds'] = importIds

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'importIds'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'importIds'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'importIds'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationInventoryOnboardingCloudMonitoringImports

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationInventoryOnboardingCloudMonitoringNetworks')
def getOrganizationInventoryOnboardingCloudMonitoringNetworks(deviceType: str, organizationId: str = None, search: str = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if deviceType is not None:
        final_kwargs['deviceType'] = deviceType
    if search is not None:
        final_kwargs['search'] = search
    if perPage is not None:
        final_kwargs['perPage'] = perPage
    if startingAfter is not None:
        final_kwargs['startingAfter'] = startingAfter
    if endingBefore is not None:
        final_kwargs['endingBefore'] = endingBefore

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'deviceType', 'search', 'perPage', 'startingAfter', 'endingBefore'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'deviceType', 'search', 'perPage', 'startingAfter', 'endingBefore'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'deviceType', 'search', 'perPage', 'startingAfter', 'endingBefore'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationInventoryOnboardingCloudMonitoringNetworks

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationLicenses')
def getOrganizationLicenses(organizationId: str = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None, deviceSerial: str = None, networkId: str = None, state: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if perPage is not None:
        final_kwargs['perPage'] = perPage
    if startingAfter is not None:
        final_kwargs['startingAfter'] = startingAfter
    if endingBefore is not None:
        final_kwargs['endingBefore'] = endingBefore
    if deviceSerial is not None:
        final_kwargs['deviceSerial'] = deviceSerial
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if state is not None:
        final_kwargs['state'] = state

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'deviceSerial', 'networkId', 'state'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'deviceSerial', 'networkId', 'state'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'deviceSerial', 'networkId', 'state'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationLicenses

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationLicensesOverview')
def getOrganizationLicensesOverview(organizationId: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationLicensesOverview

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationLicense')
def getOrganizationLicense(licenseId: str, organizationId: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if licenseId is not None:
        final_kwargs['licenseId'] = licenseId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'licenseId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'licenseId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'licenseId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationLicense

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationLicensingCotermLicenses')
def getOrganizationLicensingCotermLicenses(organizationId: str = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None, invalidated: bool = None, expired: bool = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if perPage is not None:
        final_kwargs['perPage'] = perPage
    if startingAfter is not None:
        final_kwargs['startingAfter'] = startingAfter
    if endingBefore is not None:
        final_kwargs['endingBefore'] = endingBefore
    if invalidated is not None:
        final_kwargs['invalidated'] = invalidated
    if expired is not None:
        final_kwargs['expired'] = expired

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'invalidated', 'expired'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'invalidated', 'expired'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'invalidated', 'expired'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationLicensingCotermLicenses

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationLoginSecurity')
def getOrganizationLoginSecurity(organizationId: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationLoginSecurity

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationNetworks')
def getOrganizationNetworks(organizationId: str = None, configTemplateId: str = None, isBoundToConfigTemplate: bool = None, tags: list = None, tagsFilterType: str = None, productTypes: list = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if configTemplateId is not None:
        final_kwargs['configTemplateId'] = configTemplateId
    if isBoundToConfigTemplate is not None:
        final_kwargs['isBoundToConfigTemplate'] = isBoundToConfigTemplate
    if tags is not None:
        final_kwargs['tags'] = tags
    if tagsFilterType is not None:
        final_kwargs['tagsFilterType'] = tagsFilterType
    if productTypes is not None:
        final_kwargs['productTypes'] = productTypes
    if perPage is not None:
        final_kwargs['perPage'] = perPage
    if startingAfter is not None:
        final_kwargs['startingAfter'] = startingAfter
    if endingBefore is not None:
        final_kwargs['endingBefore'] = endingBefore

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'configTemplateId', 'isBoundToConfigTemplate', 'tags', 'tagsFilterType', 'productTypes', 'perPage', 'startingAfter', 'endingBefore'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'configTemplateId', 'isBoundToConfigTemplate', 'tags', 'tagsFilterType', 'productTypes', 'perPage', 'startingAfter', 'endingBefore'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'configTemplateId', 'isBoundToConfigTemplate', 'tags', 'tagsFilterType', 'productTypes', 'perPage', 'startingAfter', 'endingBefore'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationNetworks

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationOpenapiSpec')
def getOrganizationOpenapiSpec(organizationId: str = None, version: int = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if version is not None:
        final_kwargs['version'] = version

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'version'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'version'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'version'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationOpenapiSpec

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationPolicyObjects')
def getOrganizationPolicyObjects(organizationId: str = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if perPage is not None:
        final_kwargs['perPage'] = perPage
    if startingAfter is not None:
        final_kwargs['startingAfter'] = startingAfter
    if endingBefore is not None:
        final_kwargs['endingBefore'] = endingBefore

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationPolicyObjects

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationPolicyObjectsGroups')
def getOrganizationPolicyObjectsGroups(organizationId: str = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if perPage is not None:
        final_kwargs['perPage'] = perPage
    if startingAfter is not None:
        final_kwargs['startingAfter'] = startingAfter
    if endingBefore is not None:
        final_kwargs['endingBefore'] = endingBefore

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationPolicyObjectsGroups

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationPolicyObjectsGroup')
def getOrganizationPolicyObjectsGroup(policyObjectGroupId: str, organizationId: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if policyObjectGroupId is not None:
        final_kwargs['policyObjectGroupId'] = policyObjectGroupId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'policyObjectGroupId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'policyObjectGroupId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'policyObjectGroupId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationPolicyObjectsGroup

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationPolicyObject')
def getOrganizationPolicyObject(policyObjectId: str, organizationId: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if policyObjectId is not None:
        final_kwargs['policyObjectId'] = policyObjectId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'policyObjectId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'policyObjectId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'policyObjectId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationPolicyObject

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSaml')
def getOrganizationSaml(organizationId: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationSaml

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSamlIdps')
def getOrganizationSamlIdps(organizationId: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationSamlIdps

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSamlIdp')
def getOrganizationSamlIdp(idpId: str, organizationId: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if idpId is not None:
        final_kwargs['idpId'] = idpId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'idpId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'idpId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'idpId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationSamlIdp

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSamlRoles')
def getOrganizationSamlRoles(organizationId: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationSamlRoles

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSamlRole')
def getOrganizationSamlRole(samlRoleId: str, organizationId: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if samlRoleId is not None:
        final_kwargs['samlRoleId'] = samlRoleId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'samlRoleId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'samlRoleId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'samlRoleId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationSamlRole

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSensorReadingsHistory')
def getOrganizationSensorReadingsHistory(organizationId: str = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None, t0: str = None, t1: str = None, timespan: float = None, networkIds: list = None, serials: list = None, metrics: list = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if perPage is not None:
        final_kwargs['perPage'] = perPage
    if startingAfter is not None:
        final_kwargs['startingAfter'] = startingAfter
    if endingBefore is not None:
        final_kwargs['endingBefore'] = endingBefore
    if t0 is not None:
        final_kwargs['t0'] = t0
    if t1 is not None:
        final_kwargs['t1'] = t1
    if timespan is not None:
        final_kwargs['timespan'] = timespan
    if networkIds is not None:
        final_kwargs['networkIds'] = networkIds
    if serials is not None:
        final_kwargs['serials'] = serials
    if metrics is not None:
        final_kwargs['metrics'] = metrics

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 't0', 't1', 'timespan', 'networkIds', 'serials', 'metrics'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 't0', 't1', 'timespan', 'networkIds', 'serials', 'metrics'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 't0', 't1', 'timespan', 'networkIds', 'serials', 'metrics'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationSensorReadingsHistory

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSensorReadingsLatest')
def getOrganizationSensorReadingsLatest(organizationId: str = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None, networkIds: list = None, serials: list = None, metrics: list = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if perPage is not None:
        final_kwargs['perPage'] = perPage
    if startingAfter is not None:
        final_kwargs['startingAfter'] = startingAfter
    if endingBefore is not None:
        final_kwargs['endingBefore'] = endingBefore
    if networkIds is not None:
        final_kwargs['networkIds'] = networkIds
    if serials is not None:
        final_kwargs['serials'] = serials
    if metrics is not None:
        final_kwargs['metrics'] = metrics

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'networkIds', 'serials', 'metrics'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'networkIds', 'serials', 'metrics'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'networkIds', 'serials', 'metrics'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationSensorReadingsLatest

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSmAdminsRoles')
def getOrganizationSmAdminsRoles(organizationId: str = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if perPage is not None:
        final_kwargs['perPage'] = perPage
    if startingAfter is not None:
        final_kwargs['startingAfter'] = startingAfter
    if endingBefore is not None:
        final_kwargs['endingBefore'] = endingBefore

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationSmAdminsRoles

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSmAdminsRole')
def getOrganizationSmAdminsRole(roleId: str, organizationId: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if roleId is not None:
        final_kwargs['roleId'] = roleId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'roleId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'roleId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'roleId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationSmAdminsRole

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSmApnsCert')
def getOrganizationSmApnsCert(organizationId: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationSmApnsCert

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSmSentryPoliciesAssignmentsByNetwork')
def getOrganizationSmSentryPoliciesAssignmentsByNetwork(organizationId: str = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None, networkIds: list = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if perPage is not None:
        final_kwargs['perPage'] = perPage
    if startingAfter is not None:
        final_kwargs['startingAfter'] = startingAfter
    if endingBefore is not None:
        final_kwargs['endingBefore'] = endingBefore
    if networkIds is not None:
        final_kwargs['networkIds'] = networkIds

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'networkIds'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'networkIds'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'networkIds'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationSmSentryPoliciesAssignmentsByNetwork

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSmVppAccounts')
def getOrganizationSmVppAccounts(organizationId: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationSmVppAccounts

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSmVppAccount')
def getOrganizationSmVppAccount(vppAccountId: str, organizationId: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if vppAccountId is not None:
        final_kwargs['vppAccountId'] = vppAccountId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'vppAccountId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'vppAccountId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'vppAccountId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationSmVppAccount

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSnmp')
def getOrganizationSnmp(organizationId: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationSnmp

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSplashAsset')
def getOrganizationSplashAsset(id: str, organizationId: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if id is not None:
        final_kwargs['id'] = id

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'id'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'id'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'id'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationSplashAsset

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSplashThemes')
def getOrganizationSplashThemes(organizationId: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationSplashThemes

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSummarySwitchPowerHistory')
def getOrganizationSummarySwitchPowerHistory(organizationId: str = None, t0: str = None, t1: str = None, timespan: float = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if t0 is not None:
        final_kwargs['t0'] = t0
    if t1 is not None:
        final_kwargs['t1'] = t1
    if timespan is not None:
        final_kwargs['timespan'] = timespan

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 't0', 't1', 'timespan'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 't0', 't1', 'timespan'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 't0', 't1', 'timespan'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationSummarySwitchPowerHistory

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSummaryTopAppliancesByUtilization')
def getOrganizationSummaryTopAppliancesByUtilization(organizationId: str = None, networkTag: str = None, deviceTag: str = None, quantity: int = None, ssidName: str = None, usageUplink: str = None, t0: str = None, t1: str = None, timespan: float = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if networkTag is not None:
        final_kwargs['networkTag'] = networkTag
    if deviceTag is not None:
        final_kwargs['deviceTag'] = deviceTag
    if quantity is not None:
        final_kwargs['quantity'] = quantity
    if ssidName is not None:
        final_kwargs['ssidName'] = ssidName
    if usageUplink is not None:
        final_kwargs['usageUplink'] = usageUplink
    if t0 is not None:
        final_kwargs['t0'] = t0
    if t1 is not None:
        final_kwargs['t1'] = t1
    if timespan is not None:
        final_kwargs['timespan'] = timespan

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'networkTag', 'deviceTag', 'quantity', 'ssidName', 'usageUplink', 't0', 't1', 'timespan'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'networkTag', 'deviceTag', 'quantity', 'ssidName', 'usageUplink', 't0', 't1', 'timespan'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'networkTag', 'deviceTag', 'quantity', 'ssidName', 'usageUplink', 't0', 't1', 'timespan'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationSummaryTopAppliancesByUtilization

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSummaryTopApplicationsByUsage')
def getOrganizationSummaryTopApplicationsByUsage(organizationId: str = None, networkTag: str = None, device: str = None, networkId: str = None, quantity: int = None, ssidName: str = None, usageUplink: str = None, t0: str = None, t1: str = None, timespan: float = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if networkTag is not None:
        final_kwargs['networkTag'] = networkTag
    if device is not None:
        final_kwargs['device'] = device
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if quantity is not None:
        final_kwargs['quantity'] = quantity
    if ssidName is not None:
        final_kwargs['ssidName'] = ssidName
    if usageUplink is not None:
        final_kwargs['usageUplink'] = usageUplink
    if t0 is not None:
        final_kwargs['t0'] = t0
    if t1 is not None:
        final_kwargs['t1'] = t1
    if timespan is not None:
        final_kwargs['timespan'] = timespan

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'networkTag', 'device', 'networkId', 'quantity', 'ssidName', 'usageUplink', 't0', 't1', 'timespan'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'networkTag', 'device', 'networkId', 'quantity', 'ssidName', 'usageUplink', 't0', 't1', 'timespan'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'networkTag', 'device', 'networkId', 'quantity', 'ssidName', 'usageUplink', 't0', 't1', 'timespan'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationSummaryTopApplicationsByUsage

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSummaryTopApplicationsCategoriesByUsage')
def getOrganizationSummaryTopApplicationsCategoriesByUsage(organizationId: str = None, networkTag: str = None, deviceTag: str = None, networkId: str = None, quantity: int = None, ssidName: str = None, usageUplink: str = None, t0: str = None, t1: str = None, timespan: float = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if networkTag is not None:
        final_kwargs['networkTag'] = networkTag
    if deviceTag is not None:
        final_kwargs['deviceTag'] = deviceTag
    if networkId is not None:
        final_kwargs['networkId'] = networkId
    if quantity is not None:
        final_kwargs['quantity'] = quantity
    if ssidName is not None:
        final_kwargs['ssidName'] = ssidName
    if usageUplink is not None:
        final_kwargs['usageUplink'] = usageUplink
    if t0 is not None:
        final_kwargs['t0'] = t0
    if t1 is not None:
        final_kwargs['t1'] = t1
    if timespan is not None:
        final_kwargs['timespan'] = timespan

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'networkTag', 'deviceTag', 'networkId', 'quantity', 'ssidName', 'usageUplink', 't0', 't1', 'timespan'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'networkTag', 'deviceTag', 'networkId', 'quantity', 'ssidName', 'usageUplink', 't0', 't1', 'timespan'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'networkTag', 'deviceTag', 'networkId', 'quantity', 'ssidName', 'usageUplink', 't0', 't1', 'timespan'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationSummaryTopApplicationsCategoriesByUsage

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSummaryTopClientsByUsage')
def getOrganizationSummaryTopClientsByUsage(organizationId: str = None, networkTag: str = None, deviceTag: str = None, quantity: int = None, ssidName: str = None, usageUplink: str = None, t0: str = None, t1: str = None, timespan: float = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if networkTag is not None:
        final_kwargs['networkTag'] = networkTag
    if deviceTag is not None:
        final_kwargs['deviceTag'] = deviceTag
    if quantity is not None:
        final_kwargs['quantity'] = quantity
    if ssidName is not None:
        final_kwargs['ssidName'] = ssidName
    if usageUplink is not None:
        final_kwargs['usageUplink'] = usageUplink
    if t0 is not None:
        final_kwargs['t0'] = t0
    if t1 is not None:
        final_kwargs['t1'] = t1
    if timespan is not None:
        final_kwargs['timespan'] = timespan

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'networkTag', 'deviceTag', 'quantity', 'ssidName', 'usageUplink', 't0', 't1', 'timespan'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'networkTag', 'deviceTag', 'quantity', 'ssidName', 'usageUplink', 't0', 't1', 'timespan'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'networkTag', 'deviceTag', 'quantity', 'ssidName', 'usageUplink', 't0', 't1', 'timespan'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationSummaryTopClientsByUsage

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSummaryTopClientsManufacturersByUsage')
def getOrganizationSummaryTopClientsManufacturersByUsage(organizationId: str = None, networkTag: str = None, deviceTag: str = None, quantity: int = None, ssidName: str = None, usageUplink: str = None, t0: str = None, t1: str = None, timespan: float = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if networkTag is not None:
        final_kwargs['networkTag'] = networkTag
    if deviceTag is not None:
        final_kwargs['deviceTag'] = deviceTag
    if quantity is not None:
        final_kwargs['quantity'] = quantity
    if ssidName is not None:
        final_kwargs['ssidName'] = ssidName
    if usageUplink is not None:
        final_kwargs['usageUplink'] = usageUplink
    if t0 is not None:
        final_kwargs['t0'] = t0
    if t1 is not None:
        final_kwargs['t1'] = t1
    if timespan is not None:
        final_kwargs['timespan'] = timespan

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'networkTag', 'deviceTag', 'quantity', 'ssidName', 'usageUplink', 't0', 't1', 'timespan'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'networkTag', 'deviceTag', 'quantity', 'ssidName', 'usageUplink', 't0', 't1', 'timespan'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'networkTag', 'deviceTag', 'quantity', 'ssidName', 'usageUplink', 't0', 't1', 'timespan'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationSummaryTopClientsManufacturersByUsage

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSummaryTopDevicesByUsage')
def getOrganizationSummaryTopDevicesByUsage(organizationId: str = None, networkTag: str = None, deviceTag: str = None, quantity: int = None, ssidName: str = None, usageUplink: str = None, t0: str = None, t1: str = None, timespan: float = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if networkTag is not None:
        final_kwargs['networkTag'] = networkTag
    if deviceTag is not None:
        final_kwargs['deviceTag'] = deviceTag
    if quantity is not None:
        final_kwargs['quantity'] = quantity
    if ssidName is not None:
        final_kwargs['ssidName'] = ssidName
    if usageUplink is not None:
        final_kwargs['usageUplink'] = usageUplink
    if t0 is not None:
        final_kwargs['t0'] = t0
    if t1 is not None:
        final_kwargs['t1'] = t1
    if timespan is not None:
        final_kwargs['timespan'] = timespan

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'networkTag', 'deviceTag', 'quantity', 'ssidName', 'usageUplink', 't0', 't1', 'timespan'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'networkTag', 'deviceTag', 'quantity', 'ssidName', 'usageUplink', 't0', 't1', 'timespan'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'networkTag', 'deviceTag', 'quantity', 'ssidName', 'usageUplink', 't0', 't1', 'timespan'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationSummaryTopDevicesByUsage

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSummaryTopDevicesModelsByUsage')
def getOrganizationSummaryTopDevicesModelsByUsage(organizationId: str = None, networkTag: str = None, deviceTag: str = None, quantity: int = None, ssidName: str = None, usageUplink: str = None, t0: str = None, t1: str = None, timespan: float = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if networkTag is not None:
        final_kwargs['networkTag'] = networkTag
    if deviceTag is not None:
        final_kwargs['deviceTag'] = deviceTag
    if quantity is not None:
        final_kwargs['quantity'] = quantity
    if ssidName is not None:
        final_kwargs['ssidName'] = ssidName
    if usageUplink is not None:
        final_kwargs['usageUplink'] = usageUplink
    if t0 is not None:
        final_kwargs['t0'] = t0
    if t1 is not None:
        final_kwargs['t1'] = t1
    if timespan is not None:
        final_kwargs['timespan'] = timespan

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'networkTag', 'deviceTag', 'quantity', 'ssidName', 'usageUplink', 't0', 't1', 'timespan'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'networkTag', 'deviceTag', 'quantity', 'ssidName', 'usageUplink', 't0', 't1', 'timespan'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'networkTag', 'deviceTag', 'quantity', 'ssidName', 'usageUplink', 't0', 't1', 'timespan'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationSummaryTopDevicesModelsByUsage

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSummaryTopNetworksByStatus')
def getOrganizationSummaryTopNetworksByStatus(organizationId: str = None, networkTag: str = None, deviceTag: str = None, quantity: int = None, ssidName: str = None, usageUplink: str = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if networkTag is not None:
        final_kwargs['networkTag'] = networkTag
    if deviceTag is not None:
        final_kwargs['deviceTag'] = deviceTag
    if quantity is not None:
        final_kwargs['quantity'] = quantity
    if ssidName is not None:
        final_kwargs['ssidName'] = ssidName
    if usageUplink is not None:
        final_kwargs['usageUplink'] = usageUplink
    if perPage is not None:
        final_kwargs['perPage'] = perPage
    if startingAfter is not None:
        final_kwargs['startingAfter'] = startingAfter
    if endingBefore is not None:
        final_kwargs['endingBefore'] = endingBefore

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'networkTag', 'deviceTag', 'quantity', 'ssidName', 'usageUplink', 'perPage', 'startingAfter', 'endingBefore'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'networkTag', 'deviceTag', 'quantity', 'ssidName', 'usageUplink', 'perPage', 'startingAfter', 'endingBefore'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'networkTag', 'deviceTag', 'quantity', 'ssidName', 'usageUplink', 'perPage', 'startingAfter', 'endingBefore'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationSummaryTopNetworksByStatus

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSummaryTopSsidsByUsage')
def getOrganizationSummaryTopSsidsByUsage(organizationId: str = None, networkTag: str = None, deviceTag: str = None, quantity: int = None, ssidName: str = None, usageUplink: str = None, t0: str = None, t1: str = None, timespan: float = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if networkTag is not None:
        final_kwargs['networkTag'] = networkTag
    if deviceTag is not None:
        final_kwargs['deviceTag'] = deviceTag
    if quantity is not None:
        final_kwargs['quantity'] = quantity
    if ssidName is not None:
        final_kwargs['ssidName'] = ssidName
    if usageUplink is not None:
        final_kwargs['usageUplink'] = usageUplink
    if t0 is not None:
        final_kwargs['t0'] = t0
    if t1 is not None:
        final_kwargs['t1'] = t1
    if timespan is not None:
        final_kwargs['timespan'] = timespan

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'networkTag', 'deviceTag', 'quantity', 'ssidName', 'usageUplink', 't0', 't1', 'timespan'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'networkTag', 'deviceTag', 'quantity', 'ssidName', 'usageUplink', 't0', 't1', 'timespan'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'networkTag', 'deviceTag', 'quantity', 'ssidName', 'usageUplink', 't0', 't1', 'timespan'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationSummaryTopSsidsByUsage

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSummaryTopSwitchesByEnergyUsage')
def getOrganizationSummaryTopSwitchesByEnergyUsage(organizationId: str = None, networkTag: str = None, deviceTag: str = None, quantity: int = None, ssidName: str = None, usageUplink: str = None, t0: str = None, t1: str = None, timespan: float = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if networkTag is not None:
        final_kwargs['networkTag'] = networkTag
    if deviceTag is not None:
        final_kwargs['deviceTag'] = deviceTag
    if quantity is not None:
        final_kwargs['quantity'] = quantity
    if ssidName is not None:
        final_kwargs['ssidName'] = ssidName
    if usageUplink is not None:
        final_kwargs['usageUplink'] = usageUplink
    if t0 is not None:
        final_kwargs['t0'] = t0
    if t1 is not None:
        final_kwargs['t1'] = t1
    if timespan is not None:
        final_kwargs['timespan'] = timespan

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'networkTag', 'deviceTag', 'quantity', 'ssidName', 'usageUplink', 't0', 't1', 'timespan'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'networkTag', 'deviceTag', 'quantity', 'ssidName', 'usageUplink', 't0', 't1', 'timespan'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'networkTag', 'deviceTag', 'quantity', 'ssidName', 'usageUplink', 't0', 't1', 'timespan'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationSummaryTopSwitchesByEnergyUsage

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSwitchPortsBySwitch')
def getOrganizationSwitchPortsBySwitch(organizationId: str = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None, configurationUpdatedAfter: str = None, mac: str = None, macs: list = None, name: str = None, networkIds: list = None, portProfileIds: list = None, serial: str = None, serials: list = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if perPage is not None:
        final_kwargs['perPage'] = perPage
    if startingAfter is not None:
        final_kwargs['startingAfter'] = startingAfter
    if endingBefore is not None:
        final_kwargs['endingBefore'] = endingBefore
    if configurationUpdatedAfter is not None:
        final_kwargs['configurationUpdatedAfter'] = configurationUpdatedAfter
    if mac is not None:
        final_kwargs['mac'] = mac
    if macs is not None:
        final_kwargs['macs'] = macs
    if name is not None:
        final_kwargs['name'] = name
    if networkIds is not None:
        final_kwargs['networkIds'] = networkIds
    if portProfileIds is not None:
        final_kwargs['portProfileIds'] = portProfileIds
    if serial is not None:
        final_kwargs['serial'] = serial
    if serials is not None:
        final_kwargs['serials'] = serials

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'configurationUpdatedAfter', 'mac', 'macs', 'name', 'networkIds', 'portProfileIds', 'serial', 'serials'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'configurationUpdatedAfter', 'mac', 'macs', 'name', 'networkIds', 'portProfileIds', 'serial', 'serials'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'configurationUpdatedAfter', 'mac', 'macs', 'name', 'networkIds', 'portProfileIds', 'serial', 'serials'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationSwitchPortsBySwitch

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSwitchPortsClientsOverviewByDevice')
def getOrganizationSwitchPortsClientsOverviewByDevice(organizationId: str = None, t0: str = None, timespan: float = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None, configurationUpdatedAfter: str = None, mac: str = None, macs: list = None, name: str = None, networkIds: list = None, portProfileIds: list = None, serial: str = None, serials: list = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if t0 is not None:
        final_kwargs['t0'] = t0
    if timespan is not None:
        final_kwargs['timespan'] = timespan
    if perPage is not None:
        final_kwargs['perPage'] = perPage
    if startingAfter is not None:
        final_kwargs['startingAfter'] = startingAfter
    if endingBefore is not None:
        final_kwargs['endingBefore'] = endingBefore
    if configurationUpdatedAfter is not None:
        final_kwargs['configurationUpdatedAfter'] = configurationUpdatedAfter
    if mac is not None:
        final_kwargs['mac'] = mac
    if macs is not None:
        final_kwargs['macs'] = macs
    if name is not None:
        final_kwargs['name'] = name
    if networkIds is not None:
        final_kwargs['networkIds'] = networkIds
    if portProfileIds is not None:
        final_kwargs['portProfileIds'] = portProfileIds
    if serial is not None:
        final_kwargs['serial'] = serial
    if serials is not None:
        final_kwargs['serials'] = serials

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 't0', 'timespan', 'perPage', 'startingAfter', 'endingBefore', 'configurationUpdatedAfter', 'mac', 'macs', 'name', 'networkIds', 'portProfileIds', 'serial', 'serials'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 't0', 'timespan', 'perPage', 'startingAfter', 'endingBefore', 'configurationUpdatedAfter', 'mac', 'macs', 'name', 'networkIds', 'portProfileIds', 'serial', 'serials'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 't0', 'timespan', 'perPage', 'startingAfter', 'endingBefore', 'configurationUpdatedAfter', 'mac', 'macs', 'name', 'networkIds', 'portProfileIds', 'serial', 'serials'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationSwitchPortsClientsOverviewByDevice

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSwitchPortsOverview')
def getOrganizationSwitchPortsOverview(organizationId: str = None, t0: str = None, t1: str = None, timespan: float = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if t0 is not None:
        final_kwargs['t0'] = t0
    if t1 is not None:
        final_kwargs['t1'] = t1
    if timespan is not None:
        final_kwargs['timespan'] = timespan

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 't0', 't1', 'timespan'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 't0', 't1', 'timespan'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 't0', 't1', 'timespan'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationSwitchPortsOverview

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSwitchPortsStatusesBySwitch')
def getOrganizationSwitchPortsStatusesBySwitch(organizationId: str = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None, configurationUpdatedAfter: str = None, mac: str = None, macs: list = None, name: str = None, networkIds: list = None, portProfileIds: list = None, serial: str = None, serials: list = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if perPage is not None:
        final_kwargs['perPage'] = perPage
    if startingAfter is not None:
        final_kwargs['startingAfter'] = startingAfter
    if endingBefore is not None:
        final_kwargs['endingBefore'] = endingBefore
    if configurationUpdatedAfter is not None:
        final_kwargs['configurationUpdatedAfter'] = configurationUpdatedAfter
    if mac is not None:
        final_kwargs['mac'] = mac
    if macs is not None:
        final_kwargs['macs'] = macs
    if name is not None:
        final_kwargs['name'] = name
    if networkIds is not None:
        final_kwargs['networkIds'] = networkIds
    if portProfileIds is not None:
        final_kwargs['portProfileIds'] = portProfileIds
    if serial is not None:
        final_kwargs['serial'] = serial
    if serials is not None:
        final_kwargs['serials'] = serials

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'configurationUpdatedAfter', 'mac', 'macs', 'name', 'networkIds', 'portProfileIds', 'serial', 'serials'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'configurationUpdatedAfter', 'mac', 'macs', 'name', 'networkIds', 'portProfileIds', 'serial', 'serials'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'configurationUpdatedAfter', 'mac', 'macs', 'name', 'networkIds', 'portProfileIds', 'serial', 'serials'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationSwitchPortsStatusesBySwitch

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSwitchPortsTopologyDiscoveryByDevice')
def getOrganizationSwitchPortsTopologyDiscoveryByDevice(organizationId: str = None, t0: str = None, timespan: float = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None, configurationUpdatedAfter: str = None, mac: str = None, macs: list = None, name: str = None, networkIds: list = None, portProfileIds: list = None, serial: str = None, serials: list = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if t0 is not None:
        final_kwargs['t0'] = t0
    if timespan is not None:
        final_kwargs['timespan'] = timespan
    if perPage is not None:
        final_kwargs['perPage'] = perPage
    if startingAfter is not None:
        final_kwargs['startingAfter'] = startingAfter
    if endingBefore is not None:
        final_kwargs['endingBefore'] = endingBefore
    if configurationUpdatedAfter is not None:
        final_kwargs['configurationUpdatedAfter'] = configurationUpdatedAfter
    if mac is not None:
        final_kwargs['mac'] = mac
    if macs is not None:
        final_kwargs['macs'] = macs
    if name is not None:
        final_kwargs['name'] = name
    if networkIds is not None:
        final_kwargs['networkIds'] = networkIds
    if portProfileIds is not None:
        final_kwargs['portProfileIds'] = portProfileIds
    if serial is not None:
        final_kwargs['serial'] = serial
    if serials is not None:
        final_kwargs['serials'] = serials

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 't0', 'timespan', 'perPage', 'startingAfter', 'endingBefore', 'configurationUpdatedAfter', 'mac', 'macs', 'name', 'networkIds', 'portProfileIds', 'serial', 'serials'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 't0', 'timespan', 'perPage', 'startingAfter', 'endingBefore', 'configurationUpdatedAfter', 'mac', 'macs', 'name', 'networkIds', 'portProfileIds', 'serial', 'serials'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 't0', 'timespan', 'perPage', 'startingAfter', 'endingBefore', 'configurationUpdatedAfter', 'mac', 'macs', 'name', 'networkIds', 'portProfileIds', 'serial', 'serials'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationSwitchPortsTopologyDiscoveryByDevice

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationUplinksStatuses')
def getOrganizationUplinksStatuses(organizationId: str = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None, networkIds: list = None, serials: list = None, iccids: list = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if perPage is not None:
        final_kwargs['perPage'] = perPage
    if startingAfter is not None:
        final_kwargs['startingAfter'] = startingAfter
    if endingBefore is not None:
        final_kwargs['endingBefore'] = endingBefore
    if networkIds is not None:
        final_kwargs['networkIds'] = networkIds
    if serials is not None:
        final_kwargs['serials'] = serials
    if iccids is not None:
        final_kwargs['iccids'] = iccids

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'networkIds', 'serials', 'iccids'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'networkIds', 'serials', 'iccids'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'networkIds', 'serials', 'iccids'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationUplinksStatuses

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationWebhooksAlertTypes')
def getOrganizationWebhooksAlertTypes(organizationId: str = None, productType: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if productType is not None:
        final_kwargs['productType'] = productType

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'productType'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'productType'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'productType'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationWebhooksAlertTypes

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationWebhooksCallbacksStatus')
def getOrganizationWebhooksCallbacksStatus(callbackId: str, organizationId: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if callbackId is not None:
        final_kwargs['callbackId'] = callbackId

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'callbackId'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'callbackId'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'callbackId'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationWebhooksCallbacksStatus

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationWebhooksLogs')
def getOrganizationWebhooksLogs(organizationId: str = None, t0: str = None, t1: str = None, timespan: float = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None, url: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if t0 is not None:
        final_kwargs['t0'] = t0
    if t1 is not None:
        final_kwargs['t1'] = t1
    if timespan is not None:
        final_kwargs['timespan'] = timespan
    if perPage is not None:
        final_kwargs['perPage'] = perPage
    if startingAfter is not None:
        final_kwargs['startingAfter'] = startingAfter
    if endingBefore is not None:
        final_kwargs['endingBefore'] = endingBefore
    if url is not None:
        final_kwargs['url'] = url

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 't0', 't1', 'timespan', 'perPage', 'startingAfter', 'endingBefore', 'url'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 't0', 't1', 'timespan', 'perPage', 'startingAfter', 'endingBefore', 'url'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 't0', 't1', 'timespan', 'perPage', 'startingAfter', 'endingBefore', 'url'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationWebhooksLogs

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationWirelessAirMarshalRules')
def getOrganizationWirelessAirMarshalRules(organizationId: str = None, networkIds: list = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if networkIds is not None:
        final_kwargs['networkIds'] = networkIds
    if perPage is not None:
        final_kwargs['perPage'] = perPage
    if startingAfter is not None:
        final_kwargs['startingAfter'] = startingAfter
    if endingBefore is not None:
        final_kwargs['endingBefore'] = endingBefore

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'networkIds', 'perPage', 'startingAfter', 'endingBefore'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'networkIds', 'perPage', 'startingAfter', 'endingBefore'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'networkIds', 'perPage', 'startingAfter', 'endingBefore'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationWirelessAirMarshalRules

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationWirelessAirMarshalSettingsByNetwork')
def getOrganizationWirelessAirMarshalSettingsByNetwork(organizationId: str = None, networkIds: list = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if networkIds is not None:
        final_kwargs['networkIds'] = networkIds
    if perPage is not None:
        final_kwargs['perPage'] = perPage
    if startingAfter is not None:
        final_kwargs['startingAfter'] = startingAfter
    if endingBefore is not None:
        final_kwargs['endingBefore'] = endingBefore

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'networkIds', 'perPage', 'startingAfter', 'endingBefore'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'networkIds', 'perPage', 'startingAfter', 'endingBefore'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'networkIds', 'perPage', 'startingAfter', 'endingBefore'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationWirelessAirMarshalSettingsByNetwork

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationWirelessClientsOverviewByDevice')
def getOrganizationWirelessClientsOverviewByDevice(organizationId: str = None, networkIds: list = None, serials: list = None, campusGatewayClusterIds: list = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if networkIds is not None:
        final_kwargs['networkIds'] = networkIds
    if serials is not None:
        final_kwargs['serials'] = serials
    if campusGatewayClusterIds is not None:
        final_kwargs['campusGatewayClusterIds'] = campusGatewayClusterIds
    if perPage is not None:
        final_kwargs['perPage'] = perPage
    if startingAfter is not None:
        final_kwargs['startingAfter'] = startingAfter
    if endingBefore is not None:
        final_kwargs['endingBefore'] = endingBefore

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'networkIds', 'serials', 'campusGatewayClusterIds', 'perPage', 'startingAfter', 'endingBefore'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'networkIds', 'serials', 'campusGatewayClusterIds', 'perPage', 'startingAfter', 'endingBefore'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'networkIds', 'serials', 'campusGatewayClusterIds', 'perPage', 'startingAfter', 'endingBefore'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationWirelessClientsOverviewByDevice

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationWirelessDevicesChannelUtilizationByDevice')
def getOrganizationWirelessDevicesChannelUtilizationByDevice(organizationId: str = None, networkIds: list = None, serials: list = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None, t0: str = None, t1: str = None, timespan: float = None, interval: int = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if networkIds is not None:
        final_kwargs['networkIds'] = networkIds
    if serials is not None:
        final_kwargs['serials'] = serials
    if perPage is not None:
        final_kwargs['perPage'] = perPage
    if startingAfter is not None:
        final_kwargs['startingAfter'] = startingAfter
    if endingBefore is not None:
        final_kwargs['endingBefore'] = endingBefore
    if t0 is not None:
        final_kwargs['t0'] = t0
    if t1 is not None:
        final_kwargs['t1'] = t1
    if timespan is not None:
        final_kwargs['timespan'] = timespan
    if interval is not None:
        final_kwargs['interval'] = interval

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'networkIds', 'serials', 'perPage', 'startingAfter', 'endingBefore', 't0', 't1', 'timespan', 'interval'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'networkIds', 'serials', 'perPage', 'startingAfter', 'endingBefore', 't0', 't1', 'timespan', 'interval'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'networkIds', 'serials', 'perPage', 'startingAfter', 'endingBefore', 't0', 't1', 'timespan', 'interval'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationWirelessDevicesChannelUtilizationByDevice

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationWirelessDevicesChannelUtilizationByNetwork')
def getOrganizationWirelessDevicesChannelUtilizationByNetwork(organizationId: str = None, networkIds: list = None, serials: list = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None, t0: str = None, t1: str = None, timespan: float = None, interval: int = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if networkIds is not None:
        final_kwargs['networkIds'] = networkIds
    if serials is not None:
        final_kwargs['serials'] = serials
    if perPage is not None:
        final_kwargs['perPage'] = perPage
    if startingAfter is not None:
        final_kwargs['startingAfter'] = startingAfter
    if endingBefore is not None:
        final_kwargs['endingBefore'] = endingBefore
    if t0 is not None:
        final_kwargs['t0'] = t0
    if t1 is not None:
        final_kwargs['t1'] = t1
    if timespan is not None:
        final_kwargs['timespan'] = timespan
    if interval is not None:
        final_kwargs['interval'] = interval

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'networkIds', 'serials', 'perPage', 'startingAfter', 'endingBefore', 't0', 't1', 'timespan', 'interval'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'networkIds', 'serials', 'perPage', 'startingAfter', 'endingBefore', 't0', 't1', 'timespan', 'interval'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'networkIds', 'serials', 'perPage', 'startingAfter', 'endingBefore', 't0', 't1', 'timespan', 'interval'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationWirelessDevicesChannelUtilizationByNetwork

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationWirelessDevicesChannelUtilizationHistoryByDeviceB')
def getOrganizationWirelessDevicesChannelUtilizationHistoryByDeviceB(organizationId: str = None, networkIds: list = None, serials: list = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None, t0: str = None, t1: str = None, timespan: float = None, interval: int = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if networkIds is not None:
        final_kwargs['networkIds'] = networkIds
    if serials is not None:
        final_kwargs['serials'] = serials
    if perPage is not None:
        final_kwargs['perPage'] = perPage
    if startingAfter is not None:
        final_kwargs['startingAfter'] = startingAfter
    if endingBefore is not None:
        final_kwargs['endingBefore'] = endingBefore
    if t0 is not None:
        final_kwargs['t0'] = t0
    if t1 is not None:
        final_kwargs['t1'] = t1
    if timespan is not None:
        final_kwargs['timespan'] = timespan
    if interval is not None:
        final_kwargs['interval'] = interval

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'networkIds', 'serials', 'perPage', 'startingAfter', 'endingBefore', 't0', 't1', 'timespan', 'interval'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'networkIds', 'serials', 'perPage', 'startingAfter', 'endingBefore', 't0', 't1', 'timespan', 'interval'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'networkIds', 'serials', 'perPage', 'startingAfter', 'endingBefore', 't0', 't1', 'timespan', 'interval'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationWirelessDevicesChannelUtilizationHistoryByDeviceB

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationWirelessDevicesChannelUtilizationHistoryByNetwork')
def getOrganizationWirelessDevicesChannelUtilizationHistoryByNetwork(organizationId: str = None, networkIds: list = None, serials: list = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None, t0: str = None, t1: str = None, timespan: float = None, interval: int = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if networkIds is not None:
        final_kwargs['networkIds'] = networkIds
    if serials is not None:
        final_kwargs['serials'] = serials
    if perPage is not None:
        final_kwargs['perPage'] = perPage
    if startingAfter is not None:
        final_kwargs['startingAfter'] = startingAfter
    if endingBefore is not None:
        final_kwargs['endingBefore'] = endingBefore
    if t0 is not None:
        final_kwargs['t0'] = t0
    if t1 is not None:
        final_kwargs['t1'] = t1
    if timespan is not None:
        final_kwargs['timespan'] = timespan
    if interval is not None:
        final_kwargs['interval'] = interval

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'networkIds', 'serials', 'perPage', 'startingAfter', 'endingBefore', 't0', 't1', 'timespan', 'interval'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'networkIds', 'serials', 'perPage', 'startingAfter', 'endingBefore', 't0', 't1', 'timespan', 'interval'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'networkIds', 'serials', 'perPage', 'startingAfter', 'endingBefore', 't0', 't1', 'timespan', 'interval'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationWirelessDevicesChannelUtilizationHistoryByNetwork

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationWirelessDevicesEthernetStatuses')
def getOrganizationWirelessDevicesEthernetStatuses(organizationId: str = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None, networkIds: list = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if perPage is not None:
        final_kwargs['perPage'] = perPage
    if startingAfter is not None:
        final_kwargs['startingAfter'] = startingAfter
    if endingBefore is not None:
        final_kwargs['endingBefore'] = endingBefore
    if networkIds is not None:
        final_kwargs['networkIds'] = networkIds

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'networkIds'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'networkIds'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'networkIds'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationWirelessDevicesEthernetStatuses

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationWirelessDevicesPacketLossByClient')
def getOrganizationWirelessDevicesPacketLossByClient(organizationId: str = None, networkIds: list = None, ssids: list = None, bands: list = None, macs: list = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None, t0: str = None, t1: str = None, timespan: float = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if networkIds is not None:
        final_kwargs['networkIds'] = networkIds
    if ssids is not None:
        final_kwargs['ssids'] = ssids
    if bands is not None:
        final_kwargs['bands'] = bands
    if macs is not None:
        final_kwargs['macs'] = macs
    if perPage is not None:
        final_kwargs['perPage'] = perPage
    if startingAfter is not None:
        final_kwargs['startingAfter'] = startingAfter
    if endingBefore is not None:
        final_kwargs['endingBefore'] = endingBefore
    if t0 is not None:
        final_kwargs['t0'] = t0
    if t1 is not None:
        final_kwargs['t1'] = t1
    if timespan is not None:
        final_kwargs['timespan'] = timespan

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'networkIds', 'ssids', 'bands', 'macs', 'perPage', 'startingAfter', 'endingBefore', 't0', 't1', 'timespan'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'networkIds', 'ssids', 'bands', 'macs', 'perPage', 'startingAfter', 'endingBefore', 't0', 't1', 'timespan'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'networkIds', 'ssids', 'bands', 'macs', 'perPage', 'startingAfter', 'endingBefore', 't0', 't1', 'timespan'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationWirelessDevicesPacketLossByClient

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationWirelessDevicesPacketLossByDevice')
def getOrganizationWirelessDevicesPacketLossByDevice(organizationId: str = None, networkIds: list = None, serials: list = None, ssids: list = None, bands: list = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None, t0: str = None, t1: str = None, timespan: float = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if networkIds is not None:
        final_kwargs['networkIds'] = networkIds
    if serials is not None:
        final_kwargs['serials'] = serials
    if ssids is not None:
        final_kwargs['ssids'] = ssids
    if bands is not None:
        final_kwargs['bands'] = bands
    if perPage is not None:
        final_kwargs['perPage'] = perPage
    if startingAfter is not None:
        final_kwargs['startingAfter'] = startingAfter
    if endingBefore is not None:
        final_kwargs['endingBefore'] = endingBefore
    if t0 is not None:
        final_kwargs['t0'] = t0
    if t1 is not None:
        final_kwargs['t1'] = t1
    if timespan is not None:
        final_kwargs['timespan'] = timespan

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'networkIds', 'serials', 'ssids', 'bands', 'perPage', 'startingAfter', 'endingBefore', 't0', 't1', 'timespan'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'networkIds', 'serials', 'ssids', 'bands', 'perPage', 'startingAfter', 'endingBefore', 't0', 't1', 'timespan'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'networkIds', 'serials', 'ssids', 'bands', 'perPage', 'startingAfter', 'endingBefore', 't0', 't1', 'timespan'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationWirelessDevicesPacketLossByDevice

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationWirelessDevicesPacketLossByNetwork')
def getOrganizationWirelessDevicesPacketLossByNetwork(organizationId: str = None, networkIds: list = None, serials: list = None, ssids: list = None, bands: list = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None, t0: str = None, t1: str = None, timespan: float = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if networkIds is not None:
        final_kwargs['networkIds'] = networkIds
    if serials is not None:
        final_kwargs['serials'] = serials
    if ssids is not None:
        final_kwargs['ssids'] = ssids
    if bands is not None:
        final_kwargs['bands'] = bands
    if perPage is not None:
        final_kwargs['perPage'] = perPage
    if startingAfter is not None:
        final_kwargs['startingAfter'] = startingAfter
    if endingBefore is not None:
        final_kwargs['endingBefore'] = endingBefore
    if t0 is not None:
        final_kwargs['t0'] = t0
    if t1 is not None:
        final_kwargs['t1'] = t1
    if timespan is not None:
        final_kwargs['timespan'] = timespan

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'networkIds', 'serials', 'ssids', 'bands', 'perPage', 'startingAfter', 'endingBefore', 't0', 't1', 'timespan'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'networkIds', 'serials', 'ssids', 'bands', 'perPage', 'startingAfter', 'endingBefore', 't0', 't1', 'timespan'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'networkIds', 'serials', 'ssids', 'bands', 'perPage', 'startingAfter', 'endingBefore', 't0', 't1', 'timespan'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationWirelessDevicesPacketLossByNetwork

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationWirelessDevicesWirelessControllersByDevice')
def getOrganizationWirelessDevicesWirelessControllersByDevice(organizationId: str = None, networkIds: list = None, serials: list = None, controllerSerials: list = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if networkIds is not None:
        final_kwargs['networkIds'] = networkIds
    if serials is not None:
        final_kwargs['serials'] = serials
    if controllerSerials is not None:
        final_kwargs['controllerSerials'] = controllerSerials
    if perPage is not None:
        final_kwargs['perPage'] = perPage
    if startingAfter is not None:
        final_kwargs['startingAfter'] = startingAfter
    if endingBefore is not None:
        final_kwargs['endingBefore'] = endingBefore

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'networkIds', 'serials', 'controllerSerials', 'perPage', 'startingAfter', 'endingBefore'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'networkIds', 'serials', 'controllerSerials', 'perPage', 'startingAfter', 'endingBefore'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'networkIds', 'serials', 'controllerSerials', 'perPage', 'startingAfter', 'endingBefore'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationWirelessDevicesWirelessControllersByDevice

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationWirelessRfProfilesAssignmentsByDevice')
def getOrganizationWirelessRfProfilesAssignmentsByDevice(organizationId: str = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None, networkIds: list = None, productTypes: list = None, name: str = None, mac: str = None, serial: str = None, model: str = None, macs: list = None, serials: list = None, models: list = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if perPage is not None:
        final_kwargs['perPage'] = perPage
    if startingAfter is not None:
        final_kwargs['startingAfter'] = startingAfter
    if endingBefore is not None:
        final_kwargs['endingBefore'] = endingBefore
    if networkIds is not None:
        final_kwargs['networkIds'] = networkIds
    if productTypes is not None:
        final_kwargs['productTypes'] = productTypes
    if name is not None:
        final_kwargs['name'] = name
    if mac is not None:
        final_kwargs['mac'] = mac
    if serial is not None:
        final_kwargs['serial'] = serial
    if model is not None:
        final_kwargs['model'] = model
    if macs is not None:
        final_kwargs['macs'] = macs
    if serials is not None:
        final_kwargs['serials'] = serials
    if models is not None:
        final_kwargs['models'] = models

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'networkIds', 'productTypes', 'name', 'mac', 'serial', 'model', 'macs', 'serials', 'models'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'networkIds', 'productTypes', 'name', 'mac', 'serial', 'model', 'macs', 'serials', 'models'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'networkIds', 'productTypes', 'name', 'mac', 'serial', 'model', 'macs', 'serials', 'models'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationWirelessRfProfilesAssignmentsByDevice

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationWirelessSsidsStatusesByDevice')
def getOrganizationWirelessSsidsStatusesByDevice(organizationId: str = None, networkIds: list = None, serials: list = None, bssids: list = None, hideDisabled: bool = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if networkIds is not None:
        final_kwargs['networkIds'] = networkIds
    if serials is not None:
        final_kwargs['serials'] = serials
    if bssids is not None:
        final_kwargs['bssids'] = bssids
    if hideDisabled is not None:
        final_kwargs['hideDisabled'] = hideDisabled
    if perPage is not None:
        final_kwargs['perPage'] = perPage
    if startingAfter is not None:
        final_kwargs['startingAfter'] = startingAfter
    if endingBefore is not None:
        final_kwargs['endingBefore'] = endingBefore

    # No body parameter for this function.
    body_payload = None

    # ── auto-inject MERAKI_ORG_ID ─────────────────
    env_val = os.getenv('MERAKI_ORG_ID')
    if env_val:
        if 'organizationId' in ['organizationId', 'networkIds', 'serials', 'bssids', 'hideDisabled', 'perPage', 'startingAfter', 'endingBefore'] and 'organizationId' not in final_kwargs:
            final_kwargs['organizationId'] = f"""{env_val}"""
        if 'organization_id' in ['organizationId', 'networkIds', 'serials', 'bssids', 'hideDisabled', 'perPage', 'startingAfter', 'endingBefore'] and 'organization_id' not in final_kwargs:
            final_kwargs['organization_id'] = f"""{env_val}"""
        if 'org_id' in ['organizationId', 'networkIds', 'serials', 'bssids', 'hideDisabled', 'perPage', 'startingAfter', 'endingBefore'] and 'org_id' not in final_kwargs:
            final_kwargs['org_id'] = f"""{env_val}"""

    client = MerakiClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationWirelessSsidsStatusesByDevice

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)
