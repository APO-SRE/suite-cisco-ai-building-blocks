# app/llm/function_dispatcher/catalyst_dispatcher.py
from typing import Any
from app.llm.function_dispatcher import register
from app.llm.platform_clients.catalyst_client import CatalystClient

@register('getSecureXAccessToken')
def getSecureXAccessToken(clientId: str, regionBaseUri: str):
    return CatalystClient().getSecureXAccessToken(**{'clientId': clientId, 'regionBaseUri': regionBaseUri})

@register('getAaaConfig')
def getAaaConfig():
    return CatalystClient().getAaaConfig(**{})

@register('listenAuthEvents')
def listenAuthEvents(sseSessionId: str):
    return CatalystClient().listenAuthEvents(**{'sseSessionId': sseSessionId})

@register('getRadiusConfig')
def getRadiusConfig():
    return CatalystClient().getRadiusConfig(**{})

@register('getTacacsConfig')
def getTacacsConfig():
    return CatalystClient().getTacacsConfig(**{})

@register('findUsers_1')
def findUsers_1():
    return CatalystClient().findUsers_1(**{})

@register('getActiveSessions_1')
def getActiveSessions_1():
    return CatalystClient().getActiveSessions_1(**{})

@register('findUserRole_1')
def findUserRole_1():
    return CatalystClient().findUserRole_1(**{})

@register('findUserAuthType_1')
def findUserAuthType_1():
    return CatalystClient().findUserAuthType_1(**{})

@register('findUserGroups')
def findUserGroups():
    return CatalystClient().findUserGroups(**{})

@register('createGroupGridColumns')
def createGroupGridColumns():
    return CatalystClient().createGroupGridColumns(**{})

@register('findUserGroupsAsKeyValue')
def findUserGroupsAsKeyValue():
    return CatalystClient().findUserGroupsAsKeyValue(**{})

@register('getVpnGroups')
def getVpnGroups():
    return CatalystClient().getVpnGroups(**{})

@register('getRawAlarmData')
def getRawAlarmData(**kwargs):
    return CatalystClient().getRawAlarmData(**{**kwargs})

@register('getAggregationData')
def getAggregationData(query: str, **kwargs):
    return CatalystClient().getAggregationData(**{'query': query, **kwargs})

@register('getNonViewedActiveAlarmsCount')
def getNonViewedActiveAlarmsCount(**kwargs):
    return CatalystClient().getNonViewedActiveAlarmsCount(**{**kwargs})

@register('listDisabledAlarm')
def listDisabledAlarm():
    return CatalystClient().listDisabledAlarm(**{})

@register('getDocCount')
def getDocCount(query: str, **kwargs):
    return CatalystClient().getDocCount(**{'query': query, **kwargs})

@register('getAlarmDataFields')
def getAlarmDataFields():
    return CatalystClient().getAlarmDataFields(**{})

@register('getLinkStateAlarmConfig')
def getLinkStateAlarmConfig():
    return CatalystClient().getLinkStateAlarmConfig(**{})

@register('getMasterManagerState')
def getMasterManagerState():
    return CatalystClient().getMasterManagerState(**{})

@register('getNonViewedAlarms')
def getNonViewedAlarms(**kwargs):
    return CatalystClient().getNonViewedAlarms(**{**kwargs})

@register('getPage')
def getPage(**kwargs):
    return CatalystClient().getPage(**{**kwargs})

@register('setPeriodicPurgeTimer')
def setPeriodicPurgeTimer(**kwargs):
    return CatalystClient().setPeriodicPurgeTimer(**{**kwargs})

@register('getAlarmQueryFields')
def getAlarmQueryFields():
    return CatalystClient().getAlarmQueryFields(**{})

@register('getFieldDetails')
def getFieldDetails():
    return CatalystClient().getFieldDetails(**{})

@register('reset')
def reset():
    return CatalystClient().reset(**{})

@register('restartCorrelationEngine')
def restartCorrelationEngine():
    return CatalystClient().restartCorrelationEngine(**{})

@register('getAlarmTypesAsKeyValue')
def getAlarmTypesAsKeyValue():
    return CatalystClient().getAlarmTypesAsKeyValue(**{})

@register('getBySeverity')
def getBySeverity(severity_level: list, **kwargs):
    return CatalystClient().getBySeverity(**{'severity-level': severity_level, **kwargs})

@register('getAlarmSeverityCustomHistogram')
def getAlarmSeverityCustomHistogram(query: str, **kwargs):
    return CatalystClient().getAlarmSeverityCustomHistogram(**{'query': query, **kwargs})

@register('getAlarmSeverityMappings')
def getAlarmSeverityMappings():
    return CatalystClient().getAlarmSeverityMappings(**{})

@register('getStats')
def getStats():
    return CatalystClient().getStats(**{})

@register('getDeviceTopic')
def getDeviceTopic(ip: str):
    return CatalystClient().getDeviceTopic(**{'ip': ip})

@register('getAlarmDetails')
def getAlarmDetails(alarm_uuid: str, **kwargs):
    return CatalystClient().getAlarmDetails(**{'alarm_uuid': alarm_uuid, **kwargs})

@register('getAllAppList')
def getAllAppList(**kwargs):
    return CatalystClient().getAllAppList(**{**kwargs})

@register('getAppListCategory')
def getAppListCategory():
    return CatalystClient().getAppListCategory(**{})

@register('getNetworkDiscoveredApps')
def getNetworkDiscoveredApps():
    return CatalystClient().getNetworkDiscoveredApps(**{})

@register('getAttributeMappingForApps')
def getAttributeMappingForApps():
    return CatalystClient().getAttributeMappingForApps(**{})

@register('getKubernetesServices')
def getKubernetesServices(**kwargs):
    return CatalystClient().getKubernetesServices(**{**kwargs})

@register('getAppByUuid')
def getAppByUuid(app_uuid: str):
    return CatalystClient().getAppByUuid(**{'app-uuid': app_uuid})

@register('getAppList')
def getAppList(**kwargs):
    return CatalystClient().getAppList(**{**kwargs})

@register('getKubernetesCluster')
def getKubernetesCluster(**kwargs):
    return CatalystClient().getKubernetesCluster(**{**kwargs})

@register('getActiveSaasFeeds')
def getActiveSaasFeeds():
    return CatalystClient().getActiveSaasFeeds(**{})

@register('getAllSaasFeedForSelectedApp')
def getAllSaasFeedForSelectedApp(feedId: str):
    return CatalystClient().getAllSaasFeedForSelectedApp(**{'feedId': feedId})

@register('getStatDataRawAuditLogData')
def getStatDataRawAuditLogData(query: str):
    return CatalystClient().getStatDataRawAuditLogData(**{'query': query})

@register('getPropertyAggregationData')
def getPropertyAggregationData(query: str):
    return CatalystClient().getPropertyAggregationData(**{'query': query})

@register('getCount')
def getCount(query: str):
    return CatalystClient().getCount(**{'query': query})

@register('getStatDataFields')
def getStatDataFields():
    return CatalystClient().getStatDataFields(**{})

@register('getStatBulkRawPropertyData')
def getStatBulkRawPropertyData(count: int, query: str, **kwargs):
    return CatalystClient().getStatBulkRawPropertyData(**{'count': count, 'query': query, **kwargs})

@register('getStatQueryFields')
def getStatQueryFields():
    return CatalystClient().getStatQueryFields(**{})

@register('generateAuditLog')
def generateAuditLog(query: str, **kwargs):
    return CatalystClient().generateAuditLog(**{'query': query, **kwargs})

@register('getAuditSeverityCustomHistogram')
def getAuditSeverityCustomHistogram(query: str):
    return CatalystClient().getAuditSeverityCustomHistogram(**{'query': query})

@register('getLocalBackupInfo')
def getLocalBackupInfo(localBackupInfoId: str):
    return CatalystClient().getLocalBackupInfo(**{'localBackupInfoId': localBackupInfoId})

@register('downloadBackupFile')
def downloadBackupFile(path: str):
    return CatalystClient().downloadBackupFile(**{'path': path})

@register('listBackup')
def listBackup(**kwargs):
    return CatalystClient().listBackup(**{**kwargs})

@register('getCdnaSenseService')
def getCdnaSenseService(tag: str):
    return CatalystClient().getCdnaSenseService(**{'tag': tag})

@register('getCdnaServer')
def getCdnaServer():
    return CatalystClient().getCdnaServer(**{})

@register('getControllerCertStatus')
def getControllerCertStatus():
    return CatalystClient().getControllerCertStatus(**{})

@register('getCSRViewRightMenus')
def getCSRViewRightMenus():
    return CatalystClient().getCSRViewRightMenus(**{})

@register('getDeviceViewRightMenus')
def getDeviceViewRightMenus():
    return CatalystClient().getDeviceViewRightMenus(**{})

@register('getDevicesList')
def getDevicesList():
    return CatalystClient().getDevicesList(**{})

@register('getListStatus')
def getListStatus():
    return CatalystClient().getListStatus(**{})

@register('setvSmartMtHubList')
def setvSmartMtHubList():
    return CatalystClient().setvSmartMtHubList(**{})

@register('getQuarantineBanner')
def getQuarantineBanner():
    return CatalystClient().getQuarantineBanner(**{})

@register('getCertificateData')
def getCertificateData(**kwargs):
    return CatalystClient().getCertificateData(**{**kwargs})

@register('getRootCertChains')
def getRootCertChains(action: str):
    return CatalystClient().getRootCertChains(**{'action': action})

@register('getRootCertificate')
def getRootCertificate():
    return CatalystClient().getRootCertificate(**{})

@register('rsaKeyLength2048ForAllDevices')
def rsaKeyLength2048ForAllDevices():
    return CatalystClient().rsaKeyLength2048ForAllDevices(**{})

@register('getCertificateDetail')
def getCertificateDetail(**kwargs):
    return CatalystClient().getCertificateDetail(**{**kwargs})

@register('getCertificateStats')
def getCertificateStats():
    return CatalystClient().getCertificateStats(**{})

@register('syncvBond')
def syncvBond():
    return CatalystClient().syncvBond(**{})

@register('getTokenList')
def getTokenList():
    return CatalystClient().getTokenList(**{})

@register('getInstalledCert')
def getInstalledCert(uuid: str):
    return CatalystClient().getInstalledCert(**{'uuid': uuid})

@register('getvEdgeCSR')
def getvEdgeCSR(uuid: str):
    return CatalystClient().getvEdgeCSR(**{'uuid': uuid})

@register('getvEdgeList')
def getvEdgeList(**kwargs):
    return CatalystClient().getvEdgeList(**{**kwargs})

@register('getView')
def getView():
    return CatalystClient().getView(**{})

@register('getSelfSignedCert')
def getSelfSignedCert():
    return CatalystClient().getSelfSignedCert(**{})

@register('getvSmartList')
def getvSmartList():
    return CatalystClient().getvSmartList(**{})

@register('createServerInfo')
def createServerInfo():
    return CatalystClient().createServerInfo(**{})

@register('getCsrfToken')
def getCsrfToken(**kwargs):
    return CatalystClient().getCsrfToken(**{**kwargs})

@register('getAccessTokenforDevice')
def getAccessTokenforDevice():
    return CatalystClient().getAccessTokenforDevice(**{})

@register('connect')
def connect():
    return CatalystClient().connect(**{})

@register('getCloudCredentials')
def getCloudCredentials():
    return CatalystClient().getCloudCredentials(**{})

@register('isStaging')
def isStaging():
    return CatalystClient().isStaging(**{})

@register('getTelemetryState')
def getTelemetryState():
    return CatalystClient().getTelemetryState(**{})

@register('getvAnalyticsDashboardList')
def getvAnalyticsDashboardList():
    return CatalystClient().getvAnalyticsDashboardList(**{})

@register('checkIfClusterLocked')
def checkIfClusterLocked():
    return CatalystClient().checkIfClusterLocked(**{})

@register('getClusterWorkflowVersion')
def getClusterWorkflowVersion():
    return CatalystClient().getClusterWorkflowVersion(**{})

@register('getConnectedDevices')
def getConnectedDevices(vmanageIP: str):
    return CatalystClient().getConnectedDevices(**{'vmanageIP': vmanageIP})

@register('healthDetails')
def healthDetails():
    return CatalystClient().healthDetails(**{})

@register('healthStatusInfo')
def healthStatusInfo():
    return CatalystClient().healthStatusInfo(**{})

@register('healthSummary')
def healthSummary(**kwargs):
    return CatalystClient().healthSummary(**{**kwargs})

@register('hostHealthStatus')
def hostHealthStatus():
    return CatalystClient().hostHealthStatus(**{})

@register('getConfiguredIPList')
def getConfiguredIPList(vmanageID: str):
    return CatalystClient().getConfiguredIPList(**{'vmanageID': vmanageID})

@register('isClusterReady')
def isClusterReady():
    return CatalystClient().isClusterReady(**{})

@register('listVmanages')
def listVmanages():
    return CatalystClient().listVmanages(**{})

@register('nodeProperties')
def nodeProperties():
    return CatalystClient().nodeProperties(**{})

@register('getTenancyMode')
def getTenancyMode():
    return CatalystClient().getTenancyMode(**{})

@register('getTenantsList')
def getTenantsList():
    return CatalystClient().getTenantsList(**{})

@register('getVManageDetails')
def getVManageDetails(vmanageIP: str):
    return CatalystClient().getVManageDetails(**{'vmanageIP': vmanageIP})

@register('getConnectedDevicesPerTenant')
def getConnectedDevicesPerTenant(tenantId: str, vmanageIP: str):
    return CatalystClient().getConnectedDevicesPerTenant(**{'tenantId': tenantId, 'vmanageIP': vmanageIP})

@register('getvnfByDeviceId')
def getvnfByDeviceId(deviceId: str):
    return CatalystClient().getvnfByDeviceId(**{'deviceId': deviceId})

@register('getVNFEventsCountDetail')
def getVNFEventsCountDetail(user_group: str):
    return CatalystClient().getVNFEventsCountDetail(**{'user_group': user_group})

@register('getVNFAlarmCount')
def getVNFAlarmCount(user_group: str):
    return CatalystClient().getVNFAlarmCount(**{'user_group': user_group})

@register('getVNFEventsDetail')
def getVNFEventsDetail(vnfName: str):
    return CatalystClient().getVNFEventsDetail(**{'vnfName': vnfName})

@register('getVNFInterfaceDetail')
def getVNFInterfaceDetail(vnfName: str, **kwargs):
    return CatalystClient().getVNFInterfaceDetail(**{'vnfName': vnfName, **kwargs})

@register('doesValidImageExist')
def doesValidImageExist(containerName: str):
    return CatalystClient().doesValidImageExist(**{'containerName': containerName})

@register('getContainerInspectData')
def getContainerInspectData(containerName: str, **kwargs):
    return CatalystClient().getContainerInspectData(**{'containerName': containerName, **kwargs})

@register('getContainerSettings')
def getContainerSettings(containerName: str, **kwargs):
    return CatalystClient().getContainerSettings(**{'containerName': containerName, **kwargs})

@register('generateDeviceStateData')
def generateDeviceStateData(state_data_type: str, **kwargs):
    return CatalystClient().generateDeviceStateData(**{'state_data_type': state_data_type, **kwargs})

@register('generateDeviceStateDataFields')
def generateDeviceStateDataFields(state_data_type: str):
    return CatalystClient().generateDeviceStateDataFields(**{'state_data_type': state_data_type})

@register('generateDeviceStateDataWithQueryString')
def generateDeviceStateDataWithQueryString(state_data_type: str):
    return CatalystClient().generateDeviceStateDataWithQueryString(**{'state_data_type': state_data_type})

@register('getStatisticsType')
def getStatisticsType():
    return CatalystClient().getStatisticsType(**{})

@register('getActiveAlarms')
def getActiveAlarms(**kwargs):
    return CatalystClient().getActiveAlarms(**{**kwargs})

@register('generateDeviceStatisticsData')
def generateDeviceStatisticsData(state_data_type: str, **kwargs):
    return CatalystClient().generateDeviceStatisticsData(**{'state_data_type': state_data_type, **kwargs})

@register('getCountWithStateDataType')
def getCountWithStateDataType(endDate: str, startDate: str, state_data_type: str, **kwargs):
    return CatalystClient().getCountWithStateDataType(**{'endDate': endDate, 'startDate': startDate, 'state_data_type': state_data_type, **kwargs})

@register('getStatDataFieldsByStateDataType')
def getStatDataFieldsByStateDataType(state_data_type: str):
    return CatalystClient().getStatDataFieldsByStateDataType(**{'state_data_type': state_data_type})

@register('getCloudSettings')
def getCloudSettings():
    return CatalystClient().getCloudSettings(**{})

@register('getAccessToken')
def getAccessToken():
    return CatalystClient().getAccessToken(**{})

@register('getIdToken')
def getIdToken():
    return CatalystClient().getIdToken(**{})

@register('getOTP')
def getOTP():
    return CatalystClient().getOTP(**{})

@register('getTelemetrySettings')
def getTelemetrySettings():
    return CatalystClient().getTelemetrySettings(**{})

@register('getDCATenantOwners')
def getDCATenantOwners():
    return CatalystClient().getDCATenantOwners(**{})

@register('getCrashLogsSynced')
def getCrashLogsSynced(deviceId: str):
    return CatalystClient().getCrashLogsSynced(**{'deviceId': deviceId})

@register('getCloudServicesConfigurationDCA')
def getCloudServicesConfigurationDCA():
    return CatalystClient().getCloudServicesConfigurationDCA(**{})

@register('listAllDevices')
def listAllDevices(**kwargs):
    return CatalystClient().listAllDevices(**{**kwargs})

@register('getAAAservers')
def getAAAservers(deviceId: str):
    return CatalystClient().getAAAservers(**{'deviceId': deviceId})

@register('getAAAUsers')
def getAAAUsers(deviceId: str):
    return CatalystClient().getAAAUsers(**{'deviceId': deviceId})

@register('getACLMatchCounterUsers')
def getACLMatchCounterUsers(deviceId: str):
    return CatalystClient().getACLMatchCounterUsers(**{'deviceId': deviceId})

@register('generateChangePartitionInfo')
def generateChangePartitionInfo(deviceId: list):
    return CatalystClient().generateChangePartitionInfo(**{'deviceId': deviceId})

@register('generateDeactivateInfo')
def generateDeactivateInfo(deviceId: list):
    return CatalystClient().generateDeactivateInfo(**{'deviceId': deviceId})

@register('createFilterVPNList')
def createFilterVPNList(**kwargs):
    return CatalystClient().createFilterVPNList(**{**kwargs})

@register('getFirmwareImages')
def getFirmwareImages():
    return CatalystClient().getFirmwareImages(**{})

@register('getFirmwareDevices')
def getFirmwareDevices():
    return CatalystClient().getFirmwareDevices(**{})

@register('getFirmwareRemoteImage')
def getFirmwareRemoteImage():
    return CatalystClient().getFirmwareRemoteImage(**{})

@register('getDevicesFWUpgrade')
def getDevicesFWUpgrade():
    return CatalystClient().getDevicesFWUpgrade(**{})

@register('getFirmwareImageDetails')
def getFirmwareImageDetails(versionId: str):
    return CatalystClient().getFirmwareImageDetails(**{'versionId': versionId})

@register('generateInstallInfo')
def generateInstallInfo(deviceId: list):
    return CatalystClient().generateInstallInfo(**{'deviceId': deviceId})

@register('generateDeviceList')
def generateDeviceList(deviceType: str, **kwargs):
    return CatalystClient().generateDeviceList(**{'deviceType': deviceType, **kwargs})

@register('generateDeviceActionList')
def generateDeviceActionList():
    return CatalystClient().generateDeviceActionList(**{})

@register('generateRebootInfo')
def generateRebootInfo(deviceId: list):
    return CatalystClient().generateRebootInfo(**{'deviceId': deviceId})

@register('generateRebootDeviceList')
def generateRebootDeviceList(deviceType: str, groupId: str):
    return CatalystClient().generateRebootDeviceList(**{'deviceType': deviceType, 'groupId': groupId})

@register('generateRediscoverInfo')
def generateRediscoverInfo():
    return CatalystClient().generateRediscoverInfo(**{})

@register('getRemoteServerList')
def getRemoteServerList():
    return CatalystClient().getRemoteServerList(**{})

@register('getRemoteServerById')
def getRemoteServerById(id: str):
    return CatalystClient().getRemoteServerById(**{'id': id})

@register('generateRemovePartitionInfo')
def generateRemovePartitionInfo(**kwargs):
    return CatalystClient().generateRemovePartitionInfo(**{**kwargs})

@register('testApiKey')
def testApiKey(uuid: str):
    return CatalystClient().testApiKey(**{'uuid': uuid})

@register('generateSecurityDevicesList')
def generateSecurityDevicesList(groupId: str, policyType: str):
    return CatalystClient().generateSecurityDevicesList(**{'groupId': groupId, 'policyType': policyType})

@register('findSoftwareImages')
def findSoftwareImages():
    return CatalystClient().findSoftwareImages(**{})

@register('getImageProperties')
def getImageProperties(versionId: str):
    return CatalystClient().getImageProperties(**{'versionId': versionId})

@register('findSoftwareImagesWithFilters')
def findSoftwareImagesWithFilters(imageType: list, **kwargs):
    return CatalystClient().findSoftwareImagesWithFilters(**{'imageType': imageType, **kwargs})

@register('getUploadImagesCount')
def getUploadImagesCount(**kwargs):
    return CatalystClient().getUploadImagesCount(**{**kwargs})

@register('generateUtdImageData')
def generateUtdImageData(type: str, utdsignature: str):
    return CatalystClient().generateUtdImageData(**{'type': type, 'utdsignature': utdsignature})

@register('downloadPackageFile')
def downloadPackageFile(fileName: str, **kwargs):
    return CatalystClient().downloadPackageFile(**{'fileName': fileName, **kwargs})

@register('getImageMetadata')
def getImageMetadata(versionId: str):
    return CatalystClient().getImageMetadata(**{'versionId': versionId})

@register('getImageRemoteServer')
def getImageRemoteServer(versionId: str):
    return CatalystClient().getImageRemoteServer(**{'versionId': versionId})

@register('findVEdgeSoftwareVersion')
def findVEdgeSoftwareVersion():
    return CatalystClient().findVEdgeSoftwareVersion(**{})

@register('findSoftwareVersion')
def findSoftwareVersion():
    return CatalystClient().findSoftwareVersion(**{})

@register('getVnfProperties')
def getVnfProperties(versionId: str):
    return CatalystClient().getVnfProperties(**{'versionId': versionId})

@register('findZtpSoftwareVersion')
def findZtpSoftwareVersion():
    return CatalystClient().findZtpSoftwareVersion(**{})

@register('triggerPendingTasksMonitoring')
def triggerPendingTasksMonitoring():
    return CatalystClient().triggerPendingTasksMonitoring(**{})

@register('cleanStatus')
def cleanStatus(**kwargs):
    return CatalystClient().cleanStatus(**{**kwargs})

@register('getMaintenanceWindowFlag')
def getMaintenanceWindowFlag():
    return CatalystClient().getMaintenanceWindowFlag(**{})

@register('findRunningTasks')
def findRunningTasks():
    return CatalystClient().findRunningTasks(**{})

@register('getActiveTaskCount')
def getActiveTaskCount():
    return CatalystClient().getActiveTaskCount(**{})

@register('getCleanStatus')
def getCleanStatus(processId: str):
    return CatalystClient().getCleanStatus(**{'processId': processId})

@register('findStatus')
def findStatus(processId: str):
    return CatalystClient().findStatus(**{'processId': processId})

@register('testIoxConfig')
def testIoxConfig(deviceIP: str):
    return CatalystClient().testIoxConfig(**{'deviceIP': deviceIP})

@register('createVPNList')
def createVPNList():
    return CatalystClient().createVPNList(**{})

@register('getZTPUpgradeConfig')
def getZTPUpgradeConfig():
    return CatalystClient().getZTPUpgradeConfig(**{})

@register('getZTPUpgradeConfigSetting')
def getZTPUpgradeConfigSetting():
    return CatalystClient().getZTPUpgradeConfigSetting(**{})

@register('getAppHostingAttachedDevices')
def getAppHostingAttachedDevices(deviceId: str):
    return CatalystClient().getAppHostingAttachedDevices(**{'deviceId': deviceId})

@register('getAppHostingDetails')
def getAppHostingDetails(deviceId: str):
    return CatalystClient().getAppHostingDetails(**{'deviceId': deviceId})

@register('getAppHostingGuestRoutes')
def getAppHostingGuestRoutes(deviceId: str):
    return CatalystClient().getAppHostingGuestRoutes(**{'deviceId': deviceId})

@register('getAppHostingNetworkDevices')
def getAppHostingNetworkDevices(deviceId: str):
    return CatalystClient().getAppHostingNetworkDevices(**{'deviceId': deviceId})

@register('getAppHostingNetworkUtils')
def getAppHostingNetworkUtils(deviceId: str):
    return CatalystClient().getAppHostingNetworkUtils(**{'deviceId': deviceId})

@register('getAppHostingProcesses')
def getAppHostingProcesses(deviceId: str):
    return CatalystClient().getAppHostingProcesses(**{'deviceId': deviceId})

@register('getAppHostingStorageUtils')
def getAppHostingStorageUtils(deviceId: str):
    return CatalystClient().getAppHostingStorageUtils(**{'deviceId': deviceId})

@register('getAppHostingUtilization')
def getAppHostingUtilization(deviceId: str):
    return CatalystClient().getAppHostingUtilization(**{'deviceId': deviceId})

@register('createAppRouteSlaClassList')
def createAppRouteSlaClassList(deviceId: str):
    return CatalystClient().createAppRouteSlaClassList(**{'deviceId': deviceId})

@register('createAppRouteStatisticsList')
def createAppRouteStatisticsList(deviceId: str, **kwargs):
    return CatalystClient().createAppRouteStatisticsList(**{'deviceId': deviceId, **kwargs})

@register('getAppLogFlowCount')
def getAppLogFlowCount(deviceId: str):
    return CatalystClient().getAppLogFlowCount(**{'deviceId': deviceId})

@register('getAppLogFlows')
def getAppLogFlows(deviceId: str):
    return CatalystClient().getAppLogFlows(**{'deviceId': deviceId})

@register('createAppqoeActiveFlowIdDetails')
def createAppqoeActiveFlowIdDetails(deviceId: str, flow_id: str):
    return CatalystClient().createAppqoeActiveFlowIdDetails(**{'deviceId': deviceId, 'flow-id': flow_id})

@register('getAppqoeHputStats')
def getAppqoeHputStats(deviceId: str):
    return CatalystClient().getAppqoeHputStats(**{'deviceId': deviceId})

@register('getAppqoeNatStats')
def getAppqoeNatStats(deviceId: str):
    return CatalystClient().getAppqoeNatStats(**{'deviceId': deviceId})

@register('getAppqoeRmResources')
def getAppqoeRmResources(deviceId: str):
    return CatalystClient().getAppqoeRmResources(**{'deviceId': deviceId})

@register('getAppqoeRMStats')
def getAppqoeRMStats(deviceId: str):
    return CatalystClient().getAppqoeRMStats(**{'deviceId': deviceId})

@register('getAppqoeServicesStatus')
def getAppqoeServicesStatus(deviceId: str):
    return CatalystClient().getAppqoeServicesStatus(**{'deviceId': deviceId})

@register('getAppqoeSppiPipeStats')
def getAppqoeSppiPipeStats(deviceId: str):
    return CatalystClient().getAppqoeSppiPipeStats(**{'deviceId': deviceId})

@register('getAppqoeSppiQueueStats')
def getAppqoeSppiQueueStats(deviceId: str):
    return CatalystClient().getAppqoeSppiQueueStats(**{'deviceId': deviceId})

@register('getAppqoeClusterSummary')
def getAppqoeClusterSummary(deviceId: str):
    return CatalystClient().getAppqoeClusterSummary(**{'deviceId': deviceId})

@register('getAppqoeErrorRecent')
def getAppqoeErrorRecent(deviceId: str):
    return CatalystClient().getAppqoeErrorRecent(**{'deviceId': deviceId})

@register('createAppqoeFlowIdExpiredDetails')
def createAppqoeFlowIdExpiredDetails(deviceId: str, flow_id: str):
    return CatalystClient().createAppqoeFlowIdExpiredDetails(**{'deviceId': deviceId, 'flow-id': flow_id})

@register('getAppqoeFlowClosedError')
def getAppqoeFlowClosedError(deviceId: str):
    return CatalystClient().getAppqoeFlowClosedError(**{'deviceId': deviceId})

@register('getAppqoeExpired')
def getAppqoeExpired(deviceId: str):
    return CatalystClient().getAppqoeExpired(**{'deviceId': deviceId})

@register('getAppqoeServiceControllers')
def getAppqoeServiceControllers(deviceId: str):
    return CatalystClient().getAppqoeServiceControllers(**{'deviceId': deviceId})

@register('getAppqoeStatus')
def getAppqoeStatus(deviceId: str):
    return CatalystClient().getAppqoeStatus(**{'deviceId': deviceId})

@register('createAppqoeVpnIdList')
def createAppqoeVpnIdList(deviceId: str, vpn_id: str, **kwargs):
    return CatalystClient().createAppqoeVpnIdList(**{'deviceId': deviceId, 'vpn-id': vpn_id, **kwargs})

@register('getARPInterface')
def getARPInterface(deviceId: str):
    return CatalystClient().getARPInterface(**{'deviceId': deviceId})

@register('getAutonomousSoftwareVersion')
def getAutonomousSoftwareVersion(deviceId: str):
    return CatalystClient().getAutonomousSoftwareVersion(**{'deviceId': deviceId})

@register('createBFDHistoryList')
def createBFDHistoryList(deviceId: str, **kwargs):
    return CatalystClient().createBFDHistoryList(**{'deviceId': deviceId, **kwargs})

@register('createBFDLinkList')
def createBFDLinkList(state: str):
    return CatalystClient().createBFDLinkList(**{'state': state})

@register('createBFDSessions')
def createBFDSessions(deviceId: str, **kwargs):
    return CatalystClient().createBFDSessions(**{'deviceId': deviceId, **kwargs})

@register('getBFDSiteStateDetail')
def getBFDSiteStateDetail(**kwargs):
    return CatalystClient().getBFDSiteStateDetail(**{**kwargs})

@register('getBFDSitesSummary')
def getBFDSitesSummary(vpnId: list, **kwargs):
    return CatalystClient().getBFDSitesSummary(**{'vpnId': vpnId, **kwargs})

@register('getDeviceBFDStateSummary')
def getDeviceBFDStateSummary(deviceId: str):
    return CatalystClient().getDeviceBFDStateSummary(**{'deviceId': deviceId})

@register('getDeviceBFDStateSummaryTloc')
def getDeviceBFDStateSummaryTloc(deviceId: str):
    return CatalystClient().getDeviceBFDStateSummaryTloc(**{'deviceId': deviceId})

@register('getDeviceTlocToIntfList')
def getDeviceTlocToIntfList(deviceId: str):
    return CatalystClient().getDeviceTlocToIntfList(**{'deviceId': deviceId})

@register('getDeviceBFDStatus')
def getDeviceBFDStatus():
    return CatalystClient().getDeviceBFDStatus(**{})

@register('createBFDSummary')
def createBFDSummary(deviceId: str):
    return CatalystClient().createBFDSummary(**{'deviceId': deviceId})

@register('getDeviceBFDStatusSummary')
def getDeviceBFDStatusSummary(deviceId: str):
    return CatalystClient().getDeviceBFDStatusSummary(**{'deviceId': deviceId})

@register('createSyncedBFDSession')
def createSyncedBFDSession(deviceId: str, **kwargs):
    return CatalystClient().createSyncedBFDSession(**{'deviceId': deviceId, **kwargs})

@register('createTLOCSummary')
def createTLOCSummary(deviceId: str):
    return CatalystClient().createTLOCSummary(**{'deviceId': deviceId})

@register('getBFDTlocStateDetail')
def getBFDTlocStateDetail(**kwargs):
    return CatalystClient().getBFDTlocStateDetail(**{**kwargs})

@register('createBGPNeighborsList')
def createBGPNeighborsList(deviceId: str, **kwargs):
    return CatalystClient().createBGPNeighborsList(**{'deviceId': deviceId, **kwargs})

@register('createBGPRoutesList')
def createBGPRoutesList(deviceId: str, **kwargs):
    return CatalystClient().createBGPRoutesList(**{'deviceId': deviceId, **kwargs})

@register('createBGPSummary')
def createBGPSummary(deviceId: str):
    return CatalystClient().createBGPSummary(**{'deviceId': deviceId})

@register('getBridgeInterfaceList')
def getBridgeInterfaceList(deviceId: str):
    return CatalystClient().getBridgeInterfaceList(**{'deviceId': deviceId})

@register('getBridgeInterfaceMac')
def getBridgeInterfaceMac(deviceId: str, **kwargs):
    return CatalystClient().getBridgeInterfaceMac(**{'deviceId': deviceId, **kwargs})

@register('getBridgeInterfaceTable')
def getBridgeInterfaceTable(deviceId: str):
    return CatalystClient().getBridgeInterfaceTable(**{'deviceId': deviceId})

@register('getTenantsDevicesAndSites')
def getTenantsDevicesAndSites(**kwargs):
    return CatalystClient().getTenantsDevicesAndSites(**{**kwargs})

@register('createAppFwdCflowdFlowsList')
def createAppFwdCflowdFlowsList(deviceId: str, **kwargs):
    return CatalystClient().createAppFwdCflowdFlowsList(**{'deviceId': deviceId, **kwargs})

@register('createAppFwdCflowdV6FlowsList')
def createAppFwdCflowdV6FlowsList(deviceId: str, **kwargs):
    return CatalystClient().createAppFwdCflowdV6FlowsList(**{'deviceId': deviceId, **kwargs})

@register('createCellularConnectionList')
def createCellularConnectionList(deviceId: str):
    return CatalystClient().createCellularConnectionList(**{'deviceId': deviceId})

@register('cellularCountDashlet')
def cellularCountDashlet(**kwargs):
    return CatalystClient().cellularCountDashlet(**{**kwargs})

@register('dataUsage')
def dataUsage(**kwargs):
    return CatalystClient().dataUsage(**{**kwargs})

@register('cellularCountDashletDetails')
def cellularCountDashletDetails(**kwargs):
    return CatalystClient().cellularCountDashletDetails(**{**kwargs})

@register('createHardwareList')
def createHardwareList(deviceId: str):
    return CatalystClient().createHardwareList(**{'deviceId': deviceId})

@register('cellularHealthDashlet')
def cellularHealthDashlet(**kwargs):
    return CatalystClient().cellularHealthDashlet(**{**kwargs})

@register('createModemList')
def createModemList(deviceId: str):
    return CatalystClient().createModemList(**{'deviceId': deviceId})

@register('createNetworkList')
def createNetworkList(deviceId: str):
    return CatalystClient().createNetworkList(**{'deviceId': deviceId})

@register('createProfileList')
def createProfileList(deviceId: str):
    return CatalystClient().createProfileList(**{'deviceId': deviceId})

@register('createRadioList')
def createRadioList(deviceId: str):
    return CatalystClient().createRadioList(**{'deviceId': deviceId})

@register('createSessionsList')
def createSessionsList(deviceId: str, **kwargs):
    return CatalystClient().createSessionsList(**{'deviceId': deviceId, **kwargs})

@register('getCellularStatusList')
def getCellularStatusList(deviceId: str):
    return CatalystClient().getCellularStatusList(**{'deviceId': deviceId})

@register('getEiolteConnectionInfo')
def getEiolteConnectionInfo(deviceId: str):
    return CatalystClient().getEiolteConnectionInfo(**{'deviceId': deviceId})

@register('getEiolteHardwareInfo')
def getEiolteHardwareInfo(deviceId: str):
    return CatalystClient().getEiolteHardwareInfo(**{'deviceId': deviceId})

@register('getAONIpsecInterfaceCountersInfo')
def getAONIpsecInterfaceCountersInfo(deviceId: str):
    return CatalystClient().getAONIpsecInterfaceCountersInfo(**{'deviceId': deviceId})

@register('getAONIpsecInterfaceSessionnfo')
def getAONIpsecInterfaceSessionnfo(deviceId: str):
    return CatalystClient().getAONIpsecInterfaceSessionnfo(**{'deviceId': deviceId})

@register('getEiolteNetworkInfo')
def getEiolteNetworkInfo(deviceId: str):
    return CatalystClient().getEiolteNetworkInfo(**{'deviceId': deviceId})

@register('getEiolteRadioInfo')
def getEiolteRadioInfo(deviceId: str):
    return CatalystClient().getEiolteRadioInfo(**{'deviceId': deviceId})

@register('getEiolteSimInfo')
def getEiolteSimInfo(deviceId: str):
    return CatalystClient().getEiolteSimInfo(**{'deviceId': deviceId})

@register('getCflowdDPIDeviceFieldJSON')
def getCflowdDPIDeviceFieldJSON(**kwargs):
    return CatalystClient().getCflowdDPIDeviceFieldJSON(**{**kwargs})

@register('createCflowdCollectorList')
def createCflowdCollectorList(deviceId: str):
    return CatalystClient().createCflowdCollectorList(**{'deviceId': deviceId})

@register('getCflowdDPIFieldJSON')
def getCflowdDPIFieldJSON(**kwargs):
    return CatalystClient().getCflowdDPIFieldJSON(**{**kwargs})

@register('createCflowCollectorList')
def createCflowCollectorList(deviceId: str, **kwargs):
    return CatalystClient().createCflowCollectorList(**{'deviceId': deviceId, **kwargs})

@register('createCflowdFlowsCountList')
def createCflowdFlowsCountList(deviceId: str, **kwargs):
    return CatalystClient().createCflowdFlowsCountList(**{'deviceId': deviceId, **kwargs})

@register('getFnFCacheStats')
def getFnFCacheStats(deviceId: str):
    return CatalystClient().getFnFCacheStats(**{'deviceId': deviceId})

@register('getFnFExportClientStats')
def getFnFExportClientStats(deviceId: str):
    return CatalystClient().getFnFExportClientStats(**{'deviceId': deviceId})

@register('getFnFExportStats')
def getFnFExportStats(deviceId: str):
    return CatalystClient().getFnFExportStats(**{'deviceId': deviceId})

@register('getFnf')
def getFnf(deviceId: str):
    return CatalystClient().getFnf(**{'deviceId': deviceId})

@register('getFnFMonitorStats')
def getFnFMonitorStats(deviceId: str):
    return CatalystClient().getFnFMonitorStats(**{'deviceId': deviceId})

@register('createCflowdStatistics')
def createCflowdStatistics(deviceId: str):
    return CatalystClient().createCflowdStatistics(**{'deviceId': deviceId})

@register('createCflowdTemplate')
def createCflowdTemplate(deviceId: str):
    return CatalystClient().createCflowdTemplate(**{'deviceId': deviceId})

@register('getMpDatabase')
def getMpDatabase(deviceId: str):
    return CatalystClient().getMpDatabase(**{'deviceId': deviceId})

@register('getMpLocalMep')
def getMpLocalMep(deviceId: str, **kwargs):
    return CatalystClient().getMpLocalMep(**{'deviceId': deviceId, **kwargs})

@register('getMpLocalMip')
def getMpLocalMip(deviceId: str, **kwargs):
    return CatalystClient().getMpLocalMip(**{'deviceId': deviceId, **kwargs})

@register('getMpRemoteMep')
def getMpRemoteMep(deviceId: str, **kwargs):
    return CatalystClient().getMpRemoteMep(**{'deviceId': deviceId, **kwargs})

@register('createApplicationsDetailList')
def createApplicationsDetailList(**kwargs):
    return CatalystClient().createApplicationsDetailList(**{**kwargs})

@register('createApplicationsList')
def createApplicationsList(**kwargs):
    return CatalystClient().createApplicationsList(**{**kwargs})

@register('createGatewayExitsList')
def createGatewayExitsList(deviceId: str, **kwargs):
    return CatalystClient().createGatewayExitsList(**{'deviceId': deviceId, **kwargs})

@register('createLbApplicationsList')
def createLbApplicationsList(**kwargs):
    return CatalystClient().createLbApplicationsList(**{**kwargs})

@register('createLocalExitsList')
def createLocalExitsList(deviceId: str, **kwargs):
    return CatalystClient().createLocalExitsList(**{'deviceId': deviceId, **kwargs})

@register('getComplianceDetails')
def getComplianceDetails(**kwargs):
    return CatalystClient().getComplianceDetails(**{**kwargs})

@register('getComplianceSummary')
def getComplianceSummary():
    return CatalystClient().getComplianceSummary(**{})

@register('getDeviceRunningConfig')
def getDeviceRunningConfig(deviceId: list):
    return CatalystClient().getDeviceRunningConfig(**{'deviceId': deviceId})

@register('getDeviceRunningConfigHTML')
def getDeviceRunningConfigHTML(deviceId: list):
    return CatalystClient().getDeviceRunningConfigHTML(**{'deviceId': deviceId})

@register('getDeviceConfigurationCommitList')
def getDeviceConfigurationCommitList(deviceId: str):
    return CatalystClient().getDeviceConfigurationCommitList(**{'deviceId': deviceId})

@register('getAffinityConfig')
def getAffinityConfig(deviceId: str):
    return CatalystClient().getAffinityConfig(**{'deviceId': deviceId})

@register('getAffinityStatus')
def getAffinityStatus(deviceId: str):
    return CatalystClient().getAffinityStatus(**{'deviceId': deviceId})

@register('createRealTimeConnectionList')
def createRealTimeConnectionList(deviceId: str, **kwargs):
    return CatalystClient().createRealTimeConnectionList(**{'deviceId': deviceId, **kwargs})

@register('createConnectionHistoryListRealTime')
def createConnectionHistoryListRealTime(deviceId: str, **kwargs):
    return CatalystClient().createConnectionHistoryListRealTime(**{'deviceId': deviceId, **kwargs})

@register('createRealTimeConnectionList_1')
def createRealTimeConnectionList_1(deviceId: str, **kwargs):
    return CatalystClient().createRealTimeConnectionList_1(**{'deviceId': deviceId, **kwargs})

@register('getTotalCountForDeviceStates')
def getTotalCountForDeviceStates(**kwargs):
    return CatalystClient().getTotalCountForDeviceStates(**{**kwargs})

@register('createLinkList')
def createLinkList(state: str):
    return CatalystClient().createLinkList(**{'state': state})

@register('createLocalPropertiesListListRealTIme')
def createLocalPropertiesListListRealTIme(deviceId: str):
    return CatalystClient().createLocalPropertiesListListRealTIme(**{'deviceId': deviceId})

@register('networkSummary')
def networkSummary(**kwargs):
    return CatalystClient().networkSummary(**{**kwargs})

@register('createRealTimeRegionConnectionList')
def createRealTimeRegionConnectionList(deviceId: str):
    return CatalystClient().createRealTimeRegionConnectionList(**{'deviceId': deviceId})

@register('getConnectionStatistics')
def getConnectionStatistics(deviceId: str):
    return CatalystClient().getConnectionStatistics(**{'deviceId': deviceId})

@register('getLocalDeviceStatus')
def getLocalDeviceStatus():
    return CatalystClient().getLocalDeviceStatus(**{})

@register('createConnectionsSummary')
def createConnectionsSummary(deviceId: str):
    return CatalystClient().createConnectionsSummary(**{'deviceId': deviceId})

@register('getDeviceControlStatusSummary')
def getDeviceControlStatusSummary(deviceId: str):
    return CatalystClient().getDeviceControlStatusSummary(**{'deviceId': deviceId})

@register('createSyncedConnectionList')
def createSyncedConnectionList(deviceId: str, **kwargs):
    return CatalystClient().createSyncedConnectionList(**{'deviceId': deviceId, **kwargs})

@register('createLocalPropertiesSyncedList')
def createLocalPropertiesSyncedList(deviceId: str):
    return CatalystClient().createLocalPropertiesSyncedList(**{'deviceId': deviceId})

@register('createWanInterfaceSyncedList')
def createWanInterfaceSyncedList(deviceId: str):
    return CatalystClient().createWanInterfaceSyncedList(**{'deviceId': deviceId})

@register('createValidDevicesListRealTime')
def createValidDevicesListRealTime(deviceId: str):
    return CatalystClient().createValidDevicesListRealTime(**{'deviceId': deviceId})

@register('getValidVManageIdRealTime')
def getValidVManageIdRealTime(deviceId: str):
    return CatalystClient().getValidVManageIdRealTime(**{'deviceId': deviceId})

@register('createValidVSmartsListRealTime')
def createValidVSmartsListRealTime(deviceId: str):
    return CatalystClient().createValidVSmartsListRealTime(**{'deviceId': deviceId})

@register('createWanInterfaceListList')
def createWanInterfaceListList(deviceId: str):
    return CatalystClient().createWanInterfaceListList(**{'deviceId': deviceId})

@register('getPortHopColor')
def getPortHopColor(deviceId: str):
    return CatalystClient().getPortHopColor(**{'deviceId': deviceId})

@register('getDeviceCounters')
def getDeviceCounters():
    return CatalystClient().getDeviceCounters(**{})

@register('getDeviceCrashLogs')
def getDeviceCrashLogs(deviceId: str):
    return CatalystClient().getDeviceCrashLogs(**{'deviceId': deviceId})

@register('getAllDeviceCrashLogs')
def getAllDeviceCrashLogs():
    return CatalystClient().getAllDeviceCrashLogs(**{})

@register('getDeviceCrashInformation')
def getDeviceCrashInformation(deviceId: str, filename: str):
    return CatalystClient().getDeviceCrashInformation(**{'deviceId': deviceId, 'filename': filename})

@register('getDeviceCrashLogsSynced')
def getDeviceCrashLogsSynced(deviceId: str):
    return CatalystClient().getDeviceCrashLogsSynced(**{'deviceId': deviceId})

@register('createDeviceContainersInfo')
def createDeviceContainersInfo(deviceId: str):
    return CatalystClient().createDeviceContainersInfo(**{'deviceId': deviceId})

@register('getPnicStats')
def getPnicStats(deviceId: str):
    return CatalystClient().getPnicStats(**{'deviceId': deviceId})

@register('getPNICStatsFromDevice')
def getPNICStatsFromDevice(deviceId: str):
    return CatalystClient().getPNICStatsFromDevice(**{'deviceId': deviceId})

@register('getRBACInterface')
def getRBACInterface(deviceId: str):
    return CatalystClient().getRBACInterface(**{'deviceId': deviceId})

@register('getAllocationInfo')
def getAllocationInfo(deviceId: str):
    return CatalystClient().getAllocationInfo(**{'deviceId': deviceId})

@register('getCPUInfo')
def getCPUInfo(deviceId: str):
    return CatalystClient().getCPUInfo(**{'deviceId': deviceId})

@register('getVNFInfo')
def getVNFInfo(deviceId: str):
    return CatalystClient().getVNFInfo(**{'deviceId': deviceId})

@register('createDeviceSystemSettingNativeInfo')
def createDeviceSystemSettingNativeInfo(deviceId: str):
    return CatalystClient().createDeviceSystemSettingNativeInfo(**{'deviceId': deviceId})

@register('createDeviceSystemProcessList')
def createDeviceSystemProcessList(deviceId: str):
    return CatalystClient().createDeviceSystemProcessList(**{'deviceId': deviceId})

@register('createDeviceSystemSetting')
def createDeviceSystemSetting(deviceId: str):
    return CatalystClient().createDeviceSystemSetting(**{'deviceId': deviceId})

@register('createDeviceSystemStatus')
def createDeviceSystemStatus(deviceId: str):
    return CatalystClient().createDeviceSystemStatus(**{'deviceId': deviceId})

@register('getCtsPac')
def getCtsPac(deviceId: str):
    return CatalystClient().getCtsPac(**{'deviceId': deviceId})

@register('getDeviceOnlyStatus')
def getDeviceOnlyStatus():
    return CatalystClient().getDeviceOnlyStatus(**{})

@register('getDHCPClient')
def getDHCPClient(deviceId: str):
    return CatalystClient().getDHCPClient(**{'deviceId': deviceId})

@register('getDHCPInterface')
def getDHCPInterface(deviceId: str):
    return CatalystClient().getDHCPInterface(**{'deviceId': deviceId})

@register('getDHCPServer')
def getDHCPServer(deviceId: str):
    return CatalystClient().getDHCPServer(**{'deviceId': deviceId})

@register('getDHCPv6Interface')
def getDHCPv6Interface(deviceId: str):
    return CatalystClient().getDHCPv6Interface(**{'deviceId': deviceId})

@register('getWLANDOT1xClients')
def getWLANDOT1xClients(deviceId: str):
    return CatalystClient().getWLANDOT1xClients(**{'deviceId': deviceId})

@register('getWLANDOT1xInterfaces')
def getWLANDOT1xInterfaces(deviceId: str):
    return CatalystClient().getWLANDOT1xInterfaces(**{'deviceId': deviceId})

@register('getDOT1xRadius')
def getDOT1xRadius(deviceId: str):
    return CatalystClient().getDOT1xRadius(**{'deviceId': deviceId})

@register('createSoftwareList')
def createSoftwareList(deviceId: str):
    return CatalystClient().createSoftwareList(**{'deviceId': deviceId})

@register('getSupportedApplicationList')
def getSupportedApplicationList():
    return CatalystClient().getSupportedApplicationList(**{})

@register('getDPIDeviceFieldJSON')
def getDPIDeviceFieldJSON(**kwargs):
    return CatalystClient().getDPIDeviceFieldJSON(**{**kwargs})

@register('createDPICollectorList')
def createDPICollectorList(deviceId: str, **kwargs):
    return CatalystClient().createDPICollectorList(**{'deviceId': deviceId, **kwargs})

@register('getCommonApplicationList')
def getCommonApplicationList():
    return CatalystClient().getCommonApplicationList(**{})

@register('getDPIFieldJSON')
def getDPIFieldJSON():
    return CatalystClient().getDPIFieldJSON(**{})

@register('getDPIDeviceDetailsFieldJSON')
def getDPIDeviceDetailsFieldJSON():
    return CatalystClient().getDPIDeviceDetailsFieldJSON(**{})

@register('createDPIFlowsList')
def createDPIFlowsList(deviceId: str, **kwargs):
    return CatalystClient().createDPIFlowsList(**{'deviceId': deviceId, **kwargs})

@register('getQosmosStaticApplicationList')
def getQosmosStaticApplicationList():
    return CatalystClient().getQosmosStaticApplicationList(**{})

@register('getQosmosApplicationList')
def getQosmosApplicationList():
    return CatalystClient().getQosmosApplicationList(**{})

@register('createDPISummaryRealTime')
def createDPISummaryRealTime(deviceId: str):
    return CatalystClient().createDPISummaryRealTime(**{'deviceId': deviceId})

@register('createDPIStatistics')
def createDPIStatistics(deviceId: str, **kwargs):
    return CatalystClient().createDPIStatistics(**{'deviceId': deviceId, **kwargs})

@register('getDreAutoBypassStats')
def getDreAutoBypassStats(deviceId: str, **kwargs):
    return CatalystClient().getDreAutoBypassStats(**{'deviceId': deviceId, **kwargs})

@register('getDreStats')
def getDreStats(deviceId: str):
    return CatalystClient().getDreStats(**{'deviceId': deviceId})

@register('getDreStatus')
def getDreStatus(deviceId: str):
    return CatalystClient().getDreStatus(**{'deviceId': deviceId})

@register('getDrePeerStats')
def getDrePeerStats(deviceId: str, **kwargs):
    return CatalystClient().getDrePeerStats(**{'deviceId': deviceId, **kwargs})

@register('getDualStaticRouteTrackerInfo')
def getDualStaticRouteTrackerInfo(deviceId: str):
    return CatalystClient().getDualStaticRouteTrackerInfo(**{'deviceId': deviceId})

@register('createEIGRPInterface')
def createEIGRPInterface(deviceId: str):
    return CatalystClient().createEIGRPInterface(**{'deviceId': deviceId})

@register('createEIGRPRoute')
def createEIGRPRoute(deviceId: str):
    return CatalystClient().createEIGRPRoute(**{'deviceId': deviceId})

@register('createEIGRPTopology')
def createEIGRPTopology(deviceId: str):
    return CatalystClient().createEIGRPTopology(**{'deviceId': deviceId})

@register('getEndpointTrackerInfo')
def getEndpointTrackerInfo(deviceId: str):
    return CatalystClient().getEndpointTrackerInfo(**{'deviceId': deviceId})

@register('getEndpointTrackerGroupInfo')
def getEndpointTrackerGroupInfo(deviceId: str):
    return CatalystClient().getEndpointTrackerGroupInfo(**{'deviceId': deviceId})

@register('getEnvironmentData')
def getEnvironmentData(deviceId: str):
    return CatalystClient().getEnvironmentData(**{'deviceId': deviceId})

@register('getRadiusServer')
def getRadiusServer(deviceId: str):
    return CatalystClient().getRadiusServer(**{'deviceId': deviceId})

@register('getFeatureList')
def getFeatureList(deviceId: str):
    return CatalystClient().getFeatureList(**{'deviceId': deviceId})

@register('getSyncedFeatureList')
def getSyncedFeatureList(deviceId: str):
    return CatalystClient().getSyncedFeatureList(**{'deviceId': deviceId})

@register('getDataCollectionStatusForDevice')
def getDataCollectionStatusForDevice(deviceUUID: str):
    return CatalystClient().getDataCollectionStatusForDevice(**{'deviceUUID': deviceUUID})

@register('downloadGeneratedFile')
def downloadGeneratedFile(requestUUID: str):
    return CatalystClient().downloadGeneratedFile(**{'requestUUID': requestUUID})

@register('getDataCollectionStatusForUUID')
def getDataCollectionStatusForUUID(requestUUID: str):
    return CatalystClient().getDataCollectionStatusForUUID(**{'requestUUID': requestUUID})

@register('getSupportedCommandsList')
def getSupportedCommandsList(deviceUUID: str):
    return CatalystClient().getSupportedCommandsList(**{'deviceUUID': deviceUUID})

@register('getGeofenceStatus')
def getGeofenceStatus(deviceId: str):
    return CatalystClient().getGeofenceStatus(**{'deviceId': deviceId})

@register('createAlarmList')
def createAlarmList(deviceId: str):
    return CatalystClient().createAlarmList(**{'deviceId': deviceId})

@register('createEnvironmentList')
def createEnvironmentList(deviceId: str):
    return CatalystClient().createEnvironmentList(**{'deviceId': deviceId})

@register('createErrorAlarmList')
def createErrorAlarmList():
    return CatalystClient().createErrorAlarmList(**{})

@register('createInventoryList')
def createInventoryList(deviceId: str):
    return CatalystClient().createInventoryList(**{'deviceId': deviceId})

@register('createStatusSummary')
def createStatusSummary(deviceId: str):
    return CatalystClient().createStatusSummary(**{'deviceId': deviceId})

@register('createSyncedAlarmList')
def createSyncedAlarmList(deviceId: str):
    return CatalystClient().createSyncedAlarmList(**{'deviceId': deviceId})

@register('createSyncedEnvironmentList')
def createSyncedEnvironmentList(deviceId: str):
    return CatalystClient().createSyncedEnvironmentList(**{'deviceId': deviceId})

@register('createSyncedInventoryList')
def createSyncedInventoryList(deviceId: str):
    return CatalystClient().createSyncedInventoryList(**{'deviceId': deviceId})

@register('createSystemList')
def createSystemList(deviceId: str):
    return CatalystClient().createSystemList(**{'deviceId': deviceId})

@register('createTempThresholdList')
def createTempThresholdList(deviceId: str):
    return CatalystClient().createTempThresholdList(**{'deviceId': deviceId})

@register('getHardwareHealthDetails')
def getHardwareHealthDetails(**kwargs):
    return CatalystClient().getHardwareHealthDetails(**{**kwargs})

@register('getHardwareHealthSummary')
def getHardwareHealthSummary(vpnId: list, **kwargs):
    return CatalystClient().getHardwareHealthSummary(**{'vpnId': vpnId, **kwargs})

@register('getStatDataRawData_21')
def getStatDataRawData_21(**kwargs):
    return CatalystClient().getStatDataRawData_21(**{**kwargs})

@register('getAggregationDataByQuery_23')
def getAggregationDataByQuery_23(**kwargs):
    return CatalystClient().getAggregationDataByQuery_23(**{**kwargs})

@register('getLastThousandConfigList')
def getLastThousandConfigList(deviceId: str, query: str):
    return CatalystClient().getLastThousandConfigList(**{'deviceId': deviceId, 'query': query})

@register('getConfigDiff')
def getConfigDiff(config_id1: str, config_id2: str):
    return CatalystClient().getConfigDiff(**{'config_id1': config_id1, 'config_id2': config_id2})

@register('getDeviceConfig')
def getDeviceConfig(config_id: str):
    return CatalystClient().getDeviceConfig(**{'config_id': config_id})

@register('getStatDataRawDataAsCSV_21')
def getStatDataRawDataAsCSV_21(**kwargs):
    return CatalystClient().getStatDataRawDataAsCSV_21(**{**kwargs})

@register('getCount_20')
def getCount_20(query: str):
    return CatalystClient().getCount_20(**{'query': query})

@register('getStatDataFields_22')
def getStatDataFields_22():
    return CatalystClient().getStatDataFields_22(**{})

@register('getStatsPaginationRawData_19')
def getStatsPaginationRawData_19(**kwargs):
    return CatalystClient().getStatsPaginationRawData_19(**{**kwargs})

@register('getStatQueryFields_23')
def getStatQueryFields_23():
    return CatalystClient().getStatQueryFields_23(**{})

@register('createIGMPGroupsList')
def createIGMPGroupsList(deviceId: str):
    return CatalystClient().createIGMPGroupsList(**{'deviceId': deviceId})

@register('createIGMPInterfaceList')
def createIGMPInterfaceList(deviceId: str):
    return CatalystClient().createIGMPInterfaceList(**{'deviceId': deviceId})

@register('createIGMPStatisticsList')
def createIGMPStatisticsList(deviceId: str):
    return CatalystClient().createIGMPStatisticsList(**{'deviceId': deviceId})

@register('createIGMPSummary')
def createIGMPSummary(deviceId: str):
    return CatalystClient().createIGMPSummary(**{'deviceId': deviceId})

@register('getDeviceInterface')
def getDeviceInterface(deviceId: str, **kwargs):
    return CatalystClient().getDeviceInterface(**{'deviceId': deviceId, **kwargs})

@register('getDeviceInterfaceARPStats')
def getDeviceInterfaceARPStats(deviceId: str, **kwargs):
    return CatalystClient().getDeviceInterfaceARPStats(**{'deviceId': deviceId, **kwargs})

@register('getDeviceInterfaceErrorStats')
def getDeviceInterfaceErrorStats(deviceId: str, **kwargs):
    return CatalystClient().getDeviceInterfaceErrorStats(**{'deviceId': deviceId, **kwargs})

@register('getDeviceInterfaceIpv6Stats')
def getDeviceInterfaceIpv6Stats(deviceId: str, **kwargs):
    return CatalystClient().getDeviceInterfaceIpv6Stats(**{'deviceId': deviceId, **kwargs})

@register('getDeviceInterfacePktSizes')
def getDeviceInterfacePktSizes(deviceId: str, **kwargs):
    return CatalystClient().getDeviceInterfacePktSizes(**{'deviceId': deviceId, **kwargs})

@register('getDeviceInterfacePortStats')
def getDeviceInterfacePortStats(deviceId: str, **kwargs):
    return CatalystClient().getDeviceInterfacePortStats(**{'deviceId': deviceId, **kwargs})

@register('getDeviceInterfaceQosStats')
def getDeviceInterfaceQosStats(deviceId: str, **kwargs):
    return CatalystClient().getDeviceInterfaceQosStats(**{'deviceId': deviceId, **kwargs})

@register('getDeviceInterfaceQueueStats')
def getDeviceInterfaceQueueStats(deviceId: str, **kwargs):
    return CatalystClient().getDeviceInterfaceQueueStats(**{'deviceId': deviceId, **kwargs})

@register('getDeviceSerialInterface')
def getDeviceSerialInterface(deviceId: str, **kwargs):
    return CatalystClient().getDeviceSerialInterface(**{'deviceId': deviceId, **kwargs})

@register('getDeviceInterfaceStats')
def getDeviceInterfaceStats(deviceId: str, **kwargs):
    return CatalystClient().getDeviceInterfaceStats(**{'deviceId': deviceId, **kwargs})

@register('getSyncedDeviceInterface')
def getSyncedDeviceInterface(deviceId: str, **kwargs):
    return CatalystClient().getSyncedDeviceInterface(**{'deviceId': deviceId, **kwargs})

@register('trustsec')
def trustsec(deviceId: str):
    return CatalystClient().trustsec(**{'deviceId': deviceId})

@register('generateDeviceInterfaceVPN')
def generateDeviceInterfaceVPN(deviceId: str):
    return CatalystClient().generateDeviceInterfaceVPN(**{'deviceId': deviceId})

@register('createFibList')
def createFibList(deviceId: str, **kwargs):
    return CatalystClient().createFibList(**{'deviceId': deviceId, **kwargs})

@register('createIetfRoutingList')
def createIetfRoutingList(deviceId: str, **kwargs):
    return CatalystClient().createIetfRoutingList(**{'deviceId': deviceId, **kwargs})

@register('createIPMfibOilList')
def createIPMfibOilList(deviceId: str):
    return CatalystClient().createIPMfibOilList(**{'deviceId': deviceId})

@register('createIPMfibStatsList')
def createIPMfibStatsList(deviceId: str):
    return CatalystClient().createIPMfibStatsList(**{'deviceId': deviceId})

@register('createIPMfibSummaryList')
def createIPMfibSummaryList(deviceId: str):
    return CatalystClient().createIPMfibSummaryList(**{'deviceId': deviceId})

@register('createNatFilterList')
def createNatFilterList(deviceId: str, **kwargs):
    return CatalystClient().createNatFilterList(**{'deviceId': deviceId, **kwargs})

@register('createNatInterfaceList')
def createNatInterfaceList(deviceId: str):
    return CatalystClient().createNatInterfaceList(**{'deviceId': deviceId})

@register('createNatInterfaceStatisticsList')
def createNatInterfaceStatisticsList(deviceId: str):
    return CatalystClient().createNatInterfaceStatisticsList(**{'deviceId': deviceId})

@register('createNatTranslationList')
def createNatTranslationList(deviceId: str):
    return CatalystClient().createNatTranslationList(**{'deviceId': deviceId})

@register('createNat64TranslationList')
def createNat64TranslationList(deviceId: str):
    return CatalystClient().createNat64TranslationList(**{'deviceId': deviceId})

@register('createRouteTableList')
def createRouteTableList(deviceId: str, **kwargs):
    return CatalystClient().createRouteTableList(**{'deviceId': deviceId, **kwargs})

@register('createIPv4FibList')
def createIPv4FibList(deviceId: str, **kwargs):
    return CatalystClient().createIPv4FibList(**{'deviceId': deviceId, **kwargs})

@register('createIPv6FibList')
def createIPv6FibList(deviceId: str, **kwargs):
    return CatalystClient().createIPv6FibList(**{'deviceId': deviceId, **kwargs})

@register('createCryptoIpsecIdentity')
def createCryptoIpsecIdentity(deviceId: str, **kwargs):
    return CatalystClient().createCryptoIpsecIdentity(**{'deviceId': deviceId, **kwargs})

@register('createIkeInboundList')
def createIkeInboundList(deviceId: str):
    return CatalystClient().createIkeInboundList(**{'deviceId': deviceId})

@register('createIkeOutboundList')
def createIkeOutboundList(deviceId: str):
    return CatalystClient().createIkeOutboundList(**{'deviceId': deviceId})

@register('createIkeSessions')
def createIkeSessions(deviceId: str, **kwargs):
    return CatalystClient().createIkeSessions(**{'deviceId': deviceId, **kwargs})

@register('createCryptov1LocalSAList')
def createCryptov1LocalSAList(deviceId: str, **kwargs):
    return CatalystClient().createCryptov1LocalSAList(**{'deviceId': deviceId, **kwargs})

@register('createCryptov2LocalSAList')
def createCryptov2LocalSAList(deviceId: str):
    return CatalystClient().createCryptov2LocalSAList(**{'deviceId': deviceId})

@register('createInBoundList')
def createInBoundList(deviceId: str, **kwargs):
    return CatalystClient().createInBoundList(**{'deviceId': deviceId, **kwargs})

@register('createLocalSAList')
def createLocalSAList(deviceId: str):
    return CatalystClient().createLocalSAList(**{'deviceId': deviceId})

@register('createOutBoundList')
def createOutBoundList(deviceId: str, **kwargs):
    return CatalystClient().createOutBoundList(**{'deviceId': deviceId, **kwargs})

@register('createIPsecPWKInboundConnections')
def createIPsecPWKInboundConnections(deviceId: str, **kwargs):
    return CatalystClient().createIPsecPWKInboundConnections(**{'deviceId': deviceId, **kwargs})

@register('createIPsecPWKLocalSA')
def createIPsecPWKLocalSA(deviceId: str, **kwargs):
    return CatalystClient().createIPsecPWKLocalSA(**{'deviceId': deviceId, **kwargs})

@register('createIPsecPWKOutboundConnections')
def createIPsecPWKOutboundConnections(deviceId: str, **kwargs):
    return CatalystClient().createIPsecPWKOutboundConnections(**{'deviceId': deviceId, **kwargs})

@register('getIpv6Data')
def getIpv6Data(deviceId: str):
    return CatalystClient().getIpv6Data(**{'deviceId': deviceId})

@register('getDeviceListAsKeyValue')
def getDeviceListAsKeyValue(**kwargs):
    return CatalystClient().getDeviceListAsKeyValue(**{**kwargs})

@register('getLacpInterfaceList')
def getLacpInterfaceList(deviceId: str, **kwargs):
    return CatalystClient().getLacpInterfaceList(**{'deviceId': deviceId, **kwargs})

@register('getLacpMembers')
def getLacpMembers(deviceId: str, **kwargs):
    return CatalystClient().getLacpMembers(**{'deviceId': deviceId, **kwargs})

@register('getLicenseEvalInfo')
def getLicenseEvalInfo(deviceId: str):
    return CatalystClient().getLicenseEvalInfo(**{'deviceId': deviceId})

@register('getLicensePAKInfo')
def getLicensePAKInfo(deviceId: str):
    return CatalystClient().getLicensePAKInfo(**{'deviceId': deviceId})

@register('getLicensePrivacyInfo')
def getLicensePrivacyInfo(deviceId: str):
    return CatalystClient().getLicensePrivacyInfo(**{'deviceId': deviceId})

@register('getLicenseRegInfo')
def getLicenseRegInfo(deviceId: str):
    return CatalystClient().getLicenseRegInfo(**{'deviceId': deviceId})

@register('getLicenseUDIInfo')
def getLicenseUDIInfo(deviceId: str):
    return CatalystClient().getLicenseUDIInfo(**{'deviceId': deviceId})

@register('getLicenseUsageInfo')
def getLicenseUsageInfo(deviceId: str):
    return CatalystClient().getLicenseUsageInfo(**{'deviceId': deviceId})

@register('getLoggingFromDevice')
def getLoggingFromDevice(deviceId: str):
    return CatalystClient().getLoggingFromDevice(**{'deviceId': deviceId})

@register('listAllDeviceModels')
def listAllDeviceModels():
    return CatalystClient().listAllDeviceModels(**{})

@register('getDeviceModels')
def getDeviceModels(uuid: str):
    return CatalystClient().getDeviceModels(**{'uuid': uuid})

@register('listAllMonitorDetailsDevices')
def listAllMonitorDetailsDevices():
    return CatalystClient().listAllMonitorDetailsDevices(**{})

@register('createReplicatorList')
def createReplicatorList(deviceId: str):
    return CatalystClient().createReplicatorList(**{'deviceId': deviceId})

@register('createRpfList')
def createRpfList(deviceId: str):
    return CatalystClient().createRpfList(**{'deviceId': deviceId})

@register('createTopologyList')
def createTopologyList(deviceId: str):
    return CatalystClient().createTopologyList(**{'deviceId': deviceId})

@register('createPimTunnelList')
def createPimTunnelList(deviceId: str):
    return CatalystClient().createPimTunnelList(**{'deviceId': deviceId})

@register('getIpv6Interface')
def getIpv6Interface(deviceId: str, **kwargs):
    return CatalystClient().getIpv6Interface(**{'deviceId': deviceId, **kwargs})

@register('getRunning')
def getRunning(deviceId: str):
    return CatalystClient().getRunning(**{'deviceId': deviceId})

@register('createAssociationsList')
def createAssociationsList(deviceId: str):
    return CatalystClient().createAssociationsList(**{'deviceId': deviceId})

@register('createPeerList')
def createPeerList(deviceId: str):
    return CatalystClient().createPeerList(**{'deviceId': deviceId})

@register('createNTPStatusList')
def createNTPStatusList(deviceId: str):
    return CatalystClient().createNTPStatusList(**{'deviceId': deviceId})

@register('createOMPCloudXRecv')
def createOMPCloudXRecv(deviceId: str):
    return CatalystClient().createOMPCloudXRecv(**{'deviceId': deviceId})

@register('createOMPLinkList')
def createOMPLinkList(state: str):
    return CatalystClient().createOMPLinkList(**{'state': state})

@register('createOMPMcastAutoDiscoverAdvt')
def createOMPMcastAutoDiscoverAdvt(deviceId: str):
    return CatalystClient().createOMPMcastAutoDiscoverAdvt(**{'deviceId': deviceId})

@register('createOMPMcastAutoDiscoverRecv')
def createOMPMcastAutoDiscoverRecv(deviceId: str):
    return CatalystClient().createOMPMcastAutoDiscoverRecv(**{'deviceId': deviceId})

@register('createOMPMcastRoutesAdvt')
def createOMPMcastRoutesAdvt(deviceId: str):
    return CatalystClient().createOMPMcastRoutesAdvt(**{'deviceId': deviceId})

@register('createOMPMcastRoutesRecv')
def createOMPMcastRoutesRecv(deviceId: str):
    return CatalystClient().createOMPMcastRoutesRecv(**{'deviceId': deviceId})

@register('createOMPSessionList')
def createOMPSessionList(deviceId: str):
    return CatalystClient().createOMPSessionList(**{'deviceId': deviceId})

@register('createAdvertisedRoutesList')
def createAdvertisedRoutesList(deviceId: str):
    return CatalystClient().createAdvertisedRoutesList(**{'deviceId': deviceId})

@register('createAdvertisedRoutesListIpv6')
def createAdvertisedRoutesListIpv6(deviceId: str):
    return CatalystClient().createAdvertisedRoutesListIpv6(**{'deviceId': deviceId})

@register('createReceivedRoutesList')
def createReceivedRoutesList(deviceId: str):
    return CatalystClient().createReceivedRoutesList(**{'deviceId': deviceId})

@register('createReceivedRoutesListIpv6')
def createReceivedRoutesListIpv6(deviceId: str):
    return CatalystClient().createReceivedRoutesListIpv6(**{'deviceId': deviceId})

@register('createOMPServices')
def createOMPServices(deviceId: str):
    return CatalystClient().createOMPServices(**{'deviceId': deviceId})

@register('getDeviceOMPStatus')
def getDeviceOMPStatus():
    return CatalystClient().getDeviceOMPStatus(**{})

@register('createOMPSummary')
def createOMPSummary(deviceId: str):
    return CatalystClient().createOMPSummary(**{'deviceId': deviceId})

@register('createSyncedOMPSessionList')
def createSyncedOMPSessionList(deviceId: str):
    return CatalystClient().createSyncedOMPSessionList(**{'deviceId': deviceId})

@register('createAdvertisedTlocsList')
def createAdvertisedTlocsList(deviceId: str):
    return CatalystClient().createAdvertisedTlocsList(**{'deviceId': deviceId})

@register('createReceivedTlocsList')
def createReceivedTlocsList(deviceId: str):
    return CatalystClient().createReceivedTlocsList(**{'deviceId': deviceId})

@register('getOnDemandLocal')
def getOnDemandLocal(deviceId: str):
    return CatalystClient().getOnDemandLocal(**{'deviceId': deviceId})

@register('getOnDemandRemote')
def getOnDemandRemote(deviceId: str):
    return CatalystClient().getOnDemandRemote(**{'deviceId': deviceId})

@register('createConnectionListFromDevice')
def createConnectionListFromDevice(deviceId: str):
    return CatalystClient().createConnectionListFromDevice(**{'deviceId': deviceId})

@register('createConnectionHistoryList')
def createConnectionHistoryList(deviceId: str):
    return CatalystClient().createConnectionHistoryList(**{'deviceId': deviceId})

@register('createLocalPropertiesListList')
def createLocalPropertiesListList(deviceId: str):
    return CatalystClient().createLocalPropertiesListList(**{'deviceId': deviceId})

@register('createReverseProxyMappingList')
def createReverseProxyMappingList(deviceId: str):
    return CatalystClient().createReverseProxyMappingList(**{'deviceId': deviceId})

@register('getStatistics')
def getStatistics(deviceId: str):
    return CatalystClient().getStatistics(**{'deviceId': deviceId})

@register('createConnectionSummary')
def createConnectionSummary(deviceId: str):
    return CatalystClient().createConnectionSummary(**{'deviceId': deviceId})

@register('createValidDevicesList')
def createValidDevicesList(deviceId: str):
    return CatalystClient().createValidDevicesList(**{'deviceId': deviceId})

@register('getValidVManageId')
def getValidVManageId(deviceId: str):
    return CatalystClient().getValidVManageId(**{'deviceId': deviceId})

@register('createValidVSmartsList')
def createValidVSmartsList(deviceId: str):
    return CatalystClient().createValidVSmartsList(**{'deviceId': deviceId})

@register('createOSPFDatabaseList')
def createOSPFDatabaseList(deviceId: str):
    return CatalystClient().createOSPFDatabaseList(**{'deviceId': deviceId})

@register('createOSPFDatabaseExternal')
def createOSPFDatabaseExternal(deviceId: str):
    return CatalystClient().createOSPFDatabaseExternal(**{'deviceId': deviceId})

@register('createOSPFDatabaseSummaryList')
def createOSPFDatabaseSummaryList(deviceId: str):
    return CatalystClient().createOSPFDatabaseSummaryList(**{'deviceId': deviceId})

@register('createOSPFInterface')
def createOSPFInterface(deviceId: str):
    return CatalystClient().createOSPFInterface(**{'deviceId': deviceId})

@register('createOSPFNeighbors')
def createOSPFNeighbors(deviceId: str):
    return CatalystClient().createOSPFNeighbors(**{'deviceId': deviceId})

@register('createOSPFProcess')
def createOSPFProcess(deviceId: str):
    return CatalystClient().createOSPFProcess(**{'deviceId': deviceId})

@register('createOSPFRoutesList')
def createOSPFRoutesList(deviceId: str):
    return CatalystClient().createOSPFRoutesList(**{'deviceId': deviceId})

@register('createOSPFv3Interface')
def createOSPFv3Interface(deviceId: str):
    return CatalystClient().createOSPFv3Interface(**{'deviceId': deviceId})

@register('createOSPFv3Neighbors')
def createOSPFv3Neighbors(deviceId: str):
    return CatalystClient().createOSPFv3Neighbors(**{'deviceId': deviceId})

@register('createPIMInterfaceList')
def createPIMInterfaceList(deviceId: str):
    return CatalystClient().createPIMInterfaceList(**{'deviceId': deviceId})

@register('createPIMNeighborList')
def createPIMNeighborList(deviceId: str):
    return CatalystClient().createPIMNeighborList(**{'deviceId': deviceId})

@register('createPIMRpMappingList')
def createPIMRpMappingList(deviceId: str):
    return CatalystClient().createPIMRpMappingList(**{'deviceId': deviceId})

@register('createPIMStatisticsList')
def createPIMStatisticsList(deviceId: str):
    return CatalystClient().createPIMStatisticsList(**{'deviceId': deviceId})

@register('getDevicePkiTrustpoint')
def getDevicePkiTrustpoint(deviceId: str):
    return CatalystClient().getDevicePkiTrustpoint(**{'deviceId': deviceId})

@register('getPolicedInterface')
def getPolicedInterface(deviceId: str):
    return CatalystClient().getPolicedInterface(**{'deviceId': deviceId})

@register('createPolicyAccessListAssociations')
def createPolicyAccessListAssociations(deviceId: str):
    return CatalystClient().createPolicyAccessListAssociations(**{'deviceId': deviceId})

@register('createPolicyAccessListCounters')
def createPolicyAccessListCounters(deviceId: str):
    return CatalystClient().createPolicyAccessListCounters(**{'deviceId': deviceId})

@register('createPolicyAccessListNames')
def createPolicyAccessListNames(deviceId: str):
    return CatalystClient().createPolicyAccessListNames(**{'deviceId': deviceId})

@register('createPolicyAccessListPolicers')
def createPolicyAccessListPolicers(deviceId: str):
    return CatalystClient().createPolicyAccessListPolicers(**{'deviceId': deviceId})

@register('createPolicyAppRoutePolicyFilter')
def createPolicyAppRoutePolicyFilter(deviceId: str):
    return CatalystClient().createPolicyAppRoutePolicyFilter(**{'deviceId': deviceId})

@register('createPolicDataPolicyFilter')
def createPolicDataPolicyFilter(deviceId: str):
    return CatalystClient().createPolicDataPolicyFilter(**{'deviceId': deviceId})

@register('createPolicyFilterMemoryUsage')
def createPolicyFilterMemoryUsage(deviceId: str):
    return CatalystClient().createPolicyFilterMemoryUsage(**{'deviceId': deviceId})

@register('showVsmartIptoSgtBinding')
def showVsmartIptoSgtBinding(deviceId: str):
    return CatalystClient().showVsmartIptoSgtBinding(**{'deviceId': deviceId})

@register('showVsmartIptoUserBinding')
def showVsmartIptoUserBinding(deviceId: str):
    return CatalystClient().showVsmartIptoUserBinding(**{'deviceId': deviceId})

@register('createPolicyAccessListAssociationsIpv6')
def createPolicyAccessListAssociationsIpv6(deviceId: str):
    return CatalystClient().createPolicyAccessListAssociationsIpv6(**{'deviceId': deviceId})

@register('createPolicyAccessListCountersIpv6')
def createPolicyAccessListCountersIpv6(deviceId: str):
    return CatalystClient().createPolicyAccessListCountersIpv6(**{'deviceId': deviceId})

@register('createPolicyAccessListNamesIpv6')
def createPolicyAccessListNamesIpv6(deviceId: str):
    return CatalystClient().createPolicyAccessListNamesIpv6(**{'deviceId': deviceId})

@register('createPolicyAccessListPolicersIpv6')
def createPolicyAccessListPolicersIpv6(deviceId: str):
    return CatalystClient().createPolicyAccessListPolicersIpv6(**{'deviceId': deviceId})

@register('showVsmartPxGridStatus')
def showVsmartPxGridStatus(deviceId: str):
    return CatalystClient().showVsmartPxGridStatus(**{'deviceId': deviceId})

@register('showVsmartPxGridUserSessions')
def showVsmartPxGridUserSessions(deviceId: str):
    return CatalystClient().showVsmartPxGridUserSessions(**{'deviceId': deviceId})

@register('createPolicQosMapInfo')
def createPolicQosMapInfo(deviceId: str):
    return CatalystClient().createPolicQosMapInfo(**{'deviceId': deviceId})

@register('createPolicQosSchedulerInfo')
def createPolicQosSchedulerInfo(deviceId: str):
    return CatalystClient().createPolicQosSchedulerInfo(**{'deviceId': deviceId})

@register('createPolicyRewriteAssociationsInfo')
def createPolicyRewriteAssociationsInfo(deviceId: str):
    return CatalystClient().createPolicyRewriteAssociationsInfo(**{'deviceId': deviceId})

@register('showVsmartUserUsergroupBindings')
def showVsmartUserUsergroupBindings(deviceId: str):
    return CatalystClient().showVsmartUserUsergroupBindings(**{'deviceId': deviceId})

@register('showSdwanPolicyFromVsmart')
def showSdwanPolicyFromVsmart(deviceId: str):
    return CatalystClient().showSdwanPolicyFromVsmart(**{'deviceId': deviceId})

@register('getZoneDropStatistics')
def getZoneDropStatistics(deviceId: str):
    return CatalystClient().getZoneDropStatistics(**{'deviceId': deviceId})

@register('getZbfwStatistics')
def getZbfwStatistics(deviceId: str):
    return CatalystClient().getZbfwStatistics(**{'deviceId': deviceId})

@register('getZonePairSessions')
def getZonePairSessions(deviceId: str):
    return CatalystClient().getZonePairSessions(**{'deviceId': deviceId})

@register('getZonePairs')
def getZonePairs(deviceId: str):
    return CatalystClient().getZonePairs(**{'deviceId': deviceId})

@register('getZonePolicyFilters')
def getZonePolicyFilters(deviceId: str):
    return CatalystClient().getZonePolicyFilters(**{'deviceId': deviceId})

@register('getPowerConsumption')
def getPowerConsumption(deviceId: str):
    return CatalystClient().getPowerConsumption(**{'deviceId': deviceId})

@register('createPPPInterfaceList')
def createPPPInterfaceList(deviceId: str):
    return CatalystClient().createPPPInterfaceList(**{'deviceId': deviceId})

@register('createPPPoEInterfaceList')
def createPPPoEInterfaceList(deviceId: str):
    return CatalystClient().createPPPoEInterfaceList(**{'deviceId': deviceId})

@register('createPPPoENeighborList')
def createPPPoENeighborList(deviceId: str):
    return CatalystClient().createPPPoENeighborList(**{'deviceId': deviceId})

@register('cpustat')
def cpustat(deviceId: str):
    return CatalystClient().cpustat(**{'deviceId': deviceId})

@register('memstat')
def memstat(deviceId: str):
    return CatalystClient().memstat(**{'deviceId': deviceId})

@register('getSyncQueues')
def getSyncQueues():
    return CatalystClient().getSyncQueues(**{})

@register('listReachableDevices')
def listReachableDevices():
    return CatalystClient().listReachableDevices(**{})

@register('createRebootHistoryList')
def createRebootHistoryList(deviceId: str):
    return CatalystClient().createRebootHistoryList(**{'deviceId': deviceId})

@register('getRebootHistoryDetails')
def getRebootHistoryDetails():
    return CatalystClient().getRebootHistoryDetails(**{})

@register('createSyncedRebootHistoryList')
def createSyncedRebootHistoryList(deviceId: str):
    return CatalystClient().createSyncedRebootHistoryList(**{'deviceId': deviceId})

@register('getRedundancyGroupAppGroup')
def getRedundancyGroupAppGroup(deviceId: str):
    return CatalystClient().getRedundancyGroupAppGroup(**{'deviceId': deviceId})

@register('getRoleBasedCounters')
def getRoleBasedCounters(deviceId: str):
    return CatalystClient().getRoleBasedCounters(**{'deviceId': deviceId})

@register('getRoleBasedIpv6Counters')
def getRoleBasedIpv6Counters(deviceId: str):
    return CatalystClient().getRoleBasedIpv6Counters(**{'deviceId': deviceId})

@register('getRoleBasedIpv6Permissions')
def getRoleBasedIpv6Permissions(deviceId: str):
    return CatalystClient().getRoleBasedIpv6Permissions(**{'deviceId': deviceId})

@register('getRoleBasedPermissions')
def getRoleBasedPermissions(deviceId: str):
    return CatalystClient().getRoleBasedPermissions(**{'deviceId': deviceId})

@register('getRoleBasedSgtMap')
def getRoleBasedSgtMap(deviceId: str):
    return CatalystClient().getRoleBasedSgtMap(**{'deviceId': deviceId})

@register('getSDWanGlobalDropStatistics')
def getSDWanGlobalDropStatistics(deviceId: str):
    return CatalystClient().getSDWanGlobalDropStatistics(**{'deviceId': deviceId})

@register('getSDWanStats')
def getSDWanStats(deviceId: str):
    return CatalystClient().getSDWanStats(**{'deviceId': deviceId})

@register('createSessionList')
def createSessionList(deviceId: str):
    return CatalystClient().createSessionList(**{'deviceId': deviceId})

@register('getDetail')
def getDetail(deviceId: str, **kwargs):
    return CatalystClient().getDetail(**{'deviceId': deviceId, **kwargs})

@register('getDiagnostic')
def getDiagnostic(deviceId: str, **kwargs):
    return CatalystClient().getDiagnostic(**{'deviceId': deviceId, **kwargs})

@register('getDiagnosticMeasurementAlarm')
def getDiagnosticMeasurementAlarm(deviceId: str, **kwargs):
    return CatalystClient().getDiagnosticMeasurementAlarm(**{'deviceId': deviceId, **kwargs})

@register('getDiagnosticMeasurementValue')
def getDiagnosticMeasurementValue(deviceId: str, **kwargs):
    return CatalystClient().getDiagnosticMeasurementValue(**{'deviceId': deviceId, **kwargs})

@register('getSigTunnelList')
def getSigTunnelList(**kwargs):
    return CatalystClient().getSigTunnelList(**{**kwargs})

@register('getSigTunnelTotal')
def getSigTunnelTotal():
    return CatalystClient().getSigTunnelTotal(**{})

@register('tunnelDashboard')
def tunnelDashboard():
    return CatalystClient().tunnelDashboard(**{})

@register('getSigUmbrellaTunnels')
def getSigUmbrellaTunnels(deviceId: str):
    return CatalystClient().getSigUmbrellaTunnels(**{'deviceId': deviceId})

@register('getSigZscalerTunnels')
def getSigZscalerTunnels(deviceId: str):
    return CatalystClient().getSigZscalerTunnels(**{'deviceId': deviceId})

@register('createSmuList')
def createSmuList(deviceId: str):
    return CatalystClient().createSmuList(**{'deviceId': deviceId})

@register('createSyncedSmuList')
def createSyncedSmuList(deviceId: str):
    return CatalystClient().createSyncedSmuList(**{'deviceId': deviceId})

@register('getAAAUcreateSoftwareListsers')
def getAAAUcreateSoftwareListsers(deviceId: str):
    return CatalystClient().getAAAUcreateSoftwareListsers(**{'deviceId': deviceId})

@register('createSyncedSoftwareList')
def createSyncedSoftwareList(deviceId: str):
    return CatalystClient().createSyncedSoftwareList(**{'deviceId': deviceId})

@register('getSSETunnel')
def getSSETunnel(deviceId: str):
    return CatalystClient().getSSETunnel(**{'deviceId': deviceId})

@register('getSslProxyStatistics')
def getSslProxyStatistics(deviceId: str):
    return CatalystClient().getSslProxyStatistics(**{'deviceId': deviceId})

@register('getSslProxyStatus')
def getSslProxyStatus(deviceId: str):
    return CatalystClient().getSslProxyStatus(**{'deviceId': deviceId})

@register('getStaticRouteTrackerInfo')
def getStaticRouteTrackerInfo(deviceId: str):
    return CatalystClient().getStaticRouteTrackerInfo(**{'deviceId': deviceId})

@register('getStatsQueues')
def getStatsQueues():
    return CatalystClient().getStatsQueues(**{})

@register('getAllDeviceStatus')
def getAllDeviceStatus():
    return CatalystClient().getAllDeviceStatus(**{})

@register('getSxpConnections')
def getSxpConnections(deviceId: str):
    return CatalystClient().getSxpConnections(**{'deviceId': deviceId})

@register('listCurrentlySyncingDevices')
def listCurrentlySyncingDevices(groupId: str):
    return CatalystClient().listCurrentlySyncingDevices(**{'groupId': groupId})

@register('getDeviceSystemClock')
def getDeviceSystemClock(deviceId: str):
    return CatalystClient().getDeviceSystemClock(**{'deviceId': deviceId})

@register('createDeviceInfoList')
def createDeviceInfoList(deviceId: list):
    return CatalystClient().createDeviceInfoList(**{'deviceId': deviceId})

@register('createDeviceSystemStatsList')
def createDeviceSystemStatsList(deviceId: str):
    return CatalystClient().createDeviceSystemStatsList(**{'deviceId': deviceId})

@register('createDeviceSystemStatusList')
def createDeviceSystemStatusList(deviceId: str):
    return CatalystClient().createDeviceSystemStatusList(**{'deviceId': deviceId})

@register('createSyncedDeviceSystemStatusList')
def createSyncedDeviceSystemStatusList(deviceId: str):
    return CatalystClient().createSyncedDeviceSystemStatusList(**{'deviceId': deviceId})

@register('getActiveTCPFlows')
def getActiveTCPFlows(deviceId: str):
    return CatalystClient().getActiveTCPFlows(**{'deviceId': deviceId})

@register('getExpiredTCPFlows')
def getExpiredTCPFlows(deviceId: str):
    return CatalystClient().getExpiredTCPFlows(**{'deviceId': deviceId})

@register('getTCPSummary')
def getTCPSummary(deviceId: str):
    return CatalystClient().getTCPSummary(**{'deviceId': deviceId})

@register('getTcpProxyStatistics')
def getTcpProxyStatistics(deviceId: str):
    return CatalystClient().getTcpProxyStatistics(**{'deviceId': deviceId})

@register('getTcpProxyStatus')
def getTcpProxyStatus(deviceId: str):
    return CatalystClient().getTcpProxyStatus(**{'deviceId': deviceId})

@register('getTiers')
def getTiers():
    return CatalystClient().getTiers(**{})

@register('getDeviceTlocStatus')
def getDeviceTlocStatus(**kwargs):
    return CatalystClient().getDeviceTlocStatus(**{**kwargs})

@register('getDeviceTlocUtil')
def getDeviceTlocUtil(**kwargs):
    return CatalystClient().getDeviceTlocUtil(**{**kwargs})

@register('getDeviceTlocUtilDetails')
def getDeviceTlocUtilDetails(**kwargs):
    return CatalystClient().getDeviceTlocUtilDetails(**{**kwargs})

@register('downloadAdminTechFile')
def downloadAdminTechFile(filename: str):
    return CatalystClient().downloadAdminTechFile(**{'filename': filename})

@register('getSupportedAdminTechFeatures')
def getSupportedAdminTechFeatures(deviceIP: str, deviceModel: str, personality: str):
    return CatalystClient().getSupportedAdminTechFeatures(**{'deviceIP': deviceIP, 'deviceModel': deviceModel, 'personality': personality})

@register('listAdminTechs')
def listAdminTechs():
    return CatalystClient().listAdminTechs(**{})

@register('getInProgressCount')
def getInProgressCount():
    return CatalystClient().getInProgressCount(**{})

@register('getDeviceToolsNetstat')
def getDeviceToolsNetstat(deviceId: str, **kwargs):
    return CatalystClient().getDeviceToolsNetstat(**{'deviceId': deviceId, **kwargs})

@register('getDeviceToolsNSlookup')
def getDeviceToolsNSlookup(deviceId: str, dns: str, vpn: str):
    return CatalystClient().getDeviceToolsNSlookup(**{'deviceId': deviceId, 'dns': dns, 'vpn': vpn})

@register('getRealTimeinfo')
def getRealTimeinfo(deviceId: str):
    return CatalystClient().getRealTimeinfo(**{'deviceId': deviceId})

@register('getDeviceToolsSS')
def getDeviceToolsSS(deviceId: str, **kwargs):
    return CatalystClient().getDeviceToolsSS(**{'deviceId': deviceId, **kwargs})

@register('getSystemNetfilter')
def getSystemNetfilter(deviceId: str):
    return CatalystClient().getSystemNetfilter(**{'deviceId': deviceId})

@register('createTransportConnectionList')
def createTransportConnectionList(deviceId: str):
    return CatalystClient().createTransportConnectionList(**{'deviceId': deviceId})

@register('createBfdStatisticsList')
def createBfdStatisticsList(deviceId: str):
    return CatalystClient().createBfdStatisticsList(**{'deviceId': deviceId})

@register('createFecStatistics')
def createFecStatistics(deviceId: str):
    return CatalystClient().createFecStatistics(**{'deviceId': deviceId})

@register('createGreKeepalivesList')
def createGreKeepalivesList(deviceId: str):
    return CatalystClient().createGreKeepalivesList(**{'deviceId': deviceId})

@register('createIpsecStatisticsList')
def createIpsecStatisticsList(deviceId: str):
    return CatalystClient().createIpsecStatisticsList(**{'deviceId': deviceId})

@register('createPacketDuplicateStatistics')
def createPacketDuplicateStatistics(deviceId: str):
    return CatalystClient().createPacketDuplicateStatistics(**{'deviceId': deviceId})

@register('createStatisticsList')
def createStatisticsList(deviceId: str):
    return CatalystClient().createStatisticsList(**{'deviceId': deviceId})

@register('createUcseStats')
def createUcseStats(deviceId: str, **kwargs):
    return CatalystClient().createUcseStats(**{'deviceId': deviceId, **kwargs})

@register('getUmbrellaDevReg')
def getUmbrellaDevReg(deviceId: str):
    return CatalystClient().getUmbrellaDevReg(**{'deviceId': deviceId})

@register('getUmbrellaDNSCrypt')
def getUmbrellaDNSCrypt(deviceId: str):
    return CatalystClient().getUmbrellaDNSCrypt(**{'deviceId': deviceId})

@register('getUmbrellaDpStats')
def getUmbrellaDpStats(deviceId: str):
    return CatalystClient().getUmbrellaDpStats(**{'deviceId': deviceId})

@register('getUmbrellaOverview')
def getUmbrellaOverview(deviceId: str):
    return CatalystClient().getUmbrellaOverview(**{'deviceId': deviceId})

@register('getUmbrellaConfig')
def getUmbrellaConfig(deviceId: str):
    return CatalystClient().getUmbrellaConfig(**{'deviceId': deviceId})

@register('getUnclaimedVedges')
def getUnclaimedVedges(deviceId: str):
    return CatalystClient().getUnclaimedVedges(**{'deviceId': deviceId})

@register('getUnconfigured')
def getUnconfigured():
    return CatalystClient().getUnconfigured(**{})

@register('listUnreachableDevices')
def listUnreachableDevices(personality: str):
    return CatalystClient().listUnreachableDevices(**{'personality': personality})

@register('getUsersFromDevice')
def getUsersFromDevice(deviceId: str):
    return CatalystClient().getUsersFromDevice(**{'deviceId': deviceId})

@register('getAllDeviceUsers')
def getAllDeviceUsers(deviceId: str):
    return CatalystClient().getAllDeviceUsers(**{'deviceId': deviceId})

@register('getUTDDataplaneConfig')
def getUTDDataplaneConfig(deviceId: str):
    return CatalystClient().getUTDDataplaneConfig(**{'deviceId': deviceId})

@register('getUTDDataplaneGlobal')
def getUTDDataplaneGlobal(deviceId: str):
    return CatalystClient().getUTDDataplaneGlobal(**{'deviceId': deviceId})

@register('getUTDDataplaneStats')
def getUTDDataplaneStats(deviceId: str):
    return CatalystClient().getUTDDataplaneStats(**{'deviceId': deviceId})

@register('getUTDDataplaneStatsSummary')
def getUTDDataplaneStatsSummary(deviceId: str):
    return CatalystClient().getUTDDataplaneStatsSummary(**{'deviceId': deviceId})

@register('getUTDEngineInstanceStatus')
def getUTDEngineInstanceStatus(deviceId: str):
    return CatalystClient().getUTDEngineInstanceStatus(**{'deviceId': deviceId})

@register('getUTDEngineStatus')
def getUTDEngineStatus(deviceId: str):
    return CatalystClient().getUTDEngineStatus(**{'deviceId': deviceId})

@register('getUTDFileAnalysisStatus')
def getUTDFileAnalysisStatus(deviceId: str):
    return CatalystClient().getUTDFileAnalysisStatus(**{'deviceId': deviceId})

@register('getUTDFileReputationStatus')
def getUTDFileReputationStatus(deviceId: str):
    return CatalystClient().getUTDFileReputationStatus(**{'deviceId': deviceId})

@register('getUTDIpsUpdateStatus')
def getUTDIpsUpdateStatus(deviceId: str):
    return CatalystClient().getUTDIpsUpdateStatus(**{'deviceId': deviceId})

@register('getSignatureVersionInfo')
def getSignatureVersionInfo(deviceId: str):
    return CatalystClient().getSignatureVersionInfo(**{'deviceId': deviceId})

@register('getUTDUrlfConnectionStatus')
def getUTDUrlfConnectionStatus(deviceId: str):
    return CatalystClient().getUTDUrlfConnectionStatus(**{'deviceId': deviceId})

@register('getUTDUrlfUpdateStatus')
def getUTDUrlfUpdateStatus(deviceId: str):
    return CatalystClient().getUTDUrlfUpdateStatus(**{'deviceId': deviceId})

@register('getUTDVersionStatus')
def getUTDVersionStatus(deviceId: str):
    return CatalystClient().getUTDVersionStatus(**{'deviceId': deviceId})

@register('getCoLineSpecificStats')
def getCoLineSpecificStats(deviceId: str):
    return CatalystClient().getCoLineSpecificStats(**{'deviceId': deviceId})

@register('getCoStats')
def getCoStats(deviceId: str):
    return CatalystClient().getCoStats(**{'deviceId': deviceId})

@register('getCpeLineSpecificStats')
def getCpeLineSpecificStats(deviceId: str):
    return CatalystClient().getCpeLineSpecificStats(**{'deviceId': deviceId})

@register('getCpeStats')
def getCpeStats(deviceId: str):
    return CatalystClient().getCpeStats(**{'deviceId': deviceId})

@register('getLineBondingStats')
def getLineBondingStats(deviceId: str):
    return CatalystClient().getLineBondingStats(**{'deviceId': deviceId})

@register('getLineSpecificStats')
def getLineSpecificStats(deviceId: str):
    return CatalystClient().getLineSpecificStats(**{'deviceId': deviceId})

@register('getVdslInfo')
def getVdslInfo(deviceId: str):
    return CatalystClient().getVdslInfo(**{'deviceId': deviceId})

@register('getVedgeInventory')
def getVedgeInventory(**kwargs):
    return CatalystClient().getVedgeInventory(**{**kwargs})

@register('getVedgeInventorySummary')
def getVedgeInventorySummary():
    return CatalystClient().getVedgeInventorySummary(**{})

@register('createTeList')
def createTeList(deviceId: str):
    return CatalystClient().createTeList(**{'deviceId': deviceId})

@register('createUtdList')
def createUtdList(deviceId: str):
    return CatalystClient().createUtdList(**{'deviceId': deviceId})

@register('createWaasList')
def createWaasList(deviceId: str):
    return CatalystClient().createWaasList(**{'deviceId': deviceId})

@register('getVbranchVMLifecycleNics')
def getVbranchVMLifecycleNics(deviceId: str):
    return CatalystClient().getVbranchVMLifecycleNics(**{'deviceId': deviceId})

@register('getCloudDockVMLifecycleNics')
def getCloudDockVMLifecycleNics(userGroup: str):
    return CatalystClient().getCloudDockVMLifecycleNics(**{'userGroup': userGroup})

@register('getVbranchVMLifecycle')
def getVbranchVMLifecycle(deviceId: str):
    return CatalystClient().getVbranchVMLifecycle(**{'deviceId': deviceId})

@register('getVMLifeCycleState')
def getVMLifeCycleState(deviceId: str):
    return CatalystClient().getVMLifeCycleState(**{'deviceId': deviceId})

@register('getVManageSystemIP')
def getVManageSystemIP():
    return CatalystClient().getVManageSystemIP(**{})

@register('getDspActive')
def getDspActive(deviceId: str):
    return CatalystClient().getDspActive(**{'deviceId': deviceId})

@register('getPhoneInfo')
def getPhoneInfo(deviceId: str):
    return CatalystClient().getPhoneInfo(**{'deviceId': deviceId})

@register('getDSPFarmProfiles')
def getDSPFarmProfiles(deviceId: str):
    return CatalystClient().getDSPFarmProfiles(**{'deviceId': deviceId})

@register('getSccpCcmGroups')
def getSccpCcmGroups(deviceId: str):
    return CatalystClient().getSccpCcmGroups(**{'deviceId': deviceId})

@register('getSccpConnections')
def getSccpConnections(deviceId: str):
    return CatalystClient().getSccpConnections(**{'deviceId': deviceId})

@register('getVoiceCalls')
def getVoiceCalls(deviceId: str):
    return CatalystClient().getVoiceCalls(**{'deviceId': deviceId})

@register('getVoipCalls')
def getVoipCalls(deviceId: str):
    return CatalystClient().getVoipCalls(**{'deviceId': deviceId})

@register('getT1e1IsdnStatus')
def getT1e1IsdnStatus(deviceId: str):
    return CatalystClient().getT1e1IsdnStatus(**{'deviceId': deviceId})

@register('getControllerT1e1InfoCurrent15MinStats')
def getControllerT1e1InfoCurrent15MinStats(deviceId: str):
    return CatalystClient().getControllerT1e1InfoCurrent15MinStats(**{'deviceId': deviceId})

@register('getControllerT1e1InfoTotalStats')
def getControllerT1e1InfoTotalStats(deviceId: str):
    return CatalystClient().getControllerT1e1InfoTotalStats(**{'deviceId': deviceId})

@register('getVPNInstances')
def getVPNInstances(deviceId: str):
    return CatalystClient().getVPNInstances(**{'deviceId': deviceId})

@register('getVRRPInterface')
def getVRRPInterface(deviceId: str):
    return CatalystClient().getVRRPInterface(**{'deviceId': deviceId})

@register('getWirelessClients')
def getWirelessClients(deviceId: str):
    return CatalystClient().getWirelessClients(**{'deviceId': deviceId})

@register('getWirelessRadios')
def getWirelessRadios(deviceId: str):
    return CatalystClient().getWirelessRadios(**{'deviceId': deviceId})

@register('getWirelessSsid')
def getWirelessSsid(deviceId: str):
    return CatalystClient().getWirelessSsid(**{'deviceId': deviceId})

@register('getWLANClients')
def getWLANClients(deviceId: str):
    return CatalystClient().getWLANClients(**{'deviceId': deviceId})

@register('getWLANInterfaces')
def getWLANInterfaces(deviceId: str):
    return CatalystClient().getWLANInterfaces(**{'deviceId': deviceId})

@register('getWLANRadios')
def getWLANRadios(deviceId: str):
    return CatalystClient().getWLANRadios(**{'deviceId': deviceId})

@register('getWLANRadius')
def getWLANRadius(deviceId: str):
    return CatalystClient().getWLANRadius(**{'deviceId': deviceId})

@register('getClusterInfo')
def getClusterInfo():
    return CatalystClient().getClusterInfo(**{})

@register('getConfigDBRestoreStatus')
def getConfigDBRestoreStatus():
    return CatalystClient().getConfigDBRestoreStatus(**{})

@register('getDetails')
def getDetails():
    return CatalystClient().getDetails(**{})

@register('getDisasterRecoveryStatus')
def getDisasterRecoveryStatus():
    return CatalystClient().getDisasterRecoveryStatus(**{})

@register('getHistory')
def getHistory():
    return CatalystClient().getHistory(**{})

@register('getLocalHistory')
def getLocalHistory():
    return CatalystClient().getLocalHistory(**{})

@register('getLocalDataCenterState')
def getLocalDataCenterState():
    return CatalystClient().getLocalDataCenterState(**{})

@register('getRemoteDCMembersState')
def getRemoteDCMembersState():
    return CatalystClient().getRemoteDCMembersState(**{})

@register('getRemoteDataCenterState')
def getRemoteDataCenterState():
    return CatalystClient().getRemoteDataCenterState(**{})

@register('getRemoteDataCenterVersion')
def getRemoteDataCenterVersion():
    return CatalystClient().getRemoteDataCenterVersion(**{})

@register('getDisasterRecoveryLocalReplicationSchedule')
def getDisasterRecoveryLocalReplicationSchedule():
    return CatalystClient().getDisasterRecoveryLocalReplicationSchedule(**{})

@register('getdrStatus')
def getdrStatus():
    return CatalystClient().getdrStatus(**{})

@register('get')
def get():
    return CatalystClient().get(**{})

@register('listEntityOwnershipInfo')
def listEntityOwnershipInfo():
    return CatalystClient().listEntityOwnershipInfo(**{})

@register('entityOwnershipInfo')
def entityOwnershipInfo():
    return CatalystClient().entityOwnershipInfo(**{})

@register('getEvents')
def getEvents(**kwargs):
    return CatalystClient().getEvents(**{**kwargs})

@register('getAggregationData_1')
def getAggregationData_1(query: str, **kwargs):
    return CatalystClient().getAggregationData_1(**{'query': query, **kwargs})

@register('getComponentsAsKeyValue')
def getComponentsAsKeyValue():
    return CatalystClient().getComponentsAsKeyValue(**{})

@register('getDocCount_2')
def getDocCount_2(query: str, **kwargs):
    return CatalystClient().getDocCount_2(**{'query': query, **kwargs})

@register('enableEventsFromFile')
def enableEventsFromFile():
    return CatalystClient().enableEventsFromFile(**{})

@register('getEventNamesByComponent')
def getEventNamesByComponent(query: str):
    return CatalystClient().getEventNamesByComponent(**{'query': query})

@register('getListenersInfo')
def getListenersInfo():
    return CatalystClient().getListenersInfo(**{})

@register('getPage_1')
def getPage_1(**kwargs):
    return CatalystClient().getPage_1(**{**kwargs})

@register('getQueryFields')
def getQueryFields():
    return CatalystClient().getQueryFields(**{})

@register('createEventsQueryConfig')
def createEventsQueryConfig():
    return CatalystClient().createEventsQueryConfig(**{})

@register('getBySeverities')
def getBySeverities(severity_level: list, **kwargs):
    return CatalystClient().getBySeverities(**{'severity-level': severity_level, **kwargs})

@register('getSeverityHistogram')
def getSeverityHistogram(deviceId: list, **kwargs):
    return CatalystClient().getSeverityHistogram(**{'deviceId': deviceId, **kwargs})

@register('getEventTypesAsKeyValue')
def getEventTypesAsKeyValue():
    return CatalystClient().getEventTypesAsKeyValue(**{})

@register('getDeviceCertificate')
def getDeviceCertificate(deviceId: str):
    return CatalystClient().getDeviceCertificate(**{'deviceId': deviceId})

@register('getDeviceCsr')
def getDeviceCsr(deviceId: str):
    return CatalystClient().getDeviceCsr(**{'deviceId': deviceId})

@register('getFeatureCaState')
def getFeatureCaState():
    return CatalystClient().getFeatureCaState(**{})

@register('requesDNSSecActions')
def requesDNSSecActions(action: str):
    return CatalystClient().requesDNSSecActions(**{'action': action})

@register('getDNSSecStatus')
def getDNSSecStatus():
    return CatalystClient().getDNSSecStatus(**{})

@register('requestWazuhActions')
def requestWazuhActions(**kwargs):
    return CatalystClient().requestWazuhActions(**{**kwargs})

@register('getWazuhAgentStatus')
def getWazuhAgentStatus():
    return CatalystClient().getWazuhAgentStatus(**{})

@register('listDeviceGroupList')
def listDeviceGroupList():
    return CatalystClient().listDeviceGroupList(**{})

@register('listDeviceGroups')
def listDeviceGroups(**kwargs):
    return CatalystClient().listDeviceGroups(**{**kwargs})

@register('listGroupDevices')
def listGroupDevices(**kwargs):
    return CatalystClient().listGroupDevices(**{**kwargs})

@register('listGroupDevicesForMap')
def listGroupDevicesForMap(**kwargs):
    return CatalystClient().listGroupDevicesForMap(**{**kwargs})

@register('listGroupLinksForMap')
def listGroupLinksForMap(**kwargs):
    return CatalystClient().listGroupLinksForMap(**{**kwargs})

@register('getDevicesHealth')
def getDevicesHealth(**kwargs):
    return CatalystClient().getDevicesHealth(**{**kwargs})

@register('getDevicesHealthOverview')
def getDevicesHealthOverview(**kwargs):
    return CatalystClient().getDevicesHealthOverview(**{**kwargs})

@register('fetchDeviceDetails')
def fetchDeviceDetails():
    return CatalystClient().fetchDeviceDetails(**{})

@register('InstallDeviceDetails')
def InstallDeviceDetails():
    return CatalystClient().InstallDeviceDetails(**{})

@register('fetchSAVAAccounts')
def fetchSAVAAccounts(**kwargs):
    return CatalystClient().fetchSAVAAccounts(**{**kwargs})

@register('testbedMode')
def testbedMode():
    return CatalystClient().testbedMode(**{})

@register('connect_1')
def connect_1():
    return CatalystClient().connect_1(**{})

@register('getIseServerCredentials')
def getIseServerCredentials():
    return CatalystClient().getIseServerCredentials(**{})

@register('getPxGridAccount')
def getPxGridAccount():
    return CatalystClient().getPxGridAccount(**{})

@register('getPxgridCert')
def getPxgridCert():
    return CatalystClient().getPxgridCert(**{})

@register('getSupportedLocales')
def getSupportedLocales():
    return CatalystClient().getSupportedLocales(**{})

@register('getCategory')
def getCategory():
    return CatalystClient().getCategory(**{})

@register('getvManageResourceUtilization')
def getvManageResourceUtilization():
    return CatalystClient().getvManageResourceUtilization(**{})

@register('retrieveMDPAttachedDevices')
def retrieveMDPAttachedDevices(nmsId: str):
    return CatalystClient().retrieveMDPAttachedDevices(**{'nmsId': nmsId})

@register('retrieveMDPSupportedDevices')
def retrieveMDPSupportedDevices(nmsId: str):
    return CatalystClient().retrieveMDPSupportedDevices(**{'nmsId': nmsId})

@register('disconnectFromMDP')
def disconnectFromMDP(nmsId: str):
    return CatalystClient().disconnectFromMDP(**{'nmsId': nmsId})

@register('getMDPOnboardingStatus')
def getMDPOnboardingStatus():
    return CatalystClient().getMDPOnboardingStatus(**{})

@register('retrieveMDPConfigObject')
def retrieveMDPConfigObject(deviceId: str):
    return CatalystClient().retrieveMDPConfigObject(**{'deviceId': deviceId})

@register('retrieveMDPPolicies')
def retrieveMDPPolicies(nmsId: str):
    return CatalystClient().retrieveMDPPolicies(**{'nmsId': nmsId})

@register('createDeviceVmanageConnectionList')
def createDeviceVmanageConnectionList():
    return CatalystClient().createDeviceVmanageConnectionList(**{})

@register('getCloudConnectorDomainAppRules')
def getCloudConnectorDomainAppRules():
    return CatalystClient().getCloudConnectorDomainAppRules(**{})

@register('getCloudConnectorIpAddressAppRules')
def getCloudConnectorIpAddressAppRules():
    return CatalystClient().getCloudConnectorIpAddressAppRules(**{})

@register('getWebexAppData')
def getWebexAppData():
    return CatalystClient().getWebexAppData(**{})

@register('getMSLADevices_1')
def getMSLADevices_1(**kwargs):
    return CatalystClient().getMSLADevices_1(**{**kwargs})

@register('getLicenseByUuid_1')
def getLicenseByUuid_1(uuid: str):
    return CatalystClient().getLicenseByUuid_1(**{'uuid': uuid})

@register('getMslaLicenses')
def getMslaLicenses(**kwargs):
    return CatalystClient().getMslaLicenses(**{**kwargs})

@register('getLicensesCompliance')
def getLicensesCompliance():
    return CatalystClient().getLicensesCompliance(**{})

@register('getDeviceDetailsForDashboard')
def getDeviceDetailsForDashboard():
    return CatalystClient().getDeviceDetailsForDashboard(**{})

@register('getLicenseDistributionDetails')
def getLicenseDistributionDetails():
    return CatalystClient().getLicenseDistributionDetails(**{})

@register('getPackagingDistributionDetails')
def getPackagingDistributionDetails():
    return CatalystClient().getPackagingDistributionDetails(**{})

@register('getAllTemplate')
def getAllTemplate():
    return CatalystClient().getAllTemplate(**{})

@register('getSubscriptions')
def getSubscriptions(**kwargs):
    return CatalystClient().getSubscriptions(**{**kwargs})

@register('getAllCloudAccounts')
def getAllCloudAccounts(**kwargs):
    return CatalystClient().getAllCloudAccounts(**{**kwargs})

@register('getEdgeAccounts')
def getEdgeAccounts(**kwargs):
    return CatalystClient().getEdgeAccounts(**{**kwargs})

@register('getEdgeAccountDetails')
def getEdgeAccountDetails(accountId: str):
    return CatalystClient().getEdgeAccountDetails(**{'accountId': accountId})

@register('getCloudAccountDetails')
def getCloudAccountDetails(accountId: str):
    return CatalystClient().getCloudAccountDetails(**{'accountId': accountId})

@register('auditDryRun')
def auditDryRun(cloudType: str, **kwargs):
    return CatalystClient().auditDryRun(**{'cloudType': cloudType, **kwargs})

@register('getEdgeBillingAccounts')
def getEdgeBillingAccounts(edgeAccountId: str, edgeType: str, **kwargs):
    return CatalystClient().getEdgeBillingAccounts(**{'edgeAccountId': edgeAccountId, 'edgeType': edgeType, **kwargs})

@register('getCloudRoutersAndAttachments')
def getCloudRoutersAndAttachments(**kwargs):
    return CatalystClient().getCloudRoutersAndAttachments(**{**kwargs})

@register('getCgws')
def getCgws(**kwargs):
    return CatalystClient().getCgws(**{**kwargs})

@register('getNvaSecurityRules')
def getNvaSecurityRules(cloudGatewayName: str):
    return CatalystClient().getNvaSecurityRules(**{'cloudGatewayName': cloudGatewayName})

@register('getAzureNetworkVirtualAppliances')
def getAzureNetworkVirtualAppliances(accountId: str, cloudType: str, region: str, resourceGroupName: str, resourceGroupSource: str, vhubName: str, vhubSource: str):
    return CatalystClient().getAzureNetworkVirtualAppliances(**{'accountId': accountId, 'cloudType': cloudType, 'region': region, 'resourceGroupName': resourceGroupName, 'resourceGroupSource': resourceGroupSource, 'vhubName': vhubName, 'vhubSource': vhubSource})

@register('getAzureNvaSkuResources')
def getAzureNvaSkuResources(cloudType: str):
    return CatalystClient().getAzureNvaSkuResources(**{'cloudType': cloudType})

@register('getCgwOrgResources')
def getCgwOrgResources(cloudGatewayName: str):
    return CatalystClient().getCgwOrgResources(**{'cloudGatewayName': cloudGatewayName})

@register('getAzureResourceGroups')
def getAzureResourceGroups(accountId: str, cloudType: str):
    return CatalystClient().getAzureResourceGroups(**{'accountId': accountId, 'cloudType': cloudType})

@register('getAzureVirtualHubs')
def getAzureVirtualHubs(accountId: str, cloudType: str, region: str, resourceGroupName: str, resourceGroupSource: str, vwanName: str, vwanSource: str):
    return CatalystClient().getAzureVirtualHubs(**{'accountId': accountId, 'cloudType': cloudType, 'region': region, 'resourceGroupName': resourceGroupName, 'resourceGroupSource': resourceGroupSource, 'vwanName': vwanName, 'vwanSource': vwanSource})

@register('getAzureVirtualVnetsAttached')
def getAzureVirtualVnetsAttached(cloudGatewayName: str, cloudType: str):
    return CatalystClient().getAzureVirtualVnetsAttached(**{'cloudGatewayName': cloudGatewayName, 'cloudType': cloudType})

@register('getAzureVpnGateways')
def getAzureVpnGateways(accountId: str, cloudType: str, region: str, resourceGroupName: str, resourceGroupSource: str, vhubName: str, vhubSource: str):
    return CatalystClient().getAzureVpnGateways(**{'accountId': accountId, 'cloudType': cloudType, 'region': region, 'resourceGroupName': resourceGroupName, 'resourceGroupSource': resourceGroupSource, 'vhubName': vhubName, 'vhubSource': vhubSource})

@register('getAzureVirtualWans')
def getAzureVirtualWans(accountId: str, cloudType: str, resourceGroupName: str, resourceGroupSource: str):
    return CatalystClient().getAzureVirtualWans(**{'accountId': accountId, 'cloudType': cloudType, 'resourceGroupName': resourceGroupName, 'resourceGroupSource': resourceGroupSource})

@register('getCgwDetails')
def getCgwDetails(cloudGatewayName: str):
    return CatalystClient().getCgwDetails(**{'cloudGatewayName': cloudGatewayName})

@register('getCgwAttachedSites')
def getCgwAttachedSites(cloudGatewayName: str, **kwargs):
    return CatalystClient().getCgwAttachedSites(**{'cloudGatewayName': cloudGatewayName, **kwargs})

@register('getAvailableDevicesOrByCGId')
def getAvailableDevicesOrByCGId(cloudType: str, **kwargs):
    return CatalystClient().getAvailableDevicesOrByCGId(**{'cloudType': cloudType, **kwargs})

@register('getCloudGateways')
def getCloudGateways(cloudType: str):
    return CatalystClient().getCloudGateways(**{'cloudType': cloudType})

@register('getCgwCustomSettingDetails')
def getCgwCustomSettingDetails(cloudGatewayName: str):
    return CatalystClient().getCgwCustomSettingDetails(**{'cloudGatewayName': cloudGatewayName})

@register('getCgwTypes')
def getCgwTypes(**kwargs):
    return CatalystClient().getCgwTypes(**{**kwargs})

@register('getCloudConnectedSites_1')
def getCloudConnectedSites_1(edgeType: str, **kwargs):
    return CatalystClient().getCloudConnectedSites_1(**{'edgeType': edgeType, **kwargs})

@register('getCloudConnectedSites')
def getCloudConnectedSites(cloudType: str, **kwargs):
    return CatalystClient().getCloudConnectedSites(**{'cloudType': cloudType, **kwargs})

@register('getEdgeConnectivityDetails')
def getEdgeConnectivityDetails(**kwargs):
    return CatalystClient().getEdgeConnectivityDetails(**{**kwargs})

@register('getEdgeConnectivityDetailByName')
def getEdgeConnectivityDetailByName(connectivityName: str):
    return CatalystClient().getEdgeConnectivityDetailByName(**{'connectivityName': connectivityName})

@register('getConnectivityGateways')
def getConnectivityGateways(**kwargs):
    return CatalystClient().getConnectivityGateways(**{**kwargs})

@register('getConnectivityGatewayCreationOptions')
def getConnectivityGatewayCreationOptions(**kwargs):
    return CatalystClient().getConnectivityGatewayCreationOptions(**{**kwargs})

@register('getCwanCoreNetworkPolicy')
def getCwanCoreNetworkPolicy():
    return CatalystClient().getCwanCoreNetworkPolicy(**{})

@register('getDashboardEdgeInfo')
def getDashboardEdgeInfo():
    return CatalystClient().getDashboardEdgeInfo(**{})

@register('getWanDevices')
def getWanDevices():
    return CatalystClient().getWanDevices(**{})

@register('getDeviceLinks')
def getDeviceLinks(**kwargs):
    return CatalystClient().getDeviceLinks(**{**kwargs})

@register('getDlPortSpeed')
def getDlPortSpeed(edgeType: str):
    return CatalystClient().getDlPortSpeed(**{'edgeType': edgeType})

@register('getCloudDevices_1')
def getCloudDevices_1(edgeType: str, **kwargs):
    return CatalystClient().getCloudDevices_1(**{'edgeType': edgeType, **kwargs})

@register('getCloudDevices')
def getCloudDevices(cloudType: str, **kwargs):
    return CatalystClient().getCloudDevices(**{'cloudType': cloudType, **kwargs})

@register('getEdgeWanDevices')
def getEdgeWanDevices(edgeType: str):
    return CatalystClient().getEdgeWanDevices(**{'edgeType': edgeType})

@register('getIcgws')
def getIcgws(**kwargs):
    return CatalystClient().getIcgws(**{**kwargs})

@register('getIcgwCustomSettingDetails')
def getIcgwCustomSettingDetails(edgeGatewayName: str):
    return CatalystClient().getIcgwCustomSettingDetails(**{'edgeGatewayName': edgeGatewayName})

@register('getIcgwTypes')
def getIcgwTypes(**kwargs):
    return CatalystClient().getIcgwTypes(**{**kwargs})

@register('getIcgwDetails')
def getIcgwDetails(edgeGatewayName: str):
    return CatalystClient().getIcgwDetails(**{'edgeGatewayName': edgeGatewayName})

@register('getEdgeGateways')
def getEdgeGateways(edgeType: str):
    return CatalystClient().getEdgeGateways(**{'edgeType': edgeType})

@register('getHostVpcs')
def getHostVpcs(cloudType: str, **kwargs):
    return CatalystClient().getHostVpcs(**{'cloudType': cloudType, **kwargs})

@register('getVpcTags')
def getVpcTags(**kwargs):
    return CatalystClient().getVpcTags(**{**kwargs})

@register('getSupportedEdgeImageNames')
def getSupportedEdgeImageNames(**kwargs):
    return CatalystClient().getSupportedEdgeImageNames(**{**kwargs})

@register('getSupportedInstanceSize')
def getSupportedInstanceSize(cloudType: str, **kwargs):
    return CatalystClient().getSupportedInstanceSize(**{'cloudType': cloudType, **kwargs})

@register('getSupportedEdgeInstanceSize')
def getSupportedEdgeInstanceSize(**kwargs):
    return CatalystClient().getSupportedEdgeInstanceSize(**{**kwargs})

@register('getInterconnectAccounts')
def getInterconnectAccounts(**kwargs):
    return CatalystClient().getInterconnectAccounts(**{**kwargs})

@register('getInterconnectAccount')
def getInterconnectAccount(interconnect_account_id: str):
    return CatalystClient().getInterconnectAccount(**{'interconnect-account-id': interconnect_account_id})

@register('getAuditReport')
def getAuditReport(interconnect_type: str, **kwargs):
    return CatalystClient().getAuditReport(**{'interconnect-type': interconnect_type, **kwargs})

@register('getGoogleCloudRouterAndAttachments')
def getGoogleCloudRouterAndAttachments(cloud_account_id: str, cloud_type: str, **kwargs):
    return CatalystClient().getGoogleCloudRouterAndAttachments(**{'cloud-account-id': cloud_account_id, 'cloud-type': cloud_type, **kwargs})

@register('getAwsTransitGateways')
def getAwsTransitGateways(cloud_account_id: str, cloud_type: str, **kwargs):
    return CatalystClient().getAwsTransitGateways(**{'cloud-account-id': cloud_account_id, 'cloud-type': cloud_type, **kwargs})

@register('getAzVirtualHubs')
def getAzVirtualHubs(cloud_account_id: str, cloud_type: str, **kwargs):
    return CatalystClient().getAzVirtualHubs(**{'cloud-account-id': cloud_account_id, 'cloud-type': cloud_type, **kwargs})

@register('getAzVirtualWans')
def getAzVirtualWans(cloud_account_id: str, cloud_type: str, resource_group: str, **kwargs):
    return CatalystClient().getAzVirtualWans(**{'cloud-account-id': cloud_account_id, 'cloud-type': cloud_type, 'resource-group': resource_group, **kwargs})

@register('getCloudConnectivityGateways')
def getCloudConnectivityGateways(cloud_account_id: str, cloud_type: str, **kwargs):
    return CatalystClient().getCloudConnectivityGateways(**{'cloud-account-id': cloud_account_id, 'cloud-type': cloud_type, **kwargs})

@register('getCloudConnectivityGatewayCreateOptions')
def getCloudConnectivityGatewayCreateOptions(cloud_account_id: str, cloud_type: str, **kwargs):
    return CatalystClient().getCloudConnectivityGatewayCreateOptions(**{'cloud-account-id': cloud_account_id, 'cloud-type': cloud_type, **kwargs})

@register('getInterconnectColors')
def getInterconnectColors(tunnel_type: str):
    return CatalystClient().getInterconnectColors(**{'tunnel-type': tunnel_type})

@register('getInterconnectOnRampGatewayConnections')
def getInterconnectOnRampGatewayConnections(**kwargs):
    return CatalystClient().getInterconnectOnRampGatewayConnections(**{**kwargs})

@register('getInterconnectOnRampGatewayConnection')
def getInterconnectOnRampGatewayConnection(connection_name: str):
    return CatalystClient().getInterconnectOnRampGatewayConnection(**{'connection-name': connection_name})

@register('getInterconnectMappingTags')
def getInterconnectMappingTags(cloud_account_id: str, cloud_type: str, **kwargs):
    return CatalystClient().getInterconnectMappingTags(**{'cloud-account-id': cloud_account_id, 'cloud-type': cloud_type, **kwargs})

@register('getInterconnectDeviceLinks')
def getInterconnectDeviceLinks(**kwargs):
    return CatalystClient().getInterconnectDeviceLinks(**{**kwargs})

@register('getInterconnectDeviceLink')
def getInterconnectDeviceLink(device_link_name: str):
    return CatalystClient().getInterconnectDeviceLink(**{'device-link-name': device_link_name})

@register('getInterconnectCrossConnections')
def getInterconnectCrossConnections(**kwargs):
    return CatalystClient().getInterconnectCrossConnections(**{**kwargs})

@register('getInterconnectCrossConnection')
def getInterconnectCrossConnection(connection_name: str):
    return CatalystClient().getInterconnectCrossConnection(**{'connection-name': connection_name})

@register('getInterconnectVirtualNetworkConnections')
def getInterconnectVirtualNetworkConnections(**kwargs):
    return CatalystClient().getInterconnectVirtualNetworkConnections(**{**kwargs})

@register('getInterconnectVirtualNetworkConnection')
def getInterconnectVirtualNetworkConnection(connection_name: str):
    return CatalystClient().getInterconnectVirtualNetworkConnection(**{'connection-name': connection_name})

@register('getInterconnectDashboard')
def getInterconnectDashboard():
    return CatalystClient().getInterconnectDashboard(**{})

@register('getInterconnectLicenses')
def getInterconnectLicenses(interconnect_account_id: str, interconnect_type: str, **kwargs):
    return CatalystClient().getInterconnectLicenses(**{'interconnect-account-id': interconnect_account_id, 'interconnect-type': interconnect_type, **kwargs})

@register('getInterconnectGateways')
def getInterconnectGateways(**kwargs):
    return CatalystClient().getInterconnectGateways(**{**kwargs})

@register('getInterconnectGatewayImageNames')
def getInterconnectGatewayImageNames(interconnect_type: str):
    return CatalystClient().getInterconnectGatewayImageNames(**{'interconnect-type': interconnect_type})

@register('getInterconnectGatewayInstanceSizes')
def getInterconnectGatewayInstanceSizes(interconnect_type: str):
    return CatalystClient().getInterconnectGatewayInstanceSizes(**{'interconnect-type': interconnect_type})

@register('getInterconnetGatewayTypes')
def getInterconnetGatewayTypes(interconnect_type: str):
    return CatalystClient().getInterconnetGatewayTypes(**{'interconnect-type': interconnect_type})

@register('getInterconnectGateway')
def getInterconnectGateway(interconnect_gateway_name: str):
    return CatalystClient().getInterconnectGateway(**{'interconnect-gateway-name': interconnect_gateway_name})

@register('getInterconnectGatewayCustomSettings')
def getInterconnectGatewayCustomSettings(interconnect_account_id: str, interconnect_gateway_name: str):
    return CatalystClient().getInterconnectGatewayCustomSettings(**{'interconnect-account-id': interconnect_account_id, 'interconnect-gateway-name': interconnect_gateway_name})

@register('getInterconnectIpTransit')
def getInterconnectIpTransit(interconnect_service_type: str, interconnect_type: str):
    return CatalystClient().getInterconnectIpTransit(**{'interconnect-service-type': interconnect_service_type, 'interconnect-type': interconnect_type})

@register('getInterconnectServiceSwPkg')
def getInterconnectServiceSwPkg(interconnect_account_id: str, interconnect_provider_name: str, interconnect_service_type: str, interconnect_service_vendor_name: str, **kwargs):
    return CatalystClient().getInterconnectServiceSwPkg(**{'interconnect-account-id': interconnect_account_id, 'interconnect-provider-name': interconnect_provider_name, 'interconnect-service-type': interconnect_service_type, 'interconnect-service-vendor-name': interconnect_service_vendor_name, **kwargs})

@register('getInterconnectServices')
def getInterconnectServices(interconnect_service_type: str, interconnect_service_vendor_name: str, interconnect_type: str):
    return CatalystClient().getInterconnectServices(**{'interconnect-service-type': interconnect_service_type, 'interconnect-service-vendor-name': interconnect_service_vendor_name, 'interconnect-type': interconnect_type})

@register('getInterconnectGlobalSettings')
def getInterconnectGlobalSettings(interconnect_type: str):
    return CatalystClient().getInterconnectGlobalSettings(**{'interconnect-type': interconnect_type})

@register('getInterconnectSshKeys')
def getInterconnectSshKeys(interconnect_account_id: str, interconnect_provider_name: str):
    return CatalystClient().getInterconnectSshKeys(**{'interconnect-account-id': interconnect_account_id, 'interconnect-provider-name': interconnect_provider_name})

@register('getInterconnectTypes')
def getInterconnectTypes():
    return CatalystClient().getInterconnectTypes(**{})

@register('getAllInterconnectWidgets')
def getAllInterconnectWidgets():
    return CatalystClient().getAllInterconnectWidgets(**{})

@register('getInterconnectBillingAccounts')
def getInterconnectBillingAccounts(interconnect_account_id: str, interconnect_type: str, **kwargs):
    return CatalystClient().getInterconnectBillingAccounts(**{'interconnect-account-id': interconnect_account_id, 'interconnect-type': interconnect_type, **kwargs})

@register('getInterconnectPartnerPorts')
def getInterconnectPartnerPorts(cloud_type: str, interconnect_account_id: str, interconnect_type: str, **kwargs):
    return CatalystClient().getInterconnectPartnerPorts(**{'cloud-type': cloud_type, 'interconnect-account-id': interconnect_account_id, 'interconnect-type': interconnect_type, **kwargs})

@register('getInterconnectPortSpeeds')
def getInterconnectPortSpeeds(connection_type: str, interconnect_account_id: str, interconnect_type: str, **kwargs):
    return CatalystClient().getInterconnectPortSpeeds(**{'connection-type': connection_type, 'interconnect-account-id': interconnect_account_id, 'interconnect-type': interconnect_type, **kwargs})

@register('getInterconnectLocationInfo')
def getInterconnectLocationInfo(interconnect_account_id: str, interconnect_type: str, **kwargs):
    return CatalystClient().getInterconnectLocationInfo(**{'interconnect-account-id': interconnect_account_id, 'interconnect-type': interconnect_type, **kwargs})

@register('getInterconnectConfigGroupTopology')
def getInterconnectConfigGroupTopology(config_group_id: str, interconnect_type: str):
    return CatalystClient().getInterconnectConfigGroupTopology(**{'config-group-id': config_group_id, 'interconnect-type': interconnect_type})

@register('getInterconnectDeviceLinkPortSpeeds')
def getInterconnectDeviceLinkPortSpeeds(interconnect_type: str):
    return CatalystClient().getInterconnectDeviceLinkPortSpeeds(**{'interconnect-type': interconnect_type})

@register('getAvailableDevicesOrByCGId_1')
def getAvailableDevicesOrByCGId_1(interconnect_type: str, **kwargs):
    return CatalystClient().getAvailableDevicesOrByCGId_1(**{'interconnect-type': interconnect_type, **kwargs})

@register('getInterconnectGatewayDevices')
def getInterconnectGatewayDevices(interconnect_type: str):
    return CatalystClient().getInterconnectGatewayDevices(**{'interconnect-type': interconnect_type})

@register('getMonitoringInterconnectConnectedSites')
def getMonitoringInterconnectConnectedSites(interconnect_type: str, **kwargs):
    return CatalystClient().getMonitoringInterconnectConnectedSites(**{'interconnect-type': interconnect_type, **kwargs})

@register('getMonitoringInterconnectDevices')
def getMonitoringInterconnectDevices(interconnect_type: str, **kwargs):
    return CatalystClient().getMonitoringInterconnectDevices(**{'interconnect-type': interconnect_type, **kwargs})

@register('getMonitoringInterconnectGateways')
def getMonitoringInterconnectGateways(interconnect_type: str):
    return CatalystClient().getMonitoringInterconnectGateways(**{'interconnect-type': interconnect_type})

@register('getInterconnectWidget')
def getInterconnectWidget(interconnect_type: str):
    return CatalystClient().getInterconnectWidget(**{'interconnect-type': interconnect_type})

@register('getWanInterfaceColors')
def getWanInterfaceColors():
    return CatalystClient().getWanInterfaceColors(**{})

@register('getLicenses')
def getLicenses(**kwargs):
    return CatalystClient().getLicenses(**{**kwargs})

@register('getEdgeLocationsInfo')
def getEdgeLocationsInfo(edgeType: str, **kwargs):
    return CatalystClient().getEdgeLocationsInfo(**{'edgeType': edgeType, **kwargs})

@register('getSupportedLoopbackCgwColors')
def getSupportedLoopbackCgwColors():
    return CatalystClient().getSupportedLoopbackCgwColors(**{})

@register('getSupportedLoopbackTransportColors')
def getSupportedLoopbackTransportColors():
    return CatalystClient().getSupportedLoopbackTransportColors(**{})

@register('getMappingMatrix')
def getMappingMatrix(cloudType: str):
    return CatalystClient().getMappingMatrix(**{'cloudType': cloudType})

@register('getDefaultMappingValues')
def getDefaultMappingValues(cloudType: str):
    return CatalystClient().getDefaultMappingValues(**{'cloudType': cloudType})

@register('getMappingStatus')
def getMappingStatus(cloudType: str, **kwargs):
    return CatalystClient().getMappingStatus(**{'cloudType': cloudType, **kwargs})

@register('getMappingSummary')
def getMappingSummary(**kwargs):
    return CatalystClient().getMappingSummary(**{**kwargs})

@register('getMappingTags')
def getMappingTags(**kwargs):
    return CatalystClient().getMappingTags(**{**kwargs})

@register('getEdgeMappingTags')
def getEdgeMappingTags(cloudType: str, **kwargs):
    return CatalystClient().getEdgeMappingTags(**{'cloudType': cloudType, **kwargs})

@register('getMappingVpns')
def getMappingVpns():
    return CatalystClient().getMappingVpns(**{})

@register('getCgwAssociatedMappings')
def getCgwAssociatedMappings(cloudGatewayName: str, cloudType: str, **kwargs):
    return CatalystClient().getCgwAssociatedMappings(**{'cloudGatewayName': cloudGatewayName, 'cloudType': cloudType, **kwargs})

@register('getPartnerPorts')
def getPartnerPorts(**kwargs):
    return CatalystClient().getPartnerPorts(**{**kwargs})

@register('getPortSpeed')
def getPortSpeed(connectivityType: str, edgeAccountId: str, edgeType: str, **kwargs):
    return CatalystClient().getPortSpeed(**{'connectivityType': connectivityType, 'edgeAccountId': edgeAccountId, 'edgeType': edgeType, **kwargs})

@register('getCloudRegions')
def getCloudRegions(**kwargs):
    return CatalystClient().getCloudRegions(**{**kwargs})

@register('getEdgeGlobalSettings')
def getEdgeGlobalSettings(edgeType: str):
    return CatalystClient().getEdgeGlobalSettings(**{'edgeType': edgeType})

@register('getGlobalSettings')
def getGlobalSettings(cloudType: str):
    return CatalystClient().getGlobalSettings(**{'cloudType': cloudType})

@register('getSites')
def getSites(**kwargs):
    return CatalystClient().getSites(**{**kwargs})

@register('getSshKeyList')
def getSshKeyList(accountId: str, cloudRegion: str, cloudType: str):
    return CatalystClient().getSshKeyList(**{'accountId': accountId, 'cloudRegion': cloudRegion, 'cloudType': cloudType})

@register('getSupportedSoftwareImageList')
def getSupportedSoftwareImageList(cloudType: str, **kwargs):
    return CatalystClient().getSupportedSoftwareImageList(**{'cloudType': cloudType, **kwargs})

@register('getTunnelNames')
def getTunnelNames(cloudGatewayName: str, cloudType: str):
    return CatalystClient().getTunnelNames(**{'cloudGatewayName': cloudGatewayName, 'cloudType': cloudType})

@register('getCloudTypes')
def getCloudTypes():
    return CatalystClient().getCloudTypes(**{})

@register('getEdgeTypes')
def getEdgeTypes():
    return CatalystClient().getEdgeTypes(**{})

@register('getVHubs')
def getVHubs(**kwargs):
    return CatalystClient().getVHubs(**{**kwargs})

@register('getVWans')
def getVWans(**kwargs):
    return CatalystClient().getVWans(**{**kwargs})

@register('getAllCloudWidgets')
def getAllCloudWidgets():
    return CatalystClient().getAllCloudWidgets(**{})

@register('getAllEdgeWidgets')
def getAllEdgeWidgets():
    return CatalystClient().getAllEdgeWidgets(**{})

@register('getEdgeWidget')
def getEdgeWidget(edgeType: str):
    return CatalystClient().getEdgeWidget(**{'edgeType': edgeType})

@register('getCloudWidget')
def getCloudWidget(cloudType: str):
    return CatalystClient().getCloudWidget(**{'cloudType': cloudType})

@register('getMultiCloudConfigGroupTopology')
def getMultiCloudConfigGroupTopology(cloudType: str, config_group_id: str):
    return CatalystClient().getMultiCloudConfigGroupTopology(**{'cloudType': cloudType, 'config-group-id': config_group_id})

@register('getVmanageControlStatus')
def getVmanageControlStatus(**kwargs):
    return CatalystClient().getVmanageControlStatus(**{**kwargs})

@register('getRebootCount')
def getRebootCount(isCached: bool):
    return CatalystClient().getRebootCount(**{'isCached': isCached})

@register('getNetworkIssuesSummary')
def getNetworkIssuesSummary():
    return CatalystClient().getNetworkIssuesSummary(**{})

@register('getNetworkStatusSummary')
def getNetworkStatusSummary():
    return CatalystClient().getNetworkStatusSummary(**{})

@register('getNetworkDesign')
def getNetworkDesign():
    return CatalystClient().getNetworkDesign(**{})

@register('getCircuits')
def getCircuits():
    return CatalystClient().getCircuits(**{})

@register('getGlobalParameters')
def getGlobalParameters():
    return CatalystClient().getGlobalParameters(**{})

@register('getGlobalTemplate')
def getGlobalTemplate(templateId: str):
    return CatalystClient().getGlobalTemplate(**{'templateId': templateId})

@register('runMyTest')
def runMyTest(name: str):
    return CatalystClient().runMyTest(**{'name': name})

@register('getDeviceProfileFeatureTemplateList')
def getDeviceProfileFeatureTemplateList():
    return CatalystClient().getDeviceProfileFeatureTemplateList(**{})

@register('getDeviceProfileConfigStatus')
def getDeviceProfileConfigStatus():
    return CatalystClient().getDeviceProfileConfigStatus(**{})

@register('getDeviceProfileConfigStatusByProfileId')
def getDeviceProfileConfigStatusByProfileId(profileId: str):
    return CatalystClient().getDeviceProfileConfigStatusByProfileId(**{'profileId': profileId})

@register('getDeviceProfileTaskCount')
def getDeviceProfileTaskCount():
    return CatalystClient().getDeviceProfileTaskCount(**{})

@register('getDeviceProfileTaskStatus')
def getDeviceProfileTaskStatus():
    return CatalystClient().getDeviceProfileTaskStatus(**{})

@register('getDeviceProfileTaskStatusByProfileId')
def getDeviceProfileTaskStatusByProfileId(profileId: str):
    return CatalystClient().getDeviceProfileTaskStatusByProfileId(**{'profileId': profileId})

@register('generateProfileTemplateList')
def generateProfileTemplateList():
    return CatalystClient().generateProfileTemplateList(**{})

@register('getDeviceProfileTemplate')
def getDeviceProfileTemplate(templateId: str):
    return CatalystClient().getDeviceProfileTemplate(**{'templateId': templateId})

@register('getServiceProfileConfig')
def getServiceProfileConfig(deviceModel: str, profileId: str):
    return CatalystClient().getServiceProfileConfig(**{'deviceModel': deviceModel, 'profileId': profileId})

@register('getNotificationRule')
def getNotificationRule(**kwargs):
    return CatalystClient().getNotificationRule(**{**kwargs})

@register('getDevices')
def getDevices(status: str):
    return CatalystClient().getDevices(**{'status': status})

@register('oauthAccess')
def oauthAccess(**kwargs):
    return CatalystClient().oauthAccess(**{**kwargs})

@register('getClientID')
def getClientID():
    return CatalystClient().getClientID(**{})

@register('getCall')
def getCall():
    return CatalystClient().getCall(**{})

@register('getPartners')
def getPartners():
    return CatalystClient().getPartners(**{})

@register('getACIDefinitions')
def getACIDefinitions():
    return CatalystClient().getACIDefinitions(**{})

@register('getDscpMappings')
def getDscpMappings(partnerId: str):
    return CatalystClient().getDscpMappings(**{'partnerId': partnerId})

@register('getEvents_1')
def getEvents_1(partnerId: str, **kwargs):
    return CatalystClient().getEvents_1(**{'partnerId': partnerId, **kwargs})

@register('getDataPrefixMappings')
def getDataPrefixMappings(partnerId: str):
    return CatalystClient().getDataPrefixMappings(**{'partnerId': partnerId})

@register('getDataPrefixSequences')
def getDataPrefixSequences():
    return CatalystClient().getDataPrefixSequences(**{})

@register('getSDAEnabledDevices')
def getSDAEnabledDevices(partnerId: str):
    return CatalystClient().getSDAEnabledDevices(**{'partnerId': partnerId})

@register('getDeviceDetails')
def getDeviceDetails(partnerId: str, uuid: str):
    return CatalystClient().getDeviceDetails(**{'partnerId': partnerId, 'uuid': uuid})

@register('getSitesForPartner')
def getSitesForPartner(partnerId: str):
    return CatalystClient().getSitesForPartner(**{'partnerId': partnerId})

@register('getOverlayVPNList')
def getOverlayVPNList():
    return CatalystClient().getOverlayVPNList(**{})

@register('getVPNList')
def getVPNList():
    return CatalystClient().getVPNList(**{})

@register('getPartnersByPartnerType')
def getPartnersByPartnerType(partnerType: str):
    return CatalystClient().getPartnersByPartnerType(**{'partnerType': partnerType})

@register('getPartnerDevices')
def getPartnerDevices(nmsId: str, partnerType: str):
    return CatalystClient().getPartnerDevices(**{'nmsId': nmsId, 'partnerType': partnerType})

@register('getPartner')
def getPartner(nmsId: str, partnerType: str):
    return CatalystClient().getPartner(**{'nmsId': nmsId, 'partnerType': partnerType})

@register('getSecureXRefreshToken')
def getSecureXRefreshToken(clientId: str, regionBaseUri: str):
    return CatalystClient().getSecureXRefreshToken(**{'clientId': clientId, 'regionBaseUri': regionBaseUri})

@register('getResources')
def getResources(tenantId: str, tenantVpn: int):
    return CatalystClient().getResources(**{'tenantId': tenantId, 'tenantVpn': tenantVpn})

@register('listSchedules')
def listSchedules(**kwargs):
    return CatalystClient().listSchedules(**{**kwargs})

@register('getScheduleRecordForBackup')
def getScheduleRecordForBackup(schedulerId: str):
    return CatalystClient().getScheduleRecordForBackup(**{'schedulerId': schedulerId})

@register('getExtendedApplications')
def getExtendedApplications(**kwargs):
    return CatalystClient().getExtendedApplications(**{**kwargs})

@register('getCloudConnector')
def getCloudConnector():
    return CatalystClient().getCloudConnector(**{})

@register('getCloudConnectorStatus')
def getCloudConnectorStatus():
    return CatalystClient().getCloudConnectorStatus(**{})

@register('getCustomApp')
def getCustomApp():
    return CatalystClient().getCustomApp(**{})

@register('getAllProtocolPacks')
def getAllProtocolPacks():
    return CatalystClient().getAllProtocolPacks(**{})

@register('getBaseSystemPack')
def getBaseSystemPack():
    return CatalystClient().getBaseSystemPack(**{})

@register('getAllSDAVCDevice')
def getAllSDAVCDevice():
    return CatalystClient().getAllSDAVCDevice(**{})

@register('getDefaultApplicationComplianceDetails')
def getDefaultApplicationComplianceDetails():
    return CatalystClient().getDefaultApplicationComplianceDetails(**{})

@register('isApplicationComplianceDetected')
def isApplicationComplianceDetected():
    return CatalystClient().isApplicationComplianceDetected(**{})

@register('getApplicationComplianceStatus')
def getApplicationComplianceStatus(uuid: str):
    return CatalystClient().getApplicationComplianceStatus(**{'uuid': uuid})

@register('getApplicationComplianceDetails')
def getApplicationComplianceDetails(uuid: str):
    return CatalystClient().getApplicationComplianceDetails(**{'uuid': uuid})

@register('getCustomApplicationList')
def getCustomApplicationList():
    return CatalystClient().getCustomApplicationList(**{})

@register('getNonCompliantDevicesForProtocolPack')
def getNonCompliantDevicesForProtocolPack(protocolPackName: str):
    return CatalystClient().getNonCompliantDevicesForProtocolPack(**{'protocolPackName': protocolPackName})

@register('getDeviceComplianceStatus')
def getDeviceComplianceStatus(uuid: str):
    return CatalystClient().getDeviceComplianceStatus(**{'uuid': uuid})

@register('getNewApplicationList')
def getNewApplicationList(deviceUUID: str):
    return CatalystClient().getNewApplicationList(**{'deviceUUID': deviceUUID})

@register('getCompliancePolicy')
def getCompliancePolicy(**kwargs):
    return CatalystClient().getCompliancePolicy(**{**kwargs})

@register('getPolicyComplianceStatus')
def getPolicyComplianceStatus(uuid: str):
    return CatalystClient().getPolicyComplianceStatus(**{'uuid': uuid})

@register('getDefaultSystemPack')
def getDefaultSystemPack():
    return CatalystClient().getDefaultSystemPack(**{})

@register('getLatestSystemPack')
def getLatestSystemPack():
    return CatalystClient().getLatestSystemPack(**{})

@register('getDeployJobStatus')
def getDeployJobStatus():
    return CatalystClient().getDeployJobStatus(**{})

@register('getDeployJobStatus_1')
def getDeployJobStatus_1(uuid: str):
    return CatalystClient().getDeployJobStatus_1(**{'uuid': uuid})

@register('getProtocolPackUploadStatus')
def getProtocolPackUploadStatus(uuid: str):
    return CatalystClient().getProtocolPackUploadStatus(**{'uuid': uuid})

@register('getSecurityDeviceHealth')
def getSecurityDeviceHealth(**kwargs):
    return CatalystClient().getSecurityDeviceHealth(**{**kwargs})

@register('getSecurityPolicyDeviceList')
def getSecurityPolicyDeviceList():
    return CatalystClient().getSecurityPolicyDeviceList(**{})

@register('getSegments')
def getSegments():
    return CatalystClient().getSegments(**{})

@register('getSegment')
def getSegment(id: str):
    return CatalystClient().getSegment(**{'id': id})

@register('createServerInfo_1')
def createServerInfo_1():
    return CatalystClient().createServerInfo_1(**{})

@register('getDataChangeInfo')
def getDataChangeInfo(partnerId: str, **kwargs):
    return CatalystClient().getDataChangeInfo(**{'partnerId': partnerId, **kwargs})

@register('showInfo')
def showInfo():
    return CatalystClient().showInfo(**{})

@register('getCertificate')
def getCertificate():
    return CatalystClient().getCertificate(**{})

@register('getBanner')
def getBanner():
    return CatalystClient().getBanner(**{})

@register('getSessionTimout')
def getSessionTimout():
    return CatalystClient().getSessionTimout(**{})

@register('getCertConfiguration')
def getCertConfiguration(type: str):
    return CatalystClient().getCertConfiguration(**{'type': type})

@register('getCloudxConfiguration')
def getCloudxConfiguration():
    return CatalystClient().getCloudxConfiguration(**{})

@register('getGoogleMapKey')
def getGoogleMapKey():
    return CatalystClient().getGoogleMapKey(**{})

@register('getMaintenanceWindow')
def getMaintenanceWindow():
    return CatalystClient().getMaintenanceWindow(**{})

@register('getMicrosoftTelemetryConfiguration')
def getMicrosoftTelemetryConfiguration():
    return CatalystClient().getMicrosoftTelemetryConfiguration(**{})

@register('getWaniConfiguration')
def getWaniConfiguration():
    return CatalystClient().getWaniConfiguration(**{})

@register('getConfigurationBySettingType')
def getConfigurationBySettingType(type: str):
    return CatalystClient().getConfigurationBySettingType(**{'type': type})

@register('getPasswordPolicy')
def getPasswordPolicy():
    return CatalystClient().getPasswordPolicy(**{})

@register('getSigDynamicDataCenterList')
def getSigDynamicDataCenterList(tunneltype: str, type: str):
    return CatalystClient().getSigDynamicDataCenterList(**{'tunneltype': tunneltype, 'type': type})

@register('getSigDataCenterList')
def getSigDataCenterList(devicetype: str, tunneltype: str, type: str):
    return CatalystClient().getSigDataCenterList(**{'devicetype': devicetype, 'tunneltype': tunneltype, 'type': type})

@register('getSigGlobalCredentials')
def getSigGlobalCredentials(featureTemplateType: str):
    return CatalystClient().getSigGlobalCredentials(**{'featureTemplateType': featureTemplateType})

@register('getChildOrgs')
def getChildOrgs(type: str):
    return CatalystClient().getChildOrgs(**{'type': type})

@register('fetchAccounts')
def fetchAccounts(mode: str):
    return CatalystClient().fetchAccounts(**{'mode': mode})

@register('fetchReports_1')
def fetchReports_1():
    return CatalystClient().fetchReports_1(**{})

@register('fetchReports')
def fetchReports(saDomain: str, saId: str):
    return CatalystClient().fetchReports(**{'saDomain': saDomain, 'saId': saId})

@register('getSettings')
def getSettings():
    return CatalystClient().getSettings(**{})

@register('getProxyCertOfEdge')
def getProxyCertOfEdge(deviceId: str):
    return CatalystClient().getProxyCertOfEdge(**{'deviceId': deviceId})

@register('getSslProxyCSR')
def getSslProxyCSR(deviceId: str):
    return CatalystClient().getSslProxyCSR(**{'deviceId': deviceId})

@register('getSslProxyList')
def getSslProxyList():
    return CatalystClient().getSslProxyList(**{})

@register('getCertificateState')
def getCertificateState():
    return CatalystClient().getCertificateState(**{})

@register('getEnterpriseCertificate')
def getEnterpriseCertificate():
    return CatalystClient().getEnterpriseCertificate(**{})

@register('getVManageEnterpriseRootCertificate')
def getVManageEnterpriseRootCertificate():
    return CatalystClient().getVManageEnterpriseRootCertificate(**{})

@register('getvManageCertificate')
def getvManageCertificate():
    return CatalystClient().getvManageCertificate(**{})

@register('getvManageCSR')
def getvManageCSR():
    return CatalystClient().getvManageCSR(**{})

@register('getvManageRootCA')
def getvManageRootCA():
    return CatalystClient().getvManageRootCA(**{})

@register('getStatisticType')
def getStatisticType():
    return CatalystClient().getStatisticType(**{})

@register('getAggregationDataByQuery_14')
def getAggregationDataByQuery_14(**kwargs):
    return CatalystClient().getAggregationDataByQuery_14(**{**kwargs})

@register('getStatDataRawData_1')
def getStatDataRawData_1(**kwargs):
    return CatalystClient().getStatDataRawData_1(**{**kwargs})

@register('getAggregationDataByQuery_1')
def getAggregationDataByQuery_1(**kwargs):
    return CatalystClient().getAggregationDataByQuery_1(**{**kwargs})

@register('getStatDataRawDataAsCSV_1')
def getStatDataRawDataAsCSV_1(**kwargs):
    return CatalystClient().getStatDataRawDataAsCSV_1(**{**kwargs})

@register('getCount_2')
def getCount_2(query: str):
    return CatalystClient().getCount_2(**{'query': query})

@register('getStatDataFields_2')
def getStatDataFields_2():
    return CatalystClient().getStatDataFields_2(**{})

@register('getStatsPaginationRawData_1')
def getStatsPaginationRawData_1(**kwargs):
    return CatalystClient().getStatsPaginationRawData_1(**{**kwargs})

@register('getStatQueryFields_2')
def getStatQueryFields_2():
    return CatalystClient().getStatQueryFields_2(**{})

@register('getStatDataRawData')
def getStatDataRawData(**kwargs):
    return CatalystClient().getStatDataRawData(**{**kwargs})

@register('getAggregationDataByQuery')
def getAggregationDataByQuery(**kwargs):
    return CatalystClient().getAggregationDataByQuery(**{**kwargs})

@register('getStatDataRawDataAsCSV')
def getStatDataRawDataAsCSV(**kwargs):
    return CatalystClient().getStatDataRawDataAsCSV(**{**kwargs})

@register('getCount_1')
def getCount_1(query: str):
    return CatalystClient().getCount_1(**{'query': query})

@register('getStatDataFields_1')
def getStatDataFields_1():
    return CatalystClient().getStatDataFields_1(**{})

@register('getStatsPaginationRawData')
def getStatsPaginationRawData(**kwargs):
    return CatalystClient().getStatsPaginationRawData(**{**kwargs})

@register('getStatQueryFields_1')
def getStatQueryFields_1():
    return CatalystClient().getStatQueryFields_1(**{})

@register('getStatDataRawData_2')
def getStatDataRawData_2(**kwargs):
    return CatalystClient().getStatDataRawData_2(**{**kwargs})

@register('getAggregationDataByQuery_2')
def getAggregationDataByQuery_2(**kwargs):
    return CatalystClient().getAggregationDataByQuery_2(**{**kwargs})

@register('getStatDataRawDataAsCSV_2')
def getStatDataRawDataAsCSV_2(**kwargs):
    return CatalystClient().getStatDataRawDataAsCSV_2(**{**kwargs})

@register('getStatsAppRouteDeviceTunnelSummary')
def getStatsAppRouteDeviceTunnelSummary(**kwargs):
    return CatalystClient().getStatsAppRouteDeviceTunnelSummary(**{**kwargs})

@register('getStatsAppRouteDeviceTunnels')
def getStatsAppRouteDeviceTunnels(**kwargs):
    return CatalystClient().getStatsAppRouteDeviceTunnels(**{**kwargs})

@register('getDocCount_1')
def getDocCount_1(query: str):
    return CatalystClient().getDocCount_1(**{'query': query})

@register('getStatDataFields_3')
def getStatDataFields_3():
    return CatalystClient().getStatDataFields_3(**{})

@register('getStatBulkRawData')
def getStatBulkRawData(**kwargs):
    return CatalystClient().getStatBulkRawData(**{**kwargs})

@register('getStatQueryFields_3')
def getStatQueryFields_3():
    return CatalystClient().getStatQueryFields_3(**{})

@register('getAppRouteTransportSummaryType')
def getAppRouteTransportSummaryType(type: str, **kwargs):
    return CatalystClient().getAppRouteTransportSummaryType(**{'type': type, **kwargs})

@register('getAppRouteTransportType')
def getAppRouteTransportType(limit: int, type: str, **kwargs):
    return CatalystClient().getAppRouteTransportType(**{'limit': limit, 'type': type, **kwargs})

@register('getAppRouteTunnelSummaryType')
def getAppRouteTunnelSummaryType(type: str, **kwargs):
    return CatalystClient().getAppRouteTunnelSummaryType(**{'type': type, **kwargs})

@register('getAppRouteTunnelHealth')
def getAppRouteTunnelHealth(type: str, **kwargs):
    return CatalystClient().getAppRouteTunnelHealth(**{'type': type, **kwargs})

@register('getAppRouteTunnelsSummaryType')
def getAppRouteTunnelsSummaryType(type: str, **kwargs):
    return CatalystClient().getAppRouteTunnelsSummaryType(**{'type': type, **kwargs})

@register('getAppRouteTunnelType')
def getAppRouteTunnelType(type: str, **kwargs):
    return CatalystClient().getAppRouteTunnelType(**{'type': type, **kwargs})

@register('getStatDataRawData_4')
def getStatDataRawData_4(**kwargs):
    return CatalystClient().getStatDataRawData_4(**{**kwargs})

@register('getAggregationDataByQuery_4')
def getAggregationDataByQuery_4(**kwargs):
    return CatalystClient().getAggregationDataByQuery_4(**{**kwargs})

@register('getStatDataRawDataAsCSV_4')
def getStatDataRawDataAsCSV_4(**kwargs):
    return CatalystClient().getStatDataRawDataAsCSV_4(**{**kwargs})

@register('getCount_4')
def getCount_4(query: str):
    return CatalystClient().getCount_4(**{'query': query})

@register('getStatDataFields_5')
def getStatDataFields_5():
    return CatalystClient().getStatDataFields_5(**{})

@register('getStatsPaginationRawData_3')
def getStatsPaginationRawData_3(**kwargs):
    return CatalystClient().getStatsPaginationRawData_3(**{**kwargs})

@register('getStatQueryFields_5')
def getStatQueryFields_5():
    return CatalystClient().getStatQueryFields_5(**{})

@register('getStatDataRawData_5')
def getStatDataRawData_5(**kwargs):
    return CatalystClient().getStatDataRawData_5(**{**kwargs})

@register('getAggregationDataByQuery_5')
def getAggregationDataByQuery_5(**kwargs):
    return CatalystClient().getAggregationDataByQuery_5(**{**kwargs})

@register('getStatDataRawDataAsCSV_5')
def getStatDataRawDataAsCSV_5(**kwargs):
    return CatalystClient().getStatDataRawDataAsCSV_5(**{**kwargs})

@register('getCount_5')
def getCount_5(query: str):
    return CatalystClient().getCount_5(**{'query': query})

@register('getStatDataFields_6')
def getStatDataFields_6():
    return CatalystClient().getStatDataFields_6(**{})

@register('getStatsPaginationRawData_4')
def getStatsPaginationRawData_4(**kwargs):
    return CatalystClient().getStatsPaginationRawData_4(**{**kwargs})

@register('getStatQueryFields_6')
def getStatQueryFields_6():
    return CatalystClient().getStatQueryFields_6(**{})

@register('getStatDataRawData_6')
def getStatDataRawData_6(**kwargs):
    return CatalystClient().getStatDataRawData_6(**{**kwargs})

@register('getAggregationDataByQuery_6')
def getAggregationDataByQuery_6(**kwargs):
    return CatalystClient().getAggregationDataByQuery_6(**{**kwargs})

@register('getStatDataRawDataAsCSV_6')
def getStatDataRawDataAsCSV_6(**kwargs):
    return CatalystClient().getStatDataRawDataAsCSV_6(**{**kwargs})

@register('getCount_6')
def getCount_6(query: str):
    return CatalystClient().getCount_6(**{'query': query})

@register('getStatDataFields_7')
def getStatDataFields_7():
    return CatalystClient().getStatDataFields_7(**{})

@register('getStatsPaginationRawData_5')
def getStatsPaginationRawData_5(**kwargs):
    return CatalystClient().getStatsPaginationRawData_5(**{**kwargs})

@register('getStatQueryFields_7')
def getStatQueryFields_7():
    return CatalystClient().getStatQueryFields_7(**{})

@register('getStatDataRawData_7')
def getStatDataRawData_7(**kwargs):
    return CatalystClient().getStatDataRawData_7(**{**kwargs})

@register('getAggregationDataByQuery_7')
def getAggregationDataByQuery_7(**kwargs):
    return CatalystClient().getAggregationDataByQuery_7(**{**kwargs})

@register('getStatDataRawDataAsCSV_7')
def getStatDataRawDataAsCSV_7(**kwargs):
    return CatalystClient().getStatDataRawDataAsCSV_7(**{**kwargs})

@register('getCount_7')
def getCount_7(query: str):
    return CatalystClient().getCount_7(**{'query': query})

@register('getStatDataFields_8')
def getStatDataFields_8():
    return CatalystClient().getStatDataFields_8(**{})

@register('getStatsPaginationRawData_6')
def getStatsPaginationRawData_6(**kwargs):
    return CatalystClient().getStatsPaginationRawData_6(**{**kwargs})

@register('getStatQueryFields_8')
def getStatQueryFields_8():
    return CatalystClient().getStatQueryFields_8(**{})

@register('getStatDataRawData_9')
def getStatDataRawData_9(**kwargs):
    return CatalystClient().getStatDataRawData_9(**{**kwargs})

@register('getAggregationDataByQuery_9')
def getAggregationDataByQuery_9(**kwargs):
    return CatalystClient().getAggregationDataByQuery_9(**{**kwargs})

@register('createFlowsGrid')
def createFlowsGrid(**kwargs):
    return CatalystClient().createFlowsGrid(**{**kwargs})

@register('createFlowssummary')
def createFlowssummary(**kwargs):
    return CatalystClient().createFlowssummary(**{**kwargs})

@register('getStatDataRawDataAsCSV_9')
def getStatDataRawDataAsCSV_9(**kwargs):
    return CatalystClient().getStatDataRawDataAsCSV_9(**{**kwargs})

@register('createFlowDeviceData')
def createFlowDeviceData(**kwargs):
    return CatalystClient().createFlowDeviceData(**{**kwargs})

@register('getCount_9')
def getCount_9(query: str):
    return CatalystClient().getCount_9(**{'query': query})

@register('getStatDataFields_10')
def getStatDataFields_10():
    return CatalystClient().getStatDataFields_10(**{})

@register('getStatsPaginationRawData_8')
def getStatsPaginationRawData_8(**kwargs):
    return CatalystClient().getStatsPaginationRawData_8(**{**kwargs})

@register('getStatQueryFields_10')
def getStatQueryFields_10():
    return CatalystClient().getStatQueryFields_10(**{})

@register('getStatDataRawData_10')
def getStatDataRawData_10(**kwargs):
    return CatalystClient().getStatDataRawData_10(**{**kwargs})

@register('getAggregationDataByQuery_10')
def getAggregationDataByQuery_10(**kwargs):
    return CatalystClient().getAggregationDataByQuery_10(**{**kwargs})

@register('getStatDataRawDataAsCSV_10')
def getStatDataRawDataAsCSV_10(**kwargs):
    return CatalystClient().getStatDataRawDataAsCSV_10(**{**kwargs})

@register('getCount_10')
def getCount_10(query: str):
    return CatalystClient().getCount_10(**{'query': query})

@register('getStatDataFields_11')
def getStatDataFields_11():
    return CatalystClient().getStatDataFields_11(**{})

@register('getStatsPaginationRawData_9')
def getStatsPaginationRawData_9(**kwargs):
    return CatalystClient().getStatsPaginationRawData_9(**{**kwargs})

@register('getStatQueryFields_11')
def getStatQueryFields_11():
    return CatalystClient().getStatQueryFields_11(**{})

@register('startStatsCollection')
def startStatsCollection():
    return CatalystClient().startStatsCollection(**{})

@register('generateStatsCollectThreadReport')
def generateStatsCollectThreadReport():
    return CatalystClient().generateStatsCollectThreadReport(**{})

@register('resetStatsCollection')
def resetStatsCollection(processQueue: int):
    return CatalystClient().resetStatsCollection(**{'processQueue': processQueue})

@register('getStatDataRawDataAsCSV_13')
def getStatDataRawDataAsCSV_13(**kwargs):
    return CatalystClient().getStatDataRawDataAsCSV_13(**{**kwargs})

@register('enableStatisticsDemoMode')
def enableStatisticsDemoMode(**kwargs):
    return CatalystClient().enableStatisticsDemoMode(**{**kwargs})

@register('getStatDataRawData_16')
def getStatDataRawData_16(**kwargs):
    return CatalystClient().getStatDataRawData_16(**{**kwargs})

@register('getAggregationDataByQuery_18')
def getAggregationDataByQuery_18(**kwargs):
    return CatalystClient().getAggregationDataByQuery_18(**{**kwargs})

@register('getStatDataRawDataAsCSV_16')
def getStatDataRawDataAsCSV_16(**kwargs):
    return CatalystClient().getStatDataRawDataAsCSV_16(**{**kwargs})

@register('getCount_15')
def getCount_15(query: str):
    return CatalystClient().getCount_15(**{'query': query})

@register('getStatDataFields_17')
def getStatDataFields_17():
    return CatalystClient().getStatDataFields_17(**{})

@register('getStatsPaginationRawData_14')
def getStatsPaginationRawData_14(**kwargs):
    return CatalystClient().getStatsPaginationRawData_14(**{**kwargs})

@register('getStatQueryFields_18')
def getStatQueryFields_18():
    return CatalystClient().getStatQueryFields_18(**{})

@register('getDeviceHealthHistory')
def getDeviceHealthHistory(**kwargs):
    return CatalystClient().getDeviceHealthHistory(**{**kwargs})

@register('getDeviceHealthOverview')
def getDeviceHealthOverview(type: str, **kwargs):
    return CatalystClient().getDeviceHealthOverview(**{'type': type, **kwargs})

@register('getCount_12')
def getCount_12(query: str):
    return CatalystClient().getCount_12(**{'query': query})

@register('fetchList')
def fetchList(processType: str):
    return CatalystClient().fetchList(**{'processType': processType})

@register('download')
def download(deviceIp: str, fileName: str, fileType: str, processType: str, queue: str, token: str):
    return CatalystClient().download(**{'deviceIp': deviceIp, 'fileName': fileName, 'fileType': fileType, 'processType': processType, 'queue': queue, 'token': token})

@register('getDPIStatsRawData')
def getDPIStatsRawData(**kwargs):
    return CatalystClient().getDPIStatsRawData(**{**kwargs})

@register('getDPIStatsAggregationData')
def getDPIStatsAggregationData(**kwargs):
    return CatalystClient().getDPIStatsAggregationData(**{**kwargs})

@register('getAggAppFlows')
def getAggAppFlows(query: str, **kwargs):
    return CatalystClient().getAggAppFlows(**{'query': query, **kwargs})

@register('getAggAppFlowsSummary')
def getAggAppFlowsSummary(query: str, **kwargs):
    return CatalystClient().getAggAppFlowsSummary(**{'query': query, **kwargs})

@register('getDPIStatsRawDataAsCSV')
def getDPIStatsRawDataAsCSV(**kwargs):
    return CatalystClient().getDPIStatsRawDataAsCSV(**{**kwargs})

@register('getDPIDeviceAppUniqueFlowCount')
def getDPIDeviceAppUniqueFlowCount(deviceId: str, interval: str, window: int, **kwargs):
    return CatalystClient().getDPIDeviceAppUniqueFlowCount(**{'deviceId': deviceId, 'interval': interval, 'window': window, **kwargs})

@register('getDPIDeviceAppAggregationData')
def getDPIDeviceAppAggregationData(query: str, **kwargs):
    return CatalystClient().getDPIDeviceAppAggregationData(**{'query': query, **kwargs})

@register('getDPIDeviceAppDetails')
def getDPIDeviceAppDetails(query: str):
    return CatalystClient().getDPIDeviceAppDetails(**{'query': query})

@register('getDPIStatsCount')
def getDPIStatsCount(**kwargs):
    return CatalystClient().getDPIStatsCount(**{**kwargs})

@register('getDPIFields')
def getDPIFields():
    return CatalystClient().getDPIFields(**{})

@register('getDPIStatsPaginationRawData')
def getDPIStatsPaginationRawData(**kwargs):
    return CatalystClient().getDPIStatsPaginationRawData(**{**kwargs})

@register('getDPIQueryFields')
def getDPIQueryFields():
    return CatalystClient().getDPIQueryFields(**{})

@register('getStatDataRawData_8')
def getStatDataRawData_8(**kwargs):
    return CatalystClient().getStatDataRawData_8(**{**kwargs})

@register('getAggregationDataByQuery_8')
def getAggregationDataByQuery_8(**kwargs):
    return CatalystClient().getAggregationDataByQuery_8(**{**kwargs})

@register('getStatDataRawDataAsCSV_8')
def getStatDataRawDataAsCSV_8(**kwargs):
    return CatalystClient().getStatDataRawDataAsCSV_8(**{**kwargs})

@register('getCount_8')
def getCount_8(query: str):
    return CatalystClient().getCount_8(**{'query': query})

@register('getStatDataFields_9')
def getStatDataFields_9():
    return CatalystClient().getStatDataFields_9(**{})

@register('getStatsPaginationRawData_7')
def getStatsPaginationRawData_7(**kwargs):
    return CatalystClient().getStatsPaginationRawData_7(**{**kwargs})

@register('getStatQueryFields_9')
def getStatQueryFields_9():
    return CatalystClient().getStatQueryFields_9(**{})

@register('getStatDataRawData_19')
def getStatDataRawData_19(**kwargs):
    return CatalystClient().getStatDataRawData_19(**{**kwargs})

@register('getAggregationDataByQuery_21')
def getAggregationDataByQuery_21(**kwargs):
    return CatalystClient().getAggregationDataByQuery_21(**{**kwargs})

@register('getStatDataRawDataAsCSV_19')
def getStatDataRawDataAsCSV_19(**kwargs):
    return CatalystClient().getStatDataRawDataAsCSV_19(**{**kwargs})

@register('getCount_18')
def getCount_18(query: str):
    return CatalystClient().getCount_18(**{'query': query})

@register('getStatDataFields_20')
def getStatDataFields_20():
    return CatalystClient().getStatDataFields_20(**{})

@register('getStatsPaginationRawData_17')
def getStatsPaginationRawData_17(**kwargs):
    return CatalystClient().getStatsPaginationRawData_17(**{**kwargs})

@register('getStatQueryFields_21')
def getStatQueryFields_21():
    return CatalystClient().getStatQueryFields_21(**{})

@register('getStatDataFields_14')
def getStatDataFields_14():
    return CatalystClient().getStatDataFields_14(**{})

@register('getStatDataRawData_14')
def getStatDataRawData_14(**kwargs):
    return CatalystClient().getStatDataRawData_14(**{**kwargs})

@register('getAggregationDataByQuery_28')
def getAggregationDataByQuery_28(**kwargs):
    return CatalystClient().getAggregationDataByQuery_28(**{**kwargs})

@register('getStatDataRawDataAsCSV_26')
def getStatDataRawDataAsCSV_26(**kwargs):
    return CatalystClient().getStatDataRawDataAsCSV_26(**{**kwargs})

@register('getFlowlogCount')
def getFlowlogCount(query: str):
    return CatalystClient().getFlowlogCount(**{'query': query})

@register('getFlowlogFields')
def getFlowlogFields():
    return CatalystClient().getFlowlogFields(**{})

@register('getStatsPaginationRawData_24')
def getStatsPaginationRawData_24(**kwargs):
    return CatalystClient().getStatsPaginationRawData_24(**{**kwargs})

@register('getFlowlogQueryFields')
def getFlowlogQueryFields():
    return CatalystClient().getFlowlogQueryFields(**{})

@register('getStatDataRawData_24')
def getStatDataRawData_24(**kwargs):
    return CatalystClient().getStatDataRawData_24(**{**kwargs})

@register('getAggregationDataByQuery_26')
def getAggregationDataByQuery_26(**kwargs):
    return CatalystClient().getAggregationDataByQuery_26(**{**kwargs})

@register('getStatDataRawDataAsCSV_24')
def getStatDataRawDataAsCSV_24(**kwargs):
    return CatalystClient().getStatDataRawDataAsCSV_24(**{**kwargs})

@register('getCount_23')
def getCount_23(query: str):
    return CatalystClient().getCount_23(**{'query': query})

@register('getStatDataFields_25')
def getStatDataFields_25():
    return CatalystClient().getStatDataFields_25(**{})

@register('getStatsPaginationRawData_22')
def getStatsPaginationRawData_22(**kwargs):
    return CatalystClient().getStatsPaginationRawData_22(**{**kwargs})

@register('getStatQueryFields_26')
def getStatQueryFields_26():
    return CatalystClient().getStatQueryFields_26(**{})

@register('getStatDataRawData_11')
def getStatDataRawData_11(query: str, **kwargs):
    return CatalystClient().getStatDataRawData_11(**{'query': query, **kwargs})

@register('getAggregationDataByQuery_11')
def getAggregationDataByQuery_11(query: str):
    return CatalystClient().getAggregationDataByQuery_11(**{'query': query})

@register('getBandwidthDistribution')
def getBandwidthDistribution(**kwargs):
    return CatalystClient().getBandwidthDistribution(**{**kwargs})

@register('getStatDataRawDataAsCSV_11')
def getStatDataRawDataAsCSV_11(query: str):
    return CatalystClient().getStatDataRawDataAsCSV_11(**{'query': query})

@register('getCount10')
def getCount10(query: str):
    return CatalystClient().getCount10(**{'query': query})

@register('getStatDataFields_12')
def getStatDataFields_12():
    return CatalystClient().getStatDataFields_12(**{})

@register('getStatBulkRawData_1')
def getStatBulkRawData_1(**kwargs):
    return CatalystClient().getStatBulkRawData_1(**{**kwargs})

@register('getStatQueryFields_12')
def getStatQueryFields_12():
    return CatalystClient().getStatQueryFields_12(**{})

@register('getStatisticsPerInterface')
def getStatisticsPerInterface(query: str):
    return CatalystClient().getStatisticsPerInterface(**{'query': query})

@register('getStatDataRawData_22')
def getStatDataRawData_22(**kwargs):
    return CatalystClient().getStatDataRawData_22(**{**kwargs})

@register('getAggregationDataByQuery_24')
def getAggregationDataByQuery_24(**kwargs):
    return CatalystClient().getAggregationDataByQuery_24(**{**kwargs})

@register('getStatDataRawDataAsCSV_22')
def getStatDataRawDataAsCSV_22(**kwargs):
    return CatalystClient().getStatDataRawDataAsCSV_22(**{**kwargs})

@register('getCount_21')
def getCount_21(query: str):
    return CatalystClient().getCount_21(**{'query': query})

@register('getStatDataFields_23')
def getStatDataFields_23():
    return CatalystClient().getStatDataFields_23(**{})

@register('getStatsPaginationRawData_20')
def getStatsPaginationRawData_20(**kwargs):
    return CatalystClient().getStatsPaginationRawData_20(**{**kwargs})

@register('getStatQueryFields_24')
def getStatQueryFields_24():
    return CatalystClient().getStatQueryFields_24(**{})

@register('getQueueEntries')
def getQueueEntries():
    return CatalystClient().getQueueEntries(**{})

@register('getQueueProperties')
def getQueueProperties():
    return CatalystClient().getQueueProperties(**{})

@register('getStatsPaginationRawData_11')
def getStatsPaginationRawData_11(**kwargs):
    return CatalystClient().getStatsPaginationRawData_11(**{**kwargs})

@register('getApplicationHeatMapDetail')
def getApplicationHeatMapDetail(application: str, heatmap_time: int, start_time: int, **kwargs):
    return CatalystClient().getApplicationHeatMapDetail(**{'application': application, 'heatmap_time': heatmap_time, 'start_time': start_time, **kwargs})

@register('getApplicationSitesHealth')
def getApplicationSitesHealth(application: str, **kwargs):
    return CatalystClient().getApplicationSitesHealth(**{'application': application, **kwargs})

@register('getApplicationsSiteHealth')
def getApplicationsSiteHealth(siteid: str, **kwargs):
    return CatalystClient().getApplicationsSiteHealth(**{'siteid': siteid, **kwargs})

@register('getApplicationsSitesHealth')
def getApplicationsSitesHealth(**kwargs):
    return CatalystClient().getApplicationsSitesHealth(**{**kwargs})

@register('getSupportedDeviceList')
def getSupportedDeviceList(**kwargs):
    return CatalystClient().getSupportedDeviceList(**{**kwargs})

@register('processStatisticsData')
def processStatisticsData():
    return CatalystClient().processStatisticsData(**{})

@register('getStatisticsProcessingCounters')
def getStatisticsProcessingCounters():
    return CatalystClient().getStatisticsProcessingCounters(**{})

@register('generateStatsProcessReport')
def generateStatsProcessReport(**kwargs):
    return CatalystClient().generateStatsProcessReport(**{**kwargs})

@register('generateStatsProcessThreadReport')
def generateStatsProcessThreadReport():
    return CatalystClient().generateStatsProcessThreadReport(**{})

@register('getStatDataRawData_3')
def getStatDataRawData_3(**kwargs):
    return CatalystClient().getStatDataRawData_3(**{**kwargs})

@register('getAggregationDataByQuery_15')
def getAggregationDataByQuery_15(**kwargs):
    return CatalystClient().getAggregationDataByQuery_15(**{**kwargs})

@register('getStatDataRawDataAsCSV_3')
def getStatDataRawDataAsCSV_3(**kwargs):
    return CatalystClient().getStatDataRawDataAsCSV_3(**{**kwargs})

@register('getCount_3')
def getCount_3(query: str):
    return CatalystClient().getCount_3(**{'query': query})

@register('getStatDataFields_4')
def getStatDataFields_4():
    return CatalystClient().getStatDataFields_4(**{})

@register('getStatsPaginationRawData_2')
def getStatsPaginationRawData_2(**kwargs):
    return CatalystClient().getStatsPaginationRawData_2(**{**kwargs})

@register('getStatQueryFields_4')
def getStatQueryFields_4():
    return CatalystClient().getStatQueryFields_4(**{})

@register('getStatDataRawData_13')
def getStatDataRawData_13(**kwargs):
    return CatalystClient().getStatDataRawData_13(**{**kwargs})

@register('getAggregationDataByQuery_13')
def getAggregationDataByQuery_13(**kwargs):
    return CatalystClient().getAggregationDataByQuery_13(**{**kwargs})

@register('getStatDataRawDataAsCSV12')
def getStatDataRawDataAsCSV12(**kwargs):
    return CatalystClient().getStatDataRawDataAsCSV12(**{**kwargs})

@register('getCount13')
def getCount13(query: str):
    return CatalystClient().getCount13(**{'query': query})

@register('getStatDataFields13')
def getStatDataFields13():
    return CatalystClient().getStatDataFields13(**{})

@register('getStatBulkRawData_2')
def getStatBulkRawData_2(**kwargs):
    return CatalystClient().getStatBulkRawData_2(**{**kwargs})

@register('getStatQueryFields_14')
def getStatQueryFields_14():
    return CatalystClient().getStatQueryFields_14(**{})

@register('getStatQueryFields_15')
def getStatQueryFields_15():
    return CatalystClient().getStatQueryFields_15(**{})

@register('getSdraHeadendSummary')
def getSdraHeadendSummary(**kwargs):
    return CatalystClient().getSdraHeadendSummary(**{**kwargs})

@register('getSdraSessionSummary')
def getSdraSessionSummary(**kwargs):
    return CatalystClient().getSdraSessionSummary(**{**kwargs})

@register('getDisabledDeviceList')
def getDisabledDeviceList(indexName: str):
    return CatalystClient().getDisabledDeviceList(**{'indexName': indexName})

@register('getStatisticsSettings')
def getStatisticsSettings():
    return CatalystClient().getStatisticsSettings(**{})

@register('getEnabledIndexForDevice')
def getEnabledIndexForDevice(deviceId: str):
    return CatalystClient().getEnabledIndexForDevice(**{'deviceId': deviceId})

@register('getStatDataRawData_15')
def getStatDataRawData_15(**kwargs):
    return CatalystClient().getStatDataRawData_15(**{**kwargs})

@register('getAggregationDataByQuery_16')
def getAggregationDataByQuery_16(**kwargs):
    return CatalystClient().getAggregationDataByQuery_16(**{**kwargs})

@register('getSiteHealth')
def getSiteHealth(**kwargs):
    return CatalystClient().getSiteHealth(**{**kwargs})

@register('getStatDataRawDataAsCSV_14')
def getStatDataRawDataAsCSV_14(**kwargs):
    return CatalystClient().getStatDataRawDataAsCSV_14(**{**kwargs})

@register('getCount_13')
def getCount_13(query: str):
    return CatalystClient().getCount_13(**{'query': query})

@register('getStatDataFields_15')
def getStatDataFields_15():
    return CatalystClient().getStatDataFields_15(**{})

@register('getStatsPaginationRawData_12')
def getStatsPaginationRawData_12(**kwargs):
    return CatalystClient().getStatsPaginationRawData_12(**{**kwargs})

@register('getStatQueryFields_16')
def getStatQueryFields_16():
    return CatalystClient().getStatQueryFields_16(**{})

@register('getSiteHealthTopology')
def getSiteHealthTopology(**kwargs):
    return CatalystClient().getSiteHealthTopology(**{**kwargs})

@register('getStatDataRawData_26')
def getStatDataRawData_26(**kwargs):
    return CatalystClient().getStatDataRawData_26(**{**kwargs})

@register('getAggregationDataByQuery_29')
def getAggregationDataByQuery_29(**kwargs):
    return CatalystClient().getAggregationDataByQuery_29(**{**kwargs})

@register('getStatDataRawDataAsCSV_27')
def getStatDataRawDataAsCSV_27(**kwargs):
    return CatalystClient().getStatDataRawDataAsCSV_27(**{**kwargs})

@register('getCount_25')
def getCount_25(query: str):
    return CatalystClient().getCount_25(**{'query': query})

@register('getStatDataFields_27')
def getStatDataFields_27():
    return CatalystClient().getStatDataFields_27(**{})

@register('getStatsPaginationRawData_25')
def getStatsPaginationRawData_25(**kwargs):
    return CatalystClient().getStatsPaginationRawData_25(**{**kwargs})

@register('getStatQueryFields_29')
def getStatQueryFields_29():
    return CatalystClient().getStatQueryFields_29(**{})

@register('getSulStatDataRawData')
def getSulStatDataRawData(**kwargs):
    return CatalystClient().getSulStatDataRawData(**{**kwargs})

@register('getAggregationDataByQuery_17')
def getAggregationDataByQuery_17(**kwargs):
    return CatalystClient().getAggregationDataByQuery_17(**{**kwargs})

@register('getStatDataRawDataAsCSV_15')
def getStatDataRawDataAsCSV_15(**kwargs):
    return CatalystClient().getStatDataRawDataAsCSV_15(**{**kwargs})

@register('getCount_14')
def getCount_14(query: str):
    return CatalystClient().getCount_14(**{'query': query})

@register('getStatDataFields_16')
def getStatDataFields_16():
    return CatalystClient().getStatDataFields_16(**{})

@register('getFilterPolicyNameList')
def getFilterPolicyNameList(policyType: str, query: str):
    return CatalystClient().getFilterPolicyNameList(**{'policyType': policyType, 'query': query})

@register('getStatsPaginationRawData_13')
def getStatsPaginationRawData_13(**kwargs):
    return CatalystClient().getStatsPaginationRawData_13(**{**kwargs})

@register('getStatQueryFields_17')
def getStatQueryFields_17():
    return CatalystClient().getStatQueryFields_17(**{})

@register('getStatDataRawData_17')
def getStatDataRawData_17(**kwargs):
    return CatalystClient().getStatDataRawData_17(**{**kwargs})

@register('getAggregationDataByQuery_19')
def getAggregationDataByQuery_19(**kwargs):
    return CatalystClient().getAggregationDataByQuery_19(**{**kwargs})

@register('createDeviceSystemCPUStat')
def createDeviceSystemCPUStat(deviceId: str, query: str):
    return CatalystClient().createDeviceSystemCPUStat(**{'deviceId': deviceId, 'query': query})

@register('getStatDataRawDataAsCSV_17')
def getStatDataRawDataAsCSV_17(**kwargs):
    return CatalystClient().getStatDataRawDataAsCSV_17(**{**kwargs})

@register('getCount_16')
def getCount_16(query: str):
    return CatalystClient().getCount_16(**{'query': query})

@register('getStatDataFields_18')
def getStatDataFields_18():
    return CatalystClient().getStatDataFields_18(**{})

@register('createDeviceSystemMemoryStat')
def createDeviceSystemMemoryStat(deviceId: str, query: str):
    return CatalystClient().createDeviceSystemMemoryStat(**{'deviceId': deviceId, 'query': query})

@register('getStatsPaginationRawData_15')
def getStatsPaginationRawData_15(**kwargs):
    return CatalystClient().getStatsPaginationRawData_15(**{**kwargs})

@register('getStatQueryFields_19')
def getStatQueryFields_19():
    return CatalystClient().getStatQueryFields_19(**{})

@register('getStatDataRawData_18')
def getStatDataRawData_18(**kwargs):
    return CatalystClient().getStatDataRawData_18(**{**kwargs})

@register('getAggregationDataByQuery_20')
def getAggregationDataByQuery_20(**kwargs):
    return CatalystClient().getAggregationDataByQuery_20(**{**kwargs})

@register('getStatDataRawDataAsCSV_18')
def getStatDataRawDataAsCSV_18(**kwargs):
    return CatalystClient().getStatDataRawDataAsCSV_18(**{**kwargs})

@register('getCount_17')
def getCount_17(query: str):
    return CatalystClient().getCount_17(**{'query': query})

@register('getStatDataFields_19')
def getStatDataFields_19():
    return CatalystClient().getStatDataFields_19(**{})

@register('getStatsPaginationRawData_16')
def getStatsPaginationRawData_16(**kwargs):
    return CatalystClient().getStatsPaginationRawData_16(**{**kwargs})

@register('getStatQueryFields_20')
def getStatQueryFields_20():
    return CatalystClient().getStatQueryFields_20(**{})

@register('statisticsApprouteTunnelhealthHistoryGet')
def statisticsApprouteTunnelhealthHistoryGet(**kwargs):
    return CatalystClient().statisticsApprouteTunnelhealthHistoryGet(**{**kwargs})

@register('statisticsApprouteTunnelhealthOverviewTypeGet')
def statisticsApprouteTunnelhealthOverviewTypeGet(type: str, **kwargs):
    return CatalystClient().statisticsApprouteTunnelhealthOverviewTypeGet(**{'type': type, **kwargs})

@register('getStatDataRawData_25')
def getStatDataRawData_25(**kwargs):
    return CatalystClient().getStatDataRawData_25(**{**kwargs})

@register('getAggregationDataByQuery_27')
def getAggregationDataByQuery_27(**kwargs):
    return CatalystClient().getAggregationDataByQuery_27(**{**kwargs})

@register('getStatDataRawDataAsCSV_25')
def getStatDataRawDataAsCSV_25(**kwargs):
    return CatalystClient().getStatDataRawDataAsCSV_25(**{**kwargs})

@register('getCount_24')
def getCount_24(query: str):
    return CatalystClient().getCount_24(**{'query': query})

@register('getStatDataFields_26')
def getStatDataFields_26():
    return CatalystClient().getStatDataFields_26(**{})

@register('getStatsPaginationRawData_23')
def getStatsPaginationRawData_23(**kwargs):
    return CatalystClient().getStatsPaginationRawData_23(**{**kwargs})

@register('getStatQueryFields_27')
def getStatQueryFields_27():
    return CatalystClient().getStatQueryFields_27(**{})

@register('getStatDataRawData_23')
def getStatDataRawData_23(**kwargs):
    return CatalystClient().getStatDataRawData_23(**{**kwargs})

@register('getAggregationDataByQuery_25')
def getAggregationDataByQuery_25(**kwargs):
    return CatalystClient().getAggregationDataByQuery_25(**{**kwargs})

@register('getStatDataRawDataAsCSV_23')
def getStatDataRawDataAsCSV_23(**kwargs):
    return CatalystClient().getStatDataRawDataAsCSV_23(**{**kwargs})

@register('getCount_22')
def getCount_22(query: str):
    return CatalystClient().getCount_22(**{'query': query})

@register('getStatDataFields_24')
def getStatDataFields_24():
    return CatalystClient().getStatDataFields_24(**{})

@register('getStatsPaginationRawData_21')
def getStatsPaginationRawData_21(**kwargs):
    return CatalystClient().getStatsPaginationRawData_21(**{**kwargs})

@register('getStatQueryFields_25')
def getStatQueryFields_25():
    return CatalystClient().getStatQueryFields_25(**{})

@register('getStatDataRawData_12')
def getStatDataRawData_12(**kwargs):
    return CatalystClient().getStatDataRawData_12(**{**kwargs})

@register('getAggregationDataByQuery_12')
def getAggregationDataByQuery_12(**kwargs):
    return CatalystClient().getAggregationDataByQuery_12(**{**kwargs})

@register('getStatDataRawDataAsCSV_12')
def getStatDataRawDataAsCSV_12(**kwargs):
    return CatalystClient().getStatDataRawDataAsCSV_12(**{**kwargs})

@register('getCount_11')
def getCount_11(query: str):
    return CatalystClient().getCount_11(**{'query': query})

@register('getStatDataFields_13')
def getStatDataFields_13():
    return CatalystClient().getStatDataFields_13(**{})

@register('getStatsPaginationRawData_10')
def getStatsPaginationRawData_10(**kwargs):
    return CatalystClient().getStatsPaginationRawData_10(**{**kwargs})

@register('getStatQueryFields_13')
def getStatQueryFields_13():
    return CatalystClient().getStatQueryFields_13(**{})

@register('getStatDataRawData_20')
def getStatDataRawData_20(**kwargs):
    return CatalystClient().getStatDataRawData_20(**{**kwargs})

@register('getAggregationDataByQuery_22')
def getAggregationDataByQuery_22(**kwargs):
    return CatalystClient().getAggregationDataByQuery_22(**{**kwargs})

@register('getStatDataRawDataAsCSV_20')
def getStatDataRawDataAsCSV_20(**kwargs):
    return CatalystClient().getStatDataRawDataAsCSV_20(**{**kwargs})

@register('getCount_19')
def getCount_19(query: str):
    return CatalystClient().getCount_19(**{'query': query})

@register('getStatDataFields_21')
def getStatDataFields_21():
    return CatalystClient().getStatDataFields_21(**{})

@register('getStatsPaginationRawData_18')
def getStatsPaginationRawData_18(**kwargs):
    return CatalystClient().getStatsPaginationRawData_18(**{**kwargs})

@register('getStatQueryFields_22')
def getStatQueryFields_22():
    return CatalystClient().getStatQueryFields_22(**{})

@register('disablePacketCaptureSession')
def disablePacketCaptureSession(sessionId: str):
    return CatalystClient().disablePacketCaptureSession(**{'sessionId': sessionId})

@register('downloadFile')
def downloadFile(sessionId: str):
    return CatalystClient().downloadFile(**{'sessionId': sessionId})

@register('forceStopPcapSession')
def forceStopPcapSession(sessionId: str):
    return CatalystClient().forceStopPcapSession(**{'sessionId': sessionId})

@register('startPcapSession')
def startPcapSession(sessionId: str):
    return CatalystClient().startPcapSession(**{'sessionId': sessionId})

@register('getFileDownloadStatus')
def getFileDownloadStatus(sessionId: str):
    return CatalystClient().getFileDownloadStatus(**{'sessionId': sessionId})

@register('stopPcapSession')
def stopPcapSession(sessionId: str):
    return CatalystClient().stopPcapSession(**{'sessionId': sessionId})

@register('getVnicInfoByVnfId')
def getVnicInfoByVnfId(vnfId: str):
    return CatalystClient().getVnicInfoByVnfId(**{'vnfId': vnfId})

@register('disableDeviceLog')
def disableDeviceLog(sessionId: str):
    return CatalystClient().disableDeviceLog(**{'sessionId': sessionId})

@register('downloadDebugLog')
def downloadDebugLog(sessionId: str):
    return CatalystClient().downloadDebugLog(**{'sessionId': sessionId})

@register('renewSessionInfo')
def renewSessionInfo(sessionId: str):
    return CatalystClient().renewSessionInfo(**{'sessionId': sessionId})

@register('getSessions')
def getSessions():
    return CatalystClient().getSessions(**{})

@register('clearSession')
def clearSession(sessionId: str):
    return CatalystClient().clearSession(**{'sessionId': sessionId})

@register('getLogType')
def getLogType(uuid: str):
    return CatalystClient().getLogType(**{'uuid': uuid})

@register('getDeviceLog')
def getDeviceLog(sessionId: str, **kwargs):
    return CatalystClient().getDeviceLog(**{'sessionId': sessionId, **kwargs})

@register('activeFlowWithQuery')
def activeFlowWithQuery(timestamp: int, traceId: int, **kwargs):
    return CatalystClient().activeFlowWithQuery(**{'timestamp': timestamp, 'traceId': traceId, **kwargs})

@register('getAggFlow')
def getAggFlow(timestamp: int, traceId: int, traceState: str, **kwargs):
    return CatalystClient().getAggFlow(**{'timestamp': timestamp, 'traceId': traceId, 'traceState': traceState, **kwargs})

@register('getAppQosData')
def getAppQosData(receivedTimestamp: int, timestamp: int, traceId: int, **kwargs):
    return CatalystClient().getAppQosData(**{'receivedTimestamp': receivedTimestamp, 'timestamp': timestamp, 'traceId': traceId, **kwargs})

@register('getAppQosState')
def getAppQosState(timestamp: int, traceId: int, traceState: str):
    return CatalystClient().getAppQosState(**{'timestamp': timestamp, 'traceId': traceId, 'traceState': traceState})

@register('getConcurrentData')
def getConcurrentData(timestamp: int, traceId: int):
    return CatalystClient().getConcurrentData(**{'timestamp': timestamp, 'traceId': traceId})

@register('getConcurrentDomainData')
def getConcurrentDomainData(timestamp: int, traceId: int, **kwargs):
    return CatalystClient().getConcurrentDomainData(**{'timestamp': timestamp, 'traceId': traceId, **kwargs})

@register('getCurrentTimestamp')
def getCurrentTimestamp():
    return CatalystClient().getCurrentTimestamp(**{})

@register('getDeviceBList')
def getDeviceBList():
    return CatalystClient().getDeviceBList(**{})

@register('getDevicesAndInterfacesBySite')
def getDevicesAndInterfacesBySite(site_id: str, **kwargs):
    return CatalystClient().getDevicesAndInterfacesBySite(**{'site_id': site_id, **kwargs})

@register('getDomainMetric')
def getDomainMetric(domain: str, firstTimestamp: int, lastTimestamp: int, timestamp: int, traceId: int, **kwargs):
    return CatalystClient().getDomainMetric(**{'domain': domain, 'firstTimestamp': firstTimestamp, 'lastTimestamp': lastTimestamp, 'timestamp': timestamp, 'traceId': traceId, **kwargs})

@register('getEventAppHopList')
def getEventAppHopList(timestamp: int, traceId: int, **kwargs):
    return CatalystClient().getEventAppHopList(**{'timestamp': timestamp, 'traceId': traceId, **kwargs})

@register('getEventAppScoreBandwidth')
def getEventAppScoreBandwidth(receivedTimestamp: int, timestamp: int, traceId: int, **kwargs):
    return CatalystClient().getEventAppScoreBandwidth(**{'receivedTimestamp': receivedTimestamp, 'timestamp': timestamp, 'traceId': traceId, **kwargs})

@register('getEventFlowFromAppHop')
def getEventFlowFromAppHop(deviceTraceId: int, direction: str, from_arg: str, timestamp: int, to: str, traceId: int, **kwargs):
    return CatalystClient().getEventFlowFromAppHop(**{'deviceTraceId': deviceTraceId, 'direction': direction, 'from': from_arg, 'timestamp': timestamp, 'to': to, 'traceId': traceId, **kwargs})

@register('getEventReadout')
def getEventReadout(timestamp: int, traceId: int, **kwargs):
    return CatalystClient().getEventReadout(**{'timestamp': timestamp, 'traceId': traceId, **kwargs})

@register('getEventReadoutBySite')
def getEventReadoutBySite(last_n_hours: int, site_id: str, **kwargs):
    return CatalystClient().getEventReadoutBySite(**{'last_n_hours': last_n_hours, 'site_id': site_id, **kwargs})

@register('getEventReadoutByTraces')
def getEventReadoutByTraces(entry_time: list, trace_id: list, **kwargs):
    return CatalystClient().getEventReadoutByTraces(**{'entry_time': entry_time, 'trace_id': trace_id, **kwargs})

@register('exportTrace')
def exportTrace(timestamp: int, traceId: int):
    return CatalystClient().exportTrace(**{'timestamp': timestamp, 'traceId': traceId})

@register('getFinalizedData')
def getFinalizedData(timestamp: int, traceId: int):
    return CatalystClient().getFinalizedData(**{'timestamp': timestamp, 'traceId': traceId})

@register('getFinalizedDomainData')
def getFinalizedDomainData(timestamp: int, traceId: int, **kwargs):
    return CatalystClient().getFinalizedDomainData(**{'timestamp': timestamp, 'traceId': traceId, **kwargs})

@register('getFlowDetail')
def getFlowDetail(flowId: int, timestamp: int, traceId: int):
    return CatalystClient().getFlowDetail(**{'flowId': flowId, 'timestamp': timestamp, 'traceId': traceId})

@register('getFlowMetric')
def getFlowMetric(firstTimestamp: int, flowId: int, lastTimestamp: int, timestamp: int, traceId: int):
    return CatalystClient().getFlowMetric(**{'firstTimestamp': firstTimestamp, 'flowId': flowId, 'lastTimestamp': lastTimestamp, 'timestamp': timestamp, 'traceId': traceId})

@register('getMonitorState')
def getMonitorState(state: str, traceId: int):
    return CatalystClient().getMonitorState(**{'state': state, 'traceId': traceId})

@register('getNwpiDscp')
def getNwpiDscp():
    return CatalystClient().getNwpiDscp(**{})

@register('getNwpiNbarAppGroup')
def getNwpiNbarAppGroup():
    return CatalystClient().getNwpiNbarAppGroup(**{})

@register('getNwpiProtocol')
def getNwpiProtocol():
    return CatalystClient().getNwpiProtocol(**{})

@register('nwpiSettingView')
def nwpiSettingView(**kwargs):
    return CatalystClient().nwpiSettingView(**{**kwargs})

@register('getPacketFeatures')
def getPacketFeatures(flowId: int, timestamp: int, traceId: int):
    return CatalystClient().getPacketFeatures(**{'flowId': flowId, 'timestamp': timestamp, 'traceId': traceId})

@register('getPreloadInfo')
def getPreloadInfo(**kwargs):
    return CatalystClient().getPreloadInfo(**{**kwargs})

@register('getStatQueryFields_28')
def getStatQueryFields_28():
    return CatalystClient().getStatQueryFields_28(**{})

@register('getRoutingDetailFromLocal')
def getRoutingDetailFromLocal(routePrefixs: str, timestamp: int, traceId: int, traceState: str):
    return CatalystClient().getRoutingDetailFromLocal(**{'routePrefixs': routePrefixs, 'timestamp': timestamp, 'traceId': traceId, 'traceState': traceState})

@register('getEventStatsData')
def getEventStatsData(duration: int, state: str, taskEndTime: int, taskId: int):
    return CatalystClient().getEventStatsData(**{'duration': duration, 'state': state, 'taskEndTime': taskEndTime, 'taskId': taskId})

@register('getTaskHistory')
def getTaskHistory():
    return CatalystClient().getTaskHistory(**{})

@register('getTaskTrace')
def getTaskTrace(taskId: str):
    return CatalystClient().getTaskTrace(**{'taskId': taskId})

@register('getTraceCftRecord')
def getTraceCftRecord(entryTime: int, traceId: int, traceState: str, **kwargs):
    return CatalystClient().getTraceCftRecord(**{'entryTime': entryTime, 'traceId': traceId, 'traceState': traceState, **kwargs})

@register('getFinalizedFlowCount')
def getFinalizedFlowCount(timestamp: int, traceId: int):
    return CatalystClient().getFinalizedFlowCount(**{'timestamp': timestamp, 'traceId': traceId})

@register('getFinFlowTimeRange')
def getFinFlowTimeRange(state: str, timestamp: int, traceId: int):
    return CatalystClient().getFinFlowTimeRange(**{'state': state, 'timestamp': timestamp, 'traceId': traceId})

@register('traceFinFlowWithQuery')
def traceFinFlowWithQuery(timestamp: int, traceId: int, **kwargs):
    return CatalystClient().traceFinFlowWithQuery(**{'timestamp': timestamp, 'traceId': traceId, **kwargs})

@register('getTraceFlow')
def getTraceFlow(state: str, timestamp: int, traceId: int):
    return CatalystClient().getTraceFlow(**{'state': state, 'timestamp': timestamp, 'traceId': traceId})

@register('getTraceHistory')
def getTraceHistory(**kwargs):
    return CatalystClient().getTraceHistory(**{**kwargs})

@register('getTraceInfoByBaseKey')
def getTraceInfoByBaseKey(entryTime: int, traceId: int, **kwargs):
    return CatalystClient().getTraceInfoByBaseKey(**{'entryTime': entryTime, 'traceId': traceId, **kwargs})

@register('getTraceReadoutFilter')
def getTraceReadoutFilter(entry_time: list, trace_id: list):
    return CatalystClient().getTraceReadoutFilter(**{'entry_time': entry_time, 'trace_id': trace_id})

@register('disableSpeedTestSession')
def disableSpeedTestSession(sessionId: str):
    return CatalystClient().disableSpeedTestSession(**{'sessionId': sessionId})

@register('getInterfaceBandwidth')
def getInterfaceBandwidth(deviceUUID: str, **kwargs):
    return CatalystClient().getInterfaceBandwidth(**{'deviceUUID': deviceUUID, **kwargs})

@register('startSpeedTest')
def startSpeedTest(sessionId: str):
    return CatalystClient().startSpeedTest(**{'sessionId': sessionId})

@register('getSpeedTestStatus')
def getSpeedTestStatus(sessionId: str):
    return CatalystClient().getSpeedTestStatus(**{'sessionId': sessionId})

@register('stopSpeedTest')
def stopSpeedTest(sessionId: str):
    return CatalystClient().stopSpeedTest(**{'sessionId': sessionId})

@register('getSpeedTest')
def getSpeedTest(sessionId: str, **kwargs):
    return CatalystClient().getSpeedTest(**{'sessionId': sessionId, **kwargs})

@register('getUMTSData')
def getUMTSData(deviceUUID: str, eventType: str, **kwargs):
    return CatalystClient().getUMTSData(**{'deviceUUID': deviceUUID, 'eventType': eventType, **kwargs})

@register('updateUmtsSessionStatus')
def updateUmtsSessionStatus(operation: str, sessionId: str):
    return CatalystClient().updateUmtsSessionStatus(**{'operation': operation, 'sessionId': sessionId})

@register('generateBootstrapConfigForVedge')
def generateBootstrapConfigForVedge(configtype: str, inclDefRootCert: bool, uuid: str, **kwargs):
    return CatalystClient().generateBootstrapConfigForVedge(**{'configtype': configtype, 'inclDefRootCert': inclDefRootCert, 'uuid': uuid, **kwargs})

@register('getBootstrapConfigZip')
def getBootstrapConfigZip(id: str):
    return CatalystClient().getBootstrapConfigZip(**{'id': id})

@register('generateGenericBootstrapConfigForVedges')
def generateGenericBootstrapConfigForVedges(**kwargs):
    return CatalystClient().generateGenericBootstrapConfigForVedges(**{**kwargs})

@register('getControllerVEdgeSyncStatus_1')
def getControllerVEdgeSyncStatus_1():
    return CatalystClient().getControllerVEdgeSyncStatus_1(**{})

@register('devicesWithoutSubjectSudi')
def devicesWithoutSubjectSudi():
    return CatalystClient().devicesWithoutSubjectSudi(**{})

@register('getManagementSystemIPInfo_1')
def getManagementSystemIPInfo_1():
    return CatalystClient().getManagementSystemIPInfo_1(**{})

@register('getRMACandidates')
def getRMACandidates(deviceType: str, **kwargs):
    return CatalystClient().getRMACandidates(**{'deviceType': deviceType, **kwargs})

@register('getRootCertStatusAll')
def getRootCertStatusAll(state: str):
    return CatalystClient().getRootCertStatusAll(**{'state': state})

@register('checkSelfSignedCert_1')
def checkSelfSignedCert_1():
    return CatalystClient().checkSelfSignedCert_1(**{})

@register('syncRootCertChain')
def syncRootCertChain():
    return CatalystClient().syncRootCertChain(**{})

@register('getTenantManagementSystemIPs')
def getTenantManagementSystemIPs():
    return CatalystClient().getTenantManagementSystemIPs(**{})

@register('getCloudDockDataBasedOnDeviceType')
def getCloudDockDataBasedOnDeviceType(deviceCategory: str):
    return CatalystClient().getCloudDockDataBasedOnDeviceType(**{'deviceCategory': deviceCategory})

@register('getCloudDockDefaultConfigBasedOnDeviceType')
def getCloudDockDefaultConfigBasedOnDeviceType(deviceCategory: str):
    return CatalystClient().getCloudDockDefaultConfigBasedOnDeviceType(**{'deviceCategory': deviceCategory})

@register('getAllUnclaimedDevices')
def getAllUnclaimedDevices():
    return CatalystClient().getAllUnclaimedDevices(**{})

@register('checkvEdgeDevicePresence')
def checkvEdgeDevicePresence():
    return CatalystClient().checkvEdgeDevicePresence(**{})

@register('getDevicesDetails')
def getDevicesDetails(deviceCategory: str, **kwargs):
    return CatalystClient().getDevicesDetails(**{'deviceCategory': deviceCategory, **kwargs})

@register('getReverseProxyMappings')
def getReverseProxyMappings(uuid: str):
    return CatalystClient().getReverseProxyMappings(**{'uuid': uuid})

@register('getCloudXStatus')
def getCloudXStatus():
    return CatalystClient().getCloudXStatus(**{})

@register('getAttachedClientList')
def getAttachedClientList():
    return CatalystClient().getAttachedClientList(**{})

@register('getAttachedDiaList')
def getAttachedDiaList():
    return CatalystClient().getAttachedDiaList(**{})

@register('getAttachedGatewayList')
def getAttachedGatewayList():
    return CatalystClient().getAttachedGatewayList(**{})

@register('getCloudXAvailableApps')
def getCloudXAvailableApps():
    return CatalystClient().getCloudXAvailableApps(**{})

@register('getSiteList')
def getSiteList():
    return CatalystClient().getSiteList(**{})

@register('getDiaList')
def getDiaList():
    return CatalystClient().getDiaList(**{})

@register('getGatewayList')
def getGatewayList():
    return CatalystClient().getGatewayList(**{})

@register('getApps')
def getApps():
    return CatalystClient().getApps(**{})

@register('getSigTunnelList_1')
def getSigTunnelList_1(deviceId: str):
    return CatalystClient().getSigTunnelList_1(**{'deviceId': deviceId})

@register('sitePerApp')
def sitePerApp(appName: str, **kwargs):
    return CatalystClient().sitePerApp(**{'appName': appName, **kwargs})

@register('getAttachedConfig')
def getAttachedConfig(deviceId: str, **kwargs):
    return CatalystClient().getAttachedConfig(**{'deviceId': deviceId, **kwargs})

@register('generateCLIModeDevices')
def generateCLIModeDevices(type: str):
    return CatalystClient().generateCLIModeDevices(**{'type': type})

@register('generatevManageModeDevices')
def generatevManageModeDevices(type: str):
    return CatalystClient().generatevManageModeDevices(**{'type': type})

@register('getDeviceDiff')
def getDeviceDiff(deviceId: str):
    return CatalystClient().getDeviceDiff(**{'deviceId': deviceId})

@register('getCompatibleDevices')
def getCompatibleDevices(oldDeviceId: str):
    return CatalystClient().getCompatibleDevices(**{'oldDeviceId': oldDeviceId})

@register('getRunningConfig')
def getRunningConfig(deviceId: str):
    return CatalystClient().getRunningConfig(**{'deviceId': deviceId})

@register('getVpnForDevice')
def getVpnForDevice(deviceId: str):
    return CatalystClient().getVpnForDevice(**{'deviceId': deviceId})

@register('getCORStatus')
def getCORStatus():
    return CatalystClient().getCORStatus(**{})

@register('getAmiList')
def getAmiList(accountid: str, cloudregion: str, **kwargs):
    return CatalystClient().getAmiList(**{'accountid': accountid, 'cloudregion': cloudregion, **kwargs})

@register('getCloudList')
def getCloudList():
    return CatalystClient().getCloudList(**{})

@register('getCloudAccounts')
def getCloudAccounts(cloudEnvironment: str, cloudtype: str):
    return CatalystClient().getCloudAccounts(**{'cloudEnvironment': cloudEnvironment, 'cloudtype': cloudtype})

@register('getCloudHostVpcAccountDetails')
def getCloudHostVpcAccountDetails():
    return CatalystClient().getCloudHostVpcAccountDetails(**{})

@register('getCloudMappedHostAccounts')
def getCloudMappedHostAccounts(accountid: str, cloudtype: str):
    return CatalystClient().getCloudMappedHostAccounts(**{'accountid': accountid, 'cloudtype': cloudtype})

@register('getCloudOnRampDevices')
def getCloudOnRampDevices():
    return CatalystClient().getCloudOnRampDevices(**{})

@register('getHostVPCs')
def getHostVPCs(devicePairId: str, transitVpcId: str):
    return CatalystClient().getHostVPCs(**{'devicePairId': devicePairId, 'transitVpcId': transitVpcId})

@register('getExternalId')
def getExternalId():
    return CatalystClient().getExternalId(**{})

@register('getTransitDevicePairAndHostList')
def getTransitDevicePairAndHostList(accountId: str, cloudRegion: str):
    return CatalystClient().getTransitDevicePairAndHostList(**{'accountId': accountId, 'cloudRegion': cloudRegion})

@register('getTransitVpcVpnList')
def getTransitVpcVpnList(accountId: str):
    return CatalystClient().getTransitVpcVpnList(**{'accountId': accountId})

@register('getCloudHostVPCs')
def getCloudHostVPCs(accountid: str, cloudregion: str, **kwargs):
    return CatalystClient().getCloudHostVPCs(**{'accountid': accountid, 'cloudregion': cloudregion, **kwargs})

@register('getMappedVPCs')
def getMappedVPCs(accountid: str, cloudregion: str):
    return CatalystClient().getMappedVPCs(**{'accountid': accountid, 'cloudregion': cloudregion})

@register('getPemKeyList')
def getPemKeyList(accountid: str, cloudregion: str, cloudtype: str):
    return CatalystClient().getPemKeyList(**{'accountid': accountid, 'cloudregion': cloudregion, 'cloudtype': cloudtype})

@register('getTransitVPCs')
def getTransitVPCs(accountid: str, cloudregion: str, **kwargs):
    return CatalystClient().getTransitVPCs(**{'accountid': accountid, 'cloudregion': cloudregion, **kwargs})

@register('getTransitVPCSupportedSize')
def getTransitVPCSupportedSize(cloudEnvironment: str, **kwargs):
    return CatalystClient().getTransitVPCSupportedSize(**{'cloudEnvironment': cloudEnvironment, **kwargs})

@register('getCortexStatus')
def getCortexStatus():
    return CatalystClient().getCortexStatus(**{})

@register('getMappedWanResourceGroups')
def getMappedWanResourceGroups(accountid: str, cloudregion: str):
    return CatalystClient().getMappedWanResourceGroups(**{'accountid': accountid, 'cloudregion': cloudregion})

@register('getWanResourceGroups')
def getWanResourceGroups(accountid: str):
    return CatalystClient().getWanResourceGroups(**{'accountid': accountid})

@register('generateMasterTemplateList')
def generateMasterTemplateList(feature: str):
    return CatalystClient().generateMasterTemplateList(**{'feature': feature})

@register('getAttachedDeviceList')
def getAttachedDeviceList(masterTemplateId: str):
    return CatalystClient().getAttachedDeviceList(**{'masterTemplateId': masterTemplateId})

@register('getAttachedConfigToDevice')
def getAttachedConfigToDevice(deviceId: str, **kwargs):
    return CatalystClient().getAttachedConfigToDevice(**{'deviceId': deviceId, **kwargs})

@register('getDeviceListByMasterTemplateId')
def getDeviceListByMasterTemplateId(masterTemplateId: str):
    return CatalystClient().getDeviceListByMasterTemplateId(**{'masterTemplateId': masterTemplateId})

@register('checkVbond')
def checkVbond():
    return CatalystClient().checkVbond(**{})

@register('isMigrationRequired')
def isMigrationRequired():
    return CatalystClient().isMigrationRequired(**{})

@register('generateTemplateForMigration')
def generateTemplateForMigration(**kwargs):
    return CatalystClient().generateTemplateForMigration(**{**kwargs})

@register('migrationInfo')
def migrationInfo():
    return CatalystClient().migrationInfo(**{})

@register('getMasterTemplateDefinition')
def getMasterTemplateDefinition(templateId: str):
    return CatalystClient().getMasterTemplateDefinition(**{'templateId': templateId})

@register('getOutOfSyncTemplates')
def getOutOfSyncTemplates():
    return CatalystClient().getOutOfSyncTemplates(**{})

@register('getOutOfSyncDevices')
def getOutOfSyncDevices(templateId: str):
    return CatalystClient().getOutOfSyncDevices(**{'templateId': templateId})

@register('getAssociatedFeatureTemplatesDetails')
def getAssociatedFeatureTemplatesDetails(templateId: str):
    return CatalystClient().getAssociatedFeatureTemplatesDetails(**{'templateId': templateId})

@register('generateFeatureTemplateList')
def generateFeatureTemplateList(**kwargs):
    return CatalystClient().generateFeatureTemplateList(**{**kwargs})

@register('getNetworkInterface')
def getNetworkInterface(deviceModel: str):
    return CatalystClient().getNetworkInterface(**{'deviceModel': deviceModel})

@register('getDefaultNetworks')
def getDefaultNetworks(deviceModel: str):
    return CatalystClient().getDefaultNetworks(**{'deviceModel': deviceModel})

@register('getTemplateDefinition')
def getTemplateDefinition(templateId: str):
    return CatalystClient().getTemplateDefinition(**{'templateId': templateId})

@register('getDeviceTemplatesAttachedToFeature')
def getDeviceTemplatesAttachedToFeature(templateId: str):
    return CatalystClient().getDeviceTemplatesAttachedToFeature(**{'templateId': templateId})

@register('listLITemplate')
def listLITemplate():
    return CatalystClient().listLITemplate(**{})

@register('generateMasterTemplateDefinition')
def generateMasterTemplateDefinition(type_name: str):
    return CatalystClient().generateMasterTemplateDefinition(**{'type_name': type_name})

@register('getTemplateForMigration')
def getTemplateForMigration():
    return CatalystClient().getTemplateForMigration(**{})

@register('getGeneralTemplate')
def getGeneralTemplate(templateId: str):
    return CatalystClient().getGeneralTemplate(**{'templateId': templateId})

@register('generateTemplateTypes')
def generateTemplateTypes(type: str):
    return CatalystClient().generateTemplateTypes(**{'type': type})

@register('generateTemplateTypeDefinition')
def generateTemplateTypeDefinition(type_name: str, version: str):
    return CatalystClient().generateTemplateTypeDefinition(**{'type_name': type_name, 'version': version})

@register('generateTemplateByDeviceType')
def generateTemplateByDeviceType(deviceType: str):
    return CatalystClient().generateTemplateByDeviceType(**{'deviceType': deviceType})

@register('previewById')
def previewById(id: str):
    return CatalystClient().previewById(**{'id': id})

@register('previewById_1')
def previewById_1(id: str):
    return CatalystClient().previewById_1(**{'id': id})

@register('previewById_2')
def previewById_2(id: str):
    return CatalystClient().previewById_2(**{'id': id})

@register('previewById_3')
def previewById_3(id: str):
    return CatalystClient().previewById_3(**{'id': id})

@register('getCloudDiscoveredApps')
def getCloudDiscoveredApps():
    return CatalystClient().getCloudDiscoveredApps(**{})

@register('getCustomApps')
def getCustomApps():
    return CatalystClient().getCustomApps(**{})

@register('getCustomAppById')
def getCustomAppById(id: str):
    return CatalystClient().getCustomAppById(**{'id': id})

@register('getDefinitions_8')
def getDefinitions_8():
    return CatalystClient().getDefinitions_8(**{})

@register('previewPolicyDefinitionById_8')
def previewPolicyDefinitionById_8(id: str):
    return CatalystClient().previewPolicyDefinitionById_8(**{'id': id})

@register('getPolicyDefinition_8')
def getPolicyDefinition_8(id: str):
    return CatalystClient().getPolicyDefinition_8(**{'id': id})

@register('getDefinitions_9')
def getDefinitions_9():
    return CatalystClient().getDefinitions_9(**{})

@register('previewPolicyDefinitionById_9')
def previewPolicyDefinitionById_9(id: str):
    return CatalystClient().previewPolicyDefinitionById_9(**{'id': id})

@register('getPolicyDefinition_9')
def getPolicyDefinition_9(id: str):
    return CatalystClient().getPolicyDefinition_9(**{'id': id})

@register('getDefinitions_11')
def getDefinitions_11():
    return CatalystClient().getDefinitions_11(**{})

@register('previewPolicyDefinitionById_11')
def previewPolicyDefinitionById_11(id: str):
    return CatalystClient().previewPolicyDefinitionById_11(**{'id': id})

@register('getPolicyDefinition_11')
def getPolicyDefinition_11(id: str):
    return CatalystClient().getPolicyDefinition_11(**{'id': id})

@register('getDefinitions_10')
def getDefinitions_10():
    return CatalystClient().getDefinitions_10(**{})

@register('previewPolicyDefinitionById_10')
def previewPolicyDefinitionById_10(id: str):
    return CatalystClient().previewPolicyDefinitionById_10(**{'id': id})

@register('getPolicyDefinition_10')
def getPolicyDefinition_10(id: str):
    return CatalystClient().getPolicyDefinition_10(**{'id': id})

@register('getDefinitions_12')
def getDefinitions_12():
    return CatalystClient().getDefinitions_12(**{})

@register('previewPolicyDefinitionById_12')
def previewPolicyDefinitionById_12(id: str):
    return CatalystClient().previewPolicyDefinitionById_12(**{'id': id})

@register('getPolicyDefinition_12')
def getPolicyDefinition_12(id: str):
    return CatalystClient().getPolicyDefinition_12(**{'id': id})

@register('getDefinitions_13')
def getDefinitions_13():
    return CatalystClient().getDefinitions_13(**{})

@register('previewPolicyDefinitionById_13')
def previewPolicyDefinitionById_13(id: str):
    return CatalystClient().previewPolicyDefinitionById_13(**{'id': id})

@register('getPolicyDefinition_13')
def getPolicyDefinition_13(id: str):
    return CatalystClient().getPolicyDefinition_13(**{'id': id})

@register('getDefinitions_14')
def getDefinitions_14():
    return CatalystClient().getDefinitions_14(**{})

@register('previewPolicyDefinitionById_14')
def previewPolicyDefinitionById_14(id: str):
    return CatalystClient().previewPolicyDefinitionById_14(**{'id': id})

@register('getPolicyDefinition_14')
def getPolicyDefinition_14(id: str):
    return CatalystClient().getPolicyDefinition_14(**{'id': id})

@register('getDefinitions_15')
def getDefinitions_15():
    return CatalystClient().getDefinitions_15(**{})

@register('previewPolicyDefinitionById_15')
def previewPolicyDefinitionById_15(id: str):
    return CatalystClient().previewPolicyDefinitionById_15(**{'id': id})

@register('getPolicyDefinition_15')
def getPolicyDefinition_15(id: str):
    return CatalystClient().getPolicyDefinition_15(**{'id': id})

@register('getDefinitions_16')
def getDefinitions_16():
    return CatalystClient().getDefinitions_16(**{})

@register('previewPolicyDefinitionById_16')
def previewPolicyDefinitionById_16(id: str):
    return CatalystClient().previewPolicyDefinitionById_16(**{'id': id})

@register('getPolicyDefinition_16')
def getPolicyDefinition_16(id: str):
    return CatalystClient().getPolicyDefinition_16(**{'id': id})

@register('getDefinitions_17')
def getDefinitions_17():
    return CatalystClient().getDefinitions_17(**{})

@register('previewPolicyDefinitionById_17')
def previewPolicyDefinitionById_17(id: str):
    return CatalystClient().previewPolicyDefinitionById_17(**{'id': id})

@register('getPolicyDefinition_17')
def getPolicyDefinition_17(id: str):
    return CatalystClient().getPolicyDefinition_17(**{'id': id})

@register('getDefinitions_25')
def getDefinitions_25():
    return CatalystClient().getDefinitions_25(**{})

@register('previewPolicyDefinitionById_25')
def previewPolicyDefinitionById_25(id: str):
    return CatalystClient().previewPolicyDefinitionById_25(**{'id': id})

@register('getPolicyDefinition_25')
def getPolicyDefinition_25(id: str):
    return CatalystClient().getPolicyDefinition_25(**{'id': id})

@register('getDefinitions')
def getDefinitions():
    return CatalystClient().getDefinitions(**{})

@register('previewPolicyDefinitionById')
def previewPolicyDefinitionById(id: str):
    return CatalystClient().previewPolicyDefinitionById(**{'id': id})

@register('getPolicyDefinition')
def getPolicyDefinition(id: str):
    return CatalystClient().getPolicyDefinition(**{'id': id})

@register('getDefinitions_26')
def getDefinitions_26():
    return CatalystClient().getDefinitions_26(**{})

@register('previewPolicyDefinitionById_26')
def previewPolicyDefinitionById_26(id: str):
    return CatalystClient().previewPolicyDefinitionById_26(**{'id': id})

@register('getPolicyDefinition_26')
def getPolicyDefinition_26(id: str):
    return CatalystClient().getPolicyDefinition_26(**{'id': id})

@register('getDefinitions_28')
def getDefinitions_28():
    return CatalystClient().getDefinitions_28(**{})

@register('previewPolicyDefinitionById_28')
def previewPolicyDefinitionById_28(id: str):
    return CatalystClient().previewPolicyDefinitionById_28(**{'id': id})

@register('getPolicyDefinition_28')
def getPolicyDefinition_28(id: str):
    return CatalystClient().getPolicyDefinition_28(**{'id': id})

@register('getDefinitions_27')
def getDefinitions_27():
    return CatalystClient().getDefinitions_27(**{})

@register('previewPolicyDefinitionById_27')
def previewPolicyDefinitionById_27(id: str):
    return CatalystClient().previewPolicyDefinitionById_27(**{'id': id})

@register('getPolicyDefinition_27')
def getPolicyDefinition_27(id: str):
    return CatalystClient().getPolicyDefinition_27(**{'id': id})

@register('getDefinitions_4')
def getDefinitions_4():
    return CatalystClient().getDefinitions_4(**{})

@register('previewPolicyDefinitionById_4')
def previewPolicyDefinitionById_4(id: str):
    return CatalystClient().previewPolicyDefinitionById_4(**{'id': id})

@register('getPolicyDefinition_4')
def getPolicyDefinition_4(id: str):
    return CatalystClient().getPolicyDefinition_4(**{'id': id})

@register('getDefinitions_18')
def getDefinitions_18():
    return CatalystClient().getDefinitions_18(**{})

@register('previewPolicyDefinitionById_18')
def previewPolicyDefinitionById_18(id: str):
    return CatalystClient().previewPolicyDefinitionById_18(**{'id': id})

@register('getPolicyDefinition_18')
def getPolicyDefinition_18(id: str):
    return CatalystClient().getPolicyDefinition_18(**{'id': id})

@register('getDefinitions_5')
def getDefinitions_5():
    return CatalystClient().getDefinitions_5(**{})

@register('previewPolicyDefinitionById_5')
def previewPolicyDefinitionById_5(id: str):
    return CatalystClient().previewPolicyDefinitionById_5(**{'id': id})

@register('getPolicyDefinition_5')
def getPolicyDefinition_5(id: str):
    return CatalystClient().getPolicyDefinition_5(**{'id': id})

@register('getDefinitions_29')
def getDefinitions_29():
    return CatalystClient().getDefinitions_29(**{})

@register('previewPolicyDefinitionById_29')
def previewPolicyDefinitionById_29(id: str):
    return CatalystClient().previewPolicyDefinitionById_29(**{'id': id})

@register('getPolicyDefinition_29')
def getPolicyDefinition_29(id: str):
    return CatalystClient().getPolicyDefinition_29(**{'id': id})

@register('getDefinitions_1')
def getDefinitions_1():
    return CatalystClient().getDefinitions_1(**{})

@register('previewPolicyDefinitionById_1')
def previewPolicyDefinitionById_1(id: str):
    return CatalystClient().previewPolicyDefinitionById_1(**{'id': id})

@register('getPolicyDefinition_1')
def getPolicyDefinition_1(id: str):
    return CatalystClient().getPolicyDefinition_1(**{'id': id})

@register('getDefinitions_19')
def getDefinitions_19():
    return CatalystClient().getDefinitions_19(**{})

@register('previewPolicyDefinitionById_19')
def previewPolicyDefinitionById_19(id: str):
    return CatalystClient().previewPolicyDefinitionById_19(**{'id': id})

@register('getPolicyDefinition_19')
def getPolicyDefinition_19(id: str):
    return CatalystClient().getPolicyDefinition_19(**{'id': id})

@register('getDefinitions_20')
def getDefinitions_20():
    return CatalystClient().getDefinitions_20(**{})

@register('previewPolicyDefinitionById_20')
def previewPolicyDefinitionById_20(id: str):
    return CatalystClient().previewPolicyDefinitionById_20(**{'id': id})

@register('getPolicyDefinition_20')
def getPolicyDefinition_20(id: str):
    return CatalystClient().getPolicyDefinition_20(**{'id': id})

@register('getDefinitions_21')
def getDefinitions_21():
    return CatalystClient().getDefinitions_21(**{})

@register('previewPolicyDefinitionById_21')
def previewPolicyDefinitionById_21(id: str):
    return CatalystClient().previewPolicyDefinitionById_21(**{'id': id})

@register('getPolicyDefinition_21')
def getPolicyDefinition_21(id: str):
    return CatalystClient().getPolicyDefinition_21(**{'id': id})

@register('getDefinitions_30')
def getDefinitions_30():
    return CatalystClient().getDefinitions_30(**{})

@register('previewPolicyDefinitionById_30')
def previewPolicyDefinitionById_30(id: str):
    return CatalystClient().previewPolicyDefinitionById_30(**{'id': id})

@register('getPolicyDefinition_30')
def getPolicyDefinition_30(id: str):
    return CatalystClient().getPolicyDefinition_30(**{'id': id})

@register('getDefinitions_3')
def getDefinitions_3():
    return CatalystClient().getDefinitions_3(**{})

@register('previewPolicyDefinitionById_3')
def previewPolicyDefinitionById_3(id: str):
    return CatalystClient().previewPolicyDefinitionById_3(**{'id': id})

@register('getPolicyDefinition_3')
def getPolicyDefinition_3(id: str):
    return CatalystClient().getPolicyDefinition_3(**{'id': id})

@register('getDefinitions_22')
def getDefinitions_22():
    return CatalystClient().getDefinitions_22(**{})

@register('previewPolicyDefinitionById_22')
def previewPolicyDefinitionById_22(id: str):
    return CatalystClient().previewPolicyDefinitionById_22(**{'id': id})

@register('getPolicyDefinition_22')
def getPolicyDefinition_22(id: str):
    return CatalystClient().getPolicyDefinition_22(**{'id': id})

@register('getDefinitions_23')
def getDefinitions_23():
    return CatalystClient().getDefinitions_23(**{})

@register('previewPolicyDefinitionById_23')
def previewPolicyDefinitionById_23(id: str):
    return CatalystClient().previewPolicyDefinitionById_23(**{'id': id})

@register('getPolicyDefinition_23')
def getPolicyDefinition_23(id: str):
    return CatalystClient().getPolicyDefinition_23(**{'id': id})

@register('getDefinitions_24')
def getDefinitions_24():
    return CatalystClient().getDefinitions_24(**{})

@register('previewPolicyDefinitionById_24')
def previewPolicyDefinitionById_24(id: str):
    return CatalystClient().previewPolicyDefinitionById_24(**{'id': id})

@register('getPolicyDefinition_24')
def getPolicyDefinition_24(id: str):
    return CatalystClient().getPolicyDefinition_24(**{'id': id})

@register('getDefinitions_6')
def getDefinitions_6():
    return CatalystClient().getDefinitions_6(**{})

@register('previewPolicyDefinitionById_6')
def previewPolicyDefinitionById_6(id: str):
    return CatalystClient().previewPolicyDefinitionById_6(**{'id': id})

@register('getPolicyDefinition_6')
def getPolicyDefinition_6(id: str):
    return CatalystClient().getPolicyDefinition_6(**{'id': id})

@register('getDefinitions_2')
def getDefinitions_2():
    return CatalystClient().getDefinitions_2(**{})

@register('previewPolicyDefinitionById_2')
def previewPolicyDefinitionById_2(id: str):
    return CatalystClient().previewPolicyDefinitionById_2(**{'id': id})

@register('getPolicyDefinition_2')
def getPolicyDefinition_2(id: str):
    return CatalystClient().getPolicyDefinition_2(**{'id': id})

@register('getDefinitions_7')
def getDefinitions_7():
    return CatalystClient().getDefinitions_7(**{})

@register('previewPolicyDefinitionById_7')
def previewPolicyDefinitionById_7(id: str):
    return CatalystClient().previewPolicyDefinitionById_7(**{'id': id})

@register('getPolicyDefinition_7')
def getPolicyDefinition_7(id: str):
    return CatalystClient().getPolicyDefinition_7(**{'id': id})

@register('getListReference')
def getListReference(listType: str):
    return CatalystClient().getListReference(**{'listType': listType})

@register('sgts')
def sgts():
    return CatalystClient().sgts(**{})

@register('getAllPolicyLists')
def getAllPolicyLists():
    return CatalystClient().getAllPolicyLists(**{})

@register('getPolicyLists_3')
def getPolicyLists_3():
    return CatalystClient().getPolicyLists_3(**{})

@register('getPolicyListsWithInfoTag_3')
def getPolicyListsWithInfoTag_3(**kwargs):
    return CatalystClient().getPolicyListsWithInfoTag_3(**{**kwargs})

@register('previewPolicyListById_3')
def previewPolicyListById_3(id: str):
    return CatalystClient().previewPolicyListById_3(**{'id': id})

@register('getListsById_3')
def getListsById_3(id: str):
    return CatalystClient().getListsById_3(**{'id': id})

@register('getPolicyLists_4')
def getPolicyLists_4():
    return CatalystClient().getPolicyLists_4(**{})

@register('getPolicyListsWithInfoTag_4')
def getPolicyListsWithInfoTag_4(**kwargs):
    return CatalystClient().getPolicyListsWithInfoTag_4(**{**kwargs})

@register('previewPolicyListById_4')
def previewPolicyListById_4(id: str):
    return CatalystClient().previewPolicyListById_4(**{'id': id})

@register('getListsById_4')
def getListsById_4(id: str):
    return CatalystClient().getListsById_4(**{'id': id})

@register('getPolicyLists_5')
def getPolicyLists_5():
    return CatalystClient().getPolicyLists_5(**{})

@register('getPolicyListsWithInfoTag_5')
def getPolicyListsWithInfoTag_5(**kwargs):
    return CatalystClient().getPolicyListsWithInfoTag_5(**{**kwargs})

@register('previewPolicyListById_5')
def previewPolicyListById_5(id: str):
    return CatalystClient().previewPolicyListById_5(**{'id': id})

@register('getListsById_5')
def getListsById_5(id: str):
    return CatalystClient().getListsById_5(**{'id': id})

@register('getPolicyLists_13')
def getPolicyLists_13():
    return CatalystClient().getPolicyLists_13(**{})

@register('getPolicyListsWithInfoTag_14')
def getPolicyListsWithInfoTag_14(**kwargs):
    return CatalystClient().getPolicyListsWithInfoTag_14(**{**kwargs})

@register('previewPolicyListById_14')
def previewPolicyListById_14(id: str):
    return CatalystClient().previewPolicyListById_14(**{'id': id})

@register('getListsById_14')
def getListsById_14(id: str):
    return CatalystClient().getListsById_14(**{'id': id})

@register('getPolicyLists_6')
def getPolicyLists_6():
    return CatalystClient().getPolicyLists_6(**{})

@register('getPolicyListsWithInfoTag_6')
def getPolicyListsWithInfoTag_6(**kwargs):
    return CatalystClient().getPolicyListsWithInfoTag_6(**{**kwargs})

@register('previewPolicyListById_6')
def previewPolicyListById_6(id: str):
    return CatalystClient().previewPolicyListById_6(**{'id': id})

@register('getListsById_6')
def getListsById_6(id: str):
    return CatalystClient().getListsById_6(**{'id': id})

@register('getPolicyLists_7')
def getPolicyLists_7():
    return CatalystClient().getPolicyLists_7(**{})

@register('getPolicyListsWithInfoTag_7')
def getPolicyListsWithInfoTag_7(**kwargs):
    return CatalystClient().getPolicyListsWithInfoTag_7(**{**kwargs})

@register('previewPolicyListById_7')
def previewPolicyListById_7(id: str):
    return CatalystClient().previewPolicyListById_7(**{'id': id})

@register('getListsById_7')
def getListsById_7(id: str):
    return CatalystClient().getListsById_7(**{'id': id})

@register('getPolicyLists_8')
def getPolicyLists_8():
    return CatalystClient().getPolicyLists_8(**{})

@register('getPolicyListsWithInfoTag_8')
def getPolicyListsWithInfoTag_8(**kwargs):
    return CatalystClient().getPolicyListsWithInfoTag_8(**{**kwargs})

@register('previewPolicyListById_8')
def previewPolicyListById_8(id: str):
    return CatalystClient().previewPolicyListById_8(**{'id': id})

@register('getListsById_8')
def getListsById_8(id: str):
    return CatalystClient().getListsById_8(**{'id': id})

@register('getPolicyLists_9')
def getPolicyLists_9():
    return CatalystClient().getPolicyLists_9(**{})

@register('getPolicyListsWithInfoTag_10')
def getPolicyListsWithInfoTag_10(**kwargs):
    return CatalystClient().getPolicyListsWithInfoTag_10(**{**kwargs})

@register('previewPolicyListById_10')
def previewPolicyListById_10(id: str):
    return CatalystClient().previewPolicyListById_10(**{'id': id})

@register('getListsById_10')
def getListsById_10(id: str):
    return CatalystClient().getListsById_10(**{'id': id})

@register('getListsForAllDataPrefixes')
def getListsForAllDataPrefixes():
    return CatalystClient().getListsForAllDataPrefixes(**{})

@register('getPolicyListsWithInfoTag_9')
def getPolicyListsWithInfoTag_9(**kwargs):
    return CatalystClient().getPolicyListsWithInfoTag_9(**{**kwargs})

@register('previewPolicyListById_9')
def previewPolicyListById_9(id: str):
    return CatalystClient().previewPolicyListById_9(**{'id': id})

@register('getListsById_9')
def getListsById_9(id: str):
    return CatalystClient().getListsById_9(**{'id': id})

@register('getAllDataPrefixAndFQDNLists')
def getAllDataPrefixAndFQDNLists():
    return CatalystClient().getAllDataPrefixAndFQDNLists(**{})

@register('getPolicyListsWithInfoTag_15')
def getPolicyListsWithInfoTag_15(**kwargs):
    return CatalystClient().getPolicyListsWithInfoTag_15(**{**kwargs})

@register('previewPolicyListById_15')
def previewPolicyListById_15(id: str):
    return CatalystClient().previewPolicyListById_15(**{'id': id})

@register('getListsById_15')
def getListsById_15(id: str):
    return CatalystClient().getListsById_15(**{'id': id})

@register('getPolicyLists_10')
def getPolicyLists_10():
    return CatalystClient().getPolicyLists_10(**{})

@register('getPolicyListsWithInfoTag_11')
def getPolicyListsWithInfoTag_11(**kwargs):
    return CatalystClient().getPolicyListsWithInfoTag_11(**{**kwargs})

@register('previewPolicyListById_11')
def previewPolicyListById_11(id: str):
    return CatalystClient().previewPolicyListById_11(**{'id': id})

@register('getListsById_11')
def getListsById_11(id: str):
    return CatalystClient().getListsById_11(**{'id': id})

@register('getPolicyLists_11')
def getPolicyLists_11():
    return CatalystClient().getPolicyLists_11(**{})

@register('getPolicyListsWithInfoTag_12')
def getPolicyListsWithInfoTag_12(**kwargs):
    return CatalystClient().getPolicyListsWithInfoTag_12(**{**kwargs})

@register('previewPolicyListById_12')
def previewPolicyListById_12(id: str):
    return CatalystClient().previewPolicyListById_12(**{'id': id})

@register('getListsById_12')
def getListsById_12(id: str):
    return CatalystClient().getListsById_12(**{'id': id})

@register('getPolicyLists_12')
def getPolicyLists_12():
    return CatalystClient().getPolicyLists_12(**{})

@register('getPolicyListsWithInfoTag_13')
def getPolicyListsWithInfoTag_13(**kwargs):
    return CatalystClient().getPolicyListsWithInfoTag_13(**{**kwargs})

@register('previewPolicyListById_13')
def previewPolicyListById_13(id: str):
    return CatalystClient().previewPolicyListById_13(**{'id': id})

@register('getListsById_13')
def getListsById_13(id: str):
    return CatalystClient().getListsById_13(**{'id': id})

@register('getPolicyLists_14')
def getPolicyLists_14():
    return CatalystClient().getPolicyLists_14(**{})

@register('getPolicyListsWithInfoTag_16')
def getPolicyListsWithInfoTag_16(**kwargs):
    return CatalystClient().getPolicyListsWithInfoTag_16(**{**kwargs})

@register('previewPolicyListById_16')
def previewPolicyListById_16(id: str):
    return CatalystClient().previewPolicyListById_16(**{'id': id})

@register('getListsById_16')
def getListsById_16(id: str):
    return CatalystClient().getListsById_16(**{'id': id})

@register('getPolicyLists_15')
def getPolicyLists_15():
    return CatalystClient().getPolicyLists_15(**{})

@register('getGeoLocationLists')
def getGeoLocationLists():
    return CatalystClient().getGeoLocationLists(**{})

@register('getPolicyListsWithInfoTag_17')
def getPolicyListsWithInfoTag_17(**kwargs):
    return CatalystClient().getPolicyListsWithInfoTag_17(**{**kwargs})

@register('previewPolicyListById_17')
def previewPolicyListById_17(id: str):
    return CatalystClient().previewPolicyListById_17(**{'id': id})

@register('getListsById_17')
def getListsById_17(id: str):
    return CatalystClient().getListsById_17(**{'id': id})

@register('getPolicyLists_16')
def getPolicyLists_16():
    return CatalystClient().getPolicyLists_16(**{})

@register('getPolicyListsWithInfoTag_18')
def getPolicyListsWithInfoTag_18(**kwargs):
    return CatalystClient().getPolicyListsWithInfoTag_18(**{**kwargs})

@register('previewPolicyListById_18')
def previewPolicyListById_18(id: str):
    return CatalystClient().previewPolicyListById_18(**{'id': id})

@register('getListsById_18')
def getListsById_18(id: str):
    return CatalystClient().getListsById_18(**{'id': id})

@register('getListsForAllPrefixes')
def getListsForAllPrefixes():
    return CatalystClient().getListsForAllPrefixes(**{})

@register('getPolicyListsWithInfoTag_21')
def getPolicyListsWithInfoTag_21(**kwargs):
    return CatalystClient().getPolicyListsWithInfoTag_21(**{**kwargs})

@register('previewPolicyListById_21')
def previewPolicyListById_21(id: str):
    return CatalystClient().previewPolicyListById_21(**{'id': id})

@register('getListsById_21')
def getListsById_21(id: str):
    return CatalystClient().getListsById_21(**{'id': id})

@register('getPolicyLists_17')
def getPolicyLists_17():
    return CatalystClient().getPolicyLists_17(**{})

@register('getPolicyListsWithInfoTag_19')
def getPolicyListsWithInfoTag_19(**kwargs):
    return CatalystClient().getPolicyListsWithInfoTag_19(**{**kwargs})

@register('previewPolicyListById_19')
def previewPolicyListById_19(id: str):
    return CatalystClient().previewPolicyListById_19(**{'id': id})

@register('getListsById_19')
def getListsById_19(id: str):
    return CatalystClient().getListsById_19(**{'id': id})

@register('getPolicyLists_18')
def getPolicyLists_18():
    return CatalystClient().getPolicyLists_18(**{})

@register('getPolicyListsWithInfoTag_20')
def getPolicyListsWithInfoTag_20(**kwargs):
    return CatalystClient().getPolicyListsWithInfoTag_20(**{**kwargs})

@register('previewPolicyListById_20')
def previewPolicyListById_20(id: str):
    return CatalystClient().previewPolicyListById_20(**{'id': id})

@register('getListsById_20')
def getListsById_20(id: str):
    return CatalystClient().getListsById_20(**{'id': id})

@register('getPolicyLists_19')
def getPolicyLists_19():
    return CatalystClient().getPolicyLists_19(**{})

@register('getPolicyListsWithInfoTag_22')
def getPolicyListsWithInfoTag_22(**kwargs):
    return CatalystClient().getPolicyListsWithInfoTag_22(**{**kwargs})

@register('previewPolicyListById_22')
def previewPolicyListById_22(id: str):
    return CatalystClient().previewPolicyListById_22(**{'id': id})

@register('getListsById_22')
def getListsById_22(id: str):
    return CatalystClient().getListsById_22(**{'id': id})

@register('getPolicyLists_20')
def getPolicyLists_20():
    return CatalystClient().getPolicyLists_20(**{})

@register('getPolicyListsWithInfoTag_23')
def getPolicyListsWithInfoTag_23(**kwargs):
    return CatalystClient().getPolicyListsWithInfoTag_23(**{**kwargs})

@register('previewPolicyListById_23')
def previewPolicyListById_23(id: str):
    return CatalystClient().previewPolicyListById_23(**{'id': id})

@register('getListsById_23')
def getListsById_23(id: str):
    return CatalystClient().getListsById_23(**{'id': id})

@register('getPolicyLists')
def getPolicyLists():
    return CatalystClient().getPolicyLists(**{})

@register('getPolicyListsWithInfoTag')
def getPolicyListsWithInfoTag(**kwargs):
    return CatalystClient().getPolicyListsWithInfoTag(**{**kwargs})

@register('previewPolicyListById')
def previewPolicyListById(id: str):
    return CatalystClient().previewPolicyListById(**{'id': id})

@register('getListsById')
def getListsById(id: str):
    return CatalystClient().getListsById(**{'id': id})

@register('getPolicyLists_21')
def getPolicyLists_21():
    return CatalystClient().getPolicyLists_21(**{})

@register('getPolicyListsWithInfoTag_24')
def getPolicyListsWithInfoTag_24(**kwargs):
    return CatalystClient().getPolicyListsWithInfoTag_24(**{**kwargs})

@register('previewPolicyListById_24')
def previewPolicyListById_24(id: str):
    return CatalystClient().previewPolicyListById_24(**{'id': id})

@register('getListsById_24')
def getListsById_24(id: str):
    return CatalystClient().getListsById_24(**{'id': id})

@register('getPolicyLists_22')
def getPolicyLists_22():
    return CatalystClient().getPolicyLists_22(**{})

@register('getPolicyListsWithInfoTag_25')
def getPolicyListsWithInfoTag_25(**kwargs):
    return CatalystClient().getPolicyListsWithInfoTag_25(**{**kwargs})

@register('previewPolicyListById_25')
def previewPolicyListById_25(id: str):
    return CatalystClient().previewPolicyListById_25(**{'id': id})

@register('getListsById_25')
def getListsById_25(id: str):
    return CatalystClient().getListsById_25(**{'id': id})

@register('getPolicyLists_23')
def getPolicyLists_23():
    return CatalystClient().getPolicyLists_23(**{})

@register('getPolicyListsWithInfoTag_26')
def getPolicyListsWithInfoTag_26(**kwargs):
    return CatalystClient().getPolicyListsWithInfoTag_26(**{**kwargs})

@register('previewPolicyListById_26')
def previewPolicyListById_26(id: str):
    return CatalystClient().previewPolicyListById_26(**{'id': id})

@register('getListsById_26')
def getListsById_26(id: str):
    return CatalystClient().getListsById_26(**{'id': id})

@register('getPolicyLists_24')
def getPolicyLists_24():
    return CatalystClient().getPolicyLists_24(**{})

@register('getPolicyListsWithInfoTag_27')
def getPolicyListsWithInfoTag_27(**kwargs):
    return CatalystClient().getPolicyListsWithInfoTag_27(**{**kwargs})

@register('previewPolicyListById_27')
def previewPolicyListById_27(id: str):
    return CatalystClient().previewPolicyListById_27(**{'id': id})

@register('getListsById_27')
def getListsById_27(id: str):
    return CatalystClient().getListsById_27(**{'id': id})

@register('getPolicyLists_25')
def getPolicyLists_25():
    return CatalystClient().getPolicyLists_25(**{})

@register('getPolicyListsWithInfoTag_28')
def getPolicyListsWithInfoTag_28(**kwargs):
    return CatalystClient().getPolicyListsWithInfoTag_28(**{**kwargs})

@register('previewPolicyListById_28')
def previewPolicyListById_28(id: str):
    return CatalystClient().previewPolicyListById_28(**{'id': id})

@register('getListsById_28')
def getListsById_28(id: str):
    return CatalystClient().getListsById_28(**{'id': id})

@register('getPolicyLists_26')
def getPolicyLists_26():
    return CatalystClient().getPolicyLists_26(**{})

@register('getPolicyListsWithInfoTag_29')
def getPolicyListsWithInfoTag_29(**kwargs):
    return CatalystClient().getPolicyListsWithInfoTag_29(**{**kwargs})

@register('previewPolicyListById_29')
def previewPolicyListById_29(id: str):
    return CatalystClient().previewPolicyListById_29(**{'id': id})

@register('getListsById_29')
def getListsById_29(id: str):
    return CatalystClient().getListsById_29(**{'id': id})

@register('getPolicyLists_27')
def getPolicyLists_27():
    return CatalystClient().getPolicyLists_27(**{})

@register('getPolicyListsWithInfoTag_30')
def getPolicyListsWithInfoTag_30(**kwargs):
    return CatalystClient().getPolicyListsWithInfoTag_30(**{**kwargs})

@register('previewPolicyListById_30')
def previewPolicyListById_30(id: str):
    return CatalystClient().previewPolicyListById_30(**{'id': id})

@register('getListsById_30')
def getListsById_30(id: str):
    return CatalystClient().getListsById_30(**{'id': id})

@register('getPolicyLists_28')
def getPolicyLists_28():
    return CatalystClient().getPolicyLists_28(**{})

@register('getPolicyListsWithInfoTag_31')
def getPolicyListsWithInfoTag_31(**kwargs):
    return CatalystClient().getPolicyListsWithInfoTag_31(**{**kwargs})

@register('previewPolicyListById_31')
def previewPolicyListById_31(id: str):
    return CatalystClient().previewPolicyListById_31(**{'id': id})

@register('getListsById_31')
def getListsById_31(id: str):
    return CatalystClient().getListsById_31(**{'id': id})

@register('getPolicyLists_29')
def getPolicyLists_29():
    return CatalystClient().getPolicyLists_29(**{})

@register('getPolicyListsWithInfoTag_32')
def getPolicyListsWithInfoTag_32(**kwargs):
    return CatalystClient().getPolicyListsWithInfoTag_32(**{**kwargs})

@register('previewPolicyListById_32')
def previewPolicyListById_32(id: str):
    return CatalystClient().previewPolicyListById_32(**{'id': id})

@register('getListsById_32')
def getListsById_32(id: str):
    return CatalystClient().getListsById_32(**{'id': id})

@register('getPolicyLists_30')
def getPolicyLists_30():
    return CatalystClient().getPolicyLists_30(**{})

@register('getPolicyListsWithInfoTag_33')
def getPolicyListsWithInfoTag_33(**kwargs):
    return CatalystClient().getPolicyListsWithInfoTag_33(**{**kwargs})

@register('previewPolicyListById_33')
def previewPolicyListById_33(id: str):
    return CatalystClient().previewPolicyListById_33(**{'id': id})

@register('getListsById_33')
def getListsById_33(id: str):
    return CatalystClient().getListsById_33(**{'id': id})

@register('getPolicyLists_31')
def getPolicyLists_31():
    return CatalystClient().getPolicyLists_31(**{})

@register('getPolicyListsWithInfoTag_34')
def getPolicyListsWithInfoTag_34(**kwargs):
    return CatalystClient().getPolicyListsWithInfoTag_34(**{**kwargs})

@register('previewPolicyListById_34')
def previewPolicyListById_34(id: str):
    return CatalystClient().previewPolicyListById_34(**{'id': id})

@register('getListsById_34')
def getListsById_34(id: str):
    return CatalystClient().getListsById_34(**{'id': id})

@register('getPolicyLists_32')
def getPolicyLists_32():
    return CatalystClient().getPolicyLists_32(**{})

@register('getPolicyListsWithInfoTag_35')
def getPolicyListsWithInfoTag_35(**kwargs):
    return CatalystClient().getPolicyListsWithInfoTag_35(**{**kwargs})

@register('previewPolicyListById_35')
def previewPolicyListById_35(id: str):
    return CatalystClient().previewPolicyListById_35(**{'id': id})

@register('getListsById_35')
def getListsById_35(id: str):
    return CatalystClient().getListsById_35(**{'id': id})

@register('getPolicyLists_33')
def getPolicyLists_33():
    return CatalystClient().getPolicyLists_33(**{})

@register('getPolicyListsWithInfoTag_36')
def getPolicyListsWithInfoTag_36(**kwargs):
    return CatalystClient().getPolicyListsWithInfoTag_36(**{**kwargs})

@register('previewPolicyListById_36')
def previewPolicyListById_36(id: str):
    return CatalystClient().previewPolicyListById_36(**{'id': id})

@register('getListsById_36')
def getListsById_36(id: str):
    return CatalystClient().getListsById_36(**{'id': id})

@register('getPolicyLists_34')
def getPolicyLists_34():
    return CatalystClient().getPolicyLists_34(**{})

@register('getPolicyListsWithInfoTag_37')
def getPolicyListsWithInfoTag_37(**kwargs):
    return CatalystClient().getPolicyListsWithInfoTag_37(**{**kwargs})

@register('previewPolicyListById_37')
def previewPolicyListById_37(id: str):
    return CatalystClient().previewPolicyListById_37(**{'id': id})

@register('getListsById_37')
def getListsById_37(id: str):
    return CatalystClient().getListsById_37(**{'id': id})

@register('getPolicyLists_1')
def getPolicyLists_1():
    return CatalystClient().getPolicyLists_1(**{})

@register('getPolicyListsWithInfoTag_1')
def getPolicyListsWithInfoTag_1(**kwargs):
    return CatalystClient().getPolicyListsWithInfoTag_1(**{**kwargs})

@register('previewPolicyListById_1')
def previewPolicyListById_1(id: str):
    return CatalystClient().previewPolicyListById_1(**{'id': id})

@register('getListsById_1')
def getListsById_1(id: str):
    return CatalystClient().getListsById_1(**{'id': id})

@register('getPolicyLists_2')
def getPolicyLists_2():
    return CatalystClient().getPolicyLists_2(**{})

@register('getPolicyListsWithInfoTag_2')
def getPolicyListsWithInfoTag_2(**kwargs):
    return CatalystClient().getPolicyListsWithInfoTag_2(**{**kwargs})

@register('previewPolicyListById_2')
def previewPolicyListById_2(id: str):
    return CatalystClient().previewPolicyListById_2(**{'id': id})

@register('getListsById_2')
def getListsById_2(id: str):
    return CatalystClient().getListsById_2(**{'id': id})

@register('getPolicyLists_35')
def getPolicyLists_35():
    return CatalystClient().getPolicyLists_35(**{})

@register('getPolicyListsWithInfoTag_38')
def getPolicyListsWithInfoTag_38(**kwargs):
    return CatalystClient().getPolicyListsWithInfoTag_38(**{**kwargs})

@register('previewPolicyListById_38')
def previewPolicyListById_38(id: str):
    return CatalystClient().previewPolicyListById_38(**{'id': id})

@register('getListsById_38')
def getListsById_38(id: str):
    return CatalystClient().getListsById_38(**{'id': id})

@register('getPolicyLists_36')
def getPolicyLists_36():
    return CatalystClient().getPolicyLists_36(**{})

@register('getPolicyListsWithInfoTag_39')
def getPolicyListsWithInfoTag_39(**kwargs):
    return CatalystClient().getPolicyListsWithInfoTag_39(**{**kwargs})

@register('previewPolicyListById_39')
def previewPolicyListById_39(id: str):
    return CatalystClient().previewPolicyListById_39(**{'id': id})

@register('getListsById_39')
def getListsById_39(id: str):
    return CatalystClient().getListsById_39(**{'id': id})

@register('getPolicyLists_37')
def getPolicyLists_37():
    return CatalystClient().getPolicyLists_37(**{})

@register('getPolicyListsWithInfoTag_40')
def getPolicyListsWithInfoTag_40(**kwargs):
    return CatalystClient().getPolicyListsWithInfoTag_40(**{**kwargs})

@register('previewPolicyListById_40')
def previewPolicyListById_40(id: str):
    return CatalystClient().previewPolicyListById_40(**{'id': id})

@register('getListsById_40')
def getListsById_40(id: str):
    return CatalystClient().getListsById_40(**{'id': id})

@register('getPolicyLists_38')
def getPolicyLists_38():
    return CatalystClient().getPolicyLists_38(**{})

@register('getPolicyListsWithInfoTag_41')
def getPolicyListsWithInfoTag_41(**kwargs):
    return CatalystClient().getPolicyListsWithInfoTag_41(**{**kwargs})

@register('previewPolicyListById_41')
def previewPolicyListById_41(id: str):
    return CatalystClient().previewPolicyListById_41(**{'id': id})

@register('getListsById_41')
def getListsById_41(id: str):
    return CatalystClient().getListsById_41(**{'id': id})

@register('getPolicyLists_39')
def getPolicyLists_39():
    return CatalystClient().getPolicyLists_39(**{})

@register('getPolicyListsWithInfoTag_42')
def getPolicyListsWithInfoTag_42(**kwargs):
    return CatalystClient().getPolicyListsWithInfoTag_42(**{**kwargs})

@register('previewPolicyListById_42')
def previewPolicyListById_42(id: str):
    return CatalystClient().previewPolicyListById_42(**{'id': id})

@register('getListsById_42')
def getListsById_42(id: str):
    return CatalystClient().getListsById_42(**{'id': id})

@register('getPolicyLists_40')
def getPolicyLists_40():
    return CatalystClient().getPolicyLists_40(**{})

@register('getPolicyListsWithInfoTag_43')
def getPolicyListsWithInfoTag_43(**kwargs):
    return CatalystClient().getPolicyListsWithInfoTag_43(**{**kwargs})

@register('previewPolicyListById_43')
def previewPolicyListById_43(id: str):
    return CatalystClient().previewPolicyListById_43(**{'id': id})

@register('getListsById_43')
def getListsById_43(id: str):
    return CatalystClient().getListsById_43(**{'id': id})

@register('generateSecurityTemplateList')
def generateSecurityTemplateList(**kwargs):
    return CatalystClient().generateSecurityTemplateList(**{**kwargs})

@register('getSecurityTemplate')
def getSecurityTemplate(policyId: str):
    return CatalystClient().getSecurityTemplate(**{'policyId': policyId})

@register('getSecurityPolicyDeviceList_1')
def getSecurityPolicyDeviceList_1():
    return CatalystClient().getSecurityPolicyDeviceList_1(**{})

@register('getDeviceListById')
def getDeviceListById(policyId: str):
    return CatalystClient().getDeviceListById(**{'policyId': policyId})

@register('generateSecurityPolicySummary')
def generateSecurityPolicySummary():
    return CatalystClient().generateSecurityPolicySummary(**{})

@register('getSecurityTemplatesForDevice')
def getSecurityTemplatesForDevice(deviceModel: str):
    return CatalystClient().getSecurityTemplatesForDevice(**{'deviceModel': deviceModel})

@register('generatePolicyTemplateList')
def generatePolicyTemplateList():
    return CatalystClient().generatePolicyTemplateList(**{})

@register('getVEdgeTemplate')
def getVEdgeTemplate(policyId: str):
    return CatalystClient().getVEdgeTemplate(**{'policyId': policyId})

@register('getVEdgePolicyDeviceList')
def getVEdgePolicyDeviceList():
    return CatalystClient().getVEdgePolicyDeviceList(**{})

@register('getDeviceListByPolicy')
def getDeviceListByPolicy(policyId: str):
    return CatalystClient().getDeviceListByPolicy(**{'policyId': policyId})

@register('generateVoiceTemplateList')
def generateVoiceTemplateList():
    return CatalystClient().generateVoiceTemplateList(**{})

@register('getTemplateById')
def getTemplateById(policyId: str):
    return CatalystClient().getTemplateById(**{'policyId': policyId})

@register('getVoicePolicyDeviceList')
def getVoicePolicyDeviceList():
    return CatalystClient().getVoicePolicyDeviceList(**{})

@register('getDeviceListByPolicyId')
def getDeviceListByPolicyId(policyId: str):
    return CatalystClient().getDeviceListByPolicyId(**{'policyId': policyId})

@register('generateVoicePolicySummary')
def generateVoicePolicySummary():
    return CatalystClient().generateVoicePolicySummary(**{})

@register('getVoiceTemplatesForDevice')
def getVoiceTemplatesForDevice(deviceModel: str):
    return CatalystClient().getVoiceTemplatesForDevice(**{'deviceModel': deviceModel})

@register('generateVSmartPolicyTemplateList')
def generateVSmartPolicyTemplateList():
    return CatalystClient().generateVSmartPolicyTemplateList(**{})

@register('checkVSmartConnectivityStatus')
def checkVSmartConnectivityStatus():
    return CatalystClient().checkVSmartConnectivityStatus(**{})

@register('getTemplateByPolicyId')
def getTemplateByPolicyId(policyId: str):
    return CatalystClient().getTemplateByPolicyId(**{'policyId': policyId})

@register('QosmosNbarMigrationWarning')
def QosmosNbarMigrationWarning():
    return CatalystClient().QosmosNbarMigrationWarning(**{})

@register('getAllTenants')
def getAllTenants(**kwargs):
    return CatalystClient().getAllTenants(**{**kwargs})

@register('getTenantvSmartMapping')
def getTenantvSmartMapping():
    return CatalystClient().getTenantvSmartMapping(**{})

@register('getTenantHostingCapacityOnvSmarts')
def getTenantHostingCapacityOnvSmarts():
    return CatalystClient().getTenantHostingCapacityOnvSmarts(**{})

@register('getTenant')
def getTenant(tenantId: str):
    return CatalystClient().getTenant(**{'tenantId': tenantId})

@register('downloadExistingBackupFile')
def downloadExistingBackupFile(path: str):
    return CatalystClient().downloadExistingBackupFile(**{'path': path})

@register('exportTenantBackup')
def exportTenantBackup():
    return CatalystClient().exportTenantBackup(**{})

@register('listTenantBackup')
def listTenantBackup():
    return CatalystClient().listTenantBackup(**{})

@register('downloadTenantData')
def downloadTenantData(path: str):
    return CatalystClient().downloadTenantData(**{'path': path})

@register('getMigrationToken')
def getMigrationToken(migrationId: str):
    return CatalystClient().getMigrationToken(**{'migrationId': migrationId})

@register('reTriggerNetworkMigration')
def reTriggerNetworkMigration():
    return CatalystClient().reTriggerNetworkMigration(**{})

@register('getAllTenantStatuses')
def getAllTenantStatuses():
    return CatalystClient().getAllTenantStatuses(**{})

@register('createFullTopology')
def createFullTopology():
    return CatalystClient().createFullTopology(**{})

@register('createDeviceTopology')
def createDeviceTopology(deviceId: list):
    return CatalystClient().createDeviceTopology(**{'deviceId': deviceId})

@register('getSiteTopology')
def getSiteTopology(siteId: str):
    return CatalystClient().getSiteTopology(**{'siteId': siteId})

@register('getSiteTopologyMonitorData')
def getSiteTopologyMonitorData(siteId: str):
    return CatalystClient().getSiteTopologyMonitorData(**{'siteId': siteId})

@register('createPhysicalTopology')
def createPhysicalTopology(deviceId: list):
    return CatalystClient().createPhysicalTopology(**{'deviceId': deviceId})

@register('getControlConnections')
def getControlConnections(uuid: str):
    return CatalystClient().getControlConnections(**{'uuid': uuid})

@register('getDeviceConfiguration')
def getDeviceConfiguration(uuid: str):
    return CatalystClient().getDeviceConfiguration(**{'uuid': uuid})

@register('getAllKeysFromUmbrella')
def getAllKeysFromUmbrella():
    return CatalystClient().getAllKeysFromUmbrella(**{})

@register('getManagementKeysFromUmbrella')
def getManagementKeysFromUmbrella():
    return CatalystClient().getManagementKeysFromUmbrella(**{})

@register('getNetworkKeysFromUmbrella')
def getNetworkKeysFromUmbrella():
    return CatalystClient().getNetworkKeysFromUmbrella(**{})

@register('getReportingKeysFromUmbrella')
def getReportingKeysFromUmbrella():
    return CatalystClient().getReportingKeysFromUmbrella(**{})

@register('sendMetaDataToUmbrella')
def sendMetaDataToUmbrella():
    return CatalystClient().sendMetaDataToUmbrella(**{})

@register('getStatus')
def getStatus():
    return CatalystClient().getStatus(**{})

@register('getUrlMonitor')
def getUrlMonitor():
    return CatalystClient().getUrlMonitor(**{})

@register('returnMetric')
def returnMetric(metricName: str, startDate: str, **kwargs):
    return CatalystClient().returnMetric(**{'metricName': metricName, 'startDate': startDate, **kwargs})

@register('returnMetricFiles')
def returnMetricFiles(metricName: str, startDate: str, **kwargs):
    return CatalystClient().returnMetricFiles(**{'metricName': metricName, 'startDate': startDate, **kwargs})

@register('getMetricsList')
def getMetricsList():
    return CatalystClient().getMetricsList(**{})

@register('getDBSizeOnFile')
def getDBSizeOnFile():
    return CatalystClient().getDBSizeOnFile(**{})

@register('listLogFileDetails')
def listLogFileDetails():
    return CatalystClient().listLogFileDetails(**{})

@register('listVManageServerLogLastNLines')
def listVManageServerLogLastNLines(**kwargs):
    return CatalystClient().listVManageServerLogLastNLines(**{**kwargs})

@register('listConfigurations')
def listConfigurations():
    return CatalystClient().listConfigurations(**{})

@register('listLoggers')
def listLoggers():
    return CatalystClient().listLoggers(**{})

@register('getStatsMigrationRangeConfig')
def getStatsMigrationRangeConfig():
    return CatalystClient().getStatsMigrationRangeConfig(**{})

@register('getStatsMigrationSettings')
def getStatsMigrationSettings():
    return CatalystClient().getStatsMigrationSettings(**{})

@register('getStatsMigrationStatsDbInfo')
def getStatsMigrationStatsDbInfo():
    return CatalystClient().getStatsMigrationStatsDbInfo(**{})

@register('getStatsMigrationStatus')
def getStatsMigrationStatus():
    return CatalystClient().getStatsMigrationStatus(**{})

@register('getCloudOnRampSaasStatus')
def getCloudOnRampSaasStatus():
    return CatalystClient().getCloudOnRampSaasStatus(**{})

@register('getCloudTunnelList')
def getCloudTunnelList(deviceIp: str):
    return CatalystClient().getCloudTunnelList(**{'deviceIp': deviceIp})

@register('getPolicyGroupsWithCorSaasApps')
def getPolicyGroupsWithCorSaasApps():
    return CatalystClient().getPolicyGroupsWithCorSaasApps(**{})

@register('getCorSitesPerDevice')
def getCorSitesPerDevice():
    return CatalystClient().getCorSitesPerDevice(**{})

@register('getInactiveCorSaasSites')
def getInactiveCorSaasSites():
    return CatalystClient().getInactiveCorSaasSites(**{})

@register('getLegacyDeviceList')
def getLegacyDeviceList():
    return CatalystClient().getLegacyDeviceList(**{})

@register('getCorSaasStatusPerDevice')
def getCorSaasStatusPerDevice(deviceIp: str):
    return CatalystClient().getCorSaasStatusPerDevice(**{'deviceIp': deviceIp})

@register('getWebexSyncStatus')
def getWebexSyncStatus():
    return CatalystClient().getWebexSyncStatus(**{})

@register('GetConfigGroupBySolution')
def GetConfigGroupBySolution(**kwargs):
    return CatalystClient().GetConfigGroupBySolution(**{**kwargs})

@register('GetConfigGroup')
def GetConfigGroup(configGroupId: str, **kwargs):
    return CatalystClient().GetConfigGroup(**{'configGroupId': configGroupId, **kwargs})

@register('GetConfigGroupAssociation')
def GetConfigGroupAssociation(configGroupId: str):
    return CatalystClient().GetConfigGroupAssociation(**{'configGroupId': configGroupId})

@register('getConfigGroupDeviceVariables')
def getConfigGroupDeviceVariables(configGroupId: str, **kwargs):
    return CatalystClient().getConfigGroupDeviceVariables(**{'configGroupId': configGroupId, **kwargs})

@register('getConfigGroupDeviceVariablesSchema')
def getConfigGroupDeviceVariablesSchema(configGroupId: str, **kwargs):
    return CatalystClient().getConfigGroupDeviceVariablesSchema(**{'configGroupId': configGroupId, **kwargs})

@register('getRuleAssociationByConfigGroupId')
def getRuleAssociationByConfigGroupId(configGroupId: str):
    return CatalystClient().getRuleAssociationByConfigGroupId(**{'configGroupId': configGroupId})

@register('getRunningIosCliConfig')
def getRunningIosCliConfig(deviceUUID: str):
    return CatalystClient().getRunningIosCliConfig(**{'deviceUUID': deviceUUID})

@register('getUnsupportedCliConfig')
def getUnsupportedCliConfig(deviceUUID: str, **kwargs):
    return CatalystClient().getUnsupportedCliConfig(**{'deviceUUID': deviceUUID, **kwargs})

@register('GetMobilityCliFeatureProfile')
def GetMobilityCliFeatureProfile(**kwargs):
    return CatalystClient().GetMobilityCliFeatureProfile(**{**kwargs})

@register('GetMobilityCliFeatureProfileByCliId')
def GetMobilityCliFeatureProfileByCliId(cliId: str):
    return CatalystClient().GetMobilityCliFeatureProfileByCliId(**{'cliId': cliId})

@register('GetAllConfigFeatureForMobility')
def GetAllConfigFeatureForMobility(cliId: str):
    return CatalystClient().GetAllConfigFeatureForMobility(**{'cliId': cliId})

@register('GetConfigFeatureForMobilityByParcelId')
def GetConfigFeatureForMobilityByParcelId(cliId: str, configId: str):
    return CatalystClient().GetConfigFeatureForMobilityByParcelId(**{'cliId': cliId, 'configId': configId})

@register('GetMobilityGlobalFeatureProfile')
def GetMobilityGlobalFeatureProfile(**kwargs):
    return CatalystClient().GetMobilityGlobalFeatureProfile(**{**kwargs})

@register('GetMobilityGlobalBasicParcelSchemaBySchemaType')
def GetMobilityGlobalBasicParcelSchemaBySchemaType(schemaType: str):
    return CatalystClient().GetMobilityGlobalBasicParcelSchemaBySchemaType(**{'schemaType': schemaType})

@register('GetMobilityFeatureProfileByGlobalId')
def GetMobilityFeatureProfileByGlobalId(globalId: str):
    return CatalystClient().GetMobilityFeatureProfileByGlobalId(**{'globalId': globalId})

@register('GetQosFeatureForGlobal')
def GetQosFeatureForGlobal(globalId: str):
    return CatalystClient().GetQosFeatureForGlobal(**{'globalId': globalId})

@register('GetQosFeatureByParcelIdForGlobal')
def GetQosFeatureByParcelIdForGlobal(globalId: str, qosId: str):
    return CatalystClient().GetQosFeatureByParcelIdForGlobal(**{'globalId': globalId, 'qosId': qosId})

@register('GetAaaServersProfileParcelForMobility')
def GetAaaServersProfileParcelForMobility(profileId: str):
    return CatalystClient().GetAaaServersProfileParcelForMobility(**{'profileId': profileId})

@register('GetAaaServersProfileParcelByParcelIdForMobility')
def GetAaaServersProfileParcelByParcelIdForMobility(aaaserversId: str, profileId: str):
    return CatalystClient().GetAaaServersProfileParcelByParcelIdForMobility(**{'aaaserversId': aaaserversId, 'profileId': profileId})

@register('GetBasicProfileParcelForMobility')
def GetBasicProfileParcelForMobility(profileId: str):
    return CatalystClient().GetBasicProfileParcelForMobility(**{'profileId': profileId})

@register('GetBasicProfileParcelByParcelIdForMobility')
def GetBasicProfileParcelByParcelIdForMobility(parcelId: str, profileId: str):
    return CatalystClient().GetBasicProfileParcelByParcelIdForMobility(**{'parcelId': parcelId, 'profileId': profileId})

@register('GetCellularProfileParcelListForMobility')
def GetCellularProfileParcelListForMobility(profileId: str):
    return CatalystClient().GetCellularProfileParcelListForMobility(**{'profileId': profileId})

@register('GetCellularProfileParcelForMobility')
def GetCellularProfileParcelForMobility(cellularId: str, profileId: str):
    return CatalystClient().GetCellularProfileParcelForMobility(**{'cellularId': cellularId, 'profileId': profileId})

@register('GetEsimCellularProfileFeatureForMobility')
def GetEsimCellularProfileFeatureForMobility(profileId: str):
    return CatalystClient().GetEsimCellularProfileFeatureForMobility(**{'profileId': profileId})

@register('GetEsimCellularProfileFeatureByEsimCellularIdForMobility')
def GetEsimCellularProfileFeatureByEsimCellularIdForMobility(esimCellularId: str, profileId: str):
    return CatalystClient().GetEsimCellularProfileFeatureByEsimCellularIdForMobility(**{'esimCellularId': esimCellularId, 'profileId': profileId})

@register('GetEthernetProfileParcels')
def GetEthernetProfileParcels(profileId: str):
    return CatalystClient().GetEthernetProfileParcels(**{'profileId': profileId})

@register('GetEthernetProfileParcel')
def GetEthernetProfileParcel(ethernetId: str, profileId: str):
    return CatalystClient().GetEthernetProfileParcel(**{'ethernetId': ethernetId, 'profileId': profileId})

@register('GetLoggingProfileFeatureForMobility')
def GetLoggingProfileFeatureForMobility(profileId: str):
    return CatalystClient().GetLoggingProfileFeatureForMobility(**{'profileId': profileId})

@register('GetLoggingProfileFeatureByFeatureIdForMobility')
def GetLoggingProfileFeatureByFeatureIdForMobility(loggingId: str, profileId: str):
    return CatalystClient().GetLoggingProfileFeatureByFeatureIdForMobility(**{'loggingId': loggingId, 'profileId': profileId})

@register('GetNetworkProtocolProfileParcelListForMobility')
def GetNetworkProtocolProfileParcelListForMobility(profileId: str):
    return CatalystClient().GetNetworkProtocolProfileParcelListForMobility(**{'profileId': profileId})

@register('GetNetworkProtocolProfileParcelForMobility')
def GetNetworkProtocolProfileParcelForMobility(networkProtocolId: str, profileId: str):
    return CatalystClient().GetNetworkProtocolProfileParcelForMobility(**{'networkProtocolId': networkProtocolId, 'profileId': profileId})

@register('GetSecurityPolicyProfileParcelListForMobility')
def GetSecurityPolicyProfileParcelListForMobility(profileId: str):
    return CatalystClient().GetSecurityPolicyProfileParcelListForMobility(**{'profileId': profileId})

@register('GetSecurityPolicyProfileParcelForMobility')
def GetSecurityPolicyProfileParcelForMobility(profileId: str, securityPolicyId: str):
    return CatalystClient().GetSecurityPolicyProfileParcelForMobility(**{'profileId': profileId, 'securityPolicyId': securityPolicyId})

@register('GetVpnProfileParcelForMobility')
def GetVpnProfileParcelForMobility(profileId: str):
    return CatalystClient().GetVpnProfileParcelForMobility(**{'profileId': profileId})

@register('GetVpnProfileParcelByParcelIdForMobility')
def GetVpnProfileParcelByParcelIdForMobility(profileId: str, vpnId: str):
    return CatalystClient().GetVpnProfileParcelByParcelIdForMobility(**{'profileId': profileId, 'vpnId': vpnId})

@register('GetWifiProfileParcelListForMobility')
def GetWifiProfileParcelListForMobility(profileId: str):
    return CatalystClient().GetWifiProfileParcelListForMobility(**{'profileId': profileId})

@register('GetWifiProfileParcelForMobility')
def GetWifiProfileParcelForMobility(profileId: str, wifiId: str):
    return CatalystClient().GetWifiProfileParcelForMobility(**{'profileId': profileId, 'wifiId': wifiId})

@register('GetAllNfvirtualCLIFeatureProfiles')
def GetAllNfvirtualCLIFeatureProfiles(**kwargs):
    return CatalystClient().GetAllNfvirtualCLIFeatureProfiles(**{**kwargs})

@register('GetNfvirtualCLIFeatureProfileByid')
def GetNfvirtualCLIFeatureProfileByid(cliId: str):
    return CatalystClient().GetNfvirtualCLIFeatureProfileByid(**{'cliId': cliId})

@register('getNfvirtualCLIParcel')
def getNfvirtualCLIParcel(cliId: str, configId: str):
    return CatalystClient().getNfvirtualCLIParcel(**{'cliId': cliId, 'configId': configId})

@register('GetAllNfvirtualNetworksFeatureProfiles')
def GetAllNfvirtualNetworksFeatureProfiles(limit: int, offset: int):
    return CatalystClient().GetAllNfvirtualNetworksFeatureProfiles(**{'limit': limit, 'offset': offset})

@register('GetAllNfvirtualOvsNetworksFeatureProfileByProfileId')
def GetAllNfvirtualOvsNetworksFeatureProfileByProfileId(details: bool, networkId: str):
    return CatalystClient().GetAllNfvirtualOvsNetworksFeatureProfileByProfileId(**{'details': details, 'networkId': networkId})

@register('GetNfvirtualNetworksFeatureProfileByProfileId')
def GetNfvirtualNetworksFeatureProfileByProfileId(details: bool, networkId: str):
    return CatalystClient().GetNfvirtualNetworksFeatureProfileByProfileId(**{'details': details, 'networkId': networkId})

@register('GetNfvirtualLANParcel')
def GetNfvirtualLANParcel(lanId: str, networksId: str):
    return CatalystClient().GetNfvirtualLANParcel(**{'lanId': lanId, 'networksId': networksId})

@register('GetNfvirtualOVSNetworkParcel')
def GetNfvirtualOVSNetworkParcel(networksId: str, ovsNetworkId: str):
    return CatalystClient().GetNfvirtualOVSNetworkParcel(**{'networksId': networksId, 'ovsNetworkId': ovsNetworkId})

@register('GetNfvirtualRoutesParcel')
def GetNfvirtualRoutesParcel(networksId: str, routesId: str):
    return CatalystClient().GetNfvirtualRoutesParcel(**{'networksId': networksId, 'routesId': routesId})

@register('GetNfvirtualSwitchParcel')
def GetNfvirtualSwitchParcel(networksId: str, switchId: str):
    return CatalystClient().GetNfvirtualSwitchParcel(**{'networksId': networksId, 'switchId': switchId})

@register('GetNfvirtualVNFAttributesParcel')
def GetNfvirtualVNFAttributesParcel(networksId: str, vnfAttributesId: str):
    return CatalystClient().GetNfvirtualVNFAttributesParcel(**{'networksId': networksId, 'vnfAttributesId': vnfAttributesId})

@register('GetNfvirtualVNFParcel')
def GetNfvirtualVNFParcel(networksId: str, vnfAttributesId: str, vnfId: str):
    return CatalystClient().GetNfvirtualVNFParcel(**{'networksId': networksId, 'vnfAttributesId': vnfAttributesId, 'vnfId': vnfId})

@register('GetNfvirtualWANParcel')
def GetNfvirtualWANParcel(networksId: str, wanId: str):
    return CatalystClient().GetNfvirtualWANParcel(**{'networksId': networksId, 'wanId': wanId})

@register('GetAllNfvirtualSystemFeatureProfiles')
def GetAllNfvirtualSystemFeatureProfiles(**kwargs):
    return CatalystClient().GetAllNfvirtualSystemFeatureProfiles(**{**kwargs})

@register('GetNfvirtualSystemFeatureProfileByProfileId')
def GetNfvirtualSystemFeatureProfileByProfileId(systemId: str):
    return CatalystClient().GetNfvirtualSystemFeatureProfileByProfileId(**{'systemId': systemId})

@register('GetNfvirtualAAAParcel')
def GetNfvirtualAAAParcel(aaaId: str, systemId: str):
    return CatalystClient().GetNfvirtualAAAParcel(**{'aaaId': aaaId, 'systemId': systemId})

@register('GetNfvirtualBannerParcel')
def GetNfvirtualBannerParcel(bannerId: str, systemId: str):
    return CatalystClient().GetNfvirtualBannerParcel(**{'bannerId': bannerId, 'systemId': systemId})

@register('GetNfvirtualLoggingParcel')
def GetNfvirtualLoggingParcel(loggingId: str, systemId: str):
    return CatalystClient().GetNfvirtualLoggingParcel(**{'loggingId': loggingId, 'systemId': systemId})

@register('GetNfvirtualNTPParcel')
def GetNfvirtualNTPParcel(ntpId: str, systemId: str):
    return CatalystClient().GetNfvirtualNTPParcel(**{'ntpId': ntpId, 'systemId': systemId})

@register('GetNfvirtualSNMPParcel')
def GetNfvirtualSNMPParcel(snmpId: str, systemId: str):
    return CatalystClient().GetNfvirtualSNMPParcel(**{'snmpId': snmpId, 'systemId': systemId})

@register('GetNfvirtualSystemSettingsParcel')
def GetNfvirtualSystemSettingsParcel(systemId: str, systemSettingsId: str):
    return CatalystClient().GetNfvirtualSystemSettingsParcel(**{'systemId': systemId, 'systemSettingsId': systemSettingsId})

@register('GetSdroutingFeatureProfiles')
def GetSdroutingFeatureProfiles(**kwargs):
    return CatalystClient().GetSdroutingFeatureProfiles(**{**kwargs})

@register('GetSdroutingCliFeatureProfiles')
def GetSdroutingCliFeatureProfiles(**kwargs):
    return CatalystClient().GetSdroutingCliFeatureProfiles(**{**kwargs})

@register('Get')
def Get(**kwargs):
    return CatalystClient().Get(**{**kwargs})

@register('GetSdroutingCliFeatureProfile')
def GetSdroutingCliFeatureProfile(cliId: str):
    return CatalystClient().GetSdroutingCliFeatureProfile(**{'cliId': cliId})

@register('GetSdroutingCLIAddOnFeatures')
def GetSdroutingCLIAddOnFeatures(cliId: str):
    return CatalystClient().GetSdroutingCLIAddOnFeatures(**{'cliId': cliId})

@register('GetSdroutingCLIAddOnFeature')
def GetSdroutingCLIAddOnFeature(cliId: str, configId: str):
    return CatalystClient().GetSdroutingCLIAddOnFeature(**{'cliId': cliId, 'configId': configId})

@register('GetSdroutingCliConfigGroupFeatures')
def GetSdroutingCliConfigGroupFeatures(cliId: str):
    return CatalystClient().GetSdroutingCliConfigGroupFeatures(**{'cliId': cliId})

@register('GetSdroutingCliConfigGroupFeature')
def GetSdroutingCliConfigGroupFeature(cliId: str, fullConfigId: str):
    return CatalystClient().GetSdroutingCliConfigGroupFeature(**{'cliId': cliId, 'fullConfigId': fullConfigId})

@register('GetSdroutingIosCLassicCLIAddOnFeatures')
def GetSdroutingIosCLassicCLIAddOnFeatures(cliId: str):
    return CatalystClient().GetSdroutingIosCLassicCLIAddOnFeatures(**{'cliId': cliId})

@register('GetSdroutingIosClassicCLIAddOnFeature')
def GetSdroutingIosClassicCLIAddOnFeature(cliId: str, iosConfigId: str):
    return CatalystClient().GetSdroutingIosClassicCLIAddOnFeature(**{'cliId': cliId, 'iosConfigId': iosConfigId})

@register('GetSdRoutingEmbeddedSecurityFeatureProfiles')
def GetSdRoutingEmbeddedSecurityFeatureProfiles(**kwargs):
    return CatalystClient().GetSdRoutingEmbeddedSecurityFeatureProfiles(**{**kwargs})

@register('GetSdRoutingEmbeddedSecurityFeatureProfileByProfileId')
def GetSdRoutingEmbeddedSecurityFeatureProfileByProfileId(embeddedSecurityId: str, **kwargs):
    return CatalystClient().GetSdRoutingEmbeddedSecurityFeatureProfileByProfileId(**{'embeddedSecurityId': embeddedSecurityId, **kwargs})

@register('GetSecurityFeature')
def GetSecurityFeature(securityId: str):
    return CatalystClient().GetSecurityFeature(**{'securityId': securityId})

@register('GetSecurityFeatureByFeatureId')
def GetSecurityFeatureByFeatureId(securityId: str, securityProfileParcelId: str):
    return CatalystClient().GetSecurityFeatureByFeatureId(**{'securityId': securityId, 'securityProfileParcelId': securityProfileParcelId})

@register('GetNgfirewallFeature')
def GetNgfirewallFeature(securityId: str):
    return CatalystClient().GetNgfirewallFeature(**{'securityId': securityId})

@register('GetNgfirewallFeatureByFeatureId')
def GetNgfirewallFeatureByFeatureId(securityId: str, securityProfileParcelId: str):
    return CatalystClient().GetNgfirewallFeatureByFeatureId(**{'securityId': securityId, 'securityProfileParcelId': securityProfileParcelId})

@register('GetCybervisionProfileFeatureForOther')
def GetCybervisionProfileFeatureForOther(otherId: str):
    return CatalystClient().GetCybervisionProfileFeatureForOther(**{'otherId': otherId})

@register('GetCybervisionProfileFeatureByFeatureIdForOther')
def GetCybervisionProfileFeatureByFeatureIdForOther(cybervisionId: str, otherId: str):
    return CatalystClient().GetCybervisionProfileFeatureByFeatureIdForOther(**{'cybervisionId': cybervisionId, 'otherId': otherId})

@register('GetSdroutingServiceFeatureProfiles')
def GetSdroutingServiceFeatureProfiles(**kwargs):
    return CatalystClient().GetSdroutingServiceFeatureProfiles(**{**kwargs})

@register('GetSdroutingServiceFeatureProfile')
def GetSdroutingServiceFeatureProfile(serviceId: str):
    return CatalystClient().GetSdroutingServiceFeatureProfile(**{'serviceId': serviceId})

@register('GetSdroutingDhcpServerProfileParcels')
def GetSdroutingDhcpServerProfileParcels(serviceId: str):
    return CatalystClient().GetSdroutingDhcpServerProfileParcels(**{'serviceId': serviceId})

@register('GetSdroutingDhcpServerProfileParcel')
def GetSdroutingDhcpServerProfileParcel(dhcpServerId: str, serviceId: str):
    return CatalystClient().GetSdroutingDhcpServerProfileParcel(**{'dhcpServerId': dhcpServerId, 'serviceId': serviceId})

@register('GetSdroutingServiceIpsecProfileFeatures')
def GetSdroutingServiceIpsecProfileFeatures(serviceId: str):
    return CatalystClient().GetSdroutingServiceIpsecProfileFeatures(**{'serviceId': serviceId})

@register('GetSdroutingServiceIpsecProfileFeature')
def GetSdroutingServiceIpsecProfileFeature(ipsecProfileId: str, serviceId: str):
    return CatalystClient().GetSdroutingServiceIpsecProfileFeature(**{'ipsecProfileId': ipsecProfileId, 'serviceId': serviceId})

@register('GetSdroutingServiceIpv4AclFeatures')
def GetSdroutingServiceIpv4AclFeatures(serviceId: str):
    return CatalystClient().GetSdroutingServiceIpv4AclFeatures(**{'serviceId': serviceId})

@register('GetSdroutingServiceIpv4AclFeature')
def GetSdroutingServiceIpv4AclFeature(ipv4AclId: str, serviceId: str):
    return CatalystClient().GetSdroutingServiceIpv4AclFeature(**{'ipv4AclId': ipv4AclId, 'serviceId': serviceId})

@register('GetListOfProfileParcels')
def GetListOfProfileParcels(serviceId: str):
    return CatalystClient().GetListOfProfileParcels(**{'serviceId': serviceId})

@register('GetMultiCloudConnection')
def GetMultiCloudConnection(multiCloudConnectionId: str, serviceId: str):
    return CatalystClient().GetMultiCloudConnection(**{'multiCloudConnectionId': multiCloudConnectionId, 'serviceId': serviceId})

@register('GetSdroutingServiceObjectTrackerFeatures')
def GetSdroutingServiceObjectTrackerFeatures(serviceId: str):
    return CatalystClient().GetSdroutingServiceObjectTrackerFeatures(**{'serviceId': serviceId})

@register('GetSdroutingServiceObjectTrackerFeature')
def GetSdroutingServiceObjectTrackerFeature(objectTrackerId: str, serviceId: str):
    return CatalystClient().GetSdroutingServiceObjectTrackerFeature(**{'objectTrackerId': objectTrackerId, 'serviceId': serviceId})

@register('GetSdroutingServiceObjectTrackerGroupFeatures')
def GetSdroutingServiceObjectTrackerGroupFeatures(serviceId: str):
    return CatalystClient().GetSdroutingServiceObjectTrackerGroupFeatures(**{'serviceId': serviceId})

@register('GetSdroutingServiceObjectTrackerGroupFeature')
def GetSdroutingServiceObjectTrackerGroupFeature(objectTrackerGroupId: str, serviceId: str):
    return CatalystClient().GetSdroutingServiceObjectTrackerGroupFeature(**{'objectTrackerGroupId': objectTrackerGroupId, 'serviceId': serviceId})

@register('GetSdroutingServiceRoutePolicyFeatures')
def GetSdroutingServiceRoutePolicyFeatures(serviceId: str):
    return CatalystClient().GetSdroutingServiceRoutePolicyFeatures(**{'serviceId': serviceId})

@register('GetSdroutingServiceRoutePolicyFeature')
def GetSdroutingServiceRoutePolicyFeature(routePolicyId: str, serviceId: str):
    return CatalystClient().GetSdroutingServiceRoutePolicyFeature(**{'routePolicyId': routePolicyId, 'serviceId': serviceId})

@register('GetSdroutingServiceVrfOspfFeatures')
def GetSdroutingServiceVrfOspfFeatures(serviceId: str):
    return CatalystClient().GetSdroutingServiceVrfOspfFeatures(**{'serviceId': serviceId})

@register('GetSdroutingServiceVrfOspfFeature')
def GetSdroutingServiceVrfOspfFeature(ospfId: str, serviceId: str):
    return CatalystClient().GetSdroutingServiceVrfOspfFeature(**{'ospfId': ospfId, 'serviceId': serviceId})

@register('GetSdroutingServiceVrfOspfv3Ipv4Features')
def GetSdroutingServiceVrfOspfv3Ipv4Features(serviceId: str):
    return CatalystClient().GetSdroutingServiceVrfOspfv3Ipv4Features(**{'serviceId': serviceId})

@register('GetSdroutingServiceVrfOspfv3Ipv4Feature')
def GetSdroutingServiceVrfOspfv3Ipv4Feature(ospfv3Id: str, serviceId: str):
    return CatalystClient().GetSdroutingServiceVrfOspfv3Ipv4Feature(**{'ospfv3Id': ospfv3Id, 'serviceId': serviceId})

@register('GetSdroutingServiceVrfOspfv3Ipv6Features')
def GetSdroutingServiceVrfOspfv3Ipv6Features(serviceId: str):
    return CatalystClient().GetSdroutingServiceVrfOspfv3Ipv6Features(**{'serviceId': serviceId})

@register('GetSdroutingServiceVrfOspfv3Ipv6Feature')
def GetSdroutingServiceVrfOspfv3Ipv6Feature(ospfv3Id: str, serviceId: str):
    return CatalystClient().GetSdroutingServiceVrfOspfv3Ipv6Feature(**{'ospfv3Id': ospfv3Id, 'serviceId': serviceId})

@register('GetSdroutingServiceVRFFeatures')
def GetSdroutingServiceVRFFeatures(serviceId: str):
    return CatalystClient().GetSdroutingServiceVRFFeatures(**{'serviceId': serviceId})

@register('GetSdroutingServiceVrfBgpFeatures')
def GetSdroutingServiceVrfBgpFeatures(serviceId: str):
    return CatalystClient().GetSdroutingServiceVrfBgpFeatures(**{'serviceId': serviceId})

@register('GetSdroutingServiceVrfBgpFeature')
def GetSdroutingServiceVrfBgpFeature(bgpId: str, serviceId: str):
    return CatalystClient().GetSdroutingServiceVrfBgpFeature(**{'bgpId': bgpId, 'serviceId': serviceId})

@register('GetSdroutingServiceVrfEigrpFeatures')
def GetSdroutingServiceVrfEigrpFeatures(serviceId: str):
    return CatalystClient().GetSdroutingServiceVrfEigrpFeatures(**{'serviceId': serviceId})

@register('GetSdroutingServiceVrfEigrpFeature')
def GetSdroutingServiceVrfEigrpFeature(eigrpId: str, serviceId: str):
    return CatalystClient().GetSdroutingServiceVrfEigrpFeature(**{'eigrpId': eigrpId, 'serviceId': serviceId})

@register('GetSdroutingServiceVRFFeature')
def GetSdroutingServiceVRFFeature(serviceId: str, vrfId: str):
    return CatalystClient().GetSdroutingServiceVRFFeature(**{'serviceId': serviceId, 'vrfId': vrfId})

@register('GetSdroutingServiceVRFDmvpnTunnelFeatures')
def GetSdroutingServiceVRFDmvpnTunnelFeatures(serviceId: str, vrfId: str):
    return CatalystClient().GetSdroutingServiceVRFDmvpnTunnelFeatures(**{'serviceId': serviceId, 'vrfId': vrfId})

@register('GetSdroutingServiceVRFDmvpnTunnelFeature')
def GetSdroutingServiceVRFDmvpnTunnelFeature(serviceId: str, tunnelId: str, vrfId: str):
    return CatalystClient().GetSdroutingServiceVRFDmvpnTunnelFeature(**{'serviceId': serviceId, 'tunnelId': tunnelId, 'vrfId': vrfId})

@register('GetSdroutingServiceVrfInterfaceEthernetFeaturesForService')
def GetSdroutingServiceVrfInterfaceEthernetFeaturesForService(serviceId: str, vrfId: str):
    return CatalystClient().GetSdroutingServiceVrfInterfaceEthernetFeaturesForService(**{'serviceId': serviceId, 'vrfId': vrfId})

@register('GetSdroutingServiceVrfInterfaceEthernetFeatureByFeatureIdForService')
def GetSdroutingServiceVrfInterfaceEthernetFeatureByFeatureIdForService(ethernetId: str, serviceId: str, vrfId: str):
    return CatalystClient().GetSdroutingServiceVrfInterfaceEthernetFeatureByFeatureIdForService(**{'ethernetId': ethernetId, 'serviceId': serviceId, 'vrfId': vrfId})

@register('GetVrfInterfaceEthernetAssociatedDhcpServerParcelsForService')
def GetVrfInterfaceEthernetAssociatedDhcpServerParcelsForService(ethernetId: str, serviceId: str, vrfId: str):
    return CatalystClient().GetVrfInterfaceEthernetAssociatedDhcpServerParcelsForService(**{'ethernetId': ethernetId, 'serviceId': serviceId, 'vrfId': vrfId})

@register('GetVrfInterfaceEthernetAssociatedDhcpServerParcelByFeatureIdForService')
def GetVrfInterfaceEthernetAssociatedDhcpServerParcelByFeatureIdForService(dhcpServerId: str, ethernetId: str, serviceId: str, vrfId: str):
    return CatalystClient().GetVrfInterfaceEthernetAssociatedDhcpServerParcelByFeatureIdForService(**{'dhcpServerId': dhcpServerId, 'ethernetId': ethernetId, 'serviceId': serviceId, 'vrfId': vrfId})

@register('GetSdroutingServiceVrfInterfaceIpsecFeaturesForService')
def GetSdroutingServiceVrfInterfaceIpsecFeaturesForService(serviceId: str, vrfId: str):
    return CatalystClient().GetSdroutingServiceVrfInterfaceIpsecFeaturesForService(**{'serviceId': serviceId, 'vrfId': vrfId})

@register('GetSdroutingServiceVrfInterfaceIpsecFeatureByFeatureIdForService')
def GetSdroutingServiceVrfInterfaceIpsecFeatureByFeatureIdForService(ipsecId: str, serviceId: str, vrfId: str):
    return CatalystClient().GetSdroutingServiceVrfInterfaceIpsecFeatureByFeatureIdForService(**{'ipsecId': ipsecId, 'serviceId': serviceId, 'vrfId': vrfId})

@register('GetServiceVrfAssociatedRoutingBgpFeatures')
def GetServiceVrfAssociatedRoutingBgpFeatures(serviceId: str, vrfId: str):
    return CatalystClient().GetServiceVrfAssociatedRoutingBgpFeatures(**{'serviceId': serviceId, 'vrfId': vrfId})

@register('GetServiceVrfAssociatedRoutingBgpParcelByParcelId')
def GetServiceVrfAssociatedRoutingBgpParcelByParcelId(bgpId: str, serviceId: str, vrfId: str):
    return CatalystClient().GetServiceVrfAssociatedRoutingBgpParcelByParcelId(**{'bgpId': bgpId, 'serviceId': serviceId, 'vrfId': vrfId})

@register('GetServiceVrfAssociatedRoutingEigrpFeatures')
def GetServiceVrfAssociatedRoutingEigrpFeatures(serviceId: str, vrfId: str):
    return CatalystClient().GetServiceVrfAssociatedRoutingEigrpFeatures(**{'serviceId': serviceId, 'vrfId': vrfId})

@register('GetServiceVrfAssociatedRoutingEigrpFeatureByFeatureId')
def GetServiceVrfAssociatedRoutingEigrpFeatureByFeatureId(eigrpId: str, serviceId: str, vrfId: str):
    return CatalystClient().GetServiceVrfAssociatedRoutingEigrpFeatureByFeatureId(**{'eigrpId': eigrpId, 'serviceId': serviceId, 'vrfId': vrfId})

@register('GetServiceVrfAssociatedRoutingOspfFeatures')
def GetServiceVrfAssociatedRoutingOspfFeatures(serviceId: str, vrfId: str):
    return CatalystClient().GetServiceVrfAssociatedRoutingOspfFeatures(**{'serviceId': serviceId, 'vrfId': vrfId})

@register('GetServiceVrfAssociatedRoutingOspfFeatureById')
def GetServiceVrfAssociatedRoutingOspfFeatureById(ospfId: str, serviceId: str, vrfId: str):
    return CatalystClient().GetServiceVrfAssociatedRoutingOspfFeatureById(**{'ospfId': ospfId, 'serviceId': serviceId, 'vrfId': vrfId})

@register('GetServiceVrfAssociatedRoutingOspfv3Ipv4Features')
def GetServiceVrfAssociatedRoutingOspfv3Ipv4Features(serviceId: str, vrfId: str):
    return CatalystClient().GetServiceVrfAssociatedRoutingOspfv3Ipv4Features(**{'serviceId': serviceId, 'vrfId': vrfId})

@register('GetServiceVrfAssociatedRoutingOspfv3Ipv4FeatureById')
def GetServiceVrfAssociatedRoutingOspfv3Ipv4FeatureById(ospfv3Id: str, serviceId: str, vrfId: str):
    return CatalystClient().GetServiceVrfAssociatedRoutingOspfv3Ipv4FeatureById(**{'ospfv3Id': ospfv3Id, 'serviceId': serviceId, 'vrfId': vrfId})

@register('GetServiceVrfAssociatedRoutingOspfv3Ipv6Parcels')
def GetServiceVrfAssociatedRoutingOspfv3Ipv6Parcels(serviceId: str, vrfId: str):
    return CatalystClient().GetServiceVrfAssociatedRoutingOspfv3Ipv6Parcels(**{'serviceId': serviceId, 'vrfId': vrfId})

@register('GetServiceVrfAssociatedRoutingOspfv3Ipv6FeatureById')
def GetServiceVrfAssociatedRoutingOspfv3Ipv6FeatureById(ospfv3Id: str, serviceId: str, vrfId: str):
    return CatalystClient().GetServiceVrfAssociatedRoutingOspfv3Ipv6FeatureById(**{'ospfv3Id': ospfv3Id, 'serviceId': serviceId, 'vrfId': vrfId})

@register('GetSdRoutingSseFeatureProfiles')
def GetSdRoutingSseFeatureProfiles(**kwargs):
    return CatalystClient().GetSdRoutingSseFeatureProfiles(**{**kwargs})

@register('GetSdRoutingSseFeatureProfileByProfileId')
def GetSdRoutingSseFeatureProfileByProfileId(sseId: str, **kwargs):
    return CatalystClient().GetSdRoutingSseFeatureProfileByProfileId(**{'sseId': sseId, **kwargs})

@register('GetCiscoSseFeatureForSse')
def GetCiscoSseFeatureForSse(sseId: str):
    return CatalystClient().GetCiscoSseFeatureForSse(**{'sseId': sseId})

@register('GetCiscoSseFeatureByFeatureIdForSSE')
def GetCiscoSseFeatureByFeatureIdForSSE(ciscoSseId: str, sseId: str):
    return CatalystClient().GetCiscoSseFeatureByFeatureIdForSSE(**{'ciscoSseId': ciscoSseId, 'sseId': sseId})

@register('GetSdroutingSystemFeatureProfiles')
def GetSdroutingSystemFeatureProfiles(**kwargs):
    return CatalystClient().GetSdroutingSystemFeatureProfiles(**{**kwargs})

@register('GetSdroutingSystemFeatureProfile')
def GetSdroutingSystemFeatureProfile(systemId: str):
    return CatalystClient().GetSdroutingSystemFeatureProfile(**{'systemId': systemId})

@register('GetSdroutingAaaFeatures')
def GetSdroutingAaaFeatures(systemId: str):
    return CatalystClient().GetSdroutingAaaFeatures(**{'systemId': systemId})

@register('GetSdroutingAaaFeature')
def GetSdroutingAaaFeature(aaaId: str, systemId: str):
    return CatalystClient().GetSdroutingAaaFeature(**{'aaaId': aaaId, 'systemId': systemId})

@register('GetSdroutingBannerFeatures')
def GetSdroutingBannerFeatures(systemId: str):
    return CatalystClient().GetSdroutingBannerFeatures(**{'systemId': systemId})

@register('GetSdroutingBannerFeature')
def GetSdroutingBannerFeature(bannerId: str, systemId: str):
    return CatalystClient().GetSdroutingBannerFeature(**{'bannerId': bannerId, 'systemId': systemId})

@register('GetSdroutingCertificateFeatures')
def GetSdroutingCertificateFeatures(systemId: str):
    return CatalystClient().GetSdroutingCertificateFeatures(**{'systemId': systemId})

@register('GetSdroutingCertificateFeature')
def GetSdroutingCertificateFeature(certificateId: str, systemId: str):
    return CatalystClient().GetSdroutingCertificateFeature(**{'certificateId': certificateId, 'systemId': systemId})

@register('GetSdroutingFlexiblePortSpeedFeatures')
def GetSdroutingFlexiblePortSpeedFeatures(systemId: str):
    return CatalystClient().GetSdroutingFlexiblePortSpeedFeatures(**{'systemId': systemId})

@register('GetSdroutingFlexiblePortSpeedFeature')
def GetSdroutingFlexiblePortSpeedFeature(flexiblePortSpeedId: str, systemId: str):
    return CatalystClient().GetSdroutingFlexiblePortSpeedFeature(**{'flexiblePortSpeedId': flexiblePortSpeedId, 'systemId': systemId})

@register('GetSdroutingGlobalSettingFeatures')
def GetSdroutingGlobalSettingFeatures(systemId: str):
    return CatalystClient().GetSdroutingGlobalSettingFeatures(**{'systemId': systemId})

@register('GetSdroutingGlobalSettingFeature')
def GetSdroutingGlobalSettingFeature(globalId: str, systemId: str):
    return CatalystClient().GetSdroutingGlobalSettingFeature(**{'globalId': globalId, 'systemId': systemId})

@register('GetSdroutingLoggingFeatures')
def GetSdroutingLoggingFeatures(systemId: str):
    return CatalystClient().GetSdroutingLoggingFeatures(**{'systemId': systemId})

@register('GetSdroutingLoggingFeature')
def GetSdroutingLoggingFeature(loggingId: str, systemId: str):
    return CatalystClient().GetSdroutingLoggingFeature(**{'loggingId': loggingId, 'systemId': systemId})

@register('GetSdroutingNtpFeatures')
def GetSdroutingNtpFeatures(systemId: str):
    return CatalystClient().GetSdroutingNtpFeatures(**{'systemId': systemId})

@register('GetSdroutingNtpFeature')
def GetSdroutingNtpFeature(ntpId: str, systemId: str):
    return CatalystClient().GetSdroutingNtpFeature(**{'ntpId': ntpId, 'systemId': systemId})

@register('GetSdroutingSnmpFeatures')
def GetSdroutingSnmpFeatures(systemId: str):
    return CatalystClient().GetSdroutingSnmpFeatures(**{'systemId': systemId})

@register('GetSdroutingSnmpFeature')
def GetSdroutingSnmpFeature(snmpId: str, systemId: str):
    return CatalystClient().GetSdroutingSnmpFeature(**{'snmpId': snmpId, 'systemId': systemId})

@register('GetSdroutingTransportFeatureProfiles')
def GetSdroutingTransportFeatureProfiles(**kwargs):
    return CatalystClient().GetSdroutingTransportFeatureProfiles(**{**kwargs})

@register('GetSdroutingTransportFeatureProfile')
def GetSdroutingTransportFeatureProfile(transportId: str):
    return CatalystClient().GetSdroutingTransportFeatureProfile(**{'transportId': transportId})

@register('GetCellularControllerProfileParcelForTransport_1')
def GetCellularControllerProfileParcelForTransport_1(transportId: str):
    return CatalystClient().GetCellularControllerProfileParcelForTransport_1(**{'transportId': transportId})

@register('GetCellularControllerProfileParcelByParcelIdForTransport_1')
def GetCellularControllerProfileParcelByParcelIdForTransport_1(cellularControllerId: str, transportId: str):
    return CatalystClient().GetCellularControllerProfileParcelByParcelIdForTransport_1(**{'cellularControllerId': cellularControllerId, 'transportId': transportId})

@register('GetCellularControllerAssociatedCellularProfileParcelsForTransport_1')
def GetCellularControllerAssociatedCellularProfileParcelsForTransport_1(cellularControllerId: str, transportId: str):
    return CatalystClient().GetCellularControllerAssociatedCellularProfileParcelsForTransport_1(**{'cellularControllerId': cellularControllerId, 'transportId': transportId})

@register('GetCellularControllerAssociatedCellularProfileParcelByParcelIdForTransport_1')
def GetCellularControllerAssociatedCellularProfileParcelByParcelIdForTransport_1(cellularControllerId: str, cellularProfileId: str, transportId: str):
    return CatalystClient().GetCellularControllerAssociatedCellularProfileParcelByParcelIdForTransport_1(**{'cellularControllerId': cellularControllerId, 'cellularProfileId': cellularProfileId, 'transportId': transportId})

@register('GetCellularControllerAssociatedGpsParcelsForTransport_1')
def GetCellularControllerAssociatedGpsParcelsForTransport_1(cellularControllerId: str, transportId: str):
    return CatalystClient().GetCellularControllerAssociatedGpsParcelsForTransport_1(**{'cellularControllerId': cellularControllerId, 'transportId': transportId})

@register('GetCellularControllerAssociatedGpsParcelByParcelIdForTransport_1')
def GetCellularControllerAssociatedGpsParcelByParcelIdForTransport_1(cellularControllerId: str, gpsId: str, transportId: str):
    return CatalystClient().GetCellularControllerAssociatedGpsParcelByParcelIdForTransport_1(**{'cellularControllerId': cellularControllerId, 'gpsId': gpsId, 'transportId': transportId})

@register('GetCellularProfileParcelForTransport')
def GetCellularProfileParcelForTransport(transportId: str):
    return CatalystClient().GetCellularProfileParcelForTransport(**{'transportId': transportId})

@register('GetCellularProfileParcelByParcelIdForTransport')
def GetCellularProfileParcelByParcelIdForTransport(cellularProfileId: str, transportId: str):
    return CatalystClient().GetCellularProfileParcelByParcelIdForTransport(**{'cellularProfileId': cellularProfileId, 'transportId': transportId})

@register('GetSdroutingTransportGlobalVRFFeatures')
def GetSdroutingTransportGlobalVRFFeatures(transportId: str):
    return CatalystClient().GetSdroutingTransportGlobalVRFFeatures(**{'transportId': transportId})

@register('GetSdroutingTransportGlobalVrfBgpFeatures')
def GetSdroutingTransportGlobalVrfBgpFeatures(transportId: str):
    return CatalystClient().GetSdroutingTransportGlobalVrfBgpFeatures(**{'transportId': transportId})

@register('GetSdroutingTransportGlobalVrfBgpFeature')
def GetSdroutingTransportGlobalVrfBgpFeature(bgpId: str, transportId: str):
    return CatalystClient().GetSdroutingTransportGlobalVrfBgpFeature(**{'bgpId': bgpId, 'transportId': transportId})

@register('GetSdroutingTransportGlobalVRFFeature')
def GetSdroutingTransportGlobalVRFFeature(transportId: str, vrfId: str):
    return CatalystClient().GetSdroutingTransportGlobalVRFFeature(**{'transportId': transportId, 'vrfId': vrfId})

@register('GetGlobalVRFInterfaceCellularParcelsForTransport')
def GetGlobalVRFInterfaceCellularParcelsForTransport(transportId: str, vrfId: str):
    return CatalystClient().GetGlobalVRFInterfaceCellularParcelsForTransport(**{'transportId': transportId, 'vrfId': vrfId})

@register('GetGlobalVRFInterfaceCellularAssociatedTrackerParcelsForTransport_1')
def GetGlobalVRFInterfaceCellularAssociatedTrackerParcelsForTransport_1(cellularId: str, transportId: str, vrfId: str):
    return CatalystClient().GetGlobalVRFInterfaceCellularAssociatedTrackerParcelsForTransport_1(**{'cellularId': cellularId, 'transportId': transportId, 'vrfId': vrfId})

@register('GetGlobalVRFInterfaceCellularAssociatedTrackerParcelByParcelIdForTransport_1')
def GetGlobalVRFInterfaceCellularAssociatedTrackerParcelByParcelIdForTransport_1(cellularId: str, trackerId: str, transportId: str, vrfId: str):
    return CatalystClient().GetGlobalVRFInterfaceCellularAssociatedTrackerParcelByParcelIdForTransport_1(**{'cellularId': cellularId, 'trackerId': trackerId, 'transportId': transportId, 'vrfId': vrfId})

@register('GetGlobalVRFInterfaceCellularAssociatedTrackerParcelsForTransport')
def GetGlobalVRFInterfaceCellularAssociatedTrackerParcelsForTransport(cellularId: str, transportId: str, vrfId: str):
    return CatalystClient().GetGlobalVRFInterfaceCellularAssociatedTrackerParcelsForTransport(**{'cellularId': cellularId, 'transportId': transportId, 'vrfId': vrfId})

@register('GetGlobalVRFInterfaceCellularAssociatedTrackerParcelByParcelIdForTransport')
def GetGlobalVRFInterfaceCellularAssociatedTrackerParcelByParcelIdForTransport(cellularId: str, trackerId: str, transportId: str, vrfId: str):
    return CatalystClient().GetGlobalVRFInterfaceCellularAssociatedTrackerParcelByParcelIdForTransport(**{'cellularId': cellularId, 'trackerId': trackerId, 'transportId': transportId, 'vrfId': vrfId})

@register('GetGlobalVRFInterfaceCellularParcelByParcelIdForTransport')
def GetGlobalVRFInterfaceCellularParcelByParcelIdForTransport(intfId: str, transportId: str, vrfId: str):
    return CatalystClient().GetGlobalVRFInterfaceCellularParcelByParcelIdForTransport(**{'intfId': intfId, 'transportId': transportId, 'vrfId': vrfId})

@register('GetSdroutingTransportGlobalVrfInterfaceEthernetParcelsForTransport')
def GetSdroutingTransportGlobalVrfInterfaceEthernetParcelsForTransport(transportId: str, vrfId: str):
    return CatalystClient().GetSdroutingTransportGlobalVrfInterfaceEthernetParcelsForTransport(**{'transportId': transportId, 'vrfId': vrfId})

@register('GetSdroutingTransportGlobalVrfInterfaceEthernetParcelByParcelIdForTransport')
def GetSdroutingTransportGlobalVrfInterfaceEthernetParcelByParcelIdForTransport(ethernetId: str, transportId: str, vrfId: str):
    return CatalystClient().GetSdroutingTransportGlobalVrfInterfaceEthernetParcelByParcelIdForTransport(**{'ethernetId': ethernetId, 'transportId': transportId, 'vrfId': vrfId})

@register('GetSdroutingTransportGlobalVrfInterfaceIpsecFeaturesForTransport')
def GetSdroutingTransportGlobalVrfInterfaceIpsecFeaturesForTransport(transportId: str, vrfId: str):
    return CatalystClient().GetSdroutingTransportGlobalVrfInterfaceIpsecFeaturesForTransport(**{'transportId': transportId, 'vrfId': vrfId})

@register('GetSdroutingTransportGlobalVrfInterfaceIpsecFeatureByFeatureIdForTransport')
def GetSdroutingTransportGlobalVrfInterfaceIpsecFeatureByFeatureIdForTransport(ipsecId: str, transportId: str, vrfId: str):
    return CatalystClient().GetSdroutingTransportGlobalVrfInterfaceIpsecFeatureByFeatureIdForTransport(**{'ipsecId': ipsecId, 'transportId': transportId, 'vrfId': vrfId})

@register('GetTransportVrfAssociatedRoutingBgpFeatures')
def GetTransportVrfAssociatedRoutingBgpFeatures(transportId: str, vrfId: str):
    return CatalystClient().GetTransportVrfAssociatedRoutingBgpFeatures(**{'transportId': transportId, 'vrfId': vrfId})

@register('GetVrfAssociatedRoutingBgpFeatureById')
def GetVrfAssociatedRoutingBgpFeatureById(bgpId: str, transportId: str, vrfId: str):
    return CatalystClient().GetVrfAssociatedRoutingBgpFeatureById(**{'bgpId': bgpId, 'transportId': transportId, 'vrfId': vrfId})

@register('GetTransportVrfAssociatedRoutingOspfFeatures')
def GetTransportVrfAssociatedRoutingOspfFeatures(transportId: str, vrfId: str):
    return CatalystClient().GetTransportVrfAssociatedRoutingOspfFeatures(**{'transportId': transportId, 'vrfId': vrfId})

@register('GetVrfAssociatedRoutingOspfParcelByFeatureId')
def GetVrfAssociatedRoutingOspfParcelByFeatureId(ospfId: str, transportId: str, vrfId: str):
    return CatalystClient().GetVrfAssociatedRoutingOspfParcelByFeatureId(**{'ospfId': ospfId, 'transportId': transportId, 'vrfId': vrfId})

@register('GetTransportVrfAssociatedRoutingOspfv3Ipv4Features')
def GetTransportVrfAssociatedRoutingOspfv3Ipv4Features(transportId: str, vrfId: str):
    return CatalystClient().GetTransportVrfAssociatedRoutingOspfv3Ipv4Features(**{'transportId': transportId, 'vrfId': vrfId})

@register('GetVrfAssociatedRoutingOspfv3Ipv4FeatureById')
def GetVrfAssociatedRoutingOspfv3Ipv4FeatureById(ospfv3Id: str, transportId: str, vrfId: str):
    return CatalystClient().GetVrfAssociatedRoutingOspfv3Ipv4FeatureById(**{'ospfv3Id': ospfv3Id, 'transportId': transportId, 'vrfId': vrfId})

@register('GetTransportVrfAssociatedRoutingOspfv3Ipv6Features')
def GetTransportVrfAssociatedRoutingOspfv3Ipv6Features(transportId: str, vrfId: str):
    return CatalystClient().GetTransportVrfAssociatedRoutingOspfv3Ipv6Features(**{'transportId': transportId, 'vrfId': vrfId})

@register('GetVrfAssociatedRoutingOspfv3Ipv6FeatureById')
def GetVrfAssociatedRoutingOspfv3Ipv6FeatureById(ospfv3Id: str, transportId: str, vrfId: str):
    return CatalystClient().GetVrfAssociatedRoutingOspfv3Ipv6FeatureById(**{'ospfv3Id': ospfv3Id, 'transportId': transportId, 'vrfId': vrfId})

@register('GetGPSProfileParcelForTransport')
def GetGPSProfileParcelForTransport(transportId: str):
    return CatalystClient().GetGPSProfileParcelForTransport(**{'transportId': transportId})

@register('GetGPSProfileParcelByParcelIdForTransport')
def GetGPSProfileParcelByParcelIdForTransport(gpsId: str, transportId: str):
    return CatalystClient().GetGPSProfileParcelByParcelIdForTransport(**{'gpsId': gpsId, 'transportId': transportId})

@register('GetSdroutingTransportIpv4AclFeatures')
def GetSdroutingTransportIpv4AclFeatures(transportId: str):
    return CatalystClient().GetSdroutingTransportIpv4AclFeatures(**{'transportId': transportId})

@register('GetSdroutingTransportIpv4AclFeature')
def GetSdroutingTransportIpv4AclFeature(ipv4AclId: str, transportId: str):
    return CatalystClient().GetSdroutingTransportIpv4AclFeature(**{'ipv4AclId': ipv4AclId, 'transportId': transportId})

@register('GetSdroutingManagementVRFFeatures')
def GetSdroutingManagementVRFFeatures(transportId: str):
    return CatalystClient().GetSdroutingManagementVRFFeatures(**{'transportId': transportId})

@register('GetSdroutingManagementVRFFeature')
def GetSdroutingManagementVRFFeature(transportId: str, vrfId: str):
    return CatalystClient().GetSdroutingManagementVRFFeature(**{'transportId': transportId, 'vrfId': vrfId})

@register('GetSdroutingManagementVrfInterfaceEthernetParcelsForTransportProfile')
def GetSdroutingManagementVrfInterfaceEthernetParcelsForTransportProfile(transportId: str, vrfId: str):
    return CatalystClient().GetSdroutingManagementVrfInterfaceEthernetParcelsForTransportProfile(**{'transportId': transportId, 'vrfId': vrfId})

@register('GetSdroutingManagementVrfInterfaceEthernetParcelByParcelIdForTransportProfile')
def GetSdroutingManagementVrfInterfaceEthernetParcelByParcelIdForTransportProfile(ethernetId: str, transportId: str, vrfId: str):
    return CatalystClient().GetSdroutingManagementVrfInterfaceEthernetParcelByParcelIdForTransportProfile(**{'ethernetId': ethernetId, 'transportId': transportId, 'vrfId': vrfId})

@register('GetLanVpnProfileParcelForService_1')
def GetLanVpnProfileParcelForService_1(transportId: str):
    return CatalystClient().GetLanVpnProfileParcelForService_1(**{'transportId': transportId})

@register('GetLanVpnProfileParcelByParcelIdForService_1')
def GetLanVpnProfileParcelByParcelIdForService_1(multiCloudConnectionId: str, transportId: str):
    return CatalystClient().GetLanVpnProfileParcelByParcelIdForService_1(**{'multiCloudConnectionId': multiCloudConnectionId, 'transportId': transportId})

@register('GetSdroutingTransportObjectTrackerFeatures')
def GetSdroutingTransportObjectTrackerFeatures(transportId: str):
    return CatalystClient().GetSdroutingTransportObjectTrackerFeatures(**{'transportId': transportId})

@register('GetSdroutingTransportObjectTrackerFeature')
def GetSdroutingTransportObjectTrackerFeature(objectTrackerId: str, transportId: str):
    return CatalystClient().GetSdroutingTransportObjectTrackerFeature(**{'objectTrackerId': objectTrackerId, 'transportId': transportId})

@register('GetSdroutingTransportObjectTrackerGroupFeatures')
def GetSdroutingTransportObjectTrackerGroupFeatures(transportId: str):
    return CatalystClient().GetSdroutingTransportObjectTrackerGroupFeatures(**{'transportId': transportId})

@register('GetSdroutingTransportObjectTrackerGroupFeature')
def GetSdroutingTransportObjectTrackerGroupFeature(objectTrackerGroupId: str, transportId: str):
    return CatalystClient().GetSdroutingTransportObjectTrackerGroupFeature(**{'objectTrackerGroupId': objectTrackerGroupId, 'transportId': transportId})

@register('GetSdroutingTransportRoutePolicyFeatures')
def GetSdroutingTransportRoutePolicyFeatures(transportId: str):
    return CatalystClient().GetSdroutingTransportRoutePolicyFeatures(**{'transportId': transportId})

@register('GetSdroutingTransportRoutePolicyFeature')
def GetSdroutingTransportRoutePolicyFeature(routePolicyId: str, transportId: str):
    return CatalystClient().GetSdroutingTransportRoutePolicyFeature(**{'routePolicyId': routePolicyId, 'transportId': transportId})

@register('GetSdroutingTransportRoutingOspfFeatures')
def GetSdroutingTransportRoutingOspfFeatures(transportId: str):
    return CatalystClient().GetSdroutingTransportRoutingOspfFeatures(**{'transportId': transportId})

@register('GetSdroutingTransportRoutingOspfFeature')
def GetSdroutingTransportRoutingOspfFeature(ospfId: str, transportId: str):
    return CatalystClient().GetSdroutingTransportRoutingOspfFeature(**{'ospfId': ospfId, 'transportId': transportId})

@register('GetSdroutingTransportRoutingOspfv3Ipv4Features')
def GetSdroutingTransportRoutingOspfv3Ipv4Features(transportId: str):
    return CatalystClient().GetSdroutingTransportRoutingOspfv3Ipv4Features(**{'transportId': transportId})

@register('GetSdroutingTransportRoutingOspfv3Ipv4Feature')
def GetSdroutingTransportRoutingOspfv3Ipv4Feature(ospfv3Id: str, transportId: str):
    return CatalystClient().GetSdroutingTransportRoutingOspfv3Ipv4Feature(**{'ospfv3Id': ospfv3Id, 'transportId': transportId})

@register('GetSdroutingTransportRoutingOspfv3Ipv6Features')
def GetSdroutingTransportRoutingOspfv3Ipv6Features(transportId: str):
    return CatalystClient().GetSdroutingTransportRoutingOspfv3Ipv6Features(**{'transportId': transportId})

@register('GetSdroutingTransportRoutingOspfv3Ipv6Feature')
def GetSdroutingTransportRoutingOspfv3Ipv6Feature(ospfv3Id: str, transportId: str):
    return CatalystClient().GetSdroutingTransportRoutingOspfv3Ipv6Feature(**{'ospfv3Id': ospfv3Id, 'transportId': transportId})

@register('GetTrackerProfileParcelForTransport_1')
def GetTrackerProfileParcelForTransport_1(transportId: str):
    return CatalystClient().GetTrackerProfileParcelForTransport_1(**{'transportId': transportId})

@register('GetTrackerProfileParcelByParcelIdForTransport_1')
def GetTrackerProfileParcelByParcelIdForTransport_1(trackerId: str, transportId: str):
    return CatalystClient().GetTrackerProfileParcelByParcelIdForTransport_1(**{'trackerId': trackerId, 'transportId': transportId})

@register('GetTrackerGroupProfileParcelForTransport_1')
def GetTrackerGroupProfileParcelForTransport_1(transportId: str):
    return CatalystClient().GetTrackerGroupProfileParcelForTransport_1(**{'transportId': transportId})

@register('GetTrackerGroupProfileParcelByParcelIdForTransport_1')
def GetTrackerGroupProfileParcelByParcelIdForTransport_1(trackergroupId: str, transportId: str):
    return CatalystClient().GetTrackerGroupProfileParcelByParcelIdForTransport_1(**{'trackergroupId': trackergroupId, 'transportId': transportId})

@register('GetSdroutingTransportVRFFeatures')
def GetSdroutingTransportVRFFeatures(transportId: str):
    return CatalystClient().GetSdroutingTransportVRFFeatures(**{'transportId': transportId})

@register('GetSdroutingTransportVrfBgpFeatures')
def GetSdroutingTransportVrfBgpFeatures(transportId: str):
    return CatalystClient().GetSdroutingTransportVrfBgpFeatures(**{'transportId': transportId})

@register('GetSdroutingTransportVrfBgpFeature')
def GetSdroutingTransportVrfBgpFeature(bgpId: str, transportId: str):
    return CatalystClient().GetSdroutingTransportVrfBgpFeature(**{'bgpId': bgpId, 'transportId': transportId})

@register('GetSdroutingTransportVRFFeature')
def GetSdroutingTransportVRFFeature(transportId: str, vrfId: str):
    return CatalystClient().GetSdroutingTransportVRFFeature(**{'transportId': transportId, 'vrfId': vrfId})

@register('GetSdroutingTransportVrfInterfaceEthernetParcelsForTransport')
def GetSdroutingTransportVrfInterfaceEthernetParcelsForTransport(transportId: str, vrfId: str):
    return CatalystClient().GetSdroutingTransportVrfInterfaceEthernetParcelsForTransport(**{'transportId': transportId, 'vrfId': vrfId})

@register('GetSdroutingTransportVrfInterfaceEthernetParcelByParcelIdForTransport')
def GetSdroutingTransportVrfInterfaceEthernetParcelByParcelIdForTransport(ethernetId: str, transportId: str, vrfId: str):
    return CatalystClient().GetSdroutingTransportVrfInterfaceEthernetParcelByParcelIdForTransport(**{'ethernetId': ethernetId, 'transportId': transportId, 'vrfId': vrfId})

@register('GetSdroutingTransportVrfInterfaceIpsecFeaturesForTransport')
def GetSdroutingTransportVrfInterfaceIpsecFeaturesForTransport(transportId: str, vrfId: str):
    return CatalystClient().GetSdroutingTransportVrfInterfaceIpsecFeaturesForTransport(**{'transportId': transportId, 'vrfId': vrfId})

@register('GetSdroutingTransportVrfInterfaceIpsecFeatureByFeatureIdForTransport')
def GetSdroutingTransportVrfInterfaceIpsecFeatureByFeatureIdForTransport(ipsecId: str, transportId: str, vrfId: str):
    return CatalystClient().GetSdroutingTransportVrfInterfaceIpsecFeatureByFeatureIdForTransport(**{'ipsecId': ipsecId, 'transportId': transportId, 'vrfId': vrfId})

@register('GetTransportVrfAssociatedRoutingBgpFeatures_1')
def GetTransportVrfAssociatedRoutingBgpFeatures_1(transportId: str, vrfId: str):
    return CatalystClient().GetTransportVrfAssociatedRoutingBgpFeatures_1(**{'transportId': transportId, 'vrfId': vrfId})

@register('GetTransportVrfAssociatedRoutingBgpById')
def GetTransportVrfAssociatedRoutingBgpById(bgpId: str, transportId: str, vrfId: str):
    return CatalystClient().GetTransportVrfAssociatedRoutingBgpById(**{'bgpId': bgpId, 'transportId': transportId, 'vrfId': vrfId})

@register('GetTransportVrfAssociatedRoutingOspfFeatures_1')
def GetTransportVrfAssociatedRoutingOspfFeatures_1(transportId: str, vrfId: str):
    return CatalystClient().GetTransportVrfAssociatedRoutingOspfFeatures_1(**{'transportId': transportId, 'vrfId': vrfId})

@register('GetVrfAssociatedRoutingOspfById')
def GetVrfAssociatedRoutingOspfById(ospfId: str, transportId: str, vrfId: str):
    return CatalystClient().GetVrfAssociatedRoutingOspfById(**{'ospfId': ospfId, 'transportId': transportId, 'vrfId': vrfId})

@register('GetTransportVrfAssociatedRoutingOspfv3Ipv4Features_1')
def GetTransportVrfAssociatedRoutingOspfv3Ipv4Features_1(transportId: str, vrfId: str):
    return CatalystClient().GetTransportVrfAssociatedRoutingOspfv3Ipv4Features_1(**{'transportId': transportId, 'vrfId': vrfId})

@register('GetVrfAssociatedRoutingOspfv3Ipv4FeatureById_1')
def GetVrfAssociatedRoutingOspfv3Ipv4FeatureById_1(ospfv3Id: str, transportId: str, vrfId: str):
    return CatalystClient().GetVrfAssociatedRoutingOspfv3Ipv4FeatureById_1(**{'ospfv3Id': ospfv3Id, 'transportId': transportId, 'vrfId': vrfId})

@register('GetTransportVrfAssociatedRoutingOspfv3Ipv6Features_1')
def GetTransportVrfAssociatedRoutingOspfv3Ipv6Features_1(transportId: str, vrfId: str):
    return CatalystClient().GetTransportVrfAssociatedRoutingOspfv3Ipv6Features_1(**{'transportId': transportId, 'vrfId': vrfId})

@register('GetVrfAssociatedRoutingOspfv3Ipv6FeatureById_1')
def GetVrfAssociatedRoutingOspfv3Ipv6FeatureById_1(ospfv3Id: str, transportId: str, vrfId: str):
    return CatalystClient().GetVrfAssociatedRoutingOspfv3Ipv6FeatureById_1(**{'ospfv3Id': ospfv3Id, 'transportId': transportId, 'vrfId': vrfId})

@register('GetSdwanFeatureProfileBySdwanFamily')
def GetSdwanFeatureProfileBySdwanFamily(**kwargs):
    return CatalystClient().GetSdwanFeatureProfileBySdwanFamily(**{**kwargs})

@register('GetCloudProbeProfileParcelByParcelIdForapplication-priority')
def GetCloudProbeProfileParcelByParcelIdForapplication_priority(applicationPriorityId: str, cloudProbeId: str):
    return CatalystClient().GetCloudProbeProfileParcelByParcelIdForapplication_priority(**{'applicationPriorityId': applicationPriorityId, 'cloudProbeId': cloudProbeId})

@register('getPolicyApplicationProfileParcel')
def getPolicyApplicationProfileParcel(applicationPriorityId: str, qosPolicyId: str):
    return CatalystClient().getPolicyApplicationProfileParcel(**{'applicationPriorityId': applicationPriorityId, 'qosPolicyId': qosPolicyId})

@register('GetTrafficPolicyProfileParcelByParcelIdForapplication-priority')
def GetTrafficPolicyProfileParcelByParcelIdForapplication_priority(applicationPriorityId: str, trafficPolicyId: str):
    return CatalystClient().GetTrafficPolicyProfileParcelByParcelIdForapplication_priority(**{'applicationPriorityId': applicationPriorityId, 'trafficPolicyId': trafficPolicyId})

@register('GetSdwanFeatureProfilesByFamilyAndType_1')
def GetSdwanFeatureProfilesByFamilyAndType_1(**kwargs):
    return CatalystClient().GetSdwanFeatureProfilesByFamilyAndType_1(**{**kwargs})

@register('GetSdwanCliConfigFeatureSchemaBySchemaType')
def GetSdwanCliConfigFeatureSchemaBySchemaType(schemaType: str):
    return CatalystClient().GetSdwanCliConfigFeatureSchemaBySchemaType(**{'schemaType': schemaType})

@register('GetSdwanFeatureProfilesByFamilyAndType')
def GetSdwanFeatureProfilesByFamilyAndType(**kwargs):
    return CatalystClient().GetSdwanFeatureProfilesByFamilyAndType(**{**kwargs})

@register('GetSdwanFeatureProfileByProfileId')
def GetSdwanFeatureProfileByProfileId(cliId: str):
    return CatalystClient().GetSdwanFeatureProfileByProfileId(**{'cliId': cliId})

@register('GetConfigProfileParcelForCLI')
def GetConfigProfileParcelForCLI(cliId: str):
    return CatalystClient().GetConfigProfileParcelForCLI(**{'cliId': cliId})

@register('GetConfigProfileParcelByParcelIdForCLI')
def GetConfigProfileParcelByParcelIdForCLI(cliId: str, configId: str):
    return CatalystClient().GetConfigProfileParcelByParcelIdForCLI(**{'cliId': cliId, 'configId': configId})

@register('GetSdwanDnsSecurityFeatureProfiles')
def GetSdwanDnsSecurityFeatureProfiles(**kwargs):
    return CatalystClient().GetSdwanDnsSecurityFeatureProfiles(**{**kwargs})

@register('GetSdwanDnsSecurityFeatureProfileByProfileId')
def GetSdwanDnsSecurityFeatureProfileByProfileId(dnsSecurityId: str, **kwargs):
    return CatalystClient().GetSdwanDnsSecurityFeatureProfileByProfileId(**{'dnsSecurityId': dnsSecurityId, **kwargs})

@register('GetSigSecurityProfileParcel')
def GetSigSecurityProfileParcel(dnsSecurityId: str):
    return CatalystClient().GetSigSecurityProfileParcel(**{'dnsSecurityId': dnsSecurityId})

@register('GetSigSecurityProfileParcelByParcelId')
def GetSigSecurityProfileParcelByParcelId(dnsSecurityId: str, dnsSecurityProfileParcelId: str):
    return CatalystClient().GetSigSecurityProfileParcelByParcelId(**{'dnsSecurityId': dnsSecurityId, 'dnsSecurityProfileParcelId': dnsSecurityProfileParcelId})

@register('GetSdwanSecurityFeature_1')
def GetSdwanSecurityFeature_1(securityId: str):
    return CatalystClient().GetSdwanSecurityFeature_1(**{'securityId': securityId})

@register('GetSdwanSecurityFeatureByFeatureId_1')
def GetSdwanSecurityFeatureByFeatureId_1(securityId: str, securityProfileParcelId: str):
    return CatalystClient().GetSdwanSecurityFeatureByFeatureId_1(**{'securityId': securityId, 'securityProfileParcelId': securityProfileParcelId})

@register('GetSdwanNgfirewallFeature')
def GetSdwanNgfirewallFeature(securityId: str):
    return CatalystClient().GetSdwanNgfirewallFeature(**{'securityId': securityId})

@register('GetSdwanNgfirewallFeatureByFeatureId')
def GetSdwanNgfirewallFeatureByFeatureId(securityId: str, securityProfileParcelId: str):
    return CatalystClient().GetSdwanNgfirewallFeatureByFeatureId(**{'securityId': securityId, 'securityProfileParcelId': securityProfileParcelId})

@register('GetSdwanOtherFeatureProfiles')
def GetSdwanOtherFeatureProfiles(**kwargs):
    return CatalystClient().GetSdwanOtherFeatureProfiles(**{**kwargs})

@register('GetSdwanOtherThousandeyesParcelSchemaBySchemaType')
def GetSdwanOtherThousandeyesParcelSchemaBySchemaType(schemaType: str):
    return CatalystClient().GetSdwanOtherThousandeyesParcelSchemaBySchemaType(**{'schemaType': schemaType})

@register('GetSdwanOtherFeatureProfileByProfileId')
def GetSdwanOtherFeatureProfileByProfileId(otherId: str):
    return CatalystClient().GetSdwanOtherFeatureProfileByProfileId(**{'otherId': otherId})

@register('GetThousandeyesProfileParcelForOther')
def GetThousandeyesProfileParcelForOther(otherId: str):
    return CatalystClient().GetThousandeyesProfileParcelForOther(**{'otherId': otherId})

@register('GetThousandeyesProfileParcelByParcelIdForOther')
def GetThousandeyesProfileParcelByParcelIdForOther(otherId: str, thousandeyesId: str):
    return CatalystClient().GetThousandeyesProfileParcelByParcelIdForOther(**{'otherId': otherId, 'thousandeyesId': thousandeyesId})

@register('GetUcseProfileFeatureForOther')
def GetUcseProfileFeatureForOther(otherId: str):
    return CatalystClient().GetUcseProfileFeatureForOther(**{'otherId': otherId})

@register('GetUcseProfileFeatureByIdFFeatureForOther')
def GetUcseProfileFeatureByIdFFeatureForOther(otherId: str, ucseId: str):
    return CatalystClient().GetUcseProfileFeatureByIdFFeatureForOther(**{'otherId': otherId, 'ucseId': ucseId})

@register('GetSdwanSecurityFeature')
def GetSdwanSecurityFeature(policyObjectId: str, securityProfileParcelType: str, **kwargs):
    return CatalystClient().GetSdwanSecurityFeature(**{'policyObjectId': policyObjectId, 'securityProfileParcelType': securityProfileParcelType, **kwargs})

@register('GetSdwanSecurityFeatureByFeatureId')
def GetSdwanSecurityFeatureByFeatureId(policyObjectId: str, securityProfileParcelId: str, securityProfileParcelType: str, **kwargs):
    return CatalystClient().GetSdwanSecurityFeatureByFeatureId(**{'policyObjectId': policyObjectId, 'securityProfileParcelId': securityProfileParcelId, 'securityProfileParcelType': securityProfileParcelType, **kwargs})

@register('GetDataPrefixProfileParcelForPolicyObject')
def GetDataPrefixProfileParcelForPolicyObject(policyObjectId: str, policyObjectListType: str, **kwargs):
    return CatalystClient().GetDataPrefixProfileParcelForPolicyObject(**{'policyObjectId': policyObjectId, 'policyObjectListType': policyObjectListType, **kwargs})

@register('GetDataPrefixProfileParcelByParcelIdForPolicyObject')
def GetDataPrefixProfileParcelByParcelIdForPolicyObject(listObjectId: str, policyObjectId: str, policyObjectListType: str, **kwargs):
    return CatalystClient().GetDataPrefixProfileParcelByParcelIdForPolicyObject(**{'listObjectId': listObjectId, 'policyObjectId': policyObjectId, 'policyObjectListType': policyObjectListType, **kwargs})

@register('GetSdwanPolicyObjectDataPrefixParcelSchemaBySchemaType')
def GetSdwanPolicyObjectDataPrefixParcelSchemaBySchemaType(policyObjectListType: str, schemaType: str):
    return CatalystClient().GetSdwanPolicyObjectDataPrefixParcelSchemaBySchemaType(**{'policyObjectListType': policyObjectListType, 'schemaType': schemaType})

@register('GetSdwanServiceFeatureProfiles')
def GetSdwanServiceFeatureProfiles(**kwargs):
    return CatalystClient().GetSdwanServiceFeatureProfiles(**{**kwargs})

@register('GetSdwanServiceDhcpServerParcelSchemaBySchemaType')
def GetSdwanServiceDhcpServerParcelSchemaBySchemaType(schemaType: str):
    return CatalystClient().GetSdwanServiceDhcpServerParcelSchemaBySchemaType(**{'schemaType': schemaType})

@register('GetSdwanServiceLanVpnInterfaceEthernetParcelSchemaBySchema')
def GetSdwanServiceLanVpnInterfaceEthernetParcelSchemaBySchema(schemaType: str):
    return CatalystClient().GetSdwanServiceLanVpnInterfaceEthernetParcelSchemaBySchema(**{'schemaType': schemaType})

@register('GetCedgeServiceLanVpnInterfaceGreSchemaBySchema')
def GetCedgeServiceLanVpnInterfaceGreSchemaBySchema(schemaType: str):
    return CatalystClient().GetCedgeServiceLanVpnInterfaceGreSchemaBySchema(**{'schemaType': schemaType})

@register('getSdwanProfileParcelSchema')
def getSdwanProfileParcelSchema(schemaType: str):
    return CatalystClient().getSdwanProfileParcelSchema(**{'schemaType': schemaType})

@register('GetCedgeServiceLanVpnInterfaceSviParcelSchemaBySchema')
def GetCedgeServiceLanVpnInterfaceSviParcelSchemaBySchema(schemaType: str):
    return CatalystClient().GetCedgeServiceLanVpnInterfaceSviParcelSchemaBySchema(**{'schemaType': schemaType})

@register('GetSdwanServiceLanVpnParcelSchemaBySchemaType')
def GetSdwanServiceLanVpnParcelSchemaBySchemaType(schemaType: str):
    return CatalystClient().GetSdwanServiceLanVpnParcelSchemaBySchemaType(**{'schemaType': schemaType})

@register('GetSdwanServiceRoutingBgpParcelSchemaBySchemaType')
def GetSdwanServiceRoutingBgpParcelSchemaBySchemaType(schemaType: str):
    return CatalystClient().GetSdwanServiceRoutingBgpParcelSchemaBySchemaType(**{'schemaType': schemaType})

@register('GetSdwanServiceRoutingMulticastParcelSchemaBySchemaType')
def GetSdwanServiceRoutingMulticastParcelSchemaBySchemaType(schemaType: str):
    return CatalystClient().GetSdwanServiceRoutingMulticastParcelSchemaBySchemaType(**{'schemaType': schemaType})

@register('GetCedgeServiceSwitchportParcelSchemaBySchemaType')
def GetCedgeServiceSwitchportParcelSchemaBySchemaType(schemaType: str):
    return CatalystClient().GetCedgeServiceSwitchportParcelSchemaBySchemaType(**{'schemaType': schemaType})

@register('GetSdwanServiceTrackerParcelSchemaBySchemaType')
def GetSdwanServiceTrackerParcelSchemaBySchemaType(schemaType: str):
    return CatalystClient().GetSdwanServiceTrackerParcelSchemaBySchemaType(**{'schemaType': schemaType})

@register('GetCedgeServiceTrackerGroupParcelSchemaBySchemaType')
def GetCedgeServiceTrackerGroupParcelSchemaBySchemaType(schemaType: str):
    return CatalystClient().GetCedgeServiceTrackerGroupParcelSchemaBySchemaType(**{'schemaType': schemaType})

@register('GetSdwanServiceWirelesslanParcelSchemaBySchemaType')
def GetSdwanServiceWirelesslanParcelSchemaBySchemaType(schemaType: str):
    return CatalystClient().GetSdwanServiceWirelesslanParcelSchemaBySchemaType(**{'schemaType': schemaType})

@register('GetSdwanServiceFeatureProfileByProfileId')
def GetSdwanServiceFeatureProfileByProfileId(serviceId: str, **kwargs):
    return CatalystClient().GetSdwanServiceFeatureProfileByProfileId(**{'serviceId': serviceId, **kwargs})

@register('GetAppqoeProfileParcelForService')
def GetAppqoeProfileParcelForService(serviceId: str):
    return CatalystClient().GetAppqoeProfileParcelForService(**{'serviceId': serviceId})

@register('GetAppqoeProfileParcelByParcelIdForService')
def GetAppqoeProfileParcelByParcelIdForService(appqoeId: str, serviceId: str):
    return CatalystClient().GetAppqoeProfileParcelByParcelIdForService(**{'appqoeId': appqoeId, 'serviceId': serviceId})

@register('GetDhcpServerProfileParcelForService')
def GetDhcpServerProfileParcelForService(serviceId: str):
    return CatalystClient().GetDhcpServerProfileParcelForService(**{'serviceId': serviceId})

@register('GetDhcpServerProfileParcelByParcelIdForService')
def GetDhcpServerProfileParcelByParcelIdForService(dhcpServerId: str, serviceId: str):
    return CatalystClient().GetDhcpServerProfileParcelByParcelIdForService(**{'dhcpServerId': dhcpServerId, 'serviceId': serviceId})

@register('GetLanVpnProfileParcelForService')
def GetLanVpnProfileParcelForService(serviceId: str):
    return CatalystClient().GetLanVpnProfileParcelForService(**{'serviceId': serviceId})

@register('GetLanVpnProfileParcelByParcelIdForService')
def GetLanVpnProfileParcelByParcelIdForService(serviceId: str, vpnId: str):
    return CatalystClient().GetLanVpnProfileParcelByParcelIdForService(**{'serviceId': serviceId, 'vpnId': vpnId})

@register('GetInterfaceEthernetParcelsForServiceLanVpn')
def GetInterfaceEthernetParcelsForServiceLanVpn(serviceId: str, vpnId: str):
    return CatalystClient().GetInterfaceEthernetParcelsForServiceLanVpn(**{'serviceId': serviceId, 'vpnId': vpnId})

@register('GetLanVpnInterfaceEthernetParcelByParcelIdForService')
def GetLanVpnInterfaceEthernetParcelByParcelIdForService(ethernetId: str, serviceId: str, vpnId: str):
    return CatalystClient().GetLanVpnInterfaceEthernetParcelByParcelIdForService(**{'ethernetId': ethernetId, 'serviceId': serviceId, 'vpnId': vpnId})

@register('GetLanVpnInterfaceEthernetAssociatedDhcpServerParcelsForTransport')
def GetLanVpnInterfaceEthernetAssociatedDhcpServerParcelsForTransport(ethernetId: str, serviceId: str, vpnId: str):
    return CatalystClient().GetLanVpnInterfaceEthernetAssociatedDhcpServerParcelsForTransport(**{'ethernetId': ethernetId, 'serviceId': serviceId, 'vpnId': vpnId})

@register('GetLanVpnInterfaceEthernetAssociatedDhcpServerParcelByParcelIdForTransport')
def GetLanVpnInterfaceEthernetAssociatedDhcpServerParcelByParcelIdForTransport(dhcpServerId: str, ethernetId: str, serviceId: str, vpnId: str):
    return CatalystClient().GetLanVpnInterfaceEthernetAssociatedDhcpServerParcelByParcelIdForTransport(**{'dhcpServerId': dhcpServerId, 'ethernetId': ethernetId, 'serviceId': serviceId, 'vpnId': vpnId})

@register('GetLanVpnInterfaceEthernetAssociatedTrackerParcelsForTransport')
def GetLanVpnInterfaceEthernetAssociatedTrackerParcelsForTransport(ethernetId: str, serviceId: str, vpnId: str):
    return CatalystClient().GetLanVpnInterfaceEthernetAssociatedTrackerParcelsForTransport(**{'ethernetId': ethernetId, 'serviceId': serviceId, 'vpnId': vpnId})

@register('GetLanVpnInterfaceEthernetAssociatedTrackerParcelByParcelIdForTransport')
def GetLanVpnInterfaceEthernetAssociatedTrackerParcelByParcelIdForTransport(ethernetId: str, serviceId: str, trackerId: str, vpnId: str):
    return CatalystClient().GetLanVpnInterfaceEthernetAssociatedTrackerParcelByParcelIdForTransport(**{'ethernetId': ethernetId, 'serviceId': serviceId, 'trackerId': trackerId, 'vpnId': vpnId})

@register('GetLanVpnInterfaceEthernetAssociatedTrackerGroupParcelsForTransport')
def GetLanVpnInterfaceEthernetAssociatedTrackerGroupParcelsForTransport(ethernetId: str, serviceId: str, vpnId: str):
    return CatalystClient().GetLanVpnInterfaceEthernetAssociatedTrackerGroupParcelsForTransport(**{'ethernetId': ethernetId, 'serviceId': serviceId, 'vpnId': vpnId})

@register('GetLanVpnInterfaceEthernetAssociatedTrackerGroupParcelByParcelIdForTransport')
def GetLanVpnInterfaceEthernetAssociatedTrackerGroupParcelByParcelIdForTransport(ethernetId: str, serviceId: str, trackergroupId: str, vpnId: str):
    return CatalystClient().GetLanVpnInterfaceEthernetAssociatedTrackerGroupParcelByParcelIdForTransport(**{'ethernetId': ethernetId, 'serviceId': serviceId, 'trackergroupId': trackergroupId, 'vpnId': vpnId})

@register('GetInterfaceGresForServiceLanVpn')
def GetInterfaceGresForServiceLanVpn(serviceId: str, vpnId: str):
    return CatalystClient().GetInterfaceGresForServiceLanVpn(**{'serviceId': serviceId, 'vpnId': vpnId})

@register('GetLanVpnInterfaceGreByIdForService')
def GetLanVpnInterfaceGreByIdForService(greId: str, serviceId: str, vpnId: str):
    return CatalystClient().GetLanVpnInterfaceGreByIdForService(**{'greId': greId, 'serviceId': serviceId, 'vpnId': vpnId})

@register('getListOfProfileParcels')
def getListOfProfileParcels(serviceId: str, vpnId: str):
    return CatalystClient().getListOfProfileParcels(**{'serviceId': serviceId, 'vpnId': vpnId})

@register('getProfileParcelByParcelId')
def getProfileParcelByParcelId(ipsecId: str, serviceId: str, vpnId: str):
    return CatalystClient().getProfileParcelByParcelId(**{'ipsecId': ipsecId, 'serviceId': serviceId, 'vpnId': vpnId})

@register('GetLanVpnInterfaceIpsecAssociatedDhcpServerParcelsForTransport')
def GetLanVpnInterfaceIpsecAssociatedDhcpServerParcelsForTransport(ipsecId: str, serviceId: str, vpnId: str):
    return CatalystClient().GetLanVpnInterfaceIpsecAssociatedDhcpServerParcelsForTransport(**{'ipsecId': ipsecId, 'serviceId': serviceId, 'vpnId': vpnId})

@register('GetLanVpnInterfaceIpsecAssociatedDhcpServerParcelByParcelIdForTransport')
def GetLanVpnInterfaceIpsecAssociatedDhcpServerParcelByParcelIdForTransport(dhcpServerId: str, ipsecId: str, serviceId: str, vpnId: str):
    return CatalystClient().GetLanVpnInterfaceIpsecAssociatedDhcpServerParcelByParcelIdForTransport(**{'dhcpServerId': dhcpServerId, 'ipsecId': ipsecId, 'serviceId': serviceId, 'vpnId': vpnId})

@register('GetInterfaceSviParcelsForServiceLanVpn')
def GetInterfaceSviParcelsForServiceLanVpn(serviceId: str, vpnId: str):
    return CatalystClient().GetInterfaceSviParcelsForServiceLanVpn(**{'serviceId': serviceId, 'vpnId': vpnId})

@register('GetLanVpnInterfaceSviParcelByParcelIdForService')
def GetLanVpnInterfaceSviParcelByParcelIdForService(serviceId: str, sviId: str, vpnId: str):
    return CatalystClient().GetLanVpnInterfaceSviParcelByParcelIdForService(**{'serviceId': serviceId, 'sviId': sviId, 'vpnId': vpnId})

@register('GetLanVpnInterfaceSviAssociatedDhcpServerParcelsForTransport')
def GetLanVpnInterfaceSviAssociatedDhcpServerParcelsForTransport(serviceId: str, sviId: str, vpnId: str):
    return CatalystClient().GetLanVpnInterfaceSviAssociatedDhcpServerParcelsForTransport(**{'serviceId': serviceId, 'sviId': sviId, 'vpnId': vpnId})

@register('GetLanVpnInterfaceSviAssociatedDhcpServerParcelByParcelIdForTransport')
def GetLanVpnInterfaceSviAssociatedDhcpServerParcelByParcelIdForTransport(dhcpServerId: str, serviceId: str, sviId: str, vpnId: str):
    return CatalystClient().GetLanVpnInterfaceSviAssociatedDhcpServerParcelByParcelIdForTransport(**{'dhcpServerId': dhcpServerId, 'serviceId': serviceId, 'sviId': sviId, 'vpnId': vpnId})

@register('GetLanVpnAssociatedRoutingBgpParcelsForService')
def GetLanVpnAssociatedRoutingBgpParcelsForService(serviceId: str, vpnId: str):
    return CatalystClient().GetLanVpnAssociatedRoutingBgpParcelsForService(**{'serviceId': serviceId, 'vpnId': vpnId})

@register('GetLanVpnAssociatedRoutingBgpParcelByParcelIdForService')
def GetLanVpnAssociatedRoutingBgpParcelByParcelIdForService(bgpId: str, serviceId: str, vpnId: str):
    return CatalystClient().GetLanVpnAssociatedRoutingBgpParcelByParcelIdForService(**{'bgpId': bgpId, 'serviceId': serviceId, 'vpnId': vpnId})

@register('GetLanVpnAssociatedRoutingEigrpParcelsForService')
def GetLanVpnAssociatedRoutingEigrpParcelsForService(serviceId: str, vpnId: str):
    return CatalystClient().GetLanVpnAssociatedRoutingEigrpParcelsForService(**{'serviceId': serviceId, 'vpnId': vpnId})

@register('GetLanVpnAssociatedRoutingEigrpParcelByParcelIdForService')
def GetLanVpnAssociatedRoutingEigrpParcelByParcelIdForService(eigrpId: str, serviceId: str, vpnId: str):
    return CatalystClient().GetLanVpnAssociatedRoutingEigrpParcelByParcelIdForService(**{'eigrpId': eigrpId, 'serviceId': serviceId, 'vpnId': vpnId})

@register('GetLanVpnAssociatedRoutingMulticastParcelsForService')
def GetLanVpnAssociatedRoutingMulticastParcelsForService(serviceId: str, vpnId: str):
    return CatalystClient().GetLanVpnAssociatedRoutingMulticastParcelsForService(**{'serviceId': serviceId, 'vpnId': vpnId})

@register('GetLanVpnAssociatedRoutingMulticastParcelByParcelIdForService')
def GetLanVpnAssociatedRoutingMulticastParcelByParcelIdForService(multicastId: str, serviceId: str, vpnId: str):
    return CatalystClient().GetLanVpnAssociatedRoutingMulticastParcelByParcelIdForService(**{'multicastId': multicastId, 'serviceId': serviceId, 'vpnId': vpnId})

@register('GetLanVpnAssociatedRoutingOspfParcelsForService')
def GetLanVpnAssociatedRoutingOspfParcelsForService(serviceId: str, vpnId: str):
    return CatalystClient().GetLanVpnAssociatedRoutingOspfParcelsForService(**{'serviceId': serviceId, 'vpnId': vpnId})

@register('GetLanVpnAssociatedRoutingOspfParcelByParcelIdForService')
def GetLanVpnAssociatedRoutingOspfParcelByParcelIdForService(ospfId: str, serviceId: str, vpnId: str):
    return CatalystClient().GetLanVpnAssociatedRoutingOspfParcelByParcelIdForService(**{'ospfId': ospfId, 'serviceId': serviceId, 'vpnId': vpnId})

@register('GetLanVpnAssociatedRoutingOspfv3IPv4ParcelsForService')
def GetLanVpnAssociatedRoutingOspfv3IPv4ParcelsForService(serviceId: str, vpnId: str):
    return CatalystClient().GetLanVpnAssociatedRoutingOspfv3IPv4ParcelsForService(**{'serviceId': serviceId, 'vpnId': vpnId})

@register('GetLanVpnAssociatedRoutingOspfv3IPv4ParcelByParcelIdForService')
def GetLanVpnAssociatedRoutingOspfv3IPv4ParcelByParcelIdForService(ospfv3Id: str, serviceId: str, vpnId: str):
    return CatalystClient().GetLanVpnAssociatedRoutingOspfv3IPv4ParcelByParcelIdForService(**{'ospfv3Id': ospfv3Id, 'serviceId': serviceId, 'vpnId': vpnId})

@register('GetLanVpnAssociatedRoutingOspfv3IPv6ParcelsForService')
def GetLanVpnAssociatedRoutingOspfv3IPv6ParcelsForService(serviceId: str, vpnId: str):
    return CatalystClient().GetLanVpnAssociatedRoutingOspfv3IPv6ParcelsForService(**{'serviceId': serviceId, 'vpnId': vpnId})

@register('GetLanVpnAssociatedRoutingOspfv3IPv6ParcelByParcelIdForService')
def GetLanVpnAssociatedRoutingOspfv3IPv6ParcelByParcelIdForService(ospfv3Id: str, serviceId: str, vpnId: str):
    return CatalystClient().GetLanVpnAssociatedRoutingOspfv3IPv6ParcelByParcelIdForService(**{'ospfv3Id': ospfv3Id, 'serviceId': serviceId, 'vpnId': vpnId})

@register('GetRoutingBgpProfileParcelForService')
def GetRoutingBgpProfileParcelForService(serviceId: str):
    return CatalystClient().GetRoutingBgpProfileParcelForService(**{'serviceId': serviceId})

@register('GetRoutingBgpProfileParcelByParcelIdForService')
def GetRoutingBgpProfileParcelByParcelIdForService(bgpId: str, serviceId: str):
    return CatalystClient().GetRoutingBgpProfileParcelByParcelIdForService(**{'bgpId': bgpId, 'serviceId': serviceId})

@register('GetRoutingEigrpProfileParcelForService')
def GetRoutingEigrpProfileParcelForService(serviceId: str):
    return CatalystClient().GetRoutingEigrpProfileParcelForService(**{'serviceId': serviceId})

@register('GetRoutingEigrpProfileParcelByParcelIdForService')
def GetRoutingEigrpProfileParcelByParcelIdForService(eigrpId: str, serviceId: str):
    return CatalystClient().GetRoutingEigrpProfileParcelByParcelIdForService(**{'eigrpId': eigrpId, 'serviceId': serviceId})

@register('GetRoutingMulticastProfileParcelForService')
def GetRoutingMulticastProfileParcelForService(serviceId: str):
    return CatalystClient().GetRoutingMulticastProfileParcelForService(**{'serviceId': serviceId})

@register('GetRoutingMulticastProfileParcelByParcelIdForService')
def GetRoutingMulticastProfileParcelByParcelIdForService(multicastId: str, serviceId: str):
    return CatalystClient().GetRoutingMulticastProfileParcelByParcelIdForService(**{'multicastId': multicastId, 'serviceId': serviceId})

@register('GetRoutingOspfProfileParcelForService')
def GetRoutingOspfProfileParcelForService(serviceId: str):
    return CatalystClient().GetRoutingOspfProfileParcelForService(**{'serviceId': serviceId})

@register('GetRoutingOspfProfileParcelByParcelIdForService')
def GetRoutingOspfProfileParcelByParcelIdForService(ospfId: str, serviceId: str):
    return CatalystClient().GetRoutingOspfProfileParcelByParcelIdForService(**{'ospfId': ospfId, 'serviceId': serviceId})

@register('GetRoutingOspfv3Ipv4AfProfileParcelForService')
def GetRoutingOspfv3Ipv4AfProfileParcelForService(serviceId: str):
    return CatalystClient().GetRoutingOspfv3Ipv4AfProfileParcelForService(**{'serviceId': serviceId})

@register('GetRoutingOspfv3IPv4AfProfileParcelByParcelIdForService')
def GetRoutingOspfv3IPv4AfProfileParcelByParcelIdForService(ospfv3Id: str, serviceId: str):
    return CatalystClient().GetRoutingOspfv3IPv4AfProfileParcelByParcelIdForService(**{'ospfv3Id': ospfv3Id, 'serviceId': serviceId})

@register('GetRoutingOspfv3Ipv6AfProfileParcelForService')
def GetRoutingOspfv3Ipv6AfProfileParcelForService(serviceId: str):
    return CatalystClient().GetRoutingOspfv3Ipv6AfProfileParcelForService(**{'serviceId': serviceId})

@register('GetRoutingOspfv3IPv6AfProfileParcelByParcelIdForService')
def GetRoutingOspfv3IPv6AfProfileParcelByParcelIdForService(ospfv3Id: str, serviceId: str):
    return CatalystClient().GetRoutingOspfv3IPv6AfProfileParcelByParcelIdForService(**{'ospfv3Id': ospfv3Id, 'serviceId': serviceId})

@register('GetSwitchportParcelsForService')
def GetSwitchportParcelsForService(serviceId: str):
    return CatalystClient().GetSwitchportParcelsForService(**{'serviceId': serviceId})

@register('GetSwitchportParcelByParcelIdForService')
def GetSwitchportParcelByParcelIdForService(serviceId: str, switchportId: str):
    return CatalystClient().GetSwitchportParcelByParcelIdForService(**{'serviceId': serviceId, 'switchportId': switchportId})

@register('GetTrackerProfileParcelForService')
def GetTrackerProfileParcelForService(serviceId: str):
    return CatalystClient().GetTrackerProfileParcelForService(**{'serviceId': serviceId})

@register('GetTrackerProfileParcelByParcelIdForService')
def GetTrackerProfileParcelByParcelIdForService(serviceId: str, trackerId: str):
    return CatalystClient().GetTrackerProfileParcelByParcelIdForService(**{'serviceId': serviceId, 'trackerId': trackerId})

@register('GetTrackerGroupProfileParcelForService')
def GetTrackerGroupProfileParcelForService(serviceId: str):
    return CatalystClient().GetTrackerGroupProfileParcelForService(**{'serviceId': serviceId})

@register('GetTrackerGroupProfileParcelByParcelIdForService')
def GetTrackerGroupProfileParcelByParcelIdForService(serviceId: str, trackergroupId: str):
    return CatalystClient().GetTrackerGroupProfileParcelByParcelIdForService(**{'serviceId': serviceId, 'trackergroupId': trackergroupId})

@register('GetWirelesslanProfileParcelForService')
def GetWirelesslanProfileParcelForService(serviceId: str):
    return CatalystClient().GetWirelesslanProfileParcelForService(**{'serviceId': serviceId})

@register('GetWirelesslanProfileParcelByParcelIdForService')
def GetWirelesslanProfileParcelByParcelIdForService(serviceId: str, wirelesslanId: str):
    return CatalystClient().GetWirelesslanProfileParcelByParcelIdForService(**{'serviceId': serviceId, 'wirelesslanId': wirelesslanId})

@register('GetSdwanSigSecurityFeatureProfiles')
def GetSdwanSigSecurityFeatureProfiles(**kwargs):
    return CatalystClient().GetSdwanSigSecurityFeatureProfiles(**{**kwargs})

@register('GetSdwanSigSecurityFeatureProfileByProfileId')
def GetSdwanSigSecurityFeatureProfileByProfileId(sigSecurityId: str, **kwargs):
    return CatalystClient().GetSdwanSigSecurityFeatureProfileByProfileId(**{'sigSecurityId': sigSecurityId, **kwargs})

@register('GetSigSecurityProfileParcel_1')
def GetSigSecurityProfileParcel_1(sigSecurityId: str):
    return CatalystClient().GetSigSecurityProfileParcel_1(**{'sigSecurityId': sigSecurityId})

@register('GetSigSecurityProfileParcelByParcelId_1')
def GetSigSecurityProfileParcelByParcelId_1(sigSecurityId: str, sigSecurityProfileParcelId: str):
    return CatalystClient().GetSigSecurityProfileParcelByParcelId_1(**{'sigSecurityId': sigSecurityId, 'sigSecurityProfileParcelId': sigSecurityProfileParcelId})

@register('GetSdwanSystemFeatureProfiles')
def GetSdwanSystemFeatureProfiles(**kwargs):
    return CatalystClient().GetSdwanSystemFeatureProfiles(**{**kwargs})

@register('GetSdwanSystemAaaParcelSchemaBySchemaType')
def GetSdwanSystemAaaParcelSchemaBySchemaType(schemaType: str):
    return CatalystClient().GetSdwanSystemAaaParcelSchemaBySchemaType(**{'schemaType': schemaType})

@register('GetSdwanSystemBannerParcelSchemaBySchemaType')
def GetSdwanSystemBannerParcelSchemaBySchemaType(schemaType: str):
    return CatalystClient().GetSdwanSystemBannerParcelSchemaBySchemaType(**{'schemaType': schemaType})

@register('GetSdwanSystemBasicFeatureSchemaBySchemaType')
def GetSdwanSystemBasicFeatureSchemaBySchemaType(schemaType: str):
    return CatalystClient().GetSdwanSystemBasicFeatureSchemaBySchemaType(**{'schemaType': schemaType})

@register('GetSdwanSystemBfdParcelSchemaBySchemaType')
def GetSdwanSystemBfdParcelSchemaBySchemaType(schemaType: str):
    return CatalystClient().GetSdwanSystemBfdParcelSchemaBySchemaType(**{'schemaType': schemaType})

@register('GetCedgeSystemGlobalParcelSchemaBySchemaType')
def GetCedgeSystemGlobalParcelSchemaBySchemaType(schemaType: str):
    return CatalystClient().GetCedgeSystemGlobalParcelSchemaBySchemaType(**{'schemaType': schemaType})

@register('GetSdwanSystemLoggingParcelSchemaBySchemaType')
def GetSdwanSystemLoggingParcelSchemaBySchemaType(schemaType: str):
    return CatalystClient().GetSdwanSystemLoggingParcelSchemaBySchemaType(**{'schemaType': schemaType})

@register('GetCedgeSystemMrfParcelSchemaBySchemaType')
def GetCedgeSystemMrfParcelSchemaBySchemaType(schemaType: str):
    return CatalystClient().GetCedgeSystemMrfParcelSchemaBySchemaType(**{'schemaType': schemaType})

@register('GetSdwanSystemNtpParcelSchemaBySchemaType')
def GetSdwanSystemNtpParcelSchemaBySchemaType(schemaType: str):
    return CatalystClient().GetSdwanSystemNtpParcelSchemaBySchemaType(**{'schemaType': schemaType})

@register('GetSdwanSystemOmpParcelSchemaBySchemaType')
def GetSdwanSystemOmpParcelSchemaBySchemaType(schemaType: str):
    return CatalystClient().GetSdwanSystemOmpParcelSchemaBySchemaType(**{'schemaType': schemaType})

@register('GetSdwanSystemSnmpParcelSchemaBySchemaType')
def GetSdwanSystemSnmpParcelSchemaBySchemaType(schemaType: str):
    return CatalystClient().GetSdwanSystemSnmpParcelSchemaBySchemaType(**{'schemaType': schemaType})

@register('GetSdwanSystemFeatureProfileByProfileId')
def GetSdwanSystemFeatureProfileByProfileId(systemId: str):
    return CatalystClient().GetSdwanSystemFeatureProfileByProfileId(**{'systemId': systemId})

@register('GetAaaProfileParcelForSystem')
def GetAaaProfileParcelForSystem(systemId: str):
    return CatalystClient().GetAaaProfileParcelForSystem(**{'systemId': systemId})

@register('GetAaaProfileParcelByParcelIdForSystem')
def GetAaaProfileParcelByParcelIdForSystem(aaaId: str, systemId: str):
    return CatalystClient().GetAaaProfileParcelByParcelIdForSystem(**{'aaaId': aaaId, 'systemId': systemId})

@register('GetBannerProfileParcelForSystem')
def GetBannerProfileParcelForSystem(systemId: str):
    return CatalystClient().GetBannerProfileParcelForSystem(**{'systemId': systemId})

@register('GetBannerProfileParcelByParcelIdForSystem')
def GetBannerProfileParcelByParcelIdForSystem(bannerId: str, systemId: str):
    return CatalystClient().GetBannerProfileParcelByParcelIdForSystem(**{'bannerId': bannerId, 'systemId': systemId})

@register('GetBasicProfileFeatureForSystem')
def GetBasicProfileFeatureForSystem(systemId: str):
    return CatalystClient().GetBasicProfileFeatureForSystem(**{'systemId': systemId})

@register('GetBasicProfileFeatureByFeatureIdForSystem')
def GetBasicProfileFeatureByFeatureIdForSystem(basicId: str, systemId: str):
    return CatalystClient().GetBasicProfileFeatureByFeatureIdForSystem(**{'basicId': basicId, 'systemId': systemId})

@register('GetBfdProfileParcelForSystem')
def GetBfdProfileParcelForSystem(systemId: str):
    return CatalystClient().GetBfdProfileParcelForSystem(**{'systemId': systemId})

@register('GetBfdProfileParcelByParcelIdForSystem')
def GetBfdProfileParcelByParcelIdForSystem(bfdId: str, systemId: str):
    return CatalystClient().GetBfdProfileParcelByParcelIdForSystem(**{'bfdId': bfdId, 'systemId': systemId})

@register('GetGlobalProfileParcelForSystem')
def GetGlobalProfileParcelForSystem(systemId: str):
    return CatalystClient().GetGlobalProfileParcelForSystem(**{'systemId': systemId})

@register('GetGlobalProfileParcelByParcelIdForSystem')
def GetGlobalProfileParcelByParcelIdForSystem(globalId: str, systemId: str):
    return CatalystClient().GetGlobalProfileParcelByParcelIdForSystem(**{'globalId': globalId, 'systemId': systemId})

@register('GetLoggingProfileParcelForSystem')
def GetLoggingProfileParcelForSystem(systemId: str):
    return CatalystClient().GetLoggingProfileParcelForSystem(**{'systemId': systemId})

@register('GetLoggingProfileParcelByParcelIdForSystem')
def GetLoggingProfileParcelByParcelIdForSystem(loggingId: str, systemId: str):
    return CatalystClient().GetLoggingProfileParcelByParcelIdForSystem(**{'loggingId': loggingId, 'systemId': systemId})

@register('GetMrfProfileParcelForSystem')
def GetMrfProfileParcelForSystem(systemId: str):
    return CatalystClient().GetMrfProfileParcelForSystem(**{'systemId': systemId})

@register('GetMrfProfileParcelByParcelIdForSystem')
def GetMrfProfileParcelByParcelIdForSystem(mrfId: str, systemId: str):
    return CatalystClient().GetMrfProfileParcelByParcelIdForSystem(**{'mrfId': mrfId, 'systemId': systemId})

@register('GetNtpProfileParcelForSystem')
def GetNtpProfileParcelForSystem(systemId: str):
    return CatalystClient().GetNtpProfileParcelForSystem(**{'systemId': systemId})

@register('GetNtpProfileParcelByParcelIdForSystem')
def GetNtpProfileParcelByParcelIdForSystem(ntpId: str, systemId: str):
    return CatalystClient().GetNtpProfileParcelByParcelIdForSystem(**{'ntpId': ntpId, 'systemId': systemId})

@register('GetOmpProfileParcelForSystem')
def GetOmpProfileParcelForSystem(systemId: str):
    return CatalystClient().GetOmpProfileParcelForSystem(**{'systemId': systemId})

@register('GetOmpProfileParcelByParcelIdForSystem')
def GetOmpProfileParcelByParcelIdForSystem(ompId: str, systemId: str):
    return CatalystClient().GetOmpProfileParcelByParcelIdForSystem(**{'ompId': ompId, 'systemId': systemId})

@register('GetSecurityForSystem')
def GetSecurityForSystem(systemId: str):
    return CatalystClient().GetSecurityForSystem(**{'systemId': systemId})

@register('GetSecurityBySecurityIdForSystem')
def GetSecurityBySecurityIdForSystem(securityId: str, systemId: str):
    return CatalystClient().GetSecurityBySecurityIdForSystem(**{'securityId': securityId, 'systemId': systemId})

@register('GetSnmpProfileParcelForSystem')
def GetSnmpProfileParcelForSystem(systemId: str):
    return CatalystClient().GetSnmpProfileParcelForSystem(**{'systemId': systemId})

@register('GetSnmpProfileParcelByParcelIdForSystem')
def GetSnmpProfileParcelByParcelIdForSystem(snmpId: str, systemId: str):
    return CatalystClient().GetSnmpProfileParcelByParcelIdForSystem(**{'snmpId': snmpId, 'systemId': systemId})

@register('GetSdwanTransportFeatureProfiles')
def GetSdwanTransportFeatureProfiles(**kwargs):
    return CatalystClient().GetSdwanTransportFeatureProfiles(**{**kwargs})

@register('GetSdwanTransportCellularControllerParcelSchemaBySchemaType')
def GetSdwanTransportCellularControllerParcelSchemaBySchemaType(schemaType: str):
    return CatalystClient().GetSdwanTransportCellularControllerParcelSchemaBySchemaType(**{'schemaType': schemaType})

@register('GetSdwanTransportCellularProfileParcelSchemaBySchemaType')
def GetSdwanTransportCellularProfileParcelSchemaBySchemaType(schemaType: str):
    return CatalystClient().GetSdwanTransportCellularProfileParcelSchemaBySchemaType(**{'schemaType': schemaType})

@register('GetSdwanTransportIpv6TrackerParcelSchemaBySchemaType')
def GetSdwanTransportIpv6TrackerParcelSchemaBySchemaType(schemaType: str):
    return CatalystClient().GetSdwanTransportIpv6TrackerParcelSchemaBySchemaType(**{'schemaType': schemaType})

@register('GetCedgeTransportIpv6TrackerGroupParcelSchemaBySchemaType')
def GetCedgeTransportIpv6TrackerGroupParcelSchemaBySchemaType(schemaType: str):
    return CatalystClient().GetCedgeTransportIpv6TrackerGroupParcelSchemaBySchemaType(**{'schemaType': schemaType})

@register('GetSdwanTransportManagementVpnInterfaceEthernetParcelSchemaBySchema')
def GetSdwanTransportManagementVpnInterfaceEthernetParcelSchemaBySchema(schemaType: str):
    return CatalystClient().GetSdwanTransportManagementVpnInterfaceEthernetParcelSchemaBySchema(**{'schemaType': schemaType})

@register('GetSdwanTransportManagementVpnParcelSchemaBySchemaType')
def GetSdwanTransportManagementVpnParcelSchemaBySchemaType(schemaType: str):
    return CatalystClient().GetSdwanTransportManagementVpnParcelSchemaBySchemaType(**{'schemaType': schemaType})

@register('GetSdwanTransportRoutingBgpParcelSchemaBySchemaType')
def GetSdwanTransportRoutingBgpParcelSchemaBySchemaType(schemaType: str):
    return CatalystClient().GetSdwanTransportRoutingBgpParcelSchemaBySchemaType(**{'schemaType': schemaType})

@register('GetCedgeTransportT1e1controllerParcelSchemaBySchemaType')
def GetCedgeTransportT1e1controllerParcelSchemaBySchemaType(schemaType: str):
    return CatalystClient().GetCedgeTransportT1e1controllerParcelSchemaBySchemaType(**{'schemaType': schemaType})

@register('GetSdwanTransportTrackerParcelSchemaBySchemaType')
def GetSdwanTransportTrackerParcelSchemaBySchemaType(schemaType: str):
    return CatalystClient().GetSdwanTransportTrackerParcelSchemaBySchemaType(**{'schemaType': schemaType})

@register('GetCedgeTransportTrackerGroupParcelSchemaBySchemaType')
def GetCedgeTransportTrackerGroupParcelSchemaBySchemaType(schemaType: str):
    return CatalystClient().GetCedgeTransportTrackerGroupParcelSchemaBySchemaType(**{'schemaType': schemaType})

@register('GetSdwanTransportWanVpnCellularInterfaceParcelSchemaBySchema')
def GetSdwanTransportWanVpnCellularInterfaceParcelSchemaBySchema(schemaType: str):
    return CatalystClient().GetSdwanTransportWanVpnCellularInterfaceParcelSchemaBySchema(**{'schemaType': schemaType})

@register('GetSdwanTransportWanVpnInterfaceEthernetParcelSchemaBySchema')
def GetSdwanTransportWanVpnInterfaceEthernetParcelSchemaBySchema(schemaType: str):
    return CatalystClient().GetSdwanTransportWanVpnInterfaceEthernetParcelSchemaBySchema(**{'schemaType': schemaType})

@register('GetCedgeTransportWanVpnInterfaceGreParcelSchemaBySchema')
def GetCedgeTransportWanVpnInterfaceGreParcelSchemaBySchema(schemaType: str):
    return CatalystClient().GetCedgeTransportWanVpnInterfaceGreParcelSchemaBySchema(**{'schemaType': schemaType})

@register('getSdwanProfileParcelSchema_1')
def getSdwanProfileParcelSchema_1(schemaType: str):
    return CatalystClient().getSdwanProfileParcelSchema_1(**{'schemaType': schemaType})

@register('GetCedgeTransportWanVpnInterfaceSerialParcelSchemaBySchema')
def GetCedgeTransportWanVpnInterfaceSerialParcelSchemaBySchema(schemaType: str):
    return CatalystClient().GetCedgeTransportWanVpnInterfaceSerialParcelSchemaBySchema(**{'schemaType': schemaType})

@register('GetSdwanTransportWanVpnParcelSchemaBySchemaType')
def GetSdwanTransportWanVpnParcelSchemaBySchemaType(schemaType: str):
    return CatalystClient().GetSdwanTransportWanVpnParcelSchemaBySchemaType(**{'schemaType': schemaType})

@register('GetSdwanTransportFeatureProfileByProfileId')
def GetSdwanTransportFeatureProfileByProfileId(transportId: str):
    return CatalystClient().GetSdwanTransportFeatureProfileByProfileId(**{'transportId': transportId})

@register('GetCellularControllerProfileParcelForTransport')
def GetCellularControllerProfileParcelForTransport(transportId: str):
    return CatalystClient().GetCellularControllerProfileParcelForTransport(**{'transportId': transportId})

@register('GetCellularControllerProfileParcelByParcelIdForTransport')
def GetCellularControllerProfileParcelByParcelIdForTransport(cellularControllerId: str, transportId: str):
    return CatalystClient().GetCellularControllerProfileParcelByParcelIdForTransport(**{'cellularControllerId': cellularControllerId, 'transportId': transportId})

@register('GetCellularControllerAssociatedCellularProfileParcelsForTransport')
def GetCellularControllerAssociatedCellularProfileParcelsForTransport(cellularControllerId: str, transportId: str):
    return CatalystClient().GetCellularControllerAssociatedCellularProfileParcelsForTransport(**{'cellularControllerId': cellularControllerId, 'transportId': transportId})

@register('GetCellularControllerAssociatedCellularProfileParcelByParcelIdForTransport')
def GetCellularControllerAssociatedCellularProfileParcelByParcelIdForTransport(cellularControllerId: str, cellularProfileId: str, transportId: str):
    return CatalystClient().GetCellularControllerAssociatedCellularProfileParcelByParcelIdForTransport(**{'cellularControllerId': cellularControllerId, 'cellularProfileId': cellularProfileId, 'transportId': transportId})

@register('GetCellularControllerAssociatedGpsParcelsForTransport')
def GetCellularControllerAssociatedGpsParcelsForTransport(cellularControllerId: str, transportId: str):
    return CatalystClient().GetCellularControllerAssociatedGpsParcelsForTransport(**{'cellularControllerId': cellularControllerId, 'transportId': transportId})

@register('GetCellularControllerAssociatedGpsParcelByParcelIdForTransport')
def GetCellularControllerAssociatedGpsParcelByParcelIdForTransport(cellularControllerId: str, gpsId: str, transportId: str):
    return CatalystClient().GetCellularControllerAssociatedGpsParcelByParcelIdForTransport(**{'cellularControllerId': cellularControllerId, 'gpsId': gpsId, 'transportId': transportId})

@register('GetCellularProfileProfileParcelForTransport')
def GetCellularProfileProfileParcelForTransport(transportId: str):
    return CatalystClient().GetCellularProfileProfileParcelForTransport(**{'transportId': transportId})

@register('GetCellularProfileProfileParcelByParcelIdForTransport')
def GetCellularProfileProfileParcelByParcelIdForTransport(cellularProfileId: str, transportId: str):
    return CatalystClient().GetCellularProfileProfileParcelByParcelIdForTransport(**{'cellularProfileId': cellularProfileId, 'transportId': transportId})

@register('GetEsimCellularControllerProfileFeatureForTransport')
def GetEsimCellularControllerProfileFeatureForTransport(transportId: str):
    return CatalystClient().GetEsimCellularControllerProfileFeatureForTransport(**{'transportId': transportId})

@register('GetEsimCellularControllerProfileFeatureByFeatureIdForTransport')
def GetEsimCellularControllerProfileFeatureByFeatureIdForTransport(esimCellularControllerId: str, transportId: str):
    return CatalystClient().GetEsimCellularControllerProfileFeatureByFeatureIdForTransport(**{'esimCellularControllerId': esimCellularControllerId, 'transportId': transportId})

@register('GetEsimCellularProfileProfileFeatureForTransport')
def GetEsimCellularProfileProfileFeatureForTransport(transportId: str):
    return CatalystClient().GetEsimCellularProfileProfileFeatureForTransport(**{'transportId': transportId})

@register('GetEsimCellularProfileByFeatureIdForTransport')
def GetEsimCellularProfileByFeatureIdForTransport(esimCellularProfileId: str, transportId: str):
    return CatalystClient().GetEsimCellularProfileByFeatureIdForTransport(**{'esimCellularProfileId': esimCellularProfileId, 'transportId': transportId})

@register('GetGpsProfileParcelForTransport')
def GetGpsProfileParcelForTransport(transportId: str):
    return CatalystClient().GetGpsProfileParcelForTransport(**{'transportId': transportId})

@register('GetGpsProfileParcelByParcelIdForTransport')
def GetGpsProfileParcelByParcelIdForTransport(gpsId: str, transportId: str):
    return CatalystClient().GetGpsProfileParcelByParcelIdForTransport(**{'gpsId': gpsId, 'transportId': transportId})

@register('GetIpv6TrackerProfileParcelForTransport')
def GetIpv6TrackerProfileParcelForTransport(transportId: str):
    return CatalystClient().GetIpv6TrackerProfileParcelForTransport(**{'transportId': transportId})

@register('GetIpv6TrackerProfileParcelByParcelIdForTransport')
def GetIpv6TrackerProfileParcelByParcelIdForTransport(ipv6_trackerId: str, transportId: str):
    return CatalystClient().GetIpv6TrackerProfileParcelByParcelIdForTransport(**{'ipv6-trackerId': ipv6_trackerId, 'transportId': transportId})

@register('GetIpv6TrackerGroupProfileParcelForTransport')
def GetIpv6TrackerGroupProfileParcelForTransport(transportId: str):
    return CatalystClient().GetIpv6TrackerGroupProfileParcelForTransport(**{'transportId': transportId})

@register('GetIpv6TrackerGroupProfileParcelByParcelIdForTransport')
def GetIpv6TrackerGroupProfileParcelByParcelIdForTransport(ipv6_trackergroupId: str, transportId: str):
    return CatalystClient().GetIpv6TrackerGroupProfileParcelByParcelIdForTransport(**{'ipv6-trackergroupId': ipv6_trackergroupId, 'transportId': transportId})

@register('GetManagementVpnProfileParcelForTransport')
def GetManagementVpnProfileParcelForTransport(transportId: str):
    return CatalystClient().GetManagementVpnProfileParcelForTransport(**{'transportId': transportId})

@register('GetManagementVpnProfileParcelByParcelIdForTransport')
def GetManagementVpnProfileParcelByParcelIdForTransport(transportId: str, vpnId: str):
    return CatalystClient().GetManagementVpnProfileParcelByParcelIdForTransport(**{'transportId': transportId, 'vpnId': vpnId})

@register('GetInterfaceEthernetParcelsForTransportManagementVpn')
def GetInterfaceEthernetParcelsForTransportManagementVpn(transportId: str, vpnId: str):
    return CatalystClient().GetInterfaceEthernetParcelsForTransportManagementVpn(**{'transportId': transportId, 'vpnId': vpnId})

@register('GetManagementVpnInterfaceEthernetParcelByParcelIdForTransport')
def GetManagementVpnInterfaceEthernetParcelByParcelIdForTransport(ethernetId: str, transportId: str, vpnId: str):
    return CatalystClient().GetManagementVpnInterfaceEthernetParcelByParcelIdForTransport(**{'ethernetId': ethernetId, 'transportId': transportId, 'vpnId': vpnId})

@register('GetRoutingBgpProfileParcelForTransport')
def GetRoutingBgpProfileParcelForTransport(transportId: str):
    return CatalystClient().GetRoutingBgpProfileParcelForTransport(**{'transportId': transportId})

@register('GetRoutingBgpProfileParcelByParcelIdForTransport')
def GetRoutingBgpProfileParcelByParcelIdForTransport(bgpId: str, transportId: str):
    return CatalystClient().GetRoutingBgpProfileParcelByParcelIdForTransport(**{'bgpId': bgpId, 'transportId': transportId})

@register('GetRoutingOspfProfileParcelForTransport')
def GetRoutingOspfProfileParcelForTransport(transportId: str):
    return CatalystClient().GetRoutingOspfProfileParcelForTransport(**{'transportId': transportId})

@register('GetRoutingOspfProfileParcelByParcelIdForTransport')
def GetRoutingOspfProfileParcelByParcelIdForTransport(ospfId: str, transportId: str):
    return CatalystClient().GetRoutingOspfProfileParcelByParcelIdForTransport(**{'ospfId': ospfId, 'transportId': transportId})

@register('GetRoutingOspfv3Ipv4AfProfileParcelForTransport')
def GetRoutingOspfv3Ipv4AfProfileParcelForTransport(transportId: str):
    return CatalystClient().GetRoutingOspfv3Ipv4AfProfileParcelForTransport(**{'transportId': transportId})

@register('GetRoutingOspfv3Ipv4AfProfileParcelByParcelIdForTransport')
def GetRoutingOspfv3Ipv4AfProfileParcelByParcelIdForTransport(ospfv3Id: str, transportId: str):
    return CatalystClient().GetRoutingOspfv3Ipv4AfProfileParcelByParcelIdForTransport(**{'ospfv3Id': ospfv3Id, 'transportId': transportId})

@register('GetRoutingOspfv3Ipv6AfProfileParcelForTransport')
def GetRoutingOspfv3Ipv6AfProfileParcelForTransport(transportId: str):
    return CatalystClient().GetRoutingOspfv3Ipv6AfProfileParcelForTransport(**{'transportId': transportId})

@register('GetRoutingOspfv3Ipv6AfProfileParcelByParcelIdForTransport')
def GetRoutingOspfv3Ipv6AfProfileParcelByParcelIdForTransport(ospfv3Id: str, transportId: str):
    return CatalystClient().GetRoutingOspfv3Ipv6AfProfileParcelByParcelIdForTransport(**{'ospfv3Id': ospfv3Id, 'transportId': transportId})

@register('GetT1e1controllerProfileParcelForTransport')
def GetT1e1controllerProfileParcelForTransport(transportId: str):
    return CatalystClient().GetT1e1controllerProfileParcelForTransport(**{'transportId': transportId})

@register('GetT1e1controllerProfileParcelByParcelIdForTransport')
def GetT1e1controllerProfileParcelByParcelIdForTransport(t1e1controllerId: str, transportId: str):
    return CatalystClient().GetT1e1controllerProfileParcelByParcelIdForTransport(**{'t1e1controllerId': t1e1controllerId, 'transportId': transportId})

@register('GetTrackerProfileParcelForTransport')
def GetTrackerProfileParcelForTransport(transportId: str):
    return CatalystClient().GetTrackerProfileParcelForTransport(**{'transportId': transportId})

@register('GetTrackerProfileParcelByParcelIdForTransport')
def GetTrackerProfileParcelByParcelIdForTransport(trackerId: str, transportId: str):
    return CatalystClient().GetTrackerProfileParcelByParcelIdForTransport(**{'trackerId': trackerId, 'transportId': transportId})

@register('GetTrackerGroupProfileParcelForTransport')
def GetTrackerGroupProfileParcelForTransport(transportId: str):
    return CatalystClient().GetTrackerGroupProfileParcelForTransport(**{'transportId': transportId})

@register('GetTrackerGroupProfileParcelByParcelIdForTransport')
def GetTrackerGroupProfileParcelByParcelIdForTransport(trackergroupId: str, transportId: str):
    return CatalystClient().GetTrackerGroupProfileParcelByParcelIdForTransport(**{'trackergroupId': trackergroupId, 'transportId': transportId})

@register('GetWanVpnProfileParcelForTransport')
def GetWanVpnProfileParcelForTransport(transportId: str):
    return CatalystClient().GetWanVpnProfileParcelForTransport(**{'transportId': transportId})

@register('GetWanVpnProfileParcelByParcelIdForTransport')
def GetWanVpnProfileParcelByParcelIdForTransport(transportId: str, vpnId: str):
    return CatalystClient().GetWanVpnProfileParcelByParcelIdForTransport(**{'transportId': transportId, 'vpnId': vpnId})

@register('GetInterfaceCellularParcelsForTransportWanVpn')
def GetInterfaceCellularParcelsForTransportWanVpn(transportId: str, vpnId: str):
    return CatalystClient().GetInterfaceCellularParcelsForTransportWanVpn(**{'transportId': transportId, 'vpnId': vpnId})

@register('GetWanVpnInterfaceCellularAssociatedIpv6TrackerParcelsForTransport')
def GetWanVpnInterfaceCellularAssociatedIpv6TrackerParcelsForTransport(cellularId: str, transportId: str, vpnId: str):
    return CatalystClient().GetWanVpnInterfaceCellularAssociatedIpv6TrackerParcelsForTransport(**{'cellularId': cellularId, 'transportId': transportId, 'vpnId': vpnId})

@register('GetWanVpnInterfaceCellularAssociatedIpv6TrackerParcelByParcelIdForTransport')
def GetWanVpnInterfaceCellularAssociatedIpv6TrackerParcelByParcelIdForTransport(cellularId: str, ipv6_trackerId: str, transportId: str, vpnId: str):
    return CatalystClient().GetWanVpnInterfaceCellularAssociatedIpv6TrackerParcelByParcelIdForTransport(**{'cellularId': cellularId, 'ipv6-trackerId': ipv6_trackerId, 'transportId': transportId, 'vpnId': vpnId})

@register('GetWanVpnInterfaceCellularAssociatedIpv6TrackerGroupParcelsForTransport')
def GetWanVpnInterfaceCellularAssociatedIpv6TrackerGroupParcelsForTransport(cellularId: str, transportId: str, vpnId: str):
    return CatalystClient().GetWanVpnInterfaceCellularAssociatedIpv6TrackerGroupParcelsForTransport(**{'cellularId': cellularId, 'transportId': transportId, 'vpnId': vpnId})

@register('GetWanVpnInterfaceCellularAssociatedIpv6TrackerGroupParcelByParcelIdForTransport')
def GetWanVpnInterfaceCellularAssociatedIpv6TrackerGroupParcelByParcelIdForTransport(cellularId: str, ipv6_trackergroupId: str, transportId: str, vpnId: str):
    return CatalystClient().GetWanVpnInterfaceCellularAssociatedIpv6TrackerGroupParcelByParcelIdForTransport(**{'cellularId': cellularId, 'ipv6-trackergroupId': ipv6_trackergroupId, 'transportId': transportId, 'vpnId': vpnId})

@register('GetWanVpnInterfaceCellularAssociatedTrackerParcelsForTransport')
def GetWanVpnInterfaceCellularAssociatedTrackerParcelsForTransport(cellularId: str, transportId: str, vpnId: str):
    return CatalystClient().GetWanVpnInterfaceCellularAssociatedTrackerParcelsForTransport(**{'cellularId': cellularId, 'transportId': transportId, 'vpnId': vpnId})

@register('GetWanVpnInterfaceCellularAssociatedTrackerParcelByParcelIdForTransport')
def GetWanVpnInterfaceCellularAssociatedTrackerParcelByParcelIdForTransport(cellularId: str, trackerId: str, transportId: str, vpnId: str):
    return CatalystClient().GetWanVpnInterfaceCellularAssociatedTrackerParcelByParcelIdForTransport(**{'cellularId': cellularId, 'trackerId': trackerId, 'transportId': transportId, 'vpnId': vpnId})

@register('GetWanVpnInterfaceCellularAssociatedTrackerGroupParcelsForTransport')
def GetWanVpnInterfaceCellularAssociatedTrackerGroupParcelsForTransport(cellularId: str, transportId: str, vpnId: str):
    return CatalystClient().GetWanVpnInterfaceCellularAssociatedTrackerGroupParcelsForTransport(**{'cellularId': cellularId, 'transportId': transportId, 'vpnId': vpnId})

@register('GetWanVpnInterfaceCellularAssociatedTrackerGroupParcelByParcelIdForTransport')
def GetWanVpnInterfaceCellularAssociatedTrackerGroupParcelByParcelIdForTransport(cellularId: str, trackerGroupId: str, transportId: str, vpnId: str):
    return CatalystClient().GetWanVpnInterfaceCellularAssociatedTrackerGroupParcelByParcelIdForTransport(**{'cellularId': cellularId, 'trackerGroupId': trackerGroupId, 'transportId': transportId, 'vpnId': vpnId})

@register('GetWanVpnInterfaceCellularParcelByParcelIdForTransport')
def GetWanVpnInterfaceCellularParcelByParcelIdForTransport(intfId: str, transportId: str, vpnId: str):
    return CatalystClient().GetWanVpnInterfaceCellularParcelByParcelIdForTransport(**{'intfId': intfId, 'transportId': transportId, 'vpnId': vpnId})

@register('GetInterfaceEthernetParcelsForTransportWanVpn')
def GetInterfaceEthernetParcelsForTransportWanVpn(transportId: str, vpnId: str):
    return CatalystClient().GetInterfaceEthernetParcelsForTransportWanVpn(**{'transportId': transportId, 'vpnId': vpnId})

@register('GetWanVpnInterfaceEthernetParcelByParcelIdForTransport')
def GetWanVpnInterfaceEthernetParcelByParcelIdForTransport(ethernetId: str, transportId: str, vpnId: str):
    return CatalystClient().GetWanVpnInterfaceEthernetParcelByParcelIdForTransport(**{'ethernetId': ethernetId, 'transportId': transportId, 'vpnId': vpnId})

@register('GetWanVpnInterfaceEthernetAssociatedIpv6TrackerParcelsForTransport')
def GetWanVpnInterfaceEthernetAssociatedIpv6TrackerParcelsForTransport(ethernetId: str, transportId: str, vpnId: str):
    return CatalystClient().GetWanVpnInterfaceEthernetAssociatedIpv6TrackerParcelsForTransport(**{'ethernetId': ethernetId, 'transportId': transportId, 'vpnId': vpnId})

@register('GetWanVpnInterfaceEthernetAssociatedIpv6TrackerParcelByParcelIdForTransport')
def GetWanVpnInterfaceEthernetAssociatedIpv6TrackerParcelByParcelIdForTransport(ethernetId: str, ipv6_trackerId: str, transportId: str, vpnId: str):
    return CatalystClient().GetWanVpnInterfaceEthernetAssociatedIpv6TrackerParcelByParcelIdForTransport(**{'ethernetId': ethernetId, 'ipv6-trackerId': ipv6_trackerId, 'transportId': transportId, 'vpnId': vpnId})

@register('GetWanVpnInterfaceEthernetAssociatedIpv6TrackerGroupParcelsForTransport')
def GetWanVpnInterfaceEthernetAssociatedIpv6TrackerGroupParcelsForTransport(ethernetId: str, transportId: str, vpnId: str):
    return CatalystClient().GetWanVpnInterfaceEthernetAssociatedIpv6TrackerGroupParcelsForTransport(**{'ethernetId': ethernetId, 'transportId': transportId, 'vpnId': vpnId})

@register('GetWanVpnInterfaceEthernetAssociatedIpv6TrackerGroupParcelByParcelIdForTransport')
def GetWanVpnInterfaceEthernetAssociatedIpv6TrackerGroupParcelByParcelIdForTransport(ethernetId: str, ipv6_trackergroupId: str, transportId: str, vpnId: str):
    return CatalystClient().GetWanVpnInterfaceEthernetAssociatedIpv6TrackerGroupParcelByParcelIdForTransport(**{'ethernetId': ethernetId, 'ipv6-trackergroupId': ipv6_trackergroupId, 'transportId': transportId, 'vpnId': vpnId})

@register('GetWanVpnInterfaceEthernetAssociatedTrackerParcelsForTransport')
def GetWanVpnInterfaceEthernetAssociatedTrackerParcelsForTransport(ethernetId: str, transportId: str, vpnId: str):
    return CatalystClient().GetWanVpnInterfaceEthernetAssociatedTrackerParcelsForTransport(**{'ethernetId': ethernetId, 'transportId': transportId, 'vpnId': vpnId})

@register('GetWanVpnInterfaceEthernetAssociatedTrackerParcelByParcelIdForTransport')
def GetWanVpnInterfaceEthernetAssociatedTrackerParcelByParcelIdForTransport(ethernetId: str, trackerId: str, transportId: str, vpnId: str):
    return CatalystClient().GetWanVpnInterfaceEthernetAssociatedTrackerParcelByParcelIdForTransport(**{'ethernetId': ethernetId, 'trackerId': trackerId, 'transportId': transportId, 'vpnId': vpnId})

@register('GetWanVpnInterfaceEthernetAssociatedTrackerGroupParcelsForTransport')
def GetWanVpnInterfaceEthernetAssociatedTrackerGroupParcelsForTransport(ethernetId: str, transportId: str, vpnId: str):
    return CatalystClient().GetWanVpnInterfaceEthernetAssociatedTrackerGroupParcelsForTransport(**{'ethernetId': ethernetId, 'transportId': transportId, 'vpnId': vpnId})

@register('GetWanVpnInterfaceEthernetAssociatedTrackerGroupParcelByParcelIdForTransport')
def GetWanVpnInterfaceEthernetAssociatedTrackerGroupParcelByParcelIdForTransport(ethernetId: str, trackergroupId: str, transportId: str, vpnId: str):
    return CatalystClient().GetWanVpnInterfaceEthernetAssociatedTrackerGroupParcelByParcelIdForTransport(**{'ethernetId': ethernetId, 'trackergroupId': trackergroupId, 'transportId': transportId, 'vpnId': vpnId})

@register('GetInterfaceGreParcelsForTransportWanVpn')
def GetInterfaceGreParcelsForTransportWanVpn(transportId: str, vpnId: str):
    return CatalystClient().GetInterfaceGreParcelsForTransportWanVpn(**{'transportId': transportId, 'vpnId': vpnId})

@register('GetWanVpnInterfaceGreParcelByParcelIdForTransport')
def GetWanVpnInterfaceGreParcelByParcelIdForTransport(greId: str, transportId: str, vpnId: str):
    return CatalystClient().GetWanVpnInterfaceGreParcelByParcelIdForTransport(**{'greId': greId, 'transportId': transportId, 'vpnId': vpnId})

@register('GetWanVpnInterfaceGreAssociatedTrackerParcelsForTransport')
def GetWanVpnInterfaceGreAssociatedTrackerParcelsForTransport(greId: str, transportId: str, vpnId: str):
    return CatalystClient().GetWanVpnInterfaceGreAssociatedTrackerParcelsForTransport(**{'greId': greId, 'transportId': transportId, 'vpnId': vpnId})

@register('GetWanVpnInterfaceGreAssociatedTrackerParcelByParcelIdForTransport')
def GetWanVpnInterfaceGreAssociatedTrackerParcelByParcelIdForTransport(greId: str, trackerId: str, transportId: str, vpnId: str):
    return CatalystClient().GetWanVpnInterfaceGreAssociatedTrackerParcelByParcelIdForTransport(**{'greId': greId, 'trackerId': trackerId, 'transportId': transportId, 'vpnId': vpnId})

@register('getListOfProfileParcels_1')
def getListOfProfileParcels_1(transportId: str, vpnId: str):
    return CatalystClient().getListOfProfileParcels_1(**{'transportId': transportId, 'vpnId': vpnId})

@register('getProfileParcelByParcelId_1')
def getProfileParcelByParcelId_1(ipsecId: str, transportId: str, vpnId: str):
    return CatalystClient().getProfileParcelByParcelId_1(**{'ipsecId': ipsecId, 'transportId': transportId, 'vpnId': vpnId})

@register('GetWanVpnInterfaceIpsecAssociatedTrackerParcelsForTransport')
def GetWanVpnInterfaceIpsecAssociatedTrackerParcelsForTransport(ipsecId: str, transportId: str, vpnId: str):
    return CatalystClient().GetWanVpnInterfaceIpsecAssociatedTrackerParcelsForTransport(**{'ipsecId': ipsecId, 'transportId': transportId, 'vpnId': vpnId})

@register('GetWanVpnInterfaceIpsecAssociatedTrackerParcelByParcelIdForTransport')
def GetWanVpnInterfaceIpsecAssociatedTrackerParcelByParcelIdForTransport(ipsecId: str, trackerId: str, transportId: str, vpnId: str):
    return CatalystClient().GetWanVpnInterfaceIpsecAssociatedTrackerParcelByParcelIdForTransport(**{'ipsecId': ipsecId, 'trackerId': trackerId, 'transportId': transportId, 'vpnId': vpnId})

@register('GetInterfaceSerialParcelsForTransportWanVpn')
def GetInterfaceSerialParcelsForTransportWanVpn(transportId: str, vpnId: str):
    return CatalystClient().GetInterfaceSerialParcelsForTransportWanVpn(**{'transportId': transportId, 'vpnId': vpnId})

@register('GetWanVpnInterfaceSerialParcelByParcelIdForTransport')
def GetWanVpnInterfaceSerialParcelByParcelIdForTransport(serialId: str, transportId: str, vpnId: str):
    return CatalystClient().GetWanVpnInterfaceSerialParcelByParcelIdForTransport(**{'serialId': serialId, 'transportId': transportId, 'vpnId': vpnId})

@register('GetWanVpnAssociatedRoutingBgpParcelsForTransport')
def GetWanVpnAssociatedRoutingBgpParcelsForTransport(transportId: str, vpnId: str):
    return CatalystClient().GetWanVpnAssociatedRoutingBgpParcelsForTransport(**{'transportId': transportId, 'vpnId': vpnId})

@register('GetWanVpnAssociatedRoutingBgpParcelByParcelIdForTransport')
def GetWanVpnAssociatedRoutingBgpParcelByParcelIdForTransport(bgpId: str, transportId: str, vpnId: str):
    return CatalystClient().GetWanVpnAssociatedRoutingBgpParcelByParcelIdForTransport(**{'bgpId': bgpId, 'transportId': transportId, 'vpnId': vpnId})

@register('GetWanVpnAssociatedRoutingOspfParcelsForTransport')
def GetWanVpnAssociatedRoutingOspfParcelsForTransport(transportId: str, vpnId: str):
    return CatalystClient().GetWanVpnAssociatedRoutingOspfParcelsForTransport(**{'transportId': transportId, 'vpnId': vpnId})

@register('GetWanVpnAssociatedRoutingOspfParcelByParcelIdForTransport')
def GetWanVpnAssociatedRoutingOspfParcelByParcelIdForTransport(ospfId: str, transportId: str, vpnId: str):
    return CatalystClient().GetWanVpnAssociatedRoutingOspfParcelByParcelIdForTransport(**{'ospfId': ospfId, 'transportId': transportId, 'vpnId': vpnId})

@register('GetWanVpnAssociatedRoutingOspfv3IPv4AfParcelsForTransport')
def GetWanVpnAssociatedRoutingOspfv3IPv4AfParcelsForTransport(transportId: str, vpnId: str):
    return CatalystClient().GetWanVpnAssociatedRoutingOspfv3IPv4AfParcelsForTransport(**{'transportId': transportId, 'vpnId': vpnId})

@register('GetWanVpnAssociatedRoutingOspfv3IPv4AfParcelByParcelIdForTransport')
def GetWanVpnAssociatedRoutingOspfv3IPv4AfParcelByParcelIdForTransport(ospfv3Id: str, transportId: str, vpnId: str):
    return CatalystClient().GetWanVpnAssociatedRoutingOspfv3IPv4AfParcelByParcelIdForTransport(**{'ospfv3Id': ospfv3Id, 'transportId': transportId, 'vpnId': vpnId})

@register('GetWanVpnAssociatedRoutingOspfv3IPv6AfParcelsForTransport')
def GetWanVpnAssociatedRoutingOspfv3IPv6AfParcelsForTransport(transportId: str, vpnId: str):
    return CatalystClient().GetWanVpnAssociatedRoutingOspfv3IPv6AfParcelsForTransport(**{'transportId': transportId, 'vpnId': vpnId})

@register('GetWanVpnAssociatedRoutingOspfv3IPv6AfParcelByParcelIdForTransport')
def GetWanVpnAssociatedRoutingOspfv3IPv6AfParcelByParcelIdForTransport(ospfv3Id: str, transportId: str, vpnId: str):
    return CatalystClient().GetWanVpnAssociatedRoutingOspfv3IPv6AfParcelByParcelIdForTransport(**{'ospfv3Id': ospfv3Id, 'transportId': transportId, 'vpnId': vpnId})

@register('getMSLADevices')
def getMSLADevices():
    return CatalystClient().getMSLADevices(**{})

@register('getLicenseByUuid')
def getLicenseByUuid(uuid: str):
    return CatalystClient().getLicenseByUuid(**{'uuid': uuid})

@register('GetPolicyGroupBySolution')
def GetPolicyGroupBySolution(**kwargs):
    return CatalystClient().GetPolicyGroupBySolution(**{**kwargs})

@register('GetPolicyGroup')
def GetPolicyGroup(policyGroupId: str):
    return CatalystClient().GetPolicyGroup(**{'policyGroupId': policyGroupId})

@register('GetPolicyGroupAssociation')
def GetPolicyGroupAssociation(policyGroupId: str):
    return CatalystClient().GetPolicyGroupAssociation(**{'policyGroupId': policyGroupId})

@register('getPolicyGroupDeviceVariables')
def getPolicyGroupDeviceVariables(policyGroupId: str, **kwargs):
    return CatalystClient().getPolicyGroupDeviceVariables(**{'policyGroupId': policyGroupId, **kwargs})

@register('getPolicyGroupDeviceVariablesSchema')
def getPolicyGroupDeviceVariablesSchema(policyGroupId: str):
    return CatalystClient().getPolicyGroupDeviceVariablesSchema(**{'policyGroupId': policyGroupId})

@register('getAllReportTemplates')
def getAllReportTemplates():
    return CatalystClient().getAllReportTemplates(**{})

@register('downloadReportPreviewFile')
def downloadReportPreviewFile(**kwargs):
    return CatalystClient().downloadReportPreviewFile(**{**kwargs})

@register('getReportTemplateById')
def getReportTemplateById(reportId: str):
    return CatalystClient().getReportTemplateById(**{'reportId': reportId})

@register('getAllReportTasksByReportId')
def getAllReportTasksByReportId(reportId: str):
    return CatalystClient().getAllReportTasksByReportId(**{'reportId': reportId})

@register('downloadReportDataFile')
def downloadReportDataFile(reportId: str, taskId: str):
    return CatalystClient().downloadReportDataFile(**{'reportId': reportId, 'taskId': taskId})

@register('getUrlForSdoIdentityService')
def getUrlForSdoIdentityService():
    return CatalystClient().getUrlForSdoIdentityService(**{})

@register('getAllAccounts')
def getAllAccounts():
    return CatalystClient().getAllAccounts(**{})

@register('getRatePlansByAcctId')
def getRatePlansByAcctId(accountId: str):
    return CatalystClient().getRatePlansByAcctId(**{'accountId': accountId})

@register('getProvidersInfo')
def getProvidersInfo():
    return CatalystClient().getProvidersInfo(**{})

@register('getCommPlansByAcctId')
def getCommPlansByAcctId(accountId: str):
    return CatalystClient().getCommPlansByAcctId(**{'accountId': accountId})

@register('getProviderCredentialsByAccountId')
def getProviderCredentialsByAccountId(accountId: str):
    return CatalystClient().getProviderCredentialsByAccountId(**{'accountId': accountId})

@register('getDeviceDataUsage')
def getDeviceDataUsage(deviceUUID: str):
    return CatalystClient().getDeviceDataUsage(**{'deviceUUID': deviceUUID})

@register('serviceChainMapping')
def serviceChainMapping():
    return CatalystClient().serviceChainMapping(**{})

@register('getDevicesForTemplate')
def getDevicesForTemplate(**kwargs):
    return CatalystClient().getDevicesForTemplate(**{**kwargs})

@register('license')
def license(licenseType: str, virtual_account_id: str):
    return CatalystClient().license(**{'licenseType': licenseType, 'virtual_account_id': virtual_account_id})

@register('getUserSettings')
def getUserSettings():
    return CatalystClient().getUserSettings(**{})

@register('GetTopologyGroupBySolution')
def GetTopologyGroupBySolution(**kwargs):
    return CatalystClient().GetTopologyGroupBySolution(**{**kwargs})

@register('GetTopologyGroup')
def GetTopologyGroup(topologyGroupId: str):
    return CatalystClient().GetTopologyGroup(**{'topologyGroupId': topologyGroupId})

@register('generateDeviceInterfaceStatisticsData')
def generateDeviceInterfaceStatisticsData(**kwargs):
    return CatalystClient().generateDeviceInterfaceStatisticsData(**{**kwargs})

@register('getCountWithInterfaceStatistics')
def getCountWithInterfaceStatistics(endDate: str, startDate: str, **kwargs):
    return CatalystClient().getCountWithInterfaceStatistics(**{'endDate': endDate, 'startDate': startDate, **kwargs})

@register('getStatDataFieldsByInterfaceStatistics')
def getStatDataFieldsByInterfaceStatistics():
    return CatalystClient().getStatDataFieldsByInterfaceStatistics(**{})

@register('getWaniRecommendations')
def getWaniRecommendations(**kwargs):
    return CatalystClient().getWaniRecommendations(**{**kwargs})

@register('getAppliedWaniRecommendations')
def getAppliedWaniRecommendations():
    return CatalystClient().getAppliedWaniRecommendations(**{})

@register('getListActivationStatus')
def getListActivationStatus(listId: str, listType: str):
    return CatalystClient().getListActivationStatus(**{'listId': listId, 'listType': listType})

@register('getPolicyActivationStatus')
def getPolicyActivationStatus(policyId: str, policyType: str):
    return CatalystClient().getPolicyActivationStatus(**{'policyId': policyId, 'policyType': policyType})

@register('webexAccessCode')
def webexAccessCode():
    return CatalystClient().webexAccessCode(**{})

@register('getWebexDataCentersSyncStatus')
def getWebexDataCentersSyncStatus():
    return CatalystClient().getWebexDataCentersSyncStatus(**{})

@register('redirectWebexDataCenters')
def redirectWebexDataCenters(code: str):
    return CatalystClient().redirectWebexDataCenters(**{'code': code})
