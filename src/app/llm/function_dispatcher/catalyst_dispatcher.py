# app/llm/function_dispatcher/catalyst_dispatcher.py
from typing import Any
from app.llm.function_dispatcher import register
from app.llm.platform_clients.catalyst_client import CatalystClient

@register('retrievesNetworkDeviceProductNamesAssignedToASoftwareImage.')
def retrievesNetworkDeviceProductNamesAssignedToASoftwareImage_(imageId: str, **kwargs):
    return CatalystClient().retrievesNetworkDeviceProductNamesAssignedToASoftwareImage_(**{'imageId': imageId, **kwargs})

@register('getsAllTheVersionsOfAGivenTemplate')
def getsAllTheVersionsOfAGivenTemplate(templateId: str):
    return CatalystClient().getsAllTheVersionsOfAGivenTemplate(**{'templateId': templateId})

@register('returnsTheCountOfNetworkDeviceProductNamesForASite')
def returnsTheCountOfNetworkDeviceProductNamesForASite(**kwargs):
    return CatalystClient().returnsTheCountOfNetworkDeviceProductNamesForASite(**{**kwargs})

@register('getMulticastVirtualNetworks')
def getMulticastVirtualNetworks(**kwargs):
    return CatalystClient().getMulticastVirtualNetworks(**{**kwargs})

@register('getDeviceControllabilitySettings')
def getDeviceControllabilitySettings():
    return CatalystClient().getDeviceControllabilitySettings(**{})

@register('getChassisDetailsForDevice')
def getChassisDetailsForDevice(deviceId: str):
    return CatalystClient().getChassisDetailsForDevice(**{'deviceId': deviceId})

@register('getsABuilding')
def getsABuilding(id: str):
    return CatalystClient().getsABuilding(**{'id': id})

@register('getCountOfAllDiscoveryJobs')
def getCountOfAllDiscoveryJobs():
    return CatalystClient().getCountOfAllDiscoveryJobs(**{})

@register('getViewsForAGivenViewGroup')
def getViewsForAGivenViewGroup(viewGroupId: str):
    return CatalystClient().getViewsForAGivenViewGroup(**{'viewGroupId': viewGroupId})

@register('getDeviceById')
def getDeviceById(id: str):
    return CatalystClient().getDeviceById(**{'id': id})

@register('retrieveTheVLANsAndSSIDsMappedToTheVLANWithinAFabricSite.')
def retrieveTheVLANsAndSSIDsMappedToTheVLANWithinAFabricSite_(Content_Type: str, fabricId: str, **kwargs):
    return CatalystClient().retrieveTheVLANsAndSSIDsMappedToTheVLANWithinAFabricSite_(**{'Content-Type': Content_Type, 'fabricId': fabricId, **kwargs})

@register('retrieveImageDistributionServers')
def retrieveImageDistributionServers():
    return CatalystClient().retrieveImageDistributionServers(**{})

@register('retrieveTagsAssociatedWithNetworkDevices.')
def retrieveTagsAssociatedWithNetworkDevices_(**kwargs):
    return CatalystClient().retrieveTagsAssociatedWithNetworkDevices_(**{**kwargs})

@register('statusOfTemplateDeployment')
def statusOfTemplateDeployment(deploymentId: str):
    return CatalystClient().statusOfTemplateDeployment(**{'deploymentId': deploymentId})

@register('getIssueTriggerDefinitionForGivenId.')
def getIssueTriggerDefinitionForGivenId_(id: str, **kwargs):
    return CatalystClient().getIssueTriggerDefinitionForGivenId_(**{'id': id, **kwargs})

@register('retrieveBannerSettingsForASite')
def retrieveBannerSettingsForASite(id: str, **kwargs):
    return CatalystClient().retrieveBannerSettingsForASite(**{'id': id, **kwargs})

@register('getSiteAssignedNetworkDevices')
def getSiteAssignedNetworkDevices(siteId: str, **kwargs):
    return CatalystClient().getSiteAssignedNetworkDevices(**{'siteId': siteId, **kwargs})

@register('getNetworkDevicesCredentialsSyncStatus')
def getNetworkDevicesCredentialsSyncStatus(id: str):
    return CatalystClient().getNetworkDevicesCredentialsSyncStatus(**{'id': id})

@register('getSoftwareImageDetails')
def getSoftwareImageDetails(**kwargs):
    return CatalystClient().getSoftwareImageDetails(**{**kwargs})

@register('getInterfaceByID')
def getInterfaceByID(id: str):
    return CatalystClient().getInterfaceByID(**{'id': id})

@register('getAnycastGateways')
def getAnycastGateways(**kwargs):
    return CatalystClient().getAnycastGateways(**{**kwargs})

@register('getApplicationSet/s')
def getApplicationSet_s(attributes: str, limit: float, offset: float, **kwargs):
    return CatalystClient().getApplicationSet_s(**{'attributes': attributes, 'limit': limit, 'offset': offset, **kwargs})

@register('getTagMembersById')
def getTagMembersById(id: str, memberType: str, **kwargs):
    return CatalystClient().getTagMembersById(**{'id': id, 'memberType': memberType, **kwargs})

@register('getFabricSiteCount')
def getFabricSiteCount():
    return CatalystClient().getFabricSiteCount(**{})

@register('retrievesAllTheValidationSets')
def retrievesAllTheValidationSets(**kwargs):
    return CatalystClient().retrievesAllTheValidationSets(**{**kwargs})

@register('retrievesTheListOfSitesThatTheGivenNetworkProfileForSitesIsAssignedTo')
def retrievesTheListOfSitesThatTheGivenNetworkProfileForSitesIsAssignedTo(profileId: str, **kwargs):
    return CatalystClient().retrievesTheListOfSitesThatTheGivenNetworkProfileForSitesIsAssignedTo(**{'profileId': profileId, **kwargs})

@register('getFabricDevicesLayer2HandoffsCount')
def getFabricDevicesLayer2HandoffsCount(fabricId: str, **kwargs):
    return CatalystClient().getFabricDevicesLayer2HandoffsCount(**{'fabricId': fabricId, **kwargs})

@register('countOfEventSubscriptions')
def countOfEventSubscriptions(eventIds: str):
    return CatalystClient().countOfEventSubscriptions(**{'eventIds': eventIds})

@register('getSSIDBySite')
def getSSIDBySite(siteId: str, **kwargs):
    return CatalystClient().getSSIDBySite(**{'siteId': siteId, **kwargs})

@register('getITSMIntegrationSettingById')
def getITSMIntegrationSettingById(instanceId: str):
    return CatalystClient().getITSMIntegrationSettingById(**{'instanceId': instanceId})

@register('getDetailsOfASingleAssuranceEvent')
def getDetailsOfASingleAssuranceEvent(id: str, **kwargs):
    return CatalystClient().getDetailsOfASingleAssuranceEvent(**{'id': id, **kwargs})

@register('getRFProfiles')
def getRFProfiles(**kwargs):
    return CatalystClient().getRFProfiles(**{**kwargs})

@register('retrieveTelemetrySettingsForASite')
def retrieveTelemetrySettingsForASite(id: str, **kwargs):
    return CatalystClient().retrieveTelemetrySettingsForASite(**{'id': id, **kwargs})

@register('getAllUser-Defined-Fields')
def getAllUser_Defined_Fields(**kwargs):
    return CatalystClient().getAllUser_Defined_Fields(**{**kwargs})

@register('queryAssuranceEvents')
def queryAssuranceEvents(deviceFamily: str, **kwargs):
    return CatalystClient().queryAssuranceEvents(**{'deviceFamily': deviceFamily, **kwargs})

@register('getFloorSettings')
def getFloorSettings():
    return CatalystClient().getFloorSettings(**{})

@register('getTheTotalNumberOfIssuesForGivenSetOfFilters')
def getTheTotalNumberOfIssuesForGivenSetOfFilters(**kwargs):
    return CatalystClient().getTheTotalNumberOfIssuesForGivenSetOfFilters(**{**kwargs})

@register('getTag')
def getTag(**kwargs):
    return CatalystClient().getTag(**{**kwargs})

@register('getLayer2VirtualNetworks')
def getLayer2VirtualNetworks(**kwargs):
    return CatalystClient().getLayer2VirtualNetworks(**{**kwargs})

@register('getFabricZoneCount')
def getFabricZoneCount():
    return CatalystClient().getFabricZoneCount(**{})

@register('getWebhookDestination')
def getWebhookDestination(**kwargs):
    return CatalystClient().getWebhookDestination(**{**kwargs})

@register('retrieveTimeZoneSettingsForASite')
def retrieveTimeZoneSettingsForASite(id: str, **kwargs):
    return CatalystClient().retrieveTimeZoneSettingsForASite(**{'id': id, **kwargs})

@register('getDeviceByID')
def getDeviceByID(id: str):
    return CatalystClient().getDeviceByID(**{'id': id})

@register('getApplicationPolicyQueuingProfile')
def getApplicationPolicyQueuingProfile(**kwargs):
    return CatalystClient().getApplicationPolicyQueuingProfile(**{**kwargs})

@register('getSyslogDestination')
def getSyslogDestination(**kwargs):
    return CatalystClient().getSyslogDestination(**{**kwargs})

@register('getAll802.11beProfiles')
def getAll802_11beProfiles(**kwargs):
    return CatalystClient().getAll802_11beProfiles(**{**kwargs})

@register('getSyncResultForVirtualAccount')
def getSyncResultForVirtualAccount(domain: str, name: str):
    return CatalystClient().getSyncResultForVirtualAccount(**{'domain': domain, 'name': name})

@register('getAllTheCustomIssueDefinitionsBasedOnTheGivenFilters.')
def getAllTheCustomIssueDefinitionsBasedOnTheGivenFilters_(**kwargs):
    return CatalystClient().getAllTheCustomIssueDefinitionsBasedOnTheGivenFilters_(**{**kwargs})

@register('getApplicationPolicyDefault')
def getApplicationPolicyDefault():
    return CatalystClient().getApplicationPolicyDefault(**{})

