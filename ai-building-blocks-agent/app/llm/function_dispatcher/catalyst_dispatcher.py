# app/llm/function_dispatcher/catalyst_dispatcher.py
from app.llm.function_dispatcher import register
from app.llm.platform_clients.catalyst_client import CatalystClient

@register('retrievesNetworkDeviceProductNamesAssignedToASoftwareImage.')
def retrievesNetworkDeviceProductNamesAssignedToASoftwareImage_(**kwargs):
    return CatalystClient().retrievesNetworkDeviceProductNamesAssignedToASoftwareImage_(**kwargs)

@register('getsAllTheVersionsOfAGivenTemplate')
def getsAllTheVersionsOfAGivenTemplate(**kwargs):
    return CatalystClient().getsAllTheVersionsOfAGivenTemplate(**kwargs)

@register('returnsTheCountOfNetworkDeviceProductNamesForASite')
def returnsTheCountOfNetworkDeviceProductNamesForASite(**kwargs):
    return CatalystClient().returnsTheCountOfNetworkDeviceProductNamesForASite(**kwargs)

@register('getMulticastVirtualNetworks')
def getMulticastVirtualNetworks(**kwargs):
    return CatalystClient().getMulticastVirtualNetworks(**kwargs)

@register('getDeviceControllabilitySettings')
def getDeviceControllabilitySettings(**kwargs):
    return CatalystClient().getDeviceControllabilitySettings(**kwargs)

@register('getChassisDetailsForDevice')
def getChassisDetailsForDevice(**kwargs):
    return CatalystClient().getChassisDetailsForDevice(**kwargs)

@register('getsABuilding')
def getsABuilding(**kwargs):
    return CatalystClient().getsABuilding(**kwargs)

@register('getCountOfAllDiscoveryJobs')
def getCountOfAllDiscoveryJobs(**kwargs):
    return CatalystClient().getCountOfAllDiscoveryJobs(**kwargs)

@register('getViewsForAGivenViewGroup')
def getViewsForAGivenViewGroup(**kwargs):
    return CatalystClient().getViewsForAGivenViewGroup(**kwargs)

@register('getDeviceById')
def getDeviceById(**kwargs):
    return CatalystClient().getDeviceById(**kwargs)

@register('retrieveTheVLANsAndSSIDsMappedToTheVLANWithinAFabricSite.')
def retrieveTheVLANsAndSSIDsMappedToTheVLANWithinAFabricSite_(**kwargs):
    return CatalystClient().retrieveTheVLANsAndSSIDsMappedToTheVLANWithinAFabricSite_(**kwargs)

@register('retrieveImageDistributionServers')
def retrieveImageDistributionServers(**kwargs):
    return CatalystClient().retrieveImageDistributionServers(**kwargs)

@register('retrieveTagsAssociatedWithNetworkDevices.')
def retrieveTagsAssociatedWithNetworkDevices_(**kwargs):
    return CatalystClient().retrieveTagsAssociatedWithNetworkDevices_(**kwargs)

@register('statusOfTemplateDeployment')
def statusOfTemplateDeployment(**kwargs):
    return CatalystClient().statusOfTemplateDeployment(**kwargs)

@register('getIssueTriggerDefinitionForGivenId.')
def getIssueTriggerDefinitionForGivenId_(**kwargs):
    return CatalystClient().getIssueTriggerDefinitionForGivenId_(**kwargs)

@register('retrieveBannerSettingsForASite')
def retrieveBannerSettingsForASite(**kwargs):
    return CatalystClient().retrieveBannerSettingsForASite(**kwargs)

@register('getSiteAssignedNetworkDevices')
def getSiteAssignedNetworkDevices(**kwargs):
    return CatalystClient().getSiteAssignedNetworkDevices(**kwargs)

@register('getNetworkDevicesCredentialsSyncStatus')
def getNetworkDevicesCredentialsSyncStatus(**kwargs):
    return CatalystClient().getNetworkDevicesCredentialsSyncStatus(**kwargs)

@register('getSoftwareImageDetails')
def getSoftwareImageDetails(**kwargs):
    return CatalystClient().getSoftwareImageDetails(**kwargs)

@register('getInterfaceByID')
def getInterfaceByID(**kwargs):
    return CatalystClient().getInterfaceByID(**kwargs)

@register('getAnycastGateways')
def getAnycastGateways(**kwargs):
    return CatalystClient().getAnycastGateways(**kwargs)

@register('getApplicationSet/s')
def getApplicationSet_s(**kwargs):
    return CatalystClient().getApplicationSet_s(**kwargs)

@register('getTagMembersById')
def getTagMembersById(**kwargs):
    return CatalystClient().getTagMembersById(**kwargs)

@register('getFabricSiteCount')
def getFabricSiteCount(**kwargs):
    return CatalystClient().getFabricSiteCount(**kwargs)

@register('retrievesAllTheValidationSets')
def retrievesAllTheValidationSets(**kwargs):
    return CatalystClient().retrievesAllTheValidationSets(**kwargs)

@register('retrievesTheListOfSitesThatTheGivenNetworkProfileForSitesIsAssignedTo')
def retrievesTheListOfSitesThatTheGivenNetworkProfileForSitesIsAssignedTo(**kwargs):
    return CatalystClient().retrievesTheListOfSitesThatTheGivenNetworkProfileForSitesIsAssignedTo(**kwargs)

@register('getFabricDevicesLayer2HandoffsCount')
def getFabricDevicesLayer2HandoffsCount(**kwargs):
    return CatalystClient().getFabricDevicesLayer2HandoffsCount(**kwargs)

@register('countOfEventSubscriptions')
def countOfEventSubscriptions(**kwargs):
    return CatalystClient().countOfEventSubscriptions(**kwargs)

@register('getSSIDBySite')
def getSSIDBySite(**kwargs):
    return CatalystClient().getSSIDBySite(**kwargs)

@register('getITSMIntegrationSettingById')
def getITSMIntegrationSettingById(**kwargs):
    return CatalystClient().getITSMIntegrationSettingById(**kwargs)

@register('getDetailsOfASingleAssuranceEvent')
def getDetailsOfASingleAssuranceEvent(**kwargs):
    return CatalystClient().getDetailsOfASingleAssuranceEvent(**kwargs)

@register('getRFProfiles')
def getRFProfiles(**kwargs):
    return CatalystClient().getRFProfiles(**kwargs)

@register('retrieveTelemetrySettingsForASite')
def retrieveTelemetrySettingsForASite(**kwargs):
    return CatalystClient().retrieveTelemetrySettingsForASite(**kwargs)

@register('getAllUser-Defined-Fields')
def getAllUser_Defined_Fields(**kwargs):
    return CatalystClient().getAllUser_Defined_Fields(**kwargs)

@register('queryAssuranceEvents')
def queryAssuranceEvents(**kwargs):
    return CatalystClient().queryAssuranceEvents(**kwargs)

@register('getFloorSettings')
def getFloorSettings(**kwargs):
    return CatalystClient().getFloorSettings(**kwargs)

@register('getTheTotalNumberOfIssuesForGivenSetOfFilters')
def getTheTotalNumberOfIssuesForGivenSetOfFilters(**kwargs):
    return CatalystClient().getTheTotalNumberOfIssuesForGivenSetOfFilters(**kwargs)

@register('getTag')
def getTag(**kwargs):
    return CatalystClient().getTag(**kwargs)

@register('getLayer2VirtualNetworks')
def getLayer2VirtualNetworks(**kwargs):
    return CatalystClient().getLayer2VirtualNetworks(**kwargs)

@register('getFabricZoneCount')
def getFabricZoneCount(**kwargs):
    return CatalystClient().getFabricZoneCount(**kwargs)

@register('getWebhookDestination')
def getWebhookDestination(**kwargs):
    return CatalystClient().getWebhookDestination(**kwargs)

@register('retrieveTimeZoneSettingsForASite')
def retrieveTimeZoneSettingsForASite(**kwargs):
    return CatalystClient().retrieveTimeZoneSettingsForASite(**kwargs)

@register('getDeviceByID')
def getDeviceByID(**kwargs):
    return CatalystClient().getDeviceByID(**kwargs)

@register('getApplicationPolicyQueuingProfile')
def getApplicationPolicyQueuingProfile(**kwargs):
    return CatalystClient().getApplicationPolicyQueuingProfile(**kwargs)

@register('getSyslogDestination')
def getSyslogDestination(**kwargs):
    return CatalystClient().getSyslogDestination(**kwargs)

@register('getAll802.11beProfiles')
def getAll802_11beProfiles(**kwargs):
    return CatalystClient().getAll802_11beProfiles(**kwargs)

@register('getSyncResultForVirtualAccount')
def getSyncResultForVirtualAccount(**kwargs):
    return CatalystClient().getSyncResultForVirtualAccount(**kwargs)

@register('getAllTheCustomIssueDefinitionsBasedOnTheGivenFilters.')
def getAllTheCustomIssueDefinitionsBasedOnTheGivenFilters_(**kwargs):
    return CatalystClient().getAllTheCustomIssueDefinitionsBasedOnTheGivenFilters_(**kwargs)

