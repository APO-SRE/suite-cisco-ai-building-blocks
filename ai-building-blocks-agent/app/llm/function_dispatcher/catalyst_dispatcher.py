# app/llm/function_dispatcher/catalyst_dispatcher.py
from app.llm.function_dispatcher import register
from app.llm.platform_clients.catalyst_client import CatalystClient

@register('assignNetworkDeviceProductNameToTheGivenSoftwareImage')
def assignNetworkDeviceProductNameToTheGivenSoftwareImage(**kwargs):
    return CatalystClient().assignNetworkDeviceProductNameToTheGivenSoftwareImage(**kwargs)

@register('retrievesNetworkDeviceProductNamesAssignedToASoftwareImage.')
def retrievesNetworkDeviceProductNamesAssignedToASoftwareImage_(**kwargs):
    return CatalystClient().retrievesNetworkDeviceProductNamesAssignedToASoftwareImage_(**kwargs)

@register('getsAllTheVersionsOfAGivenTemplate')
def getsAllTheVersionsOfAGivenTemplate(**kwargs):
    return CatalystClient().getsAllTheVersionsOfAGivenTemplate(**kwargs)

@register('configureAccessPointsV1')
def configureAccessPointsV1(**kwargs):
    return CatalystClient().configureAccessPointsV1(**kwargs)

@register('deployTemplateV2')
def deployTemplateV2(**kwargs):
    return CatalystClient().deployTemplateV2(**kwargs)

@register('returnsTheCountOfNetworkDeviceProductNamesForASite')
def returnsTheCountOfNetworkDeviceProductNamesForASite(**kwargs):
    return CatalystClient().returnsTheCountOfNetworkDeviceProductNamesForASite(**kwargs)

@register('getMulticastVirtualNetworks')
def getMulticastVirtualNetworks(**kwargs):
    return CatalystClient().getMulticastVirtualNetworks(**kwargs)

@register('addMulticastVirtualNetworks')
def addMulticastVirtualNetworks(**kwargs):
    return CatalystClient().addMulticastVirtualNetworks(**kwargs)

@register('updateMulticastVirtualNetworks')
def updateMulticastVirtualNetworks(**kwargs):
    return CatalystClient().updateMulticastVirtualNetworks(**kwargs)

@register('theTrendAnalyticsDataForTheNetworkDeviceInTheSpecifiedTimeRange')
def theTrendAnalyticsDataForTheNetworkDeviceInTheSpecifiedTimeRange(**kwargs):
    return CatalystClient().theTrendAnalyticsDataForTheNetworkDeviceInTheSpecifiedTimeRange(**kwargs)

@register('getDeviceControllabilitySettings')
def getDeviceControllabilitySettings(**kwargs):
    return CatalystClient().getDeviceControllabilitySettings(**kwargs)

@register('updateDeviceControllabilitySettings')
def updateDeviceControllabilitySettings(**kwargs):
    return CatalystClient().updateDeviceControllabilitySettings(**kwargs)

@register('getChassisDetailsForDevice')
def getChassisDetailsForDevice(**kwargs):
    return CatalystClient().getChassisDetailsForDevice(**kwargs)

@register('updatesABuilding')
def updatesABuilding(**kwargs):
    return CatalystClient().updatesABuilding(**kwargs)

@register('deletesABuilding')
def deletesABuilding(**kwargs):
    return CatalystClient().deletesABuilding(**kwargs)

@register('getsABuilding')
def getsABuilding(**kwargs):
    return CatalystClient().getsABuilding(**kwargs)

@register('unassignNetworkDevicesFromSites')
def unassignNetworkDevicesFromSites(**kwargs):
    return CatalystClient().unassignNetworkDevicesFromSites(**kwargs)

@register('getCountOfAllDiscoveryJobs')
def getCountOfAllDiscoveryJobs(**kwargs):
    return CatalystClient().getCountOfAllDiscoveryJobs(**kwargs)

@register('getViewsForAGivenViewGroup')
def getViewsForAGivenViewGroup(**kwargs):
    return CatalystClient().getViewsForAGivenViewGroup(**kwargs)

@register('updateDevice')
def updateDevice(**kwargs):
    return CatalystClient().updateDevice(**kwargs)

@register('getDeviceById')
def getDeviceById(**kwargs):
    return CatalystClient().getDeviceById(**kwargs)

@register('deleteDeviceByIdFromPnP')
def deleteDeviceByIdFromPnP(**kwargs):
    return CatalystClient().deleteDeviceByIdFromPnP(**kwargs)

@register('add,UpdateOrRemoveSSIDMappingToAVLAN')
def add_UpdateOrRemoveSSIDMappingToAVLAN(**kwargs):
    return CatalystClient().add_UpdateOrRemoveSSIDMappingToAVLAN(**kwargs)

@register('retrieveTheVLANsAndSSIDsMappedToTheVLANWithinAFabricSite.')
def retrieveTheVLANsAndSSIDsMappedToTheVLANWithinAFabricSite_(**kwargs):
    return CatalystClient().retrieveTheVLANsAndSSIDsMappedToTheVLANWithinAFabricSite_(**kwargs)

@register('addImageDistributionServer')
def addImageDistributionServer(**kwargs):
    return CatalystClient().addImageDistributionServer(**kwargs)

@register('retrieveImageDistributionServers')
def retrieveImageDistributionServers(**kwargs):
    return CatalystClient().retrieveImageDistributionServers(**kwargs)

@register('deleteApplicationPolicyQueuingProfile')
def deleteApplicationPolicyQueuingProfile(**kwargs):
    return CatalystClient().deleteApplicationPolicyQueuingProfile(**kwargs)

@register('retrieveTagsAssociatedWithNetworkDevices.')
def retrieveTagsAssociatedWithNetworkDevices_(**kwargs):
    return CatalystClient().retrieveTagsAssociatedWithNetworkDevices_(**kwargs)

@register('statusOfTemplateDeployment')
def statusOfTemplateDeployment(**kwargs):
    return CatalystClient().statusOfTemplateDeployment(**kwargs)

@register('un-ClaimDevice')
def un_ClaimDevice(**kwargs):
    return CatalystClient().un_ClaimDevice(**kwargs)

@register('createITSMIntegrationSetting')
def createITSMIntegrationSetting(**kwargs):
    return CatalystClient().createITSMIntegrationSetting(**kwargs)

@register('issueTriggerDefinitionUpdate.')
def issueTriggerDefinitionUpdate_(**kwargs):
    return CatalystClient().issueTriggerDefinitionUpdate_(**kwargs)

@register('getIssueTriggerDefinitionForGivenId.')
def getIssueTriggerDefinitionForGivenId_(**kwargs):
    return CatalystClient().getIssueTriggerDefinitionForGivenId_(**kwargs)

@register('getsTheTrendAnalyticsData.')
def getsTheTrendAnalyticsData_(**kwargs):
    return CatalystClient().getsTheTrendAnalyticsData_(**kwargs)

@register('setBannerSettingsForASite')
def setBannerSettingsForASite(**kwargs):
    return CatalystClient().setBannerSettingsForASite(**kwargs)

@register('retrieveBannerSettingsForASite')
def retrieveBannerSettingsForASite(**kwargs):
    return CatalystClient().retrieveBannerSettingsForASite(**kwargs)

@register('getSiteAssignedNetworkDevices')
def getSiteAssignedNetworkDevices(**kwargs):
    return CatalystClient().getSiteAssignedNetworkDevices(**kwargs)

@register('createSNMPDestination')
def createSNMPDestination(**kwargs):
    return CatalystClient().createSNMPDestination(**kwargs)

@register('updateSNMPDestination')
def updateSNMPDestination(**kwargs):
    return CatalystClient().updateSNMPDestination(**kwargs)

@register('getNetworkDevicesCredentialsSyncStatus')
def getNetworkDevicesCredentialsSyncStatus(**kwargs):
    return CatalystClient().getNetworkDevicesCredentialsSyncStatus(**kwargs)

@register('getSoftwareImageDetails')
def getSoftwareImageDetails(**kwargs):
    return CatalystClient().getSoftwareImageDetails(**kwargs)

@register('updateInterface')
def updateInterface(**kwargs):
    return CatalystClient().updateInterface(**kwargs)

@register('deleteInterface')
def deleteInterface(**kwargs):
    return CatalystClient().deleteInterface(**kwargs)

@register('getInterfaceByID')
def getInterfaceByID(**kwargs):
    return CatalystClient().getInterfaceByID(**kwargs)

@register('updateAnycastGateways')
def updateAnycastGateways(**kwargs):
    return CatalystClient().updateAnycastGateways(**kwargs)

@register('getAnycastGateways')
def getAnycastGateways(**kwargs):
    return CatalystClient().getAnycastGateways(**kwargs)

@register('addAnycastGateways')
def addAnycastGateways(**kwargs):
    return CatalystClient().addAnycastGateways(**kwargs)

@register('getApplicationSet/s')
def getApplicationSet_s(**kwargs):
    return CatalystClient().getApplicationSet_s(**kwargs)

@register('createApplicationSet/s')
def createApplicationSet_s(**kwargs):
    return CatalystClient().createApplicationSet_s(**kwargs)

@register('addMembersToTheTag')
def addMembersToTheTag(**kwargs):
    return CatalystClient().addMembersToTheTag(**kwargs)

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

@register('assignANetworkProfileForSitesToTheGivenSite')
def assignANetworkProfileForSitesToTheGivenSite(**kwargs):
    return CatalystClient().assignANetworkProfileForSitesToTheGivenSite(**kwargs)

@register('getFabricDevicesLayer2HandoffsCount')
def getFabricDevicesLayer2HandoffsCount(**kwargs):
    return CatalystClient().getFabricDevicesLayer2HandoffsCount(**kwargs)

@register('aPProvision')
def aPProvision(**kwargs):
    return CatalystClient().aPProvision(**kwargs)

@register('countOfEventSubscriptions')
def countOfEventSubscriptions(**kwargs):
    return CatalystClient().countOfEventSubscriptions(**kwargs)

@register('createSSID')
def createSSID(**kwargs):
    return CatalystClient().createSSID(**kwargs)

@register('getSSIDBySite')
def getSSIDBySite(**kwargs):
    return CatalystClient().getSSIDBySite(**kwargs)

@register('getITSMIntegrationSettingById')
def getITSMIntegrationSettingById(**kwargs):
    return CatalystClient().getITSMIntegrationSettingById(**kwargs)

@register('updateITSMIntegrationSetting')
def updateITSMIntegrationSetting(**kwargs):
    return CatalystClient().updateITSMIntegrationSetting(**kwargs)

@register('deleteITSMIntegrationSetting')
def deleteITSMIntegrationSetting(**kwargs):
    return CatalystClient().deleteITSMIntegrationSetting(**kwargs)

@register('getDetailsOfASingleAssuranceEvent')
def getDetailsOfASingleAssuranceEvent(**kwargs):
    return CatalystClient().getDetailsOfASingleAssuranceEvent(**kwargs)

@register('importLocalSoftwareImage')
def importLocalSoftwareImage(**kwargs):
    return CatalystClient().importLocalSoftwareImage(**kwargs)

@register('createsACloneOfTheGivenTemplate')
def createsACloneOfTheGivenTemplate(**kwargs):
    return CatalystClient().createsACloneOfTheGivenTemplate(**kwargs)

@register('getRFProfiles')
def getRFProfiles(**kwargs):
    return CatalystClient().getRFProfiles(**kwargs)

@register('createRFProfile')
def createRFProfile(**kwargs):
    return CatalystClient().createRFProfile(**kwargs)

@register('retrieveTelemetrySettingsForASite')
def retrieveTelemetrySettingsForASite(**kwargs):
    return CatalystClient().retrieveTelemetrySettingsForASite(**kwargs)

@register('setTelemetrySettingsForASite')
def setTelemetrySettingsForASite(**kwargs):
    return CatalystClient().setTelemetrySettingsForASite(**kwargs)

@register('getAllUser-Defined-Fields')
def getAllUser_Defined_Fields(**kwargs):
    return CatalystClient().getAllUser_Defined_Fields(**kwargs)

@register('createUser-Defined-Field')
def createUser_Defined_Field(**kwargs):
    return CatalystClient().createUser_Defined_Field(**kwargs)

@register('queryAssuranceEvents')
def queryAssuranceEvents(**kwargs):
    return CatalystClient().queryAssuranceEvents(**kwargs)

@register('updatesFloorSettings')
def updatesFloorSettings(**kwargs):
    return CatalystClient().updatesFloorSettings(**kwargs)

@register('getFloorSettings')
def getFloorSettings(**kwargs):
    return CatalystClient().getFloorSettings(**kwargs)

@register('getTheTotalNumberOfIssuesForGivenSetOfFilters')
def getTheTotalNumberOfIssuesForGivenSetOfFilters(**kwargs):
    return CatalystClient().getTheTotalNumberOfIssuesForGivenSetOfFilters(**kwargs)

@register('createTag')
def createTag(**kwargs):
    return CatalystClient().createTag(**kwargs)

@register('updateTag')
def updateTag(**kwargs):
    return CatalystClient().updateTag(**kwargs)

@register('getTag')
def getTag(**kwargs):
    return CatalystClient().getTag(**kwargs)

@register('lANAutomationStopAndUpdateDevices')
def lANAutomationStopAndUpdateDevices(**kwargs):
    return CatalystClient().lANAutomationStopAndUpdateDevices(**kwargs)

@register('lANAutomationStop')
def lANAutomationStop(**kwargs):
    return CatalystClient().lANAutomationStop(**kwargs)

@register('updateLayer2VirtualNetworks')
def updateLayer2VirtualNetworks(**kwargs):
    return CatalystClient().updateLayer2VirtualNetworks(**kwargs)

@register('getLayer2VirtualNetworks')
def getLayer2VirtualNetworks(**kwargs):
    return CatalystClient().getLayer2VirtualNetworks(**kwargs)

@register('deleteLayer2VirtualNetworks')
def deleteLayer2VirtualNetworks(**kwargs):
    return CatalystClient().deleteLayer2VirtualNetworks(**kwargs)

@register('addLayer2VirtualNetworks')
def addLayer2VirtualNetworks(**kwargs):
    return CatalystClient().addLayer2VirtualNetworks(**kwargs)

@register('getFabricZoneCount')
def getFabricZoneCount(**kwargs):
    return CatalystClient().getFabricZoneCount(**kwargs)

@register('updateWebhookDestination')
def updateWebhookDestination(**kwargs):
    return CatalystClient().updateWebhookDestination(**kwargs)

@register('getWebhookDestination')
def getWebhookDestination(**kwargs):
    return CatalystClient().getWebhookDestination(**kwargs)

@register('createWebhookDestination')
def createWebhookDestination(**kwargs):
    return CatalystClient().createWebhookDestination(**kwargs)

@register('setTimeZoneForASite')
def setTimeZoneForASite(**kwargs):
    return CatalystClient().setTimeZoneForASite(**kwargs)