@register('getPrimaryManagedAPLocationsForSpecificWirelessController')
def getPrimaryManagedAPLocationsForSpecificWirelessController(networkDeviceId: str, **kwargs):
    return CatalystClient().getPrimaryManagedAPLocationsForSpecificWirelessController(**{'networkDeviceId': networkDeviceId, **kwargs})

@register('getModuleInfoById')
def getModuleInfoById(id: str):
    return CatalystClient().getModuleInfoById(**{'id': id})

@register('getFabricDevicesLayer3HandoffsWithSdaTransit')
def getFabricDevicesLayer3HandoffsWithSdaTransit(fabricId: str, **kwargs):
    return CatalystClient().getFabricDevicesLayer3HandoffsWithSdaTransit(**{'fabricId': fabricId, **kwargs})

@register('getFabricDevicesLayer3HandoffsWithIpTransit')
def getFabricDevicesLayer3HandoffsWithIpTransit(fabricId: str, **kwargs):
    return CatalystClient().getFabricDevicesLayer3HandoffsWithIpTransit(**{'fabricId': fabricId, **kwargs})

@register('returnsNetworkDeviceProductNamesForASite')
def returnsNetworkDeviceProductNamesForASite(**kwargs):
    return CatalystClient().returnsNetworkDeviceProductNamesForASite(**{**kwargs})

@register('countOfNotifications')
def countOfNotifications(**kwargs):
    return CatalystClient().countOfNotifications(**{**kwargs})

@register('getAScheduledReport')
def getAScheduledReport(reportId: str):
    return CatalystClient().getAScheduledReport(**{'reportId': reportId})

@register('getSiteHealth')
def getSiteHealth(**kwargs):
    return CatalystClient().getSiteHealth(**{**kwargs})

@register('returnsPOEInterfaceDetailsForTheDevice.')
def returnsPOEInterfaceDetailsForTheDevice_(deviceUuid: str, **kwargs):
    return CatalystClient().returnsPOEInterfaceDetailsForTheDevice_(**{'deviceUuid': deviceUuid, **kwargs})

@register('getSitesCount')
def getSitesCount(**kwargs):
    return CatalystClient().getSitesCount(**{**kwargs})

@register('retrievesTheListOfValidationWorkflows')
def retrievesTheListOfValidationWorkflows(**kwargs):
    return CatalystClient().retrievesTheListOfValidationWorkflows(**{**kwargs})

@register('readAnAggregatedSummaryOfSiteHealthData.')
def readAnAggregatedSummaryOfSiteHealthData_(**kwargs):
    return CatalystClient().readAnAggregatedSummaryOfSiteHealthData_(**{**kwargs})

@register('retrievesTheCountOfProfilesThatTheGivenSiteHasBeenAssigned')
def retrievesTheCountOfProfilesThatTheGivenSiteHasBeenAssigned(siteId: str):
    return CatalystClient().retrievesTheCountOfProfilesThatTheGivenSiteHasBeenAssigned(**{'siteId': siteId})

@register('getSiteCountV2')
def getSiteCountV2(**kwargs):
    return CatalystClient().getSiteCountV2(**{**kwargs})

@register('returnsCountOfSoftwareImages')
def returnsCountOfSoftwareImages(**kwargs):
    return CatalystClient().returnsCountOfSoftwareImages(**{**kwargs})

@register('getExtranetPolicies')
def getExtranetPolicies(**kwargs):
    return CatalystClient().getExtranetPolicies(**{**kwargs})

@register('getWirelessProfileByID')
def getWirelessProfileByID(id: str):
    return CatalystClient().getWirelessProfileByID(**{'id': id})

@register('getFlexibleReportScheduleByReportId')
def getFlexibleReportScheduleByReportId(Content_Type: str, reportId: str):
    return CatalystClient().getFlexibleReportScheduleByReportId(**{'Content-Type': Content_Type, 'reportId': reportId})

@register('getPortChannels')
def getPortChannels(**kwargs):
    return CatalystClient().getPortChannels(**{**kwargs})

@register('getRFProfileByID')
def getRFProfileByID(id: str):
    return CatalystClient().getRFProfileByID(**{'id': id})

@register('getsTheTemplatesAvailable')
def getsTheTemplatesAvailable(**kwargs):
    return CatalystClient().getsTheTemplatesAvailable(**{**kwargs})

@register('getSyslogSubscriptionDetails')
def getSyslogSubscriptionDetails(**kwargs):
    return CatalystClient().getSyslogSubscriptionDetails(**{**kwargs})

@register('returnsAllIssueTriggerDefinitionsForGivenFilters.')
def returnsAllIssueTriggerDefinitionsForGivenFilters_(**kwargs):
    return CatalystClient().returnsAllIssueTriggerDefinitionsForGivenFilters_(**{**kwargs})

@register('getListOfScheduledReports')
def getListOfScheduledReports(**kwargs):
    return CatalystClient().getListOfScheduledReports(**{**kwargs})

@register('getAAAAttributeAPI')
def getAAAAttributeAPI():
    return CatalystClient().getAAAAttributeAPI(**{})

@register('getClientDetail')
def getClientDetail(macAddress: str, **kwargs):
    return CatalystClient().getClientDetail(**{'macAddress': macAddress, **kwargs})

@register('countTheNumberOfEvents')
def countTheNumberOfEvents(deviceFamily: str, **kwargs):
    return CatalystClient().countTheNumberOfEvents(**{'deviceFamily': deviceFamily, **kwargs})

@register('getEoXStatusForAllDevices')
def getEoXStatusForAllDevices():
    return CatalystClient().getEoXStatusForAllDevices(**{})

@register('getTagMemberCount')
def getTagMemberCount(id: str, memberType: str, **kwargs):
    return CatalystClient().getTagMemberCount(**{'id': id, 'memberType': memberType, **kwargs})

@register('retrievesConfigurationDetailsOfTheExternalIPAMServer.')
def retrievesConfigurationDetailsOfTheExternalIPAMServer_():
    return CatalystClient().retrievesConfigurationDetailsOfTheExternalIPAMServer_(**{})

@register('getViewDetailsForAGivenViewGroup&View')
def getViewDetailsForAGivenViewGroup_View(viewGroupId: str, viewId: str):
    return CatalystClient().getViewDetailsForAGivenViewGroup_View(**{'viewGroupId': viewGroupId, 'viewId': viewId})

@register('getTheDetailsOfPhysicalComponentsOfTheGivenDevice.')
def getTheDetailsOfPhysicalComponentsOfTheGivenDevice_(deviceUuid: str, **kwargs):
    return CatalystClient().getTheDetailsOfPhysicalComponentsOfTheGivenDevice_(**{'deviceUuid': deviceUuid, **kwargs})

@register('getDeviceInterfacesBySpecifiedRange')
def getDeviceInterfacesBySpecifiedRange(deviceId: str, recordsToReturn: int, startIndex: int):
    return CatalystClient().getDeviceInterfacesBySpecifiedRange(**{'deviceId': deviceId, 'recordsToReturn': recordsToReturn, 'startIndex': startIndex})

@register('getPollingIntervalForAllDevices')
def getPollingIntervalForAllDevices():
    return CatalystClient().getPollingIntervalForAllDevices(**{})

@register('getDeviceList')
def getDeviceList(**kwargs):
    return CatalystClient().getDeviceList(**{**kwargs})

@register('getAllKeywordsOfCLIsAcceptedByCommandRunner')
def getAllKeywordsOfCLIsAcceptedByCommandRunner():
    return CatalystClient().getAllKeywordsOfCLIsAcceptedByCommandRunner(**{})

@register('getQosDeviceInterfaceInfo')
def getQosDeviceInterfaceInfo(**kwargs):
    return CatalystClient().getQosDeviceInterfaceInfo(**{**kwargs})

@register('retrieveTheCountOfInterfacesThatAreAssociatedWithAtLeastOneTag.')
def retrieveTheCountOfInterfacesThatAreAssociatedWithAtLeastOneTag_():
    return CatalystClient().retrieveTheCountOfInterfacesThatAreAssociatedWithAtLeastOneTag_(**{})

@register('getDeviceFamilyIdentifiers')
def getDeviceFamilyIdentifiers(**kwargs):
    return CatalystClient().getDeviceFamilyIdentifiers(**{**kwargs})

@register('getTaskCount')
def getTaskCount(**kwargs):
    return CatalystClient().getTaskCount(**{**kwargs})

@register('devices')
def devices(**kwargs):
    return CatalystClient().devices(**{**kwargs})

@register('getSSIDCountForSpecificWirelessController')
def getSSIDCountForSpecificWirelessController(networkDeviceId: str, **kwargs):
    return CatalystClient().getSSIDCountForSpecificWirelessController(**{'networkDeviceId': networkDeviceId, **kwargs})

@register('retrievesValidationDetailsForAValidationSet')
def retrievesValidationDetailsForAValidationSet(id: str):
    return CatalystClient().retrievesValidationDetailsForAValidationSet(**{'id': id})

@register('getSmartAccountList')
def getSmartAccountList():
    return CatalystClient().getSmartAccountList(**{})

@register('getLayer3VirtualNetworks')
def getLayer3VirtualNetworks(**kwargs):
    return CatalystClient().getLayer3VirtualNetworks(**{**kwargs})

@register('getListOfAvailableNamespaces')
def getListOfAvailableNamespaces():
    return CatalystClient().getListOfAvailableNamespaces(**{})

@register('getSSIDByID')
def getSSIDByID(id: str, siteId: str):
    return CatalystClient().getSSIDByID(**{'id': id, 'siteId': siteId})

@register('retrieveNetworkDeviceProductName')
def retrieveNetworkDeviceProductName(productNameOrdinal: float):
    return CatalystClient().retrieveNetworkDeviceProductName(**{'productNameOrdinal': productNameOrdinal})

@register('getExecutionIdByReportId')
def getExecutionIdByReportId(Content_Type: str, reportId: str):
    return CatalystClient().getExecutionIdByReportId(**{'Content-Type': Content_Type, 'reportId': reportId})

@register('getMobilityGroupsCount')
def getMobilityGroupsCount():
    return CatalystClient().getMobilityGroupsCount(**{})