@register('getApplicationPolicyDefault')
def getApplicationPolicyDefault(**kwargs):
    return CatalystClient().getApplicationPolicyDefault(**kwargs)

@register('getPrimaryManagedAPLocationsForSpecificWirelessController')
def getPrimaryManagedAPLocationsForSpecificWirelessController(**kwargs):
    return CatalystClient().getPrimaryManagedAPLocationsForSpecificWirelessController(**kwargs)

@register('getModuleInfoById')
def getModuleInfoById(**kwargs):
    return CatalystClient().getModuleInfoById(**kwargs)

@register('getFabricDevicesLayer3HandoffsWithSdaTransit')
def getFabricDevicesLayer3HandoffsWithSdaTransit(**kwargs):
    return CatalystClient().getFabricDevicesLayer3HandoffsWithSdaTransit(**kwargs)

@register('getFabricDevicesLayer3HandoffsWithIpTransit')
def getFabricDevicesLayer3HandoffsWithIpTransit(**kwargs):
    return CatalystClient().getFabricDevicesLayer3HandoffsWithIpTransit(**kwargs)

@register('returnsNetworkDeviceProductNamesForASite')
def returnsNetworkDeviceProductNamesForASite(**kwargs):
    return CatalystClient().returnsNetworkDeviceProductNamesForASite(**kwargs)

@register('countOfNotifications')
def countOfNotifications(**kwargs):
    return CatalystClient().countOfNotifications(**kwargs)

@register('getAScheduledReport')
def getAScheduledReport(**kwargs):
    return CatalystClient().getAScheduledReport(**kwargs)

@register('getSiteHealth')
def getSiteHealth(**kwargs):
    return CatalystClient().getSiteHealth(**kwargs)

@register('returnsPOEInterfaceDetailsForTheDevice.')
def returnsPOEInterfaceDetailsForTheDevice_(**kwargs):
    return CatalystClient().returnsPOEInterfaceDetailsForTheDevice_(**kwargs)

@register('getSitesCount')
def getSitesCount(**kwargs):
    return CatalystClient().getSitesCount(**kwargs)

@register('retrievesTheListOfValidationWorkflows')
def retrievesTheListOfValidationWorkflows(**kwargs):
    return CatalystClient().retrievesTheListOfValidationWorkflows(**kwargs)

@register('readAnAggregatedSummaryOfSiteHealthData.')
def readAnAggregatedSummaryOfSiteHealthData_(**kwargs):
    return CatalystClient().readAnAggregatedSummaryOfSiteHealthData_(**kwargs)

@register('retrievesTheCountOfProfilesThatTheGivenSiteHasBeenAssigned')
def retrievesTheCountOfProfilesThatTheGivenSiteHasBeenAssigned(**kwargs):
    return CatalystClient().retrievesTheCountOfProfilesThatTheGivenSiteHasBeenAssigned(**kwargs)

@register('getSiteCountV2')
def getSiteCountV2(**kwargs):
    return CatalystClient().getSiteCountV2(**kwargs)

@register('returnsCountOfSoftwareImages')
def returnsCountOfSoftwareImages(**kwargs):
    return CatalystClient().returnsCountOfSoftwareImages(**kwargs)

@register('getExtranetPolicies')
def getExtranetPolicies(**kwargs):
    return CatalystClient().getExtranetPolicies(**kwargs)

@register('getWirelessProfileByID')
def getWirelessProfileByID(**kwargs):
    return CatalystClient().getWirelessProfileByID(**kwargs)

@register('getFlexibleReportScheduleByReportId')
def getFlexibleReportScheduleByReportId(**kwargs):
    return CatalystClient().getFlexibleReportScheduleByReportId(**kwargs)

@register('getPortChannels')
def getPortChannels(**kwargs):
    return CatalystClient().getPortChannels(**kwargs)

@register('getRFProfileByID')
def getRFProfileByID(**kwargs):
    return CatalystClient().getRFProfileByID(**kwargs)

@register('getsTheTemplatesAvailable')
def getsTheTemplatesAvailable(**kwargs):
    return CatalystClient().getsTheTemplatesAvailable(**kwargs)

@register('getSyslogSubscriptionDetails')
def getSyslogSubscriptionDetails(**kwargs):
    return CatalystClient().getSyslogSubscriptionDetails(**kwargs)

@register('returnsAllIssueTriggerDefinitionsForGivenFilters.')
def returnsAllIssueTriggerDefinitionsForGivenFilters_(**kwargs):
    return CatalystClient().returnsAllIssueTriggerDefinitionsForGivenFilters_(**kwargs)

@register('getListOfScheduledReports')
def getListOfScheduledReports(**kwargs):
    return CatalystClient().getListOfScheduledReports(**kwargs)

@register('getAAAAttributeAPI')
def getAAAAttributeAPI(**kwargs):
    return CatalystClient().getAAAAttributeAPI(**kwargs)

@register('getClientDetail')
def getClientDetail(**kwargs):
    return CatalystClient().getClientDetail(**kwargs)

@register('countTheNumberOfEvents')
def countTheNumberOfEvents(**kwargs):
    return CatalystClient().countTheNumberOfEvents(**kwargs)

@register('getEoXStatusForAllDevices')
def getEoXStatusForAllDevices(**kwargs):
    return CatalystClient().getEoXStatusForAllDevices(**kwargs)

@register('getTagMemberCount')
def getTagMemberCount(**kwargs):
    return CatalystClient().getTagMemberCount(**kwargs)

@register('retrievesConfigurationDetailsOfTheExternalIPAMServer.')
def retrievesConfigurationDetailsOfTheExternalIPAMServer_(**kwargs):
    return CatalystClient().retrievesConfigurationDetailsOfTheExternalIPAMServer_(**kwargs)

@register('getViewDetailsForAGivenViewGroup&View')
def getViewDetailsForAGivenViewGroup_View(**kwargs):
    return CatalystClient().getViewDetailsForAGivenViewGroup_View(**kwargs)

@register('getTheDetailsOfPhysicalComponentsOfTheGivenDevice.')
def getTheDetailsOfPhysicalComponentsOfTheGivenDevice_(**kwargs):
    return CatalystClient().getTheDetailsOfPhysicalComponentsOfTheGivenDevice_(**kwargs)

@register('getDeviceInterfacesBySpecifiedRange')
def getDeviceInterfacesBySpecifiedRange(**kwargs):
    return CatalystClient().getDeviceInterfacesBySpecifiedRange(**kwargs)

@register('getPollingIntervalForAllDevices')
def getPollingIntervalForAllDevices(**kwargs):
    return CatalystClient().getPollingIntervalForAllDevices(**kwargs)

@register('getDeviceList')
def getDeviceList(**kwargs):
    return CatalystClient().getDeviceList(**kwargs)

@register('getAllKeywordsOfCLIsAcceptedByCommandRunner')
def getAllKeywordsOfCLIsAcceptedByCommandRunner(**kwargs):
    return CatalystClient().getAllKeywordsOfCLIsAcceptedByCommandRunner(**kwargs)

@register('getQosDeviceInterfaceInfo')
def getQosDeviceInterfaceInfo(**kwargs):
    return CatalystClient().getQosDeviceInterfaceInfo(**kwargs)

@register('retrieveTheCountOfInterfacesThatAreAssociatedWithAtLeastOneTag.')
def retrieveTheCountOfInterfacesThatAreAssociatedWithAtLeastOneTag_(**kwargs):
    return CatalystClient().retrieveTheCountOfInterfacesThatAreAssociatedWithAtLeastOneTag_(**kwargs)

@register('getDeviceFamilyIdentifiers')
def getDeviceFamilyIdentifiers(**kwargs):
    return CatalystClient().getDeviceFamilyIdentifiers(**kwargs)

@register('getTaskCount')
def getTaskCount(**kwargs):
    return CatalystClient().getTaskCount(**kwargs)

@register('devices')
def devices(**kwargs):
    return CatalystClient().devices(**kwargs)

@register('getSSIDCountForSpecificWirelessController')
def getSSIDCountForSpecificWirelessController(**kwargs):
    return CatalystClient().getSSIDCountForSpecificWirelessController(**kwargs)

@register('retrievesValidationDetailsForAValidationSet')
def retrievesValidationDetailsForAValidationSet(**kwargs):
    return CatalystClient().retrievesValidationDetailsForAValidationSet(**kwargs)

@register('getSmartAccountList')
def getSmartAccountList(**kwargs):
    return CatalystClient().getSmartAccountList(**kwargs)

@register('getLayer3VirtualNetworks')
def getLayer3VirtualNetworks(**kwargs):
    return CatalystClient().getLayer3VirtualNetworks(**kwargs)

@register('getListOfAvailableNamespaces')
def getListOfAvailableNamespaces(**kwargs):
    return CatalystClient().getListOfAvailableNamespaces(**kwargs)

@register('getSSIDByID')
def getSSIDByID(**kwargs):
    return CatalystClient().getSSIDByID(**kwargs)

@register('retrieveNetworkDeviceProductName')
def retrieveNetworkDeviceProductName(**kwargs):
    return CatalystClient().retrieveNetworkDeviceProductName(**kwargs)