@register('retrieveTimeZoneSettingsForASite')
def retrieveTimeZoneSettingsForASite(**kwargs):
    return CatalystClient().retrieveTimeZoneSettingsForASite(**kwargs)

@register('deleteDeviceById')
def deleteDeviceById(**kwargs):
    return CatalystClient().deleteDeviceById(**kwargs)

@register('getDeviceByID')
def getDeviceByID(**kwargs):
    return CatalystClient().getDeviceByID(**kwargs)

@register('getApplicationPolicyQueuingProfile')
def getApplicationPolicyQueuingProfile(**kwargs):
    return CatalystClient().getApplicationPolicyQueuingProfile(**kwargs)

@register('createApplicationPolicyQueuingProfile')
def createApplicationPolicyQueuingProfile(**kwargs):
    return CatalystClient().createApplicationPolicyQueuingProfile(**kwargs)

@register('updateApplicationPolicyQueuingProfile')
def updateApplicationPolicyQueuingProfile(**kwargs):
    return CatalystClient().updateApplicationPolicyQueuingProfile(**kwargs)

@register('createSyslogDestination')
def createSyslogDestination(**kwargs):
    return CatalystClient().createSyslogDestination(**kwargs)

@register('getSyslogDestination')
def getSyslogDestination(**kwargs):
    return CatalystClient().getSyslogDestination(**kwargs)

@register('updateSyslogDestination')
def updateSyslogDestination(**kwargs):
    return CatalystClient().updateSyslogDestination(**kwargs)

@register('getAll802.11beProfiles')
def getAll802_11beProfiles(**kwargs):
    return CatalystClient().getAll802_11beProfiles(**kwargs)

@register('createA802.11beProfile')
def createA802_11beProfile(**kwargs):
    return CatalystClient().createA802_11beProfile(**kwargs)

@register('getSyncResultForVirtualAccount')
def getSyncResultForVirtualAccount(**kwargs):
    return CatalystClient().getSyncResultForVirtualAccount(**kwargs)

@register('addVirtualAccount')
def addVirtualAccount(**kwargs):
    return CatalystClient().addVirtualAccount(**kwargs)

@register('updatePnPServerProfile')
def updatePnPServerProfile(**kwargs):
    return CatalystClient().updatePnPServerProfile(**kwargs)

@register('getAllTheCustomIssueDefinitionsBasedOnTheGivenFilters.')
def getAllTheCustomIssueDefinitionsBasedOnTheGivenFilters_(**kwargs):
    return CatalystClient().getAllTheCustomIssueDefinitionsBasedOnTheGivenFilters_(**kwargs)

@register('createsANewUser-definedIssueDefinitions.')
def createsANewUser_definedIssueDefinitions_(**kwargs):
    return CatalystClient().createsANewUser_definedIssueDefinitions_(**kwargs)

@register('deployTemplate')
def deployTemplate(**kwargs):
    return CatalystClient().deployTemplate(**kwargs)

@register('deleteAuthenticationAndPolicyServerAccessConfiguration')
def deleteAuthenticationAndPolicyServerAccessConfiguration(**kwargs):
    return CatalystClient().deleteAuthenticationAndPolicyServerAccessConfiguration(**kwargs)

@register('editAuthenticationAndPolicyServerAccessConfiguration')
def editAuthenticationAndPolicyServerAccessConfiguration(**kwargs):
    return CatalystClient().editAuthenticationAndPolicyServerAccessConfiguration(**kwargs)

@register('deleteMulticastVirtualNetworkById')
def deleteMulticastVirtualNetworkById(**kwargs):
    return CatalystClient().deleteMulticastVirtualNetworkById(**kwargs)

@register('getApplicationPolicyDefault')
def getApplicationPolicyDefault(**kwargs):
    return CatalystClient().getApplicationPolicyDefault(**kwargs)

@register('getPrimaryManagedAPLocationsForSpecificWirelessController')
def getPrimaryManagedAPLocationsForSpecificWirelessController(**kwargs):
    return CatalystClient().getPrimaryManagedAPLocationsForSpecificWirelessController(**kwargs)

@register('getModuleInfoById')
def getModuleInfoById(**kwargs):
    return CatalystClient().getModuleInfoById(**kwargs)

@register('updateHealthScoreDefinitions.')
def updateHealthScoreDefinitions_(**kwargs):
    return CatalystClient().updateHealthScoreDefinitions_(**kwargs)

@register('getFabricDevicesLayer3HandoffsWithSdaTransit')
def getFabricDevicesLayer3HandoffsWithSdaTransit(**kwargs):
    return CatalystClient().getFabricDevicesLayer3HandoffsWithSdaTransit(**kwargs)

@register('addFabricDevicesLayer3HandoffsWithSdaTransit')
def addFabricDevicesLayer3HandoffsWithSdaTransit(**kwargs):
    return CatalystClient().addFabricDevicesLayer3HandoffsWithSdaTransit(**kwargs)

@register('deleteFabricDeviceLayer3HandoffsWithSdaTransit')
def deleteFabricDeviceLayer3HandoffsWithSdaTransit(**kwargs):
    return CatalystClient().deleteFabricDeviceLayer3HandoffsWithSdaTransit(**kwargs)

@register('updateFabricDevicesLayer3HandoffsWithSdaTransit')
def updateFabricDevicesLayer3HandoffsWithSdaTransit(**kwargs):
    return CatalystClient().updateFabricDevicesLayer3HandoffsWithSdaTransit(**kwargs)

@register('addFabricDevicesLayer3HandoffsWithIpTransit')
def addFabricDevicesLayer3HandoffsWithIpTransit(**kwargs):
    return CatalystClient().addFabricDevicesLayer3HandoffsWithIpTransit(**kwargs)

@register('deleteFabricDeviceLayer3HandoffsWithIpTransit')
def deleteFabricDeviceLayer3HandoffsWithIpTransit(**kwargs):
    return CatalystClient().deleteFabricDeviceLayer3HandoffsWithIpTransit(**kwargs)

@register('getFabricDevicesLayer3HandoffsWithIpTransit')
def getFabricDevicesLayer3HandoffsWithIpTransit(**kwargs):
    return CatalystClient().getFabricDevicesLayer3HandoffsWithIpTransit(**kwargs)

@register('updateFabricDevicesLayer3HandoffsWithIpTransit')
def updateFabricDevicesLayer3HandoffsWithIpTransit(**kwargs):
    return CatalystClient().updateFabricDevicesLayer3HandoffsWithIpTransit(**kwargs)

@register('returnsNetworkDeviceProductNamesForASite')
def returnsNetworkDeviceProductNamesForASite(**kwargs):
    return CatalystClient().returnsNetworkDeviceProductNamesForASite(**kwargs)

@register('countOfNotifications')
def countOfNotifications(**kwargs):
    return CatalystClient().countOfNotifications(**kwargs)

@register('updateTheListOfSitesForTheNetworkDeviceProductNameAssignedToTheSoftwareImage')
def updateTheListOfSitesForTheNetworkDeviceProductNameAssignedToTheSoftwareImage(**kwargs):
    return CatalystClient().updateTheListOfSitesForTheNetworkDeviceProductNameAssignedToTheSoftwareImage(**kwargs)

@register('unassignNetworkDeviceProductNameFromTheGivenSoftwareImage')
def unassignNetworkDeviceProductNameFromTheGivenSoftwareImage(**kwargs):
    return CatalystClient().unassignNetworkDeviceProductNameFromTheGivenSoftwareImage(**kwargs)

@register('assignDeviceCredentialToSiteV2')
def assignDeviceCredentialToSiteV2(**kwargs):
    return CatalystClient().assignDeviceCredentialToSiteV2(**kwargs)

@register('deleteAScheduledReport')
def deleteAScheduledReport(**kwargs):
    return CatalystClient().deleteAScheduledReport(**kwargs)

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

@register('submitsTheWorkflowForExecutingValidations')
def submitsTheWorkflowForExecutingValidations(**kwargs):
    return CatalystClient().submitsTheWorkflowForExecutingValidations(**kwargs)

@register('clearMac-AddressTable')
def clearMac_AddressTable(**kwargs):
    return CatalystClient().clearMac_AddressTable(**kwargs)

@register('getsTheTotalNumberNetworkDevicesBasedOnTheProvidedComplexFiltersAndAggregationFunctions.')
def getsTheTotalNumberNetworkDevicesBasedOnTheProvidedComplexFiltersAndAggregationFunctions_(**kwargs):
    return CatalystClient().getsTheTotalNumberNetworkDevicesBasedOnTheProvidedComplexFiltersAndAggregationFunctions_(**kwargs)

@register('lANAutomationDeviceUpdate')
def lANAutomationDeviceUpdate(**kwargs):
    return CatalystClient().lANAutomationDeviceUpdate(**kwargs)

@register('updateSNMPWriteCommunity')
def updateSNMPWriteCommunity(**kwargs):
    return CatalystClient().updateSNMPWriteCommunity(**kwargs)

@register('createSNMPWriteCommunity')
def createSNMPWriteCommunity(**kwargs):
    return CatalystClient().createSNMPWriteCommunity(**kwargs)

@register('queryAnAggregatedSummaryOfSiteHealthData.')
def queryAnAggregatedSummaryOfSiteHealthData_(**kwargs):
    return CatalystClient().queryAnAggregatedSummaryOfSiteHealthData_(**kwargs)

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

@register('addExtranetPolicy')
def addExtranetPolicy(**kwargs):
    return CatalystClient().addExtranetPolicy(**kwargs)

@register('getExtranetPolicies')
def getExtranetPolicies(**kwargs):
    return CatalystClient().getExtranetPolicies(**kwargs)

@register('updateExtranetPolicy')
def updateExtranetPolicy(**kwargs):
    return CatalystClient().updateExtranetPolicy(**kwargs)

@register('deleteExtranetPolicies')
def deleteExtranetPolicies(**kwargs):
    return CatalystClient().deleteExtranetPolicies(**kwargs)

@register('importCertificate')
def importCertificate(**kwargs):
    return CatalystClient().importCertificate(**kwargs)

@register('deleteWirelessProfile')
def deleteWirelessProfile(**kwargs):
    return CatalystClient().deleteWirelessProfile(**kwargs)

@register('updateWirelessProfile')
def updateWirelessProfile(**kwargs):
    return CatalystClient().updateWirelessProfile(**kwargs)

@register('getWirelessProfileByID')
def getWirelessProfileByID(**kwargs):
    return CatalystClient().getWirelessProfileByID(**kwargs)

@register('updateADevice(s)TelemetrySettingsToConformToTheTelemetrySettingsForItsSite')
def updateADevice_s_TelemetrySettingsToConformToTheTelemetrySettingsForItsSite(**kwargs):
    return CatalystClient().updateADevice_s_TelemetrySettingsToConformToTheTelemetrySettingsForItsSite(**kwargs)

@register('getFlexibleReportScheduleByReportId')
def getFlexibleReportScheduleByReportId(**kwargs):
    return CatalystClient().getFlexibleReportScheduleByReportId(**kwargs)

@register('updateScheduleOfFlexibleReport')
def updateScheduleOfFlexibleReport(**kwargs):
    return CatalystClient().updateScheduleOfFlexibleReport(**kwargs)

@register('authorizeDevice')
def authorizeDevice(**kwargs):
    return CatalystClient().authorizeDevice(**kwargs)

@register('addPortChannels')
def addPortChannels(**kwargs):
    return CatalystClient().addPortChannels(**kwargs)

@register('getPortChannels')
def getPortChannels(**kwargs):
    return CatalystClient().getPortChannels(**kwargs)

@register('updatePortChannels')
def updatePortChannels(**kwargs):
    return CatalystClient().updatePortChannels(**kwargs)

@register('deletePortChannels')
def deletePortChannels(**kwargs):
    return CatalystClient().deletePortChannels(**kwargs)

@register('uploadFile')
def uploadFile(**kwargs):
    return CatalystClient().uploadFile(**kwargs)

@register('getsTheSummaryAnalyticsDataRelatedToNetworkDevices.')
def getsTheSummaryAnalyticsDataRelatedToNetworkDevices_(**kwargs):
    return CatalystClient().getsTheSummaryAnalyticsDataRelatedToNetworkDevices_(**kwargs)

@register('deleteRFProfile')
def deleteRFProfile(**kwargs):
    return CatalystClient().deleteRFProfile(**kwargs)

@register('getRFProfileByID')
def getRFProfileByID(**kwargs):
    return CatalystClient().getRFProfileByID(**kwargs)

@register('updateRFProfile')
def updateRFProfile(**kwargs):
    return CatalystClient().updateRFProfile(**kwargs)

@register('createNetconfCredentials')
def createNetconfCredentials(**kwargs):
    return CatalystClient().createNetconfCredentials(**kwargs)

@register('updateNetconfCredentials')
def updateNetconfCredentials(**kwargs):
    return CatalystClient().updateNetconfCredentials(**kwargs)

@register('updateTemplate')
def updateTemplate(**kwargs):
    return CatalystClient().updateTemplate(**kwargs)

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

@register('createOrScheduleAReport')
def createOrScheduleAReport(**kwargs):
    return CatalystClient().createOrScheduleAReport(**kwargs)

@register('getAAAAttributeAPI')
def getAAAAttributeAPI(**kwargs):
    return CatalystClient().getAAAAttributeAPI(**kwargs)

@register('addAndUpdateAAAAttributeAPI')
def addAndUpdateAAAAttributeAPI(**kwargs):
    return CatalystClient().addAndUpdateAAAAttributeAPI(**kwargs)

@register('deleteAAAAttributeAPI')
def deleteAAAAttributeAPI(**kwargs):
    return CatalystClient().deleteAAAAttributeAPI(**kwargs)

@register('getClientDetail')
def getClientDetail(**kwargs):
    return CatalystClient().getClientDetail(**kwargs)

@register('countTheNumberOfEvents')
def countTheNumberOfEvents(**kwargs):
    return CatalystClient().countTheNumberOfEvents(**kwargs)

@register('updateSNMPv3Credentials')
def updateSNMPv3Credentials(**kwargs):
    return CatalystClient().updateSNMPv3Credentials(**kwargs)

@register('createSNMPv3Credentials')
def createSNMPv3Credentials(**kwargs):
    return CatalystClient().createSNMPv3Credentials(**kwargs)

@register('getEoXStatusForAllDevices')
def getEoXStatusForAllDevices(**kwargs):
    return CatalystClient().getEoXStatusForAllDevices(**kwargs)

@register('getTagMemberCount')
def getTagMemberCount(**kwargs):
    return CatalystClient().getTagMemberCount(**kwargs)

@register('createsConfigurationDetailsOfTheExternalIPAMServer.')
def createsConfigurationDetailsOfTheExternalIPAMServer_(**kwargs):
    return CatalystClient().createsConfigurationDetailsOfTheExternalIPAMServer_(**kwargs)

@register('retrievesConfigurationDetailsOfTheExternalIPAMServer.')
def retrievesConfigurationDetailsOfTheExternalIPAMServer_(**kwargs):
    return CatalystClient().retrievesConfigurationDetailsOfTheExternalIPAMServer_(**kwargs)