@register('getTaskDetailsByID')
def getTaskDetailsByID(id: str):
    return CatalystClient().getTaskDetailsByID(**{'id': id})

@register('custom-promptSupportGETAPI')
def custom_promptSupportGETAPI():
    return CatalystClient().custom_promptSupportGETAPI(**{})

@register('getAdvisoriesList')
def getAdvisoriesList():
    return CatalystClient().getAdvisoriesList(**{})

@register('getDeviceInterfaceVLANs')
def getDeviceInterfaceVLANs(id: str, **kwargs):
    return CatalystClient().getDeviceInterfaceVLANs(**{'id': id, **kwargs})

@register('getListOfFiles')
def getListOfFiles(nameSpace: str):
    return CatalystClient().getListOfFiles(**{'nameSpace': nameSpace})

@register('retrieveSpecificImageDistributionServer')
def retrieveSpecificImageDistributionServer(id: str):
    return CatalystClient().retrieveSpecificImageDistributionServer(**{'id': id})

@register('getApplicationPolicy')
def getApplicationPolicy(**kwargs):
    return CatalystClient().getApplicationPolicy(**{**kwargs})

@register('getWorkflowById')
def getWorkflowById(id: str):
    return CatalystClient().getWorkflowById(**{'id': id})

@register('getAdvisoriesSummary')
def getAdvisoriesSummary():
    return CatalystClient().getAdvisoriesSummary(**{})

@register('getTagResourceTypes')
def getTagResourceTypes():
    return CatalystClient().getTagResourceTypes(**{})

@register('getPortAssignmentCount')
def getPortAssignmentCount(**kwargs):
    return CatalystClient().getPortAssignmentCount(**{**kwargs})

@register('getDiscoveriesByRange')
def getDiscoveriesByRange(recordsToReturn: int, startIndex: int):
    return CatalystClient().getDiscoveriesByRange(**{'recordsToReturn': recordsToReturn, 'startIndex': startIndex})

@register('getAllITSMIntegrationSettings')
def getAllITSMIntegrationSettings():
    return CatalystClient().getAllITSMIntegrationSettings(**{})

@register('licenseUsageDetails')
def licenseUsageDetails(device_type: str, smart_account_id: str, virtual_account_name: str):
    return CatalystClient().licenseUsageDetails(**{'device_type': device_type, 'smart_account_id': smart_account_id, 'virtual_account_name': virtual_account_name})

@register('getsAnArea')
def getsAnArea(id: str):
    return CatalystClient().getsAnArea(**{'id': id})

@register('getTheCountOfHealthScoreDefinitionsBasedOnProvidedFilters.')
def getTheCountOfHealthScoreDefinitionsBasedOnProvidedFilters_(**kwargs):
    return CatalystClient().getTheCountOfHealthScoreDefinitionsBasedOnProvidedFilters_(**{**kwargs})

@register('getExtranetPolicyCount')
def getExtranetPolicyCount():
    return CatalystClient().getExtranetPolicyCount(**{})

@register('getResyncIntervalForTheNetworkDevice')
def getResyncIntervalForTheNetworkDevice(id: str):
    return CatalystClient().getResyncIntervalForTheNetworkDevice(**{'id': id})

@register('getInterfaces')
def getInterfaces(**kwargs):
    return CatalystClient().getInterfaces(**{**kwargs})

@register('getAllViewGroups')
def getAllViewGroups():
    return CatalystClient().getAllViewGroups(**{})

@register('getEvents')
def getEvents(tags: str, **kwargs):
    return CatalystClient().getEvents(**{'tags': tags, **kwargs})

@register('getEmailEventSubscriptions')
def getEmailEventSubscriptions(**kwargs):
    return CatalystClient().getEmailEventSubscriptions(**{**kwargs})

@register('getEmailSubscriptionDetails')
def getEmailSubscriptionDetails(**kwargs):
    return CatalystClient().getEmailSubscriptionDetails(**{**kwargs})

@register('retrieveAAASettingsForASite')
def retrieveAAASettingsForASite(id: str, **kwargs):
    return CatalystClient().retrieveAAASettingsForASite(**{'id': id, **kwargs})

@register('getInterfaceDetailsByDeviceIdAndInterfaceName')
def getInterfaceDetailsByDeviceIdAndInterfaceName(deviceId: str, name: str):
    return CatalystClient().getInterfaceDetailsByDeviceIdAndInterfaceName(**{'deviceId': deviceId, 'name': name})

@register('getAllGlobalCredentialsV2')
def getAllGlobalCredentialsV2():
    return CatalystClient().getAllGlobalCredentialsV2(**{})

@register('getAccessPoint(s)FactoryResetStatus')
def getAccessPoint_s_FactoryResetStatus(taskId: str):
    return CatalystClient().getAccessPoint_s_FactoryResetStatus(**{'taskId': taskId})

@register('getNetworkDevicesFromDiscovery')
def getNetworkDevicesFromDiscovery(id: str, **kwargs):
    return CatalystClient().getNetworkDevicesFromDiscovery(**{'id': id, **kwargs})

@register('getSites')
def getSites(**kwargs):
    return CatalystClient().getSites(**{**kwargs})

@register('returnTheCountOfAllTheFabricSiteWhichHasSSIDToIPPoolMapping')
def returnTheCountOfAllTheFabricSiteWhichHasSSIDToIPPoolMapping():
    return CatalystClient().returnTheCountOfAllTheFabricSiteWhichHasSSIDToIPPoolMapping(**{})

@register('getEventSubscriptions')
def getEventSubscriptions(**kwargs):
    return CatalystClient().getEventSubscriptions(**{**kwargs})

@register('readSiteHealthSummaryDataBySiteId.')
def readSiteHealthSummaryDataBySiteId_(id: str, **kwargs):
    return CatalystClient().readSiteHealthSummaryDataBySiteId_(**{'id': id, **kwargs})

@register('getPlannedAccessPointsForFloor')
def getPlannedAccessPointsForFloor(floorId: str, **kwargs):
    return CatalystClient().getPlannedAccessPointsForFloor(**{'floorId': floorId, **kwargs})

@register('returnListOfReplacementDevicesWithReplacementDetails')
def returnListOfReplacementDevicesWithReplacementDetails(**kwargs):
    return CatalystClient().returnListOfReplacementDevicesWithReplacementDetails(**{**kwargs})

@register('getDiscoveryById')
def getDiscoveryById(id: str):
    return CatalystClient().getDiscoveryById(**{'id': id})

@register('getConfigurationArchiveDetails')
def getConfigurationArchiveDetails(**kwargs):
    return CatalystClient().getConfigurationArchiveDetails(**{**kwargs})

@register('getAdvisoriesPerDevice')
def getAdvisoriesPerDevice(deviceId: str):
    return CatalystClient().getAdvisoriesPerDevice(**{'deviceId': deviceId})

@register('getDeviceInterfaceCountForMultipleDevices')
def getDeviceInterfaceCountForMultipleDevices():
    return CatalystClient().getDeviceInterfaceCountForMultipleDevices(**{})

@register('retrievesTheCountOfValidationWorkflows')
def retrievesTheCountOfValidationWorkflows(**kwargs):
    return CatalystClient().retrievesTheCountOfValidationWorkflows(**{**kwargs})

@register('getSNMPProperties')
def getSNMPProperties():
    return CatalystClient().getSNMPProperties(**{})

@register('getComplianceDetailCount')
def getComplianceDetailCount(**kwargs):
    return CatalystClient().getComplianceDetailCount(**{**kwargs})

@register('getOverallClientHealth')
def getOverallClientHealth(**kwargs):
    return CatalystClient().getOverallClientHealth(**{**kwargs})

@register('getLinecardDetails')
def getLinecardDetails(deviceUuid: str):
    return CatalystClient().getLinecardDetails(**{'deviceUuid': deviceUuid})

@register('getsTheTotalNetworkDeviceInterfaceCountsInTheSpecifiedTimeRange.WhenThereIsNoStartAndEndTimeSpecifiedReturnsTheLatestInterfacesTotalCount.')
def getsTheTotalNetworkDeviceInterfaceCountsInTheSpecifiedTimeRange_WhenThereIsNoStartAndEndTimeSpecifiedReturnsTheLatestInterfacesTotalCount_(**kwargs):
    return CatalystClient().getsTheTotalNetworkDeviceInterfaceCountsInTheSpecifiedTimeRange_WhenThereIsNoStartAndEndTimeSpecifiedReturnsTheLatestInterfacesTotalCount_(**{**kwargs})

@register('getWirelessProfilesCount')
def getWirelessProfilesCount():
    return CatalystClient().getWirelessProfilesCount(**{})

@register('getTagById')
def getTagById(id: str):
    return CatalystClient().getTagById(**{'id': id})

@register('getAuditLogSummary')
def getAuditLogSummary(**kwargs):
    return CatalystClient().getAuditLogSummary(**{**kwargs})

@register('getsAListOfProjects')
def getsAListOfProjects(**kwargs):
    return CatalystClient().getsAListOfProjects(**{**kwargs})

@register('systemHealthCountAPI')
def systemHealthCountAPI(**kwargs):
    return CatalystClient().systemHealthCountAPI(**{**kwargs})

@register('getAuthenticationAndPolicyServers')
def getAuthenticationAndPolicyServers(**kwargs):
    return CatalystClient().getAuthenticationAndPolicyServers(**{**kwargs})

@register('getSSIDCountBySite')
def getSSIDCountBySite(siteId: str):
    return CatalystClient().getSSIDCountBySite(**{'siteId': siteId})

@register('deviceLicenseSummary')
def deviceLicenseSummary(limit: float, order: str, page_number: float, **kwargs):
    return CatalystClient().deviceLicenseSummary(**{'limit': limit, 'order': order, 'page_number': page_number, **kwargs})

@register('complianceDetailsOfDevice')
def complianceDetailsOfDevice(deviceUuid: str, **kwargs):
    return CatalystClient().complianceDetailsOfDevice(**{'deviceUuid': deviceUuid, **kwargs})

