# app/llm/function_dispatcher/catalystwan_dispatcher.py
from app.llm.function_dispatcher import register
from app.llm.platform_clients.catalystwan_client import CatalystwanClient

@register('getSecureXAccessToken')
def getSecureXAccessToken(**kwargs):
    return CatalystwanClient().getSecureXAccessToken(**kwargs)

@register('getAaaConfig')
def getAaaConfig(**kwargs):
    return CatalystwanClient().getAaaConfig(**kwargs)

@register('listenAuthEvents')
def listenAuthEvents(**kwargs):
    return CatalystwanClient().listenAuthEvents(**kwargs)

@register('getRadiusConfig')
def getRadiusConfig(**kwargs):
    return CatalystwanClient().getRadiusConfig(**kwargs)

@register('getTacacsConfig')
def getTacacsConfig(**kwargs):
    return CatalystwanClient().getTacacsConfig(**kwargs)

@register('findUsers_1')
def findUsers_1(**kwargs):
    return CatalystwanClient().findUsers_1(**kwargs)

@register('getActiveSessions_1')
def getActiveSessions_1(**kwargs):
    return CatalystwanClient().getActiveSessions_1(**kwargs)

@register('findUserRole_1')
def findUserRole_1(**kwargs):
    return CatalystwanClient().findUserRole_1(**kwargs)

@register('findUserAuthType_1')
def findUserAuthType_1(**kwargs):
    return CatalystwanClient().findUserAuthType_1(**kwargs)

@register('findUserGroups')
def findUserGroups(**kwargs):
    return CatalystwanClient().findUserGroups(**kwargs)

@register('createGroupGridColumns')
def createGroupGridColumns(**kwargs):
    return CatalystwanClient().createGroupGridColumns(**kwargs)

@register('findUserGroupsAsKeyValue')
def findUserGroupsAsKeyValue(**kwargs):
    return CatalystwanClient().findUserGroupsAsKeyValue(**kwargs)

@register('getVpnGroups')
def getVpnGroups(**kwargs):
    return CatalystwanClient().getVpnGroups(**kwargs)

@register('getRawAlarmData')
def getRawAlarmData(**kwargs):
    return CatalystwanClient().getRawAlarmData(**kwargs)

@register('getAggregationData')
def getAggregationData(**kwargs):
    return CatalystwanClient().getAggregationData(**kwargs)

@register('getNonViewedActiveAlarmsCount')
def getNonViewedActiveAlarmsCount(**kwargs):
    return CatalystwanClient().getNonViewedActiveAlarmsCount(**kwargs)

@register('listDisabledAlarm')
def listDisabledAlarm(**kwargs):
    return CatalystwanClient().listDisabledAlarm(**kwargs)

@register('getDocCount')
def getDocCount(**kwargs):
    return CatalystwanClient().getDocCount(**kwargs)

@register('getAlarmDataFields')
def getAlarmDataFields(**kwargs):
    return CatalystwanClient().getAlarmDataFields(**kwargs)

@register('getLinkStateAlarmConfig')
def getLinkStateAlarmConfig(**kwargs):
    return CatalystwanClient().getLinkStateAlarmConfig(**kwargs)

@register('getMasterManagerState')
def getMasterManagerState(**kwargs):
    return CatalystwanClient().getMasterManagerState(**kwargs)

@register('getNonViewedAlarms')
def getNonViewedAlarms(**kwargs):
    return CatalystwanClient().getNonViewedAlarms(**kwargs)

@register('getPage')
def getPage(**kwargs):
    return CatalystwanClient().getPage(**kwargs)

@register('setPeriodicPurgeTimer')
def setPeriodicPurgeTimer(**kwargs):
    return CatalystwanClient().setPeriodicPurgeTimer(**kwargs)

@register('getAlarmQueryFields')
def getAlarmQueryFields(**kwargs):
    return CatalystwanClient().getAlarmQueryFields(**kwargs)

@register('getFieldDetails')
def getFieldDetails(**kwargs):
    return CatalystwanClient().getFieldDetails(**kwargs)

@register('reset')
def reset(**kwargs):
    return CatalystwanClient().reset(**kwargs)

@register('restartCorrelationEngine')
def restartCorrelationEngine(**kwargs):
    return CatalystwanClient().restartCorrelationEngine(**kwargs)

@register('getAlarmTypesAsKeyValue')
def getAlarmTypesAsKeyValue(**kwargs):
    return CatalystwanClient().getAlarmTypesAsKeyValue(**kwargs)

@register('getBySeverity')
def getBySeverity(**kwargs):
    return CatalystwanClient().getBySeverity(**kwargs)

@register('getAlarmSeverityCustomHistogram')
def getAlarmSeverityCustomHistogram(**kwargs):
    return CatalystwanClient().getAlarmSeverityCustomHistogram(**kwargs)

@register('getAlarmSeverityMappings')
def getAlarmSeverityMappings(**kwargs):
    return CatalystwanClient().getAlarmSeverityMappings(**kwargs)

@register('getStats')
def getStats(**kwargs):
    return CatalystwanClient().getStats(**kwargs)

@register('getDeviceTopic')
def getDeviceTopic(**kwargs):
    return CatalystwanClient().getDeviceTopic(**kwargs)

@register('getAlarmDetails')
def getAlarmDetails(**kwargs):
    return CatalystwanClient().getAlarmDetails(**kwargs)

@register('getAllAppList')
def getAllAppList(**kwargs):
    return CatalystwanClient().getAllAppList(**kwargs)

@register('getAppListCategory')
def getAppListCategory(**kwargs):
    return CatalystwanClient().getAppListCategory(**kwargs)

@register('getNetworkDiscoveredApps')
def getNetworkDiscoveredApps(**kwargs):
    return CatalystwanClient().getNetworkDiscoveredApps(**kwargs)

@register('getAttributeMappingForApps')
def getAttributeMappingForApps(**kwargs):
    return CatalystwanClient().getAttributeMappingForApps(**kwargs)

@register('getKubernetesServices')
def getKubernetesServices(**kwargs):
    return CatalystwanClient().getKubernetesServices(**kwargs)

@register('getAppByUuid')
def getAppByUuid(**kwargs):
    return CatalystwanClient().getAppByUuid(**kwargs)

@register('getAppList')
def getAppList(**kwargs):
    return CatalystwanClient().getAppList(**kwargs)

@register('getKubernetesCluster')
def getKubernetesCluster(**kwargs):
    return CatalystwanClient().getKubernetesCluster(**kwargs)

@register('getActiveSaasFeeds')
def getActiveSaasFeeds(**kwargs):
    return CatalystwanClient().getActiveSaasFeeds(**kwargs)

@register('getAllSaasFeedForSelectedApp')
def getAllSaasFeedForSelectedApp(**kwargs):
    return CatalystwanClient().getAllSaasFeedForSelectedApp(**kwargs)

@register('getStatDataRawAuditLogData')
def getStatDataRawAuditLogData(**kwargs):
    return CatalystwanClient().getStatDataRawAuditLogData(**kwargs)

@register('getPropertyAggregationData')
def getPropertyAggregationData(**kwargs):
    return CatalystwanClient().getPropertyAggregationData(**kwargs)

@register('getCount')
def getCount(**kwargs):
    return CatalystwanClient().getCount(**kwargs)

@register('getStatDataFields')
def getStatDataFields(**kwargs):
    return CatalystwanClient().getStatDataFields(**kwargs)

@register('getStatBulkRawPropertyData')
def getStatBulkRawPropertyData(**kwargs):
    return CatalystwanClient().getStatBulkRawPropertyData(**kwargs)

@register('getStatQueryFields')
def getStatQueryFields(**kwargs):
    return CatalystwanClient().getStatQueryFields(**kwargs)

@register('generateAuditLog')
def generateAuditLog(**kwargs):
    return CatalystwanClient().generateAuditLog(**kwargs)

@register('getAuditSeverityCustomHistogram')
def getAuditSeverityCustomHistogram(**kwargs):
    return CatalystwanClient().getAuditSeverityCustomHistogram(**kwargs)

@register('getLocalBackupInfo')
def getLocalBackupInfo(**kwargs):
    return CatalystwanClient().getLocalBackupInfo(**kwargs)

@register('downloadBackupFile')
def downloadBackupFile(**kwargs):
    return CatalystwanClient().downloadBackupFile(**kwargs)

@register('listBackup')
def listBackup(**kwargs):
    return CatalystwanClient().listBackup(**kwargs)

@register('getCdnaSenseService')
def getCdnaSenseService(**kwargs):
    return CatalystwanClient().getCdnaSenseService(**kwargs)

@register('getCdnaServer')
def getCdnaServer(**kwargs):
    return CatalystwanClient().getCdnaServer(**kwargs)

@register('getControllerCertStatus')
def getControllerCertStatus(**kwargs):
    return CatalystwanClient().getControllerCertStatus(**kwargs)

@register('getCSRViewRightMenus')
def getCSRViewRightMenus(**kwargs):
    return CatalystwanClient().getCSRViewRightMenus(**kwargs)

@register('getDeviceViewRightMenus')
def getDeviceViewRightMenus(**kwargs):
    return CatalystwanClient().getDeviceViewRightMenus(**kwargs)

@register('getDevicesList')
def getDevicesList(**kwargs):
    return CatalystwanClient().getDevicesList(**kwargs)

@register('getListStatus')
def getListStatus(**kwargs):
    return CatalystwanClient().getListStatus(**kwargs)

@register('setvSmartMtHubList')
def setvSmartMtHubList(**kwargs):
    return CatalystwanClient().setvSmartMtHubList(**kwargs)

@register('getQuarantineBanner')
def getQuarantineBanner(**kwargs):
    return CatalystwanClient().getQuarantineBanner(**kwargs)

@register('getCertificateData')
def getCertificateData(**kwargs):
    return CatalystwanClient().getCertificateData(**kwargs)

@register('getRootCertChains')
def getRootCertChains(**kwargs):
    return CatalystwanClient().getRootCertChains(**kwargs)

@register('getRootCertificate')
def getRootCertificate(**kwargs):
    return CatalystwanClient().getRootCertificate(**kwargs)

@register('rsaKeyLength2048ForAllDevices')
def rsaKeyLength2048ForAllDevices(**kwargs):
    return CatalystwanClient().rsaKeyLength2048ForAllDevices(**kwargs)

@register('getCertificateDetail')
def getCertificateDetail(**kwargs):
    return CatalystwanClient().getCertificateDetail(**kwargs)

@register('getCertificateStats')
def getCertificateStats(**kwargs):
    return CatalystwanClient().getCertificateStats(**kwargs)

@register('syncvBond')
def syncvBond(**kwargs):
    return CatalystwanClient().syncvBond(**kwargs)

@register('getTokenList')
def getTokenList(**kwargs):
    return CatalystwanClient().getTokenList(**kwargs)

@register('getInstalledCert')
def getInstalledCert(**kwargs):
    return CatalystwanClient().getInstalledCert(**kwargs)

@register('getvEdgeCSR')
def getvEdgeCSR(**kwargs):
    return CatalystwanClient().getvEdgeCSR(**kwargs)

@register('getvEdgeList')
def getvEdgeList(**kwargs):
    return CatalystwanClient().getvEdgeList(**kwargs)

@register('getView')
def getView(**kwargs):
    return CatalystwanClient().getView(**kwargs)

@register('getSelfSignedCert')
def getSelfSignedCert(**kwargs):
    return CatalystwanClient().getSelfSignedCert(**kwargs)

@register('getvSmartList')
def getvSmartList(**kwargs):
    return CatalystwanClient().getvSmartList(**kwargs)

@register('createServerInfo')
def createServerInfo(**kwargs):
    return CatalystwanClient().createServerInfo(**kwargs)

@register('getCsrfToken')
def getCsrfToken(**kwargs):
    return CatalystwanClient().getCsrfToken(**kwargs)

@register('getAccessTokenforDevice')
def getAccessTokenforDevice(**kwargs):
    return CatalystwanClient().getAccessTokenforDevice(**kwargs)

@register('connect')
def connect(**kwargs):
    return CatalystwanClient().connect(**kwargs)

@register('getCloudCredentials')
def getCloudCredentials(**kwargs):
    return CatalystwanClient().getCloudCredentials(**kwargs)

@register('isStaging')
def isStaging(**kwargs):
    return CatalystwanClient().isStaging(**kwargs)

@register('getTelemetryState')
def getTelemetryState(**kwargs):
    return CatalystwanClient().getTelemetryState(**kwargs)

@register('getvAnalyticsDashboardList')
def getvAnalyticsDashboardList(**kwargs):
    return CatalystwanClient().getvAnalyticsDashboardList(**kwargs)

@register('checkIfClusterLocked')
def checkIfClusterLocked(**kwargs):
    return CatalystwanClient().checkIfClusterLocked(**kwargs)

@register('getClusterWorkflowVersion')
def getClusterWorkflowVersion(**kwargs):
    return CatalystwanClient().getClusterWorkflowVersion(**kwargs)

@register('getConnectedDevices')
def getConnectedDevices(**kwargs):
    return CatalystwanClient().getConnectedDevices(**kwargs)

@register('healthDetails')
def healthDetails(**kwargs):
    return CatalystwanClient().healthDetails(**kwargs)

@register('healthStatusInfo')
def healthStatusInfo(**kwargs):
    return CatalystwanClient().healthStatusInfo(**kwargs)

@register('healthSummary')
def healthSummary(**kwargs):
    return CatalystwanClient().healthSummary(**kwargs)

@register('hostHealthStatus')
def hostHealthStatus(**kwargs):
    return CatalystwanClient().hostHealthStatus(**kwargs)

@register('getConfiguredIPList')
def getConfiguredIPList(**kwargs):
    return CatalystwanClient().getConfiguredIPList(**kwargs)

@register('isClusterReady')
def isClusterReady(**kwargs):
    return CatalystwanClient().isClusterReady(**kwargs)

@register('listVmanages')
def listVmanages(**kwargs):
    return CatalystwanClient().listVmanages(**kwargs)

@register('nodeProperties')
def nodeProperties(**kwargs):
    return CatalystwanClient().nodeProperties(**kwargs)

@register('getTenancyMode')
def getTenancyMode(**kwargs):
    return CatalystwanClient().getTenancyMode(**kwargs)

@register('getTenantsList')
def getTenantsList(**kwargs):
    return CatalystwanClient().getTenantsList(**kwargs)

@register('getVManageDetails')
def getVManageDetails(**kwargs):
    return CatalystwanClient().getVManageDetails(**kwargs)

@register('getConnectedDevicesPerTenant')
def getConnectedDevicesPerTenant(**kwargs):
    return CatalystwanClient().getConnectedDevicesPerTenant(**kwargs)

@register('getvnfByDeviceId')
def getvnfByDeviceId(**kwargs):
    return CatalystwanClient().getvnfByDeviceId(**kwargs)

@register('getVNFEventsCountDetail')
def getVNFEventsCountDetail(**kwargs):
    return CatalystwanClient().getVNFEventsCountDetail(**kwargs)

@register('getVNFAlarmCount')
def getVNFAlarmCount(**kwargs):
    return CatalystwanClient().getVNFAlarmCount(**kwargs)

@register('getVNFEventsDetail')
def getVNFEventsDetail(**kwargs):
    return CatalystwanClient().getVNFEventsDetail(**kwargs)

@register('getVNFInterfaceDetail')
def getVNFInterfaceDetail(**kwargs):
    return CatalystwanClient().getVNFInterfaceDetail(**kwargs)

@register('doesValidImageExist')
def doesValidImageExist(**kwargs):
    return CatalystwanClient().doesValidImageExist(**kwargs)

@register('getContainerInspectData')
def getContainerInspectData(**kwargs):
    return CatalystwanClient().getContainerInspectData(**kwargs)

@register('getContainerSettings')
def getContainerSettings(**kwargs):
    return CatalystwanClient().getContainerSettings(**kwargs)

@register('generateDeviceStateData')
def generateDeviceStateData(**kwargs):
    return CatalystwanClient().generateDeviceStateData(**kwargs)

@register('generateDeviceStateDataFields')
def generateDeviceStateDataFields(**kwargs):
    return CatalystwanClient().generateDeviceStateDataFields(**kwargs)

@register('generateDeviceStateDataWithQueryString')
def generateDeviceStateDataWithQueryString(**kwargs):
    return CatalystwanClient().generateDeviceStateDataWithQueryString(**kwargs)

@register('getStatisticsType')
def getStatisticsType(**kwargs):
    return CatalystwanClient().getStatisticsType(**kwargs)

@register('getActiveAlarms')
def getActiveAlarms(**kwargs):
    return CatalystwanClient().getActiveAlarms(**kwargs)

@register('generateDeviceStatisticsData')
def generateDeviceStatisticsData(**kwargs):
    return CatalystwanClient().generateDeviceStatisticsData(**kwargs)

@register('getCountWithStateDataType')
def getCountWithStateDataType(**kwargs):
    return CatalystwanClient().getCountWithStateDataType(**kwargs)

@register('getStatDataFieldsByStateDataType')
def getStatDataFieldsByStateDataType(**kwargs):
    return CatalystwanClient().getStatDataFieldsByStateDataType(**kwargs)

@register('getCloudSettings')
def getCloudSettings(**kwargs):
    return CatalystwanClient().getCloudSettings(**kwargs)

@register('getAccessToken')
def getAccessToken(**kwargs):
    return CatalystwanClient().getAccessToken(**kwargs)

@register('getIdToken')
def getIdToken(**kwargs):
    return CatalystwanClient().getIdToken(**kwargs)

@register('getOTP')
def getOTP(**kwargs):
    return CatalystwanClient().getOTP(**kwargs)

@register('getTelemetrySettings')
def getTelemetrySettings(**kwargs):
    return CatalystwanClient().getTelemetrySettings(**kwargs)

@register('getDCATenantOwners')
def getDCATenantOwners(**kwargs):
    return CatalystwanClient().getDCATenantOwners(**kwargs)

@register('getCrashLogsSynced')
def getCrashLogsSynced(**kwargs):
    return CatalystwanClient().getCrashLogsSynced(**kwargs)

@register('getCloudServicesConfigurationDCA')
def getCloudServicesConfigurationDCA(**kwargs):
    return CatalystwanClient().getCloudServicesConfigurationDCA(**kwargs)

@register('listAllDevices')
def listAllDevices(**kwargs):
    return CatalystwanClient().listAllDevices(**kwargs)

@register('getAAAservers')
def getAAAservers(**kwargs):
    return CatalystwanClient().getAAAservers(**kwargs)

@register('getAAAUsers')
def getAAAUsers(**kwargs):
    return CatalystwanClient().getAAAUsers(**kwargs)

@register('getACLMatchCounterUsers')
def getACLMatchCounterUsers(**kwargs):
    return CatalystwanClient().getACLMatchCounterUsers(**kwargs)

@register('generateChangePartitionInfo')
def generateChangePartitionInfo(**kwargs):
    return CatalystwanClient().generateChangePartitionInfo(**kwargs)

@register('generateDeactivateInfo')
def generateDeactivateInfo(**kwargs):
    return CatalystwanClient().generateDeactivateInfo(**kwargs)

@register('createFilterVPNList')
def createFilterVPNList(**kwargs):
    return CatalystwanClient().createFilterVPNList(**kwargs)

@register('getFirmwareImages')
def getFirmwareImages(**kwargs):
    return CatalystwanClient().getFirmwareImages(**kwargs)

@register('getFirmwareDevices')
def getFirmwareDevices(**kwargs):
    return CatalystwanClient().getFirmwareDevices(**kwargs)

@register('getFirmwareRemoteImage')
def getFirmwareRemoteImage(**kwargs):
    return CatalystwanClient().getFirmwareRemoteImage(**kwargs)

@register('getDevicesFWUpgrade')
def getDevicesFWUpgrade(**kwargs):
    return CatalystwanClient().getDevicesFWUpgrade(**kwargs)

@register('getFirmwareImageDetails')
def getFirmwareImageDetails(**kwargs):
    return CatalystwanClient().getFirmwareImageDetails(**kwargs)

@register('generateInstallInfo')
def generateInstallInfo(**kwargs):
    return CatalystwanClient().generateInstallInfo(**kwargs)

@register('generateDeviceList')
def generateDeviceList(**kwargs):
    return CatalystwanClient().generateDeviceList(**kwargs)

@register('generateDeviceActionList')
def generateDeviceActionList(**kwargs):
    return CatalystwanClient().generateDeviceActionList(**kwargs)

@register('generateRebootInfo')
def generateRebootInfo(**kwargs):
    return CatalystwanClient().generateRebootInfo(**kwargs)

@register('generateRebootDeviceList')
def generateRebootDeviceList(**kwargs):
    return CatalystwanClient().generateRebootDeviceList(**kwargs)

@register('generateRediscoverInfo')
def generateRediscoverInfo(**kwargs):
    return CatalystwanClient().generateRediscoverInfo(**kwargs)

@register('getRemoteServerList')
def getRemoteServerList(**kwargs):
    return CatalystwanClient().getRemoteServerList(**kwargs)

@register('getRemoteServerById')
def getRemoteServerById(**kwargs):
    return CatalystwanClient().getRemoteServerById(**kwargs)

@register('generateRemovePartitionInfo')
def generateRemovePartitionInfo(**kwargs):
    return CatalystwanClient().generateRemovePartitionInfo(**kwargs)

@register('testApiKey')
def testApiKey(**kwargs):
    return CatalystwanClient().testApiKey(**kwargs)

@register('generateSecurityDevicesList')
def generateSecurityDevicesList(**kwargs):
    return CatalystwanClient().generateSecurityDevicesList(**kwargs)

@register('findSoftwareImages')
def findSoftwareImages(**kwargs):
    return CatalystwanClient().findSoftwareImages(**kwargs)

@register('getImageProperties')
def getImageProperties(**kwargs):
    return CatalystwanClient().getImageProperties(**kwargs)

@register('findSoftwareImagesWithFilters')
def findSoftwareImagesWithFilters(**kwargs):
    return CatalystwanClient().findSoftwareImagesWithFilters(**kwargs)

@register('getUploadImagesCount')
def getUploadImagesCount(**kwargs):
    return CatalystwanClient().getUploadImagesCount(**kwargs)

@register('generateUtdImageData')
def generateUtdImageData(**kwargs):
    return CatalystwanClient().generateUtdImageData(**kwargs)

@register('downloadPackageFile')
def downloadPackageFile(**kwargs):
    return CatalystwanClient().downloadPackageFile(**kwargs)

@register('getImageMetadata')
def getImageMetadata(**kwargs):
    return CatalystwanClient().getImageMetadata(**kwargs)

@register('getImageRemoteServer')
def getImageRemoteServer(**kwargs):
    return CatalystwanClient().getImageRemoteServer(**kwargs)

@register('findVEdgeSoftwareVersion')
def findVEdgeSoftwareVersion(**kwargs):
    return CatalystwanClient().findVEdgeSoftwareVersion(**kwargs)

@register('findSoftwareVersion')
def findSoftwareVersion(**kwargs):
    return CatalystwanClient().findSoftwareVersion(**kwargs)

@register('getVnfProperties')
def getVnfProperties(**kwargs):
    return CatalystwanClient().getVnfProperties(**kwargs)

@register('findZtpSoftwareVersion')
def findZtpSoftwareVersion(**kwargs):
    return CatalystwanClient().findZtpSoftwareVersion(**kwargs)

@register('triggerPendingTasksMonitoring')
def triggerPendingTasksMonitoring(**kwargs):
    return CatalystwanClient().triggerPendingTasksMonitoring(**kwargs)

@register('cleanStatus')
def cleanStatus(**kwargs):
    return CatalystwanClient().cleanStatus(**kwargs)

@register('getMaintenanceWindowFlag')
def getMaintenanceWindowFlag(**kwargs):
    return CatalystwanClient().getMaintenanceWindowFlag(**kwargs)

@register('findRunningTasks')
def findRunningTasks(**kwargs):
    return CatalystwanClient().findRunningTasks(**kwargs)

@register('getActiveTaskCount')
def getActiveTaskCount(**kwargs):
    return CatalystwanClient().getActiveTaskCount(**kwargs)

@register('getCleanStatus')
def getCleanStatus(**kwargs):
    return CatalystwanClient().getCleanStatus(**kwargs)

@register('findStatus')
def findStatus(**kwargs):
    return CatalystwanClient().findStatus(**kwargs)

@register('testIoxConfig')
def testIoxConfig(**kwargs):
    return CatalystwanClient().testIoxConfig(**kwargs)

@register('createVPNList')
def createVPNList(**kwargs):
    return CatalystwanClient().createVPNList(**kwargs)

@register('getZTPUpgradeConfig')
def getZTPUpgradeConfig(**kwargs):
    return CatalystwanClient().getZTPUpgradeConfig(**kwargs)

@register('getZTPUpgradeConfigSetting')
def getZTPUpgradeConfigSetting(**kwargs):
    return CatalystwanClient().getZTPUpgradeConfigSetting(**kwargs)

@register('getAppHostingAttachedDevices')
def getAppHostingAttachedDevices(**kwargs):
    return CatalystwanClient().getAppHostingAttachedDevices(**kwargs)

@register('getAppHostingDetails')
def getAppHostingDetails(**kwargs):
    return CatalystwanClient().getAppHostingDetails(**kwargs)

@register('getAppHostingGuestRoutes')
def getAppHostingGuestRoutes(**kwargs):
    return CatalystwanClient().getAppHostingGuestRoutes(**kwargs)

@register('getAppHostingNetworkDevices')
def getAppHostingNetworkDevices(**kwargs):
    return CatalystwanClient().getAppHostingNetworkDevices(**kwargs)

@register('getAppHostingNetworkUtils')
def getAppHostingNetworkUtils(**kwargs):
    return CatalystwanClient().getAppHostingNetworkUtils(**kwargs)

@register('getAppHostingProcesses')
def getAppHostingProcesses(**kwargs):
    return CatalystwanClient().getAppHostingProcesses(**kwargs)

@register('getAppHostingStorageUtils')
def getAppHostingStorageUtils(**kwargs):
    return CatalystwanClient().getAppHostingStorageUtils(**kwargs)

@register('getAppHostingUtilization')
def getAppHostingUtilization(**kwargs):
    return CatalystwanClient().getAppHostingUtilization(**kwargs)

@register('createAppRouteSlaClassList')
def createAppRouteSlaClassList(**kwargs):
    return CatalystwanClient().createAppRouteSlaClassList(**kwargs)

@register('createAppRouteStatisticsList')
def createAppRouteStatisticsList(**kwargs):
    return CatalystwanClient().createAppRouteStatisticsList(**kwargs)

@register('getAppLogFlowCount')
def getAppLogFlowCount(**kwargs):
    return CatalystwanClient().getAppLogFlowCount(**kwargs)

@register('getAppLogFlows')
def getAppLogFlows(**kwargs):
    return CatalystwanClient().getAppLogFlows(**kwargs)

@register('createAppqoeActiveFlowIdDetails')
def createAppqoeActiveFlowIdDetails(**kwargs):
    return CatalystwanClient().createAppqoeActiveFlowIdDetails(**kwargs)

@register('getAppqoeHputStats')
def getAppqoeHputStats(**kwargs):
    return CatalystwanClient().getAppqoeHputStats(**kwargs)

@register('getAppqoeNatStats')
def getAppqoeNatStats(**kwargs):
    return CatalystwanClient().getAppqoeNatStats(**kwargs)

@register('getAppqoeRmResources')
def getAppqoeRmResources(**kwargs):
    return CatalystwanClient().getAppqoeRmResources(**kwargs)

@register('getAppqoeRMStats')
def getAppqoeRMStats(**kwargs):
    return CatalystwanClient().getAppqoeRMStats(**kwargs)

@register('getAppqoeServicesStatus')
def getAppqoeServicesStatus(**kwargs):
    return CatalystwanClient().getAppqoeServicesStatus(**kwargs)

@register('getAppqoeSppiPipeStats')
def getAppqoeSppiPipeStats(**kwargs):
    return CatalystwanClient().getAppqoeSppiPipeStats(**kwargs)

@register('getAppqoeSppiQueueStats')
def getAppqoeSppiQueueStats(**kwargs):
    return CatalystwanClient().getAppqoeSppiQueueStats(**kwargs)

@register('getAppqoeClusterSummary')
def getAppqoeClusterSummary(**kwargs):
    return CatalystwanClient().getAppqoeClusterSummary(**kwargs)

@register('getAppqoeErrorRecent')
def getAppqoeErrorRecent(**kwargs):
    return CatalystwanClient().getAppqoeErrorRecent(**kwargs)

@register('createAppqoeFlowIdExpiredDetails')
def createAppqoeFlowIdExpiredDetails(**kwargs):
    return CatalystwanClient().createAppqoeFlowIdExpiredDetails(**kwargs)

@register('getAppqoeFlowClosedError')
def getAppqoeFlowClosedError(**kwargs):
    return CatalystwanClient().getAppqoeFlowClosedError(**kwargs)

@register('getAppqoeExpired')
def getAppqoeExpired(**kwargs):
    return CatalystwanClient().getAppqoeExpired(**kwargs)

@register('getAppqoeServiceControllers')
def getAppqoeServiceControllers(**kwargs):
    return CatalystwanClient().getAppqoeServiceControllers(**kwargs)

@register('getAppqoeStatus')
def getAppqoeStatus(**kwargs):
    return CatalystwanClient().getAppqoeStatus(**kwargs)

@register('createAppqoeVpnIdList')
def createAppqoeVpnIdList(**kwargs):
    return CatalystwanClient().createAppqoeVpnIdList(**kwargs)

@register('getARPInterface')
def getARPInterface(**kwargs):
    return CatalystwanClient().getARPInterface(**kwargs)

@register('getAutonomousSoftwareVersion')
def getAutonomousSoftwareVersion(**kwargs):
    return CatalystwanClient().getAutonomousSoftwareVersion(**kwargs)

@register('createBFDHistoryList')
def createBFDHistoryList(**kwargs):
    return CatalystwanClient().createBFDHistoryList(**kwargs)

@register('createBFDLinkList')
def createBFDLinkList(**kwargs):
    return CatalystwanClient().createBFDLinkList(**kwargs)

@register('createBFDSessions')
def createBFDSessions(**kwargs):
    return CatalystwanClient().createBFDSessions(**kwargs)

@register('getBFDSiteStateDetail')
def getBFDSiteStateDetail(**kwargs):
    return CatalystwanClient().getBFDSiteStateDetail(**kwargs)

@register('getBFDSitesSummary')
def getBFDSitesSummary(**kwargs):
    return CatalystwanClient().getBFDSitesSummary(**kwargs)

@register('getDeviceBFDStateSummary')
def getDeviceBFDStateSummary(**kwargs):
    return CatalystwanClient().getDeviceBFDStateSummary(**kwargs)

@register('getDeviceBFDStateSummaryTloc')
def getDeviceBFDStateSummaryTloc(**kwargs):
    return CatalystwanClient().getDeviceBFDStateSummaryTloc(**kwargs)

@register('getDeviceTlocToIntfList')
def getDeviceTlocToIntfList(**kwargs):
    return CatalystwanClient().getDeviceTlocToIntfList(**kwargs)

@register('getDeviceBFDStatus')
def getDeviceBFDStatus(**kwargs):
    return CatalystwanClient().getDeviceBFDStatus(**kwargs)

@register('createBFDSummary')
def createBFDSummary(**kwargs):
    return CatalystwanClient().createBFDSummary(**kwargs)

@register('getDeviceBFDStatusSummary')
def getDeviceBFDStatusSummary(**kwargs):
    return CatalystwanClient().getDeviceBFDStatusSummary(**kwargs)

@register('createSyncedBFDSession')
def createSyncedBFDSession(**kwargs):
    return CatalystwanClient().createSyncedBFDSession(**kwargs)

@register('createTLOCSummary')
def createTLOCSummary(**kwargs):
    return CatalystwanClient().createTLOCSummary(**kwargs)

@register('getBFDTlocStateDetail')
def getBFDTlocStateDetail(**kwargs):
    return CatalystwanClient().getBFDTlocStateDetail(**kwargs)

@register('createBGPNeighborsList')
def createBGPNeighborsList(**kwargs):
    return CatalystwanClient().createBGPNeighborsList(**kwargs)

@register('createBGPRoutesList')
def createBGPRoutesList(**kwargs):
    return CatalystwanClient().createBGPRoutesList(**kwargs)

@register('createBGPSummary')
def createBGPSummary(**kwargs):
    return CatalystwanClient().createBGPSummary(**kwargs)

@register('getBridgeInterfaceList')
def getBridgeInterfaceList(**kwargs):
    return CatalystwanClient().getBridgeInterfaceList(**kwargs)

@register('getBridgeInterfaceMac')
def getBridgeInterfaceMac(**kwargs):
    return CatalystwanClient().getBridgeInterfaceMac(**kwargs)

@register('getBridgeInterfaceTable')
def getBridgeInterfaceTable(**kwargs):
    return CatalystwanClient().getBridgeInterfaceTable(**kwargs)

@register('getTenantsDevicesAndSites')
def getTenantsDevicesAndSites(**kwargs):
    return CatalystwanClient().getTenantsDevicesAndSites(**kwargs)

@register('createAppFwdCflowdFlowsList')
def createAppFwdCflowdFlowsList(**kwargs):
    return CatalystwanClient().createAppFwdCflowdFlowsList(**kwargs)

@register('createAppFwdCflowdV6FlowsList')
def createAppFwdCflowdV6FlowsList(**kwargs):
    return CatalystwanClient().createAppFwdCflowdV6FlowsList(**kwargs)

@register('createCellularConnectionList')
def createCellularConnectionList(**kwargs):
    return CatalystwanClient().createCellularConnectionList(**kwargs)

@register('cellularCountDashlet')
def cellularCountDashlet(**kwargs):
    return CatalystwanClient().cellularCountDashlet(**kwargs)

@register('dataUsage')
def dataUsage(**kwargs):
    return CatalystwanClient().dataUsage(**kwargs)

@register('cellularCountDashletDetails')
def cellularCountDashletDetails(**kwargs):
    return CatalystwanClient().cellularCountDashletDetails(**kwargs)

@register('createHardwareList')
def createHardwareList(**kwargs):
    return CatalystwanClient().createHardwareList(**kwargs)

@register('cellularHealthDashlet')
def cellularHealthDashlet(**kwargs):
    return CatalystwanClient().cellularHealthDashlet(**kwargs)

@register('createModemList')
def createModemList(**kwargs):
    return CatalystwanClient().createModemList(**kwargs)

@register('createNetworkList')
def createNetworkList(**kwargs):
    return CatalystwanClient().createNetworkList(**kwargs)

@register('createProfileList')
def createProfileList(**kwargs):
    return CatalystwanClient().createProfileList(**kwargs)

@register('createRadioList')
def createRadioList(**kwargs):
    return CatalystwanClient().createRadioList(**kwargs)

@register('createSessionsList')
def createSessionsList(**kwargs):
    return CatalystwanClient().createSessionsList(**kwargs)

@register('getCellularStatusList')
def getCellularStatusList(**kwargs):
    return CatalystwanClient().getCellularStatusList(**kwargs)

@register('getEiolteConnectionInfo')
def getEiolteConnectionInfo(**kwargs):
    return CatalystwanClient().getEiolteConnectionInfo(**kwargs)

@register('getEiolteHardwareInfo')
def getEiolteHardwareInfo(**kwargs):
    return CatalystwanClient().getEiolteHardwareInfo(**kwargs)

@register('getAONIpsecInterfaceCountersInfo')
def getAONIpsecInterfaceCountersInfo(**kwargs):
    return CatalystwanClient().getAONIpsecInterfaceCountersInfo(**kwargs)

@register('getAONIpsecInterfaceSessionnfo')
def getAONIpsecInterfaceSessionnfo(**kwargs):
    return CatalystwanClient().getAONIpsecInterfaceSessionnfo(**kwargs)

@register('getEiolteNetworkInfo')
def getEiolteNetworkInfo(**kwargs):
    return CatalystwanClient().getEiolteNetworkInfo(**kwargs)

@register('getEiolteRadioInfo')
def getEiolteRadioInfo(**kwargs):
    return CatalystwanClient().getEiolteRadioInfo(**kwargs)

@register('getEiolteSimInfo')
def getEiolteSimInfo(**kwargs):
    return CatalystwanClient().getEiolteSimInfo(**kwargs)

@register('getCflowdDPIDeviceFieldJSON')
def getCflowdDPIDeviceFieldJSON(**kwargs):
    return CatalystwanClient().getCflowdDPIDeviceFieldJSON(**kwargs)

@register('createCflowdCollectorList')
def createCflowdCollectorList(**kwargs):
    return CatalystwanClient().createCflowdCollectorList(**kwargs)

@register('getCflowdDPIFieldJSON')
def getCflowdDPIFieldJSON(**kwargs):
    return CatalystwanClient().getCflowdDPIFieldJSON(**kwargs)

@register('createCflowCollectorList')
def createCflowCollectorList(**kwargs):
    return CatalystwanClient().createCflowCollectorList(**kwargs)

@register('createCflowdFlowsCountList')
def createCflowdFlowsCountList(**kwargs):
    return CatalystwanClient().createCflowdFlowsCountList(**kwargs)

@register('getFnFCacheStats')
def getFnFCacheStats(**kwargs):
    return CatalystwanClient().getFnFCacheStats(**kwargs)

@register('getFnFExportClientStats')
def getFnFExportClientStats(**kwargs):
    return CatalystwanClient().getFnFExportClientStats(**kwargs)

@register('getFnFExportStats')
def getFnFExportStats(**kwargs):
    return CatalystwanClient().getFnFExportStats(**kwargs)

@register('getFnf')
def getFnf(**kwargs):
    return CatalystwanClient().getFnf(**kwargs)

@register('getFnFMonitorStats')
def getFnFMonitorStats(**kwargs):
    return CatalystwanClient().getFnFMonitorStats(**kwargs)

@register('createCflowdStatistics')
def createCflowdStatistics(**kwargs):
    return CatalystwanClient().createCflowdStatistics(**kwargs)

@register('createCflowdTemplate')
def createCflowdTemplate(**kwargs):
    return CatalystwanClient().createCflowdTemplate(**kwargs)

@register('getMpDatabase')
def getMpDatabase(**kwargs):
    return CatalystwanClient().getMpDatabase(**kwargs)

@register('getMpLocalMep')
def getMpLocalMep(**kwargs):
    return CatalystwanClient().getMpLocalMep(**kwargs)

@register('getMpLocalMip')
def getMpLocalMip(**kwargs):
    return CatalystwanClient().getMpLocalMip(**kwargs)

@register('getMpRemoteMep')
def getMpRemoteMep(**kwargs):
    return CatalystwanClient().getMpRemoteMep(**kwargs)

@register('createApplicationsDetailList')
def createApplicationsDetailList(**kwargs):
    return CatalystwanClient().createApplicationsDetailList(**kwargs)

@register('createApplicationsList')
def createApplicationsList(**kwargs):
    return CatalystwanClient().createApplicationsList(**kwargs)

@register('createGatewayExitsList')
def createGatewayExitsList(**kwargs):
    return CatalystwanClient().createGatewayExitsList(**kwargs)

@register('createLbApplicationsList')
def createLbApplicationsList(**kwargs):
    return CatalystwanClient().createLbApplicationsList(**kwargs)

@register('createLocalExitsList')
def createLocalExitsList(**kwargs):
    return CatalystwanClient().createLocalExitsList(**kwargs)

@register('getComplianceDetails')
def getComplianceDetails(**kwargs):
    return CatalystwanClient().getComplianceDetails(**kwargs)

@register('getComplianceSummary')
def getComplianceSummary(**kwargs):
    return CatalystwanClient().getComplianceSummary(**kwargs)

@register('getDeviceRunningConfig')
def getDeviceRunningConfig(**kwargs):
    return CatalystwanClient().getDeviceRunningConfig(**kwargs)

@register('getDeviceRunningConfigHTML')
def getDeviceRunningConfigHTML(**kwargs):
    return CatalystwanClient().getDeviceRunningConfigHTML(**kwargs)

@register('getDeviceConfigurationCommitList')
def getDeviceConfigurationCommitList(**kwargs):
    return CatalystwanClient().getDeviceConfigurationCommitList(**kwargs)

@register('getAffinityConfig')
def getAffinityConfig(**kwargs):
    return CatalystwanClient().getAffinityConfig(**kwargs)

@register('getAffinityStatus')
def getAffinityStatus(**kwargs):
    return CatalystwanClient().getAffinityStatus(**kwargs)

@register('createRealTimeConnectionList')
def createRealTimeConnectionList(**kwargs):
    return CatalystwanClient().createRealTimeConnectionList(**kwargs)

@register('createConnectionHistoryListRealTime')
def createConnectionHistoryListRealTime(**kwargs):
    return CatalystwanClient().createConnectionHistoryListRealTime(**kwargs)

@register('createRealTimeConnectionList_1')
def createRealTimeConnectionList_1(**kwargs):
    return CatalystwanClient().createRealTimeConnectionList_1(**kwargs)

@register('getTotalCountForDeviceStates')
def getTotalCountForDeviceStates(**kwargs):
    return CatalystwanClient().getTotalCountForDeviceStates(**kwargs)

@register('createLinkList')
def createLinkList(**kwargs):
    return CatalystwanClient().createLinkList(**kwargs)

@register('createLocalPropertiesListListRealTIme')
def createLocalPropertiesListListRealTIme(**kwargs):
    return CatalystwanClient().createLocalPropertiesListListRealTIme(**kwargs)

@register('networkSummary')
def networkSummary(**kwargs):
    return CatalystwanClient().networkSummary(**kwargs)

@register('createRealTimeRegionConnectionList')
def createRealTimeRegionConnectionList(**kwargs):
    return CatalystwanClient().createRealTimeRegionConnectionList(**kwargs)

@register('getConnectionStatistics')
def getConnectionStatistics(**kwargs):
    return CatalystwanClient().getConnectionStatistics(**kwargs)

@register('getLocalDeviceStatus')
def getLocalDeviceStatus(**kwargs):
    return CatalystwanClient().getLocalDeviceStatus(**kwargs)

@register('createConnectionsSummary')
def createConnectionsSummary(**kwargs):
    return CatalystwanClient().createConnectionsSummary(**kwargs)

@register('getDeviceControlStatusSummary')
def getDeviceControlStatusSummary(**kwargs):
    return CatalystwanClient().getDeviceControlStatusSummary(**kwargs)

@register('createSyncedConnectionList')
def createSyncedConnectionList(**kwargs):
    return CatalystwanClient().createSyncedConnectionList(**kwargs)

@register('createLocalPropertiesSyncedList')
def createLocalPropertiesSyncedList(**kwargs):
    return CatalystwanClient().createLocalPropertiesSyncedList(**kwargs)

@register('createWanInterfaceSyncedList')
def createWanInterfaceSyncedList(**kwargs):
    return CatalystwanClient().createWanInterfaceSyncedList(**kwargs)

@register('createValidDevicesListRealTime')
def createValidDevicesListRealTime(**kwargs):
    return CatalystwanClient().createValidDevicesListRealTime(**kwargs)

@register('getValidVManageIdRealTime')
def getValidVManageIdRealTime(**kwargs):
    return CatalystwanClient().getValidVManageIdRealTime(**kwargs)

@register('createValidVSmartsListRealTime')
def createValidVSmartsListRealTime(**kwargs):
    return CatalystwanClient().createValidVSmartsListRealTime(**kwargs)

@register('createWanInterfaceListList')
def createWanInterfaceListList(**kwargs):
    return CatalystwanClient().createWanInterfaceListList(**kwargs)

@register('getPortHopColor')
def getPortHopColor(**kwargs):
    return CatalystwanClient().getPortHopColor(**kwargs)

@register('getDeviceCounters')
def getDeviceCounters(**kwargs):
    return CatalystwanClient().getDeviceCounters(**kwargs)

@register('getDeviceCrashLogs')
def getDeviceCrashLogs(**kwargs):
    return CatalystwanClient().getDeviceCrashLogs(**kwargs)

@register('getAllDeviceCrashLogs')
def getAllDeviceCrashLogs(**kwargs):
    return CatalystwanClient().getAllDeviceCrashLogs(**kwargs)

@register('getDeviceCrashInformation')
def getDeviceCrashInformation(**kwargs):
    return CatalystwanClient().getDeviceCrashInformation(**kwargs)

@register('getDeviceCrashLogsSynced')
def getDeviceCrashLogsSynced(**kwargs):
    return CatalystwanClient().getDeviceCrashLogsSynced(**kwargs)

@register('createDeviceContainersInfo')
def createDeviceContainersInfo(**kwargs):
    return CatalystwanClient().createDeviceContainersInfo(**kwargs)

@register('getPnicStats')
def getPnicStats(**kwargs):
    return CatalystwanClient().getPnicStats(**kwargs)

@register('getPNICStatsFromDevice')
def getPNICStatsFromDevice(**kwargs):
    return CatalystwanClient().getPNICStatsFromDevice(**kwargs)

@register('getRBACInterface')
def getRBACInterface(**kwargs):
    return CatalystwanClient().getRBACInterface(**kwargs)

@register('getAllocationInfo')
def getAllocationInfo(**kwargs):
    return CatalystwanClient().getAllocationInfo(**kwargs)

@register('getCPUInfo')
def getCPUInfo(**kwargs):
    return CatalystwanClient().getCPUInfo(**kwargs)

@register('getVNFInfo')
def getVNFInfo(**kwargs):
    return CatalystwanClient().getVNFInfo(**kwargs)

@register('createDeviceSystemSettingNativeInfo')
def createDeviceSystemSettingNativeInfo(**kwargs):
    return CatalystwanClient().createDeviceSystemSettingNativeInfo(**kwargs)

@register('createDeviceSystemProcessList')
def createDeviceSystemProcessList(**kwargs):
    return CatalystwanClient().createDeviceSystemProcessList(**kwargs)

@register('createDeviceSystemSetting')
def createDeviceSystemSetting(**kwargs):
    return CatalystwanClient().createDeviceSystemSetting(**kwargs)

@register('createDeviceSystemStatus')
def createDeviceSystemStatus(**kwargs):
    return CatalystwanClient().createDeviceSystemStatus(**kwargs)

@register('getCtsPac')
def getCtsPac(**kwargs):
    return CatalystwanClient().getCtsPac(**kwargs)

@register('getDeviceOnlyStatus')
def getDeviceOnlyStatus(**kwargs):
    return CatalystwanClient().getDeviceOnlyStatus(**kwargs)

@register('getDHCPClient')
def getDHCPClient(**kwargs):
    return CatalystwanClient().getDHCPClient(**kwargs)

@register('getDHCPInterface')
def getDHCPInterface(**kwargs):
    return CatalystwanClient().getDHCPInterface(**kwargs)

@register('getDHCPServer')
def getDHCPServer(**kwargs):
    return CatalystwanClient().getDHCPServer(**kwargs)

@register('getDHCPv6Interface')
def getDHCPv6Interface(**kwargs):
    return CatalystwanClient().getDHCPv6Interface(**kwargs)

@register('getWLANDOT1xClients')
def getWLANDOT1xClients(**kwargs):
    return CatalystwanClient().getWLANDOT1xClients(**kwargs)

@register('getWLANDOT1xInterfaces')
def getWLANDOT1xInterfaces(**kwargs):
    return CatalystwanClient().getWLANDOT1xInterfaces(**kwargs)

@register('getDOT1xRadius')
def getDOT1xRadius(**kwargs):
    return CatalystwanClient().getDOT1xRadius(**kwargs)

@register('createSoftwareList')
def createSoftwareList(**kwargs):
    return CatalystwanClient().createSoftwareList(**kwargs)

@register('getSupportedApplicationList')
def getSupportedApplicationList(**kwargs):
    return CatalystwanClient().getSupportedApplicationList(**kwargs)

@register('getDPIDeviceFieldJSON')
def getDPIDeviceFieldJSON(**kwargs):
    return CatalystwanClient().getDPIDeviceFieldJSON(**kwargs)

@register('createDPICollectorList')
def createDPICollectorList(**kwargs):
    return CatalystwanClient().createDPICollectorList(**kwargs)

@register('getCommonApplicationList')
def getCommonApplicationList(**kwargs):
    return CatalystwanClient().getCommonApplicationList(**kwargs)

@register('getDPIFieldJSON')
def getDPIFieldJSON(**kwargs):
    return CatalystwanClient().getDPIFieldJSON(**kwargs)

@register('getDPIDeviceDetailsFieldJSON')
def getDPIDeviceDetailsFieldJSON(**kwargs):
    return CatalystwanClient().getDPIDeviceDetailsFieldJSON(**kwargs)

@register('createDPIFlowsList')
def createDPIFlowsList(**kwargs):
    return CatalystwanClient().createDPIFlowsList(**kwargs)

@register('getQosmosStaticApplicationList')
def getQosmosStaticApplicationList(**kwargs):
    return CatalystwanClient().getQosmosStaticApplicationList(**kwargs)

@register('getQosmosApplicationList')
def getQosmosApplicationList(**kwargs):
    return CatalystwanClient().getQosmosApplicationList(**kwargs)

@register('createDPISummaryRealTime')
def createDPISummaryRealTime(**kwargs):
    return CatalystwanClient().createDPISummaryRealTime(**kwargs)

@register('createDPIStatistics')
def createDPIStatistics(**kwargs):
    return CatalystwanClient().createDPIStatistics(**kwargs)

@register('getDreAutoBypassStats')
def getDreAutoBypassStats(**kwargs):
    return CatalystwanClient().getDreAutoBypassStats(**kwargs)

@register('getDreStats')
def getDreStats(**kwargs):
    return CatalystwanClient().getDreStats(**kwargs)

@register('getDreStatus')
def getDreStatus(**kwargs):
    return CatalystwanClient().getDreStatus(**kwargs)

@register('getDrePeerStats')
def getDrePeerStats(**kwargs):
    return CatalystwanClient().getDrePeerStats(**kwargs)

@register('getDualStaticRouteTrackerInfo')
def getDualStaticRouteTrackerInfo(**kwargs):
    return CatalystwanClient().getDualStaticRouteTrackerInfo(**kwargs)

@register('createEIGRPInterface')
def createEIGRPInterface(**kwargs):
    return CatalystwanClient().createEIGRPInterface(**kwargs)

@register('createEIGRPRoute')
def createEIGRPRoute(**kwargs):
    return CatalystwanClient().createEIGRPRoute(**kwargs)

@register('createEIGRPTopology')
def createEIGRPTopology(**kwargs):
    return CatalystwanClient().createEIGRPTopology(**kwargs)

@register('getEndpointTrackerInfo')
def getEndpointTrackerInfo(**kwargs):
    return CatalystwanClient().getEndpointTrackerInfo(**kwargs)

@register('getEndpointTrackerGroupInfo')
def getEndpointTrackerGroupInfo(**kwargs):
    return CatalystwanClient().getEndpointTrackerGroupInfo(**kwargs)

@register('getEnvironmentData')
def getEnvironmentData(**kwargs):
    return CatalystwanClient().getEnvironmentData(**kwargs)

@register('getRadiusServer')
def getRadiusServer(**kwargs):
    return CatalystwanClient().getRadiusServer(**kwargs)

@register('getFeatureList')
def getFeatureList(**kwargs):
    return CatalystwanClient().getFeatureList(**kwargs)

@register('getSyncedFeatureList')
def getSyncedFeatureList(**kwargs):
    return CatalystwanClient().getSyncedFeatureList(**kwargs)

@register('getDataCollectionStatusForDevice')
def getDataCollectionStatusForDevice(**kwargs):
    return CatalystwanClient().getDataCollectionStatusForDevice(**kwargs)

@register('downloadGeneratedFile')
def downloadGeneratedFile(**kwargs):
    return CatalystwanClient().downloadGeneratedFile(**kwargs)

@register('getDataCollectionStatusForUUID')
def getDataCollectionStatusForUUID(**kwargs):
    return CatalystwanClient().getDataCollectionStatusForUUID(**kwargs)

@register('getSupportedCommandsList')
def getSupportedCommandsList(**kwargs):
    return CatalystwanClient().getSupportedCommandsList(**kwargs)

@register('getGeofenceStatus')
def getGeofenceStatus(**kwargs):
    return CatalystwanClient().getGeofenceStatus(**kwargs)

@register('createAlarmList')
def createAlarmList(**kwargs):
    return CatalystwanClient().createAlarmList(**kwargs)

@register('createEnvironmentList')
def createEnvironmentList(**kwargs):
    return CatalystwanClient().createEnvironmentList(**kwargs)

@register('createErrorAlarmList')
def createErrorAlarmList(**kwargs):
    return CatalystwanClient().createErrorAlarmList(**kwargs)

@register('createInventoryList')
def createInventoryList(**kwargs):
    return CatalystwanClient().createInventoryList(**kwargs)

@register('createStatusSummary')
def createStatusSummary(**kwargs):
    return CatalystwanClient().createStatusSummary(**kwargs)

@register('createSyncedAlarmList')
def createSyncedAlarmList(**kwargs):
    return CatalystwanClient().createSyncedAlarmList(**kwargs)

@register('createSyncedEnvironmentList')
def createSyncedEnvironmentList(**kwargs):
    return CatalystwanClient().createSyncedEnvironmentList(**kwargs)

@register('createSyncedInventoryList')
def createSyncedInventoryList(**kwargs):
    return CatalystwanClient().createSyncedInventoryList(**kwargs)

@register('createSystemList')
def createSystemList(**kwargs):
    return CatalystwanClient().createSystemList(**kwargs)

@register('createTempThresholdList')
def createTempThresholdList(**kwargs):
    return CatalystwanClient().createTempThresholdList(**kwargs)

@register('getHardwareHealthDetails')
def getHardwareHealthDetails(**kwargs):
    return CatalystwanClient().getHardwareHealthDetails(**kwargs)

@register('getHardwareHealthSummary')
def getHardwareHealthSummary(**kwargs):
    return CatalystwanClient().getHardwareHealthSummary(**kwargs)

@register('getStatDataRawData_21')
def getStatDataRawData_21(**kwargs):
    return CatalystwanClient().getStatDataRawData_21(**kwargs)

@register('getAggregationDataByQuery_23')
def getAggregationDataByQuery_23(**kwargs):
    return CatalystwanClient().getAggregationDataByQuery_23(**kwargs)

@register('getLastThousandConfigList')
def getLastThousandConfigList(**kwargs):
    return CatalystwanClient().getLastThousandConfigList(**kwargs)

@register('getConfigDiff')
def getConfigDiff(**kwargs):
    return CatalystwanClient().getConfigDiff(**kwargs)

@register('getDeviceConfig')
def getDeviceConfig(**kwargs):
    return CatalystwanClient().getDeviceConfig(**kwargs)

@register('getStatDataRawDataAsCSV_21')
def getStatDataRawDataAsCSV_21(**kwargs):
    return CatalystwanClient().getStatDataRawDataAsCSV_21(**kwargs)

@register('getCount_20')
def getCount_20(**kwargs):
    return CatalystwanClient().getCount_20(**kwargs)

@register('getStatDataFields_22')
def getStatDataFields_22(**kwargs):
    return CatalystwanClient().getStatDataFields_22(**kwargs)

@register('getStatsPaginationRawData_19')
def getStatsPaginationRawData_19(**kwargs):
    return CatalystwanClient().getStatsPaginationRawData_19(**kwargs)

@register('getStatQueryFields_23')
def getStatQueryFields_23(**kwargs):
    return CatalystwanClient().getStatQueryFields_23(**kwargs)

@register('createIGMPGroupsList')
def createIGMPGroupsList(**kwargs):
    return CatalystwanClient().createIGMPGroupsList(**kwargs)

@register('createIGMPInterfaceList')
def createIGMPInterfaceList(**kwargs):
    return CatalystwanClient().createIGMPInterfaceList(**kwargs)

@register('createIGMPStatisticsList')
def createIGMPStatisticsList(**kwargs):
    return CatalystwanClient().createIGMPStatisticsList(**kwargs)

@register('createIGMPSummary')
def createIGMPSummary(**kwargs):
    return CatalystwanClient().createIGMPSummary(**kwargs)

@register('getDeviceInterface')
def getDeviceInterface(**kwargs):
    return CatalystwanClient().getDeviceInterface(**kwargs)

@register('getDeviceInterfaceARPStats')
def getDeviceInterfaceARPStats(**kwargs):
    return CatalystwanClient().getDeviceInterfaceARPStats(**kwargs)

@register('getDeviceInterfaceErrorStats')
def getDeviceInterfaceErrorStats(**kwargs):
    return CatalystwanClient().getDeviceInterfaceErrorStats(**kwargs)

@register('getDeviceInterfaceIpv6Stats')
def getDeviceInterfaceIpv6Stats(**kwargs):
    return CatalystwanClient().getDeviceInterfaceIpv6Stats(**kwargs)

@register('getDeviceInterfacePktSizes')
def getDeviceInterfacePktSizes(**kwargs):
    return CatalystwanClient().getDeviceInterfacePktSizes(**kwargs)

@register('getDeviceInterfacePortStats')
def getDeviceInterfacePortStats(**kwargs):
    return CatalystwanClient().getDeviceInterfacePortStats(**kwargs)

@register('getDeviceInterfaceQosStats')
def getDeviceInterfaceQosStats(**kwargs):
    return CatalystwanClient().getDeviceInterfaceQosStats(**kwargs)

@register('getDeviceInterfaceQueueStats')
def getDeviceInterfaceQueueStats(**kwargs):
    return CatalystwanClient().getDeviceInterfaceQueueStats(**kwargs)

@register('getDeviceSerialInterface')
def getDeviceSerialInterface(**kwargs):
    return CatalystwanClient().getDeviceSerialInterface(**kwargs)

@register('getDeviceInterfaceStats')
def getDeviceInterfaceStats(**kwargs):
    return CatalystwanClient().getDeviceInterfaceStats(**kwargs)

@register('getSyncedDeviceInterface')
def getSyncedDeviceInterface(**kwargs):
    return CatalystwanClient().getSyncedDeviceInterface(**kwargs)

@register('trustsec')
def trustsec(**kwargs):
    return CatalystwanClient().trustsec(**kwargs)

@register('generateDeviceInterfaceVPN')
def generateDeviceInterfaceVPN(**kwargs):
    return CatalystwanClient().generateDeviceInterfaceVPN(**kwargs)

@register('createFibList')
def createFibList(**kwargs):
    return CatalystwanClient().createFibList(**kwargs)

@register('createIetfRoutingList')
def createIetfRoutingList(**kwargs):
    return CatalystwanClient().createIetfRoutingList(**kwargs)

@register('createIPMfibOilList')
def createIPMfibOilList(**kwargs):
    return CatalystwanClient().createIPMfibOilList(**kwargs)

@register('createIPMfibStatsList')
def createIPMfibStatsList(**kwargs):
    return CatalystwanClient().createIPMfibStatsList(**kwargs)

@register('createIPMfibSummaryList')
def createIPMfibSummaryList(**kwargs):
    return CatalystwanClient().createIPMfibSummaryList(**kwargs)

@register('createNatFilterList')
def createNatFilterList(**kwargs):
    return CatalystwanClient().createNatFilterList(**kwargs)

@register('createNatInterfaceList')
def createNatInterfaceList(**kwargs):
    return CatalystwanClient().createNatInterfaceList(**kwargs)

@register('createNatInterfaceStatisticsList')
def createNatInterfaceStatisticsList(**kwargs):
    return CatalystwanClient().createNatInterfaceStatisticsList(**kwargs)

@register('createNatTranslationList')
def createNatTranslationList(**kwargs):
    return CatalystwanClient().createNatTranslationList(**kwargs)

@register('createNat64TranslationList')
def createNat64TranslationList(**kwargs):
    return CatalystwanClient().createNat64TranslationList(**kwargs)

@register('createRouteTableList')
def createRouteTableList(**kwargs):
    return CatalystwanClient().createRouteTableList(**kwargs)

@register('createIPv4FibList')
def createIPv4FibList(**kwargs):
    return CatalystwanClient().createIPv4FibList(**kwargs)

@register('createIPv6FibList')
def createIPv6FibList(**kwargs):
    return CatalystwanClient().createIPv6FibList(**kwargs)

@register('createCryptoIpsecIdentity')
def createCryptoIpsecIdentity(**kwargs):
    return CatalystwanClient().createCryptoIpsecIdentity(**kwargs)

@register('createIkeInboundList')
def createIkeInboundList(**kwargs):
    return CatalystwanClient().createIkeInboundList(**kwargs)

@register('createIkeOutboundList')
def createIkeOutboundList(**kwargs):
    return CatalystwanClient().createIkeOutboundList(**kwargs)

@register('createIkeSessions')
def createIkeSessions(**kwargs):
    return CatalystwanClient().createIkeSessions(**kwargs)

@register('createCryptov1LocalSAList')
def createCryptov1LocalSAList(**kwargs):
    return CatalystwanClient().createCryptov1LocalSAList(**kwargs)

@register('createCryptov2LocalSAList')
def createCryptov2LocalSAList(**kwargs):
    return CatalystwanClient().createCryptov2LocalSAList(**kwargs)

@register('createInBoundList')
def createInBoundList(**kwargs):
    return CatalystwanClient().createInBoundList(**kwargs)

@register('createLocalSAList')
def createLocalSAList(**kwargs):
    return CatalystwanClient().createLocalSAList(**kwargs)

@register('createOutBoundList')
def createOutBoundList(**kwargs):
    return CatalystwanClient().createOutBoundList(**kwargs)

@register('createIPsecPWKInboundConnections')
def createIPsecPWKInboundConnections(**kwargs):
    return CatalystwanClient().createIPsecPWKInboundConnections(**kwargs)

@register('createIPsecPWKLocalSA')
def createIPsecPWKLocalSA(**kwargs):
    return CatalystwanClient().createIPsecPWKLocalSA(**kwargs)

@register('createIPsecPWKOutboundConnections')
def createIPsecPWKOutboundConnections(**kwargs):
    return CatalystwanClient().createIPsecPWKOutboundConnections(**kwargs)

@register('getIpv6Data')
def getIpv6Data(**kwargs):
    return CatalystwanClient().getIpv6Data(**kwargs)

@register('getDeviceListAsKeyValue')
def getDeviceListAsKeyValue(**kwargs):
    return CatalystwanClient().getDeviceListAsKeyValue(**kwargs)

@register('getLacpInterfaceList')
def getLacpInterfaceList(**kwargs):
    return CatalystwanClient().getLacpInterfaceList(**kwargs)

@register('getLacpMembers')
def getLacpMembers(**kwargs):
    return CatalystwanClient().getLacpMembers(**kwargs)

@register('getLicenseEvalInfo')
def getLicenseEvalInfo(**kwargs):
    return CatalystwanClient().getLicenseEvalInfo(**kwargs)

@register('getLicensePAKInfo')
def getLicensePAKInfo(**kwargs):
    return CatalystwanClient().getLicensePAKInfo(**kwargs)

@register('getLicensePrivacyInfo')
def getLicensePrivacyInfo(**kwargs):
    return CatalystwanClient().getLicensePrivacyInfo(**kwargs)

@register('getLicenseRegInfo')
def getLicenseRegInfo(**kwargs):
    return CatalystwanClient().getLicenseRegInfo(**kwargs)

@register('getLicenseUDIInfo')
def getLicenseUDIInfo(**kwargs):
    return CatalystwanClient().getLicenseUDIInfo(**kwargs)

@register('getLicenseUsageInfo')
def getLicenseUsageInfo(**kwargs):
    return CatalystwanClient().getLicenseUsageInfo(**kwargs)

@register('getLoggingFromDevice')
def getLoggingFromDevice(**kwargs):
    return CatalystwanClient().getLoggingFromDevice(**kwargs)

@register('listAllDeviceModels')
def listAllDeviceModels(**kwargs):
    return CatalystwanClient().listAllDeviceModels(**kwargs)

@register('getDeviceModels')
def getDeviceModels(**kwargs):
    return CatalystwanClient().getDeviceModels(**kwargs)

@register('listAllMonitorDetailsDevices')
def listAllMonitorDetailsDevices(**kwargs):
    return CatalystwanClient().listAllMonitorDetailsDevices(**kwargs)

@register('createReplicatorList')
def createReplicatorList(**kwargs):
    return CatalystwanClient().createReplicatorList(**kwargs)

@register('createRpfList')
def createRpfList(**kwargs):
    return CatalystwanClient().createRpfList(**kwargs)

@register('createTopologyList')
def createTopologyList(**kwargs):
    return CatalystwanClient().createTopologyList(**kwargs)

@register('createPimTunnelList')
def createPimTunnelList(**kwargs):
    return CatalystwanClient().createPimTunnelList(**kwargs)

@register('getIpv6Interface')
def getIpv6Interface(**kwargs):
    return CatalystwanClient().getIpv6Interface(**kwargs)

@register('getRunning')
def getRunning(**kwargs):
    return CatalystwanClient().getRunning(**kwargs)

@register('createAssociationsList')
def createAssociationsList(**kwargs):
    return CatalystwanClient().createAssociationsList(**kwargs)

@register('createPeerList')
def createPeerList(**kwargs):
    return CatalystwanClient().createPeerList(**kwargs)

@register('createNTPStatusList')
def createNTPStatusList(**kwargs):
    return CatalystwanClient().createNTPStatusList(**kwargs)

@register('createOMPCloudXRecv')
def createOMPCloudXRecv(**kwargs):
    return CatalystwanClient().createOMPCloudXRecv(**kwargs)

@register('createOMPLinkList')
def createOMPLinkList(**kwargs):
    return CatalystwanClient().createOMPLinkList(**kwargs)

@register('createOMPMcastAutoDiscoverAdvt')
def createOMPMcastAutoDiscoverAdvt(**kwargs):
    return CatalystwanClient().createOMPMcastAutoDiscoverAdvt(**kwargs)

@register('createOMPMcastAutoDiscoverRecv')
def createOMPMcastAutoDiscoverRecv(**kwargs):
    return CatalystwanClient().createOMPMcastAutoDiscoverRecv(**kwargs)

@register('createOMPMcastRoutesAdvt')
def createOMPMcastRoutesAdvt(**kwargs):
    return CatalystwanClient().createOMPMcastRoutesAdvt(**kwargs)

@register('createOMPMcastRoutesRecv')
def createOMPMcastRoutesRecv(**kwargs):
    return CatalystwanClient().createOMPMcastRoutesRecv(**kwargs)

@register('createOMPSessionList')
def createOMPSessionList(**kwargs):
    return CatalystwanClient().createOMPSessionList(**kwargs)

@register('createAdvertisedRoutesList')
def createAdvertisedRoutesList(**kwargs):
    return CatalystwanClient().createAdvertisedRoutesList(**kwargs)

@register('createAdvertisedRoutesListIpv6')
def createAdvertisedRoutesListIpv6(**kwargs):
    return CatalystwanClient().createAdvertisedRoutesListIpv6(**kwargs)

@register('createReceivedRoutesList')
def createReceivedRoutesList(**kwargs):
    return CatalystwanClient().createReceivedRoutesList(**kwargs)

@register('createReceivedRoutesListIpv6')
def createReceivedRoutesListIpv6(**kwargs):
    return CatalystwanClient().createReceivedRoutesListIpv6(**kwargs)

@register('createOMPServices')
def createOMPServices(**kwargs):
    return CatalystwanClient().createOMPServices(**kwargs)

@register('getDeviceOMPStatus')
def getDeviceOMPStatus(**kwargs):
    return CatalystwanClient().getDeviceOMPStatus(**kwargs)

@register('createOMPSummary')
def createOMPSummary(**kwargs):
    return CatalystwanClient().createOMPSummary(**kwargs)

@register('createSyncedOMPSessionList')
def createSyncedOMPSessionList(**kwargs):
    return CatalystwanClient().createSyncedOMPSessionList(**kwargs)

@register('createAdvertisedTlocsList')
def createAdvertisedTlocsList(**kwargs):
    return CatalystwanClient().createAdvertisedTlocsList(**kwargs)

@register('createReceivedTlocsList')
def createReceivedTlocsList(**kwargs):
    return CatalystwanClient().createReceivedTlocsList(**kwargs)

@register('getOnDemandLocal')
def getOnDemandLocal(**kwargs):
    return CatalystwanClient().getOnDemandLocal(**kwargs)

@register('getOnDemandRemote')
def getOnDemandRemote(**kwargs):
    return CatalystwanClient().getOnDemandRemote(**kwargs)

@register('createConnectionListFromDevice')
def createConnectionListFromDevice(**kwargs):
    return CatalystwanClient().createConnectionListFromDevice(**kwargs)

@register('createConnectionHistoryList')
def createConnectionHistoryList(**kwargs):
    return CatalystwanClient().createConnectionHistoryList(**kwargs)

@register('createLocalPropertiesListList')
def createLocalPropertiesListList(**kwargs):
    return CatalystwanClient().createLocalPropertiesListList(**kwargs)

@register('createReverseProxyMappingList')
def createReverseProxyMappingList(**kwargs):
    return CatalystwanClient().createReverseProxyMappingList(**kwargs)

@register('getStatistics')
def getStatistics(**kwargs):
    return CatalystwanClient().getStatistics(**kwargs)

@register('createConnectionSummary')
def createConnectionSummary(**kwargs):
    return CatalystwanClient().createConnectionSummary(**kwargs)

@register('createValidDevicesList')
def createValidDevicesList(**kwargs):
    return CatalystwanClient().createValidDevicesList(**kwargs)

@register('getValidVManageId')
def getValidVManageId(**kwargs):
    return CatalystwanClient().getValidVManageId(**kwargs)

@register('createValidVSmartsList')
def createValidVSmartsList(**kwargs):
    return CatalystwanClient().createValidVSmartsList(**kwargs)

@register('createOSPFDatabaseList')
def createOSPFDatabaseList(**kwargs):
    return CatalystwanClient().createOSPFDatabaseList(**kwargs)

@register('createOSPFDatabaseExternal')
def createOSPFDatabaseExternal(**kwargs):
    return CatalystwanClient().createOSPFDatabaseExternal(**kwargs)

@register('createOSPFDatabaseSummaryList')
def createOSPFDatabaseSummaryList(**kwargs):
    return CatalystwanClient().createOSPFDatabaseSummaryList(**kwargs)

@register('createOSPFInterface')
def createOSPFInterface(**kwargs):
    return CatalystwanClient().createOSPFInterface(**kwargs)

@register('createOSPFNeighbors')
def createOSPFNeighbors(**kwargs):
    return CatalystwanClient().createOSPFNeighbors(**kwargs)

@register('createOSPFProcess')
def createOSPFProcess(**kwargs):
    return CatalystwanClient().createOSPFProcess(**kwargs)

@register('createOSPFRoutesList')
def createOSPFRoutesList(**kwargs):
    return CatalystwanClient().createOSPFRoutesList(**kwargs)

@register('createOSPFv3Interface')
def createOSPFv3Interface(**kwargs):
    return CatalystwanClient().createOSPFv3Interface(**kwargs)

@register('createOSPFv3Neighbors')
def createOSPFv3Neighbors(**kwargs):
    return CatalystwanClient().createOSPFv3Neighbors(**kwargs)

@register('createPIMInterfaceList')
def createPIMInterfaceList(**kwargs):
    return CatalystwanClient().createPIMInterfaceList(**kwargs)

@register('createPIMNeighborList')
def createPIMNeighborList(**kwargs):
    return CatalystwanClient().createPIMNeighborList(**kwargs)

@register('createPIMRpMappingList')
def createPIMRpMappingList(**kwargs):
    return CatalystwanClient().createPIMRpMappingList(**kwargs)

@register('createPIMStatisticsList')
def createPIMStatisticsList(**kwargs):
    return CatalystwanClient().createPIMStatisticsList(**kwargs)

@register('getDevicePkiTrustpoint')
def getDevicePkiTrustpoint(**kwargs):
    return CatalystwanClient().getDevicePkiTrustpoint(**kwargs)

@register('getPolicedInterface')
def getPolicedInterface(**kwargs):
    return CatalystwanClient().getPolicedInterface(**kwargs)

@register('createPolicyAccessListAssociations')
def createPolicyAccessListAssociations(**kwargs):
    return CatalystwanClient().createPolicyAccessListAssociations(**kwargs)

@register('createPolicyAccessListCounters')
def createPolicyAccessListCounters(**kwargs):
    return CatalystwanClient().createPolicyAccessListCounters(**kwargs)

@register('createPolicyAccessListNames')
def createPolicyAccessListNames(**kwargs):
    return CatalystwanClient().createPolicyAccessListNames(**kwargs)

@register('createPolicyAccessListPolicers')
def createPolicyAccessListPolicers(**kwargs):
    return CatalystwanClient().createPolicyAccessListPolicers(**kwargs)

@register('createPolicyAppRoutePolicyFilter')
def createPolicyAppRoutePolicyFilter(**kwargs):
    return CatalystwanClient().createPolicyAppRoutePolicyFilter(**kwargs)

@register('createPolicDataPolicyFilter')
def createPolicDataPolicyFilter(**kwargs):
    return CatalystwanClient().createPolicDataPolicyFilter(**kwargs)

@register('createPolicyFilterMemoryUsage')
def createPolicyFilterMemoryUsage(**kwargs):
    return CatalystwanClient().createPolicyFilterMemoryUsage(**kwargs)

@register('showVsmartIptoSgtBinding')
def showVsmartIptoSgtBinding(**kwargs):
    return CatalystwanClient().showVsmartIptoSgtBinding(**kwargs)

@register('showVsmartIptoUserBinding')
def showVsmartIptoUserBinding(**kwargs):
    return CatalystwanClient().showVsmartIptoUserBinding(**kwargs)

@register('createPolicyAccessListAssociationsIpv6')
def createPolicyAccessListAssociationsIpv6(**kwargs):
    return CatalystwanClient().createPolicyAccessListAssociationsIpv6(**kwargs)

@register('createPolicyAccessListCountersIpv6')
def createPolicyAccessListCountersIpv6(**kwargs):
    return CatalystwanClient().createPolicyAccessListCountersIpv6(**kwargs)

@register('createPolicyAccessListNamesIpv6')
def createPolicyAccessListNamesIpv6(**kwargs):
    return CatalystwanClient().createPolicyAccessListNamesIpv6(**kwargs)

@register('createPolicyAccessListPolicersIpv6')
def createPolicyAccessListPolicersIpv6(**kwargs):
    return CatalystwanClient().createPolicyAccessListPolicersIpv6(**kwargs)

@register('showVsmartPxGridStatus')
def showVsmartPxGridStatus(**kwargs):
    return CatalystwanClient().showVsmartPxGridStatus(**kwargs)

@register('showVsmartPxGridUserSessions')
def showVsmartPxGridUserSessions(**kwargs):
    return CatalystwanClient().showVsmartPxGridUserSessions(**kwargs)

@register('createPolicQosMapInfo')
def createPolicQosMapInfo(**kwargs):
    return CatalystwanClient().createPolicQosMapInfo(**kwargs)

@register('createPolicQosSchedulerInfo')
def createPolicQosSchedulerInfo(**kwargs):
    return CatalystwanClient().createPolicQosSchedulerInfo(**kwargs)

@register('createPolicyRewriteAssociationsInfo')
def createPolicyRewriteAssociationsInfo(**kwargs):
    return CatalystwanClient().createPolicyRewriteAssociationsInfo(**kwargs)

@register('showVsmartUserUsergroupBindings')
def showVsmartUserUsergroupBindings(**kwargs):
    return CatalystwanClient().showVsmartUserUsergroupBindings(**kwargs)

@register('showSdwanPolicyFromVsmart')
def showSdwanPolicyFromVsmart(**kwargs):
    return CatalystwanClient().showSdwanPolicyFromVsmart(**kwargs)

@register('getZoneDropStatistics')
def getZoneDropStatistics(**kwargs):
    return CatalystwanClient().getZoneDropStatistics(**kwargs)

@register('getZbfwStatistics')
def getZbfwStatistics(**kwargs):
    return CatalystwanClient().getZbfwStatistics(**kwargs)

@register('getZonePairSessions')
def getZonePairSessions(**kwargs):
    return CatalystwanClient().getZonePairSessions(**kwargs)

@register('getZonePairs')
def getZonePairs(**kwargs):
    return CatalystwanClient().getZonePairs(**kwargs)

@register('getZonePolicyFilters')
def getZonePolicyFilters(**kwargs):
    return CatalystwanClient().getZonePolicyFilters(**kwargs)

@register('getPowerConsumption')
def getPowerConsumption(**kwargs):
    return CatalystwanClient().getPowerConsumption(**kwargs)

@register('createPPPInterfaceList')
def createPPPInterfaceList(**kwargs):
    return CatalystwanClient().createPPPInterfaceList(**kwargs)

@register('createPPPoEInterfaceList')
def createPPPoEInterfaceList(**kwargs):
    return CatalystwanClient().createPPPoEInterfaceList(**kwargs)

@register('createPPPoENeighborList')
def createPPPoENeighborList(**kwargs):
    return CatalystwanClient().createPPPoENeighborList(**kwargs)

@register('cpustat')
def cpustat(**kwargs):
    return CatalystwanClient().cpustat(**kwargs)

@register('memstat')
def memstat(**kwargs):
    return CatalystwanClient().memstat(**kwargs)

@register('getSyncQueues')
def getSyncQueues(**kwargs):
    return CatalystwanClient().getSyncQueues(**kwargs)

@register('listReachableDevices')
def listReachableDevices(**kwargs):
    return CatalystwanClient().listReachableDevices(**kwargs)

@register('createRebootHistoryList')
def createRebootHistoryList(**kwargs):
    return CatalystwanClient().createRebootHistoryList(**kwargs)

@register('getRebootHistoryDetails')
def getRebootHistoryDetails(**kwargs):
    return CatalystwanClient().getRebootHistoryDetails(**kwargs)

@register('createSyncedRebootHistoryList')
def createSyncedRebootHistoryList(**kwargs):
    return CatalystwanClient().createSyncedRebootHistoryList(**kwargs)

@register('getRedundancyGroupAppGroup')
def getRedundancyGroupAppGroup(**kwargs):
    return CatalystwanClient().getRedundancyGroupAppGroup(**kwargs)

@register('getRoleBasedCounters')
def getRoleBasedCounters(**kwargs):
    return CatalystwanClient().getRoleBasedCounters(**kwargs)

@register('getRoleBasedIpv6Counters')
def getRoleBasedIpv6Counters(**kwargs):
    return CatalystwanClient().getRoleBasedIpv6Counters(**kwargs)

@register('getRoleBasedIpv6Permissions')
def getRoleBasedIpv6Permissions(**kwargs):
    return CatalystwanClient().getRoleBasedIpv6Permissions(**kwargs)

@register('getRoleBasedPermissions')
def getRoleBasedPermissions(**kwargs):
    return CatalystwanClient().getRoleBasedPermissions(**kwargs)

@register('getRoleBasedSgtMap')
def getRoleBasedSgtMap(**kwargs):
    return CatalystwanClient().getRoleBasedSgtMap(**kwargs)

@register('getSDWanGlobalDropStatistics')
def getSDWanGlobalDropStatistics(**kwargs):
    return CatalystwanClient().getSDWanGlobalDropStatistics(**kwargs)

@register('getSDWanStats')
def getSDWanStats(**kwargs):
    return CatalystwanClient().getSDWanStats(**kwargs)

@register('createSessionList')
def createSessionList(**kwargs):
    return CatalystwanClient().createSessionList(**kwargs)

@register('getDetail')
def getDetail(**kwargs):
    return CatalystwanClient().getDetail(**kwargs)

@register('getDiagnostic')
def getDiagnostic(**kwargs):
    return CatalystwanClient().getDiagnostic(**kwargs)

@register('getDiagnosticMeasurementAlarm')
def getDiagnosticMeasurementAlarm(**kwargs):
    return CatalystwanClient().getDiagnosticMeasurementAlarm(**kwargs)

@register('getDiagnosticMeasurementValue')
def getDiagnosticMeasurementValue(**kwargs):
    return CatalystwanClient().getDiagnosticMeasurementValue(**kwargs)

@register('getSigTunnelList')
def getSigTunnelList(**kwargs):
    return CatalystwanClient().getSigTunnelList(**kwargs)

@register('getSigTunnelTotal')
def getSigTunnelTotal(**kwargs):
    return CatalystwanClient().getSigTunnelTotal(**kwargs)

@register('tunnelDashboard')
def tunnelDashboard(**kwargs):
    return CatalystwanClient().tunnelDashboard(**kwargs)

@register('getSigUmbrellaTunnels')
def getSigUmbrellaTunnels(**kwargs):
    return CatalystwanClient().getSigUmbrellaTunnels(**kwargs)

@register('getSigZscalerTunnels')
def getSigZscalerTunnels(**kwargs):
    return CatalystwanClient().getSigZscalerTunnels(**kwargs)

@register('createSmuList')
def createSmuList(**kwargs):
    return CatalystwanClient().createSmuList(**kwargs)

@register('createSyncedSmuList')
def createSyncedSmuList(**kwargs):
    return CatalystwanClient().createSyncedSmuList(**kwargs)

@register('getAAAUcreateSoftwareListsers')
def getAAAUcreateSoftwareListsers(**kwargs):
    return CatalystwanClient().getAAAUcreateSoftwareListsers(**kwargs)

@register('createSyncedSoftwareList')
def createSyncedSoftwareList(**kwargs):
    return CatalystwanClient().createSyncedSoftwareList(**kwargs)

@register('getSSETunnel')
def getSSETunnel(**kwargs):
    return CatalystwanClient().getSSETunnel(**kwargs)

@register('getSslProxyStatistics')
def getSslProxyStatistics(**kwargs):
    return CatalystwanClient().getSslProxyStatistics(**kwargs)

@register('getSslProxyStatus')
def getSslProxyStatus(**kwargs):
    return CatalystwanClient().getSslProxyStatus(**kwargs)

@register('getStaticRouteTrackerInfo')
def getStaticRouteTrackerInfo(**kwargs):
    return CatalystwanClient().getStaticRouteTrackerInfo(**kwargs)

@register('getStatsQueues')
def getStatsQueues(**kwargs):
    return CatalystwanClient().getStatsQueues(**kwargs)

@register('getAllDeviceStatus')
def getAllDeviceStatus(**kwargs):
    return CatalystwanClient().getAllDeviceStatus(**kwargs)

@register('getSxpConnections')
def getSxpConnections(**kwargs):
    return CatalystwanClient().getSxpConnections(**kwargs)

@register('listCurrentlySyncingDevices')
def listCurrentlySyncingDevices(**kwargs):
    return CatalystwanClient().listCurrentlySyncingDevices(**kwargs)

@register('getDeviceSystemClock')
def getDeviceSystemClock(**kwargs):
    return CatalystwanClient().getDeviceSystemClock(**kwargs)

@register('createDeviceInfoList')
def createDeviceInfoList(**kwargs):
    return CatalystwanClient().createDeviceInfoList(**kwargs)

@register('createDeviceSystemStatsList')
def createDeviceSystemStatsList(**kwargs):
    return CatalystwanClient().createDeviceSystemStatsList(**kwargs)

@register('createDeviceSystemStatusList')
def createDeviceSystemStatusList(**kwargs):
    return CatalystwanClient().createDeviceSystemStatusList(**kwargs)

@register('createSyncedDeviceSystemStatusList')
def createSyncedDeviceSystemStatusList(**kwargs):
    return CatalystwanClient().createSyncedDeviceSystemStatusList(**kwargs)

@register('getActiveTCPFlows')
def getActiveTCPFlows(**kwargs):
    return CatalystwanClient().getActiveTCPFlows(**kwargs)

@register('getExpiredTCPFlows')
def getExpiredTCPFlows(**kwargs):
    return CatalystwanClient().getExpiredTCPFlows(**kwargs)

@register('getTCPSummary')
def getTCPSummary(**kwargs):
    return CatalystwanClient().getTCPSummary(**kwargs)

@register('getTcpProxyStatistics')
def getTcpProxyStatistics(**kwargs):
    return CatalystwanClient().getTcpProxyStatistics(**kwargs)

@register('getTcpProxyStatus')
def getTcpProxyStatus(**kwargs):
    return CatalystwanClient().getTcpProxyStatus(**kwargs)

@register('getTiers')
def getTiers(**kwargs):
    return CatalystwanClient().getTiers(**kwargs)

@register('getDeviceTlocStatus')
def getDeviceTlocStatus(**kwargs):
    return CatalystwanClient().getDeviceTlocStatus(**kwargs)

@register('getDeviceTlocUtil')
def getDeviceTlocUtil(**kwargs):
    return CatalystwanClient().getDeviceTlocUtil(**kwargs)

@register('getDeviceTlocUtilDetails')
def getDeviceTlocUtilDetails(**kwargs):
    return CatalystwanClient().getDeviceTlocUtilDetails(**kwargs)

@register('downloadAdminTechFile')
def downloadAdminTechFile(**kwargs):
    return CatalystwanClient().downloadAdminTechFile(**kwargs)

@register('getSupportedAdminTechFeatures')
def getSupportedAdminTechFeatures(**kwargs):
    return CatalystwanClient().getSupportedAdminTechFeatures(**kwargs)

@register('listAdminTechs')
def listAdminTechs(**kwargs):
    return CatalystwanClient().listAdminTechs(**kwargs)

@register('getInProgressCount')
def getInProgressCount(**kwargs):
    return CatalystwanClient().getInProgressCount(**kwargs)

@register('getDeviceToolsNetstat')
def getDeviceToolsNetstat(**kwargs):
    return CatalystwanClient().getDeviceToolsNetstat(**kwargs)

@register('getDeviceToolsNSlookup')
def getDeviceToolsNSlookup(**kwargs):
    return CatalystwanClient().getDeviceToolsNSlookup(**kwargs)

@register('getRealTimeinfo')
def getRealTimeinfo(**kwargs):
    return CatalystwanClient().getRealTimeinfo(**kwargs)

@register('getDeviceToolsSS')
def getDeviceToolsSS(**kwargs):
    return CatalystwanClient().getDeviceToolsSS(**kwargs)

@register('getSystemNetfilter')
def getSystemNetfilter(**kwargs):
    return CatalystwanClient().getSystemNetfilter(**kwargs)

@register('createTransportConnectionList')
def createTransportConnectionList(**kwargs):
    return CatalystwanClient().createTransportConnectionList(**kwargs)

@register('createBfdStatisticsList')
def createBfdStatisticsList(**kwargs):
    return CatalystwanClient().createBfdStatisticsList(**kwargs)

@register('createFecStatistics')
def createFecStatistics(**kwargs):
    return CatalystwanClient().createFecStatistics(**kwargs)

@register('createGreKeepalivesList')
def createGreKeepalivesList(**kwargs):
    return CatalystwanClient().createGreKeepalivesList(**kwargs)

@register('createIpsecStatisticsList')
def createIpsecStatisticsList(**kwargs):
    return CatalystwanClient().createIpsecStatisticsList(**kwargs)

@register('createPacketDuplicateStatistics')
def createPacketDuplicateStatistics(**kwargs):
    return CatalystwanClient().createPacketDuplicateStatistics(**kwargs)

@register('createStatisticsList')
def createStatisticsList(**kwargs):
    return CatalystwanClient().createStatisticsList(**kwargs)

@register('createUcseStats')
def createUcseStats(**kwargs):
    return CatalystwanClient().createUcseStats(**kwargs)

@register('getUmbrellaDevReg')
def getUmbrellaDevReg(**kwargs):
    return CatalystwanClient().getUmbrellaDevReg(**kwargs)

@register('getUmbrellaDNSCrypt')
def getUmbrellaDNSCrypt(**kwargs):
    return CatalystwanClient().getUmbrellaDNSCrypt(**kwargs)

@register('getUmbrellaDpStats')
def getUmbrellaDpStats(**kwargs):
    return CatalystwanClient().getUmbrellaDpStats(**kwargs)

@register('getUmbrellaOverview')
def getUmbrellaOverview(**kwargs):
    return CatalystwanClient().getUmbrellaOverview(**kwargs)

@register('getUmbrellaConfig')
def getUmbrellaConfig(**kwargs):
    return CatalystwanClient().getUmbrellaConfig(**kwargs)

@register('getUnclaimedVedges')
def getUnclaimedVedges(**kwargs):
    return CatalystwanClient().getUnclaimedVedges(**kwargs)

@register('getUnconfigured')
def getUnconfigured(**kwargs):
    return CatalystwanClient().getUnconfigured(**kwargs)

@register('listUnreachableDevices')
def listUnreachableDevices(**kwargs):
    return CatalystwanClient().listUnreachableDevices(**kwargs)

@register('getUsersFromDevice')
def getUsersFromDevice(**kwargs):
    return CatalystwanClient().getUsersFromDevice(**kwargs)

@register('getAllDeviceUsers')
def getAllDeviceUsers(**kwargs):
    return CatalystwanClient().getAllDeviceUsers(**kwargs)

@register('getUTDDataplaneConfig')
def getUTDDataplaneConfig(**kwargs):
    return CatalystwanClient().getUTDDataplaneConfig(**kwargs)

@register('getUTDDataplaneGlobal')
def getUTDDataplaneGlobal(**kwargs):
    return CatalystwanClient().getUTDDataplaneGlobal(**kwargs)

@register('getUTDDataplaneStats')
def getUTDDataplaneStats(**kwargs):
    return CatalystwanClient().getUTDDataplaneStats(**kwargs)

@register('getUTDDataplaneStatsSummary')
def getUTDDataplaneStatsSummary(**kwargs):
    return CatalystwanClient().getUTDDataplaneStatsSummary(**kwargs)

@register('getUTDEngineInstanceStatus')
def getUTDEngineInstanceStatus(**kwargs):
    return CatalystwanClient().getUTDEngineInstanceStatus(**kwargs)

@register('getUTDEngineStatus')
def getUTDEngineStatus(**kwargs):
    return CatalystwanClient().getUTDEngineStatus(**kwargs)

@register('getUTDFileAnalysisStatus')
def getUTDFileAnalysisStatus(**kwargs):
    return CatalystwanClient().getUTDFileAnalysisStatus(**kwargs)

@register('getUTDFileReputationStatus')
def getUTDFileReputationStatus(**kwargs):
    return CatalystwanClient().getUTDFileReputationStatus(**kwargs)

@register('getUTDIpsUpdateStatus')
def getUTDIpsUpdateStatus(**kwargs):
    return CatalystwanClient().getUTDIpsUpdateStatus(**kwargs)

@register('getSignatureVersionInfo')
def getSignatureVersionInfo(**kwargs):
    return CatalystwanClient().getSignatureVersionInfo(**kwargs)

@register('getUTDUrlfConnectionStatus')
def getUTDUrlfConnectionStatus(**kwargs):
    return CatalystwanClient().getUTDUrlfConnectionStatus(**kwargs)

@register('getUTDUrlfUpdateStatus')
def getUTDUrlfUpdateStatus(**kwargs):
    return CatalystwanClient().getUTDUrlfUpdateStatus(**kwargs)

@register('getUTDVersionStatus')
def getUTDVersionStatus(**kwargs):
    return CatalystwanClient().getUTDVersionStatus(**kwargs)

@register('getCoLineSpecificStats')
def getCoLineSpecificStats(**kwargs):
    return CatalystwanClient().getCoLineSpecificStats(**kwargs)

@register('getCoStats')
def getCoStats(**kwargs):
    return CatalystwanClient().getCoStats(**kwargs)

@register('getCpeLineSpecificStats')
def getCpeLineSpecificStats(**kwargs):
    return CatalystwanClient().getCpeLineSpecificStats(**kwargs)

@register('getCpeStats')
def getCpeStats(**kwargs):
    return CatalystwanClient().getCpeStats(**kwargs)

@register('getLineBondingStats')
def getLineBondingStats(**kwargs):
    return CatalystwanClient().getLineBondingStats(**kwargs)

@register('getLineSpecificStats')
def getLineSpecificStats(**kwargs):
    return CatalystwanClient().getLineSpecificStats(**kwargs)

@register('getVdslInfo')
def getVdslInfo(**kwargs):
    return CatalystwanClient().getVdslInfo(**kwargs)

@register('getVedgeInventory')
def getVedgeInventory(**kwargs):
    return CatalystwanClient().getVedgeInventory(**kwargs)

@register('getVedgeInventorySummary')
def getVedgeInventorySummary(**kwargs):
    return CatalystwanClient().getVedgeInventorySummary(**kwargs)

@register('createTeList')
def createTeList(**kwargs):
    return CatalystwanClient().createTeList(**kwargs)

@register('createUtdList')
def createUtdList(**kwargs):
    return CatalystwanClient().createUtdList(**kwargs)

@register('createWaasList')
def createWaasList(**kwargs):
    return CatalystwanClient().createWaasList(**kwargs)

@register('getVbranchVMLifecycleNics')
def getVbranchVMLifecycleNics(**kwargs):
    return CatalystwanClient().getVbranchVMLifecycleNics(**kwargs)

@register('getCloudDockVMLifecycleNics')
def getCloudDockVMLifecycleNics(**kwargs):
    return CatalystwanClient().getCloudDockVMLifecycleNics(**kwargs)

@register('getVbranchVMLifecycle')
def getVbranchVMLifecycle(**kwargs):
    return CatalystwanClient().getVbranchVMLifecycle(**kwargs)

@register('getVMLifeCycleState')
def getVMLifeCycleState(**kwargs):
    return CatalystwanClient().getVMLifeCycleState(**kwargs)

@register('getVManageSystemIP')
def getVManageSystemIP(**kwargs):
    return CatalystwanClient().getVManageSystemIP(**kwargs)

@register('getDspActive')
def getDspActive(**kwargs):
    return CatalystwanClient().getDspActive(**kwargs)

@register('getPhoneInfo')
def getPhoneInfo(**kwargs):
    return CatalystwanClient().getPhoneInfo(**kwargs)

@register('getDSPFarmProfiles')
def getDSPFarmProfiles(**kwargs):
    return CatalystwanClient().getDSPFarmProfiles(**kwargs)

@register('getSccpCcmGroups')
def getSccpCcmGroups(**kwargs):
    return CatalystwanClient().getSccpCcmGroups(**kwargs)

@register('getSccpConnections')
def getSccpConnections(**kwargs):
    return CatalystwanClient().getSccpConnections(**kwargs)

@register('getVoiceCalls')
def getVoiceCalls(**kwargs):
    return CatalystwanClient().getVoiceCalls(**kwargs)

@register('getVoipCalls')
def getVoipCalls(**kwargs):
    return CatalystwanClient().getVoipCalls(**kwargs)

@register('getT1e1IsdnStatus')
def getT1e1IsdnStatus(**kwargs):
    return CatalystwanClient().getT1e1IsdnStatus(**kwargs)

@register('getControllerT1e1InfoCurrent15MinStats')
def getControllerT1e1InfoCurrent15MinStats(**kwargs):
    return CatalystwanClient().getControllerT1e1InfoCurrent15MinStats(**kwargs)

@register('getControllerT1e1InfoTotalStats')
def getControllerT1e1InfoTotalStats(**kwargs):
    return CatalystwanClient().getControllerT1e1InfoTotalStats(**kwargs)

@register('getVPNInstances')
def getVPNInstances(**kwargs):
    return CatalystwanClient().getVPNInstances(**kwargs)

@register('getVRRPInterface')
def getVRRPInterface(**kwargs):
    return CatalystwanClient().getVRRPInterface(**kwargs)

@register('getWirelessClients')
def getWirelessClients(**kwargs):
    return CatalystwanClient().getWirelessClients(**kwargs)

@register('getWirelessRadios')
def getWirelessRadios(**kwargs):
    return CatalystwanClient().getWirelessRadios(**kwargs)

@register('getWirelessSsid')
def getWirelessSsid(**kwargs):
    return CatalystwanClient().getWirelessSsid(**kwargs)

@register('getWLANClients')
def getWLANClients(**kwargs):
    return CatalystwanClient().getWLANClients(**kwargs)

@register('getWLANInterfaces')
def getWLANInterfaces(**kwargs):
    return CatalystwanClient().getWLANInterfaces(**kwargs)

@register('getWLANRadios')
def getWLANRadios(**kwargs):
    return CatalystwanClient().getWLANRadios(**kwargs)

@register('getWLANRadius')
def getWLANRadius(**kwargs):
    return CatalystwanClient().getWLANRadius(**kwargs)

@register('getClusterInfo')
def getClusterInfo(**kwargs):
    return CatalystwanClient().getClusterInfo(**kwargs)

@register('getConfigDBRestoreStatus')
def getConfigDBRestoreStatus(**kwargs):
    return CatalystwanClient().getConfigDBRestoreStatus(**kwargs)

@register('getDetails')
def getDetails(**kwargs):
    return CatalystwanClient().getDetails(**kwargs)

@register('getDisasterRecoveryStatus')
def getDisasterRecoveryStatus(**kwargs):
    return CatalystwanClient().getDisasterRecoveryStatus(**kwargs)

@register('getHistory')
def getHistory(**kwargs):
    return CatalystwanClient().getHistory(**kwargs)

@register('getLocalHistory')
def getLocalHistory(**kwargs):
    return CatalystwanClient().getLocalHistory(**kwargs)

@register('getLocalDataCenterState')
def getLocalDataCenterState(**kwargs):
    return CatalystwanClient().getLocalDataCenterState(**kwargs)

@register('getRemoteDCMembersState')
def getRemoteDCMembersState(**kwargs):
    return CatalystwanClient().getRemoteDCMembersState(**kwargs)

@register('getRemoteDataCenterState')
def getRemoteDataCenterState(**kwargs):
    return CatalystwanClient().getRemoteDataCenterState(**kwargs)

@register('getRemoteDataCenterVersion')
def getRemoteDataCenterVersion(**kwargs):
    return CatalystwanClient().getRemoteDataCenterVersion(**kwargs)

@register('getDisasterRecoveryLocalReplicationSchedule')
def getDisasterRecoveryLocalReplicationSchedule(**kwargs):
    return CatalystwanClient().getDisasterRecoveryLocalReplicationSchedule(**kwargs)

@register('getdrStatus')
def getdrStatus(**kwargs):
    return CatalystwanClient().getdrStatus(**kwargs)

@register('get')
def get(**kwargs):
    return CatalystwanClient().get(**kwargs)

@register('listEntityOwnershipInfo')
def listEntityOwnershipInfo(**kwargs):
    return CatalystwanClient().listEntityOwnershipInfo(**kwargs)

@register('entityOwnershipInfo')
def entityOwnershipInfo(**kwargs):
    return CatalystwanClient().entityOwnershipInfo(**kwargs)

@register('getEvents')
def getEvents(**kwargs):
    return CatalystwanClient().getEvents(**kwargs)

@register('getAggregationData_1')
def getAggregationData_1(**kwargs):
    return CatalystwanClient().getAggregationData_1(**kwargs)

@register('getComponentsAsKeyValue')
def getComponentsAsKeyValue(**kwargs):
    return CatalystwanClient().getComponentsAsKeyValue(**kwargs)

@register('getDocCount_2')
def getDocCount_2(**kwargs):
    return CatalystwanClient().getDocCount_2(**kwargs)

@register('enableEventsFromFile')
def enableEventsFromFile(**kwargs):
    return CatalystwanClient().enableEventsFromFile(**kwargs)

@register('getEventNamesByComponent')
def getEventNamesByComponent(**kwargs):
    return CatalystwanClient().getEventNamesByComponent(**kwargs)

@register('getListenersInfo')
def getListenersInfo(**kwargs):
    return CatalystwanClient().getListenersInfo(**kwargs)

@register('getPage_1')
def getPage_1(**kwargs):
    return CatalystwanClient().getPage_1(**kwargs)

@register('getQueryFields')
def getQueryFields(**kwargs):
    return CatalystwanClient().getQueryFields(**kwargs)

@register('createEventsQueryConfig')
def createEventsQueryConfig(**kwargs):
    return CatalystwanClient().createEventsQueryConfig(**kwargs)

@register('getBySeverities')
def getBySeverities(**kwargs):
    return CatalystwanClient().getBySeverities(**kwargs)

@register('getSeverityHistogram')
def getSeverityHistogram(**kwargs):
    return CatalystwanClient().getSeverityHistogram(**kwargs)

@register('getEventTypesAsKeyValue')
def getEventTypesAsKeyValue(**kwargs):
    return CatalystwanClient().getEventTypesAsKeyValue(**kwargs)

@register('getDeviceCertificate')
def getDeviceCertificate(**kwargs):
    return CatalystwanClient().getDeviceCertificate(**kwargs)

@register('getDeviceCsr')
def getDeviceCsr(**kwargs):
    return CatalystwanClient().getDeviceCsr(**kwargs)

@register('getFeatureCaState')
def getFeatureCaState(**kwargs):
    return CatalystwanClient().getFeatureCaState(**kwargs)

@register('requesDNSSecActions')
def requesDNSSecActions(**kwargs):
    return CatalystwanClient().requesDNSSecActions(**kwargs)

@register('getDNSSecStatus')
def getDNSSecStatus(**kwargs):
    return CatalystwanClient().getDNSSecStatus(**kwargs)

@register('requestWazuhActions')
def requestWazuhActions(**kwargs):
    return CatalystwanClient().requestWazuhActions(**kwargs)

@register('getWazuhAgentStatus')
def getWazuhAgentStatus(**kwargs):
    return CatalystwanClient().getWazuhAgentStatus(**kwargs)

@register('listDeviceGroupList')
def listDeviceGroupList(**kwargs):
    return CatalystwanClient().listDeviceGroupList(**kwargs)

@register('listDeviceGroups')
def listDeviceGroups(**kwargs):
    return CatalystwanClient().listDeviceGroups(**kwargs)

@register('listGroupDevices')
def listGroupDevices(**kwargs):
    return CatalystwanClient().listGroupDevices(**kwargs)

@register('listGroupDevicesForMap')
def listGroupDevicesForMap(**kwargs):
    return CatalystwanClient().listGroupDevicesForMap(**kwargs)

@register('listGroupLinksForMap')
def listGroupLinksForMap(**kwargs):
    return CatalystwanClient().listGroupLinksForMap(**kwargs)

@register('getDevicesHealth')
def getDevicesHealth(**kwargs):
    return CatalystwanClient().getDevicesHealth(**kwargs)

@register('getDevicesHealthOverview')
def getDevicesHealthOverview(**kwargs):
    return CatalystwanClient().getDevicesHealthOverview(**kwargs)

@register('fetchDeviceDetails')
def fetchDeviceDetails(**kwargs):
    return CatalystwanClient().fetchDeviceDetails(**kwargs)

@register('InstallDeviceDetails')
def InstallDeviceDetails(**kwargs):
    return CatalystwanClient().InstallDeviceDetails(**kwargs)

@register('fetchSAVAAccounts')
def fetchSAVAAccounts(**kwargs):
    return CatalystwanClient().fetchSAVAAccounts(**kwargs)

@register('testbedMode')
def testbedMode(**kwargs):
    return CatalystwanClient().testbedMode(**kwargs)

@register('connect_1')
def connect_1(**kwargs):
    return CatalystwanClient().connect_1(**kwargs)

@register('getIseServerCredentials')
def getIseServerCredentials(**kwargs):
    return CatalystwanClient().getIseServerCredentials(**kwargs)

@register('getPxGridAccount')
def getPxGridAccount(**kwargs):
    return CatalystwanClient().getPxGridAccount(**kwargs)

@register('getPxgridCert')
def getPxgridCert(**kwargs):
    return CatalystwanClient().getPxgridCert(**kwargs)

@register('getSupportedLocales')
def getSupportedLocales(**kwargs):
    return CatalystwanClient().getSupportedLocales(**kwargs)

@register('getCategory')
def getCategory(**kwargs):
    return CatalystwanClient().getCategory(**kwargs)

@register('getvManageResourceUtilization')
def getvManageResourceUtilization(**kwargs):
    return CatalystwanClient().getvManageResourceUtilization(**kwargs)

@register('retrieveMDPAttachedDevices')
def retrieveMDPAttachedDevices(**kwargs):
    return CatalystwanClient().retrieveMDPAttachedDevices(**kwargs)

@register('retrieveMDPSupportedDevices')
def retrieveMDPSupportedDevices(**kwargs):
    return CatalystwanClient().retrieveMDPSupportedDevices(**kwargs)

@register('disconnectFromMDP')
def disconnectFromMDP(**kwargs):
    return CatalystwanClient().disconnectFromMDP(**kwargs)

@register('getMDPOnboardingStatus')
def getMDPOnboardingStatus(**kwargs):
    return CatalystwanClient().getMDPOnboardingStatus(**kwargs)

@register('retrieveMDPConfigObject')
def retrieveMDPConfigObject(**kwargs):
    return CatalystwanClient().retrieveMDPConfigObject(**kwargs)

@register('retrieveMDPPolicies')
def retrieveMDPPolicies(**kwargs):
    return CatalystwanClient().retrieveMDPPolicies(**kwargs)

@register('createDeviceVmanageConnectionList')
def createDeviceVmanageConnectionList(**kwargs):
    return CatalystwanClient().createDeviceVmanageConnectionList(**kwargs)

@register('getCloudConnectorDomainAppRules')
def getCloudConnectorDomainAppRules(**kwargs):
    return CatalystwanClient().getCloudConnectorDomainAppRules(**kwargs)

@register('getCloudConnectorIpAddressAppRules')
def getCloudConnectorIpAddressAppRules(**kwargs):
    return CatalystwanClient().getCloudConnectorIpAddressAppRules(**kwargs)

@register('getWebexAppData')
def getWebexAppData(**kwargs):
    return CatalystwanClient().getWebexAppData(**kwargs)

@register('getMSLADevices_1')
def getMSLADevices_1(**kwargs):
    return CatalystwanClient().getMSLADevices_1(**kwargs)

@register('getLicenseByUuid_1')
def getLicenseByUuid_1(**kwargs):
    return CatalystwanClient().getLicenseByUuid_1(**kwargs)

@register('getMslaLicenses')
def getMslaLicenses(**kwargs):
    return CatalystwanClient().getMslaLicenses(**kwargs)

@register('getLicensesCompliance')
def getLicensesCompliance(**kwargs):
    return CatalystwanClient().getLicensesCompliance(**kwargs)

@register('getDeviceDetailsForDashboard')
def getDeviceDetailsForDashboard(**kwargs):
    return CatalystwanClient().getDeviceDetailsForDashboard(**kwargs)

@register('getLicenseDistributionDetails')
def getLicenseDistributionDetails(**kwargs):
    return CatalystwanClient().getLicenseDistributionDetails(**kwargs)

@register('getPackagingDistributionDetails')
def getPackagingDistributionDetails(**kwargs):
    return CatalystwanClient().getPackagingDistributionDetails(**kwargs)

@register('getAllTemplate')
def getAllTemplate(**kwargs):
    return CatalystwanClient().getAllTemplate(**kwargs)

@register('getSubscriptions')
def getSubscriptions(**kwargs):
    return CatalystwanClient().getSubscriptions(**kwargs)

@register('getAllCloudAccounts')
def getAllCloudAccounts(**kwargs):
    return CatalystwanClient().getAllCloudAccounts(**kwargs)

@register('getEdgeAccounts')
def getEdgeAccounts(**kwargs):
    return CatalystwanClient().getEdgeAccounts(**kwargs)

@register('getEdgeAccountDetails')
def getEdgeAccountDetails(**kwargs):
    return CatalystwanClient().getEdgeAccountDetails(**kwargs)

@register('getCloudAccountDetails')
def getCloudAccountDetails(**kwargs):
    return CatalystwanClient().getCloudAccountDetails(**kwargs)

@register('auditDryRun')
def auditDryRun(**kwargs):
    return CatalystwanClient().auditDryRun(**kwargs)

@register('getEdgeBillingAccounts')
def getEdgeBillingAccounts(**kwargs):
    return CatalystwanClient().getEdgeBillingAccounts(**kwargs)

@register('getCloudRoutersAndAttachments')
def getCloudRoutersAndAttachments(**kwargs):
    return CatalystwanClient().getCloudRoutersAndAttachments(**kwargs)

@register('getCgws')
def getCgws(**kwargs):
    return CatalystwanClient().getCgws(**kwargs)

@register('getNvaSecurityRules')
def getNvaSecurityRules(**kwargs):
    return CatalystwanClient().getNvaSecurityRules(**kwargs)

@register('getAzureNetworkVirtualAppliances')
def getAzureNetworkVirtualAppliances(**kwargs):
    return CatalystwanClient().getAzureNetworkVirtualAppliances(**kwargs)

@register('getAzureNvaSkuResources')
def getAzureNvaSkuResources(**kwargs):
    return CatalystwanClient().getAzureNvaSkuResources(**kwargs)

@register('getCgwOrgResources')
def getCgwOrgResources(**kwargs):
    return CatalystwanClient().getCgwOrgResources(**kwargs)

@register('getAzureResourceGroups')
def getAzureResourceGroups(**kwargs):
    return CatalystwanClient().getAzureResourceGroups(**kwargs)

@register('getAzureVirtualHubs')
def getAzureVirtualHubs(**kwargs):
    return CatalystwanClient().getAzureVirtualHubs(**kwargs)

@register('getAzureVirtualVnetsAttached')
def getAzureVirtualVnetsAttached(**kwargs):
    return CatalystwanClient().getAzureVirtualVnetsAttached(**kwargs)

@register('getAzureVpnGateways')
def getAzureVpnGateways(**kwargs):
    return CatalystwanClient().getAzureVpnGateways(**kwargs)

@register('getAzureVirtualWans')
def getAzureVirtualWans(**kwargs):
    return CatalystwanClient().getAzureVirtualWans(**kwargs)

@register('getCgwDetails')
def getCgwDetails(**kwargs):
    return CatalystwanClient().getCgwDetails(**kwargs)

@register('getCgwAttachedSites')
def getCgwAttachedSites(**kwargs):
    return CatalystwanClient().getCgwAttachedSites(**kwargs)

@register('getAvailableDevicesOrByCGId')
def getAvailableDevicesOrByCGId(**kwargs):
    return CatalystwanClient().getAvailableDevicesOrByCGId(**kwargs)

@register('getCloudGateways')
def getCloudGateways(**kwargs):
    return CatalystwanClient().getCloudGateways(**kwargs)

@register('getCgwCustomSettingDetails')
def getCgwCustomSettingDetails(**kwargs):
    return CatalystwanClient().getCgwCustomSettingDetails(**kwargs)

@register('getCgwTypes')
def getCgwTypes(**kwargs):
    return CatalystwanClient().getCgwTypes(**kwargs)

@register('getCloudConnectedSites_1')
def getCloudConnectedSites_1(**kwargs):
    return CatalystwanClient().getCloudConnectedSites_1(**kwargs)

@register('getCloudConnectedSites')
def getCloudConnectedSites(**kwargs):
    return CatalystwanClient().getCloudConnectedSites(**kwargs)

@register('getEdgeConnectivityDetails')
def getEdgeConnectivityDetails(**kwargs):
    return CatalystwanClient().getEdgeConnectivityDetails(**kwargs)

@register('getEdgeConnectivityDetailByName')
def getEdgeConnectivityDetailByName(**kwargs):
    return CatalystwanClient().getEdgeConnectivityDetailByName(**kwargs)

@register('getConnectivityGateways')
def getConnectivityGateways(**kwargs):
    return CatalystwanClient().getConnectivityGateways(**kwargs)

@register('getConnectivityGatewayCreationOptions')
def getConnectivityGatewayCreationOptions(**kwargs):
    return CatalystwanClient().getConnectivityGatewayCreationOptions(**kwargs)

@register('getCwanCoreNetworkPolicy')
def getCwanCoreNetworkPolicy(**kwargs):
    return CatalystwanClient().getCwanCoreNetworkPolicy(**kwargs)

@register('getDashboardEdgeInfo')
def getDashboardEdgeInfo(**kwargs):
    return CatalystwanClient().getDashboardEdgeInfo(**kwargs)

@register('getWanDevices')
def getWanDevices(**kwargs):
    return CatalystwanClient().getWanDevices(**kwargs)

@register('getDeviceLinks')
def getDeviceLinks(**kwargs):
    return CatalystwanClient().getDeviceLinks(**kwargs)

@register('getDlPortSpeed')
def getDlPortSpeed(**kwargs):
    return CatalystwanClient().getDlPortSpeed(**kwargs)

@register('getCloudDevices_1')
def getCloudDevices_1(**kwargs):
    return CatalystwanClient().getCloudDevices_1(**kwargs)

@register('getCloudDevices')
def getCloudDevices(**kwargs):
    return CatalystwanClient().getCloudDevices(**kwargs)

@register('getEdgeWanDevices')
def getEdgeWanDevices(**kwargs):
    return CatalystwanClient().getEdgeWanDevices(**kwargs)

@register('getIcgws')
def getIcgws(**kwargs):
    return CatalystwanClient().getIcgws(**kwargs)

@register('getIcgwCustomSettingDetails')
def getIcgwCustomSettingDetails(**kwargs):
    return CatalystwanClient().getIcgwCustomSettingDetails(**kwargs)

@register('getIcgwTypes')
def getIcgwTypes(**kwargs):
    return CatalystwanClient().getIcgwTypes(**kwargs)

@register('getIcgwDetails')
def getIcgwDetails(**kwargs):
    return CatalystwanClient().getIcgwDetails(**kwargs)

@register('getEdgeGateways')
def getEdgeGateways(**kwargs):
    return CatalystwanClient().getEdgeGateways(**kwargs)

@register('getHostVpcs')
def getHostVpcs(**kwargs):
    return CatalystwanClient().getHostVpcs(**kwargs)

@register('getVpcTags')
def getVpcTags(**kwargs):
    return CatalystwanClient().getVpcTags(**kwargs)

@register('getSupportedEdgeImageNames')
def getSupportedEdgeImageNames(**kwargs):
    return CatalystwanClient().getSupportedEdgeImageNames(**kwargs)

@register('getSupportedInstanceSize')
def getSupportedInstanceSize(**kwargs):
    return CatalystwanClient().getSupportedInstanceSize(**kwargs)

@register('getSupportedEdgeInstanceSize')
def getSupportedEdgeInstanceSize(**kwargs):
    return CatalystwanClient().getSupportedEdgeInstanceSize(**kwargs)

@register('getInterconnectAccounts')
def getInterconnectAccounts(**kwargs):
    return CatalystwanClient().getInterconnectAccounts(**kwargs)

@register('getInterconnectAccount')
def getInterconnectAccount(**kwargs):
    return CatalystwanClient().getInterconnectAccount(**kwargs)

@register('getAuditReport')
def getAuditReport(**kwargs):
    return CatalystwanClient().getAuditReport(**kwargs)

@register('getGoogleCloudRouterAndAttachments')
def getGoogleCloudRouterAndAttachments(**kwargs):
    return CatalystwanClient().getGoogleCloudRouterAndAttachments(**kwargs)

@register('getAwsTransitGateways')
def getAwsTransitGateways(**kwargs):
    return CatalystwanClient().getAwsTransitGateways(**kwargs)

@register('getAzVirtualHubs')
def getAzVirtualHubs(**kwargs):
    return CatalystwanClient().getAzVirtualHubs(**kwargs)

@register('getAzVirtualWans')
def getAzVirtualWans(**kwargs):
    return CatalystwanClient().getAzVirtualWans(**kwargs)

@register('getCloudConnectivityGateways')
def getCloudConnectivityGateways(**kwargs):
    return CatalystwanClient().getCloudConnectivityGateways(**kwargs)

@register('getCloudConnectivityGatewayCreateOptions')
def getCloudConnectivityGatewayCreateOptions(**kwargs):
    return CatalystwanClient().getCloudConnectivityGatewayCreateOptions(**kwargs)

@register('getInterconnectColors')
def getInterconnectColors(**kwargs):
    return CatalystwanClient().getInterconnectColors(**kwargs)

@register('getInterconnectOnRampGatewayConnections')
def getInterconnectOnRampGatewayConnections(**kwargs):
    return CatalystwanClient().getInterconnectOnRampGatewayConnections(**kwargs)

@register('getInterconnectOnRampGatewayConnection')
def getInterconnectOnRampGatewayConnection(**kwargs):
    return CatalystwanClient().getInterconnectOnRampGatewayConnection(**kwargs)

@register('getInterconnectMappingTags')
def getInterconnectMappingTags(**kwargs):
    return CatalystwanClient().getInterconnectMappingTags(**kwargs)

@register('getInterconnectDeviceLinks')
def getInterconnectDeviceLinks(**kwargs):
    return CatalystwanClient().getInterconnectDeviceLinks(**kwargs)

@register('getInterconnectDeviceLink')
def getInterconnectDeviceLink(**kwargs):
    return CatalystwanClient().getInterconnectDeviceLink(**kwargs)

@register('getInterconnectCrossConnections')
def getInterconnectCrossConnections(**kwargs):
    return CatalystwanClient().getInterconnectCrossConnections(**kwargs)

@register('getInterconnectCrossConnection')
def getInterconnectCrossConnection(**kwargs):
    return CatalystwanClient().getInterconnectCrossConnection(**kwargs)

@register('getInterconnectVirtualNetworkConnections')
def getInterconnectVirtualNetworkConnections(**kwargs):
    return CatalystwanClient().getInterconnectVirtualNetworkConnections(**kwargs)

@register('getInterconnectVirtualNetworkConnection')
def getInterconnectVirtualNetworkConnection(**kwargs):
    return CatalystwanClient().getInterconnectVirtualNetworkConnection(**kwargs)

@register('getInterconnectDashboard')
def getInterconnectDashboard(**kwargs):
    return CatalystwanClient().getInterconnectDashboard(**kwargs)

@register('getInterconnectLicenses')
def getInterconnectLicenses(**kwargs):
    return CatalystwanClient().getInterconnectLicenses(**kwargs)

@register('getInterconnectGateways')
def getInterconnectGateways(**kwargs):
    return CatalystwanClient().getInterconnectGateways(**kwargs)

@register('getInterconnectGatewayImageNames')
def getInterconnectGatewayImageNames(**kwargs):
    return CatalystwanClient().getInterconnectGatewayImageNames(**kwargs)

@register('getInterconnectGatewayInstanceSizes')
def getInterconnectGatewayInstanceSizes(**kwargs):
    return CatalystwanClient().getInterconnectGatewayInstanceSizes(**kwargs)

@register('getInterconnetGatewayTypes')
def getInterconnetGatewayTypes(**kwargs):
    return CatalystwanClient().getInterconnetGatewayTypes(**kwargs)

@register('getInterconnectGateway')
def getInterconnectGateway(**kwargs):
    return CatalystwanClient().getInterconnectGateway(**kwargs)

@register('getInterconnectGatewayCustomSettings')
def getInterconnectGatewayCustomSettings(**kwargs):
    return CatalystwanClient().getInterconnectGatewayCustomSettings(**kwargs)

@register('getInterconnectIpTransit')
def getInterconnectIpTransit(**kwargs):
    return CatalystwanClient().getInterconnectIpTransit(**kwargs)

@register('getInterconnectServiceSwPkg')
def getInterconnectServiceSwPkg(**kwargs):
    return CatalystwanClient().getInterconnectServiceSwPkg(**kwargs)

@register('getInterconnectServices')
def getInterconnectServices(**kwargs):
    return CatalystwanClient().getInterconnectServices(**kwargs)

@register('getInterconnectGlobalSettings')
def getInterconnectGlobalSettings(**kwargs):
    return CatalystwanClient().getInterconnectGlobalSettings(**kwargs)

@register('getInterconnectSshKeys')
def getInterconnectSshKeys(**kwargs):
    return CatalystwanClient().getInterconnectSshKeys(**kwargs)

@register('getInterconnectTypes')
def getInterconnectTypes(**kwargs):
    return CatalystwanClient().getInterconnectTypes(**kwargs)

@register('getAllInterconnectWidgets')
def getAllInterconnectWidgets(**kwargs):
    return CatalystwanClient().getAllInterconnectWidgets(**kwargs)

@register('getInterconnectBillingAccounts')
def getInterconnectBillingAccounts(**kwargs):
    return CatalystwanClient().getInterconnectBillingAccounts(**kwargs)

@register('getInterconnectPartnerPorts')
def getInterconnectPartnerPorts(**kwargs):
    return CatalystwanClient().getInterconnectPartnerPorts(**kwargs)

@register('getInterconnectPortSpeeds')
def getInterconnectPortSpeeds(**kwargs):
    return CatalystwanClient().getInterconnectPortSpeeds(**kwargs)

@register('getInterconnectLocationInfo')
def getInterconnectLocationInfo(**kwargs):
    return CatalystwanClient().getInterconnectLocationInfo(**kwargs)

@register('getInterconnectConfigGroupTopology')
def getInterconnectConfigGroupTopology(**kwargs):
    return CatalystwanClient().getInterconnectConfigGroupTopology(**kwargs)

@register('getInterconnectDeviceLinkPortSpeeds')
def getInterconnectDeviceLinkPortSpeeds(**kwargs):
    return CatalystwanClient().getInterconnectDeviceLinkPortSpeeds(**kwargs)

@register('getAvailableDevicesOrByCGId_1')
def getAvailableDevicesOrByCGId_1(**kwargs):
    return CatalystwanClient().getAvailableDevicesOrByCGId_1(**kwargs)

@register('getInterconnectGatewayDevices')
def getInterconnectGatewayDevices(**kwargs):
    return CatalystwanClient().getInterconnectGatewayDevices(**kwargs)

@register('getMonitoringInterconnectConnectedSites')
def getMonitoringInterconnectConnectedSites(**kwargs):
    return CatalystwanClient().getMonitoringInterconnectConnectedSites(**kwargs)

@register('getMonitoringInterconnectDevices')
def getMonitoringInterconnectDevices(**kwargs):
    return CatalystwanClient().getMonitoringInterconnectDevices(**kwargs)

@register('getMonitoringInterconnectGateways')
def getMonitoringInterconnectGateways(**kwargs):
    return CatalystwanClient().getMonitoringInterconnectGateways(**kwargs)

@register('getInterconnectWidget')
def getInterconnectWidget(**kwargs):
    return CatalystwanClient().getInterconnectWidget(**kwargs)

@register('getWanInterfaceColors')
def getWanInterfaceColors(**kwargs):
    return CatalystwanClient().getWanInterfaceColors(**kwargs)

@register('getLicenses')
def getLicenses(**kwargs):
    return CatalystwanClient().getLicenses(**kwargs)

@register('getEdgeLocationsInfo')
def getEdgeLocationsInfo(**kwargs):
    return CatalystwanClient().getEdgeLocationsInfo(**kwargs)

@register('getSupportedLoopbackCgwColors')
def getSupportedLoopbackCgwColors(**kwargs):
    return CatalystwanClient().getSupportedLoopbackCgwColors(**kwargs)

@register('getSupportedLoopbackTransportColors')
def getSupportedLoopbackTransportColors(**kwargs):
    return CatalystwanClient().getSupportedLoopbackTransportColors(**kwargs)

@register('getMappingMatrix')
def getMappingMatrix(**kwargs):
    return CatalystwanClient().getMappingMatrix(**kwargs)

@register('getDefaultMappingValues')
def getDefaultMappingValues(**kwargs):
    return CatalystwanClient().getDefaultMappingValues(**kwargs)

@register('getMappingStatus')
def getMappingStatus(**kwargs):
    return CatalystwanClient().getMappingStatus(**kwargs)

@register('getMappingSummary')
def getMappingSummary(**kwargs):
    return CatalystwanClient().getMappingSummary(**kwargs)

@register('getMappingTags')
def getMappingTags(**kwargs):
    return CatalystwanClient().getMappingTags(**kwargs)

@register('getEdgeMappingTags')
def getEdgeMappingTags(**kwargs):
    return CatalystwanClient().getEdgeMappingTags(**kwargs)

@register('getMappingVpns')
def getMappingVpns(**kwargs):
    return CatalystwanClient().getMappingVpns(**kwargs)

@register('getCgwAssociatedMappings')
def getCgwAssociatedMappings(**kwargs):
    return CatalystwanClient().getCgwAssociatedMappings(**kwargs)

@register('getPartnerPorts')
def getPartnerPorts(**kwargs):
    return CatalystwanClient().getPartnerPorts(**kwargs)

@register('getPortSpeed')
def getPortSpeed(**kwargs):
    return CatalystwanClient().getPortSpeed(**kwargs)

@register('getCloudRegions')
def getCloudRegions(**kwargs):
    return CatalystwanClient().getCloudRegions(**kwargs)

@register('getEdgeGlobalSettings')
def getEdgeGlobalSettings(**kwargs):
    return CatalystwanClient().getEdgeGlobalSettings(**kwargs)

@register('getGlobalSettings')
def getGlobalSettings(**kwargs):
    return CatalystwanClient().getGlobalSettings(**kwargs)

@register('getSites')
def getSites(**kwargs):
    return CatalystwanClient().getSites(**kwargs)

@register('getSshKeyList')
def getSshKeyList(**kwargs):
    return CatalystwanClient().getSshKeyList(**kwargs)

@register('getSupportedSoftwareImageList')
def getSupportedSoftwareImageList(**kwargs):
    return CatalystwanClient().getSupportedSoftwareImageList(**kwargs)

@register('getTunnelNames')
def getTunnelNames(**kwargs):
    return CatalystwanClient().getTunnelNames(**kwargs)

@register('getCloudTypes')
def getCloudTypes(**kwargs):
    return CatalystwanClient().getCloudTypes(**kwargs)

@register('getEdgeTypes')
def getEdgeTypes(**kwargs):
    return CatalystwanClient().getEdgeTypes(**kwargs)

@register('getVHubs')
def getVHubs(**kwargs):
    return CatalystwanClient().getVHubs(**kwargs)

@register('getVWans')
def getVWans(**kwargs):
    return CatalystwanClient().getVWans(**kwargs)

@register('getAllCloudWidgets')
def getAllCloudWidgets(**kwargs):
    return CatalystwanClient().getAllCloudWidgets(**kwargs)

@register('getAllEdgeWidgets')
def getAllEdgeWidgets(**kwargs):
    return CatalystwanClient().getAllEdgeWidgets(**kwargs)

@register('getEdgeWidget')
def getEdgeWidget(**kwargs):
    return CatalystwanClient().getEdgeWidget(**kwargs)

@register('getCloudWidget')
def getCloudWidget(**kwargs):
    return CatalystwanClient().getCloudWidget(**kwargs)

@register('getMultiCloudConfigGroupTopology')
def getMultiCloudConfigGroupTopology(**kwargs):
    return CatalystwanClient().getMultiCloudConfigGroupTopology(**kwargs)

@register('getVmanageControlStatus')
def getVmanageControlStatus(**kwargs):
    return CatalystwanClient().getVmanageControlStatus(**kwargs)

@register('getRebootCount')
def getRebootCount(**kwargs):
    return CatalystwanClient().getRebootCount(**kwargs)

@register('getNetworkIssuesSummary')
def getNetworkIssuesSummary(**kwargs):
    return CatalystwanClient().getNetworkIssuesSummary(**kwargs)

@register('getNetworkStatusSummary')
def getNetworkStatusSummary(**kwargs):
    return CatalystwanClient().getNetworkStatusSummary(**kwargs)

@register('getNetworkDesign')
def getNetworkDesign(**kwargs):
    return CatalystwanClient().getNetworkDesign(**kwargs)

@register('getCircuits')
def getCircuits(**kwargs):
    return CatalystwanClient().getCircuits(**kwargs)

@register('getGlobalParameters')
def getGlobalParameters(**kwargs):
    return CatalystwanClient().getGlobalParameters(**kwargs)

@register('getGlobalTemplate')
def getGlobalTemplate(**kwargs):
    return CatalystwanClient().getGlobalTemplate(**kwargs)

@register('runMyTest')
def runMyTest(**kwargs):
    return CatalystwanClient().runMyTest(**kwargs)

@register('getDeviceProfileFeatureTemplateList')
def getDeviceProfileFeatureTemplateList(**kwargs):
    return CatalystwanClient().getDeviceProfileFeatureTemplateList(**kwargs)

@register('getDeviceProfileConfigStatus')
def getDeviceProfileConfigStatus(**kwargs):
    return CatalystwanClient().getDeviceProfileConfigStatus(**kwargs)

@register('getDeviceProfileConfigStatusByProfileId')
def getDeviceProfileConfigStatusByProfileId(**kwargs):
    return CatalystwanClient().getDeviceProfileConfigStatusByProfileId(**kwargs)

@register('getDeviceProfileTaskCount')
def getDeviceProfileTaskCount(**kwargs):
    return CatalystwanClient().getDeviceProfileTaskCount(**kwargs)

@register('getDeviceProfileTaskStatus')
def getDeviceProfileTaskStatus(**kwargs):
    return CatalystwanClient().getDeviceProfileTaskStatus(**kwargs)

@register('getDeviceProfileTaskStatusByProfileId')
def getDeviceProfileTaskStatusByProfileId(**kwargs):
    return CatalystwanClient().getDeviceProfileTaskStatusByProfileId(**kwargs)

@register('generateProfileTemplateList')
def generateProfileTemplateList(**kwargs):
    return CatalystwanClient().generateProfileTemplateList(**kwargs)

@register('getDeviceProfileTemplate')
def getDeviceProfileTemplate(**kwargs):
    return CatalystwanClient().getDeviceProfileTemplate(**kwargs)

@register('getServiceProfileConfig')
def getServiceProfileConfig(**kwargs):
    return CatalystwanClient().getServiceProfileConfig(**kwargs)

@register('getNotificationRule')
def getNotificationRule(**kwargs):
    return CatalystwanClient().getNotificationRule(**kwargs)

@register('getDevices')
def getDevices(**kwargs):
    return CatalystwanClient().getDevices(**kwargs)

@register('oauthAccess')
def oauthAccess(**kwargs):
    return CatalystwanClient().oauthAccess(**kwargs)

@register('getClientID')
def getClientID(**kwargs):
    return CatalystwanClient().getClientID(**kwargs)

@register('getCall')
def getCall(**kwargs):
    return CatalystwanClient().getCall(**kwargs)

@register('getPartners')
def getPartners(**kwargs):
    return CatalystwanClient().getPartners(**kwargs)

@register('getACIDefinitions')
def getACIDefinitions(**kwargs):
    return CatalystwanClient().getACIDefinitions(**kwargs)

@register('getDscpMappings')
def getDscpMappings(**kwargs):
    return CatalystwanClient().getDscpMappings(**kwargs)

@register('getEvents_1')
def getEvents_1(**kwargs):
    return CatalystwanClient().getEvents_1(**kwargs)

@register('getDataPrefixMappings')
def getDataPrefixMappings(**kwargs):
    return CatalystwanClient().getDataPrefixMappings(**kwargs)

@register('getDataPrefixSequences')
def getDataPrefixSequences(**kwargs):
    return CatalystwanClient().getDataPrefixSequences(**kwargs)

@register('getSDAEnabledDevices')
def getSDAEnabledDevices(**kwargs):
    return CatalystwanClient().getSDAEnabledDevices(**kwargs)

@register('getDeviceDetails')
def getDeviceDetails(**kwargs):
    return CatalystwanClient().getDeviceDetails(**kwargs)

@register('getSitesForPartner')
def getSitesForPartner(**kwargs):
    return CatalystwanClient().getSitesForPartner(**kwargs)

@register('getOverlayVPNList')
def getOverlayVPNList(**kwargs):
    return CatalystwanClient().getOverlayVPNList(**kwargs)

@register('getVPNList')
def getVPNList(**kwargs):
    return CatalystwanClient().getVPNList(**kwargs)

@register('getPartnersByPartnerType')
def getPartnersByPartnerType(**kwargs):
    return CatalystwanClient().getPartnersByPartnerType(**kwargs)

@register('getPartnerDevices')
def getPartnerDevices(**kwargs):
    return CatalystwanClient().getPartnerDevices(**kwargs)

@register('getPartner')
def getPartner(**kwargs):
    return CatalystwanClient().getPartner(**kwargs)

@register('getSecureXRefreshToken')
def getSecureXRefreshToken(**kwargs):
    return CatalystwanClient().getSecureXRefreshToken(**kwargs)

@register('getResources')
def getResources(**kwargs):
    return CatalystwanClient().getResources(**kwargs)

@register('listSchedules')
def listSchedules(**kwargs):
    return CatalystwanClient().listSchedules(**kwargs)

@register('getScheduleRecordForBackup')
def getScheduleRecordForBackup(**kwargs):
    return CatalystwanClient().getScheduleRecordForBackup(**kwargs)

@register('getExtendedApplications')
def getExtendedApplications(**kwargs):
    return CatalystwanClient().getExtendedApplications(**kwargs)

@register('getCloudConnector')
def getCloudConnector(**kwargs):
    return CatalystwanClient().getCloudConnector(**kwargs)

@register('getCloudConnectorStatus')
def getCloudConnectorStatus(**kwargs):
    return CatalystwanClient().getCloudConnectorStatus(**kwargs)

@register('getCustomApp')
def getCustomApp(**kwargs):
    return CatalystwanClient().getCustomApp(**kwargs)

@register('getAllProtocolPacks')
def getAllProtocolPacks(**kwargs):
    return CatalystwanClient().getAllProtocolPacks(**kwargs)

@register('getBaseSystemPack')
def getBaseSystemPack(**kwargs):
    return CatalystwanClient().getBaseSystemPack(**kwargs)

@register('getAllSDAVCDevice')
def getAllSDAVCDevice(**kwargs):
    return CatalystwanClient().getAllSDAVCDevice(**kwargs)

@register('getDefaultApplicationComplianceDetails')
def getDefaultApplicationComplianceDetails(**kwargs):
    return CatalystwanClient().getDefaultApplicationComplianceDetails(**kwargs)

@register('isApplicationComplianceDetected')
def isApplicationComplianceDetected(**kwargs):
    return CatalystwanClient().isApplicationComplianceDetected(**kwargs)

@register('getApplicationComplianceStatus')
def getApplicationComplianceStatus(**kwargs):
    return CatalystwanClient().getApplicationComplianceStatus(**kwargs)

@register('getApplicationComplianceDetails')
def getApplicationComplianceDetails(**kwargs):
    return CatalystwanClient().getApplicationComplianceDetails(**kwargs)

@register('getCustomApplicationList')
def getCustomApplicationList(**kwargs):
    return CatalystwanClient().getCustomApplicationList(**kwargs)

@register('getNonCompliantDevicesForProtocolPack')
def getNonCompliantDevicesForProtocolPack(**kwargs):
    return CatalystwanClient().getNonCompliantDevicesForProtocolPack(**kwargs)

@register('getDeviceComplianceStatus')
def getDeviceComplianceStatus(**kwargs):
    return CatalystwanClient().getDeviceComplianceStatus(**kwargs)

@register('getNewApplicationList')
def getNewApplicationList(**kwargs):
    return CatalystwanClient().getNewApplicationList(**kwargs)

@register('getCompliancePolicy')
def getCompliancePolicy(**kwargs):
    return CatalystwanClient().getCompliancePolicy(**kwargs)

@register('getPolicyComplianceStatus')
def getPolicyComplianceStatus(**kwargs):
    return CatalystwanClient().getPolicyComplianceStatus(**kwargs)

@register('getDefaultSystemPack')
def getDefaultSystemPack(**kwargs):
    return CatalystwanClient().getDefaultSystemPack(**kwargs)

@register('getLatestSystemPack')
def getLatestSystemPack(**kwargs):
    return CatalystwanClient().getLatestSystemPack(**kwargs)

@register('getDeployJobStatus')
def getDeployJobStatus(**kwargs):
    return CatalystwanClient().getDeployJobStatus(**kwargs)

@register('getDeployJobStatus_1')
def getDeployJobStatus_1(**kwargs):
    return CatalystwanClient().getDeployJobStatus_1(**kwargs)

@register('getProtocolPackUploadStatus')
def getProtocolPackUploadStatus(**kwargs):
    return CatalystwanClient().getProtocolPackUploadStatus(**kwargs)

@register('getSecurityDeviceHealth')
def getSecurityDeviceHealth(**kwargs):
    return CatalystwanClient().getSecurityDeviceHealth(**kwargs)

@register('getSecurityPolicyDeviceList')
def getSecurityPolicyDeviceList(**kwargs):
    return CatalystwanClient().getSecurityPolicyDeviceList(**kwargs)

@register('getSegments')
def getSegments(**kwargs):
    return CatalystwanClient().getSegments(**kwargs)

@register('getSegment')
def getSegment(**kwargs):
    return CatalystwanClient().getSegment(**kwargs)

@register('createServerInfo_1')
def createServerInfo_1(**kwargs):
    return CatalystwanClient().createServerInfo_1(**kwargs)

@register('getDataChangeInfo')
def getDataChangeInfo(**kwargs):
    return CatalystwanClient().getDataChangeInfo(**kwargs)

@register('showInfo')
def showInfo(**kwargs):
    return CatalystwanClient().showInfo(**kwargs)

@register('getCertificate')
def getCertificate(**kwargs):
    return CatalystwanClient().getCertificate(**kwargs)

@register('getBanner')
def getBanner(**kwargs):
    return CatalystwanClient().getBanner(**kwargs)

@register('getSessionTimout')
def getSessionTimout(**kwargs):
    return CatalystwanClient().getSessionTimout(**kwargs)

@register('getCertConfiguration')
def getCertConfiguration(**kwargs):
    return CatalystwanClient().getCertConfiguration(**kwargs)

@register('getCloudxConfiguration')
def getCloudxConfiguration(**kwargs):
    return CatalystwanClient().getCloudxConfiguration(**kwargs)

@register('getGoogleMapKey')
def getGoogleMapKey(**kwargs):
    return CatalystwanClient().getGoogleMapKey(**kwargs)

@register('getMaintenanceWindow')
def getMaintenanceWindow(**kwargs):
    return CatalystwanClient().getMaintenanceWindow(**kwargs)

@register('getMicrosoftTelemetryConfiguration')
def getMicrosoftTelemetryConfiguration(**kwargs):
    return CatalystwanClient().getMicrosoftTelemetryConfiguration(**kwargs)

@register('getWaniConfiguration')
def getWaniConfiguration(**kwargs):
    return CatalystwanClient().getWaniConfiguration(**kwargs)

@register('getConfigurationBySettingType')
def getConfigurationBySettingType(**kwargs):
    return CatalystwanClient().getConfigurationBySettingType(**kwargs)

@register('getPasswordPolicy')
def getPasswordPolicy(**kwargs):
    return CatalystwanClient().getPasswordPolicy(**kwargs)

@register('getSigDynamicDataCenterList')
def getSigDynamicDataCenterList(**kwargs):
    return CatalystwanClient().getSigDynamicDataCenterList(**kwargs)

@register('getSigDataCenterList')
def getSigDataCenterList(**kwargs):
    return CatalystwanClient().getSigDataCenterList(**kwargs)

@register('getSigGlobalCredentials')
def getSigGlobalCredentials(**kwargs):
    return CatalystwanClient().getSigGlobalCredentials(**kwargs)

@register('getChildOrgs')
def getChildOrgs(**kwargs):
    return CatalystwanClient().getChildOrgs(**kwargs)

@register('fetchAccounts')
def fetchAccounts(**kwargs):
    return CatalystwanClient().fetchAccounts(**kwargs)

@register('fetchReports_1')
def fetchReports_1(**kwargs):
    return CatalystwanClient().fetchReports_1(**kwargs)

@register('fetchReports')
def fetchReports(**kwargs):
    return CatalystwanClient().fetchReports(**kwargs)

@register('getSettings')
def getSettings(**kwargs):
    return CatalystwanClient().getSettings(**kwargs)

@register('getProxyCertOfEdge')
def getProxyCertOfEdge(**kwargs):
    return CatalystwanClient().getProxyCertOfEdge(**kwargs)

@register('getSslProxyCSR')
def getSslProxyCSR(**kwargs):
    return CatalystwanClient().getSslProxyCSR(**kwargs)

@register('getSslProxyList')
def getSslProxyList(**kwargs):
    return CatalystwanClient().getSslProxyList(**kwargs)

@register('getCertificateState')
def getCertificateState(**kwargs):
    return CatalystwanClient().getCertificateState(**kwargs)

@register('getEnterpriseCertificate')
def getEnterpriseCertificate(**kwargs):
    return CatalystwanClient().getEnterpriseCertificate(**kwargs)

@register('getVManageEnterpriseRootCertificate')
def getVManageEnterpriseRootCertificate(**kwargs):
    return CatalystwanClient().getVManageEnterpriseRootCertificate(**kwargs)

@register('getvManageCertificate')
def getvManageCertificate(**kwargs):
    return CatalystwanClient().getvManageCertificate(**kwargs)

@register('getvManageCSR')
def getvManageCSR(**kwargs):
    return CatalystwanClient().getvManageCSR(**kwargs)

@register('getvManageRootCA')
def getvManageRootCA(**kwargs):
    return CatalystwanClient().getvManageRootCA(**kwargs)

@register('getStatisticType')
def getStatisticType(**kwargs):
    return CatalystwanClient().getStatisticType(**kwargs)

@register('getAggregationDataByQuery_14')
def getAggregationDataByQuery_14(**kwargs):
    return CatalystwanClient().getAggregationDataByQuery_14(**kwargs)

@register('getStatDataRawData_1')
def getStatDataRawData_1(**kwargs):
    return CatalystwanClient().getStatDataRawData_1(**kwargs)

@register('getAggregationDataByQuery_1')
def getAggregationDataByQuery_1(**kwargs):
    return CatalystwanClient().getAggregationDataByQuery_1(**kwargs)

@register('getStatDataRawDataAsCSV_1')
def getStatDataRawDataAsCSV_1(**kwargs):
    return CatalystwanClient().getStatDataRawDataAsCSV_1(**kwargs)

@register('getCount_2')
def getCount_2(**kwargs):
    return CatalystwanClient().getCount_2(**kwargs)

@register('getStatDataFields_2')
def getStatDataFields_2(**kwargs):
    return CatalystwanClient().getStatDataFields_2(**kwargs)

@register('getStatsPaginationRawData_1')
def getStatsPaginationRawData_1(**kwargs):
    return CatalystwanClient().getStatsPaginationRawData_1(**kwargs)

@register('getStatQueryFields_2')
def getStatQueryFields_2(**kwargs):
    return CatalystwanClient().getStatQueryFields_2(**kwargs)

@register('getStatDataRawData')
def getStatDataRawData(**kwargs):
    return CatalystwanClient().getStatDataRawData(**kwargs)

@register('getAggregationDataByQuery')
def getAggregationDataByQuery(**kwargs):
    return CatalystwanClient().getAggregationDataByQuery(**kwargs)

@register('getStatDataRawDataAsCSV')
def getStatDataRawDataAsCSV(**kwargs):
    return CatalystwanClient().getStatDataRawDataAsCSV(**kwargs)

@register('getCount_1')
def getCount_1(**kwargs):
    return CatalystwanClient().getCount_1(**kwargs)

@register('getStatDataFields_1')
def getStatDataFields_1(**kwargs):
    return CatalystwanClient().getStatDataFields_1(**kwargs)

@register('getStatsPaginationRawData')
def getStatsPaginationRawData(**kwargs):
    return CatalystwanClient().getStatsPaginationRawData(**kwargs)

@register('getStatQueryFields_1')
def getStatQueryFields_1(**kwargs):
    return CatalystwanClient().getStatQueryFields_1(**kwargs)

@register('getStatDataRawData_2')
def getStatDataRawData_2(**kwargs):
    return CatalystwanClient().getStatDataRawData_2(**kwargs)

@register('getAggregationDataByQuery_2')
def getAggregationDataByQuery_2(**kwargs):
    return CatalystwanClient().getAggregationDataByQuery_2(**kwargs)

@register('getStatDataRawDataAsCSV_2')
def getStatDataRawDataAsCSV_2(**kwargs):
    return CatalystwanClient().getStatDataRawDataAsCSV_2(**kwargs)

@register('getStatsAppRouteDeviceTunnelSummary')
def getStatsAppRouteDeviceTunnelSummary(**kwargs):
    return CatalystwanClient().getStatsAppRouteDeviceTunnelSummary(**kwargs)

@register('getStatsAppRouteDeviceTunnels')
def getStatsAppRouteDeviceTunnels(**kwargs):
    return CatalystwanClient().getStatsAppRouteDeviceTunnels(**kwargs)

@register('getDocCount_1')
def getDocCount_1(**kwargs):
    return CatalystwanClient().getDocCount_1(**kwargs)

@register('getStatDataFields_3')
def getStatDataFields_3(**kwargs):
    return CatalystwanClient().getStatDataFields_3(**kwargs)

@register('getStatBulkRawData')
def getStatBulkRawData(**kwargs):
    return CatalystwanClient().getStatBulkRawData(**kwargs)

@register('getStatQueryFields_3')
def getStatQueryFields_3(**kwargs):
    return CatalystwanClient().getStatQueryFields_3(**kwargs)

@register('getAppRouteTransportSummaryType')
def getAppRouteTransportSummaryType(**kwargs):
    return CatalystwanClient().getAppRouteTransportSummaryType(**kwargs)

@register('getAppRouteTransportType')
def getAppRouteTransportType(**kwargs):
    return CatalystwanClient().getAppRouteTransportType(**kwargs)

@register('getAppRouteTunnelSummaryType')
def getAppRouteTunnelSummaryType(**kwargs):
    return CatalystwanClient().getAppRouteTunnelSummaryType(**kwargs)

@register('getAppRouteTunnelHealth')
def getAppRouteTunnelHealth(**kwargs):
    return CatalystwanClient().getAppRouteTunnelHealth(**kwargs)

@register('getAppRouteTunnelsSummaryType')
def getAppRouteTunnelsSummaryType(**kwargs):
    return CatalystwanClient().getAppRouteTunnelsSummaryType(**kwargs)

@register('getAppRouteTunnelType')
def getAppRouteTunnelType(**kwargs):
    return CatalystwanClient().getAppRouteTunnelType(**kwargs)

@register('getStatDataRawData_4')
def getStatDataRawData_4(**kwargs):
    return CatalystwanClient().getStatDataRawData_4(**kwargs)

@register('getAggregationDataByQuery_4')
def getAggregationDataByQuery_4(**kwargs):
    return CatalystwanClient().getAggregationDataByQuery_4(**kwargs)

@register('getStatDataRawDataAsCSV_4')
def getStatDataRawDataAsCSV_4(**kwargs):
    return CatalystwanClient().getStatDataRawDataAsCSV_4(**kwargs)

@register('getCount_4')
def getCount_4(**kwargs):
    return CatalystwanClient().getCount_4(**kwargs)

@register('getStatDataFields_5')
def getStatDataFields_5(**kwargs):
    return CatalystwanClient().getStatDataFields_5(**kwargs)

@register('getStatsPaginationRawData_3')
def getStatsPaginationRawData_3(**kwargs):
    return CatalystwanClient().getStatsPaginationRawData_3(**kwargs)

@register('getStatQueryFields_5')
def getStatQueryFields_5(**kwargs):
    return CatalystwanClient().getStatQueryFields_5(**kwargs)

@register('getStatDataRawData_5')
def getStatDataRawData_5(**kwargs):
    return CatalystwanClient().getStatDataRawData_5(**kwargs)

@register('getAggregationDataByQuery_5')
def getAggregationDataByQuery_5(**kwargs):
    return CatalystwanClient().getAggregationDataByQuery_5(**kwargs)

@register('getStatDataRawDataAsCSV_5')
def getStatDataRawDataAsCSV_5(**kwargs):
    return CatalystwanClient().getStatDataRawDataAsCSV_5(**kwargs)

@register('getCount_5')
def getCount_5(**kwargs):
    return CatalystwanClient().getCount_5(**kwargs)

@register('getStatDataFields_6')
def getStatDataFields_6(**kwargs):
    return CatalystwanClient().getStatDataFields_6(**kwargs)

@register('getStatsPaginationRawData_4')
def getStatsPaginationRawData_4(**kwargs):
    return CatalystwanClient().getStatsPaginationRawData_4(**kwargs)

@register('getStatQueryFields_6')
def getStatQueryFields_6(**kwargs):
    return CatalystwanClient().getStatQueryFields_6(**kwargs)

@register('getStatDataRawData_6')
def getStatDataRawData_6(**kwargs):
    return CatalystwanClient().getStatDataRawData_6(**kwargs)

@register('getAggregationDataByQuery_6')
def getAggregationDataByQuery_6(**kwargs):
    return CatalystwanClient().getAggregationDataByQuery_6(**kwargs)

@register('getStatDataRawDataAsCSV_6')
def getStatDataRawDataAsCSV_6(**kwargs):
    return CatalystwanClient().getStatDataRawDataAsCSV_6(**kwargs)

@register('getCount_6')
def getCount_6(**kwargs):
    return CatalystwanClient().getCount_6(**kwargs)

@register('getStatDataFields_7')
def getStatDataFields_7(**kwargs):
    return CatalystwanClient().getStatDataFields_7(**kwargs)

@register('getStatsPaginationRawData_5')
def getStatsPaginationRawData_5(**kwargs):
    return CatalystwanClient().getStatsPaginationRawData_5(**kwargs)

@register('getStatQueryFields_7')
def getStatQueryFields_7(**kwargs):
    return CatalystwanClient().getStatQueryFields_7(**kwargs)

@register('getStatDataRawData_7')
def getStatDataRawData_7(**kwargs):
    return CatalystwanClient().getStatDataRawData_7(**kwargs)

@register('getAggregationDataByQuery_7')
def getAggregationDataByQuery_7(**kwargs):
    return CatalystwanClient().getAggregationDataByQuery_7(**kwargs)

@register('getStatDataRawDataAsCSV_7')
def getStatDataRawDataAsCSV_7(**kwargs):
    return CatalystwanClient().getStatDataRawDataAsCSV_7(**kwargs)

@register('getCount_7')
def getCount_7(**kwargs):
    return CatalystwanClient().getCount_7(**kwargs)

@register('getStatDataFields_8')
def getStatDataFields_8(**kwargs):
    return CatalystwanClient().getStatDataFields_8(**kwargs)

@register('getStatsPaginationRawData_6')
def getStatsPaginationRawData_6(**kwargs):
    return CatalystwanClient().getStatsPaginationRawData_6(**kwargs)

@register('getStatQueryFields_8')
def getStatQueryFields_8(**kwargs):
    return CatalystwanClient().getStatQueryFields_8(**kwargs)

@register('getStatDataRawData_9')
def getStatDataRawData_9(**kwargs):
    return CatalystwanClient().getStatDataRawData_9(**kwargs)

@register('getAggregationDataByQuery_9')
def getAggregationDataByQuery_9(**kwargs):
    return CatalystwanClient().getAggregationDataByQuery_9(**kwargs)

@register('createFlowsGrid')
def createFlowsGrid(**kwargs):
    return CatalystwanClient().createFlowsGrid(**kwargs)

@register('createFlowssummary')
def createFlowssummary(**kwargs):
    return CatalystwanClient().createFlowssummary(**kwargs)

@register('getStatDataRawDataAsCSV_9')
def getStatDataRawDataAsCSV_9(**kwargs):
    return CatalystwanClient().getStatDataRawDataAsCSV_9(**kwargs)

@register('createFlowDeviceData')
def createFlowDeviceData(**kwargs):
    return CatalystwanClient().createFlowDeviceData(**kwargs)

@register('getCount_9')
def getCount_9(**kwargs):
    return CatalystwanClient().getCount_9(**kwargs)

@register('getStatDataFields_10')
def getStatDataFields_10(**kwargs):
    return CatalystwanClient().getStatDataFields_10(**kwargs)

@register('getStatsPaginationRawData_8')
def getStatsPaginationRawData_8(**kwargs):
    return CatalystwanClient().getStatsPaginationRawData_8(**kwargs)

@register('getStatQueryFields_10')
def getStatQueryFields_10(**kwargs):
    return CatalystwanClient().getStatQueryFields_10(**kwargs)

@register('getStatDataRawData_10')
def getStatDataRawData_10(**kwargs):
    return CatalystwanClient().getStatDataRawData_10(**kwargs)

@register('getAggregationDataByQuery_10')
def getAggregationDataByQuery_10(**kwargs):
    return CatalystwanClient().getAggregationDataByQuery_10(**kwargs)

@register('getStatDataRawDataAsCSV_10')
def getStatDataRawDataAsCSV_10(**kwargs):
    return CatalystwanClient().getStatDataRawDataAsCSV_10(**kwargs)

@register('getCount_10')
def getCount_10(**kwargs):
    return CatalystwanClient().getCount_10(**kwargs)

@register('getStatDataFields_11')
def getStatDataFields_11(**kwargs):
    return CatalystwanClient().getStatDataFields_11(**kwargs)

@register('getStatsPaginationRawData_9')
def getStatsPaginationRawData_9(**kwargs):
    return CatalystwanClient().getStatsPaginationRawData_9(**kwargs)

@register('getStatQueryFields_11')
def getStatQueryFields_11(**kwargs):
    return CatalystwanClient().getStatQueryFields_11(**kwargs)

@register('startStatsCollection')
def startStatsCollection(**kwargs):
    return CatalystwanClient().startStatsCollection(**kwargs)

@register('generateStatsCollectThreadReport')
def generateStatsCollectThreadReport(**kwargs):
    return CatalystwanClient().generateStatsCollectThreadReport(**kwargs)

@register('resetStatsCollection')
def resetStatsCollection(**kwargs):
    return CatalystwanClient().resetStatsCollection(**kwargs)

@register('getStatDataRawDataAsCSV_13')
def getStatDataRawDataAsCSV_13(**kwargs):
    return CatalystwanClient().getStatDataRawDataAsCSV_13(**kwargs)

@register('enableStatisticsDemoMode')
def enableStatisticsDemoMode(**kwargs):
    return CatalystwanClient().enableStatisticsDemoMode(**kwargs)

@register('getStatDataRawData_16')
def getStatDataRawData_16(**kwargs):
    return CatalystwanClient().getStatDataRawData_16(**kwargs)

@register('getAggregationDataByQuery_18')
def getAggregationDataByQuery_18(**kwargs):
    return CatalystwanClient().getAggregationDataByQuery_18(**kwargs)

@register('getStatDataRawDataAsCSV_16')
def getStatDataRawDataAsCSV_16(**kwargs):
    return CatalystwanClient().getStatDataRawDataAsCSV_16(**kwargs)

@register('getCount_15')
def getCount_15(**kwargs):
    return CatalystwanClient().getCount_15(**kwargs)

@register('getStatDataFields_17')
def getStatDataFields_17(**kwargs):
    return CatalystwanClient().getStatDataFields_17(**kwargs)

@register('getStatsPaginationRawData_14')
def getStatsPaginationRawData_14(**kwargs):
    return CatalystwanClient().getStatsPaginationRawData_14(**kwargs)

@register('getStatQueryFields_18')
def getStatQueryFields_18(**kwargs):
    return CatalystwanClient().getStatQueryFields_18(**kwargs)

@register('getDeviceHealthHistory')
def getDeviceHealthHistory(**kwargs):
    return CatalystwanClient().getDeviceHealthHistory(**kwargs)

@register('getDeviceHealthOverview')
def getDeviceHealthOverview(**kwargs):
    return CatalystwanClient().getDeviceHealthOverview(**kwargs)

@register('getCount_12')
def getCount_12(**kwargs):
    return CatalystwanClient().getCount_12(**kwargs)

@register('fetchList')
def fetchList(**kwargs):
    return CatalystwanClient().fetchList(**kwargs)

@register('download')
def download(**kwargs):
    return CatalystwanClient().download(**kwargs)

@register('getDPIStatsRawData')
def getDPIStatsRawData(**kwargs):
    return CatalystwanClient().getDPIStatsRawData(**kwargs)

@register('getDPIStatsAggregationData')
def getDPIStatsAggregationData(**kwargs):
    return CatalystwanClient().getDPIStatsAggregationData(**kwargs)

@register('getAggAppFlows')
def getAggAppFlows(**kwargs):
    return CatalystwanClient().getAggAppFlows(**kwargs)

@register('getAggAppFlowsSummary')
def getAggAppFlowsSummary(**kwargs):
    return CatalystwanClient().getAggAppFlowsSummary(**kwargs)

@register('getDPIStatsRawDataAsCSV')
def getDPIStatsRawDataAsCSV(**kwargs):
    return CatalystwanClient().getDPIStatsRawDataAsCSV(**kwargs)

@register('getDPIDeviceAppUniqueFlowCount')
def getDPIDeviceAppUniqueFlowCount(**kwargs):
    return CatalystwanClient().getDPIDeviceAppUniqueFlowCount(**kwargs)

@register('getDPIDeviceAppAggregationData')
def getDPIDeviceAppAggregationData(**kwargs):
    return CatalystwanClient().getDPIDeviceAppAggregationData(**kwargs)

@register('getDPIDeviceAppDetails')
def getDPIDeviceAppDetails(**kwargs):
    return CatalystwanClient().getDPIDeviceAppDetails(**kwargs)

@register('getDPIStatsCount')
def getDPIStatsCount(**kwargs):
    return CatalystwanClient().getDPIStatsCount(**kwargs)

@register('getDPIFields')
def getDPIFields(**kwargs):
    return CatalystwanClient().getDPIFields(**kwargs)

@register('getDPIStatsPaginationRawData')
def getDPIStatsPaginationRawData(**kwargs):
    return CatalystwanClient().getDPIStatsPaginationRawData(**kwargs)

@register('getDPIQueryFields')
def getDPIQueryFields(**kwargs):
    return CatalystwanClient().getDPIQueryFields(**kwargs)

@register('getStatDataRawData_8')
def getStatDataRawData_8(**kwargs):
    return CatalystwanClient().getStatDataRawData_8(**kwargs)

@register('getAggregationDataByQuery_8')
def getAggregationDataByQuery_8(**kwargs):
    return CatalystwanClient().getAggregationDataByQuery_8(**kwargs)

@register('getStatDataRawDataAsCSV_8')
def getStatDataRawDataAsCSV_8(**kwargs):
    return CatalystwanClient().getStatDataRawDataAsCSV_8(**kwargs)

@register('getCount_8')
def getCount_8(**kwargs):
    return CatalystwanClient().getCount_8(**kwargs)

@register('getStatDataFields_9')
def getStatDataFields_9(**kwargs):
    return CatalystwanClient().getStatDataFields_9(**kwargs)

@register('getStatsPaginationRawData_7')
def getStatsPaginationRawData_7(**kwargs):
    return CatalystwanClient().getStatsPaginationRawData_7(**kwargs)

@register('getStatQueryFields_9')
def getStatQueryFields_9(**kwargs):
    return CatalystwanClient().getStatQueryFields_9(**kwargs)

@register('getStatDataRawData_19')
def getStatDataRawData_19(**kwargs):
    return CatalystwanClient().getStatDataRawData_19(**kwargs)

@register('getAggregationDataByQuery_21')
def getAggregationDataByQuery_21(**kwargs):
    return CatalystwanClient().getAggregationDataByQuery_21(**kwargs)

@register('getStatDataRawDataAsCSV_19')
def getStatDataRawDataAsCSV_19(**kwargs):
    return CatalystwanClient().getStatDataRawDataAsCSV_19(**kwargs)

@register('getCount_18')
def getCount_18(**kwargs):
    return CatalystwanClient().getCount_18(**kwargs)

@register('getStatDataFields_20')
def getStatDataFields_20(**kwargs):
    return CatalystwanClient().getStatDataFields_20(**kwargs)

@register('getStatsPaginationRawData_17')
def getStatsPaginationRawData_17(**kwargs):
    return CatalystwanClient().getStatsPaginationRawData_17(**kwargs)

@register('getStatQueryFields_21')
def getStatQueryFields_21(**kwargs):
    return CatalystwanClient().getStatQueryFields_21(**kwargs)

@register('getStatDataFields_14')
def getStatDataFields_14(**kwargs):
    return CatalystwanClient().getStatDataFields_14(**kwargs)

@register('getStatDataRawData_14')
def getStatDataRawData_14(**kwargs):
    return CatalystwanClient().getStatDataRawData_14(**kwargs)

@register('getAggregationDataByQuery_28')
def getAggregationDataByQuery_28(**kwargs):
    return CatalystwanClient().getAggregationDataByQuery_28(**kwargs)

@register('getStatDataRawDataAsCSV_26')
def getStatDataRawDataAsCSV_26(**kwargs):
    return CatalystwanClient().getStatDataRawDataAsCSV_26(**kwargs)

@register('getFlowlogCount')
def getFlowlogCount(**kwargs):
    return CatalystwanClient().getFlowlogCount(**kwargs)

@register('getFlowlogFields')
def getFlowlogFields(**kwargs):
    return CatalystwanClient().getFlowlogFields(**kwargs)

@register('getStatsPaginationRawData_24')
def getStatsPaginationRawData_24(**kwargs):
    return CatalystwanClient().getStatsPaginationRawData_24(**kwargs)

@register('getFlowlogQueryFields')
def getFlowlogQueryFields(**kwargs):
    return CatalystwanClient().getFlowlogQueryFields(**kwargs)

@register('getStatDataRawData_24')
def getStatDataRawData_24(**kwargs):
    return CatalystwanClient().getStatDataRawData_24(**kwargs)

@register('getAggregationDataByQuery_26')
def getAggregationDataByQuery_26(**kwargs):
    return CatalystwanClient().getAggregationDataByQuery_26(**kwargs)

@register('getStatDataRawDataAsCSV_24')
def getStatDataRawDataAsCSV_24(**kwargs):
    return CatalystwanClient().getStatDataRawDataAsCSV_24(**kwargs)

@register('getCount_23')
def getCount_23(**kwargs):
    return CatalystwanClient().getCount_23(**kwargs)

@register('getStatDataFields_25')
def getStatDataFields_25(**kwargs):
    return CatalystwanClient().getStatDataFields_25(**kwargs)

@register('getStatsPaginationRawData_22')
def getStatsPaginationRawData_22(**kwargs):
    return CatalystwanClient().getStatsPaginationRawData_22(**kwargs)

@register('getStatQueryFields_26')
def getStatQueryFields_26(**kwargs):
    return CatalystwanClient().getStatQueryFields_26(**kwargs)

@register('getStatDataRawData_11')
def getStatDataRawData_11(**kwargs):
    return CatalystwanClient().getStatDataRawData_11(**kwargs)

@register('getAggregationDataByQuery_11')
def getAggregationDataByQuery_11(**kwargs):
    return CatalystwanClient().getAggregationDataByQuery_11(**kwargs)

@register('getBandwidthDistribution')
def getBandwidthDistribution(**kwargs):
    return CatalystwanClient().getBandwidthDistribution(**kwargs)

@register('getStatDataRawDataAsCSV_11')
def getStatDataRawDataAsCSV_11(**kwargs):
    return CatalystwanClient().getStatDataRawDataAsCSV_11(**kwargs)

@register('getCount10')
def getCount10(**kwargs):
    return CatalystwanClient().getCount10(**kwargs)

@register('getStatDataFields_12')
def getStatDataFields_12(**kwargs):
    return CatalystwanClient().getStatDataFields_12(**kwargs)

@register('getStatBulkRawData_1')
def getStatBulkRawData_1(**kwargs):
    return CatalystwanClient().getStatBulkRawData_1(**kwargs)

@register('getStatQueryFields_12')
def getStatQueryFields_12(**kwargs):
    return CatalystwanClient().getStatQueryFields_12(**kwargs)

@register('getStatisticsPerInterface')
def getStatisticsPerInterface(**kwargs):
    return CatalystwanClient().getStatisticsPerInterface(**kwargs)

@register('getStatDataRawData_22')
def getStatDataRawData_22(**kwargs):
    return CatalystwanClient().getStatDataRawData_22(**kwargs)

@register('getAggregationDataByQuery_24')
def getAggregationDataByQuery_24(**kwargs):
    return CatalystwanClient().getAggregationDataByQuery_24(**kwargs)

@register('getStatDataRawDataAsCSV_22')
def getStatDataRawDataAsCSV_22(**kwargs):
    return CatalystwanClient().getStatDataRawDataAsCSV_22(**kwargs)

@register('getCount_21')
def getCount_21(**kwargs):
    return CatalystwanClient().getCount_21(**kwargs)

@register('getStatDataFields_23')
def getStatDataFields_23(**kwargs):
    return CatalystwanClient().getStatDataFields_23(**kwargs)

@register('getStatsPaginationRawData_20')
def getStatsPaginationRawData_20(**kwargs):
    return CatalystwanClient().getStatsPaginationRawData_20(**kwargs)

@register('getStatQueryFields_24')
def getStatQueryFields_24(**kwargs):
    return CatalystwanClient().getStatQueryFields_24(**kwargs)

@register('getQueueEntries')
def getQueueEntries(**kwargs):
    return CatalystwanClient().getQueueEntries(**kwargs)

@register('getQueueProperties')
def getQueueProperties(**kwargs):
    return CatalystwanClient().getQueueProperties(**kwargs)

@register('getStatsPaginationRawData_11')
def getStatsPaginationRawData_11(**kwargs):
    return CatalystwanClient().getStatsPaginationRawData_11(**kwargs)

@register('getApplicationHeatMapDetail')
def getApplicationHeatMapDetail(**kwargs):
    return CatalystwanClient().getApplicationHeatMapDetail(**kwargs)

@register('getApplicationSitesHealth')
def getApplicationSitesHealth(**kwargs):
    return CatalystwanClient().getApplicationSitesHealth(**kwargs)

@register('getApplicationsSiteHealth')
def getApplicationsSiteHealth(**kwargs):
    return CatalystwanClient().getApplicationsSiteHealth(**kwargs)

@register('getApplicationsSitesHealth')
def getApplicationsSitesHealth(**kwargs):
    return CatalystwanClient().getApplicationsSitesHealth(**kwargs)

@register('getSupportedDeviceList')
def getSupportedDeviceList(**kwargs):
    return CatalystwanClient().getSupportedDeviceList(**kwargs)

@register('processStatisticsData')
def processStatisticsData(**kwargs):
    return CatalystwanClient().processStatisticsData(**kwargs)

@register('getStatisticsProcessingCounters')
def getStatisticsProcessingCounters(**kwargs):
    return CatalystwanClient().getStatisticsProcessingCounters(**kwargs)

@register('generateStatsProcessReport')
def generateStatsProcessReport(**kwargs):
    return CatalystwanClient().generateStatsProcessReport(**kwargs)

@register('generateStatsProcessThreadReport')
def generateStatsProcessThreadReport(**kwargs):
    return CatalystwanClient().generateStatsProcessThreadReport(**kwargs)

@register('getStatDataRawData_3')
def getStatDataRawData_3(**kwargs):
    return CatalystwanClient().getStatDataRawData_3(**kwargs)

@register('getAggregationDataByQuery_15')
def getAggregationDataByQuery_15(**kwargs):
    return CatalystwanClient().getAggregationDataByQuery_15(**kwargs)

@register('getStatDataRawDataAsCSV_3')
def getStatDataRawDataAsCSV_3(**kwargs):
    return CatalystwanClient().getStatDataRawDataAsCSV_3(**kwargs)

@register('getCount_3')
def getCount_3(**kwargs):
    return CatalystwanClient().getCount_3(**kwargs)

@register('getStatDataFields_4')
def getStatDataFields_4(**kwargs):
    return CatalystwanClient().getStatDataFields_4(**kwargs)

@register('getStatsPaginationRawData_2')
def getStatsPaginationRawData_2(**kwargs):
    return CatalystwanClient().getStatsPaginationRawData_2(**kwargs)

@register('getStatQueryFields_4')
def getStatQueryFields_4(**kwargs):
    return CatalystwanClient().getStatQueryFields_4(**kwargs)

@register('getStatDataRawData_13')
def getStatDataRawData_13(**kwargs):
    return CatalystwanClient().getStatDataRawData_13(**kwargs)

@register('getAggregationDataByQuery_13')
def getAggregationDataByQuery_13(**kwargs):
    return CatalystwanClient().getAggregationDataByQuery_13(**kwargs)

@register('getStatDataRawDataAsCSV12')
def getStatDataRawDataAsCSV12(**kwargs):
    return CatalystwanClient().getStatDataRawDataAsCSV12(**kwargs)

@register('getCount13')
def getCount13(**kwargs):
    return CatalystwanClient().getCount13(**kwargs)

@register('getStatDataFields13')
def getStatDataFields13(**kwargs):
    return CatalystwanClient().getStatDataFields13(**kwargs)

@register('getStatBulkRawData_2')
def getStatBulkRawData_2(**kwargs):
    return CatalystwanClient().getStatBulkRawData_2(**kwargs)

@register('getStatQueryFields_14')
def getStatQueryFields_14(**kwargs):
    return CatalystwanClient().getStatQueryFields_14(**kwargs)

@register('getStatQueryFields_15')
def getStatQueryFields_15(**kwargs):
    return CatalystwanClient().getStatQueryFields_15(**kwargs)

@register('getSdraHeadendSummary')
def getSdraHeadendSummary(**kwargs):
    return CatalystwanClient().getSdraHeadendSummary(**kwargs)

@register('getSdraSessionSummary')
def getSdraSessionSummary(**kwargs):
    return CatalystwanClient().getSdraSessionSummary(**kwargs)

@register('getDisabledDeviceList')
def getDisabledDeviceList(**kwargs):
    return CatalystwanClient().getDisabledDeviceList(**kwargs)

@register('getStatisticsSettings')
def getStatisticsSettings(**kwargs):
    return CatalystwanClient().getStatisticsSettings(**kwargs)

@register('getEnabledIndexForDevice')
def getEnabledIndexForDevice(**kwargs):
    return CatalystwanClient().getEnabledIndexForDevice(**kwargs)

@register('getStatDataRawData_15')
def getStatDataRawData_15(**kwargs):
    return CatalystwanClient().getStatDataRawData_15(**kwargs)

@register('getAggregationDataByQuery_16')
def getAggregationDataByQuery_16(**kwargs):
    return CatalystwanClient().getAggregationDataByQuery_16(**kwargs)

@register('getSiteHealth')
def getSiteHealth(**kwargs):
    return CatalystwanClient().getSiteHealth(**kwargs)

@register('getStatDataRawDataAsCSV_14')
def getStatDataRawDataAsCSV_14(**kwargs):
    return CatalystwanClient().getStatDataRawDataAsCSV_14(**kwargs)

@register('getCount_13')
def getCount_13(**kwargs):
    return CatalystwanClient().getCount_13(**kwargs)

@register('getStatDataFields_15')
def getStatDataFields_15(**kwargs):
    return CatalystwanClient().getStatDataFields_15(**kwargs)

@register('getStatsPaginationRawData_12')
def getStatsPaginationRawData_12(**kwargs):
    return CatalystwanClient().getStatsPaginationRawData_12(**kwargs)

@register('getStatQueryFields_16')
def getStatQueryFields_16(**kwargs):
    return CatalystwanClient().getStatQueryFields_16(**kwargs)

@register('getSiteHealthTopology')
def getSiteHealthTopology(**kwargs):
    return CatalystwanClient().getSiteHealthTopology(**kwargs)

@register('getStatDataRawData_26')
def getStatDataRawData_26(**kwargs):
    return CatalystwanClient().getStatDataRawData_26(**kwargs)

@register('getAggregationDataByQuery_29')
def getAggregationDataByQuery_29(**kwargs):
    return CatalystwanClient().getAggregationDataByQuery_29(**kwargs)

@register('getStatDataRawDataAsCSV_27')
def getStatDataRawDataAsCSV_27(**kwargs):
    return CatalystwanClient().getStatDataRawDataAsCSV_27(**kwargs)

@register('getCount_25')
def getCount_25(**kwargs):
    return CatalystwanClient().getCount_25(**kwargs)

@register('getStatDataFields_27')
def getStatDataFields_27(**kwargs):
    return CatalystwanClient().getStatDataFields_27(**kwargs)

@register('getStatsPaginationRawData_25')
def getStatsPaginationRawData_25(**kwargs):
    return CatalystwanClient().getStatsPaginationRawData_25(**kwargs)

@register('getStatQueryFields_29')
def getStatQueryFields_29(**kwargs):
    return CatalystwanClient().getStatQueryFields_29(**kwargs)

@register('getSulStatDataRawData')
def getSulStatDataRawData(**kwargs):
    return CatalystwanClient().getSulStatDataRawData(**kwargs)

@register('getAggregationDataByQuery_17')
def getAggregationDataByQuery_17(**kwargs):
    return CatalystwanClient().getAggregationDataByQuery_17(**kwargs)

@register('getStatDataRawDataAsCSV_15')
def getStatDataRawDataAsCSV_15(**kwargs):
    return CatalystwanClient().getStatDataRawDataAsCSV_15(**kwargs)

@register('getCount_14')
def getCount_14(**kwargs):
    return CatalystwanClient().getCount_14(**kwargs)

@register('getStatDataFields_16')
def getStatDataFields_16(**kwargs):
    return CatalystwanClient().getStatDataFields_16(**kwargs)

@register('getFilterPolicyNameList')
def getFilterPolicyNameList(**kwargs):
    return CatalystwanClient().getFilterPolicyNameList(**kwargs)

@register('getStatsPaginationRawData_13')
def getStatsPaginationRawData_13(**kwargs):
    return CatalystwanClient().getStatsPaginationRawData_13(**kwargs)

@register('getStatQueryFields_17')
def getStatQueryFields_17(**kwargs):
    return CatalystwanClient().getStatQueryFields_17(**kwargs)

@register('getStatDataRawData_17')
def getStatDataRawData_17(**kwargs):
    return CatalystwanClient().getStatDataRawData_17(**kwargs)

@register('getAggregationDataByQuery_19')
def getAggregationDataByQuery_19(**kwargs):
    return CatalystwanClient().getAggregationDataByQuery_19(**kwargs)

@register('createDeviceSystemCPUStat')
def createDeviceSystemCPUStat(**kwargs):
    return CatalystwanClient().createDeviceSystemCPUStat(**kwargs)

@register('getStatDataRawDataAsCSV_17')
def getStatDataRawDataAsCSV_17(**kwargs):
    return CatalystwanClient().getStatDataRawDataAsCSV_17(**kwargs)

@register('getCount_16')
def getCount_16(**kwargs):
    return CatalystwanClient().getCount_16(**kwargs)

@register('getStatDataFields_18')
def getStatDataFields_18(**kwargs):
    return CatalystwanClient().getStatDataFields_18(**kwargs)

@register('createDeviceSystemMemoryStat')
def createDeviceSystemMemoryStat(**kwargs):
    return CatalystwanClient().createDeviceSystemMemoryStat(**kwargs)

@register('getStatsPaginationRawData_15')
def getStatsPaginationRawData_15(**kwargs):
    return CatalystwanClient().getStatsPaginationRawData_15(**kwargs)

@register('getStatQueryFields_19')
def getStatQueryFields_19(**kwargs):
    return CatalystwanClient().getStatQueryFields_19(**kwargs)

@register('getStatDataRawData_18')
def getStatDataRawData_18(**kwargs):
    return CatalystwanClient().getStatDataRawData_18(**kwargs)

@register('getAggregationDataByQuery_20')
def getAggregationDataByQuery_20(**kwargs):
    return CatalystwanClient().getAggregationDataByQuery_20(**kwargs)

@register('getStatDataRawDataAsCSV_18')
def getStatDataRawDataAsCSV_18(**kwargs):
    return CatalystwanClient().getStatDataRawDataAsCSV_18(**kwargs)

@register('getCount_17')
def getCount_17(**kwargs):
    return CatalystwanClient().getCount_17(**kwargs)

@register('getStatDataFields_19')
def getStatDataFields_19(**kwargs):
    return CatalystwanClient().getStatDataFields_19(**kwargs)

@register('getStatsPaginationRawData_16')
def getStatsPaginationRawData_16(**kwargs):
    return CatalystwanClient().getStatsPaginationRawData_16(**kwargs)

@register('getStatQueryFields_20')
def getStatQueryFields_20(**kwargs):
    return CatalystwanClient().getStatQueryFields_20(**kwargs)

@register('statisticsApprouteTunnelhealthHistoryGet')
def statisticsApprouteTunnelhealthHistoryGet(**kwargs):
    return CatalystwanClient().statisticsApprouteTunnelhealthHistoryGet(**kwargs)

@register('statisticsApprouteTunnelhealthOverviewTypeGet')
def statisticsApprouteTunnelhealthOverviewTypeGet(**kwargs):
    return CatalystwanClient().statisticsApprouteTunnelhealthOverviewTypeGet(**kwargs)

@register('getStatDataRawData_25')
def getStatDataRawData_25(**kwargs):
    return CatalystwanClient().getStatDataRawData_25(**kwargs)

@register('getAggregationDataByQuery_27')
def getAggregationDataByQuery_27(**kwargs):
    return CatalystwanClient().getAggregationDataByQuery_27(**kwargs)

@register('getStatDataRawDataAsCSV_25')
def getStatDataRawDataAsCSV_25(**kwargs):
    return CatalystwanClient().getStatDataRawDataAsCSV_25(**kwargs)

@register('getCount_24')
def getCount_24(**kwargs):
    return CatalystwanClient().getCount_24(**kwargs)

@register('getStatDataFields_26')
def getStatDataFields_26(**kwargs):
    return CatalystwanClient().getStatDataFields_26(**kwargs)

@register('getStatsPaginationRawData_23')
def getStatsPaginationRawData_23(**kwargs):
    return CatalystwanClient().getStatsPaginationRawData_23(**kwargs)

@register('getStatQueryFields_27')
def getStatQueryFields_27(**kwargs):
    return CatalystwanClient().getStatQueryFields_27(**kwargs)

@register('getStatDataRawData_23')
def getStatDataRawData_23(**kwargs):
    return CatalystwanClient().getStatDataRawData_23(**kwargs)

@register('getAggregationDataByQuery_25')
def getAggregationDataByQuery_25(**kwargs):
    return CatalystwanClient().getAggregationDataByQuery_25(**kwargs)

@register('getStatDataRawDataAsCSV_23')
def getStatDataRawDataAsCSV_23(**kwargs):
    return CatalystwanClient().getStatDataRawDataAsCSV_23(**kwargs)

@register('getCount_22')
def getCount_22(**kwargs):
    return CatalystwanClient().getCount_22(**kwargs)

@register('getStatDataFields_24')
def getStatDataFields_24(**kwargs):
    return CatalystwanClient().getStatDataFields_24(**kwargs)

@register('getStatsPaginationRawData_21')
def getStatsPaginationRawData_21(**kwargs):
    return CatalystwanClient().getStatsPaginationRawData_21(**kwargs)

@register('getStatQueryFields_25')
def getStatQueryFields_25(**kwargs):
    return CatalystwanClient().getStatQueryFields_25(**kwargs)

@register('getStatDataRawData_12')
def getStatDataRawData_12(**kwargs):
    return CatalystwanClient().getStatDataRawData_12(**kwargs)

@register('getAggregationDataByQuery_12')
def getAggregationDataByQuery_12(**kwargs):
    return CatalystwanClient().getAggregationDataByQuery_12(**kwargs)

@register('getStatDataRawDataAsCSV_12')
def getStatDataRawDataAsCSV_12(**kwargs):
    return CatalystwanClient().getStatDataRawDataAsCSV_12(**kwargs)

@register('getCount_11')
def getCount_11(**kwargs):
    return CatalystwanClient().getCount_11(**kwargs)

@register('getStatDataFields_13')
def getStatDataFields_13(**kwargs):
    return CatalystwanClient().getStatDataFields_13(**kwargs)

@register('getStatsPaginationRawData_10')
def getStatsPaginationRawData_10(**kwargs):
    return CatalystwanClient().getStatsPaginationRawData_10(**kwargs)

@register('getStatQueryFields_13')
def getStatQueryFields_13(**kwargs):
    return CatalystwanClient().getStatQueryFields_13(**kwargs)

@register('getStatDataRawData_20')
def getStatDataRawData_20(**kwargs):
    return CatalystwanClient().getStatDataRawData_20(**kwargs)

@register('getAggregationDataByQuery_22')
def getAggregationDataByQuery_22(**kwargs):
    return CatalystwanClient().getAggregationDataByQuery_22(**kwargs)

@register('getStatDataRawDataAsCSV_20')
def getStatDataRawDataAsCSV_20(**kwargs):
    return CatalystwanClient().getStatDataRawDataAsCSV_20(**kwargs)

@register('getCount_19')
def getCount_19(**kwargs):
    return CatalystwanClient().getCount_19(**kwargs)

@register('getStatDataFields_21')
def getStatDataFields_21(**kwargs):
    return CatalystwanClient().getStatDataFields_21(**kwargs)

@register('getStatsPaginationRawData_18')
def getStatsPaginationRawData_18(**kwargs):
    return CatalystwanClient().getStatsPaginationRawData_18(**kwargs)

@register('getStatQueryFields_22')
def getStatQueryFields_22(**kwargs):
    return CatalystwanClient().getStatQueryFields_22(**kwargs)

@register('disablePacketCaptureSession')
def disablePacketCaptureSession(**kwargs):
    return CatalystwanClient().disablePacketCaptureSession(**kwargs)

@register('downloadFile')
def downloadFile(**kwargs):
    return CatalystwanClient().downloadFile(**kwargs)

@register('forceStopPcapSession')
def forceStopPcapSession(**kwargs):
    return CatalystwanClient().forceStopPcapSession(**kwargs)

@register('startPcapSession')
def startPcapSession(**kwargs):
    return CatalystwanClient().startPcapSession(**kwargs)

@register('getFileDownloadStatus')
def getFileDownloadStatus(**kwargs):
    return CatalystwanClient().getFileDownloadStatus(**kwargs)

@register('stopPcapSession')
def stopPcapSession(**kwargs):
    return CatalystwanClient().stopPcapSession(**kwargs)

@register('getVnicInfoByVnfId')
def getVnicInfoByVnfId(**kwargs):
    return CatalystwanClient().getVnicInfoByVnfId(**kwargs)

@register('disableDeviceLog')
def disableDeviceLog(**kwargs):
    return CatalystwanClient().disableDeviceLog(**kwargs)

@register('downloadDebugLog')
def downloadDebugLog(**kwargs):
    return CatalystwanClient().downloadDebugLog(**kwargs)

@register('renewSessionInfo')
def renewSessionInfo(**kwargs):
    return CatalystwanClient().renewSessionInfo(**kwargs)

@register('getSessions')
def getSessions(**kwargs):
    return CatalystwanClient().getSessions(**kwargs)

@register('clearSession')
def clearSession(**kwargs):
    return CatalystwanClient().clearSession(**kwargs)

@register('getLogType')
def getLogType(**kwargs):
    return CatalystwanClient().getLogType(**kwargs)

@register('getDeviceLog')
def getDeviceLog(**kwargs):
    return CatalystwanClient().getDeviceLog(**kwargs)

@register('activeFlowWithQuery')
def activeFlowWithQuery(**kwargs):
    return CatalystwanClient().activeFlowWithQuery(**kwargs)

@register('getAggFlow')
def getAggFlow(**kwargs):
    return CatalystwanClient().getAggFlow(**kwargs)

@register('getAppQosData')
def getAppQosData(**kwargs):
    return CatalystwanClient().getAppQosData(**kwargs)

@register('getAppQosState')
def getAppQosState(**kwargs):
    return CatalystwanClient().getAppQosState(**kwargs)

@register('getConcurrentData')
def getConcurrentData(**kwargs):
    return CatalystwanClient().getConcurrentData(**kwargs)

@register('getConcurrentDomainData')
def getConcurrentDomainData(**kwargs):
    return CatalystwanClient().getConcurrentDomainData(**kwargs)

@register('getCurrentTimestamp')
def getCurrentTimestamp(**kwargs):
    return CatalystwanClient().getCurrentTimestamp(**kwargs)

@register('getDeviceBList')
def getDeviceBList(**kwargs):
    return CatalystwanClient().getDeviceBList(**kwargs)

@register('getDevicesAndInterfacesBySite')
def getDevicesAndInterfacesBySite(**kwargs):
    return CatalystwanClient().getDevicesAndInterfacesBySite(**kwargs)

@register('getDomainMetric')
def getDomainMetric(**kwargs):
    return CatalystwanClient().getDomainMetric(**kwargs)

@register('getEventAppHopList')
def getEventAppHopList(**kwargs):
    return CatalystwanClient().getEventAppHopList(**kwargs)

@register('getEventAppScoreBandwidth')
def getEventAppScoreBandwidth(**kwargs):
    return CatalystwanClient().getEventAppScoreBandwidth(**kwargs)

@register('getEventFlowFromAppHop')
def getEventFlowFromAppHop(**kwargs):
    return CatalystwanClient().getEventFlowFromAppHop(**kwargs)

@register('getEventReadout')
def getEventReadout(**kwargs):
    return CatalystwanClient().getEventReadout(**kwargs)

@register('getEventReadoutBySite')
def getEventReadoutBySite(**kwargs):
    return CatalystwanClient().getEventReadoutBySite(**kwargs)

@register('getEventReadoutByTraces')
def getEventReadoutByTraces(**kwargs):
    return CatalystwanClient().getEventReadoutByTraces(**kwargs)

@register('exportTrace')
def exportTrace(**kwargs):
    return CatalystwanClient().exportTrace(**kwargs)

@register('getFinalizedData')
def getFinalizedData(**kwargs):
    return CatalystwanClient().getFinalizedData(**kwargs)

@register('getFinalizedDomainData')
def getFinalizedDomainData(**kwargs):
    return CatalystwanClient().getFinalizedDomainData(**kwargs)

@register('getFlowDetail')
def getFlowDetail(**kwargs):
    return CatalystwanClient().getFlowDetail(**kwargs)

@register('getFlowMetric')
def getFlowMetric(**kwargs):
    return CatalystwanClient().getFlowMetric(**kwargs)

@register('getMonitorState')
def getMonitorState(**kwargs):
    return CatalystwanClient().getMonitorState(**kwargs)

@register('getNwpiDscp')
def getNwpiDscp(**kwargs):
    return CatalystwanClient().getNwpiDscp(**kwargs)

@register('getNwpiNbarAppGroup')
def getNwpiNbarAppGroup(**kwargs):
    return CatalystwanClient().getNwpiNbarAppGroup(**kwargs)

@register('getNwpiProtocol')
def getNwpiProtocol(**kwargs):
    return CatalystwanClient().getNwpiProtocol(**kwargs)

@register('nwpiSettingView')
def nwpiSettingView(**kwargs):
    return CatalystwanClient().nwpiSettingView(**kwargs)

@register('getPacketFeatures')
def getPacketFeatures(**kwargs):
    return CatalystwanClient().getPacketFeatures(**kwargs)

@register('getPreloadInfo')
def getPreloadInfo(**kwargs):
    return CatalystwanClient().getPreloadInfo(**kwargs)

@register('getStatQueryFields_28')
def getStatQueryFields_28(**kwargs):
    return CatalystwanClient().getStatQueryFields_28(**kwargs)

@register('getRoutingDetailFromLocal')
def getRoutingDetailFromLocal(**kwargs):
    return CatalystwanClient().getRoutingDetailFromLocal(**kwargs)

@register('getEventStatsData')
def getEventStatsData(**kwargs):
    return CatalystwanClient().getEventStatsData(**kwargs)

@register('getTaskHistory')
def getTaskHistory(**kwargs):
    return CatalystwanClient().getTaskHistory(**kwargs)

@register('getTaskTrace')
def getTaskTrace(**kwargs):
    return CatalystwanClient().getTaskTrace(**kwargs)

@register('getTraceCftRecord')
def getTraceCftRecord(**kwargs):
    return CatalystwanClient().getTraceCftRecord(**kwargs)

@register('getFinalizedFlowCount')
def getFinalizedFlowCount(**kwargs):
    return CatalystwanClient().getFinalizedFlowCount(**kwargs)

@register('getFinFlowTimeRange')
def getFinFlowTimeRange(**kwargs):
    return CatalystwanClient().getFinFlowTimeRange(**kwargs)

@register('traceFinFlowWithQuery')
def traceFinFlowWithQuery(**kwargs):
    return CatalystwanClient().traceFinFlowWithQuery(**kwargs)

@register('getTraceFlow')
def getTraceFlow(**kwargs):
    return CatalystwanClient().getTraceFlow(**kwargs)

@register('getTraceHistory')
def getTraceHistory(**kwargs):
    return CatalystwanClient().getTraceHistory(**kwargs)

@register('getTraceInfoByBaseKey')
def getTraceInfoByBaseKey(**kwargs):
    return CatalystwanClient().getTraceInfoByBaseKey(**kwargs)

@register('getTraceReadoutFilter')
def getTraceReadoutFilter(**kwargs):
    return CatalystwanClient().getTraceReadoutFilter(**kwargs)

@register('disableSpeedTestSession')
def disableSpeedTestSession(**kwargs):
    return CatalystwanClient().disableSpeedTestSession(**kwargs)

@register('getInterfaceBandwidth')
def getInterfaceBandwidth(**kwargs):
    return CatalystwanClient().getInterfaceBandwidth(**kwargs)

@register('startSpeedTest')
def startSpeedTest(**kwargs):
    return CatalystwanClient().startSpeedTest(**kwargs)

@register('getSpeedTestStatus')
def getSpeedTestStatus(**kwargs):
    return CatalystwanClient().getSpeedTestStatus(**kwargs)

@register('stopSpeedTest')
def stopSpeedTest(**kwargs):
    return CatalystwanClient().stopSpeedTest(**kwargs)

@register('getSpeedTest')
def getSpeedTest(**kwargs):
    return CatalystwanClient().getSpeedTest(**kwargs)

@register('getUMTSData')
def getUMTSData(**kwargs):
    return CatalystwanClient().getUMTSData(**kwargs)

@register('updateUmtsSessionStatus')
def updateUmtsSessionStatus(**kwargs):
    return CatalystwanClient().updateUmtsSessionStatus(**kwargs)

@register('generateBootstrapConfigForVedge')
def generateBootstrapConfigForVedge(**kwargs):
    return CatalystwanClient().generateBootstrapConfigForVedge(**kwargs)

@register('getBootstrapConfigZip')
def getBootstrapConfigZip(**kwargs):
    return CatalystwanClient().getBootstrapConfigZip(**kwargs)

@register('generateGenericBootstrapConfigForVedges')
def generateGenericBootstrapConfigForVedges(**kwargs):
    return CatalystwanClient().generateGenericBootstrapConfigForVedges(**kwargs)

@register('getControllerVEdgeSyncStatus_1')
def getControllerVEdgeSyncStatus_1(**kwargs):
    return CatalystwanClient().getControllerVEdgeSyncStatus_1(**kwargs)

@register('devicesWithoutSubjectSudi')
def devicesWithoutSubjectSudi(**kwargs):
    return CatalystwanClient().devicesWithoutSubjectSudi(**kwargs)

@register('getManagementSystemIPInfo_1')
def getManagementSystemIPInfo_1(**kwargs):
    return CatalystwanClient().getManagementSystemIPInfo_1(**kwargs)

@register('getRMACandidates')
def getRMACandidates(**kwargs):
    return CatalystwanClient().getRMACandidates(**kwargs)

@register('getRootCertStatusAll')
def getRootCertStatusAll(**kwargs):
    return CatalystwanClient().getRootCertStatusAll(**kwargs)

@register('checkSelfSignedCert_1')
def checkSelfSignedCert_1(**kwargs):
    return CatalystwanClient().checkSelfSignedCert_1(**kwargs)

@register('syncRootCertChain')
def syncRootCertChain(**kwargs):
    return CatalystwanClient().syncRootCertChain(**kwargs)

@register('getTenantManagementSystemIPs')
def getTenantManagementSystemIPs(**kwargs):
    return CatalystwanClient().getTenantManagementSystemIPs(**kwargs)

@register('getCloudDockDataBasedOnDeviceType')
def getCloudDockDataBasedOnDeviceType(**kwargs):
    return CatalystwanClient().getCloudDockDataBasedOnDeviceType(**kwargs)

@register('getCloudDockDefaultConfigBasedOnDeviceType')
def getCloudDockDefaultConfigBasedOnDeviceType(**kwargs):
    return CatalystwanClient().getCloudDockDefaultConfigBasedOnDeviceType(**kwargs)

@register('getAllUnclaimedDevices')
def getAllUnclaimedDevices(**kwargs):
    return CatalystwanClient().getAllUnclaimedDevices(**kwargs)

@register('checkvEdgeDevicePresence')
def checkvEdgeDevicePresence(**kwargs):
    return CatalystwanClient().checkvEdgeDevicePresence(**kwargs)

@register('getDevicesDetails')
def getDevicesDetails(**kwargs):
    return CatalystwanClient().getDevicesDetails(**kwargs)

@register('getReverseProxyMappings')
def getReverseProxyMappings(**kwargs):
    return CatalystwanClient().getReverseProxyMappings(**kwargs)

@register('getCloudXStatus')
def getCloudXStatus(**kwargs):
    return CatalystwanClient().getCloudXStatus(**kwargs)

@register('getAttachedClientList')
def getAttachedClientList(**kwargs):
    return CatalystwanClient().getAttachedClientList(**kwargs)

@register('getAttachedDiaList')
def getAttachedDiaList(**kwargs):
    return CatalystwanClient().getAttachedDiaList(**kwargs)

@register('getAttachedGatewayList')
def getAttachedGatewayList(**kwargs):
    return CatalystwanClient().getAttachedGatewayList(**kwargs)

@register('getCloudXAvailableApps')
def getCloudXAvailableApps(**kwargs):
    return CatalystwanClient().getCloudXAvailableApps(**kwargs)

@register('getSiteList')
def getSiteList(**kwargs):
    return CatalystwanClient().getSiteList(**kwargs)

@register('getDiaList')
def getDiaList(**kwargs):
    return CatalystwanClient().getDiaList(**kwargs)

@register('getGatewayList')
def getGatewayList(**kwargs):
    return CatalystwanClient().getGatewayList(**kwargs)

@register('getApps')
def getApps(**kwargs):
    return CatalystwanClient().getApps(**kwargs)

@register('getSigTunnelList_1')
def getSigTunnelList_1(**kwargs):
    return CatalystwanClient().getSigTunnelList_1(**kwargs)

@register('sitePerApp')
def sitePerApp(**kwargs):
    return CatalystwanClient().sitePerApp(**kwargs)

@register('getAttachedConfig')
def getAttachedConfig(**kwargs):
    return CatalystwanClient().getAttachedConfig(**kwargs)

@register('generateCLIModeDevices')
def generateCLIModeDevices(**kwargs):
    return CatalystwanClient().generateCLIModeDevices(**kwargs)

@register('generatevManageModeDevices')
def generatevManageModeDevices(**kwargs):
    return CatalystwanClient().generatevManageModeDevices(**kwargs)

@register('getDeviceDiff')
def getDeviceDiff(**kwargs):
    return CatalystwanClient().getDeviceDiff(**kwargs)

@register('getCompatibleDevices')
def getCompatibleDevices(**kwargs):
    return CatalystwanClient().getCompatibleDevices(**kwargs)

@register('getRunningConfig')
def getRunningConfig(**kwargs):
    return CatalystwanClient().getRunningConfig(**kwargs)

@register('getVpnForDevice')
def getVpnForDevice(**kwargs):
    return CatalystwanClient().getVpnForDevice(**kwargs)

@register('getCORStatus')
def getCORStatus(**kwargs):
    return CatalystwanClient().getCORStatus(**kwargs)

@register('getAmiList')
def getAmiList(**kwargs):
    return CatalystwanClient().getAmiList(**kwargs)

@register('getCloudList')
def getCloudList(**kwargs):
    return CatalystwanClient().getCloudList(**kwargs)

@register('getCloudAccounts')
def getCloudAccounts(**kwargs):
    return CatalystwanClient().getCloudAccounts(**kwargs)

@register('getCloudHostVpcAccountDetails')
def getCloudHostVpcAccountDetails(**kwargs):
    return CatalystwanClient().getCloudHostVpcAccountDetails(**kwargs)

@register('getCloudMappedHostAccounts')
def getCloudMappedHostAccounts(**kwargs):
    return CatalystwanClient().getCloudMappedHostAccounts(**kwargs)

@register('getCloudOnRampDevices')
def getCloudOnRampDevices(**kwargs):
    return CatalystwanClient().getCloudOnRampDevices(**kwargs)

@register('getHostVPCs')
def getHostVPCs(**kwargs):
    return CatalystwanClient().getHostVPCs(**kwargs)

@register('getExternalId')
def getExternalId(**kwargs):
    return CatalystwanClient().getExternalId(**kwargs)

@register('getTransitDevicePairAndHostList')
def getTransitDevicePairAndHostList(**kwargs):
    return CatalystwanClient().getTransitDevicePairAndHostList(**kwargs)

@register('getTransitVpcVpnList')
def getTransitVpcVpnList(**kwargs):
    return CatalystwanClient().getTransitVpcVpnList(**kwargs)

@register('getCloudHostVPCs')
def getCloudHostVPCs(**kwargs):
    return CatalystwanClient().getCloudHostVPCs(**kwargs)

@register('getMappedVPCs')
def getMappedVPCs(**kwargs):
    return CatalystwanClient().getMappedVPCs(**kwargs)

@register('getPemKeyList')
def getPemKeyList(**kwargs):
    return CatalystwanClient().getPemKeyList(**kwargs)

@register('getTransitVPCs')
def getTransitVPCs(**kwargs):
    return CatalystwanClient().getTransitVPCs(**kwargs)

@register('getTransitVPCSupportedSize')
def getTransitVPCSupportedSize(**kwargs):
    return CatalystwanClient().getTransitVPCSupportedSize(**kwargs)

@register('getCortexStatus')
def getCortexStatus(**kwargs):
    return CatalystwanClient().getCortexStatus(**kwargs)

@register('getMappedWanResourceGroups')
def getMappedWanResourceGroups(**kwargs):
    return CatalystwanClient().getMappedWanResourceGroups(**kwargs)

@register('getWanResourceGroups')
def getWanResourceGroups(**kwargs):
    return CatalystwanClient().getWanResourceGroups(**kwargs)

@register('generateMasterTemplateList')
def generateMasterTemplateList(**kwargs):
    return CatalystwanClient().generateMasterTemplateList(**kwargs)

@register('getAttachedDeviceList')
def getAttachedDeviceList(**kwargs):
    return CatalystwanClient().getAttachedDeviceList(**kwargs)

@register('getAttachedConfigToDevice')
def getAttachedConfigToDevice(**kwargs):
    return CatalystwanClient().getAttachedConfigToDevice(**kwargs)

@register('getDeviceListByMasterTemplateId')
def getDeviceListByMasterTemplateId(**kwargs):
    return CatalystwanClient().getDeviceListByMasterTemplateId(**kwargs)

@register('checkVbond')
def checkVbond(**kwargs):
    return CatalystwanClient().checkVbond(**kwargs)

@register('isMigrationRequired')
def isMigrationRequired(**kwargs):
    return CatalystwanClient().isMigrationRequired(**kwargs)

@register('generateTemplateForMigration')
def generateTemplateForMigration(**kwargs):
    return CatalystwanClient().generateTemplateForMigration(**kwargs)

@register('migrationInfo')
def migrationInfo(**kwargs):
    return CatalystwanClient().migrationInfo(**kwargs)

@register('getMasterTemplateDefinition')
def getMasterTemplateDefinition(**kwargs):
    return CatalystwanClient().getMasterTemplateDefinition(**kwargs)

@register('getOutOfSyncTemplates')
def getOutOfSyncTemplates(**kwargs):
    return CatalystwanClient().getOutOfSyncTemplates(**kwargs)

@register('getOutOfSyncDevices')
def getOutOfSyncDevices(**kwargs):
    return CatalystwanClient().getOutOfSyncDevices(**kwargs)

@register('getAssociatedFeatureTemplatesDetails')
def getAssociatedFeatureTemplatesDetails(**kwargs):
    return CatalystwanClient().getAssociatedFeatureTemplatesDetails(**kwargs)

@register('generateFeatureTemplateList')
def generateFeatureTemplateList(**kwargs):
    return CatalystwanClient().generateFeatureTemplateList(**kwargs)

@register('getNetworkInterface')
def getNetworkInterface(**kwargs):
    return CatalystwanClient().getNetworkInterface(**kwargs)

@register('getDefaultNetworks')
def getDefaultNetworks(**kwargs):
    return CatalystwanClient().getDefaultNetworks(**kwargs)

@register('getTemplateDefinition')
def getTemplateDefinition(**kwargs):
    return CatalystwanClient().getTemplateDefinition(**kwargs)

@register('getDeviceTemplatesAttachedToFeature')
def getDeviceTemplatesAttachedToFeature(**kwargs):
    return CatalystwanClient().getDeviceTemplatesAttachedToFeature(**kwargs)

@register('listLITemplate')
def listLITemplate(**kwargs):
    return CatalystwanClient().listLITemplate(**kwargs)

@register('generateMasterTemplateDefinition')
def generateMasterTemplateDefinition(**kwargs):
    return CatalystwanClient().generateMasterTemplateDefinition(**kwargs)

@register('getTemplateForMigration')
def getTemplateForMigration(**kwargs):
    return CatalystwanClient().getTemplateForMigration(**kwargs)

@register('getGeneralTemplate')
def getGeneralTemplate(**kwargs):
    return CatalystwanClient().getGeneralTemplate(**kwargs)

@register('generateTemplateTypes')
def generateTemplateTypes(**kwargs):
    return CatalystwanClient().generateTemplateTypes(**kwargs)

@register('generateTemplateTypeDefinition')
def generateTemplateTypeDefinition(**kwargs):
    return CatalystwanClient().generateTemplateTypeDefinition(**kwargs)

@register('generateTemplateByDeviceType')
def generateTemplateByDeviceType(**kwargs):
    return CatalystwanClient().generateTemplateByDeviceType(**kwargs)

@register('previewById')
def previewById(**kwargs):
    return CatalystwanClient().previewById(**kwargs)

@register('previewById_1')
def previewById_1(**kwargs):
    return CatalystwanClient().previewById_1(**kwargs)

@register('previewById_2')
def previewById_2(**kwargs):
    return CatalystwanClient().previewById_2(**kwargs)

@register('previewById_3')
def previewById_3(**kwargs):
    return CatalystwanClient().previewById_3(**kwargs)

@register('getCloudDiscoveredApps')
def getCloudDiscoveredApps(**kwargs):
    return CatalystwanClient().getCloudDiscoveredApps(**kwargs)

@register('getCustomApps')
def getCustomApps(**kwargs):
    return CatalystwanClient().getCustomApps(**kwargs)

@register('getCustomAppById')
def getCustomAppById(**kwargs):
    return CatalystwanClient().getCustomAppById(**kwargs)

@register('getDefinitions_8')
def getDefinitions_8(**kwargs):
    return CatalystwanClient().getDefinitions_8(**kwargs)

@register('previewPolicyDefinitionById_8')
def previewPolicyDefinitionById_8(**kwargs):
    return CatalystwanClient().previewPolicyDefinitionById_8(**kwargs)

@register('getPolicyDefinition_8')
def getPolicyDefinition_8(**kwargs):
    return CatalystwanClient().getPolicyDefinition_8(**kwargs)

@register('getDefinitions_9')
def getDefinitions_9(**kwargs):
    return CatalystwanClient().getDefinitions_9(**kwargs)

@register('previewPolicyDefinitionById_9')
def previewPolicyDefinitionById_9(**kwargs):
    return CatalystwanClient().previewPolicyDefinitionById_9(**kwargs)

@register('getPolicyDefinition_9')
def getPolicyDefinition_9(**kwargs):
    return CatalystwanClient().getPolicyDefinition_9(**kwargs)

@register('getDefinitions_11')
def getDefinitions_11(**kwargs):
    return CatalystwanClient().getDefinitions_11(**kwargs)

@register('previewPolicyDefinitionById_11')
def previewPolicyDefinitionById_11(**kwargs):
    return CatalystwanClient().previewPolicyDefinitionById_11(**kwargs)

@register('getPolicyDefinition_11')
def getPolicyDefinition_11(**kwargs):
    return CatalystwanClient().getPolicyDefinition_11(**kwargs)

@register('getDefinitions_10')
def getDefinitions_10(**kwargs):
    return CatalystwanClient().getDefinitions_10(**kwargs)

@register('previewPolicyDefinitionById_10')
def previewPolicyDefinitionById_10(**kwargs):
    return CatalystwanClient().previewPolicyDefinitionById_10(**kwargs)

@register('getPolicyDefinition_10')
def getPolicyDefinition_10(**kwargs):
    return CatalystwanClient().getPolicyDefinition_10(**kwargs)

@register('getDefinitions_12')
def getDefinitions_12(**kwargs):
    return CatalystwanClient().getDefinitions_12(**kwargs)

@register('previewPolicyDefinitionById_12')
def previewPolicyDefinitionById_12(**kwargs):
    return CatalystwanClient().previewPolicyDefinitionById_12(**kwargs)

@register('getPolicyDefinition_12')
def getPolicyDefinition_12(**kwargs):
    return CatalystwanClient().getPolicyDefinition_12(**kwargs)

@register('getDefinitions_13')
def getDefinitions_13(**kwargs):
    return CatalystwanClient().getDefinitions_13(**kwargs)

@register('previewPolicyDefinitionById_13')
def previewPolicyDefinitionById_13(**kwargs):
    return CatalystwanClient().previewPolicyDefinitionById_13(**kwargs)

@register('getPolicyDefinition_13')
def getPolicyDefinition_13(**kwargs):
    return CatalystwanClient().getPolicyDefinition_13(**kwargs)

@register('getDefinitions_14')
def getDefinitions_14(**kwargs):
    return CatalystwanClient().getDefinitions_14(**kwargs)

@register('previewPolicyDefinitionById_14')
def previewPolicyDefinitionById_14(**kwargs):
    return CatalystwanClient().previewPolicyDefinitionById_14(**kwargs)

@register('getPolicyDefinition_14')
def getPolicyDefinition_14(**kwargs):
    return CatalystwanClient().getPolicyDefinition_14(**kwargs)

@register('getDefinitions_15')
def getDefinitions_15(**kwargs):
    return CatalystwanClient().getDefinitions_15(**kwargs)

@register('previewPolicyDefinitionById_15')
def previewPolicyDefinitionById_15(**kwargs):
    return CatalystwanClient().previewPolicyDefinitionById_15(**kwargs)

@register('getPolicyDefinition_15')
def getPolicyDefinition_15(**kwargs):
    return CatalystwanClient().getPolicyDefinition_15(**kwargs)

@register('getDefinitions_16')
def getDefinitions_16(**kwargs):
    return CatalystwanClient().getDefinitions_16(**kwargs)

@register('previewPolicyDefinitionById_16')
def previewPolicyDefinitionById_16(**kwargs):
    return CatalystwanClient().previewPolicyDefinitionById_16(**kwargs)

@register('getPolicyDefinition_16')
def getPolicyDefinition_16(**kwargs):
    return CatalystwanClient().getPolicyDefinition_16(**kwargs)

@register('getDefinitions_17')
def getDefinitions_17(**kwargs):
    return CatalystwanClient().getDefinitions_17(**kwargs)

@register('previewPolicyDefinitionById_17')
def previewPolicyDefinitionById_17(**kwargs):
    return CatalystwanClient().previewPolicyDefinitionById_17(**kwargs)

@register('getPolicyDefinition_17')
def getPolicyDefinition_17(**kwargs):
    return CatalystwanClient().getPolicyDefinition_17(**kwargs)

@register('getDefinitions_25')
def getDefinitions_25(**kwargs):
    return CatalystwanClient().getDefinitions_25(**kwargs)

@register('previewPolicyDefinitionById_25')
def previewPolicyDefinitionById_25(**kwargs):
    return CatalystwanClient().previewPolicyDefinitionById_25(**kwargs)

@register('getPolicyDefinition_25')
def getPolicyDefinition_25(**kwargs):
    return CatalystwanClient().getPolicyDefinition_25(**kwargs)

@register('getDefinitions')
def getDefinitions(**kwargs):
    return CatalystwanClient().getDefinitions(**kwargs)

@register('previewPolicyDefinitionById')
def previewPolicyDefinitionById(**kwargs):
    return CatalystwanClient().previewPolicyDefinitionById(**kwargs)

@register('getPolicyDefinition')
def getPolicyDefinition(**kwargs):
    return CatalystwanClient().getPolicyDefinition(**kwargs)

@register('getDefinitions_26')
def getDefinitions_26(**kwargs):
    return CatalystwanClient().getDefinitions_26(**kwargs)

@register('previewPolicyDefinitionById_26')
def previewPolicyDefinitionById_26(**kwargs):
    return CatalystwanClient().previewPolicyDefinitionById_26(**kwargs)

@register('getPolicyDefinition_26')
def getPolicyDefinition_26(**kwargs):
    return CatalystwanClient().getPolicyDefinition_26(**kwargs)

@register('getDefinitions_28')
def getDefinitions_28(**kwargs):
    return CatalystwanClient().getDefinitions_28(**kwargs)

@register('previewPolicyDefinitionById_28')
def previewPolicyDefinitionById_28(**kwargs):
    return CatalystwanClient().previewPolicyDefinitionById_28(**kwargs)

@register('getPolicyDefinition_28')
def getPolicyDefinition_28(**kwargs):
    return CatalystwanClient().getPolicyDefinition_28(**kwargs)

@register('getDefinitions_27')
def getDefinitions_27(**kwargs):
    return CatalystwanClient().getDefinitions_27(**kwargs)

@register('previewPolicyDefinitionById_27')
def previewPolicyDefinitionById_27(**kwargs):
    return CatalystwanClient().previewPolicyDefinitionById_27(**kwargs)

@register('getPolicyDefinition_27')
def getPolicyDefinition_27(**kwargs):
    return CatalystwanClient().getPolicyDefinition_27(**kwargs)

@register('getDefinitions_4')
def getDefinitions_4(**kwargs):
    return CatalystwanClient().getDefinitions_4(**kwargs)

@register('previewPolicyDefinitionById_4')
def previewPolicyDefinitionById_4(**kwargs):
    return CatalystwanClient().previewPolicyDefinitionById_4(**kwargs)

@register('getPolicyDefinition_4')
def getPolicyDefinition_4(**kwargs):
    return CatalystwanClient().getPolicyDefinition_4(**kwargs)

@register('getDefinitions_18')
def getDefinitions_18(**kwargs):
    return CatalystwanClient().getDefinitions_18(**kwargs)

@register('previewPolicyDefinitionById_18')
def previewPolicyDefinitionById_18(**kwargs):
    return CatalystwanClient().previewPolicyDefinitionById_18(**kwargs)

@register('getPolicyDefinition_18')
def getPolicyDefinition_18(**kwargs):
    return CatalystwanClient().getPolicyDefinition_18(**kwargs)

@register('getDefinitions_5')
def getDefinitions_5(**kwargs):
    return CatalystwanClient().getDefinitions_5(**kwargs)

@register('previewPolicyDefinitionById_5')
def previewPolicyDefinitionById_5(**kwargs):
    return CatalystwanClient().previewPolicyDefinitionById_5(**kwargs)

@register('getPolicyDefinition_5')
def getPolicyDefinition_5(**kwargs):
    return CatalystwanClient().getPolicyDefinition_5(**kwargs)

@register('getDefinitions_29')
def getDefinitions_29(**kwargs):
    return CatalystwanClient().getDefinitions_29(**kwargs)

@register('previewPolicyDefinitionById_29')
def previewPolicyDefinitionById_29(**kwargs):
    return CatalystwanClient().previewPolicyDefinitionById_29(**kwargs)

@register('getPolicyDefinition_29')
def getPolicyDefinition_29(**kwargs):
    return CatalystwanClient().getPolicyDefinition_29(**kwargs)

@register('getDefinitions_1')
def getDefinitions_1(**kwargs):
    return CatalystwanClient().getDefinitions_1(**kwargs)

@register('previewPolicyDefinitionById_1')
def previewPolicyDefinitionById_1(**kwargs):
    return CatalystwanClient().previewPolicyDefinitionById_1(**kwargs)

@register('getPolicyDefinition_1')
def getPolicyDefinition_1(**kwargs):
    return CatalystwanClient().getPolicyDefinition_1(**kwargs)

@register('getDefinitions_19')
def getDefinitions_19(**kwargs):
    return CatalystwanClient().getDefinitions_19(**kwargs)

@register('previewPolicyDefinitionById_19')
def previewPolicyDefinitionById_19(**kwargs):
    return CatalystwanClient().previewPolicyDefinitionById_19(**kwargs)

@register('getPolicyDefinition_19')
def getPolicyDefinition_19(**kwargs):
    return CatalystwanClient().getPolicyDefinition_19(**kwargs)

@register('getDefinitions_20')
def getDefinitions_20(**kwargs):
    return CatalystwanClient().getDefinitions_20(**kwargs)

@register('previewPolicyDefinitionById_20')
def previewPolicyDefinitionById_20(**kwargs):
    return CatalystwanClient().previewPolicyDefinitionById_20(**kwargs)

@register('getPolicyDefinition_20')
def getPolicyDefinition_20(**kwargs):
    return CatalystwanClient().getPolicyDefinition_20(**kwargs)

@register('getDefinitions_21')
def getDefinitions_21(**kwargs):
    return CatalystwanClient().getDefinitions_21(**kwargs)

@register('previewPolicyDefinitionById_21')
def previewPolicyDefinitionById_21(**kwargs):
    return CatalystwanClient().previewPolicyDefinitionById_21(**kwargs)

@register('getPolicyDefinition_21')
def getPolicyDefinition_21(**kwargs):
    return CatalystwanClient().getPolicyDefinition_21(**kwargs)

@register('getDefinitions_30')
def getDefinitions_30(**kwargs):
    return CatalystwanClient().getDefinitions_30(**kwargs)

@register('previewPolicyDefinitionById_30')
def previewPolicyDefinitionById_30(**kwargs):
    return CatalystwanClient().previewPolicyDefinitionById_30(**kwargs)

@register('getPolicyDefinition_30')
def getPolicyDefinition_30(**kwargs):
    return CatalystwanClient().getPolicyDefinition_30(**kwargs)

@register('getDefinitions_3')
def getDefinitions_3(**kwargs):
    return CatalystwanClient().getDefinitions_3(**kwargs)

@register('previewPolicyDefinitionById_3')
def previewPolicyDefinitionById_3(**kwargs):
    return CatalystwanClient().previewPolicyDefinitionById_3(**kwargs)

@register('getPolicyDefinition_3')
def getPolicyDefinition_3(**kwargs):
    return CatalystwanClient().getPolicyDefinition_3(**kwargs)

@register('getDefinitions_22')
def getDefinitions_22(**kwargs):
    return CatalystwanClient().getDefinitions_22(**kwargs)

@register('previewPolicyDefinitionById_22')
def previewPolicyDefinitionById_22(**kwargs):
    return CatalystwanClient().previewPolicyDefinitionById_22(**kwargs)

@register('getPolicyDefinition_22')
def getPolicyDefinition_22(**kwargs):
    return CatalystwanClient().getPolicyDefinition_22(**kwargs)

@register('getDefinitions_23')
def getDefinitions_23(**kwargs):
    return CatalystwanClient().getDefinitions_23(**kwargs)

@register('previewPolicyDefinitionById_23')
def previewPolicyDefinitionById_23(**kwargs):
    return CatalystwanClient().previewPolicyDefinitionById_23(**kwargs)

@register('getPolicyDefinition_23')
def getPolicyDefinition_23(**kwargs):
    return CatalystwanClient().getPolicyDefinition_23(**kwargs)

@register('getDefinitions_24')
def getDefinitions_24(**kwargs):
    return CatalystwanClient().getDefinitions_24(**kwargs)

@register('previewPolicyDefinitionById_24')
def previewPolicyDefinitionById_24(**kwargs):
    return CatalystwanClient().previewPolicyDefinitionById_24(**kwargs)

@register('getPolicyDefinition_24')
def getPolicyDefinition_24(**kwargs):
    return CatalystwanClient().getPolicyDefinition_24(**kwargs)

@register('getDefinitions_6')
def getDefinitions_6(**kwargs):
    return CatalystwanClient().getDefinitions_6(**kwargs)

@register('previewPolicyDefinitionById_6')
def previewPolicyDefinitionById_6(**kwargs):
    return CatalystwanClient().previewPolicyDefinitionById_6(**kwargs)

@register('getPolicyDefinition_6')
def getPolicyDefinition_6(**kwargs):
    return CatalystwanClient().getPolicyDefinition_6(**kwargs)

@register('getDefinitions_2')
def getDefinitions_2(**kwargs):
    return CatalystwanClient().getDefinitions_2(**kwargs)

@register('previewPolicyDefinitionById_2')
def previewPolicyDefinitionById_2(**kwargs):
    return CatalystwanClient().previewPolicyDefinitionById_2(**kwargs)

@register('getPolicyDefinition_2')
def getPolicyDefinition_2(**kwargs):
    return CatalystwanClient().getPolicyDefinition_2(**kwargs)

@register('getDefinitions_7')
def getDefinitions_7(**kwargs):
    return CatalystwanClient().getDefinitions_7(**kwargs)

@register('previewPolicyDefinitionById_7')
def previewPolicyDefinitionById_7(**kwargs):
    return CatalystwanClient().previewPolicyDefinitionById_7(**kwargs)

@register('getPolicyDefinition_7')
def getPolicyDefinition_7(**kwargs):
    return CatalystwanClient().getPolicyDefinition_7(**kwargs)

@register('getListReference')
def getListReference(**kwargs):
    return CatalystwanClient().getListReference(**kwargs)

@register('sgts')
def sgts(**kwargs):
    return CatalystwanClient().sgts(**kwargs)

@register('getAllPolicyLists')
def getAllPolicyLists(**kwargs):
    return CatalystwanClient().getAllPolicyLists(**kwargs)

@register('getPolicyLists_3')
def getPolicyLists_3(**kwargs):
    return CatalystwanClient().getPolicyLists_3(**kwargs)

@register('getPolicyListsWithInfoTag_3')
def getPolicyListsWithInfoTag_3(**kwargs):
    return CatalystwanClient().getPolicyListsWithInfoTag_3(**kwargs)

@register('previewPolicyListById_3')
def previewPolicyListById_3(**kwargs):
    return CatalystwanClient().previewPolicyListById_3(**kwargs)

@register('getListsById_3')
def getListsById_3(**kwargs):
    return CatalystwanClient().getListsById_3(**kwargs)

@register('getPolicyLists_4')
def getPolicyLists_4(**kwargs):
    return CatalystwanClient().getPolicyLists_4(**kwargs)

@register('getPolicyListsWithInfoTag_4')
def getPolicyListsWithInfoTag_4(**kwargs):
    return CatalystwanClient().getPolicyListsWithInfoTag_4(**kwargs)

@register('previewPolicyListById_4')
def previewPolicyListById_4(**kwargs):
    return CatalystwanClient().previewPolicyListById_4(**kwargs)

@register('getListsById_4')
def getListsById_4(**kwargs):
    return CatalystwanClient().getListsById_4(**kwargs)

@register('getPolicyLists_5')
def getPolicyLists_5(**kwargs):
    return CatalystwanClient().getPolicyLists_5(**kwargs)

@register('getPolicyListsWithInfoTag_5')
def getPolicyListsWithInfoTag_5(**kwargs):
    return CatalystwanClient().getPolicyListsWithInfoTag_5(**kwargs)

@register('previewPolicyListById_5')
def previewPolicyListById_5(**kwargs):
    return CatalystwanClient().previewPolicyListById_5(**kwargs)

@register('getListsById_5')
def getListsById_5(**kwargs):
    return CatalystwanClient().getListsById_5(**kwargs)

@register('getPolicyLists_13')
def getPolicyLists_13(**kwargs):
    return CatalystwanClient().getPolicyLists_13(**kwargs)

@register('getPolicyListsWithInfoTag_14')
def getPolicyListsWithInfoTag_14(**kwargs):
    return CatalystwanClient().getPolicyListsWithInfoTag_14(**kwargs)

@register('previewPolicyListById_14')
def previewPolicyListById_14(**kwargs):
    return CatalystwanClient().previewPolicyListById_14(**kwargs)

@register('getListsById_14')
def getListsById_14(**kwargs):
    return CatalystwanClient().getListsById_14(**kwargs)

@register('getPolicyLists_6')
def getPolicyLists_6(**kwargs):
    return CatalystwanClient().getPolicyLists_6(**kwargs)

@register('getPolicyListsWithInfoTag_6')
def getPolicyListsWithInfoTag_6(**kwargs):
    return CatalystwanClient().getPolicyListsWithInfoTag_6(**kwargs)

@register('previewPolicyListById_6')
def previewPolicyListById_6(**kwargs):
    return CatalystwanClient().previewPolicyListById_6(**kwargs)

@register('getListsById_6')
def getListsById_6(**kwargs):
    return CatalystwanClient().getListsById_6(**kwargs)

@register('getPolicyLists_7')
def getPolicyLists_7(**kwargs):
    return CatalystwanClient().getPolicyLists_7(**kwargs)

@register('getPolicyListsWithInfoTag_7')
def getPolicyListsWithInfoTag_7(**kwargs):
    return CatalystwanClient().getPolicyListsWithInfoTag_7(**kwargs)

@register('previewPolicyListById_7')
def previewPolicyListById_7(**kwargs):
    return CatalystwanClient().previewPolicyListById_7(**kwargs)

@register('getListsById_7')
def getListsById_7(**kwargs):
    return CatalystwanClient().getListsById_7(**kwargs)

@register('getPolicyLists_8')
def getPolicyLists_8(**kwargs):
    return CatalystwanClient().getPolicyLists_8(**kwargs)

@register('getPolicyListsWithInfoTag_8')
def getPolicyListsWithInfoTag_8(**kwargs):
    return CatalystwanClient().getPolicyListsWithInfoTag_8(**kwargs)

@register('previewPolicyListById_8')
def previewPolicyListById_8(**kwargs):
    return CatalystwanClient().previewPolicyListById_8(**kwargs)

@register('getListsById_8')
def getListsById_8(**kwargs):
    return CatalystwanClient().getListsById_8(**kwargs)

@register('getPolicyLists_9')
def getPolicyLists_9(**kwargs):
    return CatalystwanClient().getPolicyLists_9(**kwargs)

@register('getPolicyListsWithInfoTag_10')
def getPolicyListsWithInfoTag_10(**kwargs):
    return CatalystwanClient().getPolicyListsWithInfoTag_10(**kwargs)

@register('previewPolicyListById_10')
def previewPolicyListById_10(**kwargs):
    return CatalystwanClient().previewPolicyListById_10(**kwargs)

@register('getListsById_10')
def getListsById_10(**kwargs):
    return CatalystwanClient().getListsById_10(**kwargs)

@register('getListsForAllDataPrefixes')
def getListsForAllDataPrefixes(**kwargs):
    return CatalystwanClient().getListsForAllDataPrefixes(**kwargs)

@register('getPolicyListsWithInfoTag_9')
def getPolicyListsWithInfoTag_9(**kwargs):
    return CatalystwanClient().getPolicyListsWithInfoTag_9(**kwargs)

@register('previewPolicyListById_9')
def previewPolicyListById_9(**kwargs):
    return CatalystwanClient().previewPolicyListById_9(**kwargs)

@register('getListsById_9')
def getListsById_9(**kwargs):
    return CatalystwanClient().getListsById_9(**kwargs)

@register('getAllDataPrefixAndFQDNLists')
def getAllDataPrefixAndFQDNLists(**kwargs):
    return CatalystwanClient().getAllDataPrefixAndFQDNLists(**kwargs)

@register('getPolicyListsWithInfoTag_15')
def getPolicyListsWithInfoTag_15(**kwargs):
    return CatalystwanClient().getPolicyListsWithInfoTag_15(**kwargs)

@register('previewPolicyListById_15')
def previewPolicyListById_15(**kwargs):
    return CatalystwanClient().previewPolicyListById_15(**kwargs)

@register('getListsById_15')
def getListsById_15(**kwargs):
    return CatalystwanClient().getListsById_15(**kwargs)

@register('getPolicyLists_10')
def getPolicyLists_10(**kwargs):
    return CatalystwanClient().getPolicyLists_10(**kwargs)

@register('getPolicyListsWithInfoTag_11')
def getPolicyListsWithInfoTag_11(**kwargs):
    return CatalystwanClient().getPolicyListsWithInfoTag_11(**kwargs)

@register('previewPolicyListById_11')
def previewPolicyListById_11(**kwargs):
    return CatalystwanClient().previewPolicyListById_11(**kwargs)

@register('getListsById_11')
def getListsById_11(**kwargs):
    return CatalystwanClient().getListsById_11(**kwargs)

@register('getPolicyLists_11')
def getPolicyLists_11(**kwargs):
    return CatalystwanClient().getPolicyLists_11(**kwargs)

@register('getPolicyListsWithInfoTag_12')
def getPolicyListsWithInfoTag_12(**kwargs):
    return CatalystwanClient().getPolicyListsWithInfoTag_12(**kwargs)

@register('previewPolicyListById_12')
def previewPolicyListById_12(**kwargs):
    return CatalystwanClient().previewPolicyListById_12(**kwargs)

@register('getListsById_12')
def getListsById_12(**kwargs):
    return CatalystwanClient().getListsById_12(**kwargs)

@register('getPolicyLists_12')
def getPolicyLists_12(**kwargs):
    return CatalystwanClient().getPolicyLists_12(**kwargs)

@register('getPolicyListsWithInfoTag_13')
def getPolicyListsWithInfoTag_13(**kwargs):
    return CatalystwanClient().getPolicyListsWithInfoTag_13(**kwargs)

@register('previewPolicyListById_13')
def previewPolicyListById_13(**kwargs):
    return CatalystwanClient().previewPolicyListById_13(**kwargs)

@register('getListsById_13')
def getListsById_13(**kwargs):
    return CatalystwanClient().getListsById_13(**kwargs)

@register('getPolicyLists_14')
def getPolicyLists_14(**kwargs):
    return CatalystwanClient().getPolicyLists_14(**kwargs)

@register('getPolicyListsWithInfoTag_16')
def getPolicyListsWithInfoTag_16(**kwargs):
    return CatalystwanClient().getPolicyListsWithInfoTag_16(**kwargs)

@register('previewPolicyListById_16')
def previewPolicyListById_16(**kwargs):
    return CatalystwanClient().previewPolicyListById_16(**kwargs)

@register('getListsById_16')
def getListsById_16(**kwargs):
    return CatalystwanClient().getListsById_16(**kwargs)

@register('getPolicyLists_15')
def getPolicyLists_15(**kwargs):
    return CatalystwanClient().getPolicyLists_15(**kwargs)

@register('getGeoLocationLists')
def getGeoLocationLists(**kwargs):
    return CatalystwanClient().getGeoLocationLists(**kwargs)

@register('getPolicyListsWithInfoTag_17')
def getPolicyListsWithInfoTag_17(**kwargs):
    return CatalystwanClient().getPolicyListsWithInfoTag_17(**kwargs)

@register('previewPolicyListById_17')
def previewPolicyListById_17(**kwargs):
    return CatalystwanClient().previewPolicyListById_17(**kwargs)

@register('getListsById_17')
def getListsById_17(**kwargs):
    return CatalystwanClient().getListsById_17(**kwargs)

@register('getPolicyLists_16')
def getPolicyLists_16(**kwargs):
    return CatalystwanClient().getPolicyLists_16(**kwargs)

@register('getPolicyListsWithInfoTag_18')
def getPolicyListsWithInfoTag_18(**kwargs):
    return CatalystwanClient().getPolicyListsWithInfoTag_18(**kwargs)

@register('previewPolicyListById_18')
def previewPolicyListById_18(**kwargs):
    return CatalystwanClient().previewPolicyListById_18(**kwargs)

@register('getListsById_18')
def getListsById_18(**kwargs):
    return CatalystwanClient().getListsById_18(**kwargs)

@register('getListsForAllPrefixes')
def getListsForAllPrefixes(**kwargs):
    return CatalystwanClient().getListsForAllPrefixes(**kwargs)

@register('getPolicyListsWithInfoTag_21')
def getPolicyListsWithInfoTag_21(**kwargs):
    return CatalystwanClient().getPolicyListsWithInfoTag_21(**kwargs)

@register('previewPolicyListById_21')
def previewPolicyListById_21(**kwargs):
    return CatalystwanClient().previewPolicyListById_21(**kwargs)

@register('getListsById_21')
def getListsById_21(**kwargs):
    return CatalystwanClient().getListsById_21(**kwargs)

@register('getPolicyLists_17')
def getPolicyLists_17(**kwargs):
    return CatalystwanClient().getPolicyLists_17(**kwargs)

@register('getPolicyListsWithInfoTag_19')
def getPolicyListsWithInfoTag_19(**kwargs):
    return CatalystwanClient().getPolicyListsWithInfoTag_19(**kwargs)

@register('previewPolicyListById_19')
def previewPolicyListById_19(**kwargs):
    return CatalystwanClient().previewPolicyListById_19(**kwargs)

@register('getListsById_19')
def getListsById_19(**kwargs):
    return CatalystwanClient().getListsById_19(**kwargs)

@register('getPolicyLists_18')
def getPolicyLists_18(**kwargs):
    return CatalystwanClient().getPolicyLists_18(**kwargs)

@register('getPolicyListsWithInfoTag_20')
def getPolicyListsWithInfoTag_20(**kwargs):
    return CatalystwanClient().getPolicyListsWithInfoTag_20(**kwargs)

@register('previewPolicyListById_20')
def previewPolicyListById_20(**kwargs):
    return CatalystwanClient().previewPolicyListById_20(**kwargs)

@register('getListsById_20')
def getListsById_20(**kwargs):
    return CatalystwanClient().getListsById_20(**kwargs)

@register('getPolicyLists_19')
def getPolicyLists_19(**kwargs):
    return CatalystwanClient().getPolicyLists_19(**kwargs)

@register('getPolicyListsWithInfoTag_22')
def getPolicyListsWithInfoTag_22(**kwargs):
    return CatalystwanClient().getPolicyListsWithInfoTag_22(**kwargs)

@register('previewPolicyListById_22')
def previewPolicyListById_22(**kwargs):
    return CatalystwanClient().previewPolicyListById_22(**kwargs)

@register('getListsById_22')
def getListsById_22(**kwargs):
    return CatalystwanClient().getListsById_22(**kwargs)

@register('getPolicyLists_20')
def getPolicyLists_20(**kwargs):
    return CatalystwanClient().getPolicyLists_20(**kwargs)

@register('getPolicyListsWithInfoTag_23')
def getPolicyListsWithInfoTag_23(**kwargs):
    return CatalystwanClient().getPolicyListsWithInfoTag_23(**kwargs)

@register('previewPolicyListById_23')
def previewPolicyListById_23(**kwargs):
    return CatalystwanClient().previewPolicyListById_23(**kwargs)

@register('getListsById_23')
def getListsById_23(**kwargs):
    return CatalystwanClient().getListsById_23(**kwargs)

@register('getPolicyLists')
def getPolicyLists(**kwargs):
    return CatalystwanClient().getPolicyLists(**kwargs)

@register('getPolicyListsWithInfoTag')
def getPolicyListsWithInfoTag(**kwargs):
    return CatalystwanClient().getPolicyListsWithInfoTag(**kwargs)

@register('previewPolicyListById')
def previewPolicyListById(**kwargs):
    return CatalystwanClient().previewPolicyListById(**kwargs)

@register('getListsById')
def getListsById(**kwargs):
    return CatalystwanClient().getListsById(**kwargs)

@register('getPolicyLists_21')
def getPolicyLists_21(**kwargs):
    return CatalystwanClient().getPolicyLists_21(**kwargs)

@register('getPolicyListsWithInfoTag_24')
def getPolicyListsWithInfoTag_24(**kwargs):
    return CatalystwanClient().getPolicyListsWithInfoTag_24(**kwargs)

@register('previewPolicyListById_24')
def previewPolicyListById_24(**kwargs):
    return CatalystwanClient().previewPolicyListById_24(**kwargs)

@register('getListsById_24')
def getListsById_24(**kwargs):
    return CatalystwanClient().getListsById_24(**kwargs)

@register('getPolicyLists_22')
def getPolicyLists_22(**kwargs):
    return CatalystwanClient().getPolicyLists_22(**kwargs)

@register('getPolicyListsWithInfoTag_25')
def getPolicyListsWithInfoTag_25(**kwargs):
    return CatalystwanClient().getPolicyListsWithInfoTag_25(**kwargs)

@register('previewPolicyListById_25')
def previewPolicyListById_25(**kwargs):
    return CatalystwanClient().previewPolicyListById_25(**kwargs)

@register('getListsById_25')
def getListsById_25(**kwargs):
    return CatalystwanClient().getListsById_25(**kwargs)

@register('getPolicyLists_23')
def getPolicyLists_23(**kwargs):
    return CatalystwanClient().getPolicyLists_23(**kwargs)

@register('getPolicyListsWithInfoTag_26')
def getPolicyListsWithInfoTag_26(**kwargs):
    return CatalystwanClient().getPolicyListsWithInfoTag_26(**kwargs)

@register('previewPolicyListById_26')
def previewPolicyListById_26(**kwargs):
    return CatalystwanClient().previewPolicyListById_26(**kwargs)

@register('getListsById_26')
def getListsById_26(**kwargs):
    return CatalystwanClient().getListsById_26(**kwargs)

@register('getPolicyLists_24')
def getPolicyLists_24(**kwargs):
    return CatalystwanClient().getPolicyLists_24(**kwargs)

@register('getPolicyListsWithInfoTag_27')
def getPolicyListsWithInfoTag_27(**kwargs):
    return CatalystwanClient().getPolicyListsWithInfoTag_27(**kwargs)

@register('previewPolicyListById_27')
def previewPolicyListById_27(**kwargs):
    return CatalystwanClient().previewPolicyListById_27(**kwargs)

@register('getListsById_27')
def getListsById_27(**kwargs):
    return CatalystwanClient().getListsById_27(**kwargs)

@register('getPolicyLists_25')
def getPolicyLists_25(**kwargs):
    return CatalystwanClient().getPolicyLists_25(**kwargs)

@register('getPolicyListsWithInfoTag_28')
def getPolicyListsWithInfoTag_28(**kwargs):
    return CatalystwanClient().getPolicyListsWithInfoTag_28(**kwargs)

@register('previewPolicyListById_28')
def previewPolicyListById_28(**kwargs):
    return CatalystwanClient().previewPolicyListById_28(**kwargs)

@register('getListsById_28')
def getListsById_28(**kwargs):
    return CatalystwanClient().getListsById_28(**kwargs)

@register('getPolicyLists_26')
def getPolicyLists_26(**kwargs):
    return CatalystwanClient().getPolicyLists_26(**kwargs)

@register('getPolicyListsWithInfoTag_29')
def getPolicyListsWithInfoTag_29(**kwargs):
    return CatalystwanClient().getPolicyListsWithInfoTag_29(**kwargs)

@register('previewPolicyListById_29')
def previewPolicyListById_29(**kwargs):
    return CatalystwanClient().previewPolicyListById_29(**kwargs)

@register('getListsById_29')
def getListsById_29(**kwargs):
    return CatalystwanClient().getListsById_29(**kwargs)

@register('getPolicyLists_27')
def getPolicyLists_27(**kwargs):
    return CatalystwanClient().getPolicyLists_27(**kwargs)

@register('getPolicyListsWithInfoTag_30')
def getPolicyListsWithInfoTag_30(**kwargs):
    return CatalystwanClient().getPolicyListsWithInfoTag_30(**kwargs)

@register('previewPolicyListById_30')
def previewPolicyListById_30(**kwargs):
    return CatalystwanClient().previewPolicyListById_30(**kwargs)

@register('getListsById_30')
def getListsById_30(**kwargs):
    return CatalystwanClient().getListsById_30(**kwargs)

@register('getPolicyLists_28')
def getPolicyLists_28(**kwargs):
    return CatalystwanClient().getPolicyLists_28(**kwargs)

@register('getPolicyListsWithInfoTag_31')
def getPolicyListsWithInfoTag_31(**kwargs):
    return CatalystwanClient().getPolicyListsWithInfoTag_31(**kwargs)

@register('previewPolicyListById_31')
def previewPolicyListById_31(**kwargs):
    return CatalystwanClient().previewPolicyListById_31(**kwargs)

@register('getListsById_31')
def getListsById_31(**kwargs):
    return CatalystwanClient().getListsById_31(**kwargs)

@register('getPolicyLists_29')
def getPolicyLists_29(**kwargs):
    return CatalystwanClient().getPolicyLists_29(**kwargs)

@register('getPolicyListsWithInfoTag_32')
def getPolicyListsWithInfoTag_32(**kwargs):
    return CatalystwanClient().getPolicyListsWithInfoTag_32(**kwargs)

@register('previewPolicyListById_32')
def previewPolicyListById_32(**kwargs):
    return CatalystwanClient().previewPolicyListById_32(**kwargs)

@register('getListsById_32')
def getListsById_32(**kwargs):
    return CatalystwanClient().getListsById_32(**kwargs)

@register('getPolicyLists_30')
def getPolicyLists_30(**kwargs):
    return CatalystwanClient().getPolicyLists_30(**kwargs)

@register('getPolicyListsWithInfoTag_33')
def getPolicyListsWithInfoTag_33(**kwargs):
    return CatalystwanClient().getPolicyListsWithInfoTag_33(**kwargs)

@register('previewPolicyListById_33')
def previewPolicyListById_33(**kwargs):
    return CatalystwanClient().previewPolicyListById_33(**kwargs)

@register('getListsById_33')
def getListsById_33(**kwargs):
    return CatalystwanClient().getListsById_33(**kwargs)

@register('getPolicyLists_31')
def getPolicyLists_31(**kwargs):
    return CatalystwanClient().getPolicyLists_31(**kwargs)

@register('getPolicyListsWithInfoTag_34')
def getPolicyListsWithInfoTag_34(**kwargs):
    return CatalystwanClient().getPolicyListsWithInfoTag_34(**kwargs)

@register('previewPolicyListById_34')
def previewPolicyListById_34(**kwargs):
    return CatalystwanClient().previewPolicyListById_34(**kwargs)

@register('getListsById_34')
def getListsById_34(**kwargs):
    return CatalystwanClient().getListsById_34(**kwargs)

@register('getPolicyLists_32')
def getPolicyLists_32(**kwargs):
    return CatalystwanClient().getPolicyLists_32(**kwargs)

@register('getPolicyListsWithInfoTag_35')
def getPolicyListsWithInfoTag_35(**kwargs):
    return CatalystwanClient().getPolicyListsWithInfoTag_35(**kwargs)

@register('previewPolicyListById_35')
def previewPolicyListById_35(**kwargs):
    return CatalystwanClient().previewPolicyListById_35(**kwargs)

@register('getListsById_35')
def getListsById_35(**kwargs):
    return CatalystwanClient().getListsById_35(**kwargs)

@register('getPolicyLists_33')
def getPolicyLists_33(**kwargs):
    return CatalystwanClient().getPolicyLists_33(**kwargs)

@register('getPolicyListsWithInfoTag_36')
def getPolicyListsWithInfoTag_36(**kwargs):
    return CatalystwanClient().getPolicyListsWithInfoTag_36(**kwargs)

@register('previewPolicyListById_36')
def previewPolicyListById_36(**kwargs):
    return CatalystwanClient().previewPolicyListById_36(**kwargs)

@register('getListsById_36')
def getListsById_36(**kwargs):
    return CatalystwanClient().getListsById_36(**kwargs)

@register('getPolicyLists_34')
def getPolicyLists_34(**kwargs):
    return CatalystwanClient().getPolicyLists_34(**kwargs)

@register('getPolicyListsWithInfoTag_37')
def getPolicyListsWithInfoTag_37(**kwargs):
    return CatalystwanClient().getPolicyListsWithInfoTag_37(**kwargs)

@register('previewPolicyListById_37')
def previewPolicyListById_37(**kwargs):
    return CatalystwanClient().previewPolicyListById_37(**kwargs)

@register('getListsById_37')
def getListsById_37(**kwargs):
    return CatalystwanClient().getListsById_37(**kwargs)

@register('getPolicyLists_1')
def getPolicyLists_1(**kwargs):
    return CatalystwanClient().getPolicyLists_1(**kwargs)

@register('getPolicyListsWithInfoTag_1')
def getPolicyListsWithInfoTag_1(**kwargs):
    return CatalystwanClient().getPolicyListsWithInfoTag_1(**kwargs)

@register('previewPolicyListById_1')
def previewPolicyListById_1(**kwargs):
    return CatalystwanClient().previewPolicyListById_1(**kwargs)

@register('getListsById_1')
def getListsById_1(**kwargs):
    return CatalystwanClient().getListsById_1(**kwargs)

@register('getPolicyLists_2')
def getPolicyLists_2(**kwargs):
    return CatalystwanClient().getPolicyLists_2(**kwargs)

@register('getPolicyListsWithInfoTag_2')
def getPolicyListsWithInfoTag_2(**kwargs):
    return CatalystwanClient().getPolicyListsWithInfoTag_2(**kwargs)

@register('previewPolicyListById_2')
def previewPolicyListById_2(**kwargs):
    return CatalystwanClient().previewPolicyListById_2(**kwargs)

@register('getListsById_2')
def getListsById_2(**kwargs):
    return CatalystwanClient().getListsById_2(**kwargs)

@register('getPolicyLists_35')
def getPolicyLists_35(**kwargs):
    return CatalystwanClient().getPolicyLists_35(**kwargs)

@register('getPolicyListsWithInfoTag_38')
def getPolicyListsWithInfoTag_38(**kwargs):
    return CatalystwanClient().getPolicyListsWithInfoTag_38(**kwargs)

@register('previewPolicyListById_38')
def previewPolicyListById_38(**kwargs):
    return CatalystwanClient().previewPolicyListById_38(**kwargs)

@register('getListsById_38')
def getListsById_38(**kwargs):
    return CatalystwanClient().getListsById_38(**kwargs)

@register('getPolicyLists_36')
def getPolicyLists_36(**kwargs):
    return CatalystwanClient().getPolicyLists_36(**kwargs)

@register('getPolicyListsWithInfoTag_39')
def getPolicyListsWithInfoTag_39(**kwargs):
    return CatalystwanClient().getPolicyListsWithInfoTag_39(**kwargs)

@register('previewPolicyListById_39')
def previewPolicyListById_39(**kwargs):
    return CatalystwanClient().previewPolicyListById_39(**kwargs)

@register('getListsById_39')
def getListsById_39(**kwargs):
    return CatalystwanClient().getListsById_39(**kwargs)

@register('getPolicyLists_37')
def getPolicyLists_37(**kwargs):
    return CatalystwanClient().getPolicyLists_37(**kwargs)

@register('getPolicyListsWithInfoTag_40')
def getPolicyListsWithInfoTag_40(**kwargs):
    return CatalystwanClient().getPolicyListsWithInfoTag_40(**kwargs)

@register('previewPolicyListById_40')
def previewPolicyListById_40(**kwargs):
    return CatalystwanClient().previewPolicyListById_40(**kwargs)

@register('getListsById_40')
def getListsById_40(**kwargs):
    return CatalystwanClient().getListsById_40(**kwargs)

@register('getPolicyLists_38')
def getPolicyLists_38(**kwargs):
    return CatalystwanClient().getPolicyLists_38(**kwargs)

@register('getPolicyListsWithInfoTag_41')
def getPolicyListsWithInfoTag_41(**kwargs):
    return CatalystwanClient().getPolicyListsWithInfoTag_41(**kwargs)

@register('previewPolicyListById_41')
def previewPolicyListById_41(**kwargs):
    return CatalystwanClient().previewPolicyListById_41(**kwargs)

@register('getListsById_41')
def getListsById_41(**kwargs):
    return CatalystwanClient().getListsById_41(**kwargs)

@register('getPolicyLists_39')
def getPolicyLists_39(**kwargs):
    return CatalystwanClient().getPolicyLists_39(**kwargs)

@register('getPolicyListsWithInfoTag_42')
def getPolicyListsWithInfoTag_42(**kwargs):
    return CatalystwanClient().getPolicyListsWithInfoTag_42(**kwargs)

@register('previewPolicyListById_42')
def previewPolicyListById_42(**kwargs):
    return CatalystwanClient().previewPolicyListById_42(**kwargs)

@register('getListsById_42')
def getListsById_42(**kwargs):
    return CatalystwanClient().getListsById_42(**kwargs)

@register('getPolicyLists_40')
def getPolicyLists_40(**kwargs):
    return CatalystwanClient().getPolicyLists_40(**kwargs)

@register('getPolicyListsWithInfoTag_43')
def getPolicyListsWithInfoTag_43(**kwargs):
    return CatalystwanClient().getPolicyListsWithInfoTag_43(**kwargs)

@register('previewPolicyListById_43')
def previewPolicyListById_43(**kwargs):
    return CatalystwanClient().previewPolicyListById_43(**kwargs)

@register('getListsById_43')
def getListsById_43(**kwargs):
    return CatalystwanClient().getListsById_43(**kwargs)

@register('generateSecurityTemplateList')
def generateSecurityTemplateList(**kwargs):
    return CatalystwanClient().generateSecurityTemplateList(**kwargs)

@register('getSecurityTemplate')
def getSecurityTemplate(**kwargs):
    return CatalystwanClient().getSecurityTemplate(**kwargs)

@register('getSecurityPolicyDeviceList_1')
def getSecurityPolicyDeviceList_1(**kwargs):
    return CatalystwanClient().getSecurityPolicyDeviceList_1(**kwargs)

@register('getDeviceListById')
def getDeviceListById(**kwargs):
    return CatalystwanClient().getDeviceListById(**kwargs)

@register('generateSecurityPolicySummary')
def generateSecurityPolicySummary(**kwargs):
    return CatalystwanClient().generateSecurityPolicySummary(**kwargs)

@register('getSecurityTemplatesForDevice')
def getSecurityTemplatesForDevice(**kwargs):
    return CatalystwanClient().getSecurityTemplatesForDevice(**kwargs)

@register('generatePolicyTemplateList')
def generatePolicyTemplateList(**kwargs):
    return CatalystwanClient().generatePolicyTemplateList(**kwargs)

@register('getVEdgeTemplate')
def getVEdgeTemplate(**kwargs):
    return CatalystwanClient().getVEdgeTemplate(**kwargs)

@register('getVEdgePolicyDeviceList')
def getVEdgePolicyDeviceList(**kwargs):
    return CatalystwanClient().getVEdgePolicyDeviceList(**kwargs)

@register('getDeviceListByPolicy')
def getDeviceListByPolicy(**kwargs):
    return CatalystwanClient().getDeviceListByPolicy(**kwargs)

@register('generateVoiceTemplateList')
def generateVoiceTemplateList(**kwargs):
    return CatalystwanClient().generateVoiceTemplateList(**kwargs)

@register('getTemplateById')
def getTemplateById(**kwargs):
    return CatalystwanClient().getTemplateById(**kwargs)

@register('getVoicePolicyDeviceList')
def getVoicePolicyDeviceList(**kwargs):
    return CatalystwanClient().getVoicePolicyDeviceList(**kwargs)

@register('getDeviceListByPolicyId')
def getDeviceListByPolicyId(**kwargs):
    return CatalystwanClient().getDeviceListByPolicyId(**kwargs)

@register('generateVoicePolicySummary')
def generateVoicePolicySummary(**kwargs):
    return CatalystwanClient().generateVoicePolicySummary(**kwargs)

@register('getVoiceTemplatesForDevice')
def getVoiceTemplatesForDevice(**kwargs):
    return CatalystwanClient().getVoiceTemplatesForDevice(**kwargs)

@register('generateVSmartPolicyTemplateList')
def generateVSmartPolicyTemplateList(**kwargs):
    return CatalystwanClient().generateVSmartPolicyTemplateList(**kwargs)

@register('checkVSmartConnectivityStatus')
def checkVSmartConnectivityStatus(**kwargs):
    return CatalystwanClient().checkVSmartConnectivityStatus(**kwargs)

@register('getTemplateByPolicyId')
def getTemplateByPolicyId(**kwargs):
    return CatalystwanClient().getTemplateByPolicyId(**kwargs)

@register('QosmosNbarMigrationWarning')
def QosmosNbarMigrationWarning(**kwargs):
    return CatalystwanClient().QosmosNbarMigrationWarning(**kwargs)

@register('getAllTenants')
def getAllTenants(**kwargs):
    return CatalystwanClient().getAllTenants(**kwargs)

@register('getTenantvSmartMapping')
def getTenantvSmartMapping(**kwargs):
    return CatalystwanClient().getTenantvSmartMapping(**kwargs)

@register('getTenantHostingCapacityOnvSmarts')
def getTenantHostingCapacityOnvSmarts(**kwargs):
    return CatalystwanClient().getTenantHostingCapacityOnvSmarts(**kwargs)

@register('getTenant')
def getTenant(**kwargs):
    return CatalystwanClient().getTenant(**kwargs)

@register('downloadExistingBackupFile')
def downloadExistingBackupFile(**kwargs):
    return CatalystwanClient().downloadExistingBackupFile(**kwargs)

@register('exportTenantBackup')
def exportTenantBackup(**kwargs):
    return CatalystwanClient().exportTenantBackup(**kwargs)

@register('listTenantBackup')
def listTenantBackup(**kwargs):
    return CatalystwanClient().listTenantBackup(**kwargs)

@register('downloadTenantData')
def downloadTenantData(**kwargs):
    return CatalystwanClient().downloadTenantData(**kwargs)

@register('getMigrationToken')
def getMigrationToken(**kwargs):
    return CatalystwanClient().getMigrationToken(**kwargs)

@register('reTriggerNetworkMigration')
def reTriggerNetworkMigration(**kwargs):
    return CatalystwanClient().reTriggerNetworkMigration(**kwargs)

@register('getAllTenantStatuses')
def getAllTenantStatuses(**kwargs):
    return CatalystwanClient().getAllTenantStatuses(**kwargs)

@register('createFullTopology')
def createFullTopology(**kwargs):
    return CatalystwanClient().createFullTopology(**kwargs)

@register('createDeviceTopology')
def createDeviceTopology(**kwargs):
    return CatalystwanClient().createDeviceTopology(**kwargs)

@register('getSiteTopology')
def getSiteTopology(**kwargs):
    return CatalystwanClient().getSiteTopology(**kwargs)

@register('getSiteTopologyMonitorData')
def getSiteTopologyMonitorData(**kwargs):
    return CatalystwanClient().getSiteTopologyMonitorData(**kwargs)

@register('createPhysicalTopology')
def createPhysicalTopology(**kwargs):
    return CatalystwanClient().createPhysicalTopology(**kwargs)

@register('getControlConnections')
def getControlConnections(**kwargs):
    return CatalystwanClient().getControlConnections(**kwargs)

@register('getDeviceConfiguration')
def getDeviceConfiguration(**kwargs):
    return CatalystwanClient().getDeviceConfiguration(**kwargs)

@register('getAllKeysFromUmbrella')
def getAllKeysFromUmbrella(**kwargs):
    return CatalystwanClient().getAllKeysFromUmbrella(**kwargs)

@register('getManagementKeysFromUmbrella')
def getManagementKeysFromUmbrella(**kwargs):
    return CatalystwanClient().getManagementKeysFromUmbrella(**kwargs)

@register('getNetworkKeysFromUmbrella')
def getNetworkKeysFromUmbrella(**kwargs):
    return CatalystwanClient().getNetworkKeysFromUmbrella(**kwargs)

@register('getReportingKeysFromUmbrella')
def getReportingKeysFromUmbrella(**kwargs):
    return CatalystwanClient().getReportingKeysFromUmbrella(**kwargs)

@register('sendMetaDataToUmbrella')
def sendMetaDataToUmbrella(**kwargs):
    return CatalystwanClient().sendMetaDataToUmbrella(**kwargs)

@register('getStatus')
def getStatus(**kwargs):
    return CatalystwanClient().getStatus(**kwargs)

@register('getUrlMonitor')
def getUrlMonitor(**kwargs):
    return CatalystwanClient().getUrlMonitor(**kwargs)

@register('returnMetric')
def returnMetric(**kwargs):
    return CatalystwanClient().returnMetric(**kwargs)

@register('returnMetricFiles')
def returnMetricFiles(**kwargs):
    return CatalystwanClient().returnMetricFiles(**kwargs)

@register('getMetricsList')
def getMetricsList(**kwargs):
    return CatalystwanClient().getMetricsList(**kwargs)

@register('getDBSizeOnFile')
def getDBSizeOnFile(**kwargs):
    return CatalystwanClient().getDBSizeOnFile(**kwargs)

@register('listLogFileDetails')
def listLogFileDetails(**kwargs):
    return CatalystwanClient().listLogFileDetails(**kwargs)

@register('listVManageServerLogLastNLines')
def listVManageServerLogLastNLines(**kwargs):
    return CatalystwanClient().listVManageServerLogLastNLines(**kwargs)

@register('listConfigurations')
def listConfigurations(**kwargs):
    return CatalystwanClient().listConfigurations(**kwargs)

@register('listLoggers')
def listLoggers(**kwargs):
    return CatalystwanClient().listLoggers(**kwargs)

@register('getStatsMigrationRangeConfig')
def getStatsMigrationRangeConfig(**kwargs):
    return CatalystwanClient().getStatsMigrationRangeConfig(**kwargs)

@register('getStatsMigrationSettings')
def getStatsMigrationSettings(**kwargs):
    return CatalystwanClient().getStatsMigrationSettings(**kwargs)

@register('getStatsMigrationStatsDbInfo')
def getStatsMigrationStatsDbInfo(**kwargs):
    return CatalystwanClient().getStatsMigrationStatsDbInfo(**kwargs)

@register('getStatsMigrationStatus')
def getStatsMigrationStatus(**kwargs):
    return CatalystwanClient().getStatsMigrationStatus(**kwargs)

@register('getCloudOnRampSaasStatus')
def getCloudOnRampSaasStatus(**kwargs):
    return CatalystwanClient().getCloudOnRampSaasStatus(**kwargs)

@register('getCloudTunnelList')
def getCloudTunnelList(**kwargs):
    return CatalystwanClient().getCloudTunnelList(**kwargs)

@register('getPolicyGroupsWithCorSaasApps')
def getPolicyGroupsWithCorSaasApps(**kwargs):
    return CatalystwanClient().getPolicyGroupsWithCorSaasApps(**kwargs)

@register('getCorSitesPerDevice')
def getCorSitesPerDevice(**kwargs):
    return CatalystwanClient().getCorSitesPerDevice(**kwargs)

@register('getInactiveCorSaasSites')
def getInactiveCorSaasSites(**kwargs):
    return CatalystwanClient().getInactiveCorSaasSites(**kwargs)

@register('getLegacyDeviceList')
def getLegacyDeviceList(**kwargs):
    return CatalystwanClient().getLegacyDeviceList(**kwargs)

@register('getCorSaasStatusPerDevice')
def getCorSaasStatusPerDevice(**kwargs):
    return CatalystwanClient().getCorSaasStatusPerDevice(**kwargs)

@register('getWebexSyncStatus')
def getWebexSyncStatus(**kwargs):
    return CatalystwanClient().getWebexSyncStatus(**kwargs)

@register('GetConfigGroupBySolution')
def GetConfigGroupBySolution(**kwargs):
    return CatalystwanClient().GetConfigGroupBySolution(**kwargs)

@register('GetConfigGroup')
def GetConfigGroup(**kwargs):
    return CatalystwanClient().GetConfigGroup(**kwargs)

@register('GetConfigGroupAssociation')
def GetConfigGroupAssociation(**kwargs):
    return CatalystwanClient().GetConfigGroupAssociation(**kwargs)

@register('getConfigGroupDeviceVariables')
def getConfigGroupDeviceVariables(**kwargs):
    return CatalystwanClient().getConfigGroupDeviceVariables(**kwargs)

@register('getConfigGroupDeviceVariablesSchema')
def getConfigGroupDeviceVariablesSchema(**kwargs):
    return CatalystwanClient().getConfigGroupDeviceVariablesSchema(**kwargs)

@register('getRuleAssociationByConfigGroupId')
def getRuleAssociationByConfigGroupId(**kwargs):
    return CatalystwanClient().getRuleAssociationByConfigGroupId(**kwargs)

@register('getRunningIosCliConfig')
def getRunningIosCliConfig(**kwargs):
    return CatalystwanClient().getRunningIosCliConfig(**kwargs)

@register('getUnsupportedCliConfig')
def getUnsupportedCliConfig(**kwargs):
    return CatalystwanClient().getUnsupportedCliConfig(**kwargs)

@register('GetMobilityCliFeatureProfile')
def GetMobilityCliFeatureProfile(**kwargs):
    return CatalystwanClient().GetMobilityCliFeatureProfile(**kwargs)

@register('GetMobilityCliFeatureProfileByCliId')
def GetMobilityCliFeatureProfileByCliId(**kwargs):
    return CatalystwanClient().GetMobilityCliFeatureProfileByCliId(**kwargs)

@register('GetAllConfigFeatureForMobility')
def GetAllConfigFeatureForMobility(**kwargs):
    return CatalystwanClient().GetAllConfigFeatureForMobility(**kwargs)

@register('GetConfigFeatureForMobilityByParcelId')
def GetConfigFeatureForMobilityByParcelId(**kwargs):
    return CatalystwanClient().GetConfigFeatureForMobilityByParcelId(**kwargs)

@register('GetMobilityGlobalFeatureProfile')
def GetMobilityGlobalFeatureProfile(**kwargs):
    return CatalystwanClient().GetMobilityGlobalFeatureProfile(**kwargs)

@register('GetMobilityGlobalBasicParcelSchemaBySchemaType')
def GetMobilityGlobalBasicParcelSchemaBySchemaType(**kwargs):
    return CatalystwanClient().GetMobilityGlobalBasicParcelSchemaBySchemaType(**kwargs)

@register('GetMobilityFeatureProfileByGlobalId')
def GetMobilityFeatureProfileByGlobalId(**kwargs):
    return CatalystwanClient().GetMobilityFeatureProfileByGlobalId(**kwargs)

@register('GetQosFeatureForGlobal')
def GetQosFeatureForGlobal(**kwargs):
    return CatalystwanClient().GetQosFeatureForGlobal(**kwargs)

@register('GetQosFeatureByParcelIdForGlobal')
def GetQosFeatureByParcelIdForGlobal(**kwargs):
    return CatalystwanClient().GetQosFeatureByParcelIdForGlobal(**kwargs)

@register('GetAaaServersProfileParcelForMobility')
def GetAaaServersProfileParcelForMobility(**kwargs):
    return CatalystwanClient().GetAaaServersProfileParcelForMobility(**kwargs)

@register('GetAaaServersProfileParcelByParcelIdForMobility')
def GetAaaServersProfileParcelByParcelIdForMobility(**kwargs):
    return CatalystwanClient().GetAaaServersProfileParcelByParcelIdForMobility(**kwargs)

@register('GetBasicProfileParcelForMobility')
def GetBasicProfileParcelForMobility(**kwargs):
    return CatalystwanClient().GetBasicProfileParcelForMobility(**kwargs)

@register('GetBasicProfileParcelByParcelIdForMobility')
def GetBasicProfileParcelByParcelIdForMobility(**kwargs):
    return CatalystwanClient().GetBasicProfileParcelByParcelIdForMobility(**kwargs)

@register('GetCellularProfileParcelListForMobility')
def GetCellularProfileParcelListForMobility(**kwargs):
    return CatalystwanClient().GetCellularProfileParcelListForMobility(**kwargs)

@register('GetCellularProfileParcelForMobility')
def GetCellularProfileParcelForMobility(**kwargs):
    return CatalystwanClient().GetCellularProfileParcelForMobility(**kwargs)

@register('GetEsimCellularProfileFeatureForMobility')
def GetEsimCellularProfileFeatureForMobility(**kwargs):
    return CatalystwanClient().GetEsimCellularProfileFeatureForMobility(**kwargs)

@register('GetEsimCellularProfileFeatureByEsimCellularIdForMobility')
def GetEsimCellularProfileFeatureByEsimCellularIdForMobility(**kwargs):
    return CatalystwanClient().GetEsimCellularProfileFeatureByEsimCellularIdForMobility(**kwargs)

@register('GetEthernetProfileParcels')
def GetEthernetProfileParcels(**kwargs):
    return CatalystwanClient().GetEthernetProfileParcels(**kwargs)

@register('GetEthernetProfileParcel')
def GetEthernetProfileParcel(**kwargs):
    return CatalystwanClient().GetEthernetProfileParcel(**kwargs)

@register('GetLoggingProfileFeatureForMobility')
def GetLoggingProfileFeatureForMobility(**kwargs):
    return CatalystwanClient().GetLoggingProfileFeatureForMobility(**kwargs)

@register('GetLoggingProfileFeatureByFeatureIdForMobility')
def GetLoggingProfileFeatureByFeatureIdForMobility(**kwargs):
    return CatalystwanClient().GetLoggingProfileFeatureByFeatureIdForMobility(**kwargs)

@register('GetNetworkProtocolProfileParcelListForMobility')
def GetNetworkProtocolProfileParcelListForMobility(**kwargs):
    return CatalystwanClient().GetNetworkProtocolProfileParcelListForMobility(**kwargs)

@register('GetNetworkProtocolProfileParcelForMobility')
def GetNetworkProtocolProfileParcelForMobility(**kwargs):
    return CatalystwanClient().GetNetworkProtocolProfileParcelForMobility(**kwargs)

@register('GetSecurityPolicyProfileParcelListForMobility')
def GetSecurityPolicyProfileParcelListForMobility(**kwargs):
    return CatalystwanClient().GetSecurityPolicyProfileParcelListForMobility(**kwargs)

@register('GetSecurityPolicyProfileParcelForMobility')
def GetSecurityPolicyProfileParcelForMobility(**kwargs):
    return CatalystwanClient().GetSecurityPolicyProfileParcelForMobility(**kwargs)

@register('GetVpnProfileParcelForMobility')
def GetVpnProfileParcelForMobility(**kwargs):
    return CatalystwanClient().GetVpnProfileParcelForMobility(**kwargs)

@register('GetVpnProfileParcelByParcelIdForMobility')
def GetVpnProfileParcelByParcelIdForMobility(**kwargs):
    return CatalystwanClient().GetVpnProfileParcelByParcelIdForMobility(**kwargs)

@register('GetWifiProfileParcelListForMobility')
def GetWifiProfileParcelListForMobility(**kwargs):
    return CatalystwanClient().GetWifiProfileParcelListForMobility(**kwargs)

@register('GetWifiProfileParcelForMobility')
def GetWifiProfileParcelForMobility(**kwargs):
    return CatalystwanClient().GetWifiProfileParcelForMobility(**kwargs)

@register('GetAllNfvirtualCLIFeatureProfiles')
def GetAllNfvirtualCLIFeatureProfiles(**kwargs):
    return CatalystwanClient().GetAllNfvirtualCLIFeatureProfiles(**kwargs)

@register('GetNfvirtualCLIFeatureProfileByid')
def GetNfvirtualCLIFeatureProfileByid(**kwargs):
    return CatalystwanClient().GetNfvirtualCLIFeatureProfileByid(**kwargs)

@register('getNfvirtualCLIParcel')
def getNfvirtualCLIParcel(**kwargs):
    return CatalystwanClient().getNfvirtualCLIParcel(**kwargs)

@register('GetAllNfvirtualNetworksFeatureProfiles')
def GetAllNfvirtualNetworksFeatureProfiles(**kwargs):
    return CatalystwanClient().GetAllNfvirtualNetworksFeatureProfiles(**kwargs)

@register('GetAllNfvirtualOvsNetworksFeatureProfileByProfileId')
def GetAllNfvirtualOvsNetworksFeatureProfileByProfileId(**kwargs):
    return CatalystwanClient().GetAllNfvirtualOvsNetworksFeatureProfileByProfileId(**kwargs)

@register('GetNfvirtualNetworksFeatureProfileByProfileId')
def GetNfvirtualNetworksFeatureProfileByProfileId(**kwargs):
    return CatalystwanClient().GetNfvirtualNetworksFeatureProfileByProfileId(**kwargs)

@register('GetNfvirtualLANParcel')
def GetNfvirtualLANParcel(**kwargs):
    return CatalystwanClient().GetNfvirtualLANParcel(**kwargs)

@register('GetNfvirtualOVSNetworkParcel')
def GetNfvirtualOVSNetworkParcel(**kwargs):
    return CatalystwanClient().GetNfvirtualOVSNetworkParcel(**kwargs)

@register('GetNfvirtualRoutesParcel')
def GetNfvirtualRoutesParcel(**kwargs):
    return CatalystwanClient().GetNfvirtualRoutesParcel(**kwargs)

@register('GetNfvirtualSwitchParcel')
def GetNfvirtualSwitchParcel(**kwargs):
    return CatalystwanClient().GetNfvirtualSwitchParcel(**kwargs)

@register('GetNfvirtualVNFAttributesParcel')
def GetNfvirtualVNFAttributesParcel(**kwargs):
    return CatalystwanClient().GetNfvirtualVNFAttributesParcel(**kwargs)

@register('GetNfvirtualVNFParcel')
def GetNfvirtualVNFParcel(**kwargs):
    return CatalystwanClient().GetNfvirtualVNFParcel(**kwargs)

@register('GetNfvirtualWANParcel')
def GetNfvirtualWANParcel(**kwargs):
    return CatalystwanClient().GetNfvirtualWANParcel(**kwargs)

@register('GetAllNfvirtualSystemFeatureProfiles')
def GetAllNfvirtualSystemFeatureProfiles(**kwargs):
    return CatalystwanClient().GetAllNfvirtualSystemFeatureProfiles(**kwargs)

@register('GetNfvirtualSystemFeatureProfileByProfileId')
def GetNfvirtualSystemFeatureProfileByProfileId(**kwargs):
    return CatalystwanClient().GetNfvirtualSystemFeatureProfileByProfileId(**kwargs)

@register('GetNfvirtualAAAParcel')
def GetNfvirtualAAAParcel(**kwargs):
    return CatalystwanClient().GetNfvirtualAAAParcel(**kwargs)

@register('GetNfvirtualBannerParcel')
def GetNfvirtualBannerParcel(**kwargs):
    return CatalystwanClient().GetNfvirtualBannerParcel(**kwargs)

@register('GetNfvirtualLoggingParcel')
def GetNfvirtualLoggingParcel(**kwargs):
    return CatalystwanClient().GetNfvirtualLoggingParcel(**kwargs)

@register('GetNfvirtualNTPParcel')
def GetNfvirtualNTPParcel(**kwargs):
    return CatalystwanClient().GetNfvirtualNTPParcel(**kwargs)

@register('GetNfvirtualSNMPParcel')
def GetNfvirtualSNMPParcel(**kwargs):
    return CatalystwanClient().GetNfvirtualSNMPParcel(**kwargs)

@register('GetNfvirtualSystemSettingsParcel')
def GetNfvirtualSystemSettingsParcel(**kwargs):
    return CatalystwanClient().GetNfvirtualSystemSettingsParcel(**kwargs)

@register('GetSdroutingFeatureProfiles')
def GetSdroutingFeatureProfiles(**kwargs):
    return CatalystwanClient().GetSdroutingFeatureProfiles(**kwargs)

@register('GetSdroutingCliFeatureProfiles')
def GetSdroutingCliFeatureProfiles(**kwargs):
    return CatalystwanClient().GetSdroutingCliFeatureProfiles(**kwargs)

@register('Get')
def Get(**kwargs):
    return CatalystwanClient().Get(**kwargs)

@register('GetSdroutingCliFeatureProfile')
def GetSdroutingCliFeatureProfile(**kwargs):
    return CatalystwanClient().GetSdroutingCliFeatureProfile(**kwargs)

@register('GetSdroutingCLIAddOnFeatures')
def GetSdroutingCLIAddOnFeatures(**kwargs):
    return CatalystwanClient().GetSdroutingCLIAddOnFeatures(**kwargs)

@register('GetSdroutingCLIAddOnFeature')
def GetSdroutingCLIAddOnFeature(**kwargs):
    return CatalystwanClient().GetSdroutingCLIAddOnFeature(**kwargs)

@register('GetSdroutingCliConfigGroupFeatures')
def GetSdroutingCliConfigGroupFeatures(**kwargs):
    return CatalystwanClient().GetSdroutingCliConfigGroupFeatures(**kwargs)

@register('GetSdroutingCliConfigGroupFeature')
def GetSdroutingCliConfigGroupFeature(**kwargs):
    return CatalystwanClient().GetSdroutingCliConfigGroupFeature(**kwargs)

@register('GetSdroutingIosCLassicCLIAddOnFeatures')
def GetSdroutingIosCLassicCLIAddOnFeatures(**kwargs):
    return CatalystwanClient().GetSdroutingIosCLassicCLIAddOnFeatures(**kwargs)

@register('GetSdroutingIosClassicCLIAddOnFeature')
def GetSdroutingIosClassicCLIAddOnFeature(**kwargs):
    return CatalystwanClient().GetSdroutingIosClassicCLIAddOnFeature(**kwargs)

@register('GetSdRoutingEmbeddedSecurityFeatureProfiles')
def GetSdRoutingEmbeddedSecurityFeatureProfiles(**kwargs):
    return CatalystwanClient().GetSdRoutingEmbeddedSecurityFeatureProfiles(**kwargs)

@register('GetSdRoutingEmbeddedSecurityFeatureProfileByProfileId')
def GetSdRoutingEmbeddedSecurityFeatureProfileByProfileId(**kwargs):
    return CatalystwanClient().GetSdRoutingEmbeddedSecurityFeatureProfileByProfileId(**kwargs)

@register('GetSecurityFeature')
def GetSecurityFeature(**kwargs):
    return CatalystwanClient().GetSecurityFeature(**kwargs)

@register('GetSecurityFeatureByFeatureId')
def GetSecurityFeatureByFeatureId(**kwargs):
    return CatalystwanClient().GetSecurityFeatureByFeatureId(**kwargs)

@register('GetNgfirewallFeature')
def GetNgfirewallFeature(**kwargs):
    return CatalystwanClient().GetNgfirewallFeature(**kwargs)

@register('GetNgfirewallFeatureByFeatureId')
def GetNgfirewallFeatureByFeatureId(**kwargs):
    return CatalystwanClient().GetNgfirewallFeatureByFeatureId(**kwargs)

@register('GetCybervisionProfileFeatureForOther')
def GetCybervisionProfileFeatureForOther(**kwargs):
    return CatalystwanClient().GetCybervisionProfileFeatureForOther(**kwargs)

@register('GetCybervisionProfileFeatureByFeatureIdForOther')
def GetCybervisionProfileFeatureByFeatureIdForOther(**kwargs):
    return CatalystwanClient().GetCybervisionProfileFeatureByFeatureIdForOther(**kwargs)

@register('GetSdroutingServiceFeatureProfiles')
def GetSdroutingServiceFeatureProfiles(**kwargs):
    return CatalystwanClient().GetSdroutingServiceFeatureProfiles(**kwargs)

@register('GetSdroutingServiceFeatureProfile')
def GetSdroutingServiceFeatureProfile(**kwargs):
    return CatalystwanClient().GetSdroutingServiceFeatureProfile(**kwargs)

@register('GetSdroutingDhcpServerProfileParcels')
def GetSdroutingDhcpServerProfileParcels(**kwargs):
    return CatalystwanClient().GetSdroutingDhcpServerProfileParcels(**kwargs)

@register('GetSdroutingDhcpServerProfileParcel')
def GetSdroutingDhcpServerProfileParcel(**kwargs):
    return CatalystwanClient().GetSdroutingDhcpServerProfileParcel(**kwargs)

@register('GetSdroutingServiceIpsecProfileFeatures')
def GetSdroutingServiceIpsecProfileFeatures(**kwargs):
    return CatalystwanClient().GetSdroutingServiceIpsecProfileFeatures(**kwargs)

@register('GetSdroutingServiceIpsecProfileFeature')
def GetSdroutingServiceIpsecProfileFeature(**kwargs):
    return CatalystwanClient().GetSdroutingServiceIpsecProfileFeature(**kwargs)

@register('GetSdroutingServiceIpv4AclFeatures')
def GetSdroutingServiceIpv4AclFeatures(**kwargs):
    return CatalystwanClient().GetSdroutingServiceIpv4AclFeatures(**kwargs)

@register('GetSdroutingServiceIpv4AclFeature')
def GetSdroutingServiceIpv4AclFeature(**kwargs):
    return CatalystwanClient().GetSdroutingServiceIpv4AclFeature(**kwargs)

@register('GetListOfProfileParcels')
def GetListOfProfileParcels(**kwargs):
    return CatalystwanClient().GetListOfProfileParcels(**kwargs)

@register('GetMultiCloudConnection')
def GetMultiCloudConnection(**kwargs):
    return CatalystwanClient().GetMultiCloudConnection(**kwargs)

@register('GetSdroutingServiceObjectTrackerFeatures')
def GetSdroutingServiceObjectTrackerFeatures(**kwargs):
    return CatalystwanClient().GetSdroutingServiceObjectTrackerFeatures(**kwargs)

@register('GetSdroutingServiceObjectTrackerFeature')
def GetSdroutingServiceObjectTrackerFeature(**kwargs):
    return CatalystwanClient().GetSdroutingServiceObjectTrackerFeature(**kwargs)

@register('GetSdroutingServiceObjectTrackerGroupFeatures')
def GetSdroutingServiceObjectTrackerGroupFeatures(**kwargs):
    return CatalystwanClient().GetSdroutingServiceObjectTrackerGroupFeatures(**kwargs)

@register('GetSdroutingServiceObjectTrackerGroupFeature')
def GetSdroutingServiceObjectTrackerGroupFeature(**kwargs):
    return CatalystwanClient().GetSdroutingServiceObjectTrackerGroupFeature(**kwargs)

@register('GetSdroutingServiceRoutePolicyFeatures')
def GetSdroutingServiceRoutePolicyFeatures(**kwargs):
    return CatalystwanClient().GetSdroutingServiceRoutePolicyFeatures(**kwargs)

@register('GetSdroutingServiceRoutePolicyFeature')
def GetSdroutingServiceRoutePolicyFeature(**kwargs):
    return CatalystwanClient().GetSdroutingServiceRoutePolicyFeature(**kwargs)

@register('GetSdroutingServiceVrfOspfFeatures')
def GetSdroutingServiceVrfOspfFeatures(**kwargs):
    return CatalystwanClient().GetSdroutingServiceVrfOspfFeatures(**kwargs)

@register('GetSdroutingServiceVrfOspfFeature')
def GetSdroutingServiceVrfOspfFeature(**kwargs):
    return CatalystwanClient().GetSdroutingServiceVrfOspfFeature(**kwargs)

@register('GetSdroutingServiceVrfOspfv3Ipv4Features')
def GetSdroutingServiceVrfOspfv3Ipv4Features(**kwargs):
    return CatalystwanClient().GetSdroutingServiceVrfOspfv3Ipv4Features(**kwargs)

@register('GetSdroutingServiceVrfOspfv3Ipv4Feature')
def GetSdroutingServiceVrfOspfv3Ipv4Feature(**kwargs):
    return CatalystwanClient().GetSdroutingServiceVrfOspfv3Ipv4Feature(**kwargs)

@register('GetSdroutingServiceVrfOspfv3Ipv6Features')
def GetSdroutingServiceVrfOspfv3Ipv6Features(**kwargs):
    return CatalystwanClient().GetSdroutingServiceVrfOspfv3Ipv6Features(**kwargs)

@register('GetSdroutingServiceVrfOspfv3Ipv6Feature')
def GetSdroutingServiceVrfOspfv3Ipv6Feature(**kwargs):
    return CatalystwanClient().GetSdroutingServiceVrfOspfv3Ipv6Feature(**kwargs)

@register('GetSdroutingServiceVRFFeatures')
def GetSdroutingServiceVRFFeatures(**kwargs):
    return CatalystwanClient().GetSdroutingServiceVRFFeatures(**kwargs)

@register('GetSdroutingServiceVrfBgpFeatures')
def GetSdroutingServiceVrfBgpFeatures(**kwargs):
    return CatalystwanClient().GetSdroutingServiceVrfBgpFeatures(**kwargs)

@register('GetSdroutingServiceVrfBgpFeature')
def GetSdroutingServiceVrfBgpFeature(**kwargs):
    return CatalystwanClient().GetSdroutingServiceVrfBgpFeature(**kwargs)

@register('GetSdroutingServiceVrfEigrpFeatures')
def GetSdroutingServiceVrfEigrpFeatures(**kwargs):
    return CatalystwanClient().GetSdroutingServiceVrfEigrpFeatures(**kwargs)

@register('GetSdroutingServiceVrfEigrpFeature')
def GetSdroutingServiceVrfEigrpFeature(**kwargs):
    return CatalystwanClient().GetSdroutingServiceVrfEigrpFeature(**kwargs)

@register('GetSdroutingServiceVRFFeature')
def GetSdroutingServiceVRFFeature(**kwargs):
    return CatalystwanClient().GetSdroutingServiceVRFFeature(**kwargs)

@register('GetSdroutingServiceVRFDmvpnTunnelFeatures')
def GetSdroutingServiceVRFDmvpnTunnelFeatures(**kwargs):
    return CatalystwanClient().GetSdroutingServiceVRFDmvpnTunnelFeatures(**kwargs)

@register('GetSdroutingServiceVRFDmvpnTunnelFeature')
def GetSdroutingServiceVRFDmvpnTunnelFeature(**kwargs):
    return CatalystwanClient().GetSdroutingServiceVRFDmvpnTunnelFeature(**kwargs)

@register('GetSdroutingServiceVrfInterfaceEthernetFeaturesForService')
def GetSdroutingServiceVrfInterfaceEthernetFeaturesForService(**kwargs):
    return CatalystwanClient().GetSdroutingServiceVrfInterfaceEthernetFeaturesForService(**kwargs)

@register('GetSdroutingServiceVrfInterfaceEthernetFeatureByFeatureIdForService')
def GetSdroutingServiceVrfInterfaceEthernetFeatureByFeatureIdForService(**kwargs):
    return CatalystwanClient().GetSdroutingServiceVrfInterfaceEthernetFeatureByFeatureIdForService(**kwargs)

@register('GetVrfInterfaceEthernetAssociatedDhcpServerParcelsForService')
def GetVrfInterfaceEthernetAssociatedDhcpServerParcelsForService(**kwargs):
    return CatalystwanClient().GetVrfInterfaceEthernetAssociatedDhcpServerParcelsForService(**kwargs)

@register('GetVrfInterfaceEthernetAssociatedDhcpServerParcelByFeatureIdForService')
def GetVrfInterfaceEthernetAssociatedDhcpServerParcelByFeatureIdForService(**kwargs):
    return CatalystwanClient().GetVrfInterfaceEthernetAssociatedDhcpServerParcelByFeatureIdForService(**kwargs)

@register('GetSdroutingServiceVrfInterfaceIpsecFeaturesForService')
def GetSdroutingServiceVrfInterfaceIpsecFeaturesForService(**kwargs):
    return CatalystwanClient().GetSdroutingServiceVrfInterfaceIpsecFeaturesForService(**kwargs)

@register('GetSdroutingServiceVrfInterfaceIpsecFeatureByFeatureIdForService')
def GetSdroutingServiceVrfInterfaceIpsecFeatureByFeatureIdForService(**kwargs):
    return CatalystwanClient().GetSdroutingServiceVrfInterfaceIpsecFeatureByFeatureIdForService(**kwargs)

@register('GetServiceVrfAssociatedRoutingBgpFeatures')
def GetServiceVrfAssociatedRoutingBgpFeatures(**kwargs):
    return CatalystwanClient().GetServiceVrfAssociatedRoutingBgpFeatures(**kwargs)

@register('GetServiceVrfAssociatedRoutingBgpParcelByParcelId')
def GetServiceVrfAssociatedRoutingBgpParcelByParcelId(**kwargs):
    return CatalystwanClient().GetServiceVrfAssociatedRoutingBgpParcelByParcelId(**kwargs)

@register('GetServiceVrfAssociatedRoutingEigrpFeatures')
def GetServiceVrfAssociatedRoutingEigrpFeatures(**kwargs):
    return CatalystwanClient().GetServiceVrfAssociatedRoutingEigrpFeatures(**kwargs)

@register('GetServiceVrfAssociatedRoutingEigrpFeatureByFeatureId')
def GetServiceVrfAssociatedRoutingEigrpFeatureByFeatureId(**kwargs):
    return CatalystwanClient().GetServiceVrfAssociatedRoutingEigrpFeatureByFeatureId(**kwargs)

@register('GetServiceVrfAssociatedRoutingOspfFeatures')
def GetServiceVrfAssociatedRoutingOspfFeatures(**kwargs):
    return CatalystwanClient().GetServiceVrfAssociatedRoutingOspfFeatures(**kwargs)

@register('GetServiceVrfAssociatedRoutingOspfFeatureById')
def GetServiceVrfAssociatedRoutingOspfFeatureById(**kwargs):
    return CatalystwanClient().GetServiceVrfAssociatedRoutingOspfFeatureById(**kwargs)

@register('GetServiceVrfAssociatedRoutingOspfv3Ipv4Features')
def GetServiceVrfAssociatedRoutingOspfv3Ipv4Features(**kwargs):
    return CatalystwanClient().GetServiceVrfAssociatedRoutingOspfv3Ipv4Features(**kwargs)

@register('GetServiceVrfAssociatedRoutingOspfv3Ipv4FeatureById')
def GetServiceVrfAssociatedRoutingOspfv3Ipv4FeatureById(**kwargs):
    return CatalystwanClient().GetServiceVrfAssociatedRoutingOspfv3Ipv4FeatureById(**kwargs)

@register('GetServiceVrfAssociatedRoutingOspfv3Ipv6Parcels')
def GetServiceVrfAssociatedRoutingOspfv3Ipv6Parcels(**kwargs):
    return CatalystwanClient().GetServiceVrfAssociatedRoutingOspfv3Ipv6Parcels(**kwargs)

@register('GetServiceVrfAssociatedRoutingOspfv3Ipv6FeatureById')
def GetServiceVrfAssociatedRoutingOspfv3Ipv6FeatureById(**kwargs):
    return CatalystwanClient().GetServiceVrfAssociatedRoutingOspfv3Ipv6FeatureById(**kwargs)

@register('GetSdRoutingSseFeatureProfiles')
def GetSdRoutingSseFeatureProfiles(**kwargs):
    return CatalystwanClient().GetSdRoutingSseFeatureProfiles(**kwargs)

@register('GetSdRoutingSseFeatureProfileByProfileId')
def GetSdRoutingSseFeatureProfileByProfileId(**kwargs):
    return CatalystwanClient().GetSdRoutingSseFeatureProfileByProfileId(**kwargs)

@register('GetCiscoSseFeatureForSse')
def GetCiscoSseFeatureForSse(**kwargs):
    return CatalystwanClient().GetCiscoSseFeatureForSse(**kwargs)

@register('GetCiscoSseFeatureByFeatureIdForSSE')
def GetCiscoSseFeatureByFeatureIdForSSE(**kwargs):
    return CatalystwanClient().GetCiscoSseFeatureByFeatureIdForSSE(**kwargs)

@register('GetSdroutingSystemFeatureProfiles')
def GetSdroutingSystemFeatureProfiles(**kwargs):
    return CatalystwanClient().GetSdroutingSystemFeatureProfiles(**kwargs)

@register('GetSdroutingSystemFeatureProfile')
def GetSdroutingSystemFeatureProfile(**kwargs):
    return CatalystwanClient().GetSdroutingSystemFeatureProfile(**kwargs)

@register('GetSdroutingAaaFeatures')
def GetSdroutingAaaFeatures(**kwargs):
    return CatalystwanClient().GetSdroutingAaaFeatures(**kwargs)

@register('GetSdroutingAaaFeature')
def GetSdroutingAaaFeature(**kwargs):
    return CatalystwanClient().GetSdroutingAaaFeature(**kwargs)

@register('GetSdroutingBannerFeatures')
def GetSdroutingBannerFeatures(**kwargs):
    return CatalystwanClient().GetSdroutingBannerFeatures(**kwargs)

@register('GetSdroutingBannerFeature')
def GetSdroutingBannerFeature(**kwargs):
    return CatalystwanClient().GetSdroutingBannerFeature(**kwargs)

@register('GetSdroutingCertificateFeatures')
def GetSdroutingCertificateFeatures(**kwargs):
    return CatalystwanClient().GetSdroutingCertificateFeatures(**kwargs)

@register('GetSdroutingCertificateFeature')
def GetSdroutingCertificateFeature(**kwargs):
    return CatalystwanClient().GetSdroutingCertificateFeature(**kwargs)

@register('GetSdroutingFlexiblePortSpeedFeatures')
def GetSdroutingFlexiblePortSpeedFeatures(**kwargs):
    return CatalystwanClient().GetSdroutingFlexiblePortSpeedFeatures(**kwargs)

@register('GetSdroutingFlexiblePortSpeedFeature')
def GetSdroutingFlexiblePortSpeedFeature(**kwargs):
    return CatalystwanClient().GetSdroutingFlexiblePortSpeedFeature(**kwargs)

@register('GetSdroutingGlobalSettingFeatures')
def GetSdroutingGlobalSettingFeatures(**kwargs):
    return CatalystwanClient().GetSdroutingGlobalSettingFeatures(**kwargs)

@register('GetSdroutingGlobalSettingFeature')
def GetSdroutingGlobalSettingFeature(**kwargs):
    return CatalystwanClient().GetSdroutingGlobalSettingFeature(**kwargs)

@register('GetSdroutingLoggingFeatures')
def GetSdroutingLoggingFeatures(**kwargs):
    return CatalystwanClient().GetSdroutingLoggingFeatures(**kwargs)

@register('GetSdroutingLoggingFeature')
def GetSdroutingLoggingFeature(**kwargs):
    return CatalystwanClient().GetSdroutingLoggingFeature(**kwargs)

@register('GetSdroutingNtpFeatures')
def GetSdroutingNtpFeatures(**kwargs):
    return CatalystwanClient().GetSdroutingNtpFeatures(**kwargs)

@register('GetSdroutingNtpFeature')
def GetSdroutingNtpFeature(**kwargs):
    return CatalystwanClient().GetSdroutingNtpFeature(**kwargs)

@register('GetSdroutingSnmpFeatures')
def GetSdroutingSnmpFeatures(**kwargs):
    return CatalystwanClient().GetSdroutingSnmpFeatures(**kwargs)

@register('GetSdroutingSnmpFeature')
def GetSdroutingSnmpFeature(**kwargs):
    return CatalystwanClient().GetSdroutingSnmpFeature(**kwargs)

@register('GetSdroutingTransportFeatureProfiles')
def GetSdroutingTransportFeatureProfiles(**kwargs):
    return CatalystwanClient().GetSdroutingTransportFeatureProfiles(**kwargs)

@register('GetSdroutingTransportFeatureProfile')
def GetSdroutingTransportFeatureProfile(**kwargs):
    return CatalystwanClient().GetSdroutingTransportFeatureProfile(**kwargs)

@register('GetCellularControllerProfileParcelForTransport_1')
def GetCellularControllerProfileParcelForTransport_1(**kwargs):
    return CatalystwanClient().GetCellularControllerProfileParcelForTransport_1(**kwargs)

@register('GetCellularControllerProfileParcelByParcelIdForTransport_1')
def GetCellularControllerProfileParcelByParcelIdForTransport_1(**kwargs):
    return CatalystwanClient().GetCellularControllerProfileParcelByParcelIdForTransport_1(**kwargs)

@register('GetCellularControllerAssociatedCellularProfileParcelsForTransport_1')
def GetCellularControllerAssociatedCellularProfileParcelsForTransport_1(**kwargs):
    return CatalystwanClient().GetCellularControllerAssociatedCellularProfileParcelsForTransport_1(**kwargs)

@register('GetCellularControllerAssociatedCellularProfileParcelByParcelIdForTransport_1')
def GetCellularControllerAssociatedCellularProfileParcelByParcelIdForTransport_1(**kwargs):
    return CatalystwanClient().GetCellularControllerAssociatedCellularProfileParcelByParcelIdForTransport_1(**kwargs)

@register('GetCellularControllerAssociatedGpsParcelsForTransport_1')
def GetCellularControllerAssociatedGpsParcelsForTransport_1(**kwargs):
    return CatalystwanClient().GetCellularControllerAssociatedGpsParcelsForTransport_1(**kwargs)

@register('GetCellularControllerAssociatedGpsParcelByParcelIdForTransport_1')
def GetCellularControllerAssociatedGpsParcelByParcelIdForTransport_1(**kwargs):
    return CatalystwanClient().GetCellularControllerAssociatedGpsParcelByParcelIdForTransport_1(**kwargs)

@register('GetCellularProfileParcelForTransport')
def GetCellularProfileParcelForTransport(**kwargs):
    return CatalystwanClient().GetCellularProfileParcelForTransport(**kwargs)

@register('GetCellularProfileParcelByParcelIdForTransport')
def GetCellularProfileParcelByParcelIdForTransport(**kwargs):
    return CatalystwanClient().GetCellularProfileParcelByParcelIdForTransport(**kwargs)

@register('GetSdroutingTransportGlobalVRFFeatures')
def GetSdroutingTransportGlobalVRFFeatures(**kwargs):
    return CatalystwanClient().GetSdroutingTransportGlobalVRFFeatures(**kwargs)

@register('GetSdroutingTransportGlobalVrfBgpFeatures')
def GetSdroutingTransportGlobalVrfBgpFeatures(**kwargs):
    return CatalystwanClient().GetSdroutingTransportGlobalVrfBgpFeatures(**kwargs)

@register('GetSdroutingTransportGlobalVrfBgpFeature')
def GetSdroutingTransportGlobalVrfBgpFeature(**kwargs):
    return CatalystwanClient().GetSdroutingTransportGlobalVrfBgpFeature(**kwargs)

@register('GetSdroutingTransportGlobalVRFFeature')
def GetSdroutingTransportGlobalVRFFeature(**kwargs):
    return CatalystwanClient().GetSdroutingTransportGlobalVRFFeature(**kwargs)

@register('GetGlobalVRFInterfaceCellularParcelsForTransport')
def GetGlobalVRFInterfaceCellularParcelsForTransport(**kwargs):
    return CatalystwanClient().GetGlobalVRFInterfaceCellularParcelsForTransport(**kwargs)

@register('GetGlobalVRFInterfaceCellularAssociatedTrackerParcelsForTransport_1')
def GetGlobalVRFInterfaceCellularAssociatedTrackerParcelsForTransport_1(**kwargs):
    return CatalystwanClient().GetGlobalVRFInterfaceCellularAssociatedTrackerParcelsForTransport_1(**kwargs)

@register('GetGlobalVRFInterfaceCellularAssociatedTrackerParcelByParcelIdForTransport_1')
def GetGlobalVRFInterfaceCellularAssociatedTrackerParcelByParcelIdForTransport_1(**kwargs):
    return CatalystwanClient().GetGlobalVRFInterfaceCellularAssociatedTrackerParcelByParcelIdForTransport_1(**kwargs)

@register('GetGlobalVRFInterfaceCellularAssociatedTrackerParcelsForTransport')
def GetGlobalVRFInterfaceCellularAssociatedTrackerParcelsForTransport(**kwargs):
    return CatalystwanClient().GetGlobalVRFInterfaceCellularAssociatedTrackerParcelsForTransport(**kwargs)

@register('GetGlobalVRFInterfaceCellularAssociatedTrackerParcelByParcelIdForTransport')
def GetGlobalVRFInterfaceCellularAssociatedTrackerParcelByParcelIdForTransport(**kwargs):
    return CatalystwanClient().GetGlobalVRFInterfaceCellularAssociatedTrackerParcelByParcelIdForTransport(**kwargs)

@register('GetGlobalVRFInterfaceCellularParcelByParcelIdForTransport')
def GetGlobalVRFInterfaceCellularParcelByParcelIdForTransport(**kwargs):
    return CatalystwanClient().GetGlobalVRFInterfaceCellularParcelByParcelIdForTransport(**kwargs)

@register('GetSdroutingTransportGlobalVrfInterfaceEthernetParcelsForTransport')
def GetSdroutingTransportGlobalVrfInterfaceEthernetParcelsForTransport(**kwargs):
    return CatalystwanClient().GetSdroutingTransportGlobalVrfInterfaceEthernetParcelsForTransport(**kwargs)

@register('GetSdroutingTransportGlobalVrfInterfaceEthernetParcelByParcelIdForTransport')
def GetSdroutingTransportGlobalVrfInterfaceEthernetParcelByParcelIdForTransport(**kwargs):
    return CatalystwanClient().GetSdroutingTransportGlobalVrfInterfaceEthernetParcelByParcelIdForTransport(**kwargs)

@register('GetSdroutingTransportGlobalVrfInterfaceIpsecFeaturesForTransport')
def GetSdroutingTransportGlobalVrfInterfaceIpsecFeaturesForTransport(**kwargs):
    return CatalystwanClient().GetSdroutingTransportGlobalVrfInterfaceIpsecFeaturesForTransport(**kwargs)

@register('GetSdroutingTransportGlobalVrfInterfaceIpsecFeatureByFeatureIdForTransport')
def GetSdroutingTransportGlobalVrfInterfaceIpsecFeatureByFeatureIdForTransport(**kwargs):
    return CatalystwanClient().GetSdroutingTransportGlobalVrfInterfaceIpsecFeatureByFeatureIdForTransport(**kwargs)

@register('GetTransportVrfAssociatedRoutingBgpFeatures')
def GetTransportVrfAssociatedRoutingBgpFeatures(**kwargs):
    return CatalystwanClient().GetTransportVrfAssociatedRoutingBgpFeatures(**kwargs)

@register('GetVrfAssociatedRoutingBgpFeatureById')
def GetVrfAssociatedRoutingBgpFeatureById(**kwargs):
    return CatalystwanClient().GetVrfAssociatedRoutingBgpFeatureById(**kwargs)

@register('GetTransportVrfAssociatedRoutingOspfFeatures')
def GetTransportVrfAssociatedRoutingOspfFeatures(**kwargs):
    return CatalystwanClient().GetTransportVrfAssociatedRoutingOspfFeatures(**kwargs)

@register('GetVrfAssociatedRoutingOspfParcelByFeatureId')
def GetVrfAssociatedRoutingOspfParcelByFeatureId(**kwargs):
    return CatalystwanClient().GetVrfAssociatedRoutingOspfParcelByFeatureId(**kwargs)

@register('GetTransportVrfAssociatedRoutingOspfv3Ipv4Features')
def GetTransportVrfAssociatedRoutingOspfv3Ipv4Features(**kwargs):
    return CatalystwanClient().GetTransportVrfAssociatedRoutingOspfv3Ipv4Features(**kwargs)

@register('GetVrfAssociatedRoutingOspfv3Ipv4FeatureById')
def GetVrfAssociatedRoutingOspfv3Ipv4FeatureById(**kwargs):
    return CatalystwanClient().GetVrfAssociatedRoutingOspfv3Ipv4FeatureById(**kwargs)

@register('GetTransportVrfAssociatedRoutingOspfv3Ipv6Features')
def GetTransportVrfAssociatedRoutingOspfv3Ipv6Features(**kwargs):
    return CatalystwanClient().GetTransportVrfAssociatedRoutingOspfv3Ipv6Features(**kwargs)

@register('GetVrfAssociatedRoutingOspfv3Ipv6FeatureById')
def GetVrfAssociatedRoutingOspfv3Ipv6FeatureById(**kwargs):
    return CatalystwanClient().GetVrfAssociatedRoutingOspfv3Ipv6FeatureById(**kwargs)

@register('GetGPSProfileParcelForTransport')
def GetGPSProfileParcelForTransport(**kwargs):
    return CatalystwanClient().GetGPSProfileParcelForTransport(**kwargs)

@register('GetGPSProfileParcelByParcelIdForTransport')
def GetGPSProfileParcelByParcelIdForTransport(**kwargs):
    return CatalystwanClient().GetGPSProfileParcelByParcelIdForTransport(**kwargs)

@register('GetSdroutingTransportIpv4AclFeatures')
def GetSdroutingTransportIpv4AclFeatures(**kwargs):
    return CatalystwanClient().GetSdroutingTransportIpv4AclFeatures(**kwargs)

@register('GetSdroutingTransportIpv4AclFeature')
def GetSdroutingTransportIpv4AclFeature(**kwargs):
    return CatalystwanClient().GetSdroutingTransportIpv4AclFeature(**kwargs)

@register('GetSdroutingManagementVRFFeatures')
def GetSdroutingManagementVRFFeatures(**kwargs):
    return CatalystwanClient().GetSdroutingManagementVRFFeatures(**kwargs)

@register('GetSdroutingManagementVRFFeature')
def GetSdroutingManagementVRFFeature(**kwargs):
    return CatalystwanClient().GetSdroutingManagementVRFFeature(**kwargs)

@register('GetSdroutingManagementVrfInterfaceEthernetParcelsForTransportProfile')
def GetSdroutingManagementVrfInterfaceEthernetParcelsForTransportProfile(**kwargs):
    return CatalystwanClient().GetSdroutingManagementVrfInterfaceEthernetParcelsForTransportProfile(**kwargs)

@register('GetSdroutingManagementVrfInterfaceEthernetParcelByParcelIdForTransportProfile')
def GetSdroutingManagementVrfInterfaceEthernetParcelByParcelIdForTransportProfile(**kwargs):
    return CatalystwanClient().GetSdroutingManagementVrfInterfaceEthernetParcelByParcelIdForTransportProfile(**kwargs)

@register('GetLanVpnProfileParcelForService_1')
def GetLanVpnProfileParcelForService_1(**kwargs):
    return CatalystwanClient().GetLanVpnProfileParcelForService_1(**kwargs)

@register('GetLanVpnProfileParcelByParcelIdForService_1')
def GetLanVpnProfileParcelByParcelIdForService_1(**kwargs):
    return CatalystwanClient().GetLanVpnProfileParcelByParcelIdForService_1(**kwargs)

@register('GetSdroutingTransportObjectTrackerFeatures')
def GetSdroutingTransportObjectTrackerFeatures(**kwargs):
    return CatalystwanClient().GetSdroutingTransportObjectTrackerFeatures(**kwargs)

@register('GetSdroutingTransportObjectTrackerFeature')
def GetSdroutingTransportObjectTrackerFeature(**kwargs):
    return CatalystwanClient().GetSdroutingTransportObjectTrackerFeature(**kwargs)

@register('GetSdroutingTransportObjectTrackerGroupFeatures')
def GetSdroutingTransportObjectTrackerGroupFeatures(**kwargs):
    return CatalystwanClient().GetSdroutingTransportObjectTrackerGroupFeatures(**kwargs)

@register('GetSdroutingTransportObjectTrackerGroupFeature')
def GetSdroutingTransportObjectTrackerGroupFeature(**kwargs):
    return CatalystwanClient().GetSdroutingTransportObjectTrackerGroupFeature(**kwargs)

@register('GetSdroutingTransportRoutePolicyFeatures')
def GetSdroutingTransportRoutePolicyFeatures(**kwargs):
    return CatalystwanClient().GetSdroutingTransportRoutePolicyFeatures(**kwargs)

@register('GetSdroutingTransportRoutePolicyFeature')
def GetSdroutingTransportRoutePolicyFeature(**kwargs):
    return CatalystwanClient().GetSdroutingTransportRoutePolicyFeature(**kwargs)

@register('GetSdroutingTransportRoutingOspfFeatures')
def GetSdroutingTransportRoutingOspfFeatures(**kwargs):
    return CatalystwanClient().GetSdroutingTransportRoutingOspfFeatures(**kwargs)

@register('GetSdroutingTransportRoutingOspfFeature')
def GetSdroutingTransportRoutingOspfFeature(**kwargs):
    return CatalystwanClient().GetSdroutingTransportRoutingOspfFeature(**kwargs)

@register('GetSdroutingTransportRoutingOspfv3Ipv4Features')
def GetSdroutingTransportRoutingOspfv3Ipv4Features(**kwargs):
    return CatalystwanClient().GetSdroutingTransportRoutingOspfv3Ipv4Features(**kwargs)

@register('GetSdroutingTransportRoutingOspfv3Ipv4Feature')
def GetSdroutingTransportRoutingOspfv3Ipv4Feature(**kwargs):
    return CatalystwanClient().GetSdroutingTransportRoutingOspfv3Ipv4Feature(**kwargs)

@register('GetSdroutingTransportRoutingOspfv3Ipv6Features')
def GetSdroutingTransportRoutingOspfv3Ipv6Features(**kwargs):
    return CatalystwanClient().GetSdroutingTransportRoutingOspfv3Ipv6Features(**kwargs)

@register('GetSdroutingTransportRoutingOspfv3Ipv6Feature')
def GetSdroutingTransportRoutingOspfv3Ipv6Feature(**kwargs):
    return CatalystwanClient().GetSdroutingTransportRoutingOspfv3Ipv6Feature(**kwargs)

@register('GetTrackerProfileParcelForTransport_1')
def GetTrackerProfileParcelForTransport_1(**kwargs):
    return CatalystwanClient().GetTrackerProfileParcelForTransport_1(**kwargs)

@register('GetTrackerProfileParcelByParcelIdForTransport_1')
def GetTrackerProfileParcelByParcelIdForTransport_1(**kwargs):
    return CatalystwanClient().GetTrackerProfileParcelByParcelIdForTransport_1(**kwargs)

@register('GetTrackerGroupProfileParcelForTransport_1')
def GetTrackerGroupProfileParcelForTransport_1(**kwargs):
    return CatalystwanClient().GetTrackerGroupProfileParcelForTransport_1(**kwargs)

@register('GetTrackerGroupProfileParcelByParcelIdForTransport_1')
def GetTrackerGroupProfileParcelByParcelIdForTransport_1(**kwargs):
    return CatalystwanClient().GetTrackerGroupProfileParcelByParcelIdForTransport_1(**kwargs)

@register('GetSdroutingTransportVRFFeatures')
def GetSdroutingTransportVRFFeatures(**kwargs):
    return CatalystwanClient().GetSdroutingTransportVRFFeatures(**kwargs)

@register('GetSdroutingTransportVrfBgpFeatures')
def GetSdroutingTransportVrfBgpFeatures(**kwargs):
    return CatalystwanClient().GetSdroutingTransportVrfBgpFeatures(**kwargs)

@register('GetSdroutingTransportVrfBgpFeature')
def GetSdroutingTransportVrfBgpFeature(**kwargs):
    return CatalystwanClient().GetSdroutingTransportVrfBgpFeature(**kwargs)

@register('GetSdroutingTransportVRFFeature')
def GetSdroutingTransportVRFFeature(**kwargs):
    return CatalystwanClient().GetSdroutingTransportVRFFeature(**kwargs)

@register('GetSdroutingTransportVrfInterfaceEthernetParcelsForTransport')
def GetSdroutingTransportVrfInterfaceEthernetParcelsForTransport(**kwargs):
    return CatalystwanClient().GetSdroutingTransportVrfInterfaceEthernetParcelsForTransport(**kwargs)

@register('GetSdroutingTransportVrfInterfaceEthernetParcelByParcelIdForTransport')
def GetSdroutingTransportVrfInterfaceEthernetParcelByParcelIdForTransport(**kwargs):
    return CatalystwanClient().GetSdroutingTransportVrfInterfaceEthernetParcelByParcelIdForTransport(**kwargs)

@register('GetSdroutingTransportVrfInterfaceIpsecFeaturesForTransport')
def GetSdroutingTransportVrfInterfaceIpsecFeaturesForTransport(**kwargs):
    return CatalystwanClient().GetSdroutingTransportVrfInterfaceIpsecFeaturesForTransport(**kwargs)

@register('GetSdroutingTransportVrfInterfaceIpsecFeatureByFeatureIdForTransport')
def GetSdroutingTransportVrfInterfaceIpsecFeatureByFeatureIdForTransport(**kwargs):
    return CatalystwanClient().GetSdroutingTransportVrfInterfaceIpsecFeatureByFeatureIdForTransport(**kwargs)

@register('GetTransportVrfAssociatedRoutingBgpFeatures_1')
def GetTransportVrfAssociatedRoutingBgpFeatures_1(**kwargs):
    return CatalystwanClient().GetTransportVrfAssociatedRoutingBgpFeatures_1(**kwargs)

@register('GetTransportVrfAssociatedRoutingBgpById')
def GetTransportVrfAssociatedRoutingBgpById(**kwargs):
    return CatalystwanClient().GetTransportVrfAssociatedRoutingBgpById(**kwargs)

@register('GetTransportVrfAssociatedRoutingOspfFeatures_1')
def GetTransportVrfAssociatedRoutingOspfFeatures_1(**kwargs):
    return CatalystwanClient().GetTransportVrfAssociatedRoutingOspfFeatures_1(**kwargs)

@register('GetVrfAssociatedRoutingOspfById')
def GetVrfAssociatedRoutingOspfById(**kwargs):
    return CatalystwanClient().GetVrfAssociatedRoutingOspfById(**kwargs)

@register('GetTransportVrfAssociatedRoutingOspfv3Ipv4Features_1')
def GetTransportVrfAssociatedRoutingOspfv3Ipv4Features_1(**kwargs):
    return CatalystwanClient().GetTransportVrfAssociatedRoutingOspfv3Ipv4Features_1(**kwargs)

@register('GetVrfAssociatedRoutingOspfv3Ipv4FeatureById_1')
def GetVrfAssociatedRoutingOspfv3Ipv4FeatureById_1(**kwargs):
    return CatalystwanClient().GetVrfAssociatedRoutingOspfv3Ipv4FeatureById_1(**kwargs)

@register('GetTransportVrfAssociatedRoutingOspfv3Ipv6Features_1')
def GetTransportVrfAssociatedRoutingOspfv3Ipv6Features_1(**kwargs):
    return CatalystwanClient().GetTransportVrfAssociatedRoutingOspfv3Ipv6Features_1(**kwargs)

@register('GetVrfAssociatedRoutingOspfv3Ipv6FeatureById_1')
def GetVrfAssociatedRoutingOspfv3Ipv6FeatureById_1(**kwargs):
    return CatalystwanClient().GetVrfAssociatedRoutingOspfv3Ipv6FeatureById_1(**kwargs)

@register('GetSdwanFeatureProfileBySdwanFamily')
def GetSdwanFeatureProfileBySdwanFamily(**kwargs):
    return CatalystwanClient().GetSdwanFeatureProfileBySdwanFamily(**kwargs)

@register('GetCloudProbeProfileParcelByParcelIdForapplication-priority')
def GetCloudProbeProfileParcelByParcelIdForapplication_priority(**kwargs):
    return CatalystwanClient().GetCloudProbeProfileParcelByParcelIdForapplication_priority(**kwargs)

@register('getPolicyApplicationProfileParcel')
def getPolicyApplicationProfileParcel(**kwargs):
    return CatalystwanClient().getPolicyApplicationProfileParcel(**kwargs)

@register('GetTrafficPolicyProfileParcelByParcelIdForapplication-priority')
def GetTrafficPolicyProfileParcelByParcelIdForapplication_priority(**kwargs):
    return CatalystwanClient().GetTrafficPolicyProfileParcelByParcelIdForapplication_priority(**kwargs)

@register('GetSdwanFeatureProfilesByFamilyAndType_1')
def GetSdwanFeatureProfilesByFamilyAndType_1(**kwargs):
    return CatalystwanClient().GetSdwanFeatureProfilesByFamilyAndType_1(**kwargs)

@register('GetSdwanCliConfigFeatureSchemaBySchemaType')
def GetSdwanCliConfigFeatureSchemaBySchemaType(**kwargs):
    return CatalystwanClient().GetSdwanCliConfigFeatureSchemaBySchemaType(**kwargs)

@register('GetSdwanFeatureProfilesByFamilyAndType')
def GetSdwanFeatureProfilesByFamilyAndType(**kwargs):
    return CatalystwanClient().GetSdwanFeatureProfilesByFamilyAndType(**kwargs)

@register('GetSdwanFeatureProfileByProfileId')
def GetSdwanFeatureProfileByProfileId(**kwargs):
    return CatalystwanClient().GetSdwanFeatureProfileByProfileId(**kwargs)

@register('GetConfigProfileParcelForCLI')
def GetConfigProfileParcelForCLI(**kwargs):
    return CatalystwanClient().GetConfigProfileParcelForCLI(**kwargs)

@register('GetConfigProfileParcelByParcelIdForCLI')
def GetConfigProfileParcelByParcelIdForCLI(**kwargs):
    return CatalystwanClient().GetConfigProfileParcelByParcelIdForCLI(**kwargs)

@register('GetSdwanDnsSecurityFeatureProfiles')
def GetSdwanDnsSecurityFeatureProfiles(**kwargs):
    return CatalystwanClient().GetSdwanDnsSecurityFeatureProfiles(**kwargs)

@register('GetSdwanDnsSecurityFeatureProfileByProfileId')
def GetSdwanDnsSecurityFeatureProfileByProfileId(**kwargs):
    return CatalystwanClient().GetSdwanDnsSecurityFeatureProfileByProfileId(**kwargs)

@register('GetSigSecurityProfileParcel')
def GetSigSecurityProfileParcel(**kwargs):
    return CatalystwanClient().GetSigSecurityProfileParcel(**kwargs)

@register('GetSigSecurityProfileParcelByParcelId')
def GetSigSecurityProfileParcelByParcelId(**kwargs):
    return CatalystwanClient().GetSigSecurityProfileParcelByParcelId(**kwargs)

@register('GetSdwanSecurityFeature_1')
def GetSdwanSecurityFeature_1(**kwargs):
    return CatalystwanClient().GetSdwanSecurityFeature_1(**kwargs)

@register('GetSdwanSecurityFeatureByFeatureId_1')
def GetSdwanSecurityFeatureByFeatureId_1(**kwargs):
    return CatalystwanClient().GetSdwanSecurityFeatureByFeatureId_1(**kwargs)

@register('GetSdwanNgfirewallFeature')
def GetSdwanNgfirewallFeature(**kwargs):
    return CatalystwanClient().GetSdwanNgfirewallFeature(**kwargs)

@register('GetSdwanNgfirewallFeatureByFeatureId')
def GetSdwanNgfirewallFeatureByFeatureId(**kwargs):
    return CatalystwanClient().GetSdwanNgfirewallFeatureByFeatureId(**kwargs)

@register('GetSdwanOtherFeatureProfiles')
def GetSdwanOtherFeatureProfiles(**kwargs):
    return CatalystwanClient().GetSdwanOtherFeatureProfiles(**kwargs)

@register('GetSdwanOtherThousandeyesParcelSchemaBySchemaType')
def GetSdwanOtherThousandeyesParcelSchemaBySchemaType(**kwargs):
    return CatalystwanClient().GetSdwanOtherThousandeyesParcelSchemaBySchemaType(**kwargs)

@register('GetSdwanOtherFeatureProfileByProfileId')
def GetSdwanOtherFeatureProfileByProfileId(**kwargs):
    return CatalystwanClient().GetSdwanOtherFeatureProfileByProfileId(**kwargs)

@register('GetThousandeyesProfileParcelForOther')
def GetThousandeyesProfileParcelForOther(**kwargs):
    return CatalystwanClient().GetThousandeyesProfileParcelForOther(**kwargs)

@register('GetThousandeyesProfileParcelByParcelIdForOther')
def GetThousandeyesProfileParcelByParcelIdForOther(**kwargs):
    return CatalystwanClient().GetThousandeyesProfileParcelByParcelIdForOther(**kwargs)

@register('GetUcseProfileFeatureForOther')
def GetUcseProfileFeatureForOther(**kwargs):
    return CatalystwanClient().GetUcseProfileFeatureForOther(**kwargs)

@register('GetUcseProfileFeatureByIdFFeatureForOther')
def GetUcseProfileFeatureByIdFFeatureForOther(**kwargs):
    return CatalystwanClient().GetUcseProfileFeatureByIdFFeatureForOther(**kwargs)

@register('GetSdwanSecurityFeature')
def GetSdwanSecurityFeature(**kwargs):
    return CatalystwanClient().GetSdwanSecurityFeature(**kwargs)

@register('GetSdwanSecurityFeatureByFeatureId')
def GetSdwanSecurityFeatureByFeatureId(**kwargs):
    return CatalystwanClient().GetSdwanSecurityFeatureByFeatureId(**kwargs)

@register('GetDataPrefixProfileParcelForPolicyObject')
def GetDataPrefixProfileParcelForPolicyObject(**kwargs):
    return CatalystwanClient().GetDataPrefixProfileParcelForPolicyObject(**kwargs)

@register('GetDataPrefixProfileParcelByParcelIdForPolicyObject')
def GetDataPrefixProfileParcelByParcelIdForPolicyObject(**kwargs):
    return CatalystwanClient().GetDataPrefixProfileParcelByParcelIdForPolicyObject(**kwargs)

@register('GetSdwanPolicyObjectDataPrefixParcelSchemaBySchemaType')
def GetSdwanPolicyObjectDataPrefixParcelSchemaBySchemaType(**kwargs):
    return CatalystwanClient().GetSdwanPolicyObjectDataPrefixParcelSchemaBySchemaType(**kwargs)

@register('GetSdwanServiceFeatureProfiles')
def GetSdwanServiceFeatureProfiles(**kwargs):
    return CatalystwanClient().GetSdwanServiceFeatureProfiles(**kwargs)

@register('GetSdwanServiceDhcpServerParcelSchemaBySchemaType')
def GetSdwanServiceDhcpServerParcelSchemaBySchemaType(**kwargs):
    return CatalystwanClient().GetSdwanServiceDhcpServerParcelSchemaBySchemaType(**kwargs)

@register('GetSdwanServiceLanVpnInterfaceEthernetParcelSchemaBySchema')
def GetSdwanServiceLanVpnInterfaceEthernetParcelSchemaBySchema(**kwargs):
    return CatalystwanClient().GetSdwanServiceLanVpnInterfaceEthernetParcelSchemaBySchema(**kwargs)

@register('GetCedgeServiceLanVpnInterfaceGreSchemaBySchema')
def GetCedgeServiceLanVpnInterfaceGreSchemaBySchema(**kwargs):
    return CatalystwanClient().GetCedgeServiceLanVpnInterfaceGreSchemaBySchema(**kwargs)

@register('getSdwanProfileParcelSchema')
def getSdwanProfileParcelSchema(**kwargs):
    return CatalystwanClient().getSdwanProfileParcelSchema(**kwargs)

@register('GetCedgeServiceLanVpnInterfaceSviParcelSchemaBySchema')
def GetCedgeServiceLanVpnInterfaceSviParcelSchemaBySchema(**kwargs):
    return CatalystwanClient().GetCedgeServiceLanVpnInterfaceSviParcelSchemaBySchema(**kwargs)

@register('GetSdwanServiceLanVpnParcelSchemaBySchemaType')
def GetSdwanServiceLanVpnParcelSchemaBySchemaType(**kwargs):
    return CatalystwanClient().GetSdwanServiceLanVpnParcelSchemaBySchemaType(**kwargs)

@register('GetSdwanServiceRoutingBgpParcelSchemaBySchemaType')
def GetSdwanServiceRoutingBgpParcelSchemaBySchemaType(**kwargs):
    return CatalystwanClient().GetSdwanServiceRoutingBgpParcelSchemaBySchemaType(**kwargs)

@register('GetSdwanServiceRoutingMulticastParcelSchemaBySchemaType')
def GetSdwanServiceRoutingMulticastParcelSchemaBySchemaType(**kwargs):
    return CatalystwanClient().GetSdwanServiceRoutingMulticastParcelSchemaBySchemaType(**kwargs)

@register('GetCedgeServiceSwitchportParcelSchemaBySchemaType')
def GetCedgeServiceSwitchportParcelSchemaBySchemaType(**kwargs):
    return CatalystwanClient().GetCedgeServiceSwitchportParcelSchemaBySchemaType(**kwargs)

@register('GetSdwanServiceTrackerParcelSchemaBySchemaType')
def GetSdwanServiceTrackerParcelSchemaBySchemaType(**kwargs):
    return CatalystwanClient().GetSdwanServiceTrackerParcelSchemaBySchemaType(**kwargs)

@register('GetCedgeServiceTrackerGroupParcelSchemaBySchemaType')
def GetCedgeServiceTrackerGroupParcelSchemaBySchemaType(**kwargs):
    return CatalystwanClient().GetCedgeServiceTrackerGroupParcelSchemaBySchemaType(**kwargs)

@register('GetSdwanServiceWirelesslanParcelSchemaBySchemaType')
def GetSdwanServiceWirelesslanParcelSchemaBySchemaType(**kwargs):
    return CatalystwanClient().GetSdwanServiceWirelesslanParcelSchemaBySchemaType(**kwargs)

@register('GetSdwanServiceFeatureProfileByProfileId')
def GetSdwanServiceFeatureProfileByProfileId(**kwargs):
    return CatalystwanClient().GetSdwanServiceFeatureProfileByProfileId(**kwargs)

@register('GetAppqoeProfileParcelForService')
def GetAppqoeProfileParcelForService(**kwargs):
    return CatalystwanClient().GetAppqoeProfileParcelForService(**kwargs)

@register('GetAppqoeProfileParcelByParcelIdForService')
def GetAppqoeProfileParcelByParcelIdForService(**kwargs):
    return CatalystwanClient().GetAppqoeProfileParcelByParcelIdForService(**kwargs)

@register('GetDhcpServerProfileParcelForService')
def GetDhcpServerProfileParcelForService(**kwargs):
    return CatalystwanClient().GetDhcpServerProfileParcelForService(**kwargs)

@register('GetDhcpServerProfileParcelByParcelIdForService')
def GetDhcpServerProfileParcelByParcelIdForService(**kwargs):
    return CatalystwanClient().GetDhcpServerProfileParcelByParcelIdForService(**kwargs)

@register('GetLanVpnProfileParcelForService')
def GetLanVpnProfileParcelForService(**kwargs):
    return CatalystwanClient().GetLanVpnProfileParcelForService(**kwargs)

@register('GetLanVpnProfileParcelByParcelIdForService')
def GetLanVpnProfileParcelByParcelIdForService(**kwargs):
    return CatalystwanClient().GetLanVpnProfileParcelByParcelIdForService(**kwargs)

@register('GetInterfaceEthernetParcelsForServiceLanVpn')
def GetInterfaceEthernetParcelsForServiceLanVpn(**kwargs):
    return CatalystwanClient().GetInterfaceEthernetParcelsForServiceLanVpn(**kwargs)

@register('GetLanVpnInterfaceEthernetParcelByParcelIdForService')
def GetLanVpnInterfaceEthernetParcelByParcelIdForService(**kwargs):
    return CatalystwanClient().GetLanVpnInterfaceEthernetParcelByParcelIdForService(**kwargs)

@register('GetLanVpnInterfaceEthernetAssociatedDhcpServerParcelsForTransport')
def GetLanVpnInterfaceEthernetAssociatedDhcpServerParcelsForTransport(**kwargs):
    return CatalystwanClient().GetLanVpnInterfaceEthernetAssociatedDhcpServerParcelsForTransport(**kwargs)

@register('GetLanVpnInterfaceEthernetAssociatedDhcpServerParcelByParcelIdForTransport')
def GetLanVpnInterfaceEthernetAssociatedDhcpServerParcelByParcelIdForTransport(**kwargs):
    return CatalystwanClient().GetLanVpnInterfaceEthernetAssociatedDhcpServerParcelByParcelIdForTransport(**kwargs)

@register('GetLanVpnInterfaceEthernetAssociatedTrackerParcelsForTransport')
def GetLanVpnInterfaceEthernetAssociatedTrackerParcelsForTransport(**kwargs):
    return CatalystwanClient().GetLanVpnInterfaceEthernetAssociatedTrackerParcelsForTransport(**kwargs)

@register('GetLanVpnInterfaceEthernetAssociatedTrackerParcelByParcelIdForTransport')
def GetLanVpnInterfaceEthernetAssociatedTrackerParcelByParcelIdForTransport(**kwargs):
    return CatalystwanClient().GetLanVpnInterfaceEthernetAssociatedTrackerParcelByParcelIdForTransport(**kwargs)

@register('GetLanVpnInterfaceEthernetAssociatedTrackerGroupParcelsForTransport')
def GetLanVpnInterfaceEthernetAssociatedTrackerGroupParcelsForTransport(**kwargs):
    return CatalystwanClient().GetLanVpnInterfaceEthernetAssociatedTrackerGroupParcelsForTransport(**kwargs)

@register('GetLanVpnInterfaceEthernetAssociatedTrackerGroupParcelByParcelIdForTransport')
def GetLanVpnInterfaceEthernetAssociatedTrackerGroupParcelByParcelIdForTransport(**kwargs):
    return CatalystwanClient().GetLanVpnInterfaceEthernetAssociatedTrackerGroupParcelByParcelIdForTransport(**kwargs)

@register('GetInterfaceGresForServiceLanVpn')
def GetInterfaceGresForServiceLanVpn(**kwargs):
    return CatalystwanClient().GetInterfaceGresForServiceLanVpn(**kwargs)

@register('GetLanVpnInterfaceGreByIdForService')
def GetLanVpnInterfaceGreByIdForService(**kwargs):
    return CatalystwanClient().GetLanVpnInterfaceGreByIdForService(**kwargs)

@register('getListOfProfileParcels')
def getListOfProfileParcels(**kwargs):
    return CatalystwanClient().getListOfProfileParcels(**kwargs)

@register('getProfileParcelByParcelId')
def getProfileParcelByParcelId(**kwargs):
    return CatalystwanClient().getProfileParcelByParcelId(**kwargs)

@register('GetLanVpnInterfaceIpsecAssociatedDhcpServerParcelsForTransport')
def GetLanVpnInterfaceIpsecAssociatedDhcpServerParcelsForTransport(**kwargs):
    return CatalystwanClient().GetLanVpnInterfaceIpsecAssociatedDhcpServerParcelsForTransport(**kwargs)

@register('GetLanVpnInterfaceIpsecAssociatedDhcpServerParcelByParcelIdForTransport')
def GetLanVpnInterfaceIpsecAssociatedDhcpServerParcelByParcelIdForTransport(**kwargs):
    return CatalystwanClient().GetLanVpnInterfaceIpsecAssociatedDhcpServerParcelByParcelIdForTransport(**kwargs)

@register('GetInterfaceSviParcelsForServiceLanVpn')
def GetInterfaceSviParcelsForServiceLanVpn(**kwargs):
    return CatalystwanClient().GetInterfaceSviParcelsForServiceLanVpn(**kwargs)

@register('GetLanVpnInterfaceSviParcelByParcelIdForService')
def GetLanVpnInterfaceSviParcelByParcelIdForService(**kwargs):
    return CatalystwanClient().GetLanVpnInterfaceSviParcelByParcelIdForService(**kwargs)

@register('GetLanVpnInterfaceSviAssociatedDhcpServerParcelsForTransport')
def GetLanVpnInterfaceSviAssociatedDhcpServerParcelsForTransport(**kwargs):
    return CatalystwanClient().GetLanVpnInterfaceSviAssociatedDhcpServerParcelsForTransport(**kwargs)

@register('GetLanVpnInterfaceSviAssociatedDhcpServerParcelByParcelIdForTransport')
def GetLanVpnInterfaceSviAssociatedDhcpServerParcelByParcelIdForTransport(**kwargs):
    return CatalystwanClient().GetLanVpnInterfaceSviAssociatedDhcpServerParcelByParcelIdForTransport(**kwargs)

@register('GetLanVpnAssociatedRoutingBgpParcelsForService')
def GetLanVpnAssociatedRoutingBgpParcelsForService(**kwargs):
    return CatalystwanClient().GetLanVpnAssociatedRoutingBgpParcelsForService(**kwargs)

@register('GetLanVpnAssociatedRoutingBgpParcelByParcelIdForService')
def GetLanVpnAssociatedRoutingBgpParcelByParcelIdForService(**kwargs):
    return CatalystwanClient().GetLanVpnAssociatedRoutingBgpParcelByParcelIdForService(**kwargs)

@register('GetLanVpnAssociatedRoutingEigrpParcelsForService')
def GetLanVpnAssociatedRoutingEigrpParcelsForService(**kwargs):
    return CatalystwanClient().GetLanVpnAssociatedRoutingEigrpParcelsForService(**kwargs)

@register('GetLanVpnAssociatedRoutingEigrpParcelByParcelIdForService')
def GetLanVpnAssociatedRoutingEigrpParcelByParcelIdForService(**kwargs):
    return CatalystwanClient().GetLanVpnAssociatedRoutingEigrpParcelByParcelIdForService(**kwargs)

@register('GetLanVpnAssociatedRoutingMulticastParcelsForService')
def GetLanVpnAssociatedRoutingMulticastParcelsForService(**kwargs):
    return CatalystwanClient().GetLanVpnAssociatedRoutingMulticastParcelsForService(**kwargs)

@register('GetLanVpnAssociatedRoutingMulticastParcelByParcelIdForService')
def GetLanVpnAssociatedRoutingMulticastParcelByParcelIdForService(**kwargs):
    return CatalystwanClient().GetLanVpnAssociatedRoutingMulticastParcelByParcelIdForService(**kwargs)

@register('GetLanVpnAssociatedRoutingOspfParcelsForService')
def GetLanVpnAssociatedRoutingOspfParcelsForService(**kwargs):
    return CatalystwanClient().GetLanVpnAssociatedRoutingOspfParcelsForService(**kwargs)

@register('GetLanVpnAssociatedRoutingOspfParcelByParcelIdForService')
def GetLanVpnAssociatedRoutingOspfParcelByParcelIdForService(**kwargs):
    return CatalystwanClient().GetLanVpnAssociatedRoutingOspfParcelByParcelIdForService(**kwargs)

@register('GetLanVpnAssociatedRoutingOspfv3IPv4ParcelsForService')
def GetLanVpnAssociatedRoutingOspfv3IPv4ParcelsForService(**kwargs):
    return CatalystwanClient().GetLanVpnAssociatedRoutingOspfv3IPv4ParcelsForService(**kwargs)

@register('GetLanVpnAssociatedRoutingOspfv3IPv4ParcelByParcelIdForService')
def GetLanVpnAssociatedRoutingOspfv3IPv4ParcelByParcelIdForService(**kwargs):
    return CatalystwanClient().GetLanVpnAssociatedRoutingOspfv3IPv4ParcelByParcelIdForService(**kwargs)

@register('GetLanVpnAssociatedRoutingOspfv3IPv6ParcelsForService')
def GetLanVpnAssociatedRoutingOspfv3IPv6ParcelsForService(**kwargs):
    return CatalystwanClient().GetLanVpnAssociatedRoutingOspfv3IPv6ParcelsForService(**kwargs)

@register('GetLanVpnAssociatedRoutingOspfv3IPv6ParcelByParcelIdForService')
def GetLanVpnAssociatedRoutingOspfv3IPv6ParcelByParcelIdForService(**kwargs):
    return CatalystwanClient().GetLanVpnAssociatedRoutingOspfv3IPv6ParcelByParcelIdForService(**kwargs)

@register('GetRoutingBgpProfileParcelForService')
def GetRoutingBgpProfileParcelForService(**kwargs):
    return CatalystwanClient().GetRoutingBgpProfileParcelForService(**kwargs)

@register('GetRoutingBgpProfileParcelByParcelIdForService')
def GetRoutingBgpProfileParcelByParcelIdForService(**kwargs):
    return CatalystwanClient().GetRoutingBgpProfileParcelByParcelIdForService(**kwargs)

@register('GetRoutingEigrpProfileParcelForService')
def GetRoutingEigrpProfileParcelForService(**kwargs):
    return CatalystwanClient().GetRoutingEigrpProfileParcelForService(**kwargs)

@register('GetRoutingEigrpProfileParcelByParcelIdForService')
def GetRoutingEigrpProfileParcelByParcelIdForService(**kwargs):
    return CatalystwanClient().GetRoutingEigrpProfileParcelByParcelIdForService(**kwargs)

@register('GetRoutingMulticastProfileParcelForService')
def GetRoutingMulticastProfileParcelForService(**kwargs):
    return CatalystwanClient().GetRoutingMulticastProfileParcelForService(**kwargs)

@register('GetRoutingMulticastProfileParcelByParcelIdForService')
def GetRoutingMulticastProfileParcelByParcelIdForService(**kwargs):
    return CatalystwanClient().GetRoutingMulticastProfileParcelByParcelIdForService(**kwargs)

@register('GetRoutingOspfProfileParcelForService')
def GetRoutingOspfProfileParcelForService(**kwargs):
    return CatalystwanClient().GetRoutingOspfProfileParcelForService(**kwargs)

@register('GetRoutingOspfProfileParcelByParcelIdForService')
def GetRoutingOspfProfileParcelByParcelIdForService(**kwargs):
    return CatalystwanClient().GetRoutingOspfProfileParcelByParcelIdForService(**kwargs)

@register('GetRoutingOspfv3Ipv4AfProfileParcelForService')
def GetRoutingOspfv3Ipv4AfProfileParcelForService(**kwargs):
    return CatalystwanClient().GetRoutingOspfv3Ipv4AfProfileParcelForService(**kwargs)

@register('GetRoutingOspfv3IPv4AfProfileParcelByParcelIdForService')
def GetRoutingOspfv3IPv4AfProfileParcelByParcelIdForService(**kwargs):
    return CatalystwanClient().GetRoutingOspfv3IPv4AfProfileParcelByParcelIdForService(**kwargs)

@register('GetRoutingOspfv3Ipv6AfProfileParcelForService')
def GetRoutingOspfv3Ipv6AfProfileParcelForService(**kwargs):
    return CatalystwanClient().GetRoutingOspfv3Ipv6AfProfileParcelForService(**kwargs)

@register('GetRoutingOspfv3IPv6AfProfileParcelByParcelIdForService')
def GetRoutingOspfv3IPv6AfProfileParcelByParcelIdForService(**kwargs):
    return CatalystwanClient().GetRoutingOspfv3IPv6AfProfileParcelByParcelIdForService(**kwargs)

@register('GetSwitchportParcelsForService')
def GetSwitchportParcelsForService(**kwargs):
    return CatalystwanClient().GetSwitchportParcelsForService(**kwargs)

@register('GetSwitchportParcelByParcelIdForService')
def GetSwitchportParcelByParcelIdForService(**kwargs):
    return CatalystwanClient().GetSwitchportParcelByParcelIdForService(**kwargs)

@register('GetTrackerProfileParcelForService')
def GetTrackerProfileParcelForService(**kwargs):
    return CatalystwanClient().GetTrackerProfileParcelForService(**kwargs)

@register('GetTrackerProfileParcelByParcelIdForService')
def GetTrackerProfileParcelByParcelIdForService(**kwargs):
    return CatalystwanClient().GetTrackerProfileParcelByParcelIdForService(**kwargs)

@register('GetTrackerGroupProfileParcelForService')
def GetTrackerGroupProfileParcelForService(**kwargs):
    return CatalystwanClient().GetTrackerGroupProfileParcelForService(**kwargs)

@register('GetTrackerGroupProfileParcelByParcelIdForService')
def GetTrackerGroupProfileParcelByParcelIdForService(**kwargs):
    return CatalystwanClient().GetTrackerGroupProfileParcelByParcelIdForService(**kwargs)

@register('GetWirelesslanProfileParcelForService')
def GetWirelesslanProfileParcelForService(**kwargs):
    return CatalystwanClient().GetWirelesslanProfileParcelForService(**kwargs)

@register('GetWirelesslanProfileParcelByParcelIdForService')
def GetWirelesslanProfileParcelByParcelIdForService(**kwargs):
    return CatalystwanClient().GetWirelesslanProfileParcelByParcelIdForService(**kwargs)

@register('GetSdwanSigSecurityFeatureProfiles')
def GetSdwanSigSecurityFeatureProfiles(**kwargs):
    return CatalystwanClient().GetSdwanSigSecurityFeatureProfiles(**kwargs)

@register('GetSdwanSigSecurityFeatureProfileByProfileId')
def GetSdwanSigSecurityFeatureProfileByProfileId(**kwargs):
    return CatalystwanClient().GetSdwanSigSecurityFeatureProfileByProfileId(**kwargs)

@register('GetSigSecurityProfileParcel_1')
def GetSigSecurityProfileParcel_1(**kwargs):
    return CatalystwanClient().GetSigSecurityProfileParcel_1(**kwargs)

@register('GetSigSecurityProfileParcelByParcelId_1')
def GetSigSecurityProfileParcelByParcelId_1(**kwargs):
    return CatalystwanClient().GetSigSecurityProfileParcelByParcelId_1(**kwargs)

@register('GetSdwanSystemFeatureProfiles')
def GetSdwanSystemFeatureProfiles(**kwargs):
    return CatalystwanClient().GetSdwanSystemFeatureProfiles(**kwargs)

@register('GetSdwanSystemAaaParcelSchemaBySchemaType')
def GetSdwanSystemAaaParcelSchemaBySchemaType(**kwargs):
    return CatalystwanClient().GetSdwanSystemAaaParcelSchemaBySchemaType(**kwargs)

@register('GetSdwanSystemBannerParcelSchemaBySchemaType')
def GetSdwanSystemBannerParcelSchemaBySchemaType(**kwargs):
    return CatalystwanClient().GetSdwanSystemBannerParcelSchemaBySchemaType(**kwargs)

@register('GetSdwanSystemBasicFeatureSchemaBySchemaType')
def GetSdwanSystemBasicFeatureSchemaBySchemaType(**kwargs):
    return CatalystwanClient().GetSdwanSystemBasicFeatureSchemaBySchemaType(**kwargs)

@register('GetSdwanSystemBfdParcelSchemaBySchemaType')
def GetSdwanSystemBfdParcelSchemaBySchemaType(**kwargs):
    return CatalystwanClient().GetSdwanSystemBfdParcelSchemaBySchemaType(**kwargs)

@register('GetCedgeSystemGlobalParcelSchemaBySchemaType')
def GetCedgeSystemGlobalParcelSchemaBySchemaType(**kwargs):
    return CatalystwanClient().GetCedgeSystemGlobalParcelSchemaBySchemaType(**kwargs)

@register('GetSdwanSystemLoggingParcelSchemaBySchemaType')
def GetSdwanSystemLoggingParcelSchemaBySchemaType(**kwargs):
    return CatalystwanClient().GetSdwanSystemLoggingParcelSchemaBySchemaType(**kwargs)

@register('GetCedgeSystemMrfParcelSchemaBySchemaType')
def GetCedgeSystemMrfParcelSchemaBySchemaType(**kwargs):
    return CatalystwanClient().GetCedgeSystemMrfParcelSchemaBySchemaType(**kwargs)

@register('GetSdwanSystemNtpParcelSchemaBySchemaType')
def GetSdwanSystemNtpParcelSchemaBySchemaType(**kwargs):
    return CatalystwanClient().GetSdwanSystemNtpParcelSchemaBySchemaType(**kwargs)

@register('GetSdwanSystemOmpParcelSchemaBySchemaType')
def GetSdwanSystemOmpParcelSchemaBySchemaType(**kwargs):
    return CatalystwanClient().GetSdwanSystemOmpParcelSchemaBySchemaType(**kwargs)

@register('GetSdwanSystemSnmpParcelSchemaBySchemaType')
def GetSdwanSystemSnmpParcelSchemaBySchemaType(**kwargs):
    return CatalystwanClient().GetSdwanSystemSnmpParcelSchemaBySchemaType(**kwargs)

@register('GetSdwanSystemFeatureProfileByProfileId')
def GetSdwanSystemFeatureProfileByProfileId(**kwargs):
    return CatalystwanClient().GetSdwanSystemFeatureProfileByProfileId(**kwargs)

@register('GetAaaProfileParcelForSystem')
def GetAaaProfileParcelForSystem(**kwargs):
    return CatalystwanClient().GetAaaProfileParcelForSystem(**kwargs)

@register('GetAaaProfileParcelByParcelIdForSystem')
def GetAaaProfileParcelByParcelIdForSystem(**kwargs):
    return CatalystwanClient().GetAaaProfileParcelByParcelIdForSystem(**kwargs)

@register('GetBannerProfileParcelForSystem')
def GetBannerProfileParcelForSystem(**kwargs):
    return CatalystwanClient().GetBannerProfileParcelForSystem(**kwargs)

@register('GetBannerProfileParcelByParcelIdForSystem')
def GetBannerProfileParcelByParcelIdForSystem(**kwargs):
    return CatalystwanClient().GetBannerProfileParcelByParcelIdForSystem(**kwargs)

@register('GetBasicProfileFeatureForSystem')
def GetBasicProfileFeatureForSystem(**kwargs):
    return CatalystwanClient().GetBasicProfileFeatureForSystem(**kwargs)

@register('GetBasicProfileFeatureByFeatureIdForSystem')
def GetBasicProfileFeatureByFeatureIdForSystem(**kwargs):
    return CatalystwanClient().GetBasicProfileFeatureByFeatureIdForSystem(**kwargs)

@register('GetBfdProfileParcelForSystem')
def GetBfdProfileParcelForSystem(**kwargs):
    return CatalystwanClient().GetBfdProfileParcelForSystem(**kwargs)

@register('GetBfdProfileParcelByParcelIdForSystem')
def GetBfdProfileParcelByParcelIdForSystem(**kwargs):
    return CatalystwanClient().GetBfdProfileParcelByParcelIdForSystem(**kwargs)

@register('GetGlobalProfileParcelForSystem')
def GetGlobalProfileParcelForSystem(**kwargs):
    return CatalystwanClient().GetGlobalProfileParcelForSystem(**kwargs)

@register('GetGlobalProfileParcelByParcelIdForSystem')
def GetGlobalProfileParcelByParcelIdForSystem(**kwargs):
    return CatalystwanClient().GetGlobalProfileParcelByParcelIdForSystem(**kwargs)

@register('GetLoggingProfileParcelForSystem')
def GetLoggingProfileParcelForSystem(**kwargs):
    return CatalystwanClient().GetLoggingProfileParcelForSystem(**kwargs)

@register('GetLoggingProfileParcelByParcelIdForSystem')
def GetLoggingProfileParcelByParcelIdForSystem(**kwargs):
    return CatalystwanClient().GetLoggingProfileParcelByParcelIdForSystem(**kwargs)

@register('GetMrfProfileParcelForSystem')
def GetMrfProfileParcelForSystem(**kwargs):
    return CatalystwanClient().GetMrfProfileParcelForSystem(**kwargs)

@register('GetMrfProfileParcelByParcelIdForSystem')
def GetMrfProfileParcelByParcelIdForSystem(**kwargs):
    return CatalystwanClient().GetMrfProfileParcelByParcelIdForSystem(**kwargs)

@register('GetNtpProfileParcelForSystem')
def GetNtpProfileParcelForSystem(**kwargs):
    return CatalystwanClient().GetNtpProfileParcelForSystem(**kwargs)

@register('GetNtpProfileParcelByParcelIdForSystem')
def GetNtpProfileParcelByParcelIdForSystem(**kwargs):
    return CatalystwanClient().GetNtpProfileParcelByParcelIdForSystem(**kwargs)

@register('GetOmpProfileParcelForSystem')
def GetOmpProfileParcelForSystem(**kwargs):
    return CatalystwanClient().GetOmpProfileParcelForSystem(**kwargs)

@register('GetOmpProfileParcelByParcelIdForSystem')
def GetOmpProfileParcelByParcelIdForSystem(**kwargs):
    return CatalystwanClient().GetOmpProfileParcelByParcelIdForSystem(**kwargs)

@register('GetSecurityForSystem')
def GetSecurityForSystem(**kwargs):
    return CatalystwanClient().GetSecurityForSystem(**kwargs)

@register('GetSecurityBySecurityIdForSystem')
def GetSecurityBySecurityIdForSystem(**kwargs):
    return CatalystwanClient().GetSecurityBySecurityIdForSystem(**kwargs)

@register('GetSnmpProfileParcelForSystem')
def GetSnmpProfileParcelForSystem(**kwargs):
    return CatalystwanClient().GetSnmpProfileParcelForSystem(**kwargs)

@register('GetSnmpProfileParcelByParcelIdForSystem')
def GetSnmpProfileParcelByParcelIdForSystem(**kwargs):
    return CatalystwanClient().GetSnmpProfileParcelByParcelIdForSystem(**kwargs)

@register('GetSdwanTransportFeatureProfiles')
def GetSdwanTransportFeatureProfiles(**kwargs):
    return CatalystwanClient().GetSdwanTransportFeatureProfiles(**kwargs)

@register('GetSdwanTransportCellularControllerParcelSchemaBySchemaType')
def GetSdwanTransportCellularControllerParcelSchemaBySchemaType(**kwargs):
    return CatalystwanClient().GetSdwanTransportCellularControllerParcelSchemaBySchemaType(**kwargs)

@register('GetSdwanTransportCellularProfileParcelSchemaBySchemaType')
def GetSdwanTransportCellularProfileParcelSchemaBySchemaType(**kwargs):
    return CatalystwanClient().GetSdwanTransportCellularProfileParcelSchemaBySchemaType(**kwargs)

@register('GetSdwanTransportIpv6TrackerParcelSchemaBySchemaType')
def GetSdwanTransportIpv6TrackerParcelSchemaBySchemaType(**kwargs):
    return CatalystwanClient().GetSdwanTransportIpv6TrackerParcelSchemaBySchemaType(**kwargs)

@register('GetCedgeTransportIpv6TrackerGroupParcelSchemaBySchemaType')
def GetCedgeTransportIpv6TrackerGroupParcelSchemaBySchemaType(**kwargs):
    return CatalystwanClient().GetCedgeTransportIpv6TrackerGroupParcelSchemaBySchemaType(**kwargs)

@register('GetSdwanTransportManagementVpnInterfaceEthernetParcelSchemaBySchema')
def GetSdwanTransportManagementVpnInterfaceEthernetParcelSchemaBySchema(**kwargs):
    return CatalystwanClient().GetSdwanTransportManagementVpnInterfaceEthernetParcelSchemaBySchema(**kwargs)

@register('GetSdwanTransportManagementVpnParcelSchemaBySchemaType')
def GetSdwanTransportManagementVpnParcelSchemaBySchemaType(**kwargs):
    return CatalystwanClient().GetSdwanTransportManagementVpnParcelSchemaBySchemaType(**kwargs)

@register('GetSdwanTransportRoutingBgpParcelSchemaBySchemaType')
def GetSdwanTransportRoutingBgpParcelSchemaBySchemaType(**kwargs):
    return CatalystwanClient().GetSdwanTransportRoutingBgpParcelSchemaBySchemaType(**kwargs)

@register('GetCedgeTransportT1e1controllerParcelSchemaBySchemaType')
def GetCedgeTransportT1e1controllerParcelSchemaBySchemaType(**kwargs):
    return CatalystwanClient().GetCedgeTransportT1e1controllerParcelSchemaBySchemaType(**kwargs)

@register('GetSdwanTransportTrackerParcelSchemaBySchemaType')
def GetSdwanTransportTrackerParcelSchemaBySchemaType(**kwargs):
    return CatalystwanClient().GetSdwanTransportTrackerParcelSchemaBySchemaType(**kwargs)

@register('GetCedgeTransportTrackerGroupParcelSchemaBySchemaType')
def GetCedgeTransportTrackerGroupParcelSchemaBySchemaType(**kwargs):
    return CatalystwanClient().GetCedgeTransportTrackerGroupParcelSchemaBySchemaType(**kwargs)

@register('GetSdwanTransportWanVpnCellularInterfaceParcelSchemaBySchema')
def GetSdwanTransportWanVpnCellularInterfaceParcelSchemaBySchema(**kwargs):
    return CatalystwanClient().GetSdwanTransportWanVpnCellularInterfaceParcelSchemaBySchema(**kwargs)

@register('GetSdwanTransportWanVpnInterfaceEthernetParcelSchemaBySchema')
def GetSdwanTransportWanVpnInterfaceEthernetParcelSchemaBySchema(**kwargs):
    return CatalystwanClient().GetSdwanTransportWanVpnInterfaceEthernetParcelSchemaBySchema(**kwargs)

@register('GetCedgeTransportWanVpnInterfaceGreParcelSchemaBySchema')
def GetCedgeTransportWanVpnInterfaceGreParcelSchemaBySchema(**kwargs):
    return CatalystwanClient().GetCedgeTransportWanVpnInterfaceGreParcelSchemaBySchema(**kwargs)

@register('getSdwanProfileParcelSchema_1')
def getSdwanProfileParcelSchema_1(**kwargs):
    return CatalystwanClient().getSdwanProfileParcelSchema_1(**kwargs)

@register('GetCedgeTransportWanVpnInterfaceSerialParcelSchemaBySchema')
def GetCedgeTransportWanVpnInterfaceSerialParcelSchemaBySchema(**kwargs):
    return CatalystwanClient().GetCedgeTransportWanVpnInterfaceSerialParcelSchemaBySchema(**kwargs)

@register('GetSdwanTransportWanVpnParcelSchemaBySchemaType')
def GetSdwanTransportWanVpnParcelSchemaBySchemaType(**kwargs):
    return CatalystwanClient().GetSdwanTransportWanVpnParcelSchemaBySchemaType(**kwargs)

@register('GetSdwanTransportFeatureProfileByProfileId')
def GetSdwanTransportFeatureProfileByProfileId(**kwargs):
    return CatalystwanClient().GetSdwanTransportFeatureProfileByProfileId(**kwargs)

@register('GetCellularControllerProfileParcelForTransport')
def GetCellularControllerProfileParcelForTransport(**kwargs):
    return CatalystwanClient().GetCellularControllerProfileParcelForTransport(**kwargs)

@register('GetCellularControllerProfileParcelByParcelIdForTransport')
def GetCellularControllerProfileParcelByParcelIdForTransport(**kwargs):
    return CatalystwanClient().GetCellularControllerProfileParcelByParcelIdForTransport(**kwargs)

@register('GetCellularControllerAssociatedCellularProfileParcelsForTransport')
def GetCellularControllerAssociatedCellularProfileParcelsForTransport(**kwargs):
    return CatalystwanClient().GetCellularControllerAssociatedCellularProfileParcelsForTransport(**kwargs)

@register('GetCellularControllerAssociatedCellularProfileParcelByParcelIdForTransport')
def GetCellularControllerAssociatedCellularProfileParcelByParcelIdForTransport(**kwargs):
    return CatalystwanClient().GetCellularControllerAssociatedCellularProfileParcelByParcelIdForTransport(**kwargs)

@register('GetCellularControllerAssociatedGpsParcelsForTransport')
def GetCellularControllerAssociatedGpsParcelsForTransport(**kwargs):
    return CatalystwanClient().GetCellularControllerAssociatedGpsParcelsForTransport(**kwargs)

@register('GetCellularControllerAssociatedGpsParcelByParcelIdForTransport')
def GetCellularControllerAssociatedGpsParcelByParcelIdForTransport(**kwargs):
    return CatalystwanClient().GetCellularControllerAssociatedGpsParcelByParcelIdForTransport(**kwargs)

@register('GetCellularProfileProfileParcelForTransport')
def GetCellularProfileProfileParcelForTransport(**kwargs):
    return CatalystwanClient().GetCellularProfileProfileParcelForTransport(**kwargs)

@register('GetCellularProfileProfileParcelByParcelIdForTransport')
def GetCellularProfileProfileParcelByParcelIdForTransport(**kwargs):
    return CatalystwanClient().GetCellularProfileProfileParcelByParcelIdForTransport(**kwargs)

@register('GetEsimCellularControllerProfileFeatureForTransport')
def GetEsimCellularControllerProfileFeatureForTransport(**kwargs):
    return CatalystwanClient().GetEsimCellularControllerProfileFeatureForTransport(**kwargs)

@register('GetEsimCellularControllerProfileFeatureByFeatureIdForTransport')
def GetEsimCellularControllerProfileFeatureByFeatureIdForTransport(**kwargs):
    return CatalystwanClient().GetEsimCellularControllerProfileFeatureByFeatureIdForTransport(**kwargs)

@register('GetEsimCellularProfileProfileFeatureForTransport')
def GetEsimCellularProfileProfileFeatureForTransport(**kwargs):
    return CatalystwanClient().GetEsimCellularProfileProfileFeatureForTransport(**kwargs)

@register('GetEsimCellularProfileByFeatureIdForTransport')
def GetEsimCellularProfileByFeatureIdForTransport(**kwargs):
    return CatalystwanClient().GetEsimCellularProfileByFeatureIdForTransport(**kwargs)

@register('GetGpsProfileParcelForTransport')
def GetGpsProfileParcelForTransport(**kwargs):
    return CatalystwanClient().GetGpsProfileParcelForTransport(**kwargs)

@register('GetGpsProfileParcelByParcelIdForTransport')
def GetGpsProfileParcelByParcelIdForTransport(**kwargs):
    return CatalystwanClient().GetGpsProfileParcelByParcelIdForTransport(**kwargs)

@register('GetIpv6TrackerProfileParcelForTransport')
def GetIpv6TrackerProfileParcelForTransport(**kwargs):
    return CatalystwanClient().GetIpv6TrackerProfileParcelForTransport(**kwargs)

@register('GetIpv6TrackerProfileParcelByParcelIdForTransport')
def GetIpv6TrackerProfileParcelByParcelIdForTransport(**kwargs):
    return CatalystwanClient().GetIpv6TrackerProfileParcelByParcelIdForTransport(**kwargs)

@register('GetIpv6TrackerGroupProfileParcelForTransport')
def GetIpv6TrackerGroupProfileParcelForTransport(**kwargs):
    return CatalystwanClient().GetIpv6TrackerGroupProfileParcelForTransport(**kwargs)

@register('GetIpv6TrackerGroupProfileParcelByParcelIdForTransport')
def GetIpv6TrackerGroupProfileParcelByParcelIdForTransport(**kwargs):
    return CatalystwanClient().GetIpv6TrackerGroupProfileParcelByParcelIdForTransport(**kwargs)

@register('GetManagementVpnProfileParcelForTransport')
def GetManagementVpnProfileParcelForTransport(**kwargs):
    return CatalystwanClient().GetManagementVpnProfileParcelForTransport(**kwargs)

@register('GetManagementVpnProfileParcelByParcelIdForTransport')
def GetManagementVpnProfileParcelByParcelIdForTransport(**kwargs):
    return CatalystwanClient().GetManagementVpnProfileParcelByParcelIdForTransport(**kwargs)

@register('GetInterfaceEthernetParcelsForTransportManagementVpn')
def GetInterfaceEthernetParcelsForTransportManagementVpn(**kwargs):
    return CatalystwanClient().GetInterfaceEthernetParcelsForTransportManagementVpn(**kwargs)

@register('GetManagementVpnInterfaceEthernetParcelByParcelIdForTransport')
def GetManagementVpnInterfaceEthernetParcelByParcelIdForTransport(**kwargs):
    return CatalystwanClient().GetManagementVpnInterfaceEthernetParcelByParcelIdForTransport(**kwargs)

@register('GetRoutingBgpProfileParcelForTransport')
def GetRoutingBgpProfileParcelForTransport(**kwargs):
    return CatalystwanClient().GetRoutingBgpProfileParcelForTransport(**kwargs)

@register('GetRoutingBgpProfileParcelByParcelIdForTransport')
def GetRoutingBgpProfileParcelByParcelIdForTransport(**kwargs):
    return CatalystwanClient().GetRoutingBgpProfileParcelByParcelIdForTransport(**kwargs)

@register('GetRoutingOspfProfileParcelForTransport')
def GetRoutingOspfProfileParcelForTransport(**kwargs):
    return CatalystwanClient().GetRoutingOspfProfileParcelForTransport(**kwargs)

@register('GetRoutingOspfProfileParcelByParcelIdForTransport')
def GetRoutingOspfProfileParcelByParcelIdForTransport(**kwargs):
    return CatalystwanClient().GetRoutingOspfProfileParcelByParcelIdForTransport(**kwargs)

@register('GetRoutingOspfv3Ipv4AfProfileParcelForTransport')
def GetRoutingOspfv3Ipv4AfProfileParcelForTransport(**kwargs):
    return CatalystwanClient().GetRoutingOspfv3Ipv4AfProfileParcelForTransport(**kwargs)

@register('GetRoutingOspfv3Ipv4AfProfileParcelByParcelIdForTransport')
def GetRoutingOspfv3Ipv4AfProfileParcelByParcelIdForTransport(**kwargs):
    return CatalystwanClient().GetRoutingOspfv3Ipv4AfProfileParcelByParcelIdForTransport(**kwargs)

@register('GetRoutingOspfv3Ipv6AfProfileParcelForTransport')
def GetRoutingOspfv3Ipv6AfProfileParcelForTransport(**kwargs):
    return CatalystwanClient().GetRoutingOspfv3Ipv6AfProfileParcelForTransport(**kwargs)

@register('GetRoutingOspfv3Ipv6AfProfileParcelByParcelIdForTransport')
def GetRoutingOspfv3Ipv6AfProfileParcelByParcelIdForTransport(**kwargs):
    return CatalystwanClient().GetRoutingOspfv3Ipv6AfProfileParcelByParcelIdForTransport(**kwargs)

@register('GetT1e1controllerProfileParcelForTransport')
def GetT1e1controllerProfileParcelForTransport(**kwargs):
    return CatalystwanClient().GetT1e1controllerProfileParcelForTransport(**kwargs)

@register('GetT1e1controllerProfileParcelByParcelIdForTransport')
def GetT1e1controllerProfileParcelByParcelIdForTransport(**kwargs):
    return CatalystwanClient().GetT1e1controllerProfileParcelByParcelIdForTransport(**kwargs)

@register('GetTrackerProfileParcelForTransport')
def GetTrackerProfileParcelForTransport(**kwargs):
    return CatalystwanClient().GetTrackerProfileParcelForTransport(**kwargs)

@register('GetTrackerProfileParcelByParcelIdForTransport')
def GetTrackerProfileParcelByParcelIdForTransport(**kwargs):
    return CatalystwanClient().GetTrackerProfileParcelByParcelIdForTransport(**kwargs)

@register('GetTrackerGroupProfileParcelForTransport')
def GetTrackerGroupProfileParcelForTransport(**kwargs):
    return CatalystwanClient().GetTrackerGroupProfileParcelForTransport(**kwargs)

@register('GetTrackerGroupProfileParcelByParcelIdForTransport')
def GetTrackerGroupProfileParcelByParcelIdForTransport(**kwargs):
    return CatalystwanClient().GetTrackerGroupProfileParcelByParcelIdForTransport(**kwargs)

@register('GetWanVpnProfileParcelForTransport')
def GetWanVpnProfileParcelForTransport(**kwargs):
    return CatalystwanClient().GetWanVpnProfileParcelForTransport(**kwargs)

@register('GetWanVpnProfileParcelByParcelIdForTransport')
def GetWanVpnProfileParcelByParcelIdForTransport(**kwargs):
    return CatalystwanClient().GetWanVpnProfileParcelByParcelIdForTransport(**kwargs)

@register('GetInterfaceCellularParcelsForTransportWanVpn')
def GetInterfaceCellularParcelsForTransportWanVpn(**kwargs):
    return CatalystwanClient().GetInterfaceCellularParcelsForTransportWanVpn(**kwargs)

@register('GetWanVpnInterfaceCellularAssociatedIpv6TrackerParcelsForTransport')
def GetWanVpnInterfaceCellularAssociatedIpv6TrackerParcelsForTransport(**kwargs):
    return CatalystwanClient().GetWanVpnInterfaceCellularAssociatedIpv6TrackerParcelsForTransport(**kwargs)

@register('GetWanVpnInterfaceCellularAssociatedIpv6TrackerParcelByParcelIdForTransport')
def GetWanVpnInterfaceCellularAssociatedIpv6TrackerParcelByParcelIdForTransport(**kwargs):
    return CatalystwanClient().GetWanVpnInterfaceCellularAssociatedIpv6TrackerParcelByParcelIdForTransport(**kwargs)

@register('GetWanVpnInterfaceCellularAssociatedIpv6TrackerGroupParcelsForTransport')
def GetWanVpnInterfaceCellularAssociatedIpv6TrackerGroupParcelsForTransport(**kwargs):
    return CatalystwanClient().GetWanVpnInterfaceCellularAssociatedIpv6TrackerGroupParcelsForTransport(**kwargs)

@register('GetWanVpnInterfaceCellularAssociatedIpv6TrackerGroupParcelByParcelIdForTransport')
def GetWanVpnInterfaceCellularAssociatedIpv6TrackerGroupParcelByParcelIdForTransport(**kwargs):
    return CatalystwanClient().GetWanVpnInterfaceCellularAssociatedIpv6TrackerGroupParcelByParcelIdForTransport(**kwargs)

@register('GetWanVpnInterfaceCellularAssociatedTrackerParcelsForTransport')
def GetWanVpnInterfaceCellularAssociatedTrackerParcelsForTransport(**kwargs):
    return CatalystwanClient().GetWanVpnInterfaceCellularAssociatedTrackerParcelsForTransport(**kwargs)

@register('GetWanVpnInterfaceCellularAssociatedTrackerParcelByParcelIdForTransport')
def GetWanVpnInterfaceCellularAssociatedTrackerParcelByParcelIdForTransport(**kwargs):
    return CatalystwanClient().GetWanVpnInterfaceCellularAssociatedTrackerParcelByParcelIdForTransport(**kwargs)

@register('GetWanVpnInterfaceCellularAssociatedTrackerGroupParcelsForTransport')
def GetWanVpnInterfaceCellularAssociatedTrackerGroupParcelsForTransport(**kwargs):
    return CatalystwanClient().GetWanVpnInterfaceCellularAssociatedTrackerGroupParcelsForTransport(**kwargs)

@register('GetWanVpnInterfaceCellularAssociatedTrackerGroupParcelByParcelIdForTransport')
def GetWanVpnInterfaceCellularAssociatedTrackerGroupParcelByParcelIdForTransport(**kwargs):
    return CatalystwanClient().GetWanVpnInterfaceCellularAssociatedTrackerGroupParcelByParcelIdForTransport(**kwargs)

@register('GetWanVpnInterfaceCellularParcelByParcelIdForTransport')
def GetWanVpnInterfaceCellularParcelByParcelIdForTransport(**kwargs):
    return CatalystwanClient().GetWanVpnInterfaceCellularParcelByParcelIdForTransport(**kwargs)

@register('GetInterfaceEthernetParcelsForTransportWanVpn')
def GetInterfaceEthernetParcelsForTransportWanVpn(**kwargs):
    return CatalystwanClient().GetInterfaceEthernetParcelsForTransportWanVpn(**kwargs)

@register('GetWanVpnInterfaceEthernetParcelByParcelIdForTransport')
def GetWanVpnInterfaceEthernetParcelByParcelIdForTransport(**kwargs):
    return CatalystwanClient().GetWanVpnInterfaceEthernetParcelByParcelIdForTransport(**kwargs)

@register('GetWanVpnInterfaceEthernetAssociatedIpv6TrackerParcelsForTransport')
def GetWanVpnInterfaceEthernetAssociatedIpv6TrackerParcelsForTransport(**kwargs):
    return CatalystwanClient().GetWanVpnInterfaceEthernetAssociatedIpv6TrackerParcelsForTransport(**kwargs)

@register('GetWanVpnInterfaceEthernetAssociatedIpv6TrackerParcelByParcelIdForTransport')
def GetWanVpnInterfaceEthernetAssociatedIpv6TrackerParcelByParcelIdForTransport(**kwargs):
    return CatalystwanClient().GetWanVpnInterfaceEthernetAssociatedIpv6TrackerParcelByParcelIdForTransport(**kwargs)

@register('GetWanVpnInterfaceEthernetAssociatedIpv6TrackerGroupParcelsForTransport')
def GetWanVpnInterfaceEthernetAssociatedIpv6TrackerGroupParcelsForTransport(**kwargs):
    return CatalystwanClient().GetWanVpnInterfaceEthernetAssociatedIpv6TrackerGroupParcelsForTransport(**kwargs)

@register('GetWanVpnInterfaceEthernetAssociatedIpv6TrackerGroupParcelByParcelIdForTransport')
def GetWanVpnInterfaceEthernetAssociatedIpv6TrackerGroupParcelByParcelIdForTransport(**kwargs):
    return CatalystwanClient().GetWanVpnInterfaceEthernetAssociatedIpv6TrackerGroupParcelByParcelIdForTransport(**kwargs)

@register('GetWanVpnInterfaceEthernetAssociatedTrackerParcelsForTransport')
def GetWanVpnInterfaceEthernetAssociatedTrackerParcelsForTransport(**kwargs):
    return CatalystwanClient().GetWanVpnInterfaceEthernetAssociatedTrackerParcelsForTransport(**kwargs)

@register('GetWanVpnInterfaceEthernetAssociatedTrackerParcelByParcelIdForTransport')
def GetWanVpnInterfaceEthernetAssociatedTrackerParcelByParcelIdForTransport(**kwargs):
    return CatalystwanClient().GetWanVpnInterfaceEthernetAssociatedTrackerParcelByParcelIdForTransport(**kwargs)

@register('GetWanVpnInterfaceEthernetAssociatedTrackerGroupParcelsForTransport')
def GetWanVpnInterfaceEthernetAssociatedTrackerGroupParcelsForTransport(**kwargs):
    return CatalystwanClient().GetWanVpnInterfaceEthernetAssociatedTrackerGroupParcelsForTransport(**kwargs)

@register('GetWanVpnInterfaceEthernetAssociatedTrackerGroupParcelByParcelIdForTransport')
def GetWanVpnInterfaceEthernetAssociatedTrackerGroupParcelByParcelIdForTransport(**kwargs):
    return CatalystwanClient().GetWanVpnInterfaceEthernetAssociatedTrackerGroupParcelByParcelIdForTransport(**kwargs)

@register('GetInterfaceGreParcelsForTransportWanVpn')
def GetInterfaceGreParcelsForTransportWanVpn(**kwargs):
    return CatalystwanClient().GetInterfaceGreParcelsForTransportWanVpn(**kwargs)

@register('GetWanVpnInterfaceGreParcelByParcelIdForTransport')
def GetWanVpnInterfaceGreParcelByParcelIdForTransport(**kwargs):
    return CatalystwanClient().GetWanVpnInterfaceGreParcelByParcelIdForTransport(**kwargs)

@register('GetWanVpnInterfaceGreAssociatedTrackerParcelsForTransport')
def GetWanVpnInterfaceGreAssociatedTrackerParcelsForTransport(**kwargs):
    return CatalystwanClient().GetWanVpnInterfaceGreAssociatedTrackerParcelsForTransport(**kwargs)

@register('GetWanVpnInterfaceGreAssociatedTrackerParcelByParcelIdForTransport')
def GetWanVpnInterfaceGreAssociatedTrackerParcelByParcelIdForTransport(**kwargs):
    return CatalystwanClient().GetWanVpnInterfaceGreAssociatedTrackerParcelByParcelIdForTransport(**kwargs)

@register('getListOfProfileParcels_1')
def getListOfProfileParcels_1(**kwargs):
    return CatalystwanClient().getListOfProfileParcels_1(**kwargs)

@register('getProfileParcelByParcelId_1')
def getProfileParcelByParcelId_1(**kwargs):
    return CatalystwanClient().getProfileParcelByParcelId_1(**kwargs)

@register('GetWanVpnInterfaceIpsecAssociatedTrackerParcelsForTransport')
def GetWanVpnInterfaceIpsecAssociatedTrackerParcelsForTransport(**kwargs):
    return CatalystwanClient().GetWanVpnInterfaceIpsecAssociatedTrackerParcelsForTransport(**kwargs)

@register('GetWanVpnInterfaceIpsecAssociatedTrackerParcelByParcelIdForTransport')
def GetWanVpnInterfaceIpsecAssociatedTrackerParcelByParcelIdForTransport(**kwargs):
    return CatalystwanClient().GetWanVpnInterfaceIpsecAssociatedTrackerParcelByParcelIdForTransport(**kwargs)

@register('GetInterfaceSerialParcelsForTransportWanVpn')
def GetInterfaceSerialParcelsForTransportWanVpn(**kwargs):
    return CatalystwanClient().GetInterfaceSerialParcelsForTransportWanVpn(**kwargs)

@register('GetWanVpnInterfaceSerialParcelByParcelIdForTransport')
def GetWanVpnInterfaceSerialParcelByParcelIdForTransport(**kwargs):
    return CatalystwanClient().GetWanVpnInterfaceSerialParcelByParcelIdForTransport(**kwargs)

@register('GetWanVpnAssociatedRoutingBgpParcelsForTransport')
def GetWanVpnAssociatedRoutingBgpParcelsForTransport(**kwargs):
    return CatalystwanClient().GetWanVpnAssociatedRoutingBgpParcelsForTransport(**kwargs)

@register('GetWanVpnAssociatedRoutingBgpParcelByParcelIdForTransport')
def GetWanVpnAssociatedRoutingBgpParcelByParcelIdForTransport(**kwargs):
    return CatalystwanClient().GetWanVpnAssociatedRoutingBgpParcelByParcelIdForTransport(**kwargs)

@register('GetWanVpnAssociatedRoutingOspfParcelsForTransport')
def GetWanVpnAssociatedRoutingOspfParcelsForTransport(**kwargs):
    return CatalystwanClient().GetWanVpnAssociatedRoutingOspfParcelsForTransport(**kwargs)

@register('GetWanVpnAssociatedRoutingOspfParcelByParcelIdForTransport')
def GetWanVpnAssociatedRoutingOspfParcelByParcelIdForTransport(**kwargs):
    return CatalystwanClient().GetWanVpnAssociatedRoutingOspfParcelByParcelIdForTransport(**kwargs)

@register('GetWanVpnAssociatedRoutingOspfv3IPv4AfParcelsForTransport')
def GetWanVpnAssociatedRoutingOspfv3IPv4AfParcelsForTransport(**kwargs):
    return CatalystwanClient().GetWanVpnAssociatedRoutingOspfv3IPv4AfParcelsForTransport(**kwargs)

@register('GetWanVpnAssociatedRoutingOspfv3IPv4AfParcelByParcelIdForTransport')
def GetWanVpnAssociatedRoutingOspfv3IPv4AfParcelByParcelIdForTransport(**kwargs):
    return CatalystwanClient().GetWanVpnAssociatedRoutingOspfv3IPv4AfParcelByParcelIdForTransport(**kwargs)

@register('GetWanVpnAssociatedRoutingOspfv3IPv6AfParcelsForTransport')
def GetWanVpnAssociatedRoutingOspfv3IPv6AfParcelsForTransport(**kwargs):
    return CatalystwanClient().GetWanVpnAssociatedRoutingOspfv3IPv6AfParcelsForTransport(**kwargs)

@register('GetWanVpnAssociatedRoutingOspfv3IPv6AfParcelByParcelIdForTransport')
def GetWanVpnAssociatedRoutingOspfv3IPv6AfParcelByParcelIdForTransport(**kwargs):
    return CatalystwanClient().GetWanVpnAssociatedRoutingOspfv3IPv6AfParcelByParcelIdForTransport(**kwargs)

@register('getMSLADevices')
def getMSLADevices(**kwargs):
    return CatalystwanClient().getMSLADevices(**kwargs)

@register('getLicenseByUuid')
def getLicenseByUuid(**kwargs):
    return CatalystwanClient().getLicenseByUuid(**kwargs)

@register('GetPolicyGroupBySolution')
def GetPolicyGroupBySolution(**kwargs):
    return CatalystwanClient().GetPolicyGroupBySolution(**kwargs)

@register('GetPolicyGroup')
def GetPolicyGroup(**kwargs):
    return CatalystwanClient().GetPolicyGroup(**kwargs)

@register('GetPolicyGroupAssociation')
def GetPolicyGroupAssociation(**kwargs):
    return CatalystwanClient().GetPolicyGroupAssociation(**kwargs)

@register('getPolicyGroupDeviceVariables')
def getPolicyGroupDeviceVariables(**kwargs):
    return CatalystwanClient().getPolicyGroupDeviceVariables(**kwargs)

@register('getPolicyGroupDeviceVariablesSchema')
def getPolicyGroupDeviceVariablesSchema(**kwargs):
    return CatalystwanClient().getPolicyGroupDeviceVariablesSchema(**kwargs)

@register('getAllReportTemplates')
def getAllReportTemplates(**kwargs):
    return CatalystwanClient().getAllReportTemplates(**kwargs)

@register('downloadReportPreviewFile')
def downloadReportPreviewFile(**kwargs):
    return CatalystwanClient().downloadReportPreviewFile(**kwargs)

@register('getReportTemplateById')
def getReportTemplateById(**kwargs):
    return CatalystwanClient().getReportTemplateById(**kwargs)

@register('getAllReportTasksByReportId')
def getAllReportTasksByReportId(**kwargs):
    return CatalystwanClient().getAllReportTasksByReportId(**kwargs)

@register('downloadReportDataFile')
def downloadReportDataFile(**kwargs):
    return CatalystwanClient().downloadReportDataFile(**kwargs)

@register('getUrlForSdoIdentityService')
def getUrlForSdoIdentityService(**kwargs):
    return CatalystwanClient().getUrlForSdoIdentityService(**kwargs)

@register('getAllAccounts')
def getAllAccounts(**kwargs):
    return CatalystwanClient().getAllAccounts(**kwargs)

@register('getRatePlansByAcctId')
def getRatePlansByAcctId(**kwargs):
    return CatalystwanClient().getRatePlansByAcctId(**kwargs)

@register('getProvidersInfo')
def getProvidersInfo(**kwargs):
    return CatalystwanClient().getProvidersInfo(**kwargs)

@register('getCommPlansByAcctId')
def getCommPlansByAcctId(**kwargs):
    return CatalystwanClient().getCommPlansByAcctId(**kwargs)

@register('getProviderCredentialsByAccountId')
def getProviderCredentialsByAccountId(**kwargs):
    return CatalystwanClient().getProviderCredentialsByAccountId(**kwargs)

@register('getDeviceDataUsage')
def getDeviceDataUsage(**kwargs):
    return CatalystwanClient().getDeviceDataUsage(**kwargs)

@register('serviceChainMapping')
def serviceChainMapping(**kwargs):
    return CatalystwanClient().serviceChainMapping(**kwargs)

@register('getDevicesForTemplate')
def getDevicesForTemplate(**kwargs):
    return CatalystwanClient().getDevicesForTemplate(**kwargs)

@register('license')
def license(**kwargs):
    return CatalystwanClient().license(**kwargs)

@register('getUserSettings')
def getUserSettings(**kwargs):
    return CatalystwanClient().getUserSettings(**kwargs)

@register('GetTopologyGroupBySolution')
def GetTopologyGroupBySolution(**kwargs):
    return CatalystwanClient().GetTopologyGroupBySolution(**kwargs)

@register('GetTopologyGroup')
def GetTopologyGroup(**kwargs):
    return CatalystwanClient().GetTopologyGroup(**kwargs)

@register('generateDeviceInterfaceStatisticsData')
def generateDeviceInterfaceStatisticsData(**kwargs):
    return CatalystwanClient().generateDeviceInterfaceStatisticsData(**kwargs)

@register('getCountWithInterfaceStatistics')
def getCountWithInterfaceStatistics(**kwargs):
    return CatalystwanClient().getCountWithInterfaceStatistics(**kwargs)

@register('getStatDataFieldsByInterfaceStatistics')
def getStatDataFieldsByInterfaceStatistics(**kwargs):
    return CatalystwanClient().getStatDataFieldsByInterfaceStatistics(**kwargs)

@register('getWaniRecommendations')
def getWaniRecommendations(**kwargs):
    return CatalystwanClient().getWaniRecommendations(**kwargs)

@register('getAppliedWaniRecommendations')
def getAppliedWaniRecommendations(**kwargs):
    return CatalystwanClient().getAppliedWaniRecommendations(**kwargs)

@register('getListActivationStatus')
def getListActivationStatus(**kwargs):
    return CatalystwanClient().getListActivationStatus(**kwargs)

@register('getPolicyActivationStatus')
def getPolicyActivationStatus(**kwargs):
    return CatalystwanClient().getPolicyActivationStatus(**kwargs)

@register('webexAccessCode')
def webexAccessCode(**kwargs):
    return CatalystwanClient().webexAccessCode(**kwargs)

@register('getWebexDataCentersSyncStatus')
def getWebexDataCentersSyncStatus(**kwargs):
    return CatalystwanClient().getWebexDataCentersSyncStatus(**kwargs)

@register('redirectWebexDataCenters')
def redirectWebexDataCenters(**kwargs):
    return CatalystwanClient().redirectWebexDataCenters(**kwargs)