@register('updatesConfigurationDetailsOfTheExternalIPAMServer.')
def updatesConfigurationDetailsOfTheExternalIPAMServer_(**kwargs):
    return CatalystClient().updatesConfigurationDetailsOfTheExternalIPAMServer_(**kwargs)

@register('deletesConfigurationDetailsOfTheExternalIPAMServer.')
def deletesConfigurationDetailsOfTheExternalIPAMServer_(**kwargs):
    return CatalystClient().deletesConfigurationDetailsOfTheExternalIPAMServer_(**kwargs)

@register('getViewDetailsForAGivenViewGroup&View')
def getViewDetailsForAGivenViewGroup_View(**kwargs):
    return CatalystClient().getViewDetailsForAGivenViewGroup_View(**kwargs)

@register('getTheDetailsOfPhysicalComponentsOfTheGivenDevice.')
def getTheDetailsOfPhysicalComponentsOfTheGivenDevice_(**kwargs):
    return CatalystClient().getTheDetailsOfPhysicalComponentsOfTheGivenDevice_(**kwargs)

@register('getDeviceInterfacesBySpecifiedRange')
def getDeviceInterfacesBySpecifiedRange(**kwargs):
    return CatalystClient().getDeviceInterfacesBySpecifiedRange(**kwargs)

@register('associate')
def associate(**kwargs):
    return CatalystClient().associate(**kwargs)

@register('disassociate')
def disassociate(**kwargs):
    return CatalystClient().disassociate(**kwargs)

@register('getPollingIntervalForAllDevices')
def getPollingIntervalForAllDevices(**kwargs):
    return CatalystClient().getPollingIntervalForAllDevices(**kwargs)

@register('getTopNAnalyticsDataOfIssues')
def getTopNAnalyticsDataOfIssues(**kwargs):
    return CatalystClient().getTopNAnalyticsDataOfIssues(**kwargs)

@register('getDeviceList')
def getDeviceList(**kwargs):
    return CatalystClient().getDeviceList(**kwargs)

@register('addDevice')
def addDevice(**kwargs):
    return CatalystClient().addDevice(**kwargs)

@register('updateDeviceDetails')
def updateDeviceDetails(**kwargs):
    return CatalystClient().updateDeviceDetails(**kwargs)

@register('importCertificateP12')
def importCertificateP12(**kwargs):
    return CatalystClient().importCertificateP12(**kwargs)

@register('getAllKeywordsOfCLIsAcceptedByCommandRunner')
def getAllKeywordsOfCLIsAcceptedByCommandRunner(**kwargs):
    return CatalystClient().getAllKeywordsOfCLIsAcceptedByCommandRunner(**kwargs)

@register('syncDevices')
def syncDevices(**kwargs):
    return CatalystClient().syncDevices(**kwargs)

@register('deregisterVirtualAccount')
def deregisterVirtualAccount(**kwargs):
    return CatalystClient().deregisterVirtualAccount(**kwargs)

@register('createQosDeviceInterfaceInfo')
def createQosDeviceInterfaceInfo(**kwargs):
    return CatalystClient().createQosDeviceInterfaceInfo(**kwargs)

@register('getQosDeviceInterfaceInfo')
def getQosDeviceInterfaceInfo(**kwargs):
    return CatalystClient().getQosDeviceInterfaceInfo(**kwargs)

@register('updateQosDeviceInterfaceInfo')
def updateQosDeviceInterfaceInfo(**kwargs):
    return CatalystClient().updateQosDeviceInterfaceInfo(**kwargs)

@register('retrieveTheCountOfInterfacesThatAreAssociatedWithAtLeastOneTag.')
def retrieveTheCountOfInterfacesThatAreAssociatedWithAtLeastOneTag_(**kwargs):
    return CatalystClient().retrieveTheCountOfInterfacesThatAreAssociatedWithAtLeastOneTag_(**kwargs)

@register('getDeviceFamilyIdentifiers')
def getDeviceFamilyIdentifiers(**kwargs):
    return CatalystClient().getDeviceFamilyIdentifiers(**kwargs)

@register('importDevicesInBulk')
def importDevicesInBulk(**kwargs):
    return CatalystClient().importDevicesInBulk(**kwargs)

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

@register('deleteLayer3VirtualNetworks')
def deleteLayer3VirtualNetworks(**kwargs):
    return CatalystClient().deleteLayer3VirtualNetworks(**kwargs)

@register('addLayer3VirtualNetworks')
def addLayer3VirtualNetworks(**kwargs):
    return CatalystClient().addLayer3VirtualNetworks(**kwargs)

@register('updateLayer3VirtualNetworks')
def updateLayer3VirtualNetworks(**kwargs):
    return CatalystClient().updateLayer3VirtualNetworks(**kwargs)

@register('getListOfAvailableNamespaces')
def getListOfAvailableNamespaces(**kwargs):
    return CatalystClient().getListOfAvailableNamespaces(**kwargs)

@register('updateSSID')
def updateSSID(**kwargs):
    return CatalystClient().updateSSID(**kwargs)

@register('getSSIDByID')
def getSSIDByID(**kwargs):
    return CatalystClient().getSSIDByID(**kwargs)

@register('deleteSSID')
def deleteSSID(**kwargs):
    return CatalystClient().deleteSSID(**kwargs)

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

@register('updateGlobalResyncInterval')
def updateGlobalResyncInterval(**kwargs):
    return CatalystClient().updateGlobalResyncInterval(**kwargs)

@register('custom-promptSupportGETAPI')
def custom_promptSupportGETAPI(**kwargs):
    return CatalystClient().custom_promptSupportGETAPI(**kwargs)

@register('customPromptPOSTAPI')
def customPromptPOSTAPI(**kwargs):
    return CatalystClient().customPromptPOSTAPI(**kwargs)

@register('getAdvisoriesList')
def getAdvisoriesList(**kwargs):
    return CatalystClient().getAdvisoriesList(**kwargs)

@register('deployDeviceReplacementWorkflow')
def deployDeviceReplacementWorkflow(**kwargs):
    return CatalystClient().deployDeviceReplacementWorkflow(**kwargs)

@register('getDeviceInterfaceVLANs')
def getDeviceInterfaceVLANs(**kwargs):
    return CatalystClient().getDeviceInterfaceVLANs(**kwargs)

@register('getListOfFiles')
def getListOfFiles(**kwargs):
    return CatalystClient().getListOfFiles(**kwargs)

@register('updateRemoteImageDistributionServer')
def updateRemoteImageDistributionServer(**kwargs):
    return CatalystClient().updateRemoteImageDistributionServer(**kwargs)

@register('removeImageDistributionServer')
def removeImageDistributionServer(**kwargs):
    return CatalystClient().removeImageDistributionServer(**kwargs)

@register('retrieveSpecificImageDistributionServer')
def retrieveSpecificImageDistributionServer(**kwargs):
    return CatalystClient().retrieveSpecificImageDistributionServer(**kwargs)

@register('getApplicationPolicy')
def getApplicationPolicy(**kwargs):
    return CatalystClient().getApplicationPolicy(**kwargs)

@register('previewTemplate')
def previewTemplate(**kwargs):
    return CatalystClient().previewTemplate(**kwargs)

@register('deleteExtranetPolicyById')
def deleteExtranetPolicyById(**kwargs):
    return CatalystClient().deleteExtranetPolicyById(**kwargs)

@register('updateWorkflow')
def updateWorkflow(**kwargs):
    return CatalystClient().updateWorkflow(**kwargs)

@register('getWorkflowById')
def getWorkflowById(**kwargs):
    return CatalystClient().getWorkflowById(**kwargs)

@register('deleteWorkflowById')
def deleteWorkflowById(**kwargs):
    return CatalystClient().deleteWorkflowById(**kwargs)

@register('getAdvisoriesSummary')
def getAdvisoriesSummary(**kwargs):
    return CatalystClient().getAdvisoriesSummary(**kwargs)

@register('overrideResyncInterval')
def overrideResyncInterval(**kwargs):
    return CatalystClient().overrideResyncInterval(**kwargs)

@register('getTagResourceTypes')
def getTagResourceTypes(**kwargs):
    return CatalystClient().getTagResourceTypes(**kwargs)

@register('getPortAssignmentCount')
def getPortAssignmentCount(**kwargs):
    return CatalystClient().getPortAssignmentCount(**kwargs)

@register('getDiscoveriesByRange')
def getDiscoveriesByRange(**kwargs):
    return CatalystClient().getDiscoveriesByRange(**kwargs)

@register('updateSNMPReadCommunity')
def updateSNMPReadCommunity(**kwargs):
    return CatalystClient().updateSNMPReadCommunity(**kwargs)

@register('createSNMPReadCommunity')
def createSNMPReadCommunity(**kwargs):
    return CatalystClient().createSNMPReadCommunity(**kwargs)

@register('getAllITSMIntegrationSettings')
def getAllITSMIntegrationSettings(**kwargs):
    return CatalystClient().getAllITSMIntegrationSettings(**kwargs)

@register('licenseUsageDetails')
def licenseUsageDetails(**kwargs):
    return CatalystClient().licenseUsageDetails(**kwargs)

@register('deletesAnArea')
def deletesAnArea(**kwargs):
    return CatalystClient().deletesAnArea(**kwargs)

@register('getsAnArea')
def getsAnArea(**kwargs):
    return CatalystClient().getsAnArea(**kwargs)

@register('updatesAnArea')
def updatesAnArea(**kwargs):
    return CatalystClient().updatesAnArea(**kwargs)

@register('getTheCountOfHealthScoreDefinitionsBasedOnProvidedFilters.')
def getTheCountOfHealthScoreDefinitionsBasedOnProvidedFilters_(**kwargs):
    return CatalystClient().getTheCountOfHealthScoreDefinitionsBasedOnProvidedFilters_(**kwargs)

@register('getExtranetPolicyCount')
def getExtranetPolicyCount(**kwargs):
    return CatalystClient().getExtranetPolicyCount(**kwargs)

@register('getResyncIntervalForTheNetworkDevice')
def getResyncIntervalForTheNetworkDevice(**kwargs):
    return CatalystClient().getResyncIntervalForTheNetworkDevice(**kwargs)

@register('updateResyncIntervalForTheNetworkDevice')
def updateResyncIntervalForTheNetworkDevice(**kwargs):
    return CatalystClient().updateResyncIntervalForTheNetworkDevice(**kwargs)

@register('getInterfaces')
def getInterfaces(**kwargs):
    return CatalystClient().getInterfaces(**kwargs)

@register('createInterface')
def createInterface(**kwargs):
    return CatalystClient().createInterface(**kwargs)

@register('getAllViewGroups')
def getAllViewGroups(**kwargs):
    return CatalystClient().getAllViewGroups(**kwargs)

@register('getEvents')
def getEvents(**kwargs):
    return CatalystClient().getEvents(**kwargs)

@register('getEmailEventSubscriptions')
def getEmailEventSubscriptions(**kwargs):
    return CatalystClient().getEmailEventSubscriptions(**kwargs)

@register('createEmailEventSubscription')
def createEmailEventSubscription(**kwargs):
    return CatalystClient().createEmailEventSubscription(**kwargs)

@register('updateEmailEventSubscription')
def updateEmailEventSubscription(**kwargs):
    return CatalystClient().updateEmailEventSubscription(**kwargs)

@register('deleteLayer3VirtualNetworkById')
def deleteLayer3VirtualNetworkById(**kwargs):
    return CatalystClient().deleteLayer3VirtualNetworkById(**kwargs)

@register('getEmailSubscriptionDetails')
def getEmailSubscriptionDetails(**kwargs):
    return CatalystClient().getEmailSubscriptionDetails(**kwargs)

@register('ignoreTheGivenListOfIssues')
def ignoreTheGivenListOfIssues(**kwargs):
    return CatalystClient().ignoreTheGivenListOfIssues(**kwargs)

@register('updateTagMembership')
def updateTagMembership(**kwargs):
    return CatalystClient().updateTagMembership(**kwargs)

@register('retrieveAAASettingsForASite')
def retrieveAAASettingsForASite(**kwargs):
    return CatalystClient().retrieveAAASettingsForASite(**kwargs)

@register('setAAASettingsForASite')
def setAAASettingsForASite(**kwargs):
    return CatalystClient().setAAASettingsForASite(**kwargs)

@register('getInterfaceDetailsByDeviceIdAndInterfaceName')
def getInterfaceDetailsByDeviceIdAndInterfaceName(**kwargs):
    return CatalystClient().getInterfaceDetailsByDeviceIdAndInterfaceName(**kwargs)

@register('createGlobalCredentialsV2')
def createGlobalCredentialsV2(**kwargs):
    return CatalystClient().createGlobalCredentialsV2(**kwargs)

@register('getAllGlobalCredentialsV2')
def getAllGlobalCredentialsV2(**kwargs):
    return CatalystClient().getAllGlobalCredentialsV2(**kwargs)

@register('updateGlobalCredentialsV2')
def updateGlobalCredentialsV2(**kwargs):
    return CatalystClient().updateGlobalCredentialsV2(**kwargs)

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

@register('createEventSubscriptions')
def createEventSubscriptions(**kwargs):
    return CatalystClient().createEventSubscriptions(**kwargs)

@register('updateEventSubscriptions')
def updateEventSubscriptions(**kwargs):
    return CatalystClient().updateEventSubscriptions(**kwargs)

@register('deleteEventSubscriptions')
def deleteEventSubscriptions(**kwargs):
    return CatalystClient().deleteEventSubscriptions(**kwargs)

@register('getEventSubscriptions')
def getEventSubscriptions(**kwargs):
    return CatalystClient().getEventSubscriptions(**kwargs)

@register('readSiteHealthSummaryDataBySiteId.')
def readSiteHealthSummaryDataBySiteId_(**kwargs):
    return CatalystClient().readSiteHealthSummaryDataBySiteId_(**kwargs)

@register('updatePlannedAccessPointForFloor')
def updatePlannedAccessPointForFloor(**kwargs):
    return CatalystClient().updatePlannedAccessPointForFloor(**kwargs)

@register('getPlannedAccessPointsForFloor')
def getPlannedAccessPointsForFloor(**kwargs):
    return CatalystClient().getPlannedAccessPointsForFloor(**kwargs)

@register('createPlannedAccessPointForFloor')
def createPlannedAccessPointForFloor(**kwargs):
    return CatalystClient().createPlannedAccessPointForFloor(**kwargs)

@register('unMarkDeviceForReplacement')
def unMarkDeviceForReplacement(**kwargs):
    return CatalystClient().unMarkDeviceForReplacement(**kwargs)

@register('markDeviceForReplacement')
def markDeviceForReplacement(**kwargs):
    return CatalystClient().markDeviceForReplacement(**kwargs)

@register('returnListOfReplacementDevicesWithReplacementDetails')
def returnListOfReplacementDevicesWithReplacementDetails(**kwargs):
    return CatalystClient().returnListOfReplacementDevicesWithReplacementDetails(**kwargs)

