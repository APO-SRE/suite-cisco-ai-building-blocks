# app/llm/function_dispatcher/catalyst_dispatcher.py
import os
from typing import Any
from app.llm.function_dispatcher import register
from app.llm.platform_clients.catalyst_client import CatalystClient

@register('retrievesNetworkDeviceProductNamesAssignedToASoftwareImage.')
def retrievesNetworkDeviceProductNamesAssignedToASoftwareImage_(imageId: str, productName: str = None, productId: str = None, recommended: str = None, assigned: str = None, offset: float = None, limit: float = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if imageId is not None:
        final_kwargs['imageId'] = imageId
    if productName is not None:
        final_kwargs['productName'] = productName
    if productId is not None:
        final_kwargs['productId'] = productId
    if recommended is not None:
        final_kwargs['recommended'] = recommended
    if assigned is not None:
        final_kwargs['assigned'] = assigned
    if offset is not None:
        final_kwargs['offset'] = offset
    if limit is not None:
        final_kwargs['limit'] = limit

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.retrievesNetworkDeviceProductNamesAssignedToASoftwareImage_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getsAllTheVersionsOfAGivenTemplate')
def getsAllTheVersionsOfAGivenTemplate(templateId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if templateId is not None:
        final_kwargs['templateId'] = templateId

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getsAllTheVersionsOfAGivenTemplate

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('returnsTheCountOfNetworkDeviceProductNamesForASite')
def returnsTheCountOfNetworkDeviceProductNamesForASite(siteId: str = None, productName: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if siteId is not None:
        final_kwargs['siteId'] = siteId
    if productName is not None:
        final_kwargs['productName'] = productName

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.returnsTheCountOfNetworkDeviceProductNamesForASite

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getMulticastVirtualNetworks')
def getMulticastVirtualNetworks(fabricId: str = None, virtualNetworkName: str = None, offset: float = None, limit: float = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if fabricId is not None:
        final_kwargs['fabricId'] = fabricId
    if virtualNetworkName is not None:
        final_kwargs['virtualNetworkName'] = virtualNetworkName
    if offset is not None:
        final_kwargs['offset'] = offset
    if limit is not None:
        final_kwargs['limit'] = limit

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getMulticastVirtualNetworks

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceControllabilitySettings')
def getDeviceControllabilitySettings():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getDeviceControllabilitySettings

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getChassisDetailsForDevice')
def getChassisDetailsForDevice(deviceId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if deviceId is not None:
        final_kwargs['deviceId'] = deviceId

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getChassisDetailsForDevice

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getsABuilding')
def getsABuilding(id: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if id is not None:
        final_kwargs['id'] = id

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getsABuilding

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getCountOfAllDiscoveryJobs')
def getCountOfAllDiscoveryJobs():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getCountOfAllDiscoveryJobs

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getViewsForAGivenViewGroup')
def getViewsForAGivenViewGroup(viewGroupId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if viewGroupId is not None:
        final_kwargs['viewGroupId'] = viewGroupId

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getViewsForAGivenViewGroup

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceById')
def getDeviceById(id: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if id is not None:
        final_kwargs['id'] = id

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getDeviceById

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('retrieveTheVLANsAndSSIDsMappedToTheVLANWithinAFabricSite.')
def retrieveTheVLANsAndSSIDsMappedToTheVLANWithinAFabricSite_(Content_Type: str, fabricId: str, limit: float = None, offset: float = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if Content_Type is not None:
        final_kwargs['Content-Type'] = Content_Type
    if fabricId is not None:
        final_kwargs['fabricId'] = fabricId
    if limit is not None:
        final_kwargs['limit'] = limit
    if offset is not None:
        final_kwargs['offset'] = offset

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.retrieveTheVLANsAndSSIDsMappedToTheVLANWithinAFabricSite_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('retrieveImageDistributionServers')
def retrieveImageDistributionServers():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.retrieveImageDistributionServers

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('retrieveTagsAssociatedWithNetworkDevices.')
def retrieveTagsAssociatedWithNetworkDevices_(offset: float = None, limit: float = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if offset is not None:
        final_kwargs['offset'] = offset
    if limit is not None:
        final_kwargs['limit'] = limit

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.retrieveTagsAssociatedWithNetworkDevices_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('statusOfTemplateDeployment')
def statusOfTemplateDeployment(deploymentId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if deploymentId is not None:
        final_kwargs['deploymentId'] = deploymentId

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.statusOfTemplateDeployment

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getIssueTriggerDefinitionForGivenId.')
def getIssueTriggerDefinitionForGivenId_(id: str, X_CALLER_ID: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if X_CALLER_ID is not None:
        final_kwargs['X-CALLER-ID'] = X_CALLER_ID
    if id is not None:
        final_kwargs['id'] = id

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getIssueTriggerDefinitionForGivenId_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('retrieveBannerSettingsForASite')
def retrieveBannerSettingsForASite(id: str, _inherited: bool = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if id is not None:
        final_kwargs['id'] = id
    if _inherited is not None:
        final_kwargs['_inherited'] = _inherited

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.retrieveBannerSettingsForASite

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getSiteAssignedNetworkDevices')
def getSiteAssignedNetworkDevices(siteId: str, offset: float = None, limit: float = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if siteId is not None:
        final_kwargs['siteId'] = siteId
    if offset is not None:
        final_kwargs['offset'] = offset
    if limit is not None:
        final_kwargs['limit'] = limit

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getSiteAssignedNetworkDevices

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkDevicesCredentialsSyncStatus')
def getNetworkDevicesCredentialsSyncStatus(id: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if id is not None:
        final_kwargs['id'] = id

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkDevicesCredentialsSyncStatus

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getSoftwareImageDetails')
def getSoftwareImageDetails(imageUuid: str = None, name: str = None, family: str = None, applicationType: str = None, imageIntegrityStatus: str = None, version: str = None, imageSeries: str = None, imageName: str = None, isTaggedGolden: bool = None, isCCORecommended: bool = None, isCCOLatest: bool = None, createdTime: int = None, imageSizeGreaterThan: int = None, imageSizeLesserThan: int = None, sortBy: str = None, sortOrder: str = None, limit: int = None, offset: int = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if imageUuid is not None:
        final_kwargs['imageUuid'] = imageUuid
    if name is not None:
        final_kwargs['name'] = name
    if family is not None:
        final_kwargs['family'] = family
    if applicationType is not None:
        final_kwargs['applicationType'] = applicationType
    if imageIntegrityStatus is not None:
        final_kwargs['imageIntegrityStatus'] = imageIntegrityStatus
    if version is not None:
        final_kwargs['version'] = version
    if imageSeries is not None:
        final_kwargs['imageSeries'] = imageSeries
    if imageName is not None:
        final_kwargs['imageName'] = imageName
    if isTaggedGolden is not None:
        final_kwargs['isTaggedGolden'] = isTaggedGolden
    if isCCORecommended is not None:
        final_kwargs['isCCORecommended'] = isCCORecommended
    if isCCOLatest is not None:
        final_kwargs['isCCOLatest'] = isCCOLatest
    if createdTime is not None:
        final_kwargs['createdTime'] = createdTime
    if imageSizeGreaterThan is not None:
        final_kwargs['imageSizeGreaterThan'] = imageSizeGreaterThan
    if imageSizeLesserThan is not None:
        final_kwargs['imageSizeLesserThan'] = imageSizeLesserThan
    if sortBy is not None:
        final_kwargs['sortBy'] = sortBy
    if sortOrder is not None:
        final_kwargs['sortOrder'] = sortOrder
    if limit is not None:
        final_kwargs['limit'] = limit
    if offset is not None:
        final_kwargs['offset'] = offset

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getSoftwareImageDetails

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getInterfaceByID')
def getInterfaceByID(id: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if id is not None:
        final_kwargs['id'] = id

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getInterfaceByID

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getAnycastGateways')
def getAnycastGateways(id: str = None, fabricId: str = None, virtualNetworkName: str = None, ipPoolName: str = None, vlanName: str = None, vlanId: float = None, offset: float = None, limit: float = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if id is not None:
        final_kwargs['id'] = id
    if fabricId is not None:
        final_kwargs['fabricId'] = fabricId
    if virtualNetworkName is not None:
        final_kwargs['virtualNetworkName'] = virtualNetworkName
    if ipPoolName is not None:
        final_kwargs['ipPoolName'] = ipPoolName
    if vlanName is not None:
        final_kwargs['vlanName'] = vlanName
    if vlanId is not None:
        final_kwargs['vlanId'] = vlanId
    if offset is not None:
        final_kwargs['offset'] = offset
    if limit is not None:
        final_kwargs['limit'] = limit

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getAnycastGateways

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getApplicationSet_s')
def getApplicationSet_s(attributes: str, offset: float, limit: float, name: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if attributes is not None:
        final_kwargs['attributes'] = attributes
    if name is not None:
        final_kwargs['name'] = name
    if offset is not None:
        final_kwargs['offset'] = offset
    if limit is not None:
        final_kwargs['limit'] = limit

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getApplicationSet_s

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('s')(globals()['getApplicationSet_s'])

@register('s')
def s(attributes: str, offset: float, limit: float, name: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if attributes is not None:
        final_kwargs['attributes'] = attributes
    if name is not None:
        final_kwargs['name'] = name
    if offset is not None:
        final_kwargs['offset'] = offset
    if limit is not None:
        final_kwargs['limit'] = limit

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.s

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getTagMembersById')
def getTagMembersById(id: str, memberType: str, offset: float = None, limit: float = None, memberAssociationType: str = None, level: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if id is not None:
        final_kwargs['id'] = id
    if memberType is not None:
        final_kwargs['memberType'] = memberType
    if offset is not None:
        final_kwargs['offset'] = offset
    if limit is not None:
        final_kwargs['limit'] = limit
    if memberAssociationType is not None:
        final_kwargs['memberAssociationType'] = memberAssociationType
    if level is not None:
        final_kwargs['level'] = level

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getTagMembersById

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getFabricSiteCount')
def getFabricSiteCount():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getFabricSiteCount

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('retrievesAllTheValidationSets')
def retrievesAllTheValidationSets(view: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if view is not None:
        final_kwargs['view'] = view

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.retrievesAllTheValidationSets

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('retrievesTheListOfSitesThatTheGivenNetworkProfileForSitesIsAssig')
def retrievesTheListOfSitesThatTheGivenNetworkProfileForSitesIsAssig(profileId: str, offset: float = None, limit: float = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if profileId is not None:
        final_kwargs['profileId'] = profileId
    if offset is not None:
        final_kwargs['offset'] = offset
    if limit is not None:
        final_kwargs['limit'] = limit

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.retrievesTheListOfSitesThatTheGivenNetworkProfileForSitesIsAssig

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getFabricDevicesLayer2HandoffsCount')
def getFabricDevicesLayer2HandoffsCount(fabricId: str, networkDeviceId: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if fabricId is not None:
        final_kwargs['fabricId'] = fabricId
    if networkDeviceId is not None:
        final_kwargs['networkDeviceId'] = networkDeviceId

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getFabricDevicesLayer2HandoffsCount

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('countOfEventSubscriptions')
def countOfEventSubscriptions(eventIds: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if eventIds is not None:
        final_kwargs['eventIds'] = eventIds

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.countOfEventSubscriptions

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getSSIDBySite')
def getSSIDBySite(siteId: str, limit: float = None, offset: float = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if siteId is not None:
        final_kwargs['siteId'] = siteId
    if limit is not None:
        final_kwargs['limit'] = limit
    if offset is not None:
        final_kwargs['offset'] = offset

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getSSIDBySite

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getITSMIntegrationSettingById')
def getITSMIntegrationSettingById(instanceId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if instanceId is not None:
        final_kwargs['instanceId'] = instanceId

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getITSMIntegrationSettingById

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDetailsOfASingleAssuranceEvent')
def getDetailsOfASingleAssuranceEvent(id: str, X_CALLER_ID: str = None, attribute: str = None, view: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if X_CALLER_ID is not None:
        final_kwargs['X-CALLER-ID'] = X_CALLER_ID
    if id is not None:
        final_kwargs['id'] = id
    if attribute is not None:
        final_kwargs['attribute'] = attribute
    if view is not None:
        final_kwargs['view'] = view

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getDetailsOfASingleAssuranceEvent

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getRFProfiles')
def getRFProfiles(limit: float = None, offset: float = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if limit is not None:
        final_kwargs['limit'] = limit
    if offset is not None:
        final_kwargs['offset'] = offset

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getRFProfiles

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('retrieveTelemetrySettingsForASite')
def retrieveTelemetrySettingsForASite(id: str, _inherited: bool = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if id is not None:
        final_kwargs['id'] = id
    if _inherited is not None:
        final_kwargs['_inherited'] = _inherited

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.retrieveTelemetrySettingsForASite

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getAllUser-Defined-Fields')
def getAllUser_Defined_Fields(id: str = None, name: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if id is not None:
        final_kwargs['id'] = id
    if name is not None:
        final_kwargs['name'] = name

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getAllUser_Defined_Fields

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('queryAssuranceEvents')
def queryAssuranceEvents(deviceFamily: str, X_CALLER_ID: str = None, startTime: float = None, endTime: float = None, messageType: str = None, severity: float = None, siteId: str = None, siteHierarchyId: str = None, networkDeviceName: str = None, networkDeviceId: str = None, apMac: str = None, clientMac: str = None, attribute: str = None, view: str = None, offset: float = None, limit: float = None, sortBy: str = None, order: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if X_CALLER_ID is not None:
        final_kwargs['X-CALLER-ID'] = X_CALLER_ID
    if deviceFamily is not None:
        final_kwargs['deviceFamily'] = deviceFamily
    if startTime is not None:
        final_kwargs['startTime'] = startTime
    if endTime is not None:
        final_kwargs['endTime'] = endTime
    if messageType is not None:
        final_kwargs['messageType'] = messageType
    if severity is not None:
        final_kwargs['severity'] = severity
    if siteId is not None:
        final_kwargs['siteId'] = siteId
    if siteHierarchyId is not None:
        final_kwargs['siteHierarchyId'] = siteHierarchyId
    if networkDeviceName is not None:
        final_kwargs['networkDeviceName'] = networkDeviceName
    if networkDeviceId is not None:
        final_kwargs['networkDeviceId'] = networkDeviceId
    if apMac is not None:
        final_kwargs['apMac'] = apMac
    if clientMac is not None:
        final_kwargs['clientMac'] = clientMac
    if attribute is not None:
        final_kwargs['attribute'] = attribute
    if view is not None:
        final_kwargs['view'] = view
    if offset is not None:
        final_kwargs['offset'] = offset
    if limit is not None:
        final_kwargs['limit'] = limit
    if sortBy is not None:
        final_kwargs['sortBy'] = sortBy
    if order is not None:
        final_kwargs['order'] = order

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.queryAssuranceEvents

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getFloorSettings')
def getFloorSettings():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getFloorSettings

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getTheTotalNumberOfIssuesForGivenSetOfFilters')
def getTheTotalNumberOfIssuesForGivenSetOfFilters(X_CALLER_ID: str = None, startTime: float = None, endTime: float = None, isGlobal: bool = None, priority: str = None, severity: str = None, status: str = None, entityType: str = None, category: str = None, deviceType: str = None, name: str = None, issueId: str = None, entityId: str = None, updatedBy: str = None, siteHierarchy: str = None, siteHierarchyId: str = None, siteName: str = None, siteId: str = None, fabricSiteId: str = None, fabricVnName: str = None, fabricTransitSiteId: str = None, networkDeviceId: str = None, networkDeviceIpAddress: str = None, macAddress: str = None, aiDriven: bool = None, fabricDriven: bool = None, fabricSiteDriven: bool = None, fabricVnDriven: bool = None, fabricTransitDriven: bool = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if X_CALLER_ID is not None:
        final_kwargs['X-CALLER-ID'] = X_CALLER_ID
    if startTime is not None:
        final_kwargs['startTime'] = startTime
    if endTime is not None:
        final_kwargs['endTime'] = endTime
    if isGlobal is not None:
        final_kwargs['isGlobal'] = isGlobal
    if priority is not None:
        final_kwargs['priority'] = priority
    if severity is not None:
        final_kwargs['severity'] = severity
    if status is not None:
        final_kwargs['status'] = status
    if entityType is not None:
        final_kwargs['entityType'] = entityType
    if category is not None:
        final_kwargs['category'] = category
    if deviceType is not None:
        final_kwargs['deviceType'] = deviceType
    if name is not None:
        final_kwargs['name'] = name
    if issueId is not None:
        final_kwargs['issueId'] = issueId
    if entityId is not None:
        final_kwargs['entityId'] = entityId
    if updatedBy is not None:
        final_kwargs['updatedBy'] = updatedBy
    if siteHierarchy is not None:
        final_kwargs['siteHierarchy'] = siteHierarchy
    if siteHierarchyId is not None:
        final_kwargs['siteHierarchyId'] = siteHierarchyId
    if siteName is not None:
        final_kwargs['siteName'] = siteName
    if siteId is not None:
        final_kwargs['siteId'] = siteId
    if fabricSiteId is not None:
        final_kwargs['fabricSiteId'] = fabricSiteId
    if fabricVnName is not None:
        final_kwargs['fabricVnName'] = fabricVnName
    if fabricTransitSiteId is not None:
        final_kwargs['fabricTransitSiteId'] = fabricTransitSiteId
    if networkDeviceId is not None:
        final_kwargs['networkDeviceId'] = networkDeviceId
    if networkDeviceIpAddress is not None:
        final_kwargs['networkDeviceIpAddress'] = networkDeviceIpAddress
    if macAddress is not None:
        final_kwargs['macAddress'] = macAddress
    if aiDriven is not None:
        final_kwargs['aiDriven'] = aiDriven
    if fabricDriven is not None:
        final_kwargs['fabricDriven'] = fabricDriven
    if fabricSiteDriven is not None:
        final_kwargs['fabricSiteDriven'] = fabricSiteDriven
    if fabricVnDriven is not None:
        final_kwargs['fabricVnDriven'] = fabricVnDriven
    if fabricTransitDriven is not None:
        final_kwargs['fabricTransitDriven'] = fabricTransitDriven

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getTheTotalNumberOfIssuesForGivenSetOfFilters

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getTag')
def getTag(name: str = None, additionalInfo_nameSpace: str = None, additionalInfo_attributes: str = None, level: str = None, offset: float = None, limit: float = None, size: str = None, field: str = None, sortBy: str = None, order: str = None, systemTag: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if name is not None:
        final_kwargs['name'] = name
    if additionalInfo_nameSpace is not None:
        final_kwargs['additionalInfo.nameSpace'] = additionalInfo_nameSpace
    if additionalInfo_attributes is not None:
        final_kwargs['additionalInfo.attributes'] = additionalInfo_attributes
    if level is not None:
        final_kwargs['level'] = level
    if offset is not None:
        final_kwargs['offset'] = offset
    if limit is not None:
        final_kwargs['limit'] = limit
    if size is not None:
        final_kwargs['size'] = size
    if field is not None:
        final_kwargs['field'] = field
    if sortBy is not None:
        final_kwargs['sortBy'] = sortBy
    if order is not None:
        final_kwargs['order'] = order
    if systemTag is not None:
        final_kwargs['systemTag'] = systemTag

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getTag

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getLayer2VirtualNetworks')
def getLayer2VirtualNetworks(id: str = None, fabricId: str = None, vlanName: str = None, vlanId: float = None, trafficType: str = None, associatedLayer3VirtualNetworkName: str = None, offset: float = None, limit: float = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if id is not None:
        final_kwargs['id'] = id
    if fabricId is not None:
        final_kwargs['fabricId'] = fabricId
    if vlanName is not None:
        final_kwargs['vlanName'] = vlanName
    if vlanId is not None:
        final_kwargs['vlanId'] = vlanId
    if trafficType is not None:
        final_kwargs['trafficType'] = trafficType
    if associatedLayer3VirtualNetworkName is not None:
        final_kwargs['associatedLayer3VirtualNetworkName'] = associatedLayer3VirtualNetworkName
    if offset is not None:
        final_kwargs['offset'] = offset
    if limit is not None:
        final_kwargs['limit'] = limit

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getLayer2VirtualNetworks

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getFabricZoneCount')
def getFabricZoneCount():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getFabricZoneCount

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getWebhookDestination')
def getWebhookDestination(webhookIds: str = None, offset: float = None, limit: float = None, sortBy: str = None, order: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if webhookIds is not None:
        final_kwargs['webhookIds'] = webhookIds
    if offset is not None:
        final_kwargs['offset'] = offset
    if limit is not None:
        final_kwargs['limit'] = limit
    if sortBy is not None:
        final_kwargs['sortBy'] = sortBy
    if order is not None:
        final_kwargs['order'] = order

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getWebhookDestination

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('retrieveTimeZoneSettingsForASite')
def retrieveTimeZoneSettingsForASite(id: str, _inherited: bool = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if id is not None:
        final_kwargs['id'] = id
    if _inherited is not None:
        final_kwargs['_inherited'] = _inherited

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.retrieveTimeZoneSettingsForASite

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceByID')
def getDeviceByID(id: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if id is not None:
        final_kwargs['id'] = id

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getDeviceByID

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getApplicationPolicyQueuingProfile')
def getApplicationPolicyQueuingProfile(name: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if name is not None:
        final_kwargs['name'] = name

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getApplicationPolicyQueuingProfile

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getSyslogDestination')
def getSyslogDestination(configId: str = None, name: str = None, protocol: str = None, offset: float = None, limit: float = None, sortBy: str = None, order: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if configId is not None:
        final_kwargs['configId'] = configId
    if name is not None:
        final_kwargs['name'] = name
    if protocol is not None:
        final_kwargs['protocol'] = protocol
    if offset is not None:
        final_kwargs['offset'] = offset
    if limit is not None:
        final_kwargs['limit'] = limit
    if sortBy is not None:
        final_kwargs['sortBy'] = sortBy
    if order is not None:
        final_kwargs['order'] = order

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getSyslogDestination

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getAll802.11beProfiles')
def getAll802_11beProfiles(limit: float = None, offset: float = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if limit is not None:
        final_kwargs['limit'] = limit
    if offset is not None:
        final_kwargs['offset'] = offset

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getAll802_11beProfiles

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getSyncResultForVirtualAccount')
def getSyncResultForVirtualAccount(domain: str, name: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if domain is not None:
        final_kwargs['domain'] = domain
    if name is not None:
        final_kwargs['name'] = name

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getSyncResultForVirtualAccount

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getAllTheCustomIssueDefinitionsBasedOnTheGivenFilters.')
def getAllTheCustomIssueDefinitionsBasedOnTheGivenFilters_(X_CALLER_ID: str = None, id: str = None, profileId: str = None, name: str = None, priority: str = None, isEnabled: bool = None, severity: float = None, facility: str = None, mnemonic: str = None, limit: float = None, offset: float = None, sortBy: str = None, order: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if X_CALLER_ID is not None:
        final_kwargs['X-CALLER-ID'] = X_CALLER_ID
    if id is not None:
        final_kwargs['id'] = id
    if profileId is not None:
        final_kwargs['profileId'] = profileId
    if name is not None:
        final_kwargs['name'] = name
    if priority is not None:
        final_kwargs['priority'] = priority
    if isEnabled is not None:
        final_kwargs['isEnabled'] = isEnabled
    if severity is not None:
        final_kwargs['severity'] = severity
    if facility is not None:
        final_kwargs['facility'] = facility
    if mnemonic is not None:
        final_kwargs['mnemonic'] = mnemonic
    if limit is not None:
        final_kwargs['limit'] = limit
    if offset is not None:
        final_kwargs['offset'] = offset
    if sortBy is not None:
        final_kwargs['sortBy'] = sortBy
    if order is not None:
        final_kwargs['order'] = order

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getAllTheCustomIssueDefinitionsBasedOnTheGivenFilters_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getApplicationPolicyDefault')
def getApplicationPolicyDefault():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getApplicationPolicyDefault

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getPrimaryManagedAPLocationsForSpecificWirelessController')
def getPrimaryManagedAPLocationsForSpecificWirelessController(networkDeviceId: str, limit: float = None, offset: float = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkDeviceId is not None:
        final_kwargs['networkDeviceId'] = networkDeviceId
    if limit is not None:
        final_kwargs['limit'] = limit
    if offset is not None:
        final_kwargs['offset'] = offset

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getPrimaryManagedAPLocationsForSpecificWirelessController

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getModuleInfoById')
def getModuleInfoById(id: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if id is not None:
        final_kwargs['id'] = id

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getModuleInfoById

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getFabricDevicesLayer3HandoffsWithSdaTransit')
def getFabricDevicesLayer3HandoffsWithSdaTransit(fabricId: str, networkDeviceId: str = None, offset: float = None, limit: float = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if fabricId is not None:
        final_kwargs['fabricId'] = fabricId
    if networkDeviceId is not None:
        final_kwargs['networkDeviceId'] = networkDeviceId
    if offset is not None:
        final_kwargs['offset'] = offset
    if limit is not None:
        final_kwargs['limit'] = limit

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getFabricDevicesLayer3HandoffsWithSdaTransit

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getFabricDevicesLayer3HandoffsWithIpTransit')
def getFabricDevicesLayer3HandoffsWithIpTransit(fabricId: str, networkDeviceId: str = None, offset: float = None, limit: float = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if fabricId is not None:
        final_kwargs['fabricId'] = fabricId
    if networkDeviceId is not None:
        final_kwargs['networkDeviceId'] = networkDeviceId
    if offset is not None:
        final_kwargs['offset'] = offset
    if limit is not None:
        final_kwargs['limit'] = limit

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getFabricDevicesLayer3HandoffsWithIpTransit

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('returnsNetworkDeviceProductNamesForASite')
def returnsNetworkDeviceProductNamesForASite(siteId: str = None, productName: str = None, offset: float = None, limit: float = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if siteId is not None:
        final_kwargs['siteId'] = siteId
    if productName is not None:
        final_kwargs['productName'] = productName
    if offset is not None:
        final_kwargs['offset'] = offset
    if limit is not None:
        final_kwargs['limit'] = limit

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.returnsNetworkDeviceProductNamesForASite

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('countOfNotifications')
def countOfNotifications(eventIds: str = None, startTime: float = None, endTime: float = None, category: str = None, type: str = None, severity: str = None, domain: str = None, subDomain: str = None, source: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if eventIds is not None:
        final_kwargs['eventIds'] = eventIds
    if startTime is not None:
        final_kwargs['startTime'] = startTime
    if endTime is not None:
        final_kwargs['endTime'] = endTime
    if category is not None:
        final_kwargs['category'] = category
    if type is not None:
        final_kwargs['type'] = type
    if severity is not None:
        final_kwargs['severity'] = severity
    if domain is not None:
        final_kwargs['domain'] = domain
    if subDomain is not None:
        final_kwargs['subDomain'] = subDomain
    if source is not None:
        final_kwargs['source'] = source

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.countOfNotifications

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getAScheduledReport')
def getAScheduledReport(reportId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if reportId is not None:
        final_kwargs['reportId'] = reportId

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getAScheduledReport

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getSiteHealth')
def getSiteHealth(siteType: str = None, offset: float = None, limit: float = None, timestamp: float = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if siteType is not None:
        final_kwargs['siteType'] = siteType
    if offset is not None:
        final_kwargs['offset'] = offset
    if limit is not None:
        final_kwargs['limit'] = limit
    if timestamp is not None:
        final_kwargs['timestamp'] = timestamp

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getSiteHealth

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('returnsPOEInterfaceDetailsForTheDevice.')
def returnsPOEInterfaceDetailsForTheDevice_(deviceUuid: str, interfaceNameList: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if deviceUuid is not None:
        final_kwargs['deviceUuid'] = deviceUuid
    if interfaceNameList is not None:
        final_kwargs['interfaceNameList'] = interfaceNameList

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.returnsPOEInterfaceDetailsForTheDevice_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getSitesCount')
def getSitesCount(name: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if name is not None:
        final_kwargs['name'] = name

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getSitesCount

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('retrievesTheListOfValidationWorkflows')
def retrievesTheListOfValidationWorkflows(startTime: float = None, endTime: float = None, runStatus: str = None, offset: float = None, limit: float = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if startTime is not None:
        final_kwargs['startTime'] = startTime
    if endTime is not None:
        final_kwargs['endTime'] = endTime
    if runStatus is not None:
        final_kwargs['runStatus'] = runStatus
    if offset is not None:
        final_kwargs['offset'] = offset
    if limit is not None:
        final_kwargs['limit'] = limit

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.retrievesTheListOfValidationWorkflows

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('readAnAggregatedSummaryOfSiteHealthData.')
def readAnAggregatedSummaryOfSiteHealthData_(X_CALLER_ID: str = None, startTime: float = None, endTime: float = None, siteHierarchy: str = None, siteHierarchyId: str = None, siteType: str = None, id: str = None, view: str = None, attribute: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if X_CALLER_ID is not None:
        final_kwargs['X-CALLER-ID'] = X_CALLER_ID
    if startTime is not None:
        final_kwargs['startTime'] = startTime
    if endTime is not None:
        final_kwargs['endTime'] = endTime
    if siteHierarchy is not None:
        final_kwargs['siteHierarchy'] = siteHierarchy
    if siteHierarchyId is not None:
        final_kwargs['siteHierarchyId'] = siteHierarchyId
    if siteType is not None:
        final_kwargs['siteType'] = siteType
    if id is not None:
        final_kwargs['id'] = id
    if view is not None:
        final_kwargs['view'] = view
    if attribute is not None:
        final_kwargs['attribute'] = attribute

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.readAnAggregatedSummaryOfSiteHealthData_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('retrievesTheCountOfProfilesThatTheGivenSiteHasBeenAssigned')
def retrievesTheCountOfProfilesThatTheGivenSiteHasBeenAssigned(siteId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if siteId is not None:
        final_kwargs['siteId'] = siteId

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.retrievesTheCountOfProfilesThatTheGivenSiteHasBeenAssigned

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getSiteCountV2')
def getSiteCountV2(id: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if id is not None:
        final_kwargs['id'] = id

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getSiteCountV2

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('returnsCountOfSoftwareImages')
def returnsCountOfSoftwareImages(siteId: str = None, productNameOrdinal: float = None, supervisorProductNameOrdinal: float = None, imported: bool = None, name: str = None, version: str = None, golden: str = None, integrity: str = None, hasAddonImages: bool = None, isAddonImages: bool = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if siteId is not None:
        final_kwargs['siteId'] = siteId
    if productNameOrdinal is not None:
        final_kwargs['productNameOrdinal'] = productNameOrdinal
    if supervisorProductNameOrdinal is not None:
        final_kwargs['supervisorProductNameOrdinal'] = supervisorProductNameOrdinal
    if imported is not None:
        final_kwargs['imported'] = imported
    if name is not None:
        final_kwargs['name'] = name
    if version is not None:
        final_kwargs['version'] = version
    if golden is not None:
        final_kwargs['golden'] = golden
    if integrity is not None:
        final_kwargs['integrity'] = integrity
    if hasAddonImages is not None:
        final_kwargs['hasAddonImages'] = hasAddonImages
    if isAddonImages is not None:
        final_kwargs['isAddonImages'] = isAddonImages

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.returnsCountOfSoftwareImages

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getExtranetPolicies')
def getExtranetPolicies(extranetPolicyName: str = None, offset: float = None, limit: float = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if extranetPolicyName is not None:
        final_kwargs['extranetPolicyName'] = extranetPolicyName
    if offset is not None:
        final_kwargs['offset'] = offset
    if limit is not None:
        final_kwargs['limit'] = limit

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getExtranetPolicies

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getWirelessProfileByID')
def getWirelessProfileByID(id: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if id is not None:
        final_kwargs['id'] = id

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getWirelessProfileByID

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getFlexibleReportScheduleByReportId')
def getFlexibleReportScheduleByReportId(Content_Type: str, reportId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if Content_Type is not None:
        final_kwargs['Content-Type'] = Content_Type
    if reportId is not None:
        final_kwargs['reportId'] = reportId

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getFlexibleReportScheduleByReportId

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getPortChannels')
def getPortChannels(fabricId: str = None, networkDeviceId: str = None, portChannelName: str = None, connectedDeviceType: str = None, offset: float = None, limit: float = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if fabricId is not None:
        final_kwargs['fabricId'] = fabricId
    if networkDeviceId is not None:
        final_kwargs['networkDeviceId'] = networkDeviceId
    if portChannelName is not None:
        final_kwargs['portChannelName'] = portChannelName
    if connectedDeviceType is not None:
        final_kwargs['connectedDeviceType'] = connectedDeviceType
    if offset is not None:
        final_kwargs['offset'] = offset
    if limit is not None:
        final_kwargs['limit'] = limit

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getPortChannels

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getRFProfileByID')
def getRFProfileByID(id: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if id is not None:
        final_kwargs['id'] = id

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getRFProfileByID

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getsTheTemplatesAvailable')
def getsTheTemplatesAvailable(projectId: str = None, softwareType: str = None, softwareVersion: str = None, productFamily: str = None, productSeries: str = None, productType: str = None, filterConflictingTemplates: bool = None, tags: list = None, projectNames: list = None, unCommitted: bool = None, sortOrder: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if projectId is not None:
        final_kwargs['projectId'] = projectId
    if softwareType is not None:
        final_kwargs['softwareType'] = softwareType
    if softwareVersion is not None:
        final_kwargs['softwareVersion'] = softwareVersion
    if productFamily is not None:
        final_kwargs['productFamily'] = productFamily
    if productSeries is not None:
        final_kwargs['productSeries'] = productSeries
    if productType is not None:
        final_kwargs['productType'] = productType
    if filterConflictingTemplates is not None:
        final_kwargs['filterConflictingTemplates'] = filterConflictingTemplates
    if tags is not None:
        final_kwargs['tags'] = tags
    if projectNames is not None:
        final_kwargs['projectNames'] = projectNames
    if unCommitted is not None:
        final_kwargs['unCommitted'] = unCommitted
    if sortOrder is not None:
        final_kwargs['sortOrder'] = sortOrder

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getsTheTemplatesAvailable

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getSyslogSubscriptionDetails')
def getSyslogSubscriptionDetails(name: str = None, instanceId: str = None, offset: float = None, limit: float = None, sortBy: str = None, order: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if name is not None:
        final_kwargs['name'] = name
    if instanceId is not None:
        final_kwargs['instanceId'] = instanceId
    if offset is not None:
        final_kwargs['offset'] = offset
    if limit is not None:
        final_kwargs['limit'] = limit
    if sortBy is not None:
        final_kwargs['sortBy'] = sortBy
    if order is not None:
        final_kwargs['order'] = order

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getSyslogSubscriptionDetails

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('returnsAllIssueTriggerDefinitionsForGivenFilters.')
def returnsAllIssueTriggerDefinitionsForGivenFilters_(X_CALLER_ID: str = None, deviceType: str = None, profileId: str = None, id: str = None, name: str = None, priority: str = None, issueEnabled: bool = None, attribute: str = None, offset: float = None, limit: float = None, sortBy: str = None, order: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if X_CALLER_ID is not None:
        final_kwargs['X-CALLER-ID'] = X_CALLER_ID
    if deviceType is not None:
        final_kwargs['deviceType'] = deviceType
    if profileId is not None:
        final_kwargs['profileId'] = profileId
    if id is not None:
        final_kwargs['id'] = id
    if name is not None:
        final_kwargs['name'] = name
    if priority is not None:
        final_kwargs['priority'] = priority
    if issueEnabled is not None:
        final_kwargs['issueEnabled'] = issueEnabled
    if attribute is not None:
        final_kwargs['attribute'] = attribute
    if offset is not None:
        final_kwargs['offset'] = offset
    if limit is not None:
        final_kwargs['limit'] = limit
    if sortBy is not None:
        final_kwargs['sortBy'] = sortBy
    if order is not None:
        final_kwargs['order'] = order

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.returnsAllIssueTriggerDefinitionsForGivenFilters_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getListOfScheduledReports')
def getListOfScheduledReports(viewGroupId: str = None, viewId: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if viewGroupId is not None:
        final_kwargs['viewGroupId'] = viewGroupId
    if viewId is not None:
        final_kwargs['viewId'] = viewId

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getListOfScheduledReports

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getAAAAttributeAPI')
def getAAAAttributeAPI():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getAAAAttributeAPI

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getClientDetail')
def getClientDetail(macAddress: str, timestamp: float = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if macAddress is not None:
        final_kwargs['macAddress'] = macAddress
    if timestamp is not None:
        final_kwargs['timestamp'] = timestamp

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getClientDetail

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('countTheNumberOfEvents')
def countTheNumberOfEvents(deviceFamily: str, X_CALLER_ID: str = None, startTime: str = None, endTime: str = None, messageType: str = None, severity: str = None, siteId: str = None, siteHierarchyId: str = None, networkDeviceName: str = None, networkDeviceId: str = None, apMac: str = None, clientMac: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if X_CALLER_ID is not None:
        final_kwargs['X-CALLER-ID'] = X_CALLER_ID
    if deviceFamily is not None:
        final_kwargs['deviceFamily'] = deviceFamily
    if startTime is not None:
        final_kwargs['startTime'] = startTime
    if endTime is not None:
        final_kwargs['endTime'] = endTime
    if messageType is not None:
        final_kwargs['messageType'] = messageType
    if severity is not None:
        final_kwargs['severity'] = severity
    if siteId is not None:
        final_kwargs['siteId'] = siteId
    if siteHierarchyId is not None:
        final_kwargs['siteHierarchyId'] = siteHierarchyId
    if networkDeviceName is not None:
        final_kwargs['networkDeviceName'] = networkDeviceName
    if networkDeviceId is not None:
        final_kwargs['networkDeviceId'] = networkDeviceId
    if apMac is not None:
        final_kwargs['apMac'] = apMac
    if clientMac is not None:
        final_kwargs['clientMac'] = clientMac

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.countTheNumberOfEvents

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getEoXStatusForAllDevices')
def getEoXStatusForAllDevices():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getEoXStatusForAllDevices

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getTagMemberCount')
def getTagMemberCount(id: str, memberType: str, memberAssociationType: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if id is not None:
        final_kwargs['id'] = id
    if memberType is not None:
        final_kwargs['memberType'] = memberType
    if memberAssociationType is not None:
        final_kwargs['memberAssociationType'] = memberAssociationType

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getTagMemberCount

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('retrievesConfigurationDetailsOfTheExternalIPAMServer.')
def retrievesConfigurationDetailsOfTheExternalIPAMServer_():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.retrievesConfigurationDetailsOfTheExternalIPAMServer_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getViewDetailsForAGivenViewGroup_View')
def getViewDetailsForAGivenViewGroup_View(viewGroupId: str, viewId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if viewGroupId is not None:
        final_kwargs['viewGroupId'] = viewGroupId
    if viewId is not None:
        final_kwargs['viewId'] = viewId

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getViewDetailsForAGivenViewGroup_View

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('View')(globals()['getViewDetailsForAGivenViewGroup_View'])

@register('View')
def View(viewGroupId: str, viewId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if viewGroupId is not None:
        final_kwargs['viewGroupId'] = viewGroupId
    if viewId is not None:
        final_kwargs['viewId'] = viewId

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.View

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getTheDetailsOfPhysicalComponentsOfTheGivenDevice.')
def getTheDetailsOfPhysicalComponentsOfTheGivenDevice_(deviceUuid: str, type: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if deviceUuid is not None:
        final_kwargs['deviceUuid'] = deviceUuid
    if type is not None:
        final_kwargs['type'] = type

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getTheDetailsOfPhysicalComponentsOfTheGivenDevice_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceInterfacesBySpecifiedRange')
def getDeviceInterfacesBySpecifiedRange(deviceId: str, startIndex: int, recordsToReturn: int):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if deviceId is not None:
        final_kwargs['deviceId'] = deviceId
    if startIndex is not None:
        final_kwargs['startIndex'] = startIndex
    if recordsToReturn is not None:
        final_kwargs['recordsToReturn'] = recordsToReturn

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getDeviceInterfacesBySpecifiedRange

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getPollingIntervalForAllDevices')
def getPollingIntervalForAllDevices():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getPollingIntervalForAllDevices

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceList')
def getDeviceList(hostname: list = None, managementIpAddress: list = None, macAddress: list = None, locationName: list = None, serialNumber: list = None, location: list = None, family: list = None, type: list = None, series: list = None, collectionStatus: list = None, collectionInterval: list = None, notSyncedForMinutes: list = None, errorCode: list = None, errorDescription: list = None, softwareVersion: list = None, softwareType: list = None, platformId: list = None, role: list = None, reachabilityStatus: list = None, upTime: list = None, associatedWlcIp: list = None, license_name: list = None, license_type: list = None, license_status: list = None, module_name: list = None, module_equpimenttype: list = None, module_servicestate: list = None, module_vendorequipmenttype: list = None, module_partnumber: list = None, module_operationstatecode: list = None, id: str = None, deviceSupportLevel: str = None, offset: int = None, limit: int = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if hostname is not None:
        final_kwargs['hostname'] = hostname
    if managementIpAddress is not None:
        final_kwargs['managementIpAddress'] = managementIpAddress
    if macAddress is not None:
        final_kwargs['macAddress'] = macAddress
    if locationName is not None:
        final_kwargs['locationName'] = locationName
    if serialNumber is not None:
        final_kwargs['serialNumber'] = serialNumber
    if location is not None:
        final_kwargs['location'] = location
    if family is not None:
        final_kwargs['family'] = family
    if type is not None:
        final_kwargs['type'] = type
    if series is not None:
        final_kwargs['series'] = series
    if collectionStatus is not None:
        final_kwargs['collectionStatus'] = collectionStatus
    if collectionInterval is not None:
        final_kwargs['collectionInterval'] = collectionInterval
    if notSyncedForMinutes is not None:
        final_kwargs['notSyncedForMinutes'] = notSyncedForMinutes
    if errorCode is not None:
        final_kwargs['errorCode'] = errorCode
    if errorDescription is not None:
        final_kwargs['errorDescription'] = errorDescription
    if softwareVersion is not None:
        final_kwargs['softwareVersion'] = softwareVersion
    if softwareType is not None:
        final_kwargs['softwareType'] = softwareType
    if platformId is not None:
        final_kwargs['platformId'] = platformId
    if role is not None:
        final_kwargs['role'] = role
    if reachabilityStatus is not None:
        final_kwargs['reachabilityStatus'] = reachabilityStatus
    if upTime is not None:
        final_kwargs['upTime'] = upTime
    if associatedWlcIp is not None:
        final_kwargs['associatedWlcIp'] = associatedWlcIp
    if license_name is not None:
        final_kwargs['license.name'] = license_name
    if license_type is not None:
        final_kwargs['license.type'] = license_type
    if license_status is not None:
        final_kwargs['license.status'] = license_status
    if module_name is not None:
        final_kwargs['module+name'] = module_name
    if module_equpimenttype is not None:
        final_kwargs['module+equpimenttype'] = module_equpimenttype
    if module_servicestate is not None:
        final_kwargs['module+servicestate'] = module_servicestate
    if module_vendorequipmenttype is not None:
        final_kwargs['module+vendorequipmenttype'] = module_vendorequipmenttype
    if module_partnumber is not None:
        final_kwargs['module+partnumber'] = module_partnumber
    if module_operationstatecode is not None:
        final_kwargs['module+operationstatecode'] = module_operationstatecode
    if id is not None:
        final_kwargs['id'] = id
    if deviceSupportLevel is not None:
        final_kwargs['deviceSupportLevel'] = deviceSupportLevel
    if offset is not None:
        final_kwargs['offset'] = offset
    if limit is not None:
        final_kwargs['limit'] = limit

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getDeviceList

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getAllKeywordsOfCLIsAcceptedByCommandRunner')
def getAllKeywordsOfCLIsAcceptedByCommandRunner():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getAllKeywordsOfCLIsAcceptedByCommandRunner

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getQosDeviceInterfaceInfo')
def getQosDeviceInterfaceInfo(networkDeviceId: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkDeviceId is not None:
        final_kwargs['networkDeviceId'] = networkDeviceId

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getQosDeviceInterfaceInfo

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('retrieveTheCountOfInterfacesThatAreAssociatedWithAtLeastOneTag.')
def retrieveTheCountOfInterfacesThatAreAssociatedWithAtLeastOneTag_():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.retrieveTheCountOfInterfacesThatAreAssociatedWithAtLeastOneTag_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceFamilyIdentifiers')
def getDeviceFamilyIdentifiers(Accept: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if Accept is not None:
        final_kwargs['Accept'] = Accept

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getDeviceFamilyIdentifiers

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getTaskCount')
def getTaskCount(startTime: str = None, endTime: str = None, data: str = None, errorCode: str = None, serviceType: str = None, username: str = None, progress: str = None, isError: str = None, failureReason: str = None, parentId: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if startTime is not None:
        final_kwargs['startTime'] = startTime
    if endTime is not None:
        final_kwargs['endTime'] = endTime
    if data is not None:
        final_kwargs['data'] = data
    if errorCode is not None:
        final_kwargs['errorCode'] = errorCode
    if serviceType is not None:
        final_kwargs['serviceType'] = serviceType
    if username is not None:
        final_kwargs['username'] = username
    if progress is not None:
        final_kwargs['progress'] = progress
    if isError is not None:
        final_kwargs['isError'] = isError
    if failureReason is not None:
        final_kwargs['failureReason'] = failureReason
    if parentId is not None:
        final_kwargs['parentId'] = parentId

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getTaskCount

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('devices')
def devices(deviceRole: str = None, siteId: str = None, health: str = None, startTime: float = None, endTime: float = None, limit: float = None, offset: float = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if deviceRole is not None:
        final_kwargs['deviceRole'] = deviceRole
    if siteId is not None:
        final_kwargs['siteId'] = siteId
    if health is not None:
        final_kwargs['health'] = health
    if startTime is not None:
        final_kwargs['startTime'] = startTime
    if endTime is not None:
        final_kwargs['endTime'] = endTime
    if limit is not None:
        final_kwargs['limit'] = limit
    if offset is not None:
        final_kwargs['offset'] = offset

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.devices

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getSSIDCountForSpecificWirelessController')
def getSSIDCountForSpecificWirelessController(networkDeviceId: str, adminStatus: bool = None, managed: bool = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkDeviceId is not None:
        final_kwargs['networkDeviceId'] = networkDeviceId
    if adminStatus is not None:
        final_kwargs['adminStatus'] = adminStatus
    if managed is not None:
        final_kwargs['managed'] = managed

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getSSIDCountForSpecificWirelessController

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('retrievesValidationDetailsForAValidationSet')
def retrievesValidationDetailsForAValidationSet(id: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if id is not None:
        final_kwargs['id'] = id

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.retrievesValidationDetailsForAValidationSet

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getSmartAccountList')
def getSmartAccountList():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getSmartAccountList

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getLayer3VirtualNetworks')
def getLayer3VirtualNetworks(virtualNetworkName: str = None, fabricId: str = None, anchoredSiteId: str = None, offset: float = None, limit: float = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if virtualNetworkName is not None:
        final_kwargs['virtualNetworkName'] = virtualNetworkName
    if fabricId is not None:
        final_kwargs['fabricId'] = fabricId
    if anchoredSiteId is not None:
        final_kwargs['anchoredSiteId'] = anchoredSiteId
    if offset is not None:
        final_kwargs['offset'] = offset
    if limit is not None:
        final_kwargs['limit'] = limit

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getLayer3VirtualNetworks

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getListOfAvailableNamespaces')
def getListOfAvailableNamespaces():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getListOfAvailableNamespaces

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getSSIDByID')
def getSSIDByID(siteId: str, id: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if siteId is not None:
        final_kwargs['siteId'] = siteId
    if id is not None:
        final_kwargs['id'] = id

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getSSIDByID

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('retrieveNetworkDeviceProductName')
def retrieveNetworkDeviceProductName(productNameOrdinal: float):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if productNameOrdinal is not None:
        final_kwargs['productNameOrdinal'] = productNameOrdinal

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.retrieveNetworkDeviceProductName

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getExecutionIdByReportId')
def getExecutionIdByReportId(Content_Type: str, reportId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if Content_Type is not None:
        final_kwargs['Content-Type'] = Content_Type
    if reportId is not None:
        final_kwargs['reportId'] = reportId

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getExecutionIdByReportId

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getMobilityGroupsCount')
def getMobilityGroupsCount():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getMobilityGroupsCount

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getTaskDetailsByID')
def getTaskDetailsByID(id: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if id is not None:
        final_kwargs['id'] = id

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getTaskDetailsByID

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('custom-promptSupportGETAPI')
def custom_promptSupportGETAPI():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.custom_promptSupportGETAPI

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getAdvisoriesList')
def getAdvisoriesList():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getAdvisoriesList

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceInterfaceVLANs')
def getDeviceInterfaceVLANs(id: str, interfaceType: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if id is not None:
        final_kwargs['id'] = id
    if interfaceType is not None:
        final_kwargs['interfaceType'] = interfaceType

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getDeviceInterfaceVLANs

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getListOfFiles')
def getListOfFiles(nameSpace: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if nameSpace is not None:
        final_kwargs['nameSpace'] = nameSpace

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getListOfFiles

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('retrieveSpecificImageDistributionServer')
def retrieveSpecificImageDistributionServer(id: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if id is not None:
        final_kwargs['id'] = id

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.retrieveSpecificImageDistributionServer

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getApplicationPolicy')
def getApplicationPolicy(policyScope: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if policyScope is not None:
        final_kwargs['policyScope'] = policyScope

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getApplicationPolicy

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getWorkflowById')
def getWorkflowById(id: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if id is not None:
        final_kwargs['id'] = id

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getWorkflowById

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getAdvisoriesSummary')
def getAdvisoriesSummary():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getAdvisoriesSummary

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getTagResourceTypes')
def getTagResourceTypes():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getTagResourceTypes

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getPortAssignmentCount')
def getPortAssignmentCount(fabricId: str = None, networkDeviceId: str = None, interfaceName: str = None, dataVlanName: str = None, voiceVlanName: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if fabricId is not None:
        final_kwargs['fabricId'] = fabricId
    if networkDeviceId is not None:
        final_kwargs['networkDeviceId'] = networkDeviceId
    if interfaceName is not None:
        final_kwargs['interfaceName'] = interfaceName
    if dataVlanName is not None:
        final_kwargs['dataVlanName'] = dataVlanName
    if voiceVlanName is not None:
        final_kwargs['voiceVlanName'] = voiceVlanName

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getPortAssignmentCount

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDiscoveriesByRange')
def getDiscoveriesByRange(startIndex: int, recordsToReturn: int):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if startIndex is not None:
        final_kwargs['startIndex'] = startIndex
    if recordsToReturn is not None:
        final_kwargs['recordsToReturn'] = recordsToReturn

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getDiscoveriesByRange

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getAllITSMIntegrationSettings')
def getAllITSMIntegrationSettings():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getAllITSMIntegrationSettings

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('licenseUsageDetails')
def licenseUsageDetails(smart_account_id: str, virtual_account_name: str, device_type: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if smart_account_id is not None:
        final_kwargs['smart_account_id'] = smart_account_id
    if virtual_account_name is not None:
        final_kwargs['virtual_account_name'] = virtual_account_name
    if device_type is not None:
        final_kwargs['device_type'] = device_type

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.licenseUsageDetails

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getsAnArea')
def getsAnArea(id: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if id is not None:
        final_kwargs['id'] = id

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getsAnArea

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getTheCountOfHealthScoreDefinitionsBasedOnProvidedFilters.')
def getTheCountOfHealthScoreDefinitionsBasedOnProvidedFilters_(X_CALLER_ID: str = None, deviceType: str = None, id: str = None, includeForOverallHealth: bool = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if X_CALLER_ID is not None:
        final_kwargs['X-CALLER-ID'] = X_CALLER_ID
    if deviceType is not None:
        final_kwargs['deviceType'] = deviceType
    if id is not None:
        final_kwargs['id'] = id
    if includeForOverallHealth is not None:
        final_kwargs['includeForOverallHealth'] = includeForOverallHealth

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getTheCountOfHealthScoreDefinitionsBasedOnProvidedFilters_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getExtranetPolicyCount')
def getExtranetPolicyCount():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getExtranetPolicyCount

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getResyncIntervalForTheNetworkDevice')
def getResyncIntervalForTheNetworkDevice(id: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if id is not None:
        final_kwargs['id'] = id

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getResyncIntervalForTheNetworkDevice

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getAllViewGroups')
def getAllViewGroups():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getAllViewGroups

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getEvents')
def getEvents(tags: str, eventId: str = None, offset: float = None, limit: float = None, sortBy: str = None, order: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if eventId is not None:
        final_kwargs['eventId'] = eventId
    if tags is not None:
        final_kwargs['tags'] = tags
    if offset is not None:
        final_kwargs['offset'] = offset
    if limit is not None:
        final_kwargs['limit'] = limit
    if sortBy is not None:
        final_kwargs['sortBy'] = sortBy
    if order is not None:
        final_kwargs['order'] = order

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getEvents

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getEmailEventSubscriptions')
def getEmailEventSubscriptions(eventIds: str = None, offset: float = None, limit: float = None, sortBy: str = None, order: str = None, domain: str = None, subDomain: str = None, category: str = None, type: str = None, name: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if eventIds is not None:
        final_kwargs['eventIds'] = eventIds
    if offset is not None:
        final_kwargs['offset'] = offset
    if limit is not None:
        final_kwargs['limit'] = limit
    if sortBy is not None:
        final_kwargs['sortBy'] = sortBy
    if order is not None:
        final_kwargs['order'] = order
    if domain is not None:
        final_kwargs['domain'] = domain
    if subDomain is not None:
        final_kwargs['subDomain'] = subDomain
    if category is not None:
        final_kwargs['category'] = category
    if type is not None:
        final_kwargs['type'] = type
    if name is not None:
        final_kwargs['name'] = name

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getEmailEventSubscriptions

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getEmailSubscriptionDetails')
def getEmailSubscriptionDetails(name: str = None, instanceId: str = None, offset: float = None, limit: float = None, sortBy: str = None, order: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if name is not None:
        final_kwargs['name'] = name
    if instanceId is not None:
        final_kwargs['instanceId'] = instanceId
    if offset is not None:
        final_kwargs['offset'] = offset
    if limit is not None:
        final_kwargs['limit'] = limit
    if sortBy is not None:
        final_kwargs['sortBy'] = sortBy
    if order is not None:
        final_kwargs['order'] = order

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getEmailSubscriptionDetails

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('retrieveAAASettingsForASite')
def retrieveAAASettingsForASite(id: str, _inherited: bool = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if id is not None:
        final_kwargs['id'] = id
    if _inherited is not None:
        final_kwargs['_inherited'] = _inherited

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.retrieveAAASettingsForASite

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getInterfaceDetailsByDeviceIdAndInterfaceName')
def getInterfaceDetailsByDeviceIdAndInterfaceName(deviceId: str, name: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if deviceId is not None:
        final_kwargs['deviceId'] = deviceId
    if name is not None:
        final_kwargs['name'] = name

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getInterfaceDetailsByDeviceIdAndInterfaceName

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getAllGlobalCredentialsV2')
def getAllGlobalCredentialsV2():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getAllGlobalCredentialsV2

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getAccessPoint_s_FactoryResetStatus')
def getAccessPoint_s_FactoryResetStatus(taskId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if taskId is not None:
        final_kwargs['taskId'] = taskId

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getAccessPoint_s_FactoryResetStatus

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('s_FactoryResetStatus')(globals()['getAccessPoint_s_FactoryResetStatus'])

# alias → easier for LLM
register('s_FactoryResetStatu')(globals()['getAccessPoint_s_FactoryResetStatus'])

@register('s_FactoryResetStatus')
def s_FactoryResetStatus(taskId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if taskId is not None:
        final_kwargs['taskId'] = taskId

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.s_FactoryResetStatus

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('FactoryResetStatu')(globals()['s_FactoryResetStatus'])

# alias → easier for LLM
register('FactoryResetStatus')(globals()['s_FactoryResetStatus'])

@register('s_FactoryResetStatu')
def s_FactoryResetStatu(taskId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if taskId is not None:
        final_kwargs['taskId'] = taskId

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.s_FactoryResetStatu

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('FactoryResetStatu')(globals()['s_FactoryResetStatu'])

@register('getNetworkDevicesFromDiscovery')
def getNetworkDevicesFromDiscovery(id: str, taskId: str = None, sortBy: str = None, sortOrder: str = None, ipAddress: list = None, pingStatus: list = None, snmpStatus: list = None, cliStatus: list = None, netconfStatus: list = None, httpStatus: list = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if id is not None:
        final_kwargs['id'] = id
    if taskId is not None:
        final_kwargs['taskId'] = taskId
    if sortBy is not None:
        final_kwargs['sortBy'] = sortBy
    if sortOrder is not None:
        final_kwargs['sortOrder'] = sortOrder
    if ipAddress is not None:
        final_kwargs['ipAddress'] = ipAddress
    if pingStatus is not None:
        final_kwargs['pingStatus'] = pingStatus
    if snmpStatus is not None:
        final_kwargs['snmpStatus'] = snmpStatus
    if cliStatus is not None:
        final_kwargs['cliStatus'] = cliStatus
    if netconfStatus is not None:
        final_kwargs['netconfStatus'] = netconfStatus
    if httpStatus is not None:
        final_kwargs['httpStatus'] = httpStatus

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkDevicesFromDiscovery

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getSites')
def getSites(name: str = None, nameHierarchy: str = None, type: str = None, _unitsOfMeasure: str = None, offset: int = None, limit: int = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if name is not None:
        final_kwargs['name'] = name
    if nameHierarchy is not None:
        final_kwargs['nameHierarchy'] = nameHierarchy
    if type is not None:
        final_kwargs['type'] = type
    if _unitsOfMeasure is not None:
        final_kwargs['_unitsOfMeasure'] = _unitsOfMeasure
    if offset is not None:
        final_kwargs['offset'] = offset
    if limit is not None:
        final_kwargs['limit'] = limit

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getSites

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('returnTheCountOfAllTheFabricSiteWhichHasSSIDToIPPoolMapping')
def returnTheCountOfAllTheFabricSiteWhichHasSSIDToIPPoolMapping():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.returnTheCountOfAllTheFabricSiteWhichHasSSIDToIPPoolMapping

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getEventSubscriptions')
def getEventSubscriptions(eventIds: str = None, offset: float = None, limit: float = None, sortBy: str = None, order: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if eventIds is not None:
        final_kwargs['eventIds'] = eventIds
    if offset is not None:
        final_kwargs['offset'] = offset
    if limit is not None:
        final_kwargs['limit'] = limit
    if sortBy is not None:
        final_kwargs['sortBy'] = sortBy
    if order is not None:
        final_kwargs['order'] = order

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getEventSubscriptions

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('readSiteHealthSummaryDataBySiteId.')
def readSiteHealthSummaryDataBySiteId_(id: str, X_CALLER_ID: str = None, startTime: float = None, endTime: float = None, view: str = None, attribute: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if X_CALLER_ID is not None:
        final_kwargs['X-CALLER-ID'] = X_CALLER_ID
    if id is not None:
        final_kwargs['id'] = id
    if startTime is not None:
        final_kwargs['startTime'] = startTime
    if endTime is not None:
        final_kwargs['endTime'] = endTime
    if view is not None:
        final_kwargs['view'] = view
    if attribute is not None:
        final_kwargs['attribute'] = attribute

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.readSiteHealthSummaryDataBySiteId_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getPlannedAccessPointsForFloor')
def getPlannedAccessPointsForFloor(floorId: str, limit: float = None, offset: float = None, radios: bool = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if floorId is not None:
        final_kwargs['floorId'] = floorId
    if limit is not None:
        final_kwargs['limit'] = limit
    if offset is not None:
        final_kwargs['offset'] = offset
    if radios is not None:
        final_kwargs['radios'] = radios

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getPlannedAccessPointsForFloor

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('returnListOfReplacementDevicesWithReplacementDetails')
def returnListOfReplacementDevicesWithReplacementDetails(faultyDeviceName: str = None, faultyDevicePlatform: str = None, replacementDevicePlatform: str = None, faultyDeviceSerialNumber: str = None, replacementDeviceSerialNumber: str = None, replacementStatus: list = None, family: list = None, sortBy: str = None, sortOrder: str = None, offset: int = None, limit: int = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if faultyDeviceName is not None:
        final_kwargs['faultyDeviceName'] = faultyDeviceName
    if faultyDevicePlatform is not None:
        final_kwargs['faultyDevicePlatform'] = faultyDevicePlatform
    if replacementDevicePlatform is not None:
        final_kwargs['replacementDevicePlatform'] = replacementDevicePlatform
    if faultyDeviceSerialNumber is not None:
        final_kwargs['faultyDeviceSerialNumber'] = faultyDeviceSerialNumber
    if replacementDeviceSerialNumber is not None:
        final_kwargs['replacementDeviceSerialNumber'] = replacementDeviceSerialNumber
    if replacementStatus is not None:
        final_kwargs['replacementStatus'] = replacementStatus
    if family is not None:
        final_kwargs['family'] = family
    if sortBy is not None:
        final_kwargs['sortBy'] = sortBy
    if sortOrder is not None:
        final_kwargs['sortOrder'] = sortOrder
    if offset is not None:
        final_kwargs['offset'] = offset
    if limit is not None:
        final_kwargs['limit'] = limit

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.returnListOfReplacementDevicesWithReplacementDetails

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDiscoveryById')
def getDiscoveryById(id: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if id is not None:
        final_kwargs['id'] = id

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getDiscoveryById

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getConfigurationArchiveDetails')
def getConfigurationArchiveDetails(deviceId: str = None, fileType: str = None, createdTime: str = None, createdBy: str = None, offset: float = None, limit: float = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if deviceId is not None:
        final_kwargs['deviceId'] = deviceId
    if fileType is not None:
        final_kwargs['fileType'] = fileType
    if createdTime is not None:
        final_kwargs['createdTime'] = createdTime
    if createdBy is not None:
        final_kwargs['createdBy'] = createdBy
    if offset is not None:
        final_kwargs['offset'] = offset
    if limit is not None:
        final_kwargs['limit'] = limit

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getConfigurationArchiveDetails

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getAdvisoriesPerDevice')
def getAdvisoriesPerDevice(deviceId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if deviceId is not None:
        final_kwargs['deviceId'] = deviceId

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getAdvisoriesPerDevice

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceInterfaceCountForMultipleDevices')
def getDeviceInterfaceCountForMultipleDevices():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getDeviceInterfaceCountForMultipleDevices

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('retrievesTheCountOfValidationWorkflows')
def retrievesTheCountOfValidationWorkflows(startTime: float = None, endTime: float = None, runStatus: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if startTime is not None:
        final_kwargs['startTime'] = startTime
    if endTime is not None:
        final_kwargs['endTime'] = endTime
    if runStatus is not None:
        final_kwargs['runStatus'] = runStatus

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.retrievesTheCountOfValidationWorkflows

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getSNMPProperties')
def getSNMPProperties():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getSNMPProperties

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getComplianceDetailCount')
def getComplianceDetailCount(complianceType: str = None, complianceStatus: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if complianceType is not None:
        final_kwargs['complianceType'] = complianceType
    if complianceStatus is not None:
        final_kwargs['complianceStatus'] = complianceStatus

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getComplianceDetailCount

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOverallClientHealth')
def getOverallClientHealth(timestamp: float = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if timestamp is not None:
        final_kwargs['timestamp'] = timestamp

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOverallClientHealth

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getLinecardDetails')
def getLinecardDetails(deviceUuid: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if deviceUuid is not None:
        final_kwargs['deviceUuid'] = deviceUuid

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getLinecardDetails

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getsTheTotalNetworkDeviceInterfaceCountsInTheSpecifiedTimeRange.')
def getsTheTotalNetworkDeviceInterfaceCountsInTheSpecifiedTimeRange_(startTime: float = None, endTime: float = None, siteHierarchy: str = None, siteHierarchyId: str = None, siteId: str = None, networkDeviceId: str = None, networkDeviceIpAddress: str = None, networkDeviceMacAddress: str = None, interfaceId: str = None, interfaceName: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if startTime is not None:
        final_kwargs['startTime'] = startTime
    if endTime is not None:
        final_kwargs['endTime'] = endTime
    if siteHierarchy is not None:
        final_kwargs['siteHierarchy'] = siteHierarchy
    if siteHierarchyId is not None:
        final_kwargs['siteHierarchyId'] = siteHierarchyId
    if siteId is not None:
        final_kwargs['siteId'] = siteId
    if networkDeviceId is not None:
        final_kwargs['networkDeviceId'] = networkDeviceId
    if networkDeviceIpAddress is not None:
        final_kwargs['networkDeviceIpAddress'] = networkDeviceIpAddress
    if networkDeviceMacAddress is not None:
        final_kwargs['networkDeviceMacAddress'] = networkDeviceMacAddress
    if interfaceId is not None:
        final_kwargs['interfaceId'] = interfaceId
    if interfaceName is not None:
        final_kwargs['interfaceName'] = interfaceName

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getsTheTotalNetworkDeviceInterfaceCountsInTheSpecifiedTimeRange_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getWirelessProfilesCount')
def getWirelessProfilesCount():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getWirelessProfilesCount

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getTagById')
def getTagById(id: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if id is not None:
        final_kwargs['id'] = id

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getTagById

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getAuditLogSummary')
def getAuditLogSummary(parentInstanceId: str = None, isParentOnly: bool = None, instanceId: str = None, name: str = None, eventId: str = None, category: str = None, severity: str = None, domain: str = None, subDomain: str = None, source: str = None, userId: str = None, context: str = None, eventHierarchy: str = None, siteId: str = None, deviceId: str = None, isSystemEvents: bool = None, description: str = None, startTime: float = None, endTime: float = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if parentInstanceId is not None:
        final_kwargs['parentInstanceId'] = parentInstanceId
    if isParentOnly is not None:
        final_kwargs['isParentOnly'] = isParentOnly
    if instanceId is not None:
        final_kwargs['instanceId'] = instanceId
    if name is not None:
        final_kwargs['name'] = name
    if eventId is not None:
        final_kwargs['eventId'] = eventId
    if category is not None:
        final_kwargs['category'] = category
    if severity is not None:
        final_kwargs['severity'] = severity
    if domain is not None:
        final_kwargs['domain'] = domain
    if subDomain is not None:
        final_kwargs['subDomain'] = subDomain
    if source is not None:
        final_kwargs['source'] = source
    if userId is not None:
        final_kwargs['userId'] = userId
    if context is not None:
        final_kwargs['context'] = context
    if eventHierarchy is not None:
        final_kwargs['eventHierarchy'] = eventHierarchy
    if siteId is not None:
        final_kwargs['siteId'] = siteId
    if deviceId is not None:
        final_kwargs['deviceId'] = deviceId
    if isSystemEvents is not None:
        final_kwargs['isSystemEvents'] = isSystemEvents
    if description is not None:
        final_kwargs['description'] = description
    if startTime is not None:
        final_kwargs['startTime'] = startTime
    if endTime is not None:
        final_kwargs['endTime'] = endTime

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getAuditLogSummary

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getsAListOfProjects')
def getsAListOfProjects(name: str = None, sortOrder: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if name is not None:
        final_kwargs['name'] = name
    if sortOrder is not None:
        final_kwargs['sortOrder'] = sortOrder

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getsAListOfProjects

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('systemHealthCountAPI')
def systemHealthCountAPI(domain: str = None, subdomain: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if domain is not None:
        final_kwargs['domain'] = domain
    if subdomain is not None:
        final_kwargs['subdomain'] = subdomain

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.systemHealthCountAPI

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getAuthenticationAndPolicyServers')
def getAuthenticationAndPolicyServers(isIseEnabled: bool = None, state: str = None, role: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if isIseEnabled is not None:
        final_kwargs['isIseEnabled'] = isIseEnabled
    if state is not None:
        final_kwargs['state'] = state
    if role is not None:
        final_kwargs['role'] = role

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getAuthenticationAndPolicyServers

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getSSIDCountBySite')
def getSSIDCountBySite(siteId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if siteId is not None:
        final_kwargs['siteId'] = siteId

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getSSIDCountBySite

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('deviceLicenseSummary')
def deviceLicenseSummary(page_number: float, order: str, limit: float, sort_by: str = None, dna_level: str = None, device_type: str = None, registration_status: str = None, virtual_account_name: str = None, smart_account_id: str = None, device_uuid: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if page_number is not None:
        final_kwargs['page_number'] = page_number
    if order is not None:
        final_kwargs['order'] = order
    if sort_by is not None:
        final_kwargs['sort_by'] = sort_by
    if dna_level is not None:
        final_kwargs['dna_level'] = dna_level
    if device_type is not None:
        final_kwargs['device_type'] = device_type
    if limit is not None:
        final_kwargs['limit'] = limit
    if registration_status is not None:
        final_kwargs['registration_status'] = registration_status
    if virtual_account_name is not None:
        final_kwargs['virtual_account_name'] = virtual_account_name
    if smart_account_id is not None:
        final_kwargs['smart_account_id'] = smart_account_id
    if device_uuid is not None:
        final_kwargs['device_uuid'] = device_uuid

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.deviceLicenseSummary

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('complianceDetailsOfDevice')
def complianceDetailsOfDevice(deviceUuid: str, category: str = None, complianceType: str = None, diffList: bool = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if deviceUuid is not None:
        final_kwargs['deviceUuid'] = deviceUuid
    if category is not None:
        final_kwargs['category'] = category
    if complianceType is not None:
        final_kwargs['complianceType'] = complianceType
    if diffList is not None:
        final_kwargs['diffList'] = diffList

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.complianceDetailsOfDevice

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('retrievesTheCountOfSitesThatTheGivenNetworkProfileForSitesIsAssi')
def retrievesTheCountOfSitesThatTheGivenNetworkProfileForSitesIsAssi(profileId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if profileId is not None:
        final_kwargs['profileId'] = profileId

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.retrievesTheCountOfSitesThatTheGivenNetworkProfileForSitesIsAssi

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getProvisionedDevices')
def getProvisionedDevices(id: str = None, networkDeviceId: str = None, siteId: str = None, offset: float = None, limit: float = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if id is not None:
        final_kwargs['id'] = id
    if networkDeviceId is not None:
        final_kwargs['networkDeviceId'] = networkDeviceId
    if siteId is not None:
        final_kwargs['siteId'] = siteId
    if offset is not None:
        final_kwargs['offset'] = offset
    if limit is not None:
        final_kwargs['limit'] = limit

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getProvisionedDevices

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('retrievesAllPreviousPathtracesSummary')
def retrievesAllPreviousPathtracesSummary(periodicRefresh: bool = None, sourceIP: str = None, destIP: str = None, sourcePort: float = None, destPort: float = None, gtCreateTime: float = None, ltCreateTime: float = None, protocol: str = None, status: str = None, taskId: str = None, lastUpdateTime: float = None, limit: float = None, offset: float = None, order: str = None, sortBy: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if periodicRefresh is not None:
        final_kwargs['periodicRefresh'] = periodicRefresh
    if sourceIP is not None:
        final_kwargs['sourceIP'] = sourceIP
    if destIP is not None:
        final_kwargs['destIP'] = destIP
    if sourcePort is not None:
        final_kwargs['sourcePort'] = sourcePort
    if destPort is not None:
        final_kwargs['destPort'] = destPort
    if gtCreateTime is not None:
        final_kwargs['gtCreateTime'] = gtCreateTime
    if ltCreateTime is not None:
        final_kwargs['ltCreateTime'] = ltCreateTime
    if protocol is not None:
        final_kwargs['protocol'] = protocol
    if status is not None:
        final_kwargs['status'] = status
    if taskId is not None:
        final_kwargs['taskId'] = taskId
    if lastUpdateTime is not None:
        final_kwargs['lastUpdateTime'] = lastUpdateTime
    if limit is not None:
        final_kwargs['limit'] = limit
    if offset is not None:
        final_kwargs['offset'] = offset
    if order is not None:
        final_kwargs['order'] = order
    if sortBy is not None:
        final_kwargs['sortBy'] = sortBy

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.retrievesAllPreviousPathtracesSummary

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('inventoryInsightDeviceLinkMismatchAPI')
def inventoryInsightDeviceLinkMismatchAPI(siteId: str, category: str, offset: int = None, limit: int = None, sortBy: str = None, order: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if siteId is not None:
        final_kwargs['siteId'] = siteId
    if offset is not None:
        final_kwargs['offset'] = offset
    if limit is not None:
        final_kwargs['limit'] = limit
    if category is not None:
        final_kwargs['category'] = category
    if sortBy is not None:
        final_kwargs['sortBy'] = sortBy
    if order is not None:
        final_kwargs['order'] = order

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.inventoryInsightDeviceLinkMismatchAPI

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getTheDeviceDataForTheGivenDeviceId_Uuid_')
def getTheDeviceDataForTheGivenDeviceId_Uuid_(id: str, startTime: float = None, endTime: float = None, view: str = None, attribute: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if id is not None:
        final_kwargs['id'] = id
    if startTime is not None:
        final_kwargs['startTime'] = startTime
    if endTime is not None:
        final_kwargs['endTime'] = endTime
    if view is not None:
        final_kwargs['view'] = view
    if attribute is not None:
        final_kwargs['attribute'] = attribute

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getTheDeviceDataForTheGivenDeviceId_Uuid_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('Uuid_')(globals()['getTheDeviceDataForTheGivenDeviceId_Uuid_'])

@register('Uuid_')
def Uuid_(id: str, startTime: float = None, endTime: float = None, view: str = None, attribute: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if id is not None:
        final_kwargs['id'] = id
    if startTime is not None:
        final_kwargs['startTime'] = startTime
    if endTime is not None:
        final_kwargs['endTime'] = endTime
    if view is not None:
        final_kwargs['view'] = view
    if attribute is not None:
        final_kwargs['attribute'] = attribute

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.Uuid_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('lANAutomationLogById')
def lANAutomationLogById(id: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if id is not None:
        final_kwargs['id'] = id

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.lANAutomationLogById

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceCredentialSettingsForASite')
def getDeviceCredentialSettingsForASite(id: str, _inherited: bool = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if id is not None:
        final_kwargs['id'] = id
    if _inherited is not None:
        final_kwargs['_inherited'] = _inherited

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getDeviceCredentialSettingsForASite

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceInterfaceCount')
def getDeviceInterfaceCount(deviceId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if deviceId is not None:
        final_kwargs['deviceId'] = deviceId

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getDeviceInterfaceCount

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('ciscoDNACenterReleaseSummary')
def ciscoDNACenterReleaseSummary():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.ciscoDNACenterReleaseSummary

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getLayer2VirtualNetworkCount')
def getLayer2VirtualNetworkCount(fabricId: str = None, vlanName: str = None, vlanId: float = None, trafficType: str = None, associatedLayer3VirtualNetworkName: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if fabricId is not None:
        final_kwargs['fabricId'] = fabricId
    if vlanName is not None:
        final_kwargs['vlanName'] = vlanName
    if vlanId is not None:
        final_kwargs['vlanId'] = vlanId
    if trafficType is not None:
        final_kwargs['trafficType'] = trafficType
    if associatedLayer3VirtualNetworkName is not None:
        final_kwargs['associatedLayer3VirtualNetworkName'] = associatedLayer3VirtualNetworkName

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getLayer2VirtualNetworkCount

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('retrievesTheCountOfNetworkProfilesForSites')
def retrievesTheCountOfNetworkProfilesForSites(type: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if type is not None:
        final_kwargs['type'] = type

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.retrievesTheCountOfNetworkProfilesForSites

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceCount')
def getDeviceCount(hostname: list = None, managementIpAddress: list = None, macAddress: list = None, locationName: list = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if hostname is not None:
        final_kwargs['hostname'] = hostname
    if managementIpAddress is not None:
        final_kwargs['managementIpAddress'] = managementIpAddress
    if macAddress is not None:
        final_kwargs['macAddress'] = macAddress
    if locationName is not None:
        final_kwargs['locationName'] = locationName

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getDeviceCount

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getFabricDevicesLayer2Handoffs')
def getFabricDevicesLayer2Handoffs(fabricId: str, networkDeviceId: str = None, offset: float = None, limit: float = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if fabricId is not None:
        final_kwargs['fabricId'] = fabricId
    if networkDeviceId is not None:
        final_kwargs['networkDeviceId'] = networkDeviceId
    if offset is not None:
        final_kwargs['offset'] = offset
    if limit is not None:
        final_kwargs['limit'] = limit

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getFabricDevicesLayer2Handoffs

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getSyslogEventSubscriptions')
def getSyslogEventSubscriptions(eventIds: str = None, offset: float = None, limit: float = None, sortBy: str = None, order: str = None, domain: str = None, subDomain: str = None, category: str = None, type: str = None, name: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if eventIds is not None:
        final_kwargs['eventIds'] = eventIds
    if offset is not None:
        final_kwargs['offset'] = offset
    if limit is not None:
        final_kwargs['limit'] = limit
    if sortBy is not None:
        final_kwargs['sortBy'] = sortBy
    if order is not None:
        final_kwargs['order'] = order
    if domain is not None:
        final_kwargs['domain'] = domain
    if subDomain is not None:
        final_kwargs['subDomain'] = subDomain
    if category is not None:
        final_kwargs['category'] = category
    if type is not None:
        final_kwargs['type'] = type
    if name is not None:
        final_kwargs['name'] = name

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getSyslogEventSubscriptions

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getVLANDetails')
def getVLANDetails():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getVLANDetails

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getAllMobilityGroups_')
def getAllMobilityGroups_(networkDeviceId: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkDeviceId is not None:
        final_kwargs['networkDeviceId'] = networkDeviceId

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getAllMobilityGroups_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getSiteV2')
def getSiteV2(groupNameHierarchy: str = None, id: str = None, type: str = None, offset: str = None, limit: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if groupNameHierarchy is not None:
        final_kwargs['groupNameHierarchy'] = groupNameHierarchy
    if id is not None:
        final_kwargs['id'] = id
    if type is not None:
        final_kwargs['type'] = type
    if offset is not None:
        final_kwargs['offset'] = offset
    if limit is not None:
        final_kwargs['limit'] = limit

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getSiteV2

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('systemHealthAPI')
def systemHealthAPI(summary: bool = None, domain: str = None, subdomain: str = None, limit: float = None, offset: float = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if summary is not None:
        final_kwargs['summary'] = summary
    if domain is not None:
        final_kwargs['domain'] = domain
    if subdomain is not None:
        final_kwargs['subdomain'] = subdomain
    if limit is not None:
        final_kwargs['limit'] = limit
    if offset is not None:
        final_kwargs['offset'] = offset

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.systemHealthAPI

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('lANAutomationStatusById')
def lANAutomationStatusById(id: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if id is not None:
        final_kwargs['id'] = id

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.lANAutomationStatusById

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getApplication_s')
def getApplication_s(attributes: str, offset: float, limit: float, name: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if attributes is not None:
        final_kwargs['attributes'] = attributes
    if name is not None:
        final_kwargs['name'] = name
    if offset is not None:
        final_kwargs['offset'] = offset
    if limit is not None:
        final_kwargs['limit'] = limit

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getApplication_s

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('s')(globals()['getApplication_s'])

@register('getFabricDevices')
def getFabricDevices(fabricId: str, networkDeviceId: str = None, deviceRoles: str = None, offset: float = None, limit: float = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if fabricId is not None:
        final_kwargs['fabricId'] = fabricId
    if networkDeviceId is not None:
        final_kwargs['networkDeviceId'] = networkDeviceId
    if deviceRoles is not None:
        final_kwargs['deviceRoles'] = deviceRoles
    if offset is not None:
        final_kwargs['offset'] = offset
    if limit is not None:
        final_kwargs['limit'] = limit

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getFabricDevices

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('get802.11beProfileByID')
def get802_11beProfileByID(id: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if id is not None:
        final_kwargs['id'] = id

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.get802_11beProfileByID

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getTasksCount')
def getTasksCount(startTime: int = None, endTime: int = None, parentId: str = None, rootId: str = None, status: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if startTime is not None:
        final_kwargs['startTime'] = startTime
    if endTime is not None:
        final_kwargs['endTime'] = endTime
    if parentId is not None:
        final_kwargs['parentId'] = parentId
    if rootId is not None:
        final_kwargs['rootId'] = rootId
    if status is not None:
        final_kwargs['status'] = status

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getTasksCount

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getsAFloor')
def getsAFloor(id: str, _unitsOfMeasure: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if id is not None:
        final_kwargs['id'] = id
    if _unitsOfMeasure is not None:
        final_kwargs['_unitsOfMeasure'] = _unitsOfMeasure

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getsAFloor

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getUsersAPI')
def getUsersAPI(invokeSource: str, authSource: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if invokeSource is not None:
        final_kwargs['invokeSource'] = invokeSource
    if authSource is not None:
        final_kwargs['authSource'] = authSource

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getUsersAPI

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getFabricZones')
def getFabricZones(id: str = None, siteId: str = None, offset: float = None, limit: float = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if id is not None:
        final_kwargs['id'] = id
    if siteId is not None:
        final_kwargs['siteId'] = siteId
    if offset is not None:
        final_kwargs['offset'] = offset
    if limit is not None:
        final_kwargs['limit'] = limit

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getFabricZones

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getVirtualAccountList')
def getVirtualAccountList(domain: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if domain is not None:
        final_kwargs['domain'] = domain

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getVirtualAccountList

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getQosDeviceInterfaceInfoCount')
def getQosDeviceInterfaceInfoCount():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getQosDeviceInterfaceInfoCount

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('countOfEvents')
def countOfEvents(tags: str, eventId: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if eventId is not None:
        final_kwargs['eventId'] = eventId
    if tags is not None:
        final_kwargs['tags'] = tags

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.countOfEvents

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOSPFInterfaces')
def getOSPFInterfaces():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOSPFInterfaces

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkDeviceImageUpdates')
def getNetworkDeviceImageUpdates(id: str = None, parentId: str = None, networkDeviceId: str = None, status: str = None, imageName: str = None, hostName: str = None, managementAddress: str = None, startTime: float = None, endTime: float = None, sortBy: str = None, order: str = None, offset: float = None, limit: float = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if id is not None:
        final_kwargs['id'] = id
    if parentId is not None:
        final_kwargs['parentId'] = parentId
    if networkDeviceId is not None:
        final_kwargs['networkDeviceId'] = networkDeviceId
    if status is not None:
        final_kwargs['status'] = status
    if imageName is not None:
        final_kwargs['imageName'] = imageName
    if hostName is not None:
        final_kwargs['hostName'] = hostName
    if managementAddress is not None:
        final_kwargs['managementAddress'] = managementAddress
    if startTime is not None:
        final_kwargs['startTime'] = startTime
    if endTime is not None:
        final_kwargs['endTime'] = endTime
    if sortBy is not None:
        final_kwargs['sortBy'] = sortBy
    if order is not None:
        final_kwargs['order'] = order
    if offset is not None:
        final_kwargs['offset'] = offset
    if limit is not None:
        final_kwargs['limit'] = limit

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkDeviceImageUpdates

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getTransitNetworks')
def getTransitNetworks(id: str = None, name: str = None, type: str = None, offset: float = None, limit: float = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if id is not None:
        final_kwargs['id'] = id
    if name is not None:
        final_kwargs['name'] = name
    if type is not None:
        final_kwargs['type'] = type
    if offset is not None:
        final_kwargs['offset'] = offset
    if limit is not None:
        final_kwargs['limit'] = limit

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getTransitNetworks

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getStackDetailsForDevice')
def getStackDetailsForDevice(deviceId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if deviceId is not None:
        final_kwargs['deviceId'] = deviceId

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getStackDetailsForDevice

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getApplicationSetCount')
def getApplicationSetCount(scalableGroupType: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if scalableGroupType is not None:
        final_kwargs['scalableGroupType'] = scalableGroupType

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getApplicationSetCount

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getWorkflowCount')
def getWorkflowCount(name: list = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if name is not None:
        final_kwargs['name'] = name

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getWorkflowCount

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('deviceComplianceStatus')
def deviceComplianceStatus(deviceUuid: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if deviceUuid is not None:
        final_kwargs['deviceUuid'] = deviceUuid

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.deviceComplianceStatus

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('retrievesPreviousPathtrace')
def retrievesPreviousPathtrace(flowAnalysisId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if flowAnalysisId is not None:
        final_kwargs['flowAnalysisId'] = flowAnalysisId

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.retrievesPreviousPathtrace

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOverallNetworkHealth')
def getOverallNetworkHealth(timestamp: float = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if timestamp is not None:
        final_kwargs['timestamp'] = timestamp

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOverallNetworkHealth

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getPnPGlobalSettings')
def getPnPGlobalSettings():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getPnPGlobalSettings

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getServiceProviderDetailsV2')
def getServiceProviderDetailsV2():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getServiceProviderDetailsV2

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getWirelessProfiles')
def getWirelessProfiles(limit: float = None, offset: float = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if limit is not None:
        final_kwargs['limit'] = limit
    if offset is not None:
        final_kwargs['offset'] = offset

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getWirelessProfiles

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getConfigTaskDetails')
def getConfigTaskDetails(parentTaskId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if parentTaskId is not None:
        final_kwargs['parentTaskId'] = parentTaskId

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getConfigTaskDetails

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('retrieveTheCountOfNetworkDevicesThatAreAssociatedWithAtLeastOneT')
def retrieveTheCountOfNetworkDevicesThatAreAssociatedWithAtLeastOneT():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.retrieveTheCountOfNetworkDevicesThatAreAssociatedWithAtLeastOneT

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getMulticastVirtualNetworkCount')
def getMulticastVirtualNetworkCount(fabricId: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if fabricId is not None:
        final_kwargs['fabricId'] = fabricId

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getMulticastVirtualNetworkCount

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getTagCount')
def getTagCount(name: str = None, nameSpace: str = None, attributeName: str = None, size: str = None, systemTag: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if name is not None:
        final_kwargs['name'] = name
    if nameSpace is not None:
        final_kwargs['nameSpace'] = nameSpace
    if attributeName is not None:
        final_kwargs['attributeName'] = attributeName
    if size is not None:
        final_kwargs['size'] = size
    if systemTag is not None:
        final_kwargs['systemTag'] = systemTag

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getTagCount

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceSummary')
def getDeviceSummary(id: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if id is not None:
        final_kwargs['id'] = id

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getDeviceSummary

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getAuthenticationProfiles')
def getAuthenticationProfiles(fabricId: str = None, authenticationProfileName: str = None, offset: float = None, limit: float = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if fabricId is not None:
        final_kwargs['fabricId'] = fabricId
    if authenticationProfileName is not None:
        final_kwargs['authenticationProfileName'] = authenticationProfileName
    if offset is not None:
        final_kwargs['offset'] = offset
    if limit is not None:
        final_kwargs['limit'] = limit

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getAuthenticationProfiles

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getAllFlexibleReportSchedules')
def getAllFlexibleReportSchedules(Content_Type: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if Content_Type is not None:
        final_kwargs['Content-Type'] = Content_Type

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getAllFlexibleReportSchedules

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('virtualAccountDetails')
def virtualAccountDetails(smart_account_id: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if smart_account_id is not None:
        final_kwargs['smart_account_id'] = smart_account_id

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.virtualAccountDetails

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getFunctionalCapabilityById')
def getFunctionalCapabilityById(id: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if id is not None:
        final_kwargs['id'] = id

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getFunctionalCapabilityById

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getFabricSites')
def getFabricSites(id: str = None, siteId: str = None, offset: float = None, limit: float = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if id is not None:
        final_kwargs['id'] = id
    if siteId is not None:
        final_kwargs['siteId'] = siteId
    if offset is not None:
        final_kwargs['offset'] = offset
    if limit is not None:
        final_kwargs['limit'] = limit

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getFabricSites

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getWorkflows')
def getWorkflows(limit: int = None, offset: int = None, sort: list = None, sortOrder: str = None, type: list = None, name: list = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if limit is not None:
        final_kwargs['limit'] = limit
    if offset is not None:
        final_kwargs['offset'] = offset
    if sort is not None:
        final_kwargs['sort'] = sort
    if sortOrder is not None:
        final_kwargs['sortOrder'] = sortOrder
    if type is not None:
        final_kwargs['type'] = type
    if name is not None:
        final_kwargs['name'] = name

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getWorkflows

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceConfigById')
def getDeviceConfigById(networkDeviceId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkDeviceId is not None:
        final_kwargs['networkDeviceId'] = networkDeviceId

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getDeviceConfigById

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('retrievesSpecificClientInformationMatchingTheMACAddress.')
def retrievesSpecificClientInformationMatchingTheMACAddress_(id: str, X_CALLER_ID: str = None, startTime: float = None, endTime: float = None, view: str = None, attribute: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if X_CALLER_ID is not None:
        final_kwargs['X-CALLER-ID'] = X_CALLER_ID
    if id is not None:
        final_kwargs['id'] = id
    if startTime is not None:
        final_kwargs['startTime'] = startTime
    if endTime is not None:
        final_kwargs['endTime'] = endTime
    if view is not None:
        final_kwargs['view'] = view
    if attribute is not None:
        final_kwargs['attribute'] = attribute

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.retrievesSpecificClientInformationMatchingTheMACAddress_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getOrganizationListForMeraki')
def getOrganizationListForMeraki(id: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if id is not None:
        final_kwargs['id'] = id

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getOrganizationListForMeraki

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getPollingIntervalById')
def getPollingIntervalById(id: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if id is not None:
        final_kwargs['id'] = id

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getPollingIntervalById

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNotifications')
def getNotifications(eventIds: str = None, startTime: float = None, endTime: float = None, category: str = None, type: str = None, severity: str = None, domain: str = None, subDomain: str = None, source: str = None, offset: float = None, limit: float = None, sortBy: str = None, order: str = None, tags: str = None, namespace: str = None, siteId: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if eventIds is not None:
        final_kwargs['eventIds'] = eventIds
    if startTime is not None:
        final_kwargs['startTime'] = startTime
    if endTime is not None:
        final_kwargs['endTime'] = endTime
    if category is not None:
        final_kwargs['category'] = category
    if type is not None:
        final_kwargs['type'] = type
    if severity is not None:
        final_kwargs['severity'] = severity
    if domain is not None:
        final_kwargs['domain'] = domain
    if subDomain is not None:
        final_kwargs['subDomain'] = subDomain
    if source is not None:
        final_kwargs['source'] = source
    if offset is not None:
        final_kwargs['offset'] = offset
    if limit is not None:
        final_kwargs['limit'] = limit
    if sortBy is not None:
        final_kwargs['sortBy'] = sortBy
    if order is not None:
        final_kwargs['order'] = order
    if tags is not None:
        final_kwargs['tags'] = tags
    if namespace is not None:
        final_kwargs['namespace'] = namespace
    if siteId is not None:
        final_kwargs['siteId'] = siteId

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNotifications

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getAllTheDetailsAndSuggestedActionsOfAnIssueForTheGivenIssueId')
def getAllTheDetailsAndSuggestedActionsOfAnIssueForTheGivenIssueId(id: str, Accept_Language: str = None, X_CALLER_ID: str = None, view: str = None, attribute: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if Accept_Language is not None:
        final_kwargs['Accept-Language'] = Accept_Language
    if X_CALLER_ID is not None:
        final_kwargs['X-CALLER-ID'] = X_CALLER_ID
    if id is not None:
        final_kwargs['id'] = id
    if view is not None:
        final_kwargs['view'] = view
    if attribute is not None:
        final_kwargs['attribute'] = attribute

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getAllTheDetailsAndSuggestedActionsOfAnIssueForTheGivenIssueId

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('legitOperationsForInterface')
def legitOperationsForInterface(interfaceUuid: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if interfaceUuid is not None:
        final_kwargs['interfaceUuid'] = interfaceUuid

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.legitOperationsForInterface

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceConfigCount')
def getDeviceConfigCount():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getDeviceConfigCount

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getISISInterfaces')
def getISISInterfaces():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getISISInterfaces

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('retrieveANetworkProfileForSitesById')
def retrieveANetworkProfileForSitesById(id: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if id is not None:
        final_kwargs['id'] = id

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.retrieveANetworkProfileForSitesById

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getAuditLogRecords')
def getAuditLogRecords(parentInstanceId: str = None, instanceId: str = None, name: str = None, eventId: str = None, category: str = None, severity: str = None, domain: str = None, subDomain: str = None, source: str = None, userId: str = None, context: str = None, eventHierarchy: str = None, siteId: str = None, deviceId: str = None, isSystemEvents: bool = None, description: str = None, offset: float = None, limit: float = None, startTime: float = None, endTime: float = None, sortBy: str = None, order: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if parentInstanceId is not None:
        final_kwargs['parentInstanceId'] = parentInstanceId
    if instanceId is not None:
        final_kwargs['instanceId'] = instanceId
    if name is not None:
        final_kwargs['name'] = name
    if eventId is not None:
        final_kwargs['eventId'] = eventId
    if category is not None:
        final_kwargs['category'] = category
    if severity is not None:
        final_kwargs['severity'] = severity
    if domain is not None:
        final_kwargs['domain'] = domain
    if subDomain is not None:
        final_kwargs['subDomain'] = subDomain
    if source is not None:
        final_kwargs['source'] = source
    if userId is not None:
        final_kwargs['userId'] = userId
    if context is not None:
        final_kwargs['context'] = context
    if eventHierarchy is not None:
        final_kwargs['eventHierarchy'] = eventHierarchy
    if siteId is not None:
        final_kwargs['siteId'] = siteId
    if deviceId is not None:
        final_kwargs['deviceId'] = deviceId
    if isSystemEvents is not None:
        final_kwargs['isSystemEvents'] = isSystemEvents
    if description is not None:
        final_kwargs['description'] = description
    if offset is not None:
        final_kwargs['offset'] = offset
    if limit is not None:
        final_kwargs['limit'] = limit
    if startTime is not None:
        final_kwargs['startTime'] = startTime
    if endTime is not None:
        final_kwargs['endTime'] = endTime
    if sortBy is not None:
        final_kwargs['sortBy'] = sortBy
    if order is not None:
        final_kwargs['order'] = order

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getAuditLogRecords

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('systemPerformanceHistoricalAPI')
def systemPerformanceHistoricalAPI(kpi: str = None, startTime: float = None, endTime: float = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if kpi is not None:
        final_kwargs['kpi'] = kpi
    if startTime is not None:
        final_kwargs['startTime'] = startTime
    if endTime is not None:
        final_kwargs['endTime'] = endTime

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.systemPerformanceHistoricalAPI

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getSupervisorCardDetail')
def getSupervisorCardDetail(deviceUuid: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if deviceUuid is not None:
        final_kwargs['deviceUuid'] = deviceUuid

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getSupervisorCardDetail

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('retrieveImageDistributionSettingsForASite')
def retrieveImageDistributionSettingsForASite(id: str, _inherited: bool = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if id is not None:
        final_kwargs['id'] = id
    if _inherited is not None:
        final_kwargs['_inherited'] = _inherited

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.retrieveImageDistributionSettingsForASite

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getSSIDDetailsForSpecificWirelessController')
def getSSIDDetailsForSpecificWirelessController(networkDeviceId: str, ssidName: str = None, adminStatus: bool = None, managed: bool = None, limit: float = None, offset: float = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkDeviceId is not None:
        final_kwargs['networkDeviceId'] = networkDeviceId
    if ssidName is not None:
        final_kwargs['ssidName'] = ssidName
    if adminStatus is not None:
        final_kwargs['adminStatus'] = adminStatus
    if managed is not None:
        final_kwargs['managed'] = managed
    if limit is not None:
        final_kwargs['limit'] = limit
    if offset is not None:
        final_kwargs['offset'] = offset

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getSSIDDetailsForSpecificWirelessController

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getsDetailsOfAGivenTemplate')
def getsDetailsOfAGivenTemplate(templateId: str, latestVersion: bool = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if templateId is not None:
        final_kwargs['templateId'] = templateId
    if latestVersion is not None:
        final_kwargs['latestVersion'] = latestVersion

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getsDetailsOfAGivenTemplate

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getEventArtifacts')
def getEventArtifacts(eventIds: str = None, tags: str = None, offset: float = None, limit: float = None, sortBy: str = None, order: str = None, search: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if eventIds is not None:
        final_kwargs['eventIds'] = eventIds
    if tags is not None:
        final_kwargs['tags'] = tags
    if offset is not None:
        final_kwargs['offset'] = offset
    if limit is not None:
        final_kwargs['limit'] = limit
    if sortBy is not None:
        final_kwargs['sortBy'] = sortBy
    if order is not None:
        final_kwargs['order'] = order
    if search is not None:
        final_kwargs['search'] = search

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getEventArtifacts

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getsTheDetailsOfAGivenProject.')
def getsTheDetailsOfAGivenProject_(projectId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if projectId is not None:
        final_kwargs['projectId'] = projectId

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getsTheDetailsOfAGivenProject_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('retrievesValidationWorkflowDetails')
def retrievesValidationWorkflowDetails(id: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if id is not None:
        final_kwargs['id'] = id

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.retrievesValidationWorkflowDetails

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getModuleCount')
def getModuleCount(deviceId: str, nameList: list = None, vendorEquipmentTypeList: list = None, partNumberList: list = None, operationalStateCodeList: list = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if deviceId is not None:
        final_kwargs['deviceId'] = deviceId
    if nameList is not None:
        final_kwargs['nameList'] = nameList
    if vendorEquipmentTypeList is not None:
        final_kwargs['vendorEquipmentTypeList'] = vendorEquipmentTypeList
    if partNumberList is not None:
        final_kwargs['partNumberList'] = partNumberList
    if operationalStateCodeList is not None:
        final_kwargs['operationalStateCodeList'] = operationalStateCodeList

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getModuleCount

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getTransitNetworksCount')
def getTransitNetworksCount(type: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if type is not None:
        final_kwargs['type'] = type

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getTransitNetworksCount

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('returnsAllTheFabricSitesThatHaveVLANToSSIDMapping.')
def returnsAllTheFabricSitesThatHaveVLANToSSIDMapping_(limit: float = None, offset: float = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if limit is not None:
        final_kwargs['limit'] = limit
    if offset is not None:
        final_kwargs['offset'] = offset

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.returnsAllTheFabricSitesThatHaveVLANToSSIDMapping_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('deviceCountDetails')
def deviceCountDetails(device_type: str = None, registration_status: str = None, dna_level: str = None, virtual_account_name: str = None, smart_account_id: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if device_type is not None:
        final_kwargs['device_type'] = device_type
    if registration_status is not None:
        final_kwargs['registration_status'] = registration_status
    if dna_level is not None:
        final_kwargs['dna_level'] = dna_level
    if virtual_account_name is not None:
        final_kwargs['virtual_account_name'] = virtual_account_name
    if smart_account_id is not None:
        final_kwargs['smart_account_id'] = smart_account_id

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.deviceCountDetails

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getAllExecutionDetailsForAGivenReport')
def getAllExecutionDetailsForAGivenReport(reportId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if reportId is not None:
        final_kwargs['reportId'] = reportId

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getAllExecutionDetailsForAGivenReport

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getRest_WebhookEventSubscriptions')
def getRest_WebhookEventSubscriptions(eventIds: str = None, offset: float = None, limit: float = None, sortBy: str = None, order: str = None, domain: str = None, subDomain: str = None, category: str = None, type: str = None, name: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if eventIds is not None:
        final_kwargs['eventIds'] = eventIds
    if offset is not None:
        final_kwargs['offset'] = offset
    if limit is not None:
        final_kwargs['limit'] = limit
    if sortBy is not None:
        final_kwargs['sortBy'] = sortBy
    if order is not None:
        final_kwargs['order'] = order
    if domain is not None:
        final_kwargs['domain'] = domain
    if subDomain is not None:
        final_kwargs['subDomain'] = subDomain
    if category is not None:
        final_kwargs['category'] = category
    if type is not None:
        final_kwargs['type'] = type
    if name is not None:
        final_kwargs['name'] = name

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getRest_WebhookEventSubscriptions

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('WebhookEventSubscription')(globals()['getRest_WebhookEventSubscriptions'])

# alias → easier for LLM
register('WebhookEventSubscriptions')(globals()['getRest_WebhookEventSubscriptions'])

@register('WebhookEventSubscription')
def WebhookEventSubscription(eventIds: str = None, offset: float = None, limit: float = None, sortBy: str = None, order: str = None, domain: str = None, subDomain: str = None, category: str = None, type: str = None, name: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if eventIds is not None:
        final_kwargs['eventIds'] = eventIds
    if offset is not None:
        final_kwargs['offset'] = offset
    if limit is not None:
        final_kwargs['limit'] = limit
    if sortBy is not None:
        final_kwargs['sortBy'] = sortBy
    if order is not None:
        final_kwargs['order'] = order
    if domain is not None:
        final_kwargs['domain'] = domain
    if subDomain is not None:
        final_kwargs['subDomain'] = subDomain
    if category is not None:
        final_kwargs['category'] = category
    if type is not None:
        final_kwargs['type'] = type
    if name is not None:
        final_kwargs['name'] = name

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.WebhookEventSubscription

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('WebhookEventSubscriptions')
def WebhookEventSubscriptions(eventIds: str = None, offset: float = None, limit: float = None, sortBy: str = None, order: str = None, domain: str = None, subDomain: str = None, category: str = None, type: str = None, name: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if eventIds is not None:
        final_kwargs['eventIds'] = eventIds
    if offset is not None:
        final_kwargs['offset'] = offset
    if limit is not None:
        final_kwargs['limit'] = limit
    if sortBy is not None:
        final_kwargs['sortBy'] = sortBy
    if order is not None:
        final_kwargs['order'] = order
    if domain is not None:
        final_kwargs['domain'] = domain
    if subDomain is not None:
        final_kwargs['subDomain'] = subDomain
    if category is not None:
        final_kwargs['category'] = category
    if type is not None:
        final_kwargs['type'] = type
    if name is not None:
        final_kwargs['name'] = name

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.WebhookEventSubscriptions

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getRolesAPI')
def getRolesAPI(invokeSource: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if invokeSource is not None:
        final_kwargs['invokeSource'] = invokeSource

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getRolesAPI

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getGoldenTagStatusOfAnImage.')
def getGoldenTagStatusOfAnImage_(Accept: str, siteId: str, deviceFamilyIdentifier: str, deviceRole: str, imageId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if Accept is not None:
        final_kwargs['Accept'] = Accept
    if siteId is not None:
        final_kwargs['siteId'] = siteId
    if deviceFamilyIdentifier is not None:
        final_kwargs['deviceFamilyIdentifier'] = deviceFamilyIdentifier
    if deviceRole is not None:
        final_kwargs['deviceRole'] = deviceRole
    if imageId is not None:
        final_kwargs['imageId'] = imageId

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getGoldenTagStatusOfAnImage_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getPortChannelCount')
def getPortChannelCount(fabricId: str = None, networkDeviceId: str = None, portChannelName: str = None, connectedDeviceType: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if fabricId is not None:
        final_kwargs['fabricId'] = fabricId
    if networkDeviceId is not None:
        final_kwargs['networkDeviceId'] = networkDeviceId
    if portChannelName is not None:
        final_kwargs['portChannelName'] = portChannelName
    if connectedDeviceType is not None:
        final_kwargs['connectedDeviceType'] = connectedDeviceType

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getPortChannelCount

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('mapsSupportedAccessPoints')
def mapsSupportedAccessPoints():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.mapsSupportedAccessPoints

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getAuditLogParentRecords')
def getAuditLogParentRecords(instanceId: str = None, name: str = None, eventId: str = None, category: str = None, severity: str = None, domain: str = None, subDomain: str = None, source: str = None, userId: str = None, context: str = None, eventHierarchy: str = None, siteId: str = None, deviceId: str = None, isSystemEvents: bool = None, description: str = None, offset: float = None, limit: float = None, startTime: float = None, endTime: float = None, sortBy: str = None, order: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if instanceId is not None:
        final_kwargs['instanceId'] = instanceId
    if name is not None:
        final_kwargs['name'] = name
    if eventId is not None:
        final_kwargs['eventId'] = eventId
    if category is not None:
        final_kwargs['category'] = category
    if severity is not None:
        final_kwargs['severity'] = severity
    if domain is not None:
        final_kwargs['domain'] = domain
    if subDomain is not None:
        final_kwargs['subDomain'] = subDomain
    if source is not None:
        final_kwargs['source'] = source
    if userId is not None:
        final_kwargs['userId'] = userId
    if context is not None:
        final_kwargs['context'] = context
    if eventHierarchy is not None:
        final_kwargs['eventHierarchy'] = eventHierarchy
    if siteId is not None:
        final_kwargs['siteId'] = siteId
    if deviceId is not None:
        final_kwargs['deviceId'] = deviceId
    if isSystemEvents is not None:
        final_kwargs['isSystemEvents'] = isSystemEvents
    if description is not None:
        final_kwargs['description'] = description
    if offset is not None:
        final_kwargs['offset'] = offset
    if limit is not None:
        final_kwargs['limit'] = limit
    if startTime is not None:
        final_kwargs['startTime'] = startTime
    if endTime is not None:
        final_kwargs['endTime'] = endTime
    if sortBy is not None:
        final_kwargs['sortBy'] = sortBy
    if order is not None:
        final_kwargs['order'] = order

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getAuditLogParentRecords

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('retrieveDNSSettingsForASite')
def retrieveDNSSettingsForASite(id: str, _inherited: bool = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if id is not None:
        final_kwargs['id'] = id
    if _inherited is not None:
        final_kwargs['_inherited'] = _inherited

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.retrieveDNSSettingsForASite

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getHealthScoreDefinitionForTheGivenId.')
def getHealthScoreDefinitionForTheGivenId_(id: str, X_CALLER_ID: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if X_CALLER_ID is not None:
        final_kwargs['X-CALLER-ID'] = X_CALLER_ID
    if id is not None:
        final_kwargs['id'] = id

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getHealthScoreDefinitionForTheGivenId_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getProject_s_Details')
def getProject_s_Details(id: str = None, name: str = None, offset: int = None, limit: int = None, sortOrder: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if id is not None:
        final_kwargs['id'] = id
    if name is not None:
        final_kwargs['name'] = name
    if offset is not None:
        final_kwargs['offset'] = offset
    if limit is not None:
        final_kwargs['limit'] = limit
    if sortOrder is not None:
        final_kwargs['sortOrder'] = sortOrder

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getProject_s_Details

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('s_Details')(globals()['getProject_s_Details'])

# alias → easier for LLM
register('s_Detail')(globals()['getProject_s_Details'])

@register('s_Details')
def s_Details(id: str = None, name: str = None, offset: int = None, limit: int = None, sortOrder: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if id is not None:
        final_kwargs['id'] = id
    if name is not None:
        final_kwargs['name'] = name
    if offset is not None:
        final_kwargs['offset'] = offset
    if limit is not None:
        final_kwargs['limit'] = limit
    if sortOrder is not None:
        final_kwargs['sortOrder'] = sortOrder

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.s_Details

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('Details')(globals()['s_Details'])

# alias → easier for LLM
register('Detail')(globals()['s_Details'])

@register('s_Detail')
def s_Detail(id: str = None, name: str = None, offset: int = None, limit: int = None, sortOrder: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if id is not None:
        final_kwargs['id'] = id
    if name is not None:
        final_kwargs['name'] = name
    if offset is not None:
        final_kwargs['offset'] = offset
    if limit is not None:
        final_kwargs['limit'] = limit
    if sortOrder is not None:
        final_kwargs['sortOrder'] = sortOrder

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.s_Detail

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('Detail')(globals()['s_Detail'])

@register('downloadAFileByFileId')
def downloadAFileByFileId(fileId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if fileId is not None:
        final_kwargs['fileId'] = fileId

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.downloadAFileByFileId

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getAllHealthScoreDefinitionsForGivenFilters.')
def getAllHealthScoreDefinitionsForGivenFilters_(X_CALLER_ID: str = None, deviceType: str = None, id: str = None, includeForOverallHealth: bool = None, attribute: str = None, offset: float = None, limit: float = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if X_CALLER_ID is not None:
        final_kwargs['X-CALLER-ID'] = X_CALLER_ID
    if deviceType is not None:
        final_kwargs['deviceType'] = deviceType
    if id is not None:
        final_kwargs['id'] = id
    if includeForOverallHealth is not None:
        final_kwargs['includeForOverallHealth'] = includeForOverallHealth
    if attribute is not None:
        final_kwargs['attribute'] = attribute
    if offset is not None:
        final_kwargs['offset'] = offset
    if limit is not None:
        final_kwargs['limit'] = limit

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getAllHealthScoreDefinitionsForGivenFilters_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getEmailDestination')
def getEmailDestination():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getEmailDestination

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getsInterfacesAlongWithStatisticsDataFromAllNetworkDevices.')
def getsInterfacesAlongWithStatisticsDataFromAllNetworkDevices_(startTime: float = None, endTime: float = None, limit: float = None, offset: float = None, sortBy: str = None, order: str = None, siteHierarchy: str = None, siteHierarchyId: str = None, siteId: str = None, view: str = None, attribute: str = None, networkDeviceId: str = None, networkDeviceIpAddress: str = None, networkDeviceMacAddress: str = None, interfaceId: str = None, interfaceName: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if startTime is not None:
        final_kwargs['startTime'] = startTime
    if endTime is not None:
        final_kwargs['endTime'] = endTime
    if limit is not None:
        final_kwargs['limit'] = limit
    if offset is not None:
        final_kwargs['offset'] = offset
    if sortBy is not None:
        final_kwargs['sortBy'] = sortBy
    if order is not None:
        final_kwargs['order'] = order
    if siteHierarchy is not None:
        final_kwargs['siteHierarchy'] = siteHierarchy
    if siteHierarchyId is not None:
        final_kwargs['siteHierarchyId'] = siteHierarchyId
    if siteId is not None:
        final_kwargs['siteId'] = siteId
    if view is not None:
        final_kwargs['view'] = view
    if attribute is not None:
        final_kwargs['attribute'] = attribute
    if networkDeviceId is not None:
        final_kwargs['networkDeviceId'] = networkDeviceId
    if networkDeviceIpAddress is not None:
        final_kwargs['networkDeviceIpAddress'] = networkDeviceIpAddress
    if networkDeviceMacAddress is not None:
        final_kwargs['networkDeviceMacAddress'] = networkDeviceMacAddress
    if interfaceId is not None:
        final_kwargs['interfaceId'] = interfaceId
    if interfaceName is not None:
        final_kwargs['interfaceName'] = interfaceName

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getsInterfacesAlongWithStatisticsDataFromAllNetworkDevices_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('retrieveLicenseSetting')
def retrieveLicenseSetting():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.retrieveLicenseSetting

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getTheTotalCustomIssueDefinitionsCountBasedOnTheProvidedFilters.')
def getTheTotalCustomIssueDefinitionsCountBasedOnTheProvidedFilters_(X_CALLER_ID: str = None, id: str = None, profileId: str = None, name: str = None, priority: str = None, isEnabled: bool = None, severity: float = None, facility: str = None, mnemonic: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if X_CALLER_ID is not None:
        final_kwargs['X-CALLER-ID'] = X_CALLER_ID
    if id is not None:
        final_kwargs['id'] = id
    if profileId is not None:
        final_kwargs['profileId'] = profileId
    if name is not None:
        final_kwargs['name'] = name
    if priority is not None:
        final_kwargs['priority'] = priority
    if isEnabled is not None:
        final_kwargs['isEnabled'] = isEnabled
    if severity is not None:
        final_kwargs['severity'] = severity
    if facility is not None:
        final_kwargs['facility'] = facility
    if mnemonic is not None:
        final_kwargs['mnemonic'] = mnemonic

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getTheTotalCustomIssueDefinitionsCountBasedOnTheProvidedFilters_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('get802.11beProfilesCount')
def get802_11beProfilesCount():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.get802_11beProfilesCount

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getMulticast')
def getMulticast(fabricId: str = None, offset: float = None, limit: float = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if fabricId is not None:
        final_kwargs['fabricId'] = fabricId
    if offset is not None:
        final_kwargs['offset'] = offset
    if limit is not None:
        final_kwargs['limit'] = limit

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getMulticast

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getFabricDevicesCount')
def getFabricDevicesCount(fabricId: str, networkDeviceId: str = None, deviceRoles: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if fabricId is not None:
        final_kwargs['fabricId'] = fabricId
    if networkDeviceId is not None:
        final_kwargs['networkDeviceId'] = networkDeviceId
    if deviceRoles is not None:
        final_kwargs['deviceRoles'] = deviceRoles

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getFabricDevicesCount

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('downloadFlexibleReport')
def downloadFlexibleReport(Content_Type: str, reportId: str, executionId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if Content_Type is not None:
        final_kwargs['Content-Type'] = Content_Type
    if reportId is not None:
        final_kwargs['reportId'] = reportId
    if executionId is not None:
        final_kwargs['executionId'] = executionId

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.downloadFlexibleReport

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getExternalAuthenticationServersAPI')
def getExternalAuthenticationServersAPI(invokeSource: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if invokeSource is not None:
        final_kwargs['invokeSource'] = invokeSource

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getExternalAuthenticationServersAPI

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getLayer3VirtualNetworksCount')
def getLayer3VirtualNetworksCount(fabricId: str = None, anchoredSiteId: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if fabricId is not None:
        final_kwargs['fabricId'] = fabricId
    if anchoredSiteId is not None:
        final_kwargs['anchoredSiteId'] = anchoredSiteId

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getLayer3VirtualNetworksCount

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('lANAutomationStatus')
def lANAutomationStatus(offset: float = None, limit: float = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if offset is not None:
        final_kwargs['offset'] = offset
    if limit is not None:
        final_kwargs['limit'] = limit

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.lANAutomationStatus

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDevicesDiscoveredById')
def getDevicesDiscoveredById(id: str, taskId: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if id is not None:
        final_kwargs['id'] = id
    if taskId is not None:
        final_kwargs['taskId'] = taskId

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getDevicesDiscoveredById

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getTaskById')
def getTaskById(taskId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if taskId is not None:
        final_kwargs['taskId'] = taskId

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getTaskById

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getPermissionsAPI')
def getPermissionsAPI():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getPermissionsAPI

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDiscoveredDevicesByRange')
def getDiscoveredDevicesByRange(id: str, startIndex: int, recordsToReturn: int, taskId: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if id is not None:
        final_kwargs['id'] = id
    if startIndex is not None:
        final_kwargs['startIndex'] = startIndex
    if recordsToReturn is not None:
        final_kwargs['recordsToReturn'] = recordsToReturn
    if taskId is not None:
        final_kwargs['taskId'] = taskId

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getDiscoveredDevicesByRange

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('retrievesTheTotalCountOfClientsByApplyingBasicFiltering')
def retrievesTheTotalCountOfClientsByApplyingBasicFiltering(X_CALLER_ID: str = None, startTime: float = None, endTime: float = None, type: str = None, osType: str = None, osVersion: str = None, siteHierarchy: str = None, siteHierarchyId: str = None, siteId: str = None, ipv4Address: str = None, ipv6Address: str = None, macAddress: str = None, wlcName: str = None, connectedNetworkDeviceName: str = None, ssid: str = None, band: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if X_CALLER_ID is not None:
        final_kwargs['X-CALLER-ID'] = X_CALLER_ID
    if startTime is not None:
        final_kwargs['startTime'] = startTime
    if endTime is not None:
        final_kwargs['endTime'] = endTime
    if type is not None:
        final_kwargs['type'] = type
    if osType is not None:
        final_kwargs['osType'] = osType
    if osVersion is not None:
        final_kwargs['osVersion'] = osVersion
    if siteHierarchy is not None:
        final_kwargs['siteHierarchy'] = siteHierarchy
    if siteHierarchyId is not None:
        final_kwargs['siteHierarchyId'] = siteHierarchyId
    if siteId is not None:
        final_kwargs['siteId'] = siteId
    if ipv4Address is not None:
        final_kwargs['ipv4Address'] = ipv4Address
    if ipv6Address is not None:
        final_kwargs['ipv6Address'] = ipv6Address
    if macAddress is not None:
        final_kwargs['macAddress'] = macAddress
    if wlcName is not None:
        final_kwargs['wlcName'] = wlcName
    if connectedNetworkDeviceName is not None:
        final_kwargs['connectedNetworkDeviceName'] = connectedNetworkDeviceName
    if ssid is not None:
        final_kwargs['ssid'] = ssid
    if band is not None:
        final_kwargs['band'] = band

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.retrievesTheTotalCountOfClientsByApplyingBasicFiltering

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('pOEDetails')
def pOEDetails(deviceUuid: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if deviceUuid is not None:
        final_kwargs['deviceUuid'] = deviceUuid

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.pOEDetails

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('retrievesTheListOfNetworkDeviceProductNames')
def retrievesTheListOfNetworkDeviceProductNames(productName: str = None, productId: str = None, offset: float = None, limit: float = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if productName is not None:
        final_kwargs['productName'] = productName
    if productId is not None:
        final_kwargs['productId'] = productId
    if offset is not None:
        final_kwargs['offset'] = offset
    if limit is not None:
        final_kwargs['limit'] = limit

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.retrievesTheListOfNetworkDeviceProductNames

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getAnchorManagedAPLocationsForSpecificWirelessController')
def getAnchorManagedAPLocationsForSpecificWirelessController(networkDeviceId: str, limit: float = None, offset: float = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkDeviceId is not None:
        final_kwargs['networkDeviceId'] = networkDeviceId
    if limit is not None:
        final_kwargs['limit'] = limit
    if offset is not None:
        final_kwargs['offset'] = offset

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getAnchorManagedAPLocationsForSpecificWirelessController

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getConnectedDeviceDetail')
def getConnectedDeviceDetail(deviceUuid: str, interfaceUuid: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if deviceUuid is not None:
        final_kwargs['deviceUuid'] = deviceUuid
    if interfaceUuid is not None:
        final_kwargs['interfaceUuid'] = interfaceUuid

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getConnectedDeviceDetail

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDevicesThatAreAssignedToASite')
def getDevicesThatAreAssignedToASite(id: str, memberType: str, offset: str = None, limit: str = None, level: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if id is not None:
        final_kwargs['id'] = id
    if offset is not None:
        final_kwargs['offset'] = offset
    if limit is not None:
        final_kwargs['limit'] = limit
    if memberType is not None:
        final_kwargs['memberType'] = memberType
    if level is not None:
        final_kwargs['level'] = level

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getDevicesThatAreAssignedToASite

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('lANAutomationLog')
def lANAutomationLog(offset: float = None, limit: float = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if offset is not None:
        final_kwargs['offset'] = offset
    if limit is not None:
        final_kwargs['limit'] = limit

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.lANAutomationLog

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('retrievesTheListOfNetworkProfilesThatTheGivenSiteHasBeenAssigned')
def retrievesTheListOfNetworkProfilesThatTheGivenSiteHasBeenAssigned(siteId: str, offset: float = None, limit: float = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if siteId is not None:
        final_kwargs['siteId'] = siteId
    if offset is not None:
        final_kwargs['offset'] = offset
    if limit is not None:
        final_kwargs['limit'] = limit

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.retrievesTheListOfNetworkProfilesThatTheGivenSiteHasBeenAssigned

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDiscoveryJobsByIP')
def getDiscoveryJobsByIP(ipAddress: str, offset: int = None, limit: int = None, name: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if offset is not None:
        final_kwargs['offset'] = offset
    if limit is not None:
        final_kwargs['limit'] = limit
    if ipAddress is not None:
        final_kwargs['ipAddress'] = ipAddress
    if name is not None:
        final_kwargs['name'] = name

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getDiscoveryJobsByIP

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getTemplate_s_Details')
def getTemplate_s_Details(id: str = None, name: str = None, projectId: str = None, projectName: str = None, softwareType: str = None, softwareVersion: str = None, productFamily: str = None, productSeries: str = None, productType: str = None, filterConflictingTemplates: bool = None, tags: list = None, unCommitted: bool = None, sortOrder: str = None, allTemplateAttributes: bool = None, includeVersionDetails: bool = None, offset: int = None, limit: int = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if id is not None:
        final_kwargs['id'] = id
    if name is not None:
        final_kwargs['name'] = name
    if projectId is not None:
        final_kwargs['projectId'] = projectId
    if projectName is not None:
        final_kwargs['projectName'] = projectName
    if softwareType is not None:
        final_kwargs['softwareType'] = softwareType
    if softwareVersion is not None:
        final_kwargs['softwareVersion'] = softwareVersion
    if productFamily is not None:
        final_kwargs['productFamily'] = productFamily
    if productSeries is not None:
        final_kwargs['productSeries'] = productSeries
    if productType is not None:
        final_kwargs['productType'] = productType
    if filterConflictingTemplates is not None:
        final_kwargs['filterConflictingTemplates'] = filterConflictingTemplates
    if tags is not None:
        final_kwargs['tags'] = tags
    if unCommitted is not None:
        final_kwargs['unCommitted'] = unCommitted
    if sortOrder is not None:
        final_kwargs['sortOrder'] = sortOrder
    if allTemplateAttributes is not None:
        final_kwargs['allTemplateAttributes'] = allTemplateAttributes
    if includeVersionDetails is not None:
        final_kwargs['includeVersionDetails'] = includeVersionDetails
    if offset is not None:
        final_kwargs['offset'] = offset
    if limit is not None:
        final_kwargs['limit'] = limit

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getTemplate_s_Details

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('s_Details')(globals()['getTemplate_s_Details'])

# alias → easier for LLM
register('s_Detail')(globals()['getTemplate_s_Details'])

@register('lANAutomationLogsForIndividualDevices')
def lANAutomationLogsForIndividualDevices(id: str, serialNumber: str, logLevel: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if id is not None:
        final_kwargs['id'] = id
    if serialNumber is not None:
        final_kwargs['serialNumber'] = serialNumber
    if logLevel is not None:
        final_kwargs['logLevel'] = logLevel

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.lANAutomationLogsForIndividualDevices

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getListOfDiscoveriesByDiscoveryId')
def getListOfDiscoveriesByDiscoveryId(id: str, offset: int = None, limit: int = None, ipAddress: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if id is not None:
        final_kwargs['id'] = id
    if offset is not None:
        final_kwargs['offset'] = offset
    if limit is not None:
        final_kwargs['limit'] = limit
    if ipAddress is not None:
        final_kwargs['ipAddress'] = ipAddress

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getListOfDiscoveriesByDiscoveryId

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getPhysicalTopology')
def getPhysicalTopology(nodeType: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if nodeType is not None:
        final_kwargs['nodeType'] = nodeType

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getPhysicalTopology

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getSiteTopology')
def getSiteTopology():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getSiteTopology

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getITSMIntegrationStatus')
def getITSMIntegrationStatus():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getITSMIntegrationStatus

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getSecondaryManagedAPLocationsForSpecificWirelessController')
def getSecondaryManagedAPLocationsForSpecificWirelessController(networkDeviceId: str, limit: float = None, offset: float = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkDeviceId is not None:
        final_kwargs['networkDeviceId'] = networkDeviceId
    if limit is not None:
        final_kwargs['limit'] = limit
    if offset is not None:
        final_kwargs['offset'] = offset

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getSecondaryManagedAPLocationsForSpecificWirelessController

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('retrieveNTPSettingsForASite')
def retrieveNTPSettingsForASite(id: str, _inherited: bool = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if id is not None:
        final_kwargs['id'] = id
    if _inherited is not None:
        final_kwargs['_inherited'] = _inherited

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.retrieveNTPSettingsForASite

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('retrieveTagsAssociatedWithTheInterfaces.')
def retrieveTagsAssociatedWithTheInterfaces_(offset: float = None, limit: float = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if offset is not None:
        final_kwargs['offset'] = offset
    if limit is not None:
        final_kwargs['limit'] = limit

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.retrieveTagsAssociatedWithTheInterfaces_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('countOfNetworkDeviceImageUpdates')
def countOfNetworkDeviceImageUpdates(id: str = None, parentId: str = None, networkDeviceId: str = None, status: str = None, imageName: str = None, hostName: str = None, managementAddress: str = None, startTime: float = None, endTime: float = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if id is not None:
        final_kwargs['id'] = id
    if parentId is not None:
        final_kwargs['parentId'] = parentId
    if networkDeviceId is not None:
        final_kwargs['networkDeviceId'] = networkDeviceId
    if status is not None:
        final_kwargs['status'] = status
    if imageName is not None:
        final_kwargs['imageName'] = imageName
    if hostName is not None:
        final_kwargs['hostName'] = hostName
    if managementAddress is not None:
        final_kwargs['managementAddress'] = managementAddress
    if startTime is not None:
        final_kwargs['startTime'] = startTime
    if endTime is not None:
        final_kwargs['endTime'] = endTime

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.countOfNetworkDeviceImageUpdates

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('returnReplacementDevicesCount')
def returnReplacementDevicesCount(replacementStatus: list = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if replacementStatus is not None:
        final_kwargs['replacementStatus'] = replacementStatus

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.returnReplacementDevicesCount

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getPlannedAccessPointsForBuilding')
def getPlannedAccessPointsForBuilding(buildingId: str, limit: float = None, offset: float = None, radios: bool = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if buildingId is not None:
        final_kwargs['buildingId'] = buildingId
    if limit is not None:
        final_kwargs['limit'] = limit
    if offset is not None:
        final_kwargs['offset'] = offset
    if radios is not None:
        final_kwargs['radios'] = radios

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getPlannedAccessPointsForBuilding

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getTheCountOfSystemDefinedIssueDefinitionsBasedOnProvidedFilters')
def getTheCountOfSystemDefinedIssueDefinitionsBasedOnProvidedFilters(X_CALLER_ID: str = None, deviceType: str = None, profileId: str = None, id: str = None, name: str = None, priority: str = None, issueEnabled: bool = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if X_CALLER_ID is not None:
        final_kwargs['X-CALLER-ID'] = X_CALLER_ID
    if deviceType is not None:
        final_kwargs['deviceType'] = deviceType
    if profileId is not None:
        final_kwargs['profileId'] = profileId
    if id is not None:
        final_kwargs['id'] = id
    if name is not None:
        final_kwargs['name'] = name
    if priority is not None:
        final_kwargs['priority'] = priority
    if issueEnabled is not None:
        final_kwargs['issueEnabled'] = issueEnabled

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getTheCountOfSystemDefinedIssueDefinitionsBasedOnProvidedFilters

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('countOfNetworkProductNames')
def countOfNetworkProductNames(productName: str = None, productId: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if productName is not None:
        final_kwargs['productName'] = productName
    if productId is not None:
        final_kwargs['productId'] = productId

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.countOfNetworkProductNames

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getAccessPointConfiguration')
def getAccessPointConfiguration(key: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if key is not None:
        final_kwargs['key'] = key

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getAccessPointConfiguration

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceConfigForAllDevices')
def getDeviceConfigForAllDevices():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getDeviceConfigForAllDevices

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getTopologyDetails')
def getTopologyDetails(vlanID: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if vlanID is not None:
        final_kwargs['vlanID'] = vlanID

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getTopologyDetails

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getTheDetailsOfIssuesForGivenSetOfFilters-2')
def getTheDetailsOfIssuesForGivenSetOfFilters_2(Accept_Language: str = None, X_CALLER_ID: str = None, startTime: float = None, endTime: float = None, limit: float = None, offset: float = None, sortBy: str = None, order: str = None, isGlobal: bool = None, priority: str = None, severity: str = None, status: str = None, entityType: str = None, category: str = None, deviceType: str = None, name: str = None, issueId: str = None, entityId: str = None, updatedBy: str = None, siteHierarchy: str = None, siteHierarchyId: str = None, siteName: str = None, siteId: str = None, fabricSiteId: str = None, fabricVnName: str = None, fabricTransitSiteId: str = None, networkDeviceId: str = None, networkDeviceIpAddress: str = None, macAddress: str = None, view: str = None, attribute: str = None, aiDriven: bool = None, fabricDriven: bool = None, fabricSiteDriven: bool = None, fabricVnDriven: bool = None, fabricTransitDriven: bool = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if Accept_Language is not None:
        final_kwargs['Accept-Language'] = Accept_Language
    if X_CALLER_ID is not None:
        final_kwargs['X-CALLER-ID'] = X_CALLER_ID
    if startTime is not None:
        final_kwargs['startTime'] = startTime
    if endTime is not None:
        final_kwargs['endTime'] = endTime
    if limit is not None:
        final_kwargs['limit'] = limit
    if offset is not None:
        final_kwargs['offset'] = offset
    if sortBy is not None:
        final_kwargs['sortBy'] = sortBy
    if order is not None:
        final_kwargs['order'] = order
    if isGlobal is not None:
        final_kwargs['isGlobal'] = isGlobal
    if priority is not None:
        final_kwargs['priority'] = priority
    if severity is not None:
        final_kwargs['severity'] = severity
    if status is not None:
        final_kwargs['status'] = status
    if entityType is not None:
        final_kwargs['entityType'] = entityType
    if category is not None:
        final_kwargs['category'] = category
    if deviceType is not None:
        final_kwargs['deviceType'] = deviceType
    if name is not None:
        final_kwargs['name'] = name
    if issueId is not None:
        final_kwargs['issueId'] = issueId
    if entityId is not None:
        final_kwargs['entityId'] = entityId
    if updatedBy is not None:
        final_kwargs['updatedBy'] = updatedBy
    if siteHierarchy is not None:
        final_kwargs['siteHierarchy'] = siteHierarchy
    if siteHierarchyId is not None:
        final_kwargs['siteHierarchyId'] = siteHierarchyId
    if siteName is not None:
        final_kwargs['siteName'] = siteName
    if siteId is not None:
        final_kwargs['siteId'] = siteId
    if fabricSiteId is not None:
        final_kwargs['fabricSiteId'] = fabricSiteId
    if fabricVnName is not None:
        final_kwargs['fabricVnName'] = fabricVnName
    if fabricTransitSiteId is not None:
        final_kwargs['fabricTransitSiteId'] = fabricTransitSiteId
    if networkDeviceId is not None:
        final_kwargs['networkDeviceId'] = networkDeviceId
    if networkDeviceIpAddress is not None:
        final_kwargs['networkDeviceIpAddress'] = networkDeviceIpAddress
    if macAddress is not None:
        final_kwargs['macAddress'] = macAddress
    if view is not None:
        final_kwargs['view'] = view
    if attribute is not None:
        final_kwargs['attribute'] = attribute
    if aiDriven is not None:
        final_kwargs['aiDriven'] = aiDriven
    if fabricDriven is not None:
        final_kwargs['fabricDriven'] = fabricDriven
    if fabricSiteDriven is not None:
        final_kwargs['fabricSiteDriven'] = fabricSiteDriven
    if fabricVnDriven is not None:
        final_kwargs['fabricVnDriven'] = fabricVnDriven
    if fabricTransitDriven is not None:
        final_kwargs['fabricTransitDriven'] = fabricTransitDriven

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getTheDetailsOfIssuesForGivenSetOfFilters_2

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('smartAccountDetails')
def smartAccountDetails():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.smartAccountDetails

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getFabricDevicesLayer3HandoffsWithIpTransitCount')
def getFabricDevicesLayer3HandoffsWithIpTransitCount(fabricId: str, networkDeviceId: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if fabricId is not None:
        final_kwargs['fabricId'] = fabricId
    if networkDeviceId is not None:
        final_kwargs['networkDeviceId'] = networkDeviceId

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getFabricDevicesLayer3HandoffsWithIpTransitCount

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getFabricDevicesLayer3HandoffsWithSdaTransitCount')
def getFabricDevicesLayer3HandoffsWithSdaTransitCount(fabricId: str, networkDeviceId: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if fabricId is not None:
        final_kwargs['fabricId'] = fabricId
    if networkDeviceId is not None:
        final_kwargs['networkDeviceId'] = networkDeviceId

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getFabricDevicesLayer3HandoffsWithSdaTransitCount

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('retrievesTheListOfNetworkProfilesForSites')
def retrievesTheListOfNetworkProfilesForSites(offset: float = None, limit: float = None, sortBy: str = None, order: str = None, type: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if offset is not None:
        final_kwargs['offset'] = offset
    if limit is not None:
        final_kwargs['limit'] = limit
    if sortBy is not None:
        final_kwargs['sortBy'] = sortBy
    if order is not None:
        final_kwargs['order'] = order
    if type is not None:
        final_kwargs['type'] = type

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.retrievesTheListOfNetworkProfilesForSites

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getFunctionalCapabilityForDevices')
def getFunctionalCapabilityForDevices(deviceId: str, functionName: list = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if deviceId is not None:
        final_kwargs['deviceId'] = deviceId
    if functionName is not None:
        final_kwargs['functionName'] = functionName

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getFunctionalCapabilityForDevices

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getPortAssignments')
def getPortAssignments(fabricId: str = None, networkDeviceId: str = None, interfaceName: str = None, dataVlanName: str = None, voiceVlanName: str = None, offset: float = None, limit: float = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if fabricId is not None:
        final_kwargs['fabricId'] = fabricId
    if networkDeviceId is not None:
        final_kwargs['networkDeviceId'] = networkDeviceId
    if interfaceName is not None:
        final_kwargs['interfaceName'] = interfaceName
    if dataVlanName is not None:
        final_kwargs['dataVlanName'] = dataVlanName
    if voiceVlanName is not None:
        final_kwargs['voiceVlanName'] = voiceVlanName
    if offset is not None:
        final_kwargs['offset'] = offset
    if limit is not None:
        final_kwargs['limit'] = limit

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getPortAssignments

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getBusinessAPIExecutionDetails')
def getBusinessAPIExecutionDetails(executionId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if executionId is not None:
        final_kwargs['executionId'] = executionId

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getBusinessAPIExecutionDetails

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('lANAutomationActiveSessions')
def lANAutomationActiveSessions():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.lANAutomationActiveSessions

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getSiteNotAssignedNetworkDevices')
def getSiteNotAssignedNetworkDevices(offset: float = None, limit: float = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if offset is not None:
        final_kwargs['offset'] = offset
    if limit is not None:
        final_kwargs['limit'] = limit

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getSiteNotAssignedNetworkDevices

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getAccessPointRebootTaskResult')
def getAccessPointRebootTaskResult(parentTaskId: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if parentTaskId is not None:
        final_kwargs['parentTaskId'] = parentTaskId

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getAccessPointRebootTaskResult

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceDetail')
def getDeviceDetail(identifier: str, searchBy: str, timestamp: float = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if timestamp is not None:
        final_kwargs['timestamp'] = timestamp
    if identifier is not None:
        final_kwargs['identifier'] = identifier
    if searchBy is not None:
        final_kwargs['searchBy'] = searchBy

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getDeviceDetail

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('lANAutomationSessionCount')
def lANAutomationSessionCount():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.lANAutomationSessionCount

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkDeviceByIP')
def getNetworkDeviceByIP(ipAddress: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if ipAddress is not None:
        final_kwargs['ipAddress'] = ipAddress

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkDeviceByIP

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getSiteNotAssignedNetworkDevicesCount')
def getSiteNotAssignedNetworkDevicesCount():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getSiteNotAssignedNetworkDevicesCount

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceBySerialNumber')
def getDeviceBySerialNumber(serialNumber: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if serialNumber is not None:
        final_kwargs['serialNumber'] = serialNumber

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getDeviceBySerialNumber

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getApplicationCount')
def getApplicationCount(scalableGroupType: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if scalableGroupType is not None:
        final_kwargs['scalableGroupType'] = scalableGroupType

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getApplicationCount

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('downloadReportContent')
def downloadReportContent(reportId: str, executionId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if reportId is not None:
        final_kwargs['reportId'] = reportId
    if executionId is not None:
        final_kwargs['executionId'] = executionId

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.downloadReportContent

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceCount-2')
def getDeviceCount_2(serialNumber: list = None, state: list = None, onbState: list = None, name: list = None, pid: list = None, source: list = None, workflowId: list = None, workflowName: list = None, smartAccountId: list = None, virtualAccountId: list = None, lastContact: bool = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if serialNumber is not None:
        final_kwargs['serialNumber'] = serialNumber
    if state is not None:
        final_kwargs['state'] = state
    if onbState is not None:
        final_kwargs['onbState'] = onbState
    if name is not None:
        final_kwargs['name'] = name
    if pid is not None:
        final_kwargs['pid'] = pid
    if source is not None:
        final_kwargs['source'] = source
    if workflowId is not None:
        final_kwargs['workflowId'] = workflowId
    if workflowName is not None:
        final_kwargs['workflowName'] = workflowName
    if smartAccountId is not None:
        final_kwargs['smartAccountId'] = smartAccountId
    if virtualAccountId is not None:
        final_kwargs['virtualAccountId'] = virtualAccountId
    if lastContact is not None:
        final_kwargs['lastContact'] = lastContact

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getDeviceCount_2

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('eventArtifactCount')
def eventArtifactCount():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.eventArtifactCount

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getComplianceStatusCount')
def getComplianceStatusCount(complianceStatus: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if complianceStatus is not None:
        final_kwargs['complianceStatus'] = complianceStatus

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getComplianceStatusCount

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getTasks')
def getTasks(offset: int = None, limit: int = None, sortBy: str = None, order: str = None, startTime: int = None, endTime: int = None, parentId: str = None, rootId: str = None, status: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if offset is not None:
        final_kwargs['offset'] = offset
    if limit is not None:
        final_kwargs['limit'] = limit
    if sortBy is not None:
        final_kwargs['sortBy'] = sortBy
    if order is not None:
        final_kwargs['order'] = order
    if startTime is not None:
        final_kwargs['startTime'] = startTime
    if endTime is not None:
        final_kwargs['endTime'] = endTime
    if parentId is not None:
        final_kwargs['parentId'] = parentId
    if rootId is not None:
        final_kwargs['rootId'] = rootId
    if status is not None:
        final_kwargs['status'] = status

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getTasks

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getListOfChildEventsForTheGivenWirelessClientEvent')
def getListOfChildEventsForTheGivenWirelessClientEvent(id: str, X_CALLER_ID: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if X_CALLER_ID is not None:
        final_kwargs['X-CALLER-ID'] = X_CALLER_ID
    if id is not None:
        final_kwargs['id'] = id

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getListOfChildEventsForTheGivenWirelessClientEvent

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getProvisioningSettings')
def getProvisioningSettings():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getProvisioningSettings

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('readSiteCount.')
def readSiteCount_(X_CALLER_ID: str = None, endTime: float = None, siteHierarchy: str = None, siteHierarchyId: str = None, siteType: str = None, id: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if X_CALLER_ID is not None:
        final_kwargs['X-CALLER-ID'] = X_CALLER_ID
    if endTime is not None:
        final_kwargs['endTime'] = endTime
    if siteHierarchy is not None:
        final_kwargs['siteHierarchy'] = siteHierarchy
    if siteHierarchyId is not None:
        final_kwargs['siteHierarchyId'] = siteHierarchyId
    if siteType is not None:
        final_kwargs['siteType'] = siteType
    if id is not None:
        final_kwargs['id'] = id

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.readSiteCount_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getEoXDetailsPerDevice')
def getEoXDetailsPerDevice(deviceId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if deviceId is not None:
        final_kwargs['deviceId'] = deviceId

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getEoXDetailsPerDevice

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('ciscoDNACenterNodesConfigurationSummary')
def ciscoDNACenterNodesConfigurationSummary():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.ciscoDNACenterNodesConfigurationSummary

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('importMapArchive-ImportStatus')
def importMapArchive_ImportStatus(importContextUuid: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if importContextUuid is not None:
        final_kwargs['importContextUuid'] = importContextUuid

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.importMapArchive_ImportStatus

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getExternalAuthenticationSettingAPI')
def getExternalAuthenticationSettingAPI():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getExternalAuthenticationSettingAPI

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getInterfaceById')
def getInterfaceById(id: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if id is not None:
        final_kwargs['id'] = id

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getInterfaceById

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('deviceLicenseDetails')
def deviceLicenseDetails(device_uuid: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if device_uuid is not None:
        final_kwargs['device_uuid'] = device_uuid

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.deviceLicenseDetails

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getTheInterfaceDataForTheGivenInterfaceId_instanceUuid_AlongWith')
def getTheInterfaceDataForTheGivenInterfaceId_instanceUuid_AlongWith(id: str, startTime: float = None, endTime: float = None, view: str = None, attribute: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if id is not None:
        final_kwargs['id'] = id
    if startTime is not None:
        final_kwargs['startTime'] = startTime
    if endTime is not None:
        final_kwargs['endTime'] = endTime
    if view is not None:
        final_kwargs['view'] = view
    if attribute is not None:
        final_kwargs['attribute'] = attribute

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getTheInterfaceDataForTheGivenInterfaceId_instanceUuid_AlongWith

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('instanceUuid_AlongWith')(globals()['getTheInterfaceDataForTheGivenInterfaceId_instanceUuid_AlongWith'])

@register('instanceUuid_AlongWith')
def instanceUuid_AlongWith(id: str, startTime: float = None, endTime: float = None, view: str = None, attribute: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if id is not None:
        final_kwargs['id'] = id
    if startTime is not None:
        final_kwargs['startTime'] = startTime
    if endTime is not None:
        final_kwargs['endTime'] = endTime
    if view is not None:
        final_kwargs['view'] = view
    if attribute is not None:
        final_kwargs['attribute'] = attribute

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.instanceUuid_AlongWith

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('AlongWith')(globals()['instanceUuid_AlongWith'])

@register('getInterfaceInfoById')
def getInterfaceInfoById(deviceId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if deviceId is not None:
        final_kwargs['deviceId'] = deviceId

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getInterfaceInfoById

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getTaskByOperationId')
def getTaskByOperationId(operationId: str, offset: int, limit: int):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if operationId is not None:
        final_kwargs['operationId'] = operationId
    if offset is not None:
        final_kwargs['offset'] = offset
    if limit is not None:
        final_kwargs['limit'] = limit

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getTaskByOperationId

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('ciscoISEServerIntegrationStatus')
def ciscoISEServerIntegrationStatus():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.ciscoISEServerIntegrationStatus

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getL3TopologyDetails')
def getL3TopologyDetails(topologyType: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if topologyType is not None:
        final_kwargs['topologyType'] = topologyType

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getL3TopologyDetails

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getAdvisoryDeviceDetail')
def getAdvisoryDeviceDetail(deviceId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if deviceId is not None:
        final_kwargs['deviceId'] = deviceId

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getAdvisoryDeviceDetail

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getConnectorTypes')
def getConnectorTypes():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getConnectorTypes

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getTasksByID')
def getTasksByID(id: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if id is not None:
        final_kwargs['id'] = id

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getTasksByID

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('licenseTermDetails')
def licenseTermDetails(smart_account_id: str, virtual_account_name: str, device_type: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if smart_account_id is not None:
        final_kwargs['smart_account_id'] = smart_account_id
    if virtual_account_name is not None:
        final_kwargs['virtual_account_name'] = virtual_account_name
    if device_type is not None:
        final_kwargs['device_type'] = device_type

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.licenseTermDetails

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('retrieveDHCPSettingsForASite')
def retrieveDHCPSettingsForASite(id: str, _inherited: bool = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if id is not None:
        final_kwargs['id'] = id
    if _inherited is not None:
        final_kwargs['_inherited'] = _inherited

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.retrieveDHCPSettingsForASite

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getAnycastGatewayCount')
def getAnycastGatewayCount(fabricId: str = None, virtualNetworkName: str = None, ipPoolName: str = None, vlanName: str = None, vlanId: float = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if fabricId is not None:
        final_kwargs['fabricId'] = fabricId
    if virtualNetworkName is not None:
        final_kwargs['virtualNetworkName'] = virtualNetworkName
    if ipPoolName is not None:
        final_kwargs['ipPoolName'] = ipPoolName
    if vlanName is not None:
        final_kwargs['vlanName'] = vlanName
    if vlanId is not None:
        final_kwargs['vlanId'] = vlanId

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getAnycastGatewayCount

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getsTheNetworkDeviceDetailsBasedOnTheProvidedQueryParameters.')
def getsTheNetworkDeviceDetailsBasedOnTheProvidedQueryParameters_(startTime: float = None, endTime: float = None, limit: float = None, offset: float = None, sortBy: str = None, order: str = None, siteHierarchy: str = None, siteHierarchyId: str = None, siteId: str = None, id: str = None, managementIpAddress: str = None, macAddress: str = None, family: str = None, type: str = None, role: str = None, serialNumber: str = None, maintenanceMode: bool = None, softwareVersion: str = None, healthScore: str = None, view: str = None, attribute: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if startTime is not None:
        final_kwargs['startTime'] = startTime
    if endTime is not None:
        final_kwargs['endTime'] = endTime
    if limit is not None:
        final_kwargs['limit'] = limit
    if offset is not None:
        final_kwargs['offset'] = offset
    if sortBy is not None:
        final_kwargs['sortBy'] = sortBy
    if order is not None:
        final_kwargs['order'] = order
    if siteHierarchy is not None:
        final_kwargs['siteHierarchy'] = siteHierarchy
    if siteHierarchyId is not None:
        final_kwargs['siteHierarchyId'] = siteHierarchyId
    if siteId is not None:
        final_kwargs['siteId'] = siteId
    if id is not None:
        final_kwargs['id'] = id
    if managementIpAddress is not None:
        final_kwargs['managementIpAddress'] = managementIpAddress
    if macAddress is not None:
        final_kwargs['macAddress'] = macAddress
    if family is not None:
        final_kwargs['family'] = family
    if type is not None:
        final_kwargs['type'] = type
    if role is not None:
        final_kwargs['role'] = role
    if serialNumber is not None:
        final_kwargs['serialNumber'] = serialNumber
    if maintenanceMode is not None:
        final_kwargs['maintenanceMode'] = maintenanceMode
    if softwareVersion is not None:
        final_kwargs['softwareVersion'] = softwareVersion
    if healthScore is not None:
        final_kwargs['healthScore'] = healthScore
    if view is not None:
        final_kwargs['view'] = view
    if attribute is not None:
        final_kwargs['attribute'] = attribute

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getsTheNetworkDeviceDetailsBasedOnTheProvidedQueryParameters_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('issues')
def issues(startTime: float = None, endTime: float = None, siteId: str = None, deviceId: str = None, macAddress: str = None, priority: str = None, issueStatus: str = None, aiDriven: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if startTime is not None:
        final_kwargs['startTime'] = startTime
    if endTime is not None:
        final_kwargs['endTime'] = endTime
    if siteId is not None:
        final_kwargs['siteId'] = siteId
    if deviceId is not None:
        final_kwargs['deviceId'] = deviceId
    if macAddress is not None:
        final_kwargs['macAddress'] = macAddress
    if priority is not None:
        final_kwargs['priority'] = priority
    if issueStatus is not None:
        final_kwargs['issueStatus'] = issueStatus
    if aiDriven is not None:
        final_kwargs['aiDriven'] = aiDriven

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.issues

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDevicesRegisteredForWSANotification')
def getDevicesRegisteredForWSANotification(serialNumber: str = None, macaddress: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if serialNumber is not None:
        final_kwargs['serialNumber'] = serialNumber
    if macaddress is not None:
        final_kwargs['macaddress'] = macaddress

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getDevicesRegisteredForWSANotification

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getInterfaceByIP')
def getInterfaceByIP(ipAddress: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if ipAddress is not None:
        final_kwargs['ipAddress'] = ipAddress

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getInterfaceByIP

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('retrieveApplicableAdd-onImagesForTheGivenSoftwareImage')
def retrieveApplicableAdd_onImagesForTheGivenSoftwareImage(id: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if id is not None:
        final_kwargs['id'] = id

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.retrieveApplicableAdd_onImagesForTheGivenSoftwareImage

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('retrievesTheListOfClients_WhileAlsoOfferingBasicFilteringAndSort')
def retrievesTheListOfClients_WhileAlsoOfferingBasicFilteringAndSort(X_CALLER_ID: str = None, startTime: float = None, endTime: float = None, limit: float = None, offset: float = None, sortBy: str = None, order: str = None, type: str = None, osType: str = None, osVersion: str = None, siteHierarchy: str = None, siteHierarchyId: str = None, siteId: str = None, ipv4Address: str = None, ipv6Address: str = None, macAddress: str = None, wlcName: str = None, connectedNetworkDeviceName: str = None, ssid: str = None, band: str = None, view: str = None, attribute: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if X_CALLER_ID is not None:
        final_kwargs['X-CALLER-ID'] = X_CALLER_ID
    if startTime is not None:
        final_kwargs['startTime'] = startTime
    if endTime is not None:
        final_kwargs['endTime'] = endTime
    if limit is not None:
        final_kwargs['limit'] = limit
    if offset is not None:
        final_kwargs['offset'] = offset
    if sortBy is not None:
        final_kwargs['sortBy'] = sortBy
    if order is not None:
        final_kwargs['order'] = order
    if type is not None:
        final_kwargs['type'] = type
    if osType is not None:
        final_kwargs['osType'] = osType
    if osVersion is not None:
        final_kwargs['osVersion'] = osVersion
    if siteHierarchy is not None:
        final_kwargs['siteHierarchy'] = siteHierarchy
    if siteHierarchyId is not None:
        final_kwargs['siteHierarchyId'] = siteHierarchyId
    if siteId is not None:
        final_kwargs['siteId'] = siteId
    if ipv4Address is not None:
        final_kwargs['ipv4Address'] = ipv4Address
    if ipv6Address is not None:
        final_kwargs['ipv6Address'] = ipv6Address
    if macAddress is not None:
        final_kwargs['macAddress'] = macAddress
    if wlcName is not None:
        final_kwargs['wlcName'] = wlcName
    if connectedNetworkDeviceName is not None:
        final_kwargs['connectedNetworkDeviceName'] = connectedNetworkDeviceName
    if ssid is not None:
        final_kwargs['ssid'] = ssid
    if band is not None:
        final_kwargs['band'] = band
    if view is not None:
        final_kwargs['view'] = view
    if attribute is not None:
        final_kwargs['attribute'] = attribute

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.retrievesTheListOfClients_WhileAlsoOfferingBasicFilteringAndSort

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('WhileAlsoOfferingBasicFilteringAndSort')(globals()['retrievesTheListOfClients_WhileAlsoOfferingBasicFilteringAndSort'])

@register('WhileAlsoOfferingBasicFilteringAndSort')
def WhileAlsoOfferingBasicFilteringAndSort(X_CALLER_ID: str = None, startTime: float = None, endTime: float = None, limit: float = None, offset: float = None, sortBy: str = None, order: str = None, type: str = None, osType: str = None, osVersion: str = None, siteHierarchy: str = None, siteHierarchyId: str = None, siteId: str = None, ipv4Address: str = None, ipv6Address: str = None, macAddress: str = None, wlcName: str = None, connectedNetworkDeviceName: str = None, ssid: str = None, band: str = None, view: str = None, attribute: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if X_CALLER_ID is not None:
        final_kwargs['X-CALLER-ID'] = X_CALLER_ID
    if startTime is not None:
        final_kwargs['startTime'] = startTime
    if endTime is not None:
        final_kwargs['endTime'] = endTime
    if limit is not None:
        final_kwargs['limit'] = limit
    if offset is not None:
        final_kwargs['offset'] = offset
    if sortBy is not None:
        final_kwargs['sortBy'] = sortBy
    if order is not None:
        final_kwargs['order'] = order
    if type is not None:
        final_kwargs['type'] = type
    if osType is not None:
        final_kwargs['osType'] = osType
    if osVersion is not None:
        final_kwargs['osVersion'] = osVersion
    if siteHierarchy is not None:
        final_kwargs['siteHierarchy'] = siteHierarchy
    if siteHierarchyId is not None:
        final_kwargs['siteHierarchyId'] = siteHierarchyId
    if siteId is not None:
        final_kwargs['siteId'] = siteId
    if ipv4Address is not None:
        final_kwargs['ipv4Address'] = ipv4Address
    if ipv6Address is not None:
        final_kwargs['ipv6Address'] = ipv6Address
    if macAddress is not None:
        final_kwargs['macAddress'] = macAddress
    if wlcName is not None:
        final_kwargs['wlcName'] = wlcName
    if connectedNetworkDeviceName is not None:
        final_kwargs['connectedNetworkDeviceName'] = connectedNetworkDeviceName
    if ssid is not None:
        final_kwargs['ssid'] = ssid
    if band is not None:
        final_kwargs['band'] = band
    if view is not None:
        final_kwargs['view'] = view
    if attribute is not None:
        final_kwargs['attribute'] = attribute

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.WhileAlsoOfferingBasicFilteringAndSort

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getEoXSummary')
def getEoXSummary():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getEoXSummary

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('systemPerformanceAPI')
def systemPerformanceAPI(kpi: str = None, function: str = None, startTime: float = None, endTime: float = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if kpi is not None:
        final_kwargs['kpi'] = kpi
    if function is not None:
        final_kwargs['function'] = function
    if startTime is not None:
        final_kwargs['startTime'] = startTime
    if endTime is not None:
        final_kwargs['endTime'] = endTime

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.systemPerformanceAPI

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getManagedAPLocationsCountForSpecificWirelessController')
def getManagedAPLocationsCountForSpecificWirelessController(networkDeviceId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if networkDeviceId is not None:
        final_kwargs['networkDeviceId'] = networkDeviceId

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getManagedAPLocationsCountForSpecificWirelessController

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkDeviceByPaginationRange')
def getNetworkDeviceByPaginationRange(startIndex: int, recordsToReturn: int):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if startIndex is not None:
        final_kwargs['startIndex'] = startIndex
    if recordsToReturn is not None:
        final_kwargs['recordsToReturn'] = recordsToReturn

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkDeviceByPaginationRange

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getSiteAssignedNetworkDevice')
def getSiteAssignedNetworkDevice(id: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if id is not None:
        final_kwargs['id'] = id

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getSiteAssignedNetworkDevice

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getTheCustomIssueDefinitionForTheGivenCustomIssueDefinitionId.')
def getTheCustomIssueDefinitionForTheGivenCustomIssueDefinitionId_(id: str, X_CALLER_ID: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if X_CALLER_ID is not None:
        final_kwargs['X-CALLER-ID'] = X_CALLER_ID
    if id is not None:
        final_kwargs['id'] = id

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getTheCustomIssueDefinitionForTheGivenCustomIssueDefinitionId_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getAllInterfaces')
def getAllInterfaces(offset: int = None, limit: int = None, lastInputTime: str = None, lastOutputTime: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if offset is not None:
        final_kwargs['offset'] = offset
    if limit is not None:
        final_kwargs['limit'] = limit
    if lastInputTime is not None:
        final_kwargs['lastInputTime'] = lastInputTime
    if lastOutputTime is not None:
        final_kwargs['lastOutputTime'] = lastOutputTime

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getAllInterfaces

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias for getAllInterfaces -> list_interfaces
register('list_interfaces')(globals()['getAllInterfaces'])

# alias for getAllInterfaces -> interfaces
register('interfaces')(globals()['getAllInterfaces'])

# alias for getAllInterfaces -> get_interfaces
register('get_interfaces')(globals()['getAllInterfaces'])

# alias for getAllInterfaces -> show_interfaces
register('show_interfaces')(globals()['getAllInterfaces'])

@register('returnsCountOfAdd-onImages')
def returnsCountOfAdd_onImages(id: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if id is not None:
        final_kwargs['id'] = id

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.returnsCountOfAdd_onImages

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getWirelessLanControllerDetailsById')
def getWirelessLanControllerDetailsById(id: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if id is not None:
        final_kwargs['id'] = id

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getWirelessLanControllerDetailsById

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('ciscoDNACenterPackagesSummary')
def ciscoDNACenterPackagesSummary():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.ciscoDNACenterPackagesSummary

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getRFProfilesCount')
def getRFProfilesCount():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getRFProfilesCount

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDevicesPerAdvisory')
def getDevicesPerAdvisory(advisoryId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if advisoryId is not None:
        final_kwargs['advisoryId'] = advisoryId

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getDevicesPerAdvisory

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getAccessPointConfigurationTaskResult')
def getAccessPointConfigurationTaskResult(task_id: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if task_id is not None:
        final_kwargs['task_id'] = task_id

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getAccessPointConfigurationTaskResult

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getComplianceDetail')
def getComplianceDetail(complianceType: str = None, complianceStatus: str = None, deviceUuid: str = None, offset: float = None, limit: float = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if complianceType is not None:
        final_kwargs['complianceType'] = complianceType
    if complianceStatus is not None:
        final_kwargs['complianceStatus'] = complianceStatus
    if deviceUuid is not None:
        final_kwargs['deviceUuid'] = deviceUuid
    if offset is not None:
        final_kwargs['offset'] = offset
    if limit is not None:
        final_kwargs['limit'] = limit

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getComplianceDetail

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('returnsTheCountOfVLANsMappedToSSIDsInAFabricSite.')
def returnsTheCountOfVLANsMappedToSSIDsInAFabricSite_(Content_Type: str, fabricId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if Content_Type is not None:
        final_kwargs['Content-Type'] = Content_Type
    if fabricId is not None:
        final_kwargs['fabricId'] = fabricId

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.returnsTheCountOfVLANsMappedToSSIDsInAFabricSite_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getGlobalCredentials')
def getGlobalCredentials(credentialSubType: str, sortBy: str = None, order: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if credentialSubType is not None:
        final_kwargs['credentialSubType'] = credentialSubType
    if sortBy is not None:
        final_kwargs['sortBy'] = sortBy
    if order is not None:
        final_kwargs['order'] = order

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getGlobalCredentials

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getComplianceStatus')
def getComplianceStatus(complianceStatus: str = None, deviceUuid: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if complianceStatus is not None:
        final_kwargs['complianceStatus'] = complianceStatus
    if deviceUuid is not None:
        final_kwargs['deviceUuid'] = deviceUuid

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getComplianceStatus

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getSNMPDestination')
def getSNMPDestination(configId: str = None, offset: float = None, limit: float = None, sortBy: str = None, order: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if configId is not None:
        final_kwargs['configId'] = configId
    if offset is not None:
        final_kwargs['offset'] = offset
    if limit is not None:
        final_kwargs['limit'] = limit
    if sortBy is not None:
        final_kwargs['sortBy'] = sortBy
    if order is not None:
        final_kwargs['order'] = order

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getSNMPDestination

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getProvisionedDevicesCount')
def getProvisionedDevicesCount(siteId: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if siteId is not None:
        final_kwargs['siteId'] = siteId

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getProvisionedDevicesCount

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('returnsListOfSoftwareImages')
def returnsListOfSoftwareImages(siteId: str = None, productNameOrdinal: float = None, supervisorProductNameOrdinal: float = None, imported: bool = None, name: str = None, version: str = None, golden: bool = None, integrity: str = None, hasAddonImages: bool = None, isAddonImages: bool = None, offset: float = None, limit: float = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if siteId is not None:
        final_kwargs['siteId'] = siteId
    if productNameOrdinal is not None:
        final_kwargs['productNameOrdinal'] = productNameOrdinal
    if supervisorProductNameOrdinal is not None:
        final_kwargs['supervisorProductNameOrdinal'] = supervisorProductNameOrdinal
    if imported is not None:
        final_kwargs['imported'] = imported
    if name is not None:
        final_kwargs['name'] = name
    if version is not None:
        final_kwargs['version'] = version
    if golden is not None:
        final_kwargs['golden'] = golden
    if integrity is not None:
        final_kwargs['integrity'] = integrity
    if hasAddonImages is not None:
        final_kwargs['hasAddonImages'] = hasAddonImages
    if isAddonImages is not None:
        final_kwargs['isAddonImages'] = isAddonImages
    if offset is not None:
        final_kwargs['offset'] = offset
    if limit is not None:
        final_kwargs['limit'] = limit

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.returnsListOfSoftwareImages

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getInterfacesCount')
def getInterfacesCount():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getInterfacesCount

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('readListOfSiteHealthSummaries.')
def readListOfSiteHealthSummaries_(X_CALLER_ID: str = None, startTime: float = None, endTime: float = None, limit: float = None, offset: float = None, sortBy: str = None, order: str = None, siteHierarchy: str = None, siteHierarchyId: str = None, siteType: str = None, id: str = None, view: str = None, attribute: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if X_CALLER_ID is not None:
        final_kwargs['X-CALLER-ID'] = X_CALLER_ID
    if startTime is not None:
        final_kwargs['startTime'] = startTime
    if endTime is not None:
        final_kwargs['endTime'] = endTime
    if limit is not None:
        final_kwargs['limit'] = limit
    if offset is not None:
        final_kwargs['offset'] = offset
    if sortBy is not None:
        final_kwargs['sortBy'] = sortBy
    if order is not None:
        final_kwargs['order'] = order
    if siteHierarchy is not None:
        final_kwargs['siteHierarchy'] = siteHierarchy
    if siteHierarchyId is not None:
        final_kwargs['siteHierarchyId'] = siteHierarchyId
    if siteType is not None:
        final_kwargs['siteType'] = siteType
    if id is not None:
        final_kwargs['id'] = id
    if view is not None:
        final_kwargs['view'] = view
    if attribute is not None:
        final_kwargs['attribute'] = attribute

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.readListOfSiteHealthSummaries_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceList-2')
def getDeviceList_2(limit: int = None, offset: int = None, sort: list = None, sortOrder: str = None, serialNumber: list = None, state: list = None, onbState: list = None, name: list = None, pid: list = None, source: list = None, workflowId: list = None, workflowName: list = None, smartAccountId: list = None, virtualAccountId: list = None, lastContact: bool = None, macAddress: str = None, hostname: str = None, siteName: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if limit is not None:
        final_kwargs['limit'] = limit
    if offset is not None:
        final_kwargs['offset'] = offset
    if sort is not None:
        final_kwargs['sort'] = sort
    if sortOrder is not None:
        final_kwargs['sortOrder'] = sortOrder
    if serialNumber is not None:
        final_kwargs['serialNumber'] = serialNumber
    if state is not None:
        final_kwargs['state'] = state
    if onbState is not None:
        final_kwargs['onbState'] = onbState
    if name is not None:
        final_kwargs['name'] = name
    if pid is not None:
        final_kwargs['pid'] = pid
    if source is not None:
        final_kwargs['source'] = source
    if workflowId is not None:
        final_kwargs['workflowId'] = workflowId
    if workflowName is not None:
        final_kwargs['workflowName'] = workflowName
    if smartAccountId is not None:
        final_kwargs['smartAccountId'] = smartAccountId
    if virtualAccountId is not None:
        final_kwargs['virtualAccountId'] = virtualAccountId
    if lastContact is not None:
        final_kwargs['lastContact'] = lastContact
    if macAddress is not None:
        final_kwargs['macAddress'] = macAddress
    if hostname is not None:
        final_kwargs['hostname'] = hostname
    if siteName is not None:
        final_kwargs['siteName'] = siteName

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getDeviceList_2

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getTasks-2')
def getTasks_2(startTime: str = None, endTime: str = None, data: str = None, errorCode: str = None, serviceType: str = None, username: str = None, progress: str = None, isError: str = None, failureReason: str = None, parentId: str = None, offset: int = None, limit: int = None, sortBy: str = None, order: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if startTime is not None:
        final_kwargs['startTime'] = startTime
    if endTime is not None:
        final_kwargs['endTime'] = endTime
    if data is not None:
        final_kwargs['data'] = data
    if errorCode is not None:
        final_kwargs['errorCode'] = errorCode
    if serviceType is not None:
        final_kwargs['serviceType'] = serviceType
    if username is not None:
        final_kwargs['username'] = username
    if progress is not None:
        final_kwargs['progress'] = progress
    if isError is not None:
        final_kwargs['isError'] = isError
    if failureReason is not None:
        final_kwargs['failureReason'] = failureReason
    if parentId is not None:
        final_kwargs['parentId'] = parentId
    if offset is not None:
        final_kwargs['offset'] = offset
    if limit is not None:
        final_kwargs['limit'] = limit
    if sortBy is not None:
        final_kwargs['sortBy'] = sortBy
    if order is not None:
        final_kwargs['order'] = order

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getTasks_2

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getModules')
def getModules(deviceId: str, limit: int = None, offset: int = None, nameList: list = None, vendorEquipmentTypeList: list = None, partNumberList: list = None, operationalStateCodeList: list = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if deviceId is not None:
        final_kwargs['deviceId'] = deviceId
    if limit is not None:
        final_kwargs['limit'] = limit
    if offset is not None:
        final_kwargs['offset'] = offset
    if nameList is not None:
        final_kwargs['nameList'] = nameList
    if vendorEquipmentTypeList is not None:
        final_kwargs['vendorEquipmentTypeList'] = vendorEquipmentTypeList
    if partNumberList is not None:
        final_kwargs['partNumberList'] = partNumberList
    if operationalStateCodeList is not None:
        final_kwargs['operationalStateCodeList'] = operationalStateCodeList

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getModules

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('retrievesTheCountOfAssignedNetworkDeviceProducts')
def retrievesTheCountOfAssignedNetworkDeviceProducts(imageId: str, productName: str = None, productId: str = None, recommended: str = None, assigned: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if imageId is not None:
        final_kwargs['imageId'] = imageId
    if productName is not None:
        final_kwargs['productName'] = productName
    if productId is not None:
        final_kwargs['productId'] = productId
    if recommended is not None:
        final_kwargs['recommended'] = recommended
    if assigned is not None:
        final_kwargs['assigned'] = assigned

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.retrievesTheCountOfAssignedNetworkDeviceProducts

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getRest_WebhookSubscriptionDetails')
def getRest_WebhookSubscriptionDetails(name: str = None, instanceId: str = None, offset: float = None, limit: float = None, sortBy: str = None, order: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if name is not None:
        final_kwargs['name'] = name
    if instanceId is not None:
        final_kwargs['instanceId'] = instanceId
    if offset is not None:
        final_kwargs['offset'] = offset
    if limit is not None:
        final_kwargs['limit'] = limit
    if sortBy is not None:
        final_kwargs['sortBy'] = sortBy
    if order is not None:
        final_kwargs['order'] = order

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getRest_WebhookSubscriptionDetails

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('WebhookSubscriptionDetail')(globals()['getRest_WebhookSubscriptionDetails'])

# alias → easier for LLM
register('WebhookSubscriptionDetails')(globals()['getRest_WebhookSubscriptionDetails'])

@register('WebhookSubscriptionDetail')
def WebhookSubscriptionDetail(name: str = None, instanceId: str = None, offset: float = None, limit: float = None, sortBy: str = None, order: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if name is not None:
        final_kwargs['name'] = name
    if instanceId is not None:
        final_kwargs['instanceId'] = instanceId
    if offset is not None:
        final_kwargs['offset'] = offset
    if limit is not None:
        final_kwargs['limit'] = limit
    if sortBy is not None:
        final_kwargs['sortBy'] = sortBy
    if order is not None:
        final_kwargs['order'] = order

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.WebhookSubscriptionDetail

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('WebhookSubscriptionDetails')
def WebhookSubscriptionDetails(name: str = None, instanceId: str = None, offset: float = None, limit: float = None, sortBy: str = None, order: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if name is not None:
        final_kwargs['name'] = name
    if instanceId is not None:
        final_kwargs['instanceId'] = instanceId
    if offset is not None:
        final_kwargs['offset'] = offset
    if limit is not None:
        final_kwargs['limit'] = limit
    if sortBy is not None:
        final_kwargs['sortBy'] = sortBy
    if order is not None:
        final_kwargs['order'] = order

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.WebhookSubscriptionDetails

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceHistory')
def getDeviceHistory(serialNumber: str, sort: list = None, sortOrder: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if serialNumber is not None:
        final_kwargs['serialNumber'] = serialNumber
    if sort is not None:
        final_kwargs['sort'] = sort
    if sortOrder is not None:
        final_kwargs['sortOrder'] = sortOrder

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getDeviceHistory

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getApplicationPolicyQueuingProfileCount')
def getApplicationPolicyQueuingProfileCount():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getApplicationPolicyQueuingProfileCount

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getsTheTotalNetworkDeviceCountsBasedOnTheProvidedQueryParameters')
def getsTheTotalNetworkDeviceCountsBasedOnTheProvidedQueryParameters(startTime: float = None, endTime: float = None, id: str = None, siteHierarchy: str = None, siteHierarchyId: str = None, siteId: str = None, managementIpAddress: str = None, macAddress: str = None, family: str = None, type: str = None, role: str = None, serialNumber: str = None, maintenanceMode: bool = None, softwareVersion: str = None, healthScore: str = None, view: str = None, attribute: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if startTime is not None:
        final_kwargs['startTime'] = startTime
    if endTime is not None:
        final_kwargs['endTime'] = endTime
    if id is not None:
        final_kwargs['id'] = id
    if siteHierarchy is not None:
        final_kwargs['siteHierarchy'] = siteHierarchy
    if siteHierarchyId is not None:
        final_kwargs['siteHierarchyId'] = siteHierarchyId
    if siteId is not None:
        final_kwargs['siteId'] = siteId
    if managementIpAddress is not None:
        final_kwargs['managementIpAddress'] = managementIpAddress
    if macAddress is not None:
        final_kwargs['macAddress'] = macAddress
    if family is not None:
        final_kwargs['family'] = family
    if type is not None:
        final_kwargs['type'] = type
    if role is not None:
        final_kwargs['role'] = role
    if serialNumber is not None:
        final_kwargs['serialNumber'] = serialNumber
    if maintenanceMode is not None:
        final_kwargs['maintenanceMode'] = maintenanceMode
    if softwareVersion is not None:
        final_kwargs['softwareVersion'] = softwareVersion
    if healthScore is not None:
        final_kwargs['healthScore'] = healthScore
    if view is not None:
        final_kwargs['view'] = view
    if attribute is not None:
        final_kwargs['attribute'] = attribute

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getsTheTotalNetworkDeviceCountsBasedOnTheProvidedQueryParameters

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getTaskTree')
def getTaskTree(taskId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if taskId is not None:
        final_kwargs['taskId'] = taskId

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getTaskTree

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDiscoveredNetworkDevicesByDiscoveryId')
def getDiscoveredNetworkDevicesByDiscoveryId(id: str, taskId: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if id is not None:
        final_kwargs['id'] = id
    if taskId is not None:
        final_kwargs['taskId'] = taskId

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getDiscoveredNetworkDevicesByDiscoveryId

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getStatusAPIForEvents')
def getStatusAPIForEvents(executionId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if executionId is not None:
        final_kwargs['executionId'] = executionId

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getStatusAPIForEvents

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getSiteAssignedNetworkDevicesCount')
def getSiteAssignedNetworkDevicesCount(siteId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if siteId is not None:
        final_kwargs['siteId'] = siteId

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getSiteAssignedNetworkDevicesCount

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetworkV2')
def getNetworkV2(siteId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if siteId is not None:
        final_kwargs['siteId'] = siteId

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetworkV2

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceValuesThatMatchFullyOrPartiallyAnAttribute')
def getDeviceValuesThatMatchFullyOrPartiallyAnAttribute(vrfName: str = None, managementIpAddress: str = None, hostname: str = None, macAddress: str = None, family: str = None, collectionStatus: str = None, collectionInterval: str = None, softwareVersion: str = None, softwareType: str = None, reachabilityStatus: str = None, reachabilityFailureReason: str = None, errorCode: str = None, platformId: str = None, series: str = None, type: str = None, serialNumber: str = None, upTime: str = None, role: str = None, roleSource: str = None, associatedWlcIp: str = None, offset: int = None, limit: int = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if vrfName is not None:
        final_kwargs['vrfName'] = vrfName
    if managementIpAddress is not None:
        final_kwargs['managementIpAddress'] = managementIpAddress
    if hostname is not None:
        final_kwargs['hostname'] = hostname
    if macAddress is not None:
        final_kwargs['macAddress'] = macAddress
    if family is not None:
        final_kwargs['family'] = family
    if collectionStatus is not None:
        final_kwargs['collectionStatus'] = collectionStatus
    if collectionInterval is not None:
        final_kwargs['collectionInterval'] = collectionInterval
    if softwareVersion is not None:
        final_kwargs['softwareVersion'] = softwareVersion
    if softwareType is not None:
        final_kwargs['softwareType'] = softwareType
    if reachabilityStatus is not None:
        final_kwargs['reachabilityStatus'] = reachabilityStatus
    if reachabilityFailureReason is not None:
        final_kwargs['reachabilityFailureReason'] = reachabilityFailureReason
    if errorCode is not None:
        final_kwargs['errorCode'] = errorCode
    if platformId is not None:
        final_kwargs['platformId'] = platformId
    if series is not None:
        final_kwargs['series'] = series
    if type is not None:
        final_kwargs['type'] = type
    if serialNumber is not None:
        final_kwargs['serialNumber'] = serialNumber
    if upTime is not None:
        final_kwargs['upTime'] = upTime
    if role is not None:
        final_kwargs['role'] = role
    if roleSource is not None:
        final_kwargs['roleSource'] = roleSource
    if associatedWlcIp is not None:
        final_kwargs['associatedWlcIp'] = associatedWlcIp
    if offset is not None:
        final_kwargs['offset'] = offset
    if limit is not None:
        final_kwargs['limit'] = limit

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getDeviceValuesThatMatchFullyOrPartiallyAnAttribute

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('sensors')
def sensors(siteId: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if siteId is not None:
        final_kwargs['siteId'] = siteId

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.sensors

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceInfoFromSDAFabric')
def getDeviceInfoFromSDAFabric(deviceManagementIpAddress: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if deviceManagementIpAddress is not None:
        final_kwargs['deviceManagementIpAddress'] = deviceManagementIpAddress

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getDeviceInfoFromSDAFabric

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getPortAssignmentForAccessPointInSDAFabric')
def getPortAssignmentForAccessPointInSDAFabric(deviceManagementIpAddress: str, interfaceName: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if deviceManagementIpAddress is not None:
        final_kwargs['deviceManagementIpAddress'] = deviceManagementIpAddress
    if interfaceName is not None:
        final_kwargs['interfaceName'] = interfaceName

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getPortAssignmentForAccessPointInSDAFabric

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getIPPoolFromSDAVirtualNetwork')
def getIPPoolFromSDAVirtualNetwork(siteNameHierarchy: str, virtualNetworkName: str, ipPoolName: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if siteNameHierarchy is not None:
        final_kwargs['siteNameHierarchy'] = siteNameHierarchy
    if virtualNetworkName is not None:
        final_kwargs['virtualNetworkName'] = virtualNetworkName
    if ipPoolName is not None:
        final_kwargs['ipPoolName'] = ipPoolName

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getIPPoolFromSDAVirtualNetwork

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getEdgeDeviceFromSDAFabric')
def getEdgeDeviceFromSDAFabric(deviceManagementIpAddress: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if deviceManagementIpAddress is not None:
        final_kwargs['deviceManagementIpAddress'] = deviceManagementIpAddress

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getEdgeDeviceFromSDAFabric

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getMulticastDetailsFromSDAFabric')
def getMulticastDetailsFromSDAFabric(siteNameHierarchy: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if siteNameHierarchy is not None:
        final_kwargs['siteNameHierarchy'] = siteNameHierarchy

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getMulticastDetailsFromSDAFabric

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getApplications')
def getApplications(offset: float = None, limit: float = None, name: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if offset is not None:
        final_kwargs['offset'] = offset
    if limit is not None:
        final_kwargs['limit'] = limit
    if name is not None:
        final_kwargs['name'] = name

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getApplications

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('retrieveRFProfiles')
def retrieveRFProfiles(rf_profile_name: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if rf_profile_name is not None:
        final_kwargs['rf-profile-name'] = rf_profile_name

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.retrieveRFProfiles

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getNetwork')
def getNetwork(siteId: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if siteId is not None:
        final_kwargs['siteId'] = siteId

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getNetwork

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getReserveIPSubpool')
def getReserveIPSubpool(siteId: str = None, offset: float = None, limit: float = None, ignoreInheritedGroups: str = None, poolUsage: str = None, groupName: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if siteId is not None:
        final_kwargs['siteId'] = siteId
    if offset is not None:
        final_kwargs['offset'] = offset
    if limit is not None:
        final_kwargs['limit'] = limit
    if ignoreInheritedGroups is not None:
        final_kwargs['ignoreInheritedGroups'] = ignoreInheritedGroups
    if poolUsage is not None:
        final_kwargs['poolUsage'] = poolUsage
    if groupName is not None:
        final_kwargs['groupName'] = groupName

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getReserveIPSubpool

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getTransitPeerNetworkInfo')
def getTransitPeerNetworkInfo(transitPeerNetworkName: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if transitPeerNetworkName is not None:
        final_kwargs['transitPeerNetworkName'] = transitPeerNetworkName

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getTransitPeerNetworkInfo

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('clientProximity')
def clientProximity(username: str, number_days: float = None, time_resolution: float = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if username is not None:
        final_kwargs['username'] = username
    if number_days is not None:
        final_kwargs['number_days'] = number_days
    if time_resolution is not None:
        final_kwargs['time_resolution'] = time_resolution

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.clientProximity

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('applications')
def applications(siteId: str = None, deviceId: str = None, macAddress: str = None, startTime: float = None, endTime: float = None, applicationHealth: str = None, offset: float = None, limit: float = None, applicationName: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if siteId is not None:
        final_kwargs['siteId'] = siteId
    if deviceId is not None:
        final_kwargs['deviceId'] = deviceId
    if macAddress is not None:
        final_kwargs['macAddress'] = macAddress
    if startTime is not None:
        final_kwargs['startTime'] = startTime
    if endTime is not None:
        final_kwargs['endTime'] = endTime
    if applicationHealth is not None:
        final_kwargs['applicationHealth'] = applicationHealth
    if offset is not None:
        final_kwargs['offset'] = offset
    if limit is not None:
        final_kwargs['limit'] = limit
    if applicationName is not None:
        final_kwargs['applicationName'] = applicationName

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.applications

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getApplicationSets')
def getApplicationSets(offset: float = None, limit: float = None, name: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if offset is not None:
        final_kwargs['offset'] = offset
    if limit is not None:
        final_kwargs['limit'] = limit
    if name is not None:
        final_kwargs['name'] = name

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getApplicationSets

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getApplicationsCount')
def getApplicationsCount():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getApplicationsCount

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getGlobalPool')
def getGlobalPool(offset: float = None, limit: float = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if offset is not None:
        final_kwargs['offset'] = offset
    if limit is not None:
        final_kwargs['limit'] = limit

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getGlobalPool

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getVNFromSDAFabric')
def getVNFromSDAFabric(virtualNetworkName: str, siteNameHierarchy: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if virtualNetworkName is not None:
        final_kwargs['virtualNetworkName'] = virtualNetworkName
    if siteNameHierarchy is not None:
        final_kwargs['siteNameHierarchy'] = siteNameHierarchy

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getVNFromSDAFabric

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDefaultAuthenticationProfileFromSDAFabric')
def getDefaultAuthenticationProfileFromSDAFabric(siteNameHierarchy: str, authenticateTemplateName: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if siteNameHierarchy is not None:
        final_kwargs['siteNameHierarchy'] = siteNameHierarchy
    if authenticateTemplateName is not None:
        final_kwargs['authenticateTemplateName'] = authenticateTemplateName

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getDefaultAuthenticationProfileFromSDAFabric

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getProvisionedWiredDevice')
def getProvisionedWiredDevice(deviceManagementIpAddress: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if deviceManagementIpAddress is not None:
        final_kwargs['deviceManagementIpAddress'] = deviceManagementIpAddress

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getProvisionedWiredDevice

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceCredentialDetails')
def getDeviceCredentialDetails(siteId: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if siteId is not None:
        final_kwargs['siteId'] = siteId

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getDeviceCredentialDetails

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getSiteFromSDAFabric')
def getSiteFromSDAFabric(siteNameHierarchy: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if siteNameHierarchy is not None:
        final_kwargs['siteNameHierarchy'] = siteNameHierarchy

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getSiteFromSDAFabric

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getServiceProviderDetails')
def getServiceProviderDetails():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getServiceProviderDetails

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getSite')
def getSite(name: str = None, siteId: str = None, type: str = None, offset: int = None, limit: int = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if name is not None:
        final_kwargs['name'] = name
    if siteId is not None:
        final_kwargs['siteId'] = siteId
    if type is not None:
        final_kwargs['type'] = type
    if offset is not None:
        final_kwargs['offset'] = offset
    if limit is not None:
        final_kwargs['limit'] = limit

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getSite

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getVirtualNetworkSummary')
def getVirtualNetworkSummary(siteNameHierarchy: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if siteNameHierarchy is not None:
        final_kwargs['siteNameHierarchy'] = siteNameHierarchy

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getVirtualNetworkSummary

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getWirelessProfile')
def getWirelessProfile(profileName: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if profileName is not None:
        final_kwargs['profileName'] = profileName

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getWirelessProfile

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getIssueEnrichmentDetails')
def getIssueEnrichmentDetails(entity_type: str, entity_value: str, __persistbapioutput: bool = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if entity_type is not None:
        final_kwargs['entity_type'] = entity_type
    if entity_value is not None:
        final_kwargs['entity_value'] = entity_value
    if __persistbapioutput is not None:
        final_kwargs['__persistbapioutput'] = __persistbapioutput

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getIssueEnrichmentDetails

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('sensorTestResults')
def sensorTestResults(siteId: str = None, startTime: float = None, endTime: float = None, testFailureBy: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if siteId is not None:
        final_kwargs['siteId'] = siteId
    if startTime is not None:
        final_kwargs['startTime'] = startTime
    if endTime is not None:
        final_kwargs['endTime'] = endTime
    if testFailureBy is not None:
        final_kwargs['testFailureBy'] = testFailureBy

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.sensorTestResults

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceRoleInSDAFabric')
def getDeviceRoleInSDAFabric(deviceManagementIpAddress: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if deviceManagementIpAddress is not None:
        final_kwargs['deviceManagementIpAddress'] = deviceManagementIpAddress

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getDeviceRoleInSDAFabric

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getEnterpriseSSID')
def getEnterpriseSSID(ssidName: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if ssidName is not None:
        final_kwargs['ssidName'] = ssidName

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getEnterpriseSSID

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getBorderDeviceDetailFromSDAFabric')
def getBorderDeviceDetailFromSDAFabric(deviceManagementIpAddress: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if deviceManagementIpAddress is not None:
        final_kwargs['deviceManagementIpAddress'] = deviceManagementIpAddress

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getBorderDeviceDetailFromSDAFabric

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getPortAssignmentForUserDeviceInSDAFabric')
def getPortAssignmentForUserDeviceInSDAFabric(deviceManagementIpAddress: str, interfaceName: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if deviceManagementIpAddress is not None:
        final_kwargs['deviceManagementIpAddress'] = deviceManagementIpAddress
    if interfaceName is not None:
        final_kwargs['interfaceName'] = interfaceName

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getPortAssignmentForUserDeviceInSDAFabric

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getFailedITSMEvents')
def getFailedITSMEvents(instanceId: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if instanceId is not None:
        final_kwargs['instanceId'] = instanceId

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getFailedITSMEvents

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getSSIDToIPPoolMapping')
def getSSIDToIPPoolMapping(vlanName: str, siteNameHierarchy: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if vlanName is not None:
        final_kwargs['vlanName'] = vlanName
    if siteNameHierarchy is not None:
        final_kwargs['siteNameHierarchy'] = siteNameHierarchy

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getSSIDToIPPoolMapping

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getControlPlaneDeviceFromSDAFabric')
def getControlPlaneDeviceFromSDAFabric(deviceManagementIpAddress: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if deviceManagementIpAddress is not None:
        final_kwargs['deviceManagementIpAddress'] = deviceManagementIpAddress

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getControlPlaneDeviceFromSDAFabric

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getCMDBSyncStatus')
def getCMDBSyncStatus(status: str = None, date: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if status is not None:
        final_kwargs['status'] = status
    if date is not None:
        final_kwargs['date'] = date

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getCMDBSyncStatus

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getSiteCount')
def getSiteCount(siteId: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if siteId is not None:
        final_kwargs['siteId'] = siteId

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getSiteCount

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getClientEnrichmentDetails')
def getClientEnrichmentDetails(entity_type: str, entity_value: str, issueCategory: str = None, __persistbapioutput: bool = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if entity_type is not None:
        final_kwargs['entity_type'] = entity_type
    if entity_value is not None:
        final_kwargs['entity_value'] = entity_value
    if issueCategory is not None:
        final_kwargs['issueCategory'] = issueCategory
    if __persistbapioutput is not None:
        final_kwargs['__persistbapioutput'] = __persistbapioutput

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getClientEnrichmentDetails

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getVirtualNetworkWithScalableGroups')
def getVirtualNetworkWithScalableGroups(virtualNetworkName: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if virtualNetworkName is not None:
        final_kwargs['virtualNetworkName'] = virtualNetworkName

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getVirtualNetworkWithScalableGroups

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDynamicInterface')
def getDynamicInterface(__runsync: bool = None, __timeout: float = None, interface_name: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if __runsync is not None:
        final_kwargs['__runsync'] = __runsync
    if __timeout is not None:
        final_kwargs['__timeout'] = __timeout
    if interface_name is not None:
        final_kwargs['interface-name'] = interface_name

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getDynamicInterface

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getApplicationSetsCount')
def getApplicationSetsCount():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getApplicationSetsCount

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getUserEnrichmentDetails')
def getUserEnrichmentDetails(entity_type: str, entity_value: str, __persistbapioutput: bool = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if entity_type is not None:
        final_kwargs['entity_type'] = entity_type
    if entity_value is not None:
        final_kwargs['entity_value'] = entity_value
    if __persistbapioutput is not None:
        final_kwargs['__persistbapioutput'] = __persistbapioutput

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getUserEnrichmentDetails

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getDeviceEnrichmentDetails')
def getDeviceEnrichmentDetails(entity_type: str, entity_value: str, __persistbapioutput: bool = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if entity_type is not None:
        final_kwargs['entity_type'] = entity_type
    if entity_value is not None:
        final_kwargs['entity_value'] = entity_value
    if __persistbapioutput is not None:
        final_kwargs['__persistbapioutput'] = __persistbapioutput

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getDeviceEnrichmentDetails

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getMembership')
def getMembership(siteId: str, offset: float = None, limit: float = None, deviceFamily: str = None, serialNumber: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if siteId is not None:
        final_kwargs['siteId'] = siteId
    if offset is not None:
        final_kwargs['offset'] = offset
    if limit is not None:
        final_kwargs['limit'] = limit
    if deviceFamily is not None:
        final_kwargs['deviceFamily'] = deviceFamily
    if serialNumber is not None:
        final_kwargs['serialNumber'] = serialNumber

    # No body parameter for this function.
    body_payload = None

    client = CatalystClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getMembership

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)