@register('getExecutionIdByReportId')
def getExecutionIdByReportId(**kwargs):
    return CatalystClient().getExecutionIdByReportId(**kwargs)

@register('getMobilityGroupsCount')
def getMobilityGroupsCount(**kwargs):
    return CatalystClient().getMobilityGroupsCount(**kwargs)

@register('getTaskDetailsByID')
def getTaskDetailsByID(**kwargs):
    return CatalystClient().getTaskDetailsByID(**kwargs)

@register('custom-promptSupportGETAPI')
def custom_promptSupportGETAPI(**kwargs):
    return CatalystClient().custom_promptSupportGETAPI(**kwargs)

@register('getAdvisoriesList')
def getAdvisoriesList(**kwargs):
    return CatalystClient().getAdvisoriesList(**kwargs)

@register('getDeviceInterfaceVLANs')
def getDeviceInterfaceVLANs(**kwargs):
    return CatalystClient().getDeviceInterfaceVLANs(**kwargs)

@register('getListOfFiles')
def getListOfFiles(**kwargs):
    return CatalystClient().getListOfFiles(**kwargs)

@register('retrieveSpecificImageDistributionServer')
def retrieveSpecificImageDistributionServer(**kwargs):
    return CatalystClient().retrieveSpecificImageDistributionServer(**kwargs)

@register('getApplicationPolicy')
def getApplicationPolicy(**kwargs):
    return CatalystClient().getApplicationPolicy(**kwargs)

@register('getWorkflowById')
def getWorkflowById(**kwargs):
    return CatalystClient().getWorkflowById(**kwargs)

@register('getAdvisoriesSummary')
def getAdvisoriesSummary(**kwargs):
    return CatalystClient().getAdvisoriesSummary(**kwargs)

@register('getTagResourceTypes')
def getTagResourceTypes(**kwargs):
    return CatalystClient().getTagResourceTypes(**kwargs)

@register('getPortAssignmentCount')
def getPortAssignmentCount(**kwargs):
    return CatalystClient().getPortAssignmentCount(**kwargs)

@register('getDiscoveriesByRange')
def getDiscoveriesByRange(**kwargs):
    return CatalystClient().getDiscoveriesByRange(**kwargs)

@register('getAllITSMIntegrationSettings')
def getAllITSMIntegrationSettings(**kwargs):
    return CatalystClient().getAllITSMIntegrationSettings(**kwargs)

@register('licenseUsageDetails')
def licenseUsageDetails(**kwargs):
    return CatalystClient().licenseUsageDetails(**kwargs)

@register('getsAnArea')
def getsAnArea(**kwargs):
    return CatalystClient().getsAnArea(**kwargs)

@register('getTheCountOfHealthScoreDefinitionsBasedOnProvidedFilters.')
def getTheCountOfHealthScoreDefinitionsBasedOnProvidedFilters_(**kwargs):
    return CatalystClient().getTheCountOfHealthScoreDefinitionsBasedOnProvidedFilters_(**kwargs)

@register('getExtranetPolicyCount')
def getExtranetPolicyCount(**kwargs):
    return CatalystClient().getExtranetPolicyCount(**kwargs)

@register('getResyncIntervalForTheNetworkDevice')
def getResyncIntervalForTheNetworkDevice(**kwargs):
    return CatalystClient().getResyncIntervalForTheNetworkDevice(**kwargs)

@register('getInterfaces')
def getInterfaces(**kwargs):
    return CatalystClient().getInterfaces(**kwargs)

@register('getAllViewGroups')
def getAllViewGroups(**kwargs):
    return CatalystClient().getAllViewGroups(**kwargs)

@register('getEvents')
def getEvents(**kwargs):
    return CatalystClient().getEvents(**kwargs)

@register('getEmailEventSubscriptions')
def getEmailEventSubscriptions(**kwargs):
    return CatalystClient().getEmailEventSubscriptions(**kwargs)

@register('getEmailSubscriptionDetails')
def getEmailSubscriptionDetails(**kwargs):
    return CatalystClient().getEmailSubscriptionDetails(**kwargs)

@register('retrieveAAASettingsForASite')
def retrieveAAASettingsForASite(**kwargs):
    return CatalystClient().retrieveAAASettingsForASite(**kwargs)

@register('getInterfaceDetailsByDeviceIdAndInterfaceName')
def getInterfaceDetailsByDeviceIdAndInterfaceName(**kwargs):
    return CatalystClient().getInterfaceDetailsByDeviceIdAndInterfaceName(**kwargs)

@register('getAllGlobalCredentialsV2')
def getAllGlobalCredentialsV2(**kwargs):
    return CatalystClient().getAllGlobalCredentialsV2(**kwargs)

@register('getAccessPoint(s)FactoryResetStatus')
def getAccessPoint_s_FactoryResetStatus(**kwargs):
    return CatalystClient().getAccessPoint_s_FactoryResetStatus(**kwargs)

@register('getNetworkDevicesFromDiscovery')
def getNetworkDevicesFromDiscovery(**kwargs):
    return CatalystClient().getNetworkDevicesFromDiscovery(**kwargs)

@register('getSites')
def getSites(**kwargs):
    return CatalystClient().getSites(**kwargs)

@register('returnTheCountOfAllTheFabricSiteWhichHasSSIDToIPPoolMapping')
def returnTheCountOfAllTheFabricSiteWhichHasSSIDToIPPoolMapping(**kwargs):
    return CatalystClient().returnTheCountOfAllTheFabricSiteWhichHasSSIDToIPPoolMapping(**kwargs)

@register('getEventSubscriptions')
def getEventSubscriptions(**kwargs):
    return CatalystClient().getEventSubscriptions(**kwargs)

@register('readSiteHealthSummaryDataBySiteId.')
def readSiteHealthSummaryDataBySiteId_(**kwargs):
    return CatalystClient().readSiteHealthSummaryDataBySiteId_(**kwargs)

@register('getPlannedAccessPointsForFloor')
def getPlannedAccessPointsForFloor(**kwargs):
    return CatalystClient().getPlannedAccessPointsForFloor(**kwargs)

@register('returnListOfReplacementDevicesWithReplacementDetails')
def returnListOfReplacementDevicesWithReplacementDetails(**kwargs):
    return CatalystClient().returnListOfReplacementDevicesWithReplacementDetails(**kwargs)

@register('getDiscoveryById')
def getDiscoveryById(**kwargs):
    return CatalystClient().getDiscoveryById(**kwargs)

@register('getConfigurationArchiveDetails')
def getConfigurationArchiveDetails(**kwargs):
    return CatalystClient().getConfigurationArchiveDetails(**kwargs)

@register('getAdvisoriesPerDevice')
def getAdvisoriesPerDevice(**kwargs):
    return CatalystClient().getAdvisoriesPerDevice(**kwargs)

@register('getDeviceInterfaceCountForMultipleDevices')
def getDeviceInterfaceCountForMultipleDevices(**kwargs):
    return CatalystClient().getDeviceInterfaceCountForMultipleDevices(**kwargs)

@register('retrievesTheCountOfValidationWorkflows')
def retrievesTheCountOfValidationWorkflows(**kwargs):
    return CatalystClient().retrievesTheCountOfValidationWorkflows(**kwargs)

@register('getSNMPProperties')
def getSNMPProperties(**kwargs):
    return CatalystClient().getSNMPProperties(**kwargs)

@register('getComplianceDetailCount')
def getComplianceDetailCount(**kwargs):
    return CatalystClient().getComplianceDetailCount(**kwargs)

@register('getOverallClientHealth')
def getOverallClientHealth(**kwargs):
    return CatalystClient().getOverallClientHealth(**kwargs)

@register('getLinecardDetails')
def getLinecardDetails(**kwargs):
    return CatalystClient().getLinecardDetails(**kwargs)

@register('getsTheTotalNetworkDeviceInterfaceCountsInTheSpecifiedTimeRange.WhenThereIsNoStartAndEndTimeSpecifiedReturnsTheLatestInterfacesTotalCount.')
def getsTheTotalNetworkDeviceInterfaceCountsInTheSpecifiedTimeRange_WhenThereIsNoStartAndEndTimeSpecifiedReturnsTheLatestInterfacesTotalCount_(**kwargs):
    return CatalystClient().getsTheTotalNetworkDeviceInterfaceCountsInTheSpecifiedTimeRange_WhenThereIsNoStartAndEndTimeSpecifiedReturnsTheLatestInterfacesTotalCount_(**kwargs)

@register('getWirelessProfilesCount')
def getWirelessProfilesCount(**kwargs):
    return CatalystClient().getWirelessProfilesCount(**kwargs)

@register('getTagById')
def getTagById(**kwargs):
    return CatalystClient().getTagById(**kwargs)

@register('getAuditLogSummary')
def getAuditLogSummary(**kwargs):
    return CatalystClient().getAuditLogSummary(**kwargs)

@register('getsAListOfProjects')
def getsAListOfProjects(**kwargs):
    return CatalystClient().getsAListOfProjects(**kwargs)

@register('systemHealthCountAPI')
def systemHealthCountAPI(**kwargs):
    return CatalystClient().systemHealthCountAPI(**kwargs)

