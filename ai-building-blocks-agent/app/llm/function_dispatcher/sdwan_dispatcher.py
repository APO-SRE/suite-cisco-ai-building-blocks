# app/llm/function_dispatcher/sdwan_dispatcher.py
from app.llm.function_dispatcher import register
from app.llm.platform_clients.sdwan_client import SdwanClient

@register('getSecureXAccessToken')
def getSecureXAccessToken(**kwargs):
    return SdwanClient().getSecureXAccessToken(**kwargs)

@register('getAaaConfig')
def getAaaConfig(**kwargs):
    return SdwanClient().getAaaConfig(**kwargs)

@register('listenAuthEvents')
def listenAuthEvents(**kwargs):
    return SdwanClient().listenAuthEvents(**kwargs)

@register('getRadiusConfig')
def getRadiusConfig(**kwargs):
    return SdwanClient().getRadiusConfig(**kwargs)

@register('getTacacsConfig')
def getTacacsConfig(**kwargs):
    return SdwanClient().getTacacsConfig(**kwargs)

@register('findUsers_1')
def findUsers_1(**kwargs):
    return SdwanClient().findUsers_1(**kwargs)

@register('getActiveSessions_1')
def getActiveSessions_1(**kwargs):
    return SdwanClient().getActiveSessions_1(**kwargs)

@register('findUserRole_1')
def findUserRole_1(**kwargs):
    return SdwanClient().findUserRole_1(**kwargs)

@register('findUserAuthType_1')
def findUserAuthType_1(**kwargs):
    return SdwanClient().findUserAuthType_1(**kwargs)

@register('findUserGroups')
def findUserGroups(**kwargs):
    return SdwanClient().findUserGroups(**kwargs)

@register('createGroupGridColumns')
def createGroupGridColumns(**kwargs):
    return SdwanClient().createGroupGridColumns(**kwargs)

@register('findUserGroupsAsKeyValue')
def findUserGroupsAsKeyValue(**kwargs):
    return SdwanClient().findUserGroupsAsKeyValue(**kwargs)

@register('getVpnGroups')
def getVpnGroups(**kwargs):
    return SdwanClient().getVpnGroups(**kwargs)

@register('getRawAlarmData')
def getRawAlarmData(**kwargs):
    return SdwanClient().getRawAlarmData(**kwargs)

@register('getAggregationData')
def getAggregationData(**kwargs):
    return SdwanClient().getAggregationData(**kwargs)

@register('getNonViewedActiveAlarmsCount')
def getNonViewedActiveAlarmsCount(**kwargs):
    return SdwanClient().getNonViewedActiveAlarmsCount(**kwargs)

@register('listDisabledAlarm')
def listDisabledAlarm(**kwargs):
    return SdwanClient().listDisabledAlarm(**kwargs)

@register('getDocCount')
def getDocCount(**kwargs):
    return SdwanClient().getDocCount(**kwargs)

@register('getAlarmDataFields')
def getAlarmDataFields(**kwargs):
    return SdwanClient().getAlarmDataFields(**kwargs)

@register('getLinkStateAlarmConfig')
def getLinkStateAlarmConfig(**kwargs):
    return SdwanClient().getLinkStateAlarmConfig(**kwargs)

@register('getMasterManagerState')
def getMasterManagerState(**kwargs):
    return SdwanClient().getMasterManagerState(**kwargs)

@register('getNonViewedAlarms')
def getNonViewedAlarms(**kwargs):
    return SdwanClient().getNonViewedAlarms(**kwargs)

@register('getPage')
def getPage(**kwargs):
    return SdwanClient().getPage(**kwargs)

@register('setPeriodicPurgeTimer')
def setPeriodicPurgeTimer(**kwargs):
    return SdwanClient().setPeriodicPurgeTimer(**kwargs)

@register('getAlarmQueryFields')
def getAlarmQueryFields(**kwargs):
    return SdwanClient().getAlarmQueryFields(**kwargs)

@register('getFieldDetails')
def getFieldDetails(**kwargs):
    return SdwanClient().getFieldDetails(**kwargs)

@register('reset')
def reset(**kwargs):
    return SdwanClient().reset(**kwargs)

@register('restartCorrelationEngine')
def restartCorrelationEngine(**kwargs):
    return SdwanClient().restartCorrelationEngine(**kwargs)

@register('getAlarmTypesAsKeyValue')
def getAlarmTypesAsKeyValue(**kwargs):
    return SdwanClient().getAlarmTypesAsKeyValue(**kwargs)

@register('getBySeverity')
def getBySeverity(**kwargs):
    return SdwanClient().getBySeverity(**kwargs)

@register('getAlarmSeverityCustomHistogram')
def getAlarmSeverityCustomHistogram(**kwargs):
    return SdwanClient().getAlarmSeverityCustomHistogram(**kwargs)

@register('getAlarmSeverityMappings')
def getAlarmSeverityMappings(**kwargs):
    return SdwanClient().getAlarmSeverityMappings(**kwargs)

@register('getStats')
def getStats(**kwargs):
    return SdwanClient().getStats(**kwargs)

@register('getDeviceTopic')
def getDeviceTopic(**kwargs):
    return SdwanClient().getDeviceTopic(**kwargs)

@register('getAlarmDetails')
def getAlarmDetails(**kwargs):
    return SdwanClient().getAlarmDetails(**kwargs)

@register('getAllAppList')
def getAllAppList(**kwargs):
    return SdwanClient().getAllAppList(**kwargs)

@register('getAppListCategory')
def getAppListCategory(**kwargs):
    return SdwanClient().getAppListCategory(**kwargs)

@register('getNetworkDiscoveredApps')
def getNetworkDiscoveredApps(**kwargs):
    return SdwanClient().getNetworkDiscoveredApps(**kwargs)

@register('getAttributeMappingForApps')
def getAttributeMappingForApps(**kwargs):
    return SdwanClient().getAttributeMappingForApps(**kwargs)

@register('getKubernetesServices')
def getKubernetesServices(**kwargs):
    return SdwanClient().getKubernetesServices(**kwargs)

@register('getAppByUuid')
def getAppByUuid(**kwargs):
    return SdwanClient().getAppByUuid(**kwargs)

@register('getAppList')
def getAppList(**kwargs):
    return SdwanClient().getAppList(**kwargs)

@register('getKubernetesCluster')
def getKubernetesCluster(**kwargs):
    return SdwanClient().getKubernetesCluster(**kwargs)

@register('getActiveSaasFeeds')
def getActiveSaasFeeds(**kwargs):
    return SdwanClient().getActiveSaasFeeds(**kwargs)

@register('getAllSaasFeedForSelectedApp')
def getAllSaasFeedForSelectedApp(**kwargs):
    return SdwanClient().getAllSaasFeedForSelectedApp(**kwargs)

@register('getStatDataRawAuditLogData')
def getStatDataRawAuditLogData(**kwargs):
    return SdwanClient().getStatDataRawAuditLogData(**kwargs)

@register('getPropertyAggregationData')
def getPropertyAggregationData(**kwargs):
    return SdwanClient().getPropertyAggregationData(**kwargs)

@register('getCount')
def getCount(**kwargs):
    return SdwanClient().getCount(**kwargs)

@register('getStatDataFields')
def getStatDataFields(**kwargs):
    return SdwanClient().getStatDataFields(**kwargs)

@register('getStatBulkRawPropertyData')
def getStatBulkRawPropertyData(**kwargs):
    return SdwanClient().getStatBulkRawPropertyData(**kwargs)

@register('getStatQueryFields')
def getStatQueryFields(**kwargs):
    return SdwanClient().getStatQueryFields(**kwargs)

@register('generateAuditLog')
def generateAuditLog(**kwargs):
    return SdwanClient().generateAuditLog(**kwargs)

@register('getAuditSeverityCustomHistogram')
def getAuditSeverityCustomHistogram(**kwargs):
    return SdwanClient().getAuditSeverityCustomHistogram(**kwargs)

@register('getLocalBackupInfo')
def getLocalBackupInfo(**kwargs):
    return SdwanClient().getLocalBackupInfo(**kwargs)

@register('downloadBackupFile')
def downloadBackupFile(**kwargs):
    return SdwanClient().downloadBackupFile(**kwargs)

@register('listBackup')
def listBackup(**kwargs):
    return SdwanClient().listBackup(**kwargs)

@register('getCdnaSenseService')
def getCdnaSenseService(**kwargs):
    return SdwanClient().getCdnaSenseService(**kwargs)

@register('getCdnaServer')
def getCdnaServer(**kwargs):
    return SdwanClient().getCdnaServer(**kwargs)

@register('getControllerCertStatus')
def getControllerCertStatus(**kwargs):
    return SdwanClient().getControllerCertStatus(**kwargs)

@register('getCSRViewRightMenus')
def getCSRViewRightMenus(**kwargs):
    return SdwanClient().getCSRViewRightMenus(**kwargs)

@register('getDeviceViewRightMenus')
def getDeviceViewRightMenus(**kwargs):
    return SdwanClient().getDeviceViewRightMenus(**kwargs)

@register('getDevicesList')
def getDevicesList(**kwargs):
    return SdwanClient().getDevicesList(**kwargs)

@register('getListStatus')
def getListStatus(**kwargs):
    return SdwanClient().getListStatus(**kwargs)

@register('setvSmartMtHubList')
def setvSmartMtHubList(**kwargs):
    return SdwanClient().setvSmartMtHubList(**kwargs)

@register('getQuarantineBanner')
def getQuarantineBanner(**kwargs):
    return SdwanClient().getQuarantineBanner(**kwargs)

@register('getCertificateData')
def getCertificateData(**kwargs):
    return SdwanClient().getCertificateData(**kwargs)

@register('getRootCertChains')
def getRootCertChains(**kwargs):
    return SdwanClient().getRootCertChains(**kwargs)

@register('getRootCertificate')
def getRootCertificate(**kwargs):
    return SdwanClient().getRootCertificate(**kwargs)

@register('rsaKeyLength2048ForAllDevices')
def rsaKeyLength2048ForAllDevices(**kwargs):
    return SdwanClient().rsaKeyLength2048ForAllDevices(**kwargs)

@register('getCertificateDetail')
def getCertificateDetail(**kwargs):
    return SdwanClient().getCertificateDetail(**kwargs)

@register('getCertificateStats')
def getCertificateStats(**kwargs):
    return SdwanClient().getCertificateStats(**kwargs)

@register('syncvBond')
def syncvBond(**kwargs):
    return SdwanClient().syncvBond(**kwargs)

@register('getTokenList')
def getTokenList(**kwargs):
    return SdwanClient().getTokenList(**kwargs)

@register('getInstalledCert')
def getInstalledCert(**kwargs):
    return SdwanClient().getInstalledCert(**kwargs)

@register('getvEdgeCSR')
def getvEdgeCSR(**kwargs):
    return SdwanClient().getvEdgeCSR(**kwargs)

@register('getvEdgeList')
def getvEdgeList(**kwargs):
    return SdwanClient().getvEdgeList(**kwargs)

@register('getView')
def getView(**kwargs):
    return SdwanClient().getView(**kwargs)

@register('getSelfSignedCert')
def getSelfSignedCert(**kwargs):
    return SdwanClient().getSelfSignedCert(**kwargs)

@register('getvSmartList')
def getvSmartList(**kwargs):
    return SdwanClient().getvSmartList(**kwargs)

@register('createServerInfo')
def createServerInfo(**kwargs):
    return SdwanClient().createServerInfo(**kwargs)

@register('getCsrfToken')
def getCsrfToken(**kwargs):
    return SdwanClient().getCsrfToken(**kwargs)

@register('getAccessTokenforDevice')
def getAccessTokenforDevice(**kwargs):
    return SdwanClient().getAccessTokenforDevice(**kwargs)

@register('connect')
def connect(**kwargs):
    return SdwanClient().connect(**kwargs)

@register('getCloudCredentials')
def getCloudCredentials(**kwargs):
    return SdwanClient().getCloudCredentials(**kwargs)

@register('isStaging')
def isStaging(**kwargs):
    return SdwanClient().isStaging(**kwargs)

@register('getTelemetryState')
def getTelemetryState(**kwargs):
    return SdwanClient().getTelemetryState(**kwargs)

@register('getvAnalyticsDashboardList')
def getvAnalyticsDashboardList(**kwargs):
    return SdwanClient().getvAnalyticsDashboardList(**kwargs)

@register('checkIfClusterLocked')
def checkIfClusterLocked(**kwargs):
    return SdwanClient().checkIfClusterLocked(**kwargs)

@register('getClusterWorkflowVersion')
def getClusterWorkflowVersion(**kwargs):
    return SdwanClient().getClusterWorkflowVersion(**kwargs)

@register('getConnectedDevices')
def getConnectedDevices(**kwargs):
    return SdwanClient().getConnectedDevices(**kwargs)

@register('healthDetails')
def healthDetails(**kwargs):
    return SdwanClient().healthDetails(**kwargs)

@register('healthStatusInfo')
def healthStatusInfo(**kwargs):
    return SdwanClient().healthStatusInfo(**kwargs)

@register('healthSummary')
def healthSummary(**kwargs):
    return SdwanClient().healthSummary(**kwargs)

@register('hostHealthStatus')
def hostHealthStatus(**kwargs):
    return SdwanClient().hostHealthStatus(**kwargs)

@register('getConfiguredIPList')
def getConfiguredIPList(**kwargs):
    return SdwanClient().getConfiguredIPList(**kwargs)

@register('isClusterReady')
def isClusterReady(**kwargs):
    return SdwanClient().isClusterReady(**kwargs)

@register('listVmanages')
def listVmanages(**kwargs):
    return SdwanClient().listVmanages(**kwargs)

@register('nodeProperties')
def nodeProperties(**kwargs):
    return SdwanClient().nodeProperties(**kwargs)

@register('getTenancyMode')
def getTenancyMode(**kwargs):
    return SdwanClient().getTenancyMode(**kwargs)

@register('getTenantsList')
def getTenantsList(**kwargs):
    return SdwanClient().getTenantsList(**kwargs)

@register('getVManageDetails')
def getVManageDetails(**kwargs):
    return SdwanClient().getVManageDetails(**kwargs)

@register('getConnectedDevicesPerTenant')
def getConnectedDevicesPerTenant(**kwargs):
    return SdwanClient().getConnectedDevicesPerTenant(**kwargs)

@register('getvnfByDeviceId')
def getvnfByDeviceId(**kwargs):
    return SdwanClient().getvnfByDeviceId(**kwargs)

@register('getVNFEventsCountDetail')
def getVNFEventsCountDetail(**kwargs):
    return SdwanClient().getVNFEventsCountDetail(**kwargs)

@register('getVNFAlarmCount')
def getVNFAlarmCount(**kwargs):
    return SdwanClient().getVNFAlarmCount(**kwargs)

@register('getVNFEventsDetail')
def getVNFEventsDetail(**kwargs):
    return SdwanClient().getVNFEventsDetail(**kwargs)

@register('getVNFInterfaceDetail')
def getVNFInterfaceDetail(**kwargs):
    return SdwanClient().getVNFInterfaceDetail(**kwargs)

@register('doesValidImageExist')
def doesValidImageExist(**kwargs):
    return SdwanClient().doesValidImageExist(**kwargs)

@register('getContainerInspectData')
def getContainerInspectData(**kwargs):
    return SdwanClient().getContainerInspectData(**kwargs)

@register('getContainerSettings')
def getContainerSettings(**kwargs):
    return SdwanClient().getContainerSettings(**kwargs)

@register('generateDeviceStateData')
def generateDeviceStateData(**kwargs):
    return SdwanClient().generateDeviceStateData(**kwargs)

@register('generateDeviceStateDataFields')
def generateDeviceStateDataFields(**kwargs):
    return SdwanClient().generateDeviceStateDataFields(**kwargs)

@register('generateDeviceStateDataWithQueryString')
def generateDeviceStateDataWithQueryString(**kwargs):
    return SdwanClient().generateDeviceStateDataWithQueryString(**kwargs)

@register('getStatisticsType')
def getStatisticsType(**kwargs):
    return SdwanClient().getStatisticsType(**kwargs)

@register('getActiveAlarms')
def getActiveAlarms(**kwargs):
    return SdwanClient().getActiveAlarms(**kwargs)

@register('generateDeviceStatisticsData')
def generateDeviceStatisticsData(**kwargs):
    return SdwanClient().generateDeviceStatisticsData(**kwargs)

@register('getCountWithStateDataType')
def getCountWithStateDataType(**kwargs):
    return SdwanClient().getCountWithStateDataType(**kwargs)

@register('getStatDataFieldsByStateDataType')
def getStatDataFieldsByStateDataType(**kwargs):
    return SdwanClient().getStatDataFieldsByStateDataType(**kwargs)

@register('getCloudSettings')
def getCloudSettings(**kwargs):
    return SdwanClient().getCloudSettings(**kwargs)

@register('getAccessToken')
def getAccessToken(**kwargs):
    return SdwanClient().getAccessToken(**kwargs)

@register('getIdToken')
def getIdToken(**kwargs):
    return SdwanClient().getIdToken(**kwargs)

@register('getOTP')
def getOTP(**kwargs):
    return SdwanClient().getOTP(**kwargs)

@register('getTelemetrySettings')
def getTelemetrySettings(**kwargs):
    return SdwanClient().getTelemetrySettings(**kwargs)

@register('getDCATenantOwners')
def getDCATenantOwners(**kwargs):
    return SdwanClient().getDCATenantOwners(**kwargs)

@register('getCrashLogsSynced')
def getCrashLogsSynced(**kwargs):
    return SdwanClient().getCrashLogsSynced(**kwargs)

@register('getCloudServicesConfigurationDCA')
def getCloudServicesConfigurationDCA(**kwargs):
    return SdwanClient().getCloudServicesConfigurationDCA(**kwargs)

@register('listAllDevices')
def listAllDevices(**kwargs):
    return SdwanClient().listAllDevices(**kwargs)

@register('getAAAservers')
def getAAAservers(**kwargs):
    return SdwanClient().getAAAservers(**kwargs)

@register('getAAAUsers')
def getAAAUsers(**kwargs):
    return SdwanClient().getAAAUsers(**kwargs)

@register('getACLMatchCounterUsers')
def getACLMatchCounterUsers(**kwargs):
    return SdwanClient().getACLMatchCounterUsers(**kwargs)

@register('generateChangePartitionInfo')
def generateChangePartitionInfo(**kwargs):
    return SdwanClient().generateChangePartitionInfo(**kwargs)

@register('generateDeactivateInfo')
def generateDeactivateInfo(**kwargs):
    return SdwanClient().generateDeactivateInfo(**kwargs)

@register('createFilterVPNList')
def createFilterVPNList(**kwargs):
    return SdwanClient().createFilterVPNList(**kwargs)

@register('getFirmwareImages')
def getFirmwareImages(**kwargs):
    return SdwanClient().getFirmwareImages(**kwargs)

@register('getFirmwareDevices')
def getFirmwareDevices(**kwargs):
    return SdwanClient().getFirmwareDevices(**kwargs)

@register('getFirmwareRemoteImage')
def getFirmwareRemoteImage(**kwargs):
    return SdwanClient().getFirmwareRemoteImage(**kwargs)

@register('getDevicesFWUpgrade')
def getDevicesFWUpgrade(**kwargs):
    return SdwanClient().getDevicesFWUpgrade(**kwargs)

@register('getFirmwareImageDetails')
def getFirmwareImageDetails(**kwargs):
    return SdwanClient().getFirmwareImageDetails(**kwargs)

@register('generateInstallInfo')
def generateInstallInfo(**kwargs):
    return SdwanClient().generateInstallInfo(**kwargs)

@register('generateDeviceList')
def generateDeviceList(**kwargs):
    return SdwanClient().generateDeviceList(**kwargs)

@register('generateDeviceActionList')
def generateDeviceActionList(**kwargs):
    return SdwanClient().generateDeviceActionList(**kwargs)

@register('generateRebootInfo')
def generateRebootInfo(**kwargs):
    return SdwanClient().generateRebootInfo(**kwargs)

@register('generateRebootDeviceList')
def generateRebootDeviceList(**kwargs):
    return SdwanClient().generateRebootDeviceList(**kwargs)

@register('generateRediscoverInfo')
def generateRediscoverInfo(**kwargs):
    return SdwanClient().generateRediscoverInfo(**kwargs)

@register('getRemoteServerList')
def getRemoteServerList(**kwargs):
    return SdwanClient().getRemoteServerList(**kwargs)

@register('getRemoteServerById')
def getRemoteServerById(**kwargs):
    return SdwanClient().getRemoteServerById(**kwargs)

@register('generateRemovePartitionInfo')
def generateRemovePartitionInfo(**kwargs):
    return SdwanClient().generateRemovePartitionInfo(**kwargs)

@register('testApiKey')
def testApiKey(**kwargs):
    return SdwanClient().testApiKey(**kwargs)

@register('generateSecurityDevicesList')
def generateSecurityDevicesList(**kwargs):
    return SdwanClient().generateSecurityDevicesList(**kwargs)

@register('findSoftwareImages')
def findSoftwareImages(**kwargs):
    return SdwanClient().findSoftwareImages(**kwargs)

@register('getImageProperties')
def getImageProperties(**kwargs):
    return SdwanClient().getImageProperties(**kwargs)

@register('findSoftwareImagesWithFilters')
def findSoftwareImagesWithFilters(**kwargs):
    return SdwanClient().findSoftwareImagesWithFilters(**kwargs)

@register('getUploadImagesCount')
def getUploadImagesCount(**kwargs):
    return SdwanClient().getUploadImagesCount(**kwargs)

@register('generateUtdImageData')
def generateUtdImageData(**kwargs):
    return SdwanClient().generateUtdImageData(**kwargs)

@register('downloadPackageFile')
def downloadPackageFile(**kwargs):
    return SdwanClient().downloadPackageFile(**kwargs)

@register('getImageMetadata')
def getImageMetadata(**kwargs):
    return SdwanClient().getImageMetadata(**kwargs)

@register('getImageRemoteServer')
def getImageRemoteServer(**kwargs):
    return SdwanClient().getImageRemoteServer(**kwargs)

@register('findVEdgeSoftwareVersion')
def findVEdgeSoftwareVersion(**kwargs):
    return SdwanClient().findVEdgeSoftwareVersion(**kwargs)

@register('findSoftwareVersion')
def findSoftwareVersion(**kwargs):
    return SdwanClient().findSoftwareVersion(**kwargs)

@register('getVnfProperties')
def getVnfProperties(**kwargs):
    return SdwanClient().getVnfProperties(**kwargs)

@register('findZtpSoftwareVersion')
def findZtpSoftwareVersion(**kwargs):
    return SdwanClient().findZtpSoftwareVersion(**kwargs)

@register('triggerPendingTasksMonitoring')
def triggerPendingTasksMonitoring(**kwargs):
    return SdwanClient().triggerPendingTasksMonitoring(**kwargs)

@register('cleanStatus')
def cleanStatus(**kwargs):
    return SdwanClient().cleanStatus(**kwargs)

@register('getMaintenanceWindowFlag')
def getMaintenanceWindowFlag(**kwargs):
    return SdwanClient().getMaintenanceWindowFlag(**kwargs)

@register('findRunningTasks')
def findRunningTasks(**kwargs):
    return SdwanClient().findRunningTasks(**kwargs)

@register('getActiveTaskCount')
def getActiveTaskCount(**kwargs):
    return SdwanClient().getActiveTaskCount(**kwargs)

@register('getCleanStatus')
def getCleanStatus(**kwargs):
    return SdwanClient().getCleanStatus(**kwargs)

@register('findStatus')
def findStatus(**kwargs):
    return SdwanClient().findStatus(**kwargs)

@register('testIoxConfig')
def testIoxConfig(**kwargs):
    return SdwanClient().testIoxConfig(**kwargs)

@register('createVPNList')
def createVPNList(**kwargs):
    return SdwanClient().createVPNList(**kwargs)

@register('getZTPUpgradeConfig')
def getZTPUpgradeConfig(**kwargs):
    return SdwanClient().getZTPUpgradeConfig(**kwargs)

@register('getZTPUpgradeConfigSetting')
def getZTPUpgradeConfigSetting(**kwargs):
    return SdwanClient().getZTPUpgradeConfigSetting(**kwargs)

@register('getAppHostingAttachedDevices')
def getAppHostingAttachedDevices(**kwargs):
    return SdwanClient().getAppHostingAttachedDevices(**kwargs)

@register('getAppHostingDetails')
def getAppHostingDetails(**kwargs):
    return SdwanClient().getAppHostingDetails(**kwargs)

@register('getAppHostingGuestRoutes')
def getAppHostingGuestRoutes(**kwargs):
    return SdwanClient().getAppHostingGuestRoutes(**kwargs)

@register('getAppHostingNetworkDevices')
def getAppHostingNetworkDevices(**kwargs):
    return SdwanClient().getAppHostingNetworkDevices(**kwargs)

@register('getAppHostingNetworkUtils')
def getAppHostingNetworkUtils(**kwargs):
    return SdwanClient().getAppHostingNetworkUtils(**kwargs)

@register('getAppHostingProcesses')
def getAppHostingProcesses(**kwargs):
    return SdwanClient().getAppHostingProcesses(**kwargs)

@register('getAppHostingStorageUtils')
def getAppHostingStorageUtils(**kwargs):
    return SdwanClient().getAppHostingStorageUtils(**kwargs)

@register('getAppHostingUtilization')
def getAppHostingUtilization(**kwargs):
    return SdwanClient().getAppHostingUtilization(**kwargs)

@register('createAppRouteSlaClassList')
def createAppRouteSlaClassList(**kwargs):
    return SdwanClient().createAppRouteSlaClassList(**kwargs)

@register('createAppRouteStatisticsList')
def createAppRouteStatisticsList(**kwargs):
    return SdwanClient().createAppRouteStatisticsList(**kwargs)

@register('getAppLogFlowCount')
def getAppLogFlowCount(**kwargs):
    return SdwanClient().getAppLogFlowCount(**kwargs)

@register('getAppLogFlows')
def getAppLogFlows(**kwargs):
    return SdwanClient().getAppLogFlows(**kwargs)

@register('createAppqoeActiveFlowIdDetails')
def createAppqoeActiveFlowIdDetails(**kwargs):
    return SdwanClient().createAppqoeActiveFlowIdDetails(**kwargs)

@register('getAppqoeHputStats')
def getAppqoeHputStats(**kwargs):
    return SdwanClient().getAppqoeHputStats(**kwargs)

@register('getAppqoeNatStats')
def getAppqoeNatStats(**kwargs):
    return SdwanClient().getAppqoeNatStats(**kwargs)

@register('getAppqoeRmResources')
def getAppqoeRmResources(**kwargs):
    return SdwanClient().getAppqoeRmResources(**kwargs)

@register('getAppqoeRMStats')
def getAppqoeRMStats(**kwargs):
    return SdwanClient().getAppqoeRMStats(**kwargs)

@register('getAppqoeServicesStatus')
def getAppqoeServicesStatus(**kwargs):
    return SdwanClient().getAppqoeServicesStatus(**kwargs)

@register('getAppqoeSppiPipeStats')
def getAppqoeSppiPipeStats(**kwargs):
    return SdwanClient().getAppqoeSppiPipeStats(**kwargs)

@register('getAppqoeSppiQueueStats')
def getAppqoeSppiQueueStats(**kwargs):
    return SdwanClient().getAppqoeSppiQueueStats(**kwargs)

@register('getAppqoeClusterSummary')
def getAppqoeClusterSummary(**kwargs):
    return SdwanClient().getAppqoeClusterSummary(**kwargs)

@register('getAppqoeErrorRecent')
def getAppqoeErrorRecent(**kwargs):
    return SdwanClient().getAppqoeErrorRecent(**kwargs)

@register('createAppqoeFlowIdExpiredDetails')
def createAppqoeFlowIdExpiredDetails(**kwargs):
    return SdwanClient().createAppqoeFlowIdExpiredDetails(**kwargs)

@register('getAppqoeFlowClosedError')
def getAppqoeFlowClosedError(**kwargs):
    return SdwanClient().getAppqoeFlowClosedError(**kwargs)

@register('getAppqoeExpired')
def getAppqoeExpired(**kwargs):
    return SdwanClient().getAppqoeExpired(**kwargs)

@register('getAppqoeServiceControllers')
def getAppqoeServiceControllers(**kwargs):
    return SdwanClient().getAppqoeServiceControllers(**kwargs)

@register('getAppqoeStatus')
def getAppqoeStatus(**kwargs):
    return SdwanClient().getAppqoeStatus(**kwargs)

@register('createAppqoeVpnIdList')
def createAppqoeVpnIdList(**kwargs):
    return SdwanClient().createAppqoeVpnIdList(**kwargs)

@register('getARPInterface')
def getARPInterface(**kwargs):
    return SdwanClient().getARPInterface(**kwargs)

@register('getAutonomousSoftwareVersion')
def getAutonomousSoftwareVersion(**kwargs):
    return SdwanClient().getAutonomousSoftwareVersion(**kwargs)

@register('createBFDHistoryList')
def createBFDHistoryList(**kwargs):
    return SdwanClient().createBFDHistoryList(**kwargs)

@register('createBFDLinkList')
def createBFDLinkList(**kwargs):
    return SdwanClient().createBFDLinkList(**kwargs)

@register('createBFDSessions')
def createBFDSessions(**kwargs):
    return SdwanClient().createBFDSessions(**kwargs)

@register('getBFDSiteStateDetail')
def getBFDSiteStateDetail(**kwargs):
    return SdwanClient().getBFDSiteStateDetail(**kwargs)

@register('getBFDSitesSummary')
def getBFDSitesSummary(**kwargs):
    return SdwanClient().getBFDSitesSummary(**kwargs)

@register('getDeviceBFDStateSummary')
def getDeviceBFDStateSummary(**kwargs):
    return SdwanClient().getDeviceBFDStateSummary(**kwargs)

@register('getDeviceBFDStateSummaryTloc')
def getDeviceBFDStateSummaryTloc(**kwargs):
    return SdwanClient().getDeviceBFDStateSummaryTloc(**kwargs)

@register('getDeviceTlocToIntfList')
def getDeviceTlocToIntfList(**kwargs):
    return SdwanClient().getDeviceTlocToIntfList(**kwargs)

@register('getDeviceBFDStatus')
def getDeviceBFDStatus(**kwargs):
    return SdwanClient().getDeviceBFDStatus(**kwargs)

@register('createBFDSummary')
def createBFDSummary(**kwargs):
    return SdwanClient().createBFDSummary(**kwargs)

@register('getDeviceBFDStatusSummary')
def getDeviceBFDStatusSummary(**kwargs):
    return SdwanClient().getDeviceBFDStatusSummary(**kwargs)

@register('createSyncedBFDSession')
def createSyncedBFDSession(**kwargs):
    return SdwanClient().createSyncedBFDSession(**kwargs)

@register('createTLOCSummary')
def createTLOCSummary(**kwargs):
    return SdwanClient().createTLOCSummary(**kwargs)

@register('getBFDTlocStateDetail')
def getBFDTlocStateDetail(**kwargs):
    return SdwanClient().getBFDTlocStateDetail(**kwargs)

@register('createBGPNeighborsList')
def createBGPNeighborsList(**kwargs):
    return SdwanClient().createBGPNeighborsList(**kwargs)

@register('createBGPRoutesList')
def createBGPRoutesList(**kwargs):
    return SdwanClient().createBGPRoutesList(**kwargs)

@register('createBGPSummary')
def createBGPSummary(**kwargs):
    return SdwanClient().createBGPSummary(**kwargs)

@register('getBridgeInterfaceList')
def getBridgeInterfaceList(**kwargs):
    return SdwanClient().getBridgeInterfaceList(**kwargs)

@register('getBridgeInterfaceMac')
def getBridgeInterfaceMac(**kwargs):
    return SdwanClient().getBridgeInterfaceMac(**kwargs)

@register('getBridgeInterfaceTable')
def getBridgeInterfaceTable(**kwargs):
    return SdwanClient().getBridgeInterfaceTable(**kwargs)

@register('getTenantsDevicesAndSites')
def getTenantsDevicesAndSites(**kwargs):
    return SdwanClient().getTenantsDevicesAndSites(**kwargs)

@register('createAppFwdCflowdFlowsList')
def createAppFwdCflowdFlowsList(**kwargs):
    return SdwanClient().createAppFwdCflowdFlowsList(**kwargs)

@register('createAppFwdCflowdV6FlowsList')
def createAppFwdCflowdV6FlowsList(**kwargs):
    return SdwanClient().createAppFwdCflowdV6FlowsList(**kwargs)

@register('createCellularConnectionList')
def createCellularConnectionList(**kwargs):
    return SdwanClient().createCellularConnectionList(**kwargs)

@register('cellularCountDashlet')
def cellularCountDashlet(**kwargs):
    return SdwanClient().cellularCountDashlet(**kwargs)

@register('dataUsage')
def dataUsage(**kwargs):
    return SdwanClient().dataUsage(**kwargs)

@register('cellularCountDashletDetails')
def cellularCountDashletDetails(**kwargs):
    return SdwanClient().cellularCountDashletDetails(**kwargs)

@register('createHardwareList')
def createHardwareList(**kwargs):
    return SdwanClient().createHardwareList(**kwargs)

@register('cellularHealthDashlet')
def cellularHealthDashlet(**kwargs):
    return SdwanClient().cellularHealthDashlet(**kwargs)

@register('createModemList')
def createModemList(**kwargs):
    return SdwanClient().createModemList(**kwargs)

@register('createNetworkList')
def createNetworkList(**kwargs):
    return SdwanClient().createNetworkList(**kwargs)

@register('createProfileList')
def createProfileList(**kwargs):
    return SdwanClient().createProfileList(**kwargs)

@register('createRadioList')
def createRadioList(**kwargs):
    return SdwanClient().createRadioList(**kwargs)

@register('createSessionsList')
def createSessionsList(**kwargs):
    return SdwanClient().createSessionsList(**kwargs)

@register('getCellularStatusList')
def getCellularStatusList(**kwargs):
    return SdwanClient().getCellularStatusList(**kwargs)

@register('getEiolteConnectionInfo')
def getEiolteConnectionInfo(**kwargs):
    return SdwanClient().getEiolteConnectionInfo(**kwargs)

@register('getEiolteHardwareInfo')
def getEiolteHardwareInfo(**kwargs):
    return SdwanClient().getEiolteHardwareInfo(**kwargs)

@register('getAONIpsecInterfaceCountersInfo')
def getAONIpsecInterfaceCountersInfo(**kwargs):
    return SdwanClient().getAONIpsecInterfaceCountersInfo(**kwargs)

@register('getAONIpsecInterfaceSessionnfo')
def getAONIpsecInterfaceSessionnfo(**kwargs):
    return SdwanClient().getAONIpsecInterfaceSessionnfo(**kwargs)

@register('getEiolteNetworkInfo')
def getEiolteNetworkInfo(**kwargs):
    return SdwanClient().getEiolteNetworkInfo(**kwargs)

@register('getEiolteRadioInfo')
def getEiolteRadioInfo(**kwargs):
    return SdwanClient().getEiolteRadioInfo(**kwargs)

@register('getEiolteSimInfo')
def getEiolteSimInfo(**kwargs):
    return SdwanClient().getEiolteSimInfo(**kwargs)

@register('getCflowdDPIDeviceFieldJSON')
def getCflowdDPIDeviceFieldJSON(**kwargs):
    return SdwanClient().getCflowdDPIDeviceFieldJSON(**kwargs)

@register('createCflowdCollectorList')
def createCflowdCollectorList(**kwargs):
    return SdwanClient().createCflowdCollectorList(**kwargs)

@register('getCflowdDPIFieldJSON')
def getCflowdDPIFieldJSON(**kwargs):
    return SdwanClient().getCflowdDPIFieldJSON(**kwargs)

@register('createCflowCollectorList')
def createCflowCollectorList(**kwargs):
    return SdwanClient().createCflowCollectorList(**kwargs)

@register('createCflowdFlowsCountList')
def createCflowdFlowsCountList(**kwargs):
    return SdwanClient().createCflowdFlowsCountList(**kwargs)

@register('getFnFCacheStats')
def getFnFCacheStats(**kwargs):
    return SdwanClient().getFnFCacheStats(**kwargs)

@register('getFnFExportClientStats')
def getFnFExportClientStats(**kwargs):
    return SdwanClient().getFnFExportClientStats(**kwargs)

@register('getFnFExportStats')
def getFnFExportStats(**kwargs):
    return SdwanClient().getFnFExportStats(**kwargs)

@register('getFnf')
def getFnf(**kwargs):
    return SdwanClient().getFnf(**kwargs)

@register('getFnFMonitorStats')
def getFnFMonitorStats(**kwargs):
    return SdwanClient().getFnFMonitorStats(**kwargs)

@register('createCflowdStatistics')
def createCflowdStatistics(**kwargs):
    return SdwanClient().createCflowdStatistics(**kwargs)

@register('createCflowdTemplate')
def createCflowdTemplate(**kwargs):
    return SdwanClient().createCflowdTemplate(**kwargs)

@register('getMpDatabase')
def getMpDatabase(**kwargs):
    return SdwanClient().getMpDatabase(**kwargs)

@register('getMpLocalMep')
def getMpLocalMep(**kwargs):
    return SdwanClient().getMpLocalMep(**kwargs)

@register('getMpLocalMip')
def getMpLocalMip(**kwargs):
    return SdwanClient().getMpLocalMip(**kwargs)

@register('getMpRemoteMep')
def getMpRemoteMep(**kwargs):
    return SdwanClient().getMpRemoteMep(**kwargs)

@register('createApplicationsDetailList')
def createApplicationsDetailList(**kwargs):
    return SdwanClient().createApplicationsDetailList(**kwargs)

@register('createApplicationsList')
def createApplicationsList(**kwargs):
    return SdwanClient().createApplicationsList(**kwargs)

@register('createGatewayExitsList')
def createGatewayExitsList(**kwargs):
    return SdwanClient().createGatewayExitsList(**kwargs)

@register('createLbApplicationsList')
def createLbApplicationsList(**kwargs):
    return SdwanClient().createLbApplicationsList(**kwargs)

@register('createLocalExitsList')
def createLocalExitsList(**kwargs):
    return SdwanClient().createLocalExitsList(**kwargs)

@register('getComplianceDetails')
def getComplianceDetails(**kwargs):
    return SdwanClient().getComplianceDetails(**kwargs)

@register('getComplianceSummary')
def getComplianceSummary(**kwargs):
    return SdwanClient().getComplianceSummary(**kwargs)

@register('getDeviceRunningConfig')
def getDeviceRunningConfig(**kwargs):
    return SdwanClient().getDeviceRunningConfig(**kwargs)

@register('getDeviceRunningConfigHTML')
def getDeviceRunningConfigHTML(**kwargs):
    return SdwanClient().getDeviceRunningConfigHTML(**kwargs)

@register('getDeviceConfigurationCommitList')
def getDeviceConfigurationCommitList(**kwargs):
    return SdwanClient().getDeviceConfigurationCommitList(**kwargs)

@register('getAffinityConfig')
def getAffinityConfig(**kwargs):
    return SdwanClient().getAffinityConfig(**kwargs)

@register('getAffinityStatus')
def getAffinityStatus(**kwargs):
    return SdwanClient().getAffinityStatus(**kwargs)

@register('createRealTimeConnectionList')
def createRealTimeConnectionList(**kwargs):
    return SdwanClient().createRealTimeConnectionList(**kwargs)

@register('createConnectionHistoryListRealTime')
def createConnectionHistoryListRealTime(**kwargs):
    return SdwanClient().createConnectionHistoryListRealTime(**kwargs)

@register('createRealTimeConnectionList_1')
def createRealTimeConnectionList_1(**kwargs):
    return SdwanClient().createRealTimeConnectionList_1(**kwargs)

@register('getTotalCountForDeviceStates')
def getTotalCountForDeviceStates(**kwargs):
    return SdwanClient().getTotalCountForDeviceStates(**kwargs)

@register('createLinkList')
def createLinkList(**kwargs):
    return SdwanClient().createLinkList(**kwargs)

@register('createLocalPropertiesListListRealTIme')
def createLocalPropertiesListListRealTIme(**kwargs):
    return SdwanClient().createLocalPropertiesListListRealTIme(**kwargs)

@register('networkSummary')
def networkSummary(**kwargs):
    return SdwanClient().networkSummary(**kwargs)

@register('createRealTimeRegionConnectionList')
def createRealTimeRegionConnectionList(**kwargs):
    return SdwanClient().createRealTimeRegionConnectionList(**kwargs)

@register('getConnectionStatistics')
def getConnectionStatistics(**kwargs):
    return SdwanClient().getConnectionStatistics(**kwargs)

@register('getLocalDeviceStatus')
def getLocalDeviceStatus(**kwargs):
    return SdwanClient().getLocalDeviceStatus(**kwargs)

@register('createConnectionsSummary')
def createConnectionsSummary(**kwargs):
    return SdwanClient().createConnectionsSummary(**kwargs)

@register('getDeviceControlStatusSummary')
def getDeviceControlStatusSummary(**kwargs):
    return SdwanClient().getDeviceControlStatusSummary(**kwargs)

@register('createSyncedConnectionList')
def createSyncedConnectionList(**kwargs):
    return SdwanClient().createSyncedConnectionList(**kwargs)

@register('createLocalPropertiesSyncedList')
def createLocalPropertiesSyncedList(**kwargs):
    return SdwanClient().createLocalPropertiesSyncedList(**kwargs)

@register('createWanInterfaceSyncedList')
def createWanInterfaceSyncedList(**kwargs):
    return SdwanClient().createWanInterfaceSyncedList(**kwargs)

@register('createValidDevicesListRealTime')
def createValidDevicesListRealTime(**kwargs):
    return SdwanClient().createValidDevicesListRealTime(**kwargs)

@register('getValidVManageIdRealTime')
def getValidVManageIdRealTime(**kwargs):
    return SdwanClient().getValidVManageIdRealTime(**kwargs)

@register('createValidVSmartsListRealTime')
def createValidVSmartsListRealTime(**kwargs):
    return SdwanClient().createValidVSmartsListRealTime(**kwargs)

@register('createWanInterfaceListList')
def createWanInterfaceListList(**kwargs):
    return SdwanClient().createWanInterfaceListList(**kwargs)

@register('getPortHopColor')
def getPortHopColor(**kwargs):
    return SdwanClient().getPortHopColor(**kwargs)

@register('getDeviceCounters')
def getDeviceCounters(**kwargs):
    return SdwanClient().getDeviceCounters(**kwargs)

@register('getDeviceCrashLogs')
def getDeviceCrashLogs(**kwargs):
    return SdwanClient().getDeviceCrashLogs(**kwargs)

@register('getAllDeviceCrashLogs')
def getAllDeviceCrashLogs(**kwargs):
    return SdwanClient().getAllDeviceCrashLogs(**kwargs)

@register('getDeviceCrashInformation')
def getDeviceCrashInformation(**kwargs):
    return SdwanClient().getDeviceCrashInformation(**kwargs)

@register('getDeviceCrashLogsSynced')
def getDeviceCrashLogsSynced(**kwargs):
    return SdwanClient().getDeviceCrashLogsSynced(**kwargs)

@register('createDeviceContainersInfo')
def createDeviceContainersInfo(**kwargs):
    return SdwanClient().createDeviceContainersInfo(**kwargs)

@register('getPnicStats')
def getPnicStats(**kwargs):
    return SdwanClient().getPnicStats(**kwargs)

@register('getPNICStatsFromDevice')
def getPNICStatsFromDevice(**kwargs):
    return SdwanClient().getPNICStatsFromDevice(**kwargs)

@register('getRBACInterface')
def getRBACInterface(**kwargs):
    return SdwanClient().getRBACInterface(**kwargs)

@register('getAllocationInfo')
def getAllocationInfo(**kwargs):
    return SdwanClient().getAllocationInfo(**kwargs)

@register('getCPUInfo')
def getCPUInfo(**kwargs):
    return SdwanClient().getCPUInfo(**kwargs)

@register('getVNFInfo')
def getVNFInfo(**kwargs):
    return SdwanClient().getVNFInfo(**kwargs)

@register('createDeviceSystemSettingNativeInfo')
def createDeviceSystemSettingNativeInfo(**kwargs):
    return SdwanClient().createDeviceSystemSettingNativeInfo(**kwargs)

@register('createDeviceSystemProcessList')
def createDeviceSystemProcessList(**kwargs):
    return SdwanClient().createDeviceSystemProcessList(**kwargs)

@register('createDeviceSystemSetting')
def createDeviceSystemSetting(**kwargs):
    return SdwanClient().createDeviceSystemSetting(**kwargs)

@register('createDeviceSystemStatus')
def createDeviceSystemStatus(**kwargs):
    return SdwanClient().createDeviceSystemStatus(**kwargs)

@register('getCtsPac')
def getCtsPac(**kwargs):
    return SdwanClient().getCtsPac(**kwargs)

@register('getDeviceOnlyStatus')
def getDeviceOnlyStatus(**kwargs):
    return SdwanClient().getDeviceOnlyStatus(**kwargs)

@register('getDHCPClient')
def getDHCPClient(**kwargs):
    return SdwanClient().getDHCPClient(**kwargs)

@register('getDHCPInterface')
def getDHCPInterface(**kwargs):
    return SdwanClient().getDHCPInterface(**kwargs)

@register('getDHCPServer')
def getDHCPServer(**kwargs):
    return SdwanClient().getDHCPServer(**kwargs)

@register('getDHCPv6Interface')
def getDHCPv6Interface(**kwargs):
    return SdwanClient().getDHCPv6Interface(**kwargs)

@register('getWLANDOT1xClients')
def getWLANDOT1xClients(**kwargs):
    return SdwanClient().getWLANDOT1xClients(**kwargs)

@register('getWLANDOT1xInterfaces')
def getWLANDOT1xInterfaces(**kwargs):
    return SdwanClient().getWLANDOT1xInterfaces(**kwargs)

@register('getDOT1xRadius')
def getDOT1xRadius(**kwargs):
    return SdwanClient().getDOT1xRadius(**kwargs)

@register('createSoftwareList')
def createSoftwareList(**kwargs):
    return SdwanClient().createSoftwareList(**kwargs)

@register('getSupportedApplicationList')
def getSupportedApplicationList(**kwargs):
    return SdwanClient().getSupportedApplicationList(**kwargs)

@register('getDPIDeviceFieldJSON')
def getDPIDeviceFieldJSON(**kwargs):
    return SdwanClient().getDPIDeviceFieldJSON(**kwargs)

@register('createDPICollectorList')
def createDPICollectorList(**kwargs):
    return SdwanClient().createDPICollectorList(**kwargs)

@register('getCommonApplicationList')
def getCommonApplicationList(**kwargs):
    return SdwanClient().getCommonApplicationList(**kwargs)

@register('getDPIFieldJSON')
def getDPIFieldJSON(**kwargs):
    return SdwanClient().getDPIFieldJSON(**kwargs)

@register('getDPIDeviceDetailsFieldJSON')
def getDPIDeviceDetailsFieldJSON(**kwargs):
    return SdwanClient().getDPIDeviceDetailsFieldJSON(**kwargs)

@register('createDPIFlowsList')
def createDPIFlowsList(**kwargs):
    return SdwanClient().createDPIFlowsList(**kwargs)

@register('getQosmosStaticApplicationList')
def getQosmosStaticApplicationList(**kwargs):
    return SdwanClient().getQosmosStaticApplicationList(**kwargs)

@register('getQosmosApplicationList')
def getQosmosApplicationList(**kwargs):
    return SdwanClient().getQosmosApplicationList(**kwargs)

@register('createDPISummaryRealTime')
def createDPISummaryRealTime(**kwargs):
    return SdwanClient().createDPISummaryRealTime(**kwargs)

@register('createDPIStatistics')
def createDPIStatistics(**kwargs):
    return SdwanClient().createDPIStatistics(**kwargs)

@register('getDreAutoBypassStats')
def getDreAutoBypassStats(**kwargs):
    return SdwanClient().getDreAutoBypassStats(**kwargs)

@register('getDreStats')
def getDreStats(**kwargs):
    return SdwanClient().getDreStats(**kwargs)

@register('getDreStatus')
def getDreStatus(**kwargs):
    return SdwanClient().getDreStatus(**kwargs)

@register('getDrePeerStats')
def getDrePeerStats(**kwargs):
    return SdwanClient().getDrePeerStats(**kwargs)

@register('getDualStaticRouteTrackerInfo')
def getDualStaticRouteTrackerInfo(**kwargs):
    return SdwanClient().getDualStaticRouteTrackerInfo(**kwargs)

@register('createEIGRPInterface')
def createEIGRPInterface(**kwargs):
    return SdwanClient().createEIGRPInterface(**kwargs)

@register('createEIGRPRoute')
def createEIGRPRoute(**kwargs):
    return SdwanClient().createEIGRPRoute(**kwargs)

@register('createEIGRPTopology')
def createEIGRPTopology(**kwargs):
    return SdwanClient().createEIGRPTopology(**kwargs)

@register('getEndpointTrackerInfo')
def getEndpointTrackerInfo(**kwargs):
    return SdwanClient().getEndpointTrackerInfo(**kwargs)

@register('getEndpointTrackerGroupInfo')
def getEndpointTrackerGroupInfo(**kwargs):
    return SdwanClient().getEndpointTrackerGroupInfo(**kwargs)

@register('getEnvironmentData')
def getEnvironmentData(**kwargs):
    return SdwanClient().getEnvironmentData(**kwargs)

@register('getRadiusServer')
def getRadiusServer(**kwargs):
    return SdwanClient().getRadiusServer(**kwargs)

@register('getFeatureList')
def getFeatureList(**kwargs):
    return SdwanClient().getFeatureList(**kwargs)

@register('getSyncedFeatureList')
def getSyncedFeatureList(**kwargs):
    return SdwanClient().getSyncedFeatureList(**kwargs)

@register('getDataCollectionStatusForDevice')
def getDataCollectionStatusForDevice(**kwargs):
    return SdwanClient().getDataCollectionStatusForDevice(**kwargs)

@register('downloadGeneratedFile')
def downloadGeneratedFile(**kwargs):
    return SdwanClient().downloadGeneratedFile(**kwargs)

@register('getDataCollectionStatusForUUID')
def getDataCollectionStatusForUUID(**kwargs):
    return SdwanClient().getDataCollectionStatusForUUID(**kwargs)

@register('getSupportedCommandsList')
def getSupportedCommandsList(**kwargs):
    return SdwanClient().getSupportedCommandsList(**kwargs)

@register('getGeofenceStatus')
def getGeofenceStatus(**kwargs):
    return SdwanClient().getGeofenceStatus(**kwargs)

@register('createAlarmList')
def createAlarmList(**kwargs):
    return SdwanClient().createAlarmList(**kwargs)

@register('createEnvironmentList')
def createEnvironmentList(**kwargs):
    return SdwanClient().createEnvironmentList(**kwargs)

@register('createErrorAlarmList')
def createErrorAlarmList(**kwargs):
    return SdwanClient().createErrorAlarmList(**kwargs)

@register('createInventoryList')
def createInventoryList(**kwargs):
    return SdwanClient().createInventoryList(**kwargs)

@register('createStatusSummary')
def createStatusSummary(**kwargs):
    return SdwanClient().createStatusSummary(**kwargs)

@register('createSyncedAlarmList')
def createSyncedAlarmList(**kwargs):
    return SdwanClient().createSyncedAlarmList(**kwargs)

@register('createSyncedEnvironmentList')
def createSyncedEnvironmentList(**kwargs):
    return SdwanClient().createSyncedEnvironmentList(**kwargs)

@register('createSyncedInventoryList')
def createSyncedInventoryList(**kwargs):
    return SdwanClient().createSyncedInventoryList(**kwargs)

@register('createSystemList')
def createSystemList(**kwargs):
    return SdwanClient().createSystemList(**kwargs)

@register('createTempThresholdList')
def createTempThresholdList(**kwargs):
    return SdwanClient().createTempThresholdList(**kwargs)

@register('getHardwareHealthDetails')
def getHardwareHealthDetails(**kwargs):
    return SdwanClient().getHardwareHealthDetails(**kwargs)

@register('getHardwareHealthSummary')
def getHardwareHealthSummary(**kwargs):
    return SdwanClient().getHardwareHealthSummary(**kwargs)

@register('getStatDataRawData_21')
def getStatDataRawData_21(**kwargs):
    return SdwanClient().getStatDataRawData_21(**kwargs)

@register('getAggregationDataByQuery_23')
def getAggregationDataByQuery_23(**kwargs):
    return SdwanClient().getAggregationDataByQuery_23(**kwargs)

@register('getLastThousandConfigList')
def getLastThousandConfigList(**kwargs):
    return SdwanClient().getLastThousandConfigList(**kwargs)

@register('getConfigDiff')
def getConfigDiff(**kwargs):
    return SdwanClient().getConfigDiff(**kwargs)

@register('getDeviceConfig')
def getDeviceConfig(**kwargs):
    return SdwanClient().getDeviceConfig(**kwargs)

@register('getStatDataRawDataAsCSV_21')
def getStatDataRawDataAsCSV_21(**kwargs):
    return SdwanClient().getStatDataRawDataAsCSV_21(**kwargs)

@register('getCount_20')
def getCount_20(**kwargs):
    return SdwanClient().getCount_20(**kwargs)

@register('getStatDataFields_22')
def getStatDataFields_22(**kwargs):
    return SdwanClient().getStatDataFields_22(**kwargs)

@register('getStatsPaginationRawData_19')
def getStatsPaginationRawData_19(**kwargs):
    return SdwanClient().getStatsPaginationRawData_19(**kwargs)

@register('getStatQueryFields_23')
def getStatQueryFields_23(**kwargs):
    return SdwanClient().getStatQueryFields_23(**kwargs)

@register('createIGMPGroupsList')
def createIGMPGroupsList(**kwargs):
    return SdwanClient().createIGMPGroupsList(**kwargs)

@register('createIGMPInterfaceList')
def createIGMPInterfaceList(**kwargs):
    return SdwanClient().createIGMPInterfaceList(**kwargs)

@register('createIGMPStatisticsList')
def createIGMPStatisticsList(**kwargs):
    return SdwanClient().createIGMPStatisticsList(**kwargs)

@register('createIGMPSummary')
def createIGMPSummary(**kwargs):
    return SdwanClient().createIGMPSummary(**kwargs)

@register('getDeviceInterface')
def getDeviceInterface(**kwargs):
    return SdwanClient().getDeviceInterface(**kwargs)

@register('getDeviceInterfaceARPStats')
def getDeviceInterfaceARPStats(**kwargs):
    return SdwanClient().getDeviceInterfaceARPStats(**kwargs)

@register('getDeviceInterfaceErrorStats')
def getDeviceInterfaceErrorStats(**kwargs):
    return SdwanClient().getDeviceInterfaceErrorStats(**kwargs)

@register('getDeviceInterfaceIpv6Stats')
def getDeviceInterfaceIpv6Stats(**kwargs):
    return SdwanClient().getDeviceInterfaceIpv6Stats(**kwargs)

@register('getDeviceInterfacePktSizes')
def getDeviceInterfacePktSizes(**kwargs):
    return SdwanClient().getDeviceInterfacePktSizes(**kwargs)

@register('getDeviceInterfacePortStats')
def getDeviceInterfacePortStats(**kwargs):
    return SdwanClient().getDeviceInterfacePortStats(**kwargs)

@register('getDeviceInterfaceQosStats')
def getDeviceInterfaceQosStats(**kwargs):
    return SdwanClient().getDeviceInterfaceQosStats(**kwargs)

@register('getDeviceInterfaceQueueStats')
def getDeviceInterfaceQueueStats(**kwargs):
    return SdwanClient().getDeviceInterfaceQueueStats(**kwargs)

@register('getDeviceSerialInterface')
def getDeviceSerialInterface(**kwargs):
    return SdwanClient().getDeviceSerialInterface(**kwargs)

@register('getDeviceInterfaceStats')
def getDeviceInterfaceStats(**kwargs):
    return SdwanClient().getDeviceInterfaceStats(**kwargs)

@register('getSyncedDeviceInterface')
def getSyncedDeviceInterface(**kwargs):
    return SdwanClient().getSyncedDeviceInterface(**kwargs)

@register('trustsec')
def trustsec(**kwargs):
    return SdwanClient().trustsec(**kwargs)

@register('generateDeviceInterfaceVPN')
def generateDeviceInterfaceVPN(**kwargs):
    return SdwanClient().generateDeviceInterfaceVPN(**kwargs)

@register('createFibList')
def createFibList(**kwargs):
    return SdwanClient().createFibList(**kwargs)

@register('createIetfRoutingList')
def createIetfRoutingList(**kwargs):
    return SdwanClient().createIetfRoutingList(**kwargs)

@register('createIPMfibOilList')
def createIPMfibOilList(**kwargs):
    return SdwanClient().createIPMfibOilList(**kwargs)

@register('createIPMfibStatsList')
def createIPMfibStatsList(**kwargs):
    return SdwanClient().createIPMfibStatsList(**kwargs)

@register('createIPMfibSummaryList')
def createIPMfibSummaryList(**kwargs):
    return SdwanClient().createIPMfibSummaryList(**kwargs)

@register('createNatFilterList')
def createNatFilterList(**kwargs):
    return SdwanClient().createNatFilterList(**kwargs)

@register('createNatInterfaceList')
def createNatInterfaceList(**kwargs):
    return SdwanClient().createNatInterfaceList(**kwargs)

@register('createNatInterfaceStatisticsList')
def createNatInterfaceStatisticsList(**kwargs):
    return SdwanClient().createNatInterfaceStatisticsList(**kwargs)

@register('createNatTranslationList')
def createNatTranslationList(**kwargs):
    return SdwanClient().createNatTranslationList(**kwargs)

@register('createNat64TranslationList')
def createNat64TranslationList(**kwargs):
    return SdwanClient().createNat64TranslationList(**kwargs)

@register('createRouteTableList')
def createRouteTableList(**kwargs):
    return SdwanClient().createRouteTableList(**kwargs)

@register('createIPv4FibList')
def createIPv4FibList(**kwargs):
    return SdwanClient().createIPv4FibList(**kwargs)

@register('createIPv6FibList')
def createIPv6FibList(**kwargs):
    return SdwanClient().createIPv6FibList(**kwargs)

@register('createCryptoIpsecIdentity')
def createCryptoIpsecIdentity(**kwargs):
    return SdwanClient().createCryptoIpsecIdentity(**kwargs)

@register('createIkeInboundList')
def createIkeInboundList(**kwargs):
    return SdwanClient().createIkeInboundList(**kwargs)

@register('createIkeOutboundList')
def createIkeOutboundList(**kwargs):
    return SdwanClient().createIkeOutboundList(**kwargs)

@register('createIkeSessions')
def createIkeSessions(**kwargs):
    return SdwanClient().createIkeSessions(**kwargs)

@register('createCryptov1LocalSAList')
def createCryptov1LocalSAList(**kwargs):
    return SdwanClient().createCryptov1LocalSAList(**kwargs)

@register('createCryptov2LocalSAList')
def createCryptov2LocalSAList(**kwargs):
    return SdwanClient().createCryptov2LocalSAList(**kwargs)

@register('createInBoundList')
def createInBoundList(**kwargs):
    return SdwanClient().createInBoundList(**kwargs)

@register('createLocalSAList')
def createLocalSAList(**kwargs):
    return SdwanClient().createLocalSAList(**kwargs)

@register('createOutBoundList')
def createOutBoundList(**kwargs):
    return SdwanClient().createOutBoundList(**kwargs)

@register('createIPsecPWKInboundConnections')
def createIPsecPWKInboundConnections(**kwargs):
    return SdwanClient().createIPsecPWKInboundConnections(**kwargs)

@register('createIPsecPWKLocalSA')
def createIPsecPWKLocalSA(**kwargs):
    return SdwanClient().createIPsecPWKLocalSA(**kwargs)

@register('createIPsecPWKOutboundConnections')
def createIPsecPWKOutboundConnections(**kwargs):
    return SdwanClient().createIPsecPWKOutboundConnections(**kwargs)

@register('getIpv6Data')
def getIpv6Data(**kwargs):
    return SdwanClient().getIpv6Data(**kwargs)

@register('getDeviceListAsKeyValue')
def getDeviceListAsKeyValue(**kwargs):
    return SdwanClient().getDeviceListAsKeyValue(**kwargs)

@register('getLacpInterfaceList')
def getLacpInterfaceList(**kwargs):
    return SdwanClient().getLacpInterfaceList(**kwargs)

@register('getLacpMembers')
def getLacpMembers(**kwargs):
    return SdwanClient().getLacpMembers(**kwargs)

@register('getLicenseEvalInfo')
def getLicenseEvalInfo(**kwargs):
    return SdwanClient().getLicenseEvalInfo(**kwargs)

@register('getLicensePAKInfo')
def getLicensePAKInfo(**kwargs):
    return SdwanClient().getLicensePAKInfo(**kwargs)

@register('getLicensePrivacyInfo')
def getLicensePrivacyInfo(**kwargs):
    return SdwanClient().getLicensePrivacyInfo(**kwargs)

@register('getLicenseRegInfo')
def getLicenseRegInfo(**kwargs):
    return SdwanClient().getLicenseRegInfo(**kwargs)

@register('getLicenseUDIInfo')
def getLicenseUDIInfo(**kwargs):
    return SdwanClient().getLicenseUDIInfo(**kwargs)

@register('getLicenseUsageInfo')
def getLicenseUsageInfo(**kwargs):
    return SdwanClient().getLicenseUsageInfo(**kwargs)

@register('getLoggingFromDevice')
def getLoggingFromDevice(**kwargs):
    return SdwanClient().getLoggingFromDevice(**kwargs)

@register('listAllDeviceModels')
def listAllDeviceModels(**kwargs):
    return SdwanClient().listAllDeviceModels(**kwargs)

@register('getDeviceModels')
def getDeviceModels(**kwargs):
    return SdwanClient().getDeviceModels(**kwargs)

@register('listAllMonitorDetailsDevices')
def listAllMonitorDetailsDevices(**kwargs):
    return SdwanClient().listAllMonitorDetailsDevices(**kwargs)

@register('createReplicatorList')
def createReplicatorList(**kwargs):
    return SdwanClient().createReplicatorList(**kwargs)

@register('createRpfList')
def createRpfList(**kwargs):
    return SdwanClient().createRpfList(**kwargs)

@register('createTopologyList')
def createTopologyList(**kwargs):
    return SdwanClient().createTopologyList(**kwargs)

@register('createPimTunnelList')
def createPimTunnelList(**kwargs):
    return SdwanClient().createPimTunnelList(**kwargs)

@register('getIpv6Interface')
def getIpv6Interface(**kwargs):
    return SdwanClient().getIpv6Interface(**kwargs)

@register('getRunning')
def getRunning(**kwargs):
    return SdwanClient().getRunning(**kwargs)

@register('createAssociationsList')
def createAssociationsList(**kwargs):
    return SdwanClient().createAssociationsList(**kwargs)

@register('createPeerList')
def createPeerList(**kwargs):
    return SdwanClient().createPeerList(**kwargs)

@register('createNTPStatusList')
def createNTPStatusList(**kwargs):
    return SdwanClient().createNTPStatusList(**kwargs)

@register('createOMPCloudXRecv')
def createOMPCloudXRecv(**kwargs):
    return SdwanClient().createOMPCloudXRecv(**kwargs)

@register('createOMPLinkList')
def createOMPLinkList(**kwargs):
    return SdwanClient().createOMPLinkList(**kwargs)

@register('createOMPMcastAutoDiscoverAdvt')
def createOMPMcastAutoDiscoverAdvt(**kwargs):
    return SdwanClient().createOMPMcastAutoDiscoverAdvt(**kwargs)

@register('createOMPMcastAutoDiscoverRecv')
def createOMPMcastAutoDiscoverRecv(**kwargs):
    return SdwanClient().createOMPMcastAutoDiscoverRecv(**kwargs)

@register('createOMPMcastRoutesAdvt')
def createOMPMcastRoutesAdvt(**kwargs):
    return SdwanClient().createOMPMcastRoutesAdvt(**kwargs)

@register('createOMPMcastRoutesRecv')
def createOMPMcastRoutesRecv(**kwargs):
    return SdwanClient().createOMPMcastRoutesRecv(**kwargs)

@register('createOMPSessionList')
def createOMPSessionList(**kwargs):
    return SdwanClient().createOMPSessionList(**kwargs)

@register('createAdvertisedRoutesList')
def createAdvertisedRoutesList(**kwargs):
    return SdwanClient().createAdvertisedRoutesList(**kwargs)

@register('createAdvertisedRoutesListIpv6')
def createAdvertisedRoutesListIpv6(**kwargs):
    return SdwanClient().createAdvertisedRoutesListIpv6(**kwargs)

@register('createReceivedRoutesList')
def createReceivedRoutesList(**kwargs):
    return SdwanClient().createReceivedRoutesList(**kwargs)

@register('createReceivedRoutesListIpv6')
def createReceivedRoutesListIpv6(**kwargs):
    return SdwanClient().createReceivedRoutesListIpv6(**kwargs)

@register('createOMPServices')
def createOMPServices(**kwargs):
    return SdwanClient().createOMPServices(**kwargs)

@register('getDeviceOMPStatus')
def getDeviceOMPStatus(**kwargs):
    return SdwanClient().getDeviceOMPStatus(**kwargs)

@register('createOMPSummary')
def createOMPSummary(**kwargs):
    return SdwanClient().createOMPSummary(**kwargs)

@register('createSyncedOMPSessionList')
def createSyncedOMPSessionList(**kwargs):
    return SdwanClient().createSyncedOMPSessionList(**kwargs)

@register('createAdvertisedTlocsList')
def createAdvertisedTlocsList(**kwargs):
    return SdwanClient().createAdvertisedTlocsList(**kwargs)

@register('createReceivedTlocsList')
def createReceivedTlocsList(**kwargs):
    return SdwanClient().createReceivedTlocsList(**kwargs)

@register('getOnDemandLocal')
def getOnDemandLocal(**kwargs):
    return SdwanClient().getOnDemandLocal(**kwargs)

@register('getOnDemandRemote')
def getOnDemandRemote(**kwargs):
    return SdwanClient().getOnDemandRemote(**kwargs)

@register('createConnectionListFromDevice')
def createConnectionListFromDevice(**kwargs):
    return SdwanClient().createConnectionListFromDevice(**kwargs)

@register('createConnectionHistoryList')
def createConnectionHistoryList(**kwargs):
    return SdwanClient().createConnectionHistoryList(**kwargs)

@register('createLocalPropertiesListList')
def createLocalPropertiesListList(**kwargs):
    return SdwanClient().createLocalPropertiesListList(**kwargs)

@register('createReverseProxyMappingList')
def createReverseProxyMappingList(**kwargs):
    return SdwanClient().createReverseProxyMappingList(**kwargs)

@register('getStatistics')
def getStatistics(**kwargs):
    return SdwanClient().getStatistics(**kwargs)

@register('createConnectionSummary')
def createConnectionSummary(**kwargs):
    return SdwanClient().createConnectionSummary(**kwargs)

@register('createValidDevicesList')
def createValidDevicesList(**kwargs):
    return SdwanClient().createValidDevicesList(**kwargs)

@register('getValidVManageId')
def getValidVManageId(**kwargs):
    return SdwanClient().getValidVManageId(**kwargs)

@register('createValidVSmartsList')
def createValidVSmartsList(**kwargs):
    return SdwanClient().createValidVSmartsList(**kwargs)

@register('createOSPFDatabaseList')
def createOSPFDatabaseList(**kwargs):
    return SdwanClient().createOSPFDatabaseList(**kwargs)

@register('createOSPFDatabaseExternal')
def createOSPFDatabaseExternal(**kwargs):
    return SdwanClient().createOSPFDatabaseExternal(**kwargs)

@register('createOSPFDatabaseSummaryList')
def createOSPFDatabaseSummaryList(**kwargs):
    return SdwanClient().createOSPFDatabaseSummaryList(**kwargs)

@register('createOSPFInterface')
def createOSPFInterface(**kwargs):
    return SdwanClient().createOSPFInterface(**kwargs)

@register('createOSPFNeighbors')
def createOSPFNeighbors(**kwargs):
    return SdwanClient().createOSPFNeighbors(**kwargs)

@register('createOSPFProcess')
def createOSPFProcess(**kwargs):
    return SdwanClient().createOSPFProcess(**kwargs)

@register('createOSPFRoutesList')
def createOSPFRoutesList(**kwargs):
    return SdwanClient().createOSPFRoutesList(**kwargs)

@register('createOSPFv3Interface')
def createOSPFv3Interface(**kwargs):
    return SdwanClient().createOSPFv3Interface(**kwargs)

@register('createOSPFv3Neighbors')
def createOSPFv3Neighbors(**kwargs):
    return SdwanClient().createOSPFv3Neighbors(**kwargs)

@register('createPIMInterfaceList')
def createPIMInterfaceList(**kwargs):
    return SdwanClient().createPIMInterfaceList(**kwargs)

@register('createPIMNeighborList')
def createPIMNeighborList(**kwargs):
    return SdwanClient().createPIMNeighborList(**kwargs)

@register('createPIMRpMappingList')
def createPIMRpMappingList(**kwargs):
    return SdwanClient().createPIMRpMappingList(**kwargs)

@register('createPIMStatisticsList')
def createPIMStatisticsList(**kwargs):
    return SdwanClient().createPIMStatisticsList(**kwargs)

@register('getDevicePkiTrustpoint')
def getDevicePkiTrustpoint(**kwargs):
    return SdwanClient().getDevicePkiTrustpoint(**kwargs)

@register('getPolicedInterface')
def getPolicedInterface(**kwargs):
    return SdwanClient().getPolicedInterface(**kwargs)

@register('createPolicyAccessListAssociations')
def createPolicyAccessListAssociations(**kwargs):
    return SdwanClient().createPolicyAccessListAssociations(**kwargs)

@register('createPolicyAccessListCounters')
def createPolicyAccessListCounters(**kwargs):
    return SdwanClient().createPolicyAccessListCounters(**kwargs)

@register('createPolicyAccessListNames')
def createPolicyAccessListNames(**kwargs):
    return SdwanClient().createPolicyAccessListNames(**kwargs)

@register('createPolicyAccessListPolicers')
def createPolicyAccessListPolicers(**kwargs):
    return SdwanClient().createPolicyAccessListPolicers(**kwargs)

@register('createPolicyAppRoutePolicyFilter')
def createPolicyAppRoutePolicyFilter(**kwargs):
    return SdwanClient().createPolicyAppRoutePolicyFilter(**kwargs)

@register('createPolicDataPolicyFilter')
def createPolicDataPolicyFilter(**kwargs):
    return SdwanClient().createPolicDataPolicyFilter(**kwargs)

@register('createPolicyFilterMemoryUsage')
def createPolicyFilterMemoryUsage(**kwargs):
    return SdwanClient().createPolicyFilterMemoryUsage(**kwargs)

@register('showVsmartIptoSgtBinding')
def showVsmartIptoSgtBinding(**kwargs):
    return SdwanClient().showVsmartIptoSgtBinding(**kwargs)

@register('showVsmartIptoUserBinding')
def showVsmartIptoUserBinding(**kwargs):
    return SdwanClient().showVsmartIptoUserBinding(**kwargs)

@register('createPolicyAccessListAssociationsIpv6')
def createPolicyAccessListAssociationsIpv6(**kwargs):
    return SdwanClient().createPolicyAccessListAssociationsIpv6(**kwargs)

@register('createPolicyAccessListCountersIpv6')
def createPolicyAccessListCountersIpv6(**kwargs):
    return SdwanClient().createPolicyAccessListCountersIpv6(**kwargs)

@register('createPolicyAccessListNamesIpv6')
def createPolicyAccessListNamesIpv6(**kwargs):
    return SdwanClient().createPolicyAccessListNamesIpv6(**kwargs)

@register('createPolicyAccessListPolicersIpv6')
def createPolicyAccessListPolicersIpv6(**kwargs):
    return SdwanClient().createPolicyAccessListPolicersIpv6(**kwargs)

@register('showVsmartPxGridStatus')
def showVsmartPxGridStatus(**kwargs):
    return SdwanClient().showVsmartPxGridStatus(**kwargs)

@register('showVsmartPxGridUserSessions')
def showVsmartPxGridUserSessions(**kwargs):
    return SdwanClient().showVsmartPxGridUserSessions(**kwargs)

@register('createPolicQosMapInfo')
def createPolicQosMapInfo(**kwargs):
    return SdwanClient().createPolicQosMapInfo(**kwargs)

@register('createPolicQosSchedulerInfo')
def createPolicQosSchedulerInfo(**kwargs):
    return SdwanClient().createPolicQosSchedulerInfo(**kwargs)

@register('createPolicyRewriteAssociationsInfo')
def createPolicyRewriteAssociationsInfo(**kwargs):
    return SdwanClient().createPolicyRewriteAssociationsInfo(**kwargs)

@register('showVsmartUserUsergroupBindings')
def showVsmartUserUsergroupBindings(**kwargs):
    return SdwanClient().showVsmartUserUsergroupBindings(**kwargs)

@register('showSdwanPolicyFromVsmart')
def showSdwanPolicyFromVsmart(**kwargs):
    return SdwanClient().showSdwanPolicyFromVsmart(**kwargs)

@register('getZoneDropStatistics')
def getZoneDropStatistics(**kwargs):
    return SdwanClient().getZoneDropStatistics(**kwargs)

@register('getZbfwStatistics')
def getZbfwStatistics(**kwargs):
    return SdwanClient().getZbfwStatistics(**kwargs)

@register('getZonePairSessions')
def getZonePairSessions(**kwargs):
    return SdwanClient().getZonePairSessions(**kwargs)

@register('getZonePairs')
def getZonePairs(**kwargs):
    return SdwanClient().getZonePairs(**kwargs)

@register('getZonePolicyFilters')
def getZonePolicyFilters(**kwargs):
    return SdwanClient().getZonePolicyFilters(**kwargs)

@register('getPowerConsumption')
def getPowerConsumption(**kwargs):
    return SdwanClient().getPowerConsumption(**kwargs)

@register('createPPPInterfaceList')
def createPPPInterfaceList(**kwargs):
    return SdwanClient().createPPPInterfaceList(**kwargs)

@register('createPPPoEInterfaceList')
def createPPPoEInterfaceList(**kwargs):
    return SdwanClient().createPPPoEInterfaceList(**kwargs)

@register('createPPPoENeighborList')
def createPPPoENeighborList(**kwargs):
    return SdwanClient().createPPPoENeighborList(**kwargs)

@register('cpustat')
def cpustat(**kwargs):
    return SdwanClient().cpustat(**kwargs)

@register('memstat')
def memstat(**kwargs):
    return SdwanClient().memstat(**kwargs)

@register('getSyncQueues')
def getSyncQueues(**kwargs):
    return SdwanClient().getSyncQueues(**kwargs)

@register('listReachableDevices')
def listReachableDevices(**kwargs):
    return SdwanClient().listReachableDevices(**kwargs)

@register('createRebootHistoryList')
def createRebootHistoryList(**kwargs):
    return SdwanClient().createRebootHistoryList(**kwargs)

@register('getRebootHistoryDetails')
def getRebootHistoryDetails(**kwargs):
    return SdwanClient().getRebootHistoryDetails(**kwargs)

@register('createSyncedRebootHistoryList')
def createSyncedRebootHistoryList(**kwargs):
    return SdwanClient().createSyncedRebootHistoryList(**kwargs)

@register('getRedundancyGroupAppGroup')
def getRedundancyGroupAppGroup(**kwargs):
    return SdwanClient().getRedundancyGroupAppGroup(**kwargs)

@register('getRoleBasedCounters')
def getRoleBasedCounters(**kwargs):
    return SdwanClient().getRoleBasedCounters(**kwargs)

@register('getRoleBasedIpv6Counters')
def getRoleBasedIpv6Counters(**kwargs):
    return SdwanClient().getRoleBasedIpv6Counters(**kwargs)

@register('getRoleBasedIpv6Permissions')
def getRoleBasedIpv6Permissions(**kwargs):
    return SdwanClient().getRoleBasedIpv6Permissions(**kwargs)

@register('getRoleBasedPermissions')
def getRoleBasedPermissions(**kwargs):
    return SdwanClient().getRoleBasedPermissions(**kwargs)

@register('getRoleBasedSgtMap')
def getRoleBasedSgtMap(**kwargs):
    return SdwanClient().getRoleBasedSgtMap(**kwargs)

@register('getSDWanGlobalDropStatistics')
def getSDWanGlobalDropStatistics(**kwargs):
    return SdwanClient().getSDWanGlobalDropStatistics(**kwargs)

@register('getSDWanStats')
def getSDWanStats(**kwargs):
    return SdwanClient().getSDWanStats(**kwargs)

@register('createSessionList')
def createSessionList(**kwargs):
    return SdwanClient().createSessionList(**kwargs)

@register('getDetail')
def getDetail(**kwargs):
    return SdwanClient().getDetail(**kwargs)

@register('getDiagnostic')
def getDiagnostic(**kwargs):
    return SdwanClient().getDiagnostic(**kwargs)

@register('getDiagnosticMeasurementAlarm')
def getDiagnosticMeasurementAlarm(**kwargs):
    return SdwanClient().getDiagnosticMeasurementAlarm(**kwargs)

@register('getDiagnosticMeasurementValue')
def getDiagnosticMeasurementValue(**kwargs):
    return SdwanClient().getDiagnosticMeasurementValue(**kwargs)

@register('getSigTunnelList')
def getSigTunnelList(**kwargs):
    return SdwanClient().getSigTunnelList(**kwargs)

@register('getSigTunnelTotal')
def getSigTunnelTotal(**kwargs):
    return SdwanClient().getSigTunnelTotal(**kwargs)

@register('tunnelDashboard')
def tunnelDashboard(**kwargs):
    return SdwanClient().tunnelDashboard(**kwargs)

@register('getSigUmbrellaTunnels')
def getSigUmbrellaTunnels(**kwargs):
    return SdwanClient().getSigUmbrellaTunnels(**kwargs)

@register('getSigZscalerTunnels')
def getSigZscalerTunnels(**kwargs):
    return SdwanClient().getSigZscalerTunnels(**kwargs)

@register('createSmuList')
def createSmuList(**kwargs):
    return SdwanClient().createSmuList(**kwargs)

@register('createSyncedSmuList')
def createSyncedSmuList(**kwargs):
    return SdwanClient().createSyncedSmuList(**kwargs)

@register('getAAAUcreateSoftwareListsers')
def getAAAUcreateSoftwareListsers(**kwargs):
    return SdwanClient().getAAAUcreateSoftwareListsers(**kwargs)

@register('createSyncedSoftwareList')
def createSyncedSoftwareList(**kwargs):
    return SdwanClient().createSyncedSoftwareList(**kwargs)

@register('getSSETunnel')
def getSSETunnel(**kwargs):
    return SdwanClient().getSSETunnel(**kwargs)

@register('getSslProxyStatistics')
def getSslProxyStatistics(**kwargs):
    return SdwanClient().getSslProxyStatistics(**kwargs)

@register('getSslProxyStatus')
def getSslProxyStatus(**kwargs):
    return SdwanClient().getSslProxyStatus(**kwargs)

@register('getStaticRouteTrackerInfo')
def getStaticRouteTrackerInfo(**kwargs):
    return SdwanClient().getStaticRouteTrackerInfo(**kwargs)

@register('getStatsQueues')
def getStatsQueues(**kwargs):
    return SdwanClient().getStatsQueues(**kwargs)

@register('getAllDeviceStatus')
def getAllDeviceStatus(**kwargs):
    return SdwanClient().getAllDeviceStatus(**kwargs)

@register('getSxpConnections')
def getSxpConnections(**kwargs):
    return SdwanClient().getSxpConnections(**kwargs)

@register('listCurrentlySyncingDevices')
def listCurrentlySyncingDevices(**kwargs):
    return SdwanClient().listCurrentlySyncingDevices(**kwargs)

@register('getDeviceSystemClock')
def getDeviceSystemClock(**kwargs):
    return SdwanClient().getDeviceSystemClock(**kwargs)

@register('createDeviceInfoList')
def createDeviceInfoList(**kwargs):
    return SdwanClient().createDeviceInfoList(**kwargs)

@register('createDeviceSystemStatsList')
def createDeviceSystemStatsList(**kwargs):
    return SdwanClient().createDeviceSystemStatsList(**kwargs)

@register('createDeviceSystemStatusList')
def createDeviceSystemStatusList(**kwargs):
    return SdwanClient().createDeviceSystemStatusList(**kwargs)

@register('createSyncedDeviceSystemStatusList')
def createSyncedDeviceSystemStatusList(**kwargs):
    return SdwanClient().createSyncedDeviceSystemStatusList(**kwargs)

@register('getActiveTCPFlows')
def getActiveTCPFlows(**kwargs):
    return SdwanClient().getActiveTCPFlows(**kwargs)

@register('getExpiredTCPFlows')
def getExpiredTCPFlows(**kwargs):
    return SdwanClient().getExpiredTCPFlows(**kwargs)

@register('getTCPSummary')
def getTCPSummary(**kwargs):
    return SdwanClient().getTCPSummary(**kwargs)

@register('getTcpProxyStatistics')
def getTcpProxyStatistics(**kwargs):
    return SdwanClient().getTcpProxyStatistics(**kwargs)

@register('getTcpProxyStatus')
def getTcpProxyStatus(**kwargs):
    return SdwanClient().getTcpProxyStatus(**kwargs)

@register('getTiers')
def getTiers(**kwargs):
    return SdwanClient().getTiers(**kwargs)

@register('getDeviceTlocStatus')
def getDeviceTlocStatus(**kwargs):
    return SdwanClient().getDeviceTlocStatus(**kwargs)

@register('getDeviceTlocUtil')
def getDeviceTlocUtil(**kwargs):
    return SdwanClient().getDeviceTlocUtil(**kwargs)

@register('getDeviceTlocUtilDetails')
def getDeviceTlocUtilDetails(**kwargs):
    return SdwanClient().getDeviceTlocUtilDetails(**kwargs)

@register('downloadAdminTechFile')
def downloadAdminTechFile(**kwargs):
    return SdwanClient().downloadAdminTechFile(**kwargs)

@register('getSupportedAdminTechFeatures')
def getSupportedAdminTechFeatures(**kwargs):
    return SdwanClient().getSupportedAdminTechFeatures(**kwargs)

@register('listAdminTechs')
def listAdminTechs(**kwargs):
    return SdwanClient().listAdminTechs(**kwargs)

@register('getInProgressCount')
def getInProgressCount(**kwargs):
    return SdwanClient().getInProgressCount(**kwargs)

@register('getDeviceToolsNetstat')
def getDeviceToolsNetstat(**kwargs):
    return SdwanClient().getDeviceToolsNetstat(**kwargs)

@register('getDeviceToolsNSlookup')
def getDeviceToolsNSlookup(**kwargs):
    return SdwanClient().getDeviceToolsNSlookup(**kwargs)

@register('getRealTimeinfo')
def getRealTimeinfo(**kwargs):
    return SdwanClient().getRealTimeinfo(**kwargs)

@register('getDeviceToolsSS')
def getDeviceToolsSS(**kwargs):
    return SdwanClient().getDeviceToolsSS(**kwargs)

@register('getSystemNetfilter')
def getSystemNetfilter(**kwargs):
    return SdwanClient().getSystemNetfilter(**kwargs)

@register('createTransportConnectionList')
def createTransportConnectionList(**kwargs):
    return SdwanClient().createTransportConnectionList(**kwargs)

@register('createBfdStatisticsList')
def createBfdStatisticsList(**kwargs):
    return SdwanClient().createBfdStatisticsList(**kwargs)

@register('createFecStatistics')
def createFecStatistics(**kwargs):
    return SdwanClient().createFecStatistics(**kwargs)

@register('createGreKeepalivesList')
def createGreKeepalivesList(**kwargs):
    return SdwanClient().createGreKeepalivesList(**kwargs)

@register('createIpsecStatisticsList')
def createIpsecStatisticsList(**kwargs):
    return SdwanClient().createIpsecStatisticsList(**kwargs)

@register('createPacketDuplicateStatistics')
def createPacketDuplicateStatistics(**kwargs):
    return SdwanClient().createPacketDuplicateStatistics(**kwargs)

@register('createStatisticsList')
def createStatisticsList(**kwargs):
    return SdwanClient().createStatisticsList(**kwargs)

@register('createUcseStats')
def createUcseStats(**kwargs):
    return SdwanClient().createUcseStats(**kwargs)

@register('getUmbrellaDevReg')
def getUmbrellaDevReg(**kwargs):
    return SdwanClient().getUmbrellaDevReg(**kwargs)

@register('getUmbrellaDNSCrypt')
def getUmbrellaDNSCrypt(**kwargs):
    return SdwanClient().getUmbrellaDNSCrypt(**kwargs)

@register('getUmbrellaDpStats')
def getUmbrellaDpStats(**kwargs):
    return SdwanClient().getUmbrellaDpStats(**kwargs)

@register('getUmbrellaOverview')
def getUmbrellaOverview(**kwargs):
    return SdwanClient().getUmbrellaOverview(**kwargs)

@register('getUmbrellaConfig')
def getUmbrellaConfig(**kwargs):
    return SdwanClient().getUmbrellaConfig(**kwargs)

@register('getUnclaimedVedges')
def getUnclaimedVedges(**kwargs):
    return SdwanClient().getUnclaimedVedges(**kwargs)

@register('getUnconfigured')
def getUnconfigured(**kwargs):
    return SdwanClient().getUnconfigured(**kwargs)

@register('listUnreachableDevices')
def listUnreachableDevices(**kwargs):
    return SdwanClient().listUnreachableDevices(**kwargs)

@register('getUsersFromDevice')
def getUsersFromDevice(**kwargs):
    return SdwanClient().getUsersFromDevice(**kwargs)

@register('getAllDeviceUsers')
def getAllDeviceUsers(**kwargs):
    return SdwanClient().getAllDeviceUsers(**kwargs)

@register('getUTDDataplaneConfig')
def getUTDDataplaneConfig(**kwargs):
    return SdwanClient().getUTDDataplaneConfig(**kwargs)

@register('getUTDDataplaneGlobal')
def getUTDDataplaneGlobal(**kwargs):
    return SdwanClient().getUTDDataplaneGlobal(**kwargs)

@register('getUTDDataplaneStats')
def getUTDDataplaneStats(**kwargs):
    return SdwanClient().getUTDDataplaneStats(**kwargs)

@register('getUTDDataplaneStatsSummary')
def getUTDDataplaneStatsSummary(**kwargs):
    return SdwanClient().getUTDDataplaneStatsSummary(**kwargs)

@register('getUTDEngineInstanceStatus')
def getUTDEngineInstanceStatus(**kwargs):
    return SdwanClient().getUTDEngineInstanceStatus(**kwargs)

@register('getUTDEngineStatus')
def getUTDEngineStatus(**kwargs):
    return SdwanClient().getUTDEngineStatus(**kwargs)

@register('getUTDFileAnalysisStatus')
def getUTDFileAnalysisStatus(**kwargs):
    return SdwanClient().getUTDFileAnalysisStatus(**kwargs)

@register('getUTDFileReputationStatus')
def getUTDFileReputationStatus(**kwargs):
    return SdwanClient().getUTDFileReputationStatus(**kwargs)

@register('getUTDIpsUpdateStatus')
def getUTDIpsUpdateStatus(**kwargs):
    return SdwanClient().getUTDIpsUpdateStatus(**kwargs)

@register('getSignatureVersionInfo')
def getSignatureVersionInfo(**kwargs):
    return SdwanClient().getSignatureVersionInfo(**kwargs)

@register('getUTDUrlfConnectionStatus')
def getUTDUrlfConnectionStatus(**kwargs):
    return SdwanClient().getUTDUrlfConnectionStatus(**kwargs)

@register('getUTDUrlfUpdateStatus')
def getUTDUrlfUpdateStatus(**kwargs):
    return SdwanClient().getUTDUrlfUpdateStatus(**kwargs)

@register('getUTDVersionStatus')
def getUTDVersionStatus(**kwargs):
    return SdwanClient().getUTDVersionStatus(**kwargs)

@register('getCoLineSpecificStats')
def getCoLineSpecificStats(**kwargs):
    return SdwanClient().getCoLineSpecificStats(**kwargs)

@register('getCoStats')
def getCoStats(**kwargs):
    return SdwanClient().getCoStats(**kwargs)

@register('getCpeLineSpecificStats')
def getCpeLineSpecificStats(**kwargs):
    return SdwanClient().getCpeLineSpecificStats(**kwargs)

@register('getCpeStats')
def getCpeStats(**kwargs):
    return SdwanClient().getCpeStats(**kwargs)

@register('getLineBondingStats')
def getLineBondingStats(**kwargs):
    return SdwanClient().getLineBondingStats(**kwargs)

@register('getLineSpecificStats')
def getLineSpecificStats(**kwargs):
    return SdwanClient().getLineSpecificStats(**kwargs)

@register('getVdslInfo')
def getVdslInfo(**kwargs):
    return SdwanClient().getVdslInfo(**kwargs)

@register('getVedgeInventory')
def getVedgeInventory(**kwargs):
    return SdwanClient().getVedgeInventory(**kwargs)

@register('getVedgeInventorySummary')
def getVedgeInventorySummary(**kwargs):
    return SdwanClient().getVedgeInventorySummary(**kwargs)

@register('createTeList')
def createTeList(**kwargs):
    return SdwanClient().createTeList(**kwargs)

@register('createUtdList')
def createUtdList(**kwargs):
    return SdwanClient().createUtdList(**kwargs)

@register('createWaasList')
def createWaasList(**kwargs):
    return SdwanClient().createWaasList(**kwargs)

@register('getVbranchVMLifecycleNics')
def getVbranchVMLifecycleNics(**kwargs):
    return SdwanClient().getVbranchVMLifecycleNics(**kwargs)

@register('getCloudDockVMLifecycleNics')
def getCloudDockVMLifecycleNics(**kwargs):
    return SdwanClient().getCloudDockVMLifecycleNics(**kwargs)

@register('getVbranchVMLifecycle')
def getVbranchVMLifecycle(**kwargs):
    return SdwanClient().getVbranchVMLifecycle(**kwargs)

@register('getVMLifeCycleState')
def getVMLifeCycleState(**kwargs):
    return SdwanClient().getVMLifeCycleState(**kwargs)

@register('getVManageSystemIP')
def getVManageSystemIP(**kwargs):
    return SdwanClient().getVManageSystemIP(**kwargs)

@register('getDspActive')
def getDspActive(**kwargs):
    return SdwanClient().getDspActive(**kwargs)

@register('getPhoneInfo')
def getPhoneInfo(**kwargs):
    return SdwanClient().getPhoneInfo(**kwargs)

@register('getDSPFarmProfiles')
def getDSPFarmProfiles(**kwargs):
    return SdwanClient().getDSPFarmProfiles(**kwargs)

@register('getSccpCcmGroups')
def getSccpCcmGroups(**kwargs):
    return SdwanClient().getSccpCcmGroups(**kwargs)

@register('getSccpConnections')
def getSccpConnections(**kwargs):
    return SdwanClient().getSccpConnections(**kwargs)

@register('getVoiceCalls')
def getVoiceCalls(**kwargs):
    return SdwanClient().getVoiceCalls(**kwargs)

@register('getVoipCalls')
def getVoipCalls(**kwargs):
    return SdwanClient().getVoipCalls(**kwargs)

@register('getT1e1IsdnStatus')
def getT1e1IsdnStatus(**kwargs):
    return SdwanClient().getT1e1IsdnStatus(**kwargs)

@register('getControllerT1e1InfoCurrent15MinStats')
def getControllerT1e1InfoCurrent15MinStats(**kwargs):
    return SdwanClient().getControllerT1e1InfoCurrent15MinStats(**kwargs)

@register('getControllerT1e1InfoTotalStats')
def getControllerT1e1InfoTotalStats(**kwargs):
    return SdwanClient().getControllerT1e1InfoTotalStats(**kwargs)

@register('getVPNInstances')
def getVPNInstances(**kwargs):
    return SdwanClient().getVPNInstances(**kwargs)

@register('getVRRPInterface')
def getVRRPInterface(**kwargs):
    return SdwanClient().getVRRPInterface(**kwargs)

@register('getWirelessClients')
def getWirelessClients(**kwargs):
    return SdwanClient().getWirelessClients(**kwargs)

@register('getWirelessRadios')
def getWirelessRadios(**kwargs):
    return SdwanClient().getWirelessRadios(**kwargs)

@register('getWirelessSsid')
def getWirelessSsid(**kwargs):
    return SdwanClient().getWirelessSsid(**kwargs)

@register('getWLANClients')
def getWLANClients(**kwargs):
    return SdwanClient().getWLANClients(**kwargs)

@register('getWLANInterfaces')
def getWLANInterfaces(**kwargs):
    return SdwanClient().getWLANInterfaces(**kwargs)

@register('getWLANRadios')
def getWLANRadios(**kwargs):
    return SdwanClient().getWLANRadios(**kwargs)

@register('getWLANRadius')
def getWLANRadius(**kwargs):
    return SdwanClient().getWLANRadius(**kwargs)

@register('getClusterInfo')
def getClusterInfo(**kwargs):
    return SdwanClient().getClusterInfo(**kwargs)

@register('getConfigDBRestoreStatus')
def getConfigDBRestoreStatus(**kwargs):
    return SdwanClient().getConfigDBRestoreStatus(**kwargs)

@register('getDetails')
def getDetails(**kwargs):
    return SdwanClient().getDetails(**kwargs)

@register('getDisasterRecoveryStatus')
def getDisasterRecoveryStatus(**kwargs):
    return SdwanClient().getDisasterRecoveryStatus(**kwargs)

@register('getHistory')
def getHistory(**kwargs):
    return SdwanClient().getHistory(**kwargs)

@register('getLocalHistory')
def getLocalHistory(**kwargs):
    return SdwanClient().getLocalHistory(**kwargs)

@register('getLocalDataCenterState')
def getLocalDataCenterState(**kwargs):
    return SdwanClient().getLocalDataCenterState(**kwargs)

@register('getRemoteDCMembersState')
def getRemoteDCMembersState(**kwargs):
    return SdwanClient().getRemoteDCMembersState(**kwargs)

@register('getRemoteDataCenterState')
def getRemoteDataCenterState(**kwargs):
    return SdwanClient().getRemoteDataCenterState(**kwargs)

@register('getRemoteDataCenterVersion')
def getRemoteDataCenterVersion(**kwargs):
    return SdwanClient().getRemoteDataCenterVersion(**kwargs)

@register('getDisasterRecoveryLocalReplicationSchedule')
def getDisasterRecoveryLocalReplicationSchedule(**kwargs):
    return SdwanClient().getDisasterRecoveryLocalReplicationSchedule(**kwargs)

@register('getdrStatus')
def getdrStatus(**kwargs):
    return SdwanClient().getdrStatus(**kwargs)

@register('get')
def get(**kwargs):
    return SdwanClient().get(**kwargs)

@register('listEntityOwnershipInfo')
def listEntityOwnershipInfo(**kwargs):
    return SdwanClient().listEntityOwnershipInfo(**kwargs)

@register('entityOwnershipInfo')
def entityOwnershipInfo(**kwargs):
    return SdwanClient().entityOwnershipInfo(**kwargs)

@register('getEvents')
def getEvents(**kwargs):
    return SdwanClient().getEvents(**kwargs)

@register('getAggregationData_1')
def getAggregationData_1(**kwargs):
    return SdwanClient().getAggregationData_1(**kwargs)

@register('getComponentsAsKeyValue')
def getComponentsAsKeyValue(**kwargs):
    return SdwanClient().getComponentsAsKeyValue(**kwargs)

@register('getDocCount_2')
def getDocCount_2(**kwargs):
    return SdwanClient().getDocCount_2(**kwargs)

@register('enableEventsFromFile')
def enableEventsFromFile(**kwargs):
    return SdwanClient().enableEventsFromFile(**kwargs)

@register('getEventNamesByComponent')
def getEventNamesByComponent(**kwargs):
    return SdwanClient().getEventNamesByComponent(**kwargs)

@register('getListenersInfo')
def getListenersInfo(**kwargs):
    return SdwanClient().getListenersInfo(**kwargs)

@register('getPage_1')
def getPage_1(**kwargs):
    return SdwanClient().getPage_1(**kwargs)

@register('getQueryFields')
def getQueryFields(**kwargs):
    return SdwanClient().getQueryFields(**kwargs)

@register('createEventsQueryConfig')
def createEventsQueryConfig(**kwargs):
    return SdwanClient().createEventsQueryConfig(**kwargs)

@register('getBySeverities')
def getBySeverities(**kwargs):
    return SdwanClient().getBySeverities(**kwargs)

@register('getSeverityHistogram')
def getSeverityHistogram(**kwargs):
    return SdwanClient().getSeverityHistogram(**kwargs)

@register('getEventTypesAsKeyValue')
def getEventTypesAsKeyValue(**kwargs):
    return SdwanClient().getEventTypesAsKeyValue(**kwargs)

@register('getDeviceCertificate')
def getDeviceCertificate(**kwargs):
    return SdwanClient().getDeviceCertificate(**kwargs)

@register('getDeviceCsr')
def getDeviceCsr(**kwargs):
    return SdwanClient().getDeviceCsr(**kwargs)

@register('getFeatureCaState')
def getFeatureCaState(**kwargs):
    return SdwanClient().getFeatureCaState(**kwargs)

@register('requesDNSSecActions')
def requesDNSSecActions(**kwargs):
    return SdwanClient().requesDNSSecActions(**kwargs)

@register('getDNSSecStatus')
def getDNSSecStatus(**kwargs):
    return SdwanClient().getDNSSecStatus(**kwargs)

@register('requestWazuhActions')
def requestWazuhActions(**kwargs):
    return SdwanClient().requestWazuhActions(**kwargs)

@register('getWazuhAgentStatus')
def getWazuhAgentStatus(**kwargs):
    return SdwanClient().getWazuhAgentStatus(**kwargs)

@register('listDeviceGroupList')
def listDeviceGroupList(**kwargs):
    return SdwanClient().listDeviceGroupList(**kwargs)

@register('listDeviceGroups')
def listDeviceGroups(**kwargs):
    return SdwanClient().listDeviceGroups(**kwargs)

@register('listGroupDevices')
def listGroupDevices(**kwargs):
    return SdwanClient().listGroupDevices(**kwargs)

@register('listGroupDevicesForMap')
def listGroupDevicesForMap(**kwargs):
    return SdwanClient().listGroupDevicesForMap(**kwargs)

@register('listGroupLinksForMap')
def listGroupLinksForMap(**kwargs):
    return SdwanClient().listGroupLinksForMap(**kwargs)

@register('getDevicesHealth')
def getDevicesHealth(**kwargs):
    return SdwanClient().getDevicesHealth(**kwargs)

@register('getDevicesHealthOverview')
def getDevicesHealthOverview(**kwargs):
    return SdwanClient().getDevicesHealthOverview(**kwargs)

@register('fetchDeviceDetails')
def fetchDeviceDetails(**kwargs):
    return SdwanClient().fetchDeviceDetails(**kwargs)

@register('InstallDeviceDetails')
def InstallDeviceDetails(**kwargs):
    return SdwanClient().InstallDeviceDetails(**kwargs)

@register('fetchSAVAAccounts')
def fetchSAVAAccounts(**kwargs):
    return SdwanClient().fetchSAVAAccounts(**kwargs)

@register('testbedMode')
def testbedMode(**kwargs):
    return SdwanClient().testbedMode(**kwargs)

@register('connect_1')
def connect_1(**kwargs):
    return SdwanClient().connect_1(**kwargs)

@register('getIseServerCredentials')
def getIseServerCredentials(**kwargs):
    return SdwanClient().getIseServerCredentials(**kwargs)

@register('getPxGridAccount')
def getPxGridAccount(**kwargs):
    return SdwanClient().getPxGridAccount(**kwargs)

@register('getPxgridCert')
def getPxgridCert(**kwargs):
    return SdwanClient().getPxgridCert(**kwargs)

@register('getSupportedLocales')
def getSupportedLocales(**kwargs):
    return SdwanClient().getSupportedLocales(**kwargs)

@register('getCategory')
def getCategory(**kwargs):
    return SdwanClient().getCategory(**kwargs)

@register('getvManageResourceUtilization')
def getvManageResourceUtilization(**kwargs):
    return SdwanClient().getvManageResourceUtilization(**kwargs)

@register('retrieveMDPAttachedDevices')
def retrieveMDPAttachedDevices(**kwargs):
    return SdwanClient().retrieveMDPAttachedDevices(**kwargs)

@register('retrieveMDPSupportedDevices')
def retrieveMDPSupportedDevices(**kwargs):
    return SdwanClient().retrieveMDPSupportedDevices(**kwargs)

@register('disconnectFromMDP')
def disconnectFromMDP(**kwargs):
    return SdwanClient().disconnectFromMDP(**kwargs)

@register('getMDPOnboardingStatus')
def getMDPOnboardingStatus(**kwargs):
    return SdwanClient().getMDPOnboardingStatus(**kwargs)

@register('retrieveMDPConfigObject')
def retrieveMDPConfigObject(**kwargs):
    return SdwanClient().retrieveMDPConfigObject(**kwargs)

@register('retrieveMDPPolicies')
def retrieveMDPPolicies(**kwargs):
    return SdwanClient().retrieveMDPPolicies(**kwargs)

@register('createDeviceVmanageConnectionList')
def createDeviceVmanageConnectionList(**kwargs):
    return SdwanClient().createDeviceVmanageConnectionList(**kwargs)

@register('getCloudConnectorDomainAppRules')
def getCloudConnectorDomainAppRules(**kwargs):
    return SdwanClient().getCloudConnectorDomainAppRules(**kwargs)

@register('getCloudConnectorIpAddressAppRules')
def getCloudConnectorIpAddressAppRules(**kwargs):
    return SdwanClient().getCloudConnectorIpAddressAppRules(**kwargs)

@register('getWebexAppData')
def getWebexAppData(**kwargs):
    return SdwanClient().getWebexAppData(**kwargs)

@register('getMSLADevices_1')
def getMSLADevices_1(**kwargs):
    return SdwanClient().getMSLADevices_1(**kwargs)

@register('getLicenseByUuid_1')
def getLicenseByUuid_1(**kwargs):
    return SdwanClient().getLicenseByUuid_1(**kwargs)

@register('getMslaLicenses')
def getMslaLicenses(**kwargs):
    return SdwanClient().getMslaLicenses(**kwargs)

@register('getLicensesCompliance')
def getLicensesCompliance(**kwargs):
    return SdwanClient().getLicensesCompliance(**kwargs)

@register('getDeviceDetailsForDashboard')
def getDeviceDetailsForDashboard(**kwargs):
    return SdwanClient().getDeviceDetailsForDashboard(**kwargs)

@register('getLicenseDistributionDetails')
def getLicenseDistributionDetails(**kwargs):
    return SdwanClient().getLicenseDistributionDetails(**kwargs)

@register('getPackagingDistributionDetails')
def getPackagingDistributionDetails(**kwargs):
    return SdwanClient().getPackagingDistributionDetails(**kwargs)

@register('getAllTemplate')
def getAllTemplate(**kwargs):
    return SdwanClient().getAllTemplate(**kwargs)

@register('getSubscriptions')
def getSubscriptions(**kwargs):
    return SdwanClient().getSubscriptions(**kwargs)

@register('getAllCloudAccounts')
def getAllCloudAccounts(**kwargs):
    return SdwanClient().getAllCloudAccounts(**kwargs)

@register('getEdgeAccounts')
def getEdgeAccounts(**kwargs):
    return SdwanClient().getEdgeAccounts(**kwargs)

@register('getEdgeAccountDetails')
def getEdgeAccountDetails(**kwargs):
    return SdwanClient().getEdgeAccountDetails(**kwargs)

@register('getCloudAccountDetails')
def getCloudAccountDetails(**kwargs):
    return SdwanClient().getCloudAccountDetails(**kwargs)

@register('auditDryRun')
def auditDryRun(**kwargs):
    return SdwanClient().auditDryRun(**kwargs)

@register('getEdgeBillingAccounts')
def getEdgeBillingAccounts(**kwargs):
    return SdwanClient().getEdgeBillingAccounts(**kwargs)

@register('getCloudRoutersAndAttachments')
def getCloudRoutersAndAttachments(**kwargs):
    return SdwanClient().getCloudRoutersAndAttachments(**kwargs)

@register('getCgws')
def getCgws(**kwargs):
    return SdwanClient().getCgws(**kwargs)

@register('getNvaSecurityRules')
def getNvaSecurityRules(**kwargs):
    return SdwanClient().getNvaSecurityRules(**kwargs)

@register('getAzureNetworkVirtualAppliances')
def getAzureNetworkVirtualAppliances(**kwargs):
    return SdwanClient().getAzureNetworkVirtualAppliances(**kwargs)

@register('getAzureNvaSkuResources')
def getAzureNvaSkuResources(**kwargs):
    return SdwanClient().getAzureNvaSkuResources(**kwargs)

@register('getCgwOrgResources')
def getCgwOrgResources(**kwargs):
    return SdwanClient().getCgwOrgResources(**kwargs)

@register('getAzureResourceGroups')
def getAzureResourceGroups(**kwargs):
    return SdwanClient().getAzureResourceGroups(**kwargs)

@register('getAzureVirtualHubs')
def getAzureVirtualHubs(**kwargs):
    return SdwanClient().getAzureVirtualHubs(**kwargs)

@register('getAzureVirtualVnetsAttached')
def getAzureVirtualVnetsAttached(**kwargs):
    return SdwanClient().getAzureVirtualVnetsAttached(**kwargs)

@register('getAzureVpnGateways')
def getAzureVpnGateways(**kwargs):
    return SdwanClient().getAzureVpnGateways(**kwargs)

@register('getAzureVirtualWans')
def getAzureVirtualWans(**kwargs):
    return SdwanClient().getAzureVirtualWans(**kwargs)

@register('getCgwDetails')
def getCgwDetails(**kwargs):
    return SdwanClient().getCgwDetails(**kwargs)

@register('getCgwAttachedSites')
def getCgwAttachedSites(**kwargs):
    return SdwanClient().getCgwAttachedSites(**kwargs)

@register('getAvailableDevicesOrByCGId')
def getAvailableDevicesOrByCGId(**kwargs):
    return SdwanClient().getAvailableDevicesOrByCGId(**kwargs)

@register('getCloudGateways')
def getCloudGateways(**kwargs):
    return SdwanClient().getCloudGateways(**kwargs)

@register('getCgwCustomSettingDetails')
def getCgwCustomSettingDetails(**kwargs):
    return SdwanClient().getCgwCustomSettingDetails(**kwargs)

@register('getCgwTypes')
def getCgwTypes(**kwargs):
    return SdwanClient().getCgwTypes(**kwargs)

@register('getCloudConnectedSites_1')
def getCloudConnectedSites_1(**kwargs):
    return SdwanClient().getCloudConnectedSites_1(**kwargs)

@register('getCloudConnectedSites')
def getCloudConnectedSites(**kwargs):
    return SdwanClient().getCloudConnectedSites(**kwargs)

@register('getEdgeConnectivityDetails')
def getEdgeConnectivityDetails(**kwargs):
    return SdwanClient().getEdgeConnectivityDetails(**kwargs)

@register('getEdgeConnectivityDetailByName')
def getEdgeConnectivityDetailByName(**kwargs):
    return SdwanClient().getEdgeConnectivityDetailByName(**kwargs)

@register('getConnectivityGateways')
def getConnectivityGateways(**kwargs):
    return SdwanClient().getConnectivityGateways(**kwargs)

@register('getConnectivityGatewayCreationOptions')
def getConnectivityGatewayCreationOptions(**kwargs):
    return SdwanClient().getConnectivityGatewayCreationOptions(**kwargs)

@register('getCwanCoreNetworkPolicy')
def getCwanCoreNetworkPolicy(**kwargs):
    return SdwanClient().getCwanCoreNetworkPolicy(**kwargs)

@register('getDashboardEdgeInfo')
def getDashboardEdgeInfo(**kwargs):
    return SdwanClient().getDashboardEdgeInfo(**kwargs)

@register('getWanDevices')
def getWanDevices(**kwargs):
    return SdwanClient().getWanDevices(**kwargs)

@register('getDeviceLinks')
def getDeviceLinks(**kwargs):
    return SdwanClient().getDeviceLinks(**kwargs)

@register('getDlPortSpeed')
def getDlPortSpeed(**kwargs):
    return SdwanClient().getDlPortSpeed(**kwargs)

@register('getCloudDevices_1')
def getCloudDevices_1(**kwargs):
    return SdwanClient().getCloudDevices_1(**kwargs)

@register('getCloudDevices')
def getCloudDevices(**kwargs):
    return SdwanClient().getCloudDevices(**kwargs)

@register('getEdgeWanDevices')
def getEdgeWanDevices(**kwargs):
    return SdwanClient().getEdgeWanDevices(**kwargs)

@register('getIcgws')
def getIcgws(**kwargs):
    return SdwanClient().getIcgws(**kwargs)

@register('getIcgwCustomSettingDetails')
def getIcgwCustomSettingDetails(**kwargs):
    return SdwanClient().getIcgwCustomSettingDetails(**kwargs)

@register('getIcgwTypes')
def getIcgwTypes(**kwargs):
    return SdwanClient().getIcgwTypes(**kwargs)

@register('getIcgwDetails')
def getIcgwDetails(**kwargs):
    return SdwanClient().getIcgwDetails(**kwargs)

@register('getEdgeGateways')
def getEdgeGateways(**kwargs):
    return SdwanClient().getEdgeGateways(**kwargs)

@register('getHostVpcs')
def getHostVpcs(**kwargs):
    return SdwanClient().getHostVpcs(**kwargs)

@register('getVpcTags')
def getVpcTags(**kwargs):
    return SdwanClient().getVpcTags(**kwargs)

@register('getSupportedEdgeImageNames')
def getSupportedEdgeImageNames(**kwargs):
    return SdwanClient().getSupportedEdgeImageNames(**kwargs)

@register('getSupportedInstanceSize')
def getSupportedInstanceSize(**kwargs):
    return SdwanClient().getSupportedInstanceSize(**kwargs)

@register('getSupportedEdgeInstanceSize')
def getSupportedEdgeInstanceSize(**kwargs):
    return SdwanClient().getSupportedEdgeInstanceSize(**kwargs)

@register('getInterconnectAccounts')
def getInterconnectAccounts(**kwargs):
    return SdwanClient().getInterconnectAccounts(**kwargs)

@register('getInterconnectAccount')
def getInterconnectAccount(**kwargs):
    return SdwanClient().getInterconnectAccount(**kwargs)

@register('getAuditReport')
def getAuditReport(**kwargs):
    return SdwanClient().getAuditReport(**kwargs)

@register('getGoogleCloudRouterAndAttachments')
def getGoogleCloudRouterAndAttachments(**kwargs):
    return SdwanClient().getGoogleCloudRouterAndAttachments(**kwargs)

@register('getAwsTransitGateways')
def getAwsTransitGateways(**kwargs):
    return SdwanClient().getAwsTransitGateways(**kwargs)

@register('getAzVirtualHubs')
def getAzVirtualHubs(**kwargs):
    return SdwanClient().getAzVirtualHubs(**kwargs)

@register('getAzVirtualWans')
def getAzVirtualWans(**kwargs):
    return SdwanClient().getAzVirtualWans(**kwargs)

@register('getCloudConnectivityGateways')
def getCloudConnectivityGateways(**kwargs):
    return SdwanClient().getCloudConnectivityGateways(**kwargs)

@register('getCloudConnectivityGatewayCreateOptions')
def getCloudConnectivityGatewayCreateOptions(**kwargs):
    return SdwanClient().getCloudConnectivityGatewayCreateOptions(**kwargs)

@register('getInterconnectColors')
def getInterconnectColors(**kwargs):
    return SdwanClient().getInterconnectColors(**kwargs)

@register('getInterconnectOnRampGatewayConnections')
def getInterconnectOnRampGatewayConnections(**kwargs):
    return SdwanClient().getInterconnectOnRampGatewayConnections(**kwargs)

@register('getInterconnectOnRampGatewayConnection')
def getInterconnectOnRampGatewayConnection(**kwargs):
    return SdwanClient().getInterconnectOnRampGatewayConnection(**kwargs)

@register('getInterconnectMappingTags')
def getInterconnectMappingTags(**kwargs):
    return SdwanClient().getInterconnectMappingTags(**kwargs)

@register('getInterconnectDeviceLinks')
def getInterconnectDeviceLinks(**kwargs):
    return SdwanClient().getInterconnectDeviceLinks(**kwargs)

@register('getInterconnectDeviceLink')
def getInterconnectDeviceLink(**kwargs):
    return SdwanClient().getInterconnectDeviceLink(**kwargs)

@register('getInterconnectCrossConnections')
def getInterconnectCrossConnections(**kwargs):
    return SdwanClient().getInterconnectCrossConnections(**kwargs)

@register('getInterconnectCrossConnection')
def getInterconnectCrossConnection(**kwargs):
    return SdwanClient().getInterconnectCrossConnection(**kwargs)

@register('getInterconnectVirtualNetworkConnections')
def getInterconnectVirtualNetworkConnections(**kwargs):
    return SdwanClient().getInterconnectVirtualNetworkConnections(**kwargs)

@register('getInterconnectVirtualNetworkConnection')
def getInterconnectVirtualNetworkConnection(**kwargs):
    return SdwanClient().getInterconnectVirtualNetworkConnection(**kwargs)

@register('getInterconnectDashboard')
def getInterconnectDashboard(**kwargs):
    return SdwanClient().getInterconnectDashboard(**kwargs)

@register('getInterconnectLicenses')
def getInterconnectLicenses(**kwargs):
    return SdwanClient().getInterconnectLicenses(**kwargs)

@register('getInterconnectGateways')
def getInterconnectGateways(**kwargs):
    return SdwanClient().getInterconnectGateways(**kwargs)

@register('getInterconnectGatewayImageNames')
def getInterconnectGatewayImageNames(**kwargs):
    return SdwanClient().getInterconnectGatewayImageNames(**kwargs)

@register('getInterconnectGatewayInstanceSizes')
def getInterconnectGatewayInstanceSizes(**kwargs):
    return SdwanClient().getInterconnectGatewayInstanceSizes(**kwargs)

@register('getInterconnetGatewayTypes')
def getInterconnetGatewayTypes(**kwargs):
    return SdwanClient().getInterconnetGatewayTypes(**kwargs)

@register('getInterconnectGateway')
def getInterconnectGateway(**kwargs):
    return SdwanClient().getInterconnectGateway(**kwargs)

@register('getInterconnectGatewayCustomSettings')
def getInterconnectGatewayCustomSettings(**kwargs):
    return SdwanClient().getInterconnectGatewayCustomSettings(**kwargs)

@register('getInterconnectIpTransit')
def getInterconnectIpTransit(**kwargs):
    return SdwanClient().getInterconnectIpTransit(**kwargs)

@register('getInterconnectServiceSwPkg')
def getInterconnectServiceSwPkg(**kwargs):
    return SdwanClient().getInterconnectServiceSwPkg(**kwargs)

@register('getInterconnectServices')
def getInterconnectServices(**kwargs):
    return SdwanClient().getInterconnectServices(**kwargs)

@register('getInterconnectGlobalSettings')
def getInterconnectGlobalSettings(**kwargs):
    return SdwanClient().getInterconnectGlobalSettings(**kwargs)

@register('getInterconnectSshKeys')
def getInterconnectSshKeys(**kwargs):
    return SdwanClient().getInterconnectSshKeys(**kwargs)

@register('getInterconnectTypes')
def getInterconnectTypes(**kwargs):
    return SdwanClient().getInterconnectTypes(**kwargs)

@register('getAllInterconnectWidgets')
def getAllInterconnectWidgets(**kwargs):
    return SdwanClient().getAllInterconnectWidgets(**kwargs)

@register('getInterconnectBillingAccounts')
def getInterconnectBillingAccounts(**kwargs):
    return SdwanClient().getInterconnectBillingAccounts(**kwargs)

@register('getInterconnectPartnerPorts')
def getInterconnectPartnerPorts(**kwargs):
    return SdwanClient().getInterconnectPartnerPorts(**kwargs)

@register('getInterconnectPortSpeeds')
def getInterconnectPortSpeeds(**kwargs):
    return SdwanClient().getInterconnectPortSpeeds(**kwargs)

@register('getInterconnectLocationInfo')
def getInterconnectLocationInfo(**kwargs):
    return SdwanClient().getInterconnectLocationInfo(**kwargs)

@register('getInterconnectConfigGroupTopology')
def getInterconnectConfigGroupTopology(**kwargs):
    return SdwanClient().getInterconnectConfigGroupTopology(**kwargs)

@register('getInterconnectDeviceLinkPortSpeeds')
def getInterconnectDeviceLinkPortSpeeds(**kwargs):
    return SdwanClient().getInterconnectDeviceLinkPortSpeeds(**kwargs)

@register('getAvailableDevicesOrByCGId_1')
def getAvailableDevicesOrByCGId_1(**kwargs):
    return SdwanClient().getAvailableDevicesOrByCGId_1(**kwargs)

@register('getInterconnectGatewayDevices')
def getInterconnectGatewayDevices(**kwargs):
    return SdwanClient().getInterconnectGatewayDevices(**kwargs)

@register('getMonitoringInterconnectConnectedSites')
def getMonitoringInterconnectConnectedSites(**kwargs):
    return SdwanClient().getMonitoringInterconnectConnectedSites(**kwargs)

@register('getMonitoringInterconnectDevices')
def getMonitoringInterconnectDevices(**kwargs):
    return SdwanClient().getMonitoringInterconnectDevices(**kwargs)

@register('getMonitoringInterconnectGateways')
def getMonitoringInterconnectGateways(**kwargs):
    return SdwanClient().getMonitoringInterconnectGateways(**kwargs)

@register('getInterconnectWidget')
def getInterconnectWidget(**kwargs):
    return SdwanClient().getInterconnectWidget(**kwargs)

@register('getWanInterfaceColors')
def getWanInterfaceColors(**kwargs):
    return SdwanClient().getWanInterfaceColors(**kwargs)

@register('getLicenses')
def getLicenses(**kwargs):
    return SdwanClient().getLicenses(**kwargs)

@register('getEdgeLocationsInfo')
def getEdgeLocationsInfo(**kwargs):
    return SdwanClient().getEdgeLocationsInfo(**kwargs)

@register('getSupportedLoopbackCgwColors')
def getSupportedLoopbackCgwColors(**kwargs):
    return SdwanClient().getSupportedLoopbackCgwColors(**kwargs)

@register('getSupportedLoopbackTransportColors')
def getSupportedLoopbackTransportColors(**kwargs):
    return SdwanClient().getSupportedLoopbackTransportColors(**kwargs)

@register('getMappingMatrix')
def getMappingMatrix(**kwargs):
    return SdwanClient().getMappingMatrix(**kwargs)

@register('getDefaultMappingValues')
def getDefaultMappingValues(**kwargs):
    return SdwanClient().getDefaultMappingValues(**kwargs)

@register('getMappingStatus')
def getMappingStatus(**kwargs):
    return SdwanClient().getMappingStatus(**kwargs)

@register('getMappingSummary')
def getMappingSummary(**kwargs):
    return SdwanClient().getMappingSummary(**kwargs)

@register('getMappingTags')
def getMappingTags(**kwargs):
    return SdwanClient().getMappingTags(**kwargs)

@register('getEdgeMappingTags')
def getEdgeMappingTags(**kwargs):
    return SdwanClient().getEdgeMappingTags(**kwargs)

@register('getMappingVpns')
def getMappingVpns(**kwargs):
    return SdwanClient().getMappingVpns(**kwargs)

@register('getCgwAssociatedMappings')
def getCgwAssociatedMappings(**kwargs):
    return SdwanClient().getCgwAssociatedMappings(**kwargs)

@register('getPartnerPorts')
def getPartnerPorts(**kwargs):
    return SdwanClient().getPartnerPorts(**kwargs)

@register('getPortSpeed')
def getPortSpeed(**kwargs):
    return SdwanClient().getPortSpeed(**kwargs)

@register('getCloudRegions')
def getCloudRegions(**kwargs):
    return SdwanClient().getCloudRegions(**kwargs)

@register('getEdgeGlobalSettings')
def getEdgeGlobalSettings(**kwargs):
    return SdwanClient().getEdgeGlobalSettings(**kwargs)

@register('getGlobalSettings')
def getGlobalSettings(**kwargs):
    return SdwanClient().getGlobalSettings(**kwargs)

@register('getSites')
def getSites(**kwargs):
    return SdwanClient().getSites(**kwargs)

@register('getSshKeyList')
def getSshKeyList(**kwargs):
    return SdwanClient().getSshKeyList(**kwargs)

@register('getSupportedSoftwareImageList')
def getSupportedSoftwareImageList(**kwargs):
    return SdwanClient().getSupportedSoftwareImageList(**kwargs)

@register('getTunnelNames')
def getTunnelNames(**kwargs):
    return SdwanClient().getTunnelNames(**kwargs)

@register('getCloudTypes')
def getCloudTypes(**kwargs):
    return SdwanClient().getCloudTypes(**kwargs)

@register('getEdgeTypes')
def getEdgeTypes(**kwargs):
    return SdwanClient().getEdgeTypes(**kwargs)

@register('getVHubs')
def getVHubs(**kwargs):
    return SdwanClient().getVHubs(**kwargs)

@register('getVWans')
def getVWans(**kwargs):
    return SdwanClient().getVWans(**kwargs)

@register('getAllCloudWidgets')
def getAllCloudWidgets(**kwargs):
    return SdwanClient().getAllCloudWidgets(**kwargs)

@register('getAllEdgeWidgets')
def getAllEdgeWidgets(**kwargs):
    return SdwanClient().getAllEdgeWidgets(**kwargs)

@register('getEdgeWidget')
def getEdgeWidget(**kwargs):
    return SdwanClient().getEdgeWidget(**kwargs)

@register('getCloudWidget')
def getCloudWidget(**kwargs):
    return SdwanClient().getCloudWidget(**kwargs)

@register('getMultiCloudConfigGroupTopology')
def getMultiCloudConfigGroupTopology(**kwargs):
    return SdwanClient().getMultiCloudConfigGroupTopology(**kwargs)

@register('getVmanageControlStatus')
def getVmanageControlStatus(**kwargs):
    return SdwanClient().getVmanageControlStatus(**kwargs)

@register('getRebootCount')
def getRebootCount(**kwargs):
    return SdwanClient().getRebootCount(**kwargs)

@register('getNetworkIssuesSummary')
def getNetworkIssuesSummary(**kwargs):
    return SdwanClient().getNetworkIssuesSummary(**kwargs)

@register('getNetworkStatusSummary')
def getNetworkStatusSummary(**kwargs):
    return SdwanClient().getNetworkStatusSummary(**kwargs)

@register('getNetworkDesign')
def getNetworkDesign(**kwargs):
    return SdwanClient().getNetworkDesign(**kwargs)

@register('getCircuits')
def getCircuits(**kwargs):
    return SdwanClient().getCircuits(**kwargs)

@register('getGlobalParameters')
def getGlobalParameters(**kwargs):
    return SdwanClient().getGlobalParameters(**kwargs)

@register('getGlobalTemplate')
def getGlobalTemplate(**kwargs):
    return SdwanClient().getGlobalTemplate(**kwargs)

@register('runMyTest')
def runMyTest(**kwargs):
    return SdwanClient().runMyTest(**kwargs)

@register('getDeviceProfileFeatureTemplateList')
def getDeviceProfileFeatureTemplateList(**kwargs):
    return SdwanClient().getDeviceProfileFeatureTemplateList(**kwargs)

@register('getDeviceProfileConfigStatus')
def getDeviceProfileConfigStatus(**kwargs):
    return SdwanClient().getDeviceProfileConfigStatus(**kwargs)

@register('getDeviceProfileConfigStatusByProfileId')
def getDeviceProfileConfigStatusByProfileId(**kwargs):
    return SdwanClient().getDeviceProfileConfigStatusByProfileId(**kwargs)

@register('getDeviceProfileTaskCount')
def getDeviceProfileTaskCount(**kwargs):
    return SdwanClient().getDeviceProfileTaskCount(**kwargs)

@register('getDeviceProfileTaskStatus')
def getDeviceProfileTaskStatus(**kwargs):
    return SdwanClient().getDeviceProfileTaskStatus(**kwargs)

@register('getDeviceProfileTaskStatusByProfileId')
def getDeviceProfileTaskStatusByProfileId(**kwargs):
    return SdwanClient().getDeviceProfileTaskStatusByProfileId(**kwargs)

@register('generateProfileTemplateList')
def generateProfileTemplateList(**kwargs):
    return SdwanClient().generateProfileTemplateList(**kwargs)

@register('getDeviceProfileTemplate')
def getDeviceProfileTemplate(**kwargs):
    return SdwanClient().getDeviceProfileTemplate(**kwargs)

@register('getServiceProfileConfig')
def getServiceProfileConfig(**kwargs):
    return SdwanClient().getServiceProfileConfig(**kwargs)

@register('getNotificationRule')
def getNotificationRule(**kwargs):
    return SdwanClient().getNotificationRule(**kwargs)

@register('getDevices')
def getDevices(**kwargs):
    return SdwanClient().getDevices(**kwargs)

@register('oauthAccess')
def oauthAccess(**kwargs):
    return SdwanClient().oauthAccess(**kwargs)

@register('getClientID')
def getClientID(**kwargs):
    return SdwanClient().getClientID(**kwargs)

@register('getCall')
def getCall(**kwargs):
    return SdwanClient().getCall(**kwargs)

@register('getPartners')
def getPartners(**kwargs):
    return SdwanClient().getPartners(**kwargs)

@register('getACIDefinitions')
def getACIDefinitions(**kwargs):
    return SdwanClient().getACIDefinitions(**kwargs)

@register('getDscpMappings')
def getDscpMappings(**kwargs):
    return SdwanClient().getDscpMappings(**kwargs)

@register('getEvents_1')
def getEvents_1(**kwargs):
    return SdwanClient().getEvents_1(**kwargs)

@register('getDataPrefixMappings')
def getDataPrefixMappings(**kwargs):
    return SdwanClient().getDataPrefixMappings(**kwargs)

@register('getDataPrefixSequences')
def getDataPrefixSequences(**kwargs):
    return SdwanClient().getDataPrefixSequences(**kwargs)

@register('getSDAEnabledDevices')
def getSDAEnabledDevices(**kwargs):
    return SdwanClient().getSDAEnabledDevices(**kwargs)

@register('getDeviceDetails')
def getDeviceDetails(**kwargs):
    return SdwanClient().getDeviceDetails(**kwargs)

@register('getSitesForPartner')
def getSitesForPartner(**kwargs):
    return SdwanClient().getSitesForPartner(**kwargs)

@register('getOverlayVPNList')
def getOverlayVPNList(**kwargs):
    return SdwanClient().getOverlayVPNList(**kwargs)

@register('getVPNList')
def getVPNList(**kwargs):
    return SdwanClient().getVPNList(**kwargs)

@register('getPartnersByPartnerType')
def getPartnersByPartnerType(**kwargs):
    return SdwanClient().getPartnersByPartnerType(**kwargs)

@register('getPartnerDevices')
def getPartnerDevices(**kwargs):
    return SdwanClient().getPartnerDevices(**kwargs)

@register('getPartner')
def getPartner(**kwargs):
    return SdwanClient().getPartner(**kwargs)

@register('getSecureXRefreshToken')
def getSecureXRefreshToken(**kwargs):
    return SdwanClient().getSecureXRefreshToken(**kwargs)

@register('getResources')
def getResources(**kwargs):
    return SdwanClient().getResources(**kwargs)

@register('listSchedules')
def listSchedules(**kwargs):
    return SdwanClient().listSchedules(**kwargs)

@register('getScheduleRecordForBackup')
def getScheduleRecordForBackup(**kwargs):
    return SdwanClient().getScheduleRecordForBackup(**kwargs)

@register('getExtendedApplications')
def getExtendedApplications(**kwargs):
    return SdwanClient().getExtendedApplications(**kwargs)

@register('getCloudConnector')
def getCloudConnector(**kwargs):
    return SdwanClient().getCloudConnector(**kwargs)

@register('getCloudConnectorStatus')
def getCloudConnectorStatus(**kwargs):
    return SdwanClient().getCloudConnectorStatus(**kwargs)

@register('getCustomApp')
def getCustomApp(**kwargs):
    return SdwanClient().getCustomApp(**kwargs)

@register('getAllProtocolPacks')
def getAllProtocolPacks(**kwargs):
    return SdwanClient().getAllProtocolPacks(**kwargs)

@register('getBaseSystemPack')
def getBaseSystemPack(**kwargs):
    return SdwanClient().getBaseSystemPack(**kwargs)

@register('getAllSDAVCDevice')
def getAllSDAVCDevice(**kwargs):
    return SdwanClient().getAllSDAVCDevice(**kwargs)

@register('getDefaultApplicationComplianceDetails')
def getDefaultApplicationComplianceDetails(**kwargs):
    return SdwanClient().getDefaultApplicationComplianceDetails(**kwargs)

@register('isApplicationComplianceDetected')
def isApplicationComplianceDetected(**kwargs):
    return SdwanClient().isApplicationComplianceDetected(**kwargs)

@register('getApplicationComplianceStatus')
def getApplicationComplianceStatus(**kwargs):
    return SdwanClient().getApplicationComplianceStatus(**kwargs)

@register('getApplicationComplianceDetails')
def getApplicationComplianceDetails(**kwargs):
    return SdwanClient().getApplicationComplianceDetails(**kwargs)

@register('getCustomApplicationList')
def getCustomApplicationList(**kwargs):
    return SdwanClient().getCustomApplicationList(**kwargs)

@register('getNonCompliantDevicesForProtocolPack')
def getNonCompliantDevicesForProtocolPack(**kwargs):
    return SdwanClient().getNonCompliantDevicesForProtocolPack(**kwargs)

@register('getDeviceComplianceStatus')
def getDeviceComplianceStatus(**kwargs):
    return SdwanClient().getDeviceComplianceStatus(**kwargs)

@register('getNewApplicationList')
def getNewApplicationList(**kwargs):
    return SdwanClient().getNewApplicationList(**kwargs)

@register('getCompliancePolicy')
def getCompliancePolicy(**kwargs):
    return SdwanClient().getCompliancePolicy(**kwargs)

@register('getPolicyComplianceStatus')
def getPolicyComplianceStatus(**kwargs):
    return SdwanClient().getPolicyComplianceStatus(**kwargs)

@register('getDefaultSystemPack')
def getDefaultSystemPack(**kwargs):
    return SdwanClient().getDefaultSystemPack(**kwargs)

@register('getLatestSystemPack')
def getLatestSystemPack(**kwargs):
    return SdwanClient().getLatestSystemPack(**kwargs)

@register('getDeployJobStatus')
def getDeployJobStatus(**kwargs):
    return SdwanClient().getDeployJobStatus(**kwargs)

@register('getDeployJobStatus_1')
def getDeployJobStatus_1(**kwargs):
    return SdwanClient().getDeployJobStatus_1(**kwargs)

@register('getProtocolPackUploadStatus')
def getProtocolPackUploadStatus(**kwargs):
    return SdwanClient().getProtocolPackUploadStatus(**kwargs)

@register('getSecurityDeviceHealth')
def getSecurityDeviceHealth(**kwargs):
    return SdwanClient().getSecurityDeviceHealth(**kwargs)

@register('getSecurityPolicyDeviceList')
def getSecurityPolicyDeviceList(**kwargs):
    return SdwanClient().getSecurityPolicyDeviceList(**kwargs)

@register('getSegments')
def getSegments(**kwargs):
    return SdwanClient().getSegments(**kwargs)

@register('getSegment')
def getSegment(**kwargs):
    return SdwanClient().getSegment(**kwargs)

@register('createServerInfo_1')
def createServerInfo_1(**kwargs):
    return SdwanClient().createServerInfo_1(**kwargs)

@register('getDataChangeInfo')
def getDataChangeInfo(**kwargs):
    return SdwanClient().getDataChangeInfo(**kwargs)

@register('showInfo')
def showInfo(**kwargs):
    return SdwanClient().showInfo(**kwargs)

@register('getCertificate')
def getCertificate(**kwargs):
    return SdwanClient().getCertificate(**kwargs)

@register('getBanner')
def getBanner(**kwargs):
    return SdwanClient().getBanner(**kwargs)

@register('getSessionTimout')
def getSessionTimout(**kwargs):
    return SdwanClient().getSessionTimout(**kwargs)

@register('getCertConfiguration')
def getCertConfiguration(**kwargs):
    return SdwanClient().getCertConfiguration(**kwargs)

@register('getCloudxConfiguration')
def getCloudxConfiguration(**kwargs):
    return SdwanClient().getCloudxConfiguration(**kwargs)

@register('getGoogleMapKey')
def getGoogleMapKey(**kwargs):
    return SdwanClient().getGoogleMapKey(**kwargs)

@register('getMaintenanceWindow')
def getMaintenanceWindow(**kwargs):
    return SdwanClient().getMaintenanceWindow(**kwargs)

@register('getMicrosoftTelemetryConfiguration')
def getMicrosoftTelemetryConfiguration(**kwargs):
    return SdwanClient().getMicrosoftTelemetryConfiguration(**kwargs)

@register('getWaniConfiguration')
def getWaniConfiguration(**kwargs):
    return SdwanClient().getWaniConfiguration(**kwargs)

@register('getConfigurationBySettingType')
def getConfigurationBySettingType(**kwargs):
    return SdwanClient().getConfigurationBySettingType(**kwargs)

@register('getPasswordPolicy')
def getPasswordPolicy(**kwargs):
    return SdwanClient().getPasswordPolicy(**kwargs)

@register('getSigDynamicDataCenterList')
def getSigDynamicDataCenterList(**kwargs):
    return SdwanClient().getSigDynamicDataCenterList(**kwargs)

@register('getSigDataCenterList')
def getSigDataCenterList(**kwargs):
    return SdwanClient().getSigDataCenterList(**kwargs)

@register('getSigGlobalCredentials')
def getSigGlobalCredentials(**kwargs):
    return SdwanClient().getSigGlobalCredentials(**kwargs)

@register('getChildOrgs')
def getChildOrgs(**kwargs):
    return SdwanClient().getChildOrgs(**kwargs)

@register('fetchAccounts')
def fetchAccounts(**kwargs):
    return SdwanClient().fetchAccounts(**kwargs)

@register('fetchReports_1')
def fetchReports_1(**kwargs):
    return SdwanClient().fetchReports_1(**kwargs)

@register('fetchReports')
def fetchReports(**kwargs):
    return SdwanClient().fetchReports(**kwargs)

@register('getSettings')
def getSettings(**kwargs):
    return SdwanClient().getSettings(**kwargs)

@register('getProxyCertOfEdge')
def getProxyCertOfEdge(**kwargs):
    return SdwanClient().getProxyCertOfEdge(**kwargs)

@register('getSslProxyCSR')
def getSslProxyCSR(**kwargs):
    return SdwanClient().getSslProxyCSR(**kwargs)

@register('getSslProxyList')
def getSslProxyList(**kwargs):
    return SdwanClient().getSslProxyList(**kwargs)

@register('getCertificateState')
def getCertificateState(**kwargs):
    return SdwanClient().getCertificateState(**kwargs)

@register('getEnterpriseCertificate')
def getEnterpriseCertificate(**kwargs):
    return SdwanClient().getEnterpriseCertificate(**kwargs)

@register('getVManageEnterpriseRootCertificate')
def getVManageEnterpriseRootCertificate(**kwargs):
    return SdwanClient().getVManageEnterpriseRootCertificate(**kwargs)

@register('getvManageCertificate')
def getvManageCertificate(**kwargs):
    return SdwanClient().getvManageCertificate(**kwargs)

@register('getvManageCSR')
def getvManageCSR(**kwargs):
    return SdwanClient().getvManageCSR(**kwargs)

@register('getvManageRootCA')
def getvManageRootCA(**kwargs):
    return SdwanClient().getvManageRootCA(**kwargs)

@register('getStatisticType')
def getStatisticType(**kwargs):
    return SdwanClient().getStatisticType(**kwargs)

@register('getAggregationDataByQuery_14')
def getAggregationDataByQuery_14(**kwargs):
    return SdwanClient().getAggregationDataByQuery_14(**kwargs)

@register('getStatDataRawData_1')
def getStatDataRawData_1(**kwargs):
    return SdwanClient().getStatDataRawData_1(**kwargs)

@register('getAggregationDataByQuery_1')
def getAggregationDataByQuery_1(**kwargs):
    return SdwanClient().getAggregationDataByQuery_1(**kwargs)

@register('getStatDataRawDataAsCSV_1')
def getStatDataRawDataAsCSV_1(**kwargs):
    return SdwanClient().getStatDataRawDataAsCSV_1(**kwargs)

@register('getCount_2')
def getCount_2(**kwargs):
    return SdwanClient().getCount_2(**kwargs)

@register('getStatDataFields_2')
def getStatDataFields_2(**kwargs):
    return SdwanClient().getStatDataFields_2(**kwargs)

@register('getStatsPaginationRawData_1')
def getStatsPaginationRawData_1(**kwargs):
    return SdwanClient().getStatsPaginationRawData_1(**kwargs)

@register('getStatQueryFields_2')
def getStatQueryFields_2(**kwargs):
    return SdwanClient().getStatQueryFields_2(**kwargs)

@register('getStatDataRawData')
def getStatDataRawData(**kwargs):
    return SdwanClient().getStatDataRawData(**kwargs)

@register('getAggregationDataByQuery')
def getAggregationDataByQuery(**kwargs):
    return SdwanClient().getAggregationDataByQuery(**kwargs)

@register('getStatDataRawDataAsCSV')
def getStatDataRawDataAsCSV(**kwargs):
    return SdwanClient().getStatDataRawDataAsCSV(**kwargs)

@register('getCount_1')
def getCount_1(**kwargs):
    return SdwanClient().getCount_1(**kwargs)

@register('getStatDataFields_1')
def getStatDataFields_1(**kwargs):
    return SdwanClient().getStatDataFields_1(**kwargs)

@register('getStatsPaginationRawData')
def getStatsPaginationRawData(**kwargs):
    return SdwanClient().getStatsPaginationRawData(**kwargs)

@register('getStatQueryFields_1')
def getStatQueryFields_1(**kwargs):
    return SdwanClient().getStatQueryFields_1(**kwargs)

@register('getStatDataRawData_2')
def getStatDataRawData_2(**kwargs):
    return SdwanClient().getStatDataRawData_2(**kwargs)

@register('getAggregationDataByQuery_2')
def getAggregationDataByQuery_2(**kwargs):
    return SdwanClient().getAggregationDataByQuery_2(**kwargs)

@register('getStatDataRawDataAsCSV_2')
def getStatDataRawDataAsCSV_2(**kwargs):
    return SdwanClient().getStatDataRawDataAsCSV_2(**kwargs)

@register('getStatsAppRouteDeviceTunnelSummary')
def getStatsAppRouteDeviceTunnelSummary(**kwargs):
    return SdwanClient().getStatsAppRouteDeviceTunnelSummary(**kwargs)

@register('getStatsAppRouteDeviceTunnels')
def getStatsAppRouteDeviceTunnels(**kwargs):
    return SdwanClient().getStatsAppRouteDeviceTunnels(**kwargs)

@register('getDocCount_1')
def getDocCount_1(**kwargs):
    return SdwanClient().getDocCount_1(**kwargs)

@register('getStatDataFields_3')
def getStatDataFields_3(**kwargs):
    return SdwanClient().getStatDataFields_3(**kwargs)

@register('getStatBulkRawData')
def getStatBulkRawData(**kwargs):
    return SdwanClient().getStatBulkRawData(**kwargs)

@register('getStatQueryFields_3')
def getStatQueryFields_3(**kwargs):
    return SdwanClient().getStatQueryFields_3(**kwargs)

@register('getAppRouteTransportSummaryType')
def getAppRouteTransportSummaryType(**kwargs):
    return SdwanClient().getAppRouteTransportSummaryType(**kwargs)

@register('getAppRouteTransportType')
def getAppRouteTransportType(**kwargs):
    return SdwanClient().getAppRouteTransportType(**kwargs)

@register('getAppRouteTunnelSummaryType')
def getAppRouteTunnelSummaryType(**kwargs):
    return SdwanClient().getAppRouteTunnelSummaryType(**kwargs)

@register('getAppRouteTunnelHealth')
def getAppRouteTunnelHealth(**kwargs):
    return SdwanClient().getAppRouteTunnelHealth(**kwargs)

@register('getAppRouteTunnelsSummaryType')
def getAppRouteTunnelsSummaryType(**kwargs):
    return SdwanClient().getAppRouteTunnelsSummaryType(**kwargs)

@register('getAppRouteTunnelType')
def getAppRouteTunnelType(**kwargs):
    return SdwanClient().getAppRouteTunnelType(**kwargs)

@register('getStatDataRawData_4')
def getStatDataRawData_4(**kwargs):
    return SdwanClient().getStatDataRawData_4(**kwargs)

@register('getAggregationDataByQuery_4')
def getAggregationDataByQuery_4(**kwargs):
    return SdwanClient().getAggregationDataByQuery_4(**kwargs)

@register('getStatDataRawDataAsCSV_4')
def getStatDataRawDataAsCSV_4(**kwargs):
    return SdwanClient().getStatDataRawDataAsCSV_4(**kwargs)

@register('getCount_4')
def getCount_4(**kwargs):
    return SdwanClient().getCount_4(**kwargs)

@register('getStatDataFields_5')
def getStatDataFields_5(**kwargs):
    return SdwanClient().getStatDataFields_5(**kwargs)

@register('getStatsPaginationRawData_3')
def getStatsPaginationRawData_3(**kwargs):
    return SdwanClient().getStatsPaginationRawData_3(**kwargs)

@register('getStatQueryFields_5')
def getStatQueryFields_5(**kwargs):
    return SdwanClient().getStatQueryFields_5(**kwargs)

@register('getStatDataRawData_5')
def getStatDataRawData_5(**kwargs):
    return SdwanClient().getStatDataRawData_5(**kwargs)

@register('getAggregationDataByQuery_5')
def getAggregationDataByQuery_5(**kwargs):
    return SdwanClient().getAggregationDataByQuery_5(**kwargs)

@register('getStatDataRawDataAsCSV_5')
def getStatDataRawDataAsCSV_5(**kwargs):
    return SdwanClient().getStatDataRawDataAsCSV_5(**kwargs)

@register('getCount_5')
def getCount_5(**kwargs):
    return SdwanClient().getCount_5(**kwargs)

@register('getStatDataFields_6')
def getStatDataFields_6(**kwargs):
    return SdwanClient().getStatDataFields_6(**kwargs)

@register('getStatsPaginationRawData_4')
def getStatsPaginationRawData_4(**kwargs):
    return SdwanClient().getStatsPaginationRawData_4(**kwargs)

@register('getStatQueryFields_6')
def getStatQueryFields_6(**kwargs):
    return SdwanClient().getStatQueryFields_6(**kwargs)

@register('getStatDataRawData_6')
def getStatDataRawData_6(**kwargs):
    return SdwanClient().getStatDataRawData_6(**kwargs)

@register('getAggregationDataByQuery_6')
def getAggregationDataByQuery_6(**kwargs):
    return SdwanClient().getAggregationDataByQuery_6(**kwargs)

@register('getStatDataRawDataAsCSV_6')
def getStatDataRawDataAsCSV_6(**kwargs):
    return SdwanClient().getStatDataRawDataAsCSV_6(**kwargs)

@register('getCount_6')
def getCount_6(**kwargs):
    return SdwanClient().getCount_6(**kwargs)

@register('getStatDataFields_7')
def getStatDataFields_7(**kwargs):
    return SdwanClient().getStatDataFields_7(**kwargs)

@register('getStatsPaginationRawData_5')
def getStatsPaginationRawData_5(**kwargs):
    return SdwanClient().getStatsPaginationRawData_5(**kwargs)

@register('getStatQueryFields_7')
def getStatQueryFields_7(**kwargs):
    return SdwanClient().getStatQueryFields_7(**kwargs)

@register('getStatDataRawData_7')
def getStatDataRawData_7(**kwargs):
    return SdwanClient().getStatDataRawData_7(**kwargs)

@register('getAggregationDataByQuery_7')
def getAggregationDataByQuery_7(**kwargs):
    return SdwanClient().getAggregationDataByQuery_7(**kwargs)

@register('getStatDataRawDataAsCSV_7')
def getStatDataRawDataAsCSV_7(**kwargs):
    return SdwanClient().getStatDataRawDataAsCSV_7(**kwargs)

@register('getCount_7')
def getCount_7(**kwargs):
    return SdwanClient().getCount_7(**kwargs)

@register('getStatDataFields_8')
def getStatDataFields_8(**kwargs):
    return SdwanClient().getStatDataFields_8(**kwargs)

@register('getStatsPaginationRawData_6')
def getStatsPaginationRawData_6(**kwargs):
    return SdwanClient().getStatsPaginationRawData_6(**kwargs)

@register('getStatQueryFields_8')
def getStatQueryFields_8(**kwargs):
    return SdwanClient().getStatQueryFields_8(**kwargs)

@register('getStatDataRawData_9')
def getStatDataRawData_9(**kwargs):
    return SdwanClient().getStatDataRawData_9(**kwargs)

@register('getAggregationDataByQuery_9')
def getAggregationDataByQuery_9(**kwargs):
    return SdwanClient().getAggregationDataByQuery_9(**kwargs)

@register('createFlowsGrid')
def createFlowsGrid(**kwargs):
    return SdwanClient().createFlowsGrid(**kwargs)

@register('createFlowssummary')
def createFlowssummary(**kwargs):
    return SdwanClient().createFlowssummary(**kwargs)

@register('getStatDataRawDataAsCSV_9')
def getStatDataRawDataAsCSV_9(**kwargs):
    return SdwanClient().getStatDataRawDataAsCSV_9(**kwargs)

@register('createFlowDeviceData')
def createFlowDeviceData(**kwargs):
    return SdwanClient().createFlowDeviceData(**kwargs)

@register('getCount_9')
def getCount_9(**kwargs):
    return SdwanClient().getCount_9(**kwargs)

@register('getStatDataFields_10')
def getStatDataFields_10(**kwargs):
    return SdwanClient().getStatDataFields_10(**kwargs)

@register('getStatsPaginationRawData_8')
def getStatsPaginationRawData_8(**kwargs):
    return SdwanClient().getStatsPaginationRawData_8(**kwargs)

@register('getStatQueryFields_10')
def getStatQueryFields_10(**kwargs):
    return SdwanClient().getStatQueryFields_10(**kwargs)

@register('getStatDataRawData_10')
def getStatDataRawData_10(**kwargs):
    return SdwanClient().getStatDataRawData_10(**kwargs)

@register('getAggregationDataByQuery_10')
def getAggregationDataByQuery_10(**kwargs):
    return SdwanClient().getAggregationDataByQuery_10(**kwargs)

@register('getStatDataRawDataAsCSV_10')
def getStatDataRawDataAsCSV_10(**kwargs):
    return SdwanClient().getStatDataRawDataAsCSV_10(**kwargs)

@register('getCount_10')
def getCount_10(**kwargs):
    return SdwanClient().getCount_10(**kwargs)

@register('getStatDataFields_11')
def getStatDataFields_11(**kwargs):
    return SdwanClient().getStatDataFields_11(**kwargs)

@register('getStatsPaginationRawData_9')
def getStatsPaginationRawData_9(**kwargs):
    return SdwanClient().getStatsPaginationRawData_9(**kwargs)

@register('getStatQueryFields_11')
def getStatQueryFields_11(**kwargs):
    return SdwanClient().getStatQueryFields_11(**kwargs)

@register('startStatsCollection')
def startStatsCollection(**kwargs):
    return SdwanClient().startStatsCollection(**kwargs)

@register('generateStatsCollectThreadReport')
def generateStatsCollectThreadReport(**kwargs):
    return SdwanClient().generateStatsCollectThreadReport(**kwargs)

@register('resetStatsCollection')
def resetStatsCollection(**kwargs):
    return SdwanClient().resetStatsCollection(**kwargs)

@register('getStatDataRawDataAsCSV_13')
def getStatDataRawDataAsCSV_13(**kwargs):
    return SdwanClient().getStatDataRawDataAsCSV_13(**kwargs)

@register('enableStatisticsDemoMode')
def enableStatisticsDemoMode(**kwargs):
    return SdwanClient().enableStatisticsDemoMode(**kwargs)

@register('getStatDataRawData_16')
def getStatDataRawData_16(**kwargs):
    return SdwanClient().getStatDataRawData_16(**kwargs)

@register('getAggregationDataByQuery_18')
def getAggregationDataByQuery_18(**kwargs):
    return SdwanClient().getAggregationDataByQuery_18(**kwargs)

@register('getStatDataRawDataAsCSV_16')
def getStatDataRawDataAsCSV_16(**kwargs):
    return SdwanClient().getStatDataRawDataAsCSV_16(**kwargs)

@register('getCount_15')
def getCount_15(**kwargs):
    return SdwanClient().getCount_15(**kwargs)

@register('getStatDataFields_17')
def getStatDataFields_17(**kwargs):
    return SdwanClient().getStatDataFields_17(**kwargs)

@register('getStatsPaginationRawData_14')
def getStatsPaginationRawData_14(**kwargs):
    return SdwanClient().getStatsPaginationRawData_14(**kwargs)

@register('getStatQueryFields_18')
def getStatQueryFields_18(**kwargs):
    return SdwanClient().getStatQueryFields_18(**kwargs)

@register('getDeviceHealthHistory')
def getDeviceHealthHistory(**kwargs):
    return SdwanClient().getDeviceHealthHistory(**kwargs)

@register('getDeviceHealthOverview')
def getDeviceHealthOverview(**kwargs):
    return SdwanClient().getDeviceHealthOverview(**kwargs)

@register('getCount_12')
def getCount_12(**kwargs):
    return SdwanClient().getCount_12(**kwargs)

@register('fetchList')
def fetchList(**kwargs):
    return SdwanClient().fetchList(**kwargs)

@register('download')
def download(**kwargs):
    return SdwanClient().download(**kwargs)

@register('getDPIStatsRawData')
def getDPIStatsRawData(**kwargs):
    return SdwanClient().getDPIStatsRawData(**kwargs)

@register('getDPIStatsAggregationData')
def getDPIStatsAggregationData(**kwargs):
    return SdwanClient().getDPIStatsAggregationData(**kwargs)

@register('getAggAppFlows')
def getAggAppFlows(**kwargs):
    return SdwanClient().getAggAppFlows(**kwargs)

@register('getAggAppFlowsSummary')
def getAggAppFlowsSummary(**kwargs):
    return SdwanClient().getAggAppFlowsSummary(**kwargs)

@register('getDPIStatsRawDataAsCSV')
def getDPIStatsRawDataAsCSV(**kwargs):
    return SdwanClient().getDPIStatsRawDataAsCSV(**kwargs)

@register('getDPIDeviceAppUniqueFlowCount')
def getDPIDeviceAppUniqueFlowCount(**kwargs):
    return SdwanClient().getDPIDeviceAppUniqueFlowCount(**kwargs)

@register('getDPIDeviceAppAggregationData')
def getDPIDeviceAppAggregationData(**kwargs):
    return SdwanClient().getDPIDeviceAppAggregationData(**kwargs)

@register('getDPIDeviceAppDetails')
def getDPIDeviceAppDetails(**kwargs):
    return SdwanClient().getDPIDeviceAppDetails(**kwargs)

@register('getDPIStatsCount')
def getDPIStatsCount(**kwargs):
    return SdwanClient().getDPIStatsCount(**kwargs)

@register('getDPIFields')
def getDPIFields(**kwargs):
    return SdwanClient().getDPIFields(**kwargs)

@register('getDPIStatsPaginationRawData')
def getDPIStatsPaginationRawData(**kwargs):
    return SdwanClient().getDPIStatsPaginationRawData(**kwargs)

@register('getDPIQueryFields')
def getDPIQueryFields(**kwargs):
    return SdwanClient().getDPIQueryFields(**kwargs)

@register('getStatDataRawData_8')
def getStatDataRawData_8(**kwargs):
    return SdwanClient().getStatDataRawData_8(**kwargs)

@register('getAggregationDataByQuery_8')
def getAggregationDataByQuery_8(**kwargs):
    return SdwanClient().getAggregationDataByQuery_8(**kwargs)

@register('getStatDataRawDataAsCSV_8')
def getStatDataRawDataAsCSV_8(**kwargs):
    return SdwanClient().getStatDataRawDataAsCSV_8(**kwargs)

@register('getCount_8')
def getCount_8(**kwargs):
    return SdwanClient().getCount_8(**kwargs)

@register('getStatDataFields_9')
def getStatDataFields_9(**kwargs):
    return SdwanClient().getStatDataFields_9(**kwargs)

@register('getStatsPaginationRawData_7')
def getStatsPaginationRawData_7(**kwargs):
    return SdwanClient().getStatsPaginationRawData_7(**kwargs)

@register('getStatQueryFields_9')
def getStatQueryFields_9(**kwargs):
    return SdwanClient().getStatQueryFields_9(**kwargs)

@register('getStatDataRawData_19')
def getStatDataRawData_19(**kwargs):
    return SdwanClient().getStatDataRawData_19(**kwargs)

@register('getAggregationDataByQuery_21')
def getAggregationDataByQuery_21(**kwargs):
    return SdwanClient().getAggregationDataByQuery_21(**kwargs)

@register('getStatDataRawDataAsCSV_19')
def getStatDataRawDataAsCSV_19(**kwargs):
    return SdwanClient().getStatDataRawDataAsCSV_19(**kwargs)

@register('getCount_18')
def getCount_18(**kwargs):
    return SdwanClient().getCount_18(**kwargs)

@register('getStatDataFields_20')
def getStatDataFields_20(**kwargs):
    return SdwanClient().getStatDataFields_20(**kwargs)

@register('getStatsPaginationRawData_17')
def getStatsPaginationRawData_17(**kwargs):
    return SdwanClient().getStatsPaginationRawData_17(**kwargs)

@register('getStatQueryFields_21')
def getStatQueryFields_21(**kwargs):
    return SdwanClient().getStatQueryFields_21(**kwargs)

@register('getStatDataFields_14')
def getStatDataFields_14(**kwargs):
    return SdwanClient().getStatDataFields_14(**kwargs)

@register('getStatDataRawData_14')
def getStatDataRawData_14(**kwargs):
    return SdwanClient().getStatDataRawData_14(**kwargs)

@register('getAggregationDataByQuery_28')
def getAggregationDataByQuery_28(**kwargs):
    return SdwanClient().getAggregationDataByQuery_28(**kwargs)

@register('getStatDataRawDataAsCSV_26')
def getStatDataRawDataAsCSV_26(**kwargs):
    return SdwanClient().getStatDataRawDataAsCSV_26(**kwargs)

@register('getFlowlogCount')
def getFlowlogCount(**kwargs):
    return SdwanClient().getFlowlogCount(**kwargs)

@register('getFlowlogFields')
def getFlowlogFields(**kwargs):
    return SdwanClient().getFlowlogFields(**kwargs)

@register('getStatsPaginationRawData_24')
def getStatsPaginationRawData_24(**kwargs):
    return SdwanClient().getStatsPaginationRawData_24(**kwargs)

@register('getFlowlogQueryFields')
def getFlowlogQueryFields(**kwargs):
    return SdwanClient().getFlowlogQueryFields(**kwargs)

@register('getStatDataRawData_24')
def getStatDataRawData_24(**kwargs):
    return SdwanClient().getStatDataRawData_24(**kwargs)

@register('getAggregationDataByQuery_26')
def getAggregationDataByQuery_26(**kwargs):
    return SdwanClient().getAggregationDataByQuery_26(**kwargs)

@register('getStatDataRawDataAsCSV_24')
def getStatDataRawDataAsCSV_24(**kwargs):
    return SdwanClient().getStatDataRawDataAsCSV_24(**kwargs)

@register('getCount_23')
def getCount_23(**kwargs):
    return SdwanClient().getCount_23(**kwargs)

@register('getStatDataFields_25')
def getStatDataFields_25(**kwargs):
    return SdwanClient().getStatDataFields_25(**kwargs)

@register('getStatsPaginationRawData_22')
def getStatsPaginationRawData_22(**kwargs):
    return SdwanClient().getStatsPaginationRawData_22(**kwargs)

@register('getStatQueryFields_26')
def getStatQueryFields_26(**kwargs):
    return SdwanClient().getStatQueryFields_26(**kwargs)

@register('getStatDataRawData_11')
def getStatDataRawData_11(**kwargs):
    return SdwanClient().getStatDataRawData_11(**kwargs)

@register('getAggregationDataByQuery_11')
def getAggregationDataByQuery_11(**kwargs):
    return SdwanClient().getAggregationDataByQuery_11(**kwargs)

@register('getBandwidthDistribution')
def getBandwidthDistribution(**kwargs):
    return SdwanClient().getBandwidthDistribution(**kwargs)

@register('getStatDataRawDataAsCSV_11')
def getStatDataRawDataAsCSV_11(**kwargs):
    return SdwanClient().getStatDataRawDataAsCSV_11(**kwargs)

@register('getCount10')
def getCount10(**kwargs):
    return SdwanClient().getCount10(**kwargs)

@register('getStatDataFields_12')
def getStatDataFields_12(**kwargs):
    return SdwanClient().getStatDataFields_12(**kwargs)

@register('getStatBulkRawData_1')
def getStatBulkRawData_1(**kwargs):
    return SdwanClient().getStatBulkRawData_1(**kwargs)

@register('getStatQueryFields_12')
def getStatQueryFields_12(**kwargs):
    return SdwanClient().getStatQueryFields_12(**kwargs)

@register('getStatisticsPerInterface')
def getStatisticsPerInterface(**kwargs):
    return SdwanClient().getStatisticsPerInterface(**kwargs)

@register('getStatDataRawData_22')
def getStatDataRawData_22(**kwargs):
    return SdwanClient().getStatDataRawData_22(**kwargs)

@register('getAggregationDataByQuery_24')
def getAggregationDataByQuery_24(**kwargs):
    return SdwanClient().getAggregationDataByQuery_24(**kwargs)

@register('getStatDataRawDataAsCSV_22')
def getStatDataRawDataAsCSV_22(**kwargs):
    return SdwanClient().getStatDataRawDataAsCSV_22(**kwargs)

@register('getCount_21')
def getCount_21(**kwargs):
    return SdwanClient().getCount_21(**kwargs)

@register('getStatDataFields_23')
def getStatDataFields_23(**kwargs):
    return SdwanClient().getStatDataFields_23(**kwargs)

@register('getStatsPaginationRawData_20')
def getStatsPaginationRawData_20(**kwargs):
    return SdwanClient().getStatsPaginationRawData_20(**kwargs)

@register('getStatQueryFields_24')
def getStatQueryFields_24(**kwargs):
    return SdwanClient().getStatQueryFields_24(**kwargs)

@register('getQueueEntries')
def getQueueEntries(**kwargs):
    return SdwanClient().getQueueEntries(**kwargs)

@register('getQueueProperties')
def getQueueProperties(**kwargs):
    return SdwanClient().getQueueProperties(**kwargs)

@register('getStatsPaginationRawData_11')
def getStatsPaginationRawData_11(**kwargs):
    return SdwanClient().getStatsPaginationRawData_11(**kwargs)

@register('getApplicationHeatMapDetail')
def getApplicationHeatMapDetail(**kwargs):
    return SdwanClient().getApplicationHeatMapDetail(**kwargs)

@register('getApplicationSitesHealth')
def getApplicationSitesHealth(**kwargs):
    return SdwanClient().getApplicationSitesHealth(**kwargs)

@register('getApplicationsSiteHealth')
def getApplicationsSiteHealth(**kwargs):
    return SdwanClient().getApplicationsSiteHealth(**kwargs)

@register('getApplicationsSitesHealth')
def getApplicationsSitesHealth(**kwargs):
    return SdwanClient().getApplicationsSitesHealth(**kwargs)

@register('getSupportedDeviceList')
def getSupportedDeviceList(**kwargs):
    return SdwanClient().getSupportedDeviceList(**kwargs)

@register('processStatisticsData')
def processStatisticsData(**kwargs):
    return SdwanClient().processStatisticsData(**kwargs)

@register('getStatisticsProcessingCounters')
def getStatisticsProcessingCounters(**kwargs):
    return SdwanClient().getStatisticsProcessingCounters(**kwargs)

@register('generateStatsProcessReport')
def generateStatsProcessReport(**kwargs):
    return SdwanClient().generateStatsProcessReport(**kwargs)

@register('generateStatsProcessThreadReport')
def generateStatsProcessThreadReport(**kwargs):
    return SdwanClient().generateStatsProcessThreadReport(**kwargs)

@register('getStatDataRawData_3')
def getStatDataRawData_3(**kwargs):
    return SdwanClient().getStatDataRawData_3(**kwargs)

@register('getAggregationDataByQuery_15')
def getAggregationDataByQuery_15(**kwargs):
    return SdwanClient().getAggregationDataByQuery_15(**kwargs)

@register('getStatDataRawDataAsCSV_3')
def getStatDataRawDataAsCSV_3(**kwargs):
    return SdwanClient().getStatDataRawDataAsCSV_3(**kwargs)

@register('getCount_3')
def getCount_3(**kwargs):
    return SdwanClient().getCount_3(**kwargs)

@register('getStatDataFields_4')
def getStatDataFields_4(**kwargs):
    return SdwanClient().getStatDataFields_4(**kwargs)

@register('getStatsPaginationRawData_2')
def getStatsPaginationRawData_2(**kwargs):
    return SdwanClient().getStatsPaginationRawData_2(**kwargs)

@register('getStatQueryFields_4')
def getStatQueryFields_4(**kwargs):
    return SdwanClient().getStatQueryFields_4(**kwargs)

@register('getStatDataRawData_13')
def getStatDataRawData_13(**kwargs):
    return SdwanClient().getStatDataRawData_13(**kwargs)

@register('getAggregationDataByQuery_13')
def getAggregationDataByQuery_13(**kwargs):
    return SdwanClient().getAggregationDataByQuery_13(**kwargs)

@register('getStatDataRawDataAsCSV12')
def getStatDataRawDataAsCSV12(**kwargs):
    return SdwanClient().getStatDataRawDataAsCSV12(**kwargs)

@register('getCount13')
def getCount13(**kwargs):
    return SdwanClient().getCount13(**kwargs)

@register('getStatDataFields13')
def getStatDataFields13(**kwargs):
    return SdwanClient().getStatDataFields13(**kwargs)

@register('getStatBulkRawData_2')
def getStatBulkRawData_2(**kwargs):
    return SdwanClient().getStatBulkRawData_2(**kwargs)

@register('getStatQueryFields_14')
def getStatQueryFields_14(**kwargs):
    return SdwanClient().getStatQueryFields_14(**kwargs)

@register('getStatQueryFields_15')
def getStatQueryFields_15(**kwargs):
    return SdwanClient().getStatQueryFields_15(**kwargs)

@register('getSdraHeadendSummary')
def getSdraHeadendSummary(**kwargs):
    return SdwanClient().getSdraHeadendSummary(**kwargs)

@register('getSdraSessionSummary')
def getSdraSessionSummary(**kwargs):
    return SdwanClient().getSdraSessionSummary(**kwargs)

@register('getDisabledDeviceList')
def getDisabledDeviceList(**kwargs):
    return SdwanClient().getDisabledDeviceList(**kwargs)

@register('getStatisticsSettings')
def getStatisticsSettings(**kwargs):
    return SdwanClient().getStatisticsSettings(**kwargs)

@register('getEnabledIndexForDevice')
def getEnabledIndexForDevice(**kwargs):
    return SdwanClient().getEnabledIndexForDevice(**kwargs)

@register('getStatDataRawData_15')
def getStatDataRawData_15(**kwargs):
    return SdwanClient().getStatDataRawData_15(**kwargs)

@register('getAggregationDataByQuery_16')
def getAggregationDataByQuery_16(**kwargs):
    return SdwanClient().getAggregationDataByQuery_16(**kwargs)

@register('getSiteHealth')
def getSiteHealth(**kwargs):
    return SdwanClient().getSiteHealth(**kwargs)

@register('getStatDataRawDataAsCSV_14')
def getStatDataRawDataAsCSV_14(**kwargs):
    return SdwanClient().getStatDataRawDataAsCSV_14(**kwargs)

@register('getCount_13')
def getCount_13(**kwargs):
    return SdwanClient().getCount_13(**kwargs)

@register('getStatDataFields_15')
def getStatDataFields_15(**kwargs):
    return SdwanClient().getStatDataFields_15(**kwargs)

@register('getStatsPaginationRawData_12')
def getStatsPaginationRawData_12(**kwargs):
    return SdwanClient().getStatsPaginationRawData_12(**kwargs)

@register('getStatQueryFields_16')
def getStatQueryFields_16(**kwargs):
    return SdwanClient().getStatQueryFields_16(**kwargs)

@register('getSiteHealthTopology')
def getSiteHealthTopology(**kwargs):
    return SdwanClient().getSiteHealthTopology(**kwargs)

@register('getStatDataRawData_26')
def getStatDataRawData_26(**kwargs):
    return SdwanClient().getStatDataRawData_26(**kwargs)

@register('getAggregationDataByQuery_29')
def getAggregationDataByQuery_29(**kwargs):
    return SdwanClient().getAggregationDataByQuery_29(**kwargs)

@register('getStatDataRawDataAsCSV_27')
def getStatDataRawDataAsCSV_27(**kwargs):
    return SdwanClient().getStatDataRawDataAsCSV_27(**kwargs)

@register('getCount_25')
def getCount_25(**kwargs):
    return SdwanClient().getCount_25(**kwargs)

@register('getStatDataFields_27')
def getStatDataFields_27(**kwargs):
    return SdwanClient().getStatDataFields_27(**kwargs)

@register('getStatsPaginationRawData_25')
def getStatsPaginationRawData_25(**kwargs):
    return SdwanClient().getStatsPaginationRawData_25(**kwargs)

@register('getStatQueryFields_29')
def getStatQueryFields_29(**kwargs):
    return SdwanClient().getStatQueryFields_29(**kwargs)

@register('getSulStatDataRawData')
def getSulStatDataRawData(**kwargs):
    return SdwanClient().getSulStatDataRawData(**kwargs)

@register('getAggregationDataByQuery_17')
def getAggregationDataByQuery_17(**kwargs):
    return SdwanClient().getAggregationDataByQuery_17(**kwargs)

@register('getStatDataRawDataAsCSV_15')
def getStatDataRawDataAsCSV_15(**kwargs):
    return SdwanClient().getStatDataRawDataAsCSV_15(**kwargs)

@register('getCount_14')
def getCount_14(**kwargs):
    return SdwanClient().getCount_14(**kwargs)

@register('getStatDataFields_16')
def getStatDataFields_16(**kwargs):
    return SdwanClient().getStatDataFields_16(**kwargs)

@register('getFilterPolicyNameList')
def getFilterPolicyNameList(**kwargs):
    return SdwanClient().getFilterPolicyNameList(**kwargs)

@register('getStatsPaginationRawData_13')
def getStatsPaginationRawData_13(**kwargs):
    return SdwanClient().getStatsPaginationRawData_13(**kwargs)

@register('getStatQueryFields_17')
def getStatQueryFields_17(**kwargs):
    return SdwanClient().getStatQueryFields_17(**kwargs)

@register('getStatDataRawData_17')
def getStatDataRawData_17(**kwargs):
    return SdwanClient().getStatDataRawData_17(**kwargs)

@register('getAggregationDataByQuery_19')
def getAggregationDataByQuery_19(**kwargs):
    return SdwanClient().getAggregationDataByQuery_19(**kwargs)

@register('createDeviceSystemCPUStat')
def createDeviceSystemCPUStat(**kwargs):
    return SdwanClient().createDeviceSystemCPUStat(**kwargs)

@register('getStatDataRawDataAsCSV_17')
def getStatDataRawDataAsCSV_17(**kwargs):
    return SdwanClient().getStatDataRawDataAsCSV_17(**kwargs)

@register('getCount_16')
def getCount_16(**kwargs):
    return SdwanClient().getCount_16(**kwargs)

@register('getStatDataFields_18')
def getStatDataFields_18(**kwargs):
    return SdwanClient().getStatDataFields_18(**kwargs)

@register('createDeviceSystemMemoryStat')
def createDeviceSystemMemoryStat(**kwargs):
    return SdwanClient().createDeviceSystemMemoryStat(**kwargs)

@register('getStatsPaginationRawData_15')
def getStatsPaginationRawData_15(**kwargs):
    return SdwanClient().getStatsPaginationRawData_15(**kwargs)

@register('getStatQueryFields_19')
def getStatQueryFields_19(**kwargs):
    return SdwanClient().getStatQueryFields_19(**kwargs)

@register('getStatDataRawData_18')
def getStatDataRawData_18(**kwargs):
    return SdwanClient().getStatDataRawData_18(**kwargs)

@register('getAggregationDataByQuery_20')
def getAggregationDataByQuery_20(**kwargs):
    return SdwanClient().getAggregationDataByQuery_20(**kwargs)

@register('getStatDataRawDataAsCSV_18')
def getStatDataRawDataAsCSV_18(**kwargs):
    return SdwanClient().getStatDataRawDataAsCSV_18(**kwargs)

@register('getCount_17')
def getCount_17(**kwargs):
    return SdwanClient().getCount_17(**kwargs)

@register('getStatDataFields_19')
def getStatDataFields_19(**kwargs):
    return SdwanClient().getStatDataFields_19(**kwargs)

@register('getStatsPaginationRawData_16')
def getStatsPaginationRawData_16(**kwargs):
    return SdwanClient().getStatsPaginationRawData_16(**kwargs)

@register('getStatQueryFields_20')
def getStatQueryFields_20(**kwargs):
    return SdwanClient().getStatQueryFields_20(**kwargs)

@register('statisticsApprouteTunnelhealthHistoryGet')
def statisticsApprouteTunnelhealthHistoryGet(**kwargs):
    return SdwanClient().statisticsApprouteTunnelhealthHistoryGet(**kwargs)

@register('statisticsApprouteTunnelhealthOverviewTypeGet')
def statisticsApprouteTunnelhealthOverviewTypeGet(**kwargs):
    return SdwanClient().statisticsApprouteTunnelhealthOverviewTypeGet(**kwargs)

@register('getStatDataRawData_25')
def getStatDataRawData_25(**kwargs):
    return SdwanClient().getStatDataRawData_25(**kwargs)

@register('getAggregationDataByQuery_27')
def getAggregationDataByQuery_27(**kwargs):
    return SdwanClient().getAggregationDataByQuery_27(**kwargs)

@register('getStatDataRawDataAsCSV_25')
def getStatDataRawDataAsCSV_25(**kwargs):
    return SdwanClient().getStatDataRawDataAsCSV_25(**kwargs)

@register('getCount_24')
def getCount_24(**kwargs):
    return SdwanClient().getCount_24(**kwargs)

@register('getStatDataFields_26')
def getStatDataFields_26(**kwargs):
    return SdwanClient().getStatDataFields_26(**kwargs)

@register('getStatsPaginationRawData_23')
def getStatsPaginationRawData_23(**kwargs):
    return SdwanClient().getStatsPaginationRawData_23(**kwargs)

@register('getStatQueryFields_27')
def getStatQueryFields_27(**kwargs):
    return SdwanClient().getStatQueryFields_27(**kwargs)

@register('getStatDataRawData_23')
def getStatDataRawData_23(**kwargs):
    return SdwanClient().getStatDataRawData_23(**kwargs)

@register('getAggregationDataByQuery_25')
def getAggregationDataByQuery_25(**kwargs):
    return SdwanClient().getAggregationDataByQuery_25(**kwargs)

@register('getStatDataRawDataAsCSV_23')
def getStatDataRawDataAsCSV_23(**kwargs):
    return SdwanClient().getStatDataRawDataAsCSV_23(**kwargs)

@register('getCount_22')
def getCount_22(**kwargs):
    return SdwanClient().getCount_22(**kwargs)

@register('getStatDataFields_24')
def getStatDataFields_24(**kwargs):
    return SdwanClient().getStatDataFields_24(**kwargs)

@register('getStatsPaginationRawData_21')
def getStatsPaginationRawData_21(**kwargs):
    return SdwanClient().getStatsPaginationRawData_21(**kwargs)

@register('getStatQueryFields_25')
def getStatQueryFields_25(**kwargs):
    return SdwanClient().getStatQueryFields_25(**kwargs)

@register('getStatDataRawData_12')
def getStatDataRawData_12(**kwargs):
    return SdwanClient().getStatDataRawData_12(**kwargs)

@register('getAggregationDataByQuery_12')
def getAggregationDataByQuery_12(**kwargs):
    return SdwanClient().getAggregationDataByQuery_12(**kwargs)

@register('getStatDataRawDataAsCSV_12')
def getStatDataRawDataAsCSV_12(**kwargs):
    return SdwanClient().getStatDataRawDataAsCSV_12(**kwargs)

@register('getCount_11')
def getCount_11(**kwargs):
    return SdwanClient().getCount_11(**kwargs)

@register('getStatDataFields_13')
def getStatDataFields_13(**kwargs):
    return SdwanClient().getStatDataFields_13(**kwargs)

@register('getStatsPaginationRawData_10')
def getStatsPaginationRawData_10(**kwargs):
    return SdwanClient().getStatsPaginationRawData_10(**kwargs)

@register('getStatQueryFields_13')
def getStatQueryFields_13(**kwargs):
    return SdwanClient().getStatQueryFields_13(**kwargs)

@register('getStatDataRawData_20')
def getStatDataRawData_20(**kwargs):
    return SdwanClient().getStatDataRawData_20(**kwargs)

@register('getAggregationDataByQuery_22')
def getAggregationDataByQuery_22(**kwargs):
    return SdwanClient().getAggregationDataByQuery_22(**kwargs)

@register('getStatDataRawDataAsCSV_20')
def getStatDataRawDataAsCSV_20(**kwargs):
    return SdwanClient().getStatDataRawDataAsCSV_20(**kwargs)

@register('getCount_19')
def getCount_19(**kwargs):
    return SdwanClient().getCount_19(**kwargs)

@register('getStatDataFields_21')
def getStatDataFields_21(**kwargs):
    return SdwanClient().getStatDataFields_21(**kwargs)

@register('getStatsPaginationRawData_18')
def getStatsPaginationRawData_18(**kwargs):
    return SdwanClient().getStatsPaginationRawData_18(**kwargs)

@register('getStatQueryFields_22')
def getStatQueryFields_22(**kwargs):
    return SdwanClient().getStatQueryFields_22(**kwargs)

@register('disablePacketCaptureSession')
def disablePacketCaptureSession(**kwargs):
    return SdwanClient().disablePacketCaptureSession(**kwargs)

@register('downloadFile')
def downloadFile(**kwargs):
    return SdwanClient().downloadFile(**kwargs)

@register('forceStopPcapSession')
def forceStopPcapSession(**kwargs):
    return SdwanClient().forceStopPcapSession(**kwargs)

@register('startPcapSession')
def startPcapSession(**kwargs):
    return SdwanClient().startPcapSession(**kwargs)

@register('getFileDownloadStatus')
def getFileDownloadStatus(**kwargs):
    return SdwanClient().getFileDownloadStatus(**kwargs)

@register('stopPcapSession')
def stopPcapSession(**kwargs):
    return SdwanClient().stopPcapSession(**kwargs)

@register('getVnicInfoByVnfId')
def getVnicInfoByVnfId(**kwargs):
    return SdwanClient().getVnicInfoByVnfId(**kwargs)

@register('disableDeviceLog')
def disableDeviceLog(**kwargs):
    return SdwanClient().disableDeviceLog(**kwargs)

@register('downloadDebugLog')
def downloadDebugLog(**kwargs):
    return SdwanClient().downloadDebugLog(**kwargs)

@register('renewSessionInfo')
def renewSessionInfo(**kwargs):
    return SdwanClient().renewSessionInfo(**kwargs)

@register('getSessions')
def getSessions(**kwargs):
    return SdwanClient().getSessions(**kwargs)

@register('clearSession')
def clearSession(**kwargs):
    return SdwanClient().clearSession(**kwargs)

@register('getLogType')
def getLogType(**kwargs):
    return SdwanClient().getLogType(**kwargs)

@register('getDeviceLog')
def getDeviceLog(**kwargs):
    return SdwanClient().getDeviceLog(**kwargs)

@register('activeFlowWithQuery')
def activeFlowWithQuery(**kwargs):
    return SdwanClient().activeFlowWithQuery(**kwargs)

@register('getAggFlow')
def getAggFlow(**kwargs):
    return SdwanClient().getAggFlow(**kwargs)

@register('getAppQosData')
def getAppQosData(**kwargs):
    return SdwanClient().getAppQosData(**kwargs)

@register('getAppQosState')
def getAppQosState(**kwargs):
    return SdwanClient().getAppQosState(**kwargs)

@register('getConcurrentData')
def getConcurrentData(**kwargs):
    return SdwanClient().getConcurrentData(**kwargs)

@register('getConcurrentDomainData')
def getConcurrentDomainData(**kwargs):
    return SdwanClient().getConcurrentDomainData(**kwargs)

@register('getCurrentTimestamp')
def getCurrentTimestamp(**kwargs):
    return SdwanClient().getCurrentTimestamp(**kwargs)

@register('getDeviceBList')
def getDeviceBList(**kwargs):
    return SdwanClient().getDeviceBList(**kwargs)

@register('getDevicesAndInterfacesBySite')
def getDevicesAndInterfacesBySite(**kwargs):
    return SdwanClient().getDevicesAndInterfacesBySite(**kwargs)

@register('getDomainMetric')
def getDomainMetric(**kwargs):
    return SdwanClient().getDomainMetric(**kwargs)

@register('getEventAppHopList')
def getEventAppHopList(**kwargs):
    return SdwanClient().getEventAppHopList(**kwargs)

@register('getEventAppScoreBandwidth')
def getEventAppScoreBandwidth(**kwargs):
    return SdwanClient().getEventAppScoreBandwidth(**kwargs)

@register('getEventFlowFromAppHop')
def getEventFlowFromAppHop(**kwargs):
    return SdwanClient().getEventFlowFromAppHop(**kwargs)

@register('getEventReadout')
def getEventReadout(**kwargs):
    return SdwanClient().getEventReadout(**kwargs)

@register('getEventReadoutBySite')
def getEventReadoutBySite(**kwargs):
    return SdwanClient().getEventReadoutBySite(**kwargs)

@register('getEventReadoutByTraces')
def getEventReadoutByTraces(**kwargs):
    return SdwanClient().getEventReadoutByTraces(**kwargs)

@register('exportTrace')
def exportTrace(**kwargs):
    return SdwanClient().exportTrace(**kwargs)

@register('getFinalizedData')
def getFinalizedData(**kwargs):
    return SdwanClient().getFinalizedData(**kwargs)

@register('getFinalizedDomainData')
def getFinalizedDomainData(**kwargs):
    return SdwanClient().getFinalizedDomainData(**kwargs)

@register('getFlowDetail')
def getFlowDetail(**kwargs):
    return SdwanClient().getFlowDetail(**kwargs)

@register('getFlowMetric')
def getFlowMetric(**kwargs):
    return SdwanClient().getFlowMetric(**kwargs)

@register('getMonitorState')
def getMonitorState(**kwargs):
    return SdwanClient().getMonitorState(**kwargs)

@register('getNwpiDscp')
def getNwpiDscp(**kwargs):
    return SdwanClient().getNwpiDscp(**kwargs)

@register('getNwpiNbarAppGroup')
def getNwpiNbarAppGroup(**kwargs):
    return SdwanClient().getNwpiNbarAppGroup(**kwargs)

@register('getNwpiProtocol')
def getNwpiProtocol(**kwargs):
    return SdwanClient().getNwpiProtocol(**kwargs)

@register('nwpiSettingView')
def nwpiSettingView(**kwargs):
    return SdwanClient().nwpiSettingView(**kwargs)

@register('getPacketFeatures')
def getPacketFeatures(**kwargs):
    return SdwanClient().getPacketFeatures(**kwargs)

@register('getPreloadInfo')
def getPreloadInfo(**kwargs):
    return SdwanClient().getPreloadInfo(**kwargs)

@register('getStatQueryFields_28')
def getStatQueryFields_28(**kwargs):
    return SdwanClient().getStatQueryFields_28(**kwargs)

@register('getRoutingDetailFromLocal')
def getRoutingDetailFromLocal(**kwargs):
    return SdwanClient().getRoutingDetailFromLocal(**kwargs)

@register('getEventStatsData')
def getEventStatsData(**kwargs):
    return SdwanClient().getEventStatsData(**kwargs)

@register('getTaskHistory')
def getTaskHistory(**kwargs):
    return SdwanClient().getTaskHistory(**kwargs)

@register('getTaskTrace')
def getTaskTrace(**kwargs):
    return SdwanClient().getTaskTrace(**kwargs)

@register('getTraceCftRecord')
def getTraceCftRecord(**kwargs):
    return SdwanClient().getTraceCftRecord(**kwargs)

@register('getFinalizedFlowCount')
def getFinalizedFlowCount(**kwargs):
    return SdwanClient().getFinalizedFlowCount(**kwargs)

@register('getFinFlowTimeRange')
def getFinFlowTimeRange(**kwargs):
    return SdwanClient().getFinFlowTimeRange(**kwargs)

@register('traceFinFlowWithQuery')
def traceFinFlowWithQuery(**kwargs):
    return SdwanClient().traceFinFlowWithQuery(**kwargs)

@register('getTraceFlow')
def getTraceFlow(**kwargs):
    return SdwanClient().getTraceFlow(**kwargs)

@register('getTraceHistory')
def getTraceHistory(**kwargs):
    return SdwanClient().getTraceHistory(**kwargs)

@register('getTraceInfoByBaseKey')
def getTraceInfoByBaseKey(**kwargs):
    return SdwanClient().getTraceInfoByBaseKey(**kwargs)

@register('getTraceReadoutFilter')
def getTraceReadoutFilter(**kwargs):
    return SdwanClient().getTraceReadoutFilter(**kwargs)

@register('disableSpeedTestSession')
def disableSpeedTestSession(**kwargs):
    return SdwanClient().disableSpeedTestSession(**kwargs)

@register('getInterfaceBandwidth')
def getInterfaceBandwidth(**kwargs):
    return SdwanClient().getInterfaceBandwidth(**kwargs)

@register('startSpeedTest')
def startSpeedTest(**kwargs):
    return SdwanClient().startSpeedTest(**kwargs)

@register('getSpeedTestStatus')
def getSpeedTestStatus(**kwargs):
    return SdwanClient().getSpeedTestStatus(**kwargs)

@register('stopSpeedTest')
def stopSpeedTest(**kwargs):
    return SdwanClient().stopSpeedTest(**kwargs)

@register('getSpeedTest')
def getSpeedTest(**kwargs):
    return SdwanClient().getSpeedTest(**kwargs)

@register('getUMTSData')
def getUMTSData(**kwargs):
    return SdwanClient().getUMTSData(**kwargs)

@register('updateUmtsSessionStatus')
def updateUmtsSessionStatus(**kwargs):
    return SdwanClient().updateUmtsSessionStatus(**kwargs)

@register('generateBootstrapConfigForVedge')
def generateBootstrapConfigForVedge(**kwargs):
    return SdwanClient().generateBootstrapConfigForVedge(**kwargs)

@register('getBootstrapConfigZip')
def getBootstrapConfigZip(**kwargs):
    return SdwanClient().getBootstrapConfigZip(**kwargs)

@register('generateGenericBootstrapConfigForVedges')
def generateGenericBootstrapConfigForVedges(**kwargs):
    return SdwanClient().generateGenericBootstrapConfigForVedges(**kwargs)

@register('getControllerVEdgeSyncStatus_1')
def getControllerVEdgeSyncStatus_1(**kwargs):
    return SdwanClient().getControllerVEdgeSyncStatus_1(**kwargs)

@register('devicesWithoutSubjectSudi')
def devicesWithoutSubjectSudi(**kwargs):
    return SdwanClient().devicesWithoutSubjectSudi(**kwargs)

@register('getManagementSystemIPInfo_1')
def getManagementSystemIPInfo_1(**kwargs):
    return SdwanClient().getManagementSystemIPInfo_1(**kwargs)

@register('getRMACandidates')
def getRMACandidates(**kwargs):
    return SdwanClient().getRMACandidates(**kwargs)

@register('getRootCertStatusAll')
def getRootCertStatusAll(**kwargs):
    return SdwanClient().getRootCertStatusAll(**kwargs)

@register('checkSelfSignedCert_1')
def checkSelfSignedCert_1(**kwargs):
    return SdwanClient().checkSelfSignedCert_1(**kwargs)

@register('syncRootCertChain')
def syncRootCertChain(**kwargs):
    return SdwanClient().syncRootCertChain(**kwargs)

@register('getTenantManagementSystemIPs')
def getTenantManagementSystemIPs(**kwargs):
    return SdwanClient().getTenantManagementSystemIPs(**kwargs)

@register('getCloudDockDataBasedOnDeviceType')
def getCloudDockDataBasedOnDeviceType(**kwargs):
    return SdwanClient().getCloudDockDataBasedOnDeviceType(**kwargs)

@register('getCloudDockDefaultConfigBasedOnDeviceType')
def getCloudDockDefaultConfigBasedOnDeviceType(**kwargs):
    return SdwanClient().getCloudDockDefaultConfigBasedOnDeviceType(**kwargs)

@register('getAllUnclaimedDevices')
def getAllUnclaimedDevices(**kwargs):
    return SdwanClient().getAllUnclaimedDevices(**kwargs)

@register('checkvEdgeDevicePresence')
def checkvEdgeDevicePresence(**kwargs):
    return SdwanClient().checkvEdgeDevicePresence(**kwargs)

@register('getDevicesDetails')
def getDevicesDetails(**kwargs):
    return SdwanClient().getDevicesDetails(**kwargs)

@register('getReverseProxyMappings')
def getReverseProxyMappings(**kwargs):
    return SdwanClient().getReverseProxyMappings(**kwargs)

@register('getCloudXStatus')
def getCloudXStatus(**kwargs):
    return SdwanClient().getCloudXStatus(**kwargs)

@register('getAttachedClientList')
def getAttachedClientList(**kwargs):
    return SdwanClient().getAttachedClientList(**kwargs)

@register('getAttachedDiaList')
def getAttachedDiaList(**kwargs):
    return SdwanClient().getAttachedDiaList(**kwargs)

@register('getAttachedGatewayList')
def getAttachedGatewayList(**kwargs):
    return SdwanClient().getAttachedGatewayList(**kwargs)

@register('getCloudXAvailableApps')
def getCloudXAvailableApps(**kwargs):
    return SdwanClient().getCloudXAvailableApps(**kwargs)

@register('getSiteList')
def getSiteList(**kwargs):
    return SdwanClient().getSiteList(**kwargs)

@register('getDiaList')
def getDiaList(**kwargs):
    return SdwanClient().getDiaList(**kwargs)

@register('getGatewayList')
def getGatewayList(**kwargs):
    return SdwanClient().getGatewayList(**kwargs)

@register('getApps')
def getApps(**kwargs):
    return SdwanClient().getApps(**kwargs)

@register('getSigTunnelList_1')
def getSigTunnelList_1(**kwargs):
    return SdwanClient().getSigTunnelList_1(**kwargs)

@register('sitePerApp')
def sitePerApp(**kwargs):
    return SdwanClient().sitePerApp(**kwargs)

@register('getAttachedConfig')
def getAttachedConfig(**kwargs):
    return SdwanClient().getAttachedConfig(**kwargs)

@register('generateCLIModeDevices')
def generateCLIModeDevices(**kwargs):
    return SdwanClient().generateCLIModeDevices(**kwargs)

@register('generatevManageModeDevices')
def generatevManageModeDevices(**kwargs):
    return SdwanClient().generatevManageModeDevices(**kwargs)

@register('getDeviceDiff')
def getDeviceDiff(**kwargs):
    return SdwanClient().getDeviceDiff(**kwargs)

@register('getCompatibleDevices')
def getCompatibleDevices(**kwargs):
    return SdwanClient().getCompatibleDevices(**kwargs)

@register('getRunningConfig')
def getRunningConfig(**kwargs):
    return SdwanClient().getRunningConfig(**kwargs)

@register('getVpnForDevice')
def getVpnForDevice(**kwargs):
    return SdwanClient().getVpnForDevice(**kwargs)

@register('getCORStatus')
def getCORStatus(**kwargs):
    return SdwanClient().getCORStatus(**kwargs)

@register('getAmiList')
def getAmiList(**kwargs):
    return SdwanClient().getAmiList(**kwargs)

@register('getCloudList')
def getCloudList(**kwargs):
    return SdwanClient().getCloudList(**kwargs)

@register('getCloudAccounts')
def getCloudAccounts(**kwargs):
    return SdwanClient().getCloudAccounts(**kwargs)

@register('getCloudHostVpcAccountDetails')
def getCloudHostVpcAccountDetails(**kwargs):
    return SdwanClient().getCloudHostVpcAccountDetails(**kwargs)

@register('getCloudMappedHostAccounts')
def getCloudMappedHostAccounts(**kwargs):
    return SdwanClient().getCloudMappedHostAccounts(**kwargs)

@register('getCloudOnRampDevices')
def getCloudOnRampDevices(**kwargs):
    return SdwanClient().getCloudOnRampDevices(**kwargs)

@register('getHostVPCs')
def getHostVPCs(**kwargs):
    return SdwanClient().getHostVPCs(**kwargs)

@register('getExternalId')
def getExternalId(**kwargs):
    return SdwanClient().getExternalId(**kwargs)

@register('getTransitDevicePairAndHostList')
def getTransitDevicePairAndHostList(**kwargs):
    return SdwanClient().getTransitDevicePairAndHostList(**kwargs)

@register('getTransitVpcVpnList')
def getTransitVpcVpnList(**kwargs):
    return SdwanClient().getTransitVpcVpnList(**kwargs)

@register('getCloudHostVPCs')
def getCloudHostVPCs(**kwargs):
    return SdwanClient().getCloudHostVPCs(**kwargs)

@register('getMappedVPCs')
def getMappedVPCs(**kwargs):
    return SdwanClient().getMappedVPCs(**kwargs)

@register('getPemKeyList')
def getPemKeyList(**kwargs):
    return SdwanClient().getPemKeyList(**kwargs)

@register('getTransitVPCs')
def getTransitVPCs(**kwargs):
    return SdwanClient().getTransitVPCs(**kwargs)

@register('getTransitVPCSupportedSize')
def getTransitVPCSupportedSize(**kwargs):
    return SdwanClient().getTransitVPCSupportedSize(**kwargs)

@register('getCortexStatus')
def getCortexStatus(**kwargs):
    return SdwanClient().getCortexStatus(**kwargs)

@register('getMappedWanResourceGroups')
def getMappedWanResourceGroups(**kwargs):
    return SdwanClient().getMappedWanResourceGroups(**kwargs)

@register('getWanResourceGroups')
def getWanResourceGroups(**kwargs):
    return SdwanClient().getWanResourceGroups(**kwargs)

@register('generateMasterTemplateList')
def generateMasterTemplateList(**kwargs):
    return SdwanClient().generateMasterTemplateList(**kwargs)

@register('getAttachedDeviceList')
def getAttachedDeviceList(**kwargs):
    return SdwanClient().getAttachedDeviceList(**kwargs)

@register('getAttachedConfigToDevice')
def getAttachedConfigToDevice(**kwargs):
    return SdwanClient().getAttachedConfigToDevice(**kwargs)

@register('getDeviceListByMasterTemplateId')
def getDeviceListByMasterTemplateId(**kwargs):
    return SdwanClient().getDeviceListByMasterTemplateId(**kwargs)

@register('checkVbond')
def checkVbond(**kwargs):
    return SdwanClient().checkVbond(**kwargs)

@register('isMigrationRequired')
def isMigrationRequired(**kwargs):
    return SdwanClient().isMigrationRequired(**kwargs)

@register('generateTemplateForMigration')
def generateTemplateForMigration(**kwargs):
    return SdwanClient().generateTemplateForMigration(**kwargs)

@register('migrationInfo')
def migrationInfo(**kwargs):
    return SdwanClient().migrationInfo(**kwargs)

@register('getMasterTemplateDefinition')
def getMasterTemplateDefinition(**kwargs):
    return SdwanClient().getMasterTemplateDefinition(**kwargs)

@register('getOutOfSyncTemplates')
def getOutOfSyncTemplates(**kwargs):
    return SdwanClient().getOutOfSyncTemplates(**kwargs)

@register('getOutOfSyncDevices')
def getOutOfSyncDevices(**kwargs):
    return SdwanClient().getOutOfSyncDevices(**kwargs)

@register('getAssociatedFeatureTemplatesDetails')
def getAssociatedFeatureTemplatesDetails(**kwargs):
    return SdwanClient().getAssociatedFeatureTemplatesDetails(**kwargs)

@register('generateFeatureTemplateList')
def generateFeatureTemplateList(**kwargs):
    return SdwanClient().generateFeatureTemplateList(**kwargs)

@register('getNetworkInterface')
def getNetworkInterface(**kwargs):
    return SdwanClient().getNetworkInterface(**kwargs)

@register('getDefaultNetworks')
def getDefaultNetworks(**kwargs):
    return SdwanClient().getDefaultNetworks(**kwargs)

@register('getTemplateDefinition')
def getTemplateDefinition(**kwargs):
    return SdwanClient().getTemplateDefinition(**kwargs)

@register('getDeviceTemplatesAttachedToFeature')
def getDeviceTemplatesAttachedToFeature(**kwargs):
    return SdwanClient().getDeviceTemplatesAttachedToFeature(**kwargs)

@register('listLITemplate')
def listLITemplate(**kwargs):
    return SdwanClient().listLITemplate(**kwargs)

@register('generateMasterTemplateDefinition')
def generateMasterTemplateDefinition(**kwargs):
    return SdwanClient().generateMasterTemplateDefinition(**kwargs)

@register('getTemplateForMigration')
def getTemplateForMigration(**kwargs):
    return SdwanClient().getTemplateForMigration(**kwargs)

@register('getGeneralTemplate')
def getGeneralTemplate(**kwargs):
    return SdwanClient().getGeneralTemplate(**kwargs)

@register('generateTemplateTypes')
def generateTemplateTypes(**kwargs):
    return SdwanClient().generateTemplateTypes(**kwargs)

@register('generateTemplateTypeDefinition')
def generateTemplateTypeDefinition(**kwargs):
    return SdwanClient().generateTemplateTypeDefinition(**kwargs)

@register('generateTemplateByDeviceType')
def generateTemplateByDeviceType(**kwargs):
    return SdwanClient().generateTemplateByDeviceType(**kwargs)

@register('previewById')
def previewById(**kwargs):
    return SdwanClient().previewById(**kwargs)

@register('previewById_1')
def previewById_1(**kwargs):
    return SdwanClient().previewById_1(**kwargs)

@register('previewById_2')
def previewById_2(**kwargs):
    return SdwanClient().previewById_2(**kwargs)

@register('previewById_3')
def previewById_3(**kwargs):
    return SdwanClient().previewById_3(**kwargs)

@register('getCloudDiscoveredApps')
def getCloudDiscoveredApps(**kwargs):
    return SdwanClient().getCloudDiscoveredApps(**kwargs)

@register('getCustomApps')
def getCustomApps(**kwargs):
    return SdwanClient().getCustomApps(**kwargs)

@register('getCustomAppById')
def getCustomAppById(**kwargs):
    return SdwanClient().getCustomAppById(**kwargs)

@register('getDefinitions_8')
def getDefinitions_8(**kwargs):
    return SdwanClient().getDefinitions_8(**kwargs)

@register('previewPolicyDefinitionById_8')
def previewPolicyDefinitionById_8(**kwargs):
    return SdwanClient().previewPolicyDefinitionById_8(**kwargs)

@register('getPolicyDefinition_8')
def getPolicyDefinition_8(**kwargs):
    return SdwanClient().getPolicyDefinition_8(**kwargs)

@register('getDefinitions_9')
def getDefinitions_9(**kwargs):
    return SdwanClient().getDefinitions_9(**kwargs)

@register('previewPolicyDefinitionById_9')
def previewPolicyDefinitionById_9(**kwargs):
    return SdwanClient().previewPolicyDefinitionById_9(**kwargs)

@register('getPolicyDefinition_9')
def getPolicyDefinition_9(**kwargs):
    return SdwanClient().getPolicyDefinition_9(**kwargs)

@register('getDefinitions_11')
def getDefinitions_11(**kwargs):
    return SdwanClient().getDefinitions_11(**kwargs)

@register('previewPolicyDefinitionById_11')
def previewPolicyDefinitionById_11(**kwargs):
    return SdwanClient().previewPolicyDefinitionById_11(**kwargs)

@register('getPolicyDefinition_11')
def getPolicyDefinition_11(**kwargs):
    return SdwanClient().getPolicyDefinition_11(**kwargs)

@register('getDefinitions_10')
def getDefinitions_10(**kwargs):
    return SdwanClient().getDefinitions_10(**kwargs)

@register('previewPolicyDefinitionById_10')
def previewPolicyDefinitionById_10(**kwargs):
    return SdwanClient().previewPolicyDefinitionById_10(**kwargs)

@register('getPolicyDefinition_10')
def getPolicyDefinition_10(**kwargs):
    return SdwanClient().getPolicyDefinition_10(**kwargs)

@register('getDefinitions_12')
def getDefinitions_12(**kwargs):
    return SdwanClient().getDefinitions_12(**kwargs)

@register('previewPolicyDefinitionById_12')
def previewPolicyDefinitionById_12(**kwargs):
    return SdwanClient().previewPolicyDefinitionById_12(**kwargs)

@register('getPolicyDefinition_12')
def getPolicyDefinition_12(**kwargs):
    return SdwanClient().getPolicyDefinition_12(**kwargs)

@register('getDefinitions_13')
def getDefinitions_13(**kwargs):
    return SdwanClient().getDefinitions_13(**kwargs)

@register('previewPolicyDefinitionById_13')
def previewPolicyDefinitionById_13(**kwargs):
    return SdwanClient().previewPolicyDefinitionById_13(**kwargs)

@register('getPolicyDefinition_13')
def getPolicyDefinition_13(**kwargs):
    return SdwanClient().getPolicyDefinition_13(**kwargs)

@register('getDefinitions_14')
def getDefinitions_14(**kwargs):
    return SdwanClient().getDefinitions_14(**kwargs)

@register('previewPolicyDefinitionById_14')
def previewPolicyDefinitionById_14(**kwargs):
    return SdwanClient().previewPolicyDefinitionById_14(**kwargs)

@register('getPolicyDefinition_14')
def getPolicyDefinition_14(**kwargs):
    return SdwanClient().getPolicyDefinition_14(**kwargs)

@register('getDefinitions_15')
def getDefinitions_15(**kwargs):
    return SdwanClient().getDefinitions_15(**kwargs)

@register('previewPolicyDefinitionById_15')
def previewPolicyDefinitionById_15(**kwargs):
    return SdwanClient().previewPolicyDefinitionById_15(**kwargs)

@register('getPolicyDefinition_15')
def getPolicyDefinition_15(**kwargs):
    return SdwanClient().getPolicyDefinition_15(**kwargs)

@register('getDefinitions_16')
def getDefinitions_16(**kwargs):
    return SdwanClient().getDefinitions_16(**kwargs)

@register('previewPolicyDefinitionById_16')
def previewPolicyDefinitionById_16(**kwargs):
    return SdwanClient().previewPolicyDefinitionById_16(**kwargs)

@register('getPolicyDefinition_16')
def getPolicyDefinition_16(**kwargs):
    return SdwanClient().getPolicyDefinition_16(**kwargs)

@register('getDefinitions_17')
def getDefinitions_17(**kwargs):
    return SdwanClient().getDefinitions_17(**kwargs)

@register('previewPolicyDefinitionById_17')
def previewPolicyDefinitionById_17(**kwargs):
    return SdwanClient().previewPolicyDefinitionById_17(**kwargs)

@register('getPolicyDefinition_17')
def getPolicyDefinition_17(**kwargs):
    return SdwanClient().getPolicyDefinition_17(**kwargs)

@register('getDefinitions_25')
def getDefinitions_25(**kwargs):
    return SdwanClient().getDefinitions_25(**kwargs)

@register('previewPolicyDefinitionById_25')
def previewPolicyDefinitionById_25(**kwargs):
    return SdwanClient().previewPolicyDefinitionById_25(**kwargs)

@register('getPolicyDefinition_25')
def getPolicyDefinition_25(**kwargs):
    return SdwanClient().getPolicyDefinition_25(**kwargs)

@register('getDefinitions')
def getDefinitions(**kwargs):
    return SdwanClient().getDefinitions(**kwargs)

@register('previewPolicyDefinitionById')
def previewPolicyDefinitionById(**kwargs):
    return SdwanClient().previewPolicyDefinitionById(**kwargs)

@register('getPolicyDefinition')
def getPolicyDefinition(**kwargs):
    return SdwanClient().getPolicyDefinition(**kwargs)

@register('getDefinitions_26')
def getDefinitions_26(**kwargs):
    return SdwanClient().getDefinitions_26(**kwargs)

@register('previewPolicyDefinitionById_26')
def previewPolicyDefinitionById_26(**kwargs):
    return SdwanClient().previewPolicyDefinitionById_26(**kwargs)

@register('getPolicyDefinition_26')
def getPolicyDefinition_26(**kwargs):
    return SdwanClient().getPolicyDefinition_26(**kwargs)

@register('getDefinitions_28')
def getDefinitions_28(**kwargs):
    return SdwanClient().getDefinitions_28(**kwargs)

@register('previewPolicyDefinitionById_28')
def previewPolicyDefinitionById_28(**kwargs):
    return SdwanClient().previewPolicyDefinitionById_28(**kwargs)

@register('getPolicyDefinition_28')
def getPolicyDefinition_28(**kwargs):
    return SdwanClient().getPolicyDefinition_28(**kwargs)

@register('getDefinitions_27')
def getDefinitions_27(**kwargs):
    return SdwanClient().getDefinitions_27(**kwargs)

@register('previewPolicyDefinitionById_27')
def previewPolicyDefinitionById_27(**kwargs):
    return SdwanClient().previewPolicyDefinitionById_27(**kwargs)

@register('getPolicyDefinition_27')
def getPolicyDefinition_27(**kwargs):
    return SdwanClient().getPolicyDefinition_27(**kwargs)

@register('getDefinitions_4')
def getDefinitions_4(**kwargs):
    return SdwanClient().getDefinitions_4(**kwargs)

@register('previewPolicyDefinitionById_4')
def previewPolicyDefinitionById_4(**kwargs):
    return SdwanClient().previewPolicyDefinitionById_4(**kwargs)

@register('getPolicyDefinition_4')
def getPolicyDefinition_4(**kwargs):
    return SdwanClient().getPolicyDefinition_4(**kwargs)

@register('getDefinitions_18')
def getDefinitions_18(**kwargs):
    return SdwanClient().getDefinitions_18(**kwargs)

@register('previewPolicyDefinitionById_18')
def previewPolicyDefinitionById_18(**kwargs):
    return SdwanClient().previewPolicyDefinitionById_18(**kwargs)

@register('getPolicyDefinition_18')
def getPolicyDefinition_18(**kwargs):
    return SdwanClient().getPolicyDefinition_18(**kwargs)

@register('getDefinitions_5')
def getDefinitions_5(**kwargs):
    return SdwanClient().getDefinitions_5(**kwargs)

@register('previewPolicyDefinitionById_5')
def previewPolicyDefinitionById_5(**kwargs):
    return SdwanClient().previewPolicyDefinitionById_5(**kwargs)

@register('getPolicyDefinition_5')
def getPolicyDefinition_5(**kwargs):
    return SdwanClient().getPolicyDefinition_5(**kwargs)

@register('getDefinitions_29')
def getDefinitions_29(**kwargs):
    return SdwanClient().getDefinitions_29(**kwargs)

@register('previewPolicyDefinitionById_29')
def previewPolicyDefinitionById_29(**kwargs):
    return SdwanClient().previewPolicyDefinitionById_29(**kwargs)

@register('getPolicyDefinition_29')
def getPolicyDefinition_29(**kwargs):
    return SdwanClient().getPolicyDefinition_29(**kwargs)

@register('getDefinitions_1')
def getDefinitions_1(**kwargs):
    return SdwanClient().getDefinitions_1(**kwargs)

@register('previewPolicyDefinitionById_1')
def previewPolicyDefinitionById_1(**kwargs):
    return SdwanClient().previewPolicyDefinitionById_1(**kwargs)

@register('getPolicyDefinition_1')
def getPolicyDefinition_1(**kwargs):
    return SdwanClient().getPolicyDefinition_1(**kwargs)

@register('getDefinitions_19')
def getDefinitions_19(**kwargs):
    return SdwanClient().getDefinitions_19(**kwargs)

@register('previewPolicyDefinitionById_19')
def previewPolicyDefinitionById_19(**kwargs):
    return SdwanClient().previewPolicyDefinitionById_19(**kwargs)

@register('getPolicyDefinition_19')
def getPolicyDefinition_19(**kwargs):
    return SdwanClient().getPolicyDefinition_19(**kwargs)

@register('getDefinitions_20')
def getDefinitions_20(**kwargs):
    return SdwanClient().getDefinitions_20(**kwargs)

@register('previewPolicyDefinitionById_20')
def previewPolicyDefinitionById_20(**kwargs):
    return SdwanClient().previewPolicyDefinitionById_20(**kwargs)

@register('getPolicyDefinition_20')
def getPolicyDefinition_20(**kwargs):
    return SdwanClient().getPolicyDefinition_20(**kwargs)

@register('getDefinitions_21')
def getDefinitions_21(**kwargs):
    return SdwanClient().getDefinitions_21(**kwargs)

@register('previewPolicyDefinitionById_21')
def previewPolicyDefinitionById_21(**kwargs):
    return SdwanClient().previewPolicyDefinitionById_21(**kwargs)

@register('getPolicyDefinition_21')
def getPolicyDefinition_21(**kwargs):
    return SdwanClient().getPolicyDefinition_21(**kwargs)

@register('getDefinitions_30')
def getDefinitions_30(**kwargs):
    return SdwanClient().getDefinitions_30(**kwargs)

@register('previewPolicyDefinitionById_30')
def previewPolicyDefinitionById_30(**kwargs):
    return SdwanClient().previewPolicyDefinitionById_30(**kwargs)

@register('getPolicyDefinition_30')
def getPolicyDefinition_30(**kwargs):
    return SdwanClient().getPolicyDefinition_30(**kwargs)

@register('getDefinitions_3')
def getDefinitions_3(**kwargs):
    return SdwanClient().getDefinitions_3(**kwargs)

@register('previewPolicyDefinitionById_3')
def previewPolicyDefinitionById_3(**kwargs):
    return SdwanClient().previewPolicyDefinitionById_3(**kwargs)

@register('getPolicyDefinition_3')
def getPolicyDefinition_3(**kwargs):
    return SdwanClient().getPolicyDefinition_3(**kwargs)

@register('getDefinitions_22')
def getDefinitions_22(**kwargs):
    return SdwanClient().getDefinitions_22(**kwargs)

@register('previewPolicyDefinitionById_22')
def previewPolicyDefinitionById_22(**kwargs):
    return SdwanClient().previewPolicyDefinitionById_22(**kwargs)

@register('getPolicyDefinition_22')
def getPolicyDefinition_22(**kwargs):
    return SdwanClient().getPolicyDefinition_22(**kwargs)

@register('getDefinitions_23')
def getDefinitions_23(**kwargs):
    return SdwanClient().getDefinitions_23(**kwargs)

@register('previewPolicyDefinitionById_23')
def previewPolicyDefinitionById_23(**kwargs):
    return SdwanClient().previewPolicyDefinitionById_23(**kwargs)

@register('getPolicyDefinition_23')
def getPolicyDefinition_23(**kwargs):
    return SdwanClient().getPolicyDefinition_23(**kwargs)

@register('getDefinitions_24')
def getDefinitions_24(**kwargs):
    return SdwanClient().getDefinitions_24(**kwargs)

@register('previewPolicyDefinitionById_24')
def previewPolicyDefinitionById_24(**kwargs):
    return SdwanClient().previewPolicyDefinitionById_24(**kwargs)

@register('getPolicyDefinition_24')
def getPolicyDefinition_24(**kwargs):
    return SdwanClient().getPolicyDefinition_24(**kwargs)

@register('getDefinitions_6')
def getDefinitions_6(**kwargs):
    return SdwanClient().getDefinitions_6(**kwargs)

@register('previewPolicyDefinitionById_6')
def previewPolicyDefinitionById_6(**kwargs):
    return SdwanClient().previewPolicyDefinitionById_6(**kwargs)

@register('getPolicyDefinition_6')
def getPolicyDefinition_6(**kwargs):
    return SdwanClient().getPolicyDefinition_6(**kwargs)

@register('getDefinitions_2')
def getDefinitions_2(**kwargs):
    return SdwanClient().getDefinitions_2(**kwargs)

@register('previewPolicyDefinitionById_2')
def previewPolicyDefinitionById_2(**kwargs):
    return SdwanClient().previewPolicyDefinitionById_2(**kwargs)

@register('getPolicyDefinition_2')
def getPolicyDefinition_2(**kwargs):
    return SdwanClient().getPolicyDefinition_2(**kwargs)

@register('getDefinitions_7')
def getDefinitions_7(**kwargs):
    return SdwanClient().getDefinitions_7(**kwargs)

@register('previewPolicyDefinitionById_7')
def previewPolicyDefinitionById_7(**kwargs):
    return SdwanClient().previewPolicyDefinitionById_7(**kwargs)

@register('getPolicyDefinition_7')
def getPolicyDefinition_7(**kwargs):
    return SdwanClient().getPolicyDefinition_7(**kwargs)

@register('getListReference')
def getListReference(**kwargs):
    return SdwanClient().getListReference(**kwargs)

@register('sgts')
def sgts(**kwargs):
    return SdwanClient().sgts(**kwargs)

@register('getAllPolicyLists')
def getAllPolicyLists(**kwargs):
    return SdwanClient().getAllPolicyLists(**kwargs)

@register('getPolicyLists_3')
def getPolicyLists_3(**kwargs):
    return SdwanClient().getPolicyLists_3(**kwargs)

@register('getPolicyListsWithInfoTag_3')
def getPolicyListsWithInfoTag_3(**kwargs):
    return SdwanClient().getPolicyListsWithInfoTag_3(**kwargs)

@register('previewPolicyListById_3')
def previewPolicyListById_3(**kwargs):
    return SdwanClient().previewPolicyListById_3(**kwargs)

@register('getListsById_3')
def getListsById_3(**kwargs):
    return SdwanClient().getListsById_3(**kwargs)

@register('getPolicyLists_4')
def getPolicyLists_4(**kwargs):
    return SdwanClient().getPolicyLists_4(**kwargs)

@register('getPolicyListsWithInfoTag_4')
def getPolicyListsWithInfoTag_4(**kwargs):
    return SdwanClient().getPolicyListsWithInfoTag_4(**kwargs)

@register('previewPolicyListById_4')
def previewPolicyListById_4(**kwargs):
    return SdwanClient().previewPolicyListById_4(**kwargs)

@register('getListsById_4')
def getListsById_4(**kwargs):
    return SdwanClient().getListsById_4(**kwargs)

@register('getPolicyLists_5')
def getPolicyLists_5(**kwargs):
    return SdwanClient().getPolicyLists_5(**kwargs)

@register('getPolicyListsWithInfoTag_5')
def getPolicyListsWithInfoTag_5(**kwargs):
    return SdwanClient().getPolicyListsWithInfoTag_5(**kwargs)

@register('previewPolicyListById_5')
def previewPolicyListById_5(**kwargs):
    return SdwanClient().previewPolicyListById_5(**kwargs)

@register('getListsById_5')
def getListsById_5(**kwargs):
    return SdwanClient().getListsById_5(**kwargs)

@register('getPolicyLists_13')
def getPolicyLists_13(**kwargs):
    return SdwanClient().getPolicyLists_13(**kwargs)

@register('getPolicyListsWithInfoTag_14')
def getPolicyListsWithInfoTag_14(**kwargs):
    return SdwanClient().getPolicyListsWithInfoTag_14(**kwargs)

@register('previewPolicyListById_14')
def previewPolicyListById_14(**kwargs):
    return SdwanClient().previewPolicyListById_14(**kwargs)

@register('getListsById_14')
def getListsById_14(**kwargs):
    return SdwanClient().getListsById_14(**kwargs)

@register('getPolicyLists_6')
def getPolicyLists_6(**kwargs):
    return SdwanClient().getPolicyLists_6(**kwargs)

@register('getPolicyListsWithInfoTag_6')
def getPolicyListsWithInfoTag_6(**kwargs):
    return SdwanClient().getPolicyListsWithInfoTag_6(**kwargs)

@register('previewPolicyListById_6')
def previewPolicyListById_6(**kwargs):
    return SdwanClient().previewPolicyListById_6(**kwargs)

@register('getListsById_6')
def getListsById_6(**kwargs):
    return SdwanClient().getListsById_6(**kwargs)

@register('getPolicyLists_7')
def getPolicyLists_7(**kwargs):
    return SdwanClient().getPolicyLists_7(**kwargs)

@register('getPolicyListsWithInfoTag_7')
def getPolicyListsWithInfoTag_7(**kwargs):
    return SdwanClient().getPolicyListsWithInfoTag_7(**kwargs)

@register('previewPolicyListById_7')
def previewPolicyListById_7(**kwargs):
    return SdwanClient().previewPolicyListById_7(**kwargs)

@register('getListsById_7')
def getListsById_7(**kwargs):
    return SdwanClient().getListsById_7(**kwargs)

@register('getPolicyLists_8')
def getPolicyLists_8(**kwargs):
    return SdwanClient().getPolicyLists_8(**kwargs)

@register('getPolicyListsWithInfoTag_8')
def getPolicyListsWithInfoTag_8(**kwargs):
    return SdwanClient().getPolicyListsWithInfoTag_8(**kwargs)

@register('previewPolicyListById_8')
def previewPolicyListById_8(**kwargs):
    return SdwanClient().previewPolicyListById_8(**kwargs)

@register('getListsById_8')
def getListsById_8(**kwargs):
    return SdwanClient().getListsById_8(**kwargs)

@register('getPolicyLists_9')
def getPolicyLists_9(**kwargs):
    return SdwanClient().getPolicyLists_9(**kwargs)

@register('getPolicyListsWithInfoTag_10')
def getPolicyListsWithInfoTag_10(**kwargs):
    return SdwanClient().getPolicyListsWithInfoTag_10(**kwargs)

@register('previewPolicyListById_10')
def previewPolicyListById_10(**kwargs):
    return SdwanClient().previewPolicyListById_10(**kwargs)

@register('getListsById_10')
def getListsById_10(**kwargs):
    return SdwanClient().getListsById_10(**kwargs)

@register('getListsForAllDataPrefixes')
def getListsForAllDataPrefixes(**kwargs):
    return SdwanClient().getListsForAllDataPrefixes(**kwargs)

@register('getPolicyListsWithInfoTag_9')
def getPolicyListsWithInfoTag_9(**kwargs):
    return SdwanClient().getPolicyListsWithInfoTag_9(**kwargs)

@register('previewPolicyListById_9')
def previewPolicyListById_9(**kwargs):
    return SdwanClient().previewPolicyListById_9(**kwargs)

@register('getListsById_9')
def getListsById_9(**kwargs):
    return SdwanClient().getListsById_9(**kwargs)

@register('getAllDataPrefixAndFQDNLists')
def getAllDataPrefixAndFQDNLists(**kwargs):
    return SdwanClient().getAllDataPrefixAndFQDNLists(**kwargs)

@register('getPolicyListsWithInfoTag_15')
def getPolicyListsWithInfoTag_15(**kwargs):
    return SdwanClient().getPolicyListsWithInfoTag_15(**kwargs)

@register('previewPolicyListById_15')
def previewPolicyListById_15(**kwargs):
    return SdwanClient().previewPolicyListById_15(**kwargs)

@register('getListsById_15')
def getListsById_15(**kwargs):
    return SdwanClient().getListsById_15(**kwargs)

@register('getPolicyLists_10')
def getPolicyLists_10(**kwargs):
    return SdwanClient().getPolicyLists_10(**kwargs)

@register('getPolicyListsWithInfoTag_11')
def getPolicyListsWithInfoTag_11(**kwargs):
    return SdwanClient().getPolicyListsWithInfoTag_11(**kwargs)

@register('previewPolicyListById_11')
def previewPolicyListById_11(**kwargs):
    return SdwanClient().previewPolicyListById_11(**kwargs)

@register('getListsById_11')
def getListsById_11(**kwargs):
    return SdwanClient().getListsById_11(**kwargs)

@register('getPolicyLists_11')
def getPolicyLists_11(**kwargs):
    return SdwanClient().getPolicyLists_11(**kwargs)

@register('getPolicyListsWithInfoTag_12')
def getPolicyListsWithInfoTag_12(**kwargs):
    return SdwanClient().getPolicyListsWithInfoTag_12(**kwargs)

@register('previewPolicyListById_12')
def previewPolicyListById_12(**kwargs):
    return SdwanClient().previewPolicyListById_12(**kwargs)

@register('getListsById_12')
def getListsById_12(**kwargs):
    return SdwanClient().getListsById_12(**kwargs)

@register('getPolicyLists_12')
def getPolicyLists_12(**kwargs):
    return SdwanClient().getPolicyLists_12(**kwargs)

@register('getPolicyListsWithInfoTag_13')
def getPolicyListsWithInfoTag_13(**kwargs):
    return SdwanClient().getPolicyListsWithInfoTag_13(**kwargs)

@register('previewPolicyListById_13')
def previewPolicyListById_13(**kwargs):
    return SdwanClient().previewPolicyListById_13(**kwargs)

@register('getListsById_13')
def getListsById_13(**kwargs):
    return SdwanClient().getListsById_13(**kwargs)

@register('getPolicyLists_14')
def getPolicyLists_14(**kwargs):
    return SdwanClient().getPolicyLists_14(**kwargs)

@register('getPolicyListsWithInfoTag_16')
def getPolicyListsWithInfoTag_16(**kwargs):
    return SdwanClient().getPolicyListsWithInfoTag_16(**kwargs)

@register('previewPolicyListById_16')
def previewPolicyListById_16(**kwargs):
    return SdwanClient().previewPolicyListById_16(**kwargs)

@register('getListsById_16')
def getListsById_16(**kwargs):
    return SdwanClient().getListsById_16(**kwargs)

@register('getPolicyLists_15')
def getPolicyLists_15(**kwargs):
    return SdwanClient().getPolicyLists_15(**kwargs)

@register('getGeoLocationLists')
def getGeoLocationLists(**kwargs):
    return SdwanClient().getGeoLocationLists(**kwargs)

@register('getPolicyListsWithInfoTag_17')
def getPolicyListsWithInfoTag_17(**kwargs):
    return SdwanClient().getPolicyListsWithInfoTag_17(**kwargs)

@register('previewPolicyListById_17')
def previewPolicyListById_17(**kwargs):
    return SdwanClient().previewPolicyListById_17(**kwargs)

@register('getListsById_17')
def getListsById_17(**kwargs):
    return SdwanClient().getListsById_17(**kwargs)

@register('getPolicyLists_16')
def getPolicyLists_16(**kwargs):
    return SdwanClient().getPolicyLists_16(**kwargs)

@register('getPolicyListsWithInfoTag_18')
def getPolicyListsWithInfoTag_18(**kwargs):
    return SdwanClient().getPolicyListsWithInfoTag_18(**kwargs)

@register('previewPolicyListById_18')
def previewPolicyListById_18(**kwargs):
    return SdwanClient().previewPolicyListById_18(**kwargs)

@register('getListsById_18')
def getListsById_18(**kwargs):
    return SdwanClient().getListsById_18(**kwargs)

@register('getListsForAllPrefixes')
def getListsForAllPrefixes(**kwargs):
    return SdwanClient().getListsForAllPrefixes(**kwargs)

@register('getPolicyListsWithInfoTag_21')
def getPolicyListsWithInfoTag_21(**kwargs):
    return SdwanClient().getPolicyListsWithInfoTag_21(**kwargs)

@register('previewPolicyListById_21')
def previewPolicyListById_21(**kwargs):
    return SdwanClient().previewPolicyListById_21(**kwargs)

@register('getListsById_21')
def getListsById_21(**kwargs):
    return SdwanClient().getListsById_21(**kwargs)

@register('getPolicyLists_17')
def getPolicyLists_17(**kwargs):
    return SdwanClient().getPolicyLists_17(**kwargs)

@register('getPolicyListsWithInfoTag_19')
def getPolicyListsWithInfoTag_19(**kwargs):
    return SdwanClient().getPolicyListsWithInfoTag_19(**kwargs)

@register('previewPolicyListById_19')
def previewPolicyListById_19(**kwargs):
    return SdwanClient().previewPolicyListById_19(**kwargs)

@register('getListsById_19')
def getListsById_19(**kwargs):
    return SdwanClient().getListsById_19(**kwargs)

@register('getPolicyLists_18')
def getPolicyLists_18(**kwargs):
    return SdwanClient().getPolicyLists_18(**kwargs)

@register('getPolicyListsWithInfoTag_20')
def getPolicyListsWithInfoTag_20(**kwargs):
    return SdwanClient().getPolicyListsWithInfoTag_20(**kwargs)

@register('previewPolicyListById_20')
def previewPolicyListById_20(**kwargs):
    return SdwanClient().previewPolicyListById_20(**kwargs)

@register('getListsById_20')
def getListsById_20(**kwargs):
    return SdwanClient().getListsById_20(**kwargs)

@register('getPolicyLists_19')
def getPolicyLists_19(**kwargs):
    return SdwanClient().getPolicyLists_19(**kwargs)

@register('getPolicyListsWithInfoTag_22')
def getPolicyListsWithInfoTag_22(**kwargs):
    return SdwanClient().getPolicyListsWithInfoTag_22(**kwargs)

@register('previewPolicyListById_22')
def previewPolicyListById_22(**kwargs):
    return SdwanClient().previewPolicyListById_22(**kwargs)

@register('getListsById_22')
def getListsById_22(**kwargs):
    return SdwanClient().getListsById_22(**kwargs)

@register('getPolicyLists_20')
def getPolicyLists_20(**kwargs):
    return SdwanClient().getPolicyLists_20(**kwargs)

@register('getPolicyListsWithInfoTag_23')
def getPolicyListsWithInfoTag_23(**kwargs):
    return SdwanClient().getPolicyListsWithInfoTag_23(**kwargs)

@register('previewPolicyListById_23')
def previewPolicyListById_23(**kwargs):
    return SdwanClient().previewPolicyListById_23(**kwargs)

@register('getListsById_23')
def getListsById_23(**kwargs):
    return SdwanClient().getListsById_23(**kwargs)

@register('getPolicyLists')
def getPolicyLists(**kwargs):
    return SdwanClient().getPolicyLists(**kwargs)

@register('getPolicyListsWithInfoTag')
def getPolicyListsWithInfoTag(**kwargs):
    return SdwanClient().getPolicyListsWithInfoTag(**kwargs)

@register('previewPolicyListById')
def previewPolicyListById(**kwargs):
    return SdwanClient().previewPolicyListById(**kwargs)

@register('getListsById')
def getListsById(**kwargs):
    return SdwanClient().getListsById(**kwargs)

@register('getPolicyLists_21')
def getPolicyLists_21(**kwargs):
    return SdwanClient().getPolicyLists_21(**kwargs)

@register('getPolicyListsWithInfoTag_24')
def getPolicyListsWithInfoTag_24(**kwargs):
    return SdwanClient().getPolicyListsWithInfoTag_24(**kwargs)

@register('previewPolicyListById_24')
def previewPolicyListById_24(**kwargs):
    return SdwanClient().previewPolicyListById_24(**kwargs)

@register('getListsById_24')
def getListsById_24(**kwargs):
    return SdwanClient().getListsById_24(**kwargs)

@register('getPolicyLists_22')
def getPolicyLists_22(**kwargs):
    return SdwanClient().getPolicyLists_22(**kwargs)

@register('getPolicyListsWithInfoTag_25')
def getPolicyListsWithInfoTag_25(**kwargs):
    return SdwanClient().getPolicyListsWithInfoTag_25(**kwargs)

@register('previewPolicyListById_25')
def previewPolicyListById_25(**kwargs):
    return SdwanClient().previewPolicyListById_25(**kwargs)

@register('getListsById_25')
def getListsById_25(**kwargs):
    return SdwanClient().getListsById_25(**kwargs)

@register('getPolicyLists_23')
def getPolicyLists_23(**kwargs):
    return SdwanClient().getPolicyLists_23(**kwargs)

@register('getPolicyListsWithInfoTag_26')
def getPolicyListsWithInfoTag_26(**kwargs):
    return SdwanClient().getPolicyListsWithInfoTag_26(**kwargs)

@register('previewPolicyListById_26')
def previewPolicyListById_26(**kwargs):
    return SdwanClient().previewPolicyListById_26(**kwargs)

@register('getListsById_26')
def getListsById_26(**kwargs):
    return SdwanClient().getListsById_26(**kwargs)

@register('getPolicyLists_24')
def getPolicyLists_24(**kwargs):
    return SdwanClient().getPolicyLists_24(**kwargs)

@register('getPolicyListsWithInfoTag_27')
def getPolicyListsWithInfoTag_27(**kwargs):
    return SdwanClient().getPolicyListsWithInfoTag_27(**kwargs)

@register('previewPolicyListById_27')
def previewPolicyListById_27(**kwargs):
    return SdwanClient().previewPolicyListById_27(**kwargs)

@register('getListsById_27')
def getListsById_27(**kwargs):
    return SdwanClient().getListsById_27(**kwargs)

@register('getPolicyLists_25')
def getPolicyLists_25(**kwargs):
    return SdwanClient().getPolicyLists_25(**kwargs)

@register('getPolicyListsWithInfoTag_28')
def getPolicyListsWithInfoTag_28(**kwargs):
    return SdwanClient().getPolicyListsWithInfoTag_28(**kwargs)

@register('previewPolicyListById_28')
def previewPolicyListById_28(**kwargs):
    return SdwanClient().previewPolicyListById_28(**kwargs)

@register('getListsById_28')
def getListsById_28(**kwargs):
    return SdwanClient().getListsById_28(**kwargs)

@register('getPolicyLists_26')
def getPolicyLists_26(**kwargs):
    return SdwanClient().getPolicyLists_26(**kwargs)

@register('getPolicyListsWithInfoTag_29')
def getPolicyListsWithInfoTag_29(**kwargs):
    return SdwanClient().getPolicyListsWithInfoTag_29(**kwargs)

@register('previewPolicyListById_29')
def previewPolicyListById_29(**kwargs):
    return SdwanClient().previewPolicyListById_29(**kwargs)

@register('getListsById_29')
def getListsById_29(**kwargs):
    return SdwanClient().getListsById_29(**kwargs)

@register('getPolicyLists_27')
def getPolicyLists_27(**kwargs):
    return SdwanClient().getPolicyLists_27(**kwargs)

@register('getPolicyListsWithInfoTag_30')
def getPolicyListsWithInfoTag_30(**kwargs):
    return SdwanClient().getPolicyListsWithInfoTag_30(**kwargs)

@register('previewPolicyListById_30')
def previewPolicyListById_30(**kwargs):
    return SdwanClient().previewPolicyListById_30(**kwargs)

@register('getListsById_30')
def getListsById_30(**kwargs):
    return SdwanClient().getListsById_30(**kwargs)

@register('getPolicyLists_28')
def getPolicyLists_28(**kwargs):
    return SdwanClient().getPolicyLists_28(**kwargs)

@register('getPolicyListsWithInfoTag_31')
def getPolicyListsWithInfoTag_31(**kwargs):
    return SdwanClient().getPolicyListsWithInfoTag_31(**kwargs)

@register('previewPolicyListById_31')
def previewPolicyListById_31(**kwargs):
    return SdwanClient().previewPolicyListById_31(**kwargs)

@register('getListsById_31')
def getListsById_31(**kwargs):
    return SdwanClient().getListsById_31(**kwargs)

@register('getPolicyLists_29')
def getPolicyLists_29(**kwargs):
    return SdwanClient().getPolicyLists_29(**kwargs)

@register('getPolicyListsWithInfoTag_32')
def getPolicyListsWithInfoTag_32(**kwargs):
    return SdwanClient().getPolicyListsWithInfoTag_32(**kwargs)

@register('previewPolicyListById_32')
def previewPolicyListById_32(**kwargs):
    return SdwanClient().previewPolicyListById_32(**kwargs)

@register('getListsById_32')
def getListsById_32(**kwargs):
    return SdwanClient().getListsById_32(**kwargs)

@register('getPolicyLists_30')
def getPolicyLists_30(**kwargs):
    return SdwanClient().getPolicyLists_30(**kwargs)

@register('getPolicyListsWithInfoTag_33')
def getPolicyListsWithInfoTag_33(**kwargs):
    return SdwanClient().getPolicyListsWithInfoTag_33(**kwargs)

@register('previewPolicyListById_33')
def previewPolicyListById_33(**kwargs):
    return SdwanClient().previewPolicyListById_33(**kwargs)

@register('getListsById_33')
def getListsById_33(**kwargs):
    return SdwanClient().getListsById_33(**kwargs)

@register('getPolicyLists_31')
def getPolicyLists_31(**kwargs):
    return SdwanClient().getPolicyLists_31(**kwargs)

@register('getPolicyListsWithInfoTag_34')
def getPolicyListsWithInfoTag_34(**kwargs):
    return SdwanClient().getPolicyListsWithInfoTag_34(**kwargs)

@register('previewPolicyListById_34')
def previewPolicyListById_34(**kwargs):
    return SdwanClient().previewPolicyListById_34(**kwargs)

@register('getListsById_34')
def getListsById_34(**kwargs):
    return SdwanClient().getListsById_34(**kwargs)

@register('getPolicyLists_32')
def getPolicyLists_32(**kwargs):
    return SdwanClient().getPolicyLists_32(**kwargs)

@register('getPolicyListsWithInfoTag_35')
def getPolicyListsWithInfoTag_35(**kwargs):
    return SdwanClient().getPolicyListsWithInfoTag_35(**kwargs)

@register('previewPolicyListById_35')
def previewPolicyListById_35(**kwargs):
    return SdwanClient().previewPolicyListById_35(**kwargs)

@register('getListsById_35')
def getListsById_35(**kwargs):
    return SdwanClient().getListsById_35(**kwargs)

@register('getPolicyLists_33')
def getPolicyLists_33(**kwargs):
    return SdwanClient().getPolicyLists_33(**kwargs)

@register('getPolicyListsWithInfoTag_36')
def getPolicyListsWithInfoTag_36(**kwargs):
    return SdwanClient().getPolicyListsWithInfoTag_36(**kwargs)

@register('previewPolicyListById_36')
def previewPolicyListById_36(**kwargs):
    return SdwanClient().previewPolicyListById_36(**kwargs)

@register('getListsById_36')
def getListsById_36(**kwargs):
    return SdwanClient().getListsById_36(**kwargs)

@register('getPolicyLists_34')
def getPolicyLists_34(**kwargs):
    return SdwanClient().getPolicyLists_34(**kwargs)

@register('getPolicyListsWithInfoTag_37')
def getPolicyListsWithInfoTag_37(**kwargs):
    return SdwanClient().getPolicyListsWithInfoTag_37(**kwargs)

@register('previewPolicyListById_37')
def previewPolicyListById_37(**kwargs):
    return SdwanClient().previewPolicyListById_37(**kwargs)

@register('getListsById_37')
def getListsById_37(**kwargs):
    return SdwanClient().getListsById_37(**kwargs)

@register('getPolicyLists_1')
def getPolicyLists_1(**kwargs):
    return SdwanClient().getPolicyLists_1(**kwargs)

@register('getPolicyListsWithInfoTag_1')
def getPolicyListsWithInfoTag_1(**kwargs):
    return SdwanClient().getPolicyListsWithInfoTag_1(**kwargs)

@register('previewPolicyListById_1')
def previewPolicyListById_1(**kwargs):
    return SdwanClient().previewPolicyListById_1(**kwargs)

@register('getListsById_1')
def getListsById_1(**kwargs):
    return SdwanClient().getListsById_1(**kwargs)

@register('getPolicyLists_2')
def getPolicyLists_2(**kwargs):
    return SdwanClient().getPolicyLists_2(**kwargs)

@register('getPolicyListsWithInfoTag_2')
def getPolicyListsWithInfoTag_2(**kwargs):
    return SdwanClient().getPolicyListsWithInfoTag_2(**kwargs)

@register('previewPolicyListById_2')
def previewPolicyListById_2(**kwargs):
    return SdwanClient().previewPolicyListById_2(**kwargs)

@register('getListsById_2')
def getListsById_2(**kwargs):
    return SdwanClient().getListsById_2(**kwargs)

@register('getPolicyLists_35')
def getPolicyLists_35(**kwargs):
    return SdwanClient().getPolicyLists_35(**kwargs)

@register('getPolicyListsWithInfoTag_38')
def getPolicyListsWithInfoTag_38(**kwargs):
    return SdwanClient().getPolicyListsWithInfoTag_38(**kwargs)

@register('previewPolicyListById_38')
def previewPolicyListById_38(**kwargs):
    return SdwanClient().previewPolicyListById_38(**kwargs)

@register('getListsById_38')
def getListsById_38(**kwargs):
    return SdwanClient().getListsById_38(**kwargs)

@register('getPolicyLists_36')
def getPolicyLists_36(**kwargs):
    return SdwanClient().getPolicyLists_36(**kwargs)

@register('getPolicyListsWithInfoTag_39')
def getPolicyListsWithInfoTag_39(**kwargs):
    return SdwanClient().getPolicyListsWithInfoTag_39(**kwargs)

@register('previewPolicyListById_39')
def previewPolicyListById_39(**kwargs):
    return SdwanClient().previewPolicyListById_39(**kwargs)

@register('getListsById_39')
def getListsById_39(**kwargs):
    return SdwanClient().getListsById_39(**kwargs)

@register('getPolicyLists_37')
def getPolicyLists_37(**kwargs):
    return SdwanClient().getPolicyLists_37(**kwargs)

@register('getPolicyListsWithInfoTag_40')
def getPolicyListsWithInfoTag_40(**kwargs):
    return SdwanClient().getPolicyListsWithInfoTag_40(**kwargs)

@register('previewPolicyListById_40')
def previewPolicyListById_40(**kwargs):
    return SdwanClient().previewPolicyListById_40(**kwargs)

@register('getListsById_40')
def getListsById_40(**kwargs):
    return SdwanClient().getListsById_40(**kwargs)

@register('getPolicyLists_38')
def getPolicyLists_38(**kwargs):
    return SdwanClient().getPolicyLists_38(**kwargs)

@register('getPolicyListsWithInfoTag_41')
def getPolicyListsWithInfoTag_41(**kwargs):
    return SdwanClient().getPolicyListsWithInfoTag_41(**kwargs)

@register('previewPolicyListById_41')
def previewPolicyListById_41(**kwargs):
    return SdwanClient().previewPolicyListById_41(**kwargs)

@register('getListsById_41')
def getListsById_41(**kwargs):
    return SdwanClient().getListsById_41(**kwargs)

@register('getPolicyLists_39')
def getPolicyLists_39(**kwargs):
    return SdwanClient().getPolicyLists_39(**kwargs)

@register('getPolicyListsWithInfoTag_42')
def getPolicyListsWithInfoTag_42(**kwargs):
    return SdwanClient().getPolicyListsWithInfoTag_42(**kwargs)

@register('previewPolicyListById_42')
def previewPolicyListById_42(**kwargs):
    return SdwanClient().previewPolicyListById_42(**kwargs)

@register('getListsById_42')
def getListsById_42(**kwargs):
    return SdwanClient().getListsById_42(**kwargs)

@register('getPolicyLists_40')
def getPolicyLists_40(**kwargs):
    return SdwanClient().getPolicyLists_40(**kwargs)

@register('getPolicyListsWithInfoTag_43')
def getPolicyListsWithInfoTag_43(**kwargs):
    return SdwanClient().getPolicyListsWithInfoTag_43(**kwargs)

@register('previewPolicyListById_43')
def previewPolicyListById_43(**kwargs):
    return SdwanClient().previewPolicyListById_43(**kwargs)

@register('getListsById_43')
def getListsById_43(**kwargs):
    return SdwanClient().getListsById_43(**kwargs)

@register('generateSecurityTemplateList')
def generateSecurityTemplateList(**kwargs):
    return SdwanClient().generateSecurityTemplateList(**kwargs)

@register('getSecurityTemplate')
def getSecurityTemplate(**kwargs):
    return SdwanClient().getSecurityTemplate(**kwargs)

@register('getSecurityPolicyDeviceList_1')
def getSecurityPolicyDeviceList_1(**kwargs):
    return SdwanClient().getSecurityPolicyDeviceList_1(**kwargs)

@register('getDeviceListById')
def getDeviceListById(**kwargs):
    return SdwanClient().getDeviceListById(**kwargs)

@register('generateSecurityPolicySummary')
def generateSecurityPolicySummary(**kwargs):
    return SdwanClient().generateSecurityPolicySummary(**kwargs)

@register('getSecurityTemplatesForDevice')
def getSecurityTemplatesForDevice(**kwargs):
    return SdwanClient().getSecurityTemplatesForDevice(**kwargs)

@register('generatePolicyTemplateList')
def generatePolicyTemplateList(**kwargs):
    return SdwanClient().generatePolicyTemplateList(**kwargs)

@register('getVEdgeTemplate')
def getVEdgeTemplate(**kwargs):
    return SdwanClient().getVEdgeTemplate(**kwargs)

@register('getVEdgePolicyDeviceList')
def getVEdgePolicyDeviceList(**kwargs):
    return SdwanClient().getVEdgePolicyDeviceList(**kwargs)

@register('getDeviceListByPolicy')
def getDeviceListByPolicy(**kwargs):
    return SdwanClient().getDeviceListByPolicy(**kwargs)

@register('generateVoiceTemplateList')
def generateVoiceTemplateList(**kwargs):
    return SdwanClient().generateVoiceTemplateList(**kwargs)

@register('getTemplateById')
def getTemplateById(**kwargs):
    return SdwanClient().getTemplateById(**kwargs)

@register('getVoicePolicyDeviceList')
def getVoicePolicyDeviceList(**kwargs):
    return SdwanClient().getVoicePolicyDeviceList(**kwargs)

@register('getDeviceListByPolicyId')
def getDeviceListByPolicyId(**kwargs):
    return SdwanClient().getDeviceListByPolicyId(**kwargs)

@register('generateVoicePolicySummary')
def generateVoicePolicySummary(**kwargs):
    return SdwanClient().generateVoicePolicySummary(**kwargs)

@register('getVoiceTemplatesForDevice')
def getVoiceTemplatesForDevice(**kwargs):
    return SdwanClient().getVoiceTemplatesForDevice(**kwargs)

@register('generateVSmartPolicyTemplateList')
def generateVSmartPolicyTemplateList(**kwargs):
    return SdwanClient().generateVSmartPolicyTemplateList(**kwargs)

@register('checkVSmartConnectivityStatus')
def checkVSmartConnectivityStatus(**kwargs):
    return SdwanClient().checkVSmartConnectivityStatus(**kwargs)

@register('getTemplateByPolicyId')
def getTemplateByPolicyId(**kwargs):
    return SdwanClient().getTemplateByPolicyId(**kwargs)

@register('QosmosNbarMigrationWarning')
def QosmosNbarMigrationWarning(**kwargs):
    return SdwanClient().QosmosNbarMigrationWarning(**kwargs)

@register('getAllTenants')
def getAllTenants(**kwargs):
    return SdwanClient().getAllTenants(**kwargs)

@register('getTenantvSmartMapping')
def getTenantvSmartMapping(**kwargs):
    return SdwanClient().getTenantvSmartMapping(**kwargs)

@register('getTenantHostingCapacityOnvSmarts')
def getTenantHostingCapacityOnvSmarts(**kwargs):
    return SdwanClient().getTenantHostingCapacityOnvSmarts(**kwargs)

@register('getTenant')
def getTenant(**kwargs):
    return SdwanClient().getTenant(**kwargs)

@register('downloadExistingBackupFile')
def downloadExistingBackupFile(**kwargs):
    return SdwanClient().downloadExistingBackupFile(**kwargs)

@register('exportTenantBackup')
def exportTenantBackup(**kwargs):
    return SdwanClient().exportTenantBackup(**kwargs)

@register('listTenantBackup')
def listTenantBackup(**kwargs):
    return SdwanClient().listTenantBackup(**kwargs)

@register('downloadTenantData')
def downloadTenantData(**kwargs):
    return SdwanClient().downloadTenantData(**kwargs)

@register('getMigrationToken')
def getMigrationToken(**kwargs):
    return SdwanClient().getMigrationToken(**kwargs)

@register('reTriggerNetworkMigration')
def reTriggerNetworkMigration(**kwargs):
    return SdwanClient().reTriggerNetworkMigration(**kwargs)

@register('getAllTenantStatuses')
def getAllTenantStatuses(**kwargs):
    return SdwanClient().getAllTenantStatuses(**kwargs)

@register('createFullTopology')
def createFullTopology(**kwargs):
    return SdwanClient().createFullTopology(**kwargs)

@register('createDeviceTopology')
def createDeviceTopology(**kwargs):
    return SdwanClient().createDeviceTopology(**kwargs)

@register('getSiteTopology')
def getSiteTopology(**kwargs):
    return SdwanClient().getSiteTopology(**kwargs)

@register('getSiteTopologyMonitorData')
def getSiteTopologyMonitorData(**kwargs):
    return SdwanClient().getSiteTopologyMonitorData(**kwargs)

@register('createPhysicalTopology')
def createPhysicalTopology(**kwargs):
    return SdwanClient().createPhysicalTopology(**kwargs)

@register('getControlConnections')
def getControlConnections(**kwargs):
    return SdwanClient().getControlConnections(**kwargs)

@register('getDeviceConfiguration')
def getDeviceConfiguration(**kwargs):
    return SdwanClient().getDeviceConfiguration(**kwargs)

@register('getAllKeysFromUmbrella')
def getAllKeysFromUmbrella(**kwargs):
    return SdwanClient().getAllKeysFromUmbrella(**kwargs)

@register('getManagementKeysFromUmbrella')
def getManagementKeysFromUmbrella(**kwargs):
    return SdwanClient().getManagementKeysFromUmbrella(**kwargs)

@register('getNetworkKeysFromUmbrella')
def getNetworkKeysFromUmbrella(**kwargs):
    return SdwanClient().getNetworkKeysFromUmbrella(**kwargs)

@register('getReportingKeysFromUmbrella')
def getReportingKeysFromUmbrella(**kwargs):
    return SdwanClient().getReportingKeysFromUmbrella(**kwargs)

@register('sendMetaDataToUmbrella')
def sendMetaDataToUmbrella(**kwargs):
    return SdwanClient().sendMetaDataToUmbrella(**kwargs)

@register('getStatus')
def getStatus(**kwargs):
    return SdwanClient().getStatus(**kwargs)

@register('getUrlMonitor')
def getUrlMonitor(**kwargs):
    return SdwanClient().getUrlMonitor(**kwargs)

@register('returnMetric')
def returnMetric(**kwargs):
    return SdwanClient().returnMetric(**kwargs)

@register('returnMetricFiles')
def returnMetricFiles(**kwargs):
    return SdwanClient().returnMetricFiles(**kwargs)

@register('getMetricsList')
def getMetricsList(**kwargs):
    return SdwanClient().getMetricsList(**kwargs)

@register('getDBSizeOnFile')
def getDBSizeOnFile(**kwargs):
    return SdwanClient().getDBSizeOnFile(**kwargs)

@register('listLogFileDetails')
def listLogFileDetails(**kwargs):
    return SdwanClient().listLogFileDetails(**kwargs)

@register('listVManageServerLogLastNLines')
def listVManageServerLogLastNLines(**kwargs):
    return SdwanClient().listVManageServerLogLastNLines(**kwargs)

@register('listConfigurations')
def listConfigurations(**kwargs):
    return SdwanClient().listConfigurations(**kwargs)

@register('listLoggers')
def listLoggers(**kwargs):
    return SdwanClient().listLoggers(**kwargs)

@register('getStatsMigrationRangeConfig')
def getStatsMigrationRangeConfig(**kwargs):
    return SdwanClient().getStatsMigrationRangeConfig(**kwargs)

@register('getStatsMigrationSettings')
def getStatsMigrationSettings(**kwargs):
    return SdwanClient().getStatsMigrationSettings(**kwargs)

@register('getStatsMigrationStatsDbInfo')
def getStatsMigrationStatsDbInfo(**kwargs):
    return SdwanClient().getStatsMigrationStatsDbInfo(**kwargs)

@register('getStatsMigrationStatus')
def getStatsMigrationStatus(**kwargs):
    return SdwanClient().getStatsMigrationStatus(**kwargs)

@register('getCloudOnRampSaasStatus')
def getCloudOnRampSaasStatus(**kwargs):
    return SdwanClient().getCloudOnRampSaasStatus(**kwargs)

@register('getCloudTunnelList')
def getCloudTunnelList(**kwargs):
    return SdwanClient().getCloudTunnelList(**kwargs)

@register('getPolicyGroupsWithCorSaasApps')
def getPolicyGroupsWithCorSaasApps(**kwargs):
    return SdwanClient().getPolicyGroupsWithCorSaasApps(**kwargs)

@register('getCorSitesPerDevice')
def getCorSitesPerDevice(**kwargs):
    return SdwanClient().getCorSitesPerDevice(**kwargs)

@register('getInactiveCorSaasSites')
def getInactiveCorSaasSites(**kwargs):
    return SdwanClient().getInactiveCorSaasSites(**kwargs)

@register('getLegacyDeviceList')
def getLegacyDeviceList(**kwargs):
    return SdwanClient().getLegacyDeviceList(**kwargs)

@register('getCorSaasStatusPerDevice')
def getCorSaasStatusPerDevice(**kwargs):
    return SdwanClient().getCorSaasStatusPerDevice(**kwargs)

@register('getWebexSyncStatus')
def getWebexSyncStatus(**kwargs):
    return SdwanClient().getWebexSyncStatus(**kwargs)

@register('GetConfigGroupBySolution')
def GetConfigGroupBySolution(**kwargs):
    return SdwanClient().GetConfigGroupBySolution(**kwargs)

@register('GetConfigGroup')
def GetConfigGroup(**kwargs):
    return SdwanClient().GetConfigGroup(**kwargs)

@register('GetConfigGroupAssociation')
def GetConfigGroupAssociation(**kwargs):
    return SdwanClient().GetConfigGroupAssociation(**kwargs)

@register('getConfigGroupDeviceVariables')
def getConfigGroupDeviceVariables(**kwargs):
    return SdwanClient().getConfigGroupDeviceVariables(**kwargs)

@register('getConfigGroupDeviceVariablesSchema')
def getConfigGroupDeviceVariablesSchema(**kwargs):
    return SdwanClient().getConfigGroupDeviceVariablesSchema(**kwargs)

@register('getRuleAssociationByConfigGroupId')
def getRuleAssociationByConfigGroupId(**kwargs):
    return SdwanClient().getRuleAssociationByConfigGroupId(**kwargs)

@register('getRunningIosCliConfig')
def getRunningIosCliConfig(**kwargs):
    return SdwanClient().getRunningIosCliConfig(**kwargs)

@register('getUnsupportedCliConfig')
def getUnsupportedCliConfig(**kwargs):
    return SdwanClient().getUnsupportedCliConfig(**kwargs)

@register('GetMobilityCliFeatureProfile')
def GetMobilityCliFeatureProfile(**kwargs):
    return SdwanClient().GetMobilityCliFeatureProfile(**kwargs)

@register('GetMobilityCliFeatureProfileByCliId')
def GetMobilityCliFeatureProfileByCliId(**kwargs):
    return SdwanClient().GetMobilityCliFeatureProfileByCliId(**kwargs)

@register('GetAllConfigFeatureForMobility')
def GetAllConfigFeatureForMobility(**kwargs):
    return SdwanClient().GetAllConfigFeatureForMobility(**kwargs)

@register('GetConfigFeatureForMobilityByParcelId')
def GetConfigFeatureForMobilityByParcelId(**kwargs):
    return SdwanClient().GetConfigFeatureForMobilityByParcelId(**kwargs)

@register('GetMobilityGlobalFeatureProfile')
def GetMobilityGlobalFeatureProfile(**kwargs):
    return SdwanClient().GetMobilityGlobalFeatureProfile(**kwargs)

@register('GetMobilityGlobalBasicParcelSchemaBySchemaType')
def GetMobilityGlobalBasicParcelSchemaBySchemaType(**kwargs):
    return SdwanClient().GetMobilityGlobalBasicParcelSchemaBySchemaType(**kwargs)

@register('GetMobilityFeatureProfileByGlobalId')
def GetMobilityFeatureProfileByGlobalId(**kwargs):
    return SdwanClient().GetMobilityFeatureProfileByGlobalId(**kwargs)

@register('GetQosFeatureForGlobal')
def GetQosFeatureForGlobal(**kwargs):
    return SdwanClient().GetQosFeatureForGlobal(**kwargs)

@register('GetQosFeatureByParcelIdForGlobal')
def GetQosFeatureByParcelIdForGlobal(**kwargs):
    return SdwanClient().GetQosFeatureByParcelIdForGlobal(**kwargs)

@register('GetAaaServersProfileParcelForMobility')
def GetAaaServersProfileParcelForMobility(**kwargs):
    return SdwanClient().GetAaaServersProfileParcelForMobility(**kwargs)

@register('GetAaaServersProfileParcelByParcelIdForMobility')
def GetAaaServersProfileParcelByParcelIdForMobility(**kwargs):
    return SdwanClient().GetAaaServersProfileParcelByParcelIdForMobility(**kwargs)

@register('GetBasicProfileParcelForMobility')
def GetBasicProfileParcelForMobility(**kwargs):
    return SdwanClient().GetBasicProfileParcelForMobility(**kwargs)

@register('GetBasicProfileParcelByParcelIdForMobility')
def GetBasicProfileParcelByParcelIdForMobility(**kwargs):
    return SdwanClient().GetBasicProfileParcelByParcelIdForMobility(**kwargs)

@register('GetCellularProfileParcelListForMobility')
def GetCellularProfileParcelListForMobility(**kwargs):
    return SdwanClient().GetCellularProfileParcelListForMobility(**kwargs)

@register('GetCellularProfileParcelForMobility')
def GetCellularProfileParcelForMobility(**kwargs):
    return SdwanClient().GetCellularProfileParcelForMobility(**kwargs)

@register('GetEsimCellularProfileFeatureForMobility')
def GetEsimCellularProfileFeatureForMobility(**kwargs):
    return SdwanClient().GetEsimCellularProfileFeatureForMobility(**kwargs)

@register('GetEsimCellularProfileFeatureByEsimCellularIdForMobility')
def GetEsimCellularProfileFeatureByEsimCellularIdForMobility(**kwargs):
    return SdwanClient().GetEsimCellularProfileFeatureByEsimCellularIdForMobility(**kwargs)

@register('GetEthernetProfileParcels')
def GetEthernetProfileParcels(**kwargs):
    return SdwanClient().GetEthernetProfileParcels(**kwargs)

@register('GetEthernetProfileParcel')
def GetEthernetProfileParcel(**kwargs):
    return SdwanClient().GetEthernetProfileParcel(**kwargs)

@register('GetLoggingProfileFeatureForMobility')
def GetLoggingProfileFeatureForMobility(**kwargs):
    return SdwanClient().GetLoggingProfileFeatureForMobility(**kwargs)

@register('GetLoggingProfileFeatureByFeatureIdForMobility')
def GetLoggingProfileFeatureByFeatureIdForMobility(**kwargs):
    return SdwanClient().GetLoggingProfileFeatureByFeatureIdForMobility(**kwargs)

@register('GetNetworkProtocolProfileParcelListForMobility')
def GetNetworkProtocolProfileParcelListForMobility(**kwargs):
    return SdwanClient().GetNetworkProtocolProfileParcelListForMobility(**kwargs)

@register('GetNetworkProtocolProfileParcelForMobility')
def GetNetworkProtocolProfileParcelForMobility(**kwargs):
    return SdwanClient().GetNetworkProtocolProfileParcelForMobility(**kwargs)

@register('GetSecurityPolicyProfileParcelListForMobility')
def GetSecurityPolicyProfileParcelListForMobility(**kwargs):
    return SdwanClient().GetSecurityPolicyProfileParcelListForMobility(**kwargs)

@register('GetSecurityPolicyProfileParcelForMobility')
def GetSecurityPolicyProfileParcelForMobility(**kwargs):
    return SdwanClient().GetSecurityPolicyProfileParcelForMobility(**kwargs)

@register('GetVpnProfileParcelForMobility')
def GetVpnProfileParcelForMobility(**kwargs):
    return SdwanClient().GetVpnProfileParcelForMobility(**kwargs)

@register('GetVpnProfileParcelByParcelIdForMobility')
def GetVpnProfileParcelByParcelIdForMobility(**kwargs):
    return SdwanClient().GetVpnProfileParcelByParcelIdForMobility(**kwargs)

@register('GetWifiProfileParcelListForMobility')
def GetWifiProfileParcelListForMobility(**kwargs):
    return SdwanClient().GetWifiProfileParcelListForMobility(**kwargs)

@register('GetWifiProfileParcelForMobility')
def GetWifiProfileParcelForMobility(**kwargs):
    return SdwanClient().GetWifiProfileParcelForMobility(**kwargs)

@register('GetAllNfvirtualCLIFeatureProfiles')
def GetAllNfvirtualCLIFeatureProfiles(**kwargs):
    return SdwanClient().GetAllNfvirtualCLIFeatureProfiles(**kwargs)

@register('GetNfvirtualCLIFeatureProfileByid')
def GetNfvirtualCLIFeatureProfileByid(**kwargs):
    return SdwanClient().GetNfvirtualCLIFeatureProfileByid(**kwargs)

@register('getNfvirtualCLIParcel')
def getNfvirtualCLIParcel(**kwargs):
    return SdwanClient().getNfvirtualCLIParcel(**kwargs)

@register('GetAllNfvirtualNetworksFeatureProfiles')
def GetAllNfvirtualNetworksFeatureProfiles(**kwargs):
    return SdwanClient().GetAllNfvirtualNetworksFeatureProfiles(**kwargs)

@register('GetAllNfvirtualOvsNetworksFeatureProfileByProfileId')
def GetAllNfvirtualOvsNetworksFeatureProfileByProfileId(**kwargs):
    return SdwanClient().GetAllNfvirtualOvsNetworksFeatureProfileByProfileId(**kwargs)

@register('GetNfvirtualNetworksFeatureProfileByProfileId')
def GetNfvirtualNetworksFeatureProfileByProfileId(**kwargs):
    return SdwanClient().GetNfvirtualNetworksFeatureProfileByProfileId(**kwargs)

@register('GetNfvirtualLANParcel')
def GetNfvirtualLANParcel(**kwargs):
    return SdwanClient().GetNfvirtualLANParcel(**kwargs)

@register('GetNfvirtualOVSNetworkParcel')
def GetNfvirtualOVSNetworkParcel(**kwargs):
    return SdwanClient().GetNfvirtualOVSNetworkParcel(**kwargs)

@register('GetNfvirtualRoutesParcel')
def GetNfvirtualRoutesParcel(**kwargs):
    return SdwanClient().GetNfvirtualRoutesParcel(**kwargs)

@register('GetNfvirtualSwitchParcel')
def GetNfvirtualSwitchParcel(**kwargs):
    return SdwanClient().GetNfvirtualSwitchParcel(**kwargs)

@register('GetNfvirtualVNFAttributesParcel')
def GetNfvirtualVNFAttributesParcel(**kwargs):
    return SdwanClient().GetNfvirtualVNFAttributesParcel(**kwargs)

@register('GetNfvirtualVNFParcel')
def GetNfvirtualVNFParcel(**kwargs):
    return SdwanClient().GetNfvirtualVNFParcel(**kwargs)

@register('GetNfvirtualWANParcel')
def GetNfvirtualWANParcel(**kwargs):
    return SdwanClient().GetNfvirtualWANParcel(**kwargs)

@register('GetAllNfvirtualSystemFeatureProfiles')
def GetAllNfvirtualSystemFeatureProfiles(**kwargs):
    return SdwanClient().GetAllNfvirtualSystemFeatureProfiles(**kwargs)

@register('GetNfvirtualSystemFeatureProfileByProfileId')
def GetNfvirtualSystemFeatureProfileByProfileId(**kwargs):
    return SdwanClient().GetNfvirtualSystemFeatureProfileByProfileId(**kwargs)

@register('GetNfvirtualAAAParcel')
def GetNfvirtualAAAParcel(**kwargs):
    return SdwanClient().GetNfvirtualAAAParcel(**kwargs)

@register('GetNfvirtualBannerParcel')
def GetNfvirtualBannerParcel(**kwargs):
    return SdwanClient().GetNfvirtualBannerParcel(**kwargs)

@register('GetNfvirtualLoggingParcel')
def GetNfvirtualLoggingParcel(**kwargs):
    return SdwanClient().GetNfvirtualLoggingParcel(**kwargs)

@register('GetNfvirtualNTPParcel')
def GetNfvirtualNTPParcel(**kwargs):
    return SdwanClient().GetNfvirtualNTPParcel(**kwargs)

@register('GetNfvirtualSNMPParcel')
def GetNfvirtualSNMPParcel(**kwargs):
    return SdwanClient().GetNfvirtualSNMPParcel(**kwargs)

@register('GetNfvirtualSystemSettingsParcel')
def GetNfvirtualSystemSettingsParcel(**kwargs):
    return SdwanClient().GetNfvirtualSystemSettingsParcel(**kwargs)

@register('GetSdroutingFeatureProfiles')
def GetSdroutingFeatureProfiles(**kwargs):
    return SdwanClient().GetSdroutingFeatureProfiles(**kwargs)

@register('GetSdroutingCliFeatureProfiles')
def GetSdroutingCliFeatureProfiles(**kwargs):
    return SdwanClient().GetSdroutingCliFeatureProfiles(**kwargs)

@register('Get')
def Get(**kwargs):
    return SdwanClient().Get(**kwargs)

@register('GetSdroutingCliFeatureProfile')
def GetSdroutingCliFeatureProfile(**kwargs):
    return SdwanClient().GetSdroutingCliFeatureProfile(**kwargs)

@register('GetSdroutingCLIAddOnFeatures')
def GetSdroutingCLIAddOnFeatures(**kwargs):
    return SdwanClient().GetSdroutingCLIAddOnFeatures(**kwargs)

@register('GetSdroutingCLIAddOnFeature')
def GetSdroutingCLIAddOnFeature(**kwargs):
    return SdwanClient().GetSdroutingCLIAddOnFeature(**kwargs)

@register('GetSdroutingCliConfigGroupFeatures')
def GetSdroutingCliConfigGroupFeatures(**kwargs):
    return SdwanClient().GetSdroutingCliConfigGroupFeatures(**kwargs)

@register('GetSdroutingCliConfigGroupFeature')
def GetSdroutingCliConfigGroupFeature(**kwargs):
    return SdwanClient().GetSdroutingCliConfigGroupFeature(**kwargs)

@register('GetSdroutingIosCLassicCLIAddOnFeatures')
def GetSdroutingIosCLassicCLIAddOnFeatures(**kwargs):
    return SdwanClient().GetSdroutingIosCLassicCLIAddOnFeatures(**kwargs)

@register('GetSdroutingIosClassicCLIAddOnFeature')
def GetSdroutingIosClassicCLIAddOnFeature(**kwargs):
    return SdwanClient().GetSdroutingIosClassicCLIAddOnFeature(**kwargs)

@register('GetSdRoutingEmbeddedSecurityFeatureProfiles')
def GetSdRoutingEmbeddedSecurityFeatureProfiles(**kwargs):
    return SdwanClient().GetSdRoutingEmbeddedSecurityFeatureProfiles(**kwargs)

@register('GetSdRoutingEmbeddedSecurityFeatureProfileByProfileId')
def GetSdRoutingEmbeddedSecurityFeatureProfileByProfileId(**kwargs):
    return SdwanClient().GetSdRoutingEmbeddedSecurityFeatureProfileByProfileId(**kwargs)

@register('GetSecurityFeature')
def GetSecurityFeature(**kwargs):
    return SdwanClient().GetSecurityFeature(**kwargs)

@register('GetSecurityFeatureByFeatureId')
def GetSecurityFeatureByFeatureId(**kwargs):
    return SdwanClient().GetSecurityFeatureByFeatureId(**kwargs)

@register('GetNgfirewallFeature')
def GetNgfirewallFeature(**kwargs):
    return SdwanClient().GetNgfirewallFeature(**kwargs)

@register('GetNgfirewallFeatureByFeatureId')
def GetNgfirewallFeatureByFeatureId(**kwargs):
    return SdwanClient().GetNgfirewallFeatureByFeatureId(**kwargs)

@register('GetCybervisionProfileFeatureForOther')
def GetCybervisionProfileFeatureForOther(**kwargs):
    return SdwanClient().GetCybervisionProfileFeatureForOther(**kwargs)

@register('GetCybervisionProfileFeatureByFeatureIdForOther')
def GetCybervisionProfileFeatureByFeatureIdForOther(**kwargs):
    return SdwanClient().GetCybervisionProfileFeatureByFeatureIdForOther(**kwargs)

@register('GetSdroutingServiceFeatureProfiles')
def GetSdroutingServiceFeatureProfiles(**kwargs):
    return SdwanClient().GetSdroutingServiceFeatureProfiles(**kwargs)

@register('GetSdroutingServiceFeatureProfile')
def GetSdroutingServiceFeatureProfile(**kwargs):
    return SdwanClient().GetSdroutingServiceFeatureProfile(**kwargs)

@register('GetSdroutingDhcpServerProfileParcels')
def GetSdroutingDhcpServerProfileParcels(**kwargs):
    return SdwanClient().GetSdroutingDhcpServerProfileParcels(**kwargs)

@register('GetSdroutingDhcpServerProfileParcel')
def GetSdroutingDhcpServerProfileParcel(**kwargs):
    return SdwanClient().GetSdroutingDhcpServerProfileParcel(**kwargs)

@register('GetSdroutingServiceIpsecProfileFeatures')
def GetSdroutingServiceIpsecProfileFeatures(**kwargs):
    return SdwanClient().GetSdroutingServiceIpsecProfileFeatures(**kwargs)

@register('GetSdroutingServiceIpsecProfileFeature')
def GetSdroutingServiceIpsecProfileFeature(**kwargs):
    return SdwanClient().GetSdroutingServiceIpsecProfileFeature(**kwargs)

@register('GetSdroutingServiceIpv4AclFeatures')
def GetSdroutingServiceIpv4AclFeatures(**kwargs):
    return SdwanClient().GetSdroutingServiceIpv4AclFeatures(**kwargs)

@register('GetSdroutingServiceIpv4AclFeature')
def GetSdroutingServiceIpv4AclFeature(**kwargs):
    return SdwanClient().GetSdroutingServiceIpv4AclFeature(**kwargs)

@register('GetListOfProfileParcels')
def GetListOfProfileParcels(**kwargs):
    return SdwanClient().GetListOfProfileParcels(**kwargs)

@register('GetMultiCloudConnection')
def GetMultiCloudConnection(**kwargs):
    return SdwanClient().GetMultiCloudConnection(**kwargs)

@register('GetSdroutingServiceObjectTrackerFeatures')
def GetSdroutingServiceObjectTrackerFeatures(**kwargs):
    return SdwanClient().GetSdroutingServiceObjectTrackerFeatures(**kwargs)

@register('GetSdroutingServiceObjectTrackerFeature')
def GetSdroutingServiceObjectTrackerFeature(**kwargs):
    return SdwanClient().GetSdroutingServiceObjectTrackerFeature(**kwargs)

@register('GetSdroutingServiceObjectTrackerGroupFeatures')
def GetSdroutingServiceObjectTrackerGroupFeatures(**kwargs):
    return SdwanClient().GetSdroutingServiceObjectTrackerGroupFeatures(**kwargs)

@register('GetSdroutingServiceObjectTrackerGroupFeature')
def GetSdroutingServiceObjectTrackerGroupFeature(**kwargs):
    return SdwanClient().GetSdroutingServiceObjectTrackerGroupFeature(**kwargs)

@register('GetSdroutingServiceRoutePolicyFeatures')
def GetSdroutingServiceRoutePolicyFeatures(**kwargs):
    return SdwanClient().GetSdroutingServiceRoutePolicyFeatures(**kwargs)

@register('GetSdroutingServiceRoutePolicyFeature')
def GetSdroutingServiceRoutePolicyFeature(**kwargs):
    return SdwanClient().GetSdroutingServiceRoutePolicyFeature(**kwargs)

@register('GetSdroutingServiceVrfOspfFeatures')
def GetSdroutingServiceVrfOspfFeatures(**kwargs):
    return SdwanClient().GetSdroutingServiceVrfOspfFeatures(**kwargs)

@register('GetSdroutingServiceVrfOspfFeature')
def GetSdroutingServiceVrfOspfFeature(**kwargs):
    return SdwanClient().GetSdroutingServiceVrfOspfFeature(**kwargs)

@register('GetSdroutingServiceVrfOspfv3Ipv4Features')
def GetSdroutingServiceVrfOspfv3Ipv4Features(**kwargs):
    return SdwanClient().GetSdroutingServiceVrfOspfv3Ipv4Features(**kwargs)

@register('GetSdroutingServiceVrfOspfv3Ipv4Feature')
def GetSdroutingServiceVrfOspfv3Ipv4Feature(**kwargs):
    return SdwanClient().GetSdroutingServiceVrfOspfv3Ipv4Feature(**kwargs)

@register('GetSdroutingServiceVrfOspfv3Ipv6Features')
def GetSdroutingServiceVrfOspfv3Ipv6Features(**kwargs):
    return SdwanClient().GetSdroutingServiceVrfOspfv3Ipv6Features(**kwargs)

@register('GetSdroutingServiceVrfOspfv3Ipv6Feature')
def GetSdroutingServiceVrfOspfv3Ipv6Feature(**kwargs):
    return SdwanClient().GetSdroutingServiceVrfOspfv3Ipv6Feature(**kwargs)

@register('GetSdroutingServiceVRFFeatures')
def GetSdroutingServiceVRFFeatures(**kwargs):
    return SdwanClient().GetSdroutingServiceVRFFeatures(**kwargs)

@register('GetSdroutingServiceVrfBgpFeatures')
def GetSdroutingServiceVrfBgpFeatures(**kwargs):
    return SdwanClient().GetSdroutingServiceVrfBgpFeatures(**kwargs)

@register('GetSdroutingServiceVrfBgpFeature')
def GetSdroutingServiceVrfBgpFeature(**kwargs):
    return SdwanClient().GetSdroutingServiceVrfBgpFeature(**kwargs)

@register('GetSdroutingServiceVrfEigrpFeatures')
def GetSdroutingServiceVrfEigrpFeatures(**kwargs):
    return SdwanClient().GetSdroutingServiceVrfEigrpFeatures(**kwargs)

@register('GetSdroutingServiceVrfEigrpFeature')
def GetSdroutingServiceVrfEigrpFeature(**kwargs):
    return SdwanClient().GetSdroutingServiceVrfEigrpFeature(**kwargs)

@register('GetSdroutingServiceVRFFeature')
def GetSdroutingServiceVRFFeature(**kwargs):
    return SdwanClient().GetSdroutingServiceVRFFeature(**kwargs)

@register('GetSdroutingServiceVRFDmvpnTunnelFeatures')
def GetSdroutingServiceVRFDmvpnTunnelFeatures(**kwargs):
    return SdwanClient().GetSdroutingServiceVRFDmvpnTunnelFeatures(**kwargs)

@register('GetSdroutingServiceVRFDmvpnTunnelFeature')
def GetSdroutingServiceVRFDmvpnTunnelFeature(**kwargs):
    return SdwanClient().GetSdroutingServiceVRFDmvpnTunnelFeature(**kwargs)

@register('GetSdroutingServiceVrfInterfaceEthernetFeaturesForService')
def GetSdroutingServiceVrfInterfaceEthernetFeaturesForService(**kwargs):
    return SdwanClient().GetSdroutingServiceVrfInterfaceEthernetFeaturesForService(**kwargs)

@register('GetSdroutingServiceVrfInterfaceEthernetFeatureByFeatureIdForService')
def GetSdroutingServiceVrfInterfaceEthernetFeatureByFeatureIdForService(**kwargs):
    return SdwanClient().GetSdroutingServiceVrfInterfaceEthernetFeatureByFeatureIdForService(**kwargs)

@register('GetVrfInterfaceEthernetAssociatedDhcpServerParcelsForService')
def GetVrfInterfaceEthernetAssociatedDhcpServerParcelsForService(**kwargs):
    return SdwanClient().GetVrfInterfaceEthernetAssociatedDhcpServerParcelsForService(**kwargs)

@register('GetVrfInterfaceEthernetAssociatedDhcpServerParcelByFeatureIdForService')
def GetVrfInterfaceEthernetAssociatedDhcpServerParcelByFeatureIdForService(**kwargs):
    return SdwanClient().GetVrfInterfaceEthernetAssociatedDhcpServerParcelByFeatureIdForService(**kwargs)

@register('GetSdroutingServiceVrfInterfaceIpsecFeaturesForService')
def GetSdroutingServiceVrfInterfaceIpsecFeaturesForService(**kwargs):
    return SdwanClient().GetSdroutingServiceVrfInterfaceIpsecFeaturesForService(**kwargs)

@register('GetSdroutingServiceVrfInterfaceIpsecFeatureByFeatureIdForService')
def GetSdroutingServiceVrfInterfaceIpsecFeatureByFeatureIdForService(**kwargs):
    return SdwanClient().GetSdroutingServiceVrfInterfaceIpsecFeatureByFeatureIdForService(**kwargs)

@register('GetServiceVrfAssociatedRoutingBgpFeatures')
def GetServiceVrfAssociatedRoutingBgpFeatures(**kwargs):
    return SdwanClient().GetServiceVrfAssociatedRoutingBgpFeatures(**kwargs)

@register('GetServiceVrfAssociatedRoutingBgpParcelByParcelId')
def GetServiceVrfAssociatedRoutingBgpParcelByParcelId(**kwargs):
    return SdwanClient().GetServiceVrfAssociatedRoutingBgpParcelByParcelId(**kwargs)

@register('GetServiceVrfAssociatedRoutingEigrpFeatures')
def GetServiceVrfAssociatedRoutingEigrpFeatures(**kwargs):
    return SdwanClient().GetServiceVrfAssociatedRoutingEigrpFeatures(**kwargs)

@register('GetServiceVrfAssociatedRoutingEigrpFeatureByFeatureId')
def GetServiceVrfAssociatedRoutingEigrpFeatureByFeatureId(**kwargs):
    return SdwanClient().GetServiceVrfAssociatedRoutingEigrpFeatureByFeatureId(**kwargs)

@register('GetServiceVrfAssociatedRoutingOspfFeatures')
def GetServiceVrfAssociatedRoutingOspfFeatures(**kwargs):
    return SdwanClient().GetServiceVrfAssociatedRoutingOspfFeatures(**kwargs)

@register('GetServiceVrfAssociatedRoutingOspfFeatureById')
def GetServiceVrfAssociatedRoutingOspfFeatureById(**kwargs):
    return SdwanClient().GetServiceVrfAssociatedRoutingOspfFeatureById(**kwargs)

@register('GetServiceVrfAssociatedRoutingOspfv3Ipv4Features')
def GetServiceVrfAssociatedRoutingOspfv3Ipv4Features(**kwargs):
    return SdwanClient().GetServiceVrfAssociatedRoutingOspfv3Ipv4Features(**kwargs)

@register('GetServiceVrfAssociatedRoutingOspfv3Ipv4FeatureById')
def GetServiceVrfAssociatedRoutingOspfv3Ipv4FeatureById(**kwargs):
    return SdwanClient().GetServiceVrfAssociatedRoutingOspfv3Ipv4FeatureById(**kwargs)

@register('GetServiceVrfAssociatedRoutingOspfv3Ipv6Parcels')
def GetServiceVrfAssociatedRoutingOspfv3Ipv6Parcels(**kwargs):
    return SdwanClient().GetServiceVrfAssociatedRoutingOspfv3Ipv6Parcels(**kwargs)

@register('GetServiceVrfAssociatedRoutingOspfv3Ipv6FeatureById')
def GetServiceVrfAssociatedRoutingOspfv3Ipv6FeatureById(**kwargs):
    return SdwanClient().GetServiceVrfAssociatedRoutingOspfv3Ipv6FeatureById(**kwargs)

@register('GetSdRoutingSseFeatureProfiles')
def GetSdRoutingSseFeatureProfiles(**kwargs):
    return SdwanClient().GetSdRoutingSseFeatureProfiles(**kwargs)

@register('GetSdRoutingSseFeatureProfileByProfileId')
def GetSdRoutingSseFeatureProfileByProfileId(**kwargs):
    return SdwanClient().GetSdRoutingSseFeatureProfileByProfileId(**kwargs)

@register('GetCiscoSseFeatureForSse')
def GetCiscoSseFeatureForSse(**kwargs):
    return SdwanClient().GetCiscoSseFeatureForSse(**kwargs)

@register('GetCiscoSseFeatureByFeatureIdForSSE')
def GetCiscoSseFeatureByFeatureIdForSSE(**kwargs):
    return SdwanClient().GetCiscoSseFeatureByFeatureIdForSSE(**kwargs)

@register('GetSdroutingSystemFeatureProfiles')
def GetSdroutingSystemFeatureProfiles(**kwargs):
    return SdwanClient().GetSdroutingSystemFeatureProfiles(**kwargs)

@register('GetSdroutingSystemFeatureProfile')
def GetSdroutingSystemFeatureProfile(**kwargs):
    return SdwanClient().GetSdroutingSystemFeatureProfile(**kwargs)

@register('GetSdroutingAaaFeatures')
def GetSdroutingAaaFeatures(**kwargs):
    return SdwanClient().GetSdroutingAaaFeatures(**kwargs)

@register('GetSdroutingAaaFeature')
def GetSdroutingAaaFeature(**kwargs):
    return SdwanClient().GetSdroutingAaaFeature(**kwargs)

@register('GetSdroutingBannerFeatures')
def GetSdroutingBannerFeatures(**kwargs):
    return SdwanClient().GetSdroutingBannerFeatures(**kwargs)

@register('GetSdroutingBannerFeature')
def GetSdroutingBannerFeature(**kwargs):
    return SdwanClient().GetSdroutingBannerFeature(**kwargs)

@register('GetSdroutingCertificateFeatures')
def GetSdroutingCertificateFeatures(**kwargs):
    return SdwanClient().GetSdroutingCertificateFeatures(**kwargs)

@register('GetSdroutingCertificateFeature')
def GetSdroutingCertificateFeature(**kwargs):
    return SdwanClient().GetSdroutingCertificateFeature(**kwargs)

@register('GetSdroutingFlexiblePortSpeedFeatures')
def GetSdroutingFlexiblePortSpeedFeatures(**kwargs):
    return SdwanClient().GetSdroutingFlexiblePortSpeedFeatures(**kwargs)

@register('GetSdroutingFlexiblePortSpeedFeature')
def GetSdroutingFlexiblePortSpeedFeature(**kwargs):
    return SdwanClient().GetSdroutingFlexiblePortSpeedFeature(**kwargs)

@register('GetSdroutingGlobalSettingFeatures')
def GetSdroutingGlobalSettingFeatures(**kwargs):
    return SdwanClient().GetSdroutingGlobalSettingFeatures(**kwargs)

@register('GetSdroutingGlobalSettingFeature')
def GetSdroutingGlobalSettingFeature(**kwargs):
    return SdwanClient().GetSdroutingGlobalSettingFeature(**kwargs)

@register('GetSdroutingLoggingFeatures')
def GetSdroutingLoggingFeatures(**kwargs):
    return SdwanClient().GetSdroutingLoggingFeatures(**kwargs)

@register('GetSdroutingLoggingFeature')
def GetSdroutingLoggingFeature(**kwargs):
    return SdwanClient().GetSdroutingLoggingFeature(**kwargs)

@register('GetSdroutingNtpFeatures')
def GetSdroutingNtpFeatures(**kwargs):
    return SdwanClient().GetSdroutingNtpFeatures(**kwargs)

@register('GetSdroutingNtpFeature')
def GetSdroutingNtpFeature(**kwargs):
    return SdwanClient().GetSdroutingNtpFeature(**kwargs)

@register('GetSdroutingSnmpFeatures')
def GetSdroutingSnmpFeatures(**kwargs):
    return SdwanClient().GetSdroutingSnmpFeatures(**kwargs)

@register('GetSdroutingSnmpFeature')
def GetSdroutingSnmpFeature(**kwargs):
    return SdwanClient().GetSdroutingSnmpFeature(**kwargs)

@register('GetSdroutingTransportFeatureProfiles')
def GetSdroutingTransportFeatureProfiles(**kwargs):
    return SdwanClient().GetSdroutingTransportFeatureProfiles(**kwargs)

@register('GetSdroutingTransportFeatureProfile')
def GetSdroutingTransportFeatureProfile(**kwargs):
    return SdwanClient().GetSdroutingTransportFeatureProfile(**kwargs)

@register('GetCellularControllerProfileParcelForTransport_1')
def GetCellularControllerProfileParcelForTransport_1(**kwargs):
    return SdwanClient().GetCellularControllerProfileParcelForTransport_1(**kwargs)

@register('GetCellularControllerProfileParcelByParcelIdForTransport_1')
def GetCellularControllerProfileParcelByParcelIdForTransport_1(**kwargs):
    return SdwanClient().GetCellularControllerProfileParcelByParcelIdForTransport_1(**kwargs)

@register('GetCellularControllerAssociatedCellularProfileParcelsForTransport_1')
def GetCellularControllerAssociatedCellularProfileParcelsForTransport_1(**kwargs):
    return SdwanClient().GetCellularControllerAssociatedCellularProfileParcelsForTransport_1(**kwargs)

@register('GetCellularControllerAssociatedCellularProfileParcelByParcelIdForTransport_1')
def GetCellularControllerAssociatedCellularProfileParcelByParcelIdForTransport_1(**kwargs):
    return SdwanClient().GetCellularControllerAssociatedCellularProfileParcelByParcelIdForTransport_1(**kwargs)

@register('GetCellularControllerAssociatedGpsParcelsForTransport_1')
def GetCellularControllerAssociatedGpsParcelsForTransport_1(**kwargs):
    return SdwanClient().GetCellularControllerAssociatedGpsParcelsForTransport_1(**kwargs)

@register('GetCellularControllerAssociatedGpsParcelByParcelIdForTransport_1')
def GetCellularControllerAssociatedGpsParcelByParcelIdForTransport_1(**kwargs):
    return SdwanClient().GetCellularControllerAssociatedGpsParcelByParcelIdForTransport_1(**kwargs)

@register('GetCellularProfileParcelForTransport')
def GetCellularProfileParcelForTransport(**kwargs):
    return SdwanClient().GetCellularProfileParcelForTransport(**kwargs)

@register('GetCellularProfileParcelByParcelIdForTransport')
def GetCellularProfileParcelByParcelIdForTransport(**kwargs):
    return SdwanClient().GetCellularProfileParcelByParcelIdForTransport(**kwargs)

@register('GetSdroutingTransportGlobalVRFFeatures')
def GetSdroutingTransportGlobalVRFFeatures(**kwargs):
    return SdwanClient().GetSdroutingTransportGlobalVRFFeatures(**kwargs)

@register('GetSdroutingTransportGlobalVrfBgpFeatures')
def GetSdroutingTransportGlobalVrfBgpFeatures(**kwargs):
    return SdwanClient().GetSdroutingTransportGlobalVrfBgpFeatures(**kwargs)

@register('GetSdroutingTransportGlobalVrfBgpFeature')
def GetSdroutingTransportGlobalVrfBgpFeature(**kwargs):
    return SdwanClient().GetSdroutingTransportGlobalVrfBgpFeature(**kwargs)

@register('GetSdroutingTransportGlobalVRFFeature')
def GetSdroutingTransportGlobalVRFFeature(**kwargs):
    return SdwanClient().GetSdroutingTransportGlobalVRFFeature(**kwargs)

@register('GetGlobalVRFInterfaceCellularParcelsForTransport')
def GetGlobalVRFInterfaceCellularParcelsForTransport(**kwargs):
    return SdwanClient().GetGlobalVRFInterfaceCellularParcelsForTransport(**kwargs)

@register('GetGlobalVRFInterfaceCellularAssociatedTrackerParcelsForTransport_1')
def GetGlobalVRFInterfaceCellularAssociatedTrackerParcelsForTransport_1(**kwargs):
    return SdwanClient().GetGlobalVRFInterfaceCellularAssociatedTrackerParcelsForTransport_1(**kwargs)

@register('GetGlobalVRFInterfaceCellularAssociatedTrackerParcelByParcelIdForTransport_1')
def GetGlobalVRFInterfaceCellularAssociatedTrackerParcelByParcelIdForTransport_1(**kwargs):
    return SdwanClient().GetGlobalVRFInterfaceCellularAssociatedTrackerParcelByParcelIdForTransport_1(**kwargs)

@register('GetGlobalVRFInterfaceCellularAssociatedTrackerParcelsForTransport')
def GetGlobalVRFInterfaceCellularAssociatedTrackerParcelsForTransport(**kwargs):
    return SdwanClient().GetGlobalVRFInterfaceCellularAssociatedTrackerParcelsForTransport(**kwargs)

@register('GetGlobalVRFInterfaceCellularAssociatedTrackerParcelByParcelIdForTransport')
def GetGlobalVRFInterfaceCellularAssociatedTrackerParcelByParcelIdForTransport(**kwargs):
    return SdwanClient().GetGlobalVRFInterfaceCellularAssociatedTrackerParcelByParcelIdForTransport(**kwargs)

@register('GetGlobalVRFInterfaceCellularParcelByParcelIdForTransport')
def GetGlobalVRFInterfaceCellularParcelByParcelIdForTransport(**kwargs):
    return SdwanClient().GetGlobalVRFInterfaceCellularParcelByParcelIdForTransport(**kwargs)

@register('GetSdroutingTransportGlobalVrfInterfaceEthernetParcelsForTransport')
def GetSdroutingTransportGlobalVrfInterfaceEthernetParcelsForTransport(**kwargs):
    return SdwanClient().GetSdroutingTransportGlobalVrfInterfaceEthernetParcelsForTransport(**kwargs)

@register('GetSdroutingTransportGlobalVrfInterfaceEthernetParcelByParcelIdForTransport')
def GetSdroutingTransportGlobalVrfInterfaceEthernetParcelByParcelIdForTransport(**kwargs):
    return SdwanClient().GetSdroutingTransportGlobalVrfInterfaceEthernetParcelByParcelIdForTransport(**kwargs)

@register('GetSdroutingTransportGlobalVrfInterfaceIpsecFeaturesForTransport')
def GetSdroutingTransportGlobalVrfInterfaceIpsecFeaturesForTransport(**kwargs):
    return SdwanClient().GetSdroutingTransportGlobalVrfInterfaceIpsecFeaturesForTransport(**kwargs)

@register('GetSdroutingTransportGlobalVrfInterfaceIpsecFeatureByFeatureIdForTransport')
def GetSdroutingTransportGlobalVrfInterfaceIpsecFeatureByFeatureIdForTransport(**kwargs):
    return SdwanClient().GetSdroutingTransportGlobalVrfInterfaceIpsecFeatureByFeatureIdForTransport(**kwargs)

@register('GetTransportVrfAssociatedRoutingBgpFeatures')
def GetTransportVrfAssociatedRoutingBgpFeatures(**kwargs):
    return SdwanClient().GetTransportVrfAssociatedRoutingBgpFeatures(**kwargs)

@register('GetVrfAssociatedRoutingBgpFeatureById')
def GetVrfAssociatedRoutingBgpFeatureById(**kwargs):
    return SdwanClient().GetVrfAssociatedRoutingBgpFeatureById(**kwargs)

@register('GetTransportVrfAssociatedRoutingOspfFeatures')
def GetTransportVrfAssociatedRoutingOspfFeatures(**kwargs):
    return SdwanClient().GetTransportVrfAssociatedRoutingOspfFeatures(**kwargs)

@register('GetVrfAssociatedRoutingOspfParcelByFeatureId')
def GetVrfAssociatedRoutingOspfParcelByFeatureId(**kwargs):
    return SdwanClient().GetVrfAssociatedRoutingOspfParcelByFeatureId(**kwargs)

@register('GetTransportVrfAssociatedRoutingOspfv3Ipv4Features')
def GetTransportVrfAssociatedRoutingOspfv3Ipv4Features(**kwargs):
    return SdwanClient().GetTransportVrfAssociatedRoutingOspfv3Ipv4Features(**kwargs)

@register('GetVrfAssociatedRoutingOspfv3Ipv4FeatureById')
def GetVrfAssociatedRoutingOspfv3Ipv4FeatureById(**kwargs):
    return SdwanClient().GetVrfAssociatedRoutingOspfv3Ipv4FeatureById(**kwargs)

@register('GetTransportVrfAssociatedRoutingOspfv3Ipv6Features')
def GetTransportVrfAssociatedRoutingOspfv3Ipv6Features(**kwargs):
    return SdwanClient().GetTransportVrfAssociatedRoutingOspfv3Ipv6Features(**kwargs)

@register('GetVrfAssociatedRoutingOspfv3Ipv6FeatureById')
def GetVrfAssociatedRoutingOspfv3Ipv6FeatureById(**kwargs):
    return SdwanClient().GetVrfAssociatedRoutingOspfv3Ipv6FeatureById(**kwargs)

@register('GetGPSProfileParcelForTransport')
def GetGPSProfileParcelForTransport(**kwargs):
    return SdwanClient().GetGPSProfileParcelForTransport(**kwargs)

@register('GetGPSProfileParcelByParcelIdForTransport')
def GetGPSProfileParcelByParcelIdForTransport(**kwargs):
    return SdwanClient().GetGPSProfileParcelByParcelIdForTransport(**kwargs)

@register('GetSdroutingTransportIpv4AclFeatures')
def GetSdroutingTransportIpv4AclFeatures(**kwargs):
    return SdwanClient().GetSdroutingTransportIpv4AclFeatures(**kwargs)

@register('GetSdroutingTransportIpv4AclFeature')
def GetSdroutingTransportIpv4AclFeature(**kwargs):
    return SdwanClient().GetSdroutingTransportIpv4AclFeature(**kwargs)

@register('GetSdroutingManagementVRFFeatures')
def GetSdroutingManagementVRFFeatures(**kwargs):
    return SdwanClient().GetSdroutingManagementVRFFeatures(**kwargs)

@register('GetSdroutingManagementVRFFeature')
def GetSdroutingManagementVRFFeature(**kwargs):
    return SdwanClient().GetSdroutingManagementVRFFeature(**kwargs)

@register('GetSdroutingManagementVrfInterfaceEthernetParcelsForTransportProfile')
def GetSdroutingManagementVrfInterfaceEthernetParcelsForTransportProfile(**kwargs):
    return SdwanClient().GetSdroutingManagementVrfInterfaceEthernetParcelsForTransportProfile(**kwargs)

@register('GetSdroutingManagementVrfInterfaceEthernetParcelByParcelIdForTransportProfile')
def GetSdroutingManagementVrfInterfaceEthernetParcelByParcelIdForTransportProfile(**kwargs):
    return SdwanClient().GetSdroutingManagementVrfInterfaceEthernetParcelByParcelIdForTransportProfile(**kwargs)

@register('GetLanVpnProfileParcelForService_1')
def GetLanVpnProfileParcelForService_1(**kwargs):
    return SdwanClient().GetLanVpnProfileParcelForService_1(**kwargs)

@register('GetLanVpnProfileParcelByParcelIdForService_1')
def GetLanVpnProfileParcelByParcelIdForService_1(**kwargs):
    return SdwanClient().GetLanVpnProfileParcelByParcelIdForService_1(**kwargs)

@register('GetSdroutingTransportObjectTrackerFeatures')
def GetSdroutingTransportObjectTrackerFeatures(**kwargs):
    return SdwanClient().GetSdroutingTransportObjectTrackerFeatures(**kwargs)

@register('GetSdroutingTransportObjectTrackerFeature')
def GetSdroutingTransportObjectTrackerFeature(**kwargs):
    return SdwanClient().GetSdroutingTransportObjectTrackerFeature(**kwargs)

@register('GetSdroutingTransportObjectTrackerGroupFeatures')
def GetSdroutingTransportObjectTrackerGroupFeatures(**kwargs):
    return SdwanClient().GetSdroutingTransportObjectTrackerGroupFeatures(**kwargs)

@register('GetSdroutingTransportObjectTrackerGroupFeature')
def GetSdroutingTransportObjectTrackerGroupFeature(**kwargs):
    return SdwanClient().GetSdroutingTransportObjectTrackerGroupFeature(**kwargs)

@register('GetSdroutingTransportRoutePolicyFeatures')
def GetSdroutingTransportRoutePolicyFeatures(**kwargs):
    return SdwanClient().GetSdroutingTransportRoutePolicyFeatures(**kwargs)

@register('GetSdroutingTransportRoutePolicyFeature')
def GetSdroutingTransportRoutePolicyFeature(**kwargs):
    return SdwanClient().GetSdroutingTransportRoutePolicyFeature(**kwargs)

@register('GetSdroutingTransportRoutingOspfFeatures')
def GetSdroutingTransportRoutingOspfFeatures(**kwargs):
    return SdwanClient().GetSdroutingTransportRoutingOspfFeatures(**kwargs)

@register('GetSdroutingTransportRoutingOspfFeature')
def GetSdroutingTransportRoutingOspfFeature(**kwargs):
    return SdwanClient().GetSdroutingTransportRoutingOspfFeature(**kwargs)

@register('GetSdroutingTransportRoutingOspfv3Ipv4Features')
def GetSdroutingTransportRoutingOspfv3Ipv4Features(**kwargs):
    return SdwanClient().GetSdroutingTransportRoutingOspfv3Ipv4Features(**kwargs)

@register('GetSdroutingTransportRoutingOspfv3Ipv4Feature')
def GetSdroutingTransportRoutingOspfv3Ipv4Feature(**kwargs):
    return SdwanClient().GetSdroutingTransportRoutingOspfv3Ipv4Feature(**kwargs)

@register('GetSdroutingTransportRoutingOspfv3Ipv6Features')
def GetSdroutingTransportRoutingOspfv3Ipv6Features(**kwargs):
    return SdwanClient().GetSdroutingTransportRoutingOspfv3Ipv6Features(**kwargs)

@register('GetSdroutingTransportRoutingOspfv3Ipv6Feature')
def GetSdroutingTransportRoutingOspfv3Ipv6Feature(**kwargs):
    return SdwanClient().GetSdroutingTransportRoutingOspfv3Ipv6Feature(**kwargs)

@register('GetTrackerProfileParcelForTransport_1')
def GetTrackerProfileParcelForTransport_1(**kwargs):
    return SdwanClient().GetTrackerProfileParcelForTransport_1(**kwargs)

@register('GetTrackerProfileParcelByParcelIdForTransport_1')
def GetTrackerProfileParcelByParcelIdForTransport_1(**kwargs):
    return SdwanClient().GetTrackerProfileParcelByParcelIdForTransport_1(**kwargs)

@register('GetTrackerGroupProfileParcelForTransport_1')
def GetTrackerGroupProfileParcelForTransport_1(**kwargs):
    return SdwanClient().GetTrackerGroupProfileParcelForTransport_1(**kwargs)

@register('GetTrackerGroupProfileParcelByParcelIdForTransport_1')
def GetTrackerGroupProfileParcelByParcelIdForTransport_1(**kwargs):
    return SdwanClient().GetTrackerGroupProfileParcelByParcelIdForTransport_1(**kwargs)

@register('GetSdroutingTransportVRFFeatures')
def GetSdroutingTransportVRFFeatures(**kwargs):
    return SdwanClient().GetSdroutingTransportVRFFeatures(**kwargs)

@register('GetSdroutingTransportVrfBgpFeatures')
def GetSdroutingTransportVrfBgpFeatures(**kwargs):
    return SdwanClient().GetSdroutingTransportVrfBgpFeatures(**kwargs)

@register('GetSdroutingTransportVrfBgpFeature')
def GetSdroutingTransportVrfBgpFeature(**kwargs):
    return SdwanClient().GetSdroutingTransportVrfBgpFeature(**kwargs)

@register('GetSdroutingTransportVRFFeature')
def GetSdroutingTransportVRFFeature(**kwargs):
    return SdwanClient().GetSdroutingTransportVRFFeature(**kwargs)

@register('GetSdroutingTransportVrfInterfaceEthernetParcelsForTransport')
def GetSdroutingTransportVrfInterfaceEthernetParcelsForTransport(**kwargs):
    return SdwanClient().GetSdroutingTransportVrfInterfaceEthernetParcelsForTransport(**kwargs)

@register('GetSdroutingTransportVrfInterfaceEthernetParcelByParcelIdForTransport')
def GetSdroutingTransportVrfInterfaceEthernetParcelByParcelIdForTransport(**kwargs):
    return SdwanClient().GetSdroutingTransportVrfInterfaceEthernetParcelByParcelIdForTransport(**kwargs)

@register('GetSdroutingTransportVrfInterfaceIpsecFeaturesForTransport')
def GetSdroutingTransportVrfInterfaceIpsecFeaturesForTransport(**kwargs):
    return SdwanClient().GetSdroutingTransportVrfInterfaceIpsecFeaturesForTransport(**kwargs)

@register('GetSdroutingTransportVrfInterfaceIpsecFeatureByFeatureIdForTransport')
def GetSdroutingTransportVrfInterfaceIpsecFeatureByFeatureIdForTransport(**kwargs):
    return SdwanClient().GetSdroutingTransportVrfInterfaceIpsecFeatureByFeatureIdForTransport(**kwargs)

@register('GetTransportVrfAssociatedRoutingBgpFeatures_1')
def GetTransportVrfAssociatedRoutingBgpFeatures_1(**kwargs):
    return SdwanClient().GetTransportVrfAssociatedRoutingBgpFeatures_1(**kwargs)

@register('GetTransportVrfAssociatedRoutingBgpById')
def GetTransportVrfAssociatedRoutingBgpById(**kwargs):
    return SdwanClient().GetTransportVrfAssociatedRoutingBgpById(**kwargs)

@register('GetTransportVrfAssociatedRoutingOspfFeatures_1')
def GetTransportVrfAssociatedRoutingOspfFeatures_1(**kwargs):
    return SdwanClient().GetTransportVrfAssociatedRoutingOspfFeatures_1(**kwargs)

@register('GetVrfAssociatedRoutingOspfById')
def GetVrfAssociatedRoutingOspfById(**kwargs):
    return SdwanClient().GetVrfAssociatedRoutingOspfById(**kwargs)

@register('GetTransportVrfAssociatedRoutingOspfv3Ipv4Features_1')
def GetTransportVrfAssociatedRoutingOspfv3Ipv4Features_1(**kwargs):
    return SdwanClient().GetTransportVrfAssociatedRoutingOspfv3Ipv4Features_1(**kwargs)

@register('GetVrfAssociatedRoutingOspfv3Ipv4FeatureById_1')
def GetVrfAssociatedRoutingOspfv3Ipv4FeatureById_1(**kwargs):
    return SdwanClient().GetVrfAssociatedRoutingOspfv3Ipv4FeatureById_1(**kwargs)

@register('GetTransportVrfAssociatedRoutingOspfv3Ipv6Features_1')
def GetTransportVrfAssociatedRoutingOspfv3Ipv6Features_1(**kwargs):
    return SdwanClient().GetTransportVrfAssociatedRoutingOspfv3Ipv6Features_1(**kwargs)

@register('GetVrfAssociatedRoutingOspfv3Ipv6FeatureById_1')
def GetVrfAssociatedRoutingOspfv3Ipv6FeatureById_1(**kwargs):
    return SdwanClient().GetVrfAssociatedRoutingOspfv3Ipv6FeatureById_1(**kwargs)

@register('GetSdwanFeatureProfileBySdwanFamily')
def GetSdwanFeatureProfileBySdwanFamily(**kwargs):
    return SdwanClient().GetSdwanFeatureProfileBySdwanFamily(**kwargs)

@register('GetCloudProbeProfileParcelByParcelIdForapplication-priority')
def GetCloudProbeProfileParcelByParcelIdForapplication_priority(**kwargs):
    return SdwanClient().GetCloudProbeProfileParcelByParcelIdForapplication_priority(**kwargs)

@register('getPolicyApplicationProfileParcel')
def getPolicyApplicationProfileParcel(**kwargs):
    return SdwanClient().getPolicyApplicationProfileParcel(**kwargs)

@register('GetTrafficPolicyProfileParcelByParcelIdForapplication-priority')
def GetTrafficPolicyProfileParcelByParcelIdForapplication_priority(**kwargs):
    return SdwanClient().GetTrafficPolicyProfileParcelByParcelIdForapplication_priority(**kwargs)

@register('GetSdwanFeatureProfilesByFamilyAndType_1')
def GetSdwanFeatureProfilesByFamilyAndType_1(**kwargs):
    return SdwanClient().GetSdwanFeatureProfilesByFamilyAndType_1(**kwargs)

@register('GetSdwanCliConfigFeatureSchemaBySchemaType')
def GetSdwanCliConfigFeatureSchemaBySchemaType(**kwargs):
    return SdwanClient().GetSdwanCliConfigFeatureSchemaBySchemaType(**kwargs)

@register('GetSdwanFeatureProfilesByFamilyAndType')
def GetSdwanFeatureProfilesByFamilyAndType(**kwargs):
    return SdwanClient().GetSdwanFeatureProfilesByFamilyAndType(**kwargs)

@register('GetSdwanFeatureProfileByProfileId')
def GetSdwanFeatureProfileByProfileId(**kwargs):
    return SdwanClient().GetSdwanFeatureProfileByProfileId(**kwargs)

@register('GetConfigProfileParcelForCLI')
def GetConfigProfileParcelForCLI(**kwargs):
    return SdwanClient().GetConfigProfileParcelForCLI(**kwargs)

@register('GetConfigProfileParcelByParcelIdForCLI')
def GetConfigProfileParcelByParcelIdForCLI(**kwargs):
    return SdwanClient().GetConfigProfileParcelByParcelIdForCLI(**kwargs)

@register('GetSdwanDnsSecurityFeatureProfiles')
def GetSdwanDnsSecurityFeatureProfiles(**kwargs):
    return SdwanClient().GetSdwanDnsSecurityFeatureProfiles(**kwargs)

@register('GetSdwanDnsSecurityFeatureProfileByProfileId')
def GetSdwanDnsSecurityFeatureProfileByProfileId(**kwargs):
    return SdwanClient().GetSdwanDnsSecurityFeatureProfileByProfileId(**kwargs)

@register('GetSigSecurityProfileParcel')
def GetSigSecurityProfileParcel(**kwargs):
    return SdwanClient().GetSigSecurityProfileParcel(**kwargs)

@register('GetSigSecurityProfileParcelByParcelId')
def GetSigSecurityProfileParcelByParcelId(**kwargs):
    return SdwanClient().GetSigSecurityProfileParcelByParcelId(**kwargs)

@register('GetSdwanSecurityFeature_1')
def GetSdwanSecurityFeature_1(**kwargs):
    return SdwanClient().GetSdwanSecurityFeature_1(**kwargs)

@register('GetSdwanSecurityFeatureByFeatureId_1')
def GetSdwanSecurityFeatureByFeatureId_1(**kwargs):
    return SdwanClient().GetSdwanSecurityFeatureByFeatureId_1(**kwargs)

@register('GetSdwanNgfirewallFeature')
def GetSdwanNgfirewallFeature(**kwargs):
    return SdwanClient().GetSdwanNgfirewallFeature(**kwargs)

@register('GetSdwanNgfirewallFeatureByFeatureId')
def GetSdwanNgfirewallFeatureByFeatureId(**kwargs):
    return SdwanClient().GetSdwanNgfirewallFeatureByFeatureId(**kwargs)

@register('GetSdwanOtherFeatureProfiles')
def GetSdwanOtherFeatureProfiles(**kwargs):
    return SdwanClient().GetSdwanOtherFeatureProfiles(**kwargs)

@register('GetSdwanOtherThousandeyesParcelSchemaBySchemaType')
def GetSdwanOtherThousandeyesParcelSchemaBySchemaType(**kwargs):
    return SdwanClient().GetSdwanOtherThousandeyesParcelSchemaBySchemaType(**kwargs)

@register('GetSdwanOtherFeatureProfileByProfileId')
def GetSdwanOtherFeatureProfileByProfileId(**kwargs):
    return SdwanClient().GetSdwanOtherFeatureProfileByProfileId(**kwargs)

@register('GetThousandeyesProfileParcelForOther')
def GetThousandeyesProfileParcelForOther(**kwargs):
    return SdwanClient().GetThousandeyesProfileParcelForOther(**kwargs)

@register('GetThousandeyesProfileParcelByParcelIdForOther')
def GetThousandeyesProfileParcelByParcelIdForOther(**kwargs):
    return SdwanClient().GetThousandeyesProfileParcelByParcelIdForOther(**kwargs)

@register('GetUcseProfileFeatureForOther')
def GetUcseProfileFeatureForOther(**kwargs):
    return SdwanClient().GetUcseProfileFeatureForOther(**kwargs)

@register('GetUcseProfileFeatureByIdFFeatureForOther')
def GetUcseProfileFeatureByIdFFeatureForOther(**kwargs):
    return SdwanClient().GetUcseProfileFeatureByIdFFeatureForOther(**kwargs)

@register('GetSdwanSecurityFeature')
def GetSdwanSecurityFeature(**kwargs):
    return SdwanClient().GetSdwanSecurityFeature(**kwargs)

@register('GetSdwanSecurityFeatureByFeatureId')
def GetSdwanSecurityFeatureByFeatureId(**kwargs):
    return SdwanClient().GetSdwanSecurityFeatureByFeatureId(**kwargs)

@register('GetDataPrefixProfileParcelForPolicyObject')
def GetDataPrefixProfileParcelForPolicyObject(**kwargs):
    return SdwanClient().GetDataPrefixProfileParcelForPolicyObject(**kwargs)

@register('GetDataPrefixProfileParcelByParcelIdForPolicyObject')
def GetDataPrefixProfileParcelByParcelIdForPolicyObject(**kwargs):
    return SdwanClient().GetDataPrefixProfileParcelByParcelIdForPolicyObject(**kwargs)

@register('GetSdwanPolicyObjectDataPrefixParcelSchemaBySchemaType')
def GetSdwanPolicyObjectDataPrefixParcelSchemaBySchemaType(**kwargs):
    return SdwanClient().GetSdwanPolicyObjectDataPrefixParcelSchemaBySchemaType(**kwargs)

@register('GetSdwanServiceFeatureProfiles')
def GetSdwanServiceFeatureProfiles(**kwargs):
    return SdwanClient().GetSdwanServiceFeatureProfiles(**kwargs)

@register('GetSdwanServiceDhcpServerParcelSchemaBySchemaType')
def GetSdwanServiceDhcpServerParcelSchemaBySchemaType(**kwargs):
    return SdwanClient().GetSdwanServiceDhcpServerParcelSchemaBySchemaType(**kwargs)

@register('GetSdwanServiceLanVpnInterfaceEthernetParcelSchemaBySchema')
def GetSdwanServiceLanVpnInterfaceEthernetParcelSchemaBySchema(**kwargs):
    return SdwanClient().GetSdwanServiceLanVpnInterfaceEthernetParcelSchemaBySchema(**kwargs)

@register('GetCedgeServiceLanVpnInterfaceGreSchemaBySchema')
def GetCedgeServiceLanVpnInterfaceGreSchemaBySchema(**kwargs):
    return SdwanClient().GetCedgeServiceLanVpnInterfaceGreSchemaBySchema(**kwargs)

@register('getSdwanProfileParcelSchema')
def getSdwanProfileParcelSchema(**kwargs):
    return SdwanClient().getSdwanProfileParcelSchema(**kwargs)

@register('GetCedgeServiceLanVpnInterfaceSviParcelSchemaBySchema')
def GetCedgeServiceLanVpnInterfaceSviParcelSchemaBySchema(**kwargs):
    return SdwanClient().GetCedgeServiceLanVpnInterfaceSviParcelSchemaBySchema(**kwargs)

@register('GetSdwanServiceLanVpnParcelSchemaBySchemaType')
def GetSdwanServiceLanVpnParcelSchemaBySchemaType(**kwargs):
    return SdwanClient().GetSdwanServiceLanVpnParcelSchemaBySchemaType(**kwargs)

@register('GetSdwanServiceRoutingBgpParcelSchemaBySchemaType')
def GetSdwanServiceRoutingBgpParcelSchemaBySchemaType(**kwargs):
    return SdwanClient().GetSdwanServiceRoutingBgpParcelSchemaBySchemaType(**kwargs)

@register('GetSdwanServiceRoutingMulticastParcelSchemaBySchemaType')
def GetSdwanServiceRoutingMulticastParcelSchemaBySchemaType(**kwargs):
    return SdwanClient().GetSdwanServiceRoutingMulticastParcelSchemaBySchemaType(**kwargs)

@register('GetCedgeServiceSwitchportParcelSchemaBySchemaType')
def GetCedgeServiceSwitchportParcelSchemaBySchemaType(**kwargs):
    return SdwanClient().GetCedgeServiceSwitchportParcelSchemaBySchemaType(**kwargs)

@register('GetSdwanServiceTrackerParcelSchemaBySchemaType')
def GetSdwanServiceTrackerParcelSchemaBySchemaType(**kwargs):
    return SdwanClient().GetSdwanServiceTrackerParcelSchemaBySchemaType(**kwargs)

@register('GetCedgeServiceTrackerGroupParcelSchemaBySchemaType')
def GetCedgeServiceTrackerGroupParcelSchemaBySchemaType(**kwargs):
    return SdwanClient().GetCedgeServiceTrackerGroupParcelSchemaBySchemaType(**kwargs)

@register('GetSdwanServiceWirelesslanParcelSchemaBySchemaType')
def GetSdwanServiceWirelesslanParcelSchemaBySchemaType(**kwargs):
    return SdwanClient().GetSdwanServiceWirelesslanParcelSchemaBySchemaType(**kwargs)

@register('GetSdwanServiceFeatureProfileByProfileId')
def GetSdwanServiceFeatureProfileByProfileId(**kwargs):
    return SdwanClient().GetSdwanServiceFeatureProfileByProfileId(**kwargs)

@register('GetAppqoeProfileParcelForService')
def GetAppqoeProfileParcelForService(**kwargs):
    return SdwanClient().GetAppqoeProfileParcelForService(**kwargs)

@register('GetAppqoeProfileParcelByParcelIdForService')
def GetAppqoeProfileParcelByParcelIdForService(**kwargs):
    return SdwanClient().GetAppqoeProfileParcelByParcelIdForService(**kwargs)

@register('GetDhcpServerProfileParcelForService')
def GetDhcpServerProfileParcelForService(**kwargs):
    return SdwanClient().GetDhcpServerProfileParcelForService(**kwargs)

@register('GetDhcpServerProfileParcelByParcelIdForService')
def GetDhcpServerProfileParcelByParcelIdForService(**kwargs):
    return SdwanClient().GetDhcpServerProfileParcelByParcelIdForService(**kwargs)

@register('GetLanVpnProfileParcelForService')
def GetLanVpnProfileParcelForService(**kwargs):
    return SdwanClient().GetLanVpnProfileParcelForService(**kwargs)

@register('GetLanVpnProfileParcelByParcelIdForService')
def GetLanVpnProfileParcelByParcelIdForService(**kwargs):
    return SdwanClient().GetLanVpnProfileParcelByParcelIdForService(**kwargs)

@register('GetInterfaceEthernetParcelsForServiceLanVpn')
def GetInterfaceEthernetParcelsForServiceLanVpn(**kwargs):
    return SdwanClient().GetInterfaceEthernetParcelsForServiceLanVpn(**kwargs)

@register('GetLanVpnInterfaceEthernetParcelByParcelIdForService')
def GetLanVpnInterfaceEthernetParcelByParcelIdForService(**kwargs):
    return SdwanClient().GetLanVpnInterfaceEthernetParcelByParcelIdForService(**kwargs)

@register('GetLanVpnInterfaceEthernetAssociatedDhcpServerParcelsForTransport')
def GetLanVpnInterfaceEthernetAssociatedDhcpServerParcelsForTransport(**kwargs):
    return SdwanClient().GetLanVpnInterfaceEthernetAssociatedDhcpServerParcelsForTransport(**kwargs)

@register('GetLanVpnInterfaceEthernetAssociatedDhcpServerParcelByParcelIdForTransport')
def GetLanVpnInterfaceEthernetAssociatedDhcpServerParcelByParcelIdForTransport(**kwargs):
    return SdwanClient().GetLanVpnInterfaceEthernetAssociatedDhcpServerParcelByParcelIdForTransport(**kwargs)

@register('GetLanVpnInterfaceEthernetAssociatedTrackerParcelsForTransport')
def GetLanVpnInterfaceEthernetAssociatedTrackerParcelsForTransport(**kwargs):
    return SdwanClient().GetLanVpnInterfaceEthernetAssociatedTrackerParcelsForTransport(**kwargs)

@register('GetLanVpnInterfaceEthernetAssociatedTrackerParcelByParcelIdForTransport')
def GetLanVpnInterfaceEthernetAssociatedTrackerParcelByParcelIdForTransport(**kwargs):
    return SdwanClient().GetLanVpnInterfaceEthernetAssociatedTrackerParcelByParcelIdForTransport(**kwargs)

@register('GetLanVpnInterfaceEthernetAssociatedTrackerGroupParcelsForTransport')
def GetLanVpnInterfaceEthernetAssociatedTrackerGroupParcelsForTransport(**kwargs):
    return SdwanClient().GetLanVpnInterfaceEthernetAssociatedTrackerGroupParcelsForTransport(**kwargs)

@register('GetLanVpnInterfaceEthernetAssociatedTrackerGroupParcelByParcelIdForTransport')
def GetLanVpnInterfaceEthernetAssociatedTrackerGroupParcelByParcelIdForTransport(**kwargs):
    return SdwanClient().GetLanVpnInterfaceEthernetAssociatedTrackerGroupParcelByParcelIdForTransport(**kwargs)

@register('GetInterfaceGresForServiceLanVpn')
def GetInterfaceGresForServiceLanVpn(**kwargs):
    return SdwanClient().GetInterfaceGresForServiceLanVpn(**kwargs)

@register('GetLanVpnInterfaceGreByIdForService')
def GetLanVpnInterfaceGreByIdForService(**kwargs):
    return SdwanClient().GetLanVpnInterfaceGreByIdForService(**kwargs)

@register('getListOfProfileParcels')
def getListOfProfileParcels(**kwargs):
    return SdwanClient().getListOfProfileParcels(**kwargs)

@register('getProfileParcelByParcelId')
def getProfileParcelByParcelId(**kwargs):
    return SdwanClient().getProfileParcelByParcelId(**kwargs)

@register('GetLanVpnInterfaceIpsecAssociatedDhcpServerParcelsForTransport')
def GetLanVpnInterfaceIpsecAssociatedDhcpServerParcelsForTransport(**kwargs):
    return SdwanClient().GetLanVpnInterfaceIpsecAssociatedDhcpServerParcelsForTransport(**kwargs)

@register('GetLanVpnInterfaceIpsecAssociatedDhcpServerParcelByParcelIdForTransport')
def GetLanVpnInterfaceIpsecAssociatedDhcpServerParcelByParcelIdForTransport(**kwargs):
    return SdwanClient().GetLanVpnInterfaceIpsecAssociatedDhcpServerParcelByParcelIdForTransport(**kwargs)

@register('GetInterfaceSviParcelsForServiceLanVpn')
def GetInterfaceSviParcelsForServiceLanVpn(**kwargs):
    return SdwanClient().GetInterfaceSviParcelsForServiceLanVpn(**kwargs)

@register('GetLanVpnInterfaceSviParcelByParcelIdForService')
def GetLanVpnInterfaceSviParcelByParcelIdForService(**kwargs):
    return SdwanClient().GetLanVpnInterfaceSviParcelByParcelIdForService(**kwargs)

@register('GetLanVpnInterfaceSviAssociatedDhcpServerParcelsForTransport')
def GetLanVpnInterfaceSviAssociatedDhcpServerParcelsForTransport(**kwargs):
    return SdwanClient().GetLanVpnInterfaceSviAssociatedDhcpServerParcelsForTransport(**kwargs)

@register('GetLanVpnInterfaceSviAssociatedDhcpServerParcelByParcelIdForTransport')
def GetLanVpnInterfaceSviAssociatedDhcpServerParcelByParcelIdForTransport(**kwargs):
    return SdwanClient().GetLanVpnInterfaceSviAssociatedDhcpServerParcelByParcelIdForTransport(**kwargs)

@register('GetLanVpnAssociatedRoutingBgpParcelsForService')
def GetLanVpnAssociatedRoutingBgpParcelsForService(**kwargs):
    return SdwanClient().GetLanVpnAssociatedRoutingBgpParcelsForService(**kwargs)

@register('GetLanVpnAssociatedRoutingBgpParcelByParcelIdForService')
def GetLanVpnAssociatedRoutingBgpParcelByParcelIdForService(**kwargs):
    return SdwanClient().GetLanVpnAssociatedRoutingBgpParcelByParcelIdForService(**kwargs)

@register('GetLanVpnAssociatedRoutingEigrpParcelsForService')
def GetLanVpnAssociatedRoutingEigrpParcelsForService(**kwargs):
    return SdwanClient().GetLanVpnAssociatedRoutingEigrpParcelsForService(**kwargs)

@register('GetLanVpnAssociatedRoutingEigrpParcelByParcelIdForService')
def GetLanVpnAssociatedRoutingEigrpParcelByParcelIdForService(**kwargs):
    return SdwanClient().GetLanVpnAssociatedRoutingEigrpParcelByParcelIdForService(**kwargs)

@register('GetLanVpnAssociatedRoutingMulticastParcelsForService')
def GetLanVpnAssociatedRoutingMulticastParcelsForService(**kwargs):
    return SdwanClient().GetLanVpnAssociatedRoutingMulticastParcelsForService(**kwargs)

@register('GetLanVpnAssociatedRoutingMulticastParcelByParcelIdForService')
def GetLanVpnAssociatedRoutingMulticastParcelByParcelIdForService(**kwargs):
    return SdwanClient().GetLanVpnAssociatedRoutingMulticastParcelByParcelIdForService(**kwargs)

@register('GetLanVpnAssociatedRoutingOspfParcelsForService')
def GetLanVpnAssociatedRoutingOspfParcelsForService(**kwargs):
    return SdwanClient().GetLanVpnAssociatedRoutingOspfParcelsForService(**kwargs)

@register('GetLanVpnAssociatedRoutingOspfParcelByParcelIdForService')
def GetLanVpnAssociatedRoutingOspfParcelByParcelIdForService(**kwargs):
    return SdwanClient().GetLanVpnAssociatedRoutingOspfParcelByParcelIdForService(**kwargs)

@register('GetLanVpnAssociatedRoutingOspfv3IPv4ParcelsForService')
def GetLanVpnAssociatedRoutingOspfv3IPv4ParcelsForService(**kwargs):
    return SdwanClient().GetLanVpnAssociatedRoutingOspfv3IPv4ParcelsForService(**kwargs)

@register('GetLanVpnAssociatedRoutingOspfv3IPv4ParcelByParcelIdForService')
def GetLanVpnAssociatedRoutingOspfv3IPv4ParcelByParcelIdForService(**kwargs):
    return SdwanClient().GetLanVpnAssociatedRoutingOspfv3IPv4ParcelByParcelIdForService(**kwargs)

@register('GetLanVpnAssociatedRoutingOspfv3IPv6ParcelsForService')
def GetLanVpnAssociatedRoutingOspfv3IPv6ParcelsForService(**kwargs):
    return SdwanClient().GetLanVpnAssociatedRoutingOspfv3IPv6ParcelsForService(**kwargs)

@register('GetLanVpnAssociatedRoutingOspfv3IPv6ParcelByParcelIdForService')
def GetLanVpnAssociatedRoutingOspfv3IPv6ParcelByParcelIdForService(**kwargs):
    return SdwanClient().GetLanVpnAssociatedRoutingOspfv3IPv6ParcelByParcelIdForService(**kwargs)

@register('GetRoutingBgpProfileParcelForService')
def GetRoutingBgpProfileParcelForService(**kwargs):
    return SdwanClient().GetRoutingBgpProfileParcelForService(**kwargs)

@register('GetRoutingBgpProfileParcelByParcelIdForService')
def GetRoutingBgpProfileParcelByParcelIdForService(**kwargs):
    return SdwanClient().GetRoutingBgpProfileParcelByParcelIdForService(**kwargs)

@register('GetRoutingEigrpProfileParcelForService')
def GetRoutingEigrpProfileParcelForService(**kwargs):
    return SdwanClient().GetRoutingEigrpProfileParcelForService(**kwargs)

@register('GetRoutingEigrpProfileParcelByParcelIdForService')
def GetRoutingEigrpProfileParcelByParcelIdForService(**kwargs):
    return SdwanClient().GetRoutingEigrpProfileParcelByParcelIdForService(**kwargs)

@register('GetRoutingMulticastProfileParcelForService')
def GetRoutingMulticastProfileParcelForService(**kwargs):
    return SdwanClient().GetRoutingMulticastProfileParcelForService(**kwargs)

@register('GetRoutingMulticastProfileParcelByParcelIdForService')
def GetRoutingMulticastProfileParcelByParcelIdForService(**kwargs):
    return SdwanClient().GetRoutingMulticastProfileParcelByParcelIdForService(**kwargs)

@register('GetRoutingOspfProfileParcelForService')
def GetRoutingOspfProfileParcelForService(**kwargs):
    return SdwanClient().GetRoutingOspfProfileParcelForService(**kwargs)

@register('GetRoutingOspfProfileParcelByParcelIdForService')
def GetRoutingOspfProfileParcelByParcelIdForService(**kwargs):
    return SdwanClient().GetRoutingOspfProfileParcelByParcelIdForService(**kwargs)

@register('GetRoutingOspfv3Ipv4AfProfileParcelForService')
def GetRoutingOspfv3Ipv4AfProfileParcelForService(**kwargs):
    return SdwanClient().GetRoutingOspfv3Ipv4AfProfileParcelForService(**kwargs)

@register('GetRoutingOspfv3IPv4AfProfileParcelByParcelIdForService')
def GetRoutingOspfv3IPv4AfProfileParcelByParcelIdForService(**kwargs):
    return SdwanClient().GetRoutingOspfv3IPv4AfProfileParcelByParcelIdForService(**kwargs)

@register('GetRoutingOspfv3Ipv6AfProfileParcelForService')
def GetRoutingOspfv3Ipv6AfProfileParcelForService(**kwargs):
    return SdwanClient().GetRoutingOspfv3Ipv6AfProfileParcelForService(**kwargs)

@register('GetRoutingOspfv3IPv6AfProfileParcelByParcelIdForService')
def GetRoutingOspfv3IPv6AfProfileParcelByParcelIdForService(**kwargs):
    return SdwanClient().GetRoutingOspfv3IPv6AfProfileParcelByParcelIdForService(**kwargs)

@register('GetSwitchportParcelsForService')
def GetSwitchportParcelsForService(**kwargs):
    return SdwanClient().GetSwitchportParcelsForService(**kwargs)

@register('GetSwitchportParcelByParcelIdForService')
def GetSwitchportParcelByParcelIdForService(**kwargs):
    return SdwanClient().GetSwitchportParcelByParcelIdForService(**kwargs)

@register('GetTrackerProfileParcelForService')
def GetTrackerProfileParcelForService(**kwargs):
    return SdwanClient().GetTrackerProfileParcelForService(**kwargs)

@register('GetTrackerProfileParcelByParcelIdForService')
def GetTrackerProfileParcelByParcelIdForService(**kwargs):
    return SdwanClient().GetTrackerProfileParcelByParcelIdForService(**kwargs)

@register('GetTrackerGroupProfileParcelForService')
def GetTrackerGroupProfileParcelForService(**kwargs):
    return SdwanClient().GetTrackerGroupProfileParcelForService(**kwargs)

@register('GetTrackerGroupProfileParcelByParcelIdForService')
def GetTrackerGroupProfileParcelByParcelIdForService(**kwargs):
    return SdwanClient().GetTrackerGroupProfileParcelByParcelIdForService(**kwargs)

@register('GetWirelesslanProfileParcelForService')
def GetWirelesslanProfileParcelForService(**kwargs):
    return SdwanClient().GetWirelesslanProfileParcelForService(**kwargs)

@register('GetWirelesslanProfileParcelByParcelIdForService')
def GetWirelesslanProfileParcelByParcelIdForService(**kwargs):
    return SdwanClient().GetWirelesslanProfileParcelByParcelIdForService(**kwargs)

@register('GetSdwanSigSecurityFeatureProfiles')
def GetSdwanSigSecurityFeatureProfiles(**kwargs):
    return SdwanClient().GetSdwanSigSecurityFeatureProfiles(**kwargs)

@register('GetSdwanSigSecurityFeatureProfileByProfileId')
def GetSdwanSigSecurityFeatureProfileByProfileId(**kwargs):
    return SdwanClient().GetSdwanSigSecurityFeatureProfileByProfileId(**kwargs)

@register('GetSigSecurityProfileParcel_1')
def GetSigSecurityProfileParcel_1(**kwargs):
    return SdwanClient().GetSigSecurityProfileParcel_1(**kwargs)

@register('GetSigSecurityProfileParcelByParcelId_1')
def GetSigSecurityProfileParcelByParcelId_1(**kwargs):
    return SdwanClient().GetSigSecurityProfileParcelByParcelId_1(**kwargs)

@register('GetSdwanSystemFeatureProfiles')
def GetSdwanSystemFeatureProfiles(**kwargs):
    return SdwanClient().GetSdwanSystemFeatureProfiles(**kwargs)

@register('GetSdwanSystemAaaParcelSchemaBySchemaType')
def GetSdwanSystemAaaParcelSchemaBySchemaType(**kwargs):
    return SdwanClient().GetSdwanSystemAaaParcelSchemaBySchemaType(**kwargs)

@register('GetSdwanSystemBannerParcelSchemaBySchemaType')
def GetSdwanSystemBannerParcelSchemaBySchemaType(**kwargs):
    return SdwanClient().GetSdwanSystemBannerParcelSchemaBySchemaType(**kwargs)

@register('GetSdwanSystemBasicFeatureSchemaBySchemaType')
def GetSdwanSystemBasicFeatureSchemaBySchemaType(**kwargs):
    return SdwanClient().GetSdwanSystemBasicFeatureSchemaBySchemaType(**kwargs)

@register('GetSdwanSystemBfdParcelSchemaBySchemaType')
def GetSdwanSystemBfdParcelSchemaBySchemaType(**kwargs):
    return SdwanClient().GetSdwanSystemBfdParcelSchemaBySchemaType(**kwargs)

@register('GetCedgeSystemGlobalParcelSchemaBySchemaType')
def GetCedgeSystemGlobalParcelSchemaBySchemaType(**kwargs):
    return SdwanClient().GetCedgeSystemGlobalParcelSchemaBySchemaType(**kwargs)

@register('GetSdwanSystemLoggingParcelSchemaBySchemaType')
def GetSdwanSystemLoggingParcelSchemaBySchemaType(**kwargs):
    return SdwanClient().GetSdwanSystemLoggingParcelSchemaBySchemaType(**kwargs)

@register('GetCedgeSystemMrfParcelSchemaBySchemaType')
def GetCedgeSystemMrfParcelSchemaBySchemaType(**kwargs):
    return SdwanClient().GetCedgeSystemMrfParcelSchemaBySchemaType(**kwargs)

@register('GetSdwanSystemNtpParcelSchemaBySchemaType')
def GetSdwanSystemNtpParcelSchemaBySchemaType(**kwargs):
    return SdwanClient().GetSdwanSystemNtpParcelSchemaBySchemaType(**kwargs)

@register('GetSdwanSystemOmpParcelSchemaBySchemaType')
def GetSdwanSystemOmpParcelSchemaBySchemaType(**kwargs):
    return SdwanClient().GetSdwanSystemOmpParcelSchemaBySchemaType(**kwargs)

@register('GetSdwanSystemSnmpParcelSchemaBySchemaType')
def GetSdwanSystemSnmpParcelSchemaBySchemaType(**kwargs):
    return SdwanClient().GetSdwanSystemSnmpParcelSchemaBySchemaType(**kwargs)

@register('GetSdwanSystemFeatureProfileByProfileId')
def GetSdwanSystemFeatureProfileByProfileId(**kwargs):
    return SdwanClient().GetSdwanSystemFeatureProfileByProfileId(**kwargs)

@register('GetAaaProfileParcelForSystem')
def GetAaaProfileParcelForSystem(**kwargs):
    return SdwanClient().GetAaaProfileParcelForSystem(**kwargs)

@register('GetAaaProfileParcelByParcelIdForSystem')
def GetAaaProfileParcelByParcelIdForSystem(**kwargs):
    return SdwanClient().GetAaaProfileParcelByParcelIdForSystem(**kwargs)

@register('GetBannerProfileParcelForSystem')
def GetBannerProfileParcelForSystem(**kwargs):
    return SdwanClient().GetBannerProfileParcelForSystem(**kwargs)

@register('GetBannerProfileParcelByParcelIdForSystem')
def GetBannerProfileParcelByParcelIdForSystem(**kwargs):
    return SdwanClient().GetBannerProfileParcelByParcelIdForSystem(**kwargs)

@register('GetBasicProfileFeatureForSystem')
def GetBasicProfileFeatureForSystem(**kwargs):
    return SdwanClient().GetBasicProfileFeatureForSystem(**kwargs)

@register('GetBasicProfileFeatureByFeatureIdForSystem')
def GetBasicProfileFeatureByFeatureIdForSystem(**kwargs):
    return SdwanClient().GetBasicProfileFeatureByFeatureIdForSystem(**kwargs)

@register('GetBfdProfileParcelForSystem')
def GetBfdProfileParcelForSystem(**kwargs):
    return SdwanClient().GetBfdProfileParcelForSystem(**kwargs)

@register('GetBfdProfileParcelByParcelIdForSystem')
def GetBfdProfileParcelByParcelIdForSystem(**kwargs):
    return SdwanClient().GetBfdProfileParcelByParcelIdForSystem(**kwargs)

@register('GetGlobalProfileParcelForSystem')
def GetGlobalProfileParcelForSystem(**kwargs):
    return SdwanClient().GetGlobalProfileParcelForSystem(**kwargs)

@register('GetGlobalProfileParcelByParcelIdForSystem')
def GetGlobalProfileParcelByParcelIdForSystem(**kwargs):
    return SdwanClient().GetGlobalProfileParcelByParcelIdForSystem(**kwargs)

@register('GetLoggingProfileParcelForSystem')
def GetLoggingProfileParcelForSystem(**kwargs):
    return SdwanClient().GetLoggingProfileParcelForSystem(**kwargs)

@register('GetLoggingProfileParcelByParcelIdForSystem')
def GetLoggingProfileParcelByParcelIdForSystem(**kwargs):
    return SdwanClient().GetLoggingProfileParcelByParcelIdForSystem(**kwargs)

@register('GetMrfProfileParcelForSystem')
def GetMrfProfileParcelForSystem(**kwargs):
    return SdwanClient().GetMrfProfileParcelForSystem(**kwargs)

@register('GetMrfProfileParcelByParcelIdForSystem')
def GetMrfProfileParcelByParcelIdForSystem(**kwargs):
    return SdwanClient().GetMrfProfileParcelByParcelIdForSystem(**kwargs)

@register('GetNtpProfileParcelForSystem')
def GetNtpProfileParcelForSystem(**kwargs):
    return SdwanClient().GetNtpProfileParcelForSystem(**kwargs)

@register('GetNtpProfileParcelByParcelIdForSystem')
def GetNtpProfileParcelByParcelIdForSystem(**kwargs):
    return SdwanClient().GetNtpProfileParcelByParcelIdForSystem(**kwargs)

@register('GetOmpProfileParcelForSystem')
def GetOmpProfileParcelForSystem(**kwargs):
    return SdwanClient().GetOmpProfileParcelForSystem(**kwargs)

@register('GetOmpProfileParcelByParcelIdForSystem')
def GetOmpProfileParcelByParcelIdForSystem(**kwargs):
    return SdwanClient().GetOmpProfileParcelByParcelIdForSystem(**kwargs)

@register('GetSecurityForSystem')
def GetSecurityForSystem(**kwargs):
    return SdwanClient().GetSecurityForSystem(**kwargs)

@register('GetSecurityBySecurityIdForSystem')
def GetSecurityBySecurityIdForSystem(**kwargs):
    return SdwanClient().GetSecurityBySecurityIdForSystem(**kwargs)

@register('GetSnmpProfileParcelForSystem')
def GetSnmpProfileParcelForSystem(**kwargs):
    return SdwanClient().GetSnmpProfileParcelForSystem(**kwargs)

@register('GetSnmpProfileParcelByParcelIdForSystem')
def GetSnmpProfileParcelByParcelIdForSystem(**kwargs):
    return SdwanClient().GetSnmpProfileParcelByParcelIdForSystem(**kwargs)

@register('GetSdwanTransportFeatureProfiles')
def GetSdwanTransportFeatureProfiles(**kwargs):
    return SdwanClient().GetSdwanTransportFeatureProfiles(**kwargs)

@register('GetSdwanTransportCellularControllerParcelSchemaBySchemaType')
def GetSdwanTransportCellularControllerParcelSchemaBySchemaType(**kwargs):
    return SdwanClient().GetSdwanTransportCellularControllerParcelSchemaBySchemaType(**kwargs)

@register('GetSdwanTransportCellularProfileParcelSchemaBySchemaType')
def GetSdwanTransportCellularProfileParcelSchemaBySchemaType(**kwargs):
    return SdwanClient().GetSdwanTransportCellularProfileParcelSchemaBySchemaType(**kwargs)

@register('GetSdwanTransportIpv6TrackerParcelSchemaBySchemaType')
def GetSdwanTransportIpv6TrackerParcelSchemaBySchemaType(**kwargs):
    return SdwanClient().GetSdwanTransportIpv6TrackerParcelSchemaBySchemaType(**kwargs)

@register('GetCedgeTransportIpv6TrackerGroupParcelSchemaBySchemaType')
def GetCedgeTransportIpv6TrackerGroupParcelSchemaBySchemaType(**kwargs):
    return SdwanClient().GetCedgeTransportIpv6TrackerGroupParcelSchemaBySchemaType(**kwargs)

@register('GetSdwanTransportManagementVpnInterfaceEthernetParcelSchemaBySchema')
def GetSdwanTransportManagementVpnInterfaceEthernetParcelSchemaBySchema(**kwargs):
    return SdwanClient().GetSdwanTransportManagementVpnInterfaceEthernetParcelSchemaBySchema(**kwargs)

@register('GetSdwanTransportManagementVpnParcelSchemaBySchemaType')
def GetSdwanTransportManagementVpnParcelSchemaBySchemaType(**kwargs):
    return SdwanClient().GetSdwanTransportManagementVpnParcelSchemaBySchemaType(**kwargs)

@register('GetSdwanTransportRoutingBgpParcelSchemaBySchemaType')
def GetSdwanTransportRoutingBgpParcelSchemaBySchemaType(**kwargs):
    return SdwanClient().GetSdwanTransportRoutingBgpParcelSchemaBySchemaType(**kwargs)

@register('GetCedgeTransportT1e1controllerParcelSchemaBySchemaType')
def GetCedgeTransportT1e1controllerParcelSchemaBySchemaType(**kwargs):
    return SdwanClient().GetCedgeTransportT1e1controllerParcelSchemaBySchemaType(**kwargs)

@register('GetSdwanTransportTrackerParcelSchemaBySchemaType')
def GetSdwanTransportTrackerParcelSchemaBySchemaType(**kwargs):
    return SdwanClient().GetSdwanTransportTrackerParcelSchemaBySchemaType(**kwargs)

@register('GetCedgeTransportTrackerGroupParcelSchemaBySchemaType')
def GetCedgeTransportTrackerGroupParcelSchemaBySchemaType(**kwargs):
    return SdwanClient().GetCedgeTransportTrackerGroupParcelSchemaBySchemaType(**kwargs)

@register('GetSdwanTransportWanVpnCellularInterfaceParcelSchemaBySchema')
def GetSdwanTransportWanVpnCellularInterfaceParcelSchemaBySchema(**kwargs):
    return SdwanClient().GetSdwanTransportWanVpnCellularInterfaceParcelSchemaBySchema(**kwargs)

@register('GetSdwanTransportWanVpnInterfaceEthernetParcelSchemaBySchema')
def GetSdwanTransportWanVpnInterfaceEthernetParcelSchemaBySchema(**kwargs):
    return SdwanClient().GetSdwanTransportWanVpnInterfaceEthernetParcelSchemaBySchema(**kwargs)

@register('GetCedgeTransportWanVpnInterfaceGreParcelSchemaBySchema')
def GetCedgeTransportWanVpnInterfaceGreParcelSchemaBySchema(**kwargs):
    return SdwanClient().GetCedgeTransportWanVpnInterfaceGreParcelSchemaBySchema(**kwargs)

@register('getSdwanProfileParcelSchema_1')
def getSdwanProfileParcelSchema_1(**kwargs):
    return SdwanClient().getSdwanProfileParcelSchema_1(**kwargs)

@register('GetCedgeTransportWanVpnInterfaceSerialParcelSchemaBySchema')
def GetCedgeTransportWanVpnInterfaceSerialParcelSchemaBySchema(**kwargs):
    return SdwanClient().GetCedgeTransportWanVpnInterfaceSerialParcelSchemaBySchema(**kwargs)

@register('GetSdwanTransportWanVpnParcelSchemaBySchemaType')
def GetSdwanTransportWanVpnParcelSchemaBySchemaType(**kwargs):
    return SdwanClient().GetSdwanTransportWanVpnParcelSchemaBySchemaType(**kwargs)

@register('GetSdwanTransportFeatureProfileByProfileId')
def GetSdwanTransportFeatureProfileByProfileId(**kwargs):
    return SdwanClient().GetSdwanTransportFeatureProfileByProfileId(**kwargs)

@register('GetCellularControllerProfileParcelForTransport')
def GetCellularControllerProfileParcelForTransport(**kwargs):
    return SdwanClient().GetCellularControllerProfileParcelForTransport(**kwargs)

@register('GetCellularControllerProfileParcelByParcelIdForTransport')
def GetCellularControllerProfileParcelByParcelIdForTransport(**kwargs):
    return SdwanClient().GetCellularControllerProfileParcelByParcelIdForTransport(**kwargs)

@register('GetCellularControllerAssociatedCellularProfileParcelsForTransport')
def GetCellularControllerAssociatedCellularProfileParcelsForTransport(**kwargs):
    return SdwanClient().GetCellularControllerAssociatedCellularProfileParcelsForTransport(**kwargs)

@register('GetCellularControllerAssociatedCellularProfileParcelByParcelIdForTransport')
def GetCellularControllerAssociatedCellularProfileParcelByParcelIdForTransport(**kwargs):
    return SdwanClient().GetCellularControllerAssociatedCellularProfileParcelByParcelIdForTransport(**kwargs)

@register('GetCellularControllerAssociatedGpsParcelsForTransport')
def GetCellularControllerAssociatedGpsParcelsForTransport(**kwargs):
    return SdwanClient().GetCellularControllerAssociatedGpsParcelsForTransport(**kwargs)

@register('GetCellularControllerAssociatedGpsParcelByParcelIdForTransport')
def GetCellularControllerAssociatedGpsParcelByParcelIdForTransport(**kwargs):
    return SdwanClient().GetCellularControllerAssociatedGpsParcelByParcelIdForTransport(**kwargs)

@register('GetCellularProfileProfileParcelForTransport')
def GetCellularProfileProfileParcelForTransport(**kwargs):
    return SdwanClient().GetCellularProfileProfileParcelForTransport(**kwargs)

@register('GetCellularProfileProfileParcelByParcelIdForTransport')
def GetCellularProfileProfileParcelByParcelIdForTransport(**kwargs):
    return SdwanClient().GetCellularProfileProfileParcelByParcelIdForTransport(**kwargs)

@register('GetEsimCellularControllerProfileFeatureForTransport')
def GetEsimCellularControllerProfileFeatureForTransport(**kwargs):
    return SdwanClient().GetEsimCellularControllerProfileFeatureForTransport(**kwargs)

@register('GetEsimCellularControllerProfileFeatureByFeatureIdForTransport')
def GetEsimCellularControllerProfileFeatureByFeatureIdForTransport(**kwargs):
    return SdwanClient().GetEsimCellularControllerProfileFeatureByFeatureIdForTransport(**kwargs)

@register('GetEsimCellularProfileProfileFeatureForTransport')
def GetEsimCellularProfileProfileFeatureForTransport(**kwargs):
    return SdwanClient().GetEsimCellularProfileProfileFeatureForTransport(**kwargs)

@register('GetEsimCellularProfileByFeatureIdForTransport')
def GetEsimCellularProfileByFeatureIdForTransport(**kwargs):
    return SdwanClient().GetEsimCellularProfileByFeatureIdForTransport(**kwargs)

@register('GetGpsProfileParcelForTransport')
def GetGpsProfileParcelForTransport(**kwargs):
    return SdwanClient().GetGpsProfileParcelForTransport(**kwargs)

@register('GetGpsProfileParcelByParcelIdForTransport')
def GetGpsProfileParcelByParcelIdForTransport(**kwargs):
    return SdwanClient().GetGpsProfileParcelByParcelIdForTransport(**kwargs)

@register('GetIpv6TrackerProfileParcelForTransport')
def GetIpv6TrackerProfileParcelForTransport(**kwargs):
    return SdwanClient().GetIpv6TrackerProfileParcelForTransport(**kwargs)

@register('GetIpv6TrackerProfileParcelByParcelIdForTransport')
def GetIpv6TrackerProfileParcelByParcelIdForTransport(**kwargs):
    return SdwanClient().GetIpv6TrackerProfileParcelByParcelIdForTransport(**kwargs)

@register('GetIpv6TrackerGroupProfileParcelForTransport')
def GetIpv6TrackerGroupProfileParcelForTransport(**kwargs):
    return SdwanClient().GetIpv6TrackerGroupProfileParcelForTransport(**kwargs)

@register('GetIpv6TrackerGroupProfileParcelByParcelIdForTransport')
def GetIpv6TrackerGroupProfileParcelByParcelIdForTransport(**kwargs):
    return SdwanClient().GetIpv6TrackerGroupProfileParcelByParcelIdForTransport(**kwargs)

@register('GetManagementVpnProfileParcelForTransport')
def GetManagementVpnProfileParcelForTransport(**kwargs):
    return SdwanClient().GetManagementVpnProfileParcelForTransport(**kwargs)

@register('GetManagementVpnProfileParcelByParcelIdForTransport')
def GetManagementVpnProfileParcelByParcelIdForTransport(**kwargs):
    return SdwanClient().GetManagementVpnProfileParcelByParcelIdForTransport(**kwargs)

@register('GetInterfaceEthernetParcelsForTransportManagementVpn')
def GetInterfaceEthernetParcelsForTransportManagementVpn(**kwargs):
    return SdwanClient().GetInterfaceEthernetParcelsForTransportManagementVpn(**kwargs)

@register('GetManagementVpnInterfaceEthernetParcelByParcelIdForTransport')
def GetManagementVpnInterfaceEthernetParcelByParcelIdForTransport(**kwargs):
    return SdwanClient().GetManagementVpnInterfaceEthernetParcelByParcelIdForTransport(**kwargs)

@register('GetRoutingBgpProfileParcelForTransport')
def GetRoutingBgpProfileParcelForTransport(**kwargs):
    return SdwanClient().GetRoutingBgpProfileParcelForTransport(**kwargs)

@register('GetRoutingBgpProfileParcelByParcelIdForTransport')
def GetRoutingBgpProfileParcelByParcelIdForTransport(**kwargs):
    return SdwanClient().GetRoutingBgpProfileParcelByParcelIdForTransport(**kwargs)

@register('GetRoutingOspfProfileParcelForTransport')
def GetRoutingOspfProfileParcelForTransport(**kwargs):
    return SdwanClient().GetRoutingOspfProfileParcelForTransport(**kwargs)

@register('GetRoutingOspfProfileParcelByParcelIdForTransport')
def GetRoutingOspfProfileParcelByParcelIdForTransport(**kwargs):
    return SdwanClient().GetRoutingOspfProfileParcelByParcelIdForTransport(**kwargs)

@register('GetRoutingOspfv3Ipv4AfProfileParcelForTransport')
def GetRoutingOspfv3Ipv4AfProfileParcelForTransport(**kwargs):
    return SdwanClient().GetRoutingOspfv3Ipv4AfProfileParcelForTransport(**kwargs)

@register('GetRoutingOspfv3Ipv4AfProfileParcelByParcelIdForTransport')
def GetRoutingOspfv3Ipv4AfProfileParcelByParcelIdForTransport(**kwargs):
    return SdwanClient().GetRoutingOspfv3Ipv4AfProfileParcelByParcelIdForTransport(**kwargs)

@register('GetRoutingOspfv3Ipv6AfProfileParcelForTransport')
def GetRoutingOspfv3Ipv6AfProfileParcelForTransport(**kwargs):
    return SdwanClient().GetRoutingOspfv3Ipv6AfProfileParcelForTransport(**kwargs)

@register('GetRoutingOspfv3Ipv6AfProfileParcelByParcelIdForTransport')
def GetRoutingOspfv3Ipv6AfProfileParcelByParcelIdForTransport(**kwargs):
    return SdwanClient().GetRoutingOspfv3Ipv6AfProfileParcelByParcelIdForTransport(**kwargs)

@register('GetT1e1controllerProfileParcelForTransport')
def GetT1e1controllerProfileParcelForTransport(**kwargs):
    return SdwanClient().GetT1e1controllerProfileParcelForTransport(**kwargs)

@register('GetT1e1controllerProfileParcelByParcelIdForTransport')
def GetT1e1controllerProfileParcelByParcelIdForTransport(**kwargs):
    return SdwanClient().GetT1e1controllerProfileParcelByParcelIdForTransport(**kwargs)

@register('GetTrackerProfileParcelForTransport')
def GetTrackerProfileParcelForTransport(**kwargs):
    return SdwanClient().GetTrackerProfileParcelForTransport(**kwargs)

@register('GetTrackerProfileParcelByParcelIdForTransport')
def GetTrackerProfileParcelByParcelIdForTransport(**kwargs):
    return SdwanClient().GetTrackerProfileParcelByParcelIdForTransport(**kwargs)

@register('GetTrackerGroupProfileParcelForTransport')
def GetTrackerGroupProfileParcelForTransport(**kwargs):
    return SdwanClient().GetTrackerGroupProfileParcelForTransport(**kwargs)

@register('GetTrackerGroupProfileParcelByParcelIdForTransport')
def GetTrackerGroupProfileParcelByParcelIdForTransport(**kwargs):
    return SdwanClient().GetTrackerGroupProfileParcelByParcelIdForTransport(**kwargs)

@register('GetWanVpnProfileParcelForTransport')
def GetWanVpnProfileParcelForTransport(**kwargs):
    return SdwanClient().GetWanVpnProfileParcelForTransport(**kwargs)

@register('GetWanVpnProfileParcelByParcelIdForTransport')
def GetWanVpnProfileParcelByParcelIdForTransport(**kwargs):
    return SdwanClient().GetWanVpnProfileParcelByParcelIdForTransport(**kwargs)

@register('GetInterfaceCellularParcelsForTransportWanVpn')
def GetInterfaceCellularParcelsForTransportWanVpn(**kwargs):
    return SdwanClient().GetInterfaceCellularParcelsForTransportWanVpn(**kwargs)

@register('GetWanVpnInterfaceCellularAssociatedIpv6TrackerParcelsForTransport')
def GetWanVpnInterfaceCellularAssociatedIpv6TrackerParcelsForTransport(**kwargs):
    return SdwanClient().GetWanVpnInterfaceCellularAssociatedIpv6TrackerParcelsForTransport(**kwargs)

@register('GetWanVpnInterfaceCellularAssociatedIpv6TrackerParcelByParcelIdForTransport')
def GetWanVpnInterfaceCellularAssociatedIpv6TrackerParcelByParcelIdForTransport(**kwargs):
    return SdwanClient().GetWanVpnInterfaceCellularAssociatedIpv6TrackerParcelByParcelIdForTransport(**kwargs)

@register('GetWanVpnInterfaceCellularAssociatedIpv6TrackerGroupParcelsForTransport')
def GetWanVpnInterfaceCellularAssociatedIpv6TrackerGroupParcelsForTransport(**kwargs):
    return SdwanClient().GetWanVpnInterfaceCellularAssociatedIpv6TrackerGroupParcelsForTransport(**kwargs)

@register('GetWanVpnInterfaceCellularAssociatedIpv6TrackerGroupParcelByParcelIdForTransport')
def GetWanVpnInterfaceCellularAssociatedIpv6TrackerGroupParcelByParcelIdForTransport(**kwargs):
    return SdwanClient().GetWanVpnInterfaceCellularAssociatedIpv6TrackerGroupParcelByParcelIdForTransport(**kwargs)

@register('GetWanVpnInterfaceCellularAssociatedTrackerParcelsForTransport')
def GetWanVpnInterfaceCellularAssociatedTrackerParcelsForTransport(**kwargs):
    return SdwanClient().GetWanVpnInterfaceCellularAssociatedTrackerParcelsForTransport(**kwargs)

@register('GetWanVpnInterfaceCellularAssociatedTrackerParcelByParcelIdForTransport')
def GetWanVpnInterfaceCellularAssociatedTrackerParcelByParcelIdForTransport(**kwargs):
    return SdwanClient().GetWanVpnInterfaceCellularAssociatedTrackerParcelByParcelIdForTransport(**kwargs)

@register('GetWanVpnInterfaceCellularAssociatedTrackerGroupParcelsForTransport')
def GetWanVpnInterfaceCellularAssociatedTrackerGroupParcelsForTransport(**kwargs):
    return SdwanClient().GetWanVpnInterfaceCellularAssociatedTrackerGroupParcelsForTransport(**kwargs)

@register('GetWanVpnInterfaceCellularAssociatedTrackerGroupParcelByParcelIdForTransport')
def GetWanVpnInterfaceCellularAssociatedTrackerGroupParcelByParcelIdForTransport(**kwargs):
    return SdwanClient().GetWanVpnInterfaceCellularAssociatedTrackerGroupParcelByParcelIdForTransport(**kwargs)

@register('GetWanVpnInterfaceCellularParcelByParcelIdForTransport')
def GetWanVpnInterfaceCellularParcelByParcelIdForTransport(**kwargs):
    return SdwanClient().GetWanVpnInterfaceCellularParcelByParcelIdForTransport(**kwargs)

@register('GetInterfaceEthernetParcelsForTransportWanVpn')
def GetInterfaceEthernetParcelsForTransportWanVpn(**kwargs):
    return SdwanClient().GetInterfaceEthernetParcelsForTransportWanVpn(**kwargs)

@register('GetWanVpnInterfaceEthernetParcelByParcelIdForTransport')
def GetWanVpnInterfaceEthernetParcelByParcelIdForTransport(**kwargs):
    return SdwanClient().GetWanVpnInterfaceEthernetParcelByParcelIdForTransport(**kwargs)

@register('GetWanVpnInterfaceEthernetAssociatedIpv6TrackerParcelsForTransport')
def GetWanVpnInterfaceEthernetAssociatedIpv6TrackerParcelsForTransport(**kwargs):
    return SdwanClient().GetWanVpnInterfaceEthernetAssociatedIpv6TrackerParcelsForTransport(**kwargs)

@register('GetWanVpnInterfaceEthernetAssociatedIpv6TrackerParcelByParcelIdForTransport')
def GetWanVpnInterfaceEthernetAssociatedIpv6TrackerParcelByParcelIdForTransport(**kwargs):
    return SdwanClient().GetWanVpnInterfaceEthernetAssociatedIpv6TrackerParcelByParcelIdForTransport(**kwargs)

@register('GetWanVpnInterfaceEthernetAssociatedIpv6TrackerGroupParcelsForTransport')
def GetWanVpnInterfaceEthernetAssociatedIpv6TrackerGroupParcelsForTransport(**kwargs):
    return SdwanClient().GetWanVpnInterfaceEthernetAssociatedIpv6TrackerGroupParcelsForTransport(**kwargs)

@register('GetWanVpnInterfaceEthernetAssociatedIpv6TrackerGroupParcelByParcelIdForTransport')
def GetWanVpnInterfaceEthernetAssociatedIpv6TrackerGroupParcelByParcelIdForTransport(**kwargs):
    return SdwanClient().GetWanVpnInterfaceEthernetAssociatedIpv6TrackerGroupParcelByParcelIdForTransport(**kwargs)

@register('GetWanVpnInterfaceEthernetAssociatedTrackerParcelsForTransport')
def GetWanVpnInterfaceEthernetAssociatedTrackerParcelsForTransport(**kwargs):
    return SdwanClient().GetWanVpnInterfaceEthernetAssociatedTrackerParcelsForTransport(**kwargs)

@register('GetWanVpnInterfaceEthernetAssociatedTrackerParcelByParcelIdForTransport')
def GetWanVpnInterfaceEthernetAssociatedTrackerParcelByParcelIdForTransport(**kwargs):
    return SdwanClient().GetWanVpnInterfaceEthernetAssociatedTrackerParcelByParcelIdForTransport(**kwargs)

@register('GetWanVpnInterfaceEthernetAssociatedTrackerGroupParcelsForTransport')
def GetWanVpnInterfaceEthernetAssociatedTrackerGroupParcelsForTransport(**kwargs):
    return SdwanClient().GetWanVpnInterfaceEthernetAssociatedTrackerGroupParcelsForTransport(**kwargs)

@register('GetWanVpnInterfaceEthernetAssociatedTrackerGroupParcelByParcelIdForTransport')
def GetWanVpnInterfaceEthernetAssociatedTrackerGroupParcelByParcelIdForTransport(**kwargs):
    return SdwanClient().GetWanVpnInterfaceEthernetAssociatedTrackerGroupParcelByParcelIdForTransport(**kwargs)

@register('GetInterfaceGreParcelsForTransportWanVpn')
def GetInterfaceGreParcelsForTransportWanVpn(**kwargs):
    return SdwanClient().GetInterfaceGreParcelsForTransportWanVpn(**kwargs)

@register('GetWanVpnInterfaceGreParcelByParcelIdForTransport')
def GetWanVpnInterfaceGreParcelByParcelIdForTransport(**kwargs):
    return SdwanClient().GetWanVpnInterfaceGreParcelByParcelIdForTransport(**kwargs)

@register('GetWanVpnInterfaceGreAssociatedTrackerParcelsForTransport')
def GetWanVpnInterfaceGreAssociatedTrackerParcelsForTransport(**kwargs):
    return SdwanClient().GetWanVpnInterfaceGreAssociatedTrackerParcelsForTransport(**kwargs)

@register('GetWanVpnInterfaceGreAssociatedTrackerParcelByParcelIdForTransport')
def GetWanVpnInterfaceGreAssociatedTrackerParcelByParcelIdForTransport(**kwargs):
    return SdwanClient().GetWanVpnInterfaceGreAssociatedTrackerParcelByParcelIdForTransport(**kwargs)

@register('getListOfProfileParcels_1')
def getListOfProfileParcels_1(**kwargs):
    return SdwanClient().getListOfProfileParcels_1(**kwargs)

@register('getProfileParcelByParcelId_1')
def getProfileParcelByParcelId_1(**kwargs):
    return SdwanClient().getProfileParcelByParcelId_1(**kwargs)

@register('GetWanVpnInterfaceIpsecAssociatedTrackerParcelsForTransport')
def GetWanVpnInterfaceIpsecAssociatedTrackerParcelsForTransport(**kwargs):
    return SdwanClient().GetWanVpnInterfaceIpsecAssociatedTrackerParcelsForTransport(**kwargs)

@register('GetWanVpnInterfaceIpsecAssociatedTrackerParcelByParcelIdForTransport')
def GetWanVpnInterfaceIpsecAssociatedTrackerParcelByParcelIdForTransport(**kwargs):
    return SdwanClient().GetWanVpnInterfaceIpsecAssociatedTrackerParcelByParcelIdForTransport(**kwargs)

@register('GetInterfaceSerialParcelsForTransportWanVpn')
def GetInterfaceSerialParcelsForTransportWanVpn(**kwargs):
    return SdwanClient().GetInterfaceSerialParcelsForTransportWanVpn(**kwargs)

@register('GetWanVpnInterfaceSerialParcelByParcelIdForTransport')
def GetWanVpnInterfaceSerialParcelByParcelIdForTransport(**kwargs):
    return SdwanClient().GetWanVpnInterfaceSerialParcelByParcelIdForTransport(**kwargs)

@register('GetWanVpnAssociatedRoutingBgpParcelsForTransport')
def GetWanVpnAssociatedRoutingBgpParcelsForTransport(**kwargs):
    return SdwanClient().GetWanVpnAssociatedRoutingBgpParcelsForTransport(**kwargs)

@register('GetWanVpnAssociatedRoutingBgpParcelByParcelIdForTransport')
def GetWanVpnAssociatedRoutingBgpParcelByParcelIdForTransport(**kwargs):
    return SdwanClient().GetWanVpnAssociatedRoutingBgpParcelByParcelIdForTransport(**kwargs)

@register('GetWanVpnAssociatedRoutingOspfParcelsForTransport')
def GetWanVpnAssociatedRoutingOspfParcelsForTransport(**kwargs):
    return SdwanClient().GetWanVpnAssociatedRoutingOspfParcelsForTransport(**kwargs)

@register('GetWanVpnAssociatedRoutingOspfParcelByParcelIdForTransport')
def GetWanVpnAssociatedRoutingOspfParcelByParcelIdForTransport(**kwargs):
    return SdwanClient().GetWanVpnAssociatedRoutingOspfParcelByParcelIdForTransport(**kwargs)

@register('GetWanVpnAssociatedRoutingOspfv3IPv4AfParcelsForTransport')
def GetWanVpnAssociatedRoutingOspfv3IPv4AfParcelsForTransport(**kwargs):
    return SdwanClient().GetWanVpnAssociatedRoutingOspfv3IPv4AfParcelsForTransport(**kwargs)

@register('GetWanVpnAssociatedRoutingOspfv3IPv4AfParcelByParcelIdForTransport')
def GetWanVpnAssociatedRoutingOspfv3IPv4AfParcelByParcelIdForTransport(**kwargs):
    return SdwanClient().GetWanVpnAssociatedRoutingOspfv3IPv4AfParcelByParcelIdForTransport(**kwargs)

@register('GetWanVpnAssociatedRoutingOspfv3IPv6AfParcelsForTransport')
def GetWanVpnAssociatedRoutingOspfv3IPv6AfParcelsForTransport(**kwargs):
    return SdwanClient().GetWanVpnAssociatedRoutingOspfv3IPv6AfParcelsForTransport(**kwargs)

@register('GetWanVpnAssociatedRoutingOspfv3IPv6AfParcelByParcelIdForTransport')
def GetWanVpnAssociatedRoutingOspfv3IPv6AfParcelByParcelIdForTransport(**kwargs):
    return SdwanClient().GetWanVpnAssociatedRoutingOspfv3IPv6AfParcelByParcelIdForTransport(**kwargs)

@register('getMSLADevices')
def getMSLADevices(**kwargs):
    return SdwanClient().getMSLADevices(**kwargs)

@register('getLicenseByUuid')
def getLicenseByUuid(**kwargs):
    return SdwanClient().getLicenseByUuid(**kwargs)

@register('GetPolicyGroupBySolution')
def GetPolicyGroupBySolution(**kwargs):
    return SdwanClient().GetPolicyGroupBySolution(**kwargs)

@register('GetPolicyGroup')
def GetPolicyGroup(**kwargs):
    return SdwanClient().GetPolicyGroup(**kwargs)

@register('GetPolicyGroupAssociation')
def GetPolicyGroupAssociation(**kwargs):
    return SdwanClient().GetPolicyGroupAssociation(**kwargs)

@register('getPolicyGroupDeviceVariables')
def getPolicyGroupDeviceVariables(**kwargs):
    return SdwanClient().getPolicyGroupDeviceVariables(**kwargs)

@register('getPolicyGroupDeviceVariablesSchema')
def getPolicyGroupDeviceVariablesSchema(**kwargs):
    return SdwanClient().getPolicyGroupDeviceVariablesSchema(**kwargs)

@register('getAllReportTemplates')
def getAllReportTemplates(**kwargs):
    return SdwanClient().getAllReportTemplates(**kwargs)

@register('downloadReportPreviewFile')
def downloadReportPreviewFile(**kwargs):
    return SdwanClient().downloadReportPreviewFile(**kwargs)

@register('getReportTemplateById')
def getReportTemplateById(**kwargs):
    return SdwanClient().getReportTemplateById(**kwargs)

@register('getAllReportTasksByReportId')
def getAllReportTasksByReportId(**kwargs):
    return SdwanClient().getAllReportTasksByReportId(**kwargs)

@register('downloadReportDataFile')
def downloadReportDataFile(**kwargs):
    return SdwanClient().downloadReportDataFile(**kwargs)

@register('getUrlForSdoIdentityService')
def getUrlForSdoIdentityService(**kwargs):
    return SdwanClient().getUrlForSdoIdentityService(**kwargs)

@register('getAllAccounts')
def getAllAccounts(**kwargs):
    return SdwanClient().getAllAccounts(**kwargs)

@register('getRatePlansByAcctId')
def getRatePlansByAcctId(**kwargs):
    return SdwanClient().getRatePlansByAcctId(**kwargs)

@register('getProvidersInfo')
def getProvidersInfo(**kwargs):
    return SdwanClient().getProvidersInfo(**kwargs)

@register('getCommPlansByAcctId')
def getCommPlansByAcctId(**kwargs):
    return SdwanClient().getCommPlansByAcctId(**kwargs)

@register('getProviderCredentialsByAccountId')
def getProviderCredentialsByAccountId(**kwargs):
    return SdwanClient().getProviderCredentialsByAccountId(**kwargs)

@register('getDeviceDataUsage')
def getDeviceDataUsage(**kwargs):
    return SdwanClient().getDeviceDataUsage(**kwargs)

@register('serviceChainMapping')
def serviceChainMapping(**kwargs):
    return SdwanClient().serviceChainMapping(**kwargs)

@register('getDevicesForTemplate')
def getDevicesForTemplate(**kwargs):
    return SdwanClient().getDevicesForTemplate(**kwargs)

@register('license')
def license(**kwargs):
    return SdwanClient().license(**kwargs)

@register('getUserSettings')
def getUserSettings(**kwargs):
    return SdwanClient().getUserSettings(**kwargs)

@register('GetTopologyGroupBySolution')
def GetTopologyGroupBySolution(**kwargs):
    return SdwanClient().GetTopologyGroupBySolution(**kwargs)

@register('GetTopologyGroup')
def GetTopologyGroup(**kwargs):
    return SdwanClient().GetTopologyGroup(**kwargs)

@register('generateDeviceInterfaceStatisticsData')
def generateDeviceInterfaceStatisticsData(**kwargs):
    return SdwanClient().generateDeviceInterfaceStatisticsData(**kwargs)

@register('getCountWithInterfaceStatistics')
def getCountWithInterfaceStatistics(**kwargs):
    return SdwanClient().getCountWithInterfaceStatistics(**kwargs)

@register('getStatDataFieldsByInterfaceStatistics')
def getStatDataFieldsByInterfaceStatistics(**kwargs):
    return SdwanClient().getStatDataFieldsByInterfaceStatistics(**kwargs)

@register('getWaniRecommendations')
def getWaniRecommendations(**kwargs):
    return SdwanClient().getWaniRecommendations(**kwargs)

@register('getAppliedWaniRecommendations')
def getAppliedWaniRecommendations(**kwargs):
    return SdwanClient().getAppliedWaniRecommendations(**kwargs)

@register('getListActivationStatus')
def getListActivationStatus(**kwargs):
    return SdwanClient().getListActivationStatus(**kwargs)

@register('getPolicyActivationStatus')
def getPolicyActivationStatus(**kwargs):
    return SdwanClient().getPolicyActivationStatus(**kwargs)

@register('webexAccessCode')
def webexAccessCode(**kwargs):
    return SdwanClient().webexAccessCode(**kwargs)

@register('getWebexDataCentersSyncStatus')
def getWebexDataCentersSyncStatus(**kwargs):
    return SdwanClient().getWebexDataCentersSyncStatus(**kwargs)

@register('redirectWebexDataCenters')
def redirectWebexDataCenters(**kwargs):
    return SdwanClient().redirectWebexDataCenters(**kwargs)
