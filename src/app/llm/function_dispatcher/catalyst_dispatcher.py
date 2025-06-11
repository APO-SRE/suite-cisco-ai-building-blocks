# app/llm/function_dispatcher/catalyst_dispatcher.py
from app.llm.function_dispatcher import register
from app.llm.platform_clients.catalyst_client import CatalystClient

@register('getSecureXAccessToken')
def getSecureXAccessToken(**kwargs):
    return CatalystClient().getSecureXAccessToken(**kwargs)

@register('getAaaConfig')
def getAaaConfig(**kwargs):
    return CatalystClient().getAaaConfig(**kwargs)

@register('listenAuthEvents')
def listenAuthEvents(**kwargs):
    return CatalystClient().listenAuthEvents(**kwargs)

@register('getRadiusConfig')
def getRadiusConfig(**kwargs):
    return CatalystClient().getRadiusConfig(**kwargs)

@register('getTacacsConfig')
def getTacacsConfig(**kwargs):
    return CatalystClient().getTacacsConfig(**kwargs)

@register('findUsers_1')
def findUsers_1(**kwargs):
    return CatalystClient().findUsers_1(**kwargs)

@register('getActiveSessions_1')
def getActiveSessions_1(**kwargs):
    return CatalystClient().getActiveSessions_1(**kwargs)

@register('findUserRole_1')
def findUserRole_1(**kwargs):
    return CatalystClient().findUserRole_1(**kwargs)

@register('findUserAuthType_1')
def findUserAuthType_1(**kwargs):
    return CatalystClient().findUserAuthType_1(**kwargs)

@register('findUserGroups')
def findUserGroups(**kwargs):
    return CatalystClient().findUserGroups(**kwargs)

@register('createGroupGridColumns')
def createGroupGridColumns(**kwargs):
    return CatalystClient().createGroupGridColumns(**kwargs)

@register('findUserGroupsAsKeyValue')
def findUserGroupsAsKeyValue(**kwargs):
    return CatalystClient().findUserGroupsAsKeyValue(**kwargs)

@register('getVpnGroups')
def getVpnGroups(**kwargs):
    return CatalystClient().getVpnGroups(**kwargs)

@register('getRawAlarmData')
def getRawAlarmData(**kwargs):
    return CatalystClient().getRawAlarmData(**kwargs)

@register('getAggregationData')
def getAggregationData(**kwargs):
    return CatalystClient().getAggregationData(**kwargs)

@register('getNonViewedActiveAlarmsCount')
def getNonViewedActiveAlarmsCount(**kwargs):
    return CatalystClient().getNonViewedActiveAlarmsCount(**kwargs)

@register('listDisabledAlarm')
def listDisabledAlarm(**kwargs):
    return CatalystClient().listDisabledAlarm(**kwargs)

@register('getDocCount')
def getDocCount(**kwargs):
    return CatalystClient().getDocCount(**kwargs)

@register('getAlarmDataFields')
def getAlarmDataFields(**kwargs):
    return CatalystClient().getAlarmDataFields(**kwargs)

@register('getLinkStateAlarmConfig')
def getLinkStateAlarmConfig(**kwargs):
    return CatalystClient().getLinkStateAlarmConfig(**kwargs)

@register('getMasterManagerState')
def getMasterManagerState(**kwargs):
    return CatalystClient().getMasterManagerState(**kwargs)

@register('getNonViewedAlarms')
def getNonViewedAlarms(**kwargs):
    return CatalystClient().getNonViewedAlarms(**kwargs)

@register('getPage')
def getPage(**kwargs):
    return CatalystClient().getPage(**kwargs)

@register('setPeriodicPurgeTimer')
def setPeriodicPurgeTimer(**kwargs):
    return CatalystClient().setPeriodicPurgeTimer(**kwargs)

@register('getAlarmQueryFields')
def getAlarmQueryFields(**kwargs):
    return CatalystClient().getAlarmQueryFields(**kwargs)

@register('getFieldDetails')
def getFieldDetails(**kwargs):
    return CatalystClient().getFieldDetails(**kwargs)

@register('reset')
def reset(**kwargs):
    return CatalystClient().reset(**kwargs)

@register('restartCorrelationEngine')
def restartCorrelationEngine(**kwargs):
    return CatalystClient().restartCorrelationEngine(**kwargs)

@register('getAlarmTypesAsKeyValue')
def getAlarmTypesAsKeyValue(**kwargs):
    return CatalystClient().getAlarmTypesAsKeyValue(**kwargs)

@register('getBySeverity')
def getBySeverity(**kwargs):
    return CatalystClient().getBySeverity(**kwargs)

@register('getAlarmSeverityCustomHistogram')
def getAlarmSeverityCustomHistogram(**kwargs):
    return CatalystClient().getAlarmSeverityCustomHistogram(**kwargs)

@register('getAlarmSeverityMappings')
def getAlarmSeverityMappings(**kwargs):
    return CatalystClient().getAlarmSeverityMappings(**kwargs)

@register('getStats')
def getStats(**kwargs):
    return CatalystClient().getStats(**kwargs)

@register('getDeviceTopic')
def getDeviceTopic(**kwargs):
    return CatalystClient().getDeviceTopic(**kwargs)

@register('getAlarmDetails')
def getAlarmDetails(**kwargs):
    return CatalystClient().getAlarmDetails(**kwargs)

@register('getAllAppList')
def getAllAppList(**kwargs):
    return CatalystClient().getAllAppList(**kwargs)

@register('getAppListCategory')
def getAppListCategory(**kwargs):
    return CatalystClient().getAppListCategory(**kwargs)

@register('getNetworkDiscoveredApps')
def getNetworkDiscoveredApps(**kwargs):
    return CatalystClient().getNetworkDiscoveredApps(**kwargs)

@register('getAttributeMappingForApps')
def getAttributeMappingForApps(**kwargs):
    return CatalystClient().getAttributeMappingForApps(**kwargs)

@register('getKubernetesServices')
def getKubernetesServices(**kwargs):
    return CatalystClient().getKubernetesServices(**kwargs)

@register('getAppByUuid')
def getAppByUuid(**kwargs):
    return CatalystClient().getAppByUuid(**kwargs)

@register('getAppList')
def getAppList(**kwargs):
    return CatalystClient().getAppList(**kwargs)

@register('getKubernetesCluster')
def getKubernetesCluster(**kwargs):
    return CatalystClient().getKubernetesCluster(**kwargs)

@register('getActiveSaasFeeds')
def getActiveSaasFeeds(**kwargs):
    return CatalystClient().getActiveSaasFeeds(**kwargs)

@register('getAllSaasFeedForSelectedApp')
def getAllSaasFeedForSelectedApp(**kwargs):
    return CatalystClient().getAllSaasFeedForSelectedApp(**kwargs)

@register('getStatDataRawAuditLogData')
def getStatDataRawAuditLogData(**kwargs):
    return CatalystClient().getStatDataRawAuditLogData(**kwargs)

@register('getPropertyAggregationData')
def getPropertyAggregationData(**kwargs):
    return CatalystClient().getPropertyAggregationData(**kwargs)

@register('getCount')
def getCount(**kwargs):
    return CatalystClient().getCount(**kwargs)

@register('getStatDataFields')
def getStatDataFields(**kwargs):
    return CatalystClient().getStatDataFields(**kwargs)

@register('getStatBulkRawPropertyData')
def getStatBulkRawPropertyData(**kwargs):
    return CatalystClient().getStatBulkRawPropertyData(**kwargs)

@register('getStatQueryFields')
def getStatQueryFields(**kwargs):
    return CatalystClient().getStatQueryFields(**kwargs)

@register('getAuditSeverityCustomHistogram')
def getAuditSeverityCustomHistogram(**kwargs):
    return CatalystClient().getAuditSeverityCustomHistogram(**kwargs)

@register('getLocalBackupInfo')
def getLocalBackupInfo(**kwargs):
    return CatalystClient().getLocalBackupInfo(**kwargs)

@register('downloadBackupFile')
def downloadBackupFile(**kwargs):
    return CatalystClient().downloadBackupFile(**kwargs)

@register('listBackup')
def listBackup(**kwargs):
    return CatalystClient().listBackup(**kwargs)

@register('getCdnaSenseService')
def getCdnaSenseService(**kwargs):
    return CatalystClient().getCdnaSenseService(**kwargs)

@register('getCdnaServer')
def getCdnaServer(**kwargs):
    return CatalystClient().getCdnaServer(**kwargs)

@register('getControllerCertStatus')
def getControllerCertStatus(**kwargs):
    return CatalystClient().getControllerCertStatus(**kwargs)

@register('getCSRViewRightMenus')
def getCSRViewRightMenus(**kwargs):
    return CatalystClient().getCSRViewRightMenus(**kwargs)

@register('getDeviceViewRightMenus')
def getDeviceViewRightMenus(**kwargs):
    return CatalystClient().getDeviceViewRightMenus(**kwargs)

@register('getDevicesList')
def getDevicesList(**kwargs):
    return CatalystClient().getDevicesList(**kwargs)

@register('getListStatus')
def getListStatus(**kwargs):
    return CatalystClient().getListStatus(**kwargs)

@register('setvSmartMtHubList')
def setvSmartMtHubList(**kwargs):
    return CatalystClient().setvSmartMtHubList(**kwargs)

@register('getQuarantineBanner')
def getQuarantineBanner(**kwargs):
    return CatalystClient().getQuarantineBanner(**kwargs)

@register('getCertificateData')
def getCertificateData(**kwargs):
    return CatalystClient().getCertificateData(**kwargs)

@register('getRootCertChains')
def getRootCertChains(**kwargs):
    return CatalystClient().getRootCertChains(**kwargs)

@register('getRootCertificate')
def getRootCertificate(**kwargs):
    return CatalystClient().getRootCertificate(**kwargs)

@register('rsaKeyLength2048ForAllDevices')
def rsaKeyLength2048ForAllDevices(**kwargs):
    return CatalystClient().rsaKeyLength2048ForAllDevices(**kwargs)

@register('getCertificateDetail')
def getCertificateDetail(**kwargs):
    return CatalystClient().getCertificateDetail(**kwargs)

@register('getCertificateStats')
def getCertificateStats(**kwargs):
    return CatalystClient().getCertificateStats(**kwargs)

@register('syncvBond')
def syncvBond(**kwargs):
    return CatalystClient().syncvBond(**kwargs)

@register('getTokenList')
def getTokenList(**kwargs):
    return CatalystClient().getTokenList(**kwargs)

@register('getInstalledCert')
def getInstalledCert(**kwargs):
    return CatalystClient().getInstalledCert(**kwargs)

@register('getvEdgeCSR')
def getvEdgeCSR(**kwargs):
    return CatalystClient().getvEdgeCSR(**kwargs)

@register('getvEdgeList')
def getvEdgeList(**kwargs):
    return CatalystClient().getvEdgeList(**kwargs)

@register('getView')
def getView(**kwargs):
    return CatalystClient().getView(**kwargs)

@register('getSelfSignedCert')
def getSelfSignedCert(**kwargs):
    return CatalystClient().getSelfSignedCert(**kwargs)

@register('getvSmartList')
def getvSmartList(**kwargs):
    return CatalystClient().getvSmartList(**kwargs)

@register('createServerInfo')
def createServerInfo(**kwargs):
    return CatalystClient().createServerInfo(**kwargs)

@register('getCsrfToken')
def getCsrfToken(**kwargs):
    return CatalystClient().getCsrfToken(**kwargs)

@register('getAccessTokenforDevice')
def getAccessTokenforDevice(**kwargs):
    return CatalystClient().getAccessTokenforDevice(**kwargs)

@register('connect')
def connect(**kwargs):
    return CatalystClient().connect(**kwargs)

@register('getCloudCredentials')
def getCloudCredentials(**kwargs):
    return CatalystClient().getCloudCredentials(**kwargs)

@register('isStaging')
def isStaging(**kwargs):
    return CatalystClient().isStaging(**kwargs)

@register('getTelemetryState')
def getTelemetryState(**kwargs):
    return CatalystClient().getTelemetryState(**kwargs)

@register('getvAnalyticsDashboardList')
def getvAnalyticsDashboardList(**kwargs):
    return CatalystClient().getvAnalyticsDashboardList(**kwargs)

@register('checkIfClusterLocked')
def checkIfClusterLocked(**kwargs):
    return CatalystClient().checkIfClusterLocked(**kwargs)

@register('getClusterWorkflowVersion')
def getClusterWorkflowVersion(**kwargs):
    return CatalystClient().getClusterWorkflowVersion(**kwargs)

@register('getConnectedDevices')
def getConnectedDevices(**kwargs):
    return CatalystClient().getConnectedDevices(**kwargs)

@register('healthDetails')
def healthDetails(**kwargs):
    return CatalystClient().healthDetails(**kwargs)

@register('healthStatusInfo')
def healthStatusInfo(**kwargs):
    return CatalystClient().healthStatusInfo(**kwargs)

@register('healthSummary')
def healthSummary(**kwargs):
    return CatalystClient().healthSummary(**kwargs)

@register('hostHealthStatus')
def hostHealthStatus(**kwargs):
    return CatalystClient().hostHealthStatus(**kwargs)

@register('getConfiguredIPList')
def getConfiguredIPList(**kwargs):
    return CatalystClient().getConfiguredIPList(**kwargs)

@register('isClusterReady')
def isClusterReady(**kwargs):
    return CatalystClient().isClusterReady(**kwargs)

@register('listVmanages')
def listVmanages(**kwargs):
    return CatalystClient().listVmanages(**kwargs)

@register('nodeProperties')
def nodeProperties(**kwargs):
    return CatalystClient().nodeProperties(**kwargs)

@register('getTenancyMode')
def getTenancyMode(**kwargs):
    return CatalystClient().getTenancyMode(**kwargs)

@register('getTenantsList')
def getTenantsList(**kwargs):
    return CatalystClient().getTenantsList(**kwargs)

@register('getVManageDetails')
def getVManageDetails(**kwargs):
    return CatalystClient().getVManageDetails(**kwargs)

@register('getConnectedDevicesPerTenant')
def getConnectedDevicesPerTenant(**kwargs):
    return CatalystClient().getConnectedDevicesPerTenant(**kwargs)

@register('getvnfByDeviceId')
def getvnfByDeviceId(**kwargs):
    return CatalystClient().getvnfByDeviceId(**kwargs)

@register('getVNFEventsCountDetail')
def getVNFEventsCountDetail(**kwargs):
    return CatalystClient().getVNFEventsCountDetail(**kwargs)

@register('getVNFAlarmCount')
def getVNFAlarmCount(**kwargs):
    return CatalystClient().getVNFAlarmCount(**kwargs)

@register('getVNFEventsDetail')
def getVNFEventsDetail(**kwargs):
    return CatalystClient().getVNFEventsDetail(**kwargs)

@register('getVNFInterfaceDetail')
def getVNFInterfaceDetail(**kwargs):
    return CatalystClient().getVNFInterfaceDetail(**kwargs)

@register('doesValidImageExist')
def doesValidImageExist(**kwargs):
    return CatalystClient().doesValidImageExist(**kwargs)

@register('getContainerInspectData')
def getContainerInspectData(**kwargs):
    return CatalystClient().getContainerInspectData(**kwargs)

@register('getContainerSettings')
def getContainerSettings(**kwargs):
    return CatalystClient().getContainerSettings(**kwargs)

@register('generateDeviceStateData')
def generateDeviceStateData(**kwargs):
    return CatalystClient().generateDeviceStateData(**kwargs)

@register('generateDeviceStateDataFields')
def generateDeviceStateDataFields(**kwargs):
    return CatalystClient().generateDeviceStateDataFields(**kwargs)

@register('generateDeviceStateDataWithQueryString')
def generateDeviceStateDataWithQueryString(**kwargs):
    return CatalystClient().generateDeviceStateDataWithQueryString(**kwargs)

@register('getStatisticsType')
def getStatisticsType(**kwargs):
    return CatalystClient().getStatisticsType(**kwargs)

@register('getActiveAlarms')
def getActiveAlarms(**kwargs):
    return CatalystClient().getActiveAlarms(**kwargs)

@register('generateDeviceStatisticsData')
def generateDeviceStatisticsData(**kwargs):
    return CatalystClient().generateDeviceStatisticsData(**kwargs)

@register('getCountWithStateDataType')
def getCountWithStateDataType(**kwargs):
    return CatalystClient().getCountWithStateDataType(**kwargs)

@register('getStatDataFieldsByStateDataType')
def getStatDataFieldsByStateDataType(**kwargs):
    return CatalystClient().getStatDataFieldsByStateDataType(**kwargs)

@register('getCloudSettings')
def getCloudSettings(**kwargs):
    return CatalystClient().getCloudSettings(**kwargs)

@register('getAccessToken')
def getAccessToken(**kwargs):
    return CatalystClient().getAccessToken(**kwargs)

@register('getIdToken')
def getIdToken(**kwargs):
    return CatalystClient().getIdToken(**kwargs)

@register('getOTP')
def getOTP(**kwargs):
    return CatalystClient().getOTP(**kwargs)

@register('getTelemetrySettings')
def getTelemetrySettings(**kwargs):
    return CatalystClient().getTelemetrySettings(**kwargs)

@register('getDCATenantOwners')
def getDCATenantOwners(**kwargs):
    return CatalystClient().getDCATenantOwners(**kwargs)

@register('getCrashLogsSynced')
def getCrashLogsSynced(**kwargs):
    return CatalystClient().getCrashLogsSynced(**kwargs)

@register('getCloudServicesConfigurationDCA')
def getCloudServicesConfigurationDCA(**kwargs):
    return CatalystClient().getCloudServicesConfigurationDCA(**kwargs)

@register('listAllDevices')
def listAllDevices(**kwargs):
    return CatalystClient().listAllDevices(**kwargs)

@register('getAAAservers')
def getAAAservers(**kwargs):
    return CatalystClient().getAAAservers(**kwargs)

@register('getAAAUsers')
def getAAAUsers(**kwargs):
    return CatalystClient().getAAAUsers(**kwargs)

@register('getACLMatchCounterUsers')
def getACLMatchCounterUsers(**kwargs):
    return CatalystClient().getACLMatchCounterUsers(**kwargs)

@register('generateChangePartitionInfo')
def generateChangePartitionInfo(**kwargs):
    return CatalystClient().generateChangePartitionInfo(**kwargs)

@register('generateDeactivateInfo')
def generateDeactivateInfo(**kwargs):
    return CatalystClient().generateDeactivateInfo(**kwargs)

@register('createFilterVPNList')
def createFilterVPNList(**kwargs):
    return CatalystClient().createFilterVPNList(**kwargs)

@register('getFirmwareImages')
def getFirmwareImages(**kwargs):
    return CatalystClient().getFirmwareImages(**kwargs)

@register('getFirmwareDevices')
def getFirmwareDevices(**kwargs):
    return CatalystClient().getFirmwareDevices(**kwargs)

@register('getFirmwareRemoteImage')
def getFirmwareRemoteImage(**kwargs):
    return CatalystClient().getFirmwareRemoteImage(**kwargs)

@register('getDevicesFWUpgrade')
def getDevicesFWUpgrade(**kwargs):
    return CatalystClient().getDevicesFWUpgrade(**kwargs)

@register('getFirmwareImageDetails')
def getFirmwareImageDetails(**kwargs):
    return CatalystClient().getFirmwareImageDetails(**kwargs)

@register('generateInstallInfo')
def generateInstallInfo(**kwargs):
    return CatalystClient().generateInstallInfo(**kwargs)

@register('generateDeviceList')
def generateDeviceList(**kwargs):
    return CatalystClient().generateDeviceList(**kwargs)

@register('generateDeviceActionList')
def generateDeviceActionList(**kwargs):
    return CatalystClient().generateDeviceActionList(**kwargs)

@register('generateRebootInfo')
def generateRebootInfo(**kwargs):
    return CatalystClient().generateRebootInfo(**kwargs)

@register('generateRebootDeviceList')
def generateRebootDeviceList(**kwargs):
    return CatalystClient().generateRebootDeviceList(**kwargs)

@register('generateRediscoverInfo')
def generateRediscoverInfo(**kwargs):
    return CatalystClient().generateRediscoverInfo(**kwargs)

@register('getRemoteServerList')
def getRemoteServerList(**kwargs):
    return CatalystClient().getRemoteServerList(**kwargs)

@register('getRemoteServerById')
def getRemoteServerById(**kwargs):
    return CatalystClient().getRemoteServerById(**kwargs)

@register('generateRemovePartitionInfo')
def generateRemovePartitionInfo(**kwargs):
    return CatalystClient().generateRemovePartitionInfo(**kwargs)

@register('testApiKey')
def testApiKey(**kwargs):
    return CatalystClient().testApiKey(**kwargs)

@register('generateSecurityDevicesList')
def generateSecurityDevicesList(**kwargs):
    return CatalystClient().generateSecurityDevicesList(**kwargs)

@register('findSoftwareImages')
def findSoftwareImages(**kwargs):
    return CatalystClient().findSoftwareImages(**kwargs)

@register('getImageProperties')
def getImageProperties(**kwargs):
    return CatalystClient().getImageProperties(**kwargs)

@register('findSoftwareImagesWithFilters')
def findSoftwareImagesWithFilters(**kwargs):
    return CatalystClient().findSoftwareImagesWithFilters(**kwargs)

@register('getUploadImagesCount')
def getUploadImagesCount(**kwargs):
    return CatalystClient().getUploadImagesCount(**kwargs)

@register('generateUtdImageData')
def generateUtdImageData(**kwargs):
    return CatalystClient().generateUtdImageData(**kwargs)

@register('downloadPackageFile')
def downloadPackageFile(**kwargs):
    return CatalystClient().downloadPackageFile(**kwargs)

@register('getImageMetadata')
def getImageMetadata(**kwargs):
    return CatalystClient().getImageMetadata(**kwargs)

@register('getImageRemoteServer')
def getImageRemoteServer(**kwargs):
    return CatalystClient().getImageRemoteServer(**kwargs)

@register('findVEdgeSoftwareVersion')
def findVEdgeSoftwareVersion(**kwargs):
    return CatalystClient().findVEdgeSoftwareVersion(**kwargs)

@register('findSoftwareVersion')
def findSoftwareVersion(**kwargs):
    return CatalystClient().findSoftwareVersion(**kwargs)

@register('getVnfProperties')
def getVnfProperties(**kwargs):
    return CatalystClient().getVnfProperties(**kwargs)

@register('findZtpSoftwareVersion')
def findZtpSoftwareVersion(**kwargs):
    return CatalystClient().findZtpSoftwareVersion(**kwargs)

@register('triggerPendingTasksMonitoring')
def triggerPendingTasksMonitoring(**kwargs):
    return CatalystClient().triggerPendingTasksMonitoring(**kwargs)

@register('cleanStatus')
def cleanStatus(**kwargs):
    return CatalystClient().cleanStatus(**kwargs)

@register('getMaintenanceWindowFlag')
def getMaintenanceWindowFlag(**kwargs):
    return CatalystClient().getMaintenanceWindowFlag(**kwargs)

@register('findRunningTasks')
def findRunningTasks(**kwargs):
    return CatalystClient().findRunningTasks(**kwargs)

@register('getActiveTaskCount')
def getActiveTaskCount(**kwargs):
    return CatalystClient().getActiveTaskCount(**kwargs)

@register('getCleanStatus')
def getCleanStatus(**kwargs):
    return CatalystClient().getCleanStatus(**kwargs)

@register('findStatus')
def findStatus(**kwargs):
    return CatalystClient().findStatus(**kwargs)

@register('testIoxConfig')
def testIoxConfig(**kwargs):
    return CatalystClient().testIoxConfig(**kwargs)

@register('createVPNList')
def createVPNList(**kwargs):
    return CatalystClient().createVPNList(**kwargs)

@register('getZTPUpgradeConfig')
def getZTPUpgradeConfig(**kwargs):
    return CatalystClient().getZTPUpgradeConfig(**kwargs)

@register('getZTPUpgradeConfigSetting')
def getZTPUpgradeConfigSetting(**kwargs):
    return CatalystClient().getZTPUpgradeConfigSetting(**kwargs)

@register('getAppHostingAttachedDevices')
def getAppHostingAttachedDevices(**kwargs):
    return CatalystClient().getAppHostingAttachedDevices(**kwargs)

@register('getAppHostingDetails')
def getAppHostingDetails(**kwargs):
    return CatalystClient().getAppHostingDetails(**kwargs)

@register('getAppHostingGuestRoutes')
def getAppHostingGuestRoutes(**kwargs):
    return CatalystClient().getAppHostingGuestRoutes(**kwargs)

@register('getAppHostingNetworkDevices')
def getAppHostingNetworkDevices(**kwargs):
    return CatalystClient().getAppHostingNetworkDevices(**kwargs)

@register('getAppHostingNetworkUtils')
def getAppHostingNetworkUtils(**kwargs):
    return CatalystClient().getAppHostingNetworkUtils(**kwargs)

@register('getAppHostingProcesses')
def getAppHostingProcesses(**kwargs):
    return CatalystClient().getAppHostingProcesses(**kwargs)

@register('getAppHostingStorageUtils')
def getAppHostingStorageUtils(**kwargs):
    return CatalystClient().getAppHostingStorageUtils(**kwargs)

@register('getAppHostingUtilization')
def getAppHostingUtilization(**kwargs):
    return CatalystClient().getAppHostingUtilization(**kwargs)

@register('createAppRouteSlaClassList')
def createAppRouteSlaClassList(**kwargs):
    return CatalystClient().createAppRouteSlaClassList(**kwargs)

@register('createAppRouteStatisticsList')
def createAppRouteStatisticsList(**kwargs):
    return CatalystClient().createAppRouteStatisticsList(**kwargs)

@register('getAppLogFlowCount')
def getAppLogFlowCount(**kwargs):
    return CatalystClient().getAppLogFlowCount(**kwargs)

@register('getAppLogFlows')
def getAppLogFlows(**kwargs):
    return CatalystClient().getAppLogFlows(**kwargs)

@register('createAppqoeActiveFlowIdDetails')
def createAppqoeActiveFlowIdDetails(**kwargs):
    return CatalystClient().createAppqoeActiveFlowIdDetails(**kwargs)

@register('getAppqoeHputStats')
def getAppqoeHputStats(**kwargs):
    return CatalystClient().getAppqoeHputStats(**kwargs)

@register('getAppqoeNatStats')
def getAppqoeNatStats(**kwargs):
    return CatalystClient().getAppqoeNatStats(**kwargs)

@register('getAppqoeRmResources')
def getAppqoeRmResources(**kwargs):
    return CatalystClient().getAppqoeRmResources(**kwargs)

@register('getAppqoeRMStats')
def getAppqoeRMStats(**kwargs):
    return CatalystClient().getAppqoeRMStats(**kwargs)

@register('getAppqoeServicesStatus')
def getAppqoeServicesStatus(**kwargs):
    return CatalystClient().getAppqoeServicesStatus(**kwargs)

@register('getAppqoeSppiPipeStats')
def getAppqoeSppiPipeStats(**kwargs):
    return CatalystClient().getAppqoeSppiPipeStats(**kwargs)

@register('getAppqoeSppiQueueStats')
def getAppqoeSppiQueueStats(**kwargs):
    return CatalystClient().getAppqoeSppiQueueStats(**kwargs)

@register('getAppqoeClusterSummary')
def getAppqoeClusterSummary(**kwargs):
    return CatalystClient().getAppqoeClusterSummary(**kwargs)

@register('getAppqoeErrorRecent')
def getAppqoeErrorRecent(**kwargs):
    return CatalystClient().getAppqoeErrorRecent(**kwargs)

@register('createAppqoeFlowIdExpiredDetails')
def createAppqoeFlowIdExpiredDetails(**kwargs):
    return CatalystClient().createAppqoeFlowIdExpiredDetails(**kwargs)

@register('getAppqoeFlowClosedError')
def getAppqoeFlowClosedError(**kwargs):
    return CatalystClient().getAppqoeFlowClosedError(**kwargs)

@register('getAppqoeExpired')
def getAppqoeExpired(**kwargs):
    return CatalystClient().getAppqoeExpired(**kwargs)

@register('getAppqoeServiceControllers')
def getAppqoeServiceControllers(**kwargs):
    return CatalystClient().getAppqoeServiceControllers(**kwargs)

@register('getAppqoeStatus')
def getAppqoeStatus(**kwargs):
    return CatalystClient().getAppqoeStatus(**kwargs)

@register('createAppqoeVpnIdList')
def createAppqoeVpnIdList(**kwargs):
    return CatalystClient().createAppqoeVpnIdList(**kwargs)

@register('getARPInterface')
def getARPInterface(**kwargs):
    return CatalystClient().getARPInterface(**kwargs)

@register('getAutonomousSoftwareVersion')
def getAutonomousSoftwareVersion(**kwargs):
    return CatalystClient().getAutonomousSoftwareVersion(**kwargs)

@register('createBFDHistoryList')
def createBFDHistoryList(**kwargs):
    return CatalystClient().createBFDHistoryList(**kwargs)

@register('createBFDLinkList')
def createBFDLinkList(**kwargs):
    return CatalystClient().createBFDLinkList(**kwargs)

@register('createBFDSessions')
def createBFDSessions(**kwargs):
    return CatalystClient().createBFDSessions(**kwargs)

@register('getBFDSiteStateDetail')
def getBFDSiteStateDetail(**kwargs):
    return CatalystClient().getBFDSiteStateDetail(**kwargs)

@register('getBFDSitesSummary')
def getBFDSitesSummary(**kwargs):
    return CatalystClient().getBFDSitesSummary(**kwargs)

@register('getDeviceBFDStateSummary')
def getDeviceBFDStateSummary(**kwargs):
    return CatalystClient().getDeviceBFDStateSummary(**kwargs)

@register('getDeviceBFDStateSummaryTloc')
def getDeviceBFDStateSummaryTloc(**kwargs):
    return CatalystClient().getDeviceBFDStateSummaryTloc(**kwargs)

@register('getDeviceTlocToIntfList')
def getDeviceTlocToIntfList(**kwargs):
    return CatalystClient().getDeviceTlocToIntfList(**kwargs)

@register('getDeviceBFDStatus')
def getDeviceBFDStatus(**kwargs):
    return CatalystClient().getDeviceBFDStatus(**kwargs)

@register('createBFDSummary')
def createBFDSummary(**kwargs):
    return CatalystClient().createBFDSummary(**kwargs)

@register('getDeviceBFDStatusSummary')
def getDeviceBFDStatusSummary(**kwargs):
    return CatalystClient().getDeviceBFDStatusSummary(**kwargs)

@register('createSyncedBFDSession')
def createSyncedBFDSession(**kwargs):
    return CatalystClient().createSyncedBFDSession(**kwargs)

@register('createTLOCSummary')
def createTLOCSummary(**kwargs):
    return CatalystClient().createTLOCSummary(**kwargs)

@register('getBFDTlocStateDetail')
def getBFDTlocStateDetail(**kwargs):
    return CatalystClient().getBFDTlocStateDetail(**kwargs)

@register('createBGPNeighborsList')
def createBGPNeighborsList(**kwargs):
    return CatalystClient().createBGPNeighborsList(**kwargs)

@register('createBGPRoutesList')
def createBGPRoutesList(**kwargs):
    return CatalystClient().createBGPRoutesList(**kwargs)

@register('createBGPSummary')
def createBGPSummary(**kwargs):
    return CatalystClient().createBGPSummary(**kwargs)

@register('getBridgeInterfaceList')
def getBridgeInterfaceList(**kwargs):
    return CatalystClient().getBridgeInterfaceList(**kwargs)

@register('getBridgeInterfaceMac')
def getBridgeInterfaceMac(**kwargs):
    return CatalystClient().getBridgeInterfaceMac(**kwargs)

@register('getBridgeInterfaceTable')
def getBridgeInterfaceTable(**kwargs):
    return CatalystClient().getBridgeInterfaceTable(**kwargs)

@register('getTenantsDevicesAndSites')
def getTenantsDevicesAndSites(**kwargs):
    return CatalystClient().getTenantsDevicesAndSites(**kwargs)

@register('createAppFwdCflowdFlowsList')
def createAppFwdCflowdFlowsList(**kwargs):
    return CatalystClient().createAppFwdCflowdFlowsList(**kwargs)

@register('createAppFwdCflowdV6FlowsList')
def createAppFwdCflowdV6FlowsList(**kwargs):
    return CatalystClient().createAppFwdCflowdV6FlowsList(**kwargs)

@register('createCellularConnectionList')
def createCellularConnectionList(**kwargs):
    return CatalystClient().createCellularConnectionList(**kwargs)

@register('cellularCountDashlet')
def cellularCountDashlet(**kwargs):
    return CatalystClient().cellularCountDashlet(**kwargs)

@register('dataUsage')
def dataUsage(**kwargs):
    return CatalystClient().dataUsage(**kwargs)

@register('cellularCountDashletDetails')
def cellularCountDashletDetails(**kwargs):
    return CatalystClient().cellularCountDashletDetails(**kwargs)

@register('createHardwareList')
def createHardwareList(**kwargs):
    return CatalystClient().createHardwareList(**kwargs)

@register('cellularHealthDashlet')
def cellularHealthDashlet(**kwargs):
    return CatalystClient().cellularHealthDashlet(**kwargs)

@register('createModemList')
def createModemList(**kwargs):
    return CatalystClient().createModemList(**kwargs)

@register('createNetworkList')
def createNetworkList(**kwargs):
    return CatalystClient().createNetworkList(**kwargs)

@register('createProfileList')
def createProfileList(**kwargs):
    return CatalystClient().createProfileList(**kwargs)

@register('createRadioList')
def createRadioList(**kwargs):
    return CatalystClient().createRadioList(**kwargs)

@register('createSessionsList')
def createSessionsList(**kwargs):
    return CatalystClient().createSessionsList(**kwargs)

@register('getCellularStatusList')
def getCellularStatusList(**kwargs):
    return CatalystClient().getCellularStatusList(**kwargs)

@register('getEiolteConnectionInfo')
def getEiolteConnectionInfo(**kwargs):
    return CatalystClient().getEiolteConnectionInfo(**kwargs)

@register('getEiolteHardwareInfo')
def getEiolteHardwareInfo(**kwargs):
    return CatalystClient().getEiolteHardwareInfo(**kwargs)

@register('getAONIpsecInterfaceCountersInfo')
def getAONIpsecInterfaceCountersInfo(**kwargs):
    return CatalystClient().getAONIpsecInterfaceCountersInfo(**kwargs)

@register('getAONIpsecInterfaceSessionnfo')
def getAONIpsecInterfaceSessionnfo(**kwargs):
    return CatalystClient().getAONIpsecInterfaceSessionnfo(**kwargs)

@register('getEiolteNetworkInfo')
def getEiolteNetworkInfo(**kwargs):
    return CatalystClient().getEiolteNetworkInfo(**kwargs)

@register('getEiolteRadioInfo')
def getEiolteRadioInfo(**kwargs):
    return CatalystClient().getEiolteRadioInfo(**kwargs)

@register('getEiolteSimInfo')
def getEiolteSimInfo(**kwargs):
    return CatalystClient().getEiolteSimInfo(**kwargs)

@register('getCflowdDPIDeviceFieldJSON')
def getCflowdDPIDeviceFieldJSON(**kwargs):
    return CatalystClient().getCflowdDPIDeviceFieldJSON(**kwargs)

@register('createCflowdCollectorList')
def createCflowdCollectorList(**kwargs):
    return CatalystClient().createCflowdCollectorList(**kwargs)

@register('getCflowdDPIFieldJSON')
def getCflowdDPIFieldJSON(**kwargs):
    return CatalystClient().getCflowdDPIFieldJSON(**kwargs)

@register('createCflowCollectorList')
def createCflowCollectorList(**kwargs):
    return CatalystClient().createCflowCollectorList(**kwargs)

@register('createCflowdFlowsCountList')
def createCflowdFlowsCountList(**kwargs):
    return CatalystClient().createCflowdFlowsCountList(**kwargs)

@register('getFnFCacheStats')
def getFnFCacheStats(**kwargs):
    return CatalystClient().getFnFCacheStats(**kwargs)

@register('getFnFExportClientStats')
def getFnFExportClientStats(**kwargs):
    return CatalystClient().getFnFExportClientStats(**kwargs)

@register('getFnFExportStats')
def getFnFExportStats(**kwargs):
    return CatalystClient().getFnFExportStats(**kwargs)

@register('getFnf')
def getFnf(**kwargs):
    return CatalystClient().getFnf(**kwargs)

@register('getFnFMonitorStats')
def getFnFMonitorStats(**kwargs):
    return CatalystClient().getFnFMonitorStats(**kwargs)

@register('createCflowdStatistics')
def createCflowdStatistics(**kwargs):
    return CatalystClient().createCflowdStatistics(**kwargs)

@register('createCflowdTemplate')
def createCflowdTemplate(**kwargs):
    return CatalystClient().createCflowdTemplate(**kwargs)

@register('getMpDatabase')
def getMpDatabase(**kwargs):
    return CatalystClient().getMpDatabase(**kwargs)

@register('getMpLocalMep')
def getMpLocalMep(**kwargs):
    return CatalystClient().getMpLocalMep(**kwargs)

@register('getMpLocalMip')
def getMpLocalMip(**kwargs):
    return CatalystClient().getMpLocalMip(**kwargs)

@register('getMpRemoteMep')
def getMpRemoteMep(**kwargs):
    return CatalystClient().getMpRemoteMep(**kwargs)

@register('createApplicationsDetailList')
def createApplicationsDetailList(**kwargs):
    return CatalystClient().createApplicationsDetailList(**kwargs)

@register('createApplicationsList')
def createApplicationsList(**kwargs):
    return CatalystClient().createApplicationsList(**kwargs)

@register('createGatewayExitsList')
def createGatewayExitsList(**kwargs):
    return CatalystClient().createGatewayExitsList(**kwargs)

@register('createLbApplicationsList')
def createLbApplicationsList(**kwargs):
    return CatalystClient().createLbApplicationsList(**kwargs)

@register('createLocalExitsList')
def createLocalExitsList(**kwargs):
    return CatalystClient().createLocalExitsList(**kwargs)

@register('getComplianceDetails')
def getComplianceDetails(**kwargs):
    return CatalystClient().getComplianceDetails(**kwargs)

@register('getComplianceSummary')
def getComplianceSummary(**kwargs):
    return CatalystClient().getComplianceSummary(**kwargs)

@register('getDeviceRunningConfig')
def getDeviceRunningConfig(**kwargs):
    return CatalystClient().getDeviceRunningConfig(**kwargs)

@register('getDeviceRunningConfigHTML')
def getDeviceRunningConfigHTML(**kwargs):
    return CatalystClient().getDeviceRunningConfigHTML(**kwargs)

@register('getDeviceConfigurationCommitList')
def getDeviceConfigurationCommitList(**kwargs):
    return CatalystClient().getDeviceConfigurationCommitList(**kwargs)

@register('getAffinityConfig')
def getAffinityConfig(**kwargs):
    return CatalystClient().getAffinityConfig(**kwargs)

@register('getAffinityStatus')
def getAffinityStatus(**kwargs):
    return CatalystClient().getAffinityStatus(**kwargs)

@register('createRealTimeConnectionList')
def createRealTimeConnectionList(**kwargs):
    return CatalystClient().createRealTimeConnectionList(**kwargs)

@register('createConnectionHistoryListRealTime')
def createConnectionHistoryListRealTime(**kwargs):
    return CatalystClient().createConnectionHistoryListRealTime(**kwargs)

@register('createRealTimeConnectionList_1')
def createRealTimeConnectionList_1(**kwargs):
    return CatalystClient().createRealTimeConnectionList_1(**kwargs)

@register('getTotalCountForDeviceStates')
def getTotalCountForDeviceStates(**kwargs):
    return CatalystClient().getTotalCountForDeviceStates(**kwargs)

@register('createLinkList')
def createLinkList(**kwargs):
    return CatalystClient().createLinkList(**kwargs)

@register('createLocalPropertiesListListRealTIme')
def createLocalPropertiesListListRealTIme(**kwargs):
    return CatalystClient().createLocalPropertiesListListRealTIme(**kwargs)

@register('networkSummary')
def networkSummary(**kwargs):
    return CatalystClient().networkSummary(**kwargs)

@register('createRealTimeRegionConnectionList')
def createRealTimeRegionConnectionList(**kwargs):
    return CatalystClient().createRealTimeRegionConnectionList(**kwargs)

@register('getConnectionStatistics')
def getConnectionStatistics(**kwargs):
    return CatalystClient().getConnectionStatistics(**kwargs)

@register('getLocalDeviceStatus')
def getLocalDeviceStatus(**kwargs):
    return CatalystClient().getLocalDeviceStatus(**kwargs)

@register('createConnectionsSummary')
def createConnectionsSummary(**kwargs):
    return CatalystClient().createConnectionsSummary(**kwargs)

@register('getDeviceControlStatusSummary')
def getDeviceControlStatusSummary(**kwargs):
    return CatalystClient().getDeviceControlStatusSummary(**kwargs)

@register('createSyncedConnectionList')
def createSyncedConnectionList(**kwargs):
    return CatalystClient().createSyncedConnectionList(**kwargs)

@register('createLocalPropertiesSyncedList')
def createLocalPropertiesSyncedList(**kwargs):
    return CatalystClient().createLocalPropertiesSyncedList(**kwargs)

@register('createWanInterfaceSyncedList')
def createWanInterfaceSyncedList(**kwargs):
    return CatalystClient().createWanInterfaceSyncedList(**kwargs)

@register('createValidDevicesListRealTime')
def createValidDevicesListRealTime(**kwargs):
    return CatalystClient().createValidDevicesListRealTime(**kwargs)

@register('getValidVManageIdRealTime')
def getValidVManageIdRealTime(**kwargs):
    return CatalystClient().getValidVManageIdRealTime(**kwargs)

@register('createValidVSmartsListRealTime')
def createValidVSmartsListRealTime(**kwargs):
    return CatalystClient().createValidVSmartsListRealTime(**kwargs)

@register('createWanInterfaceListList')
def createWanInterfaceListList(**kwargs):
    return CatalystClient().createWanInterfaceListList(**kwargs)

@register('getPortHopColor')
def getPortHopColor(**kwargs):
    return CatalystClient().getPortHopColor(**kwargs)

@register('getDeviceCounters')
def getDeviceCounters(**kwargs):
    return CatalystClient().getDeviceCounters(**kwargs)

@register('getDeviceCrashLogs')
def getDeviceCrashLogs(**kwargs):
    return CatalystClient().getDeviceCrashLogs(**kwargs)

@register('getAllDeviceCrashLogs')
def getAllDeviceCrashLogs(**kwargs):
    return CatalystClient().getAllDeviceCrashLogs(**kwargs)

@register('getDeviceCrashInformation')
def getDeviceCrashInformation(**kwargs):
    return CatalystClient().getDeviceCrashInformation(**kwargs)

@register('getDeviceCrashLogsSynced')
def getDeviceCrashLogsSynced(**kwargs):
    return CatalystClient().getDeviceCrashLogsSynced(**kwargs)

@register('createDeviceContainersInfo')
def createDeviceContainersInfo(**kwargs):
    return CatalystClient().createDeviceContainersInfo(**kwargs)

@register('getPnicStats')
def getPnicStats(**kwargs):
    return CatalystClient().getPnicStats(**kwargs)

@register('getPNICStatsFromDevice')
def getPNICStatsFromDevice(**kwargs):
    return CatalystClient().getPNICStatsFromDevice(**kwargs)

@register('getRBACInterface')
def getRBACInterface(**kwargs):
    return CatalystClient().getRBACInterface(**kwargs)

@register('getAllocationInfo')
def getAllocationInfo(**kwargs):
    return CatalystClient().getAllocationInfo(**kwargs)

@register('getCPUInfo')
def getCPUInfo(**kwargs):
    return CatalystClient().getCPUInfo(**kwargs)

@register('getVNFInfo')
def getVNFInfo(**kwargs):
    return CatalystClient().getVNFInfo(**kwargs)

@register('createDeviceSystemSettingNativeInfo')
def createDeviceSystemSettingNativeInfo(**kwargs):
    return CatalystClient().createDeviceSystemSettingNativeInfo(**kwargs)

@register('createDeviceSystemProcessList')
def createDeviceSystemProcessList(**kwargs):
    return CatalystClient().createDeviceSystemProcessList(**kwargs)

@register('createDeviceSystemSetting')
def createDeviceSystemSetting(**kwargs):
    return CatalystClient().createDeviceSystemSetting(**kwargs)

@register('createDeviceSystemStatus')
def createDeviceSystemStatus(**kwargs):
    return CatalystClient().createDeviceSystemStatus(**kwargs)

@register('getCtsPac')
def getCtsPac(**kwargs):
    return CatalystClient().getCtsPac(**kwargs)

@register('getDeviceOnlyStatus')
def getDeviceOnlyStatus(**kwargs):
    return CatalystClient().getDeviceOnlyStatus(**kwargs)

@register('getDHCPClient')
def getDHCPClient(**kwargs):
    return CatalystClient().getDHCPClient(**kwargs)

@register('getDHCPInterface')
def getDHCPInterface(**kwargs):
    return CatalystClient().getDHCPInterface(**kwargs)

@register('getDHCPServer')
def getDHCPServer(**kwargs):
    return CatalystClient().getDHCPServer(**kwargs)

@register('getDHCPv6Interface')
def getDHCPv6Interface(**kwargs):
    return CatalystClient().getDHCPv6Interface(**kwargs)

@register('getWLANDOT1xClients')
def getWLANDOT1xClients(**kwargs):
    return CatalystClient().getWLANDOT1xClients(**kwargs)

@register('getWLANDOT1xInterfaces')
def getWLANDOT1xInterfaces(**kwargs):
    return CatalystClient().getWLANDOT1xInterfaces(**kwargs)

@register('getDOT1xRadius')
def getDOT1xRadius(**kwargs):
    return CatalystClient().getDOT1xRadius(**kwargs)

@register('createSoftwareList')
def createSoftwareList(**kwargs):
    return CatalystClient().createSoftwareList(**kwargs)

@register('getSupportedApplicationList')
def getSupportedApplicationList(**kwargs):
    return CatalystClient().getSupportedApplicationList(**kwargs)

@register('getDPIDeviceFieldJSON')
def getDPIDeviceFieldJSON(**kwargs):
    return CatalystClient().getDPIDeviceFieldJSON(**kwargs)

@register('createDPICollectorList')
def createDPICollectorList(**kwargs):
    return CatalystClient().createDPICollectorList(**kwargs)

@register('getCommonApplicationList')
def getCommonApplicationList(**kwargs):
    return CatalystClient().getCommonApplicationList(**kwargs)

@register('getDPIFieldJSON')
def getDPIFieldJSON(**kwargs):
    return CatalystClient().getDPIFieldJSON(**kwargs)

@register('getDPIDeviceDetailsFieldJSON')
def getDPIDeviceDetailsFieldJSON(**kwargs):
    return CatalystClient().getDPIDeviceDetailsFieldJSON(**kwargs)

@register('createDPIFlowsList')
def createDPIFlowsList(**kwargs):
    return CatalystClient().createDPIFlowsList(**kwargs)

@register('getQosmosStaticApplicationList')
def getQosmosStaticApplicationList(**kwargs):
    return CatalystClient().getQosmosStaticApplicationList(**kwargs)

@register('getQosmosApplicationList')
def getQosmosApplicationList(**kwargs):
    return CatalystClient().getQosmosApplicationList(**kwargs)

@register('createDPISummaryRealTime')
def createDPISummaryRealTime(**kwargs):
    return CatalystClient().createDPISummaryRealTime(**kwargs)

@register('createDPIStatistics')
def createDPIStatistics(**kwargs):
    return CatalystClient().createDPIStatistics(**kwargs)

@register('getDreAutoBypassStats')
def getDreAutoBypassStats(**kwargs):
    return CatalystClient().getDreAutoBypassStats(**kwargs)

@register('getDreStats')
def getDreStats(**kwargs):
    return CatalystClient().getDreStats(**kwargs)

@register('getDreStatus')
def getDreStatus(**kwargs):
    return CatalystClient().getDreStatus(**kwargs)

@register('getDrePeerStats')
def getDrePeerStats(**kwargs):
    return CatalystClient().getDrePeerStats(**kwargs)

@register('getDualStaticRouteTrackerInfo')
def getDualStaticRouteTrackerInfo(**kwargs):
    return CatalystClient().getDualStaticRouteTrackerInfo(**kwargs)

@register('createEIGRPInterface')
def createEIGRPInterface(**kwargs):
    return CatalystClient().createEIGRPInterface(**kwargs)

@register('createEIGRPRoute')
def createEIGRPRoute(**kwargs):
    return CatalystClient().createEIGRPRoute(**kwargs)

@register('createEIGRPTopology')
def createEIGRPTopology(**kwargs):
    return CatalystClient().createEIGRPTopology(**kwargs)

@register('getEndpointTrackerInfo')
def getEndpointTrackerInfo(**kwargs):
    return CatalystClient().getEndpointTrackerInfo(**kwargs)

@register('getEndpointTrackerGroupInfo')
def getEndpointTrackerGroupInfo(**kwargs):
    return CatalystClient().getEndpointTrackerGroupInfo(**kwargs)

@register('getEnvironmentData')
def getEnvironmentData(**kwargs):
    return CatalystClient().getEnvironmentData(**kwargs)

@register('getRadiusServer')
def getRadiusServer(**kwargs):
    return CatalystClient().getRadiusServer(**kwargs)

@register('getFeatureList')
def getFeatureList(**kwargs):
    return CatalystClient().getFeatureList(**kwargs)

@register('getSyncedFeatureList')
def getSyncedFeatureList(**kwargs):
    return CatalystClient().getSyncedFeatureList(**kwargs)

@register('getDataCollectionStatusForDevice')
def getDataCollectionStatusForDevice(**kwargs):
    return CatalystClient().getDataCollectionStatusForDevice(**kwargs)

@register('downloadGeneratedFile')
def downloadGeneratedFile(**kwargs):
    return CatalystClient().downloadGeneratedFile(**kwargs)

@register('getDataCollectionStatusForUUID')
def getDataCollectionStatusForUUID(**kwargs):
    return CatalystClient().getDataCollectionStatusForUUID(**kwargs)

@register('getSupportedCommandsList')
def getSupportedCommandsList(**kwargs):
    return CatalystClient().getSupportedCommandsList(**kwargs)

@register('getGeofenceStatus')
def getGeofenceStatus(**kwargs):
    return CatalystClient().getGeofenceStatus(**kwargs)

@register('createAlarmList')
def createAlarmList(**kwargs):
    return CatalystClient().createAlarmList(**kwargs)

@register('createEnvironmentList')
def createEnvironmentList(**kwargs):
    return CatalystClient().createEnvironmentList(**kwargs)

@register('createErrorAlarmList')
def createErrorAlarmList(**kwargs):
    return CatalystClient().createErrorAlarmList(**kwargs)

@register('createInventoryList')
def createInventoryList(**kwargs):
    return CatalystClient().createInventoryList(**kwargs)

@register('createStatusSummary')
def createStatusSummary(**kwargs):
    return CatalystClient().createStatusSummary(**kwargs)

@register('createSyncedAlarmList')
def createSyncedAlarmList(**kwargs):
    return CatalystClient().createSyncedAlarmList(**kwargs)

@register('createSyncedEnvironmentList')
def createSyncedEnvironmentList(**kwargs):
    return CatalystClient().createSyncedEnvironmentList(**kwargs)

@register('createSyncedInventoryList')
def createSyncedInventoryList(**kwargs):
    return CatalystClient().createSyncedInventoryList(**kwargs)

@register('createSystemList')
def createSystemList(**kwargs):
    return CatalystClient().createSystemList(**kwargs)

@register('createTempThresholdList')
def createTempThresholdList(**kwargs):
    return CatalystClient().createTempThresholdList(**kwargs)

@register('getHardwareHealthDetails')
def getHardwareHealthDetails(**kwargs):
    return CatalystClient().getHardwareHealthDetails(**kwargs)

@register('getHardwareHealthSummary')
def getHardwareHealthSummary(**kwargs):
    return CatalystClient().getHardwareHealthSummary(**kwargs)

@register('getAggregationDataByQuery_23')
def getAggregationDataByQuery_23(**kwargs):
    return CatalystClient().getAggregationDataByQuery_23(**kwargs)

@register('getLastThousandConfigList')
def getLastThousandConfigList(**kwargs):
    return CatalystClient().getLastThousandConfigList(**kwargs)

@register('getConfigDiff')
def getConfigDiff(**kwargs):
    return CatalystClient().getConfigDiff(**kwargs)

@register('getDeviceConfig')
def getDeviceConfig(**kwargs):
    return CatalystClient().getDeviceConfig(**kwargs)

@register('getStatDataRawDataAsCSV_21')
def getStatDataRawDataAsCSV_21(**kwargs):
    return CatalystClient().getStatDataRawDataAsCSV_21(**kwargs)

@register('getCount_20')
def getCount_20(**kwargs):
    return CatalystClient().getCount_20(**kwargs)

@register('getStatDataFields_22')
def getStatDataFields_22(**kwargs):
    return CatalystClient().getStatDataFields_22(**kwargs)

@register('getStatsPaginationRawData_19')
def getStatsPaginationRawData_19(**kwargs):
    return CatalystClient().getStatsPaginationRawData_19(**kwargs)

@register('getStatQueryFields_23')
def getStatQueryFields_23(**kwargs):
    return CatalystClient().getStatQueryFields_23(**kwargs)

@register('createIGMPGroupsList')
def createIGMPGroupsList(**kwargs):
    return CatalystClient().createIGMPGroupsList(**kwargs)

@register('createIGMPInterfaceList')
def createIGMPInterfaceList(**kwargs):
    return CatalystClient().createIGMPInterfaceList(**kwargs)

@register('createIGMPStatisticsList')
def createIGMPStatisticsList(**kwargs):
    return CatalystClient().createIGMPStatisticsList(**kwargs)

@register('createIGMPSummary')
def createIGMPSummary(**kwargs):
    return CatalystClient().createIGMPSummary(**kwargs)

@register('getDeviceInterface')
def getDeviceInterface(**kwargs):
    return CatalystClient().getDeviceInterface(**kwargs)

@register('getDeviceInterfaceARPStats')
def getDeviceInterfaceARPStats(**kwargs):
    return CatalystClient().getDeviceInterfaceARPStats(**kwargs)

@register('getDeviceInterfaceErrorStats')
def getDeviceInterfaceErrorStats(**kwargs):
    return CatalystClient().getDeviceInterfaceErrorStats(**kwargs)

@register('getDeviceInterfaceIpv6Stats')
def getDeviceInterfaceIpv6Stats(**kwargs):
    return CatalystClient().getDeviceInterfaceIpv6Stats(**kwargs)

@register('getDeviceInterfacePktSizes')
def getDeviceInterfacePktSizes(**kwargs):
    return CatalystClient().getDeviceInterfacePktSizes(**kwargs)

@register('getDeviceInterfacePortStats')
def getDeviceInterfacePortStats(**kwargs):
    return CatalystClient().getDeviceInterfacePortStats(**kwargs)

@register('getDeviceInterfaceQosStats')
def getDeviceInterfaceQosStats(**kwargs):
    return CatalystClient().getDeviceInterfaceQosStats(**kwargs)

@register('getDeviceInterfaceQueueStats')
def getDeviceInterfaceQueueStats(**kwargs):
    return CatalystClient().getDeviceInterfaceQueueStats(**kwargs)

@register('getDeviceSerialInterface')
def getDeviceSerialInterface(**kwargs):
    return CatalystClient().getDeviceSerialInterface(**kwargs)

@register('getDeviceInterfaceStats')
def getDeviceInterfaceStats(**kwargs):
    return CatalystClient().getDeviceInterfaceStats(**kwargs)

@register('getSyncedDeviceInterface')
def getSyncedDeviceInterface(**kwargs):
    return CatalystClient().getSyncedDeviceInterface(**kwargs)

@register('trustsec')
def trustsec(**kwargs):
    return CatalystClient().trustsec(**kwargs)

@register('generateDeviceInterfaceVPN')
def generateDeviceInterfaceVPN(**kwargs):
    return CatalystClient().generateDeviceInterfaceVPN(**kwargs)

@register('createFibList')
def createFibList(**kwargs):
    return CatalystClient().createFibList(**kwargs)

@register('createIetfRoutingList')
def createIetfRoutingList(**kwargs):
    return CatalystClient().createIetfRoutingList(**kwargs)

@register('createIPMfibOilList')
def createIPMfibOilList(**kwargs):
    return CatalystClient().createIPMfibOilList(**kwargs)

@register('createIPMfibStatsList')
def createIPMfibStatsList(**kwargs):
    return CatalystClient().createIPMfibStatsList(**kwargs)

@register('createIPMfibSummaryList')
def createIPMfibSummaryList(**kwargs):
    return CatalystClient().createIPMfibSummaryList(**kwargs)

@register('createNatFilterList')
def createNatFilterList(**kwargs):
    return CatalystClient().createNatFilterList(**kwargs)

@register('createNatInterfaceList')
def createNatInterfaceList(**kwargs):
    return CatalystClient().createNatInterfaceList(**kwargs)

@register('createNatInterfaceStatisticsList')
def createNatInterfaceStatisticsList(**kwargs):
    return CatalystClient().createNatInterfaceStatisticsList(**kwargs)

@register('createNatTranslationList')
def createNatTranslationList(**kwargs):
    return CatalystClient().createNatTranslationList(**kwargs)

@register('createNat64TranslationList')
def createNat64TranslationList(**kwargs):
    return CatalystClient().createNat64TranslationList(**kwargs)

@register('createRouteTableList')
def createRouteTableList(**kwargs):
    return CatalystClient().createRouteTableList(**kwargs)

@register('createIPv4FibList')
def createIPv4FibList(**kwargs):
    return CatalystClient().createIPv4FibList(**kwargs)

@register('createIPv6FibList')
def createIPv6FibList(**kwargs):
    return CatalystClient().createIPv6FibList(**kwargs)

@register('createCryptoIpsecIdentity')
def createCryptoIpsecIdentity(**kwargs):
    return CatalystClient().createCryptoIpsecIdentity(**kwargs)

@register('createIkeInboundList')
def createIkeInboundList(**kwargs):
    return CatalystClient().createIkeInboundList(**kwargs)

@register('createIkeOutboundList')
def createIkeOutboundList(**kwargs):
    return CatalystClient().createIkeOutboundList(**kwargs)

@register('createIkeSessions')
def createIkeSessions(**kwargs):
    return CatalystClient().createIkeSessions(**kwargs)

@register('createCryptov1LocalSAList')
def createCryptov1LocalSAList(**kwargs):
    return CatalystClient().createCryptov1LocalSAList(**kwargs)

@register('createCryptov2LocalSAList')
def createCryptov2LocalSAList(**kwargs):
    return CatalystClient().createCryptov2LocalSAList(**kwargs)

@register('createInBoundList')
def createInBoundList(**kwargs):
    return CatalystClient().createInBoundList(**kwargs)

@register('createLocalSAList')
def createLocalSAList(**kwargs):
    return CatalystClient().createLocalSAList(**kwargs)

@register('createOutBoundList')
def createOutBoundList(**kwargs):
    return CatalystClient().createOutBoundList(**kwargs)

@register('createIPsecPWKInboundConnections')
def createIPsecPWKInboundConnections(**kwargs):
    return CatalystClient().createIPsecPWKInboundConnections(**kwargs)

@register('createIPsecPWKLocalSA')
def createIPsecPWKLocalSA(**kwargs):
    return CatalystClient().createIPsecPWKLocalSA(**kwargs)

@register('createIPsecPWKOutboundConnections')
def createIPsecPWKOutboundConnections(**kwargs):
    return CatalystClient().createIPsecPWKOutboundConnections(**kwargs)

@register('getIpv6Data')
def getIpv6Data(**kwargs):
    return CatalystClient().getIpv6Data(**kwargs)

@register('getDeviceListAsKeyValue')
def getDeviceListAsKeyValue(**kwargs):
    return CatalystClient().getDeviceListAsKeyValue(**kwargs)

@register('getLacpInterfaceList')
def getLacpInterfaceList(**kwargs):
    return CatalystClient().getLacpInterfaceList(**kwargs)

@register('getLacpMembers')
def getLacpMembers(**kwargs):
    return CatalystClient().getLacpMembers(**kwargs)

@register('getLicenseEvalInfo')
def getLicenseEvalInfo(**kwargs):
    return CatalystClient().getLicenseEvalInfo(**kwargs)

@register('getLicensePAKInfo')
def getLicensePAKInfo(**kwargs):
    return CatalystClient().getLicensePAKInfo(**kwargs)

@register('getLicensePrivacyInfo')
def getLicensePrivacyInfo(**kwargs):
    return CatalystClient().getLicensePrivacyInfo(**kwargs)

@register('getLicenseRegInfo')
def getLicenseRegInfo(**kwargs):
    return CatalystClient().getLicenseRegInfo(**kwargs)

@register('getLicenseUDIInfo')
def getLicenseUDIInfo(**kwargs):
    return CatalystClient().getLicenseUDIInfo(**kwargs)

@register('getLicenseUsageInfo')
def getLicenseUsageInfo(**kwargs):
    return CatalystClient().getLicenseUsageInfo(**kwargs)

@register('getLoggingFromDevice')
def getLoggingFromDevice(**kwargs):
    return CatalystClient().getLoggingFromDevice(**kwargs)

@register('listAllDeviceModels')
def listAllDeviceModels(**kwargs):
    return CatalystClient().listAllDeviceModels(**kwargs)

@register('getDeviceModels')
def getDeviceModels(**kwargs):
    return CatalystClient().getDeviceModels(**kwargs)

@register('listAllMonitorDetailsDevices')
def listAllMonitorDetailsDevices(**kwargs):
    return CatalystClient().listAllMonitorDetailsDevices(**kwargs)

@register('createReplicatorList')
def createReplicatorList(**kwargs):
    return CatalystClient().createReplicatorList(**kwargs)

@register('createRpfList')
def createRpfList(**kwargs):
    return CatalystClient().createRpfList(**kwargs)

@register('createTopologyList')
def createTopologyList(**kwargs):
    return CatalystClient().createTopologyList(**kwargs)

@register('createPimTunnelList')
def createPimTunnelList(**kwargs):
    return CatalystClient().createPimTunnelList(**kwargs)

@register('getIpv6Interface')
def getIpv6Interface(**kwargs):
    return CatalystClient().getIpv6Interface(**kwargs)

@register('getRunning')
def getRunning(**kwargs):
    return CatalystClient().getRunning(**kwargs)

@register('createAssociationsList')
def createAssociationsList(**kwargs):
    return CatalystClient().createAssociationsList(**kwargs)

@register('createPeerList')
def createPeerList(**kwargs):
    return CatalystClient().createPeerList(**kwargs)

@register('createNTPStatusList')
def createNTPStatusList(**kwargs):
    return CatalystClient().createNTPStatusList(**kwargs)

@register('createOMPCloudXRecv')
def createOMPCloudXRecv(**kwargs):
    return CatalystClient().createOMPCloudXRecv(**kwargs)

@register('createOMPLinkList')
def createOMPLinkList(**kwargs):
    return CatalystClient().createOMPLinkList(**kwargs)

@register('createOMPMcastAutoDiscoverAdvt')
def createOMPMcastAutoDiscoverAdvt(**kwargs):
    return CatalystClient().createOMPMcastAutoDiscoverAdvt(**kwargs)

@register('createOMPMcastAutoDiscoverRecv')
def createOMPMcastAutoDiscoverRecv(**kwargs):
    return CatalystClient().createOMPMcastAutoDiscoverRecv(**kwargs)

@register('createOMPMcastRoutesAdvt')
def createOMPMcastRoutesAdvt(**kwargs):
    return CatalystClient().createOMPMcastRoutesAdvt(**kwargs)

@register('createOMPMcastRoutesRecv')
def createOMPMcastRoutesRecv(**kwargs):
    return CatalystClient().createOMPMcastRoutesRecv(**kwargs)

@register('createOMPSessionList')
def createOMPSessionList(**kwargs):
    return CatalystClient().createOMPSessionList(**kwargs)

@register('createAdvertisedRoutesList')
def createAdvertisedRoutesList(**kwargs):
    return CatalystClient().createAdvertisedRoutesList(**kwargs)

@register('createAdvertisedRoutesListIpv6')
def createAdvertisedRoutesListIpv6(**kwargs):
    return CatalystClient().createAdvertisedRoutesListIpv6(**kwargs)

@register('createReceivedRoutesList')
def createReceivedRoutesList(**kwargs):
    return CatalystClient().createReceivedRoutesList(**kwargs)

@register('createReceivedRoutesListIpv6')
def createReceivedRoutesListIpv6(**kwargs):
    return CatalystClient().createReceivedRoutesListIpv6(**kwargs)

@register('createOMPServices')
def createOMPServices(**kwargs):
    return CatalystClient().createOMPServices(**kwargs)

@register('getDeviceOMPStatus')
def getDeviceOMPStatus(**kwargs):
    return CatalystClient().getDeviceOMPStatus(**kwargs)

@register('createOMPSummary')
def createOMPSummary(**kwargs):
    return CatalystClient().createOMPSummary(**kwargs)

@register('createSyncedOMPSessionList')
def createSyncedOMPSessionList(**kwargs):
    return CatalystClient().createSyncedOMPSessionList(**kwargs)

@register('createAdvertisedTlocsList')
def createAdvertisedTlocsList(**kwargs):
    return CatalystClient().createAdvertisedTlocsList(**kwargs)

@register('createReceivedTlocsList')
def createReceivedTlocsList(**kwargs):
    return CatalystClient().createReceivedTlocsList(**kwargs)

@register('getOnDemandLocal')
def getOnDemandLocal(**kwargs):
    return CatalystClient().getOnDemandLocal(**kwargs)

@register('getOnDemandRemote')
def getOnDemandRemote(**kwargs):
    return CatalystClient().getOnDemandRemote(**kwargs)

@register('createConnectionListFromDevice')
def createConnectionListFromDevice(**kwargs):
    return CatalystClient().createConnectionListFromDevice(**kwargs)

@register('createConnectionHistoryList')
def createConnectionHistoryList(**kwargs):
    return CatalystClient().createConnectionHistoryList(**kwargs)

@register('createLocalPropertiesListList')
def createLocalPropertiesListList(**kwargs):
    return CatalystClient().createLocalPropertiesListList(**kwargs)

@register('createReverseProxyMappingList')
def createReverseProxyMappingList(**kwargs):
    return CatalystClient().createReverseProxyMappingList(**kwargs)

@register('getStatistics')
def getStatistics(**kwargs):
    return CatalystClient().getStatistics(**kwargs)

@register('createConnectionSummary')
def createConnectionSummary(**kwargs):
    return CatalystClient().createConnectionSummary(**kwargs)

@register('createValidDevicesList')
def createValidDevicesList(**kwargs):
    return CatalystClient().createValidDevicesList(**kwargs)

@register('getValidVManageId')
def getValidVManageId(**kwargs):
    return CatalystClient().getValidVManageId(**kwargs)

@register('createValidVSmartsList')
def createValidVSmartsList(**kwargs):
    return CatalystClient().createValidVSmartsList(**kwargs)

@register('createOSPFDatabaseList')
def createOSPFDatabaseList(**kwargs):
    return CatalystClient().createOSPFDatabaseList(**kwargs)

@register('createOSPFDatabaseExternal')
def createOSPFDatabaseExternal(**kwargs):
    return CatalystClient().createOSPFDatabaseExternal(**kwargs)

@register('createOSPFDatabaseSummaryList')
def createOSPFDatabaseSummaryList(**kwargs):
    return CatalystClient().createOSPFDatabaseSummaryList(**kwargs)

@register('createOSPFInterface')
def createOSPFInterface(**kwargs):
    return CatalystClient().createOSPFInterface(**kwargs)

@register('createOSPFNeighbors')
def createOSPFNeighbors(**kwargs):
    return CatalystClient().createOSPFNeighbors(**kwargs)

@register('createOSPFProcess')
def createOSPFProcess(**kwargs):
    return CatalystClient().createOSPFProcess(**kwargs)

@register('createOSPFRoutesList')
def createOSPFRoutesList(**kwargs):
    return CatalystClient().createOSPFRoutesList(**kwargs)

@register('createOSPFv3Interface')
def createOSPFv3Interface(**kwargs):
    return CatalystClient().createOSPFv3Interface(**kwargs)

@register('createOSPFv3Neighbors')
def createOSPFv3Neighbors(**kwargs):
    return CatalystClient().createOSPFv3Neighbors(**kwargs)

@register('createPIMInterfaceList')
def createPIMInterfaceList(**kwargs):
    return CatalystClient().createPIMInterfaceList(**kwargs)

@register('createPIMNeighborList')
def createPIMNeighborList(**kwargs):
    return CatalystClient().createPIMNeighborList(**kwargs)

@register('createPIMRpMappingList')
def createPIMRpMappingList(**kwargs):
    return CatalystClient().createPIMRpMappingList(**kwargs)

@register('createPIMStatisticsList')
def createPIMStatisticsList(**kwargs):
    return CatalystClient().createPIMStatisticsList(**kwargs)

@register('getDevicePkiTrustpoint')
def getDevicePkiTrustpoint(**kwargs):
    return CatalystClient().getDevicePkiTrustpoint(**kwargs)

@register('getPolicedInterface')
def getPolicedInterface(**kwargs):
    return CatalystClient().getPolicedInterface(**kwargs)

@register('createPolicyAccessListAssociations')
def createPolicyAccessListAssociations(**kwargs):
    return CatalystClient().createPolicyAccessListAssociations(**kwargs)

@register('createPolicyAccessListCounters')
def createPolicyAccessListCounters(**kwargs):
    return CatalystClient().createPolicyAccessListCounters(**kwargs)

@register('createPolicyAccessListNames')
def createPolicyAccessListNames(**kwargs):
    return CatalystClient().createPolicyAccessListNames(**kwargs)

@register('createPolicyAccessListPolicers')
def createPolicyAccessListPolicers(**kwargs):
    return CatalystClient().createPolicyAccessListPolicers(**kwargs)

@register('createPolicyAppRoutePolicyFilter')
def createPolicyAppRoutePolicyFilter(**kwargs):
    return CatalystClient().createPolicyAppRoutePolicyFilter(**kwargs)

@register('createPolicDataPolicyFilter')
def createPolicDataPolicyFilter(**kwargs):
    return CatalystClient().createPolicDataPolicyFilter(**kwargs)

@register('createPolicyFilterMemoryUsage')
def createPolicyFilterMemoryUsage(**kwargs):
    return CatalystClient().createPolicyFilterMemoryUsage(**kwargs)

@register('showVsmartIptoSgtBinding')
def showVsmartIptoSgtBinding(**kwargs):
    return CatalystClient().showVsmartIptoSgtBinding(**kwargs)

@register('showVsmartIptoUserBinding')
def showVsmartIptoUserBinding(**kwargs):
    return CatalystClient().showVsmartIptoUserBinding(**kwargs)

@register('createPolicyAccessListAssociationsIpv6')
def createPolicyAccessListAssociationsIpv6(**kwargs):
    return CatalystClient().createPolicyAccessListAssociationsIpv6(**kwargs)

@register('createPolicyAccessListCountersIpv6')
def createPolicyAccessListCountersIpv6(**kwargs):
    return CatalystClient().createPolicyAccessListCountersIpv6(**kwargs)

@register('createPolicyAccessListNamesIpv6')
def createPolicyAccessListNamesIpv6(**kwargs):
    return CatalystClient().createPolicyAccessListNamesIpv6(**kwargs)

@register('createPolicyAccessListPolicersIpv6')
def createPolicyAccessListPolicersIpv6(**kwargs):
    return CatalystClient().createPolicyAccessListPolicersIpv6(**kwargs)

@register('showVsmartPxGridStatus')
def showVsmartPxGridStatus(**kwargs):
    return CatalystClient().showVsmartPxGridStatus(**kwargs)

@register('showVsmartPxGridUserSessions')
def showVsmartPxGridUserSessions(**kwargs):
    return CatalystClient().showVsmartPxGridUserSessions(**kwargs)

@register('createPolicQosMapInfo')
def createPolicQosMapInfo(**kwargs):
    return CatalystClient().createPolicQosMapInfo(**kwargs)

@register('createPolicQosSchedulerInfo')
def createPolicQosSchedulerInfo(**kwargs):
    return CatalystClient().createPolicQosSchedulerInfo(**kwargs)

@register('createPolicyRewriteAssociationsInfo')
def createPolicyRewriteAssociationsInfo(**kwargs):
    return CatalystClient().createPolicyRewriteAssociationsInfo(**kwargs)

@register('showVsmartUserUsergroupBindings')
def showVsmartUserUsergroupBindings(**kwargs):
    return CatalystClient().showVsmartUserUsergroupBindings(**kwargs)

@register('showSdwanPolicyFromVsmart')
def showSdwanPolicyFromVsmart(**kwargs):
    return CatalystClient().showSdwanPolicyFromVsmart(**kwargs)

@register('getZoneDropStatistics')
def getZoneDropStatistics(**kwargs):
    return CatalystClient().getZoneDropStatistics(**kwargs)

@register('getZbfwStatistics')
def getZbfwStatistics(**kwargs):
    return CatalystClient().getZbfwStatistics(**kwargs)

@register('getZonePairSessions')
def getZonePairSessions(**kwargs):
    return CatalystClient().getZonePairSessions(**kwargs)

@register('getZonePairs')
def getZonePairs(**kwargs):
    return CatalystClient().getZonePairs(**kwargs)

@register('getZonePolicyFilters')
def getZonePolicyFilters(**kwargs):
    return CatalystClient().getZonePolicyFilters(**kwargs)

@register('getPowerConsumption')
def getPowerConsumption(**kwargs):
    return CatalystClient().getPowerConsumption(**kwargs)

@register('createPPPInterfaceList')
def createPPPInterfaceList(**kwargs):
    return CatalystClient().createPPPInterfaceList(**kwargs)

@register('createPPPoEInterfaceList')
def createPPPoEInterfaceList(**kwargs):
    return CatalystClient().createPPPoEInterfaceList(**kwargs)

@register('createPPPoENeighborList')
def createPPPoENeighborList(**kwargs):
    return CatalystClient().createPPPoENeighborList(**kwargs)

@register('cpustat')
def cpustat(**kwargs):
    return CatalystClient().cpustat(**kwargs)

@register('memstat')
def memstat(**kwargs):
    return CatalystClient().memstat(**kwargs)

@register('getSyncQueues')
def getSyncQueues(**kwargs):
    return CatalystClient().getSyncQueues(**kwargs)

@register('listReachableDevices')
def listReachableDevices(**kwargs):
    return CatalystClient().listReachableDevices(**kwargs)

@register('createRebootHistoryList')
def createRebootHistoryList(**kwargs):
    return CatalystClient().createRebootHistoryList(**kwargs)

@register('getRebootHistoryDetails')
def getRebootHistoryDetails(**kwargs):
    return CatalystClient().getRebootHistoryDetails(**kwargs)

@register('createSyncedRebootHistoryList')
def createSyncedRebootHistoryList(**kwargs):
    return CatalystClient().createSyncedRebootHistoryList(**kwargs)

@register('getRedundancyGroupAppGroup')
def getRedundancyGroupAppGroup(**kwargs):
    return CatalystClient().getRedundancyGroupAppGroup(**kwargs)

@register('getRoleBasedCounters')
def getRoleBasedCounters(**kwargs):
    return CatalystClient().getRoleBasedCounters(**kwargs)

@register('getRoleBasedIpv6Counters')
def getRoleBasedIpv6Counters(**kwargs):
    return CatalystClient().getRoleBasedIpv6Counters(**kwargs)

@register('getRoleBasedIpv6Permissions')
def getRoleBasedIpv6Permissions(**kwargs):
    return CatalystClient().getRoleBasedIpv6Permissions(**kwargs)

@register('getRoleBasedPermissions')
def getRoleBasedPermissions(**kwargs):
    return CatalystClient().getRoleBasedPermissions(**kwargs)

@register('getRoleBasedSgtMap')
def getRoleBasedSgtMap(**kwargs):
    return CatalystClient().getRoleBasedSgtMap(**kwargs)

@register('getSDWanGlobalDropStatistics')
def getSDWanGlobalDropStatistics(**kwargs):
    return CatalystClient().getSDWanGlobalDropStatistics(**kwargs)

@register('getSDWanStats')
def getSDWanStats(**kwargs):
    return CatalystClient().getSDWanStats(**kwargs)

@register('createSessionList')
def createSessionList(**kwargs):
    return CatalystClient().createSessionList(**kwargs)

@register('getDetail')
def getDetail(**kwargs):
    return CatalystClient().getDetail(**kwargs)

@register('getDiagnostic')
def getDiagnostic(**kwargs):
    return CatalystClient().getDiagnostic(**kwargs)

@register('getDiagnosticMeasurementAlarm')
def getDiagnosticMeasurementAlarm(**kwargs):
    return CatalystClient().getDiagnosticMeasurementAlarm(**kwargs)

@register('getDiagnosticMeasurementValue')
def getDiagnosticMeasurementValue(**kwargs):
    return CatalystClient().getDiagnosticMeasurementValue(**kwargs)

@register('getSigTunnelList')
def getSigTunnelList(**kwargs):
    return CatalystClient().getSigTunnelList(**kwargs)

@register('getSigTunnelTotal')
def getSigTunnelTotal(**kwargs):
    return CatalystClient().getSigTunnelTotal(**kwargs)

@register('tunnelDashboard')
def tunnelDashboard(**kwargs):
    return CatalystClient().tunnelDashboard(**kwargs)

@register('getSigUmbrellaTunnels')
def getSigUmbrellaTunnels(**kwargs):
    return CatalystClient().getSigUmbrellaTunnels(**kwargs)

@register('getSigZscalerTunnels')
def getSigZscalerTunnels(**kwargs):
    return CatalystClient().getSigZscalerTunnels(**kwargs)

@register('createSmuList')
def createSmuList(**kwargs):
    return CatalystClient().createSmuList(**kwargs)

@register('createSyncedSmuList')
def createSyncedSmuList(**kwargs):
    return CatalystClient().createSyncedSmuList(**kwargs)

@register('getAAAUcreateSoftwareListsers')
def getAAAUcreateSoftwareListsers(**kwargs):
    return CatalystClient().getAAAUcreateSoftwareListsers(**kwargs)

@register('createSyncedSoftwareList')
def createSyncedSoftwareList(**kwargs):
    return CatalystClient().createSyncedSoftwareList(**kwargs)

@register('getSSETunnel')
def getSSETunnel(**kwargs):
    return CatalystClient().getSSETunnel(**kwargs)

@register('getSslProxyStatistics')
def getSslProxyStatistics(**kwargs):
    return CatalystClient().getSslProxyStatistics(**kwargs)

@register('getSslProxyStatus')
def getSslProxyStatus(**kwargs):
    return CatalystClient().getSslProxyStatus(**kwargs)

@register('getStaticRouteTrackerInfo')
def getStaticRouteTrackerInfo(**kwargs):
    return CatalystClient().getStaticRouteTrackerInfo(**kwargs)

@register('getStatsQueues')
def getStatsQueues(**kwargs):
    return CatalystClient().getStatsQueues(**kwargs)

@register('getAllDeviceStatus')
def getAllDeviceStatus(**kwargs):
    return CatalystClient().getAllDeviceStatus(**kwargs)

@register('getSxpConnections')
def getSxpConnections(**kwargs):
    return CatalystClient().getSxpConnections(**kwargs)

@register('listCurrentlySyncingDevices')
def listCurrentlySyncingDevices(**kwargs):
    return CatalystClient().listCurrentlySyncingDevices(**kwargs)

@register('getDeviceSystemClock')
def getDeviceSystemClock(**kwargs):
    return CatalystClient().getDeviceSystemClock(**kwargs)

@register('createDeviceInfoList')
def createDeviceInfoList(**kwargs):
    return CatalystClient().createDeviceInfoList(**kwargs)

@register('createDeviceSystemStatsList')
def createDeviceSystemStatsList(**kwargs):
    return CatalystClient().createDeviceSystemStatsList(**kwargs)

@register('createDeviceSystemStatusList')
def createDeviceSystemStatusList(**kwargs):
    return CatalystClient().createDeviceSystemStatusList(**kwargs)

@register('createSyncedDeviceSystemStatusList')
def createSyncedDeviceSystemStatusList(**kwargs):
    return CatalystClient().createSyncedDeviceSystemStatusList(**kwargs)

@register('getActiveTCPFlows')
def getActiveTCPFlows(**kwargs):
    return CatalystClient().getActiveTCPFlows(**kwargs)

@register('getExpiredTCPFlows')
def getExpiredTCPFlows(**kwargs):
    return CatalystClient().getExpiredTCPFlows(**kwargs)

@register('getTCPSummary')
def getTCPSummary(**kwargs):
    return CatalystClient().getTCPSummary(**kwargs)

@register('getTcpProxyStatistics')
def getTcpProxyStatistics(**kwargs):
    return CatalystClient().getTcpProxyStatistics(**kwargs)

@register('getTcpProxyStatus')
def getTcpProxyStatus(**kwargs):
    return CatalystClient().getTcpProxyStatus(**kwargs)

@register('getTiers')
def getTiers(**kwargs):
    return CatalystClient().getTiers(**kwargs)

@register('getDeviceTlocStatus')
def getDeviceTlocStatus(**kwargs):
    return CatalystClient().getDeviceTlocStatus(**kwargs)

@register('getDeviceTlocUtil')
def getDeviceTlocUtil(**kwargs):
    return CatalystClient().getDeviceTlocUtil(**kwargs)

@register('getDeviceTlocUtilDetails')
def getDeviceTlocUtilDetails(**kwargs):
    return CatalystClient().getDeviceTlocUtilDetails(**kwargs)

@register('downloadAdminTechFile')
def downloadAdminTechFile(**kwargs):
    return CatalystClient().downloadAdminTechFile(**kwargs)

@register('getSupportedAdminTechFeatures')
def getSupportedAdminTechFeatures(**kwargs):
    return CatalystClient().getSupportedAdminTechFeatures(**kwargs)

@register('listAdminTechs')
def listAdminTechs(**kwargs):
    return CatalystClient().listAdminTechs(**kwargs)

@register('getInProgressCount')
def getInProgressCount(**kwargs):
    return CatalystClient().getInProgressCount(**kwargs)

@register('getDeviceToolsNetstat')
def getDeviceToolsNetstat(**kwargs):
    return CatalystClient().getDeviceToolsNetstat(**kwargs)

@register('getDeviceToolsNSlookup')
def getDeviceToolsNSlookup(**kwargs):
    return CatalystClient().getDeviceToolsNSlookup(**kwargs)

@register('getRealTimeinfo')
def getRealTimeinfo(**kwargs):
    return CatalystClient().getRealTimeinfo(**kwargs)

@register('getDeviceToolsSS')
def getDeviceToolsSS(**kwargs):
    return CatalystClient().getDeviceToolsSS(**kwargs)

@register('getSystemNetfilter')
def getSystemNetfilter(**kwargs):
    return CatalystClient().getSystemNetfilter(**kwargs)

@register('createTransportConnectionList')
def createTransportConnectionList(**kwargs):
    return CatalystClient().createTransportConnectionList(**kwargs)

@register('createBfdStatisticsList')
def createBfdStatisticsList(**kwargs):
    return CatalystClient().createBfdStatisticsList(**kwargs)

@register('createFecStatistics')
def createFecStatistics(**kwargs):
    return CatalystClient().createFecStatistics(**kwargs)

@register('createGreKeepalivesList')
def createGreKeepalivesList(**kwargs):
    return CatalystClient().createGreKeepalivesList(**kwargs)

@register('createIpsecStatisticsList')
def createIpsecStatisticsList(**kwargs):
    return CatalystClient().createIpsecStatisticsList(**kwargs)

@register('createPacketDuplicateStatistics')
def createPacketDuplicateStatistics(**kwargs):
    return CatalystClient().createPacketDuplicateStatistics(**kwargs)

@register('createStatisticsList')
def createStatisticsList(**kwargs):
    return CatalystClient().createStatisticsList(**kwargs)

@register('createUcseStats')
def createUcseStats(**kwargs):
    return CatalystClient().createUcseStats(**kwargs)

@register('getUmbrellaDevReg')
def getUmbrellaDevReg(**kwargs):
    return CatalystClient().getUmbrellaDevReg(**kwargs)

@register('getUmbrellaDNSCrypt')
def getUmbrellaDNSCrypt(**kwargs):
    return CatalystClient().getUmbrellaDNSCrypt(**kwargs)

@register('getUmbrellaDpStats')
def getUmbrellaDpStats(**kwargs):
    return CatalystClient().getUmbrellaDpStats(**kwargs)

@register('getUmbrellaOverview')
def getUmbrellaOverview(**kwargs):
    return CatalystClient().getUmbrellaOverview(**kwargs)

@register('getUmbrellaConfig')
def getUmbrellaConfig(**kwargs):
    return CatalystClient().getUmbrellaConfig(**kwargs)

@register('getUnclaimedVedges')
def getUnclaimedVedges(**kwargs):
    return CatalystClient().getUnclaimedVedges(**kwargs)

@register('getUnconfigured')
def getUnconfigured(**kwargs):
    return CatalystClient().getUnconfigured(**kwargs)

@register('listUnreachableDevices')
def listUnreachableDevices(**kwargs):
    return CatalystClient().listUnreachableDevices(**kwargs)

@register('getUsersFromDevice')
def getUsersFromDevice(**kwargs):
    return CatalystClient().getUsersFromDevice(**kwargs)

@register('getAllDeviceUsers')
def getAllDeviceUsers(**kwargs):
    return CatalystClient().getAllDeviceUsers(**kwargs)

@register('getUTDDataplaneConfig')
def getUTDDataplaneConfig(**kwargs):
    return CatalystClient().getUTDDataplaneConfig(**kwargs)

@register('getUTDDataplaneGlobal')
def getUTDDataplaneGlobal(**kwargs):
    return CatalystClient().getUTDDataplaneGlobal(**kwargs)

@register('getUTDDataplaneStats')
def getUTDDataplaneStats(**kwargs):
    return CatalystClient().getUTDDataplaneStats(**kwargs)

@register('getUTDDataplaneStatsSummary')
def getUTDDataplaneStatsSummary(**kwargs):
    return CatalystClient().getUTDDataplaneStatsSummary(**kwargs)

@register('getUTDEngineInstanceStatus')
def getUTDEngineInstanceStatus(**kwargs):
    return CatalystClient().getUTDEngineInstanceStatus(**kwargs)

@register('getUTDEngineStatus')
def getUTDEngineStatus(**kwargs):
    return CatalystClient().getUTDEngineStatus(**kwargs)

@register('getUTDFileAnalysisStatus')
def getUTDFileAnalysisStatus(**kwargs):
    return CatalystClient().getUTDFileAnalysisStatus(**kwargs)

@register('getUTDFileReputationStatus')
def getUTDFileReputationStatus(**kwargs):
    return CatalystClient().getUTDFileReputationStatus(**kwargs)

@register('getUTDIpsUpdateStatus')
def getUTDIpsUpdateStatus(**kwargs):
    return CatalystClient().getUTDIpsUpdateStatus(**kwargs)

@register('getSignatureVersionInfo')
def getSignatureVersionInfo(**kwargs):
    return CatalystClient().getSignatureVersionInfo(**kwargs)

@register('getUTDUrlfConnectionStatus')
def getUTDUrlfConnectionStatus(**kwargs):
    return CatalystClient().getUTDUrlfConnectionStatus(**kwargs)

@register('getUTDUrlfUpdateStatus')
def getUTDUrlfUpdateStatus(**kwargs):
    return CatalystClient().getUTDUrlfUpdateStatus(**kwargs)

@register('getUTDVersionStatus')
def getUTDVersionStatus(**kwargs):
    return CatalystClient().getUTDVersionStatus(**kwargs)

@register('getCoLineSpecificStats')
def getCoLineSpecificStats(**kwargs):
    return CatalystClient().getCoLineSpecificStats(**kwargs)

@register('getCoStats')
def getCoStats(**kwargs):
    return CatalystClient().getCoStats(**kwargs)

@register('getCpeLineSpecificStats')
def getCpeLineSpecificStats(**kwargs):
    return CatalystClient().getCpeLineSpecificStats(**kwargs)

@register('getCpeStats')
def getCpeStats(**kwargs):
    return CatalystClient().getCpeStats(**kwargs)

@register('getLineBondingStats')
def getLineBondingStats(**kwargs):
    return CatalystClient().getLineBondingStats(**kwargs)

@register('getLineSpecificStats')
def getLineSpecificStats(**kwargs):
    return CatalystClient().getLineSpecificStats(**kwargs)

@register('getVdslInfo')
def getVdslInfo(**kwargs):
    return CatalystClient().getVdslInfo(**kwargs)

@register('getVedgeInventory')
def getVedgeInventory(**kwargs):
    return CatalystClient().getVedgeInventory(**kwargs)

@register('getVedgeInventorySummary')
def getVedgeInventorySummary(**kwargs):
    return CatalystClient().getVedgeInventorySummary(**kwargs)

@register('createTeList')
def createTeList(**kwargs):
    return CatalystClient().createTeList(**kwargs)

@register('createUtdList')
def createUtdList(**kwargs):
    return CatalystClient().createUtdList(**kwargs)

@register('createWaasList')
def createWaasList(**kwargs):
    return CatalystClient().createWaasList(**kwargs)

@register('getVbranchVMLifecycleNics')
def getVbranchVMLifecycleNics(**kwargs):
    return CatalystClient().getVbranchVMLifecycleNics(**kwargs)

@register('getCloudDockVMLifecycleNics')
def getCloudDockVMLifecycleNics(**kwargs):
    return CatalystClient().getCloudDockVMLifecycleNics(**kwargs)

@register('getVbranchVMLifecycle')
def getVbranchVMLifecycle(**kwargs):
    return CatalystClient().getVbranchVMLifecycle(**kwargs)

@register('getVMLifeCycleState')
def getVMLifeCycleState(**kwargs):
    return CatalystClient().getVMLifeCycleState(**kwargs)

@register('getVManageSystemIP')
def getVManageSystemIP(**kwargs):
    return CatalystClient().getVManageSystemIP(**kwargs)

@register('getDspActive')
def getDspActive(**kwargs):
    return CatalystClient().getDspActive(**kwargs)

@register('getPhoneInfo')
def getPhoneInfo(**kwargs):
    return CatalystClient().getPhoneInfo(**kwargs)

@register('getDSPFarmProfiles')
def getDSPFarmProfiles(**kwargs):
    return CatalystClient().getDSPFarmProfiles(**kwargs)

@register('getSccpCcmGroups')
def getSccpCcmGroups(**kwargs):
    return CatalystClient().getSccpCcmGroups(**kwargs)

@register('getSccpConnections')
def getSccpConnections(**kwargs):
    return CatalystClient().getSccpConnections(**kwargs)

@register('getVoiceCalls')
def getVoiceCalls(**kwargs):
    return CatalystClient().getVoiceCalls(**kwargs)

@register('getVoipCalls')
def getVoipCalls(**kwargs):
    return CatalystClient().getVoipCalls(**kwargs)

@register('getT1e1IsdnStatus')
def getT1e1IsdnStatus(**kwargs):
    return CatalystClient().getT1e1IsdnStatus(**kwargs)

@register('getControllerT1e1InfoCurrent15MinStats')
def getControllerT1e1InfoCurrent15MinStats(**kwargs):
    return CatalystClient().getControllerT1e1InfoCurrent15MinStats(**kwargs)

@register('getControllerT1e1InfoTotalStats')
def getControllerT1e1InfoTotalStats(**kwargs):
    return CatalystClient().getControllerT1e1InfoTotalStats(**kwargs)

@register('getVPNInstances')
def getVPNInstances(**kwargs):
    return CatalystClient().getVPNInstances(**kwargs)

@register('getVRRPInterface')
def getVRRPInterface(**kwargs):
    return CatalystClient().getVRRPInterface(**kwargs)

@register('getWirelessClients')
def getWirelessClients(**kwargs):
    return CatalystClient().getWirelessClients(**kwargs)

@register('getWirelessRadios')
def getWirelessRadios(**kwargs):
    return CatalystClient().getWirelessRadios(**kwargs)

@register('getWirelessSsid')
def getWirelessSsid(**kwargs):
    return CatalystClient().getWirelessSsid(**kwargs)

@register('getWLANClients')
def getWLANClients(**kwargs):
    return CatalystClient().getWLANClients(**kwargs)

@register('getWLANInterfaces')
def getWLANInterfaces(**kwargs):
    return CatalystClient().getWLANInterfaces(**kwargs)

@register('getWLANRadios')
def getWLANRadios(**kwargs):
    return CatalystClient().getWLANRadios(**kwargs)

@register('getWLANRadius')
def getWLANRadius(**kwargs):
    return CatalystClient().getWLANRadius(**kwargs)

@register('getClusterInfo')
def getClusterInfo(**kwargs):
    return CatalystClient().getClusterInfo(**kwargs)

@register('getConfigDBRestoreStatus')
def getConfigDBRestoreStatus(**kwargs):
    return CatalystClient().getConfigDBRestoreStatus(**kwargs)

@register('getDetails')
def getDetails(**kwargs):
    return CatalystClient().getDetails(**kwargs)

@register('getDisasterRecoveryStatus')
def getDisasterRecoveryStatus(**kwargs):
    return CatalystClient().getDisasterRecoveryStatus(**kwargs)

@register('getHistory')
def getHistory(**kwargs):
    return CatalystClient().getHistory(**kwargs)

@register('getLocalHistory')
def getLocalHistory(**kwargs):
    return CatalystClient().getLocalHistory(**kwargs)

@register('getLocalDataCenterState')
def getLocalDataCenterState(**kwargs):
    return CatalystClient().getLocalDataCenterState(**kwargs)

@register('getRemoteDCMembersState')
def getRemoteDCMembersState(**kwargs):
    return CatalystClient().getRemoteDCMembersState(**kwargs)

@register('getRemoteDataCenterState')
def getRemoteDataCenterState(**kwargs):
    return CatalystClient().getRemoteDataCenterState(**kwargs)

@register('getRemoteDataCenterVersion')
def getRemoteDataCenterVersion(**kwargs):
    return CatalystClient().getRemoteDataCenterVersion(**kwargs)

@register('getDisasterRecoveryLocalReplicationSchedule')
def getDisasterRecoveryLocalReplicationSchedule(**kwargs):
    return CatalystClient().getDisasterRecoveryLocalReplicationSchedule(**kwargs)

@register('getdrStatus')
def getdrStatus(**kwargs):
    return CatalystClient().getdrStatus(**kwargs)

@register('get')
def get(**kwargs):
    return CatalystClient().get(**kwargs)

@register('listEntityOwnershipInfo')
def listEntityOwnershipInfo(**kwargs):
    return CatalystClient().listEntityOwnershipInfo(**kwargs)

@register('entityOwnershipInfo')
def entityOwnershipInfo(**kwargs):
    return CatalystClient().entityOwnershipInfo(**kwargs)

@register('getAggregationData_1')
def getAggregationData_1(**kwargs):
    return CatalystClient().getAggregationData_1(**kwargs)

@register('getComponentsAsKeyValue')
def getComponentsAsKeyValue(**kwargs):
    return CatalystClient().getComponentsAsKeyValue(**kwargs)

@register('getDocCount_2')
def getDocCount_2(**kwargs):
    return CatalystClient().getDocCount_2(**kwargs)

@register('enableEventsFromFile')
def enableEventsFromFile(**kwargs):
    return CatalystClient().enableEventsFromFile(**kwargs)

@register('getEventNamesByComponent')
def getEventNamesByComponent(**kwargs):
    return CatalystClient().getEventNamesByComponent(**kwargs)

@register('getListenersInfo')
def getListenersInfo(**kwargs):
    return CatalystClient().getListenersInfo(**kwargs)

@register('getPage_1')
def getPage_1(**kwargs):
    return CatalystClient().getPage_1(**kwargs)

@register('getQueryFields')
def getQueryFields(**kwargs):
    return CatalystClient().getQueryFields(**kwargs)

@register('createEventsQueryConfig')
def createEventsQueryConfig(**kwargs):
    return CatalystClient().createEventsQueryConfig(**kwargs)

@register('getBySeverities')
def getBySeverities(**kwargs):
    return CatalystClient().getBySeverities(**kwargs)

@register('getSeverityHistogram')
def getSeverityHistogram(**kwargs):
    return CatalystClient().getSeverityHistogram(**kwargs)

@register('getEventTypesAsKeyValue')
def getEventTypesAsKeyValue(**kwargs):
    return CatalystClient().getEventTypesAsKeyValue(**kwargs)

@register('getDeviceCertificate')
def getDeviceCertificate(**kwargs):
    return CatalystClient().getDeviceCertificate(**kwargs)

@register('getDeviceCsr')
def getDeviceCsr(**kwargs):
    return CatalystClient().getDeviceCsr(**kwargs)

@register('getFeatureCaState')
def getFeatureCaState(**kwargs):
    return CatalystClient().getFeatureCaState(**kwargs)

@register('requesDNSSecActions')
def requesDNSSecActions(**kwargs):
    return CatalystClient().requesDNSSecActions(**kwargs)

@register('getDNSSecStatus')
def getDNSSecStatus(**kwargs):
    return CatalystClient().getDNSSecStatus(**kwargs)

@register('requestWazuhActions')
def requestWazuhActions(**kwargs):
    return CatalystClient().requestWazuhActions(**kwargs)

@register('getWazuhAgentStatus')
def getWazuhAgentStatus(**kwargs):
    return CatalystClient().getWazuhAgentStatus(**kwargs)

@register('listDeviceGroupList')
def listDeviceGroupList(**kwargs):
    return CatalystClient().listDeviceGroupList(**kwargs)

@register('listDeviceGroups')
def listDeviceGroups(**kwargs):
    return CatalystClient().listDeviceGroups(**kwargs)

@register('listGroupDevices')
def listGroupDevices(**kwargs):
    return CatalystClient().listGroupDevices(**kwargs)

@register('listGroupDevicesForMap')
def listGroupDevicesForMap(**kwargs):
    return CatalystClient().listGroupDevicesForMap(**kwargs)

@register('listGroupLinksForMap')
def listGroupLinksForMap(**kwargs):
    return CatalystClient().listGroupLinksForMap(**kwargs)

@register('getDevicesHealthOverview')
def getDevicesHealthOverview(**kwargs):
    return CatalystClient().getDevicesHealthOverview(**kwargs)

@register('fetchDeviceDetails')
def fetchDeviceDetails(**kwargs):
    return CatalystClient().fetchDeviceDetails(**kwargs)

@register('InstallDeviceDetails')
def InstallDeviceDetails(**kwargs):
    return CatalystClient().InstallDeviceDetails(**kwargs)

@register('fetchSAVAAccounts')
def fetchSAVAAccounts(**kwargs):
    return CatalystClient().fetchSAVAAccounts(**kwargs)

@register('testbedMode')
def testbedMode(**kwargs):
    return CatalystClient().testbedMode(**kwargs)

@register('connect_1')
def connect_1(**kwargs):
    return CatalystClient().connect_1(**kwargs)

@register('getIseServerCredentials')
def getIseServerCredentials(**kwargs):
    return CatalystClient().getIseServerCredentials(**kwargs)

@register('getPxGridAccount')
def getPxGridAccount(**kwargs):
    return CatalystClient().getPxGridAccount(**kwargs)

@register('getPxgridCert')
def getPxgridCert(**kwargs):
    return CatalystClient().getPxgridCert(**kwargs)

@register('getSupportedLocales')
def getSupportedLocales(**kwargs):
    return CatalystClient().getSupportedLocales(**kwargs)

@register('getCategory')
def getCategory(**kwargs):
    return CatalystClient().getCategory(**kwargs)

@register('getvManageResourceUtilization')
def getvManageResourceUtilization(**kwargs):
    return CatalystClient().getvManageResourceUtilization(**kwargs)

@register('retrieveMDPAttachedDevices')
def retrieveMDPAttachedDevices(**kwargs):
    return CatalystClient().retrieveMDPAttachedDevices(**kwargs)

@register('retrieveMDPSupportedDevices')
def retrieveMDPSupportedDevices(**kwargs):
    return CatalystClient().retrieveMDPSupportedDevices(**kwargs)

@register('disconnectFromMDP')
def disconnectFromMDP(**kwargs):
    return CatalystClient().disconnectFromMDP(**kwargs)

@register('getMDPOnboardingStatus')
def getMDPOnboardingStatus(**kwargs):
    return CatalystClient().getMDPOnboardingStatus(**kwargs)

@register('retrieveMDPConfigObject')
def retrieveMDPConfigObject(**kwargs):
    return CatalystClient().retrieveMDPConfigObject(**kwargs)

@register('retrieveMDPPolicies')
def retrieveMDPPolicies(**kwargs):
    return CatalystClient().retrieveMDPPolicies(**kwargs)

@register('createDeviceVmanageConnectionList')
def createDeviceVmanageConnectionList(**kwargs):
    return CatalystClient().createDeviceVmanageConnectionList(**kwargs)

@register('getCloudConnectorDomainAppRules')
def getCloudConnectorDomainAppRules(**kwargs):
    return CatalystClient().getCloudConnectorDomainAppRules(**kwargs)

@register('getCloudConnectorIpAddressAppRules')
def getCloudConnectorIpAddressAppRules(**kwargs):
    return CatalystClient().getCloudConnectorIpAddressAppRules(**kwargs)

@register('getWebexAppData')
def getWebexAppData(**kwargs):
    return CatalystClient().getWebexAppData(**kwargs)

@register('getMSLADevices_1')
def getMSLADevices_1(**kwargs):
    return CatalystClient().getMSLADevices_1(**kwargs)

@register('getLicenseByUuid_1')
def getLicenseByUuid_1(**kwargs):
    return CatalystClient().getLicenseByUuid_1(**kwargs)

@register('getMslaLicenses')
def getMslaLicenses(**kwargs):
    return CatalystClient().getMslaLicenses(**kwargs)

@register('getLicensesCompliance')
def getLicensesCompliance(**kwargs):
    return CatalystClient().getLicensesCompliance(**kwargs)

@register('getDeviceDetailsForDashboard')
def getDeviceDetailsForDashboard(**kwargs):
    return CatalystClient().getDeviceDetailsForDashboard(**kwargs)

@register('getLicenseDistributionDetails')
def getLicenseDistributionDetails(**kwargs):
    return CatalystClient().getLicenseDistributionDetails(**kwargs)

@register('getPackagingDistributionDetails')
def getPackagingDistributionDetails(**kwargs):
    return CatalystClient().getPackagingDistributionDetails(**kwargs)

@register('getAllTemplate')
def getAllTemplate(**kwargs):
    return CatalystClient().getAllTemplate(**kwargs)

@register('getSubscriptions')
def getSubscriptions(**kwargs):
    return CatalystClient().getSubscriptions(**kwargs)

@register('getAllCloudAccounts')
def getAllCloudAccounts(**kwargs):
    return CatalystClient().getAllCloudAccounts(**kwargs)

@register('getEdgeAccounts')
def getEdgeAccounts(**kwargs):
    return CatalystClient().getEdgeAccounts(**kwargs)

@register('getEdgeAccountDetails')
def getEdgeAccountDetails(**kwargs):
    return CatalystClient().getEdgeAccountDetails(**kwargs)

@register('getCloudAccountDetails')
def getCloudAccountDetails(**kwargs):
    return CatalystClient().getCloudAccountDetails(**kwargs)

@register('auditDryRun')
def auditDryRun(**kwargs):
    return CatalystClient().auditDryRun(**kwargs)

@register('getEdgeBillingAccounts')
def getEdgeBillingAccounts(**kwargs):
    return CatalystClient().getEdgeBillingAccounts(**kwargs)

@register('getCloudRoutersAndAttachments')
def getCloudRoutersAndAttachments(**kwargs):
    return CatalystClient().getCloudRoutersAndAttachments(**kwargs)

@register('getCgws')
def getCgws(**kwargs):
    return CatalystClient().getCgws(**kwargs)

@register('getNvaSecurityRules')
def getNvaSecurityRules(**kwargs):
    return CatalystClient().getNvaSecurityRules(**kwargs)

@register('getAzureNetworkVirtualAppliances')
def getAzureNetworkVirtualAppliances(**kwargs):
    return CatalystClient().getAzureNetworkVirtualAppliances(**kwargs)

@register('getAzureNvaSkuResources')
def getAzureNvaSkuResources(**kwargs):
    return CatalystClient().getAzureNvaSkuResources(**kwargs)

@register('getCgwOrgResources')
def getCgwOrgResources(**kwargs):
    return CatalystClient().getCgwOrgResources(**kwargs)

@register('getAzureResourceGroups')
def getAzureResourceGroups(**kwargs):
    return CatalystClient().getAzureResourceGroups(**kwargs)

@register('getAzureVirtualHubs')
def getAzureVirtualHubs(**kwargs):
    return CatalystClient().getAzureVirtualHubs(**kwargs)

@register('getAzureVirtualVnetsAttached')
def getAzureVirtualVnetsAttached(**kwargs):
    return CatalystClient().getAzureVirtualVnetsAttached(**kwargs)

@register('getAzureVpnGateways')
def getAzureVpnGateways(**kwargs):
    return CatalystClient().getAzureVpnGateways(**kwargs)

@register('getAzureVirtualWans')
def getAzureVirtualWans(**kwargs):
    return CatalystClient().getAzureVirtualWans(**kwargs)

@register('getCgwDetails')
def getCgwDetails(**kwargs):
    return CatalystClient().getCgwDetails(**kwargs)

@register('getCgwAttachedSites')
def getCgwAttachedSites(**kwargs):
    return CatalystClient().getCgwAttachedSites(**kwargs)

@register('getAvailableDevicesOrByCGId')
def getAvailableDevicesOrByCGId(**kwargs):
    return CatalystClient().getAvailableDevicesOrByCGId(**kwargs)

@register('getCloudGateways')
def getCloudGateways(**kwargs):
    return CatalystClient().getCloudGateways(**kwargs)

@register('getCgwCustomSettingDetails')
def getCgwCustomSettingDetails(**kwargs):
    return CatalystClient().getCgwCustomSettingDetails(**kwargs)

@register('getCgwTypes')
def getCgwTypes(**kwargs):
    return CatalystClient().getCgwTypes(**kwargs)

@register('getCloudConnectedSites_1')
def getCloudConnectedSites_1(**kwargs):
    return CatalystClient().getCloudConnectedSites_1(**kwargs)

@register('getCloudConnectedSites')
def getCloudConnectedSites(**kwargs):
    return CatalystClient().getCloudConnectedSites(**kwargs)

@register('getEdgeConnectivityDetails')
def getEdgeConnectivityDetails(**kwargs):
    return CatalystClient().getEdgeConnectivityDetails(**kwargs)

@register('getEdgeConnectivityDetailByName')
def getEdgeConnectivityDetailByName(**kwargs):
    return CatalystClient().getEdgeConnectivityDetailByName(**kwargs)

@register('getConnectivityGateways')
def getConnectivityGateways(**kwargs):
    return CatalystClient().getConnectivityGateways(**kwargs)

@register('getConnectivityGatewayCreationOptions')
def getConnectivityGatewayCreationOptions(**kwargs):
    return CatalystClient().getConnectivityGatewayCreationOptions(**kwargs)

@register('getCwanCoreNetworkPolicy')
def getCwanCoreNetworkPolicy(**kwargs):
    return CatalystClient().getCwanCoreNetworkPolicy(**kwargs)

@register('getDashboardEdgeInfo')
def getDashboardEdgeInfo(**kwargs):
    return CatalystClient().getDashboardEdgeInfo(**kwargs)

@register('getWanDevices')
def getWanDevices(**kwargs):
    return CatalystClient().getWanDevices(**kwargs)

@register('getDeviceLinks')
def getDeviceLinks(**kwargs):
    return CatalystClient().getDeviceLinks(**kwargs)

@register('getDlPortSpeed')
def getDlPortSpeed(**kwargs):
    return CatalystClient().getDlPortSpeed(**kwargs)

@register('getCloudDevices_1')
def getCloudDevices_1(**kwargs):
    return CatalystClient().getCloudDevices_1(**kwargs)

@register('getCloudDevices')
def getCloudDevices(**kwargs):
    return CatalystClient().getCloudDevices(**kwargs)

@register('getEdgeWanDevices')
def getEdgeWanDevices(**kwargs):
    return CatalystClient().getEdgeWanDevices(**kwargs)

@register('getIcgws')
def getIcgws(**kwargs):
    return CatalystClient().getIcgws(**kwargs)

@register('getIcgwCustomSettingDetails')
def getIcgwCustomSettingDetails(**kwargs):
    return CatalystClient().getIcgwCustomSettingDetails(**kwargs)

@register('getIcgwTypes')
def getIcgwTypes(**kwargs):
    return CatalystClient().getIcgwTypes(**kwargs)

@register('getIcgwDetails')
def getIcgwDetails(**kwargs):
    return CatalystClient().getIcgwDetails(**kwargs)

@register('getEdgeGateways')
def getEdgeGateways(**kwargs):
    return CatalystClient().getEdgeGateways(**kwargs)

@register('getHostVpcs')
def getHostVpcs(**kwargs):
    return CatalystClient().getHostVpcs(**kwargs)

@register('getVpcTags')
def getVpcTags(**kwargs):
    return CatalystClient().getVpcTags(**kwargs)

@register('getSupportedEdgeImageNames')
def getSupportedEdgeImageNames(**kwargs):
    return CatalystClient().getSupportedEdgeImageNames(**kwargs)

@register('getSupportedInstanceSize')
def getSupportedInstanceSize(**kwargs):
    return CatalystClient().getSupportedInstanceSize(**kwargs)

@register('getSupportedEdgeInstanceSize')
def getSupportedEdgeInstanceSize(**kwargs):
    return CatalystClient().getSupportedEdgeInstanceSize(**kwargs)

@register('getInterconnectAccounts')
def getInterconnectAccounts(**kwargs):
    return CatalystClient().getInterconnectAccounts(**kwargs)

@register('getInterconnectAccount')
def getInterconnectAccount(**kwargs):
    return CatalystClient().getInterconnectAccount(**kwargs)

@register('getAuditReport')
def getAuditReport(**kwargs):
    return CatalystClient().getAuditReport(**kwargs)

@register('getGoogleCloudRouterAndAttachments')
def getGoogleCloudRouterAndAttachments(**kwargs):
    return CatalystClient().getGoogleCloudRouterAndAttachments(**kwargs)

@register('getAwsTransitGateways')
def getAwsTransitGateways(**kwargs):
    return CatalystClient().getAwsTransitGateways(**kwargs)

@register('getAzVirtualHubs')
def getAzVirtualHubs(**kwargs):
    return CatalystClient().getAzVirtualHubs(**kwargs)

@register('getAzVirtualWans')
def getAzVirtualWans(**kwargs):
    return CatalystClient().getAzVirtualWans(**kwargs)

@register('getCloudConnectivityGateways')
def getCloudConnectivityGateways(**kwargs):
    return CatalystClient().getCloudConnectivityGateways(**kwargs)

@register('getCloudConnectivityGatewayCreateOptions')
def getCloudConnectivityGatewayCreateOptions(**kwargs):
    return CatalystClient().getCloudConnectivityGatewayCreateOptions(**kwargs)

@register('getInterconnectColors')
def getInterconnectColors(**kwargs):
    return CatalystClient().getInterconnectColors(**kwargs)

@register('getInterconnectOnRampGatewayConnections')
def getInterconnectOnRampGatewayConnections(**kwargs):
    return CatalystClient().getInterconnectOnRampGatewayConnections(**kwargs)

@register('getInterconnectOnRampGatewayConnection')
def getInterconnectOnRampGatewayConnection(**kwargs):
    return CatalystClient().getInterconnectOnRampGatewayConnection(**kwargs)

@register('getInterconnectMappingTags')
def getInterconnectMappingTags(**kwargs):
    return CatalystClient().getInterconnectMappingTags(**kwargs)

@register('getInterconnectDeviceLinks')
def getInterconnectDeviceLinks(**kwargs):
    return CatalystClient().getInterconnectDeviceLinks(**kwargs)

@register('getInterconnectDeviceLink')
def getInterconnectDeviceLink(**kwargs):
    return CatalystClient().getInterconnectDeviceLink(**kwargs)

@register('getInterconnectCrossConnections')
def getInterconnectCrossConnections(**kwargs):
    return CatalystClient().getInterconnectCrossConnections(**kwargs)

@register('getInterconnectCrossConnection')
def getInterconnectCrossConnection(**kwargs):
    return CatalystClient().getInterconnectCrossConnection(**kwargs)

@register('getInterconnectVirtualNetworkConnections')
def getInterconnectVirtualNetworkConnections(**kwargs):
    return CatalystClient().getInterconnectVirtualNetworkConnections(**kwargs)

@register('getInterconnectVirtualNetworkConnection')
def getInterconnectVirtualNetworkConnection(**kwargs):
    return CatalystClient().getInterconnectVirtualNetworkConnection(**kwargs)

@register('getInterconnectDashboard')
def getInterconnectDashboard(**kwargs):
    return CatalystClient().getInterconnectDashboard(**kwargs)

@register('getInterconnectLicenses')
def getInterconnectLicenses(**kwargs):
    return CatalystClient().getInterconnectLicenses(**kwargs)

@register('getInterconnectGateways')
def getInterconnectGateways(**kwargs):
    return CatalystClient().getInterconnectGateways(**kwargs)

@register('getInterconnectGatewayImageNames')
def getInterconnectGatewayImageNames(**kwargs):
    return CatalystClient().getInterconnectGatewayImageNames(**kwargs)

@register('getInterconnectGatewayInstanceSizes')
def getInterconnectGatewayInstanceSizes(**kwargs):
    return CatalystClient().getInterconnectGatewayInstanceSizes(**kwargs)

@register('getInterconnetGatewayTypes')
def getInterconnetGatewayTypes(**kwargs):
    return CatalystClient().getInterconnetGatewayTypes(**kwargs)

@register('getInterconnectGateway')
def getInterconnectGateway(**kwargs):
    return CatalystClient().getInterconnectGateway(**kwargs)

@register('getInterconnectGatewayCustomSettings')
def getInterconnectGatewayCustomSettings(**kwargs):
    return CatalystClient().getInterconnectGatewayCustomSettings(**kwargs)

@register('getInterconnectIpTransit')
def getInterconnectIpTransit(**kwargs):
    return CatalystClient().getInterconnectIpTransit(**kwargs)

@register('getInterconnectServiceSwPkg')
def getInterconnectServiceSwPkg(**kwargs):
    return CatalystClient().getInterconnectServiceSwPkg(**kwargs)

@register('getInterconnectServices')
def getInterconnectServices(**kwargs):
    return CatalystClient().getInterconnectServices(**kwargs)

@register('getInterconnectGlobalSettings')
def getInterconnectGlobalSettings(**kwargs):
    return CatalystClient().getInterconnectGlobalSettings(**kwargs)

@register('getInterconnectSshKeys')
def getInterconnectSshKeys(**kwargs):
    return CatalystClient().getInterconnectSshKeys(**kwargs)

@register('getInterconnectTypes')
def getInterconnectTypes(**kwargs):
    return CatalystClient().getInterconnectTypes(**kwargs)

@register('getAllInterconnectWidgets')
def getAllInterconnectWidgets(**kwargs):
    return CatalystClient().getAllInterconnectWidgets(**kwargs)

@register('getInterconnectBillingAccounts')
def getInterconnectBillingAccounts(**kwargs):
    return CatalystClient().getInterconnectBillingAccounts(**kwargs)

@register('getInterconnectPartnerPorts')
def getInterconnectPartnerPorts(**kwargs):
    return CatalystClient().getInterconnectPartnerPorts(**kwargs)

@register('getInterconnectPortSpeeds')
def getInterconnectPortSpeeds(**kwargs):
    return CatalystClient().getInterconnectPortSpeeds(**kwargs)

@register('getInterconnectLocationInfo')
def getInterconnectLocationInfo(**kwargs):
    return CatalystClient().getInterconnectLocationInfo(**kwargs)

@register('getInterconnectConfigGroupTopology')
def getInterconnectConfigGroupTopology(**kwargs):
    return CatalystClient().getInterconnectConfigGroupTopology(**kwargs)

@register('getInterconnectDeviceLinkPortSpeeds')
def getInterconnectDeviceLinkPortSpeeds(**kwargs):
    return CatalystClient().getInterconnectDeviceLinkPortSpeeds(**kwargs)

@register('getAvailableDevicesOrByCGId_1')
def getAvailableDevicesOrByCGId_1(**kwargs):
    return CatalystClient().getAvailableDevicesOrByCGId_1(**kwargs)

@register('getInterconnectGatewayDevices')
def getInterconnectGatewayDevices(**kwargs):
    return CatalystClient().getInterconnectGatewayDevices(**kwargs)

@register('getMonitoringInterconnectConnectedSites')
def getMonitoringInterconnectConnectedSites(**kwargs):
    return CatalystClient().getMonitoringInterconnectConnectedSites(**kwargs)

@register('getMonitoringInterconnectDevices')
def getMonitoringInterconnectDevices(**kwargs):
    return CatalystClient().getMonitoringInterconnectDevices(**kwargs)

@register('getMonitoringInterconnectGateways')
def getMonitoringInterconnectGateways(**kwargs):
    return CatalystClient().getMonitoringInterconnectGateways(**kwargs)

@register('getInterconnectWidget')
def getInterconnectWidget(**kwargs):
    return CatalystClient().getInterconnectWidget(**kwargs)

@register('getWanInterfaceColors')
def getWanInterfaceColors(**kwargs):
    return CatalystClient().getWanInterfaceColors(**kwargs)

@register('getLicenses')
def getLicenses(**kwargs):
    return CatalystClient().getLicenses(**kwargs)

@register('getEdgeLocationsInfo')
def getEdgeLocationsInfo(**kwargs):
    return CatalystClient().getEdgeLocationsInfo(**kwargs)

@register('getSupportedLoopbackCgwColors')
def getSupportedLoopbackCgwColors(**kwargs):
    return CatalystClient().getSupportedLoopbackCgwColors(**kwargs)

@register('getSupportedLoopbackTransportColors')
def getSupportedLoopbackTransportColors(**kwargs):
    return CatalystClient().getSupportedLoopbackTransportColors(**kwargs)

@register('getMappingMatrix')
def getMappingMatrix(**kwargs):
    return CatalystClient().getMappingMatrix(**kwargs)

@register('getDefaultMappingValues')
def getDefaultMappingValues(**kwargs):
    return CatalystClient().getDefaultMappingValues(**kwargs)

@register('getMappingStatus')
def getMappingStatus(**kwargs):
    return CatalystClient().getMappingStatus(**kwargs)

@register('getMappingSummary')
def getMappingSummary(**kwargs):
    return CatalystClient().getMappingSummary(**kwargs)

@register('getMappingTags')
def getMappingTags(**kwargs):
    return CatalystClient().getMappingTags(**kwargs)

@register('getEdgeMappingTags')
def getEdgeMappingTags(**kwargs):
    return CatalystClient().getEdgeMappingTags(**kwargs)

@register('getMappingVpns')
def getMappingVpns(**kwargs):
    return CatalystClient().getMappingVpns(**kwargs)

@register('getCgwAssociatedMappings')
def getCgwAssociatedMappings(**kwargs):
    return CatalystClient().getCgwAssociatedMappings(**kwargs)

@register('getPartnerPorts')
def getPartnerPorts(**kwargs):
    return CatalystClient().getPartnerPorts(**kwargs)

@register('getPortSpeed')
def getPortSpeed(**kwargs):
    return CatalystClient().getPortSpeed(**kwargs)

@register('getCloudRegions')
def getCloudRegions(**kwargs):
    return CatalystClient().getCloudRegions(**kwargs)

@register('getEdgeGlobalSettings')
def getEdgeGlobalSettings(**kwargs):
    return CatalystClient().getEdgeGlobalSettings(**kwargs)

@register('getGlobalSettings')
def getGlobalSettings(**kwargs):
    return CatalystClient().getGlobalSettings(**kwargs)

@register('getSites')
def getSites(**kwargs):
    return CatalystClient().getSites(**kwargs)

@register('getSshKeyList')
def getSshKeyList(**kwargs):
    return CatalystClient().getSshKeyList(**kwargs)

@register('getSupportedSoftwareImageList')
def getSupportedSoftwareImageList(**kwargs):
    return CatalystClient().getSupportedSoftwareImageList(**kwargs)

@register('getTunnelNames')
def getTunnelNames(**kwargs):
    return CatalystClient().getTunnelNames(**kwargs)

@register('getCloudTypes')
def getCloudTypes(**kwargs):
    return CatalystClient().getCloudTypes(**kwargs)

@register('getEdgeTypes')
def getEdgeTypes(**kwargs):
    return CatalystClient().getEdgeTypes(**kwargs)

@register('getVHubs')
def getVHubs(**kwargs):
    return CatalystClient().getVHubs(**kwargs)

@register('getVWans')
def getVWans(**kwargs):
    return CatalystClient().getVWans(**kwargs)

@register('getAllCloudWidgets')
def getAllCloudWidgets(**kwargs):
    return CatalystClient().getAllCloudWidgets(**kwargs)

@register('getAllEdgeWidgets')
def getAllEdgeWidgets(**kwargs):
    return CatalystClient().getAllEdgeWidgets(**kwargs)

@register('getEdgeWidget')
def getEdgeWidget(**kwargs):
    return CatalystClient().getEdgeWidget(**kwargs)

@register('getCloudWidget')
def getCloudWidget(**kwargs):
    return CatalystClient().getCloudWidget(**kwargs)

@register('getMultiCloudConfigGroupTopology')
def getMultiCloudConfigGroupTopology(**kwargs):
    return CatalystClient().getMultiCloudConfigGroupTopology(**kwargs)

@register('getVmanageControlStatus')
def getVmanageControlStatus(**kwargs):
    return CatalystClient().getVmanageControlStatus(**kwargs)

@register('getRebootCount')
def getRebootCount(**kwargs):
    return CatalystClient().getRebootCount(**kwargs)

@register('getNetworkIssuesSummary')
def getNetworkIssuesSummary(**kwargs):
    return CatalystClient().getNetworkIssuesSummary(**kwargs)

@register('getNetworkStatusSummary')
def getNetworkStatusSummary(**kwargs):
    return CatalystClient().getNetworkStatusSummary(**kwargs)

@register('getNetworkDesign')
def getNetworkDesign(**kwargs):
    return CatalystClient().getNetworkDesign(**kwargs)

@register('getCircuits')
def getCircuits(**kwargs):
    return CatalystClient().getCircuits(**kwargs)

@register('getGlobalParameters')
def getGlobalParameters(**kwargs):
    return CatalystClient().getGlobalParameters(**kwargs)

@register('getGlobalTemplate')
def getGlobalTemplate(**kwargs):
    return CatalystClient().getGlobalTemplate(**kwargs)

@register('runMyTest')
def runMyTest(**kwargs):
    return CatalystClient().runMyTest(**kwargs)

@register('getDeviceProfileFeatureTemplateList')
def getDeviceProfileFeatureTemplateList(**kwargs):
    return CatalystClient().getDeviceProfileFeatureTemplateList(**kwargs)

@register('getDeviceProfileConfigStatus')
def getDeviceProfileConfigStatus(**kwargs):
    return CatalystClient().getDeviceProfileConfigStatus(**kwargs)

@register('getDeviceProfileConfigStatusByProfileId')
def getDeviceProfileConfigStatusByProfileId(**kwargs):
    return CatalystClient().getDeviceProfileConfigStatusByProfileId(**kwargs)

@register('getDeviceProfileTaskCount')
def getDeviceProfileTaskCount(**kwargs):
    return CatalystClient().getDeviceProfileTaskCount(**kwargs)

@register('getDeviceProfileTaskStatus')
def getDeviceProfileTaskStatus(**kwargs):
    return CatalystClient().getDeviceProfileTaskStatus(**kwargs)

@register('getDeviceProfileTaskStatusByProfileId')
def getDeviceProfileTaskStatusByProfileId(**kwargs):
    return CatalystClient().getDeviceProfileTaskStatusByProfileId(**kwargs)

@register('generateProfileTemplateList')
def generateProfileTemplateList(**kwargs):
    return CatalystClient().generateProfileTemplateList(**kwargs)

@register('getDeviceProfileTemplate')
def getDeviceProfileTemplate(**kwargs):
    return CatalystClient().getDeviceProfileTemplate(**kwargs)

@register('getServiceProfileConfig')
def getServiceProfileConfig(**kwargs):
    return CatalystClient().getServiceProfileConfig(**kwargs)

@register('getNotificationRule')
def getNotificationRule(**kwargs):
    return CatalystClient().getNotificationRule(**kwargs)

@register('getDevices')
def getDevices(**kwargs):
    return CatalystClient().getDevices(**kwargs)

@register('oauthAccess')
def oauthAccess(**kwargs):
    return CatalystClient().oauthAccess(**kwargs)

@register('getClientID')
def getClientID(**kwargs):
    return CatalystClient().getClientID(**kwargs)

@register('getCall')
def getCall(**kwargs):
    return CatalystClient().getCall(**kwargs)

@register('getPartners')
def getPartners(**kwargs):
    return CatalystClient().getPartners(**kwargs)

@register('getACIDefinitions')
def getACIDefinitions(**kwargs):
    return CatalystClient().getACIDefinitions(**kwargs)

@register('getDscpMappings')
def getDscpMappings(**kwargs):
    return CatalystClient().getDscpMappings(**kwargs)

@register('getEvents_1')
def getEvents_1(**kwargs):
    return CatalystClient().getEvents_1(**kwargs)

@register('getDataPrefixMappings')
def getDataPrefixMappings(**kwargs):
    return CatalystClient().getDataPrefixMappings(**kwargs)

@register('getDataPrefixSequences')
def getDataPrefixSequences(**kwargs):
    return CatalystClient().getDataPrefixSequences(**kwargs)

@register('getSDAEnabledDevices')
def getSDAEnabledDevices(**kwargs):
    return CatalystClient().getSDAEnabledDevices(**kwargs)

@register('getDeviceDetails')
def getDeviceDetails(**kwargs):
    return CatalystClient().getDeviceDetails(**kwargs)

@register('getSitesForPartner')
def getSitesForPartner(**kwargs):
    return CatalystClient().getSitesForPartner(**kwargs)

@register('getOverlayVPNList')
def getOverlayVPNList(**kwargs):
    return CatalystClient().getOverlayVPNList(**kwargs)

@register('getVPNList')
def getVPNList(**kwargs):
    return CatalystClient().getVPNList(**kwargs)

@register('getPartnersByPartnerType')
def getPartnersByPartnerType(**kwargs):
    return CatalystClient().getPartnersByPartnerType(**kwargs)

@register('getPartnerDevices')
def getPartnerDevices(**kwargs):
    return CatalystClient().getPartnerDevices(**kwargs)

@register('getPartner')
def getPartner(**kwargs):
    return CatalystClient().getPartner(**kwargs)

@register('getSecureXRefreshToken')
def getSecureXRefreshToken(**kwargs):
    return CatalystClient().getSecureXRefreshToken(**kwargs)

@register('getResources')
def getResources(**kwargs):
    return CatalystClient().getResources(**kwargs)

@register('listSchedules')
def listSchedules(**kwargs):
    return CatalystClient().listSchedules(**kwargs)

@register('getScheduleRecordForBackup')
def getScheduleRecordForBackup(**kwargs):
    return CatalystClient().getScheduleRecordForBackup(**kwargs)

@register('getExtendedApplications')
def getExtendedApplications(**kwargs):
    return CatalystClient().getExtendedApplications(**kwargs)

@register('getCloudConnector')
def getCloudConnector(**kwargs):
    return CatalystClient().getCloudConnector(**kwargs)

@register('getCloudConnectorStatus')
def getCloudConnectorStatus(**kwargs):
    return CatalystClient().getCloudConnectorStatus(**kwargs)

@register('getCustomApp')
def getCustomApp(**kwargs):
    return CatalystClient().getCustomApp(**kwargs)

@register('getAllProtocolPacks')
def getAllProtocolPacks(**kwargs):
    return CatalystClient().getAllProtocolPacks(**kwargs)

@register('getBaseSystemPack')
def getBaseSystemPack(**kwargs):
    return CatalystClient().getBaseSystemPack(**kwargs)

@register('getAllSDAVCDevice')
def getAllSDAVCDevice(**kwargs):
    return CatalystClient().getAllSDAVCDevice(**kwargs)

@register('getDefaultApplicationComplianceDetails')
def getDefaultApplicationComplianceDetails(**kwargs):
    return CatalystClient().getDefaultApplicationComplianceDetails(**kwargs)

@register('isApplicationComplianceDetected')
def isApplicationComplianceDetected(**kwargs):
    return CatalystClient().isApplicationComplianceDetected(**kwargs)

@register('getApplicationComplianceStatus')
def getApplicationComplianceStatus(**kwargs):
    return CatalystClient().getApplicationComplianceStatus(**kwargs)

@register('getApplicationComplianceDetails')
def getApplicationComplianceDetails(**kwargs):
    return CatalystClient().getApplicationComplianceDetails(**kwargs)

@register('getCustomApplicationList')
def getCustomApplicationList(**kwargs):
    return CatalystClient().getCustomApplicationList(**kwargs)

@register('getNonCompliantDevicesForProtocolPack')
def getNonCompliantDevicesForProtocolPack(**kwargs):
    return CatalystClient().getNonCompliantDevicesForProtocolPack(**kwargs)

@register('getDeviceComplianceStatus')
def getDeviceComplianceStatus(**kwargs):
    return CatalystClient().getDeviceComplianceStatus(**kwargs)

@register('getNewApplicationList')
def getNewApplicationList(**kwargs):
    return CatalystClient().getNewApplicationList(**kwargs)

@register('getCompliancePolicy')
def getCompliancePolicy(**kwargs):
    return CatalystClient().getCompliancePolicy(**kwargs)

@register('getPolicyComplianceStatus')
def getPolicyComplianceStatus(**kwargs):
    return CatalystClient().getPolicyComplianceStatus(**kwargs)

@register('getDefaultSystemPack')
def getDefaultSystemPack(**kwargs):
    return CatalystClient().getDefaultSystemPack(**kwargs)

@register('getLatestSystemPack')
def getLatestSystemPack(**kwargs):
    return CatalystClient().getLatestSystemPack(**kwargs)

@register('getDeployJobStatus')
def getDeployJobStatus(**kwargs):
    return CatalystClient().getDeployJobStatus(**kwargs)

@register('getDeployJobStatus_1')
def getDeployJobStatus_1(**kwargs):
    return CatalystClient().getDeployJobStatus_1(**kwargs)

@register('getProtocolPackUploadStatus')
def getProtocolPackUploadStatus(**kwargs):
    return CatalystClient().getProtocolPackUploadStatus(**kwargs)

@register('getSecurityDeviceHealth')
def getSecurityDeviceHealth(**kwargs):
    return CatalystClient().getSecurityDeviceHealth(**kwargs)

@register('getSecurityPolicyDeviceList')
def getSecurityPolicyDeviceList(**kwargs):
    return CatalystClient().getSecurityPolicyDeviceList(**kwargs)

@register('getSegments')
def getSegments(**kwargs):
    return CatalystClient().getSegments(**kwargs)

@register('getSegment')
def getSegment(**kwargs):
    return CatalystClient().getSegment(**kwargs)

@register('createServerInfo_1')
def createServerInfo_1(**kwargs):
    return CatalystClient().createServerInfo_1(**kwargs)

@register('getDataChangeInfo')
def getDataChangeInfo(**kwargs):
    return CatalystClient().getDataChangeInfo(**kwargs)

@register('showInfo')
def showInfo(**kwargs):
    return CatalystClient().showInfo(**kwargs)

@register('getCertificate')
def getCertificate(**kwargs):
    return CatalystClient().getCertificate(**kwargs)

@register('getBanner')
def getBanner(**kwargs):
    return CatalystClient().getBanner(**kwargs)

@register('getSessionTimout')
def getSessionTimout(**kwargs):
    return CatalystClient().getSessionTimout(**kwargs)

@register('getCertConfiguration')
def getCertConfiguration(**kwargs):
    return CatalystClient().getCertConfiguration(**kwargs)

@register('getCloudxConfiguration')
def getCloudxConfiguration(**kwargs):
    return CatalystClient().getCloudxConfiguration(**kwargs)

@register('getGoogleMapKey')
def getGoogleMapKey(**kwargs):
    return CatalystClient().getGoogleMapKey(**kwargs)

@register('getMaintenanceWindow')
def getMaintenanceWindow(**kwargs):
    return CatalystClient().getMaintenanceWindow(**kwargs)

@register('getMicrosoftTelemetryConfiguration')
def getMicrosoftTelemetryConfiguration(**kwargs):
    return CatalystClient().getMicrosoftTelemetryConfiguration(**kwargs)

@register('getWaniConfiguration')
def getWaniConfiguration(**kwargs):
    return CatalystClient().getWaniConfiguration(**kwargs)

@register('getConfigurationBySettingType')
def getConfigurationBySettingType(**kwargs):
    return CatalystClient().getConfigurationBySettingType(**kwargs)

@register('getPasswordPolicy')
def getPasswordPolicy(**kwargs):
    return CatalystClient().getPasswordPolicy(**kwargs)

@register('getSigDynamicDataCenterList')
def getSigDynamicDataCenterList(**kwargs):
    return CatalystClient().getSigDynamicDataCenterList(**kwargs)

@register('getSigDataCenterList')
def getSigDataCenterList(**kwargs):
    return CatalystClient().getSigDataCenterList(**kwargs)

@register('getSigGlobalCredentials')
def getSigGlobalCredentials(**kwargs):
    return CatalystClient().getSigGlobalCredentials(**kwargs)

@register('getChildOrgs')
def getChildOrgs(**kwargs):
    return CatalystClient().getChildOrgs(**kwargs)

@register('fetchAccounts')
def fetchAccounts(**kwargs):
    return CatalystClient().fetchAccounts(**kwargs)

@register('fetchReports_1')
def fetchReports_1(**kwargs):
    return CatalystClient().fetchReports_1(**kwargs)

@register('fetchReports')
def fetchReports(**kwargs):
    return CatalystClient().fetchReports(**kwargs)

@register('getSettings')
def getSettings(**kwargs):
    return CatalystClient().getSettings(**kwargs)

@register('getProxyCertOfEdge')
def getProxyCertOfEdge(**kwargs):
    return CatalystClient().getProxyCertOfEdge(**kwargs)

@register('getSslProxyCSR')
def getSslProxyCSR(**kwargs):
    return CatalystClient().getSslProxyCSR(**kwargs)

@register('getSslProxyList')
def getSslProxyList(**kwargs):
    return CatalystClient().getSslProxyList(**kwargs)

@register('getCertificateState')
def getCertificateState(**kwargs):
    return CatalystClient().getCertificateState(**kwargs)

@register('getEnterpriseCertificate')
def getEnterpriseCertificate(**kwargs):
    return CatalystClient().getEnterpriseCertificate(**kwargs)

@register('getVManageEnterpriseRootCertificate')
def getVManageEnterpriseRootCertificate(**kwargs):
    return CatalystClient().getVManageEnterpriseRootCertificate(**kwargs)

@register('getvManageCertificate')
def getvManageCertificate(**kwargs):
    return CatalystClient().getvManageCertificate(**kwargs)

@register('getvManageCSR')
def getvManageCSR(**kwargs):
    return CatalystClient().getvManageCSR(**kwargs)

@register('getvManageRootCA')
def getvManageRootCA(**kwargs):
    return CatalystClient().getvManageRootCA(**kwargs)

@register('getStatisticType')
def getStatisticType(**kwargs):
    return CatalystClient().getStatisticType(**kwargs)

@register('getAggregationDataByQuery_14')
def getAggregationDataByQuery_14(**kwargs):
    return CatalystClient().getAggregationDataByQuery_14(**kwargs)

@register('getAggregationDataByQuery_1')
def getAggregationDataByQuery_1(**kwargs):
    return CatalystClient().getAggregationDataByQuery_1(**kwargs)

@register('getStatDataRawDataAsCSV_1')
def getStatDataRawDataAsCSV_1(**kwargs):
    return CatalystClient().getStatDataRawDataAsCSV_1(**kwargs)

@register('getCount_2')
def getCount_2(**kwargs):
    return CatalystClient().getCount_2(**kwargs)

@register('getStatDataFields_2')
def getStatDataFields_2(**kwargs):
    return CatalystClient().getStatDataFields_2(**kwargs)

@register('getStatsPaginationRawData_1')
def getStatsPaginationRawData_1(**kwargs):
    return CatalystClient().getStatsPaginationRawData_1(**kwargs)

@register('getStatQueryFields_2')
def getStatQueryFields_2(**kwargs):
    return CatalystClient().getStatQueryFields_2(**kwargs)

@register('getAggregationDataByQuery')
def getAggregationDataByQuery(**kwargs):
    return CatalystClient().getAggregationDataByQuery(**kwargs)

@register('getStatDataRawDataAsCSV')
def getStatDataRawDataAsCSV(**kwargs):
    return CatalystClient().getStatDataRawDataAsCSV(**kwargs)

@register('getCount_1')
def getCount_1(**kwargs):
    return CatalystClient().getCount_1(**kwargs)

@register('getStatDataFields_1')
def getStatDataFields_1(**kwargs):
    return CatalystClient().getStatDataFields_1(**kwargs)

@register('getStatsPaginationRawData')
def getStatsPaginationRawData(**kwargs):
    return CatalystClient().getStatsPaginationRawData(**kwargs)

@register('getStatQueryFields_1')
def getStatQueryFields_1(**kwargs):
    return CatalystClient().getStatQueryFields_1(**kwargs)

@register('getAggregationDataByQuery_2')
def getAggregationDataByQuery_2(**kwargs):
    return CatalystClient().getAggregationDataByQuery_2(**kwargs)

@register('getStatDataRawDataAsCSV_2')
def getStatDataRawDataAsCSV_2(**kwargs):
    return CatalystClient().getStatDataRawDataAsCSV_2(**kwargs)

@register('getStatsAppRouteDeviceTunnelSummary')
def getStatsAppRouteDeviceTunnelSummary(**kwargs):
    return CatalystClient().getStatsAppRouteDeviceTunnelSummary(**kwargs)

@register('getStatsAppRouteDeviceTunnels')
def getStatsAppRouteDeviceTunnels(**kwargs):
    return CatalystClient().getStatsAppRouteDeviceTunnels(**kwargs)

@register('getDocCount_1')
def getDocCount_1(**kwargs):
    return CatalystClient().getDocCount_1(**kwargs)

@register('getStatDataFields_3')
def getStatDataFields_3(**kwargs):
    return CatalystClient().getStatDataFields_3(**kwargs)

@register('getStatBulkRawData')
def getStatBulkRawData(**kwargs):
    return CatalystClient().getStatBulkRawData(**kwargs)

@register('getStatQueryFields_3')
def getStatQueryFields_3(**kwargs):
    return CatalystClient().getStatQueryFields_3(**kwargs)

@register('getAppRouteTransportSummaryType')
def getAppRouteTransportSummaryType(**kwargs):
    return CatalystClient().getAppRouteTransportSummaryType(**kwargs)

@register('getAppRouteTransportType')
def getAppRouteTransportType(**kwargs):
    return CatalystClient().getAppRouteTransportType(**kwargs)

@register('getAppRouteTunnelSummaryType')
def getAppRouteTunnelSummaryType(**kwargs):
    return CatalystClient().getAppRouteTunnelSummaryType(**kwargs)

@register('getAppRouteTunnelHealth')
def getAppRouteTunnelHealth(**kwargs):
    return CatalystClient().getAppRouteTunnelHealth(**kwargs)

@register('getAppRouteTunnelsSummaryType')
def getAppRouteTunnelsSummaryType(**kwargs):
    return CatalystClient().getAppRouteTunnelsSummaryType(**kwargs)

@register('getAppRouteTunnelType')
def getAppRouteTunnelType(**kwargs):
    return CatalystClient().getAppRouteTunnelType(**kwargs)

@register('getAggregationDataByQuery_4')
def getAggregationDataByQuery_4(**kwargs):
    return CatalystClient().getAggregationDataByQuery_4(**kwargs)

@register('getStatDataRawDataAsCSV_4')
def getStatDataRawDataAsCSV_4(**kwargs):
    return CatalystClient().getStatDataRawDataAsCSV_4(**kwargs)

@register('getCount_4')
def getCount_4(**kwargs):
    return CatalystClient().getCount_4(**kwargs)

@register('getStatDataFields_5')
def getStatDataFields_5(**kwargs):
    return CatalystClient().getStatDataFields_5(**kwargs)

@register('getStatsPaginationRawData_3')
def getStatsPaginationRawData_3(**kwargs):
    return CatalystClient().getStatsPaginationRawData_3(**kwargs)

@register('getStatQueryFields_5')
def getStatQueryFields_5(**kwargs):
    return CatalystClient().getStatQueryFields_5(**kwargs)

@register('getAggregationDataByQuery_5')
def getAggregationDataByQuery_5(**kwargs):
    return CatalystClient().getAggregationDataByQuery_5(**kwargs)

@register('getStatDataRawDataAsCSV_5')
def getStatDataRawDataAsCSV_5(**kwargs):
    return CatalystClient().getStatDataRawDataAsCSV_5(**kwargs)

@register('getCount_5')
def getCount_5(**kwargs):
    return CatalystClient().getCount_5(**kwargs)

@register('getStatDataFields_6')
def getStatDataFields_6(**kwargs):
    return CatalystClient().getStatDataFields_6(**kwargs)

@register('getStatsPaginationRawData_4')
def getStatsPaginationRawData_4(**kwargs):
    return CatalystClient().getStatsPaginationRawData_4(**kwargs)

@register('getStatQueryFields_6')
def getStatQueryFields_6(**kwargs):
    return CatalystClient().getStatQueryFields_6(**kwargs)

@register('getAggregationDataByQuery_6')
def getAggregationDataByQuery_6(**kwargs):
    return CatalystClient().getAggregationDataByQuery_6(**kwargs)

@register('getStatDataRawDataAsCSV_6')
def getStatDataRawDataAsCSV_6(**kwargs):
    return CatalystClient().getStatDataRawDataAsCSV_6(**kwargs)

@register('getCount_6')
def getCount_6(**kwargs):
    return CatalystClient().getCount_6(**kwargs)

@register('getStatDataFields_7')
def getStatDataFields_7(**kwargs):
    return CatalystClient().getStatDataFields_7(**kwargs)

@register('getStatsPaginationRawData_5')
def getStatsPaginationRawData_5(**kwargs):
    return CatalystClient().getStatsPaginationRawData_5(**kwargs)

@register('getStatQueryFields_7')
def getStatQueryFields_7(**kwargs):
    return CatalystClient().getStatQueryFields_7(**kwargs)

@register('getAggregationDataByQuery_7')
def getAggregationDataByQuery_7(**kwargs):
    return CatalystClient().getAggregationDataByQuery_7(**kwargs)

@register('getStatDataRawDataAsCSV_7')
def getStatDataRawDataAsCSV_7(**kwargs):
    return CatalystClient().getStatDataRawDataAsCSV_7(**kwargs)

@register('getCount_7')
def getCount_7(**kwargs):
    return CatalystClient().getCount_7(**kwargs)

@register('getStatDataFields_8')
def getStatDataFields_8(**kwargs):
    return CatalystClient().getStatDataFields_8(**kwargs)

@register('getStatsPaginationRawData_6')
def getStatsPaginationRawData_6(**kwargs):
    return CatalystClient().getStatsPaginationRawData_6(**kwargs)

@register('getStatQueryFields_8')
def getStatQueryFields_8(**kwargs):
    return CatalystClient().getStatQueryFields_8(**kwargs)

@register('getAggregationDataByQuery_9')
def getAggregationDataByQuery_9(**kwargs):
    return CatalystClient().getAggregationDataByQuery_9(**kwargs)

@register('createFlowsGrid')
def createFlowsGrid(**kwargs):
    return CatalystClient().createFlowsGrid(**kwargs)

@register('createFlowssummary')
def createFlowssummary(**kwargs):
    return CatalystClient().createFlowssummary(**kwargs)

@register('getStatDataRawDataAsCSV_9')
def getStatDataRawDataAsCSV_9(**kwargs):
    return CatalystClient().getStatDataRawDataAsCSV_9(**kwargs)

@register('createFlowDeviceData')
def createFlowDeviceData(**kwargs):
    return CatalystClient().createFlowDeviceData(**kwargs)

@register('getCount_9')
def getCount_9(**kwargs):
    return CatalystClient().getCount_9(**kwargs)

@register('getStatDataFields_10')
def getStatDataFields_10(**kwargs):
    return CatalystClient().getStatDataFields_10(**kwargs)

@register('getStatsPaginationRawData_8')
def getStatsPaginationRawData_8(**kwargs):
    return CatalystClient().getStatsPaginationRawData_8(**kwargs)

@register('getStatQueryFields_10')
def getStatQueryFields_10(**kwargs):
    return CatalystClient().getStatQueryFields_10(**kwargs)

@register('getAggregationDataByQuery_10')
def getAggregationDataByQuery_10(**kwargs):
    return CatalystClient().getAggregationDataByQuery_10(**kwargs)

@register('getStatDataRawDataAsCSV_10')
def getStatDataRawDataAsCSV_10(**kwargs):
    return CatalystClient().getStatDataRawDataAsCSV_10(**kwargs)

@register('getCount_10')
def getCount_10(**kwargs):
    return CatalystClient().getCount_10(**kwargs)

@register('getStatDataFields_11')
def getStatDataFields_11(**kwargs):
    return CatalystClient().getStatDataFields_11(**kwargs)

@register('getStatsPaginationRawData_9')
def getStatsPaginationRawData_9(**kwargs):
    return CatalystClient().getStatsPaginationRawData_9(**kwargs)

@register('getStatQueryFields_11')
def getStatQueryFields_11(**kwargs):
    return CatalystClient().getStatQueryFields_11(**kwargs)

@register('startStatsCollection')
def startStatsCollection(**kwargs):
    return CatalystClient().startStatsCollection(**kwargs)

@register('generateStatsCollectThreadReport')
def generateStatsCollectThreadReport(**kwargs):
    return CatalystClient().generateStatsCollectThreadReport(**kwargs)

@register('resetStatsCollection')
def resetStatsCollection(**kwargs):
    return CatalystClient().resetStatsCollection(**kwargs)

@register('getStatDataRawDataAsCSV_13')
def getStatDataRawDataAsCSV_13(**kwargs):
    return CatalystClient().getStatDataRawDataAsCSV_13(**kwargs)

@register('enableStatisticsDemoMode')
def enableStatisticsDemoMode(**kwargs):
    return CatalystClient().enableStatisticsDemoMode(**kwargs)

@register('getAggregationDataByQuery_18')
def getAggregationDataByQuery_18(**kwargs):
    return CatalystClient().getAggregationDataByQuery_18(**kwargs)

@register('getStatDataRawDataAsCSV_16')
def getStatDataRawDataAsCSV_16(**kwargs):
    return CatalystClient().getStatDataRawDataAsCSV_16(**kwargs)

@register('getCount_15')
def getCount_15(**kwargs):
    return CatalystClient().getCount_15(**kwargs)

@register('getStatDataFields_17')
def getStatDataFields_17(**kwargs):
    return CatalystClient().getStatDataFields_17(**kwargs)

@register('getStatsPaginationRawData_14')
def getStatsPaginationRawData_14(**kwargs):
    return CatalystClient().getStatsPaginationRawData_14(**kwargs)

@register('getStatQueryFields_18')
def getStatQueryFields_18(**kwargs):
    return CatalystClient().getStatQueryFields_18(**kwargs)

@register('getDeviceHealthHistory')
def getDeviceHealthHistory(**kwargs):
    return CatalystClient().getDeviceHealthHistory(**kwargs)

@register('getDeviceHealthOverview')
def getDeviceHealthOverview(**kwargs):
    return CatalystClient().getDeviceHealthOverview(**kwargs)

@register('getCount_12')
def getCount_12(**kwargs):
    return CatalystClient().getCount_12(**kwargs)

@register('fetchList')
def fetchList(**kwargs):
    return CatalystClient().fetchList(**kwargs)

@register('download')
def download(**kwargs):
    return CatalystClient().download(**kwargs)

@register('getDPIStatsAggregationData')
def getDPIStatsAggregationData(**kwargs):
    return CatalystClient().getDPIStatsAggregationData(**kwargs)

@register('getAggAppFlows')
def getAggAppFlows(**kwargs):
    return CatalystClient().getAggAppFlows(**kwargs)

@register('getAggAppFlowsSummary')
def getAggAppFlowsSummary(**kwargs):
    return CatalystClient().getAggAppFlowsSummary(**kwargs)

@register('getDPIStatsRawDataAsCSV')
def getDPIStatsRawDataAsCSV(**kwargs):
    return CatalystClient().getDPIStatsRawDataAsCSV(**kwargs)

@register('getDPIDeviceAppUniqueFlowCount')
def getDPIDeviceAppUniqueFlowCount(**kwargs):
    return CatalystClient().getDPIDeviceAppUniqueFlowCount(**kwargs)

@register('getDPIDeviceAppAggregationData')
def getDPIDeviceAppAggregationData(**kwargs):
    return CatalystClient().getDPIDeviceAppAggregationData(**kwargs)

@register('getDPIDeviceAppDetails')
def getDPIDeviceAppDetails(**kwargs):
    return CatalystClient().getDPIDeviceAppDetails(**kwargs)

@register('getDPIStatsCount')
def getDPIStatsCount(**kwargs):
    return CatalystClient().getDPIStatsCount(**kwargs)

@register('getDPIFields')
def getDPIFields(**kwargs):
    return CatalystClient().getDPIFields(**kwargs)

@register('getDPIStatsPaginationRawData')
def getDPIStatsPaginationRawData(**kwargs):
    return CatalystClient().getDPIStatsPaginationRawData(**kwargs)

@register('getDPIQueryFields')
def getDPIQueryFields(**kwargs):
    return CatalystClient().getDPIQueryFields(**kwargs)

@register('getAggregationDataByQuery_8')
def getAggregationDataByQuery_8(**kwargs):
    return CatalystClient().getAggregationDataByQuery_8(**kwargs)

@register('getStatDataRawDataAsCSV_8')
def getStatDataRawDataAsCSV_8(**kwargs):
    return CatalystClient().getStatDataRawDataAsCSV_8(**kwargs)

@register('getCount_8')
def getCount_8(**kwargs):
    return CatalystClient().getCount_8(**kwargs)

@register('getStatDataFields_9')
def getStatDataFields_9(**kwargs):
    return CatalystClient().getStatDataFields_9(**kwargs)

@register('getStatsPaginationRawData_7')
def getStatsPaginationRawData_7(**kwargs):
    return CatalystClient().getStatsPaginationRawData_7(**kwargs)

@register('getStatQueryFields_9')
def getStatQueryFields_9(**kwargs):
    return CatalystClient().getStatQueryFields_9(**kwargs)

@register('getAggregationDataByQuery_21')
def getAggregationDataByQuery_21(**kwargs):
    return CatalystClient().getAggregationDataByQuery_21(**kwargs)

@register('getStatDataRawDataAsCSV_19')
def getStatDataRawDataAsCSV_19(**kwargs):
    return CatalystClient().getStatDataRawDataAsCSV_19(**kwargs)

@register('getCount_18')
def getCount_18(**kwargs):
    return CatalystClient().getCount_18(**kwargs)

@register('getStatDataFields_20')
def getStatDataFields_20(**kwargs):
    return CatalystClient().getStatDataFields_20(**kwargs)

@register('getStatsPaginationRawData_17')
def getStatsPaginationRawData_17(**kwargs):
    return CatalystClient().getStatsPaginationRawData_17(**kwargs)

@register('getStatQueryFields_21')
def getStatQueryFields_21(**kwargs):
    return CatalystClient().getStatQueryFields_21(**kwargs)

@register('getStatDataFields_14')
def getStatDataFields_14(**kwargs):
    return CatalystClient().getStatDataFields_14(**kwargs)

@register('getAggregationDataByQuery_28')
def getAggregationDataByQuery_28(**kwargs):
    return CatalystClient().getAggregationDataByQuery_28(**kwargs)

@register('getStatDataRawDataAsCSV_26')
def getStatDataRawDataAsCSV_26(**kwargs):
    return CatalystClient().getStatDataRawDataAsCSV_26(**kwargs)

@register('getFlowlogCount')
def getFlowlogCount(**kwargs):
    return CatalystClient().getFlowlogCount(**kwargs)

@register('getFlowlogFields')
def getFlowlogFields(**kwargs):
    return CatalystClient().getFlowlogFields(**kwargs)

@register('getStatsPaginationRawData_24')
def getStatsPaginationRawData_24(**kwargs):
    return CatalystClient().getStatsPaginationRawData_24(**kwargs)

@register('getFlowlogQueryFields')
def getFlowlogQueryFields(**kwargs):
    return CatalystClient().getFlowlogQueryFields(**kwargs)

@register('getAggregationDataByQuery_26')
def getAggregationDataByQuery_26(**kwargs):
    return CatalystClient().getAggregationDataByQuery_26(**kwargs)

@register('getStatDataRawDataAsCSV_24')
def getStatDataRawDataAsCSV_24(**kwargs):
    return CatalystClient().getStatDataRawDataAsCSV_24(**kwargs)

@register('getCount_23')
def getCount_23(**kwargs):
    return CatalystClient().getCount_23(**kwargs)

@register('getStatDataFields_25')
def getStatDataFields_25(**kwargs):
    return CatalystClient().getStatDataFields_25(**kwargs)

@register('getStatsPaginationRawData_22')
def getStatsPaginationRawData_22(**kwargs):
    return CatalystClient().getStatsPaginationRawData_22(**kwargs)

@register('getStatQueryFields_26')
def getStatQueryFields_26(**kwargs):
    return CatalystClient().getStatQueryFields_26(**kwargs)

@register('getAggregationDataByQuery_11')
def getAggregationDataByQuery_11(**kwargs):
    return CatalystClient().getAggregationDataByQuery_11(**kwargs)

@register('getBandwidthDistribution')
def getBandwidthDistribution(**kwargs):
    return CatalystClient().getBandwidthDistribution(**kwargs)

@register('getStatDataRawDataAsCSV_11')
def getStatDataRawDataAsCSV_11(**kwargs):
    return CatalystClient().getStatDataRawDataAsCSV_11(**kwargs)

@register('getCount10')
def getCount10(**kwargs):
    return CatalystClient().getCount10(**kwargs)

@register('getStatDataFields_12')
def getStatDataFields_12(**kwargs):
    return CatalystClient().getStatDataFields_12(**kwargs)

@register('getStatBulkRawData_1')
def getStatBulkRawData_1(**kwargs):
    return CatalystClient().getStatBulkRawData_1(**kwargs)

@register('getStatQueryFields_12')
def getStatQueryFields_12(**kwargs):
    return CatalystClient().getStatQueryFields_12(**kwargs)

@register('getStatisticsPerInterface')
def getStatisticsPerInterface(**kwargs):
    return CatalystClient().getStatisticsPerInterface(**kwargs)

@register('getAggregationDataByQuery_24')
def getAggregationDataByQuery_24(**kwargs):
    return CatalystClient().getAggregationDataByQuery_24(**kwargs)

@register('getStatDataRawDataAsCSV_22')
def getStatDataRawDataAsCSV_22(**kwargs):
    return CatalystClient().getStatDataRawDataAsCSV_22(**kwargs)

@register('getCount_21')
def getCount_21(**kwargs):
    return CatalystClient().getCount_21(**kwargs)

@register('getStatDataFields_23')
def getStatDataFields_23(**kwargs):
    return CatalystClient().getStatDataFields_23(**kwargs)

@register('getStatsPaginationRawData_20')
def getStatsPaginationRawData_20(**kwargs):
    return CatalystClient().getStatsPaginationRawData_20(**kwargs)

@register('getStatQueryFields_24')
def getStatQueryFields_24(**kwargs):
    return CatalystClient().getStatQueryFields_24(**kwargs)

@register('getQueueEntries')
def getQueueEntries(**kwargs):
    return CatalystClient().getQueueEntries(**kwargs)

@register('getQueueProperties')
def getQueueProperties(**kwargs):
    return CatalystClient().getQueueProperties(**kwargs)

@register('getStatsPaginationRawData_11')
def getStatsPaginationRawData_11(**kwargs):
    return CatalystClient().getStatsPaginationRawData_11(**kwargs)

@register('getApplicationHeatMapDetail')
def getApplicationHeatMapDetail(**kwargs):
    return CatalystClient().getApplicationHeatMapDetail(**kwargs)

@register('getApplicationSitesHealth')
def getApplicationSitesHealth(**kwargs):
    return CatalystClient().getApplicationSitesHealth(**kwargs)

@register('getApplicationsSiteHealth')
def getApplicationsSiteHealth(**kwargs):
    return CatalystClient().getApplicationsSiteHealth(**kwargs)

@register('getApplicationsSitesHealth')
def getApplicationsSitesHealth(**kwargs):
    return CatalystClient().getApplicationsSitesHealth(**kwargs)

@register('getSupportedDeviceList')
def getSupportedDeviceList(**kwargs):
    return CatalystClient().getSupportedDeviceList(**kwargs)

@register('processStatisticsData')
def processStatisticsData(**kwargs):
    return CatalystClient().processStatisticsData(**kwargs)

@register('getStatisticsProcessingCounters')
def getStatisticsProcessingCounters(**kwargs):
    return CatalystClient().getStatisticsProcessingCounters(**kwargs)

@register('generateStatsProcessReport')
def generateStatsProcessReport(**kwargs):
    return CatalystClient().generateStatsProcessReport(**kwargs)

@register('generateStatsProcessThreadReport')
def generateStatsProcessThreadReport(**kwargs):
    return CatalystClient().generateStatsProcessThreadReport(**kwargs)

@register('getAggregationDataByQuery_15')
def getAggregationDataByQuery_15(**kwargs):
    return CatalystClient().getAggregationDataByQuery_15(**kwargs)

@register('getStatDataRawDataAsCSV_3')
def getStatDataRawDataAsCSV_3(**kwargs):
    return CatalystClient().getStatDataRawDataAsCSV_3(**kwargs)

@register('getCount_3')
def getCount_3(**kwargs):
    return CatalystClient().getCount_3(**kwargs)

@register('getStatDataFields_4')
def getStatDataFields_4(**kwargs):
    return CatalystClient().getStatDataFields_4(**kwargs)

@register('getStatsPaginationRawData_2')
def getStatsPaginationRawData_2(**kwargs):
    return CatalystClient().getStatsPaginationRawData_2(**kwargs)

@register('getStatQueryFields_4')
def getStatQueryFields_4(**kwargs):
    return CatalystClient().getStatQueryFields_4(**kwargs)

@register('getAggregationDataByQuery_13')
def getAggregationDataByQuery_13(**kwargs):
    return CatalystClient().getAggregationDataByQuery_13(**kwargs)

@register('getStatDataRawDataAsCSV12')
def getStatDataRawDataAsCSV12(**kwargs):
    return CatalystClient().getStatDataRawDataAsCSV12(**kwargs)

@register('getCount13')
def getCount13(**kwargs):
    return CatalystClient().getCount13(**kwargs)

@register('getStatDataFields13')
def getStatDataFields13(**kwargs):
    return CatalystClient().getStatDataFields13(**kwargs)

@register('getStatBulkRawData_2')
def getStatBulkRawData_2(**kwargs):
    return CatalystClient().getStatBulkRawData_2(**kwargs)

@register('getStatQueryFields_14')
def getStatQueryFields_14(**kwargs):
    return CatalystClient().getStatQueryFields_14(**kwargs)

@register('getStatQueryFields_15')
def getStatQueryFields_15(**kwargs):
    return CatalystClient().getStatQueryFields_15(**kwargs)

@register('getSdraHeadendSummary')
def getSdraHeadendSummary(**kwargs):
    return CatalystClient().getSdraHeadendSummary(**kwargs)

@register('getSdraSessionSummary')
def getSdraSessionSummary(**kwargs):
    return CatalystClient().getSdraSessionSummary(**kwargs)

@register('getDisabledDeviceList')
def getDisabledDeviceList(**kwargs):
    return CatalystClient().getDisabledDeviceList(**kwargs)

@register('getStatisticsSettings')
def getStatisticsSettings(**kwargs):
    return CatalystClient().getStatisticsSettings(**kwargs)

@register('getEnabledIndexForDevice')
def getEnabledIndexForDevice(**kwargs):
    return CatalystClient().getEnabledIndexForDevice(**kwargs)

@register('getAggregationDataByQuery_16')
def getAggregationDataByQuery_16(**kwargs):
    return CatalystClient().getAggregationDataByQuery_16(**kwargs)

@register('getSiteHealth')
def getSiteHealth(**kwargs):
    return CatalystClient().getSiteHealth(**kwargs)

@register('getStatDataRawDataAsCSV_14')
def getStatDataRawDataAsCSV_14(**kwargs):
    return CatalystClient().getStatDataRawDataAsCSV_14(**kwargs)

@register('getCount_13')
def getCount_13(**kwargs):
    return CatalystClient().getCount_13(**kwargs)

@register('getStatDataFields_15')
def getStatDataFields_15(**kwargs):
    return CatalystClient().getStatDataFields_15(**kwargs)

@register('getStatsPaginationRawData_12')
def getStatsPaginationRawData_12(**kwargs):
    return CatalystClient().getStatsPaginationRawData_12(**kwargs)

@register('getStatQueryFields_16')
def getStatQueryFields_16(**kwargs):
    return CatalystClient().getStatQueryFields_16(**kwargs)

@register('getSiteHealthTopology')
def getSiteHealthTopology(**kwargs):
    return CatalystClient().getSiteHealthTopology(**kwargs)

@register('getAggregationDataByQuery_29')
def getAggregationDataByQuery_29(**kwargs):
    return CatalystClient().getAggregationDataByQuery_29(**kwargs)

@register('getStatDataRawDataAsCSV_27')
def getStatDataRawDataAsCSV_27(**kwargs):
    return CatalystClient().getStatDataRawDataAsCSV_27(**kwargs)

@register('getCount_25')
def getCount_25(**kwargs):
    return CatalystClient().getCount_25(**kwargs)

@register('getStatDataFields_27')
def getStatDataFields_27(**kwargs):
    return CatalystClient().getStatDataFields_27(**kwargs)

@register('getStatsPaginationRawData_25')
def getStatsPaginationRawData_25(**kwargs):
    return CatalystClient().getStatsPaginationRawData_25(**kwargs)

@register('getStatQueryFields_29')
def getStatQueryFields_29(**kwargs):
    return CatalystClient().getStatQueryFields_29(**kwargs)

@register('getAggregationDataByQuery_17')
def getAggregationDataByQuery_17(**kwargs):
    return CatalystClient().getAggregationDataByQuery_17(**kwargs)

@register('getStatDataRawDataAsCSV_15')
def getStatDataRawDataAsCSV_15(**kwargs):
    return CatalystClient().getStatDataRawDataAsCSV_15(**kwargs)

@register('getCount_14')
def getCount_14(**kwargs):
    return CatalystClient().getCount_14(**kwargs)

@register('getStatDataFields_16')
def getStatDataFields_16(**kwargs):
    return CatalystClient().getStatDataFields_16(**kwargs)

@register('getFilterPolicyNameList')
def getFilterPolicyNameList(**kwargs):
    return CatalystClient().getFilterPolicyNameList(**kwargs)

@register('getStatsPaginationRawData_13')
def getStatsPaginationRawData_13(**kwargs):
    return CatalystClient().getStatsPaginationRawData_13(**kwargs)

@register('getStatQueryFields_17')
def getStatQueryFields_17(**kwargs):
    return CatalystClient().getStatQueryFields_17(**kwargs)

@register('getAggregationDataByQuery_19')
def getAggregationDataByQuery_19(**kwargs):
    return CatalystClient().getAggregationDataByQuery_19(**kwargs)

@register('createDeviceSystemCPUStat')
def createDeviceSystemCPUStat(**kwargs):
    return CatalystClient().createDeviceSystemCPUStat(**kwargs)

@register('getStatDataRawDataAsCSV_17')
def getStatDataRawDataAsCSV_17(**kwargs):
    return CatalystClient().getStatDataRawDataAsCSV_17(**kwargs)

@register('getCount_16')
def getCount_16(**kwargs):
    return CatalystClient().getCount_16(**kwargs)

@register('getStatDataFields_18')
def getStatDataFields_18(**kwargs):
    return CatalystClient().getStatDataFields_18(**kwargs)

@register('createDeviceSystemMemoryStat')
def createDeviceSystemMemoryStat(**kwargs):
    return CatalystClient().createDeviceSystemMemoryStat(**kwargs)

@register('getStatsPaginationRawData_15')
def getStatsPaginationRawData_15(**kwargs):
    return CatalystClient().getStatsPaginationRawData_15(**kwargs)

@register('getStatQueryFields_19')
def getStatQueryFields_19(**kwargs):
    return CatalystClient().getStatQueryFields_19(**kwargs)

@register('getAggregationDataByQuery_20')
def getAggregationDataByQuery_20(**kwargs):
    return CatalystClient().getAggregationDataByQuery_20(**kwargs)

@register('getStatDataRawDataAsCSV_18')
def getStatDataRawDataAsCSV_18(**kwargs):
    return CatalystClient().getStatDataRawDataAsCSV_18(**kwargs)

@register('getCount_17')
def getCount_17(**kwargs):
    return CatalystClient().getCount_17(**kwargs)

@register('getStatDataFields_19')
def getStatDataFields_19(**kwargs):
    return CatalystClient().getStatDataFields_19(**kwargs)

@register('getStatsPaginationRawData_16')
def getStatsPaginationRawData_16(**kwargs):
    return CatalystClient().getStatsPaginationRawData_16(**kwargs)

@register('getStatQueryFields_20')
def getStatQueryFields_20(**kwargs):
    return CatalystClient().getStatQueryFields_20(**kwargs)

@register('statisticsApprouteTunnelhealthHistoryGet')
def statisticsApprouteTunnelhealthHistoryGet(**kwargs):
    return CatalystClient().statisticsApprouteTunnelhealthHistoryGet(**kwargs)

@register('statisticsApprouteTunnelhealthOverviewTypeGet')
def statisticsApprouteTunnelhealthOverviewTypeGet(**kwargs):
    return CatalystClient().statisticsApprouteTunnelhealthOverviewTypeGet(**kwargs)

@register('getAggregationDataByQuery_27')
def getAggregationDataByQuery_27(**kwargs):
    return CatalystClient().getAggregationDataByQuery_27(**kwargs)

@register('getStatDataRawDataAsCSV_25')
def getStatDataRawDataAsCSV_25(**kwargs):
    return CatalystClient().getStatDataRawDataAsCSV_25(**kwargs)

@register('getCount_24')
def getCount_24(**kwargs):
    return CatalystClient().getCount_24(**kwargs)

@register('getStatDataFields_26')
def getStatDataFields_26(**kwargs):
    return CatalystClient().getStatDataFields_26(**kwargs)

@register('getStatsPaginationRawData_23')
def getStatsPaginationRawData_23(**kwargs):
    return CatalystClient().getStatsPaginationRawData_23(**kwargs)

@register('getStatQueryFields_27')
def getStatQueryFields_27(**kwargs):
    return CatalystClient().getStatQueryFields_27(**kwargs)

@register('getAggregationDataByQuery_25')
def getAggregationDataByQuery_25(**kwargs):
    return CatalystClient().getAggregationDataByQuery_25(**kwargs)

@register('getStatDataRawDataAsCSV_23')
def getStatDataRawDataAsCSV_23(**kwargs):
    return CatalystClient().getStatDataRawDataAsCSV_23(**kwargs)

@register('getCount_22')
def getCount_22(**kwargs):
    return CatalystClient().getCount_22(**kwargs)

@register('getStatDataFields_24')
def getStatDataFields_24(**kwargs):
    return CatalystClient().getStatDataFields_24(**kwargs)

@register('getStatsPaginationRawData_21')
def getStatsPaginationRawData_21(**kwargs):
    return CatalystClient().getStatsPaginationRawData_21(**kwargs)

@register('getStatQueryFields_25')
def getStatQueryFields_25(**kwargs):
    return CatalystClient().getStatQueryFields_25(**kwargs)

@register('getAggregationDataByQuery_12')
def getAggregationDataByQuery_12(**kwargs):
    return CatalystClient().getAggregationDataByQuery_12(**kwargs)

@register('getStatDataRawDataAsCSV_12')
def getStatDataRawDataAsCSV_12(**kwargs):
    return CatalystClient().getStatDataRawDataAsCSV_12(**kwargs)

@register('getCount_11')
def getCount_11(**kwargs):
    return CatalystClient().getCount_11(**kwargs)

@register('getStatDataFields_13')
def getStatDataFields_13(**kwargs):
    return CatalystClient().getStatDataFields_13(**kwargs)

@register('getStatsPaginationRawData_10')
def getStatsPaginationRawData_10(**kwargs):
    return CatalystClient().getStatsPaginationRawData_10(**kwargs)

@register('getStatQueryFields_13')
def getStatQueryFields_13(**kwargs):
    return CatalystClient().getStatQueryFields_13(**kwargs)

@register('getAggregationDataByQuery_22')
def getAggregationDataByQuery_22(**kwargs):
    return CatalystClient().getAggregationDataByQuery_22(**kwargs)

@register('getStatDataRawDataAsCSV_20')
def getStatDataRawDataAsCSV_20(**kwargs):
    return CatalystClient().getStatDataRawDataAsCSV_20(**kwargs)

@register('getCount_19')
def getCount_19(**kwargs):
    return CatalystClient().getCount_19(**kwargs)

@register('getStatDataFields_21')
def getStatDataFields_21(**kwargs):
    return CatalystClient().getStatDataFields_21(**kwargs)

@register('getStatsPaginationRawData_18')
def getStatsPaginationRawData_18(**kwargs):
    return CatalystClient().getStatsPaginationRawData_18(**kwargs)

@register('getStatQueryFields_22')
def getStatQueryFields_22(**kwargs):
    return CatalystClient().getStatQueryFields_22(**kwargs)

@register('disablePacketCaptureSession')
def disablePacketCaptureSession(**kwargs):
    return CatalystClient().disablePacketCaptureSession(**kwargs)

@register('downloadFile')
def downloadFile(**kwargs):
    return CatalystClient().downloadFile(**kwargs)

@register('forceStopPcapSession')
def forceStopPcapSession(**kwargs):
    return CatalystClient().forceStopPcapSession(**kwargs)

@register('startPcapSession')
def startPcapSession(**kwargs):
    return CatalystClient().startPcapSession(**kwargs)

@register('getFileDownloadStatus')
def getFileDownloadStatus(**kwargs):
    return CatalystClient().getFileDownloadStatus(**kwargs)

@register('stopPcapSession')
def stopPcapSession(**kwargs):
    return CatalystClient().stopPcapSession(**kwargs)

@register('getVnicInfoByVnfId')
def getVnicInfoByVnfId(**kwargs):
    return CatalystClient().getVnicInfoByVnfId(**kwargs)

@register('disableDeviceLog')
def disableDeviceLog(**kwargs):
    return CatalystClient().disableDeviceLog(**kwargs)

@register('downloadDebugLog')
def downloadDebugLog(**kwargs):
    return CatalystClient().downloadDebugLog(**kwargs)

@register('renewSessionInfo')
def renewSessionInfo(**kwargs):
    return CatalystClient().renewSessionInfo(**kwargs)

@register('getSessions')
def getSessions(**kwargs):
    return CatalystClient().getSessions(**kwargs)

@register('clearSession')
def clearSession(**kwargs):
    return CatalystClient().clearSession(**kwargs)

@register('getLogType')
def getLogType(**kwargs):
    return CatalystClient().getLogType(**kwargs)

@register('getDeviceLog')
def getDeviceLog(**kwargs):
    return CatalystClient().getDeviceLog(**kwargs)

@register('activeFlowWithQuery')
def activeFlowWithQuery(**kwargs):
    return CatalystClient().activeFlowWithQuery(**kwargs)

@register('getAggFlow')
def getAggFlow(**kwargs):
    return CatalystClient().getAggFlow(**kwargs)

@register('getAppQosData')
def getAppQosData(**kwargs):
    return CatalystClient().getAppQosData(**kwargs)

@register('getAppQosState')
def getAppQosState(**kwargs):
    return CatalystClient().getAppQosState(**kwargs)

@register('getConcurrentData')
def getConcurrentData(**kwargs):
    return CatalystClient().getConcurrentData(**kwargs)

@register('getConcurrentDomainData')
def getConcurrentDomainData(**kwargs):
    return CatalystClient().getConcurrentDomainData(**kwargs)

@register('getCurrentTimestamp')
def getCurrentTimestamp(**kwargs):
    return CatalystClient().getCurrentTimestamp(**kwargs)

@register('getDeviceBList')
def getDeviceBList(**kwargs):
    return CatalystClient().getDeviceBList(**kwargs)

@register('getDevicesAndInterfacesBySite')
def getDevicesAndInterfacesBySite(**kwargs):
    return CatalystClient().getDevicesAndInterfacesBySite(**kwargs)

@register('getDomainMetric')
def getDomainMetric(**kwargs):
    return CatalystClient().getDomainMetric(**kwargs)

@register('getEventAppHopList')
def getEventAppHopList(**kwargs):
    return CatalystClient().getEventAppHopList(**kwargs)

@register('getEventAppScoreBandwidth')
def getEventAppScoreBandwidth(**kwargs):
    return CatalystClient().getEventAppScoreBandwidth(**kwargs)

@register('getEventFlowFromAppHop')
def getEventFlowFromAppHop(**kwargs):
    return CatalystClient().getEventFlowFromAppHop(**kwargs)

@register('getEventReadout')
def getEventReadout(**kwargs):
    return CatalystClient().getEventReadout(**kwargs)

@register('getEventReadoutBySite')
def getEventReadoutBySite(**kwargs):
    return CatalystClient().getEventReadoutBySite(**kwargs)

@register('getEventReadoutByTraces')
def getEventReadoutByTraces(**kwargs):
    return CatalystClient().getEventReadoutByTraces(**kwargs)

@register('exportTrace')
def exportTrace(**kwargs):
    return CatalystClient().exportTrace(**kwargs)

@register('getFinalizedData')
def getFinalizedData(**kwargs):
    return CatalystClient().getFinalizedData(**kwargs)

@register('getFinalizedDomainData')
def getFinalizedDomainData(**kwargs):
    return CatalystClient().getFinalizedDomainData(**kwargs)

@register('getFlowDetail')
def getFlowDetail(**kwargs):
    return CatalystClient().getFlowDetail(**kwargs)

@register('getFlowMetric')
def getFlowMetric(**kwargs):
    return CatalystClient().getFlowMetric(**kwargs)

@register('getMonitorState')
def getMonitorState(**kwargs):
    return CatalystClient().getMonitorState(**kwargs)

@register('getNwpiDscp')
def getNwpiDscp(**kwargs):
    return CatalystClient().getNwpiDscp(**kwargs)

@register('getNwpiNbarAppGroup')
def getNwpiNbarAppGroup(**kwargs):
    return CatalystClient().getNwpiNbarAppGroup(**kwargs)

@register('getNwpiProtocol')
def getNwpiProtocol(**kwargs):
    return CatalystClient().getNwpiProtocol(**kwargs)

@register('nwpiSettingView')
def nwpiSettingView(**kwargs):
    return CatalystClient().nwpiSettingView(**kwargs)

@register('getPacketFeatures')
def getPacketFeatures(**kwargs):
    return CatalystClient().getPacketFeatures(**kwargs)

@register('getPreloadInfo')
def getPreloadInfo(**kwargs):
    return CatalystClient().getPreloadInfo(**kwargs)

@register('getStatQueryFields_28')
def getStatQueryFields_28(**kwargs):
    return CatalystClient().getStatQueryFields_28(**kwargs)

@register('getRoutingDetailFromLocal')
def getRoutingDetailFromLocal(**kwargs):
    return CatalystClient().getRoutingDetailFromLocal(**kwargs)

@register('getEventStatsData')
def getEventStatsData(**kwargs):
    return CatalystClient().getEventStatsData(**kwargs)

@register('getTaskHistory')
def getTaskHistory(**kwargs):
    return CatalystClient().getTaskHistory(**kwargs)

@register('getTaskTrace')
def getTaskTrace(**kwargs):
    return CatalystClient().getTaskTrace(**kwargs)

@register('getTraceCftRecord')
def getTraceCftRecord(**kwargs):
    return CatalystClient().getTraceCftRecord(**kwargs)

@register('getFinalizedFlowCount')
def getFinalizedFlowCount(**kwargs):
    return CatalystClient().getFinalizedFlowCount(**kwargs)

@register('getFinFlowTimeRange')
def getFinFlowTimeRange(**kwargs):
    return CatalystClient().getFinFlowTimeRange(**kwargs)

@register('traceFinFlowWithQuery')
def traceFinFlowWithQuery(**kwargs):
    return CatalystClient().traceFinFlowWithQuery(**kwargs)

@register('getTraceFlow')
def getTraceFlow(**kwargs):
    return CatalystClient().getTraceFlow(**kwargs)

@register('getTraceHistory')
def getTraceHistory(**kwargs):
    return CatalystClient().getTraceHistory(**kwargs)

@register('getTraceInfoByBaseKey')
def getTraceInfoByBaseKey(**kwargs):
    return CatalystClient().getTraceInfoByBaseKey(**kwargs)

@register('getTraceReadoutFilter')
def getTraceReadoutFilter(**kwargs):
    return CatalystClient().getTraceReadoutFilter(**kwargs)

@register('disableSpeedTestSession')
def disableSpeedTestSession(**kwargs):
    return CatalystClient().disableSpeedTestSession(**kwargs)

@register('getInterfaceBandwidth')
def getInterfaceBandwidth(**kwargs):
    return CatalystClient().getInterfaceBandwidth(**kwargs)

@register('startSpeedTest')
def startSpeedTest(**kwargs):
    return CatalystClient().startSpeedTest(**kwargs)

@register('getSpeedTestStatus')
def getSpeedTestStatus(**kwargs):
    return CatalystClient().getSpeedTestStatus(**kwargs)

@register('stopSpeedTest')
def stopSpeedTest(**kwargs):
    return CatalystClient().stopSpeedTest(**kwargs)

@register('getSpeedTest')
def getSpeedTest(**kwargs):
    return CatalystClient().getSpeedTest(**kwargs)

@register('getUMTSData')
def getUMTSData(**kwargs):
    return CatalystClient().getUMTSData(**kwargs)

@register('updateUmtsSessionStatus')
def updateUmtsSessionStatus(**kwargs):
    return CatalystClient().updateUmtsSessionStatus(**kwargs)

@register('generateBootstrapConfigForVedge')
def generateBootstrapConfigForVedge(**kwargs):
    return CatalystClient().generateBootstrapConfigForVedge(**kwargs)

@register('getBootstrapConfigZip')
def getBootstrapConfigZip(**kwargs):
    return CatalystClient().getBootstrapConfigZip(**kwargs)

@register('generateGenericBootstrapConfigForVedges')
def generateGenericBootstrapConfigForVedges(**kwargs):
    return CatalystClient().generateGenericBootstrapConfigForVedges(**kwargs)

@register('getControllerVEdgeSyncStatus_1')
def getControllerVEdgeSyncStatus_1(**kwargs):
    return CatalystClient().getControllerVEdgeSyncStatus_1(**kwargs)

@register('devicesWithoutSubjectSudi')
def devicesWithoutSubjectSudi(**kwargs):
    return CatalystClient().devicesWithoutSubjectSudi(**kwargs)

@register('getManagementSystemIPInfo_1')
def getManagementSystemIPInfo_1(**kwargs):
    return CatalystClient().getManagementSystemIPInfo_1(**kwargs)

@register('getRMACandidates')
def getRMACandidates(**kwargs):
    return CatalystClient().getRMACandidates(**kwargs)

@register('getRootCertStatusAll')
def getRootCertStatusAll(**kwargs):
    return CatalystClient().getRootCertStatusAll(**kwargs)

@register('checkSelfSignedCert_1')
def checkSelfSignedCert_1(**kwargs):
    return CatalystClient().checkSelfSignedCert_1(**kwargs)

@register('syncRootCertChain')
def syncRootCertChain(**kwargs):
    return CatalystClient().syncRootCertChain(**kwargs)

@register('getTenantManagementSystemIPs')
def getTenantManagementSystemIPs(**kwargs):
    return CatalystClient().getTenantManagementSystemIPs(**kwargs)

@register('getCloudDockDataBasedOnDeviceType')
def getCloudDockDataBasedOnDeviceType(**kwargs):
    return CatalystClient().getCloudDockDataBasedOnDeviceType(**kwargs)

@register('getCloudDockDefaultConfigBasedOnDeviceType')
def getCloudDockDefaultConfigBasedOnDeviceType(**kwargs):
    return CatalystClient().getCloudDockDefaultConfigBasedOnDeviceType(**kwargs)

@register('getAllUnclaimedDevices')
def getAllUnclaimedDevices(**kwargs):
    return CatalystClient().getAllUnclaimedDevices(**kwargs)

@register('checkvEdgeDevicePresence')
def checkvEdgeDevicePresence(**kwargs):
    return CatalystClient().checkvEdgeDevicePresence(**kwargs)

@register('getDevicesDetails')
def getDevicesDetails(**kwargs):
    return CatalystClient().getDevicesDetails(**kwargs)

@register('getReverseProxyMappings')
def getReverseProxyMappings(**kwargs):
    return CatalystClient().getReverseProxyMappings(**kwargs)

@register('getCloudXStatus')
def getCloudXStatus(**kwargs):
    return CatalystClient().getCloudXStatus(**kwargs)

@register('getAttachedClientList')
def getAttachedClientList(**kwargs):
    return CatalystClient().getAttachedClientList(**kwargs)

@register('getAttachedDiaList')
def getAttachedDiaList(**kwargs):
    return CatalystClient().getAttachedDiaList(**kwargs)

@register('getAttachedGatewayList')
def getAttachedGatewayList(**kwargs):
    return CatalystClient().getAttachedGatewayList(**kwargs)

@register('getCloudXAvailableApps')
def getCloudXAvailableApps(**kwargs):
    return CatalystClient().getCloudXAvailableApps(**kwargs)

@register('getSiteList')
def getSiteList(**kwargs):
    return CatalystClient().getSiteList(**kwargs)

@register('getDiaList')
def getDiaList(**kwargs):
    return CatalystClient().getDiaList(**kwargs)

@register('getGatewayList')
def getGatewayList(**kwargs):
    return CatalystClient().getGatewayList(**kwargs)

@register('getApps')
def getApps(**kwargs):
    return CatalystClient().getApps(**kwargs)

@register('getSigTunnelList_1')
def getSigTunnelList_1(**kwargs):
    return CatalystClient().getSigTunnelList_1(**kwargs)

@register('sitePerApp')
def sitePerApp(**kwargs):
    return CatalystClient().sitePerApp(**kwargs)

@register('getAttachedConfig')
def getAttachedConfig(**kwargs):
    return CatalystClient().getAttachedConfig(**kwargs)

@register('generateCLIModeDevices')
def generateCLIModeDevices(**kwargs):
    return CatalystClient().generateCLIModeDevices(**kwargs)

@register('generatevManageModeDevices')
def generatevManageModeDevices(**kwargs):
    return CatalystClient().generatevManageModeDevices(**kwargs)

@register('getDeviceDiff')
def getDeviceDiff(**kwargs):
    return CatalystClient().getDeviceDiff(**kwargs)

@register('getCompatibleDevices')
def getCompatibleDevices(**kwargs):
    return CatalystClient().getCompatibleDevices(**kwargs)

@register('getRunningConfig')
def getRunningConfig(**kwargs):
    return CatalystClient().getRunningConfig(**kwargs)

@register('getVpnForDevice')
def getVpnForDevice(**kwargs):
    return CatalystClient().getVpnForDevice(**kwargs)

@register('getCORStatus')
def getCORStatus(**kwargs):
    return CatalystClient().getCORStatus(**kwargs)

@register('getAmiList')
def getAmiList(**kwargs):
    return CatalystClient().getAmiList(**kwargs)

@register('getCloudList')
def getCloudList(**kwargs):
    return CatalystClient().getCloudList(**kwargs)

@register('getCloudAccounts')
def getCloudAccounts(**kwargs):
    return CatalystClient().getCloudAccounts(**kwargs)

@register('getCloudHostVpcAccountDetails')
def getCloudHostVpcAccountDetails(**kwargs):
    return CatalystClient().getCloudHostVpcAccountDetails(**kwargs)

@register('getCloudMappedHostAccounts')
def getCloudMappedHostAccounts(**kwargs):
    return CatalystClient().getCloudMappedHostAccounts(**kwargs)

@register('getCloudOnRampDevices')
def getCloudOnRampDevices(**kwargs):
    return CatalystClient().getCloudOnRampDevices(**kwargs)

@register('getHostVPCs')
def getHostVPCs(**kwargs):
    return CatalystClient().getHostVPCs(**kwargs)

@register('getExternalId')
def getExternalId(**kwargs):
    return CatalystClient().getExternalId(**kwargs)

@register('getTransitDevicePairAndHostList')
def getTransitDevicePairAndHostList(**kwargs):
    return CatalystClient().getTransitDevicePairAndHostList(**kwargs)

@register('getTransitVpcVpnList')
def getTransitVpcVpnList(**kwargs):
    return CatalystClient().getTransitVpcVpnList(**kwargs)

@register('getCloudHostVPCs')
def getCloudHostVPCs(**kwargs):
    return CatalystClient().getCloudHostVPCs(**kwargs)

@register('getMappedVPCs')
def getMappedVPCs(**kwargs):
    return CatalystClient().getMappedVPCs(**kwargs)

@register('getPemKeyList')
def getPemKeyList(**kwargs):
    return CatalystClient().getPemKeyList(**kwargs)

@register('getTransitVPCs')
def getTransitVPCs(**kwargs):
    return CatalystClient().getTransitVPCs(**kwargs)

@register('getTransitVPCSupportedSize')
def getTransitVPCSupportedSize(**kwargs):
    return CatalystClient().getTransitVPCSupportedSize(**kwargs)

@register('getCortexStatus')
def getCortexStatus(**kwargs):
    return CatalystClient().getCortexStatus(**kwargs)

@register('getMappedWanResourceGroups')
def getMappedWanResourceGroups(**kwargs):
    return CatalystClient().getMappedWanResourceGroups(**kwargs)

@register('getWanResourceGroups')
def getWanResourceGroups(**kwargs):
    return CatalystClient().getWanResourceGroups(**kwargs)

@register('generateMasterTemplateList')
def generateMasterTemplateList(**kwargs):
    return CatalystClient().generateMasterTemplateList(**kwargs)

@register('getAttachedDeviceList')
def getAttachedDeviceList(**kwargs):
    return CatalystClient().getAttachedDeviceList(**kwargs)

@register('getAttachedConfigToDevice')
def getAttachedConfigToDevice(**kwargs):
    return CatalystClient().getAttachedConfigToDevice(**kwargs)

@register('getDeviceListByMasterTemplateId')
def getDeviceListByMasterTemplateId(**kwargs):
    return CatalystClient().getDeviceListByMasterTemplateId(**kwargs)

@register('checkVbond')
def checkVbond(**kwargs):
    return CatalystClient().checkVbond(**kwargs)

@register('isMigrationRequired')
def isMigrationRequired(**kwargs):
    return CatalystClient().isMigrationRequired(**kwargs)

@register('generateTemplateForMigration')
def generateTemplateForMigration(**kwargs):
    return CatalystClient().generateTemplateForMigration(**kwargs)

@register('migrationInfo')
def migrationInfo(**kwargs):
    return CatalystClient().migrationInfo(**kwargs)

@register('getMasterTemplateDefinition')
def getMasterTemplateDefinition(**kwargs):
    return CatalystClient().getMasterTemplateDefinition(**kwargs)

@register('getOutOfSyncTemplates')
def getOutOfSyncTemplates(**kwargs):
    return CatalystClient().getOutOfSyncTemplates(**kwargs)

@register('getOutOfSyncDevices')
def getOutOfSyncDevices(**kwargs):
    return CatalystClient().getOutOfSyncDevices(**kwargs)

@register('getAssociatedFeatureTemplatesDetails')
def getAssociatedFeatureTemplatesDetails(**kwargs):
    return CatalystClient().getAssociatedFeatureTemplatesDetails(**kwargs)

@register('generateFeatureTemplateList')
def generateFeatureTemplateList(**kwargs):
    return CatalystClient().generateFeatureTemplateList(**kwargs)

@register('getNetworkInterface')
def getNetworkInterface(**kwargs):
    return CatalystClient().getNetworkInterface(**kwargs)

@register('getDefaultNetworks')
def getDefaultNetworks(**kwargs):
    return CatalystClient().getDefaultNetworks(**kwargs)

@register('getTemplateDefinition')
def getTemplateDefinition(**kwargs):
    return CatalystClient().getTemplateDefinition(**kwargs)

@register('getDeviceTemplatesAttachedToFeature')
def getDeviceTemplatesAttachedToFeature(**kwargs):
    return CatalystClient().getDeviceTemplatesAttachedToFeature(**kwargs)

@register('listLITemplate')
def listLITemplate(**kwargs):
    return CatalystClient().listLITemplate(**kwargs)

@register('generateMasterTemplateDefinition')
def generateMasterTemplateDefinition(**kwargs):
    return CatalystClient().generateMasterTemplateDefinition(**kwargs)

@register('getTemplateForMigration')
def getTemplateForMigration(**kwargs):
    return CatalystClient().getTemplateForMigration(**kwargs)

@register('getGeneralTemplate')
def getGeneralTemplate(**kwargs):
    return CatalystClient().getGeneralTemplate(**kwargs)

@register('generateTemplateTypes')
def generateTemplateTypes(**kwargs):
    return CatalystClient().generateTemplateTypes(**kwargs)

@register('generateTemplateTypeDefinition')
def generateTemplateTypeDefinition(**kwargs):
    return CatalystClient().generateTemplateTypeDefinition(**kwargs)

@register('generateTemplateByDeviceType')
def generateTemplateByDeviceType(**kwargs):
    return CatalystClient().generateTemplateByDeviceType(**kwargs)

@register('previewById')
def previewById(**kwargs):
    return CatalystClient().previewById(**kwargs)

@register('previewById_1')
def previewById_1(**kwargs):
    return CatalystClient().previewById_1(**kwargs)

@register('previewById_2')
def previewById_2(**kwargs):
    return CatalystClient().previewById_2(**kwargs)

@register('previewById_3')
def previewById_3(**kwargs):
    return CatalystClient().previewById_3(**kwargs)

@register('getCloudDiscoveredApps')
def getCloudDiscoveredApps(**kwargs):
    return CatalystClient().getCloudDiscoveredApps(**kwargs)

@register('getCustomApps')
def getCustomApps(**kwargs):
    return CatalystClient().getCustomApps(**kwargs)

@register('getCustomAppById')
def getCustomAppById(**kwargs):
    return CatalystClient().getCustomAppById(**kwargs)

@register('getDefinitions_8')
def getDefinitions_8(**kwargs):
    return CatalystClient().getDefinitions_8(**kwargs)

@register('previewPolicyDefinitionById_8')
def previewPolicyDefinitionById_8(**kwargs):
    return CatalystClient().previewPolicyDefinitionById_8(**kwargs)

@register('getPolicyDefinition_8')
def getPolicyDefinition_8(**kwargs):
    return CatalystClient().getPolicyDefinition_8(**kwargs)

@register('getDefinitions_9')
def getDefinitions_9(**kwargs):
    return CatalystClient().getDefinitions_9(**kwargs)

@register('previewPolicyDefinitionById_9')
def previewPolicyDefinitionById_9(**kwargs):
    return CatalystClient().previewPolicyDefinitionById_9(**kwargs)

@register('getPolicyDefinition_9')
def getPolicyDefinition_9(**kwargs):
    return CatalystClient().getPolicyDefinition_9(**kwargs)

@register('getDefinitions_11')
def getDefinitions_11(**kwargs):
    return CatalystClient().getDefinitions_11(**kwargs)

@register('previewPolicyDefinitionById_11')
def previewPolicyDefinitionById_11(**kwargs):
    return CatalystClient().previewPolicyDefinitionById_11(**kwargs)

@register('getPolicyDefinition_11')
def getPolicyDefinition_11(**kwargs):
    return CatalystClient().getPolicyDefinition_11(**kwargs)

@register('getDefinitions_10')
def getDefinitions_10(**kwargs):
    return CatalystClient().getDefinitions_10(**kwargs)

@register('previewPolicyDefinitionById_10')
def previewPolicyDefinitionById_10(**kwargs):
    return CatalystClient().previewPolicyDefinitionById_10(**kwargs)

@register('getPolicyDefinition_10')
def getPolicyDefinition_10(**kwargs):
    return CatalystClient().getPolicyDefinition_10(**kwargs)

@register('getDefinitions_12')
def getDefinitions_12(**kwargs):
    return CatalystClient().getDefinitions_12(**kwargs)

@register('previewPolicyDefinitionById_12')
def previewPolicyDefinitionById_12(**kwargs):
    return CatalystClient().previewPolicyDefinitionById_12(**kwargs)

@register('getPolicyDefinition_12')
def getPolicyDefinition_12(**kwargs):
    return CatalystClient().getPolicyDefinition_12(**kwargs)

@register('getDefinitions_13')
def getDefinitions_13(**kwargs):
    return CatalystClient().getDefinitions_13(**kwargs)

@register('previewPolicyDefinitionById_13')
def previewPolicyDefinitionById_13(**kwargs):
    return CatalystClient().previewPolicyDefinitionById_13(**kwargs)

@register('getPolicyDefinition_13')
def getPolicyDefinition_13(**kwargs):
    return CatalystClient().getPolicyDefinition_13(**kwargs)

@register('getDefinitions_14')
def getDefinitions_14(**kwargs):
    return CatalystClient().getDefinitions_14(**kwargs)

@register('previewPolicyDefinitionById_14')
def previewPolicyDefinitionById_14(**kwargs):
    return CatalystClient().previewPolicyDefinitionById_14(**kwargs)

@register('getPolicyDefinition_14')
def getPolicyDefinition_14(**kwargs):
    return CatalystClient().getPolicyDefinition_14(**kwargs)

@register('getDefinitions_15')
def getDefinitions_15(**kwargs):
    return CatalystClient().getDefinitions_15(**kwargs)

@register('previewPolicyDefinitionById_15')
def previewPolicyDefinitionById_15(**kwargs):
    return CatalystClient().previewPolicyDefinitionById_15(**kwargs)

@register('getPolicyDefinition_15')
def getPolicyDefinition_15(**kwargs):
    return CatalystClient().getPolicyDefinition_15(**kwargs)

@register('getDefinitions_16')
def getDefinitions_16(**kwargs):
    return CatalystClient().getDefinitions_16(**kwargs)

@register('previewPolicyDefinitionById_16')
def previewPolicyDefinitionById_16(**kwargs):
    return CatalystClient().previewPolicyDefinitionById_16(**kwargs)

@register('getPolicyDefinition_16')
def getPolicyDefinition_16(**kwargs):
    return CatalystClient().getPolicyDefinition_16(**kwargs)

@register('getDefinitions_17')
def getDefinitions_17(**kwargs):
    return CatalystClient().getDefinitions_17(**kwargs)

@register('previewPolicyDefinitionById_17')
def previewPolicyDefinitionById_17(**kwargs):
    return CatalystClient().previewPolicyDefinitionById_17(**kwargs)

@register('getPolicyDefinition_17')
def getPolicyDefinition_17(**kwargs):
    return CatalystClient().getPolicyDefinition_17(**kwargs)

@register('getDefinitions_25')
def getDefinitions_25(**kwargs):
    return CatalystClient().getDefinitions_25(**kwargs)

@register('previewPolicyDefinitionById_25')
def previewPolicyDefinitionById_25(**kwargs):
    return CatalystClient().previewPolicyDefinitionById_25(**kwargs)

@register('getPolicyDefinition_25')
def getPolicyDefinition_25(**kwargs):
    return CatalystClient().getPolicyDefinition_25(**kwargs)

@register('getDefinitions')
def getDefinitions(**kwargs):
    return CatalystClient().getDefinitions(**kwargs)

@register('previewPolicyDefinitionById')
def previewPolicyDefinitionById(**kwargs):
    return CatalystClient().previewPolicyDefinitionById(**kwargs)

@register('getPolicyDefinition')
def getPolicyDefinition(**kwargs):
    return CatalystClient().getPolicyDefinition(**kwargs)

@register('getDefinitions_26')
def getDefinitions_26(**kwargs):
    return CatalystClient().getDefinitions_26(**kwargs)

@register('previewPolicyDefinitionById_26')
def previewPolicyDefinitionById_26(**kwargs):
    return CatalystClient().previewPolicyDefinitionById_26(**kwargs)

@register('getPolicyDefinition_26')
def getPolicyDefinition_26(**kwargs):
    return CatalystClient().getPolicyDefinition_26(**kwargs)

@register('getDefinitions_28')
def getDefinitions_28(**kwargs):
    return CatalystClient().getDefinitions_28(**kwargs)

@register('previewPolicyDefinitionById_28')
def previewPolicyDefinitionById_28(**kwargs):
    return CatalystClient().previewPolicyDefinitionById_28(**kwargs)

@register('getPolicyDefinition_28')
def getPolicyDefinition_28(**kwargs):
    return CatalystClient().getPolicyDefinition_28(**kwargs)

@register('getDefinitions_27')
def getDefinitions_27(**kwargs):
    return CatalystClient().getDefinitions_27(**kwargs)

@register('previewPolicyDefinitionById_27')
def previewPolicyDefinitionById_27(**kwargs):
    return CatalystClient().previewPolicyDefinitionById_27(**kwargs)

@register('getPolicyDefinition_27')
def getPolicyDefinition_27(**kwargs):
    return CatalystClient().getPolicyDefinition_27(**kwargs)

@register('getDefinitions_4')
def getDefinitions_4(**kwargs):
    return CatalystClient().getDefinitions_4(**kwargs)

@register('previewPolicyDefinitionById_4')
def previewPolicyDefinitionById_4(**kwargs):
    return CatalystClient().previewPolicyDefinitionById_4(**kwargs)

@register('getPolicyDefinition_4')
def getPolicyDefinition_4(**kwargs):
    return CatalystClient().getPolicyDefinition_4(**kwargs)

@register('getDefinitions_18')
def getDefinitions_18(**kwargs):
    return CatalystClient().getDefinitions_18(**kwargs)

@register('previewPolicyDefinitionById_18')
def previewPolicyDefinitionById_18(**kwargs):
    return CatalystClient().previewPolicyDefinitionById_18(**kwargs)

@register('getPolicyDefinition_18')
def getPolicyDefinition_18(**kwargs):
    return CatalystClient().getPolicyDefinition_18(**kwargs)

@register('getDefinitions_5')
def getDefinitions_5(**kwargs):
    return CatalystClient().getDefinitions_5(**kwargs)

@register('previewPolicyDefinitionById_5')
def previewPolicyDefinitionById_5(**kwargs):
    return CatalystClient().previewPolicyDefinitionById_5(**kwargs)

@register('getPolicyDefinition_5')
def getPolicyDefinition_5(**kwargs):
    return CatalystClient().getPolicyDefinition_5(**kwargs)

@register('getDefinitions_29')
def getDefinitions_29(**kwargs):
    return CatalystClient().getDefinitions_29(**kwargs)

@register('previewPolicyDefinitionById_29')
def previewPolicyDefinitionById_29(**kwargs):
    return CatalystClient().previewPolicyDefinitionById_29(**kwargs)

@register('getPolicyDefinition_29')
def getPolicyDefinition_29(**kwargs):
    return CatalystClient().getPolicyDefinition_29(**kwargs)

@register('getDefinitions_1')
def getDefinitions_1(**kwargs):
    return CatalystClient().getDefinitions_1(**kwargs)

@register('previewPolicyDefinitionById_1')
def previewPolicyDefinitionById_1(**kwargs):
    return CatalystClient().previewPolicyDefinitionById_1(**kwargs)

@register('getPolicyDefinition_1')
def getPolicyDefinition_1(**kwargs):
    return CatalystClient().getPolicyDefinition_1(**kwargs)

@register('getDefinitions_19')
def getDefinitions_19(**kwargs):
    return CatalystClient().getDefinitions_19(**kwargs)

@register('previewPolicyDefinitionById_19')
def previewPolicyDefinitionById_19(**kwargs):
    return CatalystClient().previewPolicyDefinitionById_19(**kwargs)

@register('getPolicyDefinition_19')
def getPolicyDefinition_19(**kwargs):
    return CatalystClient().getPolicyDefinition_19(**kwargs)

@register('getDefinitions_20')
def getDefinitions_20(**kwargs):
    return CatalystClient().getDefinitions_20(**kwargs)

@register('previewPolicyDefinitionById_20')
def previewPolicyDefinitionById_20(**kwargs):
    return CatalystClient().previewPolicyDefinitionById_20(**kwargs)

@register('getPolicyDefinition_20')
def getPolicyDefinition_20(**kwargs):
    return CatalystClient().getPolicyDefinition_20(**kwargs)

@register('getDefinitions_21')
def getDefinitions_21(**kwargs):
    return CatalystClient().getDefinitions_21(**kwargs)

@register('previewPolicyDefinitionById_21')
def previewPolicyDefinitionById_21(**kwargs):
    return CatalystClient().previewPolicyDefinitionById_21(**kwargs)

@register('getPolicyDefinition_21')
def getPolicyDefinition_21(**kwargs):
    return CatalystClient().getPolicyDefinition_21(**kwargs)

@register('getDefinitions_30')
def getDefinitions_30(**kwargs):
    return CatalystClient().getDefinitions_30(**kwargs)

@register('previewPolicyDefinitionById_30')
def previewPolicyDefinitionById_30(**kwargs):
    return CatalystClient().previewPolicyDefinitionById_30(**kwargs)

@register('getPolicyDefinition_30')
def getPolicyDefinition_30(**kwargs):
    return CatalystClient().getPolicyDefinition_30(**kwargs)

@register('getDefinitions_3')
def getDefinitions_3(**kwargs):
    return CatalystClient().getDefinitions_3(**kwargs)

@register('previewPolicyDefinitionById_3')
def previewPolicyDefinitionById_3(**kwargs):
    return CatalystClient().previewPolicyDefinitionById_3(**kwargs)

@register('getPolicyDefinition_3')
def getPolicyDefinition_3(**kwargs):
    return CatalystClient().getPolicyDefinition_3(**kwargs)

@register('getDefinitions_22')
def getDefinitions_22(**kwargs):
    return CatalystClient().getDefinitions_22(**kwargs)

@register('previewPolicyDefinitionById_22')
def previewPolicyDefinitionById_22(**kwargs):
    return CatalystClient().previewPolicyDefinitionById_22(**kwargs)

@register('getPolicyDefinition_22')
def getPolicyDefinition_22(**kwargs):
    return CatalystClient().getPolicyDefinition_22(**kwargs)

@register('getDefinitions_23')
def getDefinitions_23(**kwargs):
    return CatalystClient().getDefinitions_23(**kwargs)

@register('previewPolicyDefinitionById_23')
def previewPolicyDefinitionById_23(**kwargs):
    return CatalystClient().previewPolicyDefinitionById_23(**kwargs)

@register('getPolicyDefinition_23')
def getPolicyDefinition_23(**kwargs):
    return CatalystClient().getPolicyDefinition_23(**kwargs)

@register('getDefinitions_24')
def getDefinitions_24(**kwargs):
    return CatalystClient().getDefinitions_24(**kwargs)

@register('previewPolicyDefinitionById_24')
def previewPolicyDefinitionById_24(**kwargs):
    return CatalystClient().previewPolicyDefinitionById_24(**kwargs)

@register('getPolicyDefinition_24')
def getPolicyDefinition_24(**kwargs):
    return CatalystClient().getPolicyDefinition_24(**kwargs)

@register('getDefinitions_6')
def getDefinitions_6(**kwargs):
    return CatalystClient().getDefinitions_6(**kwargs)

@register('previewPolicyDefinitionById_6')
def previewPolicyDefinitionById_6(**kwargs):
    return CatalystClient().previewPolicyDefinitionById_6(**kwargs)

@register('getPolicyDefinition_6')
def getPolicyDefinition_6(**kwargs):
    return CatalystClient().getPolicyDefinition_6(**kwargs)

@register('getDefinitions_2')
def getDefinitions_2(**kwargs):
    return CatalystClient().getDefinitions_2(**kwargs)

@register('previewPolicyDefinitionById_2')
def previewPolicyDefinitionById_2(**kwargs):
    return CatalystClient().previewPolicyDefinitionById_2(**kwargs)

@register('getPolicyDefinition_2')
def getPolicyDefinition_2(**kwargs):
    return CatalystClient().getPolicyDefinition_2(**kwargs)

@register('getDefinitions_7')
def getDefinitions_7(**kwargs):
    return CatalystClient().getDefinitions_7(**kwargs)

@register('previewPolicyDefinitionById_7')
def previewPolicyDefinitionById_7(**kwargs):
    return CatalystClient().previewPolicyDefinitionById_7(**kwargs)

@register('getPolicyDefinition_7')
def getPolicyDefinition_7(**kwargs):
    return CatalystClient().getPolicyDefinition_7(**kwargs)

@register('getListReference')
def getListReference(**kwargs):
    return CatalystClient().getListReference(**kwargs)

@register('sgts')
def sgts(**kwargs):
    return CatalystClient().sgts(**kwargs)

@register('getAllPolicyLists')
def getAllPolicyLists(**kwargs):
    return CatalystClient().getAllPolicyLists(**kwargs)

@register('getPolicyLists_3')
def getPolicyLists_3(**kwargs):
    return CatalystClient().getPolicyLists_3(**kwargs)

@register('getPolicyListsWithInfoTag_3')
def getPolicyListsWithInfoTag_3(**kwargs):
    return CatalystClient().getPolicyListsWithInfoTag_3(**kwargs)

@register('previewPolicyListById_3')
def previewPolicyListById_3(**kwargs):
    return CatalystClient().previewPolicyListById_3(**kwargs)

@register('getListsById_3')
def getListsById_3(**kwargs):
    return CatalystClient().getListsById_3(**kwargs)

@register('getPolicyLists_4')
def getPolicyLists_4(**kwargs):
    return CatalystClient().getPolicyLists_4(**kwargs)

@register('getPolicyListsWithInfoTag_4')
def getPolicyListsWithInfoTag_4(**kwargs):
    return CatalystClient().getPolicyListsWithInfoTag_4(**kwargs)

@register('previewPolicyListById_4')
def previewPolicyListById_4(**kwargs):
    return CatalystClient().previewPolicyListById_4(**kwargs)

@register('getListsById_4')
def getListsById_4(**kwargs):
    return CatalystClient().getListsById_4(**kwargs)

@register('getPolicyLists_5')
def getPolicyLists_5(**kwargs):
    return CatalystClient().getPolicyLists_5(**kwargs)

@register('getPolicyListsWithInfoTag_5')
def getPolicyListsWithInfoTag_5(**kwargs):
    return CatalystClient().getPolicyListsWithInfoTag_5(**kwargs)

@register('previewPolicyListById_5')
def previewPolicyListById_5(**kwargs):
    return CatalystClient().previewPolicyListById_5(**kwargs)

@register('getListsById_5')
def getListsById_5(**kwargs):
    return CatalystClient().getListsById_5(**kwargs)

@register('getPolicyLists_13')
def getPolicyLists_13(**kwargs):
    return CatalystClient().getPolicyLists_13(**kwargs)

@register('getPolicyListsWithInfoTag_14')
def getPolicyListsWithInfoTag_14(**kwargs):
    return CatalystClient().getPolicyListsWithInfoTag_14(**kwargs)

@register('previewPolicyListById_14')
def previewPolicyListById_14(**kwargs):
    return CatalystClient().previewPolicyListById_14(**kwargs)

@register('getListsById_14')
def getListsById_14(**kwargs):
    return CatalystClient().getListsById_14(**kwargs)

@register('getPolicyLists_6')
def getPolicyLists_6(**kwargs):
    return CatalystClient().getPolicyLists_6(**kwargs)

@register('getPolicyListsWithInfoTag_6')
def getPolicyListsWithInfoTag_6(**kwargs):
    return CatalystClient().getPolicyListsWithInfoTag_6(**kwargs)

@register('previewPolicyListById_6')
def previewPolicyListById_6(**kwargs):
    return CatalystClient().previewPolicyListById_6(**kwargs)

@register('getListsById_6')
def getListsById_6(**kwargs):
    return CatalystClient().getListsById_6(**kwargs)

@register('getPolicyLists_7')
def getPolicyLists_7(**kwargs):
    return CatalystClient().getPolicyLists_7(**kwargs)

@register('getPolicyListsWithInfoTag_7')
def getPolicyListsWithInfoTag_7(**kwargs):
    return CatalystClient().getPolicyListsWithInfoTag_7(**kwargs)

@register('previewPolicyListById_7')
def previewPolicyListById_7(**kwargs):
    return CatalystClient().previewPolicyListById_7(**kwargs)

@register('getListsById_7')
def getListsById_7(**kwargs):
    return CatalystClient().getListsById_7(**kwargs)

@register('getPolicyLists_8')
def getPolicyLists_8(**kwargs):
    return CatalystClient().getPolicyLists_8(**kwargs)

@register('getPolicyListsWithInfoTag_8')
def getPolicyListsWithInfoTag_8(**kwargs):
    return CatalystClient().getPolicyListsWithInfoTag_8(**kwargs)

@register('previewPolicyListById_8')
def previewPolicyListById_8(**kwargs):
    return CatalystClient().previewPolicyListById_8(**kwargs)

@register('getListsById_8')
def getListsById_8(**kwargs):
    return CatalystClient().getListsById_8(**kwargs)

@register('getPolicyLists_9')
def getPolicyLists_9(**kwargs):
    return CatalystClient().getPolicyLists_9(**kwargs)

@register('getPolicyListsWithInfoTag_10')
def getPolicyListsWithInfoTag_10(**kwargs):
    return CatalystClient().getPolicyListsWithInfoTag_10(**kwargs)

@register('previewPolicyListById_10')
def previewPolicyListById_10(**kwargs):
    return CatalystClient().previewPolicyListById_10(**kwargs)

@register('getListsById_10')
def getListsById_10(**kwargs):
    return CatalystClient().getListsById_10(**kwargs)

@register('getListsForAllDataPrefixes')
def getListsForAllDataPrefixes(**kwargs):
    return CatalystClient().getListsForAllDataPrefixes(**kwargs)

@register('getPolicyListsWithInfoTag_9')
def getPolicyListsWithInfoTag_9(**kwargs):
    return CatalystClient().getPolicyListsWithInfoTag_9(**kwargs)

@register('previewPolicyListById_9')
def previewPolicyListById_9(**kwargs):
    return CatalystClient().previewPolicyListById_9(**kwargs)

@register('getListsById_9')
def getListsById_9(**kwargs):
    return CatalystClient().getListsById_9(**kwargs)

@register('getAllDataPrefixAndFQDNLists')
def getAllDataPrefixAndFQDNLists(**kwargs):
    return CatalystClient().getAllDataPrefixAndFQDNLists(**kwargs)

@register('getPolicyListsWithInfoTag_15')
def getPolicyListsWithInfoTag_15(**kwargs):
    return CatalystClient().getPolicyListsWithInfoTag_15(**kwargs)

@register('previewPolicyListById_15')
def previewPolicyListById_15(**kwargs):
    return CatalystClient().previewPolicyListById_15(**kwargs)

@register('getListsById_15')
def getListsById_15(**kwargs):
    return CatalystClient().getListsById_15(**kwargs)

@register('getPolicyLists_10')
def getPolicyLists_10(**kwargs):
    return CatalystClient().getPolicyLists_10(**kwargs)

@register('getPolicyListsWithInfoTag_11')
def getPolicyListsWithInfoTag_11(**kwargs):
    return CatalystClient().getPolicyListsWithInfoTag_11(**kwargs)

@register('previewPolicyListById_11')
def previewPolicyListById_11(**kwargs):
    return CatalystClient().previewPolicyListById_11(**kwargs)

@register('getListsById_11')
def getListsById_11(**kwargs):
    return CatalystClient().getListsById_11(**kwargs)

@register('getPolicyLists_11')
def getPolicyLists_11(**kwargs):
    return CatalystClient().getPolicyLists_11(**kwargs)

@register('getPolicyListsWithInfoTag_12')
def getPolicyListsWithInfoTag_12(**kwargs):
    return CatalystClient().getPolicyListsWithInfoTag_12(**kwargs)

@register('previewPolicyListById_12')
def previewPolicyListById_12(**kwargs):
    return CatalystClient().previewPolicyListById_12(**kwargs)

@register('getListsById_12')
def getListsById_12(**kwargs):
    return CatalystClient().getListsById_12(**kwargs)

@register('getPolicyLists_12')
def getPolicyLists_12(**kwargs):
    return CatalystClient().getPolicyLists_12(**kwargs)

@register('getPolicyListsWithInfoTag_13')
def getPolicyListsWithInfoTag_13(**kwargs):
    return CatalystClient().getPolicyListsWithInfoTag_13(**kwargs)

@register('previewPolicyListById_13')
def previewPolicyListById_13(**kwargs):
    return CatalystClient().previewPolicyListById_13(**kwargs)

@register('getListsById_13')
def getListsById_13(**kwargs):
    return CatalystClient().getListsById_13(**kwargs)

@register('getPolicyLists_14')
def getPolicyLists_14(**kwargs):
    return CatalystClient().getPolicyLists_14(**kwargs)

@register('getPolicyListsWithInfoTag_16')
def getPolicyListsWithInfoTag_16(**kwargs):
    return CatalystClient().getPolicyListsWithInfoTag_16(**kwargs)

@register('previewPolicyListById_16')
def previewPolicyListById_16(**kwargs):
    return CatalystClient().previewPolicyListById_16(**kwargs)

@register('getListsById_16')
def getListsById_16(**kwargs):
    return CatalystClient().getListsById_16(**kwargs)

@register('getPolicyLists_15')
def getPolicyLists_15(**kwargs):
    return CatalystClient().getPolicyLists_15(**kwargs)

@register('getGeoLocationLists')
def getGeoLocationLists(**kwargs):
    return CatalystClient().getGeoLocationLists(**kwargs)

@register('getPolicyListsWithInfoTag_17')
def getPolicyListsWithInfoTag_17(**kwargs):
    return CatalystClient().getPolicyListsWithInfoTag_17(**kwargs)

@register('previewPolicyListById_17')
def previewPolicyListById_17(**kwargs):
    return CatalystClient().previewPolicyListById_17(**kwargs)

@register('getListsById_17')
def getListsById_17(**kwargs):
    return CatalystClient().getListsById_17(**kwargs)

@register('getPolicyLists_16')
def getPolicyLists_16(**kwargs):
    return CatalystClient().getPolicyLists_16(**kwargs)

@register('getPolicyListsWithInfoTag_18')
def getPolicyListsWithInfoTag_18(**kwargs):
    return CatalystClient().getPolicyListsWithInfoTag_18(**kwargs)

@register('previewPolicyListById_18')
def previewPolicyListById_18(**kwargs):
    return CatalystClient().previewPolicyListById_18(**kwargs)

@register('getListsById_18')
def getListsById_18(**kwargs):
    return CatalystClient().getListsById_18(**kwargs)

@register('getListsForAllPrefixes')
def getListsForAllPrefixes(**kwargs):
    return CatalystClient().getListsForAllPrefixes(**kwargs)

@register('getPolicyListsWithInfoTag_21')
def getPolicyListsWithInfoTag_21(**kwargs):
    return CatalystClient().getPolicyListsWithInfoTag_21(**kwargs)

@register('previewPolicyListById_21')
def previewPolicyListById_21(**kwargs):
    return CatalystClient().previewPolicyListById_21(**kwargs)

@register('getListsById_21')
def getListsById_21(**kwargs):
    return CatalystClient().getListsById_21(**kwargs)

@register('getPolicyLists_17')
def getPolicyLists_17(**kwargs):
    return CatalystClient().getPolicyLists_17(**kwargs)

@register('getPolicyListsWithInfoTag_19')
def getPolicyListsWithInfoTag_19(**kwargs):
    return CatalystClient().getPolicyListsWithInfoTag_19(**kwargs)

@register('previewPolicyListById_19')
def previewPolicyListById_19(**kwargs):
    return CatalystClient().previewPolicyListById_19(**kwargs)

@register('getListsById_19')
def getListsById_19(**kwargs):
    return CatalystClient().getListsById_19(**kwargs)

@register('getPolicyLists_18')
def getPolicyLists_18(**kwargs):
    return CatalystClient().getPolicyLists_18(**kwargs)

@register('getPolicyListsWithInfoTag_20')
def getPolicyListsWithInfoTag_20(**kwargs):
    return CatalystClient().getPolicyListsWithInfoTag_20(**kwargs)

@register('previewPolicyListById_20')
def previewPolicyListById_20(**kwargs):
    return CatalystClient().previewPolicyListById_20(**kwargs)

@register('getListsById_20')
def getListsById_20(**kwargs):
    return CatalystClient().getListsById_20(**kwargs)

@register('getPolicyLists_19')
def getPolicyLists_19(**kwargs):
    return CatalystClient().getPolicyLists_19(**kwargs)

@register('getPolicyListsWithInfoTag_22')
def getPolicyListsWithInfoTag_22(**kwargs):
    return CatalystClient().getPolicyListsWithInfoTag_22(**kwargs)

@register('previewPolicyListById_22')
def previewPolicyListById_22(**kwargs):
    return CatalystClient().previewPolicyListById_22(**kwargs)

@register('getListsById_22')
def getListsById_22(**kwargs):
    return CatalystClient().getListsById_22(**kwargs)

@register('getPolicyLists_20')
def getPolicyLists_20(**kwargs):
    return CatalystClient().getPolicyLists_20(**kwargs)

@register('getPolicyListsWithInfoTag_23')
def getPolicyListsWithInfoTag_23(**kwargs):
    return CatalystClient().getPolicyListsWithInfoTag_23(**kwargs)

@register('previewPolicyListById_23')
def previewPolicyListById_23(**kwargs):
    return CatalystClient().previewPolicyListById_23(**kwargs)

@register('getListsById_23')
def getListsById_23(**kwargs):
    return CatalystClient().getListsById_23(**kwargs)

@register('getPolicyLists')
def getPolicyLists(**kwargs):
    return CatalystClient().getPolicyLists(**kwargs)

@register('getPolicyListsWithInfoTag')
def getPolicyListsWithInfoTag(**kwargs):
    return CatalystClient().getPolicyListsWithInfoTag(**kwargs)

@register('previewPolicyListById')
def previewPolicyListById(**kwargs):
    return CatalystClient().previewPolicyListById(**kwargs)

@register('getListsById')
def getListsById(**kwargs):
    return CatalystClient().getListsById(**kwargs)

@register('getPolicyLists_21')
def getPolicyLists_21(**kwargs):
    return CatalystClient().getPolicyLists_21(**kwargs)

@register('getPolicyListsWithInfoTag_24')
def getPolicyListsWithInfoTag_24(**kwargs):
    return CatalystClient().getPolicyListsWithInfoTag_24(**kwargs)

@register('previewPolicyListById_24')
def previewPolicyListById_24(**kwargs):
    return CatalystClient().previewPolicyListById_24(**kwargs)

@register('getListsById_24')
def getListsById_24(**kwargs):
    return CatalystClient().getListsById_24(**kwargs)

@register('getPolicyLists_22')
def getPolicyLists_22(**kwargs):
    return CatalystClient().getPolicyLists_22(**kwargs)

@register('getPolicyListsWithInfoTag_25')
def getPolicyListsWithInfoTag_25(**kwargs):
    return CatalystClient().getPolicyListsWithInfoTag_25(**kwargs)

@register('previewPolicyListById_25')
def previewPolicyListById_25(**kwargs):
    return CatalystClient().previewPolicyListById_25(**kwargs)

@register('getListsById_25')
def getListsById_25(**kwargs):
    return CatalystClient().getListsById_25(**kwargs)

@register('getPolicyLists_23')
def getPolicyLists_23(**kwargs):
    return CatalystClient().getPolicyLists_23(**kwargs)

@register('getPolicyListsWithInfoTag_26')
def getPolicyListsWithInfoTag_26(**kwargs):
    return CatalystClient().getPolicyListsWithInfoTag_26(**kwargs)

@register('previewPolicyListById_26')
def previewPolicyListById_26(**kwargs):
    return CatalystClient().previewPolicyListById_26(**kwargs)

@register('getListsById_26')
def getListsById_26(**kwargs):
    return CatalystClient().getListsById_26(**kwargs)

@register('getPolicyLists_24')
def getPolicyLists_24(**kwargs):
    return CatalystClient().getPolicyLists_24(**kwargs)

@register('getPolicyListsWithInfoTag_27')
def getPolicyListsWithInfoTag_27(**kwargs):
    return CatalystClient().getPolicyListsWithInfoTag_27(**kwargs)

@register('previewPolicyListById_27')
def previewPolicyListById_27(**kwargs):
    return CatalystClient().previewPolicyListById_27(**kwargs)

@register('getListsById_27')
def getListsById_27(**kwargs):
    return CatalystClient().getListsById_27(**kwargs)

@register('getPolicyLists_25')
def getPolicyLists_25(**kwargs):
    return CatalystClient().getPolicyLists_25(**kwargs)

@register('getPolicyListsWithInfoTag_28')
def getPolicyListsWithInfoTag_28(**kwargs):
    return CatalystClient().getPolicyListsWithInfoTag_28(**kwargs)

@register('previewPolicyListById_28')
def previewPolicyListById_28(**kwargs):
    return CatalystClient().previewPolicyListById_28(**kwargs)

@register('getListsById_28')
def getListsById_28(**kwargs):
    return CatalystClient().getListsById_28(**kwargs)

@register('getPolicyLists_26')
def getPolicyLists_26(**kwargs):
    return CatalystClient().getPolicyLists_26(**kwargs)

@register('getPolicyListsWithInfoTag_29')
def getPolicyListsWithInfoTag_29(**kwargs):
    return CatalystClient().getPolicyListsWithInfoTag_29(**kwargs)

@register('previewPolicyListById_29')
def previewPolicyListById_29(**kwargs):
    return CatalystClient().previewPolicyListById_29(**kwargs)

@register('getListsById_29')
def getListsById_29(**kwargs):
    return CatalystClient().getListsById_29(**kwargs)

@register('getPolicyLists_27')
def getPolicyLists_27(**kwargs):
    return CatalystClient().getPolicyLists_27(**kwargs)

@register('getPolicyListsWithInfoTag_30')
def getPolicyListsWithInfoTag_30(**kwargs):
    return CatalystClient().getPolicyListsWithInfoTag_30(**kwargs)

@register('previewPolicyListById_30')
def previewPolicyListById_30(**kwargs):
    return CatalystClient().previewPolicyListById_30(**kwargs)

@register('getListsById_30')
def getListsById_30(**kwargs):
    return CatalystClient().getListsById_30(**kwargs)

@register('getPolicyLists_28')
def getPolicyLists_28(**kwargs):
    return CatalystClient().getPolicyLists_28(**kwargs)

@register('getPolicyListsWithInfoTag_31')
def getPolicyListsWithInfoTag_31(**kwargs):
    return CatalystClient().getPolicyListsWithInfoTag_31(**kwargs)

@register('previewPolicyListById_31')
def previewPolicyListById_31(**kwargs):
    return CatalystClient().previewPolicyListById_31(**kwargs)

@register('getListsById_31')
def getListsById_31(**kwargs):
    return CatalystClient().getListsById_31(**kwargs)

@register('getPolicyLists_29')
def getPolicyLists_29(**kwargs):
    return CatalystClient().getPolicyLists_29(**kwargs)

@register('getPolicyListsWithInfoTag_32')
def getPolicyListsWithInfoTag_32(**kwargs):
    return CatalystClient().getPolicyListsWithInfoTag_32(**kwargs)

@register('previewPolicyListById_32')
def previewPolicyListById_32(**kwargs):
    return CatalystClient().previewPolicyListById_32(**kwargs)

@register('getListsById_32')
def getListsById_32(**kwargs):
    return CatalystClient().getListsById_32(**kwargs)

@register('getPolicyLists_30')
def getPolicyLists_30(**kwargs):
    return CatalystClient().getPolicyLists_30(**kwargs)

@register('getPolicyListsWithInfoTag_33')
def getPolicyListsWithInfoTag_33(**kwargs):
    return CatalystClient().getPolicyListsWithInfoTag_33(**kwargs)

@register('previewPolicyListById_33')
def previewPolicyListById_33(**kwargs):
    return CatalystClient().previewPolicyListById_33(**kwargs)

@register('getListsById_33')
def getListsById_33(**kwargs):
    return CatalystClient().getListsById_33(**kwargs)

@register('getPolicyLists_31')
def getPolicyLists_31(**kwargs):
    return CatalystClient().getPolicyLists_31(**kwargs)

@register('getPolicyListsWithInfoTag_34')
def getPolicyListsWithInfoTag_34(**kwargs):
    return CatalystClient().getPolicyListsWithInfoTag_34(**kwargs)

@register('previewPolicyListById_34')
def previewPolicyListById_34(**kwargs):
    return CatalystClient().previewPolicyListById_34(**kwargs)

@register('getListsById_34')
def getListsById_34(**kwargs):
    return CatalystClient().getListsById_34(**kwargs)

@register('getPolicyLists_32')
def getPolicyLists_32(**kwargs):
    return CatalystClient().getPolicyLists_32(**kwargs)

@register('getPolicyListsWithInfoTag_35')
def getPolicyListsWithInfoTag_35(**kwargs):
    return CatalystClient().getPolicyListsWithInfoTag_35(**kwargs)

@register('previewPolicyListById_35')
def previewPolicyListById_35(**kwargs):
    return CatalystClient().previewPolicyListById_35(**kwargs)

@register('getListsById_35')
def getListsById_35(**kwargs):
    return CatalystClient().getListsById_35(**kwargs)

@register('getPolicyLists_33')
def getPolicyLists_33(**kwargs):
    return CatalystClient().getPolicyLists_33(**kwargs)

@register('getPolicyListsWithInfoTag_36')
def getPolicyListsWithInfoTag_36(**kwargs):
    return CatalystClient().getPolicyListsWithInfoTag_36(**kwargs)

@register('previewPolicyListById_36')
def previewPolicyListById_36(**kwargs):
    return CatalystClient().previewPolicyListById_36(**kwargs)

@register('getListsById_36')
def getListsById_36(**kwargs):
    return CatalystClient().getListsById_36(**kwargs)

@register('getPolicyLists_34')
def getPolicyLists_34(**kwargs):
    return CatalystClient().getPolicyLists_34(**kwargs)

@register('getPolicyListsWithInfoTag_37')
def getPolicyListsWithInfoTag_37(**kwargs):
    return CatalystClient().getPolicyListsWithInfoTag_37(**kwargs)

@register('previewPolicyListById_37')
def previewPolicyListById_37(**kwargs):
    return CatalystClient().previewPolicyListById_37(**kwargs)

@register('getListsById_37')
def getListsById_37(**kwargs):
    return CatalystClient().getListsById_37(**kwargs)

@register('getPolicyLists_1')
def getPolicyLists_1(**kwargs):
    return CatalystClient().getPolicyLists_1(**kwargs)

@register('getPolicyListsWithInfoTag_1')
def getPolicyListsWithInfoTag_1(**kwargs):
    return CatalystClient().getPolicyListsWithInfoTag_1(**kwargs)

@register('previewPolicyListById_1')
def previewPolicyListById_1(**kwargs):
    return CatalystClient().previewPolicyListById_1(**kwargs)

@register('getListsById_1')
def getListsById_1(**kwargs):
    return CatalystClient().getListsById_1(**kwargs)

@register('getPolicyLists_2')
def getPolicyLists_2(**kwargs):
    return CatalystClient().getPolicyLists_2(**kwargs)

@register('getPolicyListsWithInfoTag_2')
def getPolicyListsWithInfoTag_2(**kwargs):
    return CatalystClient().getPolicyListsWithInfoTag_2(**kwargs)

@register('previewPolicyListById_2')
def previewPolicyListById_2(**kwargs):
    return CatalystClient().previewPolicyListById_2(**kwargs)

@register('getListsById_2')
def getListsById_2(**kwargs):
    return CatalystClient().getListsById_2(**kwargs)

@register('getPolicyLists_35')
def getPolicyLists_35(**kwargs):
    return CatalystClient().getPolicyLists_35(**kwargs)

@register('getPolicyListsWithInfoTag_38')
def getPolicyListsWithInfoTag_38(**kwargs):
    return CatalystClient().getPolicyListsWithInfoTag_38(**kwargs)

@register('previewPolicyListById_38')
def previewPolicyListById_38(**kwargs):
    return CatalystClient().previewPolicyListById_38(**kwargs)

@register('getListsById_38')
def getListsById_38(**kwargs):
    return CatalystClient().getListsById_38(**kwargs)

@register('getPolicyLists_36')
def getPolicyLists_36(**kwargs):
    return CatalystClient().getPolicyLists_36(**kwargs)

@register('getPolicyListsWithInfoTag_39')
def getPolicyListsWithInfoTag_39(**kwargs):
    return CatalystClient().getPolicyListsWithInfoTag_39(**kwargs)

@register('previewPolicyListById_39')
def previewPolicyListById_39(**kwargs):
    return CatalystClient().previewPolicyListById_39(**kwargs)

@register('getListsById_39')
def getListsById_39(**kwargs):
    return CatalystClient().getListsById_39(**kwargs)

@register('getPolicyLists_37')
def getPolicyLists_37(**kwargs):
    return CatalystClient().getPolicyLists_37(**kwargs)

@register('getPolicyListsWithInfoTag_40')
def getPolicyListsWithInfoTag_40(**kwargs):
    return CatalystClient().getPolicyListsWithInfoTag_40(**kwargs)

@register('previewPolicyListById_40')
def previewPolicyListById_40(**kwargs):
    return CatalystClient().previewPolicyListById_40(**kwargs)

@register('getListsById_40')
def getListsById_40(**kwargs):
    return CatalystClient().getListsById_40(**kwargs)

@register('getPolicyLists_38')
def getPolicyLists_38(**kwargs):
    return CatalystClient().getPolicyLists_38(**kwargs)

@register('getPolicyListsWithInfoTag_41')
def getPolicyListsWithInfoTag_41(**kwargs):
    return CatalystClient().getPolicyListsWithInfoTag_41(**kwargs)

@register('previewPolicyListById_41')
def previewPolicyListById_41(**kwargs):
    return CatalystClient().previewPolicyListById_41(**kwargs)

@register('getListsById_41')
def getListsById_41(**kwargs):
    return CatalystClient().getListsById_41(**kwargs)

@register('getPolicyLists_39')
def getPolicyLists_39(**kwargs):
    return CatalystClient().getPolicyLists_39(**kwargs)

@register('getPolicyListsWithInfoTag_42')
def getPolicyListsWithInfoTag_42(**kwargs):
    return CatalystClient().getPolicyListsWithInfoTag_42(**kwargs)

@register('previewPolicyListById_42')
def previewPolicyListById_42(**kwargs):
    return CatalystClient().previewPolicyListById_42(**kwargs)

@register('getListsById_42')
def getListsById_42(**kwargs):
    return CatalystClient().getListsById_42(**kwargs)

@register('getPolicyLists_40')
def getPolicyLists_40(**kwargs):
    return CatalystClient().getPolicyLists_40(**kwargs)

@register('getPolicyListsWithInfoTag_43')
def getPolicyListsWithInfoTag_43(**kwargs):
    return CatalystClient().getPolicyListsWithInfoTag_43(**kwargs)

@register('previewPolicyListById_43')
def previewPolicyListById_43(**kwargs):
    return CatalystClient().previewPolicyListById_43(**kwargs)

@register('getListsById_43')
def getListsById_43(**kwargs):
    return CatalystClient().getListsById_43(**kwargs)

@register('generateSecurityTemplateList')
def generateSecurityTemplateList(**kwargs):
    return CatalystClient().generateSecurityTemplateList(**kwargs)

@register('getSecurityTemplate')
def getSecurityTemplate(**kwargs):
    return CatalystClient().getSecurityTemplate(**kwargs)

@register('getSecurityPolicyDeviceList_1')
def getSecurityPolicyDeviceList_1(**kwargs):
    return CatalystClient().getSecurityPolicyDeviceList_1(**kwargs)

@register('getDeviceListById')
def getDeviceListById(**kwargs):
    return CatalystClient().getDeviceListById(**kwargs)

@register('generateSecurityPolicySummary')
def generateSecurityPolicySummary(**kwargs):
    return CatalystClient().generateSecurityPolicySummary(**kwargs)

@register('getSecurityTemplatesForDevice')
def getSecurityTemplatesForDevice(**kwargs):
    return CatalystClient().getSecurityTemplatesForDevice(**kwargs)

@register('generatePolicyTemplateList')
def generatePolicyTemplateList(**kwargs):
    return CatalystClient().generatePolicyTemplateList(**kwargs)

@register('getVEdgeTemplate')
def getVEdgeTemplate(**kwargs):
    return CatalystClient().getVEdgeTemplate(**kwargs)

@register('getVEdgePolicyDeviceList')
def getVEdgePolicyDeviceList(**kwargs):
    return CatalystClient().getVEdgePolicyDeviceList(**kwargs)

@register('getDeviceListByPolicy')
def getDeviceListByPolicy(**kwargs):
    return CatalystClient().getDeviceListByPolicy(**kwargs)

@register('generateVoiceTemplateList')
def generateVoiceTemplateList(**kwargs):
    return CatalystClient().generateVoiceTemplateList(**kwargs)

@register('getTemplateById')
def getTemplateById(**kwargs):
    return CatalystClient().getTemplateById(**kwargs)

@register('getVoicePolicyDeviceList')
def getVoicePolicyDeviceList(**kwargs):
    return CatalystClient().getVoicePolicyDeviceList(**kwargs)

@register('getDeviceListByPolicyId')
def getDeviceListByPolicyId(**kwargs):
    return CatalystClient().getDeviceListByPolicyId(**kwargs)

@register('generateVoicePolicySummary')
def generateVoicePolicySummary(**kwargs):
    return CatalystClient().generateVoicePolicySummary(**kwargs)

@register('getVoiceTemplatesForDevice')
def getVoiceTemplatesForDevice(**kwargs):
    return CatalystClient().getVoiceTemplatesForDevice(**kwargs)

@register('generateVSmartPolicyTemplateList')
def generateVSmartPolicyTemplateList(**kwargs):
    return CatalystClient().generateVSmartPolicyTemplateList(**kwargs)

@register('checkVSmartConnectivityStatus')
def checkVSmartConnectivityStatus(**kwargs):
    return CatalystClient().checkVSmartConnectivityStatus(**kwargs)

@register('getTemplateByPolicyId')
def getTemplateByPolicyId(**kwargs):
    return CatalystClient().getTemplateByPolicyId(**kwargs)

@register('QosmosNbarMigrationWarning')
def QosmosNbarMigrationWarning(**kwargs):
    return CatalystClient().QosmosNbarMigrationWarning(**kwargs)

@register('getAllTenants')
def getAllTenants(**kwargs):
    return CatalystClient().getAllTenants(**kwargs)

@register('getTenantvSmartMapping')
def getTenantvSmartMapping(**kwargs):
    return CatalystClient().getTenantvSmartMapping(**kwargs)

@register('getTenantHostingCapacityOnvSmarts')
def getTenantHostingCapacityOnvSmarts(**kwargs):
    return CatalystClient().getTenantHostingCapacityOnvSmarts(**kwargs)

@register('getTenant')
def getTenant(**kwargs):
    return CatalystClient().getTenant(**kwargs)

@register('downloadExistingBackupFile')
def downloadExistingBackupFile(**kwargs):
    return CatalystClient().downloadExistingBackupFile(**kwargs)

@register('exportTenantBackup')
def exportTenantBackup(**kwargs):
    return CatalystClient().exportTenantBackup(**kwargs)

@register('listTenantBackup')
def listTenantBackup(**kwargs):
    return CatalystClient().listTenantBackup(**kwargs)

@register('downloadTenantData')
def downloadTenantData(**kwargs):
    return CatalystClient().downloadTenantData(**kwargs)

@register('getMigrationToken')
def getMigrationToken(**kwargs):
    return CatalystClient().getMigrationToken(**kwargs)

@register('reTriggerNetworkMigration')
def reTriggerNetworkMigration(**kwargs):
    return CatalystClient().reTriggerNetworkMigration(**kwargs)

@register('getAllTenantStatuses')
def getAllTenantStatuses(**kwargs):
    return CatalystClient().getAllTenantStatuses(**kwargs)

@register('createFullTopology')
def createFullTopology(**kwargs):
    return CatalystClient().createFullTopology(**kwargs)

@register('createDeviceTopology')
def createDeviceTopology(**kwargs):
    return CatalystClient().createDeviceTopology(**kwargs)

@register('getSiteTopology')
def getSiteTopology(**kwargs):
    return CatalystClient().getSiteTopology(**kwargs)

@register('getSiteTopologyMonitorData')
def getSiteTopologyMonitorData(**kwargs):
    return CatalystClient().getSiteTopologyMonitorData(**kwargs)

@register('createPhysicalTopology')
def createPhysicalTopology(**kwargs):
    return CatalystClient().createPhysicalTopology(**kwargs)

@register('getControlConnections')
def getControlConnections(**kwargs):
    return CatalystClient().getControlConnections(**kwargs)

@register('getDeviceConfiguration')
def getDeviceConfiguration(**kwargs):
    return CatalystClient().getDeviceConfiguration(**kwargs)

@register('getAllKeysFromUmbrella')
def getAllKeysFromUmbrella(**kwargs):
    return CatalystClient().getAllKeysFromUmbrella(**kwargs)

@register('getManagementKeysFromUmbrella')
def getManagementKeysFromUmbrella(**kwargs):
    return CatalystClient().getManagementKeysFromUmbrella(**kwargs)

@register('getNetworkKeysFromUmbrella')
def getNetworkKeysFromUmbrella(**kwargs):
    return CatalystClient().getNetworkKeysFromUmbrella(**kwargs)

@register('getReportingKeysFromUmbrella')
def getReportingKeysFromUmbrella(**kwargs):
    return CatalystClient().getReportingKeysFromUmbrella(**kwargs)

@register('sendMetaDataToUmbrella')
def sendMetaDataToUmbrella(**kwargs):
    return CatalystClient().sendMetaDataToUmbrella(**kwargs)

@register('getStatus')
def getStatus(**kwargs):
    return CatalystClient().getStatus(**kwargs)

@register('getUrlMonitor')
def getUrlMonitor(**kwargs):
    return CatalystClient().getUrlMonitor(**kwargs)

@register('returnMetric')
def returnMetric(**kwargs):
    return CatalystClient().returnMetric(**kwargs)

@register('returnMetricFiles')
def returnMetricFiles(**kwargs):
    return CatalystClient().returnMetricFiles(**kwargs)

@register('getMetricsList')
def getMetricsList(**kwargs):
    return CatalystClient().getMetricsList(**kwargs)

@register('getDBSizeOnFile')
def getDBSizeOnFile(**kwargs):
    return CatalystClient().getDBSizeOnFile(**kwargs)

@register('listLogFileDetails')
def listLogFileDetails(**kwargs):
    return CatalystClient().listLogFileDetails(**kwargs)

@register('listVManageServerLogLastNLines')
def listVManageServerLogLastNLines(**kwargs):
    return CatalystClient().listVManageServerLogLastNLines(**kwargs)

@register('listConfigurations')
def listConfigurations(**kwargs):
    return CatalystClient().listConfigurations(**kwargs)

@register('listLoggers')
def listLoggers(**kwargs):
    return CatalystClient().listLoggers(**kwargs)

@register('getStatsMigrationRangeConfig')
def getStatsMigrationRangeConfig(**kwargs):
    return CatalystClient().getStatsMigrationRangeConfig(**kwargs)

@register('getStatsMigrationSettings')
def getStatsMigrationSettings(**kwargs):
    return CatalystClient().getStatsMigrationSettings(**kwargs)

@register('getStatsMigrationStatsDbInfo')
def getStatsMigrationStatsDbInfo(**kwargs):
    return CatalystClient().getStatsMigrationStatsDbInfo(**kwargs)

@register('getStatsMigrationStatus')
def getStatsMigrationStatus(**kwargs):
    return CatalystClient().getStatsMigrationStatus(**kwargs)

@register('getCloudOnRampSaasStatus')
def getCloudOnRampSaasStatus(**kwargs):
    return CatalystClient().getCloudOnRampSaasStatus(**kwargs)

@register('getCloudTunnelList')
def getCloudTunnelList(**kwargs):
    return CatalystClient().getCloudTunnelList(**kwargs)

@register('getPolicyGroupsWithCorSaasApps')
def getPolicyGroupsWithCorSaasApps(**kwargs):
    return CatalystClient().getPolicyGroupsWithCorSaasApps(**kwargs)

@register('getCorSitesPerDevice')
def getCorSitesPerDevice(**kwargs):
    return CatalystClient().getCorSitesPerDevice(**kwargs)

@register('getInactiveCorSaasSites')
def getInactiveCorSaasSites(**kwargs):
    return CatalystClient().getInactiveCorSaasSites(**kwargs)

@register('getLegacyDeviceList')
def getLegacyDeviceList(**kwargs):
    return CatalystClient().getLegacyDeviceList(**kwargs)

@register('getCorSaasStatusPerDevice')
def getCorSaasStatusPerDevice(**kwargs):
    return CatalystClient().getCorSaasStatusPerDevice(**kwargs)

@register('getWebexSyncStatus')
def getWebexSyncStatus(**kwargs):
    return CatalystClient().getWebexSyncStatus(**kwargs)

@register('GetConfigGroupBySolution')
def GetConfigGroupBySolution(**kwargs):
    return CatalystClient().GetConfigGroupBySolution(**kwargs)

@register('GetConfigGroup')
def GetConfigGroup(**kwargs):
    return CatalystClient().GetConfigGroup(**kwargs)

@register('GetConfigGroupAssociation')
def GetConfigGroupAssociation(**kwargs):
    return CatalystClient().GetConfigGroupAssociation(**kwargs)

@register('getConfigGroupDeviceVariables')
def getConfigGroupDeviceVariables(**kwargs):
    return CatalystClient().getConfigGroupDeviceVariables(**kwargs)

@register('getConfigGroupDeviceVariablesSchema')
def getConfigGroupDeviceVariablesSchema(**kwargs):
    return CatalystClient().getConfigGroupDeviceVariablesSchema(**kwargs)

@register('getRuleAssociationByConfigGroupId')
def getRuleAssociationByConfigGroupId(**kwargs):
    return CatalystClient().getRuleAssociationByConfigGroupId(**kwargs)

@register('getRunningIosCliConfig')
def getRunningIosCliConfig(**kwargs):
    return CatalystClient().getRunningIosCliConfig(**kwargs)

@register('getUnsupportedCliConfig')
def getUnsupportedCliConfig(**kwargs):
    return CatalystClient().getUnsupportedCliConfig(**kwargs)

@register('GetMobilityCliFeatureProfile')
def GetMobilityCliFeatureProfile(**kwargs):
    return CatalystClient().GetMobilityCliFeatureProfile(**kwargs)

@register('GetMobilityCliFeatureProfileByCliId')
def GetMobilityCliFeatureProfileByCliId(**kwargs):
    return CatalystClient().GetMobilityCliFeatureProfileByCliId(**kwargs)

@register('GetAllConfigFeatureForMobility')
def GetAllConfigFeatureForMobility(**kwargs):
    return CatalystClient().GetAllConfigFeatureForMobility(**kwargs)

@register('GetConfigFeatureForMobilityByParcelId')
def GetConfigFeatureForMobilityByParcelId(**kwargs):
    return CatalystClient().GetConfigFeatureForMobilityByParcelId(**kwargs)

@register('GetMobilityGlobalFeatureProfile')
def GetMobilityGlobalFeatureProfile(**kwargs):
    return CatalystClient().GetMobilityGlobalFeatureProfile(**kwargs)

@register('GetMobilityGlobalBasicParcelSchemaBySchemaType')
def GetMobilityGlobalBasicParcelSchemaBySchemaType(**kwargs):
    return CatalystClient().GetMobilityGlobalBasicParcelSchemaBySchemaType(**kwargs)

@register('GetMobilityFeatureProfileByGlobalId')
def GetMobilityFeatureProfileByGlobalId(**kwargs):
    return CatalystClient().GetMobilityFeatureProfileByGlobalId(**kwargs)

@register('GetQosFeatureForGlobal')
def GetQosFeatureForGlobal(**kwargs):
    return CatalystClient().GetQosFeatureForGlobal(**kwargs)

@register('GetQosFeatureByParcelIdForGlobal')
def GetQosFeatureByParcelIdForGlobal(**kwargs):
    return CatalystClient().GetQosFeatureByParcelIdForGlobal(**kwargs)

@register('GetAaaServersProfileParcelForMobility')
def GetAaaServersProfileParcelForMobility(**kwargs):
    return CatalystClient().GetAaaServersProfileParcelForMobility(**kwargs)

@register('GetAaaServersProfileParcelByParcelIdForMobility')
def GetAaaServersProfileParcelByParcelIdForMobility(**kwargs):
    return CatalystClient().GetAaaServersProfileParcelByParcelIdForMobility(**kwargs)

@register('GetBasicProfileParcelForMobility')
def GetBasicProfileParcelForMobility(**kwargs):
    return CatalystClient().GetBasicProfileParcelForMobility(**kwargs)

@register('GetBasicProfileParcelByParcelIdForMobility')
def GetBasicProfileParcelByParcelIdForMobility(**kwargs):
    return CatalystClient().GetBasicProfileParcelByParcelIdForMobility(**kwargs)

@register('GetCellularProfileParcelListForMobility')
def GetCellularProfileParcelListForMobility(**kwargs):
    return CatalystClient().GetCellularProfileParcelListForMobility(**kwargs)

@register('GetCellularProfileParcelForMobility')
def GetCellularProfileParcelForMobility(**kwargs):
    return CatalystClient().GetCellularProfileParcelForMobility(**kwargs)

@register('GetEsimCellularProfileFeatureForMobility')
def GetEsimCellularProfileFeatureForMobility(**kwargs):
    return CatalystClient().GetEsimCellularProfileFeatureForMobility(**kwargs)

@register('GetEsimCellularProfileFeatureByEsimCellularIdForMobility')
def GetEsimCellularProfileFeatureByEsimCellularIdForMobility(**kwargs):
    return CatalystClient().GetEsimCellularProfileFeatureByEsimCellularIdForMobility(**kwargs)

@register('GetEthernetProfileParcels')
def GetEthernetProfileParcels(**kwargs):
    return CatalystClient().GetEthernetProfileParcels(**kwargs)

@register('GetEthernetProfileParcel')
def GetEthernetProfileParcel(**kwargs):
    return CatalystClient().GetEthernetProfileParcel(**kwargs)

@register('GetLoggingProfileFeatureForMobility')
def GetLoggingProfileFeatureForMobility(**kwargs):
    return CatalystClient().GetLoggingProfileFeatureForMobility(**kwargs)

@register('GetLoggingProfileFeatureByFeatureIdForMobility')
def GetLoggingProfileFeatureByFeatureIdForMobility(**kwargs):
    return CatalystClient().GetLoggingProfileFeatureByFeatureIdForMobility(**kwargs)

@register('GetNetworkProtocolProfileParcelListForMobility')
def GetNetworkProtocolProfileParcelListForMobility(**kwargs):
    return CatalystClient().GetNetworkProtocolProfileParcelListForMobility(**kwargs)

@register('GetNetworkProtocolProfileParcelForMobility')
def GetNetworkProtocolProfileParcelForMobility(**kwargs):
    return CatalystClient().GetNetworkProtocolProfileParcelForMobility(**kwargs)

@register('GetSecurityPolicyProfileParcelListForMobility')
def GetSecurityPolicyProfileParcelListForMobility(**kwargs):
    return CatalystClient().GetSecurityPolicyProfileParcelListForMobility(**kwargs)

@register('GetSecurityPolicyProfileParcelForMobility')
def GetSecurityPolicyProfileParcelForMobility(**kwargs):
    return CatalystClient().GetSecurityPolicyProfileParcelForMobility(**kwargs)

@register('GetVpnProfileParcelForMobility')
def GetVpnProfileParcelForMobility(**kwargs):
    return CatalystClient().GetVpnProfileParcelForMobility(**kwargs)

@register('GetVpnProfileParcelByParcelIdForMobility')
def GetVpnProfileParcelByParcelIdForMobility(**kwargs):
    return CatalystClient().GetVpnProfileParcelByParcelIdForMobility(**kwargs)

@register('GetWifiProfileParcelListForMobility')
def GetWifiProfileParcelListForMobility(**kwargs):
    return CatalystClient().GetWifiProfileParcelListForMobility(**kwargs)

@register('GetWifiProfileParcelForMobility')
def GetWifiProfileParcelForMobility(**kwargs):
    return CatalystClient().GetWifiProfileParcelForMobility(**kwargs)

@register('GetAllNfvirtualCLIFeatureProfiles')
def GetAllNfvirtualCLIFeatureProfiles(**kwargs):
    return CatalystClient().GetAllNfvirtualCLIFeatureProfiles(**kwargs)

@register('GetNfvirtualCLIFeatureProfileByid')
def GetNfvirtualCLIFeatureProfileByid(**kwargs):
    return CatalystClient().GetNfvirtualCLIFeatureProfileByid(**kwargs)

@register('getNfvirtualCLIParcel')
def getNfvirtualCLIParcel(**kwargs):
    return CatalystClient().getNfvirtualCLIParcel(**kwargs)

@register('GetAllNfvirtualNetworksFeatureProfiles')
def GetAllNfvirtualNetworksFeatureProfiles(**kwargs):
    return CatalystClient().GetAllNfvirtualNetworksFeatureProfiles(**kwargs)

@register('GetAllNfvirtualOvsNetworksFeatureProfileByProfileId')
def GetAllNfvirtualOvsNetworksFeatureProfileByProfileId(**kwargs):
    return CatalystClient().GetAllNfvirtualOvsNetworksFeatureProfileByProfileId(**kwargs)

@register('GetNfvirtualNetworksFeatureProfileByProfileId')
def GetNfvirtualNetworksFeatureProfileByProfileId(**kwargs):
    return CatalystClient().GetNfvirtualNetworksFeatureProfileByProfileId(**kwargs)

@register('GetNfvirtualLANParcel')
def GetNfvirtualLANParcel(**kwargs):
    return CatalystClient().GetNfvirtualLANParcel(**kwargs)

@register('GetNfvirtualOVSNetworkParcel')
def GetNfvirtualOVSNetworkParcel(**kwargs):
    return CatalystClient().GetNfvirtualOVSNetworkParcel(**kwargs)

@register('GetNfvirtualRoutesParcel')
def GetNfvirtualRoutesParcel(**kwargs):
    return CatalystClient().GetNfvirtualRoutesParcel(**kwargs)

@register('GetNfvirtualSwitchParcel')
def GetNfvirtualSwitchParcel(**kwargs):
    return CatalystClient().GetNfvirtualSwitchParcel(**kwargs)

@register('GetNfvirtualVNFAttributesParcel')
def GetNfvirtualVNFAttributesParcel(**kwargs):
    return CatalystClient().GetNfvirtualVNFAttributesParcel(**kwargs)

@register('GetNfvirtualVNFParcel')
def GetNfvirtualVNFParcel(**kwargs):
    return CatalystClient().GetNfvirtualVNFParcel(**kwargs)

@register('GetNfvirtualWANParcel')
def GetNfvirtualWANParcel(**kwargs):
    return CatalystClient().GetNfvirtualWANParcel(**kwargs)

@register('GetAllNfvirtualSystemFeatureProfiles')
def GetAllNfvirtualSystemFeatureProfiles(**kwargs):
    return CatalystClient().GetAllNfvirtualSystemFeatureProfiles(**kwargs)

@register('GetNfvirtualSystemFeatureProfileByProfileId')
def GetNfvirtualSystemFeatureProfileByProfileId(**kwargs):
    return CatalystClient().GetNfvirtualSystemFeatureProfileByProfileId(**kwargs)

@register('GetNfvirtualAAAParcel')
def GetNfvirtualAAAParcel(**kwargs):
    return CatalystClient().GetNfvirtualAAAParcel(**kwargs)

@register('GetNfvirtualBannerParcel')
def GetNfvirtualBannerParcel(**kwargs):
    return CatalystClient().GetNfvirtualBannerParcel(**kwargs)

@register('GetNfvirtualLoggingParcel')
def GetNfvirtualLoggingParcel(**kwargs):
    return CatalystClient().GetNfvirtualLoggingParcel(**kwargs)

@register('GetNfvirtualNTPParcel')
def GetNfvirtualNTPParcel(**kwargs):
    return CatalystClient().GetNfvirtualNTPParcel(**kwargs)

@register('GetNfvirtualSNMPParcel')
def GetNfvirtualSNMPParcel(**kwargs):
    return CatalystClient().GetNfvirtualSNMPParcel(**kwargs)

@register('GetNfvirtualSystemSettingsParcel')
def GetNfvirtualSystemSettingsParcel(**kwargs):
    return CatalystClient().GetNfvirtualSystemSettingsParcel(**kwargs)

@register('GetSdroutingFeatureProfiles')
def GetSdroutingFeatureProfiles(**kwargs):
    return CatalystClient().GetSdroutingFeatureProfiles(**kwargs)

@register('GetSdroutingCliFeatureProfiles')
def GetSdroutingCliFeatureProfiles(**kwargs):
    return CatalystClient().GetSdroutingCliFeatureProfiles(**kwargs)

@register('Get')
def Get(**kwargs):
    return CatalystClient().Get(**kwargs)

@register('GetSdroutingCliFeatureProfile')
def GetSdroutingCliFeatureProfile(**kwargs):
    return CatalystClient().GetSdroutingCliFeatureProfile(**kwargs)

@register('GetSdroutingCLIAddOnFeatures')
def GetSdroutingCLIAddOnFeatures(**kwargs):
    return CatalystClient().GetSdroutingCLIAddOnFeatures(**kwargs)

@register('GetSdroutingCLIAddOnFeature')
def GetSdroutingCLIAddOnFeature(**kwargs):
    return CatalystClient().GetSdroutingCLIAddOnFeature(**kwargs)

@register('GetSdroutingCliConfigGroupFeatures')
def GetSdroutingCliConfigGroupFeatures(**kwargs):
    return CatalystClient().GetSdroutingCliConfigGroupFeatures(**kwargs)

@register('GetSdroutingCliConfigGroupFeature')
def GetSdroutingCliConfigGroupFeature(**kwargs):
    return CatalystClient().GetSdroutingCliConfigGroupFeature(**kwargs)

@register('GetSdroutingIosCLassicCLIAddOnFeatures')
def GetSdroutingIosCLassicCLIAddOnFeatures(**kwargs):
    return CatalystClient().GetSdroutingIosCLassicCLIAddOnFeatures(**kwargs)

@register('GetSdroutingIosClassicCLIAddOnFeature')
def GetSdroutingIosClassicCLIAddOnFeature(**kwargs):
    return CatalystClient().GetSdroutingIosClassicCLIAddOnFeature(**kwargs)

@register('GetSdRoutingEmbeddedSecurityFeatureProfiles')
def GetSdRoutingEmbeddedSecurityFeatureProfiles(**kwargs):
    return CatalystClient().GetSdRoutingEmbeddedSecurityFeatureProfiles(**kwargs)

@register('GetSdRoutingEmbeddedSecurityFeatureProfileByProfileId')
def GetSdRoutingEmbeddedSecurityFeatureProfileByProfileId(**kwargs):
    return CatalystClient().GetSdRoutingEmbeddedSecurityFeatureProfileByProfileId(**kwargs)

@register('GetSecurityFeature')
def GetSecurityFeature(**kwargs):
    return CatalystClient().GetSecurityFeature(**kwargs)

@register('GetSecurityFeatureByFeatureId')
def GetSecurityFeatureByFeatureId(**kwargs):
    return CatalystClient().GetSecurityFeatureByFeatureId(**kwargs)

@register('GetNgfirewallFeature')
def GetNgfirewallFeature(**kwargs):
    return CatalystClient().GetNgfirewallFeature(**kwargs)

@register('GetNgfirewallFeatureByFeatureId')
def GetNgfirewallFeatureByFeatureId(**kwargs):
    return CatalystClient().GetNgfirewallFeatureByFeatureId(**kwargs)

@register('GetCybervisionProfileFeatureForOther')
def GetCybervisionProfileFeatureForOther(**kwargs):
    return CatalystClient().GetCybervisionProfileFeatureForOther(**kwargs)

@register('GetCybervisionProfileFeatureByFeatureIdForOther')
def GetCybervisionProfileFeatureByFeatureIdForOther(**kwargs):
    return CatalystClient().GetCybervisionProfileFeatureByFeatureIdForOther(**kwargs)

@register('GetSdroutingServiceFeatureProfiles')
def GetSdroutingServiceFeatureProfiles(**kwargs):
    return CatalystClient().GetSdroutingServiceFeatureProfiles(**kwargs)

@register('GetSdroutingServiceFeatureProfile')
def GetSdroutingServiceFeatureProfile(**kwargs):
    return CatalystClient().GetSdroutingServiceFeatureProfile(**kwargs)

@register('GetSdroutingDhcpServerProfileParcels')
def GetSdroutingDhcpServerProfileParcels(**kwargs):
    return CatalystClient().GetSdroutingDhcpServerProfileParcels(**kwargs)

@register('GetSdroutingDhcpServerProfileParcel')
def GetSdroutingDhcpServerProfileParcel(**kwargs):
    return CatalystClient().GetSdroutingDhcpServerProfileParcel(**kwargs)

@register('GetSdroutingServiceIpsecProfileFeatures')
def GetSdroutingServiceIpsecProfileFeatures(**kwargs):
    return CatalystClient().GetSdroutingServiceIpsecProfileFeatures(**kwargs)

@register('GetSdroutingServiceIpsecProfileFeature')
def GetSdroutingServiceIpsecProfileFeature(**kwargs):
    return CatalystClient().GetSdroutingServiceIpsecProfileFeature(**kwargs)

@register('GetSdroutingServiceIpv4AclFeatures')
def GetSdroutingServiceIpv4AclFeatures(**kwargs):
    return CatalystClient().GetSdroutingServiceIpv4AclFeatures(**kwargs)

@register('GetSdroutingServiceIpv4AclFeature')
def GetSdroutingServiceIpv4AclFeature(**kwargs):
    return CatalystClient().GetSdroutingServiceIpv4AclFeature(**kwargs)

@register('GetListOfProfileParcels')
def GetListOfProfileParcels(**kwargs):
    return CatalystClient().GetListOfProfileParcels(**kwargs)

@register('GetMultiCloudConnection')
def GetMultiCloudConnection(**kwargs):
    return CatalystClient().GetMultiCloudConnection(**kwargs)

@register('GetSdroutingServiceObjectTrackerFeatures')
def GetSdroutingServiceObjectTrackerFeatures(**kwargs):
    return CatalystClient().GetSdroutingServiceObjectTrackerFeatures(**kwargs)

@register('GetSdroutingServiceObjectTrackerFeature')
def GetSdroutingServiceObjectTrackerFeature(**kwargs):
    return CatalystClient().GetSdroutingServiceObjectTrackerFeature(**kwargs)

@register('GetSdroutingServiceObjectTrackerGroupFeatures')
def GetSdroutingServiceObjectTrackerGroupFeatures(**kwargs):
    return CatalystClient().GetSdroutingServiceObjectTrackerGroupFeatures(**kwargs)

@register('GetSdroutingServiceObjectTrackerGroupFeature')
def GetSdroutingServiceObjectTrackerGroupFeature(**kwargs):
    return CatalystClient().GetSdroutingServiceObjectTrackerGroupFeature(**kwargs)

@register('GetSdroutingServiceRoutePolicyFeatures')
def GetSdroutingServiceRoutePolicyFeatures(**kwargs):
    return CatalystClient().GetSdroutingServiceRoutePolicyFeatures(**kwargs)

@register('GetSdroutingServiceRoutePolicyFeature')
def GetSdroutingServiceRoutePolicyFeature(**kwargs):
    return CatalystClient().GetSdroutingServiceRoutePolicyFeature(**kwargs)

@register('GetSdroutingServiceVrfOspfFeatures')
def GetSdroutingServiceVrfOspfFeatures(**kwargs):
    return CatalystClient().GetSdroutingServiceVrfOspfFeatures(**kwargs)

@register('GetSdroutingServiceVrfOspfFeature')
def GetSdroutingServiceVrfOspfFeature(**kwargs):
    return CatalystClient().GetSdroutingServiceVrfOspfFeature(**kwargs)

@register('GetSdroutingServiceVrfOspfv3Ipv4Features')
def GetSdroutingServiceVrfOspfv3Ipv4Features(**kwargs):
    return CatalystClient().GetSdroutingServiceVrfOspfv3Ipv4Features(**kwargs)

@register('GetSdroutingServiceVrfOspfv3Ipv4Feature')
def GetSdroutingServiceVrfOspfv3Ipv4Feature(**kwargs):
    return CatalystClient().GetSdroutingServiceVrfOspfv3Ipv4Feature(**kwargs)

@register('GetSdroutingServiceVrfOspfv3Ipv6Features')
def GetSdroutingServiceVrfOspfv3Ipv6Features(**kwargs):
    return CatalystClient().GetSdroutingServiceVrfOspfv3Ipv6Features(**kwargs)

@register('GetSdroutingServiceVrfOspfv3Ipv6Feature')
def GetSdroutingServiceVrfOspfv3Ipv6Feature(**kwargs):
    return CatalystClient().GetSdroutingServiceVrfOspfv3Ipv6Feature(**kwargs)

@register('GetSdroutingServiceVRFFeatures')
def GetSdroutingServiceVRFFeatures(**kwargs):
    return CatalystClient().GetSdroutingServiceVRFFeatures(**kwargs)

@register('GetSdroutingServiceVrfBgpFeatures')
def GetSdroutingServiceVrfBgpFeatures(**kwargs):
    return CatalystClient().GetSdroutingServiceVrfBgpFeatures(**kwargs)

@register('GetSdroutingServiceVrfBgpFeature')
def GetSdroutingServiceVrfBgpFeature(**kwargs):
    return CatalystClient().GetSdroutingServiceVrfBgpFeature(**kwargs)

@register('GetSdroutingServiceVrfEigrpFeatures')
def GetSdroutingServiceVrfEigrpFeatures(**kwargs):
    return CatalystClient().GetSdroutingServiceVrfEigrpFeatures(**kwargs)

@register('GetSdroutingServiceVrfEigrpFeature')
def GetSdroutingServiceVrfEigrpFeature(**kwargs):
    return CatalystClient().GetSdroutingServiceVrfEigrpFeature(**kwargs)

@register('GetSdroutingServiceVRFFeature')
def GetSdroutingServiceVRFFeature(**kwargs):
    return CatalystClient().GetSdroutingServiceVRFFeature(**kwargs)

@register('GetSdroutingServiceVRFDmvpnTunnelFeatures')
def GetSdroutingServiceVRFDmvpnTunnelFeatures(**kwargs):
    return CatalystClient().GetSdroutingServiceVRFDmvpnTunnelFeatures(**kwargs)

@register('GetSdroutingServiceVRFDmvpnTunnelFeature')
def GetSdroutingServiceVRFDmvpnTunnelFeature(**kwargs):
    return CatalystClient().GetSdroutingServiceVRFDmvpnTunnelFeature(**kwargs)

@register('GetSdroutingServiceVrfInterfaceEthernetFeaturesForService')
def GetSdroutingServiceVrfInterfaceEthernetFeaturesForService(**kwargs):
    return CatalystClient().GetSdroutingServiceVrfInterfaceEthernetFeaturesForService(**kwargs)

@register('GetSdroutingServiceVrfInterfaceEthernetFeatureByFeatureIdForService')
def GetSdroutingServiceVrfInterfaceEthernetFeatureByFeatureIdForService(**kwargs):
    return CatalystClient().GetSdroutingServiceVrfInterfaceEthernetFeatureByFeatureIdForService(**kwargs)

@register('GetVrfInterfaceEthernetAssociatedDhcpServerParcelsForService')
def GetVrfInterfaceEthernetAssociatedDhcpServerParcelsForService(**kwargs):
    return CatalystClient().GetVrfInterfaceEthernetAssociatedDhcpServerParcelsForService(**kwargs)

@register('GetVrfInterfaceEthernetAssociatedDhcpServerParcelByFeatureIdForService')
def GetVrfInterfaceEthernetAssociatedDhcpServerParcelByFeatureIdForService(**kwargs):
    return CatalystClient().GetVrfInterfaceEthernetAssociatedDhcpServerParcelByFeatureIdForService(**kwargs)

@register('GetSdroutingServiceVrfInterfaceIpsecFeaturesForService')
def GetSdroutingServiceVrfInterfaceIpsecFeaturesForService(**kwargs):
    return CatalystClient().GetSdroutingServiceVrfInterfaceIpsecFeaturesForService(**kwargs)

@register('GetSdroutingServiceVrfInterfaceIpsecFeatureByFeatureIdForService')
def GetSdroutingServiceVrfInterfaceIpsecFeatureByFeatureIdForService(**kwargs):
    return CatalystClient().GetSdroutingServiceVrfInterfaceIpsecFeatureByFeatureIdForService(**kwargs)

@register('GetServiceVrfAssociatedRoutingBgpFeatures')
def GetServiceVrfAssociatedRoutingBgpFeatures(**kwargs):
    return CatalystClient().GetServiceVrfAssociatedRoutingBgpFeatures(**kwargs)

@register('GetServiceVrfAssociatedRoutingBgpParcelByParcelId')
def GetServiceVrfAssociatedRoutingBgpParcelByParcelId(**kwargs):
    return CatalystClient().GetServiceVrfAssociatedRoutingBgpParcelByParcelId(**kwargs)

@register('GetServiceVrfAssociatedRoutingEigrpFeatures')
def GetServiceVrfAssociatedRoutingEigrpFeatures(**kwargs):
    return CatalystClient().GetServiceVrfAssociatedRoutingEigrpFeatures(**kwargs)

@register('GetServiceVrfAssociatedRoutingEigrpFeatureByFeatureId')
def GetServiceVrfAssociatedRoutingEigrpFeatureByFeatureId(**kwargs):
    return CatalystClient().GetServiceVrfAssociatedRoutingEigrpFeatureByFeatureId(**kwargs)

@register('GetServiceVrfAssociatedRoutingOspfFeatures')
def GetServiceVrfAssociatedRoutingOspfFeatures(**kwargs):
    return CatalystClient().GetServiceVrfAssociatedRoutingOspfFeatures(**kwargs)

@register('GetServiceVrfAssociatedRoutingOspfFeatureById')
def GetServiceVrfAssociatedRoutingOspfFeatureById(**kwargs):
    return CatalystClient().GetServiceVrfAssociatedRoutingOspfFeatureById(**kwargs)

@register('GetServiceVrfAssociatedRoutingOspfv3Ipv4Features')
def GetServiceVrfAssociatedRoutingOspfv3Ipv4Features(**kwargs):
    return CatalystClient().GetServiceVrfAssociatedRoutingOspfv3Ipv4Features(**kwargs)

@register('GetServiceVrfAssociatedRoutingOspfv3Ipv4FeatureById')
def GetServiceVrfAssociatedRoutingOspfv3Ipv4FeatureById(**kwargs):
    return CatalystClient().GetServiceVrfAssociatedRoutingOspfv3Ipv4FeatureById(**kwargs)

@register('GetServiceVrfAssociatedRoutingOspfv3Ipv6Parcels')
def GetServiceVrfAssociatedRoutingOspfv3Ipv6Parcels(**kwargs):
    return CatalystClient().GetServiceVrfAssociatedRoutingOspfv3Ipv6Parcels(**kwargs)

@register('GetServiceVrfAssociatedRoutingOspfv3Ipv6FeatureById')
def GetServiceVrfAssociatedRoutingOspfv3Ipv6FeatureById(**kwargs):
    return CatalystClient().GetServiceVrfAssociatedRoutingOspfv3Ipv6FeatureById(**kwargs)

@register('GetSdRoutingSseFeatureProfiles')
def GetSdRoutingSseFeatureProfiles(**kwargs):
    return CatalystClient().GetSdRoutingSseFeatureProfiles(**kwargs)

@register('GetSdRoutingSseFeatureProfileByProfileId')
def GetSdRoutingSseFeatureProfileByProfileId(**kwargs):
    return CatalystClient().GetSdRoutingSseFeatureProfileByProfileId(**kwargs)

@register('GetCiscoSseFeatureForSse')
def GetCiscoSseFeatureForSse(**kwargs):
    return CatalystClient().GetCiscoSseFeatureForSse(**kwargs)

@register('GetCiscoSseFeatureByFeatureIdForSSE')
def GetCiscoSseFeatureByFeatureIdForSSE(**kwargs):
    return CatalystClient().GetCiscoSseFeatureByFeatureIdForSSE(**kwargs)

@register('GetSdroutingSystemFeatureProfiles')
def GetSdroutingSystemFeatureProfiles(**kwargs):
    return CatalystClient().GetSdroutingSystemFeatureProfiles(**kwargs)

@register('GetSdroutingSystemFeatureProfile')
def GetSdroutingSystemFeatureProfile(**kwargs):
    return CatalystClient().GetSdroutingSystemFeatureProfile(**kwargs)

@register('GetSdroutingAaaFeatures')
def GetSdroutingAaaFeatures(**kwargs):
    return CatalystClient().GetSdroutingAaaFeatures(**kwargs)

@register('GetSdroutingAaaFeature')
def GetSdroutingAaaFeature(**kwargs):
    return CatalystClient().GetSdroutingAaaFeature(**kwargs)

@register('GetSdroutingBannerFeatures')
def GetSdroutingBannerFeatures(**kwargs):
    return CatalystClient().GetSdroutingBannerFeatures(**kwargs)

@register('GetSdroutingBannerFeature')
def GetSdroutingBannerFeature(**kwargs):
    return CatalystClient().GetSdroutingBannerFeature(**kwargs)

@register('GetSdroutingCertificateFeatures')
def GetSdroutingCertificateFeatures(**kwargs):
    return CatalystClient().GetSdroutingCertificateFeatures(**kwargs)

@register('GetSdroutingCertificateFeature')
def GetSdroutingCertificateFeature(**kwargs):
    return CatalystClient().GetSdroutingCertificateFeature(**kwargs)

@register('GetSdroutingFlexiblePortSpeedFeatures')
def GetSdroutingFlexiblePortSpeedFeatures(**kwargs):
    return CatalystClient().GetSdroutingFlexiblePortSpeedFeatures(**kwargs)

@register('GetSdroutingFlexiblePortSpeedFeature')
def GetSdroutingFlexiblePortSpeedFeature(**kwargs):
    return CatalystClient().GetSdroutingFlexiblePortSpeedFeature(**kwargs)

@register('GetSdroutingGlobalSettingFeatures')
def GetSdroutingGlobalSettingFeatures(**kwargs):
    return CatalystClient().GetSdroutingGlobalSettingFeatures(**kwargs)

@register('GetSdroutingGlobalSettingFeature')
def GetSdroutingGlobalSettingFeature(**kwargs):
    return CatalystClient().GetSdroutingGlobalSettingFeature(**kwargs)

@register('GetSdroutingLoggingFeatures')
def GetSdroutingLoggingFeatures(**kwargs):
    return CatalystClient().GetSdroutingLoggingFeatures(**kwargs)

@register('GetSdroutingLoggingFeature')
def GetSdroutingLoggingFeature(**kwargs):
    return CatalystClient().GetSdroutingLoggingFeature(**kwargs)

@register('GetSdroutingNtpFeatures')
def GetSdroutingNtpFeatures(**kwargs):
    return CatalystClient().GetSdroutingNtpFeatures(**kwargs)

@register('GetSdroutingNtpFeature')
def GetSdroutingNtpFeature(**kwargs):
    return CatalystClient().GetSdroutingNtpFeature(**kwargs)

@register('GetSdroutingSnmpFeatures')
def GetSdroutingSnmpFeatures(**kwargs):
    return CatalystClient().GetSdroutingSnmpFeatures(**kwargs)

@register('GetSdroutingSnmpFeature')
def GetSdroutingSnmpFeature(**kwargs):
    return CatalystClient().GetSdroutingSnmpFeature(**kwargs)

@register('GetSdroutingTransportFeatureProfiles')
def GetSdroutingTransportFeatureProfiles(**kwargs):
    return CatalystClient().GetSdroutingTransportFeatureProfiles(**kwargs)

@register('GetSdroutingTransportFeatureProfile')
def GetSdroutingTransportFeatureProfile(**kwargs):
    return CatalystClient().GetSdroutingTransportFeatureProfile(**kwargs)

@register('GetCellularControllerProfileParcelForTransport_1')
def GetCellularControllerProfileParcelForTransport_1(**kwargs):
    return CatalystClient().GetCellularControllerProfileParcelForTransport_1(**kwargs)

@register('GetCellularControllerProfileParcelByParcelIdForTransport_1')
def GetCellularControllerProfileParcelByParcelIdForTransport_1(**kwargs):
    return CatalystClient().GetCellularControllerProfileParcelByParcelIdForTransport_1(**kwargs)

@register('GetCellularControllerAssociatedCellularProfileParcelsForTransport_1')
def GetCellularControllerAssociatedCellularProfileParcelsForTransport_1(**kwargs):
    return CatalystClient().GetCellularControllerAssociatedCellularProfileParcelsForTransport_1(**kwargs)

@register('GetCellularControllerAssociatedCellularProfileParcelByParcelIdForTransport_1')
def GetCellularControllerAssociatedCellularProfileParcelByParcelIdForTransport_1(**kwargs):
    return CatalystClient().GetCellularControllerAssociatedCellularProfileParcelByParcelIdForTransport_1(**kwargs)

@register('GetCellularControllerAssociatedGpsParcelsForTransport_1')
def GetCellularControllerAssociatedGpsParcelsForTransport_1(**kwargs):
    return CatalystClient().GetCellularControllerAssociatedGpsParcelsForTransport_1(**kwargs)

@register('GetCellularControllerAssociatedGpsParcelByParcelIdForTransport_1')
def GetCellularControllerAssociatedGpsParcelByParcelIdForTransport_1(**kwargs):
    return CatalystClient().GetCellularControllerAssociatedGpsParcelByParcelIdForTransport_1(**kwargs)

@register('GetCellularProfileParcelForTransport')
def GetCellularProfileParcelForTransport(**kwargs):
    return CatalystClient().GetCellularProfileParcelForTransport(**kwargs)

@register('GetCellularProfileParcelByParcelIdForTransport')
def GetCellularProfileParcelByParcelIdForTransport(**kwargs):
    return CatalystClient().GetCellularProfileParcelByParcelIdForTransport(**kwargs)

@register('GetSdroutingTransportGlobalVRFFeatures')
def GetSdroutingTransportGlobalVRFFeatures(**kwargs):
    return CatalystClient().GetSdroutingTransportGlobalVRFFeatures(**kwargs)

@register('GetSdroutingTransportGlobalVrfBgpFeatures')
def GetSdroutingTransportGlobalVrfBgpFeatures(**kwargs):
    return CatalystClient().GetSdroutingTransportGlobalVrfBgpFeatures(**kwargs)

@register('GetSdroutingTransportGlobalVrfBgpFeature')
def GetSdroutingTransportGlobalVrfBgpFeature(**kwargs):
    return CatalystClient().GetSdroutingTransportGlobalVrfBgpFeature(**kwargs)

@register('GetSdroutingTransportGlobalVRFFeature')
def GetSdroutingTransportGlobalVRFFeature(**kwargs):
    return CatalystClient().GetSdroutingTransportGlobalVRFFeature(**kwargs)

@register('GetGlobalVRFInterfaceCellularParcelsForTransport')
def GetGlobalVRFInterfaceCellularParcelsForTransport(**kwargs):
    return CatalystClient().GetGlobalVRFInterfaceCellularParcelsForTransport(**kwargs)

@register('GetGlobalVRFInterfaceCellularAssociatedTrackerParcelsForTransport_1')
def GetGlobalVRFInterfaceCellularAssociatedTrackerParcelsForTransport_1(**kwargs):
    return CatalystClient().GetGlobalVRFInterfaceCellularAssociatedTrackerParcelsForTransport_1(**kwargs)

@register('GetGlobalVRFInterfaceCellularAssociatedTrackerParcelByParcelIdForTransport_1')
def GetGlobalVRFInterfaceCellularAssociatedTrackerParcelByParcelIdForTransport_1(**kwargs):
    return CatalystClient().GetGlobalVRFInterfaceCellularAssociatedTrackerParcelByParcelIdForTransport_1(**kwargs)

@register('GetGlobalVRFInterfaceCellularAssociatedTrackerParcelsForTransport')
def GetGlobalVRFInterfaceCellularAssociatedTrackerParcelsForTransport(**kwargs):
    return CatalystClient().GetGlobalVRFInterfaceCellularAssociatedTrackerParcelsForTransport(**kwargs)

@register('GetGlobalVRFInterfaceCellularAssociatedTrackerParcelByParcelIdForTransport')
def GetGlobalVRFInterfaceCellularAssociatedTrackerParcelByParcelIdForTransport(**kwargs):
    return CatalystClient().GetGlobalVRFInterfaceCellularAssociatedTrackerParcelByParcelIdForTransport(**kwargs)

@register('GetGlobalVRFInterfaceCellularParcelByParcelIdForTransport')
def GetGlobalVRFInterfaceCellularParcelByParcelIdForTransport(**kwargs):
    return CatalystClient().GetGlobalVRFInterfaceCellularParcelByParcelIdForTransport(**kwargs)

@register('GetSdroutingTransportGlobalVrfInterfaceEthernetParcelsForTransport')
def GetSdroutingTransportGlobalVrfInterfaceEthernetParcelsForTransport(**kwargs):
    return CatalystClient().GetSdroutingTransportGlobalVrfInterfaceEthernetParcelsForTransport(**kwargs)

@register('GetSdroutingTransportGlobalVrfInterfaceEthernetParcelByParcelIdForTransport')
def GetSdroutingTransportGlobalVrfInterfaceEthernetParcelByParcelIdForTransport(**kwargs):
    return CatalystClient().GetSdroutingTransportGlobalVrfInterfaceEthernetParcelByParcelIdForTransport(**kwargs)

@register('GetSdroutingTransportGlobalVrfInterfaceIpsecFeaturesForTransport')
def GetSdroutingTransportGlobalVrfInterfaceIpsecFeaturesForTransport(**kwargs):
    return CatalystClient().GetSdroutingTransportGlobalVrfInterfaceIpsecFeaturesForTransport(**kwargs)

@register('GetSdroutingTransportGlobalVrfInterfaceIpsecFeatureByFeatureIdForTransport')
def GetSdroutingTransportGlobalVrfInterfaceIpsecFeatureByFeatureIdForTransport(**kwargs):
    return CatalystClient().GetSdroutingTransportGlobalVrfInterfaceIpsecFeatureByFeatureIdForTransport(**kwargs)

@register('GetTransportVrfAssociatedRoutingBgpFeatures')
def GetTransportVrfAssociatedRoutingBgpFeatures(**kwargs):
    return CatalystClient().GetTransportVrfAssociatedRoutingBgpFeatures(**kwargs)

@register('GetVrfAssociatedRoutingBgpFeatureById')
def GetVrfAssociatedRoutingBgpFeatureById(**kwargs):
    return CatalystClient().GetVrfAssociatedRoutingBgpFeatureById(**kwargs)

@register('GetTransportVrfAssociatedRoutingOspfFeatures')
def GetTransportVrfAssociatedRoutingOspfFeatures(**kwargs):
    return CatalystClient().GetTransportVrfAssociatedRoutingOspfFeatures(**kwargs)

@register('GetVrfAssociatedRoutingOspfParcelByFeatureId')
def GetVrfAssociatedRoutingOspfParcelByFeatureId(**kwargs):
    return CatalystClient().GetVrfAssociatedRoutingOspfParcelByFeatureId(**kwargs)

@register('GetTransportVrfAssociatedRoutingOspfv3Ipv4Features')
def GetTransportVrfAssociatedRoutingOspfv3Ipv4Features(**kwargs):
    return CatalystClient().GetTransportVrfAssociatedRoutingOspfv3Ipv4Features(**kwargs)

@register('GetVrfAssociatedRoutingOspfv3Ipv4FeatureById')
def GetVrfAssociatedRoutingOspfv3Ipv4FeatureById(**kwargs):
    return CatalystClient().GetVrfAssociatedRoutingOspfv3Ipv4FeatureById(**kwargs)

@register('GetTransportVrfAssociatedRoutingOspfv3Ipv6Features')
def GetTransportVrfAssociatedRoutingOspfv3Ipv6Features(**kwargs):
    return CatalystClient().GetTransportVrfAssociatedRoutingOspfv3Ipv6Features(**kwargs)

@register('GetVrfAssociatedRoutingOspfv3Ipv6FeatureById')
def GetVrfAssociatedRoutingOspfv3Ipv6FeatureById(**kwargs):
    return CatalystClient().GetVrfAssociatedRoutingOspfv3Ipv6FeatureById(**kwargs)

@register('GetGPSProfileParcelForTransport')
def GetGPSProfileParcelForTransport(**kwargs):
    return CatalystClient().GetGPSProfileParcelForTransport(**kwargs)

@register('GetGPSProfileParcelByParcelIdForTransport')
def GetGPSProfileParcelByParcelIdForTransport(**kwargs):
    return CatalystClient().GetGPSProfileParcelByParcelIdForTransport(**kwargs)

@register('GetSdroutingTransportIpv4AclFeatures')
def GetSdroutingTransportIpv4AclFeatures(**kwargs):
    return CatalystClient().GetSdroutingTransportIpv4AclFeatures(**kwargs)

@register('GetSdroutingTransportIpv4AclFeature')
def GetSdroutingTransportIpv4AclFeature(**kwargs):
    return CatalystClient().GetSdroutingTransportIpv4AclFeature(**kwargs)

@register('GetSdroutingManagementVRFFeatures')
def GetSdroutingManagementVRFFeatures(**kwargs):
    return CatalystClient().GetSdroutingManagementVRFFeatures(**kwargs)

@register('GetSdroutingManagementVRFFeature')
def GetSdroutingManagementVRFFeature(**kwargs):
    return CatalystClient().GetSdroutingManagementVRFFeature(**kwargs)

@register('GetSdroutingManagementVrfInterfaceEthernetParcelsForTransportProfile')
def GetSdroutingManagementVrfInterfaceEthernetParcelsForTransportProfile(**kwargs):
    return CatalystClient().GetSdroutingManagementVrfInterfaceEthernetParcelsForTransportProfile(**kwargs)

@register('GetSdroutingManagementVrfInterfaceEthernetParcelByParcelIdForTransportProfile')
def GetSdroutingManagementVrfInterfaceEthernetParcelByParcelIdForTransportProfile(**kwargs):
    return CatalystClient().GetSdroutingManagementVrfInterfaceEthernetParcelByParcelIdForTransportProfile(**kwargs)

@register('GetLanVpnProfileParcelForService_1')
def GetLanVpnProfileParcelForService_1(**kwargs):
    return CatalystClient().GetLanVpnProfileParcelForService_1(**kwargs)

@register('GetLanVpnProfileParcelByParcelIdForService_1')
def GetLanVpnProfileParcelByParcelIdForService_1(**kwargs):
    return CatalystClient().GetLanVpnProfileParcelByParcelIdForService_1(**kwargs)

@register('GetSdroutingTransportObjectTrackerFeatures')
def GetSdroutingTransportObjectTrackerFeatures(**kwargs):
    return CatalystClient().GetSdroutingTransportObjectTrackerFeatures(**kwargs)

@register('GetSdroutingTransportObjectTrackerFeature')
def GetSdroutingTransportObjectTrackerFeature(**kwargs):
    return CatalystClient().GetSdroutingTransportObjectTrackerFeature(**kwargs)

@register('GetSdroutingTransportObjectTrackerGroupFeatures')
def GetSdroutingTransportObjectTrackerGroupFeatures(**kwargs):
    return CatalystClient().GetSdroutingTransportObjectTrackerGroupFeatures(**kwargs)

@register('GetSdroutingTransportObjectTrackerGroupFeature')
def GetSdroutingTransportObjectTrackerGroupFeature(**kwargs):
    return CatalystClient().GetSdroutingTransportObjectTrackerGroupFeature(**kwargs)

@register('GetSdroutingTransportRoutePolicyFeatures')
def GetSdroutingTransportRoutePolicyFeatures(**kwargs):
    return CatalystClient().GetSdroutingTransportRoutePolicyFeatures(**kwargs)

@register('GetSdroutingTransportRoutePolicyFeature')
def GetSdroutingTransportRoutePolicyFeature(**kwargs):
    return CatalystClient().GetSdroutingTransportRoutePolicyFeature(**kwargs)

@register('GetSdroutingTransportRoutingOspfFeatures')
def GetSdroutingTransportRoutingOspfFeatures(**kwargs):
    return CatalystClient().GetSdroutingTransportRoutingOspfFeatures(**kwargs)

@register('GetSdroutingTransportRoutingOspfFeature')
def GetSdroutingTransportRoutingOspfFeature(**kwargs):
    return CatalystClient().GetSdroutingTransportRoutingOspfFeature(**kwargs)

@register('GetSdroutingTransportRoutingOspfv3Ipv4Features')
def GetSdroutingTransportRoutingOspfv3Ipv4Features(**kwargs):
    return CatalystClient().GetSdroutingTransportRoutingOspfv3Ipv4Features(**kwargs)

@register('GetSdroutingTransportRoutingOspfv3Ipv4Feature')
def GetSdroutingTransportRoutingOspfv3Ipv4Feature(**kwargs):
    return CatalystClient().GetSdroutingTransportRoutingOspfv3Ipv4Feature(**kwargs)

@register('GetSdroutingTransportRoutingOspfv3Ipv6Features')
def GetSdroutingTransportRoutingOspfv3Ipv6Features(**kwargs):
    return CatalystClient().GetSdroutingTransportRoutingOspfv3Ipv6Features(**kwargs)

@register('GetSdroutingTransportRoutingOspfv3Ipv6Feature')
def GetSdroutingTransportRoutingOspfv3Ipv6Feature(**kwargs):
    return CatalystClient().GetSdroutingTransportRoutingOspfv3Ipv6Feature(**kwargs)

@register('GetTrackerProfileParcelForTransport_1')
def GetTrackerProfileParcelForTransport_1(**kwargs):
    return CatalystClient().GetTrackerProfileParcelForTransport_1(**kwargs)

@register('GetTrackerProfileParcelByParcelIdForTransport_1')
def GetTrackerProfileParcelByParcelIdForTransport_1(**kwargs):
    return CatalystClient().GetTrackerProfileParcelByParcelIdForTransport_1(**kwargs)

@register('GetTrackerGroupProfileParcelForTransport_1')
def GetTrackerGroupProfileParcelForTransport_1(**kwargs):
    return CatalystClient().GetTrackerGroupProfileParcelForTransport_1(**kwargs)

@register('GetTrackerGroupProfileParcelByParcelIdForTransport_1')
def GetTrackerGroupProfileParcelByParcelIdForTransport_1(**kwargs):
    return CatalystClient().GetTrackerGroupProfileParcelByParcelIdForTransport_1(**kwargs)

@register('GetSdroutingTransportVRFFeatures')
def GetSdroutingTransportVRFFeatures(**kwargs):
    return CatalystClient().GetSdroutingTransportVRFFeatures(**kwargs)

@register('GetSdroutingTransportVrfBgpFeatures')
def GetSdroutingTransportVrfBgpFeatures(**kwargs):
    return CatalystClient().GetSdroutingTransportVrfBgpFeatures(**kwargs)

@register('GetSdroutingTransportVrfBgpFeature')
def GetSdroutingTransportVrfBgpFeature(**kwargs):
    return CatalystClient().GetSdroutingTransportVrfBgpFeature(**kwargs)

@register('GetSdroutingTransportVRFFeature')
def GetSdroutingTransportVRFFeature(**kwargs):
    return CatalystClient().GetSdroutingTransportVRFFeature(**kwargs)

@register('GetSdroutingTransportVrfInterfaceEthernetParcelsForTransport')
def GetSdroutingTransportVrfInterfaceEthernetParcelsForTransport(**kwargs):
    return CatalystClient().GetSdroutingTransportVrfInterfaceEthernetParcelsForTransport(**kwargs)

@register('GetSdroutingTransportVrfInterfaceEthernetParcelByParcelIdForTransport')
def GetSdroutingTransportVrfInterfaceEthernetParcelByParcelIdForTransport(**kwargs):
    return CatalystClient().GetSdroutingTransportVrfInterfaceEthernetParcelByParcelIdForTransport(**kwargs)

@register('GetSdroutingTransportVrfInterfaceIpsecFeaturesForTransport')
def GetSdroutingTransportVrfInterfaceIpsecFeaturesForTransport(**kwargs):
    return CatalystClient().GetSdroutingTransportVrfInterfaceIpsecFeaturesForTransport(**kwargs)

@register('GetSdroutingTransportVrfInterfaceIpsecFeatureByFeatureIdForTransport')
def GetSdroutingTransportVrfInterfaceIpsecFeatureByFeatureIdForTransport(**kwargs):
    return CatalystClient().GetSdroutingTransportVrfInterfaceIpsecFeatureByFeatureIdForTransport(**kwargs)

@register('GetTransportVrfAssociatedRoutingBgpFeatures_1')
def GetTransportVrfAssociatedRoutingBgpFeatures_1(**kwargs):
    return CatalystClient().GetTransportVrfAssociatedRoutingBgpFeatures_1(**kwargs)

@register('GetTransportVrfAssociatedRoutingBgpById')
def GetTransportVrfAssociatedRoutingBgpById(**kwargs):
    return CatalystClient().GetTransportVrfAssociatedRoutingBgpById(**kwargs)

@register('GetTransportVrfAssociatedRoutingOspfFeatures_1')
def GetTransportVrfAssociatedRoutingOspfFeatures_1(**kwargs):
    return CatalystClient().GetTransportVrfAssociatedRoutingOspfFeatures_1(**kwargs)

@register('GetVrfAssociatedRoutingOspfById')
def GetVrfAssociatedRoutingOspfById(**kwargs):
    return CatalystClient().GetVrfAssociatedRoutingOspfById(**kwargs)

@register('GetTransportVrfAssociatedRoutingOspfv3Ipv4Features_1')
def GetTransportVrfAssociatedRoutingOspfv3Ipv4Features_1(**kwargs):
    return CatalystClient().GetTransportVrfAssociatedRoutingOspfv3Ipv4Features_1(**kwargs)

@register('GetVrfAssociatedRoutingOspfv3Ipv4FeatureById_1')
def GetVrfAssociatedRoutingOspfv3Ipv4FeatureById_1(**kwargs):
    return CatalystClient().GetVrfAssociatedRoutingOspfv3Ipv4FeatureById_1(**kwargs)

@register('GetTransportVrfAssociatedRoutingOspfv3Ipv6Features_1')
def GetTransportVrfAssociatedRoutingOspfv3Ipv6Features_1(**kwargs):
    return CatalystClient().GetTransportVrfAssociatedRoutingOspfv3Ipv6Features_1(**kwargs)

@register('GetVrfAssociatedRoutingOspfv3Ipv6FeatureById_1')
def GetVrfAssociatedRoutingOspfv3Ipv6FeatureById_1(**kwargs):
    return CatalystClient().GetVrfAssociatedRoutingOspfv3Ipv6FeatureById_1(**kwargs)

@register('GetSdwanFeatureProfileBySdwanFamily')
def GetSdwanFeatureProfileBySdwanFamily(**kwargs):
    return CatalystClient().GetSdwanFeatureProfileBySdwanFamily(**kwargs)

@register('GetCloudProbeProfileParcelByParcelIdForapplication-priority')
def GetCloudProbeProfileParcelByParcelIdForapplication_priority(**kwargs):
    return CatalystClient().GetCloudProbeProfileParcelByParcelIdForapplication_priority(**kwargs)

@register('getPolicyApplicationProfileParcel')
def getPolicyApplicationProfileParcel(**kwargs):
    return CatalystClient().getPolicyApplicationProfileParcel(**kwargs)

@register('GetTrafficPolicyProfileParcelByParcelIdForapplication-priority')
def GetTrafficPolicyProfileParcelByParcelIdForapplication_priority(**kwargs):
    return CatalystClient().GetTrafficPolicyProfileParcelByParcelIdForapplication_priority(**kwargs)

@register('GetSdwanFeatureProfilesByFamilyAndType_1')
def GetSdwanFeatureProfilesByFamilyAndType_1(**kwargs):
    return CatalystClient().GetSdwanFeatureProfilesByFamilyAndType_1(**kwargs)

@register('GetSdwanCliConfigFeatureSchemaBySchemaType')
def GetSdwanCliConfigFeatureSchemaBySchemaType(**kwargs):
    return CatalystClient().GetSdwanCliConfigFeatureSchemaBySchemaType(**kwargs)

@register('GetSdwanFeatureProfilesByFamilyAndType')
def GetSdwanFeatureProfilesByFamilyAndType(**kwargs):
    return CatalystClient().GetSdwanFeatureProfilesByFamilyAndType(**kwargs)

@register('GetSdwanFeatureProfileByProfileId')
def GetSdwanFeatureProfileByProfileId(**kwargs):
    return CatalystClient().GetSdwanFeatureProfileByProfileId(**kwargs)

@register('GetConfigProfileParcelForCLI')
def GetConfigProfileParcelForCLI(**kwargs):
    return CatalystClient().GetConfigProfileParcelForCLI(**kwargs)

@register('GetConfigProfileParcelByParcelIdForCLI')
def GetConfigProfileParcelByParcelIdForCLI(**kwargs):
    return CatalystClient().GetConfigProfileParcelByParcelIdForCLI(**kwargs)

@register('GetSdwanDnsSecurityFeatureProfiles')
def GetSdwanDnsSecurityFeatureProfiles(**kwargs):
    return CatalystClient().GetSdwanDnsSecurityFeatureProfiles(**kwargs)

@register('GetSdwanDnsSecurityFeatureProfileByProfileId')
def GetSdwanDnsSecurityFeatureProfileByProfileId(**kwargs):
    return CatalystClient().GetSdwanDnsSecurityFeatureProfileByProfileId(**kwargs)

@register('GetSigSecurityProfileParcel')
def GetSigSecurityProfileParcel(**kwargs):
    return CatalystClient().GetSigSecurityProfileParcel(**kwargs)

@register('GetSigSecurityProfileParcelByParcelId')
def GetSigSecurityProfileParcelByParcelId(**kwargs):
    return CatalystClient().GetSigSecurityProfileParcelByParcelId(**kwargs)

@register('GetSdwanSecurityFeature_1')
def GetSdwanSecurityFeature_1(**kwargs):
    return CatalystClient().GetSdwanSecurityFeature_1(**kwargs)

@register('GetSdwanSecurityFeatureByFeatureId_1')
def GetSdwanSecurityFeatureByFeatureId_1(**kwargs):
    return CatalystClient().GetSdwanSecurityFeatureByFeatureId_1(**kwargs)

@register('GetSdwanNgfirewallFeature')
def GetSdwanNgfirewallFeature(**kwargs):
    return CatalystClient().GetSdwanNgfirewallFeature(**kwargs)

@register('GetSdwanNgfirewallFeatureByFeatureId')
def GetSdwanNgfirewallFeatureByFeatureId(**kwargs):
    return CatalystClient().GetSdwanNgfirewallFeatureByFeatureId(**kwargs)

@register('GetSdwanOtherFeatureProfiles')
def GetSdwanOtherFeatureProfiles(**kwargs):
    return CatalystClient().GetSdwanOtherFeatureProfiles(**kwargs)

@register('GetSdwanOtherThousandeyesParcelSchemaBySchemaType')
def GetSdwanOtherThousandeyesParcelSchemaBySchemaType(**kwargs):
    return CatalystClient().GetSdwanOtherThousandeyesParcelSchemaBySchemaType(**kwargs)

@register('GetSdwanOtherFeatureProfileByProfileId')
def GetSdwanOtherFeatureProfileByProfileId(**kwargs):
    return CatalystClient().GetSdwanOtherFeatureProfileByProfileId(**kwargs)

@register('GetThousandeyesProfileParcelForOther')
def GetThousandeyesProfileParcelForOther(**kwargs):
    return CatalystClient().GetThousandeyesProfileParcelForOther(**kwargs)

@register('GetThousandeyesProfileParcelByParcelIdForOther')
def GetThousandeyesProfileParcelByParcelIdForOther(**kwargs):
    return CatalystClient().GetThousandeyesProfileParcelByParcelIdForOther(**kwargs)

@register('GetUcseProfileFeatureForOther')
def GetUcseProfileFeatureForOther(**kwargs):
    return CatalystClient().GetUcseProfileFeatureForOther(**kwargs)

@register('GetUcseProfileFeatureByIdFFeatureForOther')
def GetUcseProfileFeatureByIdFFeatureForOther(**kwargs):
    return CatalystClient().GetUcseProfileFeatureByIdFFeatureForOther(**kwargs)

@register('GetSdwanSecurityFeature')
def GetSdwanSecurityFeature(**kwargs):
    return CatalystClient().GetSdwanSecurityFeature(**kwargs)

@register('GetSdwanSecurityFeatureByFeatureId')
def GetSdwanSecurityFeatureByFeatureId(**kwargs):
    return CatalystClient().GetSdwanSecurityFeatureByFeatureId(**kwargs)

@register('GetDataPrefixProfileParcelForPolicyObject')
def GetDataPrefixProfileParcelForPolicyObject(**kwargs):
    return CatalystClient().GetDataPrefixProfileParcelForPolicyObject(**kwargs)

@register('GetDataPrefixProfileParcelByParcelIdForPolicyObject')
def GetDataPrefixProfileParcelByParcelIdForPolicyObject(**kwargs):
    return CatalystClient().GetDataPrefixProfileParcelByParcelIdForPolicyObject(**kwargs)

@register('GetSdwanPolicyObjectDataPrefixParcelSchemaBySchemaType')
def GetSdwanPolicyObjectDataPrefixParcelSchemaBySchemaType(**kwargs):
    return CatalystClient().GetSdwanPolicyObjectDataPrefixParcelSchemaBySchemaType(**kwargs)

@register('GetSdwanServiceFeatureProfiles')
def GetSdwanServiceFeatureProfiles(**kwargs):
    return CatalystClient().GetSdwanServiceFeatureProfiles(**kwargs)

@register('GetSdwanServiceDhcpServerParcelSchemaBySchemaType')
def GetSdwanServiceDhcpServerParcelSchemaBySchemaType(**kwargs):
    return CatalystClient().GetSdwanServiceDhcpServerParcelSchemaBySchemaType(**kwargs)

@register('GetSdwanServiceLanVpnInterfaceEthernetParcelSchemaBySchema')
def GetSdwanServiceLanVpnInterfaceEthernetParcelSchemaBySchema(**kwargs):
    return CatalystClient().GetSdwanServiceLanVpnInterfaceEthernetParcelSchemaBySchema(**kwargs)

@register('GetCedgeServiceLanVpnInterfaceGreSchemaBySchema')
def GetCedgeServiceLanVpnInterfaceGreSchemaBySchema(**kwargs):
    return CatalystClient().GetCedgeServiceLanVpnInterfaceGreSchemaBySchema(**kwargs)

@register('getSdwanProfileParcelSchema')
def getSdwanProfileParcelSchema(**kwargs):
    return CatalystClient().getSdwanProfileParcelSchema(**kwargs)

@register('GetCedgeServiceLanVpnInterfaceSviParcelSchemaBySchema')
def GetCedgeServiceLanVpnInterfaceSviParcelSchemaBySchema(**kwargs):
    return CatalystClient().GetCedgeServiceLanVpnInterfaceSviParcelSchemaBySchema(**kwargs)

@register('GetSdwanServiceLanVpnParcelSchemaBySchemaType')
def GetSdwanServiceLanVpnParcelSchemaBySchemaType(**kwargs):
    return CatalystClient().GetSdwanServiceLanVpnParcelSchemaBySchemaType(**kwargs)

@register('GetSdwanServiceRoutingBgpParcelSchemaBySchemaType')
def GetSdwanServiceRoutingBgpParcelSchemaBySchemaType(**kwargs):
    return CatalystClient().GetSdwanServiceRoutingBgpParcelSchemaBySchemaType(**kwargs)

@register('GetSdwanServiceRoutingMulticastParcelSchemaBySchemaType')
def GetSdwanServiceRoutingMulticastParcelSchemaBySchemaType(**kwargs):
    return CatalystClient().GetSdwanServiceRoutingMulticastParcelSchemaBySchemaType(**kwargs)

@register('GetCedgeServiceSwitchportParcelSchemaBySchemaType')
def GetCedgeServiceSwitchportParcelSchemaBySchemaType(**kwargs):
    return CatalystClient().GetCedgeServiceSwitchportParcelSchemaBySchemaType(**kwargs)

@register('GetSdwanServiceTrackerParcelSchemaBySchemaType')
def GetSdwanServiceTrackerParcelSchemaBySchemaType(**kwargs):
    return CatalystClient().GetSdwanServiceTrackerParcelSchemaBySchemaType(**kwargs)

@register('GetCedgeServiceTrackerGroupParcelSchemaBySchemaType')
def GetCedgeServiceTrackerGroupParcelSchemaBySchemaType(**kwargs):
    return CatalystClient().GetCedgeServiceTrackerGroupParcelSchemaBySchemaType(**kwargs)

@register('GetSdwanServiceWirelesslanParcelSchemaBySchemaType')
def GetSdwanServiceWirelesslanParcelSchemaBySchemaType(**kwargs):
    return CatalystClient().GetSdwanServiceWirelesslanParcelSchemaBySchemaType(**kwargs)

@register('GetSdwanServiceFeatureProfileByProfileId')
def GetSdwanServiceFeatureProfileByProfileId(**kwargs):
    return CatalystClient().GetSdwanServiceFeatureProfileByProfileId(**kwargs)

@register('GetAppqoeProfileParcelForService')
def GetAppqoeProfileParcelForService(**kwargs):
    return CatalystClient().GetAppqoeProfileParcelForService(**kwargs)

@register('GetAppqoeProfileParcelByParcelIdForService')
def GetAppqoeProfileParcelByParcelIdForService(**kwargs):
    return CatalystClient().GetAppqoeProfileParcelByParcelIdForService(**kwargs)

@register('GetDhcpServerProfileParcelForService')
def GetDhcpServerProfileParcelForService(**kwargs):
    return CatalystClient().GetDhcpServerProfileParcelForService(**kwargs)

@register('GetDhcpServerProfileParcelByParcelIdForService')
def GetDhcpServerProfileParcelByParcelIdForService(**kwargs):
    return CatalystClient().GetDhcpServerProfileParcelByParcelIdForService(**kwargs)

@register('GetLanVpnProfileParcelForService')
def GetLanVpnProfileParcelForService(**kwargs):
    return CatalystClient().GetLanVpnProfileParcelForService(**kwargs)

@register('GetLanVpnProfileParcelByParcelIdForService')
def GetLanVpnProfileParcelByParcelIdForService(**kwargs):
    return CatalystClient().GetLanVpnProfileParcelByParcelIdForService(**kwargs)

@register('GetInterfaceEthernetParcelsForServiceLanVpn')
def GetInterfaceEthernetParcelsForServiceLanVpn(**kwargs):
    return CatalystClient().GetInterfaceEthernetParcelsForServiceLanVpn(**kwargs)

@register('GetLanVpnInterfaceEthernetParcelByParcelIdForService')
def GetLanVpnInterfaceEthernetParcelByParcelIdForService(**kwargs):
    return CatalystClient().GetLanVpnInterfaceEthernetParcelByParcelIdForService(**kwargs)

@register('GetLanVpnInterfaceEthernetAssociatedDhcpServerParcelsForTransport')
def GetLanVpnInterfaceEthernetAssociatedDhcpServerParcelsForTransport(**kwargs):
    return CatalystClient().GetLanVpnInterfaceEthernetAssociatedDhcpServerParcelsForTransport(**kwargs)

@register('GetLanVpnInterfaceEthernetAssociatedDhcpServerParcelByParcelIdForTransport')
def GetLanVpnInterfaceEthernetAssociatedDhcpServerParcelByParcelIdForTransport(**kwargs):
    return CatalystClient().GetLanVpnInterfaceEthernetAssociatedDhcpServerParcelByParcelIdForTransport(**kwargs)

@register('GetLanVpnInterfaceEthernetAssociatedTrackerParcelsForTransport')
def GetLanVpnInterfaceEthernetAssociatedTrackerParcelsForTransport(**kwargs):
    return CatalystClient().GetLanVpnInterfaceEthernetAssociatedTrackerParcelsForTransport(**kwargs)

@register('GetLanVpnInterfaceEthernetAssociatedTrackerParcelByParcelIdForTransport')
def GetLanVpnInterfaceEthernetAssociatedTrackerParcelByParcelIdForTransport(**kwargs):
    return CatalystClient().GetLanVpnInterfaceEthernetAssociatedTrackerParcelByParcelIdForTransport(**kwargs)

@register('GetLanVpnInterfaceEthernetAssociatedTrackerGroupParcelsForTransport')
def GetLanVpnInterfaceEthernetAssociatedTrackerGroupParcelsForTransport(**kwargs):
    return CatalystClient().GetLanVpnInterfaceEthernetAssociatedTrackerGroupParcelsForTransport(**kwargs)

@register('GetLanVpnInterfaceEthernetAssociatedTrackerGroupParcelByParcelIdForTransport')
def GetLanVpnInterfaceEthernetAssociatedTrackerGroupParcelByParcelIdForTransport(**kwargs):
    return CatalystClient().GetLanVpnInterfaceEthernetAssociatedTrackerGroupParcelByParcelIdForTransport(**kwargs)

@register('GetInterfaceGresForServiceLanVpn')
def GetInterfaceGresForServiceLanVpn(**kwargs):
    return CatalystClient().GetInterfaceGresForServiceLanVpn(**kwargs)

@register('GetLanVpnInterfaceGreByIdForService')
def GetLanVpnInterfaceGreByIdForService(**kwargs):
    return CatalystClient().GetLanVpnInterfaceGreByIdForService(**kwargs)

@register('getListOfProfileParcels')
def getListOfProfileParcels(**kwargs):
    return CatalystClient().getListOfProfileParcels(**kwargs)

@register('getProfileParcelByParcelId')
def getProfileParcelByParcelId(**kwargs):
    return CatalystClient().getProfileParcelByParcelId(**kwargs)

@register('GetLanVpnInterfaceIpsecAssociatedDhcpServerParcelsForTransport')
def GetLanVpnInterfaceIpsecAssociatedDhcpServerParcelsForTransport(**kwargs):
    return CatalystClient().GetLanVpnInterfaceIpsecAssociatedDhcpServerParcelsForTransport(**kwargs)

@register('GetLanVpnInterfaceIpsecAssociatedDhcpServerParcelByParcelIdForTransport')
def GetLanVpnInterfaceIpsecAssociatedDhcpServerParcelByParcelIdForTransport(**kwargs):
    return CatalystClient().GetLanVpnInterfaceIpsecAssociatedDhcpServerParcelByParcelIdForTransport(**kwargs)

@register('GetInterfaceSviParcelsForServiceLanVpn')
def GetInterfaceSviParcelsForServiceLanVpn(**kwargs):
    return CatalystClient().GetInterfaceSviParcelsForServiceLanVpn(**kwargs)

@register('GetLanVpnInterfaceSviParcelByParcelIdForService')
def GetLanVpnInterfaceSviParcelByParcelIdForService(**kwargs):
    return CatalystClient().GetLanVpnInterfaceSviParcelByParcelIdForService(**kwargs)

@register('GetLanVpnInterfaceSviAssociatedDhcpServerParcelsForTransport')
def GetLanVpnInterfaceSviAssociatedDhcpServerParcelsForTransport(**kwargs):
    return CatalystClient().GetLanVpnInterfaceSviAssociatedDhcpServerParcelsForTransport(**kwargs)

@register('GetLanVpnInterfaceSviAssociatedDhcpServerParcelByParcelIdForTransport')
def GetLanVpnInterfaceSviAssociatedDhcpServerParcelByParcelIdForTransport(**kwargs):
    return CatalystClient().GetLanVpnInterfaceSviAssociatedDhcpServerParcelByParcelIdForTransport(**kwargs)

@register('GetLanVpnAssociatedRoutingBgpParcelsForService')
def GetLanVpnAssociatedRoutingBgpParcelsForService(**kwargs):
    return CatalystClient().GetLanVpnAssociatedRoutingBgpParcelsForService(**kwargs)

@register('GetLanVpnAssociatedRoutingBgpParcelByParcelIdForService')
def GetLanVpnAssociatedRoutingBgpParcelByParcelIdForService(**kwargs):
    return CatalystClient().GetLanVpnAssociatedRoutingBgpParcelByParcelIdForService(**kwargs)

@register('GetLanVpnAssociatedRoutingEigrpParcelsForService')
def GetLanVpnAssociatedRoutingEigrpParcelsForService(**kwargs):
    return CatalystClient().GetLanVpnAssociatedRoutingEigrpParcelsForService(**kwargs)

@register('GetLanVpnAssociatedRoutingEigrpParcelByParcelIdForService')
def GetLanVpnAssociatedRoutingEigrpParcelByParcelIdForService(**kwargs):
    return CatalystClient().GetLanVpnAssociatedRoutingEigrpParcelByParcelIdForService(**kwargs)

@register('GetLanVpnAssociatedRoutingMulticastParcelsForService')
def GetLanVpnAssociatedRoutingMulticastParcelsForService(**kwargs):
    return CatalystClient().GetLanVpnAssociatedRoutingMulticastParcelsForService(**kwargs)

@register('GetLanVpnAssociatedRoutingMulticastParcelByParcelIdForService')
def GetLanVpnAssociatedRoutingMulticastParcelByParcelIdForService(**kwargs):
    return CatalystClient().GetLanVpnAssociatedRoutingMulticastParcelByParcelIdForService(**kwargs)

@register('GetLanVpnAssociatedRoutingOspfParcelsForService')
def GetLanVpnAssociatedRoutingOspfParcelsForService(**kwargs):
    return CatalystClient().GetLanVpnAssociatedRoutingOspfParcelsForService(**kwargs)

@register('GetLanVpnAssociatedRoutingOspfParcelByParcelIdForService')
def GetLanVpnAssociatedRoutingOspfParcelByParcelIdForService(**kwargs):
    return CatalystClient().GetLanVpnAssociatedRoutingOspfParcelByParcelIdForService(**kwargs)

@register('GetLanVpnAssociatedRoutingOspfv3IPv4ParcelsForService')
def GetLanVpnAssociatedRoutingOspfv3IPv4ParcelsForService(**kwargs):
    return CatalystClient().GetLanVpnAssociatedRoutingOspfv3IPv4ParcelsForService(**kwargs)

@register('GetLanVpnAssociatedRoutingOspfv3IPv4ParcelByParcelIdForService')
def GetLanVpnAssociatedRoutingOspfv3IPv4ParcelByParcelIdForService(**kwargs):
    return CatalystClient().GetLanVpnAssociatedRoutingOspfv3IPv4ParcelByParcelIdForService(**kwargs)

@register('GetLanVpnAssociatedRoutingOspfv3IPv6ParcelsForService')
def GetLanVpnAssociatedRoutingOspfv3IPv6ParcelsForService(**kwargs):
    return CatalystClient().GetLanVpnAssociatedRoutingOspfv3IPv6ParcelsForService(**kwargs)

@register('GetLanVpnAssociatedRoutingOspfv3IPv6ParcelByParcelIdForService')
def GetLanVpnAssociatedRoutingOspfv3IPv6ParcelByParcelIdForService(**kwargs):
    return CatalystClient().GetLanVpnAssociatedRoutingOspfv3IPv6ParcelByParcelIdForService(**kwargs)

@register('GetRoutingBgpProfileParcelForService')
def GetRoutingBgpProfileParcelForService(**kwargs):
    return CatalystClient().GetRoutingBgpProfileParcelForService(**kwargs)

@register('GetRoutingBgpProfileParcelByParcelIdForService')
def GetRoutingBgpProfileParcelByParcelIdForService(**kwargs):
    return CatalystClient().GetRoutingBgpProfileParcelByParcelIdForService(**kwargs)

@register('GetRoutingEigrpProfileParcelForService')
def GetRoutingEigrpProfileParcelForService(**kwargs):
    return CatalystClient().GetRoutingEigrpProfileParcelForService(**kwargs)

@register('GetRoutingEigrpProfileParcelByParcelIdForService')
def GetRoutingEigrpProfileParcelByParcelIdForService(**kwargs):
    return CatalystClient().GetRoutingEigrpProfileParcelByParcelIdForService(**kwargs)

@register('GetRoutingMulticastProfileParcelForService')
def GetRoutingMulticastProfileParcelForService(**kwargs):
    return CatalystClient().GetRoutingMulticastProfileParcelForService(**kwargs)

@register('GetRoutingMulticastProfileParcelByParcelIdForService')
def GetRoutingMulticastProfileParcelByParcelIdForService(**kwargs):
    return CatalystClient().GetRoutingMulticastProfileParcelByParcelIdForService(**kwargs)

@register('GetRoutingOspfProfileParcelForService')
def GetRoutingOspfProfileParcelForService(**kwargs):
    return CatalystClient().GetRoutingOspfProfileParcelForService(**kwargs)

@register('GetRoutingOspfProfileParcelByParcelIdForService')
def GetRoutingOspfProfileParcelByParcelIdForService(**kwargs):
    return CatalystClient().GetRoutingOspfProfileParcelByParcelIdForService(**kwargs)

@register('GetRoutingOspfv3Ipv4AfProfileParcelForService')
def GetRoutingOspfv3Ipv4AfProfileParcelForService(**kwargs):
    return CatalystClient().GetRoutingOspfv3Ipv4AfProfileParcelForService(**kwargs)

@register('GetRoutingOspfv3IPv4AfProfileParcelByParcelIdForService')
def GetRoutingOspfv3IPv4AfProfileParcelByParcelIdForService(**kwargs):
    return CatalystClient().GetRoutingOspfv3IPv4AfProfileParcelByParcelIdForService(**kwargs)

@register('GetRoutingOspfv3Ipv6AfProfileParcelForService')
def GetRoutingOspfv3Ipv6AfProfileParcelForService(**kwargs):
    return CatalystClient().GetRoutingOspfv3Ipv6AfProfileParcelForService(**kwargs)

@register('GetRoutingOspfv3IPv6AfProfileParcelByParcelIdForService')
def GetRoutingOspfv3IPv6AfProfileParcelByParcelIdForService(**kwargs):
    return CatalystClient().GetRoutingOspfv3IPv6AfProfileParcelByParcelIdForService(**kwargs)

@register('GetSwitchportParcelsForService')
def GetSwitchportParcelsForService(**kwargs):
    return CatalystClient().GetSwitchportParcelsForService(**kwargs)

@register('GetSwitchportParcelByParcelIdForService')
def GetSwitchportParcelByParcelIdForService(**kwargs):
    return CatalystClient().GetSwitchportParcelByParcelIdForService(**kwargs)

@register('GetTrackerProfileParcelForService')
def GetTrackerProfileParcelForService(**kwargs):
    return CatalystClient().GetTrackerProfileParcelForService(**kwargs)

@register('GetTrackerProfileParcelByParcelIdForService')
def GetTrackerProfileParcelByParcelIdForService(**kwargs):
    return CatalystClient().GetTrackerProfileParcelByParcelIdForService(**kwargs)

@register('GetTrackerGroupProfileParcelForService')
def GetTrackerGroupProfileParcelForService(**kwargs):
    return CatalystClient().GetTrackerGroupProfileParcelForService(**kwargs)

@register('GetTrackerGroupProfileParcelByParcelIdForService')
def GetTrackerGroupProfileParcelByParcelIdForService(**kwargs):
    return CatalystClient().GetTrackerGroupProfileParcelByParcelIdForService(**kwargs)

@register('GetWirelesslanProfileParcelForService')
def GetWirelesslanProfileParcelForService(**kwargs):
    return CatalystClient().GetWirelesslanProfileParcelForService(**kwargs)

@register('GetWirelesslanProfileParcelByParcelIdForService')
def GetWirelesslanProfileParcelByParcelIdForService(**kwargs):
    return CatalystClient().GetWirelesslanProfileParcelByParcelIdForService(**kwargs)

@register('GetSdwanSigSecurityFeatureProfiles')
def GetSdwanSigSecurityFeatureProfiles(**kwargs):
    return CatalystClient().GetSdwanSigSecurityFeatureProfiles(**kwargs)

@register('GetSdwanSigSecurityFeatureProfileByProfileId')
def GetSdwanSigSecurityFeatureProfileByProfileId(**kwargs):
    return CatalystClient().GetSdwanSigSecurityFeatureProfileByProfileId(**kwargs)

@register('GetSigSecurityProfileParcel_1')
def GetSigSecurityProfileParcel_1(**kwargs):
    return CatalystClient().GetSigSecurityProfileParcel_1(**kwargs)

@register('GetSigSecurityProfileParcelByParcelId_1')
def GetSigSecurityProfileParcelByParcelId_1(**kwargs):
    return CatalystClient().GetSigSecurityProfileParcelByParcelId_1(**kwargs)

@register('GetSdwanSystemFeatureProfiles')
def GetSdwanSystemFeatureProfiles(**kwargs):
    return CatalystClient().GetSdwanSystemFeatureProfiles(**kwargs)

@register('GetSdwanSystemAaaParcelSchemaBySchemaType')
def GetSdwanSystemAaaParcelSchemaBySchemaType(**kwargs):
    return CatalystClient().GetSdwanSystemAaaParcelSchemaBySchemaType(**kwargs)

@register('GetSdwanSystemBannerParcelSchemaBySchemaType')
def GetSdwanSystemBannerParcelSchemaBySchemaType(**kwargs):
    return CatalystClient().GetSdwanSystemBannerParcelSchemaBySchemaType(**kwargs)

@register('GetSdwanSystemBasicFeatureSchemaBySchemaType')
def GetSdwanSystemBasicFeatureSchemaBySchemaType(**kwargs):
    return CatalystClient().GetSdwanSystemBasicFeatureSchemaBySchemaType(**kwargs)

@register('GetSdwanSystemBfdParcelSchemaBySchemaType')
def GetSdwanSystemBfdParcelSchemaBySchemaType(**kwargs):
    return CatalystClient().GetSdwanSystemBfdParcelSchemaBySchemaType(**kwargs)

@register('GetCedgeSystemGlobalParcelSchemaBySchemaType')
def GetCedgeSystemGlobalParcelSchemaBySchemaType(**kwargs):
    return CatalystClient().GetCedgeSystemGlobalParcelSchemaBySchemaType(**kwargs)

@register('GetSdwanSystemLoggingParcelSchemaBySchemaType')
def GetSdwanSystemLoggingParcelSchemaBySchemaType(**kwargs):
    return CatalystClient().GetSdwanSystemLoggingParcelSchemaBySchemaType(**kwargs)

@register('GetCedgeSystemMrfParcelSchemaBySchemaType')
def GetCedgeSystemMrfParcelSchemaBySchemaType(**kwargs):
    return CatalystClient().GetCedgeSystemMrfParcelSchemaBySchemaType(**kwargs)

@register('GetSdwanSystemNtpParcelSchemaBySchemaType')
def GetSdwanSystemNtpParcelSchemaBySchemaType(**kwargs):
    return CatalystClient().GetSdwanSystemNtpParcelSchemaBySchemaType(**kwargs)

@register('GetSdwanSystemOmpParcelSchemaBySchemaType')
def GetSdwanSystemOmpParcelSchemaBySchemaType(**kwargs):
    return CatalystClient().GetSdwanSystemOmpParcelSchemaBySchemaType(**kwargs)

@register('GetSdwanSystemSnmpParcelSchemaBySchemaType')
def GetSdwanSystemSnmpParcelSchemaBySchemaType(**kwargs):
    return CatalystClient().GetSdwanSystemSnmpParcelSchemaBySchemaType(**kwargs)

@register('GetSdwanSystemFeatureProfileByProfileId')
def GetSdwanSystemFeatureProfileByProfileId(**kwargs):
    return CatalystClient().GetSdwanSystemFeatureProfileByProfileId(**kwargs)

@register('GetAaaProfileParcelForSystem')
def GetAaaProfileParcelForSystem(**kwargs):
    return CatalystClient().GetAaaProfileParcelForSystem(**kwargs)

@register('GetAaaProfileParcelByParcelIdForSystem')
def GetAaaProfileParcelByParcelIdForSystem(**kwargs):
    return CatalystClient().GetAaaProfileParcelByParcelIdForSystem(**kwargs)

@register('GetBannerProfileParcelForSystem')
def GetBannerProfileParcelForSystem(**kwargs):
    return CatalystClient().GetBannerProfileParcelForSystem(**kwargs)

@register('GetBannerProfileParcelByParcelIdForSystem')
def GetBannerProfileParcelByParcelIdForSystem(**kwargs):
    return CatalystClient().GetBannerProfileParcelByParcelIdForSystem(**kwargs)

@register('GetBasicProfileFeatureForSystem')
def GetBasicProfileFeatureForSystem(**kwargs):
    return CatalystClient().GetBasicProfileFeatureForSystem(**kwargs)

@register('GetBasicProfileFeatureByFeatureIdForSystem')
def GetBasicProfileFeatureByFeatureIdForSystem(**kwargs):
    return CatalystClient().GetBasicProfileFeatureByFeatureIdForSystem(**kwargs)

@register('GetBfdProfileParcelForSystem')
def GetBfdProfileParcelForSystem(**kwargs):
    return CatalystClient().GetBfdProfileParcelForSystem(**kwargs)

@register('GetBfdProfileParcelByParcelIdForSystem')
def GetBfdProfileParcelByParcelIdForSystem(**kwargs):
    return CatalystClient().GetBfdProfileParcelByParcelIdForSystem(**kwargs)

@register('GetGlobalProfileParcelForSystem')
def GetGlobalProfileParcelForSystem(**kwargs):
    return CatalystClient().GetGlobalProfileParcelForSystem(**kwargs)

@register('GetGlobalProfileParcelByParcelIdForSystem')
def GetGlobalProfileParcelByParcelIdForSystem(**kwargs):
    return CatalystClient().GetGlobalProfileParcelByParcelIdForSystem(**kwargs)

@register('GetLoggingProfileParcelForSystem')
def GetLoggingProfileParcelForSystem(**kwargs):
    return CatalystClient().GetLoggingProfileParcelForSystem(**kwargs)

@register('GetLoggingProfileParcelByParcelIdForSystem')
def GetLoggingProfileParcelByParcelIdForSystem(**kwargs):
    return CatalystClient().GetLoggingProfileParcelByParcelIdForSystem(**kwargs)

@register('GetMrfProfileParcelForSystem')
def GetMrfProfileParcelForSystem(**kwargs):
    return CatalystClient().GetMrfProfileParcelForSystem(**kwargs)

@register('GetMrfProfileParcelByParcelIdForSystem')
def GetMrfProfileParcelByParcelIdForSystem(**kwargs):
    return CatalystClient().GetMrfProfileParcelByParcelIdForSystem(**kwargs)

@register('GetNtpProfileParcelForSystem')
def GetNtpProfileParcelForSystem(**kwargs):
    return CatalystClient().GetNtpProfileParcelForSystem(**kwargs)

@register('GetNtpProfileParcelByParcelIdForSystem')
def GetNtpProfileParcelByParcelIdForSystem(**kwargs):
    return CatalystClient().GetNtpProfileParcelByParcelIdForSystem(**kwargs)

@register('GetOmpProfileParcelForSystem')
def GetOmpProfileParcelForSystem(**kwargs):
    return CatalystClient().GetOmpProfileParcelForSystem(**kwargs)

@register('GetOmpProfileParcelByParcelIdForSystem')
def GetOmpProfileParcelByParcelIdForSystem(**kwargs):
    return CatalystClient().GetOmpProfileParcelByParcelIdForSystem(**kwargs)

@register('GetSecurityForSystem')
def GetSecurityForSystem(**kwargs):
    return CatalystClient().GetSecurityForSystem(**kwargs)

@register('GetSecurityBySecurityIdForSystem')
def GetSecurityBySecurityIdForSystem(**kwargs):
    return CatalystClient().GetSecurityBySecurityIdForSystem(**kwargs)

@register('GetSnmpProfileParcelForSystem')
def GetSnmpProfileParcelForSystem(**kwargs):
    return CatalystClient().GetSnmpProfileParcelForSystem(**kwargs)

@register('GetSnmpProfileParcelByParcelIdForSystem')
def GetSnmpProfileParcelByParcelIdForSystem(**kwargs):
    return CatalystClient().GetSnmpProfileParcelByParcelIdForSystem(**kwargs)

@register('GetSdwanTransportFeatureProfiles')
def GetSdwanTransportFeatureProfiles(**kwargs):
    return CatalystClient().GetSdwanTransportFeatureProfiles(**kwargs)

@register('GetSdwanTransportCellularControllerParcelSchemaBySchemaType')
def GetSdwanTransportCellularControllerParcelSchemaBySchemaType(**kwargs):
    return CatalystClient().GetSdwanTransportCellularControllerParcelSchemaBySchemaType(**kwargs)

@register('GetSdwanTransportCellularProfileParcelSchemaBySchemaType')
def GetSdwanTransportCellularProfileParcelSchemaBySchemaType(**kwargs):
    return CatalystClient().GetSdwanTransportCellularProfileParcelSchemaBySchemaType(**kwargs)

@register('GetSdwanTransportIpv6TrackerParcelSchemaBySchemaType')
def GetSdwanTransportIpv6TrackerParcelSchemaBySchemaType(**kwargs):
    return CatalystClient().GetSdwanTransportIpv6TrackerParcelSchemaBySchemaType(**kwargs)

@register('GetCedgeTransportIpv6TrackerGroupParcelSchemaBySchemaType')
def GetCedgeTransportIpv6TrackerGroupParcelSchemaBySchemaType(**kwargs):
    return CatalystClient().GetCedgeTransportIpv6TrackerGroupParcelSchemaBySchemaType(**kwargs)

@register('GetSdwanTransportManagementVpnInterfaceEthernetParcelSchemaBySchema')
def GetSdwanTransportManagementVpnInterfaceEthernetParcelSchemaBySchema(**kwargs):
    return CatalystClient().GetSdwanTransportManagementVpnInterfaceEthernetParcelSchemaBySchema(**kwargs)

@register('GetSdwanTransportManagementVpnParcelSchemaBySchemaType')
def GetSdwanTransportManagementVpnParcelSchemaBySchemaType(**kwargs):
    return CatalystClient().GetSdwanTransportManagementVpnParcelSchemaBySchemaType(**kwargs)

@register('GetSdwanTransportRoutingBgpParcelSchemaBySchemaType')
def GetSdwanTransportRoutingBgpParcelSchemaBySchemaType(**kwargs):
    return CatalystClient().GetSdwanTransportRoutingBgpParcelSchemaBySchemaType(**kwargs)

@register('GetCedgeTransportT1e1controllerParcelSchemaBySchemaType')
def GetCedgeTransportT1e1controllerParcelSchemaBySchemaType(**kwargs):
    return CatalystClient().GetCedgeTransportT1e1controllerParcelSchemaBySchemaType(**kwargs)

@register('GetSdwanTransportTrackerParcelSchemaBySchemaType')
def GetSdwanTransportTrackerParcelSchemaBySchemaType(**kwargs):
    return CatalystClient().GetSdwanTransportTrackerParcelSchemaBySchemaType(**kwargs)

@register('GetCedgeTransportTrackerGroupParcelSchemaBySchemaType')
def GetCedgeTransportTrackerGroupParcelSchemaBySchemaType(**kwargs):
    return CatalystClient().GetCedgeTransportTrackerGroupParcelSchemaBySchemaType(**kwargs)

@register('GetSdwanTransportWanVpnCellularInterfaceParcelSchemaBySchema')
def GetSdwanTransportWanVpnCellularInterfaceParcelSchemaBySchema(**kwargs):
    return CatalystClient().GetSdwanTransportWanVpnCellularInterfaceParcelSchemaBySchema(**kwargs)

@register('GetSdwanTransportWanVpnInterfaceEthernetParcelSchemaBySchema')
def GetSdwanTransportWanVpnInterfaceEthernetParcelSchemaBySchema(**kwargs):
    return CatalystClient().GetSdwanTransportWanVpnInterfaceEthernetParcelSchemaBySchema(**kwargs)

@register('GetCedgeTransportWanVpnInterfaceGreParcelSchemaBySchema')
def GetCedgeTransportWanVpnInterfaceGreParcelSchemaBySchema(**kwargs):
    return CatalystClient().GetCedgeTransportWanVpnInterfaceGreParcelSchemaBySchema(**kwargs)

@register('getSdwanProfileParcelSchema_1')
def getSdwanProfileParcelSchema_1(**kwargs):
    return CatalystClient().getSdwanProfileParcelSchema_1(**kwargs)

@register('GetCedgeTransportWanVpnInterfaceSerialParcelSchemaBySchema')
def GetCedgeTransportWanVpnInterfaceSerialParcelSchemaBySchema(**kwargs):
    return CatalystClient().GetCedgeTransportWanVpnInterfaceSerialParcelSchemaBySchema(**kwargs)

@register('GetSdwanTransportWanVpnParcelSchemaBySchemaType')
def GetSdwanTransportWanVpnParcelSchemaBySchemaType(**kwargs):
    return CatalystClient().GetSdwanTransportWanVpnParcelSchemaBySchemaType(**kwargs)

@register('GetSdwanTransportFeatureProfileByProfileId')
def GetSdwanTransportFeatureProfileByProfileId(**kwargs):
    return CatalystClient().GetSdwanTransportFeatureProfileByProfileId(**kwargs)

@register('GetCellularControllerProfileParcelForTransport')
def GetCellularControllerProfileParcelForTransport(**kwargs):
    return CatalystClient().GetCellularControllerProfileParcelForTransport(**kwargs)

@register('GetCellularControllerProfileParcelByParcelIdForTransport')
def GetCellularControllerProfileParcelByParcelIdForTransport(**kwargs):
    return CatalystClient().GetCellularControllerProfileParcelByParcelIdForTransport(**kwargs)

@register('GetCellularControllerAssociatedCellularProfileParcelsForTransport')
def GetCellularControllerAssociatedCellularProfileParcelsForTransport(**kwargs):
    return CatalystClient().GetCellularControllerAssociatedCellularProfileParcelsForTransport(**kwargs)

@register('GetCellularControllerAssociatedCellularProfileParcelByParcelIdForTransport')
def GetCellularControllerAssociatedCellularProfileParcelByParcelIdForTransport(**kwargs):
    return CatalystClient().GetCellularControllerAssociatedCellularProfileParcelByParcelIdForTransport(**kwargs)

@register('GetCellularControllerAssociatedGpsParcelsForTransport')
def GetCellularControllerAssociatedGpsParcelsForTransport(**kwargs):
    return CatalystClient().GetCellularControllerAssociatedGpsParcelsForTransport(**kwargs)

@register('GetCellularControllerAssociatedGpsParcelByParcelIdForTransport')
def GetCellularControllerAssociatedGpsParcelByParcelIdForTransport(**kwargs):
    return CatalystClient().GetCellularControllerAssociatedGpsParcelByParcelIdForTransport(**kwargs)

@register('GetCellularProfileProfileParcelForTransport')
def GetCellularProfileProfileParcelForTransport(**kwargs):
    return CatalystClient().GetCellularProfileProfileParcelForTransport(**kwargs)

@register('GetCellularProfileProfileParcelByParcelIdForTransport')
def GetCellularProfileProfileParcelByParcelIdForTransport(**kwargs):
    return CatalystClient().GetCellularProfileProfileParcelByParcelIdForTransport(**kwargs)

@register('GetEsimCellularControllerProfileFeatureForTransport')
def GetEsimCellularControllerProfileFeatureForTransport(**kwargs):
    return CatalystClient().GetEsimCellularControllerProfileFeatureForTransport(**kwargs)

@register('GetEsimCellularControllerProfileFeatureByFeatureIdForTransport')
def GetEsimCellularControllerProfileFeatureByFeatureIdForTransport(**kwargs):
    return CatalystClient().GetEsimCellularControllerProfileFeatureByFeatureIdForTransport(**kwargs)

@register('GetEsimCellularProfileProfileFeatureForTransport')
def GetEsimCellularProfileProfileFeatureForTransport(**kwargs):
    return CatalystClient().GetEsimCellularProfileProfileFeatureForTransport(**kwargs)

@register('GetEsimCellularProfileByFeatureIdForTransport')
def GetEsimCellularProfileByFeatureIdForTransport(**kwargs):
    return CatalystClient().GetEsimCellularProfileByFeatureIdForTransport(**kwargs)

@register('GetGpsProfileParcelForTransport')
def GetGpsProfileParcelForTransport(**kwargs):
    return CatalystClient().GetGpsProfileParcelForTransport(**kwargs)

@register('GetGpsProfileParcelByParcelIdForTransport')
def GetGpsProfileParcelByParcelIdForTransport(**kwargs):
    return CatalystClient().GetGpsProfileParcelByParcelIdForTransport(**kwargs)

@register('GetIpv6TrackerProfileParcelForTransport')
def GetIpv6TrackerProfileParcelForTransport(**kwargs):
    return CatalystClient().GetIpv6TrackerProfileParcelForTransport(**kwargs)

@register('GetIpv6TrackerProfileParcelByParcelIdForTransport')
def GetIpv6TrackerProfileParcelByParcelIdForTransport(**kwargs):
    return CatalystClient().GetIpv6TrackerProfileParcelByParcelIdForTransport(**kwargs)

@register('GetIpv6TrackerGroupProfileParcelForTransport')
def GetIpv6TrackerGroupProfileParcelForTransport(**kwargs):
    return CatalystClient().GetIpv6TrackerGroupProfileParcelForTransport(**kwargs)

@register('GetIpv6TrackerGroupProfileParcelByParcelIdForTransport')
def GetIpv6TrackerGroupProfileParcelByParcelIdForTransport(**kwargs):
    return CatalystClient().GetIpv6TrackerGroupProfileParcelByParcelIdForTransport(**kwargs)

@register('GetManagementVpnProfileParcelForTransport')
def GetManagementVpnProfileParcelForTransport(**kwargs):
    return CatalystClient().GetManagementVpnProfileParcelForTransport(**kwargs)

@register('GetManagementVpnProfileParcelByParcelIdForTransport')
def GetManagementVpnProfileParcelByParcelIdForTransport(**kwargs):
    return CatalystClient().GetManagementVpnProfileParcelByParcelIdForTransport(**kwargs)

@register('GetInterfaceEthernetParcelsForTransportManagementVpn')
def GetInterfaceEthernetParcelsForTransportManagementVpn(**kwargs):
    return CatalystClient().GetInterfaceEthernetParcelsForTransportManagementVpn(**kwargs)

@register('GetManagementVpnInterfaceEthernetParcelByParcelIdForTransport')
def GetManagementVpnInterfaceEthernetParcelByParcelIdForTransport(**kwargs):
    return CatalystClient().GetManagementVpnInterfaceEthernetParcelByParcelIdForTransport(**kwargs)

@register('GetRoutingBgpProfileParcelForTransport')
def GetRoutingBgpProfileParcelForTransport(**kwargs):
    return CatalystClient().GetRoutingBgpProfileParcelForTransport(**kwargs)

@register('GetRoutingBgpProfileParcelByParcelIdForTransport')
def GetRoutingBgpProfileParcelByParcelIdForTransport(**kwargs):
    return CatalystClient().GetRoutingBgpProfileParcelByParcelIdForTransport(**kwargs)

@register('GetRoutingOspfProfileParcelForTransport')
def GetRoutingOspfProfileParcelForTransport(**kwargs):
    return CatalystClient().GetRoutingOspfProfileParcelForTransport(**kwargs)

@register('GetRoutingOspfProfileParcelByParcelIdForTransport')
def GetRoutingOspfProfileParcelByParcelIdForTransport(**kwargs):
    return CatalystClient().GetRoutingOspfProfileParcelByParcelIdForTransport(**kwargs)

@register('GetRoutingOspfv3Ipv4AfProfileParcelForTransport')
def GetRoutingOspfv3Ipv4AfProfileParcelForTransport(**kwargs):
    return CatalystClient().GetRoutingOspfv3Ipv4AfProfileParcelForTransport(**kwargs)

@register('GetRoutingOspfv3Ipv4AfProfileParcelByParcelIdForTransport')
def GetRoutingOspfv3Ipv4AfProfileParcelByParcelIdForTransport(**kwargs):
    return CatalystClient().GetRoutingOspfv3Ipv4AfProfileParcelByParcelIdForTransport(**kwargs)

@register('GetRoutingOspfv3Ipv6AfProfileParcelForTransport')
def GetRoutingOspfv3Ipv6AfProfileParcelForTransport(**kwargs):
    return CatalystClient().GetRoutingOspfv3Ipv6AfProfileParcelForTransport(**kwargs)

@register('GetRoutingOspfv3Ipv6AfProfileParcelByParcelIdForTransport')
def GetRoutingOspfv3Ipv6AfProfileParcelByParcelIdForTransport(**kwargs):
    return CatalystClient().GetRoutingOspfv3Ipv6AfProfileParcelByParcelIdForTransport(**kwargs)

@register('GetT1e1controllerProfileParcelForTransport')
def GetT1e1controllerProfileParcelForTransport(**kwargs):
    return CatalystClient().GetT1e1controllerProfileParcelForTransport(**kwargs)

@register('GetT1e1controllerProfileParcelByParcelIdForTransport')
def GetT1e1controllerProfileParcelByParcelIdForTransport(**kwargs):
    return CatalystClient().GetT1e1controllerProfileParcelByParcelIdForTransport(**kwargs)

@register('GetTrackerProfileParcelForTransport')
def GetTrackerProfileParcelForTransport(**kwargs):
    return CatalystClient().GetTrackerProfileParcelForTransport(**kwargs)

@register('GetTrackerProfileParcelByParcelIdForTransport')
def GetTrackerProfileParcelByParcelIdForTransport(**kwargs):
    return CatalystClient().GetTrackerProfileParcelByParcelIdForTransport(**kwargs)

@register('GetTrackerGroupProfileParcelForTransport')
def GetTrackerGroupProfileParcelForTransport(**kwargs):
    return CatalystClient().GetTrackerGroupProfileParcelForTransport(**kwargs)

@register('GetTrackerGroupProfileParcelByParcelIdForTransport')
def GetTrackerGroupProfileParcelByParcelIdForTransport(**kwargs):
    return CatalystClient().GetTrackerGroupProfileParcelByParcelIdForTransport(**kwargs)

@register('GetWanVpnProfileParcelForTransport')
def GetWanVpnProfileParcelForTransport(**kwargs):
    return CatalystClient().GetWanVpnProfileParcelForTransport(**kwargs)

@register('GetWanVpnProfileParcelByParcelIdForTransport')
def GetWanVpnProfileParcelByParcelIdForTransport(**kwargs):
    return CatalystClient().GetWanVpnProfileParcelByParcelIdForTransport(**kwargs)

@register('GetInterfaceCellularParcelsForTransportWanVpn')
def GetInterfaceCellularParcelsForTransportWanVpn(**kwargs):
    return CatalystClient().GetInterfaceCellularParcelsForTransportWanVpn(**kwargs)

@register('GetWanVpnInterfaceCellularAssociatedIpv6TrackerParcelsForTransport')
def GetWanVpnInterfaceCellularAssociatedIpv6TrackerParcelsForTransport(**kwargs):
    return CatalystClient().GetWanVpnInterfaceCellularAssociatedIpv6TrackerParcelsForTransport(**kwargs)

@register('GetWanVpnInterfaceCellularAssociatedIpv6TrackerParcelByParcelIdForTransport')
def GetWanVpnInterfaceCellularAssociatedIpv6TrackerParcelByParcelIdForTransport(**kwargs):
    return CatalystClient().GetWanVpnInterfaceCellularAssociatedIpv6TrackerParcelByParcelIdForTransport(**kwargs)

@register('GetWanVpnInterfaceCellularAssociatedIpv6TrackerGroupParcelsForTransport')
def GetWanVpnInterfaceCellularAssociatedIpv6TrackerGroupParcelsForTransport(**kwargs):
    return CatalystClient().GetWanVpnInterfaceCellularAssociatedIpv6TrackerGroupParcelsForTransport(**kwargs)

@register('GetWanVpnInterfaceCellularAssociatedIpv6TrackerGroupParcelByParcelIdForTransport')
def GetWanVpnInterfaceCellularAssociatedIpv6TrackerGroupParcelByParcelIdForTransport(**kwargs):
    return CatalystClient().GetWanVpnInterfaceCellularAssociatedIpv6TrackerGroupParcelByParcelIdForTransport(**kwargs)

@register('GetWanVpnInterfaceCellularAssociatedTrackerParcelsForTransport')
def GetWanVpnInterfaceCellularAssociatedTrackerParcelsForTransport(**kwargs):
    return CatalystClient().GetWanVpnInterfaceCellularAssociatedTrackerParcelsForTransport(**kwargs)

@register('GetWanVpnInterfaceCellularAssociatedTrackerParcelByParcelIdForTransport')
def GetWanVpnInterfaceCellularAssociatedTrackerParcelByParcelIdForTransport(**kwargs):
    return CatalystClient().GetWanVpnInterfaceCellularAssociatedTrackerParcelByParcelIdForTransport(**kwargs)

@register('GetWanVpnInterfaceCellularAssociatedTrackerGroupParcelsForTransport')
def GetWanVpnInterfaceCellularAssociatedTrackerGroupParcelsForTransport(**kwargs):
    return CatalystClient().GetWanVpnInterfaceCellularAssociatedTrackerGroupParcelsForTransport(**kwargs)

@register('GetWanVpnInterfaceCellularAssociatedTrackerGroupParcelByParcelIdForTransport')
def GetWanVpnInterfaceCellularAssociatedTrackerGroupParcelByParcelIdForTransport(**kwargs):
    return CatalystClient().GetWanVpnInterfaceCellularAssociatedTrackerGroupParcelByParcelIdForTransport(**kwargs)

@register('GetWanVpnInterfaceCellularParcelByParcelIdForTransport')
def GetWanVpnInterfaceCellularParcelByParcelIdForTransport(**kwargs):
    return CatalystClient().GetWanVpnInterfaceCellularParcelByParcelIdForTransport(**kwargs)

@register('GetInterfaceEthernetParcelsForTransportWanVpn')
def GetInterfaceEthernetParcelsForTransportWanVpn(**kwargs):
    return CatalystClient().GetInterfaceEthernetParcelsForTransportWanVpn(**kwargs)

@register('GetWanVpnInterfaceEthernetParcelByParcelIdForTransport')
def GetWanVpnInterfaceEthernetParcelByParcelIdForTransport(**kwargs):
    return CatalystClient().GetWanVpnInterfaceEthernetParcelByParcelIdForTransport(**kwargs)

@register('GetWanVpnInterfaceEthernetAssociatedIpv6TrackerParcelsForTransport')
def GetWanVpnInterfaceEthernetAssociatedIpv6TrackerParcelsForTransport(**kwargs):
    return CatalystClient().GetWanVpnInterfaceEthernetAssociatedIpv6TrackerParcelsForTransport(**kwargs)

@register('GetWanVpnInterfaceEthernetAssociatedIpv6TrackerParcelByParcelIdForTransport')
def GetWanVpnInterfaceEthernetAssociatedIpv6TrackerParcelByParcelIdForTransport(**kwargs):
    return CatalystClient().GetWanVpnInterfaceEthernetAssociatedIpv6TrackerParcelByParcelIdForTransport(**kwargs)

@register('GetWanVpnInterfaceEthernetAssociatedIpv6TrackerGroupParcelsForTransport')
def GetWanVpnInterfaceEthernetAssociatedIpv6TrackerGroupParcelsForTransport(**kwargs):
    return CatalystClient().GetWanVpnInterfaceEthernetAssociatedIpv6TrackerGroupParcelsForTransport(**kwargs)

@register('GetWanVpnInterfaceEthernetAssociatedIpv6TrackerGroupParcelByParcelIdForTransport')
def GetWanVpnInterfaceEthernetAssociatedIpv6TrackerGroupParcelByParcelIdForTransport(**kwargs):
    return CatalystClient().GetWanVpnInterfaceEthernetAssociatedIpv6TrackerGroupParcelByParcelIdForTransport(**kwargs)

@register('GetWanVpnInterfaceEthernetAssociatedTrackerParcelsForTransport')
def GetWanVpnInterfaceEthernetAssociatedTrackerParcelsForTransport(**kwargs):
    return CatalystClient().GetWanVpnInterfaceEthernetAssociatedTrackerParcelsForTransport(**kwargs)

@register('GetWanVpnInterfaceEthernetAssociatedTrackerParcelByParcelIdForTransport')
def GetWanVpnInterfaceEthernetAssociatedTrackerParcelByParcelIdForTransport(**kwargs):
    return CatalystClient().GetWanVpnInterfaceEthernetAssociatedTrackerParcelByParcelIdForTransport(**kwargs)

@register('GetWanVpnInterfaceEthernetAssociatedTrackerGroupParcelsForTransport')
def GetWanVpnInterfaceEthernetAssociatedTrackerGroupParcelsForTransport(**kwargs):
    return CatalystClient().GetWanVpnInterfaceEthernetAssociatedTrackerGroupParcelsForTransport(**kwargs)

@register('GetWanVpnInterfaceEthernetAssociatedTrackerGroupParcelByParcelIdForTransport')
def GetWanVpnInterfaceEthernetAssociatedTrackerGroupParcelByParcelIdForTransport(**kwargs):
    return CatalystClient().GetWanVpnInterfaceEthernetAssociatedTrackerGroupParcelByParcelIdForTransport(**kwargs)

@register('GetInterfaceGreParcelsForTransportWanVpn')
def GetInterfaceGreParcelsForTransportWanVpn(**kwargs):
    return CatalystClient().GetInterfaceGreParcelsForTransportWanVpn(**kwargs)

@register('GetWanVpnInterfaceGreParcelByParcelIdForTransport')
def GetWanVpnInterfaceGreParcelByParcelIdForTransport(**kwargs):
    return CatalystClient().GetWanVpnInterfaceGreParcelByParcelIdForTransport(**kwargs)

@register('GetWanVpnInterfaceGreAssociatedTrackerParcelsForTransport')
def GetWanVpnInterfaceGreAssociatedTrackerParcelsForTransport(**kwargs):
    return CatalystClient().GetWanVpnInterfaceGreAssociatedTrackerParcelsForTransport(**kwargs)

@register('GetWanVpnInterfaceGreAssociatedTrackerParcelByParcelIdForTransport')
def GetWanVpnInterfaceGreAssociatedTrackerParcelByParcelIdForTransport(**kwargs):
    return CatalystClient().GetWanVpnInterfaceGreAssociatedTrackerParcelByParcelIdForTransport(**kwargs)

@register('getListOfProfileParcels_1')
def getListOfProfileParcels_1(**kwargs):
    return CatalystClient().getListOfProfileParcels_1(**kwargs)

@register('getProfileParcelByParcelId_1')
def getProfileParcelByParcelId_1(**kwargs):
    return CatalystClient().getProfileParcelByParcelId_1(**kwargs)

@register('GetWanVpnInterfaceIpsecAssociatedTrackerParcelsForTransport')
def GetWanVpnInterfaceIpsecAssociatedTrackerParcelsForTransport(**kwargs):
    return CatalystClient().GetWanVpnInterfaceIpsecAssociatedTrackerParcelsForTransport(**kwargs)

@register('GetWanVpnInterfaceIpsecAssociatedTrackerParcelByParcelIdForTransport')
def GetWanVpnInterfaceIpsecAssociatedTrackerParcelByParcelIdForTransport(**kwargs):
    return CatalystClient().GetWanVpnInterfaceIpsecAssociatedTrackerParcelByParcelIdForTransport(**kwargs)

@register('GetInterfaceSerialParcelsForTransportWanVpn')
def GetInterfaceSerialParcelsForTransportWanVpn(**kwargs):
    return CatalystClient().GetInterfaceSerialParcelsForTransportWanVpn(**kwargs)

@register('GetWanVpnInterfaceSerialParcelByParcelIdForTransport')
def GetWanVpnInterfaceSerialParcelByParcelIdForTransport(**kwargs):
    return CatalystClient().GetWanVpnInterfaceSerialParcelByParcelIdForTransport(**kwargs)

@register('GetWanVpnAssociatedRoutingBgpParcelsForTransport')
def GetWanVpnAssociatedRoutingBgpParcelsForTransport(**kwargs):
    return CatalystClient().GetWanVpnAssociatedRoutingBgpParcelsForTransport(**kwargs)

@register('GetWanVpnAssociatedRoutingBgpParcelByParcelIdForTransport')
def GetWanVpnAssociatedRoutingBgpParcelByParcelIdForTransport(**kwargs):
    return CatalystClient().GetWanVpnAssociatedRoutingBgpParcelByParcelIdForTransport(**kwargs)

@register('GetWanVpnAssociatedRoutingOspfParcelsForTransport')
def GetWanVpnAssociatedRoutingOspfParcelsForTransport(**kwargs):
    return CatalystClient().GetWanVpnAssociatedRoutingOspfParcelsForTransport(**kwargs)

@register('GetWanVpnAssociatedRoutingOspfParcelByParcelIdForTransport')
def GetWanVpnAssociatedRoutingOspfParcelByParcelIdForTransport(**kwargs):
    return CatalystClient().GetWanVpnAssociatedRoutingOspfParcelByParcelIdForTransport(**kwargs)

@register('GetWanVpnAssociatedRoutingOspfv3IPv4AfParcelsForTransport')
def GetWanVpnAssociatedRoutingOspfv3IPv4AfParcelsForTransport(**kwargs):
    return CatalystClient().GetWanVpnAssociatedRoutingOspfv3IPv4AfParcelsForTransport(**kwargs)

@register('GetWanVpnAssociatedRoutingOspfv3IPv4AfParcelByParcelIdForTransport')
def GetWanVpnAssociatedRoutingOspfv3IPv4AfParcelByParcelIdForTransport(**kwargs):
    return CatalystClient().GetWanVpnAssociatedRoutingOspfv3IPv4AfParcelByParcelIdForTransport(**kwargs)

@register('GetWanVpnAssociatedRoutingOspfv3IPv6AfParcelsForTransport')
def GetWanVpnAssociatedRoutingOspfv3IPv6AfParcelsForTransport(**kwargs):
    return CatalystClient().GetWanVpnAssociatedRoutingOspfv3IPv6AfParcelsForTransport(**kwargs)

@register('GetWanVpnAssociatedRoutingOspfv3IPv6AfParcelByParcelIdForTransport')
def GetWanVpnAssociatedRoutingOspfv3IPv6AfParcelByParcelIdForTransport(**kwargs):
    return CatalystClient().GetWanVpnAssociatedRoutingOspfv3IPv6AfParcelByParcelIdForTransport(**kwargs)

@register('getMSLADevices')
def getMSLADevices(**kwargs):
    return CatalystClient().getMSLADevices(**kwargs)

@register('getLicenseByUuid')
def getLicenseByUuid(**kwargs):
    return CatalystClient().getLicenseByUuid(**kwargs)

@register('GetPolicyGroupBySolution')
def GetPolicyGroupBySolution(**kwargs):
    return CatalystClient().GetPolicyGroupBySolution(**kwargs)

@register('GetPolicyGroup')
def GetPolicyGroup(**kwargs):
    return CatalystClient().GetPolicyGroup(**kwargs)

@register('GetPolicyGroupAssociation')
def GetPolicyGroupAssociation(**kwargs):
    return CatalystClient().GetPolicyGroupAssociation(**kwargs)

@register('getPolicyGroupDeviceVariables')
def getPolicyGroupDeviceVariables(**kwargs):
    return CatalystClient().getPolicyGroupDeviceVariables(**kwargs)

@register('getPolicyGroupDeviceVariablesSchema')
def getPolicyGroupDeviceVariablesSchema(**kwargs):
    return CatalystClient().getPolicyGroupDeviceVariablesSchema(**kwargs)

@register('getAllReportTemplates')
def getAllReportTemplates(**kwargs):
    return CatalystClient().getAllReportTemplates(**kwargs)

@register('downloadReportPreviewFile')
def downloadReportPreviewFile(**kwargs):
    return CatalystClient().downloadReportPreviewFile(**kwargs)

@register('getReportTemplateById')
def getReportTemplateById(**kwargs):
    return CatalystClient().getReportTemplateById(**kwargs)

@register('getAllReportTasksByReportId')
def getAllReportTasksByReportId(**kwargs):
    return CatalystClient().getAllReportTasksByReportId(**kwargs)

@register('downloadReportDataFile')
def downloadReportDataFile(**kwargs):
    return CatalystClient().downloadReportDataFile(**kwargs)

@register('getUrlForSdoIdentityService')
def getUrlForSdoIdentityService(**kwargs):
    return CatalystClient().getUrlForSdoIdentityService(**kwargs)

@register('getAllAccounts')
def getAllAccounts(**kwargs):
    return CatalystClient().getAllAccounts(**kwargs)

@register('getRatePlansByAcctId')
def getRatePlansByAcctId(**kwargs):
    return CatalystClient().getRatePlansByAcctId(**kwargs)

@register('getProvidersInfo')
def getProvidersInfo(**kwargs):
    return CatalystClient().getProvidersInfo(**kwargs)

@register('getCommPlansByAcctId')
def getCommPlansByAcctId(**kwargs):
    return CatalystClient().getCommPlansByAcctId(**kwargs)

@register('getProviderCredentialsByAccountId')
def getProviderCredentialsByAccountId(**kwargs):
    return CatalystClient().getProviderCredentialsByAccountId(**kwargs)

@register('getDeviceDataUsage')
def getDeviceDataUsage(**kwargs):
    return CatalystClient().getDeviceDataUsage(**kwargs)

@register('serviceChainMapping')
def serviceChainMapping(**kwargs):
    return CatalystClient().serviceChainMapping(**kwargs)

@register('getDevicesForTemplate')
def getDevicesForTemplate(**kwargs):
    return CatalystClient().getDevicesForTemplate(**kwargs)

@register('license')
def license(**kwargs):
    return CatalystClient().license(**kwargs)

@register('getUserSettings')
def getUserSettings(**kwargs):
    return CatalystClient().getUserSettings(**kwargs)

@register('GetTopologyGroupBySolution')
def GetTopologyGroupBySolution(**kwargs):
    return CatalystClient().GetTopologyGroupBySolution(**kwargs)

@register('GetTopologyGroup')
def GetTopologyGroup(**kwargs):
    return CatalystClient().GetTopologyGroup(**kwargs)

@register('generateDeviceInterfaceStatisticsData')
def generateDeviceInterfaceStatisticsData(**kwargs):
    return CatalystClient().generateDeviceInterfaceStatisticsData(**kwargs)

@register('getCountWithInterfaceStatistics')
def getCountWithInterfaceStatistics(**kwargs):
    return CatalystClient().getCountWithInterfaceStatistics(**kwargs)

@register('getStatDataFieldsByInterfaceStatistics')
def getStatDataFieldsByInterfaceStatistics(**kwargs):
    return CatalystClient().getStatDataFieldsByInterfaceStatistics(**kwargs)

@register('getWaniRecommendations')
def getWaniRecommendations(**kwargs):
    return CatalystClient().getWaniRecommendations(**kwargs)

@register('getAppliedWaniRecommendations')
def getAppliedWaniRecommendations(**kwargs):
    return CatalystClient().getAppliedWaniRecommendations(**kwargs)

@register('getListActivationStatus')
def getListActivationStatus(**kwargs):
    return CatalystClient().getListActivationStatus(**kwargs)

@register('getPolicyActivationStatus')
def getPolicyActivationStatus(**kwargs):
    return CatalystClient().getPolicyActivationStatus(**kwargs)

@register('webexAccessCode')
def webexAccessCode(**kwargs):
    return CatalystClient().webexAccessCode(**kwargs)

@register('getWebexDataCentersSyncStatus')
def getWebexDataCentersSyncStatus(**kwargs):
    return CatalystClient().getWebexDataCentersSyncStatus(**kwargs)

@register('redirectWebexDataCenters')
def redirectWebexDataCenters(**kwargs):
    return CatalystClient().redirectWebexDataCenters(**kwargs)
