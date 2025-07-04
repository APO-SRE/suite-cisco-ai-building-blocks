# app/llm/function_dispatcher/meraki_dispatcher.py
import os
from typing import Any
from app.llm.function_dispatcher import register
from app.llm.platform_clients.meraki_client import MerakiClient

@register('getAdministeredIdentitiesMe')
def getAdministeredIdentitiesMe():
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in [] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getAdministeredIdentitiesMe')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getAdministeredIdentitiesMeApiKeys')
def getAdministeredIdentitiesMeApiKeys():
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in [] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getAdministeredIdentitiesMeApiKeys')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getAdministeredLicensingSubscriptionEntitlements')
def getAdministeredLicensingSubscriptionEntitlements(skus: list = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'skus': 'skus'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['skus'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getAdministeredLicensingSubscriptionEntitlements')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getAdministeredLicensingSubscriptionSubscriptions')
def getAdministeredLicensingSubscriptionSubscriptions(perPage: int = None, startingAfter: str = None, endingBefore: str = None, subscriptionIds: list = None, organizationIds: list = None, statuses: list = None, productTypes: list = None, name: str = None, startDate: str = None, endDate: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore', 'subscriptionIds': 'subscriptionIds', 'organizationIds': 'organizationIds', 'statuses': 'statuses', 'productTypes': 'productTypes', 'name': 'name', 'startDate': 'startDate', 'endDate': 'endDate'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['perPage', 'startingAfter', 'endingBefore', 'subscriptionIds', 'organizationIds', 'statuses', 'productTypes', 'name', 'startDate', 'endDate'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getAdministeredLicensingSubscriptionSubscriptions')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getAdministeredLicensingSubscriptionSubscriptionsComplianceStatu')
def getAdministeredLicensingSubscriptionSubscriptionsComplianceStatu(organizationIds: list, subscriptionIds: list = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationIds': 'organizationIds', 'subscriptionIds': 'subscriptionIds'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationIds', 'subscriptionIds'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getAdministeredLicensingSubscriptionSubscriptionsComplianceStatu')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDevice')
def getDevice(serial: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'serial': 'serial'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getDevice')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceApplianceDhcpSubnets')
def getDeviceApplianceDhcpSubnets(serial: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'serial': 'serial'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getDeviceApplianceDhcpSubnets')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceAppliancePerformance')
def getDeviceAppliancePerformance(serial: str, t0: str = None, t1: str = None, timespan: float = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'serial': 'serial', 't0': 't0', 't1': 't1', 'timespan': 'timespan'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial', 't0', 't1', 'timespan'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getDeviceAppliancePerformance')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceAppliancePrefixesDelegated')
def getDeviceAppliancePrefixesDelegated(serial: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'serial': 'serial'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getDeviceAppliancePrefixesDelegated')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceAppliancePrefixesDelegatedVlanAssignments')
def getDeviceAppliancePrefixesDelegatedVlanAssignments(serial: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'serial': 'serial'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getDeviceAppliancePrefixesDelegatedVlanAssignments')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceApplianceRadioSettings')
def getDeviceApplianceRadioSettings(serial: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'serial': 'serial'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getDeviceApplianceRadioSettings')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceApplianceUplinksSettings')
def getDeviceApplianceUplinksSettings(serial: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'serial': 'serial'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getDeviceApplianceUplinksSettings')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceCameraAnalyticsLive')
def getDeviceCameraAnalyticsLive(serial: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'serial': 'serial'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getDeviceCameraAnalyticsLive')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceCameraAnalyticsOverview')
def getDeviceCameraAnalyticsOverview(serial: str, t0: str = None, t1: str = None, timespan: float = None, objectType: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'serial': 'serial', 't0': 't0', 't1': 't1', 'timespan': 'timespan', 'objectType': 'objectType'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial', 't0', 't1', 'timespan', 'objectType'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getDeviceCameraAnalyticsOverview')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceCameraAnalyticsRecent')
def getDeviceCameraAnalyticsRecent(serial: str, objectType: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'serial': 'serial', 'objectType': 'objectType'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial', 'objectType'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getDeviceCameraAnalyticsRecent')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceCameraAnalyticsZones')
def getDeviceCameraAnalyticsZones(serial: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'serial': 'serial'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getDeviceCameraAnalyticsZones')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceCameraAnalyticsZoneHistory')
def getDeviceCameraAnalyticsZoneHistory(serial: str, zoneId: str, t0: str = None, t1: str = None, timespan: float = None, resolution: int = None, objectType: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'serial': 'serial', 'zoneId': 'zoneId', 't0': 't0', 't1': 't1', 'timespan': 'timespan', 'resolution': 'resolution', 'objectType': 'objectType'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial', 'zoneId', 't0', 't1', 'timespan', 'resolution', 'objectType'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getDeviceCameraAnalyticsZoneHistory')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceCameraCustomAnalytics')
def getDeviceCameraCustomAnalytics(serial: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'serial': 'serial'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getDeviceCameraCustomAnalytics')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceCameraQualityAndRetention')
def getDeviceCameraQualityAndRetention(serial: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'serial': 'serial'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getDeviceCameraQualityAndRetention')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceCameraSense')
def getDeviceCameraSense(serial: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'serial': 'serial'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getDeviceCameraSense')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceCameraSenseObjectDetectionModels')
def getDeviceCameraSenseObjectDetectionModels(serial: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'serial': 'serial'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getDeviceCameraSenseObjectDetectionModels')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceCameraVideoSettings')
def getDeviceCameraVideoSettings(serial: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'serial': 'serial'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getDeviceCameraVideoSettings')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceCameraVideoLink')
def getDeviceCameraVideoLink(serial: str, timestamp: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'serial': 'serial', 'timestamp': 'timestamp'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial', 'timestamp'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getDeviceCameraVideoLink')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceCameraWirelessProfiles')
def getDeviceCameraWirelessProfiles(serial: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'serial': 'serial'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getDeviceCameraWirelessProfiles')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceCellularSims')
def getDeviceCellularSims(serial: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'serial': 'serial'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getDeviceCellularSims')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceCellularGatewayLan')
def getDeviceCellularGatewayLan(serial: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'serial': 'serial'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getDeviceCellularGatewayLan')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceCellularGatewayPortForwardingRules')
def getDeviceCellularGatewayPortForwardingRules(serial: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'serial': 'serial'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getDeviceCellularGatewayPortForwardingRules')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceClients')
def getDeviceClients(serial: str, t0: str = None, timespan: float = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'serial': 'serial', 't0': 't0', 'timespan': 'timespan'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial', 't0', 'timespan'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getDeviceClients')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceLiveToolsArpTable')
def getDeviceLiveToolsArpTable(serial: str, arpTableId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'serial': 'serial', 'arpTableId': 'arpTableId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial', 'arpTableId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getDeviceLiveToolsArpTable')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceLiveToolsCableTest')
def getDeviceLiveToolsCableTest(serial: str, id: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'serial': 'serial', 'id': 'id'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial', 'id'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getDeviceLiveToolsCableTest')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceLiveToolsLedsBlink')
def getDeviceLiveToolsLedsBlink(serial: str, ledsBlinkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'serial': 'serial', 'ledsBlinkId': 'ledsBlinkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial', 'ledsBlinkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getDeviceLiveToolsLedsBlink')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceLiveToolsPing')
def getDeviceLiveToolsPing(serial: str, id: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'serial': 'serial', 'id': 'id'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial', 'id'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getDeviceLiveToolsPing')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceLiveToolsPingDevice')
def getDeviceLiveToolsPingDevice(serial: str, id: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'serial': 'serial', 'id': 'id'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial', 'id'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getDeviceLiveToolsPingDevice')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceLiveToolsThroughputTest')
def getDeviceLiveToolsThroughputTest(serial: str, throughputTestId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'serial': 'serial', 'throughputTestId': 'throughputTestId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial', 'throughputTestId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getDeviceLiveToolsThroughputTest')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceLiveToolsWakeOnLan')
def getDeviceLiveToolsWakeOnLan(serial: str, wakeOnLanId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'serial': 'serial', 'wakeOnLanId': 'wakeOnLanId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial', 'wakeOnLanId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getDeviceLiveToolsWakeOnLan')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceLldpCdp')
def getDeviceLldpCdp(serial: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'serial': 'serial'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getDeviceLldpCdp')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceLossAndLatencyHistory')
def getDeviceLossAndLatencyHistory(serial: str, ip: str, t0: str = None, t1: str = None, timespan: float = None, resolution: int = None, uplink: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'serial': 'serial', 't0': 't0', 't1': 't1', 'timespan': 'timespan', 'resolution': 'resolution', 'uplink': 'uplink', 'ip': 'ip'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial', 't0', 't1', 'timespan', 'resolution', 'uplink', 'ip'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getDeviceLossAndLatencyHistory')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceManagementInterface')
def getDeviceManagementInterface(serial: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'serial': 'serial'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getDeviceManagementInterface')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceSensorCommands')
def getDeviceSensorCommands(serial: str, operations: list = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None, sortOrder: str = None, t0: str = None, t1: str = None, timespan: float = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'serial': 'serial', 'operations': 'operations', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore', 'sortOrder': 'sortOrder', 't0': 't0', 't1': 't1', 'timespan': 'timespan'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial', 'operations', 'perPage', 'startingAfter', 'endingBefore', 'sortOrder', 't0', 't1', 'timespan'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getDeviceSensorCommands')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceSensorCommand')
def getDeviceSensorCommand(serial: str, commandId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'serial': 'serial', 'commandId': 'commandId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial', 'commandId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getDeviceSensorCommand')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceSensorRelationships')
def getDeviceSensorRelationships(serial: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'serial': 'serial'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getDeviceSensorRelationships')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceSwitchPorts')
def getDeviceSwitchPorts(serial: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'serial': 'serial'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getDeviceSwitchPorts')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceSwitchPortsStatuses')
def getDeviceSwitchPortsStatuses(serial: str, t0: str = None, timespan: float = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'serial': 'serial', 't0': 't0', 'timespan': 'timespan'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial', 't0', 'timespan'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getDeviceSwitchPortsStatuses')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceSwitchPortsStatusesPackets')
def getDeviceSwitchPortsStatusesPackets(serial: str, t0: str = None, timespan: float = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'serial': 'serial', 't0': 't0', 'timespan': 'timespan'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial', 't0', 'timespan'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getDeviceSwitchPortsStatusesPackets')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceSwitchPort')
def getDeviceSwitchPort(serial: str, portId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'serial': 'serial', 'portId': 'portId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial', 'portId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getDeviceSwitchPort')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceSwitchRoutingInterfaces')
def getDeviceSwitchRoutingInterfaces(serial: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'serial': 'serial'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getDeviceSwitchRoutingInterfaces')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceSwitchRoutingInterface')
def getDeviceSwitchRoutingInterface(serial: str, interfaceId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'serial': 'serial', 'interfaceId': 'interfaceId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial', 'interfaceId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getDeviceSwitchRoutingInterface')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceSwitchRoutingInterfaceDhcp')
def getDeviceSwitchRoutingInterfaceDhcp(serial: str, interfaceId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'serial': 'serial', 'interfaceId': 'interfaceId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial', 'interfaceId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getDeviceSwitchRoutingInterfaceDhcp')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceSwitchRoutingStaticRoutes')
def getDeviceSwitchRoutingStaticRoutes(serial: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'serial': 'serial'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getDeviceSwitchRoutingStaticRoutes')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceSwitchRoutingStaticRoute')
def getDeviceSwitchRoutingStaticRoute(serial: str, staticRouteId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'serial': 'serial', 'staticRouteId': 'staticRouteId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial', 'staticRouteId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getDeviceSwitchRoutingStaticRoute')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceSwitchWarmSpare')
def getDeviceSwitchWarmSpare(serial: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'serial': 'serial'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getDeviceSwitchWarmSpare')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceWirelessBluetoothSettings')
def getDeviceWirelessBluetoothSettings(serial: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'serial': 'serial'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getDeviceWirelessBluetoothSettings')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceWirelessConnectionStats')
def getDeviceWirelessConnectionStats(serial: str, t0: str = None, t1: str = None, timespan: float = None, band: str = None, ssid: int = None, vlan: int = None, apTag: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'serial': 'serial', 't0': 't0', 't1': 't1', 'timespan': 'timespan', 'band': 'band', 'ssid': 'ssid', 'vlan': 'vlan', 'apTag': 'apTag'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial', 't0', 't1', 'timespan', 'band', 'ssid', 'vlan', 'apTag'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getDeviceWirelessConnectionStats')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceWirelessElectronicShelfLabel')
def getDeviceWirelessElectronicShelfLabel(serial: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'serial': 'serial'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getDeviceWirelessElectronicShelfLabel')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceWirelessLatencyStats')
def getDeviceWirelessLatencyStats(serial: str, t0: str = None, t1: str = None, timespan: float = None, band: str = None, ssid: int = None, vlan: int = None, apTag: str = None, fields: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'serial': 'serial', 't0': 't0', 't1': 't1', 'timespan': 'timespan', 'band': 'band', 'ssid': 'ssid', 'vlan': 'vlan', 'apTag': 'apTag', 'fields': 'fields'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial', 't0', 't1', 'timespan', 'band', 'ssid', 'vlan', 'apTag', 'fields'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getDeviceWirelessLatencyStats')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceWirelessRadioSettings')
def getDeviceWirelessRadioSettings(serial: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'serial': 'serial'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getDeviceWirelessRadioSettings')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceWirelessStatus')
def getDeviceWirelessStatus(serial: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'serial': 'serial'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['serial'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getDeviceWirelessStatus')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetwork')
def getNetwork(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetwork')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkAlertsHistory')
def getNetworkAlertsHistory(networkId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'perPage', 'startingAfter', 'endingBefore'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkAlertsHistory')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkAlertsSettings')
def getNetworkAlertsSettings(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkAlertsSettings')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkApplianceClientSecurityEvents')
def getNetworkApplianceClientSecurityEvents(networkId: str, clientId: str, t0: str = None, t1: str = None, timespan: float = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None, sortOrder: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'clientId': 'clientId', 't0': 't0', 't1': 't1', 'timespan': 'timespan', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore', 'sortOrder': 'sortOrder'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'clientId', 't0', 't1', 'timespan', 'perPage', 'startingAfter', 'endingBefore', 'sortOrder'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkApplianceClientSecurityEvents')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkApplianceConnectivityMonitoringDestinations')
def getNetworkApplianceConnectivityMonitoringDestinations(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkApplianceConnectivityMonitoringDestinations')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkApplianceContentFiltering')
def getNetworkApplianceContentFiltering(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkApplianceContentFiltering')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkApplianceContentFilteringCategories')
def getNetworkApplianceContentFilteringCategories(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkApplianceContentFilteringCategories')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkApplianceFirewallCellularFirewallRules')
def getNetworkApplianceFirewallCellularFirewallRules(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkApplianceFirewallCellularFirewallRules')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkApplianceFirewallFirewalledServices')
def getNetworkApplianceFirewallFirewalledServices(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkApplianceFirewallFirewalledServices')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkApplianceFirewallFirewalledService')
def getNetworkApplianceFirewallFirewalledService(networkId: str, service: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'service': 'service'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'service'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkApplianceFirewallFirewalledService')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkApplianceFirewallInboundCellularFirewallRules')
def getNetworkApplianceFirewallInboundCellularFirewallRules(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkApplianceFirewallInboundCellularFirewallRules')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkApplianceFirewallInboundFirewallRules')
def getNetworkApplianceFirewallInboundFirewallRules(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkApplianceFirewallInboundFirewallRules')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkApplianceFirewallL3FirewallRules')
def getNetworkApplianceFirewallL3FirewallRules(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkApplianceFirewallL3FirewallRules')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkApplianceFirewallL7FirewallRules')
def getNetworkApplianceFirewallL7FirewallRules(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkApplianceFirewallL7FirewallRules')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkApplianceFirewallL7FirewallRulesApplicationCategories')
def getNetworkApplianceFirewallL7FirewallRulesApplicationCategories(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkApplianceFirewallL7FirewallRulesApplicationCategories')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkApplianceFirewallOneToManyNatRules')
def getNetworkApplianceFirewallOneToManyNatRules(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkApplianceFirewallOneToManyNatRules')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkApplianceFirewallOneToOneNatRules')
def getNetworkApplianceFirewallOneToOneNatRules(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkApplianceFirewallOneToOneNatRules')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkApplianceFirewallPortForwardingRules')
def getNetworkApplianceFirewallPortForwardingRules(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkApplianceFirewallPortForwardingRules')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkApplianceFirewallSettings')
def getNetworkApplianceFirewallSettings(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkApplianceFirewallSettings')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkAppliancePorts')
def getNetworkAppliancePorts(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkAppliancePorts')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkAppliancePort')
def getNetworkAppliancePort(networkId: str, portId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'portId': 'portId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'portId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkAppliancePort')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkAppliancePrefixesDelegatedStatics')
def getNetworkAppliancePrefixesDelegatedStatics(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkAppliancePrefixesDelegatedStatics')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkAppliancePrefixesDelegatedStatic')
def getNetworkAppliancePrefixesDelegatedStatic(networkId: str, staticDelegatedPrefixId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'staticDelegatedPrefixId': 'staticDelegatedPrefixId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'staticDelegatedPrefixId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkAppliancePrefixesDelegatedStatic')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkApplianceRfProfiles')
def getNetworkApplianceRfProfiles(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkApplianceRfProfiles')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkApplianceRfProfile')
def getNetworkApplianceRfProfile(networkId: str, rfProfileId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'rfProfileId': 'rfProfileId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'rfProfileId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkApplianceRfProfile')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkApplianceSecurityEvents')
def getNetworkApplianceSecurityEvents(networkId: str, t0: str = None, t1: str = None, timespan: float = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None, sortOrder: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 't0': 't0', 't1': 't1', 'timespan': 'timespan', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore', 'sortOrder': 'sortOrder'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 't0', 't1', 'timespan', 'perPage', 'startingAfter', 'endingBefore', 'sortOrder'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkApplianceSecurityEvents')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkApplianceSecurityIntrusion')
def getNetworkApplianceSecurityIntrusion(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkApplianceSecurityIntrusion')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkApplianceSecurityMalware')
def getNetworkApplianceSecurityMalware(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkApplianceSecurityMalware')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkApplianceSettings')
def getNetworkApplianceSettings(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkApplianceSettings')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkApplianceSingleLan')
def getNetworkApplianceSingleLan(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkApplianceSingleLan')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkApplianceSsids')
def getNetworkApplianceSsids(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkApplianceSsids')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkApplianceSsid')
def getNetworkApplianceSsid(networkId: str, number: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'number': 'number'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'number'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkApplianceSsid')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkApplianceStaticRoutes')
def getNetworkApplianceStaticRoutes(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkApplianceStaticRoutes')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkApplianceStaticRoute')
def getNetworkApplianceStaticRoute(networkId: str, staticRouteId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'staticRouteId': 'staticRouteId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'staticRouteId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkApplianceStaticRoute')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkApplianceTrafficShaping')
def getNetworkApplianceTrafficShaping(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkApplianceTrafficShaping')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkApplianceTrafficShapingCustomPerformanceClasses')
def getNetworkApplianceTrafficShapingCustomPerformanceClasses(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkApplianceTrafficShapingCustomPerformanceClasses')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkApplianceTrafficShapingCustomPerformanceClass')
def getNetworkApplianceTrafficShapingCustomPerformanceClass(networkId: str, customPerformanceClassId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'customPerformanceClassId': 'customPerformanceClassId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'customPerformanceClassId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkApplianceTrafficShapingCustomPerformanceClass')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkApplianceTrafficShapingRules')
def getNetworkApplianceTrafficShapingRules(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkApplianceTrafficShapingRules')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkApplianceTrafficShapingUplinkBandwidth')
def getNetworkApplianceTrafficShapingUplinkBandwidth(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkApplianceTrafficShapingUplinkBandwidth')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkApplianceTrafficShapingUplinkSelection')
def getNetworkApplianceTrafficShapingUplinkSelection(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkApplianceTrafficShapingUplinkSelection')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkApplianceUplinksUsageHistory')
def getNetworkApplianceUplinksUsageHistory(networkId: str, t0: str = None, t1: str = None, timespan: float = None, resolution: int = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 't0': 't0', 't1': 't1', 'timespan': 'timespan', 'resolution': 'resolution'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 't0', 't1', 'timespan', 'resolution'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkApplianceUplinksUsageHistory')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkApplianceVlans')
def getNetworkApplianceVlans(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkApplianceVlans')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkApplianceVlansSettings')
def getNetworkApplianceVlansSettings(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkApplianceVlansSettings')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkApplianceVlan')
def getNetworkApplianceVlan(networkId: str, vlanId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'vlanId': 'vlanId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'vlanId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkApplianceVlan')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkApplianceVpnBgp')
def getNetworkApplianceVpnBgp(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkApplianceVpnBgp')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkApplianceVpnSiteToSiteVpn')
def getNetworkApplianceVpnSiteToSiteVpn(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkApplianceVpnSiteToSiteVpn')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkApplianceWarmSpare')
def getNetworkApplianceWarmSpare(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkApplianceWarmSpare')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkBluetoothClients')
def getNetworkBluetoothClients(networkId: str, t0: str = None, timespan: float = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None, includeConnectivityHistory: bool = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 't0': 't0', 'timespan': 'timespan', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore', 'includeConnectivityHistory': 'includeConnectivityHistory'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 't0', 'timespan', 'perPage', 'startingAfter', 'endingBefore', 'includeConnectivityHistory'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkBluetoothClients')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkBluetoothClient')
def getNetworkBluetoothClient(networkId: str, bluetoothClientId: str, includeConnectivityHistory: bool = None, connectivityHistoryTimespan: int = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'bluetoothClientId': 'bluetoothClientId', 'includeConnectivityHistory': 'includeConnectivityHistory', 'connectivityHistoryTimespan': 'connectivityHistoryTimespan'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'bluetoothClientId', 'includeConnectivityHistory', 'connectivityHistoryTimespan'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkBluetoothClient')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkCameraQualityRetentionProfiles')
def getNetworkCameraQualityRetentionProfiles(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkCameraQualityRetentionProfiles')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkCameraQualityRetentionProfile')
def getNetworkCameraQualityRetentionProfile(networkId: str, qualityRetentionProfileId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'qualityRetentionProfileId': 'qualityRetentionProfileId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'qualityRetentionProfileId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkCameraQualityRetentionProfile')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkCameraSchedules')
def getNetworkCameraSchedules(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkCameraSchedules')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkCameraWirelessProfiles')
def getNetworkCameraWirelessProfiles(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkCameraWirelessProfiles')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkCameraWirelessProfile')
def getNetworkCameraWirelessProfile(networkId: str, wirelessProfileId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'wirelessProfileId': 'wirelessProfileId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'wirelessProfileId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkCameraWirelessProfile')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkCellularGatewayConnectivityMonitoringDestinations')
def getNetworkCellularGatewayConnectivityMonitoringDestinations(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkCellularGatewayConnectivityMonitoringDestinations')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkCellularGatewayDhcp')
def getNetworkCellularGatewayDhcp(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkCellularGatewayDhcp')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkCellularGatewaySubnetPool')
def getNetworkCellularGatewaySubnetPool(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkCellularGatewaySubnetPool')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkCellularGatewayUplink')
def getNetworkCellularGatewayUplink(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkCellularGatewayUplink')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkClients')
def getNetworkClients(networkId: str, t0: str = None, timespan: float = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None, statuses: list = None, ip: str = None, ip6: str = None, ip6Local: str = None, mac: str = None, os: str = None, pskGroup: str = None, description: str = None, vlan: str = None, namedVlan: str = None, recentDeviceConnections: list = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 't0': 't0', 'timespan': 'timespan', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore', 'statuses': 'statuses', 'ip': 'ip', 'ip6': 'ip6', 'ip6Local': 'ip6Local', 'mac': 'mac', 'os': 'os', 'pskGroup': 'pskGroup', 'description': 'description', 'vlan': 'vlan', 'namedVlan': 'namedVlan', 'recentDeviceConnections': 'recentDeviceConnections'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 't0', 'timespan', 'perPage', 'startingAfter', 'endingBefore', 'statuses', 'ip', 'ip6', 'ip6Local', 'mac', 'os', 'pskGroup', 'description', 'vlan', 'namedVlan', 'recentDeviceConnections'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkClients')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkClientsApplicationUsage')
def getNetworkClientsApplicationUsage(networkId: str, clients: str, ssidNumber: int = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None, t0: str = None, t1: str = None, timespan: float = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'clients': 'clients', 'ssidNumber': 'ssidNumber', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore', 't0': 't0', 't1': 't1', 'timespan': 'timespan'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'clients', 'ssidNumber', 'perPage', 'startingAfter', 'endingBefore', 't0', 't1', 'timespan'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkClientsApplicationUsage')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkClientsBandwidthUsageHistory')
def getNetworkClientsBandwidthUsageHistory(networkId: str, t0: str = None, t1: str = None, timespan: float = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 't0': 't0', 't1': 't1', 'timespan': 'timespan', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 't0', 't1', 'timespan', 'perPage', 'startingAfter', 'endingBefore'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkClientsBandwidthUsageHistory')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkClientsOverview')
def getNetworkClientsOverview(networkId: str, t0: str = None, t1: str = None, timespan: float = None, resolution: int = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 't0': 't0', 't1': 't1', 'timespan': 'timespan', 'resolution': 'resolution'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 't0', 't1', 'timespan', 'resolution'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkClientsOverview')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkClientsUsageHistories')
def getNetworkClientsUsageHistories(networkId: str, clients: str, ssidNumber: int = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None, t0: str = None, t1: str = None, timespan: float = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'clients': 'clients', 'ssidNumber': 'ssidNumber', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore', 't0': 't0', 't1': 't1', 'timespan': 'timespan'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'clients', 'ssidNumber', 'perPage', 'startingAfter', 'endingBefore', 't0', 't1', 'timespan'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkClientsUsageHistories')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkClient')
def getNetworkClient(networkId: str, clientId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'clientId': 'clientId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'clientId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkClient')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkClientPolicy')
def getNetworkClientPolicy(networkId: str, clientId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'clientId': 'clientId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'clientId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkClientPolicy')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkClientSplashAuthorizationStatus')
def getNetworkClientSplashAuthorizationStatus(networkId: str, clientId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'clientId': 'clientId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'clientId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkClientSplashAuthorizationStatus')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkClientTrafficHistory')
def getNetworkClientTrafficHistory(networkId: str, clientId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'clientId': 'clientId', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'clientId', 'perPage', 'startingAfter', 'endingBefore'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkClientTrafficHistory')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkClientUsageHistory')
def getNetworkClientUsageHistory(networkId: str, clientId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'clientId': 'clientId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'clientId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkClientUsageHistory')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkDevices')
def getNetworkDevices(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkDevices')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkEvents')
def getNetworkEvents(networkId: str, productType: str = None, includedEventTypes: list = None, excludedEventTypes: list = None, deviceMac: str = None, deviceSerial: str = None, deviceName: str = None, clientIp: str = None, clientMac: str = None, clientName: str = None, smDeviceMac: str = None, smDeviceName: str = None, eventDetails: str = None, eventSeverity: str = None, isCatalyst: bool = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'productType': 'productType', 'includedEventTypes': 'includedEventTypes', 'excludedEventTypes': 'excludedEventTypes', 'deviceMac': 'deviceMac', 'deviceSerial': 'deviceSerial', 'deviceName': 'deviceName', 'clientIp': 'clientIp', 'clientMac': 'clientMac', 'clientName': 'clientName', 'smDeviceMac': 'smDeviceMac', 'smDeviceName': 'smDeviceName', 'eventDetails': 'eventDetails', 'eventSeverity': 'eventSeverity', 'isCatalyst': 'isCatalyst', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'productType', 'includedEventTypes', 'excludedEventTypes', 'deviceMac', 'deviceSerial', 'deviceName', 'clientIp', 'clientMac', 'clientName', 'smDeviceMac', 'smDeviceName', 'eventDetails', 'eventSeverity', 'isCatalyst', 'perPage', 'startingAfter', 'endingBefore'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkEvents')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkEventsEventTypes')
def getNetworkEventsEventTypes(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkEventsEventTypes')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkFirmwareUpgrades')
def getNetworkFirmwareUpgrades(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkFirmwareUpgrades')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkFirmwareUpgradesStagedEvents')
def getNetworkFirmwareUpgradesStagedEvents(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkFirmwareUpgradesStagedEvents')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkFirmwareUpgradesStagedGroups')
def getNetworkFirmwareUpgradesStagedGroups(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkFirmwareUpgradesStagedGroups')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkFirmwareUpgradesStagedGroup')
def getNetworkFirmwareUpgradesStagedGroup(networkId: str, groupId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'groupId': 'groupId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'groupId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkFirmwareUpgradesStagedGroup')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkFirmwareUpgradesStagedStages')
def getNetworkFirmwareUpgradesStagedStages(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkFirmwareUpgradesStagedStages')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkFloorPlans')
def getNetworkFloorPlans(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkFloorPlans')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkFloorPlan')
def getNetworkFloorPlan(networkId: str, floorPlanId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'floorPlanId': 'floorPlanId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'floorPlanId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkFloorPlan')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkGroupPolicies')
def getNetworkGroupPolicies(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkGroupPolicies')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkGroupPolicy')
def getNetworkGroupPolicy(networkId: str, groupPolicyId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'groupPolicyId': 'groupPolicyId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'groupPolicyId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkGroupPolicy')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkHealthAlerts')
def getNetworkHealthAlerts(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkHealthAlerts')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkInsightApplicationHealthByTime')
def getNetworkInsightApplicationHealthByTime(networkId: str, applicationId: str, t0: str = None, t1: str = None, timespan: float = None, resolution: int = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'applicationId': 'applicationId', 't0': 't0', 't1': 't1', 'timespan': 'timespan', 'resolution': 'resolution'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'applicationId', 't0', 't1', 'timespan', 'resolution'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkInsightApplicationHealthByTime')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkMerakiAuthUsers')
def getNetworkMerakiAuthUsers(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkMerakiAuthUsers')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkMerakiAuthUser')
def getNetworkMerakiAuthUser(networkId: str, merakiAuthUserId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'merakiAuthUserId': 'merakiAuthUserId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'merakiAuthUserId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkMerakiAuthUser')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkMqttBrokers')
def getNetworkMqttBrokers(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkMqttBrokers')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkMqttBroker')
def getNetworkMqttBroker(networkId: str, mqttBrokerId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'mqttBrokerId': 'mqttBrokerId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'mqttBrokerId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkMqttBroker')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkNetflow')
def getNetworkNetflow(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkNetflow')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkNetworkHealthChannelUtilization')
def getNetworkNetworkHealthChannelUtilization(networkId: str, t0: str = None, t1: str = None, timespan: float = None, resolution: int = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 't0': 't0', 't1': 't1', 'timespan': 'timespan', 'resolution': 'resolution', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 't0', 't1', 'timespan', 'resolution', 'perPage', 'startingAfter', 'endingBefore'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkNetworkHealthChannelUtilization')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkPiiPiiKeys')
def getNetworkPiiPiiKeys(networkId: str, username: str = None, email: str = None, mac: str = None, serial: str = None, imei: str = None, bluetoothMac: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'username': 'username', 'email': 'email', 'mac': 'mac', 'serial': 'serial', 'imei': 'imei', 'bluetoothMac': 'bluetoothMac'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'username', 'email', 'mac', 'serial', 'imei', 'bluetoothMac'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkPiiPiiKeys')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkPiiRequests')
def getNetworkPiiRequests(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkPiiRequests')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkPiiRequest')
def getNetworkPiiRequest(networkId: str, requestId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'requestId': 'requestId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'requestId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkPiiRequest')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkPiiSmDevicesForKey')
def getNetworkPiiSmDevicesForKey(networkId: str, username: str = None, email: str = None, mac: str = None, serial: str = None, imei: str = None, bluetoothMac: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'username': 'username', 'email': 'email', 'mac': 'mac', 'serial': 'serial', 'imei': 'imei', 'bluetoothMac': 'bluetoothMac'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'username', 'email', 'mac', 'serial', 'imei', 'bluetoothMac'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkPiiSmDevicesForKey')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkPiiSmOwnersForKey')
def getNetworkPiiSmOwnersForKey(networkId: str, username: str = None, email: str = None, mac: str = None, serial: str = None, imei: str = None, bluetoothMac: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'username': 'username', 'email': 'email', 'mac': 'mac', 'serial': 'serial', 'imei': 'imei', 'bluetoothMac': 'bluetoothMac'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'username', 'email', 'mac', 'serial', 'imei', 'bluetoothMac'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkPiiSmOwnersForKey')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkPoliciesByClient')
def getNetworkPoliciesByClient(networkId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None, t0: str = None, timespan: float = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore', 't0': 't0', 'timespan': 'timespan'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'perPage', 'startingAfter', 'endingBefore', 't0', 'timespan'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkPoliciesByClient')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSensorAlertsCurrentOverviewByMetric')
def getNetworkSensorAlertsCurrentOverviewByMetric(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkSensorAlertsCurrentOverviewByMetric')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSensorAlertsOverviewByMetric')
def getNetworkSensorAlertsOverviewByMetric(networkId: str, t0: str = None, t1: str = None, timespan: float = None, interval: int = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 't0': 't0', 't1': 't1', 'timespan': 'timespan', 'interval': 'interval'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 't0', 't1', 'timespan', 'interval'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkSensorAlertsOverviewByMetric')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSensorAlertsProfiles')
def getNetworkSensorAlertsProfiles(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkSensorAlertsProfiles')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSensorAlertsProfile')
def getNetworkSensorAlertsProfile(networkId: str, id: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'id': 'id'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'id'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkSensorAlertsProfile')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSensorMqttBrokers')
def getNetworkSensorMqttBrokers(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkSensorMqttBrokers')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSensorMqttBroker')
def getNetworkSensorMqttBroker(networkId: str, mqttBrokerId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'mqttBrokerId': 'mqttBrokerId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'mqttBrokerId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkSensorMqttBroker')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSensorRelationships')
def getNetworkSensorRelationships(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkSensorRelationships')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSettings')
def getNetworkSettings(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkSettings')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSmBypassActivationLockAttempt')
def getNetworkSmBypassActivationLockAttempt(networkId: str, attemptId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'attemptId': 'attemptId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'attemptId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkSmBypassActivationLockAttempt')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSmDevices')
def getNetworkSmDevices(networkId: str, fields: list = None, wifiMacs: list = None, serials: list = None, ids: list = None, uuids: list = None, systemTypes: list = None, scope: list = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'fields': 'fields', 'wifiMacs': 'wifiMacs', 'serials': 'serials', 'ids': 'ids', 'uuids': 'uuids', 'systemTypes': 'systemTypes', 'scope': 'scope', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'fields', 'wifiMacs', 'serials', 'ids', 'uuids', 'systemTypes', 'scope', 'perPage', 'startingAfter', 'endingBefore'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkSmDevices')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSmDeviceCellularUsageHistory')
def getNetworkSmDeviceCellularUsageHistory(networkId: str, deviceId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'deviceId': 'deviceId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'deviceId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkSmDeviceCellularUsageHistory')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSmDeviceCerts')
def getNetworkSmDeviceCerts(networkId: str, deviceId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'deviceId': 'deviceId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'deviceId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkSmDeviceCerts')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSmDeviceConnectivity')
def getNetworkSmDeviceConnectivity(networkId: str, deviceId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'deviceId': 'deviceId', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'deviceId', 'perPage', 'startingAfter', 'endingBefore'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkSmDeviceConnectivity')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSmDeviceDesktopLogs')
def getNetworkSmDeviceDesktopLogs(networkId: str, deviceId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'deviceId': 'deviceId', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'deviceId', 'perPage', 'startingAfter', 'endingBefore'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkSmDeviceDesktopLogs')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSmDeviceDeviceCommandLogs')
def getNetworkSmDeviceDeviceCommandLogs(networkId: str, deviceId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'deviceId': 'deviceId', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'deviceId', 'perPage', 'startingAfter', 'endingBefore'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkSmDeviceDeviceCommandLogs')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSmDeviceDeviceProfiles')
def getNetworkSmDeviceDeviceProfiles(networkId: str, deviceId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'deviceId': 'deviceId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'deviceId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkSmDeviceDeviceProfiles')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSmDeviceNetworkAdapters')
def getNetworkSmDeviceNetworkAdapters(networkId: str, deviceId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'deviceId': 'deviceId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'deviceId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkSmDeviceNetworkAdapters')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSmDevicePerformanceHistory')
def getNetworkSmDevicePerformanceHistory(networkId: str, deviceId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'deviceId': 'deviceId', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'deviceId', 'perPage', 'startingAfter', 'endingBefore'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkSmDevicePerformanceHistory')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSmDeviceRestrictions')
def getNetworkSmDeviceRestrictions(networkId: str, deviceId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'deviceId': 'deviceId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'deviceId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkSmDeviceRestrictions')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSmDeviceSecurityCenters')
def getNetworkSmDeviceSecurityCenters(networkId: str, deviceId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'deviceId': 'deviceId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'deviceId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkSmDeviceSecurityCenters')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSmDeviceSoftwares')
def getNetworkSmDeviceSoftwares(networkId: str, deviceId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'deviceId': 'deviceId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'deviceId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkSmDeviceSoftwares')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSmDeviceWlanLists')
def getNetworkSmDeviceWlanLists(networkId: str, deviceId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'deviceId': 'deviceId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'deviceId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkSmDeviceWlanLists')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSmProfiles')
def getNetworkSmProfiles(networkId: str, payloadTypes: list = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'payloadTypes': 'payloadTypes'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'payloadTypes'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkSmProfiles')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSmTargetGroups')
def getNetworkSmTargetGroups(networkId: str, withDetails: bool = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'withDetails': 'withDetails'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'withDetails'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkSmTargetGroups')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSmTargetGroup')
def getNetworkSmTargetGroup(networkId: str, targetGroupId: str, withDetails: bool = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'targetGroupId': 'targetGroupId', 'withDetails': 'withDetails'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'targetGroupId', 'withDetails'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkSmTargetGroup')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSmTrustedAccessConfigs')
def getNetworkSmTrustedAccessConfigs(networkId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'perPage', 'startingAfter', 'endingBefore'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkSmTrustedAccessConfigs')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSmUserAccessDevices')
def getNetworkSmUserAccessDevices(networkId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'perPage', 'startingAfter', 'endingBefore'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkSmUserAccessDevices')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSmUsers')
def getNetworkSmUsers(networkId: str, ids: list = None, usernames: list = None, emails: list = None, scope: list = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'ids': 'ids', 'usernames': 'usernames', 'emails': 'emails', 'scope': 'scope'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'ids', 'usernames', 'emails', 'scope'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkSmUsers')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSmUserDeviceProfiles')
def getNetworkSmUserDeviceProfiles(networkId: str, userId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'userId': 'userId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'userId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkSmUserDeviceProfiles')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSmUserSoftwares')
def getNetworkSmUserSoftwares(networkId: str, userId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'userId': 'userId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'userId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkSmUserSoftwares')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSnmp')
def getNetworkSnmp(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkSnmp')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSplashLoginAttempts')
def getNetworkSplashLoginAttempts(networkId: str, ssidNumber: int = None, loginIdentifier: str = None, timespan: int = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'ssidNumber': 'ssidNumber', 'loginIdentifier': 'loginIdentifier', 'timespan': 'timespan'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'ssidNumber', 'loginIdentifier', 'timespan'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkSplashLoginAttempts')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSwitchAccessControlLists')
def getNetworkSwitchAccessControlLists(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkSwitchAccessControlLists')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSwitchAccessPolicies')
def getNetworkSwitchAccessPolicies(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkSwitchAccessPolicies')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSwitchAccessPolicy')
def getNetworkSwitchAccessPolicy(networkId: str, accessPolicyNumber: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'accessPolicyNumber': 'accessPolicyNumber'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'accessPolicyNumber'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkSwitchAccessPolicy')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSwitchAlternateManagementInterface')
def getNetworkSwitchAlternateManagementInterface(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkSwitchAlternateManagementInterface')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSwitchDhcpV4ServersSeen')
def getNetworkSwitchDhcpV4ServersSeen(networkId: str, t0: str = None, timespan: float = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 't0': 't0', 'timespan': 'timespan', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 't0', 'timespan', 'perPage', 'startingAfter', 'endingBefore'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkSwitchDhcpV4ServersSeen')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSwitchDhcpServerPolicy')
def getNetworkSwitchDhcpServerPolicy(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkSwitchDhcpServerPolicy')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers')
def getNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers(networkId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'perPage', 'startingAfter', 'endingBefore'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSwitchDhcpServerPolicyArpInspectionWarningsByDevice')
def getNetworkSwitchDhcpServerPolicyArpInspectionWarningsByDevice(networkId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'perPage', 'startingAfter', 'endingBefore'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkSwitchDhcpServerPolicyArpInspectionWarningsByDevice')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSwitchDscpToCosMappings')
def getNetworkSwitchDscpToCosMappings(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkSwitchDscpToCosMappings')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSwitchLinkAggregations')
def getNetworkSwitchLinkAggregations(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkSwitchLinkAggregations')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSwitchMtu')
def getNetworkSwitchMtu(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkSwitchMtu')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSwitchPortSchedules')
def getNetworkSwitchPortSchedules(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkSwitchPortSchedules')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSwitchQosRules')
def getNetworkSwitchQosRules(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkSwitchQosRules')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSwitchQosRulesOrder')
def getNetworkSwitchQosRulesOrder(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkSwitchQosRulesOrder')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSwitchQosRule')
def getNetworkSwitchQosRule(networkId: str, qosRuleId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'qosRuleId': 'qosRuleId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'qosRuleId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkSwitchQosRule')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSwitchRoutingMulticast')
def getNetworkSwitchRoutingMulticast(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkSwitchRoutingMulticast')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSwitchRoutingMulticastRendezvousPoints')
def getNetworkSwitchRoutingMulticastRendezvousPoints(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkSwitchRoutingMulticastRendezvousPoints')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSwitchRoutingMulticastRendezvousPoint')
def getNetworkSwitchRoutingMulticastRendezvousPoint(networkId: str, rendezvousPointId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'rendezvousPointId': 'rendezvousPointId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'rendezvousPointId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkSwitchRoutingMulticastRendezvousPoint')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSwitchRoutingOspf')
def getNetworkSwitchRoutingOspf(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkSwitchRoutingOspf')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSwitchSettings')
def getNetworkSwitchSettings(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkSwitchSettings')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSwitchStacks')
def getNetworkSwitchStacks(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkSwitchStacks')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSwitchStack')
def getNetworkSwitchStack(networkId: str, switchStackId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'switchStackId': 'switchStackId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'switchStackId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkSwitchStack')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSwitchStackRoutingInterfaces')
def getNetworkSwitchStackRoutingInterfaces(networkId: str, switchStackId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'switchStackId': 'switchStackId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'switchStackId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkSwitchStackRoutingInterfaces')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSwitchStackRoutingInterface')
def getNetworkSwitchStackRoutingInterface(networkId: str, switchStackId: str, interfaceId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'switchStackId': 'switchStackId', 'interfaceId': 'interfaceId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'switchStackId', 'interfaceId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkSwitchStackRoutingInterface')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSwitchStackRoutingInterfaceDhcp')
def getNetworkSwitchStackRoutingInterfaceDhcp(networkId: str, switchStackId: str, interfaceId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'switchStackId': 'switchStackId', 'interfaceId': 'interfaceId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'switchStackId', 'interfaceId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkSwitchStackRoutingInterfaceDhcp')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSwitchStackRoutingStaticRoutes')
def getNetworkSwitchStackRoutingStaticRoutes(networkId: str, switchStackId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'switchStackId': 'switchStackId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'switchStackId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkSwitchStackRoutingStaticRoutes')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSwitchStackRoutingStaticRoute')
def getNetworkSwitchStackRoutingStaticRoute(networkId: str, switchStackId: str, staticRouteId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'switchStackId': 'switchStackId', 'staticRouteId': 'staticRouteId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'switchStackId', 'staticRouteId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkSwitchStackRoutingStaticRoute')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSwitchStormControl')
def getNetworkSwitchStormControl(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkSwitchStormControl')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSwitchStp')
def getNetworkSwitchStp(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkSwitchStp')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkSyslogServers')
def getNetworkSyslogServers(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkSyslogServers')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkTopologyLinkLayer')
def getNetworkTopologyLinkLayer(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkTopologyLinkLayer')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkTraffic')
def getNetworkTraffic(networkId: str, t0: str = None, timespan: float = None, deviceType: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 't0': 't0', 'timespan': 'timespan', 'deviceType': 'deviceType'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 't0', 'timespan', 'deviceType'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkTraffic')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkTrafficAnalysis')
def getNetworkTrafficAnalysis(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkTrafficAnalysis')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkTrafficShapingApplicationCategories')
def getNetworkTrafficShapingApplicationCategories(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkTrafficShapingApplicationCategories')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkTrafficShapingDscpTaggingOptions')
def getNetworkTrafficShapingDscpTaggingOptions(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkTrafficShapingDscpTaggingOptions')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkVlanProfiles')
def getNetworkVlanProfiles(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkVlanProfiles')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkVlanProfilesAssignmentsByDevice')
def getNetworkVlanProfilesAssignmentsByDevice(networkId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None, serials: list = None, productTypes: list = None, stackIds: list = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore', 'serials': 'serials', 'productTypes': 'productTypes', 'stackIds': 'stackIds'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'perPage', 'startingAfter', 'endingBefore', 'serials', 'productTypes', 'stackIds'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkVlanProfilesAssignmentsByDevice')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkVlanProfile')
def getNetworkVlanProfile(networkId: str, iname: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'iname': 'iname'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'iname'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkVlanProfile')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWebhooksHttpServers')
def getNetworkWebhooksHttpServers(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkWebhooksHttpServers')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWebhooksHttpServer')
def getNetworkWebhooksHttpServer(networkId: str, httpServerId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'httpServerId': 'httpServerId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'httpServerId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkWebhooksHttpServer')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWebhooksPayloadTemplates')
def getNetworkWebhooksPayloadTemplates(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkWebhooksPayloadTemplates')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWebhooksPayloadTemplate')
def getNetworkWebhooksPayloadTemplate(networkId: str, payloadTemplateId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'payloadTemplateId': 'payloadTemplateId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'payloadTemplateId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkWebhooksPayloadTemplate')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWebhooksWebhookTest')
def getNetworkWebhooksWebhookTest(networkId: str, webhookTestId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'webhookTestId': 'webhookTestId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'webhookTestId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkWebhooksWebhookTest')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWirelessAirMarshal')
def getNetworkWirelessAirMarshal(networkId: str, t0: str = None, timespan: float = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 't0': 't0', 'timespan': 'timespan'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 't0', 'timespan'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkWirelessAirMarshal')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWirelessAlternateManagementInterface')
def getNetworkWirelessAlternateManagementInterface(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkWirelessAlternateManagementInterface')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWirelessBilling')
def getNetworkWirelessBilling(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkWirelessBilling')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWirelessBluetoothSettings')
def getNetworkWirelessBluetoothSettings(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkWirelessBluetoothSettings')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWirelessChannelUtilizationHistory')
def getNetworkWirelessChannelUtilizationHistory(networkId: str, t0: str = None, t1: str = None, timespan: float = None, resolution: int = None, autoResolution: bool = None, clientId: str = None, deviceSerial: str = None, apTag: str = None, band: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 't0': 't0', 't1': 't1', 'timespan': 'timespan', 'resolution': 'resolution', 'autoResolution': 'autoResolution', 'clientId': 'clientId', 'deviceSerial': 'deviceSerial', 'apTag': 'apTag', 'band': 'band'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 't0', 't1', 'timespan', 'resolution', 'autoResolution', 'clientId', 'deviceSerial', 'apTag', 'band'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkWirelessChannelUtilizationHistory')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWirelessClientCountHistory')
def getNetworkWirelessClientCountHistory(networkId: str, t0: str = None, t1: str = None, timespan: float = None, resolution: int = None, autoResolution: bool = None, clientId: str = None, deviceSerial: str = None, apTag: str = None, band: str = None, ssid: int = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 't0': 't0', 't1': 't1', 'timespan': 'timespan', 'resolution': 'resolution', 'autoResolution': 'autoResolution', 'clientId': 'clientId', 'deviceSerial': 'deviceSerial', 'apTag': 'apTag', 'band': 'band', 'ssid': 'ssid'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 't0', 't1', 'timespan', 'resolution', 'autoResolution', 'clientId', 'deviceSerial', 'apTag', 'band', 'ssid'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkWirelessClientCountHistory')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWirelessClientsConnectionStats')
def getNetworkWirelessClientsConnectionStats(networkId: str, t0: str = None, t1: str = None, timespan: float = None, band: str = None, ssid: int = None, vlan: int = None, apTag: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 't0': 't0', 't1': 't1', 'timespan': 'timespan', 'band': 'band', 'ssid': 'ssid', 'vlan': 'vlan', 'apTag': 'apTag'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 't0', 't1', 'timespan', 'band', 'ssid', 'vlan', 'apTag'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkWirelessClientsConnectionStats')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWirelessClientsLatencyStats')
def getNetworkWirelessClientsLatencyStats(networkId: str, t0: str = None, t1: str = None, timespan: float = None, band: str = None, ssid: int = None, vlan: int = None, apTag: str = None, fields: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 't0': 't0', 't1': 't1', 'timespan': 'timespan', 'band': 'band', 'ssid': 'ssid', 'vlan': 'vlan', 'apTag': 'apTag', 'fields': 'fields'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 't0', 't1', 'timespan', 'band', 'ssid', 'vlan', 'apTag', 'fields'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkWirelessClientsLatencyStats')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWirelessClientConnectionStats')
def getNetworkWirelessClientConnectionStats(networkId: str, clientId: str, t0: str = None, t1: str = None, timespan: float = None, band: str = None, ssid: int = None, vlan: int = None, apTag: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'clientId': 'clientId', 't0': 't0', 't1': 't1', 'timespan': 'timespan', 'band': 'band', 'ssid': 'ssid', 'vlan': 'vlan', 'apTag': 'apTag'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'clientId', 't0', 't1', 'timespan', 'band', 'ssid', 'vlan', 'apTag'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkWirelessClientConnectionStats')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWirelessClientConnectivityEvents')
def getNetworkWirelessClientConnectivityEvents(networkId: str, clientId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None, sortOrder: str = None, t0: str = None, t1: str = None, timespan: float = None, types: list = None, band: str = None, ssidNumber: int = None, includedSeverities: list = None, deviceSerial: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'clientId': 'clientId', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore', 'sortOrder': 'sortOrder', 't0': 't0', 't1': 't1', 'timespan': 'timespan', 'types': 'types', 'band': 'band', 'ssidNumber': 'ssidNumber', 'includedSeverities': 'includedSeverities', 'deviceSerial': 'deviceSerial'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'clientId', 'perPage', 'startingAfter', 'endingBefore', 'sortOrder', 't0', 't1', 'timespan', 'types', 'band', 'ssidNumber', 'includedSeverities', 'deviceSerial'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkWirelessClientConnectivityEvents')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWirelessClientLatencyHistory')
def getNetworkWirelessClientLatencyHistory(networkId: str, clientId: str, t0: str = None, t1: str = None, timespan: float = None, resolution: int = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'clientId': 'clientId', 't0': 't0', 't1': 't1', 'timespan': 'timespan', 'resolution': 'resolution'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'clientId', 't0', 't1', 'timespan', 'resolution'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkWirelessClientLatencyHistory')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWirelessClientLatencyStats')
def getNetworkWirelessClientLatencyStats(networkId: str, clientId: str, t0: str = None, t1: str = None, timespan: float = None, band: str = None, ssid: int = None, vlan: int = None, apTag: str = None, fields: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'clientId': 'clientId', 't0': 't0', 't1': 't1', 'timespan': 'timespan', 'band': 'band', 'ssid': 'ssid', 'vlan': 'vlan', 'apTag': 'apTag', 'fields': 'fields'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'clientId', 't0', 't1', 'timespan', 'band', 'ssid', 'vlan', 'apTag', 'fields'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkWirelessClientLatencyStats')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWirelessConnectionStats')
def getNetworkWirelessConnectionStats(networkId: str, t0: str = None, t1: str = None, timespan: float = None, band: str = None, ssid: int = None, vlan: int = None, apTag: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 't0': 't0', 't1': 't1', 'timespan': 'timespan', 'band': 'band', 'ssid': 'ssid', 'vlan': 'vlan', 'apTag': 'apTag'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 't0', 't1', 'timespan', 'band', 'ssid', 'vlan', 'apTag'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkWirelessConnectionStats')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWirelessDataRateHistory')
def getNetworkWirelessDataRateHistory(networkId: str, t0: str = None, t1: str = None, timespan: float = None, resolution: int = None, autoResolution: bool = None, clientId: str = None, deviceSerial: str = None, apTag: str = None, band: str = None, ssid: int = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 't0': 't0', 't1': 't1', 'timespan': 'timespan', 'resolution': 'resolution', 'autoResolution': 'autoResolution', 'clientId': 'clientId', 'deviceSerial': 'deviceSerial', 'apTag': 'apTag', 'band': 'band', 'ssid': 'ssid'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 't0', 't1', 'timespan', 'resolution', 'autoResolution', 'clientId', 'deviceSerial', 'apTag', 'band', 'ssid'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkWirelessDataRateHistory')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWirelessDevicesConnectionStats')
def getNetworkWirelessDevicesConnectionStats(networkId: str, t0: str = None, t1: str = None, timespan: float = None, band: str = None, ssid: int = None, vlan: int = None, apTag: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 't0': 't0', 't1': 't1', 'timespan': 'timespan', 'band': 'band', 'ssid': 'ssid', 'vlan': 'vlan', 'apTag': 'apTag'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 't0', 't1', 'timespan', 'band', 'ssid', 'vlan', 'apTag'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkWirelessDevicesConnectionStats')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWirelessDevicesLatencyStats')
def getNetworkWirelessDevicesLatencyStats(networkId: str, t0: str = None, t1: str = None, timespan: float = None, band: str = None, ssid: int = None, vlan: int = None, apTag: str = None, fields: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 't0': 't0', 't1': 't1', 'timespan': 'timespan', 'band': 'band', 'ssid': 'ssid', 'vlan': 'vlan', 'apTag': 'apTag', 'fields': 'fields'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 't0', 't1', 'timespan', 'band', 'ssid', 'vlan', 'apTag', 'fields'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkWirelessDevicesLatencyStats')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWirelessElectronicShelfLabel')
def getNetworkWirelessElectronicShelfLabel(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkWirelessElectronicShelfLabel')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWirelessElectronicShelfLabelConfiguredDevices')
def getNetworkWirelessElectronicShelfLabelConfiguredDevices(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkWirelessElectronicShelfLabelConfiguredDevices')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWirelessEthernetPortsProfiles')
def getNetworkWirelessEthernetPortsProfiles(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkWirelessEthernetPortsProfiles')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWirelessEthernetPortsProfile')
def getNetworkWirelessEthernetPortsProfile(networkId: str, profileId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'profileId': 'profileId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'profileId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkWirelessEthernetPortsProfile')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWirelessFailedConnections')
def getNetworkWirelessFailedConnections(networkId: str, t0: str = None, t1: str = None, timespan: float = None, band: str = None, ssid: int = None, vlan: int = None, apTag: str = None, serial: str = None, clientId: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 't0': 't0', 't1': 't1', 'timespan': 'timespan', 'band': 'band', 'ssid': 'ssid', 'vlan': 'vlan', 'apTag': 'apTag', 'serial': 'serial', 'clientId': 'clientId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 't0', 't1', 'timespan', 'band', 'ssid', 'vlan', 'apTag', 'serial', 'clientId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkWirelessFailedConnections')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWirelessLatencyHistory')
def getNetworkWirelessLatencyHistory(networkId: str, t0: str = None, t1: str = None, timespan: float = None, resolution: int = None, autoResolution: bool = None, clientId: str = None, deviceSerial: str = None, apTag: str = None, band: str = None, ssid: int = None, accessCategory: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 't0': 't0', 't1': 't1', 'timespan': 'timespan', 'resolution': 'resolution', 'autoResolution': 'autoResolution', 'clientId': 'clientId', 'deviceSerial': 'deviceSerial', 'apTag': 'apTag', 'band': 'band', 'ssid': 'ssid', 'accessCategory': 'accessCategory'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 't0', 't1', 'timespan', 'resolution', 'autoResolution', 'clientId', 'deviceSerial', 'apTag', 'band', 'ssid', 'accessCategory'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkWirelessLatencyHistory')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWirelessLatencyStats')
def getNetworkWirelessLatencyStats(networkId: str, t0: str = None, t1: str = None, timespan: float = None, band: str = None, ssid: int = None, vlan: int = None, apTag: str = None, fields: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 't0': 't0', 't1': 't1', 'timespan': 'timespan', 'band': 'band', 'ssid': 'ssid', 'vlan': 'vlan', 'apTag': 'apTag', 'fields': 'fields'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 't0', 't1', 'timespan', 'band', 'ssid', 'vlan', 'apTag', 'fields'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkWirelessLatencyStats')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWirelessMeshStatuses')
def getNetworkWirelessMeshStatuses(networkId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'perPage', 'startingAfter', 'endingBefore'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkWirelessMeshStatuses')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWirelessRfProfiles')
def getNetworkWirelessRfProfiles(networkId: str, includeTemplateProfiles: bool = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'includeTemplateProfiles': 'includeTemplateProfiles'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'includeTemplateProfiles'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkWirelessRfProfiles')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWirelessRfProfile')
def getNetworkWirelessRfProfile(networkId: str, rfProfileId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'rfProfileId': 'rfProfileId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'rfProfileId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkWirelessRfProfile')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWirelessSettings')
def getNetworkWirelessSettings(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkWirelessSettings')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWirelessSignalQualityHistory')
def getNetworkWirelessSignalQualityHistory(networkId: str, t0: str = None, t1: str = None, timespan: float = None, resolution: int = None, autoResolution: bool = None, clientId: str = None, deviceSerial: str = None, apTag: str = None, band: str = None, ssid: int = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 't0': 't0', 't1': 't1', 'timespan': 'timespan', 'resolution': 'resolution', 'autoResolution': 'autoResolution', 'clientId': 'clientId', 'deviceSerial': 'deviceSerial', 'apTag': 'apTag', 'band': 'band', 'ssid': 'ssid'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 't0', 't1', 'timespan', 'resolution', 'autoResolution', 'clientId', 'deviceSerial', 'apTag', 'band', 'ssid'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkWirelessSignalQualityHistory')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWirelessSsids')
def getNetworkWirelessSsids(networkId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkWirelessSsids')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWirelessSsid')
def getNetworkWirelessSsid(networkId: str, number: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'number': 'number'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'number'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkWirelessSsid')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWirelessSsidBonjourForwarding')
def getNetworkWirelessSsidBonjourForwarding(networkId: str, number: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'number': 'number'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'number'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkWirelessSsidBonjourForwarding')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWirelessSsidDeviceTypeGroupPolicies')
def getNetworkWirelessSsidDeviceTypeGroupPolicies(networkId: str, number: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'number': 'number'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'number'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkWirelessSsidDeviceTypeGroupPolicies')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWirelessSsidEapOverride')
def getNetworkWirelessSsidEapOverride(networkId: str, number: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'number': 'number'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'number'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkWirelessSsidEapOverride')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWirelessSsidFirewallL3FirewallRules')
def getNetworkWirelessSsidFirewallL3FirewallRules(networkId: str, number: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'number': 'number'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'number'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkWirelessSsidFirewallL3FirewallRules')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWirelessSsidFirewallL7FirewallRules')
def getNetworkWirelessSsidFirewallL7FirewallRules(networkId: str, number: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'number': 'number'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'number'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkWirelessSsidFirewallL7FirewallRules')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWirelessSsidHotspot20')
def getNetworkWirelessSsidHotspot20(networkId: str, number: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'number': 'number'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'number'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkWirelessSsidHotspot20')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWirelessSsidIdentityPsks')
def getNetworkWirelessSsidIdentityPsks(networkId: str, number: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'number': 'number'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'number'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkWirelessSsidIdentityPsks')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWirelessSsidIdentityPsk')
def getNetworkWirelessSsidIdentityPsk(networkId: str, number: str, identityPskId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'number': 'number', 'identityPskId': 'identityPskId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'number', 'identityPskId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkWirelessSsidIdentityPsk')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWirelessSsidSchedules')
def getNetworkWirelessSsidSchedules(networkId: str, number: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'number': 'number'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'number'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkWirelessSsidSchedules')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWirelessSsidSplashSettings')
def getNetworkWirelessSsidSplashSettings(networkId: str, number: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'number': 'number'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'number'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkWirelessSsidSplashSettings')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWirelessSsidTrafficShapingRules')
def getNetworkWirelessSsidTrafficShapingRules(networkId: str, number: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'number': 'number'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'number'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkWirelessSsidTrafficShapingRules')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWirelessSsidVpn')
def getNetworkWirelessSsidVpn(networkId: str, number: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 'number': 'number'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 'number'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkWirelessSsidVpn')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkWirelessUsageHistory')
def getNetworkWirelessUsageHistory(networkId: str, t0: str = None, t1: str = None, timespan: float = None, resolution: int = None, autoResolution: bool = None, clientId: str = None, deviceSerial: str = None, apTag: str = None, band: str = None, ssid: int = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkId': 'networkId', 't0': 't0', 't1': 't1', 'timespan': 'timespan', 'resolution': 'resolution', 'autoResolution': 'autoResolution', 'clientId': 'clientId', 'deviceSerial': 'deviceSerial', 'apTag': 'apTag', 'band': 'band', 'ssid': 'ssid'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['networkId', 't0', 't1', 'timespan', 'resolution', 'autoResolution', 'clientId', 'deviceSerial', 'apTag', 'band', 'ssid'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getNetworkWirelessUsageHistory')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizations')
def getOrganizations(perPage: int = None, startingAfter: str = None, endingBefore: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['perPage', 'startingAfter', 'endingBefore'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizations')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganization')
def getOrganization(organizationId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganization')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationActionBatches')
def getOrganizationActionBatches(organizationId: str, status: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'status': 'status'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'status'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationActionBatches')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationActionBatch')
def getOrganizationActionBatch(organizationId: str, actionBatchId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'actionBatchId': 'actionBatchId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'actionBatchId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationActionBatch')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationAdaptivePolicyAcls')
def getOrganizationAdaptivePolicyAcls(organizationId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationAdaptivePolicyAcls')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationAdaptivePolicyAcl')
def getOrganizationAdaptivePolicyAcl(organizationId: str, aclId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'aclId': 'aclId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'aclId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationAdaptivePolicyAcl')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationAdaptivePolicyGroups')
def getOrganizationAdaptivePolicyGroups(organizationId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationAdaptivePolicyGroups')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationAdaptivePolicyGroup')
def getOrganizationAdaptivePolicyGroup(organizationId: str, id: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'id': 'id'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'id'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationAdaptivePolicyGroup')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationAdaptivePolicyOverview')
def getOrganizationAdaptivePolicyOverview(organizationId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationAdaptivePolicyOverview')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationAdaptivePolicyPolicies')
def getOrganizationAdaptivePolicyPolicies(organizationId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationAdaptivePolicyPolicies')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationAdaptivePolicyPolicy')
def getOrganizationAdaptivePolicyPolicy(organizationId: str, id: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'id': 'id'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'id'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationAdaptivePolicyPolicy')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationAdaptivePolicySettings')
def getOrganizationAdaptivePolicySettings(organizationId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationAdaptivePolicySettings')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationAdmins')
def getOrganizationAdmins(organizationId: str, networkIds: list = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'networkIds': 'networkIds'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'networkIds'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationAdmins')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationAlertsProfiles')
def getOrganizationAlertsProfiles(organizationId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationAlertsProfiles')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationApiRequests')
def getOrganizationApiRequests(organizationId: str, t0: str = None, t1: str = None, timespan: float = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None, adminId: str = None, path: str = None, method: str = None, responseCode: int = None, sourceIp: str = None, userAgent: str = None, version: int = None, operationIds: list = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 't0': 't0', 't1': 't1', 'timespan': 'timespan', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore', 'adminId': 'adminId', 'path': 'path', 'method': 'method', 'responseCode': 'responseCode', 'sourceIp': 'sourceIp', 'userAgent': 'userAgent', 'version': 'version', 'operationIds': 'operationIds'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 't0', 't1', 'timespan', 'perPage', 'startingAfter', 'endingBefore', 'adminId', 'path', 'method', 'responseCode', 'sourceIp', 'userAgent', 'version', 'operationIds'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationApiRequests')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationApiRequestsOverview')
def getOrganizationApiRequestsOverview(organizationId: str, t0: str = None, t1: str = None, timespan: float = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 't0': 't0', 't1': 't1', 'timespan': 'timespan'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 't0', 't1', 'timespan'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationApiRequestsOverview')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationApiRequestsOverviewResponseCodesByInterval')
def getOrganizationApiRequestsOverviewResponseCodesByInterval(organizationId: str, t0: str = None, t1: str = None, timespan: float = None, interval: int = None, version: int = None, operationIds: list = None, sourceIps: list = None, adminIds: list = None, userAgent: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 't0': 't0', 't1': 't1', 'timespan': 'timespan', 'interval': 'interval', 'version': 'version', 'operationIds': 'operationIds', 'sourceIps': 'sourceIps', 'adminIds': 'adminIds', 'userAgent': 'userAgent'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 't0', 't1', 'timespan', 'interval', 'version', 'operationIds', 'sourceIps', 'adminIds', 'userAgent'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationApiRequestsOverviewResponseCodesByInterval')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationApplianceSecurityEvents')
def getOrganizationApplianceSecurityEvents(organizationId: str, t0: str = None, t1: str = None, timespan: float = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None, sortOrder: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 't0': 't0', 't1': 't1', 'timespan': 'timespan', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore', 'sortOrder': 'sortOrder'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 't0', 't1', 'timespan', 'perPage', 'startingAfter', 'endingBefore', 'sortOrder'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationApplianceSecurityEvents')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationApplianceSecurityIntrusion')
def getOrganizationApplianceSecurityIntrusion(organizationId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationApplianceSecurityIntrusion')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationApplianceTrafficShapingVpnExclusionsByNetwork')
def getOrganizationApplianceTrafficShapingVpnExclusionsByNetwork(organizationId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None, networkIds: list = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore', 'networkIds': 'networkIds'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'networkIds'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationApplianceTrafficShapingVpnExclusionsByNetwork')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationApplianceUplinkStatuses')
def getOrganizationApplianceUplinkStatuses(organizationId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None, networkIds: list = None, serials: list = None, iccids: list = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore', 'networkIds': 'networkIds', 'serials': 'serials', 'iccids': 'iccids'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'networkIds', 'serials', 'iccids'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationApplianceUplinkStatuses')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationApplianceUplinksStatusesOverview')
def getOrganizationApplianceUplinksStatusesOverview(organizationId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationApplianceUplinksStatusesOverview')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationApplianceUplinksUsageByNetwork')
def getOrganizationApplianceUplinksUsageByNetwork(organizationId: str, t0: str = None, t1: str = None, timespan: float = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 't0': 't0', 't1': 't1', 'timespan': 'timespan'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 't0', 't1', 'timespan'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationApplianceUplinksUsageByNetwork')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationApplianceVpnStats')
def getOrganizationApplianceVpnStats(organizationId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None, networkIds: list = None, t0: str = None, t1: str = None, timespan: float = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore', 'networkIds': 'networkIds', 't0': 't0', 't1': 't1', 'timespan': 'timespan'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'networkIds', 't0', 't1', 'timespan'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationApplianceVpnStats')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationApplianceVpnStatuses')
def getOrganizationApplianceVpnStatuses(organizationId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None, networkIds: list = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore', 'networkIds': 'networkIds'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'networkIds'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationApplianceVpnStatuses')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationApplianceVpnThirdPartyVPNPeers')
def getOrganizationApplianceVpnThirdPartyVPNPeers(organizationId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationApplianceVpnThirdPartyVPNPeers')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationApplianceVpnVpnFirewallRules')
def getOrganizationApplianceVpnVpnFirewallRules(organizationId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationApplianceVpnVpnFirewallRules')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationAssuranceAlerts')
def getOrganizationAssuranceAlerts(organizationId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None, sortOrder: str = None, networkId: str = None, severity: str = None, types: list = None, tsStart: str = None, tsEnd: str = None, category: str = None, sortBy: str = None, serials: list = None, deviceTypes: list = None, deviceTags: list = None, active: bool = None, dismissed: bool = None, resolved: bool = None, suppressAlertsForOfflineNodes: bool = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore', 'sortOrder': 'sortOrder', 'networkId': 'networkId', 'severity': 'severity', 'types': 'types', 'tsStart': 'tsStart', 'tsEnd': 'tsEnd', 'category': 'category', 'sortBy': 'sortBy', 'serials': 'serials', 'deviceTypes': 'deviceTypes', 'deviceTags': 'deviceTags', 'active': 'active', 'dismissed': 'dismissed', 'resolved': 'resolved', 'suppressAlertsForOfflineNodes': 'suppressAlertsForOfflineNodes'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'sortOrder', 'networkId', 'severity', 'types', 'tsStart', 'tsEnd', 'category', 'sortBy', 'serials', 'deviceTypes', 'deviceTags', 'active', 'dismissed', 'resolved', 'suppressAlertsForOfflineNodes'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationAssuranceAlerts')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationAssuranceAlertsOverview')
def getOrganizationAssuranceAlertsOverview(organizationId: str, networkId: str = None, severity: str = None, types: list = None, tsStart: str = None, tsEnd: str = None, category: str = None, serials: list = None, deviceTypes: list = None, deviceTags: list = None, active: bool = None, dismissed: bool = None, resolved: bool = None, suppressAlertsForOfflineNodes: bool = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'networkId': 'networkId', 'severity': 'severity', 'types': 'types', 'tsStart': 'tsStart', 'tsEnd': 'tsEnd', 'category': 'category', 'serials': 'serials', 'deviceTypes': 'deviceTypes', 'deviceTags': 'deviceTags', 'active': 'active', 'dismissed': 'dismissed', 'resolved': 'resolved', 'suppressAlertsForOfflineNodes': 'suppressAlertsForOfflineNodes'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'networkId', 'severity', 'types', 'tsStart', 'tsEnd', 'category', 'serials', 'deviceTypes', 'deviceTags', 'active', 'dismissed', 'resolved', 'suppressAlertsForOfflineNodes'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationAssuranceAlertsOverview')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationAssuranceAlertsOverviewByNetwork')
def getOrganizationAssuranceAlertsOverviewByNetwork(organizationId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None, sortOrder: str = None, networkId: str = None, severity: str = None, types: list = None, tsStart: str = None, tsEnd: str = None, category: str = None, serials: list = None, deviceTypes: list = None, deviceTags: list = None, active: bool = None, dismissed: bool = None, resolved: bool = None, suppressAlertsForOfflineNodes: bool = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore', 'sortOrder': 'sortOrder', 'networkId': 'networkId', 'severity': 'severity', 'types': 'types', 'tsStart': 'tsStart', 'tsEnd': 'tsEnd', 'category': 'category', 'serials': 'serials', 'deviceTypes': 'deviceTypes', 'deviceTags': 'deviceTags', 'active': 'active', 'dismissed': 'dismissed', 'resolved': 'resolved', 'suppressAlertsForOfflineNodes': 'suppressAlertsForOfflineNodes'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'sortOrder', 'networkId', 'severity', 'types', 'tsStart', 'tsEnd', 'category', 'serials', 'deviceTypes', 'deviceTags', 'active', 'dismissed', 'resolved', 'suppressAlertsForOfflineNodes'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationAssuranceAlertsOverviewByNetwork')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationAssuranceAlertsOverviewByType')
def getOrganizationAssuranceAlertsOverviewByType(organizationId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None, sortOrder: str = None, networkId: str = None, severity: str = None, types: list = None, tsStart: str = None, tsEnd: str = None, category: str = None, sortBy: str = None, serials: list = None, deviceTypes: list = None, deviceTags: list = None, active: bool = None, dismissed: bool = None, resolved: bool = None, suppressAlertsForOfflineNodes: bool = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore', 'sortOrder': 'sortOrder', 'networkId': 'networkId', 'severity': 'severity', 'types': 'types', 'tsStart': 'tsStart', 'tsEnd': 'tsEnd', 'category': 'category', 'sortBy': 'sortBy', 'serials': 'serials', 'deviceTypes': 'deviceTypes', 'deviceTags': 'deviceTags', 'active': 'active', 'dismissed': 'dismissed', 'resolved': 'resolved', 'suppressAlertsForOfflineNodes': 'suppressAlertsForOfflineNodes'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'sortOrder', 'networkId', 'severity', 'types', 'tsStart', 'tsEnd', 'category', 'sortBy', 'serials', 'deviceTypes', 'deviceTags', 'active', 'dismissed', 'resolved', 'suppressAlertsForOfflineNodes'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationAssuranceAlertsOverviewByType')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationAssuranceAlertsOverviewHistorical')
def getOrganizationAssuranceAlertsOverviewHistorical(organizationId: str, segmentDuration: int, tsStart: str, networkId: str = None, severity: str = None, types: list = None, tsEnd: str = None, category: str = None, serials: list = None, deviceTypes: list = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'segmentDuration': 'segmentDuration', 'networkId': 'networkId', 'severity': 'severity', 'types': 'types', 'tsStart': 'tsStart', 'tsEnd': 'tsEnd', 'category': 'category', 'serials': 'serials', 'deviceTypes': 'deviceTypes'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'segmentDuration', 'networkId', 'severity', 'types', 'tsStart', 'tsEnd', 'category', 'serials', 'deviceTypes'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationAssuranceAlertsOverviewHistorical')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationAssuranceAlert')
def getOrganizationAssuranceAlert(organizationId: str, id: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'id': 'id'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'id'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationAssuranceAlert')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationBrandingPolicies')
def getOrganizationBrandingPolicies(organizationId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationBrandingPolicies')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationBrandingPoliciesPriorities')
def getOrganizationBrandingPoliciesPriorities(organizationId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationBrandingPoliciesPriorities')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationBrandingPolicy')
def getOrganizationBrandingPolicy(organizationId: str, brandingPolicyId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'brandingPolicyId': 'brandingPolicyId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'brandingPolicyId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationBrandingPolicy')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationCameraBoundariesAreasByDevice')
def getOrganizationCameraBoundariesAreasByDevice(organizationId: str, serials: list = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'serials': 'serials'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'serials'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationCameraBoundariesAreasByDevice')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationCameraBoundariesLinesByDevice')
def getOrganizationCameraBoundariesLinesByDevice(organizationId: str, serials: list = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'serials': 'serials'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'serials'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationCameraBoundariesLinesByDevice')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationCameraCustomAnalyticsArtifacts')
def getOrganizationCameraCustomAnalyticsArtifacts(organizationId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationCameraCustomAnalyticsArtifacts')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationCameraCustomAnalyticsArtifact')
def getOrganizationCameraCustomAnalyticsArtifact(organizationId: str, artifactId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'artifactId': 'artifactId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'artifactId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationCameraCustomAnalyticsArtifact')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationCameraDetectionsHistoryByBoundaryByInterval')
def getOrganizationCameraDetectionsHistoryByBoundaryByInterval(organizationId: str, boundaryIds: list, ranges: list, duration: int = None, perPage: int = None, boundaryTypes: list = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'boundaryIds': 'boundaryIds', 'ranges': 'ranges', 'duration': 'duration', 'perPage': 'perPage', 'boundaryTypes': 'boundaryTypes'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'boundaryIds', 'ranges', 'duration', 'perPage', 'boundaryTypes'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationCameraDetectionsHistoryByBoundaryByInterval')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationCameraOnboardingStatuses')
def getOrganizationCameraOnboardingStatuses(organizationId: str, serials: list = None, networkIds: list = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'serials': 'serials', 'networkIds': 'networkIds'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'serials', 'networkIds'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationCameraOnboardingStatuses')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationCameraPermissions')
def getOrganizationCameraPermissions(organizationId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationCameraPermissions')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationCameraPermission')
def getOrganizationCameraPermission(organizationId: str, permissionScopeId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'permissionScopeId': 'permissionScopeId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'permissionScopeId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationCameraPermission')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationCameraRoles')
def getOrganizationCameraRoles(organizationId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationCameraRoles')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationCameraRole')
def getOrganizationCameraRole(organizationId: str, roleId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'roleId': 'roleId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'roleId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationCameraRole')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationCellularGatewayEsimsInventory')
def getOrganizationCellularGatewayEsimsInventory(organizationId: str, eids: list = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'eids': 'eids'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'eids'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationCellularGatewayEsimsInventory')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationCellularGatewayEsimsServiceProviders')
def getOrganizationCellularGatewayEsimsServiceProviders(organizationId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationCellularGatewayEsimsServiceProviders')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationCellularGatewayEsimsServiceProvidersAccounts')
def getOrganizationCellularGatewayEsimsServiceProvidersAccounts(organizationId: str, accountIds: list = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'accountIds': 'accountIds'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'accountIds'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationCellularGatewayEsimsServiceProvidersAccounts')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationCellularGatewayEsimsServiceProvidersAccountsCommu')
def getOrganizationCellularGatewayEsimsServiceProvidersAccountsCommu(organizationId: str, accountIds: list):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'accountIds': 'accountIds'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'accountIds'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationCellularGatewayEsimsServiceProvidersAccountsCommu')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationCellularGatewayEsimsServiceProvidersAccountsRateP')
def getOrganizationCellularGatewayEsimsServiceProvidersAccountsRateP(organizationId: str, accountIds: list):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'accountIds': 'accountIds'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'accountIds'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationCellularGatewayEsimsServiceProvidersAccountsRateP')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationCellularGatewayUplinkStatuses')
def getOrganizationCellularGatewayUplinkStatuses(organizationId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None, networkIds: list = None, serials: list = None, iccids: list = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore', 'networkIds': 'networkIds', 'serials': 'serials', 'iccids': 'iccids'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'networkIds', 'serials', 'iccids'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationCellularGatewayUplinkStatuses')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationClientsBandwidthUsageHistory')
def getOrganizationClientsBandwidthUsageHistory(organizationId: str, networkTag: str = None, deviceTag: str = None, ssidName: str = None, usageUplink: str = None, t0: str = None, t1: str = None, timespan: float = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'networkTag': 'networkTag', 'deviceTag': 'deviceTag', 'ssidName': 'ssidName', 'usageUplink': 'usageUplink', 't0': 't0', 't1': 't1', 'timespan': 'timespan'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'networkTag', 'deviceTag', 'ssidName', 'usageUplink', 't0', 't1', 'timespan'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationClientsBandwidthUsageHistory')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationClientsOverview')
def getOrganizationClientsOverview(organizationId: str, t0: str = None, t1: str = None, timespan: float = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 't0': 't0', 't1': 't1', 'timespan': 'timespan'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 't0', 't1', 'timespan'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationClientsOverview')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationClientsSearch')
def getOrganizationClientsSearch(organizationId: str, mac: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore', 'mac': 'mac'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'mac'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationClientsSearch')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationConfigTemplates')
def getOrganizationConfigTemplates(organizationId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationConfigTemplates')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationConfigTemplate')
def getOrganizationConfigTemplate(organizationId: str, configTemplateId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'configTemplateId': 'configTemplateId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'configTemplateId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationConfigTemplate')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationConfigTemplateSwitchProfiles')
def getOrganizationConfigTemplateSwitchProfiles(organizationId: str, configTemplateId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'configTemplateId': 'configTemplateId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'configTemplateId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationConfigTemplateSwitchProfiles')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationConfigTemplateSwitchProfilePorts')
def getOrganizationConfigTemplateSwitchProfilePorts(organizationId: str, configTemplateId: str, profileId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'configTemplateId': 'configTemplateId', 'profileId': 'profileId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'configTemplateId', 'profileId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationConfigTemplateSwitchProfilePorts')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationConfigTemplateSwitchProfilePort')
def getOrganizationConfigTemplateSwitchProfilePort(organizationId: str, configTemplateId: str, profileId: str, portId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'configTemplateId': 'configTemplateId', 'profileId': 'profileId', 'portId': 'portId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'configTemplateId', 'profileId', 'portId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationConfigTemplateSwitchProfilePort')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationConfigurationChanges')
def getOrganizationConfigurationChanges(organizationId: str, t0: str = None, t1: str = None, timespan: float = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None, networkId: str = None, adminId: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 't0': 't0', 't1': 't1', 'timespan': 'timespan', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore', 'networkId': 'networkId', 'adminId': 'adminId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 't0', 't1', 'timespan', 'perPage', 'startingAfter', 'endingBefore', 'networkId', 'adminId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationConfigurationChanges')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationDevices')
def getOrganizationDevices(organizationId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None, configurationUpdatedAfter: str = None, networkIds: list = None, productTypes: list = None, tags: list = None, tagsFilterType: str = None, name: str = None, mac: str = None, serial: str = None, model: str = None, macs: list = None, serials: list = None, sensorMetrics: list = None, sensorAlertProfileIds: list = None, models: list = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore', 'configurationUpdatedAfter': 'configurationUpdatedAfter', 'networkIds': 'networkIds', 'productTypes': 'productTypes', 'tags': 'tags', 'tagsFilterType': 'tagsFilterType', 'name': 'name', 'mac': 'mac', 'serial': 'serial', 'model': 'model', 'macs': 'macs', 'serials': 'serials', 'sensorMetrics': 'sensorMetrics', 'sensorAlertProfileIds': 'sensorAlertProfileIds', 'models': 'models'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'configurationUpdatedAfter', 'networkIds', 'productTypes', 'tags', 'tagsFilterType', 'name', 'mac', 'serial', 'model', 'macs', 'serials', 'sensorMetrics', 'sensorAlertProfileIds', 'models'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationDevices')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationDevicesAvailabilities')
def getOrganizationDevicesAvailabilities(organizationId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None, networkIds: list = None, productTypes: list = None, serials: list = None, tags: list = None, tagsFilterType: str = None, statuses: list = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore', 'networkIds': 'networkIds', 'productTypes': 'productTypes', 'serials': 'serials', 'tags': 'tags', 'tagsFilterType': 'tagsFilterType', 'statuses': 'statuses'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'networkIds', 'productTypes', 'serials', 'tags', 'tagsFilterType', 'statuses'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationDevicesAvailabilities')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationDevicesAvailabilitiesChangeHistory')
def getOrganizationDevicesAvailabilitiesChangeHistory(organizationId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None, t0: str = None, t1: str = None, timespan: float = None, serials: list = None, productTypes: list = None, networkIds: list = None, statuses: list = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore', 't0': 't0', 't1': 't1', 'timespan': 'timespan', 'serials': 'serials', 'productTypes': 'productTypes', 'networkIds': 'networkIds', 'statuses': 'statuses'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 't0', 't1', 'timespan', 'serials', 'productTypes', 'networkIds', 'statuses'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationDevicesAvailabilitiesChangeHistory')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationDevicesOverviewByModel')
def getOrganizationDevicesOverviewByModel(organizationId: str, models: list = None, networkIds: list = None, productTypes: list = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'models': 'models', 'networkIds': 'networkIds', 'productTypes': 'productTypes'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'models', 'networkIds', 'productTypes'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationDevicesOverviewByModel')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationDevicesPowerModulesStatusesByDevice')
def getOrganizationDevicesPowerModulesStatusesByDevice(organizationId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None, networkIds: list = None, productTypes: list = None, serials: list = None, tags: list = None, tagsFilterType: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore', 'networkIds': 'networkIds', 'productTypes': 'productTypes', 'serials': 'serials', 'tags': 'tags', 'tagsFilterType': 'tagsFilterType'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'networkIds', 'productTypes', 'serials', 'tags', 'tagsFilterType'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationDevicesPowerModulesStatusesByDevice')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationDevicesProvisioningStatuses')
def getOrganizationDevicesProvisioningStatuses(organizationId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None, networkIds: list = None, productTypes: list = None, serials: list = None, status: str = None, tags: list = None, tagsFilterType: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore', 'networkIds': 'networkIds', 'productTypes': 'productTypes', 'serials': 'serials', 'status': 'status', 'tags': 'tags', 'tagsFilterType': 'tagsFilterType'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'networkIds', 'productTypes', 'serials', 'status', 'tags', 'tagsFilterType'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationDevicesProvisioningStatuses')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationDevicesStatuses')
def getOrganizationDevicesStatuses(organizationId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None, networkIds: list = None, serials: list = None, statuses: list = None, productTypes: list = None, models: list = None, tags: list = None, tagsFilterType: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore', 'networkIds': 'networkIds', 'serials': 'serials', 'statuses': 'statuses', 'productTypes': 'productTypes', 'models': 'models', 'tags': 'tags', 'tagsFilterType': 'tagsFilterType'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'networkIds', 'serials', 'statuses', 'productTypes', 'models', 'tags', 'tagsFilterType'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationDevicesStatuses')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationDevicesStatusesOverview')
def getOrganizationDevicesStatusesOverview(organizationId: str, productTypes: list = None, networkIds: list = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'productTypes': 'productTypes', 'networkIds': 'networkIds'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'productTypes', 'networkIds'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationDevicesStatusesOverview')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationDevicesUplinksAddressesByDevice')
def getOrganizationDevicesUplinksAddressesByDevice(organizationId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None, networkIds: list = None, productTypes: list = None, serials: list = None, tags: list = None, tagsFilterType: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore', 'networkIds': 'networkIds', 'productTypes': 'productTypes', 'serials': 'serials', 'tags': 'tags', 'tagsFilterType': 'tagsFilterType'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'networkIds', 'productTypes', 'serials', 'tags', 'tagsFilterType'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationDevicesUplinksAddressesByDevice')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationDevicesUplinksLossAndLatency')
def getOrganizationDevicesUplinksLossAndLatency(organizationId: str, t0: str = None, t1: str = None, timespan: float = None, uplink: str = None, ip: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 't0': 't0', 't1': 't1', 'timespan': 'timespan', 'uplink': 'uplink', 'ip': 'ip'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 't0', 't1', 'timespan', 'uplink', 'ip'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationDevicesUplinksLossAndLatency')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationEarlyAccessFeatures')
def getOrganizationEarlyAccessFeatures(organizationId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationEarlyAccessFeatures')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationEarlyAccessFeaturesOptIns')
def getOrganizationEarlyAccessFeaturesOptIns(organizationId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationEarlyAccessFeaturesOptIns')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationEarlyAccessFeaturesOptIn')
def getOrganizationEarlyAccessFeaturesOptIn(organizationId: str, optInId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'optInId': 'optInId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'optInId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationEarlyAccessFeaturesOptIn')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationFirmwareUpgrades')
def getOrganizationFirmwareUpgrades(organizationId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None, status: list = None, productTypes: list = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore', 'status': 'status', 'productTypes': 'productTypes'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'status', 'productTypes'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationFirmwareUpgrades')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationFirmwareUpgradesByDevice')
def getOrganizationFirmwareUpgradesByDevice(organizationId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None, networkIds: list = None, serials: list = None, macs: list = None, firmwareUpgradeBatchIds: list = None, upgradeStatuses: list = None, currentUpgradesOnly: bool = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore', 'networkIds': 'networkIds', 'serials': 'serials', 'macs': 'macs', 'firmwareUpgradeBatchIds': 'firmwareUpgradeBatchIds', 'upgradeStatuses': 'upgradeStatuses', 'currentUpgradesOnly': 'currentUpgradesOnly'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'networkIds', 'serials', 'macs', 'firmwareUpgradeBatchIds', 'upgradeStatuses', 'currentUpgradesOnly'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationFirmwareUpgradesByDevice')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationFloorPlansAutoLocateDevices')
def getOrganizationFloorPlansAutoLocateDevices(organizationId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None, networkIds: list = None, floorPlanIds: list = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore', 'networkIds': 'networkIds', 'floorPlanIds': 'floorPlanIds'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'networkIds', 'floorPlanIds'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationFloorPlansAutoLocateDevices')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationFloorPlansAutoLocateStatuses')
def getOrganizationFloorPlansAutoLocateStatuses(organizationId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None, networkIds: list = None, floorPlanIds: list = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore', 'networkIds': 'networkIds', 'floorPlanIds': 'floorPlanIds'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'networkIds', 'floorPlanIds'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationFloorPlansAutoLocateStatuses')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationInsightApplications')
def getOrganizationInsightApplications(organizationId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationInsightApplications')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationInsightMonitoredMediaServers')
def getOrganizationInsightMonitoredMediaServers(organizationId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationInsightMonitoredMediaServers')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationInsightMonitoredMediaServer')
def getOrganizationInsightMonitoredMediaServer(organizationId: str, monitoredMediaServerId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'monitoredMediaServerId': 'monitoredMediaServerId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'monitoredMediaServerId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationInsightMonitoredMediaServer')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationInventoryDevices')
def getOrganizationInventoryDevices(organizationId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None, usedState: str = None, search: str = None, macs: list = None, networkIds: list = None, serials: list = None, models: list = None, orderNumbers: list = None, tags: list = None, tagsFilterType: str = None, productTypes: list = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore', 'usedState': 'usedState', 'search': 'search', 'macs': 'macs', 'networkIds': 'networkIds', 'serials': 'serials', 'models': 'models', 'orderNumbers': 'orderNumbers', 'tags': 'tags', 'tagsFilterType': 'tagsFilterType', 'productTypes': 'productTypes'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'usedState', 'search', 'macs', 'networkIds', 'serials', 'models', 'orderNumbers', 'tags', 'tagsFilterType', 'productTypes'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationInventoryDevices')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationInventoryDevicesSwapsBulk')
def getOrganizationInventoryDevicesSwapsBulk(organizationId: str, id: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'id': 'id'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'id'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationInventoryDevicesSwapsBulk')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationInventoryDevice')
def getOrganizationInventoryDevice(organizationId: str, serial: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'serial': 'serial'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'serial'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationInventoryDevice')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationInventoryOnboardingCloudMonitoringImports')
def getOrganizationInventoryOnboardingCloudMonitoringImports(organizationId: str, importIds: list):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'importIds': 'importIds'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'importIds'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationInventoryOnboardingCloudMonitoringImports')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationInventoryOnboardingCloudMonitoringNetworks')
def getOrganizationInventoryOnboardingCloudMonitoringNetworks(organizationId: str, deviceType: str, search: str = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'deviceType': 'deviceType', 'search': 'search', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'deviceType', 'search', 'perPage', 'startingAfter', 'endingBefore'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationInventoryOnboardingCloudMonitoringNetworks')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationLicenses')
def getOrganizationLicenses(organizationId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None, deviceSerial: str = None, networkId: str = None, state: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore', 'deviceSerial': 'deviceSerial', 'networkId': 'networkId', 'state': 'state'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'deviceSerial', 'networkId', 'state'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationLicenses')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationLicensesOverview')
def getOrganizationLicensesOverview(organizationId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationLicensesOverview')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationLicense')
def getOrganizationLicense(organizationId: str, licenseId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'licenseId': 'licenseId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'licenseId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationLicense')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationLicensingCotermLicenses')
def getOrganizationLicensingCotermLicenses(organizationId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None, invalidated: bool = None, expired: bool = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore', 'invalidated': 'invalidated', 'expired': 'expired'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'invalidated', 'expired'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationLicensingCotermLicenses')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationLoginSecurity')
def getOrganizationLoginSecurity(organizationId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationLoginSecurity')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationNetworks')
def getOrganizationNetworks(organizationId: str, configTemplateId: str = None, isBoundToConfigTemplate: bool = None, tags: list = None, tagsFilterType: str = None, productTypes: list = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'configTemplateId': 'configTemplateId', 'isBoundToConfigTemplate': 'isBoundToConfigTemplate', 'tags': 'tags', 'tagsFilterType': 'tagsFilterType', 'productTypes': 'productTypes', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'configTemplateId', 'isBoundToConfigTemplate', 'tags', 'tagsFilterType', 'productTypes', 'perPage', 'startingAfter', 'endingBefore'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationNetworks')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationOpenapiSpec')
def getOrganizationOpenapiSpec(organizationId: str, version: int = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'version': 'version'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'version'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationOpenapiSpec')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationPolicyObjects')
def getOrganizationPolicyObjects(organizationId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'perPage', 'startingAfter', 'endingBefore'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationPolicyObjects')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationPolicyObjectsGroups')
def getOrganizationPolicyObjectsGroups(organizationId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'perPage', 'startingAfter', 'endingBefore'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationPolicyObjectsGroups')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationPolicyObjectsGroup')
def getOrganizationPolicyObjectsGroup(organizationId: str, policyObjectGroupId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'policyObjectGroupId': 'policyObjectGroupId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'policyObjectGroupId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationPolicyObjectsGroup')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationPolicyObject')
def getOrganizationPolicyObject(organizationId: str, policyObjectId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'policyObjectId': 'policyObjectId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'policyObjectId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationPolicyObject')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSaml')
def getOrganizationSaml(organizationId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationSaml')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSamlIdps')
def getOrganizationSamlIdps(organizationId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationSamlIdps')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSamlIdp')
def getOrganizationSamlIdp(organizationId: str, idpId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'idpId': 'idpId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'idpId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationSamlIdp')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSamlRoles')
def getOrganizationSamlRoles(organizationId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationSamlRoles')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSamlRole')
def getOrganizationSamlRole(organizationId: str, samlRoleId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'samlRoleId': 'samlRoleId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'samlRoleId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationSamlRole')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSensorReadingsHistory')
def getOrganizationSensorReadingsHistory(organizationId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None, t0: str = None, t1: str = None, timespan: float = None, networkIds: list = None, serials: list = None, metrics: list = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore', 't0': 't0', 't1': 't1', 'timespan': 'timespan', 'networkIds': 'networkIds', 'serials': 'serials', 'metrics': 'metrics'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 't0', 't1', 'timespan', 'networkIds', 'serials', 'metrics'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationSensorReadingsHistory')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSensorReadingsLatest')
def getOrganizationSensorReadingsLatest(organizationId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None, networkIds: list = None, serials: list = None, metrics: list = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore', 'networkIds': 'networkIds', 'serials': 'serials', 'metrics': 'metrics'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'networkIds', 'serials', 'metrics'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationSensorReadingsLatest')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSmAdminsRoles')
def getOrganizationSmAdminsRoles(organizationId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'perPage', 'startingAfter', 'endingBefore'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationSmAdminsRoles')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSmAdminsRole')
def getOrganizationSmAdminsRole(organizationId: str, roleId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'roleId': 'roleId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'roleId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationSmAdminsRole')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSmApnsCert')
def getOrganizationSmApnsCert(organizationId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationSmApnsCert')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSmSentryPoliciesAssignmentsByNetwork')
def getOrganizationSmSentryPoliciesAssignmentsByNetwork(organizationId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None, networkIds: list = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore', 'networkIds': 'networkIds'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'networkIds'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationSmSentryPoliciesAssignmentsByNetwork')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSmVppAccounts')
def getOrganizationSmVppAccounts(organizationId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationSmVppAccounts')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSmVppAccount')
def getOrganizationSmVppAccount(organizationId: str, vppAccountId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'vppAccountId': 'vppAccountId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'vppAccountId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationSmVppAccount')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSnmp')
def getOrganizationSnmp(organizationId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationSnmp')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSplashAsset')
def getOrganizationSplashAsset(organizationId: str, id: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'id': 'id'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'id'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationSplashAsset')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSplashThemes')
def getOrganizationSplashThemes(organizationId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationSplashThemes')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSummarySwitchPowerHistory')
def getOrganizationSummarySwitchPowerHistory(organizationId: str, t0: str = None, t1: str = None, timespan: float = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 't0': 't0', 't1': 't1', 'timespan': 'timespan'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 't0', 't1', 'timespan'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationSummarySwitchPowerHistory')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSummaryTopAppliancesByUtilization')
def getOrganizationSummaryTopAppliancesByUtilization(organizationId: str, networkTag: str = None, deviceTag: str = None, quantity: int = None, ssidName: str = None, usageUplink: str = None, t0: str = None, t1: str = None, timespan: float = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'networkTag': 'networkTag', 'deviceTag': 'deviceTag', 'quantity': 'quantity', 'ssidName': 'ssidName', 'usageUplink': 'usageUplink', 't0': 't0', 't1': 't1', 'timespan': 'timespan'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'networkTag', 'deviceTag', 'quantity', 'ssidName', 'usageUplink', 't0', 't1', 'timespan'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationSummaryTopAppliancesByUtilization')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSummaryTopApplicationsByUsage')
def getOrganizationSummaryTopApplicationsByUsage(organizationId: str, networkTag: str = None, device: str = None, networkId: str = None, quantity: int = None, ssidName: str = None, usageUplink: str = None, t0: str = None, t1: str = None, timespan: float = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'networkTag': 'networkTag', 'device': 'device', 'networkId': 'networkId', 'quantity': 'quantity', 'ssidName': 'ssidName', 'usageUplink': 'usageUplink', 't0': 't0', 't1': 't1', 'timespan': 'timespan'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'networkTag', 'device', 'networkId', 'quantity', 'ssidName', 'usageUplink', 't0', 't1', 'timespan'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationSummaryTopApplicationsByUsage')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSummaryTopApplicationsCategoriesByUsage')
def getOrganizationSummaryTopApplicationsCategoriesByUsage(organizationId: str, networkTag: str = None, deviceTag: str = None, networkId: str = None, quantity: int = None, ssidName: str = None, usageUplink: str = None, t0: str = None, t1: str = None, timespan: float = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'networkTag': 'networkTag', 'deviceTag': 'deviceTag', 'networkId': 'networkId', 'quantity': 'quantity', 'ssidName': 'ssidName', 'usageUplink': 'usageUplink', 't0': 't0', 't1': 't1', 'timespan': 'timespan'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'networkTag', 'deviceTag', 'networkId', 'quantity', 'ssidName', 'usageUplink', 't0', 't1', 'timespan'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationSummaryTopApplicationsCategoriesByUsage')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSummaryTopClientsByUsage')
def getOrganizationSummaryTopClientsByUsage(organizationId: str, networkTag: str = None, deviceTag: str = None, quantity: int = None, ssidName: str = None, usageUplink: str = None, t0: str = None, t1: str = None, timespan: float = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'networkTag': 'networkTag', 'deviceTag': 'deviceTag', 'quantity': 'quantity', 'ssidName': 'ssidName', 'usageUplink': 'usageUplink', 't0': 't0', 't1': 't1', 'timespan': 'timespan'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'networkTag', 'deviceTag', 'quantity', 'ssidName', 'usageUplink', 't0', 't1', 'timespan'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationSummaryTopClientsByUsage')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSummaryTopClientsManufacturersByUsage')
def getOrganizationSummaryTopClientsManufacturersByUsage(organizationId: str, networkTag: str = None, deviceTag: str = None, quantity: int = None, ssidName: str = None, usageUplink: str = None, t0: str = None, t1: str = None, timespan: float = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'networkTag': 'networkTag', 'deviceTag': 'deviceTag', 'quantity': 'quantity', 'ssidName': 'ssidName', 'usageUplink': 'usageUplink', 't0': 't0', 't1': 't1', 'timespan': 'timespan'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'networkTag', 'deviceTag', 'quantity', 'ssidName', 'usageUplink', 't0', 't1', 'timespan'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationSummaryTopClientsManufacturersByUsage')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSummaryTopDevicesByUsage')
def getOrganizationSummaryTopDevicesByUsage(organizationId: str, networkTag: str = None, deviceTag: str = None, quantity: int = None, ssidName: str = None, usageUplink: str = None, t0: str = None, t1: str = None, timespan: float = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'networkTag': 'networkTag', 'deviceTag': 'deviceTag', 'quantity': 'quantity', 'ssidName': 'ssidName', 'usageUplink': 'usageUplink', 't0': 't0', 't1': 't1', 'timespan': 'timespan'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'networkTag', 'deviceTag', 'quantity', 'ssidName', 'usageUplink', 't0', 't1', 'timespan'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationSummaryTopDevicesByUsage')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSummaryTopDevicesModelsByUsage')
def getOrganizationSummaryTopDevicesModelsByUsage(organizationId: str, networkTag: str = None, deviceTag: str = None, quantity: int = None, ssidName: str = None, usageUplink: str = None, t0: str = None, t1: str = None, timespan: float = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'networkTag': 'networkTag', 'deviceTag': 'deviceTag', 'quantity': 'quantity', 'ssidName': 'ssidName', 'usageUplink': 'usageUplink', 't0': 't0', 't1': 't1', 'timespan': 'timespan'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'networkTag', 'deviceTag', 'quantity', 'ssidName', 'usageUplink', 't0', 't1', 'timespan'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationSummaryTopDevicesModelsByUsage')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSummaryTopNetworksByStatus')
def getOrganizationSummaryTopNetworksByStatus(organizationId: str, networkTag: str = None, deviceTag: str = None, quantity: int = None, ssidName: str = None, usageUplink: str = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'networkTag': 'networkTag', 'deviceTag': 'deviceTag', 'quantity': 'quantity', 'ssidName': 'ssidName', 'usageUplink': 'usageUplink', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'networkTag', 'deviceTag', 'quantity', 'ssidName', 'usageUplink', 'perPage', 'startingAfter', 'endingBefore'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationSummaryTopNetworksByStatus')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSummaryTopSsidsByUsage')
def getOrganizationSummaryTopSsidsByUsage(organizationId: str, networkTag: str = None, deviceTag: str = None, quantity: int = None, ssidName: str = None, usageUplink: str = None, t0: str = None, t1: str = None, timespan: float = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'networkTag': 'networkTag', 'deviceTag': 'deviceTag', 'quantity': 'quantity', 'ssidName': 'ssidName', 'usageUplink': 'usageUplink', 't0': 't0', 't1': 't1', 'timespan': 'timespan'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'networkTag', 'deviceTag', 'quantity', 'ssidName', 'usageUplink', 't0', 't1', 'timespan'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationSummaryTopSsidsByUsage')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSummaryTopSwitchesByEnergyUsage')
def getOrganizationSummaryTopSwitchesByEnergyUsage(organizationId: str, networkTag: str = None, deviceTag: str = None, quantity: int = None, ssidName: str = None, usageUplink: str = None, t0: str = None, t1: str = None, timespan: float = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'networkTag': 'networkTag', 'deviceTag': 'deviceTag', 'quantity': 'quantity', 'ssidName': 'ssidName', 'usageUplink': 'usageUplink', 't0': 't0', 't1': 't1', 'timespan': 'timespan'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'networkTag', 'deviceTag', 'quantity', 'ssidName', 'usageUplink', 't0', 't1', 'timespan'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationSummaryTopSwitchesByEnergyUsage')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSwitchPortsBySwitch')
def getOrganizationSwitchPortsBySwitch(organizationId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None, configurationUpdatedAfter: str = None, mac: str = None, macs: list = None, name: str = None, networkIds: list = None, portProfileIds: list = None, serial: str = None, serials: list = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore', 'configurationUpdatedAfter': 'configurationUpdatedAfter', 'mac': 'mac', 'macs': 'macs', 'name': 'name', 'networkIds': 'networkIds', 'portProfileIds': 'portProfileIds', 'serial': 'serial', 'serials': 'serials'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'configurationUpdatedAfter', 'mac', 'macs', 'name', 'networkIds', 'portProfileIds', 'serial', 'serials'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationSwitchPortsBySwitch')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSwitchPortsClientsOverviewByDevice')
def getOrganizationSwitchPortsClientsOverviewByDevice(organizationId: str, t0: str = None, timespan: float = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None, configurationUpdatedAfter: str = None, mac: str = None, macs: list = None, name: str = None, networkIds: list = None, portProfileIds: list = None, serial: str = None, serials: list = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 't0': 't0', 'timespan': 'timespan', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore', 'configurationUpdatedAfter': 'configurationUpdatedAfter', 'mac': 'mac', 'macs': 'macs', 'name': 'name', 'networkIds': 'networkIds', 'portProfileIds': 'portProfileIds', 'serial': 'serial', 'serials': 'serials'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 't0', 'timespan', 'perPage', 'startingAfter', 'endingBefore', 'configurationUpdatedAfter', 'mac', 'macs', 'name', 'networkIds', 'portProfileIds', 'serial', 'serials'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationSwitchPortsClientsOverviewByDevice')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSwitchPortsOverview')
def getOrganizationSwitchPortsOverview(organizationId: str, t0: str = None, t1: str = None, timespan: float = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 't0': 't0', 't1': 't1', 'timespan': 'timespan'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 't0', 't1', 'timespan'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationSwitchPortsOverview')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSwitchPortsStatusesBySwitch')
def getOrganizationSwitchPortsStatusesBySwitch(organizationId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None, configurationUpdatedAfter: str = None, mac: str = None, macs: list = None, name: str = None, networkIds: list = None, portProfileIds: list = None, serial: str = None, serials: list = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore', 'configurationUpdatedAfter': 'configurationUpdatedAfter', 'mac': 'mac', 'macs': 'macs', 'name': 'name', 'networkIds': 'networkIds', 'portProfileIds': 'portProfileIds', 'serial': 'serial', 'serials': 'serials'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'configurationUpdatedAfter', 'mac', 'macs', 'name', 'networkIds', 'portProfileIds', 'serial', 'serials'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationSwitchPortsStatusesBySwitch')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationSwitchPortsTopologyDiscoveryByDevice')
def getOrganizationSwitchPortsTopologyDiscoveryByDevice(organizationId: str, t0: str = None, timespan: float = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None, configurationUpdatedAfter: str = None, mac: str = None, macs: list = None, name: str = None, networkIds: list = None, portProfileIds: list = None, serial: str = None, serials: list = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 't0': 't0', 'timespan': 'timespan', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore', 'configurationUpdatedAfter': 'configurationUpdatedAfter', 'mac': 'mac', 'macs': 'macs', 'name': 'name', 'networkIds': 'networkIds', 'portProfileIds': 'portProfileIds', 'serial': 'serial', 'serials': 'serials'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 't0', 'timespan', 'perPage', 'startingAfter', 'endingBefore', 'configurationUpdatedAfter', 'mac', 'macs', 'name', 'networkIds', 'portProfileIds', 'serial', 'serials'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationSwitchPortsTopologyDiscoveryByDevice')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationUplinksStatuses')
def getOrganizationUplinksStatuses(organizationId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None, networkIds: list = None, serials: list = None, iccids: list = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore', 'networkIds': 'networkIds', 'serials': 'serials', 'iccids': 'iccids'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'networkIds', 'serials', 'iccids'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationUplinksStatuses')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationWebhooksAlertTypes')
def getOrganizationWebhooksAlertTypes(organizationId: str, productType: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'productType': 'productType'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'productType'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationWebhooksAlertTypes')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationWebhooksCallbacksStatus')
def getOrganizationWebhooksCallbacksStatus(organizationId: str, callbackId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'callbackId': 'callbackId'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'callbackId'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationWebhooksCallbacksStatus')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationWebhooksLogs')
def getOrganizationWebhooksLogs(organizationId: str, t0: str = None, t1: str = None, timespan: float = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None, url: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 't0': 't0', 't1': 't1', 'timespan': 'timespan', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore', 'url': 'url'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 't0', 't1', 'timespan', 'perPage', 'startingAfter', 'endingBefore', 'url'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationWebhooksLogs')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationWirelessAirMarshalRules')
def getOrganizationWirelessAirMarshalRules(organizationId: str, networkIds: list = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'networkIds': 'networkIds', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'networkIds', 'perPage', 'startingAfter', 'endingBefore'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationWirelessAirMarshalRules')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationWirelessAirMarshalSettingsByNetwork')
def getOrganizationWirelessAirMarshalSettingsByNetwork(organizationId: str, networkIds: list = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'networkIds': 'networkIds', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'networkIds', 'perPage', 'startingAfter', 'endingBefore'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationWirelessAirMarshalSettingsByNetwork')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationWirelessClientsOverviewByDevice')
def getOrganizationWirelessClientsOverviewByDevice(organizationId: str, networkIds: list = None, serials: list = None, campusGatewayClusterIds: list = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'networkIds': 'networkIds', 'serials': 'serials', 'campusGatewayClusterIds': 'campusGatewayClusterIds', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'networkIds', 'serials', 'campusGatewayClusterIds', 'perPage', 'startingAfter', 'endingBefore'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationWirelessClientsOverviewByDevice')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationWirelessDevicesChannelUtilizationByDevice')
def getOrganizationWirelessDevicesChannelUtilizationByDevice(organizationId: str, networkIds: list = None, serials: list = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None, t0: str = None, t1: str = None, timespan: float = None, interval: int = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'networkIds': 'networkIds', 'serials': 'serials', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore', 't0': 't0', 't1': 't1', 'timespan': 'timespan', 'interval': 'interval'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'networkIds', 'serials', 'perPage', 'startingAfter', 'endingBefore', 't0', 't1', 'timespan', 'interval'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationWirelessDevicesChannelUtilizationByDevice')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationWirelessDevicesChannelUtilizationByNetwork')
def getOrganizationWirelessDevicesChannelUtilizationByNetwork(organizationId: str, networkIds: list = None, serials: list = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None, t0: str = None, t1: str = None, timespan: float = None, interval: int = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'networkIds': 'networkIds', 'serials': 'serials', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore', 't0': 't0', 't1': 't1', 'timespan': 'timespan', 'interval': 'interval'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'networkIds', 'serials', 'perPage', 'startingAfter', 'endingBefore', 't0', 't1', 'timespan', 'interval'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationWirelessDevicesChannelUtilizationByNetwork')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationWirelessDevicesChannelUtilizationHistoryByDeviceB')
def getOrganizationWirelessDevicesChannelUtilizationHistoryByDeviceB(organizationId: str, networkIds: list = None, serials: list = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None, t0: str = None, t1: str = None, timespan: float = None, interval: int = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'networkIds': 'networkIds', 'serials': 'serials', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore', 't0': 't0', 't1': 't1', 'timespan': 'timespan', 'interval': 'interval'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'networkIds', 'serials', 'perPage', 'startingAfter', 'endingBefore', 't0', 't1', 'timespan', 'interval'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationWirelessDevicesChannelUtilizationHistoryByDeviceB')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationWirelessDevicesChannelUtilizationHistoryByNetwork')
def getOrganizationWirelessDevicesChannelUtilizationHistoryByNetwork(organizationId: str, networkIds: list = None, serials: list = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None, t0: str = None, t1: str = None, timespan: float = None, interval: int = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'networkIds': 'networkIds', 'serials': 'serials', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore', 't0': 't0', 't1': 't1', 'timespan': 'timespan', 'interval': 'interval'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'networkIds', 'serials', 'perPage', 'startingAfter', 'endingBefore', 't0', 't1', 'timespan', 'interval'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationWirelessDevicesChannelUtilizationHistoryByNetwork')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationWirelessDevicesEthernetStatuses')
def getOrganizationWirelessDevicesEthernetStatuses(organizationId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None, networkIds: list = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore', 'networkIds': 'networkIds'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'networkIds'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationWirelessDevicesEthernetStatuses')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationWirelessDevicesPacketLossByClient')
def getOrganizationWirelessDevicesPacketLossByClient(organizationId: str, networkIds: list = None, ssids: list = None, bands: list = None, macs: list = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None, t0: str = None, t1: str = None, timespan: float = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'networkIds': 'networkIds', 'ssids': 'ssids', 'bands': 'bands', 'macs': 'macs', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore', 't0': 't0', 't1': 't1', 'timespan': 'timespan'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'networkIds', 'ssids', 'bands', 'macs', 'perPage', 'startingAfter', 'endingBefore', 't0', 't1', 'timespan'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationWirelessDevicesPacketLossByClient')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationWirelessDevicesPacketLossByDevice')
def getOrganizationWirelessDevicesPacketLossByDevice(organizationId: str, networkIds: list = None, serials: list = None, ssids: list = None, bands: list = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None, t0: str = None, t1: str = None, timespan: float = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'networkIds': 'networkIds', 'serials': 'serials', 'ssids': 'ssids', 'bands': 'bands', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore', 't0': 't0', 't1': 't1', 'timespan': 'timespan'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'networkIds', 'serials', 'ssids', 'bands', 'perPage', 'startingAfter', 'endingBefore', 't0', 't1', 'timespan'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationWirelessDevicesPacketLossByDevice')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationWirelessDevicesPacketLossByNetwork')
def getOrganizationWirelessDevicesPacketLossByNetwork(organizationId: str, networkIds: list = None, serials: list = None, ssids: list = None, bands: list = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None, t0: str = None, t1: str = None, timespan: float = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'networkIds': 'networkIds', 'serials': 'serials', 'ssids': 'ssids', 'bands': 'bands', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore', 't0': 't0', 't1': 't1', 'timespan': 'timespan'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'networkIds', 'serials', 'ssids', 'bands', 'perPage', 'startingAfter', 'endingBefore', 't0', 't1', 'timespan'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationWirelessDevicesPacketLossByNetwork')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationWirelessDevicesWirelessControllersByDevice')
def getOrganizationWirelessDevicesWirelessControllersByDevice(organizationId: str, networkIds: list = None, serials: list = None, controllerSerials: list = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'networkIds': 'networkIds', 'serials': 'serials', 'controllerSerials': 'controllerSerials', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'networkIds', 'serials', 'controllerSerials', 'perPage', 'startingAfter', 'endingBefore'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationWirelessDevicesWirelessControllersByDevice')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationWirelessRfProfilesAssignmentsByDevice')
def getOrganizationWirelessRfProfilesAssignmentsByDevice(organizationId: str, perPage: int = None, startingAfter: str = None, endingBefore: str = None, networkIds: list = None, productTypes: list = None, name: str = None, mac: str = None, serial: str = None, model: str = None, macs: list = None, serials: list = None, models: list = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore', 'networkIds': 'networkIds', 'productTypes': 'productTypes', 'name': 'name', 'mac': 'mac', 'serial': 'serial', 'model': 'model', 'macs': 'macs', 'serials': 'serials', 'models': 'models'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'perPage', 'startingAfter', 'endingBefore', 'networkIds', 'productTypes', 'name', 'mac', 'serial', 'model', 'macs', 'serials', 'models'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationWirelessRfProfilesAssignmentsByDevice')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationWirelessSsidsStatusesByDevice')
def getOrganizationWirelessSsidsStatusesByDevice(organizationId: str, networkIds: list = None, serials: list = None, bssids: list = None, hideDisabled: bool = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'networkIds': 'networkIds', 'serials': 'serials', 'bssids': 'bssids', 'hideDisabled': 'hideDisabled', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'networkIds', 'serials', 'bssids', 'hideDisabled', 'perPage', 'startingAfter', 'endingBefore'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationWirelessSsidsStatusesByDevice')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationWirelessControllerAvailabilitiesChangeHistory')
def getOrganizationWirelessControllerAvailabilitiesChangeHistory(organizationId: str, serials: list = None, t0: str = None, t1: str = None, timespan: float = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'serials': 'serials', 't0': 't0', 't1': 't1', 'timespan': 'timespan', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'serials', 't0', 't1', 'timespan', 'perPage', 'startingAfter', 'endingBefore'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationWirelessControllerAvailabilitiesChangeHistory')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationWirelessControllerClientsOverviewHistoryByDeviceB')
def getOrganizationWirelessControllerClientsOverviewHistoryByDeviceB(organizationId: str, networkIds: list = None, serials: list = None, t0: str = None, t1: str = None, timespan: float = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None, resolution: int = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'networkIds': 'networkIds', 'serials': 'serials', 't0': 't0', 't1': 't1', 'timespan': 'timespan', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore', 'resolution': 'resolution'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'networkIds', 'serials', 't0', 't1', 'timespan', 'perPage', 'startingAfter', 'endingBefore', 'resolution'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationWirelessControllerClientsOverviewHistoryByDeviceB')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationWirelessControllerConnections')
def getOrganizationWirelessControllerConnections(organizationId: str, networkIds: list = None, controllerSerials: list = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'networkIds': 'networkIds', 'controllerSerials': 'controllerSerials', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'networkIds', 'controllerSerials', 'perPage', 'startingAfter', 'endingBefore'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationWirelessControllerConnections')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationWirelessControllerDevicesInterfacesL2ByDevice')
def getOrganizationWirelessControllerDevicesInterfacesL2ByDevice(organizationId: str, serials: list = None, t0: str = None, t1: str = None, timespan: float = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'serials': 'serials', 't0': 't0', 't1': 't1', 'timespan': 'timespan', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'serials', 't0', 't1', 'timespan', 'perPage', 'startingAfter', 'endingBefore'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationWirelessControllerDevicesInterfacesL2ByDevice')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationWirelessControllerDevicesInterfacesL2StatusesChan')
def getOrganizationWirelessControllerDevicesInterfacesL2StatusesChan(organizationId: str, serials: list = None, includeInterfacesWithoutChanges: bool = None, t0: str = None, t1: str = None, timespan: float = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'serials': 'serials', 'includeInterfacesWithoutChanges': 'includeInterfacesWithoutChanges', 't0': 't0', 't1': 't1', 'timespan': 'timespan', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'serials', 'includeInterfacesWithoutChanges', 't0', 't1', 'timespan', 'perPage', 'startingAfter', 'endingBefore'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationWirelessControllerDevicesInterfacesL2StatusesChan')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationWirelessControllerDevicesInterfacesL2UsageHistory')
def getOrganizationWirelessControllerDevicesInterfacesL2UsageHistory(organizationId: str, serials: list = None, t0: str = None, t1: str = None, timespan: float = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'serials': 'serials', 't0': 't0', 't1': 't1', 'timespan': 'timespan', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'serials', 't0', 't1', 'timespan', 'perPage', 'startingAfter', 'endingBefore'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationWirelessControllerDevicesInterfacesL2UsageHistory')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationWirelessControllerDevicesInterfacesL3ByDevice')
def getOrganizationWirelessControllerDevicesInterfacesL3ByDevice(organizationId: str, serials: list = None, t0: str = None, t1: str = None, timespan: float = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'serials': 'serials', 't0': 't0', 't1': 't1', 'timespan': 'timespan', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'serials', 't0', 't1', 'timespan', 'perPage', 'startingAfter', 'endingBefore'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationWirelessControllerDevicesInterfacesL3ByDevice')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationWirelessControllerDevicesInterfacesL3StatusesChan')
def getOrganizationWirelessControllerDevicesInterfacesL3StatusesChan(organizationId: str, serials: list = None, includeInterfacesWithoutChanges: bool = None, t0: str = None, t1: str = None, timespan: float = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'serials': 'serials', 'includeInterfacesWithoutChanges': 'includeInterfacesWithoutChanges', 't0': 't0', 't1': 't1', 'timespan': 'timespan', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'serials', 'includeInterfacesWithoutChanges', 't0', 't1', 'timespan', 'perPage', 'startingAfter', 'endingBefore'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationWirelessControllerDevicesInterfacesL3StatusesChan')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationWirelessControllerDevicesInterfacesL3UsageHistory')
def getOrganizationWirelessControllerDevicesInterfacesL3UsageHistory(organizationId: str, serials: list = None, t0: str = None, t1: str = None, timespan: float = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'serials': 'serials', 't0': 't0', 't1': 't1', 'timespan': 'timespan', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'serials', 't0', 't1', 'timespan', 'perPage', 'startingAfter', 'endingBefore'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationWirelessControllerDevicesInterfacesL3UsageHistory')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationWirelessControllerDevicesInterfacesPacketsOvervie')
def getOrganizationWirelessControllerDevicesInterfacesPacketsOvervie(organizationId: str, serials: list = None, names: list = None, t0: str = None, t1: str = None, timespan: float = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'serials': 'serials', 'names': 'names', 't0': 't0', 't1': 't1', 'timespan': 'timespan', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'serials', 'names', 't0', 't1', 'timespan', 'perPage', 'startingAfter', 'endingBefore'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationWirelessControllerDevicesInterfacesPacketsOvervie')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationWirelessControllerDevicesInterfacesUsageHistoryBy')
def getOrganizationWirelessControllerDevicesInterfacesUsageHistoryBy(organizationId: str, serials: list = None, names: list = None, t0: str = None, t1: str = None, timespan: float = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'serials': 'serials', 'names': 'names', 't0': 't0', 't1': 't1', 'timespan': 'timespan', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'serials', 'names', 't0', 't1', 'timespan', 'perPage', 'startingAfter', 'endingBefore'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationWirelessControllerDevicesInterfacesUsageHistoryBy')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationWirelessControllerDevicesRedundancyFailoverHistor')
def getOrganizationWirelessControllerDevicesRedundancyFailoverHistor(organizationId: str, serials: list = None, t0: str = None, t1: str = None, timespan: float = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'serials': 'serials', 't0': 't0', 't1': 't1', 'timespan': 'timespan', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'serials', 't0', 't1', 'timespan', 'perPage', 'startingAfter', 'endingBefore'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationWirelessControllerDevicesRedundancyFailoverHistor')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationWirelessControllerDevicesRedundancyStatuses')
def getOrganizationWirelessControllerDevicesRedundancyStatuses(organizationId: str, serials: list = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'serials': 'serials', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'serials', 'perPage', 'startingAfter', 'endingBefore'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationWirelessControllerDevicesRedundancyStatuses')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationWirelessControllerDevicesSystemUtilizationHistory')
def getOrganizationWirelessControllerDevicesSystemUtilizationHistory(organizationId: str, serials: list = None, t0: str = None, t1: str = None, timespan: float = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'serials': 'serials', 't0': 't0', 't1': 't1', 'timespan': 'timespan', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'serials', 't0', 't1', 'timespan', 'perPage', 'startingAfter', 'endingBefore'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationWirelessControllerDevicesSystemUtilizationHistory')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationWirelessControllerOverviewByDevice')
def getOrganizationWirelessControllerOverviewByDevice(organizationId: str, networkIds: list = None, serials: list = None, perPage: int = None, startingAfter: str = None, endingBefore: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'organizationId': 'organizationId', 'networkIds': 'networkIds', 'serials': 'serials', 'perPage': 'perPage', 'startingAfter': 'startingAfter', 'endingBefore': 'endingBefore'}.items()
        if locals_[san] is not None
    }

    # ── auto‑inject MERAKI_ORG_ID ───────────────────────────────
    org_env = os.getenv('MERAKI_ORG_ID')
    if org_env:
        for cand in ('organization_id', 'organizationId', 'org_id'):
            if cand in ['organizationId', 'networkIds', 'serials', 'perPage', 'startingAfter', 'endingBefore'] and cand not in final_kwargs:
                final_kwargs[cand] = org_env
                break

    target = MerakiClient().__getattr__('getOrganizationWirelessControllerOverviewByDevice')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)