@register('deleteDiscoveryById')
def deleteDiscoveryById(**kwargs):
    return CatalystClient().deleteDiscoveryById(**kwargs)

@register('getDiscoveryById')
def getDiscoveryById(**kwargs):
    return CatalystClient().getDiscoveryById(**kwargs)

@register('getConfigurationArchiveDetails')
def getConfigurationArchiveDetails(**kwargs):
    return CatalystClient().getConfigurationArchiveDetails(**kwargs)

@register('createHTTPWriteCredentials')
def createHTTPWriteCredentials(**kwargs):
    return CatalystClient().createHTTPWriteCredentials(**kwargs)

@register('updateHTTPWriteCredentials')
def updateHTTPWriteCredentials(**kwargs):
    return CatalystClient().updateHTTPWriteCredentials(**kwargs)

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

@register('create/UpdateSNMPProperties')
def create_UpdateSNMPProperties(**kwargs):
    return CatalystClient().create_UpdateSNMPProperties(**kwargs)

@register('getComplianceDetailCount')
def getComplianceDetailCount(**kwargs):
    return CatalystClient().getComplianceDetailCount(**kwargs)

@register('getsTheListOfInterfacesAcrossTheNetworkDevicesBasedOnTheProvidedComplexFiltersAndAggregationFunctions')
def getsTheListOfInterfacesAcrossTheNetworkDevicesBasedOnTheProvidedComplexFiltersAndAggregationFunctions(**kwargs):
    return CatalystClient().getsTheListOfInterfacesAcrossTheNetworkDevicesBasedOnTheProvidedComplexFiltersAndAggregationFunctions(**kwargs)

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

@register('deleteTag')
def deleteTag(**kwargs):
    return CatalystClient().deleteTag(**kwargs)

@register('getTagById')
def getTagById(**kwargs):
    return CatalystClient().getTagById(**kwargs)

@register('getAuditLogSummary')
def getAuditLogSummary(**kwargs):
    return CatalystClient().getAuditLogSummary(**kwargs)

@register('deleteAnycastGatewayById')
def deleteAnycastGatewayById(**kwargs):
    return CatalystClient().deleteAnycastGatewayById(**kwargs)

@register('importsTheTemplatesProvided')
def importsTheTemplatesProvided(**kwargs):
    return CatalystClient().importsTheTemplatesProvided(**kwargs)

@register('createNetworkV2')
def createNetworkV2(**kwargs):
    return CatalystClient().createNetworkV2(**kwargs)

@register('updateNetworkV2')
def updateNetworkV2(**kwargs):
    return CatalystClient().updateNetworkV2(**kwargs)

@register('executingTheFlexibleReport')
def executingTheFlexibleReport(**kwargs):
    return CatalystClient().executingTheFlexibleReport(**kwargs)

@register('deleteQosDeviceInterfaceInfo')
def deleteQosDeviceInterfaceInfo(**kwargs):
    return CatalystClient().deleteQosDeviceInterfaceInfo(**kwargs)

@register('getsAListOfProjects')
def getsAListOfProjects(**kwargs):
    return CatalystClient().getsAListOfProjects(**kwargs)

@register('createProject')
def createProject(**kwargs):
    return CatalystClient().createProject(**kwargs)

@register('updateProject')
def updateProject(**kwargs):
    return CatalystClient().updateProject(**kwargs)

@register('exportDeviceConfigurations')
def exportDeviceConfigurations(**kwargs):
    return CatalystClient().exportDeviceConfigurations(**kwargs)

@register('lANAutomationStartV2')
def lANAutomationStartV2(**kwargs):
    return CatalystClient().lANAutomationStartV2(**kwargs)

@register('systemHealthCountAPI')
def systemHealthCountAPI(**kwargs):
    return CatalystClient().systemHealthCountAPI(**kwargs)

@register('addAuthenticationAndPolicyServerAccessConfiguration')
def addAuthenticationAndPolicyServerAccessConfiguration(**kwargs):
    return CatalystClient().addAuthenticationAndPolicyServerAccessConfiguration(**kwargs)

@register('getAuthenticationAndPolicyServers')
def getAuthenticationAndPolicyServers(**kwargs):
    return CatalystClient().getAuthenticationAndPolicyServers(**kwargs)

@register('getSSIDCountBySite')
def getSSIDCountBySite(**kwargs):
    return CatalystClient().getSSIDCountBySite(**kwargs)

@register('deviceLicenseSummary')
def deviceLicenseSummary(**kwargs):
    return CatalystClient().deviceLicenseSummary(**kwargs)

@register('importMapArchive-CancelAnImport')
def importMapArchive_CancelAnImport(**kwargs):
    return CatalystClient().importMapArchive_CancelAnImport(**kwargs)

@register('complianceDetailsOfDevice')
def complianceDetailsOfDevice(**kwargs):
    return CatalystClient().complianceDetailsOfDevice(**kwargs)

@register('retrievesTheCountOfSitesThatTheGivenNetworkProfileForSitesIsAssignedTo')
def retrievesTheCountOfSitesThatTheGivenNetworkProfileForSitesIsAssignedTo(**kwargs):
    return CatalystClient().retrievesTheCountOfSitesThatTheGivenNetworkProfileForSitesIsAssignedTo(**kwargs)

@register('deleteProvisionedDevices')
def deleteProvisionedDevices(**kwargs):
    return CatalystClient().deleteProvisionedDevices(**kwargs)

@register('provisionDevices')
def provisionDevices(**kwargs):
    return CatalystClient().provisionDevices(**kwargs)

@register('getProvisionedDevices')
def getProvisionedDevices(**kwargs):
    return CatalystClient().getProvisionedDevices(**kwargs)

@register('re-provisionDevices')
def re_provisionDevices(**kwargs):
    return CatalystClient().re_provisionDevices(**kwargs)

@register('deletePortChannelById')
def deletePortChannelById(**kwargs):
    return CatalystClient().deletePortChannelById(**kwargs)

@register('retrievesAllPreviousPathtracesSummary')
def retrievesAllPreviousPathtracesSummary(**kwargs):
    return CatalystClient().retrievesAllPreviousPathtracesSummary(**kwargs)

@register('initiateANewPathtrace')
def initiateANewPathtrace(**kwargs):
    return CatalystClient().initiateANewPathtrace(**kwargs)

@register('commitDeviceConfiguration')
def commitDeviceConfiguration(**kwargs):
    return CatalystClient().commitDeviceConfiguration(**kwargs)

@register('updateRoleAPI')
def updateRoleAPI(**kwargs):
    return CatalystClient().updateRoleAPI(**kwargs)

@register('addRoleAPI')
def addRoleAPI(**kwargs):
    return CatalystClient().addRoleAPI(**kwargs)

@register('inventoryInsightDeviceLinkMismatchAPI')
def inventoryInsightDeviceLinkMismatchAPI(**kwargs):
    return CatalystClient().inventoryInsightDeviceLinkMismatchAPI(**kwargs)

@register('claimADeviceToASite')
def claimADeviceToASite(**kwargs):
    return CatalystClient().claimADeviceToASite(**kwargs)

@register('getTheDeviceDataForTheGivenDeviceId(Uuid)')
def getTheDeviceDataForTheGivenDeviceId_Uuid_(**kwargs):
    return CatalystClient().getTheDeviceDataForTheGivenDeviceId_Uuid_(**kwargs)

@register('lANAutomationLogById')
def lANAutomationLogById(**kwargs):
    return CatalystClient().lANAutomationLogById(**kwargs)

@register('updateDeviceCredentialSettingsForASite.')
def updateDeviceCredentialSettingsForASite_(**kwargs):
    return CatalystClient().updateDeviceCredentialSettingsForASite_(**kwargs)

@register('getDeviceCredentialSettingsForASite')
def getDeviceCredentialSettingsForASite(**kwargs):
    return CatalystClient().getDeviceCredentialSettingsForASite(**kwargs)

@register('startDiscovery')
def startDiscovery(**kwargs):
    return CatalystClient().startDiscovery(**kwargs)

@register('updatesAnExistingDiscoveryBySpecifiedId')
def updatesAnExistingDiscoveryBySpecifiedId(**kwargs):
    return CatalystClient().updatesAnExistingDiscoveryBySpecifiedId(**kwargs)

@register('deleteAllDiscovery')
def deleteAllDiscovery(**kwargs):
    return CatalystClient().deleteAllDiscovery(**kwargs)

@register('getDeviceInterfaceCount')
def getDeviceInterfaceCount(**kwargs):
    return CatalystClient().getDeviceInterfaceCount(**kwargs)

@register('ciscoDNACenterReleaseSummary')
def ciscoDNACenterReleaseSummary(**kwargs):
    return CatalystClient().ciscoDNACenterReleaseSummary(**kwargs)

@register('tagAsGoldenImage')
def tagAsGoldenImage(**kwargs):
    return CatalystClient().tagAsGoldenImage(**kwargs)

@register('getLayer2VirtualNetworkCount')
def getLayer2VirtualNetworkCount(**kwargs):
    return CatalystClient().getLayer2VirtualNetworkCount(**kwargs)

@register('syncNetworkDevicesCredential')
def syncNetworkDevicesCredential(**kwargs):
    return CatalystClient().syncNetworkDevicesCredential(**kwargs)

@register('retrievesTheCountOfNetworkProfilesForSites')
def retrievesTheCountOfNetworkProfilesForSites(**kwargs):
    return CatalystClient().retrievesTheCountOfNetworkProfilesForSites(**kwargs)

@register('retrievesTheTrendAnalyticsDataRelatedToClients.')
def retrievesTheTrendAnalyticsDataRelatedToClients_(**kwargs):
    return CatalystClient().retrievesTheTrendAnalyticsDataRelatedToClients_(**kwargs)

@register('getDeviceCount')
def getDeviceCount(**kwargs):
    return CatalystClient().getDeviceCount(**kwargs)

@register('deleteSPProfileV2')
def deleteSPProfileV2(**kwargs):
    return CatalystClient().deleteSPProfileV2(**kwargs)

@register('importMapArchive-PerformImport')
def importMapArchive_PerformImport(**kwargs):
    return CatalystClient().importMapArchive_PerformImport(**kwargs)

@register('rebootAccessPoints')
def rebootAccessPoints(**kwargs):
    return CatalystClient().rebootAccessPoints(**kwargs)

@register('addFabricDevicesLayer2Handoffs')
def addFabricDevicesLayer2Handoffs(**kwargs):
    return CatalystClient().addFabricDevicesLayer2Handoffs(**kwargs)

@register('getFabricDevicesLayer2Handoffs')
def getFabricDevicesLayer2Handoffs(**kwargs):
    return CatalystClient().getFabricDevicesLayer2Handoffs(**kwargs)

@register('deleteFabricDeviceLayer2Handoffs')
def deleteFabricDeviceLayer2Handoffs(**kwargs):
    return CatalystClient().deleteFabricDeviceLayer2Handoffs(**kwargs)

@register('updateSyslogEventSubscription')
def updateSyslogEventSubscription(**kwargs):
    return CatalystClient().updateSyslogEventSubscription(**kwargs)

@register('createSyslogEventSubscription')
def createSyslogEventSubscription(**kwargs):
    return CatalystClient().createSyslogEventSubscription(**kwargs)

@register('getSyslogEventSubscriptions')
def getSyslogEventSubscriptions(**kwargs):
    return CatalystClient().getSyslogEventSubscriptions(**kwargs)

@register('getVLANDetails')
def getVLANDetails(**kwargs):
    return CatalystClient().getVLANDetails(**kwargs)

@register('getAllMobilityGroups	')
def getAllMobilityGroups_(**kwargs):
    return CatalystClient().getAllMobilityGroups_(**kwargs)

@register('deleteGlobalCredentialV2')
def deleteGlobalCredentialV2(**kwargs):
    return CatalystClient().deleteGlobalCredentialV2(**kwargs)

@register('queryTheTagsAssociatedWithNetworkDevices.')
def queryTheTagsAssociatedWithNetworkDevices_(**kwargs):
    return CatalystClient().queryTheTagsAssociatedWithNetworkDevices_(**kwargs)

@register('getSiteV2')
def getSiteV2(**kwargs):
    return CatalystClient().getSiteV2(**kwargs)

@register('systemHealthAPI')
def systemHealthAPI(**kwargs):
    return CatalystClient().systemHealthAPI(**kwargs)

@register('importTrustedCertificate')
def importTrustedCertificate(**kwargs):
    return CatalystClient().importTrustedCertificate(**kwargs)

@register('lANAutomationStatusById')
def lANAutomationStatusById(**kwargs):
    return CatalystClient().lANAutomationStatusById(**kwargs)

@register('deleteFabricDeviceLayer2HandoffById')
def deleteFabricDeviceLayer2HandoffById(**kwargs):
    return CatalystClient().deleteFabricDeviceLayer2HandoffById(**kwargs)

@register('editApplication/s')
def editApplication_s(**kwargs):
    return CatalystClient().editApplication_s(**kwargs)

@register('createApplication/s')
def createApplication_s(**kwargs):
    return CatalystClient().createApplication_s(**kwargs)

@register('getApplication/s')
def getApplication_s(**kwargs):
    return CatalystClient().getApplication_s(**kwargs)

@register('addFabricDevices')
def addFabricDevices(**kwargs):
    return CatalystClient().addFabricDevices(**kwargs)

@register('deleteFabricDevices')
def deleteFabricDevices(**kwargs):
    return CatalystClient().deleteFabricDevices(**kwargs)

@register('updateFabricDevices')
def updateFabricDevices(**kwargs):
    return CatalystClient().updateFabricDevices(**kwargs)

@register('getFabricDevices')
def getFabricDevices(**kwargs):
    return CatalystClient().getFabricDevices(**kwargs)

@register('update802.11beProfile')
def update802_11beProfile(**kwargs):
    return CatalystClient().update802_11beProfile(**kwargs)

@register('deleteA802.11beProfile')
def deleteA802_11beProfile(**kwargs):
    return CatalystClient().deleteA802_11beProfile(**kwargs)

@register('get802.11beProfileByID')
def get802_11beProfileByID(**kwargs):
    return CatalystClient().get802_11beProfileByID(**kwargs)

@register('assignANetworkProfileForSitesToAListOfSites')
def assignANetworkProfileForSitesToAListOfSites(**kwargs):
    return CatalystClient().assignANetworkProfileForSitesToAListOfSites(**kwargs)

@register('unassignsANetworkProfileForSitesFromMultipleSites')
def unassignsANetworkProfileForSitesFromMultipleSites(**kwargs):
    return CatalystClient().unassignsANetworkProfileForSitesFromMultipleSites(**kwargs)

@register('getTasksCount')
def getTasksCount(**kwargs):
    return CatalystClient().getTasksCount(**kwargs)

@register('deletesAFloor')
def deletesAFloor(**kwargs):
    return CatalystClient().deletesAFloor(**kwargs)