@register('getAuthenticationAndPolicyServers')
def getAuthenticationAndPolicyServers(**kwargs):
    return CatalystClient().getAuthenticationAndPolicyServers(**kwargs)

@register('getSSIDCountBySite')
def getSSIDCountBySite(**kwargs):
    return CatalystClient().getSSIDCountBySite(**kwargs)

@register('deviceLicenseSummary')
def deviceLicenseSummary(**kwargs):
    return CatalystClient().deviceLicenseSummary(**kwargs)

@register('complianceDetailsOfDevice')
def complianceDetailsOfDevice(**kwargs):
    return CatalystClient().complianceDetailsOfDevice(**kwargs)

@register('retrievesTheCountOfSitesThatTheGivenNetworkProfileForSitesIsAssignedTo')
def retrievesTheCountOfSitesThatTheGivenNetworkProfileForSitesIsAssignedTo(**kwargs):
    return CatalystClient().retrievesTheCountOfSitesThatTheGivenNetworkProfileForSitesIsAssignedTo(**kwargs)

@register('getProvisionedDevices')
def getProvisionedDevices(**kwargs):
    return CatalystClient().getProvisionedDevices(**kwargs)

@register('retrievesAllPreviousPathtracesSummary')
def retrievesAllPreviousPathtracesSummary(**kwargs):
    return CatalystClient().retrievesAllPreviousPathtracesSummary(**kwargs)

@register('inventoryInsightDeviceLinkMismatchAPI')
def inventoryInsightDeviceLinkMismatchAPI(**kwargs):
    return CatalystClient().inventoryInsightDeviceLinkMismatchAPI(**kwargs)

@register('getTheDeviceDataForTheGivenDeviceId(Uuid)')
def getTheDeviceDataForTheGivenDeviceId_Uuid_(**kwargs):
    return CatalystClient().getTheDeviceDataForTheGivenDeviceId_Uuid_(**kwargs)

@register('lANAutomationLogById')
def lANAutomationLogById(**kwargs):
    return CatalystClient().lANAutomationLogById(**kwargs)

@register('getDeviceCredentialSettingsForASite')
def getDeviceCredentialSettingsForASite(**kwargs):
    return CatalystClient().getDeviceCredentialSettingsForASite(**kwargs)

@register('getDeviceInterfaceCount')
def getDeviceInterfaceCount(**kwargs):
    return CatalystClient().getDeviceInterfaceCount(**kwargs)

@register('ciscoDNACenterReleaseSummary')
def ciscoDNACenterReleaseSummary(**kwargs):
    return CatalystClient().ciscoDNACenterReleaseSummary(**kwargs)

@register('getLayer2VirtualNetworkCount')
def getLayer2VirtualNetworkCount(**kwargs):
    return CatalystClient().getLayer2VirtualNetworkCount(**kwargs)

@register('retrievesTheCountOfNetworkProfilesForSites')
def retrievesTheCountOfNetworkProfilesForSites(**kwargs):
    return CatalystClient().retrievesTheCountOfNetworkProfilesForSites(**kwargs)

@register('getDeviceCount')
def getDeviceCount(**kwargs):
    return CatalystClient().getDeviceCount(**kwargs)

@register('getFabricDevicesLayer2Handoffs')
def getFabricDevicesLayer2Handoffs(**kwargs):
    return CatalystClient().getFabricDevicesLayer2Handoffs(**kwargs)

@register('getSyslogEventSubscriptions')
def getSyslogEventSubscriptions(**kwargs):
    return CatalystClient().getSyslogEventSubscriptions(**kwargs)

@register('getVLANDetails')
def getVLANDetails(**kwargs):
    return CatalystClient().getVLANDetails(**kwargs)

@register('getAllMobilityGroups	')
def getAllMobilityGroups_(**kwargs):
    return CatalystClient().getAllMobilityGroups_(**kwargs)

@register('getSiteV2')
def getSiteV2(**kwargs):
    return CatalystClient().getSiteV2(**kwargs)

@register('systemHealthAPI')
def systemHealthAPI(**kwargs):
    return CatalystClient().systemHealthAPI(**kwargs)

@register('lANAutomationStatusById')
def lANAutomationStatusById(**kwargs):
    return CatalystClient().lANAutomationStatusById(**kwargs)

@register('getApplication/s')
def getApplication_s(**kwargs):
    return CatalystClient().getApplication_s(**kwargs)

@register('getFabricDevices')
def getFabricDevices(**kwargs):
    return CatalystClient().getFabricDevices(**kwargs)

@register('get802.11beProfileByID')
def get802_11beProfileByID(**kwargs):
    return CatalystClient().get802_11beProfileByID(**kwargs)

@register('getTasksCount')
def getTasksCount(**kwargs):
    return CatalystClient().getTasksCount(**kwargs)

@register('getsAFloor')
def getsAFloor(**kwargs):
    return CatalystClient().getsAFloor(**kwargs)

@register('getUsersAPI')
def getUsersAPI(**kwargs):
    return CatalystClient().getUsersAPI(**kwargs)

@register('getFabricZones')
def getFabricZones(**kwargs):
    return CatalystClient().getFabricZones(**kwargs)

@register('getVirtualAccountList')
def getVirtualAccountList(**kwargs):
    return CatalystClient().getVirtualAccountList(**kwargs)

@register('getQosDeviceInterfaceInfoCount')
def getQosDeviceInterfaceInfoCount(**kwargs):
    return CatalystClient().getQosDeviceInterfaceInfoCount(**kwargs)

@register('countOfEvents')
def countOfEvents(**kwargs):
    return CatalystClient().countOfEvents(**kwargs)

@register('getOSPFInterfaces')
def getOSPFInterfaces(**kwargs):
    return CatalystClient().getOSPFInterfaces(**kwargs)

@register('getNetworkDeviceImageUpdates')
def getNetworkDeviceImageUpdates(**kwargs):
    return CatalystClient().getNetworkDeviceImageUpdates(**kwargs)

@register('getTransitNetworks')
def getTransitNetworks(**kwargs):
    return CatalystClient().getTransitNetworks(**kwargs)

@register('getStackDetailsForDevice')
def getStackDetailsForDevice(**kwargs):
    return CatalystClient().getStackDetailsForDevice(**kwargs)

@register('getApplicationSetCount')
def getApplicationSetCount(**kwargs):
    return CatalystClient().getApplicationSetCount(**kwargs)

@register('getWorkflowCount')
def getWorkflowCount(**kwargs):
    return CatalystClient().getWorkflowCount(**kwargs)

@register('deviceComplianceStatus')
def deviceComplianceStatus(**kwargs):
    return CatalystClient().deviceComplianceStatus(**kwargs)

@register('retrievesPreviousPathtrace')
def retrievesPreviousPathtrace(**kwargs):
    return CatalystClient().retrievesPreviousPathtrace(**kwargs)

@register('getOverallNetworkHealth')
def getOverallNetworkHealth(**kwargs):
    return CatalystClient().getOverallNetworkHealth(**kwargs)

@register('getPnPGlobalSettings')
def getPnPGlobalSettings(**kwargs):
    return CatalystClient().getPnPGlobalSettings(**kwargs)

@register('getServiceProviderDetailsV2')
def getServiceProviderDetailsV2(**kwargs):
    return CatalystClient().getServiceProviderDetailsV2(**kwargs)

@register('getWirelessProfiles')
def getWirelessProfiles(**kwargs):
    return CatalystClient().getWirelessProfiles(**kwargs)

@register('getConfigTaskDetails')
def getConfigTaskDetails(**kwargs):
    return CatalystClient().getConfigTaskDetails(**kwargs)

@register('retrieveTheCountOfNetworkDevicesThatAreAssociatedWithAtLeastOneTag.')
def retrieveTheCountOfNetworkDevicesThatAreAssociatedWithAtLeastOneTag_(**kwargs):
    return CatalystClient().retrieveTheCountOfNetworkDevicesThatAreAssociatedWithAtLeastOneTag_(**kwargs)

@register('getMulticastVirtualNetworkCount')
def getMulticastVirtualNetworkCount(**kwargs):
    return CatalystClient().getMulticastVirtualNetworkCount(**kwargs)

@register('getTagCount')
def getTagCount(**kwargs):
    return CatalystClient().getTagCount(**kwargs)

@register('getDeviceSummary')
def getDeviceSummary(**kwargs):
    return CatalystClient().getDeviceSummary(**kwargs)

@register('getAuthenticationProfiles')
def getAuthenticationProfiles(**kwargs):
    return CatalystClient().getAuthenticationProfiles(**kwargs)

@register('getAllFlexibleReportSchedules')
def getAllFlexibleReportSchedules(**kwargs):
    return CatalystClient().getAllFlexibleReportSchedules(**kwargs)

@register('virtualAccountDetails')
def virtualAccountDetails(**kwargs):
    return CatalystClient().virtualAccountDetails(**kwargs)

@register('getFunctionalCapabilityById')
def getFunctionalCapabilityById(**kwargs):
    return CatalystClient().getFunctionalCapabilityById(**kwargs)

@register('getFabricSites')
def getFabricSites(**kwargs):
    return CatalystClient().getFabricSites(**kwargs)