@register('retrievesTheCountOfSitesThatTheGivenNetworkProfileForSitesIsAssignedTo')
def retrievesTheCountOfSitesThatTheGivenNetworkProfileForSitesIsAssignedTo(profileId: str):
    return CatalystClient().retrievesTheCountOfSitesThatTheGivenNetworkProfileForSitesIsAssignedTo(**{'profileId': profileId})

@register('getProvisionedDevices')
def getProvisionedDevices(**kwargs):
    return CatalystClient().getProvisionedDevices(**{**kwargs})

@register('retrievesAllPreviousPathtracesSummary')
def retrievesAllPreviousPathtracesSummary(**kwargs):
    return CatalystClient().retrievesAllPreviousPathtracesSummary(**{**kwargs})

@register('inventoryInsightDeviceLinkMismatchAPI')
def inventoryInsightDeviceLinkMismatchAPI(category: str, siteId: str, **kwargs):
    return CatalystClient().inventoryInsightDeviceLinkMismatchAPI(**{'category': category, 'siteId': siteId, **kwargs})

@register('getTheDeviceDataForTheGivenDeviceId(Uuid)')
def getTheDeviceDataForTheGivenDeviceId_Uuid_(id: str, **kwargs):
    return CatalystClient().getTheDeviceDataForTheGivenDeviceId_Uuid_(**{'id': id, **kwargs})

@register('lANAutomationLogById')
def lANAutomationLogById(id: str):
    return CatalystClient().lANAutomationLogById(**{'id': id})

@register('getDeviceCredentialSettingsForASite')
def getDeviceCredentialSettingsForASite(id: str, **kwargs):
    return CatalystClient().getDeviceCredentialSettingsForASite(**{'id': id, **kwargs})

@register('getDeviceInterfaceCount')
def getDeviceInterfaceCount(deviceId: str):
    return CatalystClient().getDeviceInterfaceCount(**{'deviceId': deviceId})

@register('ciscoDNACenterReleaseSummary')
def ciscoDNACenterReleaseSummary():
    return CatalystClient().ciscoDNACenterReleaseSummary(**{})

@register('getLayer2VirtualNetworkCount')
def getLayer2VirtualNetworkCount(**kwargs):
    return CatalystClient().getLayer2VirtualNetworkCount(**{**kwargs})

@register('retrievesTheCountOfNetworkProfilesForSites')
def retrievesTheCountOfNetworkProfilesForSites(**kwargs):
    return CatalystClient().retrievesTheCountOfNetworkProfilesForSites(**{**kwargs})

@register('getDeviceCount')
def getDeviceCount(**kwargs):
    return CatalystClient().getDeviceCount(**{**kwargs})

@register('getFabricDevicesLayer2Handoffs')
def getFabricDevicesLayer2Handoffs(fabricId: str, **kwargs):
    return CatalystClient().getFabricDevicesLayer2Handoffs(**{'fabricId': fabricId, **kwargs})

@register('getSyslogEventSubscriptions')
def getSyslogEventSubscriptions(**kwargs):
    return CatalystClient().getSyslogEventSubscriptions(**{**kwargs})

@register('getVLANDetails')
def getVLANDetails():
    return CatalystClient().getVLANDetails(**{})

@register('getAllMobilityGroups	')
def getAllMobilityGroups_(**kwargs):
    return CatalystClient().getAllMobilityGroups_(**{**kwargs})

@register('getSiteV2')
def getSiteV2(**kwargs):
    return CatalystClient().getSiteV2(**{**kwargs})

@register('systemHealthAPI')
def systemHealthAPI(**kwargs):
    return CatalystClient().systemHealthAPI(**{**kwargs})

@register('lANAutomationStatusById')
def lANAutomationStatusById(id: str):
    return CatalystClient().lANAutomationStatusById(**{'id': id})

@register('getApplication/s')
def getApplication_s(attributes: str, limit: float, offset: float, **kwargs):
    return CatalystClient().getApplication_s(**{'attributes': attributes, 'limit': limit, 'offset': offset, **kwargs})

@register('getFabricDevices')
def getFabricDevices(fabricId: str, **kwargs):
    return CatalystClient().getFabricDevices(**{'fabricId': fabricId, **kwargs})

@register('get802.11beProfileByID')
def get802_11beProfileByID(id: str):
    return CatalystClient().get802_11beProfileByID(**{'id': id})

@register('getTasksCount')
def getTasksCount(**kwargs):
    return CatalystClient().getTasksCount(**{**kwargs})

@register('getsAFloor')
def getsAFloor(id: str, **kwargs):
    return CatalystClient().getsAFloor(**{'id': id, **kwargs})

@register('getUsersAPI')
def getUsersAPI(invokeSource: str, **kwargs):
    return CatalystClient().getUsersAPI(**{'invokeSource': invokeSource, **kwargs})

@register('getFabricZones')
def getFabricZones(**kwargs):
    return CatalystClient().getFabricZones(**{**kwargs})

@register('getVirtualAccountList')
def getVirtualAccountList(domain: str):
    return CatalystClient().getVirtualAccountList(**{'domain': domain})

@register('getQosDeviceInterfaceInfoCount')
def getQosDeviceInterfaceInfoCount():
    return CatalystClient().getQosDeviceInterfaceInfoCount(**{})

@register('countOfEvents')
def countOfEvents(tags: str, **kwargs):
    return CatalystClient().countOfEvents(**{'tags': tags, **kwargs})

@register('getOSPFInterfaces')
def getOSPFInterfaces():
    return CatalystClient().getOSPFInterfaces(**{})

@register('getNetworkDeviceImageUpdates')
def getNetworkDeviceImageUpdates(**kwargs):
    return CatalystClient().getNetworkDeviceImageUpdates(**{**kwargs})

@register('getTransitNetworks')
def getTransitNetworks(**kwargs):
    return CatalystClient().getTransitNetworks(**{**kwargs})

@register('getStackDetailsForDevice')
def getStackDetailsForDevice(deviceId: str):
    return CatalystClient().getStackDetailsForDevice(**{'deviceId': deviceId})

@register('getApplicationSetCount')
def getApplicationSetCount(scalableGroupType: str):
    return CatalystClient().getApplicationSetCount(**{'scalableGroupType': scalableGroupType})

@register('getWorkflowCount')
def getWorkflowCount(**kwargs):
    return CatalystClient().getWorkflowCount(**{**kwargs})

@register('deviceComplianceStatus')
def deviceComplianceStatus(deviceUuid: str):
    return CatalystClient().deviceComplianceStatus(**{'deviceUuid': deviceUuid})

@register('retrievesPreviousPathtrace')
def retrievesPreviousPathtrace(flowAnalysisId: str):
    return CatalystClient().retrievesPreviousPathtrace(**{'flowAnalysisId': flowAnalysisId})

@register('getOverallNetworkHealth')
def getOverallNetworkHealth(**kwargs):
    return CatalystClient().getOverallNetworkHealth(**{**kwargs})

@register('getPnPGlobalSettings')
def getPnPGlobalSettings():
    return CatalystClient().getPnPGlobalSettings(**{})

@register('getServiceProviderDetailsV2')
def getServiceProviderDetailsV2():
    return CatalystClient().getServiceProviderDetailsV2(**{})

@register('getWirelessProfiles')
def getWirelessProfiles(**kwargs):
    return CatalystClient().getWirelessProfiles(**{**kwargs})

@register('getConfigTaskDetails')
def getConfigTaskDetails(parentTaskId: str):
    return CatalystClient().getConfigTaskDetails(**{'parentTaskId': parentTaskId})

@register('retrieveTheCountOfNetworkDevicesThatAreAssociatedWithAtLeastOneTag.')
def retrieveTheCountOfNetworkDevicesThatAreAssociatedWithAtLeastOneTag_():
    return CatalystClient().retrieveTheCountOfNetworkDevicesThatAreAssociatedWithAtLeastOneTag_(**{})

@register('getMulticastVirtualNetworkCount')
def getMulticastVirtualNetworkCount(**kwargs):
    return CatalystClient().getMulticastVirtualNetworkCount(**{**kwargs})

@register('getTagCount')
def getTagCount(**kwargs):
    return CatalystClient().getTagCount(**{**kwargs})

@register('getDeviceSummary')
def getDeviceSummary(id: str):
    return CatalystClient().getDeviceSummary(**{'id': id})

@register('getAuthenticationProfiles')
def getAuthenticationProfiles(**kwargs):
    return CatalystClient().getAuthenticationProfiles(**{**kwargs})

@register('getAllFlexibleReportSchedules')
def getAllFlexibleReportSchedules(Content_Type: str):
    return CatalystClient().getAllFlexibleReportSchedules(**{'Content-Type': Content_Type})

@register('virtualAccountDetails')
def virtualAccountDetails(smart_account_id: str):
    return CatalystClient().virtualAccountDetails(**{'smart_account_id': smart_account_id})

@register('getFunctionalCapabilityById')
def getFunctionalCapabilityById(id: str):
    return CatalystClient().getFunctionalCapabilityById(**{'id': id})

@register('getFabricSites')
def getFabricSites(**kwargs):
    return CatalystClient().getFabricSites(**{**kwargs})

@register('getWorkflows')
def getWorkflows(**kwargs):
    return CatalystClient().getWorkflows(**{**kwargs})

@register('getDeviceConfigById')
def getDeviceConfigById(networkDeviceId: str):
    return CatalystClient().getDeviceConfigById(**{'networkDeviceId': networkDeviceId})

@register('retrievesSpecificClientInformationMatchingTheMACAddress.')
def retrievesSpecificClientInformationMatchingTheMACAddress_(id: str, **kwargs):
    return CatalystClient().retrievesSpecificClientInformationMatchingTheMACAddress_(**{'id': id, **kwargs})

@register('getOrganizationListForMeraki')
def getOrganizationListForMeraki(id: str):
    return CatalystClient().getOrganizationListForMeraki(**{'id': id})

@register('getPollingIntervalById')
def getPollingIntervalById(id: str):
    return CatalystClient().getPollingIntervalById(**{'id': id})

@register('getNotifications')
def getNotifications(**kwargs):
    return CatalystClient().getNotifications(**{**kwargs})