@register('updatesAFloor')
def updatesAFloor(**kwargs):
    return CatalystClient().updatesAFloor(**kwargs)

@register('getsAFloor')
def getsAFloor(**kwargs):
    return CatalystClient().getsAFloor(**kwargs)

@register('addUserAPI')
def addUserAPI(**kwargs):
    return CatalystClient().addUserAPI(**kwargs)

@register('getUsersAPI')
def getUsersAPI(**kwargs):
    return CatalystClient().getUsersAPI(**kwargs)

@register('updateUserAPI')
def updateUserAPI(**kwargs):
    return CatalystClient().updateUserAPI(**kwargs)

@register('addFabricZone')
def addFabricZone(**kwargs):
    return CatalystClient().addFabricZone(**kwargs)

@register('getFabricZones')
def getFabricZones(**kwargs):
    return CatalystClient().getFabricZones(**kwargs)

@register('updateFabricZone')
def updateFabricZone(**kwargs):
    return CatalystClient().updateFabricZone(**kwargs)

@register('configureAccessPointsV2')
def configureAccessPointsV2(**kwargs):
    return CatalystClient().configureAccessPointsV2(**kwargs)

@register('getVirtualAccountList')
def getVirtualAccountList(**kwargs):
    return CatalystClient().getVirtualAccountList(**kwargs)

@register('updateGlobalCredentials')
def updateGlobalCredentials(**kwargs):
    return CatalystClient().updateGlobalCredentials(**kwargs)

@register('deleteGlobalCredentialsById')
def deleteGlobalCredentialsById(**kwargs):
    return CatalystClient().deleteGlobalCredentialsById(**kwargs)

@register('deletePlannedAccessPointForFloor')
def deletePlannedAccessPointForFloor(**kwargs):
    return CatalystClient().deletePlannedAccessPointForFloor(**kwargs)

@register('exportsTheProjectsForAGivenCriteria.')
def exportsTheProjectsForAGivenCriteria_(**kwargs):
    return CatalystClient().exportsTheProjectsForAGivenCriteria_(**kwargs)

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

@register('mobilityProvision')
def mobilityProvision(**kwargs):
    return CatalystClient().mobilityProvision(**kwargs)

@register('deleteFabricDeviceById')
def deleteFabricDeviceById(**kwargs):
    return CatalystClient().deleteFabricDeviceById(**kwargs)

@register('createsABuilding')
def createsABuilding(**kwargs):
    return CatalystClient().createsABuilding(**kwargs)

@register('updateTransitNetworks')
def updateTransitNetworks(**kwargs):
    return CatalystClient().updateTransitNetworks(**kwargs)

@register('addTransitNetworks')
def addTransitNetworks(**kwargs):
    return CatalystClient().addTransitNetworks(**kwargs)

@register('getTransitNetworks')
def getTransitNetworks(**kwargs):
    return CatalystClient().getTransitNetworks(**kwargs)

@register('getStackDetailsForDevice')
def getStackDetailsForDevice(**kwargs):
    return CatalystClient().getStackDetailsForDevice(**kwargs)

@register('getDeviceInterfaceStatsInfo')
def getDeviceInterfaceStatsInfo(**kwargs):
    return CatalystClient().getDeviceInterfaceStatsInfo(**kwargs)

@register('getApplicationSetCount')
def getApplicationSetCount(**kwargs):
    return CatalystClient().getApplicationSetCount(**kwargs)

@register('getWorkflowCount')
def getWorkflowCount(**kwargs):
    return CatalystClient().getWorkflowCount(**kwargs)

@register('deleteFabricZoneById')
def deleteFabricZoneById(**kwargs):
    return CatalystClient().deleteFabricZoneById(**kwargs)

@register('deviceComplianceStatus')
def deviceComplianceStatus(**kwargs):
    return CatalystClient().deviceComplianceStatus(**kwargs)

@register('retrievesPreviousPathtrace')
def retrievesPreviousPathtrace(**kwargs):
    return CatalystClient().retrievesPreviousPathtrace(**kwargs)

@register('deletesPathtraceById')
def deletesPathtraceById(**kwargs):
    return CatalystClient().deletesPathtraceById(**kwargs)

@register('getOverallNetworkHealth')
def getOverallNetworkHealth(**kwargs):
    return CatalystClient().getOverallNetworkHealth(**kwargs)

@register('complianceRemediation')
def complianceRemediation(**kwargs):
    return CatalystClient().complianceRemediation(**kwargs)

@register('deleteUser-Defined-Field')
def deleteUser_Defined_Field(**kwargs):
    return CatalystClient().deleteUser_Defined_Field(**kwargs)

@register('updateUser-Defined-Field')
def updateUser_Defined_Field(**kwargs):
    return CatalystClient().updateUser_Defined_Field(**kwargs)

@register('getPnPGlobalSettings')
def getPnPGlobalSettings(**kwargs):
    return CatalystClient().getPnPGlobalSettings(**kwargs)

@register('updatePnPGlobalSettings')
def updatePnPGlobalSettings(**kwargs):
    return CatalystClient().updatePnPGlobalSettings(**kwargs)

@register('updateSPProfileV2')
def updateSPProfileV2(**kwargs):
    return CatalystClient().updateSPProfileV2(**kwargs)

@register('createSPProfileV2')
def createSPProfileV2(**kwargs):
    return CatalystClient().createSPProfileV2(**kwargs)

@register('getServiceProviderDetailsV2')
def getServiceProviderDetailsV2(**kwargs):
    return CatalystClient().getServiceProviderDetailsV2(**kwargs)

@register('getWirelessProfiles')
def getWirelessProfiles(**kwargs):
    return CatalystClient().getWirelessProfiles(**kwargs)

@register('createWirelessProfile')
def createWirelessProfile(**kwargs):
    return CatalystClient().createWirelessProfile(**kwargs)

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

@register('updateAuthenticationProfile')
def updateAuthenticationProfile(**kwargs):
    return CatalystClient().updateAuthenticationProfile(**kwargs)

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

@register('addFabricSite')
def addFabricSite(**kwargs):
    return CatalystClient().addFabricSite(**kwargs)

@register('getFabricSites')
def getFabricSites(**kwargs):
    return CatalystClient().getFabricSites(**kwargs)

@register('updateFabricSite')
def updateFabricSite(**kwargs):
    return CatalystClient().updateFabricSite(**kwargs)

@register('addAWorkflow')
def addAWorkflow(**kwargs):
    return CatalystClient().addAWorkflow(**kwargs)

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

@register('queryTheTagsAssociatedWithInterfaces.')
def queryTheTagsAssociatedWithInterfaces_(**kwargs):
    return CatalystClient().queryTheTagsAssociatedWithInterfaces_(**kwargs)

@register('getNotifications')
def getNotifications(**kwargs):
    return CatalystClient().getNotifications(**kwargs)

@register('getAllTheDetailsAndSuggestedActionsOfAnIssueForTheGivenIssueId')
def getAllTheDetailsAndSuggestedActionsOfAnIssueForTheGivenIssueId(**kwargs):
    return CatalystClient().getAllTheDetailsAndSuggestedActionsOfAnIssueForTheGivenIssueId(**kwargs)

@register('legitOperationsForInterface')
def legitOperationsForInterface(**kwargs):
    return CatalystClient().legitOperationsForInterface(**kwargs)

@register('createsAFloor')
def createsAFloor(**kwargs):
    return CatalystClient().createsAFloor(**kwargs)

@register('updateInterfaceDetails')
def updateInterfaceDetails(**kwargs):
    return CatalystClient().updateInterfaceDetails(**kwargs)

@register('deleteUserAPI')
def deleteUserAPI(**kwargs):
    return CatalystClient().deleteUserAPI(**kwargs)

@register('getDeviceConfigCount')
def getDeviceConfigCount(**kwargs):
    return CatalystClient().getDeviceConfigCount(**kwargs)

@register('getISISInterfaces')
def getISISInterfaces(**kwargs):
    return CatalystClient().getISISInterfaces(**kwargs)

@register('retrieveANetworkProfileForSitesById')
def retrieveANetworkProfileForSitesById(**kwargs):
    return CatalystClient().retrieveANetworkProfileForSitesById(**kwargs)

@register('deletesANetworkProfileForSites')
def deletesANetworkProfileForSites(**kwargs):
    return CatalystClient().deletesANetworkProfileForSites(**kwargs)

@register('getAuditLogRecords')
def getAuditLogRecords(**kwargs):
    return CatalystClient().getAuditLogRecords(**kwargs)

@register('updateHTTPReadCredential')
def updateHTTPReadCredential(**kwargs):
    return CatalystClient().updateHTTPReadCredential(**kwargs)

@register('createHTTPReadCredentials')
def createHTTPReadCredentials(**kwargs):
    return CatalystClient().createHTTPReadCredentials(**kwargs)

@register('systemPerformanceHistoricalAPI')
def systemPerformanceHistoricalAPI(**kwargs):
    return CatalystClient().systemPerformanceHistoricalAPI(**kwargs)

@register('getSupervisorCardDetail')
def getSupervisorCardDetail(**kwargs):
    return CatalystClient().getSupervisorCardDetail(**kwargs)

@register('setImageDistributionSettingsForASite')
def setImageDistributionSettingsForASite(**kwargs):
    return CatalystClient().setImageDistributionSettingsForASite(**kwargs)

@register('retrieveImageDistributionSettingsForASite')
def retrieveImageDistributionSettingsForASite(**kwargs):
    return CatalystClient().retrieveImageDistributionSettingsForASite(**kwargs)

@register('getSSIDDetailsForSpecificWirelessController')
def getSSIDDetailsForSpecificWirelessController(**kwargs):
    return CatalystClient().getSSIDDetailsForSpecificWirelessController(**kwargs)

@register('getsDetailsOfAGivenTemplate')
def getsDetailsOfAGivenTemplate(**kwargs):
    return CatalystClient().getsDetailsOfAGivenTemplate(**kwargs)

@register('deletesTheTemplate')
def deletesTheTemplate(**kwargs):
    return CatalystClient().deletesTheTemplate(**kwargs)

@register('deviceDeregistration')
def deviceDeregistration(**kwargs):
    return CatalystClient().deviceDeregistration(**kwargs)

@register('updatesAnExistingCustomIssueDefinitionBasedOnTheProvidedId.')
def updatesAnExistingCustomIssueDefinitionBasedOnTheProvidedId_(**kwargs):
    return CatalystClient().updatesAnExistingCustomIssueDefinitionBasedOnTheProvidedId_(**kwargs)

@register('deletesAnExistingCustomIssueDefinition.')
def deletesAnExistingCustomIssueDefinition_(**kwargs):
    return CatalystClient().deletesAnExistingCustomIssueDefinition_(**kwargs)

@register('getEventArtifacts')
def getEventArtifacts(**kwargs):
    return CatalystClient().getEventArtifacts(**kwargs)

@register('deletesTheProject')
def deletesTheProject(**kwargs):
    return CatalystClient().deletesTheProject(**kwargs)

@register('getsTheDetailsOfAGivenProject.')
def getsTheDetailsOfAGivenProject_(**kwargs):
    return CatalystClient().getsTheDetailsOfAGivenProject_(**kwargs)

@register('unassignsANetworkProfileForSitesFromASite')
def unassignsANetworkProfileForSitesFromASite(**kwargs):
    return CatalystClient().unassignsANetworkProfileForSitesFromASite(**kwargs)

@register('deletesAValidationWorkflow')
def deletesAValidationWorkflow(**kwargs):
    return CatalystClient().deletesAValidationWorkflow(**kwargs)

@register('retrievesValidationWorkflowDetails')
def retrievesValidationWorkflowDetails(**kwargs):
    return CatalystClient().retrievesValidationWorkflowDetails(**kwargs)

@register('getModuleCount')
def getModuleCount(**kwargs):
    return CatalystClient().getModuleCount(**kwargs)

@register('deleteProvisionedDeviceById')
def deleteProvisionedDeviceById(**kwargs):
    return CatalystClient().deleteProvisionedDeviceById(**kwargs)

@register('triggerSoftwareImageDistribution')
def triggerSoftwareImageDistribution(**kwargs):
    return CatalystClient().triggerSoftwareImageDistribution(**kwargs)

@register('getTransitNetworksCount')
def getTransitNetworksCount(**kwargs):
    return CatalystClient().getTransitNetworksCount(**kwargs)

@register('lANAutomationStopAndUpdateDevicesV2')
def lANAutomationStopAndUpdateDevicesV2(**kwargs):
    return CatalystClient().lANAutomationStopAndUpdateDevicesV2(**kwargs)

@register('returnsAllTheFabricSitesThatHaveVLANToSSIDMapping.')
def returnsAllTheFabricSitesThatHaveVLANToSSIDMapping_(**kwargs):
    return CatalystClient().returnsAllTheFabricSitesThatHaveVLANToSSIDMapping_(**kwargs)

@register('deviceCountDetails')
def deviceCountDetails(**kwargs):
    return CatalystClient().deviceCountDetails(**kwargs)

@register('getAllExecutionDetailsForAGivenReport')
def getAllExecutionDetailsForAGivenReport(**kwargs):
    return CatalystClient().getAllExecutionDetailsForAGivenReport(**kwargs)

@register('createRest/WebhookEventSubscription')
def createRest_WebhookEventSubscription(**kwargs):
    return CatalystClient().createRest_WebhookEventSubscription(**kwargs)

@register('updateRest/WebhookEventSubscription')
def updateRest_WebhookEventSubscription(**kwargs):
    return CatalystClient().updateRest_WebhookEventSubscription(**kwargs)

@register('getRest/WebhookEventSubscriptions')
def getRest_WebhookEventSubscriptions(**kwargs):
    return CatalystClient().getRest_WebhookEventSubscriptions(**kwargs)

@register('getRolesAPI')
def getRolesAPI(**kwargs):
    return CatalystClient().getRolesAPI(**kwargs)

@register('deleteApplication')
def deleteApplication(**kwargs):
    return CatalystClient().deleteApplication(**kwargs)

@register('getGoldenTagStatusOfAnImage.')
def getGoldenTagStatusOfAnImage_(**kwargs):
    return CatalystClient().getGoldenTagStatusOfAnImage_(**kwargs)

@register('removeGoldenTagForImage.')
def removeGoldenTagForImage_(**kwargs):
    return CatalystClient().removeGoldenTagForImage_(**kwargs)

@register('getPortChannelCount')
def getPortChannelCount(**kwargs):
    return CatalystClient().getPortChannelCount(**kwargs)

@register('mapsSupportedAccessPoints')
def mapsSupportedAccessPoints(**kwargs):
    return CatalystClient().mapsSupportedAccessPoints(**kwargs)

@register('getAuditLogParentRecords')
def getAuditLogParentRecords(**kwargs):
    return CatalystClient().getAuditLogParentRecords(**kwargs)

@register('setDNSSettingsForASite')
def setDNSSettingsForASite(**kwargs):
    return CatalystClient().setDNSSettingsForASite(**kwargs)