@register('getWorkflows')
def getWorkflows(**kwargs):
    return CatalystClient().getWorkflows(**kwargs)

@register('getDeviceConfigById')
def getDeviceConfigById(**kwargs):
    return CatalystClient().getDeviceConfigById(**kwargs)

@register('retrievesSpecificClientInformationMatchingTheMACAddress.')
def retrievesSpecificClientInformationMatchingTheMACAddress_(**kwargs):
    return CatalystClient().retrievesSpecificClientInformationMatchingTheMACAddress_(**kwargs)

@register('getOrganizationListForMeraki')
def getOrganizationListForMeraki(**kwargs):
    return CatalystClient().getOrganizationListForMeraki(**kwargs)

@register('getPollingIntervalById')
def getPollingIntervalById(**kwargs):
    return CatalystClient().getPollingIntervalById(**kwargs)

@register('getNotifications')
def getNotifications(**kwargs):
    return CatalystClient().getNotifications(**kwargs)

@register('getAllTheDetailsAndSuggestedActionsOfAnIssueForTheGivenIssueId')
def getAllTheDetailsAndSuggestedActionsOfAnIssueForTheGivenIssueId(**kwargs):
    return CatalystClient().getAllTheDetailsAndSuggestedActionsOfAnIssueForTheGivenIssueId(**kwargs)

@register('legitOperationsForInterface')
def legitOperationsForInterface(**kwargs):
    return CatalystClient().legitOperationsForInterface(**kwargs)

@register('getDeviceConfigCount')
def getDeviceConfigCount(**kwargs):
    return CatalystClient().getDeviceConfigCount(**kwargs)

@register('getISISInterfaces')
def getISISInterfaces(**kwargs):
    return CatalystClient().getISISInterfaces(**kwargs)

@register('retrieveANetworkProfileForSitesById')
def retrieveANetworkProfileForSitesById(**kwargs):
    return CatalystClient().retrieveANetworkProfileForSitesById(**kwargs)

@register('getAuditLogRecords')
def getAuditLogRecords(**kwargs):
    return CatalystClient().getAuditLogRecords(**kwargs)

@register('systemPerformanceHistoricalAPI')
def systemPerformanceHistoricalAPI(**kwargs):
    return CatalystClient().systemPerformanceHistoricalAPI(**kwargs)

@register('getSupervisorCardDetail')
def getSupervisorCardDetail(**kwargs):
    return CatalystClient().getSupervisorCardDetail(**kwargs)

@register('retrieveImageDistributionSettingsForASite')
def retrieveImageDistributionSettingsForASite(**kwargs):
    return CatalystClient().retrieveImageDistributionSettingsForASite(**kwargs)

@register('getSSIDDetailsForSpecificWirelessController')
def getSSIDDetailsForSpecificWirelessController(**kwargs):
    return CatalystClient().getSSIDDetailsForSpecificWirelessController(**kwargs)

@register('getsDetailsOfAGivenTemplate')
def getsDetailsOfAGivenTemplate(**kwargs):
    return CatalystClient().getsDetailsOfAGivenTemplate(**kwargs)

@register('getEventArtifacts')
def getEventArtifacts(**kwargs):
    return CatalystClient().getEventArtifacts(**kwargs)

@register('getsTheDetailsOfAGivenProject.')
def getsTheDetailsOfAGivenProject_(**kwargs):
    return CatalystClient().getsTheDetailsOfAGivenProject_(**kwargs)

@register('retrievesValidationWorkflowDetails')
def retrievesValidationWorkflowDetails(**kwargs):
    return CatalystClient().retrievesValidationWorkflowDetails(**kwargs)

@register('getModuleCount')
def getModuleCount(**kwargs):
    return CatalystClient().getModuleCount(**kwargs)

@register('getTransitNetworksCount')
def getTransitNetworksCount(**kwargs):
    return CatalystClient().getTransitNetworksCount(**kwargs)

@register('returnsAllTheFabricSitesThatHaveVLANToSSIDMapping.')
def returnsAllTheFabricSitesThatHaveVLANToSSIDMapping_(**kwargs):
    return CatalystClient().returnsAllTheFabricSitesThatHaveVLANToSSIDMapping_(**kwargs)

@register('deviceCountDetails')
def deviceCountDetails(**kwargs):
    return CatalystClient().deviceCountDetails(**kwargs)

@register('getAllExecutionDetailsForAGivenReport')
def getAllExecutionDetailsForAGivenReport(**kwargs):
    return CatalystClient().getAllExecutionDetailsForAGivenReport(**kwargs)

@register('getRest/WebhookEventSubscriptions')
def getRest_WebhookEventSubscriptions(**kwargs):
    return CatalystClient().getRest_WebhookEventSubscriptions(**kwargs)

@register('getRolesAPI')
def getRolesAPI(**kwargs):
    return CatalystClient().getRolesAPI(**kwargs)

@register('getGoldenTagStatusOfAnImage.')
def getGoldenTagStatusOfAnImage_(**kwargs):
    return CatalystClient().getGoldenTagStatusOfAnImage_(**kwargs)

@register('getPortChannelCount')
def getPortChannelCount(**kwargs):
    return CatalystClient().getPortChannelCount(**kwargs)

@register('mapsSupportedAccessPoints')
def mapsSupportedAccessPoints(**kwargs):
    return CatalystClient().mapsSupportedAccessPoints(**kwargs)

@register('getAuditLogParentRecords')
def getAuditLogParentRecords(**kwargs):
    return CatalystClient().getAuditLogParentRecords(**kwargs)

@register('retrieveDNSSettingsForASite')
def retrieveDNSSettingsForASite(**kwargs):
    return CatalystClient().retrieveDNSSettingsForASite(**kwargs)

@register('getHealthScoreDefinitionForTheGivenId.')
def getHealthScoreDefinitionForTheGivenId_(**kwargs):
    return CatalystClient().getHealthScoreDefinitionForTheGivenId_(**kwargs)

@register('getProject(s)Details')
def getProject_s_Details(**kwargs):
    return CatalystClient().getProject_s_Details(**kwargs)

@register('downloadAFileByFileId')
def downloadAFileByFileId(**kwargs):
    return CatalystClient().downloadAFileByFileId(**kwargs)

@register('getAllHealthScoreDefinitionsForGivenFilters.')
def getAllHealthScoreDefinitionsForGivenFilters_(**kwargs):
    return CatalystClient().getAllHealthScoreDefinitionsForGivenFilters_(**kwargs)

@register('getEmailDestination')
def getEmailDestination(**kwargs):
    return CatalystClient().getEmailDestination(**kwargs)

@register('getsInterfacesAlongWithStatisticsDataFromAllNetworkDevices.')
def getsInterfacesAlongWithStatisticsDataFromAllNetworkDevices_(**kwargs):
    return CatalystClient().getsInterfacesAlongWithStatisticsDataFromAllNetworkDevices_(**kwargs)

@register('retrieveLicenseSetting')
def retrieveLicenseSetting(**kwargs):
    return CatalystClient().retrieveLicenseSetting(**kwargs)

@register('getTheTotalCustomIssueDefinitionsCountBasedOnTheProvidedFilters.')
def getTheTotalCustomIssueDefinitionsCountBasedOnTheProvidedFilters_(**kwargs):
    return CatalystClient().getTheTotalCustomIssueDefinitionsCountBasedOnTheProvidedFilters_(**kwargs)

@register('get802.11beProfilesCount')
def get802_11beProfilesCount(**kwargs):
    return CatalystClient().get802_11beProfilesCount(**kwargs)

@register('getMulticast')
def getMulticast(**kwargs):
    return CatalystClient().getMulticast(**kwargs)

@register('getFabricDevicesCount')
def getFabricDevicesCount(**kwargs):
    return CatalystClient().getFabricDevicesCount(**kwargs)

@register('downloadFlexibleReport')
def downloadFlexibleReport(**kwargs):
    return CatalystClient().downloadFlexibleReport(**kwargs)

@register('getExternalAuthenticationServersAPI')
def getExternalAuthenticationServersAPI(**kwargs):
    return CatalystClient().getExternalAuthenticationServersAPI(**kwargs)

@register('getLayer3VirtualNetworksCount')
def getLayer3VirtualNetworksCount(**kwargs):
    return CatalystClient().getLayer3VirtualNetworksCount(**kwargs)

@register('lANAutomationStatus')
def lANAutomationStatus(**kwargs):
    return CatalystClient().lANAutomationStatus(**kwargs)

@register('getDevicesDiscoveredById')
def getDevicesDiscoveredById(**kwargs):
    return CatalystClient().getDevicesDiscoveredById(**kwargs)

@register('getTaskById')
def getTaskById(**kwargs):
    return CatalystClient().getTaskById(**kwargs)

@register('getPermissionsAPI')
def getPermissionsAPI(**kwargs):
    return CatalystClient().getPermissionsAPI(**kwargs)

@register('getDiscoveredDevicesByRange')
def getDiscoveredDevicesByRange(**kwargs):
    return CatalystClient().getDiscoveredDevicesByRange(**kwargs)