@register('getAllTheDetailsAndSuggestedActionsOfAnIssueForTheGivenIssueId')
def getAllTheDetailsAndSuggestedActionsOfAnIssueForTheGivenIssueId(id: str, **kwargs):
    return CatalystClient().getAllTheDetailsAndSuggestedActionsOfAnIssueForTheGivenIssueId(**{'id': id, **kwargs})

@register('legitOperationsForInterface')
def legitOperationsForInterface(interfaceUuid: str):
    return CatalystClient().legitOperationsForInterface(**{'interfaceUuid': interfaceUuid})

@register('getDeviceConfigCount')
def getDeviceConfigCount():
    return CatalystClient().getDeviceConfigCount(**{})

@register('getISISInterfaces')
def getISISInterfaces():
    return CatalystClient().getISISInterfaces(**{})

@register('retrieveANetworkProfileForSitesById')
def retrieveANetworkProfileForSitesById(id: str):
    return CatalystClient().retrieveANetworkProfileForSitesById(**{'id': id})

@register('getAuditLogRecords')
def getAuditLogRecords(**kwargs):
    return CatalystClient().getAuditLogRecords(**{**kwargs})

@register('systemPerformanceHistoricalAPI')
def systemPerformanceHistoricalAPI(**kwargs):
    return CatalystClient().systemPerformanceHistoricalAPI(**{**kwargs})

@register('getSupervisorCardDetail')
def getSupervisorCardDetail(deviceUuid: str):
    return CatalystClient().getSupervisorCardDetail(**{'deviceUuid': deviceUuid})

@register('retrieveImageDistributionSettingsForASite')
def retrieveImageDistributionSettingsForASite(id: str, **kwargs):
    return CatalystClient().retrieveImageDistributionSettingsForASite(**{'id': id, **kwargs})

@register('getSSIDDetailsForSpecificWirelessController')
def getSSIDDetailsForSpecificWirelessController(networkDeviceId: str, **kwargs):
    return CatalystClient().getSSIDDetailsForSpecificWirelessController(**{'networkDeviceId': networkDeviceId, **kwargs})

@register('getsDetailsOfAGivenTemplate')
def getsDetailsOfAGivenTemplate(templateId: str, **kwargs):
    return CatalystClient().getsDetailsOfAGivenTemplate(**{'templateId': templateId, **kwargs})

@register('getEventArtifacts')
def getEventArtifacts(**kwargs):
    return CatalystClient().getEventArtifacts(**{**kwargs})

@register('getsTheDetailsOfAGivenProject.')
def getsTheDetailsOfAGivenProject_(projectId: str):
    return CatalystClient().getsTheDetailsOfAGivenProject_(**{'projectId': projectId})

@register('retrievesValidationWorkflowDetails')
def retrievesValidationWorkflowDetails(id: str):
    return CatalystClient().retrievesValidationWorkflowDetails(**{'id': id})

@register('getModuleCount')
def getModuleCount(deviceId: str, **kwargs):
    return CatalystClient().getModuleCount(**{'deviceId': deviceId, **kwargs})

@register('getTransitNetworksCount')
def getTransitNetworksCount(**kwargs):
    return CatalystClient().getTransitNetworksCount(**{**kwargs})

@register('returnsAllTheFabricSitesThatHaveVLANToSSIDMapping.')
def returnsAllTheFabricSitesThatHaveVLANToSSIDMapping_(**kwargs):
    return CatalystClient().returnsAllTheFabricSitesThatHaveVLANToSSIDMapping_(**{**kwargs})

@register('deviceCountDetails')
def deviceCountDetails(**kwargs):
    return CatalystClient().deviceCountDetails(**{**kwargs})

@register('getAllExecutionDetailsForAGivenReport')
def getAllExecutionDetailsForAGivenReport(reportId: str):
    return CatalystClient().getAllExecutionDetailsForAGivenReport(**{'reportId': reportId})

@register('getRest/WebhookEventSubscriptions')
def getRest_WebhookEventSubscriptions(**kwargs):
    return CatalystClient().getRest_WebhookEventSubscriptions(**{**kwargs})

@register('getRolesAPI')
def getRolesAPI(invokeSource: str):
    return CatalystClient().getRolesAPI(**{'invokeSource': invokeSource})

@register('getGoldenTagStatusOfAnImage.')
def getGoldenTagStatusOfAnImage_(Accept: str, deviceFamilyIdentifier: str, deviceRole: str, imageId: str, siteId: str):
    return CatalystClient().getGoldenTagStatusOfAnImage_(**{'Accept': Accept, 'deviceFamilyIdentifier': deviceFamilyIdentifier, 'deviceRole': deviceRole, 'imageId': imageId, 'siteId': siteId})

@register('getPortChannelCount')
def getPortChannelCount(**kwargs):
    return CatalystClient().getPortChannelCount(**{**kwargs})

@register('mapsSupportedAccessPoints')
def mapsSupportedAccessPoints():
    return CatalystClient().mapsSupportedAccessPoints(**{})

@register('getAuditLogParentRecords')
def getAuditLogParentRecords(**kwargs):
    return CatalystClient().getAuditLogParentRecords(**{**kwargs})

@register('retrieveDNSSettingsForASite')
def retrieveDNSSettingsForASite(id: str, **kwargs):
    return CatalystClient().retrieveDNSSettingsForASite(**{'id': id, **kwargs})

@register('getHealthScoreDefinitionForTheGivenId.')
def getHealthScoreDefinitionForTheGivenId_(id: str, **kwargs):
    return CatalystClient().getHealthScoreDefinitionForTheGivenId_(**{'id': id, **kwargs})

@register('getProject(s)Details')
def getProject_s_Details(**kwargs):
    return CatalystClient().getProject_s_Details(**{**kwargs})

@register('downloadAFileByFileId')
def downloadAFileByFileId(fileId: str):
    return CatalystClient().downloadAFileByFileId(**{'fileId': fileId})

@register('getAllHealthScoreDefinitionsForGivenFilters.')
def getAllHealthScoreDefinitionsForGivenFilters_(**kwargs):
    return CatalystClient().getAllHealthScoreDefinitionsForGivenFilters_(**{**kwargs})

@register('getEmailDestination')
def getEmailDestination():
    return CatalystClient().getEmailDestination(**{})

@register('getsInterfacesAlongWithStatisticsDataFromAllNetworkDevices.')
def getsInterfacesAlongWithStatisticsDataFromAllNetworkDevices_(**kwargs):
    return CatalystClient().getsInterfacesAlongWithStatisticsDataFromAllNetworkDevices_(**{**kwargs})

@register('retrieveLicenseSetting')
def retrieveLicenseSetting():
    return CatalystClient().retrieveLicenseSetting(**{})

@register('getTheTotalCustomIssueDefinitionsCountBasedOnTheProvidedFilters.')
def getTheTotalCustomIssueDefinitionsCountBasedOnTheProvidedFilters_(**kwargs):
    return CatalystClient().getTheTotalCustomIssueDefinitionsCountBasedOnTheProvidedFilters_(**{**kwargs})

@register('get802.11beProfilesCount')
def get802_11beProfilesCount():
    return CatalystClient().get802_11beProfilesCount(**{})

@register('getMulticast')
def getMulticast(**kwargs):
    return CatalystClient().getMulticast(**{**kwargs})

@register('getFabricDevicesCount')
def getFabricDevicesCount(fabricId: str, **kwargs):
    return CatalystClient().getFabricDevicesCount(**{'fabricId': fabricId, **kwargs})

@register('downloadFlexibleReport')
def downloadFlexibleReport(Content_Type: str, executionId: str, reportId: str):
    return CatalystClient().downloadFlexibleReport(**{'Content-Type': Content_Type, 'executionId': executionId, 'reportId': reportId})

@register('getExternalAuthenticationServersAPI')
def getExternalAuthenticationServersAPI(invokeSource: str):
    return CatalystClient().getExternalAuthenticationServersAPI(**{'invokeSource': invokeSource})

@register('getLayer3VirtualNetworksCount')
def getLayer3VirtualNetworksCount(**kwargs):
    return CatalystClient().getLayer3VirtualNetworksCount(**{**kwargs})

@register('lANAutomationStatus')
def lANAutomationStatus(**kwargs):
    return CatalystClient().lANAutomationStatus(**{**kwargs})

@register('getDevicesDiscoveredById')
def getDevicesDiscoveredById(id: str, **kwargs):
    return CatalystClient().getDevicesDiscoveredById(**{'id': id, **kwargs})

@register('getTaskById')
def getTaskById(taskId: str):
    return CatalystClient().getTaskById(**{'taskId': taskId})

@register('getPermissionsAPI')
def getPermissionsAPI():
    return CatalystClient().getPermissionsAPI(**{})

@register('getDiscoveredDevicesByRange')
def getDiscoveredDevicesByRange(id: str, recordsToReturn: int, startIndex: int, **kwargs):
    return CatalystClient().getDiscoveredDevicesByRange(**{'id': id, 'recordsToReturn': recordsToReturn, 'startIndex': startIndex, **kwargs})

@register('retrievesTheTotalCountOfClientsByApplyingBasicFiltering')
def retrievesTheTotalCountOfClientsByApplyingBasicFiltering(**kwargs):
    return CatalystClient().retrievesTheTotalCountOfClientsByApplyingBasicFiltering(**{**kwargs})

@register('pOEDetails')
def pOEDetails(deviceUuid: str):
    return CatalystClient().pOEDetails(**{'deviceUuid': deviceUuid})

@register('retrievesTheListOfNetworkDeviceProductNames')
def retrievesTheListOfNetworkDeviceProductNames(**kwargs):
    return CatalystClient().retrievesTheListOfNetworkDeviceProductNames(**{**kwargs})

@register('getAnchorManagedAPLocationsForSpecificWirelessController')
def getAnchorManagedAPLocationsForSpecificWirelessController(networkDeviceId: str, **kwargs):
    return CatalystClient().getAnchorManagedAPLocationsForSpecificWirelessController(**{'networkDeviceId': networkDeviceId, **kwargs})