@register('retrieveDNSSettingsForASite')
def retrieveDNSSettingsForASite(**kwargs):
    return CatalystClient().retrieveDNSSettingsForASite(**kwargs)

@register('createCLICredentials')
def createCLICredentials(**kwargs):
    return CatalystClient().createCLICredentials(**kwargs)

@register('updateCLICredentials')
def updateCLICredentials(**kwargs):
    return CatalystClient().updateCLICredentials(**kwargs)

@register('getHealthScoreDefinitionForTheGivenId.')
def getHealthScoreDefinitionForTheGivenId_(**kwargs):
    return CatalystClient().getHealthScoreDefinitionForTheGivenId_(**kwargs)

@register('updateHealthScoreDefinitionForTheGivenId.')
def updateHealthScoreDefinitionForTheGivenId_(**kwargs):
    return CatalystClient().updateHealthScoreDefinitionForTheGivenId_(**kwargs)

@register('getProject(s)Details')
def getProject_s_Details(**kwargs):
    return CatalystClient().getProject_s_Details(**kwargs)

@register('lANAutomationStart')
def lANAutomationStart(**kwargs):
    return CatalystClient().lANAutomationStart(**kwargs)

@register('downloadAFileByFileId')
def downloadAFileByFileId(**kwargs):
    return CatalystClient().downloadAFileByFileId(**kwargs)

@register('getAllHealthScoreDefinitionsForGivenFilters.')
def getAllHealthScoreDefinitionsForGivenFilters_(**kwargs):
    return CatalystClient().getAllHealthScoreDefinitionsForGivenFilters_(**kwargs)

@register('updateEmailDestination')
def updateEmailDestination(**kwargs):
    return CatalystClient().updateEmailDestination(**kwargs)

@register('createEmailDestination')
def createEmailDestination(**kwargs):
    return CatalystClient().createEmailDestination(**kwargs)

@register('getEmailDestination')
def getEmailDestination(**kwargs):
    return CatalystClient().getEmailDestination(**kwargs)

@register('getsInterfacesAlongWithStatisticsDataFromAllNetworkDevices.')
def getsInterfacesAlongWithStatisticsDataFromAllNetworkDevices_(**kwargs):
    return CatalystClient().getsInterfacesAlongWithStatisticsDataFromAllNetworkDevices_(**kwargs)

@register('updateLicenseSetting')
def updateLicenseSetting(**kwargs):
    return CatalystClient().updateLicenseSetting(**kwargs)

@register('retrieveLicenseSetting')
def retrieveLicenseSetting(**kwargs):
    return CatalystClient().retrieveLicenseSetting(**kwargs)

@register('resetDevice')
def resetDevice(**kwargs):
    return CatalystClient().resetDevice(**kwargs)

@register('getTheDetailsOfIssuesForGivenSetOfFilters')
def getTheDetailsOfIssuesForGivenSetOfFilters(**kwargs):
    return CatalystClient().getTheDetailsOfIssuesForGivenSetOfFilters(**kwargs)

@register('wirelessControllerProvision')
def wirelessControllerProvision(**kwargs):
    return CatalystClient().wirelessControllerProvision(**kwargs)

@register('getTheTotalCustomIssueDefinitionsCountBasedOnTheProvidedFilters.')
def getTheTotalCustomIssueDefinitionsCountBasedOnTheProvidedFilters_(**kwargs):
    return CatalystClient().getTheTotalCustomIssueDefinitionsCountBasedOnTheProvidedFilters_(**kwargs)

@register('get802.11beProfilesCount')
def get802_11beProfilesCount(**kwargs):
    return CatalystClient().get802_11beProfilesCount(**kwargs)

@register('updateMulticast')
def updateMulticast(**kwargs):
    return CatalystClient().updateMulticast(**kwargs)

@register('getMulticast')
def getMulticast(**kwargs):
    return CatalystClient().getMulticast(**kwargs)

@register('assignNetworkDevicesToASite')
def assignNetworkDevicesToASite(**kwargs):
    return CatalystClient().assignNetworkDevicesToASite(**kwargs)

@register('getFabricDevicesCount')
def getFabricDevicesCount(**kwargs):
    return CatalystClient().getFabricDevicesCount(**kwargs)

@register('downloadFlexibleReport')
def downloadFlexibleReport(**kwargs):
    return CatalystClient().downloadFlexibleReport(**kwargs)

@register('exportsTheTemplatesForAGivenCriteria.')
def exportsTheTemplatesForAGivenCriteria_(**kwargs):
    return CatalystClient().exportsTheTemplatesForAGivenCriteria_(**kwargs)

@register('getExternalAuthenticationServersAPI')
def getExternalAuthenticationServersAPI(**kwargs):
    return CatalystClient().getExternalAuthenticationServersAPI(**kwargs)

@register('getLayer3VirtualNetworksCount')
def getLayer3VirtualNetworksCount(**kwargs):
    return CatalystClient().getLayer3VirtualNetworksCount(**kwargs)

@register('theTotalInterfacesCountAcrossTheNetworkDevices.')
def theTotalInterfacesCountAcrossTheNetworkDevices_(**kwargs):
    return CatalystClient().theTotalInterfacesCountAcrossTheNetworkDevices_(**kwargs)

@register('lANAutomationStatus')
def lANAutomationStatus(**kwargs):
    return CatalystClient().lANAutomationStatus(**kwargs)

@register('deviceRegistration')
def deviceRegistration(**kwargs):
    return CatalystClient().deviceRegistration(**kwargs)

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

@register('syncVirtualAccountDevices')
def syncVirtualAccountDevices(**kwargs):
    return CatalystClient().syncVirtualAccountDevices(**kwargs)

@register('removeUser-Defined-FieldFromDevice')
def removeUser_Defined_FieldFromDevice(**kwargs):
    return CatalystClient().removeUser_Defined_FieldFromDevice(**kwargs)

@register('addUser-Defined-FieldToDevice')
def addUser_Defined_FieldToDevice(**kwargs):
    return CatalystClient().addUser_Defined_FieldToDevice(**kwargs)

@register('createTemplate')
def createTemplate(**kwargs):
    return CatalystClient().createTemplate(**kwargs)

@register('getAnchorManagedAPLocationsForSpecificWirelessController')
def getAnchorManagedAPLocationsForSpecificWirelessController(**kwargs):
    return CatalystClient().getAnchorManagedAPLocationsForSpecificWirelessController(**kwargs)

@register('getConnectedDeviceDetail')
def getConnectedDeviceDetail(**kwargs):
    return CatalystClient().getConnectedDeviceDetail(**kwargs)

@register('getDevicesThatAreAssignedToASite')
def getDevicesThatAreAssignedToASite(**kwargs):
    return CatalystClient().getDevicesThatAreAssignedToASite(**kwargs)

@register('getSummaryAnalyticsDataOfIssues')
def getSummaryAnalyticsDataOfIssues(**kwargs):
    return CatalystClient().getSummaryAnalyticsDataOfIssues(**kwargs)

@register('deleteTransitNetworkById')
def deleteTransitNetworkById(**kwargs):
    return CatalystClient().deleteTransitNetworkById(**kwargs)

@register('deleteFabricSiteById')
def deleteFabricSiteById(**kwargs):
    return CatalystClient().deleteFabricSiteById(**kwargs)

@register('lANAutomationLog')
def lANAutomationLog(**kwargs):
    return CatalystClient().lANAutomationLog(**kwargs)

@register('retrievesTheListOfNetworkProfilesThatTheGivenSiteHasBeenAssigned')
def retrievesTheListOfNetworkProfilesThatTheGivenSiteHasBeenAssigned(**kwargs):
    return CatalystClient().retrievesTheListOfNetworkProfilesThatTheGivenSiteHasBeenAssigned(**kwargs)

@register('assignManagedAPLocationsForWLC')
def assignManagedAPLocationsForWLC(**kwargs):
    return CatalystClient().assignManagedAPLocationsForWLC(**kwargs)

@register('getDiscoveryJobsByIP')
def getDiscoveryJobsByIP(**kwargs):
    return CatalystClient().getDiscoveryJobsByIP(**kwargs)

@register('deleteApplicationSet')
def deleteApplicationSet(**kwargs):
    return CatalystClient().deleteApplicationSet(**kwargs)

@register('getTemplate(s)Details')
def getTemplate_s_Details(**kwargs):
    return CatalystClient().getTemplate_s_Details(**kwargs)

@register('deleteLayer2VirtualNetworkById')
def deleteLayer2VirtualNetworkById(**kwargs):
    return CatalystClient().deleteLayer2VirtualNetworkById(**kwargs)

@register('lANAutomationLogsForIndividualDevices')
def lANAutomationLogsForIndividualDevices(**kwargs):
    return CatalystClient().lANAutomationLogsForIndividualDevices(**kwargs)

@register('updateTheGivenIssueByUpdatingSelectedFields')
def updateTheGivenIssueByUpdatingSelectedFields(**kwargs):
    return CatalystClient().updateTheGivenIssueByUpdatingSelectedFields(**kwargs)

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

@register('setNTPSettingsForASite')
def setNTPSettingsForASite(**kwargs):
    return CatalystClient().setNTPSettingsForASite(**kwargs)

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

@register('updateDeviceRole')
def updateDeviceRole(**kwargs):
    return CatalystClient().updateDeviceRole(**kwargs)

@register('importSoftwareImageViaURL')
def importSoftwareImageViaURL(**kwargs):
    return CatalystClient().importSoftwareImageViaURL(**kwargs)

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

@register('createsAnArea')
def createsAnArea(**kwargs):
    return CatalystClient().createsAnArea(**kwargs)

@register('getPortAssignments')
def getPortAssignments(**kwargs):
    return CatalystClient().getPortAssignments(**kwargs)

@register('deletePortAssignments')
def deletePortAssignments(**kwargs):
    return CatalystClient().deletePortAssignments(**kwargs)

@register('updatePortAssignments')
def updatePortAssignments(**kwargs):
    return CatalystClient().updatePortAssignments(**kwargs)

@register('addPortAssignments')
def addPortAssignments(**kwargs):
    return CatalystClient().addPortAssignments(**kwargs)

@register('authenticationAPI')
def authenticationAPI(**kwargs):
    return CatalystClient().authenticationAPI(**kwargs)

@register('queryAssuranceEventsWithFilters')
def queryAssuranceEventsWithFilters(**kwargs):
    return CatalystClient().queryAssuranceEventsWithFilters(**kwargs)

@register('getBusinessAPIExecutionDetails')
def getBusinessAPIExecutionDetails(**kwargs):
    return CatalystClient().getBusinessAPIExecutionDetails(**kwargs)

@register('lANAutomationActiveSessions')
def lANAutomationActiveSessions(**kwargs):
    return CatalystClient().lANAutomationActiveSessions(**kwargs)

@register('applicationPolicyIntent')
def applicationPolicyIntent(**kwargs):
    return CatalystClient().applicationPolicyIntent(**kwargs)

@register('getSiteNotAssignedNetworkDevices')
def getSiteNotAssignedNetworkDevices(**kwargs):
    return CatalystClient().getSiteNotAssignedNetworkDevices(**kwargs)

@register('getAccessPointRebootTaskResult')
def getAccessPointRebootTaskResult(**kwargs):
    return CatalystClient().getAccessPointRebootTaskResult(**kwargs)

@register('getDeviceDetail')
def getDeviceDetail(**kwargs):
    return CatalystClient().getDeviceDetail(**kwargs)

@register('acceptCiscoISEServerCertificateForCiscoISEServerIntegration')
def acceptCiscoISEServerCertificateForCiscoISEServerIntegration(**kwargs):
    return CatalystClient().acceptCiscoISEServerCertificateForCiscoISEServerIntegration(**kwargs)

@register('lANAutomationSessionCount')
def lANAutomationSessionCount(**kwargs):
    return CatalystClient().lANAutomationSessionCount(**kwargs)

@register('getNetworkDeviceByIP')
def getNetworkDeviceByIP(**kwargs):
    return CatalystClient().getNetworkDeviceByIP(**kwargs)

@register('exportDeviceList')
def exportDeviceList(**kwargs):
    return CatalystClient().exportDeviceList(**kwargs)

@register('updateDeviceManagementAddress')
def updateDeviceManagementAddress(**kwargs):
    return CatalystClient().updateDeviceManagementAddress(**kwargs)

@register('removeTagMember')
def removeTagMember(**kwargs):
    return CatalystClient().removeTagMember(**kwargs)

@register('previewConfig')
def previewConfig(**kwargs):
    return CatalystClient().previewConfig(**kwargs)

@register('getTheTotalNumberOfIssuesForGivenSetOfFilters-2')
def getTheTotalNumberOfIssuesForGivenSetOfFilters_2(**kwargs):
    return CatalystClient().getTheTotalNumberOfIssuesForGivenSetOfFilters_2(**kwargs)

@register('runRead-onlyCommandsOnDevicesToGetTheirReal-timeConfiguration')
def runRead_onlyCommandsOnDevicesToGetTheirReal_timeConfiguration(**kwargs):
    return CatalystClient().runRead_onlyCommandsOnDevicesToGetTheirReal_timeConfiguration(**kwargs)

@register('factoryResetAccessPoint(s)')
def factoryResetAccessPoint_s_(**kwargs):
    return CatalystClient().factoryResetAccessPoint_s_(**kwargs)

@register('retrievesTheNumberOfClientsByApplyingComplexFilters.')
def retrievesTheNumberOfClientsByApplyingComplexFilters_(**kwargs):
    return CatalystClient().retrievesTheNumberOfClientsByApplyingComplexFilters_(**kwargs)

@register('getSiteNotAssignedNetworkDevicesCount')
def getSiteNotAssignedNetworkDevicesCount(**kwargs):
    return CatalystClient().getSiteNotAssignedNetworkDevicesCount(**kwargs)

@register('deleteRoleAPI')
def deleteRoleAPI(**kwargs):
    return CatalystClient().deleteRoleAPI(**kwargs)

@register('getDeviceBySerialNumber')
def getDeviceBySerialNumber(**kwargs):
    return CatalystClient().getDeviceBySerialNumber(**kwargs)

@register('getApplicationCount')
def getApplicationCount(**kwargs):
    return CatalystClient().getApplicationCount(**kwargs)

@register('downloadReportContent')
def downloadReportContent(**kwargs):
    return CatalystClient().downloadReportContent(**kwargs)

@register('importMapArchive-StartImport')
def importMapArchive_StartImport(**kwargs):
    return CatalystClient().importMapArchive_StartImport(**kwargs)

@register('getDeviceCount-2')
def getDeviceCount_2(**kwargs):
    return CatalystClient().getDeviceCount_2(**kwargs)

@register('eventArtifactCount')
def eventArtifactCount(**kwargs):
    return CatalystClient().eventArtifactCount(**kwargs)

@register('claimDevice')
def claimDevice(**kwargs):
    return CatalystClient().claimDevice(**kwargs)

@register('resolveTheGivenListsOfIssues')
def resolveTheGivenListsOfIssues(**kwargs):
    return CatalystClient().resolveTheGivenListsOfIssues(**kwargs)

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