@register('retrievesTheTotalCountOfClientsByApplyingBasicFiltering')
def retrievesTheTotalCountOfClientsByApplyingBasicFiltering(**kwargs):
    return CatalystClient().retrievesTheTotalCountOfClientsByApplyingBasicFiltering(**kwargs)

@register('pOEDetails')
def pOEDetails(**kwargs):
    return CatalystClient().pOEDetails(**kwargs)

@register('retrievesTheListOfNetworkDeviceProductNames')
def retrievesTheListOfNetworkDeviceProductNames(**kwargs):
    return CatalystClient().retrievesTheListOfNetworkDeviceProductNames(**kwargs)

@register('getAnchorManagedAPLocationsForSpecificWirelessController')
def getAnchorManagedAPLocationsForSpecificWirelessController(**kwargs):
    return CatalystClient().getAnchorManagedAPLocationsForSpecificWirelessController(**kwargs)

@register('getConnectedDeviceDetail')
def getConnectedDeviceDetail(**kwargs):
    return CatalystClient().getConnectedDeviceDetail(**kwargs)

@register('getDevicesThatAreAssignedToASite')
def getDevicesThatAreAssignedToASite(**kwargs):
    return CatalystClient().getDevicesThatAreAssignedToASite(**kwargs)

@register('lANAutomationLog')
def lANAutomationLog(**kwargs):
    return CatalystClient().lANAutomationLog(**kwargs)

@register('retrievesTheListOfNetworkProfilesThatTheGivenSiteHasBeenAssigned')
def retrievesTheListOfNetworkProfilesThatTheGivenSiteHasBeenAssigned(**kwargs):
    return CatalystClient().retrievesTheListOfNetworkProfilesThatTheGivenSiteHasBeenAssigned(**kwargs)

@register('getDiscoveryJobsByIP')
def getDiscoveryJobsByIP(**kwargs):
    return CatalystClient().getDiscoveryJobsByIP(**kwargs)

@register('getTemplate(s)Details')
def getTemplate_s_Details(**kwargs):
    return CatalystClient().getTemplate_s_Details(**kwargs)

@register('lANAutomationLogsForIndividualDevices')
def lANAutomationLogsForIndividualDevices(**kwargs):
    return CatalystClient().lANAutomationLogsForIndividualDevices(**kwargs)

@register('getListOfDiscoveriesByDiscoveryId')
def getListOfDiscoveriesByDiscoveryId(**kwargs):
    return CatalystClient().getListOfDiscoveriesByDiscoveryId(**kwargs)

@register('getPhysicalTopology')
def getPhysicalTopology(**kwargs):
    return CatalystClient().getPhysicalTopology(**kwargs)

@register('getSiteTopology')
def getSiteTopology(**kwargs):
    return CatalystClient().getSiteTopology(**kwargs)

@register('getITSMIntegrationStatus')
def getITSMIntegrationStatus(**kwargs):
    return CatalystClient().getITSMIntegrationStatus(**kwargs)

@register('getSecondaryManagedAPLocationsForSpecificWirelessController')
def getSecondaryManagedAPLocationsForSpecificWirelessController(**kwargs):
    return CatalystClient().getSecondaryManagedAPLocationsForSpecificWirelessController(**kwargs)

@register('retrieveNTPSettingsForASite')
def retrieveNTPSettingsForASite(**kwargs):
    return CatalystClient().retrieveNTPSettingsForASite(**kwargs)

@register('retrieveTagsAssociatedWithTheInterfaces.')
def retrieveTagsAssociatedWithTheInterfaces_(**kwargs):
    return CatalystClient().retrieveTagsAssociatedWithTheInterfaces_(**kwargs)

@register('countOfNetworkDeviceImageUpdates')
def countOfNetworkDeviceImageUpdates(**kwargs):
    return CatalystClient().countOfNetworkDeviceImageUpdates(**kwargs)

@register('returnReplacementDevicesCount')
def returnReplacementDevicesCount(**kwargs):
    return CatalystClient().returnReplacementDevicesCount(**kwargs)

@register('getPlannedAccessPointsForBuilding')
def getPlannedAccessPointsForBuilding(**kwargs):
    return CatalystClient().getPlannedAccessPointsForBuilding(**kwargs)

@register('getTheCountOfSystemDefinedIssueDefinitionsBasedOnProvidedFilters.')
def getTheCountOfSystemDefinedIssueDefinitionsBasedOnProvidedFilters_(**kwargs):
    return CatalystClient().getTheCountOfSystemDefinedIssueDefinitionsBasedOnProvidedFilters_(**kwargs)

@register('countOfNetworkProductNames')
def countOfNetworkProductNames(**kwargs):
    return CatalystClient().countOfNetworkProductNames(**kwargs)

@register('getAccessPointConfiguration')
def getAccessPointConfiguration(**kwargs):
    return CatalystClient().getAccessPointConfiguration(**kwargs)

@register('getDeviceConfigForAllDevices')
def getDeviceConfigForAllDevices(**kwargs):
    return CatalystClient().getDeviceConfigForAllDevices(**kwargs)

@register('getTopologyDetails')
def getTopologyDetails(**kwargs):
    return CatalystClient().getTopologyDetails(**kwargs)

@register('getTheDetailsOfIssuesForGivenSetOfFilters-2')
def getTheDetailsOfIssuesForGivenSetOfFilters_2(**kwargs):
    return CatalystClient().getTheDetailsOfIssuesForGivenSetOfFilters_2(**kwargs)

@register('smartAccountDetails')
def smartAccountDetails(**kwargs):
    return CatalystClient().smartAccountDetails(**kwargs)

@register('getFabricDevicesLayer3HandoffsWithIpTransitCount')
def getFabricDevicesLayer3HandoffsWithIpTransitCount(**kwargs):
    return CatalystClient().getFabricDevicesLayer3HandoffsWithIpTransitCount(**kwargs)

@register('getFabricDevicesLayer3HandoffsWithSdaTransitCount')
def getFabricDevicesLayer3HandoffsWithSdaTransitCount(**kwargs):
    return CatalystClient().getFabricDevicesLayer3HandoffsWithSdaTransitCount(**kwargs)

@register('retrievesTheListOfNetworkProfilesForSites')
def retrievesTheListOfNetworkProfilesForSites(**kwargs):
    return CatalystClient().retrievesTheListOfNetworkProfilesForSites(**kwargs)

@register('getFunctionalCapabilityForDevices')
def getFunctionalCapabilityForDevices(**kwargs):
    return CatalystClient().getFunctionalCapabilityForDevices(**kwargs)

@register('getPortAssignments')
def getPortAssignments(**kwargs):
    return CatalystClient().getPortAssignments(**kwargs)

@register('getBusinessAPIExecutionDetails')
def getBusinessAPIExecutionDetails(**kwargs):
    return CatalystClient().getBusinessAPIExecutionDetails(**kwargs)

@register('lANAutomationActiveSessions')
def lANAutomationActiveSessions(**kwargs):
    return CatalystClient().lANAutomationActiveSessions(**kwargs)

@register('getSiteNotAssignedNetworkDevices')
def getSiteNotAssignedNetworkDevices(**kwargs):
    return CatalystClient().getSiteNotAssignedNetworkDevices(**kwargs)

@register('getAccessPointRebootTaskResult')
def getAccessPointRebootTaskResult(**kwargs):
    return CatalystClient().getAccessPointRebootTaskResult(**kwargs)

@register('getDeviceDetail')
def getDeviceDetail(**kwargs):
    return CatalystClient().getDeviceDetail(**kwargs)

@register('lANAutomationSessionCount')
def lANAutomationSessionCount(**kwargs):
    return CatalystClient().lANAutomationSessionCount(**kwargs)

@register('getNetworkDeviceByIP')
def getNetworkDeviceByIP(**kwargs):
    return CatalystClient().getNetworkDeviceByIP(**kwargs)

@register('getSiteNotAssignedNetworkDevicesCount')
def getSiteNotAssignedNetworkDevicesCount(**kwargs):
    return CatalystClient().getSiteNotAssignedNetworkDevicesCount(**kwargs)

@register('getDeviceBySerialNumber')
def getDeviceBySerialNumber(**kwargs):
    return CatalystClient().getDeviceBySerialNumber(**kwargs)

@register('getApplicationCount')
def getApplicationCount(**kwargs):
    return CatalystClient().getApplicationCount(**kwargs)

@register('downloadReportContent')
def downloadReportContent(**kwargs):
    return CatalystClient().downloadReportContent(**kwargs)

@register('getDeviceCount-2')
def getDeviceCount_2(**kwargs):
    return CatalystClient().getDeviceCount_2(**kwargs)

@register('eventArtifactCount')
def eventArtifactCount(**kwargs):
    return CatalystClient().eventArtifactCount(**kwargs)

@register('getComplianceStatusCount')
def getComplianceStatusCount(**kwargs):
    return CatalystClient().getComplianceStatusCount(**kwargs)

@register('getTasks')
def getTasks(**kwargs):
    return CatalystClient().getTasks(**kwargs)

@register('getListOfChildEventsForTheGivenWirelessClientEvent')
def getListOfChildEventsForTheGivenWirelessClientEvent(**kwargs):
    return CatalystClient().getListOfChildEventsForTheGivenWirelessClientEvent(**kwargs)