@register('getConnectedDeviceDetail')
def getConnectedDeviceDetail(deviceUuid: str, interfaceUuid: str):
    return CatalystClient().getConnectedDeviceDetail(**{'deviceUuid': deviceUuid, 'interfaceUuid': interfaceUuid})

@register('getDevicesThatAreAssignedToASite')
def getDevicesThatAreAssignedToASite(id: str, memberType: str, **kwargs):
    return CatalystClient().getDevicesThatAreAssignedToASite(**{'id': id, 'memberType': memberType, **kwargs})

@register('lANAutomationLog')
def lANAutomationLog(**kwargs):
    return CatalystClient().lANAutomationLog(**{**kwargs})

@register('retrievesTheListOfNetworkProfilesThatTheGivenSiteHasBeenAssigned')
def retrievesTheListOfNetworkProfilesThatTheGivenSiteHasBeenAssigned(siteId: str, **kwargs):
    return CatalystClient().retrievesTheListOfNetworkProfilesThatTheGivenSiteHasBeenAssigned(**{'siteId': siteId, **kwargs})

@register('getDiscoveryJobsByIP')
def getDiscoveryJobsByIP(ipAddress: str, **kwargs):
    return CatalystClient().getDiscoveryJobsByIP(**{'ipAddress': ipAddress, **kwargs})

@register('getTemplate(s)Details')
def getTemplate_s_Details(**kwargs):
    return CatalystClient().getTemplate_s_Details(**{**kwargs})

@register('lANAutomationLogsForIndividualDevices')
def lANAutomationLogsForIndividualDevices(id: str, serialNumber: str, **kwargs):
    return CatalystClient().lANAutomationLogsForIndividualDevices(**{'id': id, 'serialNumber': serialNumber, **kwargs})

@register('getListOfDiscoveriesByDiscoveryId')
def getListOfDiscoveriesByDiscoveryId(id: str, **kwargs):
    return CatalystClient().getListOfDiscoveriesByDiscoveryId(**{'id': id, **kwargs})

@register('getPhysicalTopology')
def getPhysicalTopology(**kwargs):
    return CatalystClient().getPhysicalTopology(**{**kwargs})

@register('getSiteTopology')
def getSiteTopology():
    return CatalystClient().getSiteTopology(**{})

@register('getITSMIntegrationStatus')
def getITSMIntegrationStatus():
    return CatalystClient().getITSMIntegrationStatus(**{})

@register('getSecondaryManagedAPLocationsForSpecificWirelessController')
def getSecondaryManagedAPLocationsForSpecificWirelessController(networkDeviceId: str, **kwargs):
    return CatalystClient().getSecondaryManagedAPLocationsForSpecificWirelessController(**{'networkDeviceId': networkDeviceId, **kwargs})

@register('retrieveNTPSettingsForASite')
def retrieveNTPSettingsForASite(id: str, **kwargs):
    return CatalystClient().retrieveNTPSettingsForASite(**{'id': id, **kwargs})

@register('retrieveTagsAssociatedWithTheInterfaces.')
def retrieveTagsAssociatedWithTheInterfaces_(**kwargs):
    return CatalystClient().retrieveTagsAssociatedWithTheInterfaces_(**{**kwargs})

@register('countOfNetworkDeviceImageUpdates')
def countOfNetworkDeviceImageUpdates(**kwargs):
    return CatalystClient().countOfNetworkDeviceImageUpdates(**{**kwargs})

@register('returnReplacementDevicesCount')
def returnReplacementDevicesCount(**kwargs):
    return CatalystClient().returnReplacementDevicesCount(**{**kwargs})

@register('getPlannedAccessPointsForBuilding')
def getPlannedAccessPointsForBuilding(buildingId: str, **kwargs):
    return CatalystClient().getPlannedAccessPointsForBuilding(**{'buildingId': buildingId, **kwargs})

@register('getTheCountOfSystemDefinedIssueDefinitionsBasedOnProvidedFilters.')
def getTheCountOfSystemDefinedIssueDefinitionsBasedOnProvidedFilters_(**kwargs):
    return CatalystClient().getTheCountOfSystemDefinedIssueDefinitionsBasedOnProvidedFilters_(**{**kwargs})

@register('countOfNetworkProductNames')
def countOfNetworkProductNames(**kwargs):
    return CatalystClient().countOfNetworkProductNames(**{**kwargs})

@register('getAccessPointConfiguration')
def getAccessPointConfiguration(key: str):
    return CatalystClient().getAccessPointConfiguration(**{'key': key})

@register('getDeviceConfigForAllDevices')
def getDeviceConfigForAllDevices():
    return CatalystClient().getDeviceConfigForAllDevices(**{})

@register('getTopologyDetails')
def getTopologyDetails(vlanID: str):
    return CatalystClient().getTopologyDetails(**{'vlanID': vlanID})

@register('getTheDetailsOfIssuesForGivenSetOfFilters-2')
def getTheDetailsOfIssuesForGivenSetOfFilters_2(**kwargs):
    return CatalystClient().getTheDetailsOfIssuesForGivenSetOfFilters_2(**{**kwargs})

@register('smartAccountDetails')
def smartAccountDetails():
    return CatalystClient().smartAccountDetails(**{})

@register('getFabricDevicesLayer3HandoffsWithIpTransitCount')
def getFabricDevicesLayer3HandoffsWithIpTransitCount(fabricId: str, **kwargs):
    return CatalystClient().getFabricDevicesLayer3HandoffsWithIpTransitCount(**{'fabricId': fabricId, **kwargs})

@register('getFabricDevicesLayer3HandoffsWithSdaTransitCount')
def getFabricDevicesLayer3HandoffsWithSdaTransitCount(fabricId: str, **kwargs):
    return CatalystClient().getFabricDevicesLayer3HandoffsWithSdaTransitCount(**{'fabricId': fabricId, **kwargs})

@register('retrievesTheListOfNetworkProfilesForSites')
def retrievesTheListOfNetworkProfilesForSites(**kwargs):
    return CatalystClient().retrievesTheListOfNetworkProfilesForSites(**{**kwargs})

@register('getFunctionalCapabilityForDevices')
def getFunctionalCapabilityForDevices(deviceId: str, **kwargs):
    return CatalystClient().getFunctionalCapabilityForDevices(**{'deviceId': deviceId, **kwargs})

@register('getPortAssignments')
def getPortAssignments(**kwargs):
    return CatalystClient().getPortAssignments(**{**kwargs})

@register('getBusinessAPIExecutionDetails')
def getBusinessAPIExecutionDetails(executionId: str):
    return CatalystClient().getBusinessAPIExecutionDetails(**{'executionId': executionId})

@register('lANAutomationActiveSessions')
def lANAutomationActiveSessions():
    return CatalystClient().lANAutomationActiveSessions(**{})

@register('getSiteNotAssignedNetworkDevices')
def getSiteNotAssignedNetworkDevices(**kwargs):
    return CatalystClient().getSiteNotAssignedNetworkDevices(**{**kwargs})

@register('getAccessPointRebootTaskResult')
def getAccessPointRebootTaskResult(**kwargs):
    return CatalystClient().getAccessPointRebootTaskResult(**{**kwargs})

@register('getDeviceDetail')
def getDeviceDetail(identifier: str, searchBy: str, **kwargs):
    return CatalystClient().getDeviceDetail(**{'identifier': identifier, 'searchBy': searchBy, **kwargs})

@register('lANAutomationSessionCount')
def lANAutomationSessionCount():
    return CatalystClient().lANAutomationSessionCount(**{})

@register('getNetworkDeviceByIP')
def getNetworkDeviceByIP(ipAddress: str):
    return CatalystClient().getNetworkDeviceByIP(**{'ipAddress': ipAddress})

@register('getSiteNotAssignedNetworkDevicesCount')
def getSiteNotAssignedNetworkDevicesCount():
    return CatalystClient().getSiteNotAssignedNetworkDevicesCount(**{})

@register('getDeviceBySerialNumber')
def getDeviceBySerialNumber(serialNumber: str):
    return CatalystClient().getDeviceBySerialNumber(**{'serialNumber': serialNumber})

@register('getApplicationCount')
def getApplicationCount(scalableGroupType: str):
    return CatalystClient().getApplicationCount(**{'scalableGroupType': scalableGroupType})

@register('downloadReportContent')
def downloadReportContent(executionId: str, reportId: str):
    return CatalystClient().downloadReportContent(**{'executionId': executionId, 'reportId': reportId})

@register('getDeviceCount-2')
def getDeviceCount_2(**kwargs):
    return CatalystClient().getDeviceCount_2(**{**kwargs})

@register('eventArtifactCount')
def eventArtifactCount():
    return CatalystClient().eventArtifactCount(**{})

@register('getComplianceStatusCount')
def getComplianceStatusCount(**kwargs):
    return CatalystClient().getComplianceStatusCount(**{**kwargs})

@register('getTasks')
def getTasks(**kwargs):
    return CatalystClient().getTasks(**{**kwargs})

@register('getListOfChildEventsForTheGivenWirelessClientEvent')
def getListOfChildEventsForTheGivenWirelessClientEvent(id: str, **kwargs):
    return CatalystClient().getListOfChildEventsForTheGivenWirelessClientEvent(**{'id': id, **kwargs})

@register('getProvisioningSettings')
def getProvisioningSettings():
    return CatalystClient().getProvisioningSettings(**{})

@register('readSiteCount.')
def readSiteCount_(**kwargs):
    return CatalystClient().readSiteCount_(**{**kwargs})

@register('getEoXDetailsPerDevice')
def getEoXDetailsPerDevice(deviceId: str):
    return CatalystClient().getEoXDetailsPerDevice(**{'deviceId': deviceId})

@register('ciscoDNACenterNodesConfigurationSummary')
def ciscoDNACenterNodesConfigurationSummary():
    return CatalystClient().ciscoDNACenterNodesConfigurationSummary(**{})

@register('importMapArchive-ImportStatus')
def importMapArchive_ImportStatus(importContextUuid: str):
    return CatalystClient().importMapArchive_ImportStatus(**{'importContextUuid': importContextUuid})