@register('setProvisioningSettings')
def setProvisioningSettings(**kwargs):
    return CatalystClient().setProvisioningSettings(**kwargs)

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

@register('manageExternalAuthenticationSettingAPI')
def manageExternalAuthenticationSettingAPI(**kwargs):
    return CatalystClient().manageExternalAuthenticationSettingAPI(**kwargs)

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

@register('retrievesTheTop-NAnalyticsDataRelatedToClients.')
def retrievesTheTop_NAnalyticsDataRelatedToClients_(**kwargs):
    return CatalystClient().retrievesTheTop_NAnalyticsDataRelatedToClients_(**kwargs)

@register('getTaskByOperationId')
def getTaskByOperationId(**kwargs):
    return CatalystClient().getTaskByOperationId(**kwargs)

@register('ciscoISEServerIntegrationStatus')
def ciscoISEServerIntegrationStatus(**kwargs):
    return CatalystClient().ciscoISEServerIntegrationStatus(**kwargs)

@register('getL3TopologyDetails')
def getL3TopologyDetails(**kwargs):
    return CatalystClient().getL3TopologyDetails(**kwargs)

@register('changeVirtualAccount')
def changeVirtualAccount(**kwargs):
    return CatalystClient().changeVirtualAccount(**kwargs)

@register('getAdvisoryDeviceDetail')
def getAdvisoryDeviceDetail(**kwargs):
    return CatalystClient().getAdvisoryDeviceDetail(**kwargs)

@register('getConnectorTypes')
def getConnectorTypes(**kwargs):
    return CatalystClient().getConnectorTypes(**kwargs)

@register('getsTheListOfNetworkDevicesBasedOnTheProvidedComplexFiltersAndAggregationFunctions.')
def getsTheListOfNetworkDevicesBasedOnTheProvidedComplexFiltersAndAggregationFunctions_(**kwargs):
    return CatalystClient().getsTheListOfNetworkDevicesBasedOnTheProvidedComplexFiltersAndAggregationFunctions_(**kwargs)

@register('getTasksByID')
def getTasksByID(**kwargs):
    return CatalystClient().getTasksByID(**kwargs)

@register('licenseTermDetails')
def licenseTermDetails(**kwargs):
    return CatalystClient().licenseTermDetails(**kwargs)

@register('setDhcpSettingsForASite')
def setDhcpSettingsForASite(**kwargs):
    return CatalystClient().setDhcpSettingsForASite(**kwargs)

@register('retrieveDHCPSettingsForASite')
def retrieveDHCPSettingsForASite(**kwargs):
    return CatalystClient().retrieveDHCPSettingsForASite(**kwargs)

@register('getAnycastGatewayCount')
def getAnycastGatewayCount(**kwargs):
    return CatalystClient().getAnycastGatewayCount(**kwargs)

@register('getsTheNetworkDeviceDetailsBasedOnTheProvidedQueryParameters.')
def getsTheNetworkDeviceDetailsBasedOnTheProvidedQueryParameters_(**kwargs):
    return CatalystClient().getsTheNetworkDeviceDetailsBasedOnTheProvidedQueryParameters_(**kwargs)

@register('downloadTheSoftwareImage')
def downloadTheSoftwareImage(**kwargs):
    return CatalystClient().downloadTheSoftwareImage(**kwargs)

@register('issues')
def issues(**kwargs):
    return CatalystClient().issues(**kwargs)

@register('getDevicesRegisteredForWSANotification')
def getDevicesRegisteredForWSANotification(**kwargs):
    return CatalystClient().getDevicesRegisteredForWSANotification(**kwargs)

@register('createSites')
def createSites(**kwargs):
    return CatalystClient().createSites(**kwargs)

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

@register('deleteFabricDeviceLayer3HandoffWithIpTransitById')
def deleteFabricDeviceLayer3HandoffWithIpTransitById(**kwargs):
    return CatalystClient().deleteFabricDeviceLayer3HandoffWithIpTransitById(**kwargs)

@register('systemPerformanceAPI')
def systemPerformanceAPI(**kwargs):
    return CatalystClient().systemPerformanceAPI(**kwargs)

@register('countTheNumberOfEventsWithFilters')
def countTheNumberOfEventsWithFilters(**kwargs):
    return CatalystClient().countTheNumberOfEventsWithFilters(**kwargs)

@register('retrievesSpecificClientInformationOverASpecifiedPeriodOfTime.')
def retrievesSpecificClientInformationOverASpecifiedPeriodOfTime_(**kwargs):
    return CatalystClient().retrievesSpecificClientInformationOverASpecifiedPeriodOfTime_(**kwargs)

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

@register('retrievesSummaryAnalyticsDataRelatedToClients.')
def retrievesSummaryAnalyticsDataRelatedToClients_(**kwargs):
    return CatalystClient().retrievesSummaryAnalyticsDataRelatedToClients_(**kwargs)

@register('getRFProfilesCount')
def getRFProfilesCount(**kwargs):
    return CatalystClient().getRFProfilesCount(**kwargs)

@register('getDevicesPerAdvisory')
def getDevicesPerAdvisory(**kwargs):
    return CatalystClient().getDevicesPerAdvisory(**kwargs)

@register('getAccessPointConfigurationTaskResult')
def getAccessPointConfigurationTaskResult(**kwargs):
    return CatalystClient().getAccessPointConfigurationTaskResult(**kwargs)

@register('importsTheProjectsProvided')
def importsTheProjectsProvided(**kwargs):
    return CatalystClient().importsTheProjectsProvided(**kwargs)

@register('getComplianceDetail')
def getComplianceDetail(**kwargs):
    return CatalystClient().getComplianceDetail(**kwargs)

@register('uploadsFloorImage')
def uploadsFloorImage(**kwargs):
    return CatalystClient().uploadsFloorImage(**kwargs)

@register('deletePortAssignmentById')
def deletePortAssignmentById(**kwargs):
    return CatalystClient().deletePortAssignmentById(**kwargs)

@register('returnsTheCountOfVLANsMappedToSSIDsInAFabricSite.')
def returnsTheCountOfVLANsMappedToSSIDsInAFabricSite_(**kwargs):
    return CatalystClient().returnsTheCountOfVLANsMappedToSSIDsInAFabricSite_(**kwargs)

@register('getGlobalCredentials')
def getGlobalCredentials(**kwargs):
    return CatalystClient().getGlobalCredentials(**kwargs)

@register('getTrendAnalyticsDataOfIssues')
def getTrendAnalyticsDataOfIssues(**kwargs):
    return CatalystClient().getTrendAnalyticsDataOfIssues(**kwargs)

@register('getComplianceStatus')
def getComplianceStatus(**kwargs):
    return CatalystClient().getComplianceStatus(**kwargs)

@register('getSNMPDestination')
def getSNMPDestination(**kwargs):
    return CatalystClient().getSNMPDestination(**kwargs)

@register('triggerSoftwareImageActivation')
def triggerSoftwareImageActivation(**kwargs):
    return CatalystClient().triggerSoftwareImageActivation(**kwargs)

@register('getProvisionedDevicesCount')
def getProvisionedDevicesCount(**kwargs):
    return CatalystClient().getProvisionedDevicesCount(**kwargs)

@register('returnsListOfSoftwareImages')
def returnsListOfSoftwareImages(**kwargs):
    return CatalystClient().returnsListOfSoftwareImages(**kwargs)

@register('getInterfacesCount')
def getInterfacesCount(**kwargs):
    return CatalystClient().getInterfacesCount(**kwargs)

@register('mobilityReset')
def mobilityReset(**kwargs):
    return CatalystClient().mobilityReset(**kwargs)

@register('readListOfSiteHealthSummaries.')
def readListOfSiteHealthSummaries_(**kwargs):
    return CatalystClient().readListOfSiteHealthSummaries_(**kwargs)

@register('getDeviceList-2')
def getDeviceList_2(**kwargs):
    return CatalystClient().getDeviceList_2(**kwargs)

@register('addDevice-2')
def addDevice_2(**kwargs):
    return CatalystClient().addDevice_2(**kwargs)

@register('retrievesTheListOfClientsByApplyingComplexFiltersWhileAlsoSupportingAggregateAttributes.')
def retrievesTheListOfClientsByApplyingComplexFiltersWhileAlsoSupportingAggregateAttributes_(**kwargs):
    return CatalystClient().retrievesTheListOfClientsByApplyingComplexFiltersWhileAlsoSupportingAggregateAttributes_(**kwargs)

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

@register('versionTemplate')
def versionTemplate(**kwargs):
    return CatalystClient().versionTemplate(**kwargs)

@register('getTaskTree')
def getTaskTree(**kwargs):
    return CatalystClient().getTaskTree(**kwargs)

@register('getDiscoveredNetworkDevicesByDiscoveryId')
def getDiscoveredNetworkDevicesByDiscoveryId(**kwargs):
    return CatalystClient().getDiscoveredNetworkDevicesByDiscoveryId(**kwargs)

@register('runCompliance')
def runCompliance(**kwargs):
    return CatalystClient().runCompliance(**kwargs)

@register('getStatusAPIForEvents')
def getStatusAPIForEvents(**kwargs):
    return CatalystClient().getStatusAPIForEvents(**kwargs)

@register('exportMapArchive')
def exportMapArchive(**kwargs):
    return CatalystClient().exportMapArchive(**kwargs)

@register('getSiteAssignedNetworkDevicesCount')
def getSiteAssignedNetworkDevicesCount(**kwargs):
    return CatalystClient().getSiteAssignedNetworkDevicesCount(**kwargs)

@register('getNetworkV2')
def getNetworkV2(**kwargs):
    return CatalystClient().getNetworkV2(**kwargs)

@register('getDeviceValuesThatMatchFullyOrPartiallyAnAttribute')
def getDeviceValuesThatMatchFullyOrPartiallyAnAttribute(**kwargs):
    return CatalystClient().getDeviceValuesThatMatchFullyOrPartiallyAnAttribute(**kwargs)

@register('createSensorTestTemplate')
def createSensorTestTemplate(**kwargs):
    return CatalystClient().createSensorTestTemplate(**kwargs)

@register('deleteSensorTest')
def deleteSensorTest(**kwargs):
    return CatalystClient().deleteSensorTest(**kwargs)

@register('sensors')
def sensors(**kwargs):
    return CatalystClient().sensors(**kwargs)

@register('getDeviceInfoFromSDAFabric')
def getDeviceInfoFromSDAFabric(**kwargs):
    return CatalystClient().getDeviceInfoFromSDAFabric(**kwargs)

@register('deletePortAssignmentForAccessPointInSDAFabric')
def deletePortAssignmentForAccessPointInSDAFabric(**kwargs):
    return CatalystClient().deletePortAssignmentForAccessPointInSDAFabric(**kwargs)

@register('getPortAssignmentForAccessPointInSDAFabric')
def getPortAssignmentForAccessPointInSDAFabric(**kwargs):
    return CatalystClient().getPortAssignmentForAccessPointInSDAFabric(**kwargs)

@register('addPortAssignmentForAccessPointInSDAFabric')
def addPortAssignmentForAccessPointInSDAFabric(**kwargs):
    return CatalystClient().addPortAssignmentForAccessPointInSDAFabric(**kwargs)

@register('removeWLCFromFabricDomain')
def removeWLCFromFabricDomain(**kwargs):
    return CatalystClient().removeWLCFromFabricDomain(**kwargs)

@register('addWLCToFabricDomain')
def addWLCToFabricDomain(**kwargs):
    return CatalystClient().addWLCToFabricDomain(**kwargs)

@register('addIPPoolInSDAVirtualNetwork')
def addIPPoolInSDAVirtualNetwork(**kwargs):
    return CatalystClient().addIPPoolInSDAVirtualNetwork(**kwargs)

@register('deleteIPPoolFromSDAVirtualNetwork')
def deleteIPPoolFromSDAVirtualNetwork(**kwargs):
    return CatalystClient().deleteIPPoolFromSDAVirtualNetwork(**kwargs)

@register('getIPPoolFromSDAVirtualNetwork')
def getIPPoolFromSDAVirtualNetwork(**kwargs):
    return CatalystClient().getIPPoolFromSDAVirtualNetwork(**kwargs)

@register('deleteEdgeDeviceFromSDAFabric')
def deleteEdgeDeviceFromSDAFabric(**kwargs):
    return CatalystClient().deleteEdgeDeviceFromSDAFabric(**kwargs)

@register('getEdgeDeviceFromSDAFabric')
def getEdgeDeviceFromSDAFabric(**kwargs):
    return CatalystClient().getEdgeDeviceFromSDAFabric(**kwargs)

@register('addEdgeDeviceInSDAFabric')
def addEdgeDeviceInSDAFabric(**kwargs):
    return CatalystClient().addEdgeDeviceInSDAFabric(**kwargs)

@register('deleteMulticastFromSDAFabric')
def deleteMulticastFromSDAFabric(**kwargs):
    return CatalystClient().deleteMulticastFromSDAFabric(**kwargs)

@register('getMulticastDetailsFromSDAFabric')
def getMulticastDetailsFromSDAFabric(**kwargs):
    return CatalystClient().getMulticastDetailsFromSDAFabric(**kwargs)

@register('addMulticastInSDAFabric')
def addMulticastInSDAFabric(**kwargs):
    return CatalystClient().addMulticastInSDAFabric(**kwargs)

@register('editApplication')
def editApplication(**kwargs):
    return CatalystClient().editApplication(**kwargs)

@register('getApplications')
def getApplications(**kwargs):
    return CatalystClient().getApplications(**kwargs)

@register('deleteApplication-2')
def deleteApplication_2(**kwargs):
    return CatalystClient().deleteApplication_2(**kwargs)

@register('createApplication')
def createApplication(**kwargs):
    return CatalystClient().createApplication(**kwargs)

@register('retrieveRFProfiles')
def retrieveRFProfiles(**kwargs):
    return CatalystClient().retrieveRFProfiles(**kwargs)

@register('createOrUpdateRFProfile')
def createOrUpdateRFProfile(**kwargs):
    return CatalystClient().createOrUpdateRFProfile(**kwargs)

@register('getNetwork')
def getNetwork(**kwargs):
    return CatalystClient().getNetwork(**kwargs)

@register('getReserveIPSubpool')
def getReserveIPSubpool(**kwargs):
    return CatalystClient().getReserveIPSubpool(**kwargs)

@register('getTransitPeerNetworkInfo')
def getTransitPeerNetworkInfo(**kwargs):
    return CatalystClient().getTransitPeerNetworkInfo(**kwargs)

@register('addTransitPeerNetwork')
def addTransitPeerNetwork(**kwargs):
    return CatalystClient().addTransitPeerNetwork(**kwargs)

@register('deleteTransitPeerNetwork')
def deleteTransitPeerNetwork(**kwargs):
    return CatalystClient().deleteTransitPeerNetwork(**kwargs)

@register('clientProximity')
def clientProximity(**kwargs):
    return CatalystClient().clientProximity(**kwargs)