@register('getProvisioningSettings')
def getProvisioningSettings(**kwargs):
    return CatalystClient().getProvisioningSettings(**kwargs)

@register('readSiteCount.')
def readSiteCount_(**kwargs):
    return CatalystClient().readSiteCount_(**kwargs)

@register('getEoXDetailsPerDevice')
def getEoXDetailsPerDevice(**kwargs):
    return CatalystClient().getEoXDetailsPerDevice(**kwargs)

@register('ciscoDNACenterNodesConfigurationSummary')
def ciscoDNACenterNodesConfigurationSummary(**kwargs):
    return CatalystClient().ciscoDNACenterNodesConfigurationSummary(**kwargs)

@register('importMapArchive-ImportStatus')
def importMapArchive_ImportStatus(**kwargs):
    return CatalystClient().importMapArchive_ImportStatus(**kwargs)

@register('getExternalAuthenticationSettingAPI')
def getExternalAuthenticationSettingAPI(**kwargs):
    return CatalystClient().getExternalAuthenticationSettingAPI(**kwargs)

@register('getInterfaceById')
def getInterfaceById(**kwargs):
    return CatalystClient().getInterfaceById(**kwargs)

@register('deviceLicenseDetails')
def deviceLicenseDetails(**kwargs):
    return CatalystClient().deviceLicenseDetails(**kwargs)

@register('getTheInterfaceDataForTheGivenInterfaceId(instanceUuid)AlongWithTheStatisticsData')
def getTheInterfaceDataForTheGivenInterfaceId_instanceUuid_AlongWithTheStatisticsData(**kwargs):
    return CatalystClient().getTheInterfaceDataForTheGivenInterfaceId_instanceUuid_AlongWithTheStatisticsData(**kwargs)

@register('getInterfaceInfoById')
def getInterfaceInfoById(**kwargs):
    return CatalystClient().getInterfaceInfoById(**kwargs)

@register('getTaskByOperationId')
def getTaskByOperationId(**kwargs):
    return CatalystClient().getTaskByOperationId(**kwargs)

@register('ciscoISEServerIntegrationStatus')
def ciscoISEServerIntegrationStatus(**kwargs):
    return CatalystClient().ciscoISEServerIntegrationStatus(**kwargs)

@register('getL3TopologyDetails')
def getL3TopologyDetails(**kwargs):
    return CatalystClient().getL3TopologyDetails(**kwargs)

@register('getAdvisoryDeviceDetail')
def getAdvisoryDeviceDetail(**kwargs):
    return CatalystClient().getAdvisoryDeviceDetail(**kwargs)

@register('getConnectorTypes')
def getConnectorTypes(**kwargs):
    return CatalystClient().getConnectorTypes(**kwargs)

@register('getTasksByID')
def getTasksByID(**kwargs):
    return CatalystClient().getTasksByID(**kwargs)

@register('licenseTermDetails')
def licenseTermDetails(**kwargs):
    return CatalystClient().licenseTermDetails(**kwargs)

@register('retrieveDHCPSettingsForASite')
def retrieveDHCPSettingsForASite(**kwargs):
    return CatalystClient().retrieveDHCPSettingsForASite(**kwargs)

@register('getAnycastGatewayCount')
def getAnycastGatewayCount(**kwargs):
    return CatalystClient().getAnycastGatewayCount(**kwargs)

@register('getsTheNetworkDeviceDetailsBasedOnTheProvidedQueryParameters.')
def getsTheNetworkDeviceDetailsBasedOnTheProvidedQueryParameters_(**kwargs):
    return CatalystClient().getsTheNetworkDeviceDetailsBasedOnTheProvidedQueryParameters_(**kwargs)

@register('issues')
def issues(**kwargs):
    return CatalystClient().issues(**kwargs)

@register('getDevicesRegisteredForWSANotification')
def getDevicesRegisteredForWSANotification(**kwargs):
    return CatalystClient().getDevicesRegisteredForWSANotification(**kwargs)

@register('getInterfaceByIP')
def getInterfaceByIP(**kwargs):
    return CatalystClient().getInterfaceByIP(**kwargs)

@register('retrieveApplicableAdd-onImagesForTheGivenSoftwareImage')
def retrieveApplicableAdd_onImagesForTheGivenSoftwareImage(**kwargs):
    return CatalystClient().retrieveApplicableAdd_onImagesForTheGivenSoftwareImage(**kwargs)

@register('retrievesTheListOfClients,WhileAlsoOfferingBasicFilteringAndSortingCapabilities.')
def retrievesTheListOfClients_WhileAlsoOfferingBasicFilteringAndSortingCapabilities_(**kwargs):
    return CatalystClient().retrievesTheListOfClients_WhileAlsoOfferingBasicFilteringAndSortingCapabilities_(**kwargs)

@register('getEoXSummary')
def getEoXSummary(**kwargs):
    return CatalystClient().getEoXSummary(**kwargs)

@register('systemPerformanceAPI')
def systemPerformanceAPI(**kwargs):
    return CatalystClient().systemPerformanceAPI(**kwargs)

@register('getManagedAPLocationsCountForSpecificWirelessController')
def getManagedAPLocationsCountForSpecificWirelessController(**kwargs):
    return CatalystClient().getManagedAPLocationsCountForSpecificWirelessController(**kwargs)

@register('getNetworkDeviceByPaginationRange')
def getNetworkDeviceByPaginationRange(**kwargs):
    return CatalystClient().getNetworkDeviceByPaginationRange(**kwargs)

@register('getSiteAssignedNetworkDevice')
def getSiteAssignedNetworkDevice(**kwargs):
    return CatalystClient().getSiteAssignedNetworkDevice(**kwargs)

@register('getTheCustomIssueDefinitionForTheGivenCustomIssueDefinitionId.')
def getTheCustomIssueDefinitionForTheGivenCustomIssueDefinitionId_(**kwargs):
    return CatalystClient().getTheCustomIssueDefinitionForTheGivenCustomIssueDefinitionId_(**kwargs)

@register('getAllInterfaces')
def getAllInterfaces(**kwargs):
    return CatalystClient().getAllInterfaces(**kwargs)

@register('returnsCountOfAdd-onImages')
def returnsCountOfAdd_onImages(**kwargs):
    return CatalystClient().returnsCountOfAdd_onImages(**kwargs)

@register('getWirelessLanControllerDetailsById')
def getWirelessLanControllerDetailsById(**kwargs):
    return CatalystClient().getWirelessLanControllerDetailsById(**kwargs)

@register('ciscoDNACenterPackagesSummary')
def ciscoDNACenterPackagesSummary(**kwargs):
    return CatalystClient().ciscoDNACenterPackagesSummary(**kwargs)

@register('getRFProfilesCount')
def getRFProfilesCount(**kwargs):
    return CatalystClient().getRFProfilesCount(**kwargs)

@register('getDevicesPerAdvisory')
def getDevicesPerAdvisory(**kwargs):
    return CatalystClient().getDevicesPerAdvisory(**kwargs)

@register('getAccessPointConfigurationTaskResult')
def getAccessPointConfigurationTaskResult(**kwargs):
    return CatalystClient().getAccessPointConfigurationTaskResult(**kwargs)

@register('getComplianceDetail')
def getComplianceDetail(**kwargs):
    return CatalystClient().getComplianceDetail(**kwargs)

@register('returnsTheCountOfVLANsMappedToSSIDsInAFabricSite.')
def returnsTheCountOfVLANsMappedToSSIDsInAFabricSite_(**kwargs):
    return CatalystClient().returnsTheCountOfVLANsMappedToSSIDsInAFabricSite_(**kwargs)

@register('getGlobalCredentials')
def getGlobalCredentials(**kwargs):
    return CatalystClient().getGlobalCredentials(**kwargs)

@register('getComplianceStatus')
def getComplianceStatus(**kwargs):
    return CatalystClient().getComplianceStatus(**kwargs)

@register('getSNMPDestination')
def getSNMPDestination(**kwargs):
    return CatalystClient().getSNMPDestination(**kwargs)

@register('getProvisionedDevicesCount')
def getProvisionedDevicesCount(**kwargs):
    return CatalystClient().getProvisionedDevicesCount(**kwargs)

@register('returnsListOfSoftwareImages')
def returnsListOfSoftwareImages(**kwargs):
    return CatalystClient().returnsListOfSoftwareImages(**kwargs)

@register('getInterfacesCount')
def getInterfacesCount(**kwargs):
    return CatalystClient().getInterfacesCount(**kwargs)

@register('readListOfSiteHealthSummaries.')
def readListOfSiteHealthSummaries_(**kwargs):
    return CatalystClient().readListOfSiteHealthSummaries_(**kwargs)

@register('getDeviceList-2')
def getDeviceList_2(**kwargs):
    return CatalystClient().getDeviceList_2(**kwargs)

@register('getTasks-2')
def getTasks_2(**kwargs):
    return CatalystClient().getTasks_2(**kwargs)

@register('getModules')
def getModules(**kwargs):
    return CatalystClient().getModules(**kwargs)