@register('getExternalAuthenticationSettingAPI')
def getExternalAuthenticationSettingAPI():
    return CatalystClient().getExternalAuthenticationSettingAPI(**{})

@register('getInterfaceById')
def getInterfaceById(id: str):
    return CatalystClient().getInterfaceById(**{'id': id})

@register('deviceLicenseDetails')
def deviceLicenseDetails(device_uuid: str):
    return CatalystClient().deviceLicenseDetails(**{'device_uuid': device_uuid})

@register('getTheInterfaceDataForTheGivenInterfaceId(instanceUuid)AlongWithTheStatisticsData')
def getTheInterfaceDataForTheGivenInterfaceId_instanceUuid_AlongWithTheStatisticsData(id: str, **kwargs):
    return CatalystClient().getTheInterfaceDataForTheGivenInterfaceId_instanceUuid_AlongWithTheStatisticsData(**{'id': id, **kwargs})

@register('getInterfaceInfoById')
def getInterfaceInfoById(deviceId: str):
    return CatalystClient().getInterfaceInfoById(**{'deviceId': deviceId})

@register('getTaskByOperationId')
def getTaskByOperationId(limit: int, offset: int, operationId: str):
    return CatalystClient().getTaskByOperationId(**{'limit': limit, 'offset': offset, 'operationId': operationId})

@register('ciscoISEServerIntegrationStatus')
def ciscoISEServerIntegrationStatus():
    return CatalystClient().ciscoISEServerIntegrationStatus(**{})

@register('getL3TopologyDetails')
def getL3TopologyDetails(topologyType: str):
    return CatalystClient().getL3TopologyDetails(**{'topologyType': topologyType})

@register('getAdvisoryDeviceDetail')
def getAdvisoryDeviceDetail(deviceId: str):
    return CatalystClient().getAdvisoryDeviceDetail(**{'deviceId': deviceId})

@register('getConnectorTypes')
def getConnectorTypes():
    return CatalystClient().getConnectorTypes(**{})

@register('getTasksByID')
def getTasksByID(id: str):
    return CatalystClient().getTasksByID(**{'id': id})

@register('licenseTermDetails')
def licenseTermDetails(device_type: str, smart_account_id: str, virtual_account_name: str):
    return CatalystClient().licenseTermDetails(**{'device_type': device_type, 'smart_account_id': smart_account_id, 'virtual_account_name': virtual_account_name})

@register('retrieveDHCPSettingsForASite')
def retrieveDHCPSettingsForASite(id: str, **kwargs):
    return CatalystClient().retrieveDHCPSettingsForASite(**{'id': id, **kwargs})

@register('getAnycastGatewayCount')
def getAnycastGatewayCount(**kwargs):
    return CatalystClient().getAnycastGatewayCount(**{**kwargs})

@register('getsTheNetworkDeviceDetailsBasedOnTheProvidedQueryParameters.')
def getsTheNetworkDeviceDetailsBasedOnTheProvidedQueryParameters_(**kwargs):
    return CatalystClient().getsTheNetworkDeviceDetailsBasedOnTheProvidedQueryParameters_(**{**kwargs})

@register('issues')
def issues(**kwargs):
    return CatalystClient().issues(**{**kwargs})

@register('getDevicesRegisteredForWSANotification')
def getDevicesRegisteredForWSANotification(**kwargs):
    return CatalystClient().getDevicesRegisteredForWSANotification(**{**kwargs})

@register('getInterfaceByIP')
def getInterfaceByIP(ipAddress: str):
    return CatalystClient().getInterfaceByIP(**{'ipAddress': ipAddress})

@register('retrieveApplicableAdd-onImagesForTheGivenSoftwareImage')
def retrieveApplicableAdd_onImagesForTheGivenSoftwareImage(id: str):
    return CatalystClient().retrieveApplicableAdd_onImagesForTheGivenSoftwareImage(**{'id': id})

@register('retrievesTheListOfClients,WhileAlsoOfferingBasicFilteringAndSortingCapabilities.')
def retrievesTheListOfClients_WhileAlsoOfferingBasicFilteringAndSortingCapabilities_(**kwargs):
    return CatalystClient().retrievesTheListOfClients_WhileAlsoOfferingBasicFilteringAndSortingCapabilities_(**{**kwargs})

@register('getEoXSummary')
def getEoXSummary():
    return CatalystClient().getEoXSummary(**{})

@register('systemPerformanceAPI')
def systemPerformanceAPI(**kwargs):
    return CatalystClient().systemPerformanceAPI(**{**kwargs})

@register('getManagedAPLocationsCountForSpecificWirelessController')
def getManagedAPLocationsCountForSpecificWirelessController(networkDeviceId: str):
    return CatalystClient().getManagedAPLocationsCountForSpecificWirelessController(**{'networkDeviceId': networkDeviceId})

@register('getNetworkDeviceByPaginationRange')
def getNetworkDeviceByPaginationRange(recordsToReturn: int, startIndex: int):
    return CatalystClient().getNetworkDeviceByPaginationRange(**{'recordsToReturn': recordsToReturn, 'startIndex': startIndex})

@register('getSiteAssignedNetworkDevice')
def getSiteAssignedNetworkDevice(id: str):
    return CatalystClient().getSiteAssignedNetworkDevice(**{'id': id})

@register('getTheCustomIssueDefinitionForTheGivenCustomIssueDefinitionId.')
def getTheCustomIssueDefinitionForTheGivenCustomIssueDefinitionId_(id: str, **kwargs):
    return CatalystClient().getTheCustomIssueDefinitionForTheGivenCustomIssueDefinitionId_(**{'id': id, **kwargs})

@register('getAllInterfaces')
def getAllInterfaces(**kwargs):
    return CatalystClient().getAllInterfaces(**{**kwargs})

@register('returnsCountOfAdd-onImages')
def returnsCountOfAdd_onImages(id: str):
    return CatalystClient().returnsCountOfAdd_onImages(**{'id': id})

@register('getWirelessLanControllerDetailsById')
def getWirelessLanControllerDetailsById(id: str):
    return CatalystClient().getWirelessLanControllerDetailsById(**{'id': id})

@register('ciscoDNACenterPackagesSummary')
def ciscoDNACenterPackagesSummary():
    return CatalystClient().ciscoDNACenterPackagesSummary(**{})

@register('getRFProfilesCount')
def getRFProfilesCount():
    return CatalystClient().getRFProfilesCount(**{})

@register('getDevicesPerAdvisory')
def getDevicesPerAdvisory(advisoryId: str):
    return CatalystClient().getDevicesPerAdvisory(**{'advisoryId': advisoryId})

@register('getAccessPointConfigurationTaskResult')
def getAccessPointConfigurationTaskResult(task_id: str):
    return CatalystClient().getAccessPointConfigurationTaskResult(**{'task_id': task_id})

@register('getComplianceDetail')
def getComplianceDetail(**kwargs):
    return CatalystClient().getComplianceDetail(**{**kwargs})

@register('returnsTheCountOfVLANsMappedToSSIDsInAFabricSite.')
def returnsTheCountOfVLANsMappedToSSIDsInAFabricSite_(Content_Type: str, fabricId: str):
    return CatalystClient().returnsTheCountOfVLANsMappedToSSIDsInAFabricSite_(**{'Content-Type': Content_Type, 'fabricId': fabricId})

@register('getGlobalCredentials')
def getGlobalCredentials(credentialSubType: str, **kwargs):
    return CatalystClient().getGlobalCredentials(**{'credentialSubType': credentialSubType, **kwargs})

@register('getComplianceStatus')
def getComplianceStatus(**kwargs):
    return CatalystClient().getComplianceStatus(**{**kwargs})

@register('getSNMPDestination')
def getSNMPDestination(**kwargs):
    return CatalystClient().getSNMPDestination(**{**kwargs})

@register('getProvisionedDevicesCount')
def getProvisionedDevicesCount(**kwargs):
    return CatalystClient().getProvisionedDevicesCount(**{**kwargs})

@register('returnsListOfSoftwareImages')
def returnsListOfSoftwareImages(**kwargs):
    return CatalystClient().returnsListOfSoftwareImages(**{**kwargs})

@register('getInterfacesCount')
def getInterfacesCount():
    return CatalystClient().getInterfacesCount(**{})

@register('readListOfSiteHealthSummaries.')
def readListOfSiteHealthSummaries_(**kwargs):
    return CatalystClient().readListOfSiteHealthSummaries_(**{**kwargs})

@register('getDeviceList-2')
def getDeviceList_2(**kwargs):
    return CatalystClient().getDeviceList_2(**{**kwargs})

@register('getTasks-2')
def getTasks_2(**kwargs):
    return CatalystClient().getTasks_2(**{**kwargs})

@register('getModules')
def getModules(deviceId: str, **kwargs):
    return CatalystClient().getModules(**{'deviceId': deviceId, **kwargs})

@register('retrievesTheCountOfAssignedNetworkDeviceProducts')
def retrievesTheCountOfAssignedNetworkDeviceProducts(imageId: str, **kwargs):
    return CatalystClient().retrievesTheCountOfAssignedNetworkDeviceProducts(**{'imageId': imageId, **kwargs})

@register('getRest/WebhookSubscriptionDetails')
def getRest_WebhookSubscriptionDetails(**kwargs):
    return CatalystClient().getRest_WebhookSubscriptionDetails(**{**kwargs})

@register('getDeviceHistory')
def getDeviceHistory(serialNumber: str, **kwargs):
    return CatalystClient().getDeviceHistory(**{'serialNumber': serialNumber, **kwargs})

@register('getApplicationPolicyQueuingProfileCount')
def getApplicationPolicyQueuingProfileCount():
    return CatalystClient().getApplicationPolicyQueuingProfileCount(**{})

@register('getsTheTotalNetworkDeviceCountsBasedOnTheProvidedQueryParameters.')
def getsTheTotalNetworkDeviceCountsBasedOnTheProvidedQueryParameters_(**kwargs):
    return CatalystClient().getsTheTotalNetworkDeviceCountsBasedOnTheProvidedQueryParameters_(**{**kwargs})