@register('deleteDeviceCredential')
def deleteDeviceCredential(**kwargs):
    return CatalystClient().deleteDeviceCredential(**kwargs)

@register('deleteSPProfile')
def deleteSPProfile(**kwargs):
    return CatalystClient().deleteSPProfile(**kwargs)

@register('applications')
def applications(**kwargs):
    return CatalystClient().applications(**kwargs)

@register('createApplicationSet')
def createApplicationSet(**kwargs):
    return CatalystClient().createApplicationSet(**kwargs)

@register('deleteApplicationSet-2')
def deleteApplicationSet_2(**kwargs):
    return CatalystClient().deleteApplicationSet_2(**kwargs)

@register('getApplicationSets')
def getApplicationSets(**kwargs):
    return CatalystClient().getApplicationSets(**kwargs)

@register('getApplicationsCount')
def getApplicationsCount(**kwargs):
    return CatalystClient().getApplicationsCount(**kwargs)

@register('deleteGlobalIPPool')
def deleteGlobalIPPool(**kwargs):
    return CatalystClient().deleteGlobalIPPool(**kwargs)

@register('updateGlobalPool')
def updateGlobalPool(**kwargs):
    return CatalystClient().updateGlobalPool(**kwargs)

@register('getGlobalPool')
def getGlobalPool(**kwargs):
    return CatalystClient().getGlobalPool(**kwargs)

@register('createGlobalPool')
def createGlobalPool(**kwargs):
    return CatalystClient().createGlobalPool(**kwargs)

@register('createAndProvisionSSID')
def createAndProvisionSSID(**kwargs):
    return CatalystClient().createAndProvisionSSID(**kwargs)

@register('deleteRFProfiles')
def deleteRFProfiles(**kwargs):
    return CatalystClient().deleteRFProfiles(**kwargs)

@register('getVNFromSDAFabric')
def getVNFromSDAFabric(**kwargs):
    return CatalystClient().getVNFromSDAFabric(**kwargs)

@register('addVNInFabric')
def addVNInFabric(**kwargs):
    return CatalystClient().addVNInFabric(**kwargs)

@register('deleteVNFromSDAFabric')
def deleteVNFromSDAFabric(**kwargs):
    return CatalystClient().deleteVNFromSDAFabric(**kwargs)

@register('deleteDefaultAuthenticationProfileFromSDAFabric')
def deleteDefaultAuthenticationProfileFromSDAFabric(**kwargs):
    return CatalystClient().deleteDefaultAuthenticationProfileFromSDAFabric(**kwargs)

@register('updateDefaultAuthenticationProfileInSDAFabric')
def updateDefaultAuthenticationProfileInSDAFabric(**kwargs):
    return CatalystClient().updateDefaultAuthenticationProfileInSDAFabric(**kwargs)

@register('getDefaultAuthenticationProfileFromSDAFabric')
def getDefaultAuthenticationProfileFromSDAFabric(**kwargs):
    return CatalystClient().getDefaultAuthenticationProfileFromSDAFabric(**kwargs)

@register('addDefaultAuthenticationTemplateInSDAFabric')
def addDefaultAuthenticationTemplateInSDAFabric(**kwargs):
    return CatalystClient().addDefaultAuthenticationTemplateInSDAFabric(**kwargs)

@register('reserveIPSubpool')
def reserveIPSubpool(**kwargs):
    return CatalystClient().reserveIPSubpool(**kwargs)

@register('updateReserveIPSubpool')
def updateReserveIPSubpool(**kwargs):
    return CatalystClient().updateReserveIPSubpool(**kwargs)

@register('pSKOverride')
def pSKOverride(**kwargs):
    return CatalystClient().pSKOverride(**kwargs)

@register('assignDeviceCredentialToSite')
def assignDeviceCredentialToSite(**kwargs):
    return CatalystClient().assignDeviceCredentialToSite(**kwargs)

@register('re-ProvisionWiredDevice')
def re_ProvisionWiredDevice(**kwargs):
    return CatalystClient().re_ProvisionWiredDevice(**kwargs)

@register('provisionWiredDevice')
def provisionWiredDevice(**kwargs):
    return CatalystClient().provisionWiredDevice(**kwargs)

@register('deleteProvisionedWiredDevice')
def deleteProvisionedWiredDevice(**kwargs):
    return CatalystClient().deleteProvisionedWiredDevice(**kwargs)

@register('getProvisionedWiredDevice')
def getProvisionedWiredDevice(**kwargs):
    return CatalystClient().getProvisionedWiredDevice(**kwargs)

@register('updateDeviceCredentials')
def updateDeviceCredentials(**kwargs):
    return CatalystClient().updateDeviceCredentials(**kwargs)

@register('getDeviceCredentialDetails')
def getDeviceCredentialDetails(**kwargs):
    return CatalystClient().getDeviceCredentialDetails(**kwargs)

@register('createDeviceCredentials')
def createDeviceCredentials(**kwargs):
    return CatalystClient().createDeviceCredentials(**kwargs)

@register('deleteSiteFromSDAFabric')
def deleteSiteFromSDAFabric(**kwargs):
    return CatalystClient().deleteSiteFromSDAFabric(**kwargs)

@register('getSiteFromSDAFabric')
def getSiteFromSDAFabric(**kwargs):
    return CatalystClient().getSiteFromSDAFabric(**kwargs)

@register('addSiteInSDAFabric')
def addSiteInSDAFabric(**kwargs):
    return CatalystClient().addSiteInSDAFabric(**kwargs)

@register('updateSPProfile')
def updateSPProfile(**kwargs):
    return CatalystClient().updateSPProfile(**kwargs)

@register('getServiceProviderDetails')
def getServiceProviderDetails(**kwargs):
    return CatalystClient().getServiceProviderDetails(**kwargs)

@register('createSPProfile')
def createSPProfile(**kwargs):
    return CatalystClient().createSPProfile(**kwargs)

@register('createSite')
def createSite(**kwargs):
    return CatalystClient().createSite(**kwargs)

@register('getSite')
def getSite(**kwargs):
    return CatalystClient().getSite(**kwargs)

@register('updateNetwork')
def updateNetwork(**kwargs):
    return CatalystClient().updateNetwork(**kwargs)

@register('createNetwork')
def createNetwork(**kwargs):
    return CatalystClient().createNetwork(**kwargs)

@register('getVirtualNetworkSummary')
def getVirtualNetworkSummary(**kwargs):
    return CatalystClient().getVirtualNetworkSummary(**kwargs)

@register('createWirelessProfile-2')
def createWirelessProfile_2(**kwargs):
    return CatalystClient().createWirelessProfile_2(**kwargs)

@register('getWirelessProfile')
def getWirelessProfile(**kwargs):
    return CatalystClient().getWirelessProfile(**kwargs)

@register('updateWirelessProfile-2')
def updateWirelessProfile_2(**kwargs):
    return CatalystClient().updateWirelessProfile_2(**kwargs)

@register('releaseReserveIPSubpool')
def releaseReserveIPSubpool(**kwargs):
    return CatalystClient().releaseReserveIPSubpool(**kwargs)

@register('duplicateSensorTestTemplate')
def duplicateSensorTestTemplate(**kwargs):
    return CatalystClient().duplicateSensorTestTemplate(**kwargs)

@register('getIssueEnrichmentDetails')
def getIssueEnrichmentDetails(**kwargs):
    return CatalystClient().getIssueEnrichmentDetails(**kwargs)

@register('provisionUpdate')
def provisionUpdate(**kwargs):
    return CatalystClient().provisionUpdate(**kwargs)

@register('provision')
def provision(**kwargs):
    return CatalystClient().provision(**kwargs)

@register('sensorTestResults')
def sensorTestResults(**kwargs):
    return CatalystClient().sensorTestResults(**kwargs)

@register('getDeviceRoleInSDAFabric')
def getDeviceRoleInSDAFabric(**kwargs):
    return CatalystClient().getDeviceRoleInSDAFabric(**kwargs)

@register('createEnterpriseSSID')
def createEnterpriseSSID(**kwargs):
    return CatalystClient().createEnterpriseSSID(**kwargs)

@register('updateEnterpriseSSID')
def updateEnterpriseSSID(**kwargs):
    return CatalystClient().updateEnterpriseSSID(**kwargs)

@register('getEnterpriseSSID')
def getEnterpriseSSID(**kwargs):
    return CatalystClient().getEnterpriseSSID(**kwargs)

@register('assignDevicesToSite')
def assignDevicesToSite(**kwargs):
    return CatalystClient().assignDevicesToSite(**kwargs)

@register('getBorderDeviceDetailFromSDAFabric')
def getBorderDeviceDetailFromSDAFabric(**kwargs):
    return CatalystClient().getBorderDeviceDetailFromSDAFabric(**kwargs)

@register('addBorderDeviceInSDAFabric')
def addBorderDeviceInSDAFabric(**kwargs):
    return CatalystClient().addBorderDeviceInSDAFabric(**kwargs)

@register('deleteBorderDeviceFromSDAFabric')
def deleteBorderDeviceFromSDAFabric(**kwargs):
    return CatalystClient().deleteBorderDeviceFromSDAFabric(**kwargs)

@register('addPortAssignmentForUserDeviceInSDAFabric')
def addPortAssignmentForUserDeviceInSDAFabric(**kwargs):
    return CatalystClient().addPortAssignmentForUserDeviceInSDAFabric(**kwargs)

@register('getPortAssignmentForUserDeviceInSDAFabric')
def getPortAssignmentForUserDeviceInSDAFabric(**kwargs):
    return CatalystClient().getPortAssignmentForUserDeviceInSDAFabric(**kwargs)

@register('deletePortAssignmentForUserDeviceInSDAFabric')
def deletePortAssignmentForUserDeviceInSDAFabric(**kwargs):
    return CatalystClient().deletePortAssignmentForUserDeviceInSDAFabric(**kwargs)

@register('getFailedITSMEvents')
def getFailedITSMEvents(**kwargs):
    return CatalystClient().getFailedITSMEvents(**kwargs)

@register('retryIntegrationEvents')
def retryIntegrationEvents(**kwargs):
    return CatalystClient().retryIntegrationEvents(**kwargs)

@register('updateSSIDToIPPoolMapping')
def updateSSIDToIPPoolMapping(**kwargs):
    return CatalystClient().updateSSIDToIPPoolMapping(**kwargs)

@register('addSSIDToIPPoolMapping')
def addSSIDToIPPoolMapping(**kwargs):
    return CatalystClient().addSSIDToIPPoolMapping(**kwargs)

@register('getSSIDToIPPoolMapping')
def getSSIDToIPPoolMapping(**kwargs):
    return CatalystClient().getSSIDToIPPoolMapping(**kwargs)

@register('getControlPlaneDeviceFromSDAFabric')
def getControlPlaneDeviceFromSDAFabric(**kwargs):
    return CatalystClient().getControlPlaneDeviceFromSDAFabric(**kwargs)

@register('addControlPlaneDeviceInSDAFabric')
def addControlPlaneDeviceInSDAFabric(**kwargs):
    return CatalystClient().addControlPlaneDeviceInSDAFabric(**kwargs)

@register('deleteControlPlaneDeviceInSDAFabric')
def deleteControlPlaneDeviceInSDAFabric(**kwargs):
    return CatalystClient().deleteControlPlaneDeviceInSDAFabric(**kwargs)

@register('getCMDBSyncStatus')
def getCMDBSyncStatus(**kwargs):
    return CatalystClient().getCMDBSyncStatus(**kwargs)

@register('getSiteCount')
def getSiteCount(**kwargs):
    return CatalystClient().getSiteCount(**kwargs)

@register('getClientEnrichmentDetails')
def getClientEnrichmentDetails(**kwargs):
    return CatalystClient().getClientEnrichmentDetails(**kwargs)

@register('updateVirtualNetworkWithScalableGroups')
def updateVirtualNetworkWithScalableGroups(**kwargs):
    return CatalystClient().updateVirtualNetworkWithScalableGroups(**kwargs)

@register('deleteVirtualNetworkWithScalableGroups')
def deleteVirtualNetworkWithScalableGroups(**kwargs):
    return CatalystClient().deleteVirtualNetworkWithScalableGroups(**kwargs)

@register('addVirtualNetworkWithScalableGroups')
def addVirtualNetworkWithScalableGroups(**kwargs):
    return CatalystClient().addVirtualNetworkWithScalableGroups(**kwargs)

@register('getVirtualNetworkWithScalableGroups')
def getVirtualNetworkWithScalableGroups(**kwargs):
    return CatalystClient().getVirtualNetworkWithScalableGroups(**kwargs)

@register('editSensorTestTemplate')
def editSensorTestTemplate(**kwargs):
    return CatalystClient().editSensorTestTemplate(**kwargs)

@register('deleteEnterpriseSSID')
def deleteEnterpriseSSID(**kwargs):
    return CatalystClient().deleteEnterpriseSSID(**kwargs)

@register('getDynamicInterface')
def getDynamicInterface(**kwargs):
    return CatalystClient().getDynamicInterface(**kwargs)

@register('createUpdateDynamicInterface')
def createUpdateDynamicInterface(**kwargs):
    return CatalystClient().createUpdateDynamicInterface(**kwargs)

@register('deleteDynamicInterface')
def deleteDynamicInterface(**kwargs):
    return CatalystClient().deleteDynamicInterface(**kwargs)

@register('executeSuggestedActionsCommands')
def executeSuggestedActionsCommands(**kwargs):
    return CatalystClient().executeSuggestedActionsCommands(**kwargs)

@register('getApplicationSetsCount')
def getApplicationSetsCount(**kwargs):
    return CatalystClient().getApplicationSetsCount(**kwargs)

@register('getUserEnrichmentDetails')
def getUserEnrichmentDetails(**kwargs):
    return CatalystClient().getUserEnrichmentDetails(**kwargs)

@register('aPProvision-2')
def aPProvision_2(**kwargs):
    return CatalystClient().aPProvision_2(**kwargs)

@register('getDeviceEnrichmentDetails')
def getDeviceEnrichmentDetails(**kwargs):
    return CatalystClient().getDeviceEnrichmentDetails(**kwargs)

@register('deleteSite')
def deleteSite(**kwargs):
    return CatalystClient().deleteSite(**kwargs)

@register('updateSite')
def updateSite(**kwargs):
    return CatalystClient().updateSite(**kwargs)

@register('getMembership')
def getMembership(**kwargs):
    return CatalystClient().getMembership(**kwargs)

@register('runNowSensorTest')
def runNowSensorTest(**kwargs):
    return CatalystClient().runNowSensorTest(**kwargs)

@register('deleteWirelessProfile-2')
def deleteWirelessProfile_2(**kwargs):
    return CatalystClient().deleteWirelessProfile_2(**kwargs)

@register('deleteSSIDAndProvisionItToDevices')
def deleteSSIDAndProvisionItToDevices(**kwargs):
    return CatalystClient().deleteSSIDAndProvisionItToDevices(**kwargs)