@register('retrievesTheCountOfAssignedNetworkDeviceProducts')
def retrievesTheCountOfAssignedNetworkDeviceProducts(**kwargs):
    return CatalystClient().retrievesTheCountOfAssignedNetworkDeviceProducts(**kwargs)

@register('getRest/WebhookSubscriptionDetails')
def getRest_WebhookSubscriptionDetails(**kwargs):
    return CatalystClient().getRest_WebhookSubscriptionDetails(**kwargs)

@register('getDeviceHistory')
def getDeviceHistory(**kwargs):
    return CatalystClient().getDeviceHistory(**kwargs)

@register('getApplicationPolicyQueuingProfileCount')
def getApplicationPolicyQueuingProfileCount(**kwargs):
    return CatalystClient().getApplicationPolicyQueuingProfileCount(**kwargs)

@register('getsTheTotalNetworkDeviceCountsBasedOnTheProvidedQueryParameters.')
def getsTheTotalNetworkDeviceCountsBasedOnTheProvidedQueryParameters_(**kwargs):
    return CatalystClient().getsTheTotalNetworkDeviceCountsBasedOnTheProvidedQueryParameters_(**kwargs)

@register('getTaskTree')
def getTaskTree(**kwargs):
    return CatalystClient().getTaskTree(**kwargs)

@register('getDiscoveredNetworkDevicesByDiscoveryId')
def getDiscoveredNetworkDevicesByDiscoveryId(**kwargs):
    return CatalystClient().getDiscoveredNetworkDevicesByDiscoveryId(**kwargs)

@register('getStatusAPIForEvents')
def getStatusAPIForEvents(**kwargs):
    return CatalystClient().getStatusAPIForEvents(**kwargs)

@register('getSiteAssignedNetworkDevicesCount')
def getSiteAssignedNetworkDevicesCount(**kwargs):
    return CatalystClient().getSiteAssignedNetworkDevicesCount(**kwargs)

@register('getNetworkV2')
def getNetworkV2(**kwargs):
    return CatalystClient().getNetworkV2(**kwargs)

@register('getDeviceValuesThatMatchFullyOrPartiallyAnAttribute')
def getDeviceValuesThatMatchFullyOrPartiallyAnAttribute(**kwargs):
    return CatalystClient().getDeviceValuesThatMatchFullyOrPartiallyAnAttribute(**kwargs)

@register('sensors')
def sensors(**kwargs):
    return CatalystClient().sensors(**kwargs)

@register('getDeviceInfoFromSDAFabric')
def getDeviceInfoFromSDAFabric(**kwargs):
    return CatalystClient().getDeviceInfoFromSDAFabric(**kwargs)

@register('getPortAssignmentForAccessPointInSDAFabric')
def getPortAssignmentForAccessPointInSDAFabric(**kwargs):
    return CatalystClient().getPortAssignmentForAccessPointInSDAFabric(**kwargs)

@register('getIPPoolFromSDAVirtualNetwork')
def getIPPoolFromSDAVirtualNetwork(**kwargs):
    return CatalystClient().getIPPoolFromSDAVirtualNetwork(**kwargs)

@register('getEdgeDeviceFromSDAFabric')
def getEdgeDeviceFromSDAFabric(**kwargs):
    return CatalystClient().getEdgeDeviceFromSDAFabric(**kwargs)

@register('getMulticastDetailsFromSDAFabric')
def getMulticastDetailsFromSDAFabric(**kwargs):
    return CatalystClient().getMulticastDetailsFromSDAFabric(**kwargs)

@register('getApplications')
def getApplications(**kwargs):
    return CatalystClient().getApplications(**kwargs)

@register('retrieveRFProfiles')
def retrieveRFProfiles(**kwargs):
    return CatalystClient().retrieveRFProfiles(**kwargs)

@register('getNetwork')
def getNetwork(**kwargs):
    return CatalystClient().getNetwork(**kwargs)

@register('getReserveIPSubpool')
def getReserveIPSubpool(**kwargs):
    return CatalystClient().getReserveIPSubpool(**kwargs)

@register('getTransitPeerNetworkInfo')
def getTransitPeerNetworkInfo(**kwargs):
    return CatalystClient().getTransitPeerNetworkInfo(**kwargs)

@register('clientProximity')
def clientProximity(**kwargs):
    return CatalystClient().clientProximity(**kwargs)

@register('applications')
def applications(**kwargs):
    return CatalystClient().applications(**kwargs)

@register('getApplicationSets')
def getApplicationSets(**kwargs):
    return CatalystClient().getApplicationSets(**kwargs)

@register('getApplicationsCount')
def getApplicationsCount(**kwargs):
    return CatalystClient().getApplicationsCount(**kwargs)

@register('getGlobalPool')
def getGlobalPool(**kwargs):
    return CatalystClient().getGlobalPool(**kwargs)

@register('getVNFromSDAFabric')
def getVNFromSDAFabric(**kwargs):
    return CatalystClient().getVNFromSDAFabric(**kwargs)

@register('getDefaultAuthenticationProfileFromSDAFabric')
def getDefaultAuthenticationProfileFromSDAFabric(**kwargs):
    return CatalystClient().getDefaultAuthenticationProfileFromSDAFabric(**kwargs)

@register('getProvisionedWiredDevice')
def getProvisionedWiredDevice(**kwargs):
    return CatalystClient().getProvisionedWiredDevice(**kwargs)

@register('getDeviceCredentialDetails')
def getDeviceCredentialDetails(**kwargs):
    return CatalystClient().getDeviceCredentialDetails(**kwargs)

@register('getSiteFromSDAFabric')
def getSiteFromSDAFabric(**kwargs):
    return CatalystClient().getSiteFromSDAFabric(**kwargs)

@register('getServiceProviderDetails')
def getServiceProviderDetails(**kwargs):
    return CatalystClient().getServiceProviderDetails(**kwargs)

@register('getSite')
def getSite(**kwargs):
    return CatalystClient().getSite(**kwargs)

@register('getVirtualNetworkSummary')
def getVirtualNetworkSummary(**kwargs):
    return CatalystClient().getVirtualNetworkSummary(**kwargs)

@register('getWirelessProfile')
def getWirelessProfile(**kwargs):
    return CatalystClient().getWirelessProfile(**kwargs)

@register('getIssueEnrichmentDetails')
def getIssueEnrichmentDetails(**kwargs):
    return CatalystClient().getIssueEnrichmentDetails(**kwargs)

@register('sensorTestResults')
def sensorTestResults(**kwargs):
    return CatalystClient().sensorTestResults(**kwargs)

@register('getDeviceRoleInSDAFabric')
def getDeviceRoleInSDAFabric(**kwargs):
    return CatalystClient().getDeviceRoleInSDAFabric(**kwargs)

@register('getEnterpriseSSID')
def getEnterpriseSSID(**kwargs):
    return CatalystClient().getEnterpriseSSID(**kwargs)

@register('getBorderDeviceDetailFromSDAFabric')
def getBorderDeviceDetailFromSDAFabric(**kwargs):
    return CatalystClient().getBorderDeviceDetailFromSDAFabric(**kwargs)

@register('getPortAssignmentForUserDeviceInSDAFabric')
def getPortAssignmentForUserDeviceInSDAFabric(**kwargs):
    return CatalystClient().getPortAssignmentForUserDeviceInSDAFabric(**kwargs)

@register('getFailedITSMEvents')
def getFailedITSMEvents(**kwargs):
    return CatalystClient().getFailedITSMEvents(**kwargs)

@register('getSSIDToIPPoolMapping')
def getSSIDToIPPoolMapping(**kwargs):
    return CatalystClient().getSSIDToIPPoolMapping(**kwargs)

@register('getControlPlaneDeviceFromSDAFabric')
def getControlPlaneDeviceFromSDAFabric(**kwargs):
    return CatalystClient().getControlPlaneDeviceFromSDAFabric(**kwargs)

@register('getCMDBSyncStatus')
def getCMDBSyncStatus(**kwargs):
    return CatalystClient().getCMDBSyncStatus(**kwargs)

@register('getSiteCount')
def getSiteCount(**kwargs):
    return CatalystClient().getSiteCount(**kwargs)

@register('getClientEnrichmentDetails')
def getClientEnrichmentDetails(**kwargs):
    return CatalystClient().getClientEnrichmentDetails(**kwargs)

@register('getVirtualNetworkWithScalableGroups')
def getVirtualNetworkWithScalableGroups(**kwargs):
    return CatalystClient().getVirtualNetworkWithScalableGroups(**kwargs)

@register('getDynamicInterface')
def getDynamicInterface(**kwargs):
    return CatalystClient().getDynamicInterface(**kwargs)

@register('getApplicationSetsCount')
def getApplicationSetsCount(**kwargs):
    return CatalystClient().getApplicationSetsCount(**kwargs)

@register('getUserEnrichmentDetails')
def getUserEnrichmentDetails(**kwargs):
    return CatalystClient().getUserEnrichmentDetails(**kwargs)

@register('getDeviceEnrichmentDetails')
def getDeviceEnrichmentDetails(**kwargs):
    return CatalystClient().getDeviceEnrichmentDetails(**kwargs)

@register('getMembership')
def getMembership(**kwargs):
    return CatalystClient().getMembership(**kwargs)