@register('getTaskTree')
def getTaskTree(taskId: str):
    return CatalystClient().getTaskTree(**{'taskId': taskId})

@register('getDiscoveredNetworkDevicesByDiscoveryId')
def getDiscoveredNetworkDevicesByDiscoveryId(id: str, **kwargs):
    return CatalystClient().getDiscoveredNetworkDevicesByDiscoveryId(**{'id': id, **kwargs})

@register('getStatusAPIForEvents')
def getStatusAPIForEvents(executionId: str):
    return CatalystClient().getStatusAPIForEvents(**{'executionId': executionId})

@register('getSiteAssignedNetworkDevicesCount')
def getSiteAssignedNetworkDevicesCount(siteId: str):
    return CatalystClient().getSiteAssignedNetworkDevicesCount(**{'siteId': siteId})

@register('getNetworkV2')
def getNetworkV2(siteId: str):
    return CatalystClient().getNetworkV2(**{'siteId': siteId})

@register('getDeviceValuesThatMatchFullyOrPartiallyAnAttribute')
def getDeviceValuesThatMatchFullyOrPartiallyAnAttribute(**kwargs):
    return CatalystClient().getDeviceValuesThatMatchFullyOrPartiallyAnAttribute(**{**kwargs})

@register('sensors')
def sensors(**kwargs):
    return CatalystClient().sensors(**{**kwargs})

@register('getDeviceInfoFromSDAFabric')
def getDeviceInfoFromSDAFabric(deviceManagementIpAddress: str):
    return CatalystClient().getDeviceInfoFromSDAFabric(**{'deviceManagementIpAddress': deviceManagementIpAddress})

@register('getPortAssignmentForAccessPointInSDAFabric')
def getPortAssignmentForAccessPointInSDAFabric(deviceManagementIpAddress: str, interfaceName: str):
    return CatalystClient().getPortAssignmentForAccessPointInSDAFabric(**{'deviceManagementIpAddress': deviceManagementIpAddress, 'interfaceName': interfaceName})

@register('getIPPoolFromSDAVirtualNetwork')
def getIPPoolFromSDAVirtualNetwork(ipPoolName: str, siteNameHierarchy: str, virtualNetworkName: str):
    return CatalystClient().getIPPoolFromSDAVirtualNetwork(**{'ipPoolName': ipPoolName, 'siteNameHierarchy': siteNameHierarchy, 'virtualNetworkName': virtualNetworkName})

@register('getEdgeDeviceFromSDAFabric')
def getEdgeDeviceFromSDAFabric(deviceManagementIpAddress: str):
    return CatalystClient().getEdgeDeviceFromSDAFabric(**{'deviceManagementIpAddress': deviceManagementIpAddress})

@register('getMulticastDetailsFromSDAFabric')
def getMulticastDetailsFromSDAFabric(siteNameHierarchy: str):
    return CatalystClient().getMulticastDetailsFromSDAFabric(**{'siteNameHierarchy': siteNameHierarchy})

@register('getApplications')
def getApplications(**kwargs):
    return CatalystClient().getApplications(**{**kwargs})

@register('retrieveRFProfiles')
def retrieveRFProfiles(**kwargs):
    return CatalystClient().retrieveRFProfiles(**{**kwargs})

@register('getNetwork')
def getNetwork(**kwargs):
    return CatalystClient().getNetwork(**{**kwargs})

@register('getReserveIPSubpool')
def getReserveIPSubpool(**kwargs):
    return CatalystClient().getReserveIPSubpool(**{**kwargs})

@register('getTransitPeerNetworkInfo')
def getTransitPeerNetworkInfo(transitPeerNetworkName: str):
    return CatalystClient().getTransitPeerNetworkInfo(**{'transitPeerNetworkName': transitPeerNetworkName})

@register('clientProximity')
def clientProximity(username: str, **kwargs):
    return CatalystClient().clientProximity(**{'username': username, **kwargs})

@register('applications')
def applications(**kwargs):
    return CatalystClient().applications(**{**kwargs})

@register('getApplicationSets')
def getApplicationSets(**kwargs):
    return CatalystClient().getApplicationSets(**{**kwargs})

@register('getApplicationsCount')
def getApplicationsCount():
    return CatalystClient().getApplicationsCount(**{})

@register('getGlobalPool')
def getGlobalPool(**kwargs):
    return CatalystClient().getGlobalPool(**{**kwargs})

@register('getVNFromSDAFabric')
def getVNFromSDAFabric(siteNameHierarchy: str, virtualNetworkName: str):
    return CatalystClient().getVNFromSDAFabric(**{'siteNameHierarchy': siteNameHierarchy, 'virtualNetworkName': virtualNetworkName})

@register('getDefaultAuthenticationProfileFromSDAFabric')
def getDefaultAuthenticationProfileFromSDAFabric(siteNameHierarchy: str, **kwargs):
    return CatalystClient().getDefaultAuthenticationProfileFromSDAFabric(**{'siteNameHierarchy': siteNameHierarchy, **kwargs})

@register('getProvisionedWiredDevice')
def getProvisionedWiredDevice(deviceManagementIpAddress: str):
    return CatalystClient().getProvisionedWiredDevice(**{'deviceManagementIpAddress': deviceManagementIpAddress})

@register('getDeviceCredentialDetails')
def getDeviceCredentialDetails(**kwargs):
    return CatalystClient().getDeviceCredentialDetails(**{**kwargs})

@register('getSiteFromSDAFabric')
def getSiteFromSDAFabric(siteNameHierarchy: str):
    return CatalystClient().getSiteFromSDAFabric(**{'siteNameHierarchy': siteNameHierarchy})

@register('getServiceProviderDetails')
def getServiceProviderDetails():
    return CatalystClient().getServiceProviderDetails(**{})

@register('getSite')
def getSite(**kwargs):
    return CatalystClient().getSite(**{**kwargs})

@register('getVirtualNetworkSummary')
def getVirtualNetworkSummary(siteNameHierarchy: str):
    return CatalystClient().getVirtualNetworkSummary(**{'siteNameHierarchy': siteNameHierarchy})

@register('getWirelessProfile')
def getWirelessProfile(**kwargs):
    return CatalystClient().getWirelessProfile(**{**kwargs})

@register('getIssueEnrichmentDetails')
def getIssueEnrichmentDetails(entity_type: str, entity_value: str, **kwargs):
    return CatalystClient().getIssueEnrichmentDetails(**{'entity_type': entity_type, 'entity_value': entity_value, **kwargs})

@register('sensorTestResults')
def sensorTestResults(**kwargs):
    return CatalystClient().sensorTestResults(**{**kwargs})

@register('getDeviceRoleInSDAFabric')
def getDeviceRoleInSDAFabric(deviceManagementIpAddress: str):
    return CatalystClient().getDeviceRoleInSDAFabric(**{'deviceManagementIpAddress': deviceManagementIpAddress})

@register('getEnterpriseSSID')
def getEnterpriseSSID(**kwargs):
    return CatalystClient().getEnterpriseSSID(**{**kwargs})

@register('getBorderDeviceDetailFromSDAFabric')
def getBorderDeviceDetailFromSDAFabric(deviceManagementIpAddress: str):
    return CatalystClient().getBorderDeviceDetailFromSDAFabric(**{'deviceManagementIpAddress': deviceManagementIpAddress})

@register('getPortAssignmentForUserDeviceInSDAFabric')
def getPortAssignmentForUserDeviceInSDAFabric(deviceManagementIpAddress: str, interfaceName: str):
    return CatalystClient().getPortAssignmentForUserDeviceInSDAFabric(**{'deviceManagementIpAddress': deviceManagementIpAddress, 'interfaceName': interfaceName})

@register('getFailedITSMEvents')
def getFailedITSMEvents(**kwargs):
    return CatalystClient().getFailedITSMEvents(**{**kwargs})

@register('getSSIDToIPPoolMapping')
def getSSIDToIPPoolMapping(siteNameHierarchy: str, vlanName: str):
    return CatalystClient().getSSIDToIPPoolMapping(**{'siteNameHierarchy': siteNameHierarchy, 'vlanName': vlanName})

@register('getControlPlaneDeviceFromSDAFabric')
def getControlPlaneDeviceFromSDAFabric(deviceManagementIpAddress: str):
    return CatalystClient().getControlPlaneDeviceFromSDAFabric(**{'deviceManagementIpAddress': deviceManagementIpAddress})

@register('getCMDBSyncStatus')
def getCMDBSyncStatus(**kwargs):
    return CatalystClient().getCMDBSyncStatus(**{**kwargs})

@register('getSiteCount')
def getSiteCount(**kwargs):
    return CatalystClient().getSiteCount(**{**kwargs})

@register('getClientEnrichmentDetails')
def getClientEnrichmentDetails(entity_type: str, entity_value: str, **kwargs):
    return CatalystClient().getClientEnrichmentDetails(**{'entity_type': entity_type, 'entity_value': entity_value, **kwargs})

@register('getVirtualNetworkWithScalableGroups')
def getVirtualNetworkWithScalableGroups(virtualNetworkName: str):
    return CatalystClient().getVirtualNetworkWithScalableGroups(**{'virtualNetworkName': virtualNetworkName})

@register('getDynamicInterface')
def getDynamicInterface(**kwargs):
    return CatalystClient().getDynamicInterface(**{**kwargs})

@register('getApplicationSetsCount')
def getApplicationSetsCount():
    return CatalystClient().getApplicationSetsCount(**{})

@register('getUserEnrichmentDetails')
def getUserEnrichmentDetails(entity_type: str, entity_value: str, **kwargs):
    return CatalystClient().getUserEnrichmentDetails(**{'entity_type': entity_type, 'entity_value': entity_value, **kwargs})

@register('getDeviceEnrichmentDetails')
def getDeviceEnrichmentDetails(entity_type: str, entity_value: str, **kwargs):
    return CatalystClient().getDeviceEnrichmentDetails(**{'entity_type': entity_type, 'entity_value': entity_value, **kwargs})

@register('getMembership')
def getMembership(siteId: str, **kwargs):
    return CatalystClient().getMembership(**{'siteId': siteId, **kwargs})
