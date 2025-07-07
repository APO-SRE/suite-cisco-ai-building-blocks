# app/llm/function_dispatcher/catalyst_dispatcher.py
import os
from typing import Any
from app.llm.function_dispatcher import register
from app.llm.platform_clients.catalyst_client import CatalystClient

@register('retrievesNetworkDeviceProductNamesAssignedToASoftwareImage.')
def retrievesNetworkDeviceProductNamesAssignedToASoftwareImage_(imageId: str, productName: str = None, productId: str = None, recommended: str = None, assigned: str = None, offset: float = None, limit: float = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'imageId': 'imageId', 'productName': 'productName', 'productId': 'productId', 'recommended': 'recommended', 'assigned': 'assigned', 'offset': 'offset', 'limit': 'limit'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('retrievesNetworkDeviceProductNamesAssignedToASoftwareImage_')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getsAllTheVersionsOfAGivenTemplate')
def getsAllTheVersionsOfAGivenTemplate(templateId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'templateId': 'templateId'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getsAllTheVersionsOfAGivenTemplate')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('returnsTheCountOfNetworkDeviceProductNamesForASite')
def returnsTheCountOfNetworkDeviceProductNamesForASite(siteId: str = None, productName: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'siteId': 'siteId', 'productName': 'productName'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('returnsTheCountOfNetworkDeviceProductNamesForASite')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getMulticastVirtualNetworks')
def getMulticastVirtualNetworks(fabricId: str = None, virtualNetworkName: str = None, offset: float = None, limit: float = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'fabricId': 'fabricId', 'virtualNetworkName': 'virtualNetworkName', 'offset': 'offset', 'limit': 'limit'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getMulticastVirtualNetworks')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceControllabilitySettings')
def getDeviceControllabilitySettings():
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getDeviceControllabilitySettings')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getChassisDetailsForDevice')
def getChassisDetailsForDevice(deviceId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'deviceId': 'deviceId'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getChassisDetailsForDevice')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getsABuilding')
def getsABuilding(id: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'id': 'id'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getsABuilding')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getCountOfAllDiscoveryJobs')
def getCountOfAllDiscoveryJobs():
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getCountOfAllDiscoveryJobs')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getViewsForAGivenViewGroup')
def getViewsForAGivenViewGroup(viewGroupId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'viewGroupId': 'viewGroupId'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getViewsForAGivenViewGroup')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceById')
def getDeviceById(id: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'id': 'id'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getDeviceById')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('retrieveTheVLANsAndSSIDsMappedToTheVLANWithinAFabricSite.')
def retrieveTheVLANsAndSSIDsMappedToTheVLANWithinAFabricSite_(Content_Type: str, fabricId: str, limit: float = None, offset: float = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'Content-Type': 'Content_Type', 'fabricId': 'fabricId', 'limit': 'limit', 'offset': 'offset'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('retrieveTheVLANsAndSSIDsMappedToTheVLANWithinAFabricSite_')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('retrieveImageDistributionServers')
def retrieveImageDistributionServers():
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('retrieveImageDistributionServers')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('retrieveTagsAssociatedWithNetworkDevices.')
def retrieveTagsAssociatedWithNetworkDevices_(offset: float = None, limit: float = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'offset': 'offset', 'limit': 'limit'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('retrieveTagsAssociatedWithNetworkDevices_')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('statusOfTemplateDeployment')
def statusOfTemplateDeployment(deploymentId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'deploymentId': 'deploymentId'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('statusOfTemplateDeployment')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getIssueTriggerDefinitionForGivenId.')
def getIssueTriggerDefinitionForGivenId_(id: str, X_CALLER_ID: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'X-CALLER-ID': 'X_CALLER_ID', 'id': 'id'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getIssueTriggerDefinitionForGivenId_')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('retrieveBannerSettingsForASite')
def retrieveBannerSettingsForASite(id: str, _inherited: bool = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'id': 'id', '_inherited': '_inherited'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('retrieveBannerSettingsForASite')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getSiteAssignedNetworkDevices')
def getSiteAssignedNetworkDevices(siteId: str, offset: float = None, limit: float = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'siteId': 'siteId', 'offset': 'offset', 'limit': 'limit'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getSiteAssignedNetworkDevices')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkDevicesCredentialsSyncStatus')
def getNetworkDevicesCredentialsSyncStatus(id: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'id': 'id'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getNetworkDevicesCredentialsSyncStatus')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getSoftwareImageDetails')
def getSoftwareImageDetails(imageUuid: str = None, name: str = None, family: str = None, applicationType: str = None, imageIntegrityStatus: str = None, version: str = None, imageSeries: str = None, imageName: str = None, isTaggedGolden: bool = None, isCCORecommended: bool = None, isCCOLatest: bool = None, createdTime: int = None, imageSizeGreaterThan: int = None, imageSizeLesserThan: int = None, sortBy: str = None, sortOrder: str = None, limit: int = None, offset: int = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'imageUuid': 'imageUuid', 'name': 'name', 'family': 'family', 'applicationType': 'applicationType', 'imageIntegrityStatus': 'imageIntegrityStatus', 'version': 'version', 'imageSeries': 'imageSeries', 'imageName': 'imageName', 'isTaggedGolden': 'isTaggedGolden', 'isCCORecommended': 'isCCORecommended', 'isCCOLatest': 'isCCOLatest', 'createdTime': 'createdTime', 'imageSizeGreaterThan': 'imageSizeGreaterThan', 'imageSizeLesserThan': 'imageSizeLesserThan', 'sortBy': 'sortBy', 'sortOrder': 'sortOrder', 'limit': 'limit', 'offset': 'offset'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getSoftwareImageDetails')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getInterfaceByID')
def getInterfaceByID(id: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'id': 'id'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getInterfaceByID')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getAnycastGateways')
def getAnycastGateways(id: str = None, fabricId: str = None, virtualNetworkName: str = None, ipPoolName: str = None, vlanName: str = None, vlanId: float = None, offset: float = None, limit: float = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'id': 'id', 'fabricId': 'fabricId', 'virtualNetworkName': 'virtualNetworkName', 'ipPoolName': 'ipPoolName', 'vlanName': 'vlanName', 'vlanId': 'vlanId', 'offset': 'offset', 'limit': 'limit'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getAnycastGateways')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getApplicationSet_s')
def getApplicationSet_s(attributes: str, offset: float, limit: float, name: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'attributes': 'attributes', 'name': 'name', 'offset': 'offset', 'limit': 'limit'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getApplicationSet_s')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('s')(globals()['getApplicationSet_s'])

@register('s')
def s(attributes: str, offset: float, limit: float, name: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'attributes': 'attributes', 'name': 'name', 'offset': 'offset', 'limit': 'limit'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('s')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getTagMembersById')
def getTagMembersById(id: str, memberType: str, offset: float = None, limit: float = None, memberAssociationType: str = None, level: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'id': 'id', 'memberType': 'memberType', 'offset': 'offset', 'limit': 'limit', 'memberAssociationType': 'memberAssociationType', 'level': 'level'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getTagMembersById')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getFabricSiteCount')
def getFabricSiteCount():
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getFabricSiteCount')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('retrievesAllTheValidationSets')
def retrievesAllTheValidationSets(view: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'view': 'view'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('retrievesAllTheValidationSets')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('retrievesTheListOfSitesThatTheGivenNetworkProfileForSitesIsAssig')
def retrievesTheListOfSitesThatTheGivenNetworkProfileForSitesIsAssig(profileId: str, offset: float = None, limit: float = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'profileId': 'profileId', 'offset': 'offset', 'limit': 'limit'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('retrievesTheListOfSitesThatTheGivenNetworkProfileForSitesIsAssig')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getFabricDevicesLayer2HandoffsCount')
def getFabricDevicesLayer2HandoffsCount(fabricId: str, networkDeviceId: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'fabricId': 'fabricId', 'networkDeviceId': 'networkDeviceId'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getFabricDevicesLayer2HandoffsCount')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('countOfEventSubscriptions')
def countOfEventSubscriptions(eventIds: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'eventIds': 'eventIds'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('countOfEventSubscriptions')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getSSIDBySite')
def getSSIDBySite(siteId: str, limit: float = None, offset: float = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'siteId': 'siteId', 'limit': 'limit', 'offset': 'offset'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getSSIDBySite')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getITSMIntegrationSettingById')
def getITSMIntegrationSettingById(instanceId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'instanceId': 'instanceId'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getITSMIntegrationSettingById')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDetailsOfASingleAssuranceEvent')
def getDetailsOfASingleAssuranceEvent(id: str, X_CALLER_ID: str = None, attribute: str = None, view: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'X-CALLER-ID': 'X_CALLER_ID', 'id': 'id', 'attribute': 'attribute', 'view': 'view'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getDetailsOfASingleAssuranceEvent')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getRFProfiles')
def getRFProfiles(limit: float = None, offset: float = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'limit': 'limit', 'offset': 'offset'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getRFProfiles')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('retrieveTelemetrySettingsForASite')
def retrieveTelemetrySettingsForASite(id: str, _inherited: bool = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'id': 'id', '_inherited': '_inherited'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('retrieveTelemetrySettingsForASite')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getAllUser-Defined-Fields')
def getAllUser_Defined_Fields(id: str = None, name: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'id': 'id', 'name': 'name'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getAllUser_Defined_Fields')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('queryAssuranceEvents')
def queryAssuranceEvents(deviceFamily: str, X_CALLER_ID: str = None, startTime: float = None, endTime: float = None, messageType: str = None, severity: float = None, siteId: str = None, siteHierarchyId: str = None, networkDeviceName: str = None, networkDeviceId: str = None, apMac: str = None, clientMac: str = None, attribute: str = None, view: str = None, offset: float = None, limit: float = None, sortBy: str = None, order: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'X-CALLER-ID': 'X_CALLER_ID', 'deviceFamily': 'deviceFamily', 'startTime': 'startTime', 'endTime': 'endTime', 'messageType': 'messageType', 'severity': 'severity', 'siteId': 'siteId', 'siteHierarchyId': 'siteHierarchyId', 'networkDeviceName': 'networkDeviceName', 'networkDeviceId': 'networkDeviceId', 'apMac': 'apMac', 'clientMac': 'clientMac', 'attribute': 'attribute', 'view': 'view', 'offset': 'offset', 'limit': 'limit', 'sortBy': 'sortBy', 'order': 'order'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('queryAssuranceEvents')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getFloorSettings')
def getFloorSettings():
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getFloorSettings')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getTheTotalNumberOfIssuesForGivenSetOfFilters')
def getTheTotalNumberOfIssuesForGivenSetOfFilters(X_CALLER_ID: str = None, startTime: float = None, endTime: float = None, isGlobal: bool = None, priority: str = None, severity: str = None, status: str = None, entityType: str = None, category: str = None, deviceType: str = None, name: str = None, issueId: str = None, entityId: str = None, updatedBy: str = None, siteHierarchy: str = None, siteHierarchyId: str = None, siteName: str = None, siteId: str = None, fabricSiteId: str = None, fabricVnName: str = None, fabricTransitSiteId: str = None, networkDeviceId: str = None, networkDeviceIpAddress: str = None, macAddress: str = None, aiDriven: bool = None, fabricDriven: bool = None, fabricSiteDriven: bool = None, fabricVnDriven: bool = None, fabricTransitDriven: bool = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'X-CALLER-ID': 'X_CALLER_ID', 'startTime': 'startTime', 'endTime': 'endTime', 'isGlobal': 'isGlobal', 'priority': 'priority', 'severity': 'severity', 'status': 'status', 'entityType': 'entityType', 'category': 'category', 'deviceType': 'deviceType', 'name': 'name', 'issueId': 'issueId', 'entityId': 'entityId', 'updatedBy': 'updatedBy', 'siteHierarchy': 'siteHierarchy', 'siteHierarchyId': 'siteHierarchyId', 'siteName': 'siteName', 'siteId': 'siteId', 'fabricSiteId': 'fabricSiteId', 'fabricVnName': 'fabricVnName', 'fabricTransitSiteId': 'fabricTransitSiteId', 'networkDeviceId': 'networkDeviceId', 'networkDeviceIpAddress': 'networkDeviceIpAddress', 'macAddress': 'macAddress', 'aiDriven': 'aiDriven', 'fabricDriven': 'fabricDriven', 'fabricSiteDriven': 'fabricSiteDriven', 'fabricVnDriven': 'fabricVnDriven', 'fabricTransitDriven': 'fabricTransitDriven'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getTheTotalNumberOfIssuesForGivenSetOfFilters')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getTag')
def getTag(name: str = None, additionalInfo_nameSpace: str = None, additionalInfo_attributes: str = None, level: str = None, offset: float = None, limit: float = None, size: str = None, field: str = None, sortBy: str = None, order: str = None, systemTag: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'name': 'name', 'additionalInfo.nameSpace': 'additionalInfo_nameSpace', 'additionalInfo.attributes': 'additionalInfo_attributes', 'level': 'level', 'offset': 'offset', 'limit': 'limit', 'size': 'size', 'field': 'field', 'sortBy': 'sortBy', 'order': 'order', 'systemTag': 'systemTag'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getTag')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getLayer2VirtualNetworks')
def getLayer2VirtualNetworks(id: str = None, fabricId: str = None, vlanName: str = None, vlanId: float = None, trafficType: str = None, associatedLayer3VirtualNetworkName: str = None, offset: float = None, limit: float = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'id': 'id', 'fabricId': 'fabricId', 'vlanName': 'vlanName', 'vlanId': 'vlanId', 'trafficType': 'trafficType', 'associatedLayer3VirtualNetworkName': 'associatedLayer3VirtualNetworkName', 'offset': 'offset', 'limit': 'limit'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getLayer2VirtualNetworks')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getFabricZoneCount')
def getFabricZoneCount():
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getFabricZoneCount')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getWebhookDestination')
def getWebhookDestination(webhookIds: str = None, offset: float = None, limit: float = None, sortBy: str = None, order: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'webhookIds': 'webhookIds', 'offset': 'offset', 'limit': 'limit', 'sortBy': 'sortBy', 'order': 'order'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getWebhookDestination')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('retrieveTimeZoneSettingsForASite')
def retrieveTimeZoneSettingsForASite(id: str, _inherited: bool = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'id': 'id', '_inherited': '_inherited'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('retrieveTimeZoneSettingsForASite')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceByID')
def getDeviceByID(id: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'id': 'id'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getDeviceByID')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getApplicationPolicyQueuingProfile')
def getApplicationPolicyQueuingProfile(name: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'name': 'name'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getApplicationPolicyQueuingProfile')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getSyslogDestination')
def getSyslogDestination(configId: str = None, name: str = None, protocol: str = None, offset: float = None, limit: float = None, sortBy: str = None, order: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'configId': 'configId', 'name': 'name', 'protocol': 'protocol', 'offset': 'offset', 'limit': 'limit', 'sortBy': 'sortBy', 'order': 'order'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getSyslogDestination')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getAll802.11beProfiles')
def getAll802_11beProfiles(limit: float = None, offset: float = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'limit': 'limit', 'offset': 'offset'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getAll802_11beProfiles')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getSyncResultForVirtualAccount')
def getSyncResultForVirtualAccount(domain: str, name: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'domain': 'domain', 'name': 'name'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getSyncResultForVirtualAccount')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getAllTheCustomIssueDefinitionsBasedOnTheGivenFilters.')
def getAllTheCustomIssueDefinitionsBasedOnTheGivenFilters_(X_CALLER_ID: str = None, id: str = None, profileId: str = None, name: str = None, priority: str = None, isEnabled: bool = None, severity: float = None, facility: str = None, mnemonic: str = None, limit: float = None, offset: float = None, sortBy: str = None, order: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'X-CALLER-ID': 'X_CALLER_ID', 'id': 'id', 'profileId': 'profileId', 'name': 'name', 'priority': 'priority', 'isEnabled': 'isEnabled', 'severity': 'severity', 'facility': 'facility', 'mnemonic': 'mnemonic', 'limit': 'limit', 'offset': 'offset', 'sortBy': 'sortBy', 'order': 'order'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getAllTheCustomIssueDefinitionsBasedOnTheGivenFilters_')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getApplicationPolicyDefault')
def getApplicationPolicyDefault():
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getApplicationPolicyDefault')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getPrimaryManagedAPLocationsForSpecificWirelessController')
def getPrimaryManagedAPLocationsForSpecificWirelessController(networkDeviceId: str, limit: float = None, offset: float = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkDeviceId': 'networkDeviceId', 'limit': 'limit', 'offset': 'offset'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getPrimaryManagedAPLocationsForSpecificWirelessController')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getModuleInfoById')
def getModuleInfoById(id: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'id': 'id'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getModuleInfoById')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getFabricDevicesLayer3HandoffsWithSdaTransit')
def getFabricDevicesLayer3HandoffsWithSdaTransit(fabricId: str, networkDeviceId: str = None, offset: float = None, limit: float = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'fabricId': 'fabricId', 'networkDeviceId': 'networkDeviceId', 'offset': 'offset', 'limit': 'limit'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getFabricDevicesLayer3HandoffsWithSdaTransit')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getFabricDevicesLayer3HandoffsWithIpTransit')
def getFabricDevicesLayer3HandoffsWithIpTransit(fabricId: str, networkDeviceId: str = None, offset: float = None, limit: float = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'fabricId': 'fabricId', 'networkDeviceId': 'networkDeviceId', 'offset': 'offset', 'limit': 'limit'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getFabricDevicesLayer3HandoffsWithIpTransit')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('returnsNetworkDeviceProductNamesForASite')
def returnsNetworkDeviceProductNamesForASite(siteId: str = None, productName: str = None, offset: float = None, limit: float = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'siteId': 'siteId', 'productName': 'productName', 'offset': 'offset', 'limit': 'limit'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('returnsNetworkDeviceProductNamesForASite')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('countOfNotifications')
def countOfNotifications(eventIds: str = None, startTime: float = None, endTime: float = None, category: str = None, type: str = None, severity: str = None, domain: str = None, subDomain: str = None, source: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'eventIds': 'eventIds', 'startTime': 'startTime', 'endTime': 'endTime', 'category': 'category', 'type': 'type', 'severity': 'severity', 'domain': 'domain', 'subDomain': 'subDomain', 'source': 'source'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('countOfNotifications')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getAScheduledReport')
def getAScheduledReport(reportId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'reportId': 'reportId'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getAScheduledReport')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getSiteHealth')
def getSiteHealth(siteType: str = None, offset: float = None, limit: float = None, timestamp: float = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'siteType': 'siteType', 'offset': 'offset', 'limit': 'limit', 'timestamp': 'timestamp'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getSiteHealth')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('returnsPOEInterfaceDetailsForTheDevice.')
def returnsPOEInterfaceDetailsForTheDevice_(deviceUuid: str, interfaceNameList: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'deviceUuid': 'deviceUuid', 'interfaceNameList': 'interfaceNameList'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('returnsPOEInterfaceDetailsForTheDevice_')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getSitesCount')
def getSitesCount(name: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'name': 'name'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getSitesCount')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('retrievesTheListOfValidationWorkflows')
def retrievesTheListOfValidationWorkflows(startTime: float = None, endTime: float = None, runStatus: str = None, offset: float = None, limit: float = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'startTime': 'startTime', 'endTime': 'endTime', 'runStatus': 'runStatus', 'offset': 'offset', 'limit': 'limit'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('retrievesTheListOfValidationWorkflows')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('readAnAggregatedSummaryOfSiteHealthData.')
def readAnAggregatedSummaryOfSiteHealthData_(X_CALLER_ID: str = None, startTime: float = None, endTime: float = None, siteHierarchy: str = None, siteHierarchyId: str = None, siteType: str = None, id: str = None, view: str = None, attribute: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'X-CALLER-ID': 'X_CALLER_ID', 'startTime': 'startTime', 'endTime': 'endTime', 'siteHierarchy': 'siteHierarchy', 'siteHierarchyId': 'siteHierarchyId', 'siteType': 'siteType', 'id': 'id', 'view': 'view', 'attribute': 'attribute'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('readAnAggregatedSummaryOfSiteHealthData_')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('retrievesTheCountOfProfilesThatTheGivenSiteHasBeenAssigned')
def retrievesTheCountOfProfilesThatTheGivenSiteHasBeenAssigned(siteId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'siteId': 'siteId'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('retrievesTheCountOfProfilesThatTheGivenSiteHasBeenAssigned')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getSiteCountV2')
def getSiteCountV2(id: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'id': 'id'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getSiteCountV2')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('returnsCountOfSoftwareImages')
def returnsCountOfSoftwareImages(siteId: str = None, productNameOrdinal: float = None, supervisorProductNameOrdinal: float = None, imported: bool = None, name: str = None, version: str = None, golden: str = None, integrity: str = None, hasAddonImages: bool = None, isAddonImages: bool = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'siteId': 'siteId', 'productNameOrdinal': 'productNameOrdinal', 'supervisorProductNameOrdinal': 'supervisorProductNameOrdinal', 'imported': 'imported', 'name': 'name', 'version': 'version', 'golden': 'golden', 'integrity': 'integrity', 'hasAddonImages': 'hasAddonImages', 'isAddonImages': 'isAddonImages'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('returnsCountOfSoftwareImages')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getExtranetPolicies')
def getExtranetPolicies(extranetPolicyName: str = None, offset: float = None, limit: float = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'extranetPolicyName': 'extranetPolicyName', 'offset': 'offset', 'limit': 'limit'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getExtranetPolicies')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getWirelessProfileByID')
def getWirelessProfileByID(id: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'id': 'id'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getWirelessProfileByID')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getFlexibleReportScheduleByReportId')
def getFlexibleReportScheduleByReportId(Content_Type: str, reportId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'Content-Type': 'Content_Type', 'reportId': 'reportId'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getFlexibleReportScheduleByReportId')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getPortChannels')
def getPortChannels(fabricId: str = None, networkDeviceId: str = None, portChannelName: str = None, connectedDeviceType: str = None, offset: float = None, limit: float = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'fabricId': 'fabricId', 'networkDeviceId': 'networkDeviceId', 'portChannelName': 'portChannelName', 'connectedDeviceType': 'connectedDeviceType', 'offset': 'offset', 'limit': 'limit'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getPortChannels')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getRFProfileByID')
def getRFProfileByID(id: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'id': 'id'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getRFProfileByID')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getsTheTemplatesAvailable')
def getsTheTemplatesAvailable(projectId: str = None, softwareType: str = None, softwareVersion: str = None, productFamily: str = None, productSeries: str = None, productType: str = None, filterConflictingTemplates: bool = None, tags: list = None, projectNames: list = None, unCommitted: bool = None, sortOrder: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'projectId': 'projectId', 'softwareType': 'softwareType', 'softwareVersion': 'softwareVersion', 'productFamily': 'productFamily', 'productSeries': 'productSeries', 'productType': 'productType', 'filterConflictingTemplates': 'filterConflictingTemplates', 'tags': 'tags', 'projectNames': 'projectNames', 'unCommitted': 'unCommitted', 'sortOrder': 'sortOrder'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getsTheTemplatesAvailable')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getSyslogSubscriptionDetails')
def getSyslogSubscriptionDetails(name: str = None, instanceId: str = None, offset: float = None, limit: float = None, sortBy: str = None, order: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'name': 'name', 'instanceId': 'instanceId', 'offset': 'offset', 'limit': 'limit', 'sortBy': 'sortBy', 'order': 'order'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getSyslogSubscriptionDetails')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('returnsAllIssueTriggerDefinitionsForGivenFilters.')
def returnsAllIssueTriggerDefinitionsForGivenFilters_(X_CALLER_ID: str = None, deviceType: str = None, profileId: str = None, id: str = None, name: str = None, priority: str = None, issueEnabled: bool = None, attribute: str = None, offset: float = None, limit: float = None, sortBy: str = None, order: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'X-CALLER-ID': 'X_CALLER_ID', 'deviceType': 'deviceType', 'profileId': 'profileId', 'id': 'id', 'name': 'name', 'priority': 'priority', 'issueEnabled': 'issueEnabled', 'attribute': 'attribute', 'offset': 'offset', 'limit': 'limit', 'sortBy': 'sortBy', 'order': 'order'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('returnsAllIssueTriggerDefinitionsForGivenFilters_')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getListOfScheduledReports')
def getListOfScheduledReports(viewGroupId: str = None, viewId: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'viewGroupId': 'viewGroupId', 'viewId': 'viewId'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getListOfScheduledReports')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getAAAAttributeAPI')
def getAAAAttributeAPI():
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getAAAAttributeAPI')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getClientDetail')
def getClientDetail(macAddress: str, timestamp: float = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'macAddress': 'macAddress', 'timestamp': 'timestamp'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getClientDetail')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('countTheNumberOfEvents')
def countTheNumberOfEvents(deviceFamily: str, X_CALLER_ID: str = None, startTime: str = None, endTime: str = None, messageType: str = None, severity: str = None, siteId: str = None, siteHierarchyId: str = None, networkDeviceName: str = None, networkDeviceId: str = None, apMac: str = None, clientMac: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'X-CALLER-ID': 'X_CALLER_ID', 'deviceFamily': 'deviceFamily', 'startTime': 'startTime', 'endTime': 'endTime', 'messageType': 'messageType', 'severity': 'severity', 'siteId': 'siteId', 'siteHierarchyId': 'siteHierarchyId', 'networkDeviceName': 'networkDeviceName', 'networkDeviceId': 'networkDeviceId', 'apMac': 'apMac', 'clientMac': 'clientMac'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('countTheNumberOfEvents')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getEoXStatusForAllDevices')
def getEoXStatusForAllDevices():
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getEoXStatusForAllDevices')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getTagMemberCount')
def getTagMemberCount(id: str, memberType: str, memberAssociationType: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'id': 'id', 'memberType': 'memberType', 'memberAssociationType': 'memberAssociationType'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getTagMemberCount')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('retrievesConfigurationDetailsOfTheExternalIPAMServer.')
def retrievesConfigurationDetailsOfTheExternalIPAMServer_():
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('retrievesConfigurationDetailsOfTheExternalIPAMServer_')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getViewDetailsForAGivenViewGroup_View')
def getViewDetailsForAGivenViewGroup_View(viewGroupId: str, viewId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'viewGroupId': 'viewGroupId', 'viewId': 'viewId'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getViewDetailsForAGivenViewGroup_View')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('View')(globals()['getViewDetailsForAGivenViewGroup_View'])

@register('View')
def View(viewGroupId: str, viewId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'viewGroupId': 'viewGroupId', 'viewId': 'viewId'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('View')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getTheDetailsOfPhysicalComponentsOfTheGivenDevice.')
def getTheDetailsOfPhysicalComponentsOfTheGivenDevice_(deviceUuid: str, type: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'deviceUuid': 'deviceUuid', 'type': 'type'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getTheDetailsOfPhysicalComponentsOfTheGivenDevice_')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceInterfacesBySpecifiedRange')
def getDeviceInterfacesBySpecifiedRange(deviceId: str, startIndex: int, recordsToReturn: int):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'deviceId': 'deviceId', 'startIndex': 'startIndex', 'recordsToReturn': 'recordsToReturn'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getDeviceInterfacesBySpecifiedRange')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getPollingIntervalForAllDevices')
def getPollingIntervalForAllDevices():
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getPollingIntervalForAllDevices')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceList')
def getDeviceList(hostname: list = None, managementIpAddress: list = None, macAddress: list = None, locationName: list = None, serialNumber: list = None, location: list = None, family: list = None, type: list = None, series: list = None, collectionStatus: list = None, collectionInterval: list = None, notSyncedForMinutes: list = None, errorCode: list = None, errorDescription: list = None, softwareVersion: list = None, softwareType: list = None, platformId: list = None, role: list = None, reachabilityStatus: list = None, upTime: list = None, associatedWlcIp: list = None, license_name: list = None, license_type: list = None, license_status: list = None, module_name: list = None, module_equpimenttype: list = None, module_servicestate: list = None, module_vendorequipmenttype: list = None, module_partnumber: list = None, module_operationstatecode: list = None, id: str = None, deviceSupportLevel: str = None, offset: int = None, limit: int = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'hostname': 'hostname', 'managementIpAddress': 'managementIpAddress', 'macAddress': 'macAddress', 'locationName': 'locationName', 'serialNumber': 'serialNumber', 'location': 'location', 'family': 'family', 'type': 'type', 'series': 'series', 'collectionStatus': 'collectionStatus', 'collectionInterval': 'collectionInterval', 'notSyncedForMinutes': 'notSyncedForMinutes', 'errorCode': 'errorCode', 'errorDescription': 'errorDescription', 'softwareVersion': 'softwareVersion', 'softwareType': 'softwareType', 'platformId': 'platformId', 'role': 'role', 'reachabilityStatus': 'reachabilityStatus', 'upTime': 'upTime', 'associatedWlcIp': 'associatedWlcIp', 'license.name': 'license_name', 'license.type': 'license_type', 'license.status': 'license_status', 'module+name': 'module_name', 'module+equpimenttype': 'module_equpimenttype', 'module+servicestate': 'module_servicestate', 'module+vendorequipmenttype': 'module_vendorequipmenttype', 'module+partnumber': 'module_partnumber', 'module+operationstatecode': 'module_operationstatecode', 'id': 'id', 'deviceSupportLevel': 'deviceSupportLevel', 'offset': 'offset', 'limit': 'limit'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getDeviceList')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getAllKeywordsOfCLIsAcceptedByCommandRunner')
def getAllKeywordsOfCLIsAcceptedByCommandRunner():
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getAllKeywordsOfCLIsAcceptedByCommandRunner')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getQosDeviceInterfaceInfo')
def getQosDeviceInterfaceInfo(networkDeviceId: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkDeviceId': 'networkDeviceId'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getQosDeviceInterfaceInfo')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('retrieveTheCountOfInterfacesThatAreAssociatedWithAtLeastOneTag.')
def retrieveTheCountOfInterfacesThatAreAssociatedWithAtLeastOneTag_():
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('retrieveTheCountOfInterfacesThatAreAssociatedWithAtLeastOneTag_')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceFamilyIdentifiers')
def getDeviceFamilyIdentifiers(Accept: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'Accept': 'Accept'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getDeviceFamilyIdentifiers')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getTaskCount')
def getTaskCount(startTime: str = None, endTime: str = None, data: str = None, errorCode: str = None, serviceType: str = None, username: str = None, progress: str = None, isError: str = None, failureReason: str = None, parentId: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'startTime': 'startTime', 'endTime': 'endTime', 'data': 'data', 'errorCode': 'errorCode', 'serviceType': 'serviceType', 'username': 'username', 'progress': 'progress', 'isError': 'isError', 'failureReason': 'failureReason', 'parentId': 'parentId'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getTaskCount')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('devices')
def devices(deviceRole: str = None, siteId: str = None, health: str = None, startTime: float = None, endTime: float = None, limit: float = None, offset: float = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'deviceRole': 'deviceRole', 'siteId': 'siteId', 'health': 'health', 'startTime': 'startTime', 'endTime': 'endTime', 'limit': 'limit', 'offset': 'offset'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('devices')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getSSIDCountForSpecificWirelessController')
def getSSIDCountForSpecificWirelessController(networkDeviceId: str, adminStatus: bool = None, managed: bool = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkDeviceId': 'networkDeviceId', 'adminStatus': 'adminStatus', 'managed': 'managed'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getSSIDCountForSpecificWirelessController')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('retrievesValidationDetailsForAValidationSet')
def retrievesValidationDetailsForAValidationSet(id: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'id': 'id'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('retrievesValidationDetailsForAValidationSet')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getSmartAccountList')
def getSmartAccountList():
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getSmartAccountList')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getLayer3VirtualNetworks')
def getLayer3VirtualNetworks(virtualNetworkName: str = None, fabricId: str = None, anchoredSiteId: str = None, offset: float = None, limit: float = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'virtualNetworkName': 'virtualNetworkName', 'fabricId': 'fabricId', 'anchoredSiteId': 'anchoredSiteId', 'offset': 'offset', 'limit': 'limit'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getLayer3VirtualNetworks')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getListOfAvailableNamespaces')
def getListOfAvailableNamespaces():
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getListOfAvailableNamespaces')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getSSIDByID')
def getSSIDByID(siteId: str, id: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'siteId': 'siteId', 'id': 'id'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getSSIDByID')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('retrieveNetworkDeviceProductName')
def retrieveNetworkDeviceProductName(productNameOrdinal: float):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'productNameOrdinal': 'productNameOrdinal'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('retrieveNetworkDeviceProductName')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getExecutionIdByReportId')
def getExecutionIdByReportId(Content_Type: str, reportId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'Content-Type': 'Content_Type', 'reportId': 'reportId'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getExecutionIdByReportId')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getMobilityGroupsCount')
def getMobilityGroupsCount():
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getMobilityGroupsCount')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getTaskDetailsByID')
def getTaskDetailsByID(id: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'id': 'id'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getTaskDetailsByID')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('custom-promptSupportGETAPI')
def custom_promptSupportGETAPI():
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('custom_promptSupportGETAPI')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getAdvisoriesList')
def getAdvisoriesList():
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getAdvisoriesList')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceInterfaceVLANs')
def getDeviceInterfaceVLANs(id: str, interfaceType: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'id': 'id', 'interfaceType': 'interfaceType'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getDeviceInterfaceVLANs')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getListOfFiles')
def getListOfFiles(nameSpace: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'nameSpace': 'nameSpace'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getListOfFiles')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('retrieveSpecificImageDistributionServer')
def retrieveSpecificImageDistributionServer(id: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'id': 'id'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('retrieveSpecificImageDistributionServer')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getApplicationPolicy')
def getApplicationPolicy(policyScope: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'policyScope': 'policyScope'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getApplicationPolicy')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getWorkflowById')
def getWorkflowById(id: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'id': 'id'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getWorkflowById')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getAdvisoriesSummary')
def getAdvisoriesSummary():
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getAdvisoriesSummary')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getTagResourceTypes')
def getTagResourceTypes():
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getTagResourceTypes')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getPortAssignmentCount')
def getPortAssignmentCount(fabricId: str = None, networkDeviceId: str = None, interfaceName: str = None, dataVlanName: str = None, voiceVlanName: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'fabricId': 'fabricId', 'networkDeviceId': 'networkDeviceId', 'interfaceName': 'interfaceName', 'dataVlanName': 'dataVlanName', 'voiceVlanName': 'voiceVlanName'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getPortAssignmentCount')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDiscoveriesByRange')
def getDiscoveriesByRange(startIndex: int, recordsToReturn: int):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'startIndex': 'startIndex', 'recordsToReturn': 'recordsToReturn'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getDiscoveriesByRange')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getAllITSMIntegrationSettings')
def getAllITSMIntegrationSettings():
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getAllITSMIntegrationSettings')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('licenseUsageDetails')
def licenseUsageDetails(smart_account_id: str, virtual_account_name: str, device_type: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'smart_account_id': 'smart_account_id', 'virtual_account_name': 'virtual_account_name', 'device_type': 'device_type'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('licenseUsageDetails')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getsAnArea')
def getsAnArea(id: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'id': 'id'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getsAnArea')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getTheCountOfHealthScoreDefinitionsBasedOnProvidedFilters.')
def getTheCountOfHealthScoreDefinitionsBasedOnProvidedFilters_(X_CALLER_ID: str = None, deviceType: str = None, id: str = None, includeForOverallHealth: bool = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'X-CALLER-ID': 'X_CALLER_ID', 'deviceType': 'deviceType', 'id': 'id', 'includeForOverallHealth': 'includeForOverallHealth'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getTheCountOfHealthScoreDefinitionsBasedOnProvidedFilters_')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getExtranetPolicyCount')
def getExtranetPolicyCount():
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getExtranetPolicyCount')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getResyncIntervalForTheNetworkDevice')
def getResyncIntervalForTheNetworkDevice(id: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'id': 'id'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getResyncIntervalForTheNetworkDevice')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getInterfaces')
def getInterfaces(limit: float = None, offset: float = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'limit': 'limit', 'offset': 'offset'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getInterfaces')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getAllViewGroups')
def getAllViewGroups():
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getAllViewGroups')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getEvents')
def getEvents(tags: str, eventId: str = None, offset: float = None, limit: float = None, sortBy: str = None, order: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'eventId': 'eventId', 'tags': 'tags', 'offset': 'offset', 'limit': 'limit', 'sortBy': 'sortBy', 'order': 'order'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getEvents')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getEmailEventSubscriptions')
def getEmailEventSubscriptions(eventIds: str = None, offset: float = None, limit: float = None, sortBy: str = None, order: str = None, domain: str = None, subDomain: str = None, category: str = None, type: str = None, name: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'eventIds': 'eventIds', 'offset': 'offset', 'limit': 'limit', 'sortBy': 'sortBy', 'order': 'order', 'domain': 'domain', 'subDomain': 'subDomain', 'category': 'category', 'type': 'type', 'name': 'name'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getEmailEventSubscriptions')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getEmailSubscriptionDetails')
def getEmailSubscriptionDetails(name: str = None, instanceId: str = None, offset: float = None, limit: float = None, sortBy: str = None, order: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'name': 'name', 'instanceId': 'instanceId', 'offset': 'offset', 'limit': 'limit', 'sortBy': 'sortBy', 'order': 'order'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getEmailSubscriptionDetails')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('retrieveAAASettingsForASite')
def retrieveAAASettingsForASite(id: str, _inherited: bool = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'id': 'id', '_inherited': '_inherited'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('retrieveAAASettingsForASite')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getInterfaceDetailsByDeviceIdAndInterfaceName')
def getInterfaceDetailsByDeviceIdAndInterfaceName(deviceId: str, name: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'deviceId': 'deviceId', 'name': 'name'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getInterfaceDetailsByDeviceIdAndInterfaceName')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getAllGlobalCredentialsV2')
def getAllGlobalCredentialsV2():
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getAllGlobalCredentialsV2')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getAccessPoint_s_FactoryResetStatus')
def getAccessPoint_s_FactoryResetStatus(taskId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'taskId': 'taskId'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getAccessPoint_s_FactoryResetStatus')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('s_FactoryResetStatus')(globals()['getAccessPoint_s_FactoryResetStatus'])

# alias → easier for LLM
register('s_FactoryResetStatu')(globals()['getAccessPoint_s_FactoryResetStatus'])

@register('s_FactoryResetStatus')
def s_FactoryResetStatus(taskId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'taskId': 'taskId'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('s_FactoryResetStatus')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('FactoryResetStatu')(globals()['s_FactoryResetStatus'])

# alias → easier for LLM
register('FactoryResetStatus')(globals()['s_FactoryResetStatus'])

@register('s_FactoryResetStatu')
def s_FactoryResetStatu(taskId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'taskId': 'taskId'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('s_FactoryResetStatu')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('FactoryResetStatu')(globals()['s_FactoryResetStatu'])

@register('getNetworkDevicesFromDiscovery')
def getNetworkDevicesFromDiscovery(id: str, taskId: str = None, sortBy: str = None, sortOrder: str = None, ipAddress: list = None, pingStatus: list = None, snmpStatus: list = None, cliStatus: list = None, netconfStatus: list = None, httpStatus: list = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'id': 'id', 'taskId': 'taskId', 'sortBy': 'sortBy', 'sortOrder': 'sortOrder', 'ipAddress': 'ipAddress', 'pingStatus': 'pingStatus', 'snmpStatus': 'snmpStatus', 'cliStatus': 'cliStatus', 'netconfStatus': 'netconfStatus', 'httpStatus': 'httpStatus'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getNetworkDevicesFromDiscovery')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getSites')
def getSites(name: str = None, nameHierarchy: str = None, type: str = None, _unitsOfMeasure: str = None, offset: int = None, limit: int = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'name': 'name', 'nameHierarchy': 'nameHierarchy', 'type': 'type', '_unitsOfMeasure': '_unitsOfMeasure', 'offset': 'offset', 'limit': 'limit'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getSites')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('returnTheCountOfAllTheFabricSiteWhichHasSSIDToIPPoolMapping')
def returnTheCountOfAllTheFabricSiteWhichHasSSIDToIPPoolMapping():
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('returnTheCountOfAllTheFabricSiteWhichHasSSIDToIPPoolMapping')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getEventSubscriptions')
def getEventSubscriptions(eventIds: str = None, offset: float = None, limit: float = None, sortBy: str = None, order: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'eventIds': 'eventIds', 'offset': 'offset', 'limit': 'limit', 'sortBy': 'sortBy', 'order': 'order'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getEventSubscriptions')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('readSiteHealthSummaryDataBySiteId.')
def readSiteHealthSummaryDataBySiteId_(id: str, X_CALLER_ID: str = None, startTime: float = None, endTime: float = None, view: str = None, attribute: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'X-CALLER-ID': 'X_CALLER_ID', 'id': 'id', 'startTime': 'startTime', 'endTime': 'endTime', 'view': 'view', 'attribute': 'attribute'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('readSiteHealthSummaryDataBySiteId_')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getPlannedAccessPointsForFloor')
def getPlannedAccessPointsForFloor(floorId: str, limit: float = None, offset: float = None, radios: bool = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'floorId': 'floorId', 'limit': 'limit', 'offset': 'offset', 'radios': 'radios'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getPlannedAccessPointsForFloor')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('returnListOfReplacementDevicesWithReplacementDetails')
def returnListOfReplacementDevicesWithReplacementDetails(faultyDeviceName: str = None, faultyDevicePlatform: str = None, replacementDevicePlatform: str = None, faultyDeviceSerialNumber: str = None, replacementDeviceSerialNumber: str = None, replacementStatus: list = None, family: list = None, sortBy: str = None, sortOrder: str = None, offset: int = None, limit: int = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'faultyDeviceName': 'faultyDeviceName', 'faultyDevicePlatform': 'faultyDevicePlatform', 'replacementDevicePlatform': 'replacementDevicePlatform', 'faultyDeviceSerialNumber': 'faultyDeviceSerialNumber', 'replacementDeviceSerialNumber': 'replacementDeviceSerialNumber', 'replacementStatus': 'replacementStatus', 'family': 'family', 'sortBy': 'sortBy', 'sortOrder': 'sortOrder', 'offset': 'offset', 'limit': 'limit'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('returnListOfReplacementDevicesWithReplacementDetails')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDiscoveryById')
def getDiscoveryById(id: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'id': 'id'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getDiscoveryById')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getConfigurationArchiveDetails')
def getConfigurationArchiveDetails(deviceId: str = None, fileType: str = None, createdTime: str = None, createdBy: str = None, offset: float = None, limit: float = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'deviceId': 'deviceId', 'fileType': 'fileType', 'createdTime': 'createdTime', 'createdBy': 'createdBy', 'offset': 'offset', 'limit': 'limit'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getConfigurationArchiveDetails')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getAdvisoriesPerDevice')
def getAdvisoriesPerDevice(deviceId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'deviceId': 'deviceId'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getAdvisoriesPerDevice')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceInterfaceCountForMultipleDevices')
def getDeviceInterfaceCountForMultipleDevices():
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getDeviceInterfaceCountForMultipleDevices')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('retrievesTheCountOfValidationWorkflows')
def retrievesTheCountOfValidationWorkflows(startTime: float = None, endTime: float = None, runStatus: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'startTime': 'startTime', 'endTime': 'endTime', 'runStatus': 'runStatus'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('retrievesTheCountOfValidationWorkflows')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getSNMPProperties')
def getSNMPProperties():
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getSNMPProperties')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getComplianceDetailCount')
def getComplianceDetailCount(complianceType: str = None, complianceStatus: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'complianceType': 'complianceType', 'complianceStatus': 'complianceStatus'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getComplianceDetailCount')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOverallClientHealth')
def getOverallClientHealth(timestamp: float = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'timestamp': 'timestamp'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getOverallClientHealth')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getLinecardDetails')
def getLinecardDetails(deviceUuid: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'deviceUuid': 'deviceUuid'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getLinecardDetails')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getsTheTotalNetworkDeviceInterfaceCountsInTheSpecifiedTimeRange.')
def getsTheTotalNetworkDeviceInterfaceCountsInTheSpecifiedTimeRange_(startTime: float = None, endTime: float = None, siteHierarchy: str = None, siteHierarchyId: str = None, siteId: str = None, networkDeviceId: str = None, networkDeviceIpAddress: str = None, networkDeviceMacAddress: str = None, interfaceId: str = None, interfaceName: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'startTime': 'startTime', 'endTime': 'endTime', 'siteHierarchy': 'siteHierarchy', 'siteHierarchyId': 'siteHierarchyId', 'siteId': 'siteId', 'networkDeviceId': 'networkDeviceId', 'networkDeviceIpAddress': 'networkDeviceIpAddress', 'networkDeviceMacAddress': 'networkDeviceMacAddress', 'interfaceId': 'interfaceId', 'interfaceName': 'interfaceName'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getsTheTotalNetworkDeviceInterfaceCountsInTheSpecifiedTimeRange_')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getWirelessProfilesCount')
def getWirelessProfilesCount():
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getWirelessProfilesCount')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getTagById')
def getTagById(id: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'id': 'id'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getTagById')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getAuditLogSummary')
def getAuditLogSummary(parentInstanceId: str = None, isParentOnly: bool = None, instanceId: str = None, name: str = None, eventId: str = None, category: str = None, severity: str = None, domain: str = None, subDomain: str = None, source: str = None, userId: str = None, context: str = None, eventHierarchy: str = None, siteId: str = None, deviceId: str = None, isSystemEvents: bool = None, description: str = None, startTime: float = None, endTime: float = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'parentInstanceId': 'parentInstanceId', 'isParentOnly': 'isParentOnly', 'instanceId': 'instanceId', 'name': 'name', 'eventId': 'eventId', 'category': 'category', 'severity': 'severity', 'domain': 'domain', 'subDomain': 'subDomain', 'source': 'source', 'userId': 'userId', 'context': 'context', 'eventHierarchy': 'eventHierarchy', 'siteId': 'siteId', 'deviceId': 'deviceId', 'isSystemEvents': 'isSystemEvents', 'description': 'description', 'startTime': 'startTime', 'endTime': 'endTime'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getAuditLogSummary')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getsAListOfProjects')
def getsAListOfProjects(name: str = None, sortOrder: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'name': 'name', 'sortOrder': 'sortOrder'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getsAListOfProjects')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('systemHealthCountAPI')
def systemHealthCountAPI(domain: str = None, subdomain: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'domain': 'domain', 'subdomain': 'subdomain'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('systemHealthCountAPI')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getAuthenticationAndPolicyServers')
def getAuthenticationAndPolicyServers(isIseEnabled: bool = None, state: str = None, role: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'isIseEnabled': 'isIseEnabled', 'state': 'state', 'role': 'role'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getAuthenticationAndPolicyServers')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getSSIDCountBySite')
def getSSIDCountBySite(siteId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'siteId': 'siteId'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getSSIDCountBySite')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('deviceLicenseSummary')
def deviceLicenseSummary(page_number: float, order: str, limit: float, sort_by: str = None, dna_level: str = None, device_type: str = None, registration_status: str = None, virtual_account_name: str = None, smart_account_id: str = None, device_uuid: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'page_number': 'page_number', 'order': 'order', 'sort_by': 'sort_by', 'dna_level': 'dna_level', 'device_type': 'device_type', 'limit': 'limit', 'registration_status': 'registration_status', 'virtual_account_name': 'virtual_account_name', 'smart_account_id': 'smart_account_id', 'device_uuid': 'device_uuid'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('deviceLicenseSummary')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('complianceDetailsOfDevice')
def complianceDetailsOfDevice(deviceUuid: str, category: str = None, complianceType: str = None, diffList: bool = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'deviceUuid': 'deviceUuid', 'category': 'category', 'complianceType': 'complianceType', 'diffList': 'diffList'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('complianceDetailsOfDevice')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('retrievesTheCountOfSitesThatTheGivenNetworkProfileForSitesIsAssi')
def retrievesTheCountOfSitesThatTheGivenNetworkProfileForSitesIsAssi(profileId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'profileId': 'profileId'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('retrievesTheCountOfSitesThatTheGivenNetworkProfileForSitesIsAssi')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getProvisionedDevices')
def getProvisionedDevices(id: str = None, networkDeviceId: str = None, siteId: str = None, offset: float = None, limit: float = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'id': 'id', 'networkDeviceId': 'networkDeviceId', 'siteId': 'siteId', 'offset': 'offset', 'limit': 'limit'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getProvisionedDevices')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('retrievesAllPreviousPathtracesSummary')
def retrievesAllPreviousPathtracesSummary(periodicRefresh: bool = None, sourceIP: str = None, destIP: str = None, sourcePort: float = None, destPort: float = None, gtCreateTime: float = None, ltCreateTime: float = None, protocol: str = None, status: str = None, taskId: str = None, lastUpdateTime: float = None, limit: float = None, offset: float = None, order: str = None, sortBy: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'periodicRefresh': 'periodicRefresh', 'sourceIP': 'sourceIP', 'destIP': 'destIP', 'sourcePort': 'sourcePort', 'destPort': 'destPort', 'gtCreateTime': 'gtCreateTime', 'ltCreateTime': 'ltCreateTime', 'protocol': 'protocol', 'status': 'status', 'taskId': 'taskId', 'lastUpdateTime': 'lastUpdateTime', 'limit': 'limit', 'offset': 'offset', 'order': 'order', 'sortBy': 'sortBy'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('retrievesAllPreviousPathtracesSummary')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('inventoryInsightDeviceLinkMismatchAPI')
def inventoryInsightDeviceLinkMismatchAPI(siteId: str, category: str, offset: int = None, limit: int = None, sortBy: str = None, order: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'siteId': 'siteId', 'offset': 'offset', 'limit': 'limit', 'category': 'category', 'sortBy': 'sortBy', 'order': 'order'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('inventoryInsightDeviceLinkMismatchAPI')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getTheDeviceDataForTheGivenDeviceId_Uuid_')
def getTheDeviceDataForTheGivenDeviceId_Uuid_(id: str, startTime: float = None, endTime: float = None, view: str = None, attribute: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'id': 'id', 'startTime': 'startTime', 'endTime': 'endTime', 'view': 'view', 'attribute': 'attribute'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getTheDeviceDataForTheGivenDeviceId_Uuid_')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('Uuid_')(globals()['getTheDeviceDataForTheGivenDeviceId_Uuid_'])

@register('Uuid_')
def Uuid_(id: str, startTime: float = None, endTime: float = None, view: str = None, attribute: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'id': 'id', 'startTime': 'startTime', 'endTime': 'endTime', 'view': 'view', 'attribute': 'attribute'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('Uuid_')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('lANAutomationLogById')
def lANAutomationLogById(id: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'id': 'id'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('lANAutomationLogById')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceCredentialSettingsForASite')
def getDeviceCredentialSettingsForASite(id: str, _inherited: bool = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'id': 'id', '_inherited': '_inherited'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getDeviceCredentialSettingsForASite')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceInterfaceCount')
def getDeviceInterfaceCount(deviceId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'deviceId': 'deviceId'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getDeviceInterfaceCount')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('ciscoDNACenterReleaseSummary')
def ciscoDNACenterReleaseSummary():
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('ciscoDNACenterReleaseSummary')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getLayer2VirtualNetworkCount')
def getLayer2VirtualNetworkCount(fabricId: str = None, vlanName: str = None, vlanId: float = None, trafficType: str = None, associatedLayer3VirtualNetworkName: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'fabricId': 'fabricId', 'vlanName': 'vlanName', 'vlanId': 'vlanId', 'trafficType': 'trafficType', 'associatedLayer3VirtualNetworkName': 'associatedLayer3VirtualNetworkName'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getLayer2VirtualNetworkCount')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('retrievesTheCountOfNetworkProfilesForSites')
def retrievesTheCountOfNetworkProfilesForSites(type: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'type': 'type'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('retrievesTheCountOfNetworkProfilesForSites')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceCount')
def getDeviceCount(hostname: list = None, managementIpAddress: list = None, macAddress: list = None, locationName: list = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'hostname': 'hostname', 'managementIpAddress': 'managementIpAddress', 'macAddress': 'macAddress', 'locationName': 'locationName'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getDeviceCount')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getFabricDevicesLayer2Handoffs')
def getFabricDevicesLayer2Handoffs(fabricId: str, networkDeviceId: str = None, offset: float = None, limit: float = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'fabricId': 'fabricId', 'networkDeviceId': 'networkDeviceId', 'offset': 'offset', 'limit': 'limit'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getFabricDevicesLayer2Handoffs')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getSyslogEventSubscriptions')
def getSyslogEventSubscriptions(eventIds: str = None, offset: float = None, limit: float = None, sortBy: str = None, order: str = None, domain: str = None, subDomain: str = None, category: str = None, type: str = None, name: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'eventIds': 'eventIds', 'offset': 'offset', 'limit': 'limit', 'sortBy': 'sortBy', 'order': 'order', 'domain': 'domain', 'subDomain': 'subDomain', 'category': 'category', 'type': 'type', 'name': 'name'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getSyslogEventSubscriptions')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getVLANDetails')
def getVLANDetails():
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getVLANDetails')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getAllMobilityGroups_')
def getAllMobilityGroups_(networkDeviceId: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkDeviceId': 'networkDeviceId'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getAllMobilityGroups_')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getSiteV2')
def getSiteV2(groupNameHierarchy: str = None, id: str = None, type: str = None, offset: str = None, limit: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'groupNameHierarchy': 'groupNameHierarchy', 'id': 'id', 'type': 'type', 'offset': 'offset', 'limit': 'limit'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getSiteV2')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('systemHealthAPI')
def systemHealthAPI(summary: bool = None, domain: str = None, subdomain: str = None, limit: float = None, offset: float = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'summary': 'summary', 'domain': 'domain', 'subdomain': 'subdomain', 'limit': 'limit', 'offset': 'offset'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('systemHealthAPI')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('lANAutomationStatusById')
def lANAutomationStatusById(id: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'id': 'id'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('lANAutomationStatusById')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getApplication_s')
def getApplication_s(attributes: str, offset: float, limit: float, name: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'attributes': 'attributes', 'name': 'name', 'offset': 'offset', 'limit': 'limit'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getApplication_s')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('s')(globals()['getApplication_s'])

@register('getFabricDevices')
def getFabricDevices(fabricId: str, networkDeviceId: str = None, deviceRoles: str = None, offset: float = None, limit: float = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'fabricId': 'fabricId', 'networkDeviceId': 'networkDeviceId', 'deviceRoles': 'deviceRoles', 'offset': 'offset', 'limit': 'limit'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getFabricDevices')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('get802.11beProfileByID')
def get802_11beProfileByID(id: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'id': 'id'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('get802_11beProfileByID')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getTasksCount')
def getTasksCount(startTime: int = None, endTime: int = None, parentId: str = None, rootId: str = None, status: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'startTime': 'startTime', 'endTime': 'endTime', 'parentId': 'parentId', 'rootId': 'rootId', 'status': 'status'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getTasksCount')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getsAFloor')
def getsAFloor(id: str, _unitsOfMeasure: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'id': 'id', '_unitsOfMeasure': '_unitsOfMeasure'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getsAFloor')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getUsersAPI')
def getUsersAPI(invokeSource: str, authSource: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'invokeSource': 'invokeSource', 'authSource': 'authSource'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getUsersAPI')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getFabricZones')
def getFabricZones(id: str = None, siteId: str = None, offset: float = None, limit: float = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'id': 'id', 'siteId': 'siteId', 'offset': 'offset', 'limit': 'limit'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getFabricZones')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getVirtualAccountList')
def getVirtualAccountList(domain: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'domain': 'domain'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getVirtualAccountList')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getQosDeviceInterfaceInfoCount')
def getQosDeviceInterfaceInfoCount():
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getQosDeviceInterfaceInfoCount')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('countOfEvents')
def countOfEvents(tags: str, eventId: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'eventId': 'eventId', 'tags': 'tags'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('countOfEvents')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOSPFInterfaces')
def getOSPFInterfaces():
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getOSPFInterfaces')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkDeviceImageUpdates')
def getNetworkDeviceImageUpdates(id: str = None, parentId: str = None, networkDeviceId: str = None, status: str = None, imageName: str = None, hostName: str = None, managementAddress: str = None, startTime: float = None, endTime: float = None, sortBy: str = None, order: str = None, offset: float = None, limit: float = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'id': 'id', 'parentId': 'parentId', 'networkDeviceId': 'networkDeviceId', 'status': 'status', 'imageName': 'imageName', 'hostName': 'hostName', 'managementAddress': 'managementAddress', 'startTime': 'startTime', 'endTime': 'endTime', 'sortBy': 'sortBy', 'order': 'order', 'offset': 'offset', 'limit': 'limit'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getNetworkDeviceImageUpdates')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getTransitNetworks')
def getTransitNetworks(id: str = None, name: str = None, type: str = None, offset: float = None, limit: float = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'id': 'id', 'name': 'name', 'type': 'type', 'offset': 'offset', 'limit': 'limit'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getTransitNetworks')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getStackDetailsForDevice')
def getStackDetailsForDevice(deviceId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'deviceId': 'deviceId'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getStackDetailsForDevice')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getApplicationSetCount')
def getApplicationSetCount(scalableGroupType: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'scalableGroupType': 'scalableGroupType'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getApplicationSetCount')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getWorkflowCount')
def getWorkflowCount(name: list = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'name': 'name'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getWorkflowCount')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('deviceComplianceStatus')
def deviceComplianceStatus(deviceUuid: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'deviceUuid': 'deviceUuid'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('deviceComplianceStatus')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('retrievesPreviousPathtrace')
def retrievesPreviousPathtrace(flowAnalysisId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'flowAnalysisId': 'flowAnalysisId'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('retrievesPreviousPathtrace')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOverallNetworkHealth')
def getOverallNetworkHealth(timestamp: float = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'timestamp': 'timestamp'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getOverallNetworkHealth')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getPnPGlobalSettings')
def getPnPGlobalSettings():
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getPnPGlobalSettings')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getServiceProviderDetailsV2')
def getServiceProviderDetailsV2():
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getServiceProviderDetailsV2')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getWirelessProfiles')
def getWirelessProfiles(limit: float = None, offset: float = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'limit': 'limit', 'offset': 'offset'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getWirelessProfiles')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getConfigTaskDetails')
def getConfigTaskDetails(parentTaskId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'parentTaskId': 'parentTaskId'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getConfigTaskDetails')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('retrieveTheCountOfNetworkDevicesThatAreAssociatedWithAtLeastOneT')
def retrieveTheCountOfNetworkDevicesThatAreAssociatedWithAtLeastOneT():
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('retrieveTheCountOfNetworkDevicesThatAreAssociatedWithAtLeastOneT')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getMulticastVirtualNetworkCount')
def getMulticastVirtualNetworkCount(fabricId: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'fabricId': 'fabricId'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getMulticastVirtualNetworkCount')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getTagCount')
def getTagCount(name: str = None, nameSpace: str = None, attributeName: str = None, size: str = None, systemTag: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'name': 'name', 'nameSpace': 'nameSpace', 'attributeName': 'attributeName', 'size': 'size', 'systemTag': 'systemTag'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getTagCount')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceSummary')
def getDeviceSummary(id: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'id': 'id'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getDeviceSummary')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getAuthenticationProfiles')
def getAuthenticationProfiles(fabricId: str = None, authenticationProfileName: str = None, offset: float = None, limit: float = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'fabricId': 'fabricId', 'authenticationProfileName': 'authenticationProfileName', 'offset': 'offset', 'limit': 'limit'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getAuthenticationProfiles')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getAllFlexibleReportSchedules')
def getAllFlexibleReportSchedules(Content_Type: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'Content-Type': 'Content_Type'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getAllFlexibleReportSchedules')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('virtualAccountDetails')
def virtualAccountDetails(smart_account_id: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'smart_account_id': 'smart_account_id'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('virtualAccountDetails')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getFunctionalCapabilityById')
def getFunctionalCapabilityById(id: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'id': 'id'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getFunctionalCapabilityById')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getFabricSites')
def getFabricSites(id: str = None, siteId: str = None, offset: float = None, limit: float = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'id': 'id', 'siteId': 'siteId', 'offset': 'offset', 'limit': 'limit'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getFabricSites')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getWorkflows')
def getWorkflows(limit: int = None, offset: int = None, sort: list = None, sortOrder: str = None, type: list = None, name: list = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'limit': 'limit', 'offset': 'offset', 'sort': 'sort', 'sortOrder': 'sortOrder', 'type': 'type', 'name': 'name'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getWorkflows')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceConfigById')
def getDeviceConfigById(networkDeviceId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkDeviceId': 'networkDeviceId'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getDeviceConfigById')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('retrievesSpecificClientInformationMatchingTheMACAddress.')
def retrievesSpecificClientInformationMatchingTheMACAddress_(id: str, X_CALLER_ID: str = None, startTime: float = None, endTime: float = None, view: str = None, attribute: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'X-CALLER-ID': 'X_CALLER_ID', 'id': 'id', 'startTime': 'startTime', 'endTime': 'endTime', 'view': 'view', 'attribute': 'attribute'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('retrievesSpecificClientInformationMatchingTheMACAddress_')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationListForMeraki')
def getOrganizationListForMeraki(id: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'id': 'id'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getOrganizationListForMeraki')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getPollingIntervalById')
def getPollingIntervalById(id: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'id': 'id'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getPollingIntervalById')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNotifications')
def getNotifications(eventIds: str = None, startTime: float = None, endTime: float = None, category: str = None, type: str = None, severity: str = None, domain: str = None, subDomain: str = None, source: str = None, offset: float = None, limit: float = None, sortBy: str = None, order: str = None, tags: str = None, namespace: str = None, siteId: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'eventIds': 'eventIds', 'startTime': 'startTime', 'endTime': 'endTime', 'category': 'category', 'type': 'type', 'severity': 'severity', 'domain': 'domain', 'subDomain': 'subDomain', 'source': 'source', 'offset': 'offset', 'limit': 'limit', 'sortBy': 'sortBy', 'order': 'order', 'tags': 'tags', 'namespace': 'namespace', 'siteId': 'siteId'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getNotifications')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getAllTheDetailsAndSuggestedActionsOfAnIssueForTheGivenIssueId')
def getAllTheDetailsAndSuggestedActionsOfAnIssueForTheGivenIssueId(id: str, Accept_Language: str = None, X_CALLER_ID: str = None, view: str = None, attribute: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'Accept-Language': 'Accept_Language', 'X-CALLER-ID': 'X_CALLER_ID', 'id': 'id', 'view': 'view', 'attribute': 'attribute'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getAllTheDetailsAndSuggestedActionsOfAnIssueForTheGivenIssueId')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('legitOperationsForInterface')
def legitOperationsForInterface(interfaceUuid: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'interfaceUuid': 'interfaceUuid'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('legitOperationsForInterface')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceConfigCount')
def getDeviceConfigCount():
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getDeviceConfigCount')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getISISInterfaces')
def getISISInterfaces():
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getISISInterfaces')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('retrieveANetworkProfileForSitesById')
def retrieveANetworkProfileForSitesById(id: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'id': 'id'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('retrieveANetworkProfileForSitesById')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getAuditLogRecords')
def getAuditLogRecords(parentInstanceId: str = None, instanceId: str = None, name: str = None, eventId: str = None, category: str = None, severity: str = None, domain: str = None, subDomain: str = None, source: str = None, userId: str = None, context: str = None, eventHierarchy: str = None, siteId: str = None, deviceId: str = None, isSystemEvents: bool = None, description: str = None, offset: float = None, limit: float = None, startTime: float = None, endTime: float = None, sortBy: str = None, order: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'parentInstanceId': 'parentInstanceId', 'instanceId': 'instanceId', 'name': 'name', 'eventId': 'eventId', 'category': 'category', 'severity': 'severity', 'domain': 'domain', 'subDomain': 'subDomain', 'source': 'source', 'userId': 'userId', 'context': 'context', 'eventHierarchy': 'eventHierarchy', 'siteId': 'siteId', 'deviceId': 'deviceId', 'isSystemEvents': 'isSystemEvents', 'description': 'description', 'offset': 'offset', 'limit': 'limit', 'startTime': 'startTime', 'endTime': 'endTime', 'sortBy': 'sortBy', 'order': 'order'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getAuditLogRecords')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('systemPerformanceHistoricalAPI')
def systemPerformanceHistoricalAPI(kpi: str = None, startTime: float = None, endTime: float = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'kpi': 'kpi', 'startTime': 'startTime', 'endTime': 'endTime'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('systemPerformanceHistoricalAPI')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getSupervisorCardDetail')
def getSupervisorCardDetail(deviceUuid: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'deviceUuid': 'deviceUuid'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getSupervisorCardDetail')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('retrieveImageDistributionSettingsForASite')
def retrieveImageDistributionSettingsForASite(id: str, _inherited: bool = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'id': 'id', '_inherited': '_inherited'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('retrieveImageDistributionSettingsForASite')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getSSIDDetailsForSpecificWirelessController')
def getSSIDDetailsForSpecificWirelessController(networkDeviceId: str, ssidName: str = None, adminStatus: bool = None, managed: bool = None, limit: float = None, offset: float = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkDeviceId': 'networkDeviceId', 'ssidName': 'ssidName', 'adminStatus': 'adminStatus', 'managed': 'managed', 'limit': 'limit', 'offset': 'offset'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getSSIDDetailsForSpecificWirelessController')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getsDetailsOfAGivenTemplate')
def getsDetailsOfAGivenTemplate(templateId: str, latestVersion: bool = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'templateId': 'templateId', 'latestVersion': 'latestVersion'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getsDetailsOfAGivenTemplate')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getEventArtifacts')
def getEventArtifacts(eventIds: str = None, tags: str = None, offset: float = None, limit: float = None, sortBy: str = None, order: str = None, search: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'eventIds': 'eventIds', 'tags': 'tags', 'offset': 'offset', 'limit': 'limit', 'sortBy': 'sortBy', 'order': 'order', 'search': 'search'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getEventArtifacts')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getsTheDetailsOfAGivenProject.')
def getsTheDetailsOfAGivenProject_(projectId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'projectId': 'projectId'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getsTheDetailsOfAGivenProject_')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('retrievesValidationWorkflowDetails')
def retrievesValidationWorkflowDetails(id: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'id': 'id'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('retrievesValidationWorkflowDetails')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getModuleCount')
def getModuleCount(deviceId: str, nameList: list = None, vendorEquipmentTypeList: list = None, partNumberList: list = None, operationalStateCodeList: list = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'deviceId': 'deviceId', 'nameList': 'nameList', 'vendorEquipmentTypeList': 'vendorEquipmentTypeList', 'partNumberList': 'partNumberList', 'operationalStateCodeList': 'operationalStateCodeList'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getModuleCount')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getTransitNetworksCount')
def getTransitNetworksCount(type: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'type': 'type'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getTransitNetworksCount')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('returnsAllTheFabricSitesThatHaveVLANToSSIDMapping.')
def returnsAllTheFabricSitesThatHaveVLANToSSIDMapping_(limit: float = None, offset: float = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'limit': 'limit', 'offset': 'offset'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('returnsAllTheFabricSitesThatHaveVLANToSSIDMapping_')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('deviceCountDetails')
def deviceCountDetails(device_type: str = None, registration_status: str = None, dna_level: str = None, virtual_account_name: str = None, smart_account_id: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'device_type': 'device_type', 'registration_status': 'registration_status', 'dna_level': 'dna_level', 'virtual_account_name': 'virtual_account_name', 'smart_account_id': 'smart_account_id'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('deviceCountDetails')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getAllExecutionDetailsForAGivenReport')
def getAllExecutionDetailsForAGivenReport(reportId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'reportId': 'reportId'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getAllExecutionDetailsForAGivenReport')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getRest_WebhookEventSubscriptions')
def getRest_WebhookEventSubscriptions(eventIds: str = None, offset: float = None, limit: float = None, sortBy: str = None, order: str = None, domain: str = None, subDomain: str = None, category: str = None, type: str = None, name: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'eventIds': 'eventIds', 'offset': 'offset', 'limit': 'limit', 'sortBy': 'sortBy', 'order': 'order', 'domain': 'domain', 'subDomain': 'subDomain', 'category': 'category', 'type': 'type', 'name': 'name'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getRest_WebhookEventSubscriptions')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('WebhookEventSubscription')(globals()['getRest_WebhookEventSubscriptions'])

# alias → easier for LLM
register('WebhookEventSubscriptions')(globals()['getRest_WebhookEventSubscriptions'])

@register('WebhookEventSubscription')
def WebhookEventSubscription(eventIds: str = None, offset: float = None, limit: float = None, sortBy: str = None, order: str = None, domain: str = None, subDomain: str = None, category: str = None, type: str = None, name: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'eventIds': 'eventIds', 'offset': 'offset', 'limit': 'limit', 'sortBy': 'sortBy', 'order': 'order', 'domain': 'domain', 'subDomain': 'subDomain', 'category': 'category', 'type': 'type', 'name': 'name'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('WebhookEventSubscription')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('WebhookEventSubscriptions')
def WebhookEventSubscriptions(eventIds: str = None, offset: float = None, limit: float = None, sortBy: str = None, order: str = None, domain: str = None, subDomain: str = None, category: str = None, type: str = None, name: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'eventIds': 'eventIds', 'offset': 'offset', 'limit': 'limit', 'sortBy': 'sortBy', 'order': 'order', 'domain': 'domain', 'subDomain': 'subDomain', 'category': 'category', 'type': 'type', 'name': 'name'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('WebhookEventSubscriptions')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getRolesAPI')
def getRolesAPI(invokeSource: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'invokeSource': 'invokeSource'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getRolesAPI')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getGoldenTagStatusOfAnImage.')
def getGoldenTagStatusOfAnImage_(Accept: str, siteId: str, deviceFamilyIdentifier: str, deviceRole: str, imageId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'Accept': 'Accept', 'siteId': 'siteId', 'deviceFamilyIdentifier': 'deviceFamilyIdentifier', 'deviceRole': 'deviceRole', 'imageId': 'imageId'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getGoldenTagStatusOfAnImage_')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getPortChannelCount')
def getPortChannelCount(fabricId: str = None, networkDeviceId: str = None, portChannelName: str = None, connectedDeviceType: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'fabricId': 'fabricId', 'networkDeviceId': 'networkDeviceId', 'portChannelName': 'portChannelName', 'connectedDeviceType': 'connectedDeviceType'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getPortChannelCount')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('mapsSupportedAccessPoints')
def mapsSupportedAccessPoints():
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('mapsSupportedAccessPoints')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getAuditLogParentRecords')
def getAuditLogParentRecords(instanceId: str = None, name: str = None, eventId: str = None, category: str = None, severity: str = None, domain: str = None, subDomain: str = None, source: str = None, userId: str = None, context: str = None, eventHierarchy: str = None, siteId: str = None, deviceId: str = None, isSystemEvents: bool = None, description: str = None, offset: float = None, limit: float = None, startTime: float = None, endTime: float = None, sortBy: str = None, order: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'instanceId': 'instanceId', 'name': 'name', 'eventId': 'eventId', 'category': 'category', 'severity': 'severity', 'domain': 'domain', 'subDomain': 'subDomain', 'source': 'source', 'userId': 'userId', 'context': 'context', 'eventHierarchy': 'eventHierarchy', 'siteId': 'siteId', 'deviceId': 'deviceId', 'isSystemEvents': 'isSystemEvents', 'description': 'description', 'offset': 'offset', 'limit': 'limit', 'startTime': 'startTime', 'endTime': 'endTime', 'sortBy': 'sortBy', 'order': 'order'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getAuditLogParentRecords')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('retrieveDNSSettingsForASite')
def retrieveDNSSettingsForASite(id: str, _inherited: bool = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'id': 'id', '_inherited': '_inherited'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('retrieveDNSSettingsForASite')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getHealthScoreDefinitionForTheGivenId.')
def getHealthScoreDefinitionForTheGivenId_(id: str, X_CALLER_ID: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'X-CALLER-ID': 'X_CALLER_ID', 'id': 'id'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getHealthScoreDefinitionForTheGivenId_')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getProject_s_Details')
def getProject_s_Details(id: str = None, name: str = None, offset: int = None, limit: int = None, sortOrder: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'id': 'id', 'name': 'name', 'offset': 'offset', 'limit': 'limit', 'sortOrder': 'sortOrder'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getProject_s_Details')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('s_Details')(globals()['getProject_s_Details'])

# alias → easier for LLM
register('s_Detail')(globals()['getProject_s_Details'])

@register('s_Details')
def s_Details(id: str = None, name: str = None, offset: int = None, limit: int = None, sortOrder: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'id': 'id', 'name': 'name', 'offset': 'offset', 'limit': 'limit', 'sortOrder': 'sortOrder'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('s_Details')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('Detail')(globals()['s_Details'])

# alias → easier for LLM
register('Details')(globals()['s_Details'])

@register('s_Detail')
def s_Detail(id: str = None, name: str = None, offset: int = None, limit: int = None, sortOrder: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'id': 'id', 'name': 'name', 'offset': 'offset', 'limit': 'limit', 'sortOrder': 'sortOrder'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('s_Detail')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('Detail')(globals()['s_Detail'])

@register('downloadAFileByFileId')
def downloadAFileByFileId(fileId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'fileId': 'fileId'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('downloadAFileByFileId')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getAllHealthScoreDefinitionsForGivenFilters.')
def getAllHealthScoreDefinitionsForGivenFilters_(X_CALLER_ID: str = None, deviceType: str = None, id: str = None, includeForOverallHealth: bool = None, attribute: str = None, offset: float = None, limit: float = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'X-CALLER-ID': 'X_CALLER_ID', 'deviceType': 'deviceType', 'id': 'id', 'includeForOverallHealth': 'includeForOverallHealth', 'attribute': 'attribute', 'offset': 'offset', 'limit': 'limit'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getAllHealthScoreDefinitionsForGivenFilters_')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getEmailDestination')
def getEmailDestination():
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getEmailDestination')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getsInterfacesAlongWithStatisticsDataFromAllNetworkDevices.')
def getsInterfacesAlongWithStatisticsDataFromAllNetworkDevices_(startTime: float = None, endTime: float = None, limit: float = None, offset: float = None, sortBy: str = None, order: str = None, siteHierarchy: str = None, siteHierarchyId: str = None, siteId: str = None, view: str = None, attribute: str = None, networkDeviceId: str = None, networkDeviceIpAddress: str = None, networkDeviceMacAddress: str = None, interfaceId: str = None, interfaceName: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'startTime': 'startTime', 'endTime': 'endTime', 'limit': 'limit', 'offset': 'offset', 'sortBy': 'sortBy', 'order': 'order', 'siteHierarchy': 'siteHierarchy', 'siteHierarchyId': 'siteHierarchyId', 'siteId': 'siteId', 'view': 'view', 'attribute': 'attribute', 'networkDeviceId': 'networkDeviceId', 'networkDeviceIpAddress': 'networkDeviceIpAddress', 'networkDeviceMacAddress': 'networkDeviceMacAddress', 'interfaceId': 'interfaceId', 'interfaceName': 'interfaceName'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getsInterfacesAlongWithStatisticsDataFromAllNetworkDevices_')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('retrieveLicenseSetting')
def retrieveLicenseSetting():
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('retrieveLicenseSetting')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getTheTotalCustomIssueDefinitionsCountBasedOnTheProvidedFilters.')
def getTheTotalCustomIssueDefinitionsCountBasedOnTheProvidedFilters_(X_CALLER_ID: str = None, id: str = None, profileId: str = None, name: str = None, priority: str = None, isEnabled: bool = None, severity: float = None, facility: str = None, mnemonic: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'X-CALLER-ID': 'X_CALLER_ID', 'id': 'id', 'profileId': 'profileId', 'name': 'name', 'priority': 'priority', 'isEnabled': 'isEnabled', 'severity': 'severity', 'facility': 'facility', 'mnemonic': 'mnemonic'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getTheTotalCustomIssueDefinitionsCountBasedOnTheProvidedFilters_')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('get802.11beProfilesCount')
def get802_11beProfilesCount():
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('get802_11beProfilesCount')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getMulticast')
def getMulticast(fabricId: str = None, offset: float = None, limit: float = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'fabricId': 'fabricId', 'offset': 'offset', 'limit': 'limit'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getMulticast')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getFabricDevicesCount')
def getFabricDevicesCount(fabricId: str, networkDeviceId: str = None, deviceRoles: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'fabricId': 'fabricId', 'networkDeviceId': 'networkDeviceId', 'deviceRoles': 'deviceRoles'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getFabricDevicesCount')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('downloadFlexibleReport')
def downloadFlexibleReport(Content_Type: str, reportId: str, executionId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'Content-Type': 'Content_Type', 'reportId': 'reportId', 'executionId': 'executionId'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('downloadFlexibleReport')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getExternalAuthenticationServersAPI')
def getExternalAuthenticationServersAPI(invokeSource: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'invokeSource': 'invokeSource'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getExternalAuthenticationServersAPI')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getLayer3VirtualNetworksCount')
def getLayer3VirtualNetworksCount(fabricId: str = None, anchoredSiteId: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'fabricId': 'fabricId', 'anchoredSiteId': 'anchoredSiteId'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getLayer3VirtualNetworksCount')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('lANAutomationStatus')
def lANAutomationStatus(offset: float = None, limit: float = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'offset': 'offset', 'limit': 'limit'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('lANAutomationStatus')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDevicesDiscoveredById')
def getDevicesDiscoveredById(id: str, taskId: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'id': 'id', 'taskId': 'taskId'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getDevicesDiscoveredById')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getTaskById')
def getTaskById(taskId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'taskId': 'taskId'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getTaskById')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getPermissionsAPI')
def getPermissionsAPI():
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getPermissionsAPI')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDiscoveredDevicesByRange')
def getDiscoveredDevicesByRange(id: str, startIndex: int, recordsToReturn: int, taskId: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'id': 'id', 'startIndex': 'startIndex', 'recordsToReturn': 'recordsToReturn', 'taskId': 'taskId'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getDiscoveredDevicesByRange')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('retrievesTheTotalCountOfClientsByApplyingBasicFiltering')
def retrievesTheTotalCountOfClientsByApplyingBasicFiltering(X_CALLER_ID: str = None, startTime: float = None, endTime: float = None, type: str = None, osType: str = None, osVersion: str = None, siteHierarchy: str = None, siteHierarchyId: str = None, siteId: str = None, ipv4Address: str = None, ipv6Address: str = None, macAddress: str = None, wlcName: str = None, connectedNetworkDeviceName: str = None, ssid: str = None, band: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'X-CALLER-ID': 'X_CALLER_ID', 'startTime': 'startTime', 'endTime': 'endTime', 'type': 'type', 'osType': 'osType', 'osVersion': 'osVersion', 'siteHierarchy': 'siteHierarchy', 'siteHierarchyId': 'siteHierarchyId', 'siteId': 'siteId', 'ipv4Address': 'ipv4Address', 'ipv6Address': 'ipv6Address', 'macAddress': 'macAddress', 'wlcName': 'wlcName', 'connectedNetworkDeviceName': 'connectedNetworkDeviceName', 'ssid': 'ssid', 'band': 'band'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('retrievesTheTotalCountOfClientsByApplyingBasicFiltering')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('pOEDetails')
def pOEDetails(deviceUuid: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'deviceUuid': 'deviceUuid'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('pOEDetails')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('retrievesTheListOfNetworkDeviceProductNames')
def retrievesTheListOfNetworkDeviceProductNames(productName: str = None, productId: str = None, offset: float = None, limit: float = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'productName': 'productName', 'productId': 'productId', 'offset': 'offset', 'limit': 'limit'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('retrievesTheListOfNetworkDeviceProductNames')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getAnchorManagedAPLocationsForSpecificWirelessController')
def getAnchorManagedAPLocationsForSpecificWirelessController(networkDeviceId: str, limit: float = None, offset: float = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkDeviceId': 'networkDeviceId', 'limit': 'limit', 'offset': 'offset'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getAnchorManagedAPLocationsForSpecificWirelessController')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getConnectedDeviceDetail')
def getConnectedDeviceDetail(deviceUuid: str, interfaceUuid: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'deviceUuid': 'deviceUuid', 'interfaceUuid': 'interfaceUuid'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getConnectedDeviceDetail')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDevicesThatAreAssignedToASite')
def getDevicesThatAreAssignedToASite(id: str, memberType: str, offset: str = None, limit: str = None, level: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'id': 'id', 'offset': 'offset', 'limit': 'limit', 'memberType': 'memberType', 'level': 'level'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getDevicesThatAreAssignedToASite')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('lANAutomationLog')
def lANAutomationLog(offset: float = None, limit: float = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'offset': 'offset', 'limit': 'limit'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('lANAutomationLog')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('retrievesTheListOfNetworkProfilesThatTheGivenSiteHasBeenAssigned')
def retrievesTheListOfNetworkProfilesThatTheGivenSiteHasBeenAssigned(siteId: str, offset: float = None, limit: float = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'siteId': 'siteId', 'offset': 'offset', 'limit': 'limit'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('retrievesTheListOfNetworkProfilesThatTheGivenSiteHasBeenAssigned')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDiscoveryJobsByIP')
def getDiscoveryJobsByIP(ipAddress: str, offset: int = None, limit: int = None, name: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'offset': 'offset', 'limit': 'limit', 'ipAddress': 'ipAddress', 'name': 'name'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getDiscoveryJobsByIP')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getTemplate_s_Details')
def getTemplate_s_Details(id: str = None, name: str = None, projectId: str = None, projectName: str = None, softwareType: str = None, softwareVersion: str = None, productFamily: str = None, productSeries: str = None, productType: str = None, filterConflictingTemplates: bool = None, tags: list = None, unCommitted: bool = None, sortOrder: str = None, allTemplateAttributes: bool = None, includeVersionDetails: bool = None, offset: int = None, limit: int = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'id': 'id', 'name': 'name', 'projectId': 'projectId', 'projectName': 'projectName', 'softwareType': 'softwareType', 'softwareVersion': 'softwareVersion', 'productFamily': 'productFamily', 'productSeries': 'productSeries', 'productType': 'productType', 'filterConflictingTemplates': 'filterConflictingTemplates', 'tags': 'tags', 'unCommitted': 'unCommitted', 'sortOrder': 'sortOrder', 'allTemplateAttributes': 'allTemplateAttributes', 'includeVersionDetails': 'includeVersionDetails', 'offset': 'offset', 'limit': 'limit'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getTemplate_s_Details')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('s_Details')(globals()['getTemplate_s_Details'])

# alias → easier for LLM
register('s_Detail')(globals()['getTemplate_s_Details'])

@register('lANAutomationLogsForIndividualDevices')
def lANAutomationLogsForIndividualDevices(id: str, serialNumber: str, logLevel: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'id': 'id', 'serialNumber': 'serialNumber', 'logLevel': 'logLevel'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('lANAutomationLogsForIndividualDevices')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getListOfDiscoveriesByDiscoveryId')
def getListOfDiscoveriesByDiscoveryId(id: str, offset: int = None, limit: int = None, ipAddress: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'id': 'id', 'offset': 'offset', 'limit': 'limit', 'ipAddress': 'ipAddress'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getListOfDiscoveriesByDiscoveryId')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getPhysicalTopology')
def getPhysicalTopology(nodeType: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'nodeType': 'nodeType'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getPhysicalTopology')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getSiteTopology')
def getSiteTopology():
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getSiteTopology')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getITSMIntegrationStatus')
def getITSMIntegrationStatus():
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getITSMIntegrationStatus')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getSecondaryManagedAPLocationsForSpecificWirelessController')
def getSecondaryManagedAPLocationsForSpecificWirelessController(networkDeviceId: str, limit: float = None, offset: float = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkDeviceId': 'networkDeviceId', 'limit': 'limit', 'offset': 'offset'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getSecondaryManagedAPLocationsForSpecificWirelessController')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('retrieveNTPSettingsForASite')
def retrieveNTPSettingsForASite(id: str, _inherited: bool = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'id': 'id', '_inherited': '_inherited'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('retrieveNTPSettingsForASite')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('retrieveTagsAssociatedWithTheInterfaces.')
def retrieveTagsAssociatedWithTheInterfaces_(offset: float = None, limit: float = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'offset': 'offset', 'limit': 'limit'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('retrieveTagsAssociatedWithTheInterfaces_')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('countOfNetworkDeviceImageUpdates')
def countOfNetworkDeviceImageUpdates(id: str = None, parentId: str = None, networkDeviceId: str = None, status: str = None, imageName: str = None, hostName: str = None, managementAddress: str = None, startTime: float = None, endTime: float = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'id': 'id', 'parentId': 'parentId', 'networkDeviceId': 'networkDeviceId', 'status': 'status', 'imageName': 'imageName', 'hostName': 'hostName', 'managementAddress': 'managementAddress', 'startTime': 'startTime', 'endTime': 'endTime'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('countOfNetworkDeviceImageUpdates')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('returnReplacementDevicesCount')
def returnReplacementDevicesCount(replacementStatus: list = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'replacementStatus': 'replacementStatus'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('returnReplacementDevicesCount')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getPlannedAccessPointsForBuilding')
def getPlannedAccessPointsForBuilding(buildingId: str, limit: float = None, offset: float = None, radios: bool = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'buildingId': 'buildingId', 'limit': 'limit', 'offset': 'offset', 'radios': 'radios'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getPlannedAccessPointsForBuilding')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getTheCountOfSystemDefinedIssueDefinitionsBasedOnProvidedFilters')
def getTheCountOfSystemDefinedIssueDefinitionsBasedOnProvidedFilters(X_CALLER_ID: str = None, deviceType: str = None, profileId: str = None, id: str = None, name: str = None, priority: str = None, issueEnabled: bool = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'X-CALLER-ID': 'X_CALLER_ID', 'deviceType': 'deviceType', 'profileId': 'profileId', 'id': 'id', 'name': 'name', 'priority': 'priority', 'issueEnabled': 'issueEnabled'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getTheCountOfSystemDefinedIssueDefinitionsBasedOnProvidedFilters')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('countOfNetworkProductNames')
def countOfNetworkProductNames(productName: str = None, productId: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'productName': 'productName', 'productId': 'productId'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('countOfNetworkProductNames')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getAccessPointConfiguration')
def getAccessPointConfiguration(key: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'key': 'key'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getAccessPointConfiguration')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceConfigForAllDevices')
def getDeviceConfigForAllDevices():
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getDeviceConfigForAllDevices')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getTopologyDetails')
def getTopologyDetails(vlanID: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'vlanID': 'vlanID'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getTopologyDetails')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getTheDetailsOfIssuesForGivenSetOfFilters-2')
def getTheDetailsOfIssuesForGivenSetOfFilters_2(Accept_Language: str = None, X_CALLER_ID: str = None, startTime: float = None, endTime: float = None, limit: float = None, offset: float = None, sortBy: str = None, order: str = None, isGlobal: bool = None, priority: str = None, severity: str = None, status: str = None, entityType: str = None, category: str = None, deviceType: str = None, name: str = None, issueId: str = None, entityId: str = None, updatedBy: str = None, siteHierarchy: str = None, siteHierarchyId: str = None, siteName: str = None, siteId: str = None, fabricSiteId: str = None, fabricVnName: str = None, fabricTransitSiteId: str = None, networkDeviceId: str = None, networkDeviceIpAddress: str = None, macAddress: str = None, view: str = None, attribute: str = None, aiDriven: bool = None, fabricDriven: bool = None, fabricSiteDriven: bool = None, fabricVnDriven: bool = None, fabricTransitDriven: bool = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'Accept-Language': 'Accept_Language', 'X-CALLER-ID': 'X_CALLER_ID', 'startTime': 'startTime', 'endTime': 'endTime', 'limit': 'limit', 'offset': 'offset', 'sortBy': 'sortBy', 'order': 'order', 'isGlobal': 'isGlobal', 'priority': 'priority', 'severity': 'severity', 'status': 'status', 'entityType': 'entityType', 'category': 'category', 'deviceType': 'deviceType', 'name': 'name', 'issueId': 'issueId', 'entityId': 'entityId', 'updatedBy': 'updatedBy', 'siteHierarchy': 'siteHierarchy', 'siteHierarchyId': 'siteHierarchyId', 'siteName': 'siteName', 'siteId': 'siteId', 'fabricSiteId': 'fabricSiteId', 'fabricVnName': 'fabricVnName', 'fabricTransitSiteId': 'fabricTransitSiteId', 'networkDeviceId': 'networkDeviceId', 'networkDeviceIpAddress': 'networkDeviceIpAddress', 'macAddress': 'macAddress', 'view': 'view', 'attribute': 'attribute', 'aiDriven': 'aiDriven', 'fabricDriven': 'fabricDriven', 'fabricSiteDriven': 'fabricSiteDriven', 'fabricVnDriven': 'fabricVnDriven', 'fabricTransitDriven': 'fabricTransitDriven'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getTheDetailsOfIssuesForGivenSetOfFilters_2')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('smartAccountDetails')
def smartAccountDetails():
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('smartAccountDetails')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getFabricDevicesLayer3HandoffsWithIpTransitCount')
def getFabricDevicesLayer3HandoffsWithIpTransitCount(fabricId: str, networkDeviceId: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'fabricId': 'fabricId', 'networkDeviceId': 'networkDeviceId'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getFabricDevicesLayer3HandoffsWithIpTransitCount')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getFabricDevicesLayer3HandoffsWithSdaTransitCount')
def getFabricDevicesLayer3HandoffsWithSdaTransitCount(fabricId: str, networkDeviceId: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'fabricId': 'fabricId', 'networkDeviceId': 'networkDeviceId'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getFabricDevicesLayer3HandoffsWithSdaTransitCount')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('retrievesTheListOfNetworkProfilesForSites')
def retrievesTheListOfNetworkProfilesForSites(offset: float = None, limit: float = None, sortBy: str = None, order: str = None, type: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'offset': 'offset', 'limit': 'limit', 'sortBy': 'sortBy', 'order': 'order', 'type': 'type'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('retrievesTheListOfNetworkProfilesForSites')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getFunctionalCapabilityForDevices')
def getFunctionalCapabilityForDevices(deviceId: str, functionName: list = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'deviceId': 'deviceId', 'functionName': 'functionName'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getFunctionalCapabilityForDevices')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getPortAssignments')
def getPortAssignments(fabricId: str = None, networkDeviceId: str = None, interfaceName: str = None, dataVlanName: str = None, voiceVlanName: str = None, offset: float = None, limit: float = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'fabricId': 'fabricId', 'networkDeviceId': 'networkDeviceId', 'interfaceName': 'interfaceName', 'dataVlanName': 'dataVlanName', 'voiceVlanName': 'voiceVlanName', 'offset': 'offset', 'limit': 'limit'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getPortAssignments')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getBusinessAPIExecutionDetails')
def getBusinessAPIExecutionDetails(executionId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'executionId': 'executionId'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getBusinessAPIExecutionDetails')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('lANAutomationActiveSessions')
def lANAutomationActiveSessions():
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('lANAutomationActiveSessions')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getSiteNotAssignedNetworkDevices')
def getSiteNotAssignedNetworkDevices(offset: float = None, limit: float = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'offset': 'offset', 'limit': 'limit'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getSiteNotAssignedNetworkDevices')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getAccessPointRebootTaskResult')
def getAccessPointRebootTaskResult(parentTaskId: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'parentTaskId': 'parentTaskId'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getAccessPointRebootTaskResult')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceDetail')
def getDeviceDetail(identifier: str, searchBy: str, timestamp: float = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'timestamp': 'timestamp', 'identifier': 'identifier', 'searchBy': 'searchBy'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getDeviceDetail')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('lANAutomationSessionCount')
def lANAutomationSessionCount():
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('lANAutomationSessionCount')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkDeviceByIP')
def getNetworkDeviceByIP(ipAddress: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'ipAddress': 'ipAddress'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getNetworkDeviceByIP')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getSiteNotAssignedNetworkDevicesCount')
def getSiteNotAssignedNetworkDevicesCount():
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getSiteNotAssignedNetworkDevicesCount')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceBySerialNumber')
def getDeviceBySerialNumber(serialNumber: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'serialNumber': 'serialNumber'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getDeviceBySerialNumber')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getApplicationCount')
def getApplicationCount(scalableGroupType: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'scalableGroupType': 'scalableGroupType'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getApplicationCount')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('downloadReportContent')
def downloadReportContent(reportId: str, executionId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'reportId': 'reportId', 'executionId': 'executionId'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('downloadReportContent')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceCount-2')
def getDeviceCount_2(serialNumber: list = None, state: list = None, onbState: list = None, name: list = None, pid: list = None, source: list = None, workflowId: list = None, workflowName: list = None, smartAccountId: list = None, virtualAccountId: list = None, lastContact: bool = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'serialNumber': 'serialNumber', 'state': 'state', 'onbState': 'onbState', 'name': 'name', 'pid': 'pid', 'source': 'source', 'workflowId': 'workflowId', 'workflowName': 'workflowName', 'smartAccountId': 'smartAccountId', 'virtualAccountId': 'virtualAccountId', 'lastContact': 'lastContact'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getDeviceCount_2')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('eventArtifactCount')
def eventArtifactCount():
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('eventArtifactCount')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getComplianceStatusCount')
def getComplianceStatusCount(complianceStatus: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'complianceStatus': 'complianceStatus'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getComplianceStatusCount')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getTasks')
def getTasks(offset: int = None, limit: int = None, sortBy: str = None, order: str = None, startTime: int = None, endTime: int = None, parentId: str = None, rootId: str = None, status: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'offset': 'offset', 'limit': 'limit', 'sortBy': 'sortBy', 'order': 'order', 'startTime': 'startTime', 'endTime': 'endTime', 'parentId': 'parentId', 'rootId': 'rootId', 'status': 'status'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getTasks')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getListOfChildEventsForTheGivenWirelessClientEvent')
def getListOfChildEventsForTheGivenWirelessClientEvent(id: str, X_CALLER_ID: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'X-CALLER-ID': 'X_CALLER_ID', 'id': 'id'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getListOfChildEventsForTheGivenWirelessClientEvent')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getProvisioningSettings')
def getProvisioningSettings():
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getProvisioningSettings')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('readSiteCount.')
def readSiteCount_(X_CALLER_ID: str = None, endTime: float = None, siteHierarchy: str = None, siteHierarchyId: str = None, siteType: str = None, id: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'X-CALLER-ID': 'X_CALLER_ID', 'endTime': 'endTime', 'siteHierarchy': 'siteHierarchy', 'siteHierarchyId': 'siteHierarchyId', 'siteType': 'siteType', 'id': 'id'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('readSiteCount_')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getEoXDetailsPerDevice')
def getEoXDetailsPerDevice(deviceId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'deviceId': 'deviceId'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getEoXDetailsPerDevice')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('ciscoDNACenterNodesConfigurationSummary')
def ciscoDNACenterNodesConfigurationSummary():
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('ciscoDNACenterNodesConfigurationSummary')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('importMapArchive-ImportStatus')
def importMapArchive_ImportStatus(importContextUuid: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'importContextUuid': 'importContextUuid'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('importMapArchive_ImportStatus')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getExternalAuthenticationSettingAPI')
def getExternalAuthenticationSettingAPI():
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getExternalAuthenticationSettingAPI')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getInterfaceById')
def getInterfaceById(id: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'id': 'id'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getInterfaceById')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('deviceLicenseDetails')
def deviceLicenseDetails(device_uuid: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'device_uuid': 'device_uuid'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('deviceLicenseDetails')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getTheInterfaceDataForTheGivenInterfaceId_instanceUuid_AlongWith')
def getTheInterfaceDataForTheGivenInterfaceId_instanceUuid_AlongWith(id: str, startTime: float = None, endTime: float = None, view: str = None, attribute: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'id': 'id', 'startTime': 'startTime', 'endTime': 'endTime', 'view': 'view', 'attribute': 'attribute'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getTheInterfaceDataForTheGivenInterfaceId_instanceUuid_AlongWith')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('instanceUuid_AlongWith')(globals()['getTheInterfaceDataForTheGivenInterfaceId_instanceUuid_AlongWith'])

@register('instanceUuid_AlongWith')
def instanceUuid_AlongWith(id: str, startTime: float = None, endTime: float = None, view: str = None, attribute: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'id': 'id', 'startTime': 'startTime', 'endTime': 'endTime', 'view': 'view', 'attribute': 'attribute'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('instanceUuid_AlongWith')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('AlongWith')(globals()['instanceUuid_AlongWith'])

@register('getInterfaceInfoById')
def getInterfaceInfoById(deviceId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'deviceId': 'deviceId'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getInterfaceInfoById')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getTaskByOperationId')
def getTaskByOperationId(operationId: str, offset: int, limit: int):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'operationId': 'operationId', 'offset': 'offset', 'limit': 'limit'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getTaskByOperationId')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('ciscoISEServerIntegrationStatus')
def ciscoISEServerIntegrationStatus():
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('ciscoISEServerIntegrationStatus')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getL3TopologyDetails')
def getL3TopologyDetails(topologyType: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'topologyType': 'topologyType'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getL3TopologyDetails')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getAdvisoryDeviceDetail')
def getAdvisoryDeviceDetail(deviceId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'deviceId': 'deviceId'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getAdvisoryDeviceDetail')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getConnectorTypes')
def getConnectorTypes():
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getConnectorTypes')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getTasksByID')
def getTasksByID(id: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'id': 'id'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getTasksByID')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('licenseTermDetails')
def licenseTermDetails(smart_account_id: str, virtual_account_name: str, device_type: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'smart_account_id': 'smart_account_id', 'virtual_account_name': 'virtual_account_name', 'device_type': 'device_type'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('licenseTermDetails')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('retrieveDHCPSettingsForASite')
def retrieveDHCPSettingsForASite(id: str, _inherited: bool = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'id': 'id', '_inherited': '_inherited'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('retrieveDHCPSettingsForASite')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getAnycastGatewayCount')
def getAnycastGatewayCount(fabricId: str = None, virtualNetworkName: str = None, ipPoolName: str = None, vlanName: str = None, vlanId: float = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'fabricId': 'fabricId', 'virtualNetworkName': 'virtualNetworkName', 'ipPoolName': 'ipPoolName', 'vlanName': 'vlanName', 'vlanId': 'vlanId'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getAnycastGatewayCount')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getsTheNetworkDeviceDetailsBasedOnTheProvidedQueryParameters.')
def getsTheNetworkDeviceDetailsBasedOnTheProvidedQueryParameters_(startTime: float = None, endTime: float = None, limit: float = None, offset: float = None, sortBy: str = None, order: str = None, siteHierarchy: str = None, siteHierarchyId: str = None, siteId: str = None, id: str = None, managementIpAddress: str = None, macAddress: str = None, family: str = None, type: str = None, role: str = None, serialNumber: str = None, maintenanceMode: bool = None, softwareVersion: str = None, healthScore: str = None, view: str = None, attribute: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'startTime': 'startTime', 'endTime': 'endTime', 'limit': 'limit', 'offset': 'offset', 'sortBy': 'sortBy', 'order': 'order', 'siteHierarchy': 'siteHierarchy', 'siteHierarchyId': 'siteHierarchyId', 'siteId': 'siteId', 'id': 'id', 'managementIpAddress': 'managementIpAddress', 'macAddress': 'macAddress', 'family': 'family', 'type': 'type', 'role': 'role', 'serialNumber': 'serialNumber', 'maintenanceMode': 'maintenanceMode', 'softwareVersion': 'softwareVersion', 'healthScore': 'healthScore', 'view': 'view', 'attribute': 'attribute'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getsTheNetworkDeviceDetailsBasedOnTheProvidedQueryParameters_')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('issues')
def issues(startTime: float = None, endTime: float = None, siteId: str = None, deviceId: str = None, macAddress: str = None, priority: str = None, issueStatus: str = None, aiDriven: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'startTime': 'startTime', 'endTime': 'endTime', 'siteId': 'siteId', 'deviceId': 'deviceId', 'macAddress': 'macAddress', 'priority': 'priority', 'issueStatus': 'issueStatus', 'aiDriven': 'aiDriven'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('issues')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDevicesRegisteredForWSANotification')
def getDevicesRegisteredForWSANotification(serialNumber: str = None, macaddress: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'serialNumber': 'serialNumber', 'macaddress': 'macaddress'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getDevicesRegisteredForWSANotification')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getInterfaceByIP')
def getInterfaceByIP(ipAddress: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'ipAddress': 'ipAddress'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getInterfaceByIP')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('retrieveApplicableAdd-onImagesForTheGivenSoftwareImage')
def retrieveApplicableAdd_onImagesForTheGivenSoftwareImage(id: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'id': 'id'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('retrieveApplicableAdd_onImagesForTheGivenSoftwareImage')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('retrievesTheListOfClients_WhileAlsoOfferingBasicFilteringAndSort')
def retrievesTheListOfClients_WhileAlsoOfferingBasicFilteringAndSort(X_CALLER_ID: str = None, startTime: float = None, endTime: float = None, limit: float = None, offset: float = None, sortBy: str = None, order: str = None, type: str = None, osType: str = None, osVersion: str = None, siteHierarchy: str = None, siteHierarchyId: str = None, siteId: str = None, ipv4Address: str = None, ipv6Address: str = None, macAddress: str = None, wlcName: str = None, connectedNetworkDeviceName: str = None, ssid: str = None, band: str = None, view: str = None, attribute: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'X-CALLER-ID': 'X_CALLER_ID', 'startTime': 'startTime', 'endTime': 'endTime', 'limit': 'limit', 'offset': 'offset', 'sortBy': 'sortBy', 'order': 'order', 'type': 'type', 'osType': 'osType', 'osVersion': 'osVersion', 'siteHierarchy': 'siteHierarchy', 'siteHierarchyId': 'siteHierarchyId', 'siteId': 'siteId', 'ipv4Address': 'ipv4Address', 'ipv6Address': 'ipv6Address', 'macAddress': 'macAddress', 'wlcName': 'wlcName', 'connectedNetworkDeviceName': 'connectedNetworkDeviceName', 'ssid': 'ssid', 'band': 'band', 'view': 'view', 'attribute': 'attribute'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('retrievesTheListOfClients_WhileAlsoOfferingBasicFilteringAndSort')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('WhileAlsoOfferingBasicFilteringAndSort')(globals()['retrievesTheListOfClients_WhileAlsoOfferingBasicFilteringAndSort'])

@register('WhileAlsoOfferingBasicFilteringAndSort')
def WhileAlsoOfferingBasicFilteringAndSort(X_CALLER_ID: str = None, startTime: float = None, endTime: float = None, limit: float = None, offset: float = None, sortBy: str = None, order: str = None, type: str = None, osType: str = None, osVersion: str = None, siteHierarchy: str = None, siteHierarchyId: str = None, siteId: str = None, ipv4Address: str = None, ipv6Address: str = None, macAddress: str = None, wlcName: str = None, connectedNetworkDeviceName: str = None, ssid: str = None, band: str = None, view: str = None, attribute: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'X-CALLER-ID': 'X_CALLER_ID', 'startTime': 'startTime', 'endTime': 'endTime', 'limit': 'limit', 'offset': 'offset', 'sortBy': 'sortBy', 'order': 'order', 'type': 'type', 'osType': 'osType', 'osVersion': 'osVersion', 'siteHierarchy': 'siteHierarchy', 'siteHierarchyId': 'siteHierarchyId', 'siteId': 'siteId', 'ipv4Address': 'ipv4Address', 'ipv6Address': 'ipv6Address', 'macAddress': 'macAddress', 'wlcName': 'wlcName', 'connectedNetworkDeviceName': 'connectedNetworkDeviceName', 'ssid': 'ssid', 'band': 'band', 'view': 'view', 'attribute': 'attribute'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('WhileAlsoOfferingBasicFilteringAndSort')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getEoXSummary')
def getEoXSummary():
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getEoXSummary')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('systemPerformanceAPI')
def systemPerformanceAPI(kpi: str = None, function: str = None, startTime: float = None, endTime: float = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'kpi': 'kpi', 'function': 'function', 'startTime': 'startTime', 'endTime': 'endTime'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('systemPerformanceAPI')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getManagedAPLocationsCountForSpecificWirelessController')
def getManagedAPLocationsCountForSpecificWirelessController(networkDeviceId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'networkDeviceId': 'networkDeviceId'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getManagedAPLocationsCountForSpecificWirelessController')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkDeviceByPaginationRange')
def getNetworkDeviceByPaginationRange(startIndex: int, recordsToReturn: int):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'startIndex': 'startIndex', 'recordsToReturn': 'recordsToReturn'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getNetworkDeviceByPaginationRange')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getSiteAssignedNetworkDevice')
def getSiteAssignedNetworkDevice(id: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'id': 'id'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getSiteAssignedNetworkDevice')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getTheCustomIssueDefinitionForTheGivenCustomIssueDefinitionId.')
def getTheCustomIssueDefinitionForTheGivenCustomIssueDefinitionId_(id: str, X_CALLER_ID: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'X-CALLER-ID': 'X_CALLER_ID', 'id': 'id'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getTheCustomIssueDefinitionForTheGivenCustomIssueDefinitionId_')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getAllInterfaces')
def getAllInterfaces(offset: int = None, limit: int = None, lastInputTime: str = None, lastOutputTime: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'offset': 'offset', 'limit': 'limit', 'lastInputTime': 'lastInputTime', 'lastOutputTime': 'lastOutputTime'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getAllInterfaces')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('returnsCountOfAdd-onImages')
def returnsCountOfAdd_onImages(id: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'id': 'id'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('returnsCountOfAdd_onImages')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getWirelessLanControllerDetailsById')
def getWirelessLanControllerDetailsById(id: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'id': 'id'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getWirelessLanControllerDetailsById')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('ciscoDNACenterPackagesSummary')
def ciscoDNACenterPackagesSummary():
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('ciscoDNACenterPackagesSummary')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getRFProfilesCount')
def getRFProfilesCount():
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getRFProfilesCount')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDevicesPerAdvisory')
def getDevicesPerAdvisory(advisoryId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'advisoryId': 'advisoryId'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getDevicesPerAdvisory')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getAccessPointConfigurationTaskResult')
def getAccessPointConfigurationTaskResult(task_id: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'task_id': 'task_id'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getAccessPointConfigurationTaskResult')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getComplianceDetail')
def getComplianceDetail(complianceType: str = None, complianceStatus: str = None, deviceUuid: str = None, offset: float = None, limit: float = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'complianceType': 'complianceType', 'complianceStatus': 'complianceStatus', 'deviceUuid': 'deviceUuid', 'offset': 'offset', 'limit': 'limit'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getComplianceDetail')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('returnsTheCountOfVLANsMappedToSSIDsInAFabricSite.')
def returnsTheCountOfVLANsMappedToSSIDsInAFabricSite_(Content_Type: str, fabricId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'Content-Type': 'Content_Type', 'fabricId': 'fabricId'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('returnsTheCountOfVLANsMappedToSSIDsInAFabricSite_')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getGlobalCredentials')
def getGlobalCredentials(credentialSubType: str, sortBy: str = None, order: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'credentialSubType': 'credentialSubType', 'sortBy': 'sortBy', 'order': 'order'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getGlobalCredentials')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getComplianceStatus')
def getComplianceStatus(complianceStatus: str = None, deviceUuid: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'complianceStatus': 'complianceStatus', 'deviceUuid': 'deviceUuid'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getComplianceStatus')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getSNMPDestination')
def getSNMPDestination(configId: str = None, offset: float = None, limit: float = None, sortBy: str = None, order: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'configId': 'configId', 'offset': 'offset', 'limit': 'limit', 'sortBy': 'sortBy', 'order': 'order'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getSNMPDestination')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getProvisionedDevicesCount')
def getProvisionedDevicesCount(siteId: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'siteId': 'siteId'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getProvisionedDevicesCount')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('returnsListOfSoftwareImages')
def returnsListOfSoftwareImages(siteId: str = None, productNameOrdinal: float = None, supervisorProductNameOrdinal: float = None, imported: bool = None, name: str = None, version: str = None, golden: bool = None, integrity: str = None, hasAddonImages: bool = None, isAddonImages: bool = None, offset: float = None, limit: float = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'siteId': 'siteId', 'productNameOrdinal': 'productNameOrdinal', 'supervisorProductNameOrdinal': 'supervisorProductNameOrdinal', 'imported': 'imported', 'name': 'name', 'version': 'version', 'golden': 'golden', 'integrity': 'integrity', 'hasAddonImages': 'hasAddonImages', 'isAddonImages': 'isAddonImages', 'offset': 'offset', 'limit': 'limit'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('returnsListOfSoftwareImages')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getInterfacesCount')
def getInterfacesCount():
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getInterfacesCount')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('readListOfSiteHealthSummaries.')
def readListOfSiteHealthSummaries_(X_CALLER_ID: str = None, startTime: float = None, endTime: float = None, limit: float = None, offset: float = None, sortBy: str = None, order: str = None, siteHierarchy: str = None, siteHierarchyId: str = None, siteType: str = None, id: str = None, view: str = None, attribute: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'X-CALLER-ID': 'X_CALLER_ID', 'startTime': 'startTime', 'endTime': 'endTime', 'limit': 'limit', 'offset': 'offset', 'sortBy': 'sortBy', 'order': 'order', 'siteHierarchy': 'siteHierarchy', 'siteHierarchyId': 'siteHierarchyId', 'siteType': 'siteType', 'id': 'id', 'view': 'view', 'attribute': 'attribute'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('readListOfSiteHealthSummaries_')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceList-2')
def getDeviceList_2(limit: int = None, offset: int = None, sort: list = None, sortOrder: str = None, serialNumber: list = None, state: list = None, onbState: list = None, name: list = None, pid: list = None, source: list = None, workflowId: list = None, workflowName: list = None, smartAccountId: list = None, virtualAccountId: list = None, lastContact: bool = None, macAddress: str = None, hostname: str = None, siteName: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'limit': 'limit', 'offset': 'offset', 'sort': 'sort', 'sortOrder': 'sortOrder', 'serialNumber': 'serialNumber', 'state': 'state', 'onbState': 'onbState', 'name': 'name', 'pid': 'pid', 'source': 'source', 'workflowId': 'workflowId', 'workflowName': 'workflowName', 'smartAccountId': 'smartAccountId', 'virtualAccountId': 'virtualAccountId', 'lastContact': 'lastContact', 'macAddress': 'macAddress', 'hostname': 'hostname', 'siteName': 'siteName'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getDeviceList_2')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getTasks-2')
def getTasks_2(startTime: str = None, endTime: str = None, data: str = None, errorCode: str = None, serviceType: str = None, username: str = None, progress: str = None, isError: str = None, failureReason: str = None, parentId: str = None, offset: int = None, limit: int = None, sortBy: str = None, order: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'startTime': 'startTime', 'endTime': 'endTime', 'data': 'data', 'errorCode': 'errorCode', 'serviceType': 'serviceType', 'username': 'username', 'progress': 'progress', 'isError': 'isError', 'failureReason': 'failureReason', 'parentId': 'parentId', 'offset': 'offset', 'limit': 'limit', 'sortBy': 'sortBy', 'order': 'order'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getTasks_2')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getModules')
def getModules(deviceId: str, limit: int = None, offset: int = None, nameList: list = None, vendorEquipmentTypeList: list = None, partNumberList: list = None, operationalStateCodeList: list = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'deviceId': 'deviceId', 'limit': 'limit', 'offset': 'offset', 'nameList': 'nameList', 'vendorEquipmentTypeList': 'vendorEquipmentTypeList', 'partNumberList': 'partNumberList', 'operationalStateCodeList': 'operationalStateCodeList'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getModules')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('retrievesTheCountOfAssignedNetworkDeviceProducts')
def retrievesTheCountOfAssignedNetworkDeviceProducts(imageId: str, productName: str = None, productId: str = None, recommended: str = None, assigned: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'imageId': 'imageId', 'productName': 'productName', 'productId': 'productId', 'recommended': 'recommended', 'assigned': 'assigned'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('retrievesTheCountOfAssignedNetworkDeviceProducts')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getRest_WebhookSubscriptionDetails')
def getRest_WebhookSubscriptionDetails(name: str = None, instanceId: str = None, offset: float = None, limit: float = None, sortBy: str = None, order: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'name': 'name', 'instanceId': 'instanceId', 'offset': 'offset', 'limit': 'limit', 'sortBy': 'sortBy', 'order': 'order'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getRest_WebhookSubscriptionDetails')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('WebhookSubscriptionDetail')(globals()['getRest_WebhookSubscriptionDetails'])

# alias → easier for LLM
register('WebhookSubscriptionDetails')(globals()['getRest_WebhookSubscriptionDetails'])

@register('WebhookSubscriptionDetail')
def WebhookSubscriptionDetail(name: str = None, instanceId: str = None, offset: float = None, limit: float = None, sortBy: str = None, order: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'name': 'name', 'instanceId': 'instanceId', 'offset': 'offset', 'limit': 'limit', 'sortBy': 'sortBy', 'order': 'order'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('WebhookSubscriptionDetail')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('WebhookSubscriptionDetails')
def WebhookSubscriptionDetails(name: str = None, instanceId: str = None, offset: float = None, limit: float = None, sortBy: str = None, order: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'name': 'name', 'instanceId': 'instanceId', 'offset': 'offset', 'limit': 'limit', 'sortBy': 'sortBy', 'order': 'order'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('WebhookSubscriptionDetails')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceHistory')
def getDeviceHistory(serialNumber: str, sort: list = None, sortOrder: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'serialNumber': 'serialNumber', 'sort': 'sort', 'sortOrder': 'sortOrder'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getDeviceHistory')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getApplicationPolicyQueuingProfileCount')
def getApplicationPolicyQueuingProfileCount():
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getApplicationPolicyQueuingProfileCount')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getsTheTotalNetworkDeviceCountsBasedOnTheProvidedQueryParameters')
def getsTheTotalNetworkDeviceCountsBasedOnTheProvidedQueryParameters(startTime: float = None, endTime: float = None, id: str = None, siteHierarchy: str = None, siteHierarchyId: str = None, siteId: str = None, managementIpAddress: str = None, macAddress: str = None, family: str = None, type: str = None, role: str = None, serialNumber: str = None, maintenanceMode: bool = None, softwareVersion: str = None, healthScore: str = None, view: str = None, attribute: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'startTime': 'startTime', 'endTime': 'endTime', 'id': 'id', 'siteHierarchy': 'siteHierarchy', 'siteHierarchyId': 'siteHierarchyId', 'siteId': 'siteId', 'managementIpAddress': 'managementIpAddress', 'macAddress': 'macAddress', 'family': 'family', 'type': 'type', 'role': 'role', 'serialNumber': 'serialNumber', 'maintenanceMode': 'maintenanceMode', 'softwareVersion': 'softwareVersion', 'healthScore': 'healthScore', 'view': 'view', 'attribute': 'attribute'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getsTheTotalNetworkDeviceCountsBasedOnTheProvidedQueryParameters')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getTaskTree')
def getTaskTree(taskId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'taskId': 'taskId'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getTaskTree')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDiscoveredNetworkDevicesByDiscoveryId')
def getDiscoveredNetworkDevicesByDiscoveryId(id: str, taskId: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'id': 'id', 'taskId': 'taskId'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getDiscoveredNetworkDevicesByDiscoveryId')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getStatusAPIForEvents')
def getStatusAPIForEvents(executionId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'executionId': 'executionId'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getStatusAPIForEvents')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getSiteAssignedNetworkDevicesCount')
def getSiteAssignedNetworkDevicesCount(siteId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'siteId': 'siteId'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getSiteAssignedNetworkDevicesCount')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkV2')
def getNetworkV2(siteId: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'siteId': 'siteId'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getNetworkV2')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceValuesThatMatchFullyOrPartiallyAnAttribute')
def getDeviceValuesThatMatchFullyOrPartiallyAnAttribute(vrfName: str = None, managementIpAddress: str = None, hostname: str = None, macAddress: str = None, family: str = None, collectionStatus: str = None, collectionInterval: str = None, softwareVersion: str = None, softwareType: str = None, reachabilityStatus: str = None, reachabilityFailureReason: str = None, errorCode: str = None, platformId: str = None, series: str = None, type: str = None, serialNumber: str = None, upTime: str = None, role: str = None, roleSource: str = None, associatedWlcIp: str = None, offset: int = None, limit: int = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'vrfName': 'vrfName', 'managementIpAddress': 'managementIpAddress', 'hostname': 'hostname', 'macAddress': 'macAddress', 'family': 'family', 'collectionStatus': 'collectionStatus', 'collectionInterval': 'collectionInterval', 'softwareVersion': 'softwareVersion', 'softwareType': 'softwareType', 'reachabilityStatus': 'reachabilityStatus', 'reachabilityFailureReason': 'reachabilityFailureReason', 'errorCode': 'errorCode', 'platformId': 'platformId', 'series': 'series', 'type': 'type', 'serialNumber': 'serialNumber', 'upTime': 'upTime', 'role': 'role', 'roleSource': 'roleSource', 'associatedWlcIp': 'associatedWlcIp', 'offset': 'offset', 'limit': 'limit'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getDeviceValuesThatMatchFullyOrPartiallyAnAttribute')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('sensors')
def sensors(siteId: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'siteId': 'siteId'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('sensors')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceInfoFromSDAFabric')
def getDeviceInfoFromSDAFabric(deviceManagementIpAddress: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'deviceManagementIpAddress': 'deviceManagementIpAddress'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getDeviceInfoFromSDAFabric')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getPortAssignmentForAccessPointInSDAFabric')
def getPortAssignmentForAccessPointInSDAFabric(deviceManagementIpAddress: str, interfaceName: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'deviceManagementIpAddress': 'deviceManagementIpAddress', 'interfaceName': 'interfaceName'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getPortAssignmentForAccessPointInSDAFabric')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getIPPoolFromSDAVirtualNetwork')
def getIPPoolFromSDAVirtualNetwork(siteNameHierarchy: str, virtualNetworkName: str, ipPoolName: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'siteNameHierarchy': 'siteNameHierarchy', 'virtualNetworkName': 'virtualNetworkName', 'ipPoolName': 'ipPoolName'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getIPPoolFromSDAVirtualNetwork')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getEdgeDeviceFromSDAFabric')
def getEdgeDeviceFromSDAFabric(deviceManagementIpAddress: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'deviceManagementIpAddress': 'deviceManagementIpAddress'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getEdgeDeviceFromSDAFabric')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getMulticastDetailsFromSDAFabric')
def getMulticastDetailsFromSDAFabric(siteNameHierarchy: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'siteNameHierarchy': 'siteNameHierarchy'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getMulticastDetailsFromSDAFabric')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getApplications')
def getApplications(offset: float = None, limit: float = None, name: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'offset': 'offset', 'limit': 'limit', 'name': 'name'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getApplications')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('retrieveRFProfiles')
def retrieveRFProfiles(rf_profile_name: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'rf-profile-name': 'rf_profile_name'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('retrieveRFProfiles')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetwork')
def getNetwork(siteId: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'siteId': 'siteId'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getNetwork')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getReserveIPSubpool')
def getReserveIPSubpool(siteId: str = None, offset: float = None, limit: float = None, ignoreInheritedGroups: str = None, poolUsage: str = None, groupName: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'siteId': 'siteId', 'offset': 'offset', 'limit': 'limit', 'ignoreInheritedGroups': 'ignoreInheritedGroups', 'poolUsage': 'poolUsage', 'groupName': 'groupName'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getReserveIPSubpool')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getTransitPeerNetworkInfo')
def getTransitPeerNetworkInfo(transitPeerNetworkName: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'transitPeerNetworkName': 'transitPeerNetworkName'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getTransitPeerNetworkInfo')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('clientProximity')
def clientProximity(username: str, number_days: float = None, time_resolution: float = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'username': 'username', 'number_days': 'number_days', 'time_resolution': 'time_resolution'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('clientProximity')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('applications')
def applications(siteId: str = None, deviceId: str = None, macAddress: str = None, startTime: float = None, endTime: float = None, applicationHealth: str = None, offset: float = None, limit: float = None, applicationName: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'siteId': 'siteId', 'deviceId': 'deviceId', 'macAddress': 'macAddress', 'startTime': 'startTime', 'endTime': 'endTime', 'applicationHealth': 'applicationHealth', 'offset': 'offset', 'limit': 'limit', 'applicationName': 'applicationName'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('applications')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getApplicationSets')
def getApplicationSets(offset: float = None, limit: float = None, name: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'offset': 'offset', 'limit': 'limit', 'name': 'name'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getApplicationSets')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getApplicationsCount')
def getApplicationsCount():
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getApplicationsCount')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getGlobalPool')
def getGlobalPool(offset: float = None, limit: float = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'offset': 'offset', 'limit': 'limit'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getGlobalPool')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getVNFromSDAFabric')
def getVNFromSDAFabric(virtualNetworkName: str, siteNameHierarchy: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'virtualNetworkName': 'virtualNetworkName', 'siteNameHierarchy': 'siteNameHierarchy'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getVNFromSDAFabric')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDefaultAuthenticationProfileFromSDAFabric')
def getDefaultAuthenticationProfileFromSDAFabric(siteNameHierarchy: str, authenticateTemplateName: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'siteNameHierarchy': 'siteNameHierarchy', 'authenticateTemplateName': 'authenticateTemplateName'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getDefaultAuthenticationProfileFromSDAFabric')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getProvisionedWiredDevice')
def getProvisionedWiredDevice(deviceManagementIpAddress: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'deviceManagementIpAddress': 'deviceManagementIpAddress'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getProvisionedWiredDevice')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceCredentialDetails')
def getDeviceCredentialDetails(siteId: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'siteId': 'siteId'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getDeviceCredentialDetails')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getSiteFromSDAFabric')
def getSiteFromSDAFabric(siteNameHierarchy: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'siteNameHierarchy': 'siteNameHierarchy'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getSiteFromSDAFabric')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getServiceProviderDetails')
def getServiceProviderDetails():
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getServiceProviderDetails')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getSite')
def getSite(name: str = None, siteId: str = None, type: str = None, offset: int = None, limit: int = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'name': 'name', 'siteId': 'siteId', 'type': 'type', 'offset': 'offset', 'limit': 'limit'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getSite')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getVirtualNetworkSummary')
def getVirtualNetworkSummary(siteNameHierarchy: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'siteNameHierarchy': 'siteNameHierarchy'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getVirtualNetworkSummary')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getWirelessProfile')
def getWirelessProfile(profileName: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'profileName': 'profileName'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getWirelessProfile')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getIssueEnrichmentDetails')
def getIssueEnrichmentDetails(entity_type: str, entity_value: str, __persistbapioutput: bool = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'entity_type': 'entity_type', 'entity_value': 'entity_value', '__persistbapioutput': '__persistbapioutput'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getIssueEnrichmentDetails')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('sensorTestResults')
def sensorTestResults(siteId: str = None, startTime: float = None, endTime: float = None, testFailureBy: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'siteId': 'siteId', 'startTime': 'startTime', 'endTime': 'endTime', 'testFailureBy': 'testFailureBy'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('sensorTestResults')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceRoleInSDAFabric')
def getDeviceRoleInSDAFabric(deviceManagementIpAddress: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'deviceManagementIpAddress': 'deviceManagementIpAddress'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getDeviceRoleInSDAFabric')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getEnterpriseSSID')
def getEnterpriseSSID(ssidName: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'ssidName': 'ssidName'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getEnterpriseSSID')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getBorderDeviceDetailFromSDAFabric')
def getBorderDeviceDetailFromSDAFabric(deviceManagementIpAddress: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'deviceManagementIpAddress': 'deviceManagementIpAddress'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getBorderDeviceDetailFromSDAFabric')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getPortAssignmentForUserDeviceInSDAFabric')
def getPortAssignmentForUserDeviceInSDAFabric(deviceManagementIpAddress: str, interfaceName: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'deviceManagementIpAddress': 'deviceManagementIpAddress', 'interfaceName': 'interfaceName'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getPortAssignmentForUserDeviceInSDAFabric')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getFailedITSMEvents')
def getFailedITSMEvents(instanceId: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'instanceId': 'instanceId'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getFailedITSMEvents')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getSSIDToIPPoolMapping')
def getSSIDToIPPoolMapping(vlanName: str, siteNameHierarchy: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'vlanName': 'vlanName', 'siteNameHierarchy': 'siteNameHierarchy'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getSSIDToIPPoolMapping')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getControlPlaneDeviceFromSDAFabric')
def getControlPlaneDeviceFromSDAFabric(deviceManagementIpAddress: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'deviceManagementIpAddress': 'deviceManagementIpAddress'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getControlPlaneDeviceFromSDAFabric')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getCMDBSyncStatus')
def getCMDBSyncStatus(status: str = None, date: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'status': 'status', 'date': 'date'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getCMDBSyncStatus')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getSiteCount')
def getSiteCount(siteId: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'siteId': 'siteId'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getSiteCount')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getClientEnrichmentDetails')
def getClientEnrichmentDetails(entity_type: str, entity_value: str, issueCategory: str = None, __persistbapioutput: bool = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'entity_type': 'entity_type', 'entity_value': 'entity_value', 'issueCategory': 'issueCategory', '__persistbapioutput': '__persistbapioutput'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getClientEnrichmentDetails')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getVirtualNetworkWithScalableGroups')
def getVirtualNetworkWithScalableGroups(virtualNetworkName: str):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'virtualNetworkName': 'virtualNetworkName'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getVirtualNetworkWithScalableGroups')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDynamicInterface')
def getDynamicInterface(__runsync: bool = None, __timeout: float = None, interface_name: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'__runsync': '__runsync', '__timeout': '__timeout', 'interface-name': 'interface_name'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getDynamicInterface')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getApplicationSetsCount')
def getApplicationSetsCount():
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getApplicationSetsCount')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getUserEnrichmentDetails')
def getUserEnrichmentDetails(entity_type: str, entity_value: str, __persistbapioutput: bool = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'entity_type': 'entity_type', 'entity_value': 'entity_value', '__persistbapioutput': '__persistbapioutput'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getUserEnrichmentDetails')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceEnrichmentDetails')
def getDeviceEnrichmentDetails(entity_type: str, entity_value: str, __persistbapioutput: bool = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'entity_type': 'entity_type', 'entity_value': 'entity_value', '__persistbapioutput': '__persistbapioutput'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getDeviceEnrichmentDetails')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getMembership')
def getMembership(siteId: str, offset: float = None, limit: float = None, deviceFamily: str = None, serialNumber: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'siteId': 'siteId', 'offset': 'offset', 'limit': 'limit', 'deviceFamily': 'deviceFamily', 'serialNumber': 'serialNumber'}.items()
        if locals_[san] is not None
    }

    target = CatalystClient().__getattr__('getMembership')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)
