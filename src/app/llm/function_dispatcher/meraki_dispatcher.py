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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in [] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getAdministeredIdentitiesMe')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in [] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getAdministeredIdentitiesMeApiKeys')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['skus'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getAdministeredLicensingSubscriptionEntitlements')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['perPage', 'startingAfter', 'endingBefore', 'subscriptionIds', 'organizationIds', 'statuses', 'productTypes', 'name', 'startDate', 'endDate'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getAdministeredLicensingSubscriptionSubscriptions')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationIds', 'subscriptionIds'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getAdministeredLicensingSubscriptionSubscriptionsComplianceStatu')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getDevice')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getDeviceApplianceDhcpSubnets')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial', 't0', 't1', 'timespan'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getDeviceAppliancePerformance')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getDeviceAppliancePrefixesDelegated')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getDeviceAppliancePrefixesDelegatedVlanAssignments')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getDeviceApplianceRadioSettings')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getDeviceApplianceUplinksSettings')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getDeviceCameraAnalyticsLive')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial', 't0', 't1', 'timespan', 'objectType'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getDeviceCameraAnalyticsOverview')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial', 'objectType'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getDeviceCameraAnalyticsRecent')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getDeviceCameraAnalyticsZones')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial', 'zoneId', 't0', 't1', 'timespan', 'resolution', 'objectType'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getDeviceCameraAnalyticsZoneHistory')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getDeviceCameraCustomAnalytics')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getDeviceCameraQualityAndRetention')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getDeviceCameraSense')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getDeviceCameraSenseObjectDetectionModels')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getDeviceCameraVideoSettings')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial', 'timestamp'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getDeviceCameraVideoLink')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getDeviceCameraWirelessProfiles')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getDeviceCellularSims')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getDeviceCellularGatewayLan')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getDeviceCellularGatewayPortForwardingRules')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial', 't0', 'timespan'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getDeviceClients')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial', 'arpTableId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getDeviceLiveToolsArpTable')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial', 'id'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getDeviceLiveToolsCableTest')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial', 'ledsBlinkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getDeviceLiveToolsLedsBlink')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial', 'id'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getDeviceLiveToolsPing')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial', 'id'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getDeviceLiveToolsPingDevice')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial', 'throughputTestId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getDeviceLiveToolsThroughputTest')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial', 'wakeOnLanId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getDeviceLiveToolsWakeOnLan')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getDeviceLldpCdp')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial', 't0', 't1', 'timespan', 'resolution', 'uplink', 'ip'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getDeviceLossAndLatencyHistory')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getDeviceManagementInterface')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial', 'operations', 'perPage', 'startingAfter', 'endingBefore', 'sortOrder', 't0', 't1', 'timespan'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getDeviceSensorCommands')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial', 'commandId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getDeviceSensorCommand')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getDeviceSensorRelationships')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getDeviceSwitchPorts')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial', 't0', 'timespan'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getDeviceSwitchPortsStatuses')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial', 't0', 'timespan'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getDeviceSwitchPortsStatusesPackets')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial', 'portId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getDeviceSwitchPort')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getDeviceSwitchRoutingInterfaces')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial', 'interfaceId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getDeviceSwitchRoutingInterface')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial', 'interfaceId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getDeviceSwitchRoutingInterfaceDhcp')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getDeviceSwitchRoutingStaticRoutes')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial', 'staticRouteId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getDeviceSwitchRoutingStaticRoute')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getDeviceSwitchWarmSpare')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getDeviceWirelessBluetoothSettings')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial', 't0', 't1', 'timespan', 'band', 'ssid', 'vlan', 'apTag'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getDeviceWirelessConnectionStats')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getDeviceWirelessElectronicShelfLabel')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial', 't0', 't1', 'timespan', 'band', 'ssid', 'vlan', 'apTag', 'fields'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getDeviceWirelessLatencyStats')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getDeviceWirelessRadioSettings')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getDeviceWirelessStatus')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetwork')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'perPage', 'startingAfter', 'endingBefore'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkAlertsHistory')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkAlertsSettings')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'clientId', 't0', 't1', 'timespan', 'perPage', 'startingAfter', 'endingBefore', 'sortOrder'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkApplianceClientSecurityEvents')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkApplianceConnectivityMonitoringDestinations')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkApplianceContentFiltering')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkApplianceContentFilteringCategories')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkApplianceFirewallCellularFirewallRules')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkApplianceFirewallFirewalledServices')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'service'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkApplianceFirewallFirewalledService')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkApplianceFirewallInboundCellularFirewallRules')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkApplianceFirewallInboundFirewallRules')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkApplianceFirewallL3FirewallRules')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkApplianceFirewallL7FirewallRules')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkApplianceFirewallL7FirewallRulesApplicationCategories')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkApplianceFirewallOneToManyNatRules')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkApplianceFirewallOneToOneNatRules')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkApplianceFirewallPortForwardingRules')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkApplianceFirewallSettings')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkAppliancePorts')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'portId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkAppliancePort')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkAppliancePrefixesDelegatedStatics')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'staticDelegatedPrefixId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkAppliancePrefixesDelegatedStatic')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkApplianceRfProfiles')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'rfProfileId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkApplianceRfProfile')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 't0', 't1', 'timespan', 'perPage', 'startingAfter', 'endingBefore', 'sortOrder'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkApplianceSecurityEvents')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkApplianceSecurityIntrusion')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkApplianceSecurityMalware')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkApplianceSettings')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkApplianceSingleLan')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkApplianceSsids')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'number'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkApplianceSsid')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkApplianceStaticRoutes')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'staticRouteId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkApplianceStaticRoute')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkApplianceTrafficShaping')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkApplianceTrafficShapingCustomPerformanceClasses')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'customPerformanceClassId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkApplianceTrafficShapingCustomPerformanceClass')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkApplianceTrafficShapingRules')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkApplianceTrafficShapingUplinkBandwidth')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkApplianceTrafficShapingUplinkSelection')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 't0', 't1', 'timespan', 'resolution'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkApplianceUplinksUsageHistory')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkApplianceVlans')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkApplianceVlansSettings')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'vlanId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkApplianceVlan')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkApplianceVpnBgp')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkApplianceVpnSiteToSiteVpn')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkApplianceWarmSpare')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 't0', 'timespan', 'perPage', 'startingAfter', 'endingBefore', 'includeConnectivityHistory'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkBluetoothClients')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'bluetoothClientId', 'includeConnectivityHistory', 'connectivityHistoryTimespan'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkBluetoothClient')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkCameraQualityRetentionProfiles')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'qualityRetentionProfileId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkCameraQualityRetentionProfile')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkCameraSchedules')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkCameraWirelessProfiles')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'wirelessProfileId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkCameraWirelessProfile')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkCellularGatewayConnectivityMonitoringDestinations')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkCellularGatewayDhcp')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkCellularGatewaySubnetPool')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkCellularGatewayUplink')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 't0', 'timespan', 'perPage', 'startingAfter', 'endingBefore', 'statuses', 'ip', 'ip6', 'ip6Local', 'mac', 'os', 'pskGroup', 'description', 'vlan', 'namedVlan', 'recentDeviceConnections'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkClients')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'clients', 'ssidNumber', 'perPage', 'startingAfter', 'endingBefore', 't0', 't1', 'timespan'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkClientsApplicationUsage')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 't0', 't1', 'timespan', 'perPage', 'startingAfter', 'endingBefore'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkClientsBandwidthUsageHistory')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 't0', 't1', 'timespan', 'resolution'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkClientsOverview')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'clients', 'ssidNumber', 'perPage', 'startingAfter', 'endingBefore', 't0', 't1', 'timespan'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkClientsUsageHistories')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'clientId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkClient')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'clientId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkClientPolicy')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'clientId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkClientSplashAuthorizationStatus')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'clientId', 'perPage', 'startingAfter', 'endingBefore'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkClientTrafficHistory')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'clientId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkClientUsageHistory')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkDevices')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'productType', 'includedEventTypes', 'excludedEventTypes', 'deviceMac', 'deviceSerial', 'deviceName', 'clientIp', 'clientMac', 'clientName', 'smDeviceMac', 'smDeviceName', 'eventDetails', 'eventSeverity', 'isCatalyst', 'perPage', 'startingAfter', 'endingBefore'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkEvents')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkEventsEventTypes')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkFirmwareUpgrades')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkFirmwareUpgradesStagedEvents')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkFirmwareUpgradesStagedGroups')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'groupId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkFirmwareUpgradesStagedGroup')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkFirmwareUpgradesStagedStages')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkFloorPlans')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'floorPlanId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkFloorPlan')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkGroupPolicies')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'groupPolicyId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkGroupPolicy')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkHealthAlerts')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'applicationId', 't0', 't1', 'timespan', 'resolution'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkInsightApplicationHealthByTime')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkMerakiAuthUsers')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'merakiAuthUserId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkMerakiAuthUser')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkMqttBrokers')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'mqttBrokerId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkMqttBroker')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkNetflow')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 't0', 't1', 'timespan', 'resolution', 'perPage', 'startingAfter', 'endingBefore'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkNetworkHealthChannelUtilization')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'username', 'email', 'mac', 'serial', 'imei', 'bluetoothMac'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkPiiPiiKeys')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkPiiRequests')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'requestId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkPiiRequest')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'username', 'email', 'mac', 'serial', 'imei', 'bluetoothMac'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkPiiSmDevicesForKey')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'username', 'email', 'mac', 'serial', 'imei', 'bluetoothMac'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkPiiSmOwnersForKey')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'perPage', 'startingAfter', 'endingBefore', 't0', 'timespan'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkPoliciesByClient')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkSensorAlertsCurrentOverviewByMetric')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 't0', 't1', 'timespan', 'interval'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkSensorAlertsOverviewByMetric')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkSensorAlertsProfiles')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'id'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkSensorAlertsProfile')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkSensorMqttBrokers')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'mqttBrokerId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkSensorMqttBroker')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkSensorRelationships')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkSettings')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'attemptId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkSmBypassActivationLockAttempt')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'fields', 'wifiMacs', 'serials', 'ids', 'uuids', 'systemTypes', 'scope', 'perPage', 'startingAfter', 'endingBefore'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkSmDevices')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'deviceId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkSmDeviceCellularUsageHistory')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'deviceId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkSmDeviceCerts')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'deviceId', 'perPage', 'startingAfter', 'endingBefore'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkSmDeviceConnectivity')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'deviceId', 'perPage', 'startingAfter', 'endingBefore'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkSmDeviceDesktopLogs')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'deviceId', 'perPage', 'startingAfter', 'endingBefore'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkSmDeviceDeviceCommandLogs')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'deviceId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkSmDeviceDeviceProfiles')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'deviceId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkSmDeviceNetworkAdapters')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'deviceId', 'perPage', 'startingAfter', 'endingBefore'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkSmDevicePerformanceHistory')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'deviceId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkSmDeviceRestrictions')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'deviceId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkSmDeviceSecurityCenters')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'deviceId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkSmDeviceSoftwares')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'deviceId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkSmDeviceWlanLists')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'payloadTypes'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkSmProfiles')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'withDetails'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkSmTargetGroups')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'targetGroupId', 'withDetails'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkSmTargetGroup')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'perPage', 'startingAfter', 'endingBefore'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkSmTrustedAccessConfigs')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'perPage', 'startingAfter', 'endingBefore'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkSmUserAccessDevices')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'ids', 'usernames', 'emails', 'scope'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkSmUsers')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'userId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkSmUserDeviceProfiles')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'userId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkSmUserSoftwares')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkSnmp')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'ssidNumber', 'loginIdentifier', 'timespan'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkSplashLoginAttempts')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkSwitchAccessControlLists')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkSwitchAccessPolicies')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'accessPolicyNumber'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkSwitchAccessPolicy')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkSwitchAlternateManagementInterface')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 't0', 'timespan', 'perPage', 'startingAfter', 'endingBefore'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkSwitchDhcpV4ServersSeen')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkSwitchDhcpServerPolicy')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'perPage', 'startingAfter', 'endingBefore'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'perPage', 'startingAfter', 'endingBefore'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkSwitchDhcpServerPolicyArpInspectionWarningsByDevice')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkSwitchDscpToCosMappings')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkSwitchLinkAggregations')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkSwitchMtu')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkSwitchPortSchedules')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkSwitchQosRules')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkSwitchQosRulesOrder')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'qosRuleId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkSwitchQosRule')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkSwitchRoutingMulticast')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkSwitchRoutingMulticastRendezvousPoints')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'rendezvousPointId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkSwitchRoutingMulticastRendezvousPoint')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkSwitchRoutingOspf')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkSwitchSettings')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkSwitchStacks')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'switchStackId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkSwitchStack')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'switchStackId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkSwitchStackRoutingInterfaces')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'switchStackId', 'interfaceId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkSwitchStackRoutingInterface')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'switchStackId', 'interfaceId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkSwitchStackRoutingInterfaceDhcp')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'switchStackId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkSwitchStackRoutingStaticRoutes')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'switchStackId', 'staticRouteId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkSwitchStackRoutingStaticRoute')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkSwitchStormControl')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkSwitchStp')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkSyslogServers')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkTopologyLinkLayer')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 't0', 'timespan', 'deviceType'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkTraffic')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkTrafficAnalysis')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkTrafficShapingApplicationCategories')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkTrafficShapingDscpTaggingOptions')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkVlanProfiles')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'perPage', 'startingAfter', 'endingBefore', 'serials', 'productTypes', 'stackIds'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkVlanProfilesAssignmentsByDevice')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'iname'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkVlanProfile')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkWebhooksHttpServers')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'httpServerId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkWebhooksHttpServer')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkWebhooksPayloadTemplates')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'payloadTemplateId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkWebhooksPayloadTemplate')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'webhookTestId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkWebhooksWebhookTest')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 't0', 'timespan'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkWirelessAirMarshal')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkWirelessAlternateManagementInterface')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkWirelessBilling')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkWirelessBluetoothSettings')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 't0', 't1', 'timespan', 'resolution', 'autoResolution', 'clientId', 'deviceSerial', 'apTag', 'band'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkWirelessChannelUtilizationHistory')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 't0', 't1', 'timespan', 'resolution', 'autoResolution', 'clientId', 'deviceSerial', 'apTag', 'band', 'ssid'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkWirelessClientCountHistory')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 't0', 't1', 'timespan', 'band', 'ssid', 'vlan', 'apTag'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkWirelessClientsConnectionStats')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 't0', 't1', 'timespan', 'band', 'ssid', 'vlan', 'apTag', 'fields'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkWirelessClientsLatencyStats')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'clientId', 't0', 't1', 'timespan', 'band', 'ssid', 'vlan', 'apTag'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkWirelessClientConnectionStats')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'clientId', 'perPage', 'startingAfter', 'endingBefore', 'sortOrder', 't0', 't1', 'timespan', 'types', 'band', 'ssidNumber', 'includedSeverities', 'deviceSerial'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkWirelessClientConnectivityEvents')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'clientId', 't0', 't1', 'timespan', 'resolution'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkWirelessClientLatencyHistory')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'clientId', 't0', 't1', 'timespan', 'band', 'ssid', 'vlan', 'apTag', 'fields'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkWirelessClientLatencyStats')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 't0', 't1', 'timespan', 'band', 'ssid', 'vlan', 'apTag'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkWirelessConnectionStats')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 't0', 't1', 'timespan', 'resolution', 'autoResolution', 'clientId', 'deviceSerial', 'apTag', 'band', 'ssid'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkWirelessDataRateHistory')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 't0', 't1', 'timespan', 'band', 'ssid', 'vlan', 'apTag'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkWirelessDevicesConnectionStats')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 't0', 't1', 'timespan', 'band', 'ssid', 'vlan', 'apTag', 'fields'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkWirelessDevicesLatencyStats')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkWirelessElectronicShelfLabel')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkWirelessElectronicShelfLabelConfiguredDevices')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkWirelessEthernetPortsProfiles')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'profileId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkWirelessEthernetPortsProfile')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 't0', 't1', 'timespan', 'band', 'ssid', 'vlan', 'apTag', 'serial', 'clientId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkWirelessFailedConnections')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 't0', 't1', 'timespan', 'resolution', 'autoResolution', 'clientId', 'deviceSerial', 'apTag', 'band', 'ssid', 'accessCategory'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkWirelessLatencyHistory')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 't0', 't1', 'timespan', 'band', 'ssid', 'vlan', 'apTag', 'fields'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkWirelessLatencyStats')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'perPage', 'startingAfter', 'endingBefore'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkWirelessMeshStatuses')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'includeTemplateProfiles'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkWirelessRfProfiles')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'rfProfileId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkWirelessRfProfile')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkWirelessSettings')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 't0', 't1', 'timespan', 'resolution', 'autoResolution', 'clientId', 'deviceSerial', 'apTag', 'band', 'ssid'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkWirelessSignalQualityHistory')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkWirelessSsids')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'number'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkWirelessSsid')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'number'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkWirelessSsidBonjourForwarding')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'number'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkWirelessSsidDeviceTypeGroupPolicies')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'number'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkWirelessSsidEapOverride')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'number'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkWirelessSsidFirewallL3FirewallRules')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'number'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkWirelessSsidFirewallL7FirewallRules')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'number'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkWirelessSsidHotspot20')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'number'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkWirelessSsidIdentityPsks')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'number', 'identityPskId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkWirelessSsidIdentityPsk')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'number'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkWirelessSsidSchedules')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'number'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkWirelessSsidSplashSettings')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'number'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkWirelessSsidTrafficShapingRules')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'number'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkWirelessSsidVpn')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 't0', 't1', 'timespan', 'resolution', 'autoResolution', 'clientId', 'deviceSerial', 'apTag', 'band', 'ssid'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getNetworkWirelessUsageHistory')

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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['perPage', 'startingAfter', 'endingBefore'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizations')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganization')
def getOrganization(organizationId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId

    # No body parameter for this function.
    body_payload = None

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganization')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationActionBatches')
def getOrganizationActionBatches(organizationId: str, status: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if status is not None:
        final_kwargs['status'] = status

    # No body parameter for this function.
    body_payload = None

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'status'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationActionBatches')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationActionBatch')
def getOrganizationActionBatch(organizationId: str, actionBatchId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if actionBatchId is not None:
        final_kwargs['actionBatchId'] = actionBatchId

    # No body parameter for this function.
    body_payload = None

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'actionBatchId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationActionBatch')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationAdaptivePolicyAcls')
def getOrganizationAdaptivePolicyAcls(organizationId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId

    # No body parameter for this function.
    body_payload = None

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationAdaptivePolicyAcls')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationAdaptivePolicyAcl')
def getOrganizationAdaptivePolicyAcl(organizationId: str, aclId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if aclId is not None:
        final_kwargs['aclId'] = aclId

    # No body parameter for this function.
    body_payload = None

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'aclId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationAdaptivePolicyAcl')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationAdaptivePolicyGroups')
def getOrganizationAdaptivePolicyGroups(organizationId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId

    # No body parameter for this function.
    body_payload = None

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationAdaptivePolicyGroups')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationAdaptivePolicyGroup')
def getOrganizationAdaptivePolicyGroup(organizationId: str, id: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if id is not None:
        final_kwargs['id'] = id

    # No body parameter for this function.
    body_payload = None

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'id'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationAdaptivePolicyGroup')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationAdaptivePolicyOverview')
def getOrganizationAdaptivePolicyOverview(organizationId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId

    # No body parameter for this function.
    body_payload = None

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationAdaptivePolicyOverview')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationAdaptivePolicyPolicies')
def getOrganizationAdaptivePolicyPolicies(organizationId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId

    # No body parameter for this function.
    body_payload = None

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationAdaptivePolicyPolicies')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationAdaptivePolicyPolicy')
def getOrganizationAdaptivePolicyPolicy(organizationId: str, id: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if id is not None:
        final_kwargs['id'] = id

    # No body parameter for this function.
    body_payload = None

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'id'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationAdaptivePolicyPolicy')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationAdaptivePolicySettings')
def getOrganizationAdaptivePolicySettings(organizationId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId

    # No body parameter for this function.
    body_payload = None

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationAdaptivePolicySettings')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationAdmins')
def getOrganizationAdmins(organizationId: str, networkIds: list = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if networkIds is not None:
        final_kwargs['networkIds'] = networkIds

    # No body parameter for this function.
    body_payload = None

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'networkIds'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationAdmins')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationAlertsProfiles')
def getOrganizationAlertsProfiles(organizationId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId

    # No body parameter for this function.
    body_payload = None

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationAlertsProfiles')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationApiRequests')
def getOrganizationApiRequests(organizationId: str, t0: str = None, t1: str = None, timespan: float = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None, adminId: str = None, path: str = None, method: str = None, responseCode: int = None, sourceIp: str = None, userAgent: str = None, version: int = None, operationIds: list = None):
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 't0', 't1', 'timespan', 'perPage', 'startingAfter', 'endingBefore', 'adminId', 'path', 'method', 'responseCode', 'sourceIp', 'userAgent', 'version', 'operationIds'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationApiRequests')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationApiRequestsOverview')
def getOrganizationApiRequestsOverview(organizationId: str, t0: str = None, t1: str = None, timespan: float = None):
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 't0', 't1', 'timespan'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationApiRequestsOverview')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationApiRequestsOverviewResponseCodesByInterval')
def getOrganizationApiRequestsOverviewResponseCodesByInterval(organizationId: str, t0: str = None, t1: str = None, timespan: float = None, interval: int = None, version: int = None, operationIds: list = None, sourceIps: list = None, adminIds: list = None, userAgent: str = None):
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 't0', 't1', 'timespan', 'interval', 'version', 'operationIds', 'sourceIps', 'adminIds', 'userAgent'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationApiRequestsOverviewResponseCodesByInterval')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationApplianceSecurityEvents')
def getOrganizationApplianceSecurityEvents(organizationId: str, t0: str = None, t1: str = None, timespan: float = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None, sortOrder: str = None):
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 't0', 't1', 'timespan', 'perPage', 'startingAfter', 'endingBefore', 'sortOrder'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationApplianceSecurityEvents')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationApplianceSecurityIntrusion')
def getOrganizationApplianceSecurityIntrusion(organizationId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId

    # No body parameter for this function.
    body_payload = None

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationApplianceSecurityIntrusion')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationApplianceTrafficShapingVpnExclusionsByNetwork')
def getOrganizationApplianceTrafficShapingVpnExclusionsByNetwork(organizationId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None, networkIds: list = None):
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'networkIds'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationApplianceTrafficShapingVpnExclusionsByNetwork')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationApplianceUplinkStatuses')
def getOrganizationApplianceUplinkStatuses(organizationId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None, networkIds: list = None, serials: list = None, iccids: list = None):
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'networkIds', 'serials', 'iccids'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationApplianceUplinkStatuses')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationApplianceUplinksStatusesOverview')
def getOrganizationApplianceUplinksStatusesOverview(organizationId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId

    # No body parameter for this function.
    body_payload = None

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationApplianceUplinksStatusesOverview')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationApplianceUplinksUsageByNetwork')
def getOrganizationApplianceUplinksUsageByNetwork(organizationId: str, t0: str = None, t1: str = None, timespan: float = None):
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 't0', 't1', 'timespan'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationApplianceUplinksUsageByNetwork')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationApplianceVpnStats')
def getOrganizationApplianceVpnStats(organizationId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None, networkIds: list = None, t0: str = None, t1: str = None, timespan: float = None):
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'networkIds', 't0', 't1', 'timespan'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationApplianceVpnStats')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationApplianceVpnStatuses')
def getOrganizationApplianceVpnStatuses(organizationId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None, networkIds: list = None):
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'networkIds'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationApplianceVpnStatuses')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationApplianceVpnThirdPartyVPNPeers')
def getOrganizationApplianceVpnThirdPartyVPNPeers(organizationId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId

    # No body parameter for this function.
    body_payload = None

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationApplianceVpnThirdPartyVPNPeers')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationApplianceVpnVpnFirewallRules')
def getOrganizationApplianceVpnVpnFirewallRules(organizationId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId

    # No body parameter for this function.
    body_payload = None

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationApplianceVpnVpnFirewallRules')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationAssuranceAlerts')
def getOrganizationAssuranceAlerts(organizationId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None, sortOrder: str = None, networkId: str = None, severity: str = None, types: list = None, tsStart: str = None, tsEnd: str = None, category: str = None, sortBy: str = None, serials: list = None, deviceTypes: list = None, deviceTags: list = None, active: bool = None, dismissed: bool = None, resolved: bool = None, suppressAlertsForOfflineNodes: bool = None):
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'sortOrder', 'networkId', 'severity', 'types', 'tsStart', 'tsEnd', 'category', 'sortBy', 'serials', 'deviceTypes', 'deviceTags', 'active', 'dismissed', 'resolved', 'suppressAlertsForOfflineNodes'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationAssuranceAlerts')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationAssuranceAlertsOverview')
def getOrganizationAssuranceAlertsOverview(organizationId: str, networkId: str = None, severity: str = None, types: list = None, tsStart: str = None, tsEnd: str = None, category: str = None, serials: list = None, deviceTypes: list = None, deviceTags: list = None, active: bool = None, dismissed: bool = None, resolved: bool = None, suppressAlertsForOfflineNodes: bool = None):
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'networkId', 'severity', 'types', 'tsStart', 'tsEnd', 'category', 'serials', 'deviceTypes', 'deviceTags', 'active', 'dismissed', 'resolved', 'suppressAlertsForOfflineNodes'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationAssuranceAlertsOverview')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationAssuranceAlertsOverviewByNetwork')
def getOrganizationAssuranceAlertsOverviewByNetwork(organizationId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None, sortOrder: str = None, networkId: str = None, severity: str = None, types: list = None, tsStart: str = None, tsEnd: str = None, category: str = None, serials: list = None, deviceTypes: list = None, deviceTags: list = None, active: bool = None, dismissed: bool = None, resolved: bool = None, suppressAlertsForOfflineNodes: bool = None):
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'sortOrder', 'networkId', 'severity', 'types', 'tsStart', 'tsEnd', 'category', 'serials', 'deviceTypes', 'deviceTags', 'active', 'dismissed', 'resolved', 'suppressAlertsForOfflineNodes'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationAssuranceAlertsOverviewByNetwork')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationAssuranceAlertsOverviewByType')
def getOrganizationAssuranceAlertsOverviewByType(organizationId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None, sortOrder: str = None, networkId: str = None, severity: str = None, types: list = None, tsStart: str = None, tsEnd: str = None, category: str = None, sortBy: str = None, serials: list = None, deviceTypes: list = None, deviceTags: list = None, active: bool = None, dismissed: bool = None, resolved: bool = None, suppressAlertsForOfflineNodes: bool = None):
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'sortOrder', 'networkId', 'severity', 'types', 'tsStart', 'tsEnd', 'category', 'sortBy', 'serials', 'deviceTypes', 'deviceTags', 'active', 'dismissed', 'resolved', 'suppressAlertsForOfflineNodes'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationAssuranceAlertsOverviewByType')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationAssuranceAlertsOverviewHistorical')
def getOrganizationAssuranceAlertsOverviewHistorical(organizationId: str, segmentDuration: int, tsStart: str, networkId: str = None, severity: str = None, types: list = None, tsEnd: str = None, category: str = None, serials: list = None, deviceTypes: list = None):
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'segmentDuration', 'networkId', 'severity', 'types', 'tsStart', 'tsEnd', 'category', 'serials', 'deviceTypes'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationAssuranceAlertsOverviewHistorical')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationAssuranceAlert')
def getOrganizationAssuranceAlert(organizationId: str, id: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if id is not None:
        final_kwargs['id'] = id

    # No body parameter for this function.
    body_payload = None

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'id'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationAssuranceAlert')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationBrandingPolicies')
def getOrganizationBrandingPolicies(organizationId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId

    # No body parameter for this function.
    body_payload = None

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationBrandingPolicies')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationBrandingPoliciesPriorities')
def getOrganizationBrandingPoliciesPriorities(organizationId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId

    # No body parameter for this function.
    body_payload = None

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationBrandingPoliciesPriorities')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationBrandingPolicy')
def getOrganizationBrandingPolicy(organizationId: str, brandingPolicyId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if brandingPolicyId is not None:
        final_kwargs['brandingPolicyId'] = brandingPolicyId

    # No body parameter for this function.
    body_payload = None

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'brandingPolicyId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationBrandingPolicy')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationCameraBoundariesAreasByDevice')
def getOrganizationCameraBoundariesAreasByDevice(organizationId: str, serials: list = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if serials is not None:
        final_kwargs['serials'] = serials

    # No body parameter for this function.
    body_payload = None

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'serials'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationCameraBoundariesAreasByDevice')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationCameraBoundariesLinesByDevice')
def getOrganizationCameraBoundariesLinesByDevice(organizationId: str, serials: list = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if serials is not None:
        final_kwargs['serials'] = serials

    # No body parameter for this function.
    body_payload = None

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'serials'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationCameraBoundariesLinesByDevice')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationCameraCustomAnalyticsArtifacts')
def getOrganizationCameraCustomAnalyticsArtifacts(organizationId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId

    # No body parameter for this function.
    body_payload = None

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationCameraCustomAnalyticsArtifacts')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationCameraCustomAnalyticsArtifact')
def getOrganizationCameraCustomAnalyticsArtifact(organizationId: str, artifactId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if artifactId is not None:
        final_kwargs['artifactId'] = artifactId

    # No body parameter for this function.
    body_payload = None

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'artifactId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationCameraCustomAnalyticsArtifact')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationCameraDetectionsHistoryByBoundaryByInterval')
def getOrganizationCameraDetectionsHistoryByBoundaryByInterval(organizationId: str, boundaryIds: list, ranges: list, duration: int = None, perPage: int = None, boundaryTypes: list = None):
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'boundaryIds', 'ranges', 'duration', 'perPage', 'boundaryTypes'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationCameraDetectionsHistoryByBoundaryByInterval')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationCameraOnboardingStatuses')
def getOrganizationCameraOnboardingStatuses(organizationId: str, serials: list = None, networkIds: list = None):
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'serials', 'networkIds'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationCameraOnboardingStatuses')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationCameraPermissions')
def getOrganizationCameraPermissions(organizationId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId

    # No body parameter for this function.
    body_payload = None

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationCameraPermissions')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationCameraPermission')
def getOrganizationCameraPermission(organizationId: str, permissionScopeId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if permissionScopeId is not None:
        final_kwargs['permissionScopeId'] = permissionScopeId

    # No body parameter for this function.
    body_payload = None

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'permissionScopeId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationCameraPermission')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationCameraRoles')
def getOrganizationCameraRoles(organizationId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId

    # No body parameter for this function.
    body_payload = None

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationCameraRoles')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationCameraRole')
def getOrganizationCameraRole(organizationId: str, roleId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if roleId is not None:
        final_kwargs['roleId'] = roleId

    # No body parameter for this function.
    body_payload = None

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'roleId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationCameraRole')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationCellularGatewayEsimsInventory')
def getOrganizationCellularGatewayEsimsInventory(organizationId: str, eids: list = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if eids is not None:
        final_kwargs['eids'] = eids

    # No body parameter for this function.
    body_payload = None

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'eids'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationCellularGatewayEsimsInventory')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationCellularGatewayEsimsServiceProviders')
def getOrganizationCellularGatewayEsimsServiceProviders(organizationId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId

    # No body parameter for this function.
    body_payload = None

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationCellularGatewayEsimsServiceProviders')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationCellularGatewayEsimsServiceProvidersAccounts')
def getOrganizationCellularGatewayEsimsServiceProvidersAccounts(organizationId: str, accountIds: list = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if accountIds is not None:
        final_kwargs['accountIds'] = accountIds

    # No body parameter for this function.
    body_payload = None

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'accountIds'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationCellularGatewayEsimsServiceProvidersAccounts')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationCellularGatewayEsimsServiceProvidersAccountsCommu')
def getOrganizationCellularGatewayEsimsServiceProvidersAccountsCommu(organizationId: str, accountIds: list):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if accountIds is not None:
        final_kwargs['accountIds'] = accountIds

    # No body parameter for this function.
    body_payload = None

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'accountIds'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationCellularGatewayEsimsServiceProvidersAccountsCommu')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationCellularGatewayEsimsServiceProvidersAccountsRateP')
def getOrganizationCellularGatewayEsimsServiceProvidersAccountsRateP(organizationId: str, accountIds: list):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if accountIds is not None:
        final_kwargs['accountIds'] = accountIds

    # No body parameter for this function.
    body_payload = None

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'accountIds'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationCellularGatewayEsimsServiceProvidersAccountsRateP')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationCellularGatewayUplinkStatuses')
def getOrganizationCellularGatewayUplinkStatuses(organizationId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None, networkIds: list = None, serials: list = None, iccids: list = None):
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'networkIds', 'serials', 'iccids'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationCellularGatewayUplinkStatuses')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationClientsBandwidthUsageHistory')
def getOrganizationClientsBandwidthUsageHistory(organizationId: str, networkTag: str = None, deviceTag: str = None, ssidName: str = None, usageUplink: str = None, t0: str = None, t1: str = None, timespan: float = None):
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'networkTag', 'deviceTag', 'ssidName', 'usageUplink', 't0', 't1', 'timespan'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationClientsBandwidthUsageHistory')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationClientsOverview')
def getOrganizationClientsOverview(organizationId: str, t0: str = None, t1: str = None, timespan: float = None):
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 't0', 't1', 'timespan'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationClientsOverview')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationClientsSearch')
def getOrganizationClientsSearch(organizationId: str, mac: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'mac'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationClientsSearch')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationConfigTemplates')
def getOrganizationConfigTemplates(organizationId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId

    # No body parameter for this function.
    body_payload = None

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationConfigTemplates')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationConfigTemplate')
def getOrganizationConfigTemplate(organizationId: str, configTemplateId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if configTemplateId is not None:
        final_kwargs['configTemplateId'] = configTemplateId

    # No body parameter for this function.
    body_payload = None

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'configTemplateId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationConfigTemplate')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationConfigTemplateSwitchProfiles')
def getOrganizationConfigTemplateSwitchProfiles(organizationId: str, configTemplateId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if configTemplateId is not None:
        final_kwargs['configTemplateId'] = configTemplateId

    # No body parameter for this function.
    body_payload = None

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'configTemplateId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationConfigTemplateSwitchProfiles')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationConfigTemplateSwitchProfilePorts')
def getOrganizationConfigTemplateSwitchProfilePorts(organizationId: str, configTemplateId: str, profileId: str):
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'configTemplateId', 'profileId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationConfigTemplateSwitchProfilePorts')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationConfigTemplateSwitchProfilePort')
def getOrganizationConfigTemplateSwitchProfilePort(organizationId: str, configTemplateId: str, profileId: str, portId: str):
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'configTemplateId', 'profileId', 'portId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationConfigTemplateSwitchProfilePort')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationConfigurationChanges')
def getOrganizationConfigurationChanges(organizationId: str, t0: str = None, t1: str = None, timespan: float = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None, networkId: str = None, adminId: str = None):
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 't0', 't1', 'timespan', 'perPage', 'startingAfter', 'endingBefore', 'networkId', 'adminId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationConfigurationChanges')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationDevices')
def getOrganizationDevices(organizationId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None, configurationUpdatedAfter: str = None, networkIds: list = None, productTypes: list = None, tags: list = None, tagsFilterType: str = None, name: str = None, mac: str = None, serial: str = None, model: str = None, macs: list = None, serials: list = None, sensorMetrics: list = None, sensorAlertProfileIds: list = None, models: list = None):
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'configurationUpdatedAfter', 'networkIds', 'productTypes', 'tags', 'tagsFilterType', 'name', 'mac', 'serial', 'model', 'macs', 'serials', 'sensorMetrics', 'sensorAlertProfileIds', 'models'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationDevices')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationDevicesAvailabilities')
def getOrganizationDevicesAvailabilities(organizationId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None, networkIds: list = None, productTypes: list = None, serials: list = None, tags: list = None, tagsFilterType: str = None, statuses: list = None):
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'networkIds', 'productTypes', 'serials', 'tags', 'tagsFilterType', 'statuses'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationDevicesAvailabilities')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationDevicesAvailabilitiesChangeHistory')
def getOrganizationDevicesAvailabilitiesChangeHistory(organizationId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None, t0: str = None, t1: str = None, timespan: float = None, serials: list = None, productTypes: list = None, networkIds: list = None, statuses: list = None):
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 't0', 't1', 'timespan', 'serials', 'productTypes', 'networkIds', 'statuses'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationDevicesAvailabilitiesChangeHistory')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationDevicesOverviewByModel')
def getOrganizationDevicesOverviewByModel(organizationId: str, models: list = None, networkIds: list = None, productTypes: list = None):
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'models', 'networkIds', 'productTypes'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationDevicesOverviewByModel')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationDevicesPowerModulesStatusesByDevice')
def getOrganizationDevicesPowerModulesStatusesByDevice(organizationId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None, networkIds: list = None, productTypes: list = None, serials: list = None, tags: list = None, tagsFilterType: str = None):
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'networkIds', 'productTypes', 'serials', 'tags', 'tagsFilterType'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationDevicesPowerModulesStatusesByDevice')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationDevicesProvisioningStatuses')
def getOrganizationDevicesProvisioningStatuses(organizationId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None, networkIds: list = None, productTypes: list = None, serials: list = None, status: str = None, tags: list = None, tagsFilterType: str = None):
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'networkIds', 'productTypes', 'serials', 'status', 'tags', 'tagsFilterType'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationDevicesProvisioningStatuses')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationDevicesStatuses')
def getOrganizationDevicesStatuses(organizationId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None, networkIds: list = None, serials: list = None, statuses: list = None, productTypes: list = None, models: list = None, tags: list = None, tagsFilterType: str = None):
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'networkIds', 'serials', 'statuses', 'productTypes', 'models', 'tags', 'tagsFilterType'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationDevicesStatuses')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationDevicesStatusesOverview')
def getOrganizationDevicesStatusesOverview(organizationId: str, productTypes: list = None, networkIds: list = None):
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'productTypes', 'networkIds'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationDevicesStatusesOverview')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationDevicesUplinksAddressesByDevice')
def getOrganizationDevicesUplinksAddressesByDevice(organizationId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None, networkIds: list = None, productTypes: list = None, serials: list = None, tags: list = None, tagsFilterType: str = None):
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'networkIds', 'productTypes', 'serials', 'tags', 'tagsFilterType'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationDevicesUplinksAddressesByDevice')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationDevicesUplinksLossAndLatency')
def getOrganizationDevicesUplinksLossAndLatency(organizationId: str, t0: str = None, t1: str = None, timespan: float = None, uplink: str = None, ip: str = None):
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 't0', 't1', 'timespan', 'uplink', 'ip'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationDevicesUplinksLossAndLatency')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationEarlyAccessFeatures')
def getOrganizationEarlyAccessFeatures(organizationId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId

    # No body parameter for this function.
    body_payload = None

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationEarlyAccessFeatures')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationEarlyAccessFeaturesOptIns')
def getOrganizationEarlyAccessFeaturesOptIns(organizationId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId

    # No body parameter for this function.
    body_payload = None

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationEarlyAccessFeaturesOptIns')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationEarlyAccessFeaturesOptIn')
def getOrganizationEarlyAccessFeaturesOptIn(organizationId: str, optInId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if optInId is not None:
        final_kwargs['optInId'] = optInId

    # No body parameter for this function.
    body_payload = None

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'optInId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationEarlyAccessFeaturesOptIn')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationFirmwareUpgrades')
def getOrganizationFirmwareUpgrades(organizationId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None, status: list = None, productTypes: list = None):
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'status', 'productTypes'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationFirmwareUpgrades')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationFirmwareUpgradesByDevice')
def getOrganizationFirmwareUpgradesByDevice(organizationId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None, networkIds: list = None, serials: list = None, macs: list = None, firmwareUpgradeBatchIds: list = None, upgradeStatuses: list = None, currentUpgradesOnly: bool = None):
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'networkIds', 'serials', 'macs', 'firmwareUpgradeBatchIds', 'upgradeStatuses', 'currentUpgradesOnly'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationFirmwareUpgradesByDevice')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationFloorPlansAutoLocateDevices')
def getOrganizationFloorPlansAutoLocateDevices(organizationId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None, networkIds: list = None, floorPlanIds: list = None):
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'networkIds', 'floorPlanIds'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationFloorPlansAutoLocateDevices')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationFloorPlansAutoLocateStatuses')
def getOrganizationFloorPlansAutoLocateStatuses(organizationId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None, networkIds: list = None, floorPlanIds: list = None):
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'networkIds', 'floorPlanIds'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationFloorPlansAutoLocateStatuses')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationInsightApplications')
def getOrganizationInsightApplications(organizationId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId

    # No body parameter for this function.
    body_payload = None

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationInsightApplications')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationInsightMonitoredMediaServers')
def getOrganizationInsightMonitoredMediaServers(organizationId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId

    # No body parameter for this function.
    body_payload = None

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationInsightMonitoredMediaServers')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationInsightMonitoredMediaServer')
def getOrganizationInsightMonitoredMediaServer(organizationId: str, monitoredMediaServerId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if monitoredMediaServerId is not None:
        final_kwargs['monitoredMediaServerId'] = monitoredMediaServerId

    # No body parameter for this function.
    body_payload = None

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'monitoredMediaServerId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationInsightMonitoredMediaServer')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationInventoryDevices')
def getOrganizationInventoryDevices(organizationId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None, usedState: str = None, search: str = None, macs: list = None, networkIds: list = None, serials: list = None, models: list = None, orderNumbers: list = None, tags: list = None, tagsFilterType: str = None, productTypes: list = None):
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'usedState', 'search', 'macs', 'networkIds', 'serials', 'models', 'orderNumbers', 'tags', 'tagsFilterType', 'productTypes'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationInventoryDevices')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationInventoryDevicesSwapsBulk')
def getOrganizationInventoryDevicesSwapsBulk(organizationId: str, id: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if id is not None:
        final_kwargs['id'] = id

    # No body parameter for this function.
    body_payload = None

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'id'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationInventoryDevicesSwapsBulk')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationInventoryDevice')
def getOrganizationInventoryDevice(organizationId: str, serial: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if serial is not None:
        final_kwargs['serial'] = serial

    # No body parameter for this function.
    body_payload = None

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'serial'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationInventoryDevice')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationInventoryOnboardingCloudMonitoringImports')
def getOrganizationInventoryOnboardingCloudMonitoringImports(organizationId: str, importIds: list):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if importIds is not None:
        final_kwargs['importIds'] = importIds

    # No body parameter for this function.
    body_payload = None

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'importIds'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationInventoryOnboardingCloudMonitoringImports')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationInventoryOnboardingCloudMonitoringNetworks')
def getOrganizationInventoryOnboardingCloudMonitoringNetworks(organizationId: str, deviceType: str, search: str = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'deviceType', 'search', 'perPage', 'startingAfter', 'endingBefore'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationInventoryOnboardingCloudMonitoringNetworks')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationLicenses')
def getOrganizationLicenses(organizationId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None, deviceSerial: str = None, networkId: str = None, state: str = None):
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'deviceSerial', 'networkId', 'state'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationLicenses')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationLicensesOverview')
def getOrganizationLicensesOverview(organizationId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId

    # No body parameter for this function.
    body_payload = None

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationLicensesOverview')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationLicense')
def getOrganizationLicense(organizationId: str, licenseId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if licenseId is not None:
        final_kwargs['licenseId'] = licenseId

    # No body parameter for this function.
    body_payload = None

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'licenseId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationLicense')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationLicensingCotermLicenses')
def getOrganizationLicensingCotermLicenses(organizationId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None, invalidated: bool = None, expired: bool = None):
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'invalidated', 'expired'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationLicensingCotermLicenses')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationLoginSecurity')
def getOrganizationLoginSecurity(organizationId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId

    # No body parameter for this function.
    body_payload = None

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationLoginSecurity')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationNetworks')
def getOrganizationNetworks(organizationId: str, configTemplateId: str = None, isBoundToConfigTemplate: bool = None, tags: list = None, tagsFilterType: str = None, productTypes: list = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'configTemplateId', 'isBoundToConfigTemplate', 'tags', 'tagsFilterType', 'productTypes', 'perPage', 'startingAfter', 'endingBefore'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationNetworks')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationOpenapiSpec')
def getOrganizationOpenapiSpec(organizationId: str, version: int = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if version is not None:
        final_kwargs['version'] = version

    # No body parameter for this function.
    body_payload = None

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'version'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationOpenapiSpec')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationPolicyObjects')
def getOrganizationPolicyObjects(organizationId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'perPage', 'startingAfter', 'endingBefore'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationPolicyObjects')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationPolicyObjectsGroups')
def getOrganizationPolicyObjectsGroups(organizationId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'perPage', 'startingAfter', 'endingBefore'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationPolicyObjectsGroups')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationPolicyObjectsGroup')
def getOrganizationPolicyObjectsGroup(organizationId: str, policyObjectGroupId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if policyObjectGroupId is not None:
        final_kwargs['policyObjectGroupId'] = policyObjectGroupId

    # No body parameter for this function.
    body_payload = None

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'policyObjectGroupId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationPolicyObjectsGroup')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationPolicyObject')
def getOrganizationPolicyObject(organizationId: str, policyObjectId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if policyObjectId is not None:
        final_kwargs['policyObjectId'] = policyObjectId

    # No body parameter for this function.
    body_payload = None

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'policyObjectId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationPolicyObject')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSaml')
def getOrganizationSaml(organizationId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId

    # No body parameter for this function.
    body_payload = None

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationSaml')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSamlIdps')
def getOrganizationSamlIdps(organizationId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId

    # No body parameter for this function.
    body_payload = None

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationSamlIdps')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSamlIdp')
def getOrganizationSamlIdp(organizationId: str, idpId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if idpId is not None:
        final_kwargs['idpId'] = idpId

    # No body parameter for this function.
    body_payload = None

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'idpId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationSamlIdp')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSamlRoles')
def getOrganizationSamlRoles(organizationId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId

    # No body parameter for this function.
    body_payload = None

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationSamlRoles')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSamlRole')
def getOrganizationSamlRole(organizationId: str, samlRoleId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if samlRoleId is not None:
        final_kwargs['samlRoleId'] = samlRoleId

    # No body parameter for this function.
    body_payload = None

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'samlRoleId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationSamlRole')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSensorReadingsHistory')
def getOrganizationSensorReadingsHistory(organizationId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None, t0: str = None, t1: str = None, timespan: float = None, networkIds: list = None, serials: list = None, metrics: list = None):
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 't0', 't1', 'timespan', 'networkIds', 'serials', 'metrics'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationSensorReadingsHistory')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSensorReadingsLatest')
def getOrganizationSensorReadingsLatest(organizationId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None, networkIds: list = None, serials: list = None, metrics: list = None):
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'networkIds', 'serials', 'metrics'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationSensorReadingsLatest')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSmAdminsRoles')
def getOrganizationSmAdminsRoles(organizationId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'perPage', 'startingAfter', 'endingBefore'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationSmAdminsRoles')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSmAdminsRole')
def getOrganizationSmAdminsRole(organizationId: str, roleId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if roleId is not None:
        final_kwargs['roleId'] = roleId

    # No body parameter for this function.
    body_payload = None

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'roleId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationSmAdminsRole')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSmApnsCert')
def getOrganizationSmApnsCert(organizationId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId

    # No body parameter for this function.
    body_payload = None

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationSmApnsCert')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSmSentryPoliciesAssignmentsByNetwork')
def getOrganizationSmSentryPoliciesAssignmentsByNetwork(organizationId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None, networkIds: list = None):
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'networkIds'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationSmSentryPoliciesAssignmentsByNetwork')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSmVppAccounts')
def getOrganizationSmVppAccounts(organizationId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId

    # No body parameter for this function.
    body_payload = None

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationSmVppAccounts')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSmVppAccount')
def getOrganizationSmVppAccount(organizationId: str, vppAccountId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if vppAccountId is not None:
        final_kwargs['vppAccountId'] = vppAccountId

    # No body parameter for this function.
    body_payload = None

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'vppAccountId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationSmVppAccount')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSnmp')
def getOrganizationSnmp(organizationId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId

    # No body parameter for this function.
    body_payload = None

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationSnmp')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSplashAsset')
def getOrganizationSplashAsset(organizationId: str, id: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if id is not None:
        final_kwargs['id'] = id

    # No body parameter for this function.
    body_payload = None

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'id'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationSplashAsset')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSplashThemes')
def getOrganizationSplashThemes(organizationId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId

    # No body parameter for this function.
    body_payload = None

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationSplashThemes')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSummarySwitchPowerHistory')
def getOrganizationSummarySwitchPowerHistory(organizationId: str, t0: str = None, t1: str = None, timespan: float = None):
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 't0', 't1', 'timespan'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationSummarySwitchPowerHistory')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSummaryTopAppliancesByUtilization')
def getOrganizationSummaryTopAppliancesByUtilization(organizationId: str, networkTag: str = None, deviceTag: str = None, quantity: int = None, ssidName: str = None, usageUplink: str = None, t0: str = None, t1: str = None, timespan: float = None):
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'networkTag', 'deviceTag', 'quantity', 'ssidName', 'usageUplink', 't0', 't1', 'timespan'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationSummaryTopAppliancesByUtilization')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSummaryTopApplicationsByUsage')
def getOrganizationSummaryTopApplicationsByUsage(organizationId: str, networkTag: str = None, device: str = None, networkId: str = None, quantity: int = None, ssidName: str = None, usageUplink: str = None, t0: str = None, t1: str = None, timespan: float = None):
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'networkTag', 'device', 'networkId', 'quantity', 'ssidName', 'usageUplink', 't0', 't1', 'timespan'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationSummaryTopApplicationsByUsage')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSummaryTopApplicationsCategoriesByUsage')
def getOrganizationSummaryTopApplicationsCategoriesByUsage(organizationId: str, networkTag: str = None, deviceTag: str = None, networkId: str = None, quantity: int = None, ssidName: str = None, usageUplink: str = None, t0: str = None, t1: str = None, timespan: float = None):
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'networkTag', 'deviceTag', 'networkId', 'quantity', 'ssidName', 'usageUplink', 't0', 't1', 'timespan'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationSummaryTopApplicationsCategoriesByUsage')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSummaryTopClientsByUsage')
def getOrganizationSummaryTopClientsByUsage(organizationId: str, networkTag: str = None, deviceTag: str = None, quantity: int = None, ssidName: str = None, usageUplink: str = None, t0: str = None, t1: str = None, timespan: float = None):
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'networkTag', 'deviceTag', 'quantity', 'ssidName', 'usageUplink', 't0', 't1', 'timespan'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationSummaryTopClientsByUsage')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSummaryTopClientsManufacturersByUsage')
def getOrganizationSummaryTopClientsManufacturersByUsage(organizationId: str, networkTag: str = None, deviceTag: str = None, quantity: int = None, ssidName: str = None, usageUplink: str = None, t0: str = None, t1: str = None, timespan: float = None):
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'networkTag', 'deviceTag', 'quantity', 'ssidName', 'usageUplink', 't0', 't1', 'timespan'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationSummaryTopClientsManufacturersByUsage')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSummaryTopDevicesByUsage')
def getOrganizationSummaryTopDevicesByUsage(organizationId: str, networkTag: str = None, deviceTag: str = None, quantity: int = None, ssidName: str = None, usageUplink: str = None, t0: str = None, t1: str = None, timespan: float = None):
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'networkTag', 'deviceTag', 'quantity', 'ssidName', 'usageUplink', 't0', 't1', 'timespan'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationSummaryTopDevicesByUsage')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSummaryTopDevicesModelsByUsage')
def getOrganizationSummaryTopDevicesModelsByUsage(organizationId: str, networkTag: str = None, deviceTag: str = None, quantity: int = None, ssidName: str = None, usageUplink: str = None, t0: str = None, t1: str = None, timespan: float = None):
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'networkTag', 'deviceTag', 'quantity', 'ssidName', 'usageUplink', 't0', 't1', 'timespan'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationSummaryTopDevicesModelsByUsage')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSummaryTopNetworksByStatus')
def getOrganizationSummaryTopNetworksByStatus(organizationId: str, networkTag: str = None, deviceTag: str = None, quantity: int = None, ssidName: str = None, usageUplink: str = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'networkTag', 'deviceTag', 'quantity', 'ssidName', 'usageUplink', 'perPage', 'startingAfter', 'endingBefore'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationSummaryTopNetworksByStatus')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSummaryTopSsidsByUsage')
def getOrganizationSummaryTopSsidsByUsage(organizationId: str, networkTag: str = None, deviceTag: str = None, quantity: int = None, ssidName: str = None, usageUplink: str = None, t0: str = None, t1: str = None, timespan: float = None):
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'networkTag', 'deviceTag', 'quantity', 'ssidName', 'usageUplink', 't0', 't1', 'timespan'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationSummaryTopSsidsByUsage')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSummaryTopSwitchesByEnergyUsage')
def getOrganizationSummaryTopSwitchesByEnergyUsage(organizationId: str, networkTag: str = None, deviceTag: str = None, quantity: int = None, ssidName: str = None, usageUplink: str = None, t0: str = None, t1: str = None, timespan: float = None):
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'networkTag', 'deviceTag', 'quantity', 'ssidName', 'usageUplink', 't0', 't1', 'timespan'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationSummaryTopSwitchesByEnergyUsage')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSwitchPortsBySwitch')
def getOrganizationSwitchPortsBySwitch(organizationId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None, configurationUpdatedAfter: str = None, mac: str = None, macs: list = None, name: str = None, networkIds: list = None, portProfileIds: list = None, serial: str = None, serials: list = None):
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'configurationUpdatedAfter', 'mac', 'macs', 'name', 'networkIds', 'portProfileIds', 'serial', 'serials'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationSwitchPortsBySwitch')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSwitchPortsClientsOverviewByDevice')
def getOrganizationSwitchPortsClientsOverviewByDevice(organizationId: str, t0: str = None, timespan: float = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None, configurationUpdatedAfter: str = None, mac: str = None, macs: list = None, name: str = None, networkIds: list = None, portProfileIds: list = None, serial: str = None, serials: list = None):
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 't0', 'timespan', 'perPage', 'startingAfter', 'endingBefore', 'configurationUpdatedAfter', 'mac', 'macs', 'name', 'networkIds', 'portProfileIds', 'serial', 'serials'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationSwitchPortsClientsOverviewByDevice')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSwitchPortsOverview')
def getOrganizationSwitchPortsOverview(organizationId: str, t0: str = None, t1: str = None, timespan: float = None):
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 't0', 't1', 'timespan'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationSwitchPortsOverview')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSwitchPortsStatusesBySwitch')
def getOrganizationSwitchPortsStatusesBySwitch(organizationId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None, configurationUpdatedAfter: str = None, mac: str = None, macs: list = None, name: str = None, networkIds: list = None, portProfileIds: list = None, serial: str = None, serials: list = None):
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'configurationUpdatedAfter', 'mac', 'macs', 'name', 'networkIds', 'portProfileIds', 'serial', 'serials'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationSwitchPortsStatusesBySwitch')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSwitchPortsTopologyDiscoveryByDevice')
def getOrganizationSwitchPortsTopologyDiscoveryByDevice(organizationId: str, t0: str = None, timespan: float = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None, configurationUpdatedAfter: str = None, mac: str = None, macs: list = None, name: str = None, networkIds: list = None, portProfileIds: list = None, serial: str = None, serials: list = None):
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 't0', 'timespan', 'perPage', 'startingAfter', 'endingBefore', 'configurationUpdatedAfter', 'mac', 'macs', 'name', 'networkIds', 'portProfileIds', 'serial', 'serials'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationSwitchPortsTopologyDiscoveryByDevice')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationUplinksStatuses')
def getOrganizationUplinksStatuses(organizationId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None, networkIds: list = None, serials: list = None, iccids: list = None):
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'networkIds', 'serials', 'iccids'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationUplinksStatuses')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationWebhooksAlertTypes')
def getOrganizationWebhooksAlertTypes(organizationId: str, productType: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if productType is not None:
        final_kwargs['productType'] = productType

    # No body parameter for this function.
    body_payload = None

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'productType'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationWebhooksAlertTypes')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationWebhooksCallbacksStatus')
def getOrganizationWebhooksCallbacksStatus(organizationId: str, callbackId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if callbackId is not None:
        final_kwargs['callbackId'] = callbackId

    # No body parameter for this function.
    body_payload = None

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'callbackId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationWebhooksCallbacksStatus')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationWebhooksLogs')
def getOrganizationWebhooksLogs(organizationId: str, t0: str = None, t1: str = None, timespan: float = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None, url: str = None):
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 't0', 't1', 'timespan', 'perPage', 'startingAfter', 'endingBefore', 'url'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationWebhooksLogs')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationWirelessAirMarshalRules')
def getOrganizationWirelessAirMarshalRules(organizationId: str, networkIds: list = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'networkIds', 'perPage', 'startingAfter', 'endingBefore'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationWirelessAirMarshalRules')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationWirelessAirMarshalSettingsByNetwork')
def getOrganizationWirelessAirMarshalSettingsByNetwork(organizationId: str, networkIds: list = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'networkIds', 'perPage', 'startingAfter', 'endingBefore'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationWirelessAirMarshalSettingsByNetwork')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationWirelessClientsOverviewByDevice')
def getOrganizationWirelessClientsOverviewByDevice(organizationId: str, networkIds: list = None, serials: list = None, campusGatewayClusterIds: list = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'networkIds', 'serials', 'campusGatewayClusterIds', 'perPage', 'startingAfter', 'endingBefore'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationWirelessClientsOverviewByDevice')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationWirelessDevicesChannelUtilizationByDevice')
def getOrganizationWirelessDevicesChannelUtilizationByDevice(organizationId: str, networkIds: list = None, serials: list = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None, t0: str = None, t1: str = None, timespan: float = None, interval: int = None):
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'networkIds', 'serials', 'perPage', 'startingAfter', 'endingBefore', 't0', 't1', 'timespan', 'interval'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationWirelessDevicesChannelUtilizationByDevice')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationWirelessDevicesChannelUtilizationByNetwork')
def getOrganizationWirelessDevicesChannelUtilizationByNetwork(organizationId: str, networkIds: list = None, serials: list = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None, t0: str = None, t1: str = None, timespan: float = None, interval: int = None):
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'networkIds', 'serials', 'perPage', 'startingAfter', 'endingBefore', 't0', 't1', 'timespan', 'interval'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationWirelessDevicesChannelUtilizationByNetwork')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationWirelessDevicesChannelUtilizationHistoryByDeviceB')
def getOrganizationWirelessDevicesChannelUtilizationHistoryByDeviceB(organizationId: str, networkIds: list = None, serials: list = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None, t0: str = None, t1: str = None, timespan: float = None, interval: int = None):
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'networkIds', 'serials', 'perPage', 'startingAfter', 'endingBefore', 't0', 't1', 'timespan', 'interval'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationWirelessDevicesChannelUtilizationHistoryByDeviceB')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationWirelessDevicesChannelUtilizationHistoryByNetwork')
def getOrganizationWirelessDevicesChannelUtilizationHistoryByNetwork(organizationId: str, networkIds: list = None, serials: list = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None, t0: str = None, t1: str = None, timespan: float = None, interval: int = None):
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'networkIds', 'serials', 'perPage', 'startingAfter', 'endingBefore', 't0', 't1', 'timespan', 'interval'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationWirelessDevicesChannelUtilizationHistoryByNetwork')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationWirelessDevicesEthernetStatuses')
def getOrganizationWirelessDevicesEthernetStatuses(organizationId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None, networkIds: list = None):
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'networkIds'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationWirelessDevicesEthernetStatuses')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationWirelessDevicesPacketLossByClient')
def getOrganizationWirelessDevicesPacketLossByClient(organizationId: str, networkIds: list = None, ssids: list = None, bands: list = None, macs: list = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None, t0: str = None, t1: str = None, timespan: float = None):
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'networkIds', 'ssids', 'bands', 'macs', 'perPage', 'startingAfter', 'endingBefore', 't0', 't1', 'timespan'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationWirelessDevicesPacketLossByClient')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationWirelessDevicesPacketLossByDevice')
def getOrganizationWirelessDevicesPacketLossByDevice(organizationId: str, networkIds: list = None, serials: list = None, ssids: list = None, bands: list = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None, t0: str = None, t1: str = None, timespan: float = None):
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'networkIds', 'serials', 'ssids', 'bands', 'perPage', 'startingAfter', 'endingBefore', 't0', 't1', 'timespan'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationWirelessDevicesPacketLossByDevice')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationWirelessDevicesPacketLossByNetwork')
def getOrganizationWirelessDevicesPacketLossByNetwork(organizationId: str, networkIds: list = None, serials: list = None, ssids: list = None, bands: list = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None, t0: str = None, t1: str = None, timespan: float = None):
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'networkIds', 'serials', 'ssids', 'bands', 'perPage', 'startingAfter', 'endingBefore', 't0', 't1', 'timespan'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationWirelessDevicesPacketLossByNetwork')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationWirelessDevicesWirelessControllersByDevice')
def getOrganizationWirelessDevicesWirelessControllersByDevice(organizationId: str, networkIds: list = None, serials: list = None, controllerSerials: list = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'networkIds', 'serials', 'controllerSerials', 'perPage', 'startingAfter', 'endingBefore'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationWirelessDevicesWirelessControllersByDevice')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationWirelessRfProfilesAssignmentsByDevice')
def getOrganizationWirelessRfProfilesAssignmentsByDevice(organizationId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None, networkIds: list = None, productTypes: list = None, name: str = None, mac: str = None, serial: str = None, model: str = None, macs: list = None, serials: list = None, models: list = None):
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'networkIds', 'productTypes', 'name', 'mac', 'serial', 'model', 'macs', 'serials', 'models'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationWirelessRfProfilesAssignmentsByDevice')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationWirelessSsidsStatusesByDevice')
def getOrganizationWirelessSsidsStatusesByDevice(organizationId: str, networkIds: list = None, serials: list = None, bssids: list = None, hideDisabled: bool = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'networkIds', 'serials', 'bssids', 'hideDisabled', 'perPage', 'startingAfter', 'endingBefore'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationWirelessSsidsStatusesByDevice')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationWirelessControllerAvailabilitiesChangeHistory')
def getOrganizationWirelessControllerAvailabilitiesChangeHistory(organizationId: str, serials: list = None, t0: str = None, t1: str = None, timespan: float = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if serials is not None:
        final_kwargs['serials'] = serials
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'serials', 't0', 't1', 'timespan', 'perPage', 'startingAfter', 'endingBefore'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationWirelessControllerAvailabilitiesChangeHistory')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationWirelessControllerClientsOverviewHistoryByDeviceB')
def getOrganizationWirelessControllerClientsOverviewHistoryByDeviceB(organizationId: str, networkIds: list = None, serials: list = None, t0: str = None, t1: str = None, timespan: float = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None, resolution: int = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if networkIds is not None:
        final_kwargs['networkIds'] = networkIds
    if serials is not None:
        final_kwargs['serials'] = serials
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
    if resolution is not None:
        final_kwargs['resolution'] = resolution

    # No body parameter for this function.
    body_payload = None

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'networkIds', 'serials', 't0', 't1', 'timespan', 'perPage', 'startingAfter', 'endingBefore', 'resolution'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationWirelessControllerClientsOverviewHistoryByDeviceB')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationWirelessControllerConnections')
def getOrganizationWirelessControllerConnections(organizationId: str, networkIds: list = None, controllerSerials: list = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if networkIds is not None:
        final_kwargs['networkIds'] = networkIds
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'networkIds', 'controllerSerials', 'perPage', 'startingAfter', 'endingBefore'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationWirelessControllerConnections')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationWirelessControllerDevicesInterfacesL2ByDevice')
def getOrganizationWirelessControllerDevicesInterfacesL2ByDevice(organizationId: str, serials: list = None, t0: str = None, t1: str = None, timespan: float = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if serials is not None:
        final_kwargs['serials'] = serials
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'serials', 't0', 't1', 'timespan', 'perPage', 'startingAfter', 'endingBefore'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationWirelessControllerDevicesInterfacesL2ByDevice')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationWirelessControllerDevicesInterfacesL2StatusesChan')
def getOrganizationWirelessControllerDevicesInterfacesL2StatusesChan(organizationId: str, serials: list = None, includeInterfacesWithoutChanges: bool = None, t0: str = None, t1: str = None, timespan: float = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if serials is not None:
        final_kwargs['serials'] = serials
    if includeInterfacesWithoutChanges is not None:
        final_kwargs['includeInterfacesWithoutChanges'] = includeInterfacesWithoutChanges
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'serials', 'includeInterfacesWithoutChanges', 't0', 't1', 'timespan', 'perPage', 'startingAfter', 'endingBefore'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationWirelessControllerDevicesInterfacesL2StatusesChan')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationWirelessControllerDevicesInterfacesL2UsageHistory')
def getOrganizationWirelessControllerDevicesInterfacesL2UsageHistory(organizationId: str, serials: list = None, t0: str = None, t1: str = None, timespan: float = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if serials is not None:
        final_kwargs['serials'] = serials
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'serials', 't0', 't1', 'timespan', 'perPage', 'startingAfter', 'endingBefore'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationWirelessControllerDevicesInterfacesL2UsageHistory')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationWirelessControllerDevicesInterfacesL3ByDevice')
def getOrganizationWirelessControllerDevicesInterfacesL3ByDevice(organizationId: str, serials: list = None, t0: str = None, t1: str = None, timespan: float = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if serials is not None:
        final_kwargs['serials'] = serials
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'serials', 't0', 't1', 'timespan', 'perPage', 'startingAfter', 'endingBefore'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationWirelessControllerDevicesInterfacesL3ByDevice')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationWirelessControllerDevicesInterfacesL3StatusesChan')
def getOrganizationWirelessControllerDevicesInterfacesL3StatusesChan(organizationId: str, serials: list = None, includeInterfacesWithoutChanges: bool = None, t0: str = None, t1: str = None, timespan: float = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if serials is not None:
        final_kwargs['serials'] = serials
    if includeInterfacesWithoutChanges is not None:
        final_kwargs['includeInterfacesWithoutChanges'] = includeInterfacesWithoutChanges
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'serials', 'includeInterfacesWithoutChanges', 't0', 't1', 'timespan', 'perPage', 'startingAfter', 'endingBefore'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationWirelessControllerDevicesInterfacesL3StatusesChan')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationWirelessControllerDevicesInterfacesL3UsageHistory')
def getOrganizationWirelessControllerDevicesInterfacesL3UsageHistory(organizationId: str, serials: list = None, t0: str = None, t1: str = None, timespan: float = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if serials is not None:
        final_kwargs['serials'] = serials
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'serials', 't0', 't1', 'timespan', 'perPage', 'startingAfter', 'endingBefore'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationWirelessControllerDevicesInterfacesL3UsageHistory')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationWirelessControllerDevicesInterfacesPacketsOvervie')
def getOrganizationWirelessControllerDevicesInterfacesPacketsOvervie(organizationId: str, serials: list = None, names: list = None, t0: str = None, t1: str = None, timespan: float = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if serials is not None:
        final_kwargs['serials'] = serials
    if names is not None:
        final_kwargs['names'] = names
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'serials', 'names', 't0', 't1', 'timespan', 'perPage', 'startingAfter', 'endingBefore'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationWirelessControllerDevicesInterfacesPacketsOvervie')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationWirelessControllerDevicesInterfacesUsageHistoryBy')
def getOrganizationWirelessControllerDevicesInterfacesUsageHistoryBy(organizationId: str, serials: list = None, names: list = None, t0: str = None, t1: str = None, timespan: float = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if serials is not None:
        final_kwargs['serials'] = serials
    if names is not None:
        final_kwargs['names'] = names
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'serials', 'names', 't0', 't1', 'timespan', 'perPage', 'startingAfter', 'endingBefore'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationWirelessControllerDevicesInterfacesUsageHistoryBy')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationWirelessControllerDevicesRedundancyFailoverHistor')
def getOrganizationWirelessControllerDevicesRedundancyFailoverHistor(organizationId: str, serials: list = None, t0: str = None, t1: str = None, timespan: float = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if serials is not None:
        final_kwargs['serials'] = serials
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'serials', 't0', 't1', 'timespan', 'perPage', 'startingAfter', 'endingBefore'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationWirelessControllerDevicesRedundancyFailoverHistor')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationWirelessControllerDevicesRedundancyStatuses')
def getOrganizationWirelessControllerDevicesRedundancyStatuses(organizationId: str, serials: list = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if serials is not None:
        final_kwargs['serials'] = serials
    if perPage is not None:
        final_kwargs['perPage'] = perPage
    if startingAfter is not None:
        final_kwargs['startingAfter'] = startingAfter
    if endingBefore is not None:
        final_kwargs['endingBefore'] = endingBefore

    # No body parameter for this function.
    body_payload = None

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'serials', 'perPage', 'startingAfter', 'endingBefore'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationWirelessControllerDevicesRedundancyStatuses')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationWirelessControllerDevicesSystemUtilizationHistory')
def getOrganizationWirelessControllerDevicesSystemUtilizationHistory(organizationId: str, serials: list = None, t0: str = None, t1: str = None, timespan: float = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if organizationId is not None:
        final_kwargs['organizationId'] = organizationId
    if serials is not None:
        final_kwargs['serials'] = serials
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

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'serials', 't0', 't1', 'timespan', 'perPage', 'startingAfter', 'endingBefore'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationWirelessControllerDevicesSystemUtilizationHistory')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationWirelessControllerOverviewByDevice')
def getOrganizationWirelessControllerOverviewByDevice(organizationId: str, networkIds: list = None, serials: list = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
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

    # No body parameter for this function.
    body_payload = None

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'networkIds', 'serials', 'perPage', 'startingAfter', 'endingBefore'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    client = MerakiClient()
    target = getattr(client, 'getOrganizationWirelessControllerOverviewByDevice')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)
