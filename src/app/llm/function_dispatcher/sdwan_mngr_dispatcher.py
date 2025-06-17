# app/llm/function_dispatcher/sdwan_mngr_dispatcher.py
from typing import Any
from app.llm.function_dispatcher import register
from app.llm.platform_clients.sdwan_mngr_client import Sdwan_mngrClient

@register('getSecureXAccessToken')
def getSecureXAccessToken(clientId: str, regionBaseUri: str):
    return Sdwan_mngrClient().getSecureXAccessToken(clientId=clientId, regionBaseUri=regionBaseUri)

@register('getAaaConfig')
def getAaaConfig():
    return Sdwan_mngrClient().getAaaConfig()

@register('listenAuthEvents')
def listenAuthEvents(sseSessionId: str):
    return Sdwan_mngrClient().listenAuthEvents(sseSessionId=sseSessionId)

@register('getRadiusConfig')
def getRadiusConfig():
    return Sdwan_mngrClient().getRadiusConfig()

@register('getTacacsConfig')
def getTacacsConfig():
    return Sdwan_mngrClient().getTacacsConfig()

@register('findUsers_1')
def findUsers_1():
    return Sdwan_mngrClient().findUsers_1()

@register('getActiveSessions_1')
def getActiveSessions_1():
    return Sdwan_mngrClient().getActiveSessions_1()

@register('findUserRole_1')
def findUserRole_1():
    return Sdwan_mngrClient().findUserRole_1()

@register('findUserAuthType_1')
def findUserAuthType_1():
    return Sdwan_mngrClient().findUserAuthType_1()

@register('findUserGroups')
def findUserGroups():
    return Sdwan_mngrClient().findUserGroups()

@register('createGroupGridColumns')
def createGroupGridColumns():
    return Sdwan_mngrClient().createGroupGridColumns()

@register('findUserGroupsAsKeyValue')
def findUserGroupsAsKeyValue():
    return Sdwan_mngrClient().findUserGroupsAsKeyValue()

@register('getVpnGroups')
def getVpnGroups():
    return Sdwan_mngrClient().getVpnGroups()

@register('getRawAlarmData')
def getRawAlarmData(**kwargs):
    return Sdwan_mngrClient().getRawAlarmData(**kwargs)

@register('getAggregationData')
def getAggregationData(query: str, **kwargs):
    return Sdwan_mngrClient().getAggregationData(query=query, **kwargs)

@register('getNonViewedActiveAlarmsCount')
def getNonViewedActiveAlarmsCount(**kwargs):
    return Sdwan_mngrClient().getNonViewedActiveAlarmsCount(**kwargs)

@register('listDisabledAlarm')
def listDisabledAlarm():
    return Sdwan_mngrClient().listDisabledAlarm()

@register('getDocCount')
def getDocCount(query: str, **kwargs):
    return Sdwan_mngrClient().getDocCount(query=query, **kwargs)

@register('getAlarmDataFields')
def getAlarmDataFields():
    return Sdwan_mngrClient().getAlarmDataFields()

@register('getLinkStateAlarmConfig')
def getLinkStateAlarmConfig():
    return Sdwan_mngrClient().getLinkStateAlarmConfig()

@register('getMasterManagerState')
def getMasterManagerState():
    return Sdwan_mngrClient().getMasterManagerState()

@register('getNonViewedAlarms')
def getNonViewedAlarms(**kwargs):
    return Sdwan_mngrClient().getNonViewedAlarms(**kwargs)

@register('getPage')
def getPage(**kwargs):
    return Sdwan_mngrClient().getPage(**kwargs)

@register('setPeriodicPurgeTimer')
def setPeriodicPurgeTimer(**kwargs):
    return Sdwan_mngrClient().setPeriodicPurgeTimer(**kwargs)

@register('getAlarmQueryFields')
def getAlarmQueryFields():
    return Sdwan_mngrClient().getAlarmQueryFields()

@register('getFieldDetails')
def getFieldDetails():
    return Sdwan_mngrClient().getFieldDetails()

@register('reset')
def reset():
    return Sdwan_mngrClient().reset()

@register('restartCorrelationEngine')
def restartCorrelationEngine():
    return Sdwan_mngrClient().restartCorrelationEngine()

@register('getAlarmTypesAsKeyValue')
def getAlarmTypesAsKeyValue():
    return Sdwan_mngrClient().getAlarmTypesAsKeyValue()

@register('getBySeverity')
def getBySeverity(severity-level: list, **kwargs):
    return Sdwan_mngrClient().getBySeverity(severity-level=severity-level, **kwargs)

@register('getAlarmSeverityCustomHistogram')
def getAlarmSeverityCustomHistogram(query: str, **kwargs):
    return Sdwan_mngrClient().getAlarmSeverityCustomHistogram(query=query, **kwargs)

@register('getAlarmSeverityMappings')
def getAlarmSeverityMappings():
    return Sdwan_mngrClient().getAlarmSeverityMappings()

@register('getStats')
def getStats():
    return Sdwan_mngrClient().getStats()

@register('getDeviceTopic')
def getDeviceTopic(ip: str):
    return Sdwan_mngrClient().getDeviceTopic(ip=ip)

@register('getAlarmDetails')
def getAlarmDetails(alarm_uuid: str, **kwargs):
    return Sdwan_mngrClient().getAlarmDetails(alarm_uuid=alarm_uuid, **kwargs)

@register('getAllAppList')
def getAllAppList(**kwargs):
    return Sdwan_mngrClient().getAllAppList(**kwargs)

@register('getAppListCategory')
def getAppListCategory():
    return Sdwan_mngrClient().getAppListCategory()

@register('getNetworkDiscoveredApps')
def getNetworkDiscoveredApps():
    return Sdwan_mngrClient().getNetworkDiscoveredApps()

@register('getAttributeMappingForApps')
def getAttributeMappingForApps():
    return Sdwan_mngrClient().getAttributeMappingForApps()

@register('getKubernetesServices')
def getKubernetesServices(**kwargs):
    return Sdwan_mngrClient().getKubernetesServices(**kwargs)

@register('getAppByUuid')
def getAppByUuid(app-uuid: str):
    return Sdwan_mngrClient().getAppByUuid(app-uuid=app-uuid)

@register('getAppList')
def getAppList(**kwargs):
    return Sdwan_mngrClient().getAppList(**kwargs)

@register('getKubernetesCluster')
def getKubernetesCluster(**kwargs):
    return Sdwan_mngrClient().getKubernetesCluster(**kwargs)

@register('getActiveSaasFeeds')
def getActiveSaasFeeds():
    return Sdwan_mngrClient().getActiveSaasFeeds()

@register('getAllSaasFeedForSelectedApp')
def getAllSaasFeedForSelectedApp(feedId: str):
    return Sdwan_mngrClient().getAllSaasFeedForSelectedApp(feedId=feedId)

@register('getStatDataRawAuditLogData')
def getStatDataRawAuditLogData(query: str):
    return Sdwan_mngrClient().getStatDataRawAuditLogData(query=query)

@register('getPropertyAggregationData')
def getPropertyAggregationData(query: str):
    return Sdwan_mngrClient().getPropertyAggregationData(query=query)

@register('getCount')
def getCount(query: str):
    return Sdwan_mngrClient().getCount(query=query)

@register('getStatDataFields')
def getStatDataFields():
    return Sdwan_mngrClient().getStatDataFields()

@register('getStatBulkRawPropertyData')
def getStatBulkRawPropertyData(count: int, query: str, **kwargs):
    return Sdwan_mngrClient().getStatBulkRawPropertyData(count=count, query=query, **kwargs)

@register('getStatQueryFields')
def getStatQueryFields():
    return Sdwan_mngrClient().getStatQueryFields()

@register('generateAuditLog')
def generateAuditLog(query: str, **kwargs):
    return Sdwan_mngrClient().generateAuditLog(query=query, **kwargs)

@register('getAuditSeverityCustomHistogram')
def getAuditSeverityCustomHistogram(query: str):
    return Sdwan_mngrClient().getAuditSeverityCustomHistogram(query=query)

@register('getLocalBackupInfo')
def getLocalBackupInfo(localBackupInfoId: str):
    return Sdwan_mngrClient().getLocalBackupInfo(localBackupInfoId=localBackupInfoId)

@register('downloadBackupFile')
def downloadBackupFile(path: str):
    return Sdwan_mngrClient().downloadBackupFile(path=path)

@register('listBackup')
def listBackup(**kwargs):
    return Sdwan_mngrClient().listBackup(**kwargs)

@register('getCdnaSenseService')
def getCdnaSenseService(tag: str):
    return Sdwan_mngrClient().getCdnaSenseService(tag=tag)

@register('getCdnaServer')
def getCdnaServer():
    return Sdwan_mngrClient().getCdnaServer()

@register('getControllerCertStatus')
def getControllerCertStatus():
    return Sdwan_mngrClient().getControllerCertStatus()

@register('getCSRViewRightMenus')
def getCSRViewRightMenus():
    return Sdwan_mngrClient().getCSRViewRightMenus()

@register('getDeviceViewRightMenus')
def getDeviceViewRightMenus():
    return Sdwan_mngrClient().getDeviceViewRightMenus()

@register('getDevicesList')
def getDevicesList():
    return Sdwan_mngrClient().getDevicesList()

@register('getListStatus')
def getListStatus():
    return Sdwan_mngrClient().getListStatus()

@register('setvSmartMtHubList')
def setvSmartMtHubList():
    return Sdwan_mngrClient().setvSmartMtHubList()

@register('getQuarantineBanner')
def getQuarantineBanner():
    return Sdwan_mngrClient().getQuarantineBanner()

@register('getCertificateData')
def getCertificateData(**kwargs):
    return Sdwan_mngrClient().getCertificateData(**kwargs)

@register('getRootCertChains')
def getRootCertChains(action: str):
    return Sdwan_mngrClient().getRootCertChains(action=action)

@register('getRootCertificate')
def getRootCertificate():
    return Sdwan_mngrClient().getRootCertificate()

@register('rsaKeyLength2048ForAllDevices')
def rsaKeyLength2048ForAllDevices():
    return Sdwan_mngrClient().rsaKeyLength2048ForAllDevices()

@register('getCertificateDetail')
def getCertificateDetail(**kwargs):
    return Sdwan_mngrClient().getCertificateDetail(**kwargs)

@register('getCertificateStats')
def getCertificateStats():
    return Sdwan_mngrClient().getCertificateStats()

@register('syncvBond')
def syncvBond():
    return Sdwan_mngrClient().syncvBond()

@register('getTokenList')
def getTokenList():
    return Sdwan_mngrClient().getTokenList()

@register('getInstalledCert')
def getInstalledCert(uuid: str):
    return Sdwan_mngrClient().getInstalledCert(uuid=uuid)

@register('getvEdgeCSR')
def getvEdgeCSR(uuid: str):
    return Sdwan_mngrClient().getvEdgeCSR(uuid=uuid)

@register('getvEdgeList')
def getvEdgeList(**kwargs):
    return Sdwan_mngrClient().getvEdgeList(**kwargs)

@register('getView')
def getView():
    return Sdwan_mngrClient().getView()

@register('getSelfSignedCert')
def getSelfSignedCert():
    return Sdwan_mngrClient().getSelfSignedCert()

@register('getvSmartList')
def getvSmartList():
    return Sdwan_mngrClient().getvSmartList()

@register('createServerInfo')
def createServerInfo():
    return Sdwan_mngrClient().createServerInfo()

@register('getCsrfToken')
def getCsrfToken(**kwargs):
    return Sdwan_mngrClient().getCsrfToken(**kwargs)

@register('getAccessTokenforDevice')
def getAccessTokenforDevice():
    return Sdwan_mngrClient().getAccessTokenforDevice()

@register('connect')
def connect():
    return Sdwan_mngrClient().connect()

@register('getCloudCredentials')
def getCloudCredentials():
    return Sdwan_mngrClient().getCloudCredentials()

@register('isStaging')
def isStaging():
    return Sdwan_mngrClient().isStaging()

@register('getTelemetryState')
def getTelemetryState():
    return Sdwan_mngrClient().getTelemetryState()

@register('getvAnalyticsDashboardList')
def getvAnalyticsDashboardList():
    return Sdwan_mngrClient().getvAnalyticsDashboardList()

@register('checkIfClusterLocked')
def checkIfClusterLocked():
    return Sdwan_mngrClient().checkIfClusterLocked()

@register('getClusterWorkflowVersion')
def getClusterWorkflowVersion():
    return Sdwan_mngrClient().getClusterWorkflowVersion()

@register('getConnectedDevices')
def getConnectedDevices(vmanageIP: str):
    return Sdwan_mngrClient().getConnectedDevices(vmanageIP=vmanageIP)

@register('healthDetails')
def healthDetails():
    return Sdwan_mngrClient().healthDetails()

@register('healthStatusInfo')
def healthStatusInfo():
    return Sdwan_mngrClient().healthStatusInfo()

@register('healthSummary')
def healthSummary(**kwargs):
    return Sdwan_mngrClient().healthSummary(**kwargs)

@register('hostHealthStatus')
def hostHealthStatus():
    return Sdwan_mngrClient().hostHealthStatus()

@register('getConfiguredIPList')
def getConfiguredIPList(vmanageID: str):
    return Sdwan_mngrClient().getConfiguredIPList(vmanageID=vmanageID)

@register('isClusterReady')
def isClusterReady():
    return Sdwan_mngrClient().isClusterReady()

@register('listVmanages')
def listVmanages():
    return Sdwan_mngrClient().listVmanages()

@register('nodeProperties')
def nodeProperties():
    return Sdwan_mngrClient().nodeProperties()

@register('getTenancyMode')
def getTenancyMode():
    return Sdwan_mngrClient().getTenancyMode()

@register('getTenantsList')
def getTenantsList():
    return Sdwan_mngrClient().getTenantsList()

@register('getVManageDetails')
def getVManageDetails(vmanageIP: str):
    return Sdwan_mngrClient().getVManageDetails(vmanageIP=vmanageIP)

@register('getConnectedDevicesPerTenant')
def getConnectedDevicesPerTenant(tenantId: str, vmanageIP: str):
    return Sdwan_mngrClient().getConnectedDevicesPerTenant(tenantId=tenantId, vmanageIP=vmanageIP)

@register('getvnfByDeviceId')
def getvnfByDeviceId(deviceId: str):
    return Sdwan_mngrClient().getvnfByDeviceId(deviceId=deviceId)

@register('getVNFEventsCountDetail')
def getVNFEventsCountDetail(user_group: str):
    return Sdwan_mngrClient().getVNFEventsCountDetail(user_group=user_group)

@register('getVNFAlarmCount')
def getVNFAlarmCount(user_group: str):
    return Sdwan_mngrClient().getVNFAlarmCount(user_group=user_group)

@register('getVNFEventsDetail')
def getVNFEventsDetail(vnfName: str):
    return Sdwan_mngrClient().getVNFEventsDetail(vnfName=vnfName)

@register('getVNFInterfaceDetail')
def getVNFInterfaceDetail(vnfName: str, **kwargs):
    return Sdwan_mngrClient().getVNFInterfaceDetail(vnfName=vnfName, **kwargs)

@register('doesValidImageExist')
def doesValidImageExist(containerName: str):
    return Sdwan_mngrClient().doesValidImageExist(containerName=containerName)

@register('getContainerInspectData')
def getContainerInspectData(containerName: str, **kwargs):
    return Sdwan_mngrClient().getContainerInspectData(containerName=containerName, **kwargs)

@register('getContainerSettings')
def getContainerSettings(containerName: str, **kwargs):
    return Sdwan_mngrClient().getContainerSettings(containerName=containerName, **kwargs)

@register('generateDeviceStateData')
def generateDeviceStateData(state_data_type: str, **kwargs):
    return Sdwan_mngrClient().generateDeviceStateData(state_data_type=state_data_type, **kwargs)

@register('generateDeviceStateDataFields')
def generateDeviceStateDataFields(state_data_type: str):
    return Sdwan_mngrClient().generateDeviceStateDataFields(state_data_type=state_data_type)

@register('generateDeviceStateDataWithQueryString')
def generateDeviceStateDataWithQueryString(state_data_type: str):
    return Sdwan_mngrClient().generateDeviceStateDataWithQueryString(state_data_type=state_data_type)

@register('getStatisticsType')
def getStatisticsType():
    return Sdwan_mngrClient().getStatisticsType()

@register('getActiveAlarms')
def getActiveAlarms(**kwargs):
    return Sdwan_mngrClient().getActiveAlarms(**kwargs)

@register('generateDeviceStatisticsData')
def generateDeviceStatisticsData(state_data_type: str, **kwargs):
    return Sdwan_mngrClient().generateDeviceStatisticsData(state_data_type=state_data_type, **kwargs)

@register('getCountWithStateDataType')
def getCountWithStateDataType(endDate: str, startDate: str, state_data_type: str, **kwargs):
    return Sdwan_mngrClient().getCountWithStateDataType(endDate=endDate, startDate=startDate, state_data_type=state_data_type, **kwargs)

@register('getStatDataFieldsByStateDataType')
def getStatDataFieldsByStateDataType(state_data_type: str):
    return Sdwan_mngrClient().getStatDataFieldsByStateDataType(state_data_type=state_data_type)

@register('getCloudSettings')
def getCloudSettings():
    return Sdwan_mngrClient().getCloudSettings()

@register('getAccessToken')
def getAccessToken():
    return Sdwan_mngrClient().getAccessToken()

@register('getIdToken')
def getIdToken():
    return Sdwan_mngrClient().getIdToken()

@register('getOTP')
def getOTP():
    return Sdwan_mngrClient().getOTP()

@register('getTelemetrySettings')
def getTelemetrySettings():
    return Sdwan_mngrClient().getTelemetrySettings()

@register('getDCATenantOwners')
def getDCATenantOwners():
    return Sdwan_mngrClient().getDCATenantOwners()

@register('getCrashLogsSynced')
def getCrashLogsSynced(deviceId: str):
    return Sdwan_mngrClient().getCrashLogsSynced(deviceId=deviceId)

@register('getCloudServicesConfigurationDCA')
def getCloudServicesConfigurationDCA():
    return Sdwan_mngrClient().getCloudServicesConfigurationDCA()

@register('listAllDevices')
def listAllDevices(**kwargs):
    return Sdwan_mngrClient().listAllDevices(**kwargs)

@register('getAAAservers')
def getAAAservers(deviceId: str):
    return Sdwan_mngrClient().getAAAservers(deviceId=deviceId)

@register('getAAAUsers')
def getAAAUsers(deviceId: str):
    return Sdwan_mngrClient().getAAAUsers(deviceId=deviceId)

@register('getACLMatchCounterUsers')
def getACLMatchCounterUsers(deviceId: str):
    return Sdwan_mngrClient().getACLMatchCounterUsers(deviceId=deviceId)

@register('generateChangePartitionInfo')
def generateChangePartitionInfo(deviceId: list):
    return Sdwan_mngrClient().generateChangePartitionInfo(deviceId=deviceId)

@register('generateDeactivateInfo')
def generateDeactivateInfo(deviceId: list):
    return Sdwan_mngrClient().generateDeactivateInfo(deviceId=deviceId)

@register('createFilterVPNList')
def createFilterVPNList(**kwargs):
    return Sdwan_mngrClient().createFilterVPNList(**kwargs)

@register('getFirmwareImages')
def getFirmwareImages():
    return Sdwan_mngrClient().getFirmwareImages()

@register('getFirmwareDevices')
def getFirmwareDevices():
    return Sdwan_mngrClient().getFirmwareDevices()

@register('getFirmwareRemoteImage')
def getFirmwareRemoteImage():
    return Sdwan_mngrClient().getFirmwareRemoteImage()

@register('getDevicesFWUpgrade')
def getDevicesFWUpgrade():
    return Sdwan_mngrClient().getDevicesFWUpgrade()

@register('getFirmwareImageDetails')
def getFirmwareImageDetails(versionId: str):
    return Sdwan_mngrClient().getFirmwareImageDetails(versionId=versionId)

@register('generateInstallInfo')
def generateInstallInfo(deviceId: list):
    return Sdwan_mngrClient().generateInstallInfo(deviceId=deviceId)

@register('generateDeviceList')
def generateDeviceList(deviceType: str, **kwargs):
    return Sdwan_mngrClient().generateDeviceList(deviceType=deviceType, **kwargs)

@register('generateDeviceActionList')
def generateDeviceActionList():
    return Sdwan_mngrClient().generateDeviceActionList()

@register('generateRebootInfo')
def generateRebootInfo(deviceId: list):
    return Sdwan_mngrClient().generateRebootInfo(deviceId=deviceId)

@register('generateRebootDeviceList')
def generateRebootDeviceList(deviceType: str, groupId: str):
    return Sdwan_mngrClient().generateRebootDeviceList(deviceType=deviceType, groupId=groupId)

@register('generateRediscoverInfo')
def generateRediscoverInfo():
    return Sdwan_mngrClient().generateRediscoverInfo()

@register('getRemoteServerList')
def getRemoteServerList():
    return Sdwan_mngrClient().getRemoteServerList()

@register('getRemoteServerById')
def getRemoteServerById(id: str):
    return Sdwan_mngrClient().getRemoteServerById(id=id)

@register('generateRemovePartitionInfo')
def generateRemovePartitionInfo(**kwargs):
    return Sdwan_mngrClient().generateRemovePartitionInfo(**kwargs)

@register('testApiKey')
def testApiKey(uuid: str):
    return Sdwan_mngrClient().testApiKey(uuid=uuid)

@register('generateSecurityDevicesList')
def generateSecurityDevicesList(groupId: str, policyType: str):
    return Sdwan_mngrClient().generateSecurityDevicesList(groupId=groupId, policyType=policyType)

@register('findSoftwareImages')
def findSoftwareImages():
    return Sdwan_mngrClient().findSoftwareImages()

@register('getImageProperties')
def getImageProperties(versionId: str):
    return Sdwan_mngrClient().getImageProperties(versionId=versionId)

@register('findSoftwareImagesWithFilters')
def findSoftwareImagesWithFilters(imageType: list, **kwargs):
    return Sdwan_mngrClient().findSoftwareImagesWithFilters(imageType=imageType, **kwargs)

@register('getUploadImagesCount')
def getUploadImagesCount(**kwargs):
    return Sdwan_mngrClient().getUploadImagesCount(**kwargs)

@register('generateUtdImageData')
def generateUtdImageData(type: str, utdsignature: str):
    return Sdwan_mngrClient().generateUtdImageData(type=type, utdsignature=utdsignature)

@register('downloadPackageFile')
def downloadPackageFile(fileName: str, **kwargs):
    return Sdwan_mngrClient().downloadPackageFile(fileName=fileName, **kwargs)

@register('getImageMetadata')
def getImageMetadata(versionId: str):
    return Sdwan_mngrClient().getImageMetadata(versionId=versionId)

@register('getImageRemoteServer')
def getImageRemoteServer(versionId: str):
    return Sdwan_mngrClient().getImageRemoteServer(versionId=versionId)

@register('findVEdgeSoftwareVersion')
def findVEdgeSoftwareVersion():
    return Sdwan_mngrClient().findVEdgeSoftwareVersion()

@register('findSoftwareVersion')
def findSoftwareVersion():
    return Sdwan_mngrClient().findSoftwareVersion()

@register('getVnfProperties')
def getVnfProperties(versionId: str):
    return Sdwan_mngrClient().getVnfProperties(versionId=versionId)

@register('findZtpSoftwareVersion')
def findZtpSoftwareVersion():
    return Sdwan_mngrClient().findZtpSoftwareVersion()

@register('triggerPendingTasksMonitoring')
def triggerPendingTasksMonitoring():
    return Sdwan_mngrClient().triggerPendingTasksMonitoring()

@register('cleanStatus')
def cleanStatus(**kwargs):
    return Sdwan_mngrClient().cleanStatus(**kwargs)

@register('getMaintenanceWindowFlag')
def getMaintenanceWindowFlag():
    return Sdwan_mngrClient().getMaintenanceWindowFlag()

@register('findRunningTasks')
def findRunningTasks():
    return Sdwan_mngrClient().findRunningTasks()

@register('getActiveTaskCount')
def getActiveTaskCount():
    return Sdwan_mngrClient().getActiveTaskCount()

@register('getCleanStatus')
def getCleanStatus(processId: str):
    return Sdwan_mngrClient().getCleanStatus(processId=processId)

@register('findStatus')
def findStatus(processId: str):
    return Sdwan_mngrClient().findStatus(processId=processId)

@register('testIoxConfig')
def testIoxConfig(deviceIP: str):
    return Sdwan_mngrClient().testIoxConfig(deviceIP=deviceIP)

@register('createVPNList')
def createVPNList():
    return Sdwan_mngrClient().createVPNList()

@register('getZTPUpgradeConfig')
def getZTPUpgradeConfig():
    return Sdwan_mngrClient().getZTPUpgradeConfig()

@register('getZTPUpgradeConfigSetting')
def getZTPUpgradeConfigSetting():
    return Sdwan_mngrClient().getZTPUpgradeConfigSetting()

@register('getAppHostingAttachedDevices')
def getAppHostingAttachedDevices(deviceId: str):
    return Sdwan_mngrClient().getAppHostingAttachedDevices(deviceId=deviceId)

@register('getAppHostingDetails')
def getAppHostingDetails(deviceId: str):
    return Sdwan_mngrClient().getAppHostingDetails(deviceId=deviceId)

@register('getAppHostingGuestRoutes')
def getAppHostingGuestRoutes(deviceId: str):
    return Sdwan_mngrClient().getAppHostingGuestRoutes(deviceId=deviceId)

@register('getAppHostingNetworkDevices')
def getAppHostingNetworkDevices(deviceId: str):
    return Sdwan_mngrClient().getAppHostingNetworkDevices(deviceId=deviceId)

@register('getAppHostingNetworkUtils')
def getAppHostingNetworkUtils(deviceId: str):
    return Sdwan_mngrClient().getAppHostingNetworkUtils(deviceId=deviceId)

@register('getAppHostingProcesses')
def getAppHostingProcesses(deviceId: str):
    return Sdwan_mngrClient().getAppHostingProcesses(deviceId=deviceId)

@register('getAppHostingStorageUtils')
def getAppHostingStorageUtils(deviceId: str):
    return Sdwan_mngrClient().getAppHostingStorageUtils(deviceId=deviceId)

@register('getAppHostingUtilization')
def getAppHostingUtilization(deviceId: str):
    return Sdwan_mngrClient().getAppHostingUtilization(deviceId=deviceId)

@register('createAppRouteSlaClassList')
def createAppRouteSlaClassList(deviceId: str):
    return Sdwan_mngrClient().createAppRouteSlaClassList(deviceId=deviceId)

@register('createAppRouteStatisticsList')
def createAppRouteStatisticsList(deviceId: str, **kwargs):
    return Sdwan_mngrClient().createAppRouteStatisticsList(deviceId=deviceId, **kwargs)

@register('getAppLogFlowCount')
def getAppLogFlowCount(deviceId: str):
    return Sdwan_mngrClient().getAppLogFlowCount(deviceId=deviceId)

@register('getAppLogFlows')
def getAppLogFlows(deviceId: str):
    return Sdwan_mngrClient().getAppLogFlows(deviceId=deviceId)

@register('createAppqoeActiveFlowIdDetails')
def createAppqoeActiveFlowIdDetails(deviceId: str, flow-id: str):
    return Sdwan_mngrClient().createAppqoeActiveFlowIdDetails(deviceId=deviceId, flow-id=flow-id)

@register('getAppqoeHputStats')
def getAppqoeHputStats(deviceId: str):
    return Sdwan_mngrClient().getAppqoeHputStats(deviceId=deviceId)

@register('getAppqoeNatStats')
def getAppqoeNatStats(deviceId: str):
    return Sdwan_mngrClient().getAppqoeNatStats(deviceId=deviceId)

@register('getAppqoeRmResources')
def getAppqoeRmResources(deviceId: str):
    return Sdwan_mngrClient().getAppqoeRmResources(deviceId=deviceId)

@register('getAppqoeRMStats')
def getAppqoeRMStats(deviceId: str):
    return Sdwan_mngrClient().getAppqoeRMStats(deviceId=deviceId)

@register('getAppqoeServicesStatus')
def getAppqoeServicesStatus(deviceId: str):
    return Sdwan_mngrClient().getAppqoeServicesStatus(deviceId=deviceId)

@register('getAppqoeSppiPipeStats')
def getAppqoeSppiPipeStats(deviceId: str):
    return Sdwan_mngrClient().getAppqoeSppiPipeStats(deviceId=deviceId)

@register('getAppqoeSppiQueueStats')
def getAppqoeSppiQueueStats(deviceId: str):
    return Sdwan_mngrClient().getAppqoeSppiQueueStats(deviceId=deviceId)

@register('getAppqoeClusterSummary')
def getAppqoeClusterSummary(deviceId: str):
    return Sdwan_mngrClient().getAppqoeClusterSummary(deviceId=deviceId)

@register('getAppqoeErrorRecent')
def getAppqoeErrorRecent(deviceId: str):
    return Sdwan_mngrClient().getAppqoeErrorRecent(deviceId=deviceId)

@register('createAppqoeFlowIdExpiredDetails')
def createAppqoeFlowIdExpiredDetails(deviceId: str, flow-id: str):
    return Sdwan_mngrClient().createAppqoeFlowIdExpiredDetails(deviceId=deviceId, flow-id=flow-id)

@register('getAppqoeFlowClosedError')
def getAppqoeFlowClosedError(deviceId: str):
    return Sdwan_mngrClient().getAppqoeFlowClosedError(deviceId=deviceId)

@register('getAppqoeExpired')
def getAppqoeExpired(deviceId: str):
    return Sdwan_mngrClient().getAppqoeExpired(deviceId=deviceId)

@register('getAppqoeServiceControllers')
def getAppqoeServiceControllers(deviceId: str):
    return Sdwan_mngrClient().getAppqoeServiceControllers(deviceId=deviceId)

@register('getAppqoeStatus')
def getAppqoeStatus(deviceId: str):
    return Sdwan_mngrClient().getAppqoeStatus(deviceId=deviceId)

@register('createAppqoeVpnIdList')
def createAppqoeVpnIdList(deviceId: str, vpn-id: str, **kwargs):
    return Sdwan_mngrClient().createAppqoeVpnIdList(deviceId=deviceId, vpn-id=vpn-id, **kwargs)

@register('getARPInterface')
def getARPInterface(deviceId: str):
    return Sdwan_mngrClient().getARPInterface(deviceId=deviceId)

@register('getAutonomousSoftwareVersion')
def getAutonomousSoftwareVersion(deviceId: str):
    return Sdwan_mngrClient().getAutonomousSoftwareVersion(deviceId=deviceId)

@register('createBFDHistoryList')
def createBFDHistoryList(deviceId: str, **kwargs):
    return Sdwan_mngrClient().createBFDHistoryList(deviceId=deviceId, **kwargs)

@register('createBFDLinkList')
def createBFDLinkList(state: str):
    return Sdwan_mngrClient().createBFDLinkList(state=state)

@register('createBFDSessions')
def createBFDSessions(deviceId: str, **kwargs):
    return Sdwan_mngrClient().createBFDSessions(deviceId=deviceId, **kwargs)

@register('getBFDSiteStateDetail')
def getBFDSiteStateDetail(**kwargs):
    return Sdwan_mngrClient().getBFDSiteStateDetail(**kwargs)

@register('getBFDSitesSummary')
def getBFDSitesSummary(vpnId: list, **kwargs):
    return Sdwan_mngrClient().getBFDSitesSummary(vpnId=vpnId, **kwargs)

@register('getDeviceBFDStateSummary')
def getDeviceBFDStateSummary(deviceId: str):
    return Sdwan_mngrClient().getDeviceBFDStateSummary(deviceId=deviceId)

@register('getDeviceBFDStateSummaryTloc')
def getDeviceBFDStateSummaryTloc(deviceId: str):
    return Sdwan_mngrClient().getDeviceBFDStateSummaryTloc(deviceId=deviceId)

@register('getDeviceTlocToIntfList')
def getDeviceTlocToIntfList(deviceId: str):
    return Sdwan_mngrClient().getDeviceTlocToIntfList(deviceId=deviceId)

@register('getDeviceBFDStatus')
def getDeviceBFDStatus():
    return Sdwan_mngrClient().getDeviceBFDStatus()

@register('createBFDSummary')
def createBFDSummary(deviceId: str):
    return Sdwan_mngrClient().createBFDSummary(deviceId=deviceId)

@register('getDeviceBFDStatusSummary')
def getDeviceBFDStatusSummary(deviceId: str):
    return Sdwan_mngrClient().getDeviceBFDStatusSummary(deviceId=deviceId)

@register('createSyncedBFDSession')
def createSyncedBFDSession(deviceId: str, **kwargs):
    return Sdwan_mngrClient().createSyncedBFDSession(deviceId=deviceId, **kwargs)

@register('createTLOCSummary')
def createTLOCSummary(deviceId: str):
    return Sdwan_mngrClient().createTLOCSummary(deviceId=deviceId)

@register('getBFDTlocStateDetail')
def getBFDTlocStateDetail(**kwargs):
    return Sdwan_mngrClient().getBFDTlocStateDetail(**kwargs)

@register('createBGPNeighborsList')
def createBGPNeighborsList(deviceId: str, **kwargs):
    return Sdwan_mngrClient().createBGPNeighborsList(deviceId=deviceId, **kwargs)

@register('createBGPRoutesList')
def createBGPRoutesList(deviceId: str, **kwargs):
    return Sdwan_mngrClient().createBGPRoutesList(deviceId=deviceId, **kwargs)

@register('createBGPSummary')
def createBGPSummary(deviceId: str):
    return Sdwan_mngrClient().createBGPSummary(deviceId=deviceId)

@register('getBridgeInterfaceList')
def getBridgeInterfaceList(deviceId: str):
    return Sdwan_mngrClient().getBridgeInterfaceList(deviceId=deviceId)

@register('getBridgeInterfaceMac')
def getBridgeInterfaceMac(deviceId: str, **kwargs):
    return Sdwan_mngrClient().getBridgeInterfaceMac(deviceId=deviceId, **kwargs)

@register('getBridgeInterfaceTable')
def getBridgeInterfaceTable(deviceId: str):
    return Sdwan_mngrClient().getBridgeInterfaceTable(deviceId=deviceId)

@register('getTenantsDevicesAndSites')
def getTenantsDevicesAndSites(**kwargs):
    return Sdwan_mngrClient().getTenantsDevicesAndSites(**kwargs)

@register('createAppFwdCflowdFlowsList')
def createAppFwdCflowdFlowsList(deviceId: str, **kwargs):
    return Sdwan_mngrClient().createAppFwdCflowdFlowsList(deviceId=deviceId, **kwargs)

@register('createAppFwdCflowdV6FlowsList')
def createAppFwdCflowdV6FlowsList(deviceId: str, **kwargs):
    return Sdwan_mngrClient().createAppFwdCflowdV6FlowsList(deviceId=deviceId, **kwargs)

@register('createCellularConnectionList')
def createCellularConnectionList(deviceId: str):
    return Sdwan_mngrClient().createCellularConnectionList(deviceId=deviceId)

@register('cellularCountDashlet')
def cellularCountDashlet(**kwargs):
    return Sdwan_mngrClient().cellularCountDashlet(**kwargs)

@register('dataUsage')
def dataUsage(**kwargs):
    return Sdwan_mngrClient().dataUsage(**kwargs)

@register('cellularCountDashletDetails')
def cellularCountDashletDetails(**kwargs):
    return Sdwan_mngrClient().cellularCountDashletDetails(**kwargs)

@register('createHardwareList')
def createHardwareList(deviceId: str):
    return Sdwan_mngrClient().createHardwareList(deviceId=deviceId)

@register('cellularHealthDashlet')
def cellularHealthDashlet(**kwargs):
    return Sdwan_mngrClient().cellularHealthDashlet(**kwargs)

@register('createModemList')
def createModemList(deviceId: str):
    return Sdwan_mngrClient().createModemList(deviceId=deviceId)

@register('createNetworkList')
def createNetworkList(deviceId: str):
    return Sdwan_mngrClient().createNetworkList(deviceId=deviceId)

@register('createProfileList')
def createProfileList(deviceId: str):
    return Sdwan_mngrClient().createProfileList(deviceId=deviceId)

@register('createRadioList')
def createRadioList(deviceId: str):
    return Sdwan_mngrClient().createRadioList(deviceId=deviceId)

@register('createSessionsList')
def createSessionsList(deviceId: str, **kwargs):
    return Sdwan_mngrClient().createSessionsList(deviceId=deviceId, **kwargs)

@register('getCellularStatusList')
def getCellularStatusList(deviceId: str):
    return Sdwan_mngrClient().getCellularStatusList(deviceId=deviceId)

@register('getEiolteConnectionInfo')
def getEiolteConnectionInfo(deviceId: str):
    return Sdwan_mngrClient().getEiolteConnectionInfo(deviceId=deviceId)

@register('getEiolteHardwareInfo')
def getEiolteHardwareInfo(deviceId: str):
    return Sdwan_mngrClient().getEiolteHardwareInfo(deviceId=deviceId)

@register('getAONIpsecInterfaceCountersInfo')
def getAONIpsecInterfaceCountersInfo(deviceId: str):
    return Sdwan_mngrClient().getAONIpsecInterfaceCountersInfo(deviceId=deviceId)

@register('getAONIpsecInterfaceSessionnfo')
def getAONIpsecInterfaceSessionnfo(deviceId: str):
    return Sdwan_mngrClient().getAONIpsecInterfaceSessionnfo(deviceId=deviceId)

@register('getEiolteNetworkInfo')
def getEiolteNetworkInfo(deviceId: str):
    return Sdwan_mngrClient().getEiolteNetworkInfo(deviceId=deviceId)

@register('getEiolteRadioInfo')
def getEiolteRadioInfo(deviceId: str):
    return Sdwan_mngrClient().getEiolteRadioInfo(deviceId=deviceId)

@register('getEiolteSimInfo')
def getEiolteSimInfo(deviceId: str):
    return Sdwan_mngrClient().getEiolteSimInfo(deviceId=deviceId)

@register('getCflowdDPIDeviceFieldJSON')
def getCflowdDPIDeviceFieldJSON(**kwargs):
    return Sdwan_mngrClient().getCflowdDPIDeviceFieldJSON(**kwargs)

@register('createCflowdCollectorList')
def createCflowdCollectorList(deviceId: str):
    return Sdwan_mngrClient().createCflowdCollectorList(deviceId=deviceId)

@register('getCflowdDPIFieldJSON')
def getCflowdDPIFieldJSON(**kwargs):
    return Sdwan_mngrClient().getCflowdDPIFieldJSON(**kwargs)

@register('createCflowCollectorList')
def createCflowCollectorList(deviceId: str, **kwargs):
    return Sdwan_mngrClient().createCflowCollectorList(deviceId=deviceId, **kwargs)

@register('createCflowdFlowsCountList')
def createCflowdFlowsCountList(deviceId: str, **kwargs):
    return Sdwan_mngrClient().createCflowdFlowsCountList(deviceId=deviceId, **kwargs)

@register('getFnFCacheStats')
def getFnFCacheStats(deviceId: str):
    return Sdwan_mngrClient().getFnFCacheStats(deviceId=deviceId)

@register('getFnFExportClientStats')
def getFnFExportClientStats(deviceId: str):
    return Sdwan_mngrClient().getFnFExportClientStats(deviceId=deviceId)

@register('getFnFExportStats')
def getFnFExportStats(deviceId: str):
    return Sdwan_mngrClient().getFnFExportStats(deviceId=deviceId)

@register('getFnf')
def getFnf(deviceId: str):
    return Sdwan_mngrClient().getFnf(deviceId=deviceId)

@register('getFnFMonitorStats')
def getFnFMonitorStats(deviceId: str):
    return Sdwan_mngrClient().getFnFMonitorStats(deviceId=deviceId)

@register('createCflowdStatistics')
def createCflowdStatistics(deviceId: str):
    return Sdwan_mngrClient().createCflowdStatistics(deviceId=deviceId)

@register('createCflowdTemplate')
def createCflowdTemplate(deviceId: str):
    return Sdwan_mngrClient().createCflowdTemplate(deviceId=deviceId)

@register('getMpDatabase')
def getMpDatabase(deviceId: str):
    return Sdwan_mngrClient().getMpDatabase(deviceId=deviceId)

@register('getMpLocalMep')
def getMpLocalMep(deviceId: str, **kwargs):
    return Sdwan_mngrClient().getMpLocalMep(deviceId=deviceId, **kwargs)

@register('getMpLocalMip')
def getMpLocalMip(deviceId: str, **kwargs):
    return Sdwan_mngrClient().getMpLocalMip(deviceId=deviceId, **kwargs)

@register('getMpRemoteMep')
def getMpRemoteMep(deviceId: str, **kwargs):
    return Sdwan_mngrClient().getMpRemoteMep(deviceId=deviceId, **kwargs)

@register('createApplicationsDetailList')
def createApplicationsDetailList(**kwargs):
    return Sdwan_mngrClient().createApplicationsDetailList(**kwargs)

@register('createApplicationsList')
def createApplicationsList(**kwargs):
    return Sdwan_mngrClient().createApplicationsList(**kwargs)

@register('createGatewayExitsList')
def createGatewayExitsList(deviceId: str, **kwargs):
    return Sdwan_mngrClient().createGatewayExitsList(deviceId=deviceId, **kwargs)

@register('createLbApplicationsList')
def createLbApplicationsList(**kwargs):
    return Sdwan_mngrClient().createLbApplicationsList(**kwargs)

@register('createLocalExitsList')
def createLocalExitsList(deviceId: str, **kwargs):
    return Sdwan_mngrClient().createLocalExitsList(deviceId=deviceId, **kwargs)

@register('getComplianceDetails')
def getComplianceDetails(**kwargs):
    return Sdwan_mngrClient().getComplianceDetails(**kwargs)

@register('getComplianceSummary')
def getComplianceSummary():
    return Sdwan_mngrClient().getComplianceSummary()

@register('getDeviceRunningConfig')
def getDeviceRunningConfig(deviceId: list):
    return Sdwan_mngrClient().getDeviceRunningConfig(deviceId=deviceId)

@register('getDeviceRunningConfigHTML')
def getDeviceRunningConfigHTML(deviceId: list):
    return Sdwan_mngrClient().getDeviceRunningConfigHTML(deviceId=deviceId)

@register('getDeviceConfigurationCommitList')
def getDeviceConfigurationCommitList(deviceId: str):
    return Sdwan_mngrClient().getDeviceConfigurationCommitList(deviceId=deviceId)

@register('getAffinityConfig')
def getAffinityConfig(deviceId: str):
    return Sdwan_mngrClient().getAffinityConfig(deviceId=deviceId)

@register('getAffinityStatus')
def getAffinityStatus(deviceId: str):
    return Sdwan_mngrClient().getAffinityStatus(deviceId=deviceId)

@register('createRealTimeConnectionList')
def createRealTimeConnectionList(deviceId: str, **kwargs):
    return Sdwan_mngrClient().createRealTimeConnectionList(deviceId=deviceId, **kwargs)

@register('createConnectionHistoryListRealTime')
def createConnectionHistoryListRealTime(deviceId: str, **kwargs):
    return Sdwan_mngrClient().createConnectionHistoryListRealTime(deviceId=deviceId, **kwargs)

@register('createRealTimeConnectionList_1')
def createRealTimeConnectionList_1(deviceId: str, **kwargs):
    return Sdwan_mngrClient().createRealTimeConnectionList_1(deviceId=deviceId, **kwargs)

@register('getTotalCountForDeviceStates')
def getTotalCountForDeviceStates(**kwargs):
    return Sdwan_mngrClient().getTotalCountForDeviceStates(**kwargs)

@register('createLinkList')
def createLinkList(state: str):
    return Sdwan_mngrClient().createLinkList(state=state)

@register('createLocalPropertiesListListRealTIme')
def createLocalPropertiesListListRealTIme(deviceId: str):
    return Sdwan_mngrClient().createLocalPropertiesListListRealTIme(deviceId=deviceId)

@register('networkSummary')
def networkSummary(**kwargs):
    return Sdwan_mngrClient().networkSummary(**kwargs)

@register('createRealTimeRegionConnectionList')
def createRealTimeRegionConnectionList(deviceId: str):
    return Sdwan_mngrClient().createRealTimeRegionConnectionList(deviceId=deviceId)

@register('getConnectionStatistics')
def getConnectionStatistics(deviceId: str):
    return Sdwan_mngrClient().getConnectionStatistics(deviceId=deviceId)

@register('getLocalDeviceStatus')
def getLocalDeviceStatus():
    return Sdwan_mngrClient().getLocalDeviceStatus()

@register('createConnectionsSummary')
def createConnectionsSummary(deviceId: str):
    return Sdwan_mngrClient().createConnectionsSummary(deviceId=deviceId)

@register('getDeviceControlStatusSummary')
def getDeviceControlStatusSummary(deviceId: str):
    return Sdwan_mngrClient().getDeviceControlStatusSummary(deviceId=deviceId)

@register('createSyncedConnectionList')
def createSyncedConnectionList(deviceId: str, **kwargs):
    return Sdwan_mngrClient().createSyncedConnectionList(deviceId=deviceId, **kwargs)

@register('createLocalPropertiesSyncedList')
def createLocalPropertiesSyncedList(deviceId: str):
    return Sdwan_mngrClient().createLocalPropertiesSyncedList(deviceId=deviceId)

@register('createWanInterfaceSyncedList')
def createWanInterfaceSyncedList(deviceId: str):
    return Sdwan_mngrClient().createWanInterfaceSyncedList(deviceId=deviceId)

@register('createValidDevicesListRealTime')
def createValidDevicesListRealTime(deviceId: str):
    return Sdwan_mngrClient().createValidDevicesListRealTime(deviceId=deviceId)

@register('getValidVManageIdRealTime')
def getValidVManageIdRealTime(deviceId: str):
    return Sdwan_mngrClient().getValidVManageIdRealTime(deviceId=deviceId)

@register('createValidVSmartsListRealTime')
def createValidVSmartsListRealTime(deviceId: str):
    return Sdwan_mngrClient().createValidVSmartsListRealTime(deviceId=deviceId)

@register('createWanInterfaceListList')
def createWanInterfaceListList(deviceId: str):
    return Sdwan_mngrClient().createWanInterfaceListList(deviceId=deviceId)

@register('getPortHopColor')
def getPortHopColor(deviceId: str):
    return Sdwan_mngrClient().getPortHopColor(deviceId=deviceId)

@register('getDeviceCounters')
def getDeviceCounters():
    return Sdwan_mngrClient().getDeviceCounters()

@register('getDeviceCrashLogs')
def getDeviceCrashLogs(deviceId: str):
    return Sdwan_mngrClient().getDeviceCrashLogs(deviceId=deviceId)

@register('getAllDeviceCrashLogs')
def getAllDeviceCrashLogs():
    return Sdwan_mngrClient().getAllDeviceCrashLogs()

@register('getDeviceCrashInformation')
def getDeviceCrashInformation(deviceId: str, filename: str):
    return Sdwan_mngrClient().getDeviceCrashInformation(deviceId=deviceId, filename=filename)

@register('getDeviceCrashLogsSynced')
def getDeviceCrashLogsSynced(deviceId: str):
    return Sdwan_mngrClient().getDeviceCrashLogsSynced(deviceId=deviceId)

@register('createDeviceContainersInfo')
def createDeviceContainersInfo(deviceId: str):
    return Sdwan_mngrClient().createDeviceContainersInfo(deviceId=deviceId)

@register('getPnicStats')
def getPnicStats(deviceId: str):
    return Sdwan_mngrClient().getPnicStats(deviceId=deviceId)

@register('getPNICStatsFromDevice')
def getPNICStatsFromDevice(deviceId: str):
    return Sdwan_mngrClient().getPNICStatsFromDevice(deviceId=deviceId)

@register('getRBACInterface')
def getRBACInterface(deviceId: str):
    return Sdwan_mngrClient().getRBACInterface(deviceId=deviceId)

@register('getAllocationInfo')
def getAllocationInfo(deviceId: str):
    return Sdwan_mngrClient().getAllocationInfo(deviceId=deviceId)

@register('getCPUInfo')
def getCPUInfo(deviceId: str):
    return Sdwan_mngrClient().getCPUInfo(deviceId=deviceId)

@register('getVNFInfo')
def getVNFInfo(deviceId: str):
    return Sdwan_mngrClient().getVNFInfo(deviceId=deviceId)

@register('createDeviceSystemSettingNativeInfo')
def createDeviceSystemSettingNativeInfo(deviceId: str):
    return Sdwan_mngrClient().createDeviceSystemSettingNativeInfo(deviceId=deviceId)

@register('createDeviceSystemProcessList')
def createDeviceSystemProcessList(deviceId: str):
    return Sdwan_mngrClient().createDeviceSystemProcessList(deviceId=deviceId)

@register('createDeviceSystemSetting')
def createDeviceSystemSetting(deviceId: str):
    return Sdwan_mngrClient().createDeviceSystemSetting(deviceId=deviceId)

@register('createDeviceSystemStatus')
def createDeviceSystemStatus(deviceId: str):
    return Sdwan_mngrClient().createDeviceSystemStatus(deviceId=deviceId)

@register('getCtsPac')
def getCtsPac(deviceId: str):
    return Sdwan_mngrClient().getCtsPac(deviceId=deviceId)

@register('getDeviceOnlyStatus')
def getDeviceOnlyStatus():
    return Sdwan_mngrClient().getDeviceOnlyStatus()

@register('getDHCPClient')
def getDHCPClient(deviceId: str):
    return Sdwan_mngrClient().getDHCPClient(deviceId=deviceId)

@register('getDHCPInterface')
def getDHCPInterface(deviceId: str):
    return Sdwan_mngrClient().getDHCPInterface(deviceId=deviceId)

@register('getDHCPServer')
def getDHCPServer(deviceId: str):
    return Sdwan_mngrClient().getDHCPServer(deviceId=deviceId)

@register('getDHCPv6Interface')
def getDHCPv6Interface(deviceId: str):
    return Sdwan_mngrClient().getDHCPv6Interface(deviceId=deviceId)

@register('getWLANDOT1xClients')
def getWLANDOT1xClients(deviceId: str):
    return Sdwan_mngrClient().getWLANDOT1xClients(deviceId=deviceId)

@register('getWLANDOT1xInterfaces')
def getWLANDOT1xInterfaces(deviceId: str):
    return Sdwan_mngrClient().getWLANDOT1xInterfaces(deviceId=deviceId)

@register('getDOT1xRadius')
def getDOT1xRadius(deviceId: str):
    return Sdwan_mngrClient().getDOT1xRadius(deviceId=deviceId)

@register('createSoftwareList')
def createSoftwareList(deviceId: str):
    return Sdwan_mngrClient().createSoftwareList(deviceId=deviceId)

@register('getSupportedApplicationList')
def getSupportedApplicationList():
    return Sdwan_mngrClient().getSupportedApplicationList()

@register('getDPIDeviceFieldJSON')
def getDPIDeviceFieldJSON(**kwargs):
    return Sdwan_mngrClient().getDPIDeviceFieldJSON(**kwargs)

@register('createDPICollectorList')
def createDPICollectorList(deviceId: str, **kwargs):
    return Sdwan_mngrClient().createDPICollectorList(deviceId=deviceId, **kwargs)

@register('getCommonApplicationList')
def getCommonApplicationList():
    return Sdwan_mngrClient().getCommonApplicationList()

@register('getDPIFieldJSON')
def getDPIFieldJSON():
    return Sdwan_mngrClient().getDPIFieldJSON()

@register('getDPIDeviceDetailsFieldJSON')
def getDPIDeviceDetailsFieldJSON():
    return Sdwan_mngrClient().getDPIDeviceDetailsFieldJSON()

@register('createDPIFlowsList')
def createDPIFlowsList(deviceId: str, **kwargs):
    return Sdwan_mngrClient().createDPIFlowsList(deviceId=deviceId, **kwargs)

@register('getQosmosStaticApplicationList')
def getQosmosStaticApplicationList():
    return Sdwan_mngrClient().getQosmosStaticApplicationList()

@register('getQosmosApplicationList')
def getQosmosApplicationList():
    return Sdwan_mngrClient().getQosmosApplicationList()

@register('createDPISummaryRealTime')
def createDPISummaryRealTime(deviceId: str):
    return Sdwan_mngrClient().createDPISummaryRealTime(deviceId=deviceId)

@register('createDPIStatistics')
def createDPIStatistics(deviceId: str, **kwargs):
    return Sdwan_mngrClient().createDPIStatistics(deviceId=deviceId, **kwargs)

@register('getDreAutoBypassStats')
def getDreAutoBypassStats(deviceId: str, **kwargs):
    return Sdwan_mngrClient().getDreAutoBypassStats(deviceId=deviceId, **kwargs)

@register('getDreStats')
def getDreStats(deviceId: str):
    return Sdwan_mngrClient().getDreStats(deviceId=deviceId)

@register('getDreStatus')
def getDreStatus(deviceId: str):
    return Sdwan_mngrClient().getDreStatus(deviceId=deviceId)

@register('getDrePeerStats')
def getDrePeerStats(deviceId: str, **kwargs):
    return Sdwan_mngrClient().getDrePeerStats(deviceId=deviceId, **kwargs)

@register('getDualStaticRouteTrackerInfo')
def getDualStaticRouteTrackerInfo(deviceId: str):
    return Sdwan_mngrClient().getDualStaticRouteTrackerInfo(deviceId=deviceId)

@register('createEIGRPInterface')
def createEIGRPInterface(deviceId: str):
    return Sdwan_mngrClient().createEIGRPInterface(deviceId=deviceId)

@register('createEIGRPRoute')
def createEIGRPRoute(deviceId: str):
    return Sdwan_mngrClient().createEIGRPRoute(deviceId=deviceId)

@register('createEIGRPTopology')
def createEIGRPTopology(deviceId: str):
    return Sdwan_mngrClient().createEIGRPTopology(deviceId=deviceId)

@register('getEndpointTrackerInfo')
def getEndpointTrackerInfo(deviceId: str):
    return Sdwan_mngrClient().getEndpointTrackerInfo(deviceId=deviceId)

@register('getEndpointTrackerGroupInfo')
def getEndpointTrackerGroupInfo(deviceId: str):
    return Sdwan_mngrClient().getEndpointTrackerGroupInfo(deviceId=deviceId)

@register('getEnvironmentData')
def getEnvironmentData(deviceId: str):
    return Sdwan_mngrClient().getEnvironmentData(deviceId=deviceId)

@register('getRadiusServer')
def getRadiusServer(deviceId: str):
    return Sdwan_mngrClient().getRadiusServer(deviceId=deviceId)

@register('getFeatureList')
def getFeatureList(deviceId: str):
    return Sdwan_mngrClient().getFeatureList(deviceId=deviceId)

@register('getSyncedFeatureList')
def getSyncedFeatureList(deviceId: str):
    return Sdwan_mngrClient().getSyncedFeatureList(deviceId=deviceId)

@register('getDataCollectionStatusForDevice')
def getDataCollectionStatusForDevice(deviceUUID: str):
    return Sdwan_mngrClient().getDataCollectionStatusForDevice(deviceUUID=deviceUUID)

@register('downloadGeneratedFile')
def downloadGeneratedFile(requestUUID: str):
    return Sdwan_mngrClient().downloadGeneratedFile(requestUUID=requestUUID)

@register('getDataCollectionStatusForUUID')
def getDataCollectionStatusForUUID(requestUUID: str):
    return Sdwan_mngrClient().getDataCollectionStatusForUUID(requestUUID=requestUUID)

@register('getSupportedCommandsList')
def getSupportedCommandsList(deviceUUID: str):
    return Sdwan_mngrClient().getSupportedCommandsList(deviceUUID=deviceUUID)

@register('getGeofenceStatus')
def getGeofenceStatus(deviceId: str):
    return Sdwan_mngrClient().getGeofenceStatus(deviceId=deviceId)

@register('createAlarmList')
def createAlarmList(deviceId: str):
    return Sdwan_mngrClient().createAlarmList(deviceId=deviceId)

@register('createEnvironmentList')
def createEnvironmentList(deviceId: str):
    return Sdwan_mngrClient().createEnvironmentList(deviceId=deviceId)

@register('createErrorAlarmList')
def createErrorAlarmList():
    return Sdwan_mngrClient().createErrorAlarmList()

@register('createInventoryList')
def createInventoryList(deviceId: str):
    return Sdwan_mngrClient().createInventoryList(deviceId=deviceId)

@register('createStatusSummary')
def createStatusSummary(deviceId: str):
    return Sdwan_mngrClient().createStatusSummary(deviceId=deviceId)

@register('createSyncedAlarmList')
def createSyncedAlarmList(deviceId: str):
    return Sdwan_mngrClient().createSyncedAlarmList(deviceId=deviceId)

@register('createSyncedEnvironmentList')
def createSyncedEnvironmentList(deviceId: str):
    return Sdwan_mngrClient().createSyncedEnvironmentList(deviceId=deviceId)

@register('createSyncedInventoryList')
def createSyncedInventoryList(deviceId: str):
    return Sdwan_mngrClient().createSyncedInventoryList(deviceId=deviceId)

@register('createSystemList')
def createSystemList(deviceId: str):
    return Sdwan_mngrClient().createSystemList(deviceId=deviceId)

@register('createTempThresholdList')
def createTempThresholdList(deviceId: str):
    return Sdwan_mngrClient().createTempThresholdList(deviceId=deviceId)

@register('getHardwareHealthDetails')
def getHardwareHealthDetails(**kwargs):
    return Sdwan_mngrClient().getHardwareHealthDetails(**kwargs)

@register('getHardwareHealthSummary')
def getHardwareHealthSummary(vpnId: list, **kwargs):
    return Sdwan_mngrClient().getHardwareHealthSummary(vpnId=vpnId, **kwargs)

@register('getStatDataRawData_21')
def getStatDataRawData_21(**kwargs):
    return Sdwan_mngrClient().getStatDataRawData_21(**kwargs)

@register('getAggregationDataByQuery_23')
def getAggregationDataByQuery_23(**kwargs):
    return Sdwan_mngrClient().getAggregationDataByQuery_23(**kwargs)

@register('getLastThousandConfigList')
def getLastThousandConfigList(deviceId: str, query: str):
    return Sdwan_mngrClient().getLastThousandConfigList(deviceId=deviceId, query=query)

@register('getConfigDiff')
def getConfigDiff(config_id1: str, config_id2: str):
    return Sdwan_mngrClient().getConfigDiff(config_id1=config_id1, config_id2=config_id2)

@register('getDeviceConfig')
def getDeviceConfig(config_id: str):
    return Sdwan_mngrClient().getDeviceConfig(config_id=config_id)

@register('getStatDataRawDataAsCSV_21')
def getStatDataRawDataAsCSV_21(**kwargs):
    return Sdwan_mngrClient().getStatDataRawDataAsCSV_21(**kwargs)

@register('getCount_20')
def getCount_20(query: str):
    return Sdwan_mngrClient().getCount_20(query=query)

@register('getStatDataFields_22')
def getStatDataFields_22():
    return Sdwan_mngrClient().getStatDataFields_22()

@register('getStatsPaginationRawData_19')
def getStatsPaginationRawData_19(**kwargs):
    return Sdwan_mngrClient().getStatsPaginationRawData_19(**kwargs)

@register('getStatQueryFields_23')
def getStatQueryFields_23():
    return Sdwan_mngrClient().getStatQueryFields_23()

@register('createIGMPGroupsList')
def createIGMPGroupsList(deviceId: str):
    return Sdwan_mngrClient().createIGMPGroupsList(deviceId=deviceId)

@register('createIGMPInterfaceList')
def createIGMPInterfaceList(deviceId: str):
    return Sdwan_mngrClient().createIGMPInterfaceList(deviceId=deviceId)

@register('createIGMPStatisticsList')
def createIGMPStatisticsList(deviceId: str):
    return Sdwan_mngrClient().createIGMPStatisticsList(deviceId=deviceId)

@register('createIGMPSummary')
def createIGMPSummary(deviceId: str):
    return Sdwan_mngrClient().createIGMPSummary(deviceId=deviceId)

@register('getDeviceInterface')
def getDeviceInterface(deviceId: str, **kwargs):
    return Sdwan_mngrClient().getDeviceInterface(deviceId=deviceId, **kwargs)

@register('getDeviceInterfaceARPStats')
def getDeviceInterfaceARPStats(deviceId: str, **kwargs):
    return Sdwan_mngrClient().getDeviceInterfaceARPStats(deviceId=deviceId, **kwargs)

@register('getDeviceInterfaceErrorStats')
def getDeviceInterfaceErrorStats(deviceId: str, **kwargs):
    return Sdwan_mngrClient().getDeviceInterfaceErrorStats(deviceId=deviceId, **kwargs)

@register('getDeviceInterfaceIpv6Stats')
def getDeviceInterfaceIpv6Stats(deviceId: str, **kwargs):
    return Sdwan_mngrClient().getDeviceInterfaceIpv6Stats(deviceId=deviceId, **kwargs)

@register('getDeviceInterfacePktSizes')
def getDeviceInterfacePktSizes(deviceId: str, **kwargs):
    return Sdwan_mngrClient().getDeviceInterfacePktSizes(deviceId=deviceId, **kwargs)

@register('getDeviceInterfacePortStats')
def getDeviceInterfacePortStats(deviceId: str, **kwargs):
    return Sdwan_mngrClient().getDeviceInterfacePortStats(deviceId=deviceId, **kwargs)

@register('getDeviceInterfaceQosStats')
def getDeviceInterfaceQosStats(deviceId: str, **kwargs):
    return Sdwan_mngrClient().getDeviceInterfaceQosStats(deviceId=deviceId, **kwargs)

@register('getDeviceInterfaceQueueStats')
def getDeviceInterfaceQueueStats(deviceId: str, **kwargs):
    return Sdwan_mngrClient().getDeviceInterfaceQueueStats(deviceId=deviceId, **kwargs)

@register('getDeviceSerialInterface')
def getDeviceSerialInterface(deviceId: str, **kwargs):
    return Sdwan_mngrClient().getDeviceSerialInterface(deviceId=deviceId, **kwargs)

@register('getDeviceInterfaceStats')
def getDeviceInterfaceStats(deviceId: str, **kwargs):
    return Sdwan_mngrClient().getDeviceInterfaceStats(deviceId=deviceId, **kwargs)

@register('getSyncedDeviceInterface')
def getSyncedDeviceInterface(deviceId: str, **kwargs):
    return Sdwan_mngrClient().getSyncedDeviceInterface(deviceId=deviceId, **kwargs)

@register('trustsec')
def trustsec(deviceId: str):
    return Sdwan_mngrClient().trustsec(deviceId=deviceId)

@register('generateDeviceInterfaceVPN')
def generateDeviceInterfaceVPN(deviceId: str):
    return Sdwan_mngrClient().generateDeviceInterfaceVPN(deviceId=deviceId)

@register('createFibList')
def createFibList(deviceId: str, **kwargs):
    return Sdwan_mngrClient().createFibList(deviceId=deviceId, **kwargs)

@register('createIetfRoutingList')
def createIetfRoutingList(deviceId: str, **kwargs):
    return Sdwan_mngrClient().createIetfRoutingList(deviceId=deviceId, **kwargs)

@register('createIPMfibOilList')
def createIPMfibOilList(deviceId: str):
    return Sdwan_mngrClient().createIPMfibOilList(deviceId=deviceId)

@register('createIPMfibStatsList')
def createIPMfibStatsList(deviceId: str):
    return Sdwan_mngrClient().createIPMfibStatsList(deviceId=deviceId)

@register('createIPMfibSummaryList')
def createIPMfibSummaryList(deviceId: str):
    return Sdwan_mngrClient().createIPMfibSummaryList(deviceId=deviceId)

@register('createNatFilterList')
def createNatFilterList(deviceId: str, **kwargs):
    return Sdwan_mngrClient().createNatFilterList(deviceId=deviceId, **kwargs)

@register('createNatInterfaceList')
def createNatInterfaceList(deviceId: str):
    return Sdwan_mngrClient().createNatInterfaceList(deviceId=deviceId)

@register('createNatInterfaceStatisticsList')
def createNatInterfaceStatisticsList(deviceId: str):
    return Sdwan_mngrClient().createNatInterfaceStatisticsList(deviceId=deviceId)

@register('createNatTranslationList')
def createNatTranslationList(deviceId: str):
    return Sdwan_mngrClient().createNatTranslationList(deviceId=deviceId)

@register('createNat64TranslationList')
def createNat64TranslationList(deviceId: str):
    return Sdwan_mngrClient().createNat64TranslationList(deviceId=deviceId)

@register('createRouteTableList')
def createRouteTableList(deviceId: str, **kwargs):
    return Sdwan_mngrClient().createRouteTableList(deviceId=deviceId, **kwargs)

@register('createIPv4FibList')
def createIPv4FibList(deviceId: str, **kwargs):
    return Sdwan_mngrClient().createIPv4FibList(deviceId=deviceId, **kwargs)

@register('createIPv6FibList')
def createIPv6FibList(deviceId: str, **kwargs):
    return Sdwan_mngrClient().createIPv6FibList(deviceId=deviceId, **kwargs)

@register('createCryptoIpsecIdentity')
def createCryptoIpsecIdentity(deviceId: str, **kwargs):
    return Sdwan_mngrClient().createCryptoIpsecIdentity(deviceId=deviceId, **kwargs)

@register('createIkeInboundList')
def createIkeInboundList(deviceId: str):
    return Sdwan_mngrClient().createIkeInboundList(deviceId=deviceId)

@register('createIkeOutboundList')
def createIkeOutboundList(deviceId: str):
    return Sdwan_mngrClient().createIkeOutboundList(deviceId=deviceId)

@register('createIkeSessions')
def createIkeSessions(deviceId: str, **kwargs):
    return Sdwan_mngrClient().createIkeSessions(deviceId=deviceId, **kwargs)

@register('createCryptov1LocalSAList')
def createCryptov1LocalSAList(deviceId: str, **kwargs):
    return Sdwan_mngrClient().createCryptov1LocalSAList(deviceId=deviceId, **kwargs)

@register('createCryptov2LocalSAList')
def createCryptov2LocalSAList(deviceId: str):
    return Sdwan_mngrClient().createCryptov2LocalSAList(deviceId=deviceId)

@register('createInBoundList')
def createInBoundList(deviceId: str, **kwargs):
    return Sdwan_mngrClient().createInBoundList(deviceId=deviceId, **kwargs)

@register('createLocalSAList')
def createLocalSAList(deviceId: str):
    return Sdwan_mngrClient().createLocalSAList(deviceId=deviceId)

@register('createOutBoundList')
def createOutBoundList(deviceId: str, **kwargs):
    return Sdwan_mngrClient().createOutBoundList(deviceId=deviceId, **kwargs)

@register('createIPsecPWKInboundConnections')
def createIPsecPWKInboundConnections(deviceId: str, **kwargs):
    return Sdwan_mngrClient().createIPsecPWKInboundConnections(deviceId=deviceId, **kwargs)

@register('createIPsecPWKLocalSA')
def createIPsecPWKLocalSA(deviceId: str, **kwargs):
    return Sdwan_mngrClient().createIPsecPWKLocalSA(deviceId=deviceId, **kwargs)

@register('createIPsecPWKOutboundConnections')
def createIPsecPWKOutboundConnections(deviceId: str, **kwargs):
    return Sdwan_mngrClient().createIPsecPWKOutboundConnections(deviceId=deviceId, **kwargs)

@register('getIpv6Data')
def getIpv6Data(deviceId: str):
    return Sdwan_mngrClient().getIpv6Data(deviceId=deviceId)

@register('getDeviceListAsKeyValue')
def getDeviceListAsKeyValue(**kwargs):
    return Sdwan_mngrClient().getDeviceListAsKeyValue(**kwargs)

@register('getLacpInterfaceList')
def getLacpInterfaceList(deviceId: str, **kwargs):
    return Sdwan_mngrClient().getLacpInterfaceList(deviceId=deviceId, **kwargs)

@register('getLacpMembers')
def getLacpMembers(deviceId: str, **kwargs):
    return Sdwan_mngrClient().getLacpMembers(deviceId=deviceId, **kwargs)

@register('getLicenseEvalInfo')
def getLicenseEvalInfo(deviceId: str):
    return Sdwan_mngrClient().getLicenseEvalInfo(deviceId=deviceId)

@register('getLicensePAKInfo')
def getLicensePAKInfo(deviceId: str):
    return Sdwan_mngrClient().getLicensePAKInfo(deviceId=deviceId)

@register('getLicensePrivacyInfo')
def getLicensePrivacyInfo(deviceId: str):
    return Sdwan_mngrClient().getLicensePrivacyInfo(deviceId=deviceId)

@register('getLicenseRegInfo')
def getLicenseRegInfo(deviceId: str):
    return Sdwan_mngrClient().getLicenseRegInfo(deviceId=deviceId)

@register('getLicenseUDIInfo')
def getLicenseUDIInfo(deviceId: str):
    return Sdwan_mngrClient().getLicenseUDIInfo(deviceId=deviceId)

@register('getLicenseUsageInfo')
def getLicenseUsageInfo(deviceId: str):
    return Sdwan_mngrClient().getLicenseUsageInfo(deviceId=deviceId)

@register('getLoggingFromDevice')
def getLoggingFromDevice(deviceId: str):
    return Sdwan_mngrClient().getLoggingFromDevice(deviceId=deviceId)

@register('listAllDeviceModels')
def listAllDeviceModels():
    return Sdwan_mngrClient().listAllDeviceModels()

@register('getDeviceModels')
def getDeviceModels(uuid: str):
    return Sdwan_mngrClient().getDeviceModels(uuid=uuid)

@register('listAllMonitorDetailsDevices')
def listAllMonitorDetailsDevices():
    return Sdwan_mngrClient().listAllMonitorDetailsDevices()

@register('createReplicatorList')
def createReplicatorList(deviceId: str):
    return Sdwan_mngrClient().createReplicatorList(deviceId=deviceId)

@register('createRpfList')
def createRpfList(deviceId: str):
    return Sdwan_mngrClient().createRpfList(deviceId=deviceId)

@register('createTopologyList')
def createTopologyList(deviceId: str):
    return Sdwan_mngrClient().createTopologyList(deviceId=deviceId)

@register('createPimTunnelList')
def createPimTunnelList(deviceId: str):
    return Sdwan_mngrClient().createPimTunnelList(deviceId=deviceId)

@register('getIpv6Interface')
def getIpv6Interface(deviceId: str, **kwargs):
    return Sdwan_mngrClient().getIpv6Interface(deviceId=deviceId, **kwargs)

@register('getRunning')
def getRunning(deviceId: str):
    return Sdwan_mngrClient().getRunning(deviceId=deviceId)

@register('createAssociationsList')
def createAssociationsList(deviceId: str):
    return Sdwan_mngrClient().createAssociationsList(deviceId=deviceId)

@register('createPeerList')
def createPeerList(deviceId: str):
    return Sdwan_mngrClient().createPeerList(deviceId=deviceId)

@register('createNTPStatusList')
def createNTPStatusList(deviceId: str):
    return Sdwan_mngrClient().createNTPStatusList(deviceId=deviceId)

@register('createOMPCloudXRecv')
def createOMPCloudXRecv(deviceId: str):
    return Sdwan_mngrClient().createOMPCloudXRecv(deviceId=deviceId)

@register('createOMPLinkList')
def createOMPLinkList(state: str):
    return Sdwan_mngrClient().createOMPLinkList(state=state)

@register('createOMPMcastAutoDiscoverAdvt')
def createOMPMcastAutoDiscoverAdvt(deviceId: str):
    return Sdwan_mngrClient().createOMPMcastAutoDiscoverAdvt(deviceId=deviceId)

@register('createOMPMcastAutoDiscoverRecv')
def createOMPMcastAutoDiscoverRecv(deviceId: str):
    return Sdwan_mngrClient().createOMPMcastAutoDiscoverRecv(deviceId=deviceId)

@register('createOMPMcastRoutesAdvt')
def createOMPMcastRoutesAdvt(deviceId: str):
    return Sdwan_mngrClient().createOMPMcastRoutesAdvt(deviceId=deviceId)

@register('createOMPMcastRoutesRecv')
def createOMPMcastRoutesRecv(deviceId: str):
    return Sdwan_mngrClient().createOMPMcastRoutesRecv(deviceId=deviceId)

@register('createOMPSessionList')
def createOMPSessionList(deviceId: str):
    return Sdwan_mngrClient().createOMPSessionList(deviceId=deviceId)

@register('createAdvertisedRoutesList')
def createAdvertisedRoutesList(deviceId: str):
    return Sdwan_mngrClient().createAdvertisedRoutesList(deviceId=deviceId)

@register('createAdvertisedRoutesListIpv6')
def createAdvertisedRoutesListIpv6(deviceId: str):
    return Sdwan_mngrClient().createAdvertisedRoutesListIpv6(deviceId=deviceId)

@register('createReceivedRoutesList')
def createReceivedRoutesList(deviceId: str):
    return Sdwan_mngrClient().createReceivedRoutesList(deviceId=deviceId)

@register('createReceivedRoutesListIpv6')
def createReceivedRoutesListIpv6(deviceId: str):
    return Sdwan_mngrClient().createReceivedRoutesListIpv6(deviceId=deviceId)

@register('createOMPServices')
def createOMPServices(deviceId: str):
    return Sdwan_mngrClient().createOMPServices(deviceId=deviceId)

@register('getDeviceOMPStatus')
def getDeviceOMPStatus():
    return Sdwan_mngrClient().getDeviceOMPStatus()

@register('createOMPSummary')
def createOMPSummary(deviceId: str):
    return Sdwan_mngrClient().createOMPSummary(deviceId=deviceId)

@register('createSyncedOMPSessionList')
def createSyncedOMPSessionList(deviceId: str):
    return Sdwan_mngrClient().createSyncedOMPSessionList(deviceId=deviceId)

@register('createAdvertisedTlocsList')
def createAdvertisedTlocsList(deviceId: str):
    return Sdwan_mngrClient().createAdvertisedTlocsList(deviceId=deviceId)

@register('createReceivedTlocsList')
def createReceivedTlocsList(deviceId: str):
    return Sdwan_mngrClient().createReceivedTlocsList(deviceId=deviceId)

@register('getOnDemandLocal')
def getOnDemandLocal(deviceId: str):
    return Sdwan_mngrClient().getOnDemandLocal(deviceId=deviceId)

@register('getOnDemandRemote')
def getOnDemandRemote(deviceId: str):
    return Sdwan_mngrClient().getOnDemandRemote(deviceId=deviceId)

@register('createConnectionListFromDevice')
def createConnectionListFromDevice(deviceId: str):
    return Sdwan_mngrClient().createConnectionListFromDevice(deviceId=deviceId)

@register('createConnectionHistoryList')
def createConnectionHistoryList(deviceId: str):
    return Sdwan_mngrClient().createConnectionHistoryList(deviceId=deviceId)

@register('createLocalPropertiesListList')
def createLocalPropertiesListList(deviceId: str):
    return Sdwan_mngrClient().createLocalPropertiesListList(deviceId=deviceId)

@register('createReverseProxyMappingList')
def createReverseProxyMappingList(deviceId: str):
    return Sdwan_mngrClient().createReverseProxyMappingList(deviceId=deviceId)

@register('getStatistics')
def getStatistics(deviceId: str):
    return Sdwan_mngrClient().getStatistics(deviceId=deviceId)

@register('createConnectionSummary')
def createConnectionSummary(deviceId: str):
    return Sdwan_mngrClient().createConnectionSummary(deviceId=deviceId)

@register('createValidDevicesList')
def createValidDevicesList(deviceId: str):
    return Sdwan_mngrClient().createValidDevicesList(deviceId=deviceId)

@register('getValidVManageId')
def getValidVManageId(deviceId: str):
    return Sdwan_mngrClient().getValidVManageId(deviceId=deviceId)

@register('createValidVSmartsList')
def createValidVSmartsList(deviceId: str):
    return Sdwan_mngrClient().createValidVSmartsList(deviceId=deviceId)

@register('createOSPFDatabaseList')
def createOSPFDatabaseList(deviceId: str):
    return Sdwan_mngrClient().createOSPFDatabaseList(deviceId=deviceId)

@register('createOSPFDatabaseExternal')
def createOSPFDatabaseExternal(deviceId: str):
    return Sdwan_mngrClient().createOSPFDatabaseExternal(deviceId=deviceId)

@register('createOSPFDatabaseSummaryList')
def createOSPFDatabaseSummaryList(deviceId: str):
    return Sdwan_mngrClient().createOSPFDatabaseSummaryList(deviceId=deviceId)

@register('createOSPFInterface')
def createOSPFInterface(deviceId: str):
    return Sdwan_mngrClient().createOSPFInterface(deviceId=deviceId)

@register('createOSPFNeighbors')
def createOSPFNeighbors(deviceId: str):
    return Sdwan_mngrClient().createOSPFNeighbors(deviceId=deviceId)

@register('createOSPFProcess')
def createOSPFProcess(deviceId: str):
    return Sdwan_mngrClient().createOSPFProcess(deviceId=deviceId)

@register('createOSPFRoutesList')
def createOSPFRoutesList(deviceId: str):
    return Sdwan_mngrClient().createOSPFRoutesList(deviceId=deviceId)

@register('createOSPFv3Interface')
def createOSPFv3Interface(deviceId: str):
    return Sdwan_mngrClient().createOSPFv3Interface(deviceId=deviceId)

@register('createOSPFv3Neighbors')
def createOSPFv3Neighbors(deviceId: str):
    return Sdwan_mngrClient().createOSPFv3Neighbors(deviceId=deviceId)

@register('createPIMInterfaceList')
def createPIMInterfaceList(deviceId: str):
    return Sdwan_mngrClient().createPIMInterfaceList(deviceId=deviceId)

@register('createPIMNeighborList')
def createPIMNeighborList(deviceId: str):
    return Sdwan_mngrClient().createPIMNeighborList(deviceId=deviceId)

@register('createPIMRpMappingList')
def createPIMRpMappingList(deviceId: str):
    return Sdwan_mngrClient().createPIMRpMappingList(deviceId=deviceId)

@register('createPIMStatisticsList')
def createPIMStatisticsList(deviceId: str):
    return Sdwan_mngrClient().createPIMStatisticsList(deviceId=deviceId)

@register('getDevicePkiTrustpoint')
def getDevicePkiTrustpoint(deviceId: str):
    return Sdwan_mngrClient().getDevicePkiTrustpoint(deviceId=deviceId)

@register('getPolicedInterface')
def getPolicedInterface(deviceId: str):
    return Sdwan_mngrClient().getPolicedInterface(deviceId=deviceId)

@register('createPolicyAccessListAssociations')
def createPolicyAccessListAssociations(deviceId: str):
    return Sdwan_mngrClient().createPolicyAccessListAssociations(deviceId=deviceId)

@register('createPolicyAccessListCounters')
def createPolicyAccessListCounters(deviceId: str):
    return Sdwan_mngrClient().createPolicyAccessListCounters(deviceId=deviceId)

@register('createPolicyAccessListNames')
def createPolicyAccessListNames(deviceId: str):
    return Sdwan_mngrClient().createPolicyAccessListNames(deviceId=deviceId)

@register('createPolicyAccessListPolicers')
def createPolicyAccessListPolicers(deviceId: str):
    return Sdwan_mngrClient().createPolicyAccessListPolicers(deviceId=deviceId)

@register('createPolicyAppRoutePolicyFilter')
def createPolicyAppRoutePolicyFilter(deviceId: str):
    return Sdwan_mngrClient().createPolicyAppRoutePolicyFilter(deviceId=deviceId)

@register('createPolicDataPolicyFilter')
def createPolicDataPolicyFilter(deviceId: str):
    return Sdwan_mngrClient().createPolicDataPolicyFilter(deviceId=deviceId)

@register('createPolicyFilterMemoryUsage')
def createPolicyFilterMemoryUsage(deviceId: str):
    return Sdwan_mngrClient().createPolicyFilterMemoryUsage(deviceId=deviceId)

@register('showVsmartIptoSgtBinding')
def showVsmartIptoSgtBinding(deviceId: str):
    return Sdwan_mngrClient().showVsmartIptoSgtBinding(deviceId=deviceId)

@register('showVsmartIptoUserBinding')
def showVsmartIptoUserBinding(deviceId: str):
    return Sdwan_mngrClient().showVsmartIptoUserBinding(deviceId=deviceId)

@register('createPolicyAccessListAssociationsIpv6')
def createPolicyAccessListAssociationsIpv6(deviceId: str):
    return Sdwan_mngrClient().createPolicyAccessListAssociationsIpv6(deviceId=deviceId)

@register('createPolicyAccessListCountersIpv6')
def createPolicyAccessListCountersIpv6(deviceId: str):
    return Sdwan_mngrClient().createPolicyAccessListCountersIpv6(deviceId=deviceId)

@register('createPolicyAccessListNamesIpv6')
def createPolicyAccessListNamesIpv6(deviceId: str):
    return Sdwan_mngrClient().createPolicyAccessListNamesIpv6(deviceId=deviceId)

@register('createPolicyAccessListPolicersIpv6')
def createPolicyAccessListPolicersIpv6(deviceId: str):
    return Sdwan_mngrClient().createPolicyAccessListPolicersIpv6(deviceId=deviceId)

@register('showVsmartPxGridStatus')
def showVsmartPxGridStatus(deviceId: str):
    return Sdwan_mngrClient().showVsmartPxGridStatus(deviceId=deviceId)

@register('showVsmartPxGridUserSessions')
def showVsmartPxGridUserSessions(deviceId: str):
    return Sdwan_mngrClient().showVsmartPxGridUserSessions(deviceId=deviceId)

@register('createPolicQosMapInfo')
def createPolicQosMapInfo(deviceId: str):
    return Sdwan_mngrClient().createPolicQosMapInfo(deviceId=deviceId)

@register('createPolicQosSchedulerInfo')
def createPolicQosSchedulerInfo(deviceId: str):
    return Sdwan_mngrClient().createPolicQosSchedulerInfo(deviceId=deviceId)

@register('createPolicyRewriteAssociationsInfo')
def createPolicyRewriteAssociationsInfo(deviceId: str):
    return Sdwan_mngrClient().createPolicyRewriteAssociationsInfo(deviceId=deviceId)

@register('showVsmartUserUsergroupBindings')
def showVsmartUserUsergroupBindings(deviceId: str):
    return Sdwan_mngrClient().showVsmartUserUsergroupBindings(deviceId=deviceId)

@register('showSdwanPolicyFromVsmart')
def showSdwanPolicyFromVsmart(deviceId: str):
    return Sdwan_mngrClient().showSdwanPolicyFromVsmart(deviceId=deviceId)

@register('getZoneDropStatistics')
def getZoneDropStatistics(deviceId: str):
    return Sdwan_mngrClient().getZoneDropStatistics(deviceId=deviceId)

@register('getZbfwStatistics')
def getZbfwStatistics(deviceId: str):
    return Sdwan_mngrClient().getZbfwStatistics(deviceId=deviceId)

@register('getZonePairSessions')
def getZonePairSessions(deviceId: str):
    return Sdwan_mngrClient().getZonePairSessions(deviceId=deviceId)

@register('getZonePairs')
def getZonePairs(deviceId: str):
    return Sdwan_mngrClient().getZonePairs(deviceId=deviceId)

@register('getZonePolicyFilters')
def getZonePolicyFilters(deviceId: str):
    return Sdwan_mngrClient().getZonePolicyFilters(deviceId=deviceId)

@register('getPowerConsumption')
def getPowerConsumption(deviceId: str):
    return Sdwan_mngrClient().getPowerConsumption(deviceId=deviceId)

@register('createPPPInterfaceList')
def createPPPInterfaceList(deviceId: str):
    return Sdwan_mngrClient().createPPPInterfaceList(deviceId=deviceId)

@register('createPPPoEInterfaceList')
def createPPPoEInterfaceList(deviceId: str):
    return Sdwan_mngrClient().createPPPoEInterfaceList(deviceId=deviceId)

@register('createPPPoENeighborList')
def createPPPoENeighborList(deviceId: str):
    return Sdwan_mngrClient().createPPPoENeighborList(deviceId=deviceId)

@register('cpustat')
def cpustat(deviceId: str):
    return Sdwan_mngrClient().cpustat(deviceId=deviceId)

@register('memstat')
def memstat(deviceId: str):
    return Sdwan_mngrClient().memstat(deviceId=deviceId)

@register('getSyncQueues')
def getSyncQueues():
    return Sdwan_mngrClient().getSyncQueues()

@register('listReachableDevices')
def listReachableDevices():
    return Sdwan_mngrClient().listReachableDevices()

@register('createRebootHistoryList')
def createRebootHistoryList(deviceId: str):
    return Sdwan_mngrClient().createRebootHistoryList(deviceId=deviceId)

@register('getRebootHistoryDetails')
def getRebootHistoryDetails():
    return Sdwan_mngrClient().getRebootHistoryDetails()

@register('createSyncedRebootHistoryList')
def createSyncedRebootHistoryList(deviceId: str):
    return Sdwan_mngrClient().createSyncedRebootHistoryList(deviceId=deviceId)

@register('getRedundancyGroupAppGroup')
def getRedundancyGroupAppGroup(deviceId: str):
    return Sdwan_mngrClient().getRedundancyGroupAppGroup(deviceId=deviceId)

@register('getRoleBasedCounters')
def getRoleBasedCounters(deviceId: str):
    return Sdwan_mngrClient().getRoleBasedCounters(deviceId=deviceId)

@register('getRoleBasedIpv6Counters')
def getRoleBasedIpv6Counters(deviceId: str):
    return Sdwan_mngrClient().getRoleBasedIpv6Counters(deviceId=deviceId)

@register('getRoleBasedIpv6Permissions')
def getRoleBasedIpv6Permissions(deviceId: str):
    return Sdwan_mngrClient().getRoleBasedIpv6Permissions(deviceId=deviceId)

@register('getRoleBasedPermissions')
def getRoleBasedPermissions(deviceId: str):
    return Sdwan_mngrClient().getRoleBasedPermissions(deviceId=deviceId)

@register('getRoleBasedSgtMap')
def getRoleBasedSgtMap(deviceId: str):
    return Sdwan_mngrClient().getRoleBasedSgtMap(deviceId=deviceId)

@register('getSDWanGlobalDropStatistics')
def getSDWanGlobalDropStatistics(deviceId: str):
    return Sdwan_mngrClient().getSDWanGlobalDropStatistics(deviceId=deviceId)

@register('getSDWanStats')
def getSDWanStats(deviceId: str):
    return Sdwan_mngrClient().getSDWanStats(deviceId=deviceId)

@register('createSessionList')
def createSessionList(deviceId: str):
    return Sdwan_mngrClient().createSessionList(deviceId=deviceId)

@register('getDetail')
def getDetail(deviceId: str, **kwargs):
    return Sdwan_mngrClient().getDetail(deviceId=deviceId, **kwargs)

@register('getDiagnostic')
def getDiagnostic(deviceId: str, **kwargs):
    return Sdwan_mngrClient().getDiagnostic(deviceId=deviceId, **kwargs)

@register('getDiagnosticMeasurementAlarm')
def getDiagnosticMeasurementAlarm(deviceId: str, **kwargs):
    return Sdwan_mngrClient().getDiagnosticMeasurementAlarm(deviceId=deviceId, **kwargs)

@register('getDiagnosticMeasurementValue')
def getDiagnosticMeasurementValue(deviceId: str, **kwargs):
    return Sdwan_mngrClient().getDiagnosticMeasurementValue(deviceId=deviceId, **kwargs)

@register('getSigTunnelList')
def getSigTunnelList(**kwargs):
    return Sdwan_mngrClient().getSigTunnelList(**kwargs)

@register('getSigTunnelTotal')
def getSigTunnelTotal():
    return Sdwan_mngrClient().getSigTunnelTotal()

@register('tunnelDashboard')
def tunnelDashboard():
    return Sdwan_mngrClient().tunnelDashboard()

@register('getSigUmbrellaTunnels')
def getSigUmbrellaTunnels(deviceId: str):
    return Sdwan_mngrClient().getSigUmbrellaTunnels(deviceId=deviceId)

@register('getSigZscalerTunnels')
def getSigZscalerTunnels(deviceId: str):
    return Sdwan_mngrClient().getSigZscalerTunnels(deviceId=deviceId)

@register('createSmuList')
def createSmuList(deviceId: str):
    return Sdwan_mngrClient().createSmuList(deviceId=deviceId)

@register('createSyncedSmuList')
def createSyncedSmuList(deviceId: str):
    return Sdwan_mngrClient().createSyncedSmuList(deviceId=deviceId)

@register('getAAAUcreateSoftwareListsers')
def getAAAUcreateSoftwareListsers(deviceId: str):
    return Sdwan_mngrClient().getAAAUcreateSoftwareListsers(deviceId=deviceId)

@register('createSyncedSoftwareList')
def createSyncedSoftwareList(deviceId: str):
    return Sdwan_mngrClient().createSyncedSoftwareList(deviceId=deviceId)

@register('getSSETunnel')
def getSSETunnel(deviceId: str):
    return Sdwan_mngrClient().getSSETunnel(deviceId=deviceId)

@register('getSslProxyStatistics')
def getSslProxyStatistics(deviceId: str):
    return Sdwan_mngrClient().getSslProxyStatistics(deviceId=deviceId)

@register('getSslProxyStatus')
def getSslProxyStatus(deviceId: str):
    return Sdwan_mngrClient().getSslProxyStatus(deviceId=deviceId)

@register('getStaticRouteTrackerInfo')
def getStaticRouteTrackerInfo(deviceId: str):
    return Sdwan_mngrClient().getStaticRouteTrackerInfo(deviceId=deviceId)

@register('getStatsQueues')
def getStatsQueues():
    return Sdwan_mngrClient().getStatsQueues()

@register('getAllDeviceStatus')
def getAllDeviceStatus():
    return Sdwan_mngrClient().getAllDeviceStatus()

@register('getSxpConnections')
def getSxpConnections(deviceId: str):
    return Sdwan_mngrClient().getSxpConnections(deviceId=deviceId)

@register('listCurrentlySyncingDevices')
def listCurrentlySyncingDevices(groupId: str):
    return Sdwan_mngrClient().listCurrentlySyncingDevices(groupId=groupId)

@register('getDeviceSystemClock')
def getDeviceSystemClock(deviceId: str):
    return Sdwan_mngrClient().getDeviceSystemClock(deviceId=deviceId)

@register('createDeviceInfoList')
def createDeviceInfoList(deviceId: list):
    return Sdwan_mngrClient().createDeviceInfoList(deviceId=deviceId)

@register('createDeviceSystemStatsList')
def createDeviceSystemStatsList(deviceId: str):
    return Sdwan_mngrClient().createDeviceSystemStatsList(deviceId=deviceId)

@register('createDeviceSystemStatusList')
def createDeviceSystemStatusList(deviceId: str):
    return Sdwan_mngrClient().createDeviceSystemStatusList(deviceId=deviceId)

@register('createSyncedDeviceSystemStatusList')
def createSyncedDeviceSystemStatusList(deviceId: str):
    return Sdwan_mngrClient().createSyncedDeviceSystemStatusList(deviceId=deviceId)

@register('getActiveTCPFlows')
def getActiveTCPFlows(deviceId: str):
    return Sdwan_mngrClient().getActiveTCPFlows(deviceId=deviceId)

@register('getExpiredTCPFlows')
def getExpiredTCPFlows(deviceId: str):
    return Sdwan_mngrClient().getExpiredTCPFlows(deviceId=deviceId)

@register('getTCPSummary')
def getTCPSummary(deviceId: str):
    return Sdwan_mngrClient().getTCPSummary(deviceId=deviceId)

@register('getTcpProxyStatistics')
def getTcpProxyStatistics(deviceId: str):
    return Sdwan_mngrClient().getTcpProxyStatistics(deviceId=deviceId)

@register('getTcpProxyStatus')
def getTcpProxyStatus(deviceId: str):
    return Sdwan_mngrClient().getTcpProxyStatus(deviceId=deviceId)

@register('getTiers')
def getTiers():
    return Sdwan_mngrClient().getTiers()

@register('getDeviceTlocStatus')
def getDeviceTlocStatus(**kwargs):
    return Sdwan_mngrClient().getDeviceTlocStatus(**kwargs)

@register('getDeviceTlocUtil')
def getDeviceTlocUtil(**kwargs):
    return Sdwan_mngrClient().getDeviceTlocUtil(**kwargs)

@register('getDeviceTlocUtilDetails')
def getDeviceTlocUtilDetails(**kwargs):
    return Sdwan_mngrClient().getDeviceTlocUtilDetails(**kwargs)

@register('downloadAdminTechFile')
def downloadAdminTechFile(filename: str):
    return Sdwan_mngrClient().downloadAdminTechFile(filename=filename)

@register('getSupportedAdminTechFeatures')
def getSupportedAdminTechFeatures(deviceIP: str, deviceModel: str, personality: str):
    return Sdwan_mngrClient().getSupportedAdminTechFeatures(deviceIP=deviceIP, deviceModel=deviceModel, personality=personality)

@register('listAdminTechs')
def listAdminTechs():
    return Sdwan_mngrClient().listAdminTechs()

@register('getInProgressCount')
def getInProgressCount():
    return Sdwan_mngrClient().getInProgressCount()

@register('getDeviceToolsNetstat')
def getDeviceToolsNetstat(deviceId: str, **kwargs):
    return Sdwan_mngrClient().getDeviceToolsNetstat(deviceId=deviceId, **kwargs)

@register('getDeviceToolsNSlookup')
def getDeviceToolsNSlookup(deviceId: str, dns: str, vpn: str):
    return Sdwan_mngrClient().getDeviceToolsNSlookup(deviceId=deviceId, dns=dns, vpn=vpn)

@register('getRealTimeinfo')
def getRealTimeinfo(deviceId: str):
    return Sdwan_mngrClient().getRealTimeinfo(deviceId=deviceId)

@register('getDeviceToolsSS')
def getDeviceToolsSS(deviceId: str, **kwargs):
    return Sdwan_mngrClient().getDeviceToolsSS(deviceId=deviceId, **kwargs)

@register('getSystemNetfilter')
def getSystemNetfilter(deviceId: str):
    return Sdwan_mngrClient().getSystemNetfilter(deviceId=deviceId)

@register('createTransportConnectionList')
def createTransportConnectionList(deviceId: str):
    return Sdwan_mngrClient().createTransportConnectionList(deviceId=deviceId)

@register('createBfdStatisticsList')
def createBfdStatisticsList(deviceId: str):
    return Sdwan_mngrClient().createBfdStatisticsList(deviceId=deviceId)

@register('createFecStatistics')
def createFecStatistics(deviceId: str):
    return Sdwan_mngrClient().createFecStatistics(deviceId=deviceId)

@register('createGreKeepalivesList')
def createGreKeepalivesList(deviceId: str):
    return Sdwan_mngrClient().createGreKeepalivesList(deviceId=deviceId)

@register('createIpsecStatisticsList')
def createIpsecStatisticsList(deviceId: str):
    return Sdwan_mngrClient().createIpsecStatisticsList(deviceId=deviceId)

@register('createPacketDuplicateStatistics')
def createPacketDuplicateStatistics(deviceId: str):
    return Sdwan_mngrClient().createPacketDuplicateStatistics(deviceId=deviceId)

@register('createStatisticsList')
def createStatisticsList(deviceId: str):
    return Sdwan_mngrClient().createStatisticsList(deviceId=deviceId)

@register('createUcseStats')
def createUcseStats(deviceId: str, **kwargs):
    return Sdwan_mngrClient().createUcseStats(deviceId=deviceId, **kwargs)

@register('getUmbrellaDevReg')
def getUmbrellaDevReg(deviceId: str):
    return Sdwan_mngrClient().getUmbrellaDevReg(deviceId=deviceId)

@register('getUmbrellaDNSCrypt')
def getUmbrellaDNSCrypt(deviceId: str):
    return Sdwan_mngrClient().getUmbrellaDNSCrypt(deviceId=deviceId)

@register('getUmbrellaDpStats')
def getUmbrellaDpStats(deviceId: str):
    return Sdwan_mngrClient().getUmbrellaDpStats(deviceId=deviceId)

@register('getUmbrellaOverview')
def getUmbrellaOverview(deviceId: str):
    return Sdwan_mngrClient().getUmbrellaOverview(deviceId=deviceId)

@register('getUmbrellaConfig')
def getUmbrellaConfig(deviceId: str):
    return Sdwan_mngrClient().getUmbrellaConfig(deviceId=deviceId)

@register('getUnclaimedVedges')
def getUnclaimedVedges(deviceId: str):
    return Sdwan_mngrClient().getUnclaimedVedges(deviceId=deviceId)

@register('getUnconfigured')
def getUnconfigured():
    return Sdwan_mngrClient().getUnconfigured()

@register('listUnreachableDevices')
def listUnreachableDevices(personality: str):
    return Sdwan_mngrClient().listUnreachableDevices(personality=personality)

@register('getUsersFromDevice')
def getUsersFromDevice(deviceId: str):
    return Sdwan_mngrClient().getUsersFromDevice(deviceId=deviceId)

@register('getAllDeviceUsers')
def getAllDeviceUsers(deviceId: str):
    return Sdwan_mngrClient().getAllDeviceUsers(deviceId=deviceId)

@register('getUTDDataplaneConfig')
def getUTDDataplaneConfig(deviceId: str):
    return Sdwan_mngrClient().getUTDDataplaneConfig(deviceId=deviceId)

@register('getUTDDataplaneGlobal')
def getUTDDataplaneGlobal(deviceId: str):
    return Sdwan_mngrClient().getUTDDataplaneGlobal(deviceId=deviceId)

@register('getUTDDataplaneStats')
def getUTDDataplaneStats(deviceId: str):
    return Sdwan_mngrClient().getUTDDataplaneStats(deviceId=deviceId)

@register('getUTDDataplaneStatsSummary')
def getUTDDataplaneStatsSummary(deviceId: str):
    return Sdwan_mngrClient().getUTDDataplaneStatsSummary(deviceId=deviceId)

@register('getUTDEngineInstanceStatus')
def getUTDEngineInstanceStatus(deviceId: str):
    return Sdwan_mngrClient().getUTDEngineInstanceStatus(deviceId=deviceId)

@register('getUTDEngineStatus')
def getUTDEngineStatus(deviceId: str):
    return Sdwan_mngrClient().getUTDEngineStatus(deviceId=deviceId)

@register('getUTDFileAnalysisStatus')
def getUTDFileAnalysisStatus(deviceId: str):
    return Sdwan_mngrClient().getUTDFileAnalysisStatus(deviceId=deviceId)

@register('getUTDFileReputationStatus')
def getUTDFileReputationStatus(deviceId: str):
    return Sdwan_mngrClient().getUTDFileReputationStatus(deviceId=deviceId)

@register('getUTDIpsUpdateStatus')
def getUTDIpsUpdateStatus(deviceId: str):
    return Sdwan_mngrClient().getUTDIpsUpdateStatus(deviceId=deviceId)

@register('getSignatureVersionInfo')
def getSignatureVersionInfo(deviceId: str):
    return Sdwan_mngrClient().getSignatureVersionInfo(deviceId=deviceId)

@register('getUTDUrlfConnectionStatus')
def getUTDUrlfConnectionStatus(deviceId: str):
    return Sdwan_mngrClient().getUTDUrlfConnectionStatus(deviceId=deviceId)

@register('getUTDUrlfUpdateStatus')
def getUTDUrlfUpdateStatus(deviceId: str):
    return Sdwan_mngrClient().getUTDUrlfUpdateStatus(deviceId=deviceId)

@register('getUTDVersionStatus')
def getUTDVersionStatus(deviceId: str):
    return Sdwan_mngrClient().getUTDVersionStatus(deviceId=deviceId)

@register('getCoLineSpecificStats')
def getCoLineSpecificStats(deviceId: str):
    return Sdwan_mngrClient().getCoLineSpecificStats(deviceId=deviceId)

@register('getCoStats')
def getCoStats(deviceId: str):
    return Sdwan_mngrClient().getCoStats(deviceId=deviceId)

@register('getCpeLineSpecificStats')
def getCpeLineSpecificStats(deviceId: str):
    return Sdwan_mngrClient().getCpeLineSpecificStats(deviceId=deviceId)

@register('getCpeStats')
def getCpeStats(deviceId: str):
    return Sdwan_mngrClient().getCpeStats(deviceId=deviceId)

@register('getLineBondingStats')
def getLineBondingStats(deviceId: str):
    return Sdwan_mngrClient().getLineBondingStats(deviceId=deviceId)

@register('getLineSpecificStats')
def getLineSpecificStats(deviceId: str):
    return Sdwan_mngrClient().getLineSpecificStats(deviceId=deviceId)

@register('getVdslInfo')
def getVdslInfo(deviceId: str):
    return Sdwan_mngrClient().getVdslInfo(deviceId=deviceId)

@register('getVedgeInventory')
def getVedgeInventory(**kwargs):
    return Sdwan_mngrClient().getVedgeInventory(**kwargs)

@register('getVedgeInventorySummary')
def getVedgeInventorySummary():
    return Sdwan_mngrClient().getVedgeInventorySummary()

@register('createTeList')
def createTeList(deviceId: str):
    return Sdwan_mngrClient().createTeList(deviceId=deviceId)

@register('createUtdList')
def createUtdList(deviceId: str):
    return Sdwan_mngrClient().createUtdList(deviceId=deviceId)

@register('createWaasList')
def createWaasList(deviceId: str):
    return Sdwan_mngrClient().createWaasList(deviceId=deviceId)

@register('getVbranchVMLifecycleNics')
def getVbranchVMLifecycleNics(deviceId: str):
    return Sdwan_mngrClient().getVbranchVMLifecycleNics(deviceId=deviceId)

@register('getCloudDockVMLifecycleNics')
def getCloudDockVMLifecycleNics(userGroup: str):
    return Sdwan_mngrClient().getCloudDockVMLifecycleNics(userGroup=userGroup)

@register('getVbranchVMLifecycle')
def getVbranchVMLifecycle(deviceId: str):
    return Sdwan_mngrClient().getVbranchVMLifecycle(deviceId=deviceId)

@register('getVMLifeCycleState')
def getVMLifeCycleState(deviceId: str):
    return Sdwan_mngrClient().getVMLifeCycleState(deviceId=deviceId)

@register('getVManageSystemIP')
def getVManageSystemIP():
    return Sdwan_mngrClient().getVManageSystemIP()

@register('getDspActive')
def getDspActive(deviceId: str):
    return Sdwan_mngrClient().getDspActive(deviceId=deviceId)

@register('getPhoneInfo')
def getPhoneInfo(deviceId: str):
    return Sdwan_mngrClient().getPhoneInfo(deviceId=deviceId)

@register('getDSPFarmProfiles')
def getDSPFarmProfiles(deviceId: str):
    return Sdwan_mngrClient().getDSPFarmProfiles(deviceId=deviceId)

@register('getSccpCcmGroups')
def getSccpCcmGroups(deviceId: str):
    return Sdwan_mngrClient().getSccpCcmGroups(deviceId=deviceId)

@register('getSccpConnections')
def getSccpConnections(deviceId: str):
    return Sdwan_mngrClient().getSccpConnections(deviceId=deviceId)

@register('getVoiceCalls')
def getVoiceCalls(deviceId: str):
    return Sdwan_mngrClient().getVoiceCalls(deviceId=deviceId)

@register('getVoipCalls')
def getVoipCalls(deviceId: str):
    return Sdwan_mngrClient().getVoipCalls(deviceId=deviceId)

@register('getT1e1IsdnStatus')
def getT1e1IsdnStatus(deviceId: str):
    return Sdwan_mngrClient().getT1e1IsdnStatus(deviceId=deviceId)

@register('getControllerT1e1InfoCurrent15MinStats')
def getControllerT1e1InfoCurrent15MinStats(deviceId: str):
    return Sdwan_mngrClient().getControllerT1e1InfoCurrent15MinStats(deviceId=deviceId)

@register('getControllerT1e1InfoTotalStats')
def getControllerT1e1InfoTotalStats(deviceId: str):
    return Sdwan_mngrClient().getControllerT1e1InfoTotalStats(deviceId=deviceId)

@register('getVPNInstances')
def getVPNInstances(deviceId: str):
    return Sdwan_mngrClient().getVPNInstances(deviceId=deviceId)

@register('getVRRPInterface')
def getVRRPInterface(deviceId: str):
    return Sdwan_mngrClient().getVRRPInterface(deviceId=deviceId)

@register('getWirelessClients')
def getWirelessClients(deviceId: str):
    return Sdwan_mngrClient().getWirelessClients(deviceId=deviceId)

@register('getWirelessRadios')
def getWirelessRadios(deviceId: str):
    return Sdwan_mngrClient().getWirelessRadios(deviceId=deviceId)

@register('getWirelessSsid')
def getWirelessSsid(deviceId: str):
    return Sdwan_mngrClient().getWirelessSsid(deviceId=deviceId)

@register('getWLANClients')
def getWLANClients(deviceId: str):
    return Sdwan_mngrClient().getWLANClients(deviceId=deviceId)

@register('getWLANInterfaces')
def getWLANInterfaces(deviceId: str):
    return Sdwan_mngrClient().getWLANInterfaces(deviceId=deviceId)

@register('getWLANRadios')
def getWLANRadios(deviceId: str):
    return Sdwan_mngrClient().getWLANRadios(deviceId=deviceId)

@register('getWLANRadius')
def getWLANRadius(deviceId: str):
    return Sdwan_mngrClient().getWLANRadius(deviceId=deviceId)

@register('getClusterInfo')
def getClusterInfo():
    return Sdwan_mngrClient().getClusterInfo()

@register('getConfigDBRestoreStatus')
def getConfigDBRestoreStatus():
    return Sdwan_mngrClient().getConfigDBRestoreStatus()

@register('getDetails')
def getDetails():
    return Sdwan_mngrClient().getDetails()

@register('getDisasterRecoveryStatus')
def getDisasterRecoveryStatus():
    return Sdwan_mngrClient().getDisasterRecoveryStatus()

@register('getHistory')
def getHistory():
    return Sdwan_mngrClient().getHistory()

@register('getLocalHistory')
def getLocalHistory():
    return Sdwan_mngrClient().getLocalHistory()

@register('getLocalDataCenterState')
def getLocalDataCenterState():
    return Sdwan_mngrClient().getLocalDataCenterState()

@register('getRemoteDCMembersState')
def getRemoteDCMembersState():
    return Sdwan_mngrClient().getRemoteDCMembersState()

@register('getRemoteDataCenterState')
def getRemoteDataCenterState():
    return Sdwan_mngrClient().getRemoteDataCenterState()

@register('getRemoteDataCenterVersion')
def getRemoteDataCenterVersion():
    return Sdwan_mngrClient().getRemoteDataCenterVersion()

@register('getDisasterRecoveryLocalReplicationSchedule')
def getDisasterRecoveryLocalReplicationSchedule():
    return Sdwan_mngrClient().getDisasterRecoveryLocalReplicationSchedule()

@register('getdrStatus')
def getdrStatus():
    return Sdwan_mngrClient().getdrStatus()

@register('get')
def get():
    return Sdwan_mngrClient().get()

@register('listEntityOwnershipInfo')
def listEntityOwnershipInfo():
    return Sdwan_mngrClient().listEntityOwnershipInfo()

@register('entityOwnershipInfo')
def entityOwnershipInfo():
    return Sdwan_mngrClient().entityOwnershipInfo()

@register('getEvents')
def getEvents(**kwargs):
    return Sdwan_mngrClient().getEvents(**kwargs)

@register('getAggregationData_1')
def getAggregationData_1(query: str, **kwargs):
    return Sdwan_mngrClient().getAggregationData_1(query=query, **kwargs)

@register('getComponentsAsKeyValue')
def getComponentsAsKeyValue():
    return Sdwan_mngrClient().getComponentsAsKeyValue()

@register('getDocCount_2')
def getDocCount_2(query: str, **kwargs):
    return Sdwan_mngrClient().getDocCount_2(query=query, **kwargs)

@register('enableEventsFromFile')
def enableEventsFromFile():
    return Sdwan_mngrClient().enableEventsFromFile()

@register('getEventNamesByComponent')
def getEventNamesByComponent(query: str):
    return Sdwan_mngrClient().getEventNamesByComponent(query=query)

@register('getListenersInfo')
def getListenersInfo():
    return Sdwan_mngrClient().getListenersInfo()

@register('getPage_1')
def getPage_1(**kwargs):
    return Sdwan_mngrClient().getPage_1(**kwargs)

@register('getQueryFields')
def getQueryFields():
    return Sdwan_mngrClient().getQueryFields()

@register('createEventsQueryConfig')
def createEventsQueryConfig():
    return Sdwan_mngrClient().createEventsQueryConfig()

@register('getBySeverities')
def getBySeverities(severity-level: list, **kwargs):
    return Sdwan_mngrClient().getBySeverities(severity-level=severity-level, **kwargs)

@register('getSeverityHistogram')
def getSeverityHistogram(deviceId: list, **kwargs):
    return Sdwan_mngrClient().getSeverityHistogram(deviceId=deviceId, **kwargs)

@register('getEventTypesAsKeyValue')
def getEventTypesAsKeyValue():
    return Sdwan_mngrClient().getEventTypesAsKeyValue()

@register('getDeviceCertificate')
def getDeviceCertificate(deviceId: str):
    return Sdwan_mngrClient().getDeviceCertificate(deviceId=deviceId)

@register('getDeviceCsr')
def getDeviceCsr(deviceId: str):
    return Sdwan_mngrClient().getDeviceCsr(deviceId=deviceId)

@register('getFeatureCaState')
def getFeatureCaState():
    return Sdwan_mngrClient().getFeatureCaState()

@register('requesDNSSecActions')
def requesDNSSecActions(action: str):
    return Sdwan_mngrClient().requesDNSSecActions(action=action)

@register('getDNSSecStatus')
def getDNSSecStatus():
    return Sdwan_mngrClient().getDNSSecStatus()

@register('requestWazuhActions')
def requestWazuhActions(**kwargs):
    return Sdwan_mngrClient().requestWazuhActions(**kwargs)

@register('getWazuhAgentStatus')
def getWazuhAgentStatus():
    return Sdwan_mngrClient().getWazuhAgentStatus()

@register('listDeviceGroupList')
def listDeviceGroupList():
    return Sdwan_mngrClient().listDeviceGroupList()

@register('listDeviceGroups')
def listDeviceGroups(**kwargs):
    return Sdwan_mngrClient().listDeviceGroups(**kwargs)

@register('listGroupDevices')
def listGroupDevices(**kwargs):
    return Sdwan_mngrClient().listGroupDevices(**kwargs)

@register('listGroupDevicesForMap')
def listGroupDevicesForMap(**kwargs):
    return Sdwan_mngrClient().listGroupDevicesForMap(**kwargs)

@register('listGroupLinksForMap')
def listGroupLinksForMap(**kwargs):
    return Sdwan_mngrClient().listGroupLinksForMap(**kwargs)

@register('getDevicesHealth')
def getDevicesHealth(**kwargs):
    return Sdwan_mngrClient().getDevicesHealth(**kwargs)

@register('getDevicesHealthOverview')
def getDevicesHealthOverview(**kwargs):
    return Sdwan_mngrClient().getDevicesHealthOverview(**kwargs)

@register('fetchDeviceDetails')
def fetchDeviceDetails():
    return Sdwan_mngrClient().fetchDeviceDetails()

@register('InstallDeviceDetails')
def InstallDeviceDetails():
    return Sdwan_mngrClient().InstallDeviceDetails()

@register('fetchSAVAAccounts')
def fetchSAVAAccounts(**kwargs):
    return Sdwan_mngrClient().fetchSAVAAccounts(**kwargs)

@register('testbedMode')
def testbedMode():
    return Sdwan_mngrClient().testbedMode()

@register('connect_1')
def connect_1():
    return Sdwan_mngrClient().connect_1()

@register('getIseServerCredentials')
def getIseServerCredentials():
    return Sdwan_mngrClient().getIseServerCredentials()

@register('getPxGridAccount')
def getPxGridAccount():
    return Sdwan_mngrClient().getPxGridAccount()

@register('getPxgridCert')
def getPxgridCert():
    return Sdwan_mngrClient().getPxgridCert()

@register('getSupportedLocales')
def getSupportedLocales():
    return Sdwan_mngrClient().getSupportedLocales()

@register('getCategory')
def getCategory():
    return Sdwan_mngrClient().getCategory()

@register('getvManageResourceUtilization')
def getvManageResourceUtilization():
    return Sdwan_mngrClient().getvManageResourceUtilization()

@register('retrieveMDPAttachedDevices')
def retrieveMDPAttachedDevices(nmsId: str):
    return Sdwan_mngrClient().retrieveMDPAttachedDevices(nmsId=nmsId)

@register('retrieveMDPSupportedDevices')
def retrieveMDPSupportedDevices(nmsId: str):
    return Sdwan_mngrClient().retrieveMDPSupportedDevices(nmsId=nmsId)

@register('disconnectFromMDP')
def disconnectFromMDP(nmsId: str):
    return Sdwan_mngrClient().disconnectFromMDP(nmsId=nmsId)

@register('getMDPOnboardingStatus')
def getMDPOnboardingStatus():
    return Sdwan_mngrClient().getMDPOnboardingStatus()

@register('retrieveMDPConfigObject')
def retrieveMDPConfigObject(deviceId: str):
    return Sdwan_mngrClient().retrieveMDPConfigObject(deviceId=deviceId)

@register('retrieveMDPPolicies')
def retrieveMDPPolicies(nmsId: str):
    return Sdwan_mngrClient().retrieveMDPPolicies(nmsId=nmsId)

@register('createDeviceVmanageConnectionList')
def createDeviceVmanageConnectionList():
    return Sdwan_mngrClient().createDeviceVmanageConnectionList()

@register('getCloudConnectorDomainAppRules')
def getCloudConnectorDomainAppRules():
    return Sdwan_mngrClient().getCloudConnectorDomainAppRules()

@register('getCloudConnectorIpAddressAppRules')
def getCloudConnectorIpAddressAppRules():
    return Sdwan_mngrClient().getCloudConnectorIpAddressAppRules()

@register('getWebexAppData')
def getWebexAppData():
    return Sdwan_mngrClient().getWebexAppData()

@register('getMSLADevices_1')
def getMSLADevices_1(**kwargs):
    return Sdwan_mngrClient().getMSLADevices_1(**kwargs)

@register('getLicenseByUuid_1')
def getLicenseByUuid_1(uuid: str):
    return Sdwan_mngrClient().getLicenseByUuid_1(uuid=uuid)

@register('getMslaLicenses')
def getMslaLicenses(**kwargs):
    return Sdwan_mngrClient().getMslaLicenses(**kwargs)

@register('getLicensesCompliance')
def getLicensesCompliance():
    return Sdwan_mngrClient().getLicensesCompliance()

@register('getDeviceDetailsForDashboard')
def getDeviceDetailsForDashboard():
    return Sdwan_mngrClient().getDeviceDetailsForDashboard()

@register('getLicenseDistributionDetails')
def getLicenseDistributionDetails():
    return Sdwan_mngrClient().getLicenseDistributionDetails()

@register('getPackagingDistributionDetails')
def getPackagingDistributionDetails():
    return Sdwan_mngrClient().getPackagingDistributionDetails()

@register('getAllTemplate')
def getAllTemplate():
    return Sdwan_mngrClient().getAllTemplate()

@register('getSubscriptions')
def getSubscriptions(**kwargs):
    return Sdwan_mngrClient().getSubscriptions(**kwargs)

@register('getAllCloudAccounts')
def getAllCloudAccounts(**kwargs):
    return Sdwan_mngrClient().getAllCloudAccounts(**kwargs)

@register('getEdgeAccounts')
def getEdgeAccounts(**kwargs):
    return Sdwan_mngrClient().getEdgeAccounts(**kwargs)

@register('getEdgeAccountDetails')
def getEdgeAccountDetails(accountId: str):
    return Sdwan_mngrClient().getEdgeAccountDetails(accountId=accountId)

@register('getCloudAccountDetails')
def getCloudAccountDetails(accountId: str):
    return Sdwan_mngrClient().getCloudAccountDetails(accountId=accountId)

@register('auditDryRun')
def auditDryRun(cloudType: str, **kwargs):
    return Sdwan_mngrClient().auditDryRun(cloudType=cloudType, **kwargs)

@register('getEdgeBillingAccounts')
def getEdgeBillingAccounts(edgeAccountId: str, edgeType: str, **kwargs):
    return Sdwan_mngrClient().getEdgeBillingAccounts(edgeAccountId=edgeAccountId, edgeType=edgeType, **kwargs)

@register('getCloudRoutersAndAttachments')
def getCloudRoutersAndAttachments(**kwargs):
    return Sdwan_mngrClient().getCloudRoutersAndAttachments(**kwargs)

@register('getCgws')
def getCgws(**kwargs):
    return Sdwan_mngrClient().getCgws(**kwargs)

@register('getNvaSecurityRules')
def getNvaSecurityRules(cloudGatewayName: str):
    return Sdwan_mngrClient().getNvaSecurityRules(cloudGatewayName=cloudGatewayName)

@register('getAzureNetworkVirtualAppliances')
def getAzureNetworkVirtualAppliances(accountId: str, cloudType: str, region: str, resourceGroupName: str, resourceGroupSource: str, vhubName: str, vhubSource: str):
    return Sdwan_mngrClient().getAzureNetworkVirtualAppliances(accountId=accountId, cloudType=cloudType, region=region, resourceGroupName=resourceGroupName, resourceGroupSource=resourceGroupSource, vhubName=vhubName, vhubSource=vhubSource)

@register('getAzureNvaSkuResources')
def getAzureNvaSkuResources(cloudType: str):
    return Sdwan_mngrClient().getAzureNvaSkuResources(cloudType=cloudType)

@register('getCgwOrgResources')
def getCgwOrgResources(cloudGatewayName: str):
    return Sdwan_mngrClient().getCgwOrgResources(cloudGatewayName=cloudGatewayName)

@register('getAzureResourceGroups')
def getAzureResourceGroups(accountId: str, cloudType: str):
    return Sdwan_mngrClient().getAzureResourceGroups(accountId=accountId, cloudType=cloudType)

@register('getAzureVirtualHubs')
def getAzureVirtualHubs(accountId: str, cloudType: str, region: str, resourceGroupName: str, resourceGroupSource: str, vwanName: str, vwanSource: str):
    return Sdwan_mngrClient().getAzureVirtualHubs(accountId=accountId, cloudType=cloudType, region=region, resourceGroupName=resourceGroupName, resourceGroupSource=resourceGroupSource, vwanName=vwanName, vwanSource=vwanSource)

@register('getAzureVirtualVnetsAttached')
def getAzureVirtualVnetsAttached(cloudGatewayName: str, cloudType: str):
    return Sdwan_mngrClient().getAzureVirtualVnetsAttached(cloudGatewayName=cloudGatewayName, cloudType=cloudType)

@register('getAzureVpnGateways')
def getAzureVpnGateways(accountId: str, cloudType: str, region: str, resourceGroupName: str, resourceGroupSource: str, vhubName: str, vhubSource: str):
    return Sdwan_mngrClient().getAzureVpnGateways(accountId=accountId, cloudType=cloudType, region=region, resourceGroupName=resourceGroupName, resourceGroupSource=resourceGroupSource, vhubName=vhubName, vhubSource=vhubSource)

@register('getAzureVirtualWans')
def getAzureVirtualWans(accountId: str, cloudType: str, resourceGroupName: str, resourceGroupSource: str):
    return Sdwan_mngrClient().getAzureVirtualWans(accountId=accountId, cloudType=cloudType, resourceGroupName=resourceGroupName, resourceGroupSource=resourceGroupSource)

@register('getCgwDetails')
def getCgwDetails(cloudGatewayName: str):
    return Sdwan_mngrClient().getCgwDetails(cloudGatewayName=cloudGatewayName)

@register('getCgwAttachedSites')
def getCgwAttachedSites(cloudGatewayName: str, **kwargs):
    return Sdwan_mngrClient().getCgwAttachedSites(cloudGatewayName=cloudGatewayName, **kwargs)

@register('getAvailableDevicesOrByCGId')
def getAvailableDevicesOrByCGId(cloudType: str, **kwargs):
    return Sdwan_mngrClient().getAvailableDevicesOrByCGId(cloudType=cloudType, **kwargs)

@register('getCloudGateways')
def getCloudGateways(cloudType: str):
    return Sdwan_mngrClient().getCloudGateways(cloudType=cloudType)

@register('getCgwCustomSettingDetails')
def getCgwCustomSettingDetails(cloudGatewayName: str):
    return Sdwan_mngrClient().getCgwCustomSettingDetails(cloudGatewayName=cloudGatewayName)

@register('getCgwTypes')
def getCgwTypes(**kwargs):
    return Sdwan_mngrClient().getCgwTypes(**kwargs)

@register('getCloudConnectedSites_1')
def getCloudConnectedSites_1(edgeType: str, **kwargs):
    return Sdwan_mngrClient().getCloudConnectedSites_1(edgeType=edgeType, **kwargs)

@register('getCloudConnectedSites')
def getCloudConnectedSites(cloudType: str, **kwargs):
    return Sdwan_mngrClient().getCloudConnectedSites(cloudType=cloudType, **kwargs)

@register('getEdgeConnectivityDetails')
def getEdgeConnectivityDetails(**kwargs):
    return Sdwan_mngrClient().getEdgeConnectivityDetails(**kwargs)

@register('getEdgeConnectivityDetailByName')
def getEdgeConnectivityDetailByName(connectivityName: str):
    return Sdwan_mngrClient().getEdgeConnectivityDetailByName(connectivityName=connectivityName)

@register('getConnectivityGateways')
def getConnectivityGateways(**kwargs):
    return Sdwan_mngrClient().getConnectivityGateways(**kwargs)

@register('getConnectivityGatewayCreationOptions')
def getConnectivityGatewayCreationOptions(**kwargs):
    return Sdwan_mngrClient().getConnectivityGatewayCreationOptions(**kwargs)

@register('getCwanCoreNetworkPolicy')
def getCwanCoreNetworkPolicy():
    return Sdwan_mngrClient().getCwanCoreNetworkPolicy()

@register('getDashboardEdgeInfo')
def getDashboardEdgeInfo():
    return Sdwan_mngrClient().getDashboardEdgeInfo()

@register('getWanDevices')
def getWanDevices():
    return Sdwan_mngrClient().getWanDevices()

@register('getDeviceLinks')
def getDeviceLinks(**kwargs):
    return Sdwan_mngrClient().getDeviceLinks(**kwargs)

@register('getDlPortSpeed')
def getDlPortSpeed(edgeType: str):
    return Sdwan_mngrClient().getDlPortSpeed(edgeType=edgeType)

@register('getCloudDevices_1')
def getCloudDevices_1(edgeType: str, **kwargs):
    return Sdwan_mngrClient().getCloudDevices_1(edgeType=edgeType, **kwargs)

@register('getCloudDevices')
def getCloudDevices(cloudType: str, **kwargs):
    return Sdwan_mngrClient().getCloudDevices(cloudType=cloudType, **kwargs)

@register('getEdgeWanDevices')
def getEdgeWanDevices(edgeType: str):
    return Sdwan_mngrClient().getEdgeWanDevices(edgeType=edgeType)

@register('getIcgws')
def getIcgws(**kwargs):
    return Sdwan_mngrClient().getIcgws(**kwargs)

@register('getIcgwCustomSettingDetails')
def getIcgwCustomSettingDetails(edgeGatewayName: str):
    return Sdwan_mngrClient().getIcgwCustomSettingDetails(edgeGatewayName=edgeGatewayName)

@register('getIcgwTypes')
def getIcgwTypes(**kwargs):
    return Sdwan_mngrClient().getIcgwTypes(**kwargs)

@register('getIcgwDetails')
def getIcgwDetails(edgeGatewayName: str):
    return Sdwan_mngrClient().getIcgwDetails(edgeGatewayName=edgeGatewayName)

@register('getEdgeGateways')
def getEdgeGateways(edgeType: str):
    return Sdwan_mngrClient().getEdgeGateways(edgeType=edgeType)

@register('getHostVpcs')
def getHostVpcs(cloudType: str, **kwargs):
    return Sdwan_mngrClient().getHostVpcs(cloudType=cloudType, **kwargs)

@register('getVpcTags')
def getVpcTags(**kwargs):
    return Sdwan_mngrClient().getVpcTags(**kwargs)

@register('getSupportedEdgeImageNames')
def getSupportedEdgeImageNames(**kwargs):
    return Sdwan_mngrClient().getSupportedEdgeImageNames(**kwargs)

@register('getSupportedInstanceSize')
def getSupportedInstanceSize(cloudType: str, **kwargs):
    return Sdwan_mngrClient().getSupportedInstanceSize(cloudType=cloudType, **kwargs)

@register('getSupportedEdgeInstanceSize')
def getSupportedEdgeInstanceSize(**kwargs):
    return Sdwan_mngrClient().getSupportedEdgeInstanceSize(**kwargs)

@register('getInterconnectAccounts')
def getInterconnectAccounts(**kwargs):
    return Sdwan_mngrClient().getInterconnectAccounts(**kwargs)

@register('getInterconnectAccount')
def getInterconnectAccount(interconnect-account-id: str):
    return Sdwan_mngrClient().getInterconnectAccount(interconnect-account-id=interconnect-account-id)

@register('getAuditReport')
def getAuditReport(interconnect-type: str, **kwargs):
    return Sdwan_mngrClient().getAuditReport(interconnect-type=interconnect-type, **kwargs)

@register('getGoogleCloudRouterAndAttachments')
def getGoogleCloudRouterAndAttachments(cloud-account-id: str, cloud-type: str, **kwargs):
    return Sdwan_mngrClient().getGoogleCloudRouterAndAttachments(cloud-account-id=cloud-account-id, cloud-type=cloud-type, **kwargs)

@register('getAwsTransitGateways')
def getAwsTransitGateways(cloud-account-id: str, cloud-type: str, **kwargs):
    return Sdwan_mngrClient().getAwsTransitGateways(cloud-account-id=cloud-account-id, cloud-type=cloud-type, **kwargs)

@register('getAzVirtualHubs')
def getAzVirtualHubs(cloud-account-id: str, cloud-type: str, **kwargs):
    return Sdwan_mngrClient().getAzVirtualHubs(cloud-account-id=cloud-account-id, cloud-type=cloud-type, **kwargs)

@register('getAzVirtualWans')
def getAzVirtualWans(cloud-account-id: str, cloud-type: str, resource-group: str, **kwargs):
    return Sdwan_mngrClient().getAzVirtualWans(cloud-account-id=cloud-account-id, cloud-type=cloud-type, resource-group=resource-group, **kwargs)

@register('getCloudConnectivityGateways')
def getCloudConnectivityGateways(cloud-account-id: str, cloud-type: str, **kwargs):
    return Sdwan_mngrClient().getCloudConnectivityGateways(cloud-account-id=cloud-account-id, cloud-type=cloud-type, **kwargs)

@register('getCloudConnectivityGatewayCreateOptions')
def getCloudConnectivityGatewayCreateOptions(cloud-account-id: str, cloud-type: str, **kwargs):
    return Sdwan_mngrClient().getCloudConnectivityGatewayCreateOptions(cloud-account-id=cloud-account-id, cloud-type=cloud-type, **kwargs)

@register('getInterconnectColors')
def getInterconnectColors(tunnel-type: str):
    return Sdwan_mngrClient().getInterconnectColors(tunnel-type=tunnel-type)

@register('getInterconnectOnRampGatewayConnections')
def getInterconnectOnRampGatewayConnections(**kwargs):
    return Sdwan_mngrClient().getInterconnectOnRampGatewayConnections(**kwargs)

@register('getInterconnectOnRampGatewayConnection')
def getInterconnectOnRampGatewayConnection(connection-name: str):
    return Sdwan_mngrClient().getInterconnectOnRampGatewayConnection(connection-name=connection-name)

@register('getInterconnectMappingTags')
def getInterconnectMappingTags(cloud-account-id: str, cloud-type: str, **kwargs):
    return Sdwan_mngrClient().getInterconnectMappingTags(cloud-account-id=cloud-account-id, cloud-type=cloud-type, **kwargs)

@register('getInterconnectDeviceLinks')
def getInterconnectDeviceLinks(**kwargs):
    return Sdwan_mngrClient().getInterconnectDeviceLinks(**kwargs)

@register('getInterconnectDeviceLink')
def getInterconnectDeviceLink(device-link-name: str):
    return Sdwan_mngrClient().getInterconnectDeviceLink(device-link-name=device-link-name)

@register('getInterconnectCrossConnections')
def getInterconnectCrossConnections(**kwargs):
    return Sdwan_mngrClient().getInterconnectCrossConnections(**kwargs)

@register('getInterconnectCrossConnection')
def getInterconnectCrossConnection(connection-name: str):
    return Sdwan_mngrClient().getInterconnectCrossConnection(connection-name=connection-name)

@register('getInterconnectVirtualNetworkConnections')
def getInterconnectVirtualNetworkConnections(**kwargs):
    return Sdwan_mngrClient().getInterconnectVirtualNetworkConnections(**kwargs)

@register('getInterconnectVirtualNetworkConnection')
def getInterconnectVirtualNetworkConnection(connection-name: str):
    return Sdwan_mngrClient().getInterconnectVirtualNetworkConnection(connection-name=connection-name)

@register('getInterconnectDashboard')
def getInterconnectDashboard():
    return Sdwan_mngrClient().getInterconnectDashboard()

@register('getInterconnectLicenses')
def getInterconnectLicenses(interconnect-account-id: str, interconnect-type: str, **kwargs):
    return Sdwan_mngrClient().getInterconnectLicenses(interconnect-account-id=interconnect-account-id, interconnect-type=interconnect-type, **kwargs)

@register('getInterconnectGateways')
def getInterconnectGateways(**kwargs):
    return Sdwan_mngrClient().getInterconnectGateways(**kwargs)

@register('getInterconnectGatewayImageNames')
def getInterconnectGatewayImageNames(interconnect-type: str):
    return Sdwan_mngrClient().getInterconnectGatewayImageNames(interconnect-type=interconnect-type)

@register('getInterconnectGatewayInstanceSizes')
def getInterconnectGatewayInstanceSizes(interconnect-type: str):
    return Sdwan_mngrClient().getInterconnectGatewayInstanceSizes(interconnect-type=interconnect-type)

@register('getInterconnetGatewayTypes')
def getInterconnetGatewayTypes(interconnect-type: str):
    return Sdwan_mngrClient().getInterconnetGatewayTypes(interconnect-type=interconnect-type)

@register('getInterconnectGateway')
def getInterconnectGateway(interconnect-gateway-name: str):
    return Sdwan_mngrClient().getInterconnectGateway(interconnect-gateway-name=interconnect-gateway-name)

@register('getInterconnectGatewayCustomSettings')
def getInterconnectGatewayCustomSettings(interconnect-account-id: str, interconnect-gateway-name: str):
    return Sdwan_mngrClient().getInterconnectGatewayCustomSettings(interconnect-account-id=interconnect-account-id, interconnect-gateway-name=interconnect-gateway-name)

@register('getInterconnectIpTransit')
def getInterconnectIpTransit(interconnect-service-type: str, interconnect-type: str):
    return Sdwan_mngrClient().getInterconnectIpTransit(interconnect-service-type=interconnect-service-type, interconnect-type=interconnect-type)

@register('getInterconnectServiceSwPkg')
def getInterconnectServiceSwPkg(interconnect-account-id: str, interconnect-provider-name: str, interconnect-service-type: str, interconnect-service-vendor-name: str, **kwargs):
    return Sdwan_mngrClient().getInterconnectServiceSwPkg(interconnect-account-id=interconnect-account-id, interconnect-provider-name=interconnect-provider-name, interconnect-service-type=interconnect-service-type, interconnect-service-vendor-name=interconnect-service-vendor-name, **kwargs)

@register('getInterconnectServices')
def getInterconnectServices(interconnect-service-type: str, interconnect-service-vendor-name: str, interconnect-type: str):
    return Sdwan_mngrClient().getInterconnectServices(interconnect-service-type=interconnect-service-type, interconnect-service-vendor-name=interconnect-service-vendor-name, interconnect-type=interconnect-type)

@register('getInterconnectGlobalSettings')
def getInterconnectGlobalSettings(interconnect-type: str):
    return Sdwan_mngrClient().getInterconnectGlobalSettings(interconnect-type=interconnect-type)

@register('getInterconnectSshKeys')
def getInterconnectSshKeys(interconnect-account-id: str, interconnect-provider-name: str):
    return Sdwan_mngrClient().getInterconnectSshKeys(interconnect-account-id=interconnect-account-id, interconnect-provider-name=interconnect-provider-name)

@register('getInterconnectTypes')
def getInterconnectTypes():
    return Sdwan_mngrClient().getInterconnectTypes()

@register('getAllInterconnectWidgets')
def getAllInterconnectWidgets():
    return Sdwan_mngrClient().getAllInterconnectWidgets()

@register('getInterconnectBillingAccounts')
def getInterconnectBillingAccounts(interconnect-account-id: str, interconnect-type: str, **kwargs):
    return Sdwan_mngrClient().getInterconnectBillingAccounts(interconnect-account-id=interconnect-account-id, interconnect-type=interconnect-type, **kwargs)

@register('getInterconnectPartnerPorts')
def getInterconnectPartnerPorts(cloud-type: str, interconnect-account-id: str, interconnect-type: str, **kwargs):
    return Sdwan_mngrClient().getInterconnectPartnerPorts(cloud-type=cloud-type, interconnect-account-id=interconnect-account-id, interconnect-type=interconnect-type, **kwargs)

@register('getInterconnectPortSpeeds')
def getInterconnectPortSpeeds(connection-type: str, interconnect-account-id: str, interconnect-type: str, **kwargs):
    return Sdwan_mngrClient().getInterconnectPortSpeeds(connection-type=connection-type, interconnect-account-id=interconnect-account-id, interconnect-type=interconnect-type, **kwargs)

@register('getInterconnectLocationInfo')
def getInterconnectLocationInfo(interconnect-account-id: str, interconnect-type: str, **kwargs):
    return Sdwan_mngrClient().getInterconnectLocationInfo(interconnect-account-id=interconnect-account-id, interconnect-type=interconnect-type, **kwargs)

@register('getInterconnectConfigGroupTopology')
def getInterconnectConfigGroupTopology(config-group-id: str, interconnect-type: str):
    return Sdwan_mngrClient().getInterconnectConfigGroupTopology(config-group-id=config-group-id, interconnect-type=interconnect-type)

@register('getInterconnectDeviceLinkPortSpeeds')
def getInterconnectDeviceLinkPortSpeeds(interconnect-type: str):
    return Sdwan_mngrClient().getInterconnectDeviceLinkPortSpeeds(interconnect-type=interconnect-type)

@register('getAvailableDevicesOrByCGId_1')
def getAvailableDevicesOrByCGId_1(interconnect-type: str, **kwargs):
    return Sdwan_mngrClient().getAvailableDevicesOrByCGId_1(interconnect-type=interconnect-type, **kwargs)

@register('getInterconnectGatewayDevices')
def getInterconnectGatewayDevices(interconnect-type: str):
    return Sdwan_mngrClient().getInterconnectGatewayDevices(interconnect-type=interconnect-type)

@register('getMonitoringInterconnectConnectedSites')
def getMonitoringInterconnectConnectedSites(interconnect-type: str, **kwargs):
    return Sdwan_mngrClient().getMonitoringInterconnectConnectedSites(interconnect-type=interconnect-type, **kwargs)

@register('getMonitoringInterconnectDevices')
def getMonitoringInterconnectDevices(interconnect-type: str, **kwargs):
    return Sdwan_mngrClient().getMonitoringInterconnectDevices(interconnect-type=interconnect-type, **kwargs)

@register('getMonitoringInterconnectGateways')
def getMonitoringInterconnectGateways(interconnect-type: str):
    return Sdwan_mngrClient().getMonitoringInterconnectGateways(interconnect-type=interconnect-type)

@register('getInterconnectWidget')
def getInterconnectWidget(interconnect-type: str):
    return Sdwan_mngrClient().getInterconnectWidget(interconnect-type=interconnect-type)

@register('getWanInterfaceColors')
def getWanInterfaceColors():
    return Sdwan_mngrClient().getWanInterfaceColors()

@register('getLicenses')
def getLicenses(**kwargs):
    return Sdwan_mngrClient().getLicenses(**kwargs)

@register('getEdgeLocationsInfo')
def getEdgeLocationsInfo(edgeType: str, **kwargs):
    return Sdwan_mngrClient().getEdgeLocationsInfo(edgeType=edgeType, **kwargs)

@register('getSupportedLoopbackCgwColors')
def getSupportedLoopbackCgwColors():
    return Sdwan_mngrClient().getSupportedLoopbackCgwColors()

@register('getSupportedLoopbackTransportColors')
def getSupportedLoopbackTransportColors():
    return Sdwan_mngrClient().getSupportedLoopbackTransportColors()

@register('getMappingMatrix')
def getMappingMatrix(cloudType: str):
    return Sdwan_mngrClient().getMappingMatrix(cloudType=cloudType)

@register('getDefaultMappingValues')
def getDefaultMappingValues(cloudType: str):
    return Sdwan_mngrClient().getDefaultMappingValues(cloudType=cloudType)

@register('getMappingStatus')
def getMappingStatus(cloudType: str, **kwargs):
    return Sdwan_mngrClient().getMappingStatus(cloudType=cloudType, **kwargs)

@register('getMappingSummary')
def getMappingSummary(**kwargs):
    return Sdwan_mngrClient().getMappingSummary(**kwargs)

@register('getMappingTags')
def getMappingTags(**kwargs):
    return Sdwan_mngrClient().getMappingTags(**kwargs)

@register('getEdgeMappingTags')
def getEdgeMappingTags(cloudType: str, **kwargs):
    return Sdwan_mngrClient().getEdgeMappingTags(cloudType=cloudType, **kwargs)

@register('getMappingVpns')
def getMappingVpns():
    return Sdwan_mngrClient().getMappingVpns()

@register('getCgwAssociatedMappings')
def getCgwAssociatedMappings(cloudGatewayName: str, cloudType: str, **kwargs):
    return Sdwan_mngrClient().getCgwAssociatedMappings(cloudGatewayName=cloudGatewayName, cloudType=cloudType, **kwargs)

@register('getPartnerPorts')
def getPartnerPorts(**kwargs):
    return Sdwan_mngrClient().getPartnerPorts(**kwargs)

@register('getPortSpeed')
def getPortSpeed(connectivityType: str, edgeAccountId: str, edgeType: str, **kwargs):
    return Sdwan_mngrClient().getPortSpeed(connectivityType=connectivityType, edgeAccountId=edgeAccountId, edgeType=edgeType, **kwargs)

@register('getCloudRegions')
def getCloudRegions(**kwargs):
    return Sdwan_mngrClient().getCloudRegions(**kwargs)

@register('getEdgeGlobalSettings')
def getEdgeGlobalSettings(edgeType: str):
    return Sdwan_mngrClient().getEdgeGlobalSettings(edgeType=edgeType)

@register('getGlobalSettings')
def getGlobalSettings(cloudType: str):
    return Sdwan_mngrClient().getGlobalSettings(cloudType=cloudType)

@register('getSites')
def getSites(**kwargs):
    return Sdwan_mngrClient().getSites(**kwargs)

@register('getSshKeyList')
def getSshKeyList(accountId: str, cloudRegion: str, cloudType: str):
    return Sdwan_mngrClient().getSshKeyList(accountId=accountId, cloudRegion=cloudRegion, cloudType=cloudType)

@register('getSupportedSoftwareImageList')
def getSupportedSoftwareImageList(cloudType: str, **kwargs):
    return Sdwan_mngrClient().getSupportedSoftwareImageList(cloudType=cloudType, **kwargs)

@register('getTunnelNames')
def getTunnelNames(cloudGatewayName: str, cloudType: str):
    return Sdwan_mngrClient().getTunnelNames(cloudGatewayName=cloudGatewayName, cloudType=cloudType)

@register('getCloudTypes')
def getCloudTypes():
    return Sdwan_mngrClient().getCloudTypes()

@register('getEdgeTypes')
def getEdgeTypes():
    return Sdwan_mngrClient().getEdgeTypes()

@register('getVHubs')
def getVHubs(**kwargs):
    return Sdwan_mngrClient().getVHubs(**kwargs)

@register('getVWans')
def getVWans(**kwargs):
    return Sdwan_mngrClient().getVWans(**kwargs)

@register('getAllCloudWidgets')
def getAllCloudWidgets():
    return Sdwan_mngrClient().getAllCloudWidgets()

@register('getAllEdgeWidgets')
def getAllEdgeWidgets():
    return Sdwan_mngrClient().getAllEdgeWidgets()

@register('getEdgeWidget')
def getEdgeWidget(edgeType: str):
    return Sdwan_mngrClient().getEdgeWidget(edgeType=edgeType)

@register('getCloudWidget')
def getCloudWidget(cloudType: str):
    return Sdwan_mngrClient().getCloudWidget(cloudType=cloudType)

@register('getMultiCloudConfigGroupTopology')
def getMultiCloudConfigGroupTopology(cloudType: str, config-group-id: str):
    return Sdwan_mngrClient().getMultiCloudConfigGroupTopology(cloudType=cloudType, config-group-id=config-group-id)

@register('getVmanageControlStatus')
def getVmanageControlStatus(**kwargs):
    return Sdwan_mngrClient().getVmanageControlStatus(**kwargs)

@register('getRebootCount')
def getRebootCount(isCached: bool):
    return Sdwan_mngrClient().getRebootCount(isCached=isCached)

@register('getNetworkIssuesSummary')
def getNetworkIssuesSummary():
    return Sdwan_mngrClient().getNetworkIssuesSummary()

@register('getNetworkStatusSummary')
def getNetworkStatusSummary():
    return Sdwan_mngrClient().getNetworkStatusSummary()

@register('getNetworkDesign')
def getNetworkDesign():
    return Sdwan_mngrClient().getNetworkDesign()

@register('getCircuits')
def getCircuits():
    return Sdwan_mngrClient().getCircuits()

@register('getGlobalParameters')
def getGlobalParameters():
    return Sdwan_mngrClient().getGlobalParameters()

@register('getGlobalTemplate')
def getGlobalTemplate(templateId: str):
    return Sdwan_mngrClient().getGlobalTemplate(templateId=templateId)

@register('runMyTest')
def runMyTest(name: str):
    return Sdwan_mngrClient().runMyTest(name=name)

@register('getDeviceProfileFeatureTemplateList')
def getDeviceProfileFeatureTemplateList():
    return Sdwan_mngrClient().getDeviceProfileFeatureTemplateList()

@register('getDeviceProfileConfigStatus')
def getDeviceProfileConfigStatus():
    return Sdwan_mngrClient().getDeviceProfileConfigStatus()

@register('getDeviceProfileConfigStatusByProfileId')
def getDeviceProfileConfigStatusByProfileId(profileId: str):
    return Sdwan_mngrClient().getDeviceProfileConfigStatusByProfileId(profileId=profileId)

@register('getDeviceProfileTaskCount')
def getDeviceProfileTaskCount():
    return Sdwan_mngrClient().getDeviceProfileTaskCount()

@register('getDeviceProfileTaskStatus')
def getDeviceProfileTaskStatus():
    return Sdwan_mngrClient().getDeviceProfileTaskStatus()

@register('getDeviceProfileTaskStatusByProfileId')
def getDeviceProfileTaskStatusByProfileId(profileId: str):
    return Sdwan_mngrClient().getDeviceProfileTaskStatusByProfileId(profileId=profileId)

@register('generateProfileTemplateList')
def generateProfileTemplateList():
    return Sdwan_mngrClient().generateProfileTemplateList()

@register('getDeviceProfileTemplate')
def getDeviceProfileTemplate(templateId: str):
    return Sdwan_mngrClient().getDeviceProfileTemplate(templateId=templateId)

@register('getServiceProfileConfig')
def getServiceProfileConfig(deviceModel: str, profileId: str):
    return Sdwan_mngrClient().getServiceProfileConfig(deviceModel=deviceModel, profileId=profileId)

@register('getNotificationRule')
def getNotificationRule(**kwargs):
    return Sdwan_mngrClient().getNotificationRule(**kwargs)

@register('getDevices')
def getDevices(status: str):
    return Sdwan_mngrClient().getDevices(status=status)

@register('oauthAccess')
def oauthAccess(**kwargs):
    return Sdwan_mngrClient().oauthAccess(**kwargs)

@register('getClientID')
def getClientID():
    return Sdwan_mngrClient().getClientID()

@register('getCall')
def getCall():
    return Sdwan_mngrClient().getCall()

@register('getPartners')
def getPartners():
    return Sdwan_mngrClient().getPartners()

@register('getACIDefinitions')
def getACIDefinitions():
    return Sdwan_mngrClient().getACIDefinitions()

@register('getDscpMappings')
def getDscpMappings(partnerId: str):
    return Sdwan_mngrClient().getDscpMappings(partnerId=partnerId)

@register('getEvents_1')
def getEvents_1(partnerId: str, **kwargs):
    return Sdwan_mngrClient().getEvents_1(partnerId=partnerId, **kwargs)

@register('getDataPrefixMappings')
def getDataPrefixMappings(partnerId: str):
    return Sdwan_mngrClient().getDataPrefixMappings(partnerId=partnerId)

@register('getDataPrefixSequences')
def getDataPrefixSequences():
    return Sdwan_mngrClient().getDataPrefixSequences()

@register('getSDAEnabledDevices')
def getSDAEnabledDevices(partnerId: str):
    return Sdwan_mngrClient().getSDAEnabledDevices(partnerId=partnerId)

@register('getDeviceDetails')
def getDeviceDetails(partnerId: str, uuid: str):
    return Sdwan_mngrClient().getDeviceDetails(partnerId=partnerId, uuid=uuid)

@register('getSitesForPartner')
def getSitesForPartner(partnerId: str):
    return Sdwan_mngrClient().getSitesForPartner(partnerId=partnerId)

@register('getOverlayVPNList')
def getOverlayVPNList():
    return Sdwan_mngrClient().getOverlayVPNList()

@register('getVPNList')
def getVPNList():
    return Sdwan_mngrClient().getVPNList()

@register('getPartnersByPartnerType')
def getPartnersByPartnerType(partnerType: str):
    return Sdwan_mngrClient().getPartnersByPartnerType(partnerType=partnerType)

@register('getPartnerDevices')
def getPartnerDevices(nmsId: str, partnerType: str):
    return Sdwan_mngrClient().getPartnerDevices(nmsId=nmsId, partnerType=partnerType)

@register('getPartner')
def getPartner(nmsId: str, partnerType: str):
    return Sdwan_mngrClient().getPartner(nmsId=nmsId, partnerType=partnerType)

@register('getSecureXRefreshToken')
def getSecureXRefreshToken(clientId: str, regionBaseUri: str):
    return Sdwan_mngrClient().getSecureXRefreshToken(clientId=clientId, regionBaseUri=regionBaseUri)

@register('getResources')
def getResources(tenantId: str, tenantVpn: int):
    return Sdwan_mngrClient().getResources(tenantId=tenantId, tenantVpn=tenantVpn)

@register('listSchedules')
def listSchedules(**kwargs):
    return Sdwan_mngrClient().listSchedules(**kwargs)

@register('getScheduleRecordForBackup')
def getScheduleRecordForBackup(schedulerId: str):
    return Sdwan_mngrClient().getScheduleRecordForBackup(schedulerId=schedulerId)

@register('getExtendedApplications')
def getExtendedApplications(**kwargs):
    return Sdwan_mngrClient().getExtendedApplications(**kwargs)

@register('getCloudConnector')
def getCloudConnector():
    return Sdwan_mngrClient().getCloudConnector()

@register('getCloudConnectorStatus')
def getCloudConnectorStatus():
    return Sdwan_mngrClient().getCloudConnectorStatus()

@register('getCustomApp')
def getCustomApp():
    return Sdwan_mngrClient().getCustomApp()

@register('getAllProtocolPacks')
def getAllProtocolPacks():
    return Sdwan_mngrClient().getAllProtocolPacks()

@register('getBaseSystemPack')
def getBaseSystemPack():
    return Sdwan_mngrClient().getBaseSystemPack()

@register('getAllSDAVCDevice')
def getAllSDAVCDevice():
    return Sdwan_mngrClient().getAllSDAVCDevice()

@register('getDefaultApplicationComplianceDetails')
def getDefaultApplicationComplianceDetails():
    return Sdwan_mngrClient().getDefaultApplicationComplianceDetails()

@register('isApplicationComplianceDetected')
def isApplicationComplianceDetected():
    return Sdwan_mngrClient().isApplicationComplianceDetected()

@register('getApplicationComplianceStatus')
def getApplicationComplianceStatus(uuid: str):
    return Sdwan_mngrClient().getApplicationComplianceStatus(uuid=uuid)

@register('getApplicationComplianceDetails')
def getApplicationComplianceDetails(uuid: str):
    return Sdwan_mngrClient().getApplicationComplianceDetails(uuid=uuid)

@register('getCustomApplicationList')
def getCustomApplicationList():
    return Sdwan_mngrClient().getCustomApplicationList()

@register('getNonCompliantDevicesForProtocolPack')
def getNonCompliantDevicesForProtocolPack(protocolPackName: str):
    return Sdwan_mngrClient().getNonCompliantDevicesForProtocolPack(protocolPackName=protocolPackName)

@register('getDeviceComplianceStatus')
def getDeviceComplianceStatus(uuid: str):
    return Sdwan_mngrClient().getDeviceComplianceStatus(uuid=uuid)

@register('getNewApplicationList')
def getNewApplicationList(deviceUUID: str):
    return Sdwan_mngrClient().getNewApplicationList(deviceUUID=deviceUUID)

@register('getCompliancePolicy')
def getCompliancePolicy(**kwargs):
    return Sdwan_mngrClient().getCompliancePolicy(**kwargs)

@register('getPolicyComplianceStatus')
def getPolicyComplianceStatus(uuid: str):
    return Sdwan_mngrClient().getPolicyComplianceStatus(uuid=uuid)

@register('getDefaultSystemPack')
def getDefaultSystemPack():
    return Sdwan_mngrClient().getDefaultSystemPack()

@register('getLatestSystemPack')
def getLatestSystemPack():
    return Sdwan_mngrClient().getLatestSystemPack()

@register('getDeployJobStatus')
def getDeployJobStatus():
    return Sdwan_mngrClient().getDeployJobStatus()

@register('getDeployJobStatus_1')
def getDeployJobStatus_1(uuid: str):
    return Sdwan_mngrClient().getDeployJobStatus_1(uuid=uuid)

@register('getProtocolPackUploadStatus')
def getProtocolPackUploadStatus(uuid: str):
    return Sdwan_mngrClient().getProtocolPackUploadStatus(uuid=uuid)

@register('getSecurityDeviceHealth')
def getSecurityDeviceHealth(**kwargs):
    return Sdwan_mngrClient().getSecurityDeviceHealth(**kwargs)

@register('getSecurityPolicyDeviceList')
def getSecurityPolicyDeviceList():
    return Sdwan_mngrClient().getSecurityPolicyDeviceList()

@register('getSegments')
def getSegments():
    return Sdwan_mngrClient().getSegments()

@register('getSegment')
def getSegment(id: str):
    return Sdwan_mngrClient().getSegment(id=id)

@register('createServerInfo_1')
def createServerInfo_1():
    return Sdwan_mngrClient().createServerInfo_1()

@register('getDataChangeInfo')
def getDataChangeInfo(partnerId: str, **kwargs):
    return Sdwan_mngrClient().getDataChangeInfo(partnerId=partnerId, **kwargs)

@register('showInfo')
def showInfo():
    return Sdwan_mngrClient().showInfo()

@register('getCertificate')
def getCertificate():
    return Sdwan_mngrClient().getCertificate()

@register('getBanner')
def getBanner():
    return Sdwan_mngrClient().getBanner()

@register('getSessionTimout')
def getSessionTimout():
    return Sdwan_mngrClient().getSessionTimout()

@register('getCertConfiguration')
def getCertConfiguration(type: str):
    return Sdwan_mngrClient().getCertConfiguration(type=type)

@register('getCloudxConfiguration')
def getCloudxConfiguration():
    return Sdwan_mngrClient().getCloudxConfiguration()

@register('getGoogleMapKey')
def getGoogleMapKey():
    return Sdwan_mngrClient().getGoogleMapKey()

@register('getMaintenanceWindow')
def getMaintenanceWindow():
    return Sdwan_mngrClient().getMaintenanceWindow()

@register('getMicrosoftTelemetryConfiguration')
def getMicrosoftTelemetryConfiguration():
    return Sdwan_mngrClient().getMicrosoftTelemetryConfiguration()

@register('getWaniConfiguration')
def getWaniConfiguration():
    return Sdwan_mngrClient().getWaniConfiguration()

@register('getConfigurationBySettingType')
def getConfigurationBySettingType(type: str):
    return Sdwan_mngrClient().getConfigurationBySettingType(type=type)

@register('getPasswordPolicy')
def getPasswordPolicy():
    return Sdwan_mngrClient().getPasswordPolicy()

@register('getSigDynamicDataCenterList')
def getSigDynamicDataCenterList(tunneltype: str, type: str):
    return Sdwan_mngrClient().getSigDynamicDataCenterList(tunneltype=tunneltype, type=type)

@register('getSigDataCenterList')
def getSigDataCenterList(devicetype: str, tunneltype: str, type: str):
    return Sdwan_mngrClient().getSigDataCenterList(devicetype=devicetype, tunneltype=tunneltype, type=type)

@register('getSigGlobalCredentials')
def getSigGlobalCredentials(featureTemplateType: str):
    return Sdwan_mngrClient().getSigGlobalCredentials(featureTemplateType=featureTemplateType)

@register('getChildOrgs')
def getChildOrgs(type: str):
    return Sdwan_mngrClient().getChildOrgs(type=type)

@register('fetchAccounts')
def fetchAccounts(mode: str):
    return Sdwan_mngrClient().fetchAccounts(mode=mode)

@register('fetchReports_1')
def fetchReports_1():
    return Sdwan_mngrClient().fetchReports_1()

@register('fetchReports')
def fetchReports(saDomain: str, saId: str):
    return Sdwan_mngrClient().fetchReports(saDomain=saDomain, saId=saId)

@register('getSettings')
def getSettings():
    return Sdwan_mngrClient().getSettings()

@register('getProxyCertOfEdge')
def getProxyCertOfEdge(deviceId: str):
    return Sdwan_mngrClient().getProxyCertOfEdge(deviceId=deviceId)

@register('getSslProxyCSR')
def getSslProxyCSR(deviceId: str):
    return Sdwan_mngrClient().getSslProxyCSR(deviceId=deviceId)

@register('getSslProxyList')
def getSslProxyList():
    return Sdwan_mngrClient().getSslProxyList()

@register('getCertificateState')
def getCertificateState():
    return Sdwan_mngrClient().getCertificateState()

@register('getEnterpriseCertificate')
def getEnterpriseCertificate():
    return Sdwan_mngrClient().getEnterpriseCertificate()

@register('getVManageEnterpriseRootCertificate')
def getVManageEnterpriseRootCertificate():
    return Sdwan_mngrClient().getVManageEnterpriseRootCertificate()

@register('getvManageCertificate')
def getvManageCertificate():
    return Sdwan_mngrClient().getvManageCertificate()

@register('getvManageCSR')
def getvManageCSR():
    return Sdwan_mngrClient().getvManageCSR()

@register('getvManageRootCA')
def getvManageRootCA():
    return Sdwan_mngrClient().getvManageRootCA()

@register('getStatisticType')
def getStatisticType():
    return Sdwan_mngrClient().getStatisticType()

@register('getAggregationDataByQuery_14')
def getAggregationDataByQuery_14(**kwargs):
    return Sdwan_mngrClient().getAggregationDataByQuery_14(**kwargs)

@register('getStatDataRawData_1')
def getStatDataRawData_1(**kwargs):
    return Sdwan_mngrClient().getStatDataRawData_1(**kwargs)

@register('getAggregationDataByQuery_1')
def getAggregationDataByQuery_1(**kwargs):
    return Sdwan_mngrClient().getAggregationDataByQuery_1(**kwargs)

@register('getStatDataRawDataAsCSV_1')
def getStatDataRawDataAsCSV_1(**kwargs):
    return Sdwan_mngrClient().getStatDataRawDataAsCSV_1(**kwargs)

@register('getCount_2')
def getCount_2(query: str):
    return Sdwan_mngrClient().getCount_2(query=query)

@register('getStatDataFields_2')
def getStatDataFields_2():
    return Sdwan_mngrClient().getStatDataFields_2()

@register('getStatsPaginationRawData_1')
def getStatsPaginationRawData_1(**kwargs):
    return Sdwan_mngrClient().getStatsPaginationRawData_1(**kwargs)

@register('getStatQueryFields_2')
def getStatQueryFields_2():
    return Sdwan_mngrClient().getStatQueryFields_2()

@register('getStatDataRawData')
def getStatDataRawData(**kwargs):
    return Sdwan_mngrClient().getStatDataRawData(**kwargs)

@register('getAggregationDataByQuery')
def getAggregationDataByQuery(**kwargs):
    return Sdwan_mngrClient().getAggregationDataByQuery(**kwargs)

@register('getStatDataRawDataAsCSV')
def getStatDataRawDataAsCSV(**kwargs):
    return Sdwan_mngrClient().getStatDataRawDataAsCSV(**kwargs)

@register('getCount_1')
def getCount_1(query: str):
    return Sdwan_mngrClient().getCount_1(query=query)

@register('getStatDataFields_1')
def getStatDataFields_1():
    return Sdwan_mngrClient().getStatDataFields_1()

@register('getStatsPaginationRawData')
def getStatsPaginationRawData(**kwargs):
    return Sdwan_mngrClient().getStatsPaginationRawData(**kwargs)

@register('getStatQueryFields_1')
def getStatQueryFields_1():
    return Sdwan_mngrClient().getStatQueryFields_1()

@register('getStatDataRawData_2')
def getStatDataRawData_2(**kwargs):
    return Sdwan_mngrClient().getStatDataRawData_2(**kwargs)

@register('getAggregationDataByQuery_2')
def getAggregationDataByQuery_2(**kwargs):
    return Sdwan_mngrClient().getAggregationDataByQuery_2(**kwargs)

@register('getStatDataRawDataAsCSV_2')
def getStatDataRawDataAsCSV_2(**kwargs):
    return Sdwan_mngrClient().getStatDataRawDataAsCSV_2(**kwargs)

@register('getStatsAppRouteDeviceTunnelSummary')
def getStatsAppRouteDeviceTunnelSummary(**kwargs):
    return Sdwan_mngrClient().getStatsAppRouteDeviceTunnelSummary(**kwargs)

@register('getStatsAppRouteDeviceTunnels')
def getStatsAppRouteDeviceTunnels(**kwargs):
    return Sdwan_mngrClient().getStatsAppRouteDeviceTunnels(**kwargs)

@register('getDocCount_1')
def getDocCount_1(query: str):
    return Sdwan_mngrClient().getDocCount_1(query=query)

@register('getStatDataFields_3')
def getStatDataFields_3():
    return Sdwan_mngrClient().getStatDataFields_3()

@register('getStatBulkRawData')
def getStatBulkRawData(**kwargs):
    return Sdwan_mngrClient().getStatBulkRawData(**kwargs)

@register('getStatQueryFields_3')
def getStatQueryFields_3():
    return Sdwan_mngrClient().getStatQueryFields_3()

@register('getAppRouteTransportSummaryType')
def getAppRouteTransportSummaryType(type: str, **kwargs):
    return Sdwan_mngrClient().getAppRouteTransportSummaryType(type=type, **kwargs)

@register('getAppRouteTransportType')
def getAppRouteTransportType(limit: int, type: str, **kwargs):
    return Sdwan_mngrClient().getAppRouteTransportType(limit=limit, type=type, **kwargs)

@register('getAppRouteTunnelSummaryType')
def getAppRouteTunnelSummaryType(type: str, **kwargs):
    return Sdwan_mngrClient().getAppRouteTunnelSummaryType(type=type, **kwargs)

@register('getAppRouteTunnelHealth')
def getAppRouteTunnelHealth(type: str, **kwargs):
    return Sdwan_mngrClient().getAppRouteTunnelHealth(type=type, **kwargs)

@register('getAppRouteTunnelsSummaryType')
def getAppRouteTunnelsSummaryType(type: str, **kwargs):
    return Sdwan_mngrClient().getAppRouteTunnelsSummaryType(type=type, **kwargs)

@register('getAppRouteTunnelType')
def getAppRouteTunnelType(type: str, **kwargs):
    return Sdwan_mngrClient().getAppRouteTunnelType(type=type, **kwargs)

@register('getStatDataRawData_4')
def getStatDataRawData_4(**kwargs):
    return Sdwan_mngrClient().getStatDataRawData_4(**kwargs)

@register('getAggregationDataByQuery_4')
def getAggregationDataByQuery_4(**kwargs):
    return Sdwan_mngrClient().getAggregationDataByQuery_4(**kwargs)

@register('getStatDataRawDataAsCSV_4')
def getStatDataRawDataAsCSV_4(**kwargs):
    return Sdwan_mngrClient().getStatDataRawDataAsCSV_4(**kwargs)

@register('getCount_4')
def getCount_4(query: str):
    return Sdwan_mngrClient().getCount_4(query=query)

@register('getStatDataFields_5')
def getStatDataFields_5():
    return Sdwan_mngrClient().getStatDataFields_5()

@register('getStatsPaginationRawData_3')
def getStatsPaginationRawData_3(**kwargs):
    return Sdwan_mngrClient().getStatsPaginationRawData_3(**kwargs)

@register('getStatQueryFields_5')
def getStatQueryFields_5():
    return Sdwan_mngrClient().getStatQueryFields_5()

@register('getStatDataRawData_5')
def getStatDataRawData_5(**kwargs):
    return Sdwan_mngrClient().getStatDataRawData_5(**kwargs)

@register('getAggregationDataByQuery_5')
def getAggregationDataByQuery_5(**kwargs):
    return Sdwan_mngrClient().getAggregationDataByQuery_5(**kwargs)

@register('getStatDataRawDataAsCSV_5')
def getStatDataRawDataAsCSV_5(**kwargs):
    return Sdwan_mngrClient().getStatDataRawDataAsCSV_5(**kwargs)

@register('getCount_5')
def getCount_5(query: str):
    return Sdwan_mngrClient().getCount_5(query=query)

@register('getStatDataFields_6')
def getStatDataFields_6():
    return Sdwan_mngrClient().getStatDataFields_6()

@register('getStatsPaginationRawData_4')
def getStatsPaginationRawData_4(**kwargs):
    return Sdwan_mngrClient().getStatsPaginationRawData_4(**kwargs)

@register('getStatQueryFields_6')
def getStatQueryFields_6():
    return Sdwan_mngrClient().getStatQueryFields_6()

@register('getStatDataRawData_6')
def getStatDataRawData_6(**kwargs):
    return Sdwan_mngrClient().getStatDataRawData_6(**kwargs)

@register('getAggregationDataByQuery_6')
def getAggregationDataByQuery_6(**kwargs):
    return Sdwan_mngrClient().getAggregationDataByQuery_6(**kwargs)

@register('getStatDataRawDataAsCSV_6')
def getStatDataRawDataAsCSV_6(**kwargs):
    return Sdwan_mngrClient().getStatDataRawDataAsCSV_6(**kwargs)

@register('getCount_6')
def getCount_6(query: str):
    return Sdwan_mngrClient().getCount_6(query=query)

@register('getStatDataFields_7')
def getStatDataFields_7():
    return Sdwan_mngrClient().getStatDataFields_7()

@register('getStatsPaginationRawData_5')
def getStatsPaginationRawData_5(**kwargs):
    return Sdwan_mngrClient().getStatsPaginationRawData_5(**kwargs)

@register('getStatQueryFields_7')
def getStatQueryFields_7():
    return Sdwan_mngrClient().getStatQueryFields_7()

@register('getStatDataRawData_7')
def getStatDataRawData_7(**kwargs):
    return Sdwan_mngrClient().getStatDataRawData_7(**kwargs)

@register('getAggregationDataByQuery_7')
def getAggregationDataByQuery_7(**kwargs):
    return Sdwan_mngrClient().getAggregationDataByQuery_7(**kwargs)

@register('getStatDataRawDataAsCSV_7')
def getStatDataRawDataAsCSV_7(**kwargs):
    return Sdwan_mngrClient().getStatDataRawDataAsCSV_7(**kwargs)

@register('getCount_7')
def getCount_7(query: str):
    return Sdwan_mngrClient().getCount_7(query=query)

@register('getStatDataFields_8')
def getStatDataFields_8():
    return Sdwan_mngrClient().getStatDataFields_8()

@register('getStatsPaginationRawData_6')
def getStatsPaginationRawData_6(**kwargs):
    return Sdwan_mngrClient().getStatsPaginationRawData_6(**kwargs)

@register('getStatQueryFields_8')
def getStatQueryFields_8():
    return Sdwan_mngrClient().getStatQueryFields_8()

@register('getStatDataRawData_9')
def getStatDataRawData_9(**kwargs):
    return Sdwan_mngrClient().getStatDataRawData_9(**kwargs)

@register('getAggregationDataByQuery_9')
def getAggregationDataByQuery_9(**kwargs):
    return Sdwan_mngrClient().getAggregationDataByQuery_9(**kwargs)

@register('createFlowsGrid')
def createFlowsGrid(**kwargs):
    return Sdwan_mngrClient().createFlowsGrid(**kwargs)

@register('createFlowssummary')
def createFlowssummary(**kwargs):
    return Sdwan_mngrClient().createFlowssummary(**kwargs)

@register('getStatDataRawDataAsCSV_9')
def getStatDataRawDataAsCSV_9(**kwargs):
    return Sdwan_mngrClient().getStatDataRawDataAsCSV_9(**kwargs)

@register('createFlowDeviceData')
def createFlowDeviceData(**kwargs):
    return Sdwan_mngrClient().createFlowDeviceData(**kwargs)

@register('getCount_9')
def getCount_9(query: str):
    return Sdwan_mngrClient().getCount_9(query=query)

@register('getStatDataFields_10')
def getStatDataFields_10():
    return Sdwan_mngrClient().getStatDataFields_10()

@register('getStatsPaginationRawData_8')
def getStatsPaginationRawData_8(**kwargs):
    return Sdwan_mngrClient().getStatsPaginationRawData_8(**kwargs)

@register('getStatQueryFields_10')
def getStatQueryFields_10():
    return Sdwan_mngrClient().getStatQueryFields_10()

@register('getStatDataRawData_10')
def getStatDataRawData_10(**kwargs):
    return Sdwan_mngrClient().getStatDataRawData_10(**kwargs)

@register('getAggregationDataByQuery_10')
def getAggregationDataByQuery_10(**kwargs):
    return Sdwan_mngrClient().getAggregationDataByQuery_10(**kwargs)

@register('getStatDataRawDataAsCSV_10')
def getStatDataRawDataAsCSV_10(**kwargs):
    return Sdwan_mngrClient().getStatDataRawDataAsCSV_10(**kwargs)

@register('getCount_10')
def getCount_10(query: str):
    return Sdwan_mngrClient().getCount_10(query=query)

@register('getStatDataFields_11')
def getStatDataFields_11():
    return Sdwan_mngrClient().getStatDataFields_11()

@register('getStatsPaginationRawData_9')
def getStatsPaginationRawData_9(**kwargs):
    return Sdwan_mngrClient().getStatsPaginationRawData_9(**kwargs)

@register('getStatQueryFields_11')
def getStatQueryFields_11():
    return Sdwan_mngrClient().getStatQueryFields_11()

@register('startStatsCollection')
def startStatsCollection():
    return Sdwan_mngrClient().startStatsCollection()

@register('generateStatsCollectThreadReport')
def generateStatsCollectThreadReport():
    return Sdwan_mngrClient().generateStatsCollectThreadReport()

@register('resetStatsCollection')
def resetStatsCollection(processQueue: int):
    return Sdwan_mngrClient().resetStatsCollection(processQueue=processQueue)

@register('getStatDataRawDataAsCSV_13')
def getStatDataRawDataAsCSV_13(**kwargs):
    return Sdwan_mngrClient().getStatDataRawDataAsCSV_13(**kwargs)

@register('enableStatisticsDemoMode')
def enableStatisticsDemoMode(**kwargs):
    return Sdwan_mngrClient().enableStatisticsDemoMode(**kwargs)

@register('getStatDataRawData_16')
def getStatDataRawData_16(**kwargs):
    return Sdwan_mngrClient().getStatDataRawData_16(**kwargs)

@register('getAggregationDataByQuery_18')
def getAggregationDataByQuery_18(**kwargs):
    return Sdwan_mngrClient().getAggregationDataByQuery_18(**kwargs)

@register('getStatDataRawDataAsCSV_16')
def getStatDataRawDataAsCSV_16(**kwargs):
    return Sdwan_mngrClient().getStatDataRawDataAsCSV_16(**kwargs)

@register('getCount_15')
def getCount_15(query: str):
    return Sdwan_mngrClient().getCount_15(query=query)

@register('getStatDataFields_17')
def getStatDataFields_17():
    return Sdwan_mngrClient().getStatDataFields_17()

@register('getStatsPaginationRawData_14')
def getStatsPaginationRawData_14(**kwargs):
    return Sdwan_mngrClient().getStatsPaginationRawData_14(**kwargs)

@register('getStatQueryFields_18')
def getStatQueryFields_18():
    return Sdwan_mngrClient().getStatQueryFields_18()

@register('getDeviceHealthHistory')
def getDeviceHealthHistory(**kwargs):
    return Sdwan_mngrClient().getDeviceHealthHistory(**kwargs)

@register('getDeviceHealthOverview')
def getDeviceHealthOverview(type: str, **kwargs):
    return Sdwan_mngrClient().getDeviceHealthOverview(type=type, **kwargs)

@register('getCount_12')
def getCount_12(query: str):
    return Sdwan_mngrClient().getCount_12(query=query)

@register('fetchList')
def fetchList(processType: str):
    return Sdwan_mngrClient().fetchList(processType=processType)

@register('download')
def download(deviceIp: str, fileName: str, fileType: str, processType: str, queue: str, token: str):
    return Sdwan_mngrClient().download(deviceIp=deviceIp, fileName=fileName, fileType=fileType, processType=processType, queue=queue, token=token)

@register('getDPIStatsRawData')
def getDPIStatsRawData(**kwargs):
    return Sdwan_mngrClient().getDPIStatsRawData(**kwargs)

@register('getDPIStatsAggregationData')
def getDPIStatsAggregationData(**kwargs):
    return Sdwan_mngrClient().getDPIStatsAggregationData(**kwargs)

@register('getAggAppFlows')
def getAggAppFlows(query: str, **kwargs):
    return Sdwan_mngrClient().getAggAppFlows(query=query, **kwargs)

@register('getAggAppFlowsSummary')
def getAggAppFlowsSummary(query: str, **kwargs):
    return Sdwan_mngrClient().getAggAppFlowsSummary(query=query, **kwargs)

@register('getDPIStatsRawDataAsCSV')
def getDPIStatsRawDataAsCSV(**kwargs):
    return Sdwan_mngrClient().getDPIStatsRawDataAsCSV(**kwargs)

@register('getDPIDeviceAppUniqueFlowCount')
def getDPIDeviceAppUniqueFlowCount(deviceId: str, interval: str, window: int, **kwargs):
    return Sdwan_mngrClient().getDPIDeviceAppUniqueFlowCount(deviceId=deviceId, interval=interval, window=window, **kwargs)

@register('getDPIDeviceAppAggregationData')
def getDPIDeviceAppAggregationData(query: str, **kwargs):
    return Sdwan_mngrClient().getDPIDeviceAppAggregationData(query=query, **kwargs)

@register('getDPIDeviceAppDetails')
def getDPIDeviceAppDetails(query: str):
    return Sdwan_mngrClient().getDPIDeviceAppDetails(query=query)

@register('getDPIStatsCount')
def getDPIStatsCount(**kwargs):
    return Sdwan_mngrClient().getDPIStatsCount(**kwargs)

@register('getDPIFields')
def getDPIFields():
    return Sdwan_mngrClient().getDPIFields()

@register('getDPIStatsPaginationRawData')
def getDPIStatsPaginationRawData(**kwargs):
    return Sdwan_mngrClient().getDPIStatsPaginationRawData(**kwargs)

@register('getDPIQueryFields')
def getDPIQueryFields():
    return Sdwan_mngrClient().getDPIQueryFields()

@register('getStatDataRawData_8')
def getStatDataRawData_8(**kwargs):
    return Sdwan_mngrClient().getStatDataRawData_8(**kwargs)

@register('getAggregationDataByQuery_8')
def getAggregationDataByQuery_8(**kwargs):
    return Sdwan_mngrClient().getAggregationDataByQuery_8(**kwargs)

@register('getStatDataRawDataAsCSV_8')
def getStatDataRawDataAsCSV_8(**kwargs):
    return Sdwan_mngrClient().getStatDataRawDataAsCSV_8(**kwargs)

@register('getCount_8')
def getCount_8(query: str):
    return Sdwan_mngrClient().getCount_8(query=query)

@register('getStatDataFields_9')
def getStatDataFields_9():
    return Sdwan_mngrClient().getStatDataFields_9()

@register('getStatsPaginationRawData_7')
def getStatsPaginationRawData_7(**kwargs):
    return Sdwan_mngrClient().getStatsPaginationRawData_7(**kwargs)

@register('getStatQueryFields_9')
def getStatQueryFields_9():
    return Sdwan_mngrClient().getStatQueryFields_9()

@register('getStatDataRawData_19')
def getStatDataRawData_19(**kwargs):
    return Sdwan_mngrClient().getStatDataRawData_19(**kwargs)

@register('getAggregationDataByQuery_21')
def getAggregationDataByQuery_21(**kwargs):
    return Sdwan_mngrClient().getAggregationDataByQuery_21(**kwargs)

@register('getStatDataRawDataAsCSV_19')
def getStatDataRawDataAsCSV_19(**kwargs):
    return Sdwan_mngrClient().getStatDataRawDataAsCSV_19(**kwargs)

@register('getCount_18')
def getCount_18(query: str):
    return Sdwan_mngrClient().getCount_18(query=query)

@register('getStatDataFields_20')
def getStatDataFields_20():
    return Sdwan_mngrClient().getStatDataFields_20()

@register('getStatsPaginationRawData_17')
def getStatsPaginationRawData_17(**kwargs):
    return Sdwan_mngrClient().getStatsPaginationRawData_17(**kwargs)

@register('getStatQueryFields_21')
def getStatQueryFields_21():
    return Sdwan_mngrClient().getStatQueryFields_21()

@register('getStatDataFields_14')
def getStatDataFields_14():
    return Sdwan_mngrClient().getStatDataFields_14()

@register('getStatDataRawData_14')
def getStatDataRawData_14(**kwargs):
    return Sdwan_mngrClient().getStatDataRawData_14(**kwargs)

@register('getAggregationDataByQuery_28')
def getAggregationDataByQuery_28(**kwargs):
    return Sdwan_mngrClient().getAggregationDataByQuery_28(**kwargs)

@register('getStatDataRawDataAsCSV_26')
def getStatDataRawDataAsCSV_26(**kwargs):
    return Sdwan_mngrClient().getStatDataRawDataAsCSV_26(**kwargs)

@register('getFlowlogCount')
def getFlowlogCount(query: str):
    return Sdwan_mngrClient().getFlowlogCount(query=query)

@register('getFlowlogFields')
def getFlowlogFields():
    return Sdwan_mngrClient().getFlowlogFields()

@register('getStatsPaginationRawData_24')
def getStatsPaginationRawData_24(**kwargs):
    return Sdwan_mngrClient().getStatsPaginationRawData_24(**kwargs)

@register('getFlowlogQueryFields')
def getFlowlogQueryFields():
    return Sdwan_mngrClient().getFlowlogQueryFields()

@register('getStatDataRawData_24')
def getStatDataRawData_24(**kwargs):
    return Sdwan_mngrClient().getStatDataRawData_24(**kwargs)

@register('getAggregationDataByQuery_26')
def getAggregationDataByQuery_26(**kwargs):
    return Sdwan_mngrClient().getAggregationDataByQuery_26(**kwargs)

@register('getStatDataRawDataAsCSV_24')
def getStatDataRawDataAsCSV_24(**kwargs):
    return Sdwan_mngrClient().getStatDataRawDataAsCSV_24(**kwargs)

@register('getCount_23')
def getCount_23(query: str):
    return Sdwan_mngrClient().getCount_23(query=query)

@register('getStatDataFields_25')
def getStatDataFields_25():
    return Sdwan_mngrClient().getStatDataFields_25()

@register('getStatsPaginationRawData_22')
def getStatsPaginationRawData_22(**kwargs):
    return Sdwan_mngrClient().getStatsPaginationRawData_22(**kwargs)

@register('getStatQueryFields_26')
def getStatQueryFields_26():
    return Sdwan_mngrClient().getStatQueryFields_26()

@register('getStatDataRawData_11')
def getStatDataRawData_11(query: str, **kwargs):
    return Sdwan_mngrClient().getStatDataRawData_11(query=query, **kwargs)

@register('getAggregationDataByQuery_11')
def getAggregationDataByQuery_11(query: str):
    return Sdwan_mngrClient().getAggregationDataByQuery_11(query=query)

@register('getBandwidthDistribution')
def getBandwidthDistribution(**kwargs):
    return Sdwan_mngrClient().getBandwidthDistribution(**kwargs)

@register('getStatDataRawDataAsCSV_11')
def getStatDataRawDataAsCSV_11(query: str):
    return Sdwan_mngrClient().getStatDataRawDataAsCSV_11(query=query)

@register('getCount10')
def getCount10(query: str):
    return Sdwan_mngrClient().getCount10(query=query)

@register('getStatDataFields_12')
def getStatDataFields_12():
    return Sdwan_mngrClient().getStatDataFields_12()

@register('getStatBulkRawData_1')
def getStatBulkRawData_1(**kwargs):
    return Sdwan_mngrClient().getStatBulkRawData_1(**kwargs)

@register('getStatQueryFields_12')
def getStatQueryFields_12():
    return Sdwan_mngrClient().getStatQueryFields_12()

@register('getStatisticsPerInterface')
def getStatisticsPerInterface(query: str):
    return Sdwan_mngrClient().getStatisticsPerInterface(query=query)

@register('getStatDataRawData_22')
def getStatDataRawData_22(**kwargs):
    return Sdwan_mngrClient().getStatDataRawData_22(**kwargs)

@register('getAggregationDataByQuery_24')
def getAggregationDataByQuery_24(**kwargs):
    return Sdwan_mngrClient().getAggregationDataByQuery_24(**kwargs)

@register('getStatDataRawDataAsCSV_22')
def getStatDataRawDataAsCSV_22(**kwargs):
    return Sdwan_mngrClient().getStatDataRawDataAsCSV_22(**kwargs)

@register('getCount_21')
def getCount_21(query: str):
    return Sdwan_mngrClient().getCount_21(query=query)

@register('getStatDataFields_23')
def getStatDataFields_23():
    return Sdwan_mngrClient().getStatDataFields_23()

@register('getStatsPaginationRawData_20')
def getStatsPaginationRawData_20(**kwargs):
    return Sdwan_mngrClient().getStatsPaginationRawData_20(**kwargs)

@register('getStatQueryFields_24')
def getStatQueryFields_24():
    return Sdwan_mngrClient().getStatQueryFields_24()

@register('getQueueEntries')
def getQueueEntries():
    return Sdwan_mngrClient().getQueueEntries()

@register('getQueueProperties')
def getQueueProperties():
    return Sdwan_mngrClient().getQueueProperties()

@register('getStatsPaginationRawData_11')
def getStatsPaginationRawData_11(**kwargs):
    return Sdwan_mngrClient().getStatsPaginationRawData_11(**kwargs)

@register('getApplicationHeatMapDetail')
def getApplicationHeatMapDetail(application: str, heatmap_time: int, start_time: int, **kwargs):
    return Sdwan_mngrClient().getApplicationHeatMapDetail(application=application, heatmap_time=heatmap_time, start_time=start_time, **kwargs)

@register('getApplicationSitesHealth')
def getApplicationSitesHealth(application: str, **kwargs):
    return Sdwan_mngrClient().getApplicationSitesHealth(application=application, **kwargs)

@register('getApplicationsSiteHealth')
def getApplicationsSiteHealth(siteid: str, **kwargs):
    return Sdwan_mngrClient().getApplicationsSiteHealth(siteid=siteid, **kwargs)

@register('getApplicationsSitesHealth')
def getApplicationsSitesHealth(**kwargs):
    return Sdwan_mngrClient().getApplicationsSitesHealth(**kwargs)

@register('getSupportedDeviceList')
def getSupportedDeviceList(**kwargs):
    return Sdwan_mngrClient().getSupportedDeviceList(**kwargs)

@register('processStatisticsData')
def processStatisticsData():
    return Sdwan_mngrClient().processStatisticsData()

@register('getStatisticsProcessingCounters')
def getStatisticsProcessingCounters():
    return Sdwan_mngrClient().getStatisticsProcessingCounters()

@register('generateStatsProcessReport')
def generateStatsProcessReport(**kwargs):
    return Sdwan_mngrClient().generateStatsProcessReport(**kwargs)

@register('generateStatsProcessThreadReport')
def generateStatsProcessThreadReport():
    return Sdwan_mngrClient().generateStatsProcessThreadReport()

@register('getStatDataRawData_3')
def getStatDataRawData_3(**kwargs):
    return Sdwan_mngrClient().getStatDataRawData_3(**kwargs)

@register('getAggregationDataByQuery_15')
def getAggregationDataByQuery_15(**kwargs):
    return Sdwan_mngrClient().getAggregationDataByQuery_15(**kwargs)

@register('getStatDataRawDataAsCSV_3')
def getStatDataRawDataAsCSV_3(**kwargs):
    return Sdwan_mngrClient().getStatDataRawDataAsCSV_3(**kwargs)

@register('getCount_3')
def getCount_3(query: str):
    return Sdwan_mngrClient().getCount_3(query=query)

@register('getStatDataFields_4')
def getStatDataFields_4():
    return Sdwan_mngrClient().getStatDataFields_4()

@register('getStatsPaginationRawData_2')
def getStatsPaginationRawData_2(**kwargs):
    return Sdwan_mngrClient().getStatsPaginationRawData_2(**kwargs)

@register('getStatQueryFields_4')
def getStatQueryFields_4():
    return Sdwan_mngrClient().getStatQueryFields_4()

@register('getStatDataRawData_13')
def getStatDataRawData_13(**kwargs):
    return Sdwan_mngrClient().getStatDataRawData_13(**kwargs)

@register('getAggregationDataByQuery_13')
def getAggregationDataByQuery_13(**kwargs):
    return Sdwan_mngrClient().getAggregationDataByQuery_13(**kwargs)

@register('getStatDataRawDataAsCSV12')
def getStatDataRawDataAsCSV12(**kwargs):
    return Sdwan_mngrClient().getStatDataRawDataAsCSV12(**kwargs)

@register('getCount13')
def getCount13(query: str):
    return Sdwan_mngrClient().getCount13(query=query)

@register('getStatDataFields13')
def getStatDataFields13():
    return Sdwan_mngrClient().getStatDataFields13()

@register('getStatBulkRawData_2')
def getStatBulkRawData_2(**kwargs):
    return Sdwan_mngrClient().getStatBulkRawData_2(**kwargs)

@register('getStatQueryFields_14')
def getStatQueryFields_14():
    return Sdwan_mngrClient().getStatQueryFields_14()

@register('getStatQueryFields_15')
def getStatQueryFields_15():
    return Sdwan_mngrClient().getStatQueryFields_15()

@register('getSdraHeadendSummary')
def getSdraHeadendSummary(**kwargs):
    return Sdwan_mngrClient().getSdraHeadendSummary(**kwargs)

@register('getSdraSessionSummary')
def getSdraSessionSummary(**kwargs):
    return Sdwan_mngrClient().getSdraSessionSummary(**kwargs)

@register('getDisabledDeviceList')
def getDisabledDeviceList(indexName: str):
    return Sdwan_mngrClient().getDisabledDeviceList(indexName=indexName)

@register('getStatisticsSettings')
def getStatisticsSettings():
    return Sdwan_mngrClient().getStatisticsSettings()

@register('getEnabledIndexForDevice')
def getEnabledIndexForDevice(deviceId: str):
    return Sdwan_mngrClient().getEnabledIndexForDevice(deviceId=deviceId)

@register('getStatDataRawData_15')
def getStatDataRawData_15(**kwargs):
    return Sdwan_mngrClient().getStatDataRawData_15(**kwargs)

@register('getAggregationDataByQuery_16')
def getAggregationDataByQuery_16(**kwargs):
    return Sdwan_mngrClient().getAggregationDataByQuery_16(**kwargs)

@register('getSiteHealth')
def getSiteHealth(**kwargs):
    return Sdwan_mngrClient().getSiteHealth(**kwargs)

@register('getStatDataRawDataAsCSV_14')
def getStatDataRawDataAsCSV_14(**kwargs):
    return Sdwan_mngrClient().getStatDataRawDataAsCSV_14(**kwargs)

@register('getCount_13')
def getCount_13(query: str):
    return Sdwan_mngrClient().getCount_13(query=query)

@register('getStatDataFields_15')
def getStatDataFields_15():
    return Sdwan_mngrClient().getStatDataFields_15()

@register('getStatsPaginationRawData_12')
def getStatsPaginationRawData_12(**kwargs):
    return Sdwan_mngrClient().getStatsPaginationRawData_12(**kwargs)

@register('getStatQueryFields_16')
def getStatQueryFields_16():
    return Sdwan_mngrClient().getStatQueryFields_16()

@register('getSiteHealthTopology')
def getSiteHealthTopology(**kwargs):
    return Sdwan_mngrClient().getSiteHealthTopology(**kwargs)

@register('getStatDataRawData_26')
def getStatDataRawData_26(**kwargs):
    return Sdwan_mngrClient().getStatDataRawData_26(**kwargs)

@register('getAggregationDataByQuery_29')
def getAggregationDataByQuery_29(**kwargs):
    return Sdwan_mngrClient().getAggregationDataByQuery_29(**kwargs)

@register('getStatDataRawDataAsCSV_27')
def getStatDataRawDataAsCSV_27(**kwargs):
    return Sdwan_mngrClient().getStatDataRawDataAsCSV_27(**kwargs)

@register('getCount_25')
def getCount_25(query: str):
    return Sdwan_mngrClient().getCount_25(query=query)

@register('getStatDataFields_27')
def getStatDataFields_27():
    return Sdwan_mngrClient().getStatDataFields_27()

@register('getStatsPaginationRawData_25')
def getStatsPaginationRawData_25(**kwargs):
    return Sdwan_mngrClient().getStatsPaginationRawData_25(**kwargs)

@register('getStatQueryFields_29')
def getStatQueryFields_29():
    return Sdwan_mngrClient().getStatQueryFields_29()

@register('getSulStatDataRawData')
def getSulStatDataRawData(**kwargs):
    return Sdwan_mngrClient().getSulStatDataRawData(**kwargs)

@register('getAggregationDataByQuery_17')
def getAggregationDataByQuery_17(**kwargs):
    return Sdwan_mngrClient().getAggregationDataByQuery_17(**kwargs)

@register('getStatDataRawDataAsCSV_15')
def getStatDataRawDataAsCSV_15(**kwargs):
    return Sdwan_mngrClient().getStatDataRawDataAsCSV_15(**kwargs)

@register('getCount_14')
def getCount_14(query: str):
    return Sdwan_mngrClient().getCount_14(query=query)

@register('getStatDataFields_16')
def getStatDataFields_16():
    return Sdwan_mngrClient().getStatDataFields_16()

@register('getFilterPolicyNameList')
def getFilterPolicyNameList(policyType: str, query: str):
    return Sdwan_mngrClient().getFilterPolicyNameList(policyType=policyType, query=query)

@register('getStatsPaginationRawData_13')
def getStatsPaginationRawData_13(**kwargs):
    return Sdwan_mngrClient().getStatsPaginationRawData_13(**kwargs)

@register('getStatQueryFields_17')
def getStatQueryFields_17():
    return Sdwan_mngrClient().getStatQueryFields_17()

@register('getStatDataRawData_17')
def getStatDataRawData_17(**kwargs):
    return Sdwan_mngrClient().getStatDataRawData_17(**kwargs)

@register('getAggregationDataByQuery_19')
def getAggregationDataByQuery_19(**kwargs):
    return Sdwan_mngrClient().getAggregationDataByQuery_19(**kwargs)

@register('createDeviceSystemCPUStat')
def createDeviceSystemCPUStat(deviceId: str, query: str):
    return Sdwan_mngrClient().createDeviceSystemCPUStat(deviceId=deviceId, query=query)

@register('getStatDataRawDataAsCSV_17')
def getStatDataRawDataAsCSV_17(**kwargs):
    return Sdwan_mngrClient().getStatDataRawDataAsCSV_17(**kwargs)

@register('getCount_16')
def getCount_16(query: str):
    return Sdwan_mngrClient().getCount_16(query=query)

@register('getStatDataFields_18')
def getStatDataFields_18():
    return Sdwan_mngrClient().getStatDataFields_18()

@register('createDeviceSystemMemoryStat')
def createDeviceSystemMemoryStat(deviceId: str, query: str):
    return Sdwan_mngrClient().createDeviceSystemMemoryStat(deviceId=deviceId, query=query)

@register('getStatsPaginationRawData_15')
def getStatsPaginationRawData_15(**kwargs):
    return Sdwan_mngrClient().getStatsPaginationRawData_15(**kwargs)

@register('getStatQueryFields_19')
def getStatQueryFields_19():
    return Sdwan_mngrClient().getStatQueryFields_19()

@register('getStatDataRawData_18')
def getStatDataRawData_18(**kwargs):
    return Sdwan_mngrClient().getStatDataRawData_18(**kwargs)

@register('getAggregationDataByQuery_20')
def getAggregationDataByQuery_20(**kwargs):
    return Sdwan_mngrClient().getAggregationDataByQuery_20(**kwargs)

@register('getStatDataRawDataAsCSV_18')
def getStatDataRawDataAsCSV_18(**kwargs):
    return Sdwan_mngrClient().getStatDataRawDataAsCSV_18(**kwargs)

@register('getCount_17')
def getCount_17(query: str):
    return Sdwan_mngrClient().getCount_17(query=query)

@register('getStatDataFields_19')
def getStatDataFields_19():
    return Sdwan_mngrClient().getStatDataFields_19()

@register('getStatsPaginationRawData_16')
def getStatsPaginationRawData_16(**kwargs):
    return Sdwan_mngrClient().getStatsPaginationRawData_16(**kwargs)

@register('getStatQueryFields_20')
def getStatQueryFields_20():
    return Sdwan_mngrClient().getStatQueryFields_20()

@register('statisticsApprouteTunnelhealthHistoryGet')
def statisticsApprouteTunnelhealthHistoryGet(**kwargs):
    return Sdwan_mngrClient().statisticsApprouteTunnelhealthHistoryGet(**kwargs)

@register('statisticsApprouteTunnelhealthOverviewTypeGet')
def statisticsApprouteTunnelhealthOverviewTypeGet(type: str, **kwargs):
    return Sdwan_mngrClient().statisticsApprouteTunnelhealthOverviewTypeGet(type=type, **kwargs)

@register('getStatDataRawData_25')
def getStatDataRawData_25(**kwargs):
    return Sdwan_mngrClient().getStatDataRawData_25(**kwargs)

@register('getAggregationDataByQuery_27')
def getAggregationDataByQuery_27(**kwargs):
    return Sdwan_mngrClient().getAggregationDataByQuery_27(**kwargs)

@register('getStatDataRawDataAsCSV_25')
def getStatDataRawDataAsCSV_25(**kwargs):
    return Sdwan_mngrClient().getStatDataRawDataAsCSV_25(**kwargs)

@register('getCount_24')
def getCount_24(query: str):
    return Sdwan_mngrClient().getCount_24(query=query)

@register('getStatDataFields_26')
def getStatDataFields_26():
    return Sdwan_mngrClient().getStatDataFields_26()

@register('getStatsPaginationRawData_23')
def getStatsPaginationRawData_23(**kwargs):
    return Sdwan_mngrClient().getStatsPaginationRawData_23(**kwargs)

@register('getStatQueryFields_27')
def getStatQueryFields_27():
    return Sdwan_mngrClient().getStatQueryFields_27()

@register('getStatDataRawData_23')
def getStatDataRawData_23(**kwargs):
    return Sdwan_mngrClient().getStatDataRawData_23(**kwargs)

@register('getAggregationDataByQuery_25')
def getAggregationDataByQuery_25(**kwargs):
    return Sdwan_mngrClient().getAggregationDataByQuery_25(**kwargs)

@register('getStatDataRawDataAsCSV_23')
def getStatDataRawDataAsCSV_23(**kwargs):
    return Sdwan_mngrClient().getStatDataRawDataAsCSV_23(**kwargs)

@register('getCount_22')
def getCount_22(query: str):
    return Sdwan_mngrClient().getCount_22(query=query)

@register('getStatDataFields_24')
def getStatDataFields_24():
    return Sdwan_mngrClient().getStatDataFields_24()

@register('getStatsPaginationRawData_21')
def getStatsPaginationRawData_21(**kwargs):
    return Sdwan_mngrClient().getStatsPaginationRawData_21(**kwargs)

@register('getStatQueryFields_25')
def getStatQueryFields_25():
    return Sdwan_mngrClient().getStatQueryFields_25()

@register('getStatDataRawData_12')
def getStatDataRawData_12(**kwargs):
    return Sdwan_mngrClient().getStatDataRawData_12(**kwargs)

@register('getAggregationDataByQuery_12')
def getAggregationDataByQuery_12(**kwargs):
    return Sdwan_mngrClient().getAggregationDataByQuery_12(**kwargs)

@register('getStatDataRawDataAsCSV_12')
def getStatDataRawDataAsCSV_12(**kwargs):
    return Sdwan_mngrClient().getStatDataRawDataAsCSV_12(**kwargs)

@register('getCount_11')
def getCount_11(query: str):
    return Sdwan_mngrClient().getCount_11(query=query)

@register('getStatDataFields_13')
def getStatDataFields_13():
    return Sdwan_mngrClient().getStatDataFields_13()

@register('getStatsPaginationRawData_10')
def getStatsPaginationRawData_10(**kwargs):
    return Sdwan_mngrClient().getStatsPaginationRawData_10(**kwargs)

@register('getStatQueryFields_13')
def getStatQueryFields_13():
    return Sdwan_mngrClient().getStatQueryFields_13()

@register('getStatDataRawData_20')
def getStatDataRawData_20(**kwargs):
    return Sdwan_mngrClient().getStatDataRawData_20(**kwargs)

@register('getAggregationDataByQuery_22')
def getAggregationDataByQuery_22(**kwargs):
    return Sdwan_mngrClient().getAggregationDataByQuery_22(**kwargs)

@register('getStatDataRawDataAsCSV_20')
def getStatDataRawDataAsCSV_20(**kwargs):
    return Sdwan_mngrClient().getStatDataRawDataAsCSV_20(**kwargs)

@register('getCount_19')
def getCount_19(query: str):
    return Sdwan_mngrClient().getCount_19(query=query)

@register('getStatDataFields_21')
def getStatDataFields_21():
    return Sdwan_mngrClient().getStatDataFields_21()

@register('getStatsPaginationRawData_18')
def getStatsPaginationRawData_18(**kwargs):
    return Sdwan_mngrClient().getStatsPaginationRawData_18(**kwargs)

@register('getStatQueryFields_22')
def getStatQueryFields_22():
    return Sdwan_mngrClient().getStatQueryFields_22()

@register('disablePacketCaptureSession')
def disablePacketCaptureSession(sessionId: str):
    return Sdwan_mngrClient().disablePacketCaptureSession(sessionId=sessionId)

@register('downloadFile')
def downloadFile(sessionId: str):
    return Sdwan_mngrClient().downloadFile(sessionId=sessionId)

@register('forceStopPcapSession')
def forceStopPcapSession(sessionId: str):
    return Sdwan_mngrClient().forceStopPcapSession(sessionId=sessionId)

@register('startPcapSession')
def startPcapSession(sessionId: str):
    return Sdwan_mngrClient().startPcapSession(sessionId=sessionId)

@register('getFileDownloadStatus')
def getFileDownloadStatus(sessionId: str):
    return Sdwan_mngrClient().getFileDownloadStatus(sessionId=sessionId)

@register('stopPcapSession')
def stopPcapSession(sessionId: str):
    return Sdwan_mngrClient().stopPcapSession(sessionId=sessionId)

@register('getVnicInfoByVnfId')
def getVnicInfoByVnfId(vnfId: str):
    return Sdwan_mngrClient().getVnicInfoByVnfId(vnfId=vnfId)

@register('disableDeviceLog')
def disableDeviceLog(sessionId: str):
    return Sdwan_mngrClient().disableDeviceLog(sessionId=sessionId)

@register('downloadDebugLog')
def downloadDebugLog(sessionId: str):
    return Sdwan_mngrClient().downloadDebugLog(sessionId=sessionId)

@register('renewSessionInfo')
def renewSessionInfo(sessionId: str):
    return Sdwan_mngrClient().renewSessionInfo(sessionId=sessionId)

@register('getSessions')
def getSessions():
    return Sdwan_mngrClient().getSessions()

@register('clearSession')
def clearSession(sessionId: str):
    return Sdwan_mngrClient().clearSession(sessionId=sessionId)

@register('getLogType')
def getLogType(uuid: str):
    return Sdwan_mngrClient().getLogType(uuid=uuid)

@register('getDeviceLog')
def getDeviceLog(sessionId: str, **kwargs):
    return Sdwan_mngrClient().getDeviceLog(sessionId=sessionId, **kwargs)

@register('activeFlowWithQuery')
def activeFlowWithQuery(timestamp: int, traceId: int, **kwargs):
    return Sdwan_mngrClient().activeFlowWithQuery(timestamp=timestamp, traceId=traceId, **kwargs)

@register('getAggFlow')
def getAggFlow(timestamp: int, traceId: int, traceState: str, **kwargs):
    return Sdwan_mngrClient().getAggFlow(timestamp=timestamp, traceId=traceId, traceState=traceState, **kwargs)

@register('getAppQosData')
def getAppQosData(receivedTimestamp: int, timestamp: int, traceId: int, **kwargs):
    return Sdwan_mngrClient().getAppQosData(receivedTimestamp=receivedTimestamp, timestamp=timestamp, traceId=traceId, **kwargs)

@register('getAppQosState')
def getAppQosState(timestamp: int, traceId: int, traceState: str):
    return Sdwan_mngrClient().getAppQosState(timestamp=timestamp, traceId=traceId, traceState=traceState)

@register('getConcurrentData')
def getConcurrentData(timestamp: int, traceId: int):
    return Sdwan_mngrClient().getConcurrentData(timestamp=timestamp, traceId=traceId)

@register('getConcurrentDomainData')
def getConcurrentDomainData(timestamp: int, traceId: int, **kwargs):
    return Sdwan_mngrClient().getConcurrentDomainData(timestamp=timestamp, traceId=traceId, **kwargs)

@register('getCurrentTimestamp')
def getCurrentTimestamp():
    return Sdwan_mngrClient().getCurrentTimestamp()

@register('getDeviceBList')
def getDeviceBList():
    return Sdwan_mngrClient().getDeviceBList()

@register('getDevicesAndInterfacesBySite')
def getDevicesAndInterfacesBySite(site_id: str, **kwargs):
    return Sdwan_mngrClient().getDevicesAndInterfacesBySite(site_id=site_id, **kwargs)

@register('getDomainMetric')
def getDomainMetric(domain: str, firstTimestamp: int, lastTimestamp: int, timestamp: int, traceId: int, **kwargs):
    return Sdwan_mngrClient().getDomainMetric(domain=domain, firstTimestamp=firstTimestamp, lastTimestamp=lastTimestamp, timestamp=timestamp, traceId=traceId, **kwargs)

@register('getEventAppHopList')
def getEventAppHopList(timestamp: int, traceId: int, **kwargs):
    return Sdwan_mngrClient().getEventAppHopList(timestamp=timestamp, traceId=traceId, **kwargs)

@register('getEventAppScoreBandwidth')
def getEventAppScoreBandwidth(receivedTimestamp: int, timestamp: int, traceId: int, **kwargs):
    return Sdwan_mngrClient().getEventAppScoreBandwidth(receivedTimestamp=receivedTimestamp, timestamp=timestamp, traceId=traceId, **kwargs)

@register('getEventFlowFromAppHop')
def getEventFlowFromAppHop(deviceTraceId: int, direction: str, from: str, timestamp: int, to: str, traceId: int, **kwargs):
    return Sdwan_mngrClient().getEventFlowFromAppHop(deviceTraceId=deviceTraceId, direction=direction, from=from, timestamp=timestamp, to=to, traceId=traceId, **kwargs)

@register('getEventReadout')
def getEventReadout(timestamp: int, traceId: int, **kwargs):
    return Sdwan_mngrClient().getEventReadout(timestamp=timestamp, traceId=traceId, **kwargs)

@register('getEventReadoutBySite')
def getEventReadoutBySite(last_n_hours: int, site_id: str, **kwargs):
    return Sdwan_mngrClient().getEventReadoutBySite(last_n_hours=last_n_hours, site_id=site_id, **kwargs)

@register('getEventReadoutByTraces')
def getEventReadoutByTraces(entry_time: list, trace_id: list, **kwargs):
    return Sdwan_mngrClient().getEventReadoutByTraces(entry_time=entry_time, trace_id=trace_id, **kwargs)

@register('exportTrace')
def exportTrace(timestamp: int, traceId: int):
    return Sdwan_mngrClient().exportTrace(timestamp=timestamp, traceId=traceId)

@register('getFinalizedData')
def getFinalizedData(timestamp: int, traceId: int):
    return Sdwan_mngrClient().getFinalizedData(timestamp=timestamp, traceId=traceId)

@register('getFinalizedDomainData')
def getFinalizedDomainData(timestamp: int, traceId: int, **kwargs):
    return Sdwan_mngrClient().getFinalizedDomainData(timestamp=timestamp, traceId=traceId, **kwargs)

@register('getFlowDetail')
def getFlowDetail(flowId: int, timestamp: int, traceId: int):
    return Sdwan_mngrClient().getFlowDetail(flowId=flowId, timestamp=timestamp, traceId=traceId)

@register('getFlowMetric')
def getFlowMetric(firstTimestamp: int, flowId: int, lastTimestamp: int, timestamp: int, traceId: int):
    return Sdwan_mngrClient().getFlowMetric(firstTimestamp=firstTimestamp, flowId=flowId, lastTimestamp=lastTimestamp, timestamp=timestamp, traceId=traceId)

@register('getMonitorState')
def getMonitorState(state: str, traceId: int):
    return Sdwan_mngrClient().getMonitorState(state=state, traceId=traceId)

@register('getNwpiDscp')
def getNwpiDscp():
    return Sdwan_mngrClient().getNwpiDscp()

@register('getNwpiNbarAppGroup')
def getNwpiNbarAppGroup():
    return Sdwan_mngrClient().getNwpiNbarAppGroup()

@register('getNwpiProtocol')
def getNwpiProtocol():
    return Sdwan_mngrClient().getNwpiProtocol()

@register('nwpiSettingView')
def nwpiSettingView(**kwargs):
    return Sdwan_mngrClient().nwpiSettingView(**kwargs)

@register('getPacketFeatures')
def getPacketFeatures(flowId: int, timestamp: int, traceId: int):
    return Sdwan_mngrClient().getPacketFeatures(flowId=flowId, timestamp=timestamp, traceId=traceId)

@register('getPreloadInfo')
def getPreloadInfo(**kwargs):
    return Sdwan_mngrClient().getPreloadInfo(**kwargs)

@register('getStatQueryFields_28')
def getStatQueryFields_28():
    return Sdwan_mngrClient().getStatQueryFields_28()

@register('getRoutingDetailFromLocal')
def getRoutingDetailFromLocal(routePrefixs: str, timestamp: int, traceId: int, traceState: str):
    return Sdwan_mngrClient().getRoutingDetailFromLocal(routePrefixs=routePrefixs, timestamp=timestamp, traceId=traceId, traceState=traceState)

@register('getEventStatsData')
def getEventStatsData(duration: int, state: str, taskEndTime: int, taskId: int):
    return Sdwan_mngrClient().getEventStatsData(duration=duration, state=state, taskEndTime=taskEndTime, taskId=taskId)

@register('getTaskHistory')
def getTaskHistory():
    return Sdwan_mngrClient().getTaskHistory()

@register('getTaskTrace')
def getTaskTrace(taskId: str):
    return Sdwan_mngrClient().getTaskTrace(taskId=taskId)

@register('getTraceCftRecord')
def getTraceCftRecord(entryTime: int, traceId: int, traceState: str, **kwargs):
    return Sdwan_mngrClient().getTraceCftRecord(entryTime=entryTime, traceId=traceId, traceState=traceState, **kwargs)

@register('getFinalizedFlowCount')
def getFinalizedFlowCount(timestamp: int, traceId: int):
    return Sdwan_mngrClient().getFinalizedFlowCount(timestamp=timestamp, traceId=traceId)

@register('getFinFlowTimeRange')
def getFinFlowTimeRange(state: str, timestamp: int, traceId: int):
    return Sdwan_mngrClient().getFinFlowTimeRange(state=state, timestamp=timestamp, traceId=traceId)

@register('traceFinFlowWithQuery')
def traceFinFlowWithQuery(timestamp: int, traceId: int, **kwargs):
    return Sdwan_mngrClient().traceFinFlowWithQuery(timestamp=timestamp, traceId=traceId, **kwargs)

@register('getTraceFlow')
def getTraceFlow(state: str, timestamp: int, traceId: int):
    return Sdwan_mngrClient().getTraceFlow(state=state, timestamp=timestamp, traceId=traceId)

@register('getTraceHistory')
def getTraceHistory(**kwargs):
    return Sdwan_mngrClient().getTraceHistory(**kwargs)

@register('getTraceInfoByBaseKey')
def getTraceInfoByBaseKey(entryTime: int, traceId: int, **kwargs):
    return Sdwan_mngrClient().getTraceInfoByBaseKey(entryTime=entryTime, traceId=traceId, **kwargs)

@register('getTraceReadoutFilter')
def getTraceReadoutFilter(entry_time: list, trace_id: list):
    return Sdwan_mngrClient().getTraceReadoutFilter(entry_time=entry_time, trace_id=trace_id)

@register('disableSpeedTestSession')
def disableSpeedTestSession(sessionId: str):
    return Sdwan_mngrClient().disableSpeedTestSession(sessionId=sessionId)

@register('getInterfaceBandwidth')
def getInterfaceBandwidth(deviceUUID: str, **kwargs):
    return Sdwan_mngrClient().getInterfaceBandwidth(deviceUUID=deviceUUID, **kwargs)

@register('startSpeedTest')
def startSpeedTest(sessionId: str):
    return Sdwan_mngrClient().startSpeedTest(sessionId=sessionId)

@register('getSpeedTestStatus')
def getSpeedTestStatus(sessionId: str):
    return Sdwan_mngrClient().getSpeedTestStatus(sessionId=sessionId)

@register('stopSpeedTest')
def stopSpeedTest(sessionId: str):
    return Sdwan_mngrClient().stopSpeedTest(sessionId=sessionId)

@register('getSpeedTest')
def getSpeedTest(sessionId: str, **kwargs):
    return Sdwan_mngrClient().getSpeedTest(sessionId=sessionId, **kwargs)

@register('getUMTSData')
def getUMTSData(deviceUUID: str, eventType: str, **kwargs):
    return Sdwan_mngrClient().getUMTSData(deviceUUID=deviceUUID, eventType=eventType, **kwargs)

@register('updateUmtsSessionStatus')
def updateUmtsSessionStatus(operation: str, sessionId: str):
    return Sdwan_mngrClient().updateUmtsSessionStatus(operation=operation, sessionId=sessionId)

@register('generateBootstrapConfigForVedge')
def generateBootstrapConfigForVedge(configtype: str, inclDefRootCert: bool, uuid: str, **kwargs):
    return Sdwan_mngrClient().generateBootstrapConfigForVedge(configtype=configtype, inclDefRootCert=inclDefRootCert, uuid=uuid, **kwargs)

@register('getBootstrapConfigZip')
def getBootstrapConfigZip(id: str):
    return Sdwan_mngrClient().getBootstrapConfigZip(id=id)

@register('generateGenericBootstrapConfigForVedges')
def generateGenericBootstrapConfigForVedges(**kwargs):
    return Sdwan_mngrClient().generateGenericBootstrapConfigForVedges(**kwargs)

@register('getControllerVEdgeSyncStatus_1')
def getControllerVEdgeSyncStatus_1():
    return Sdwan_mngrClient().getControllerVEdgeSyncStatus_1()

@register('devicesWithoutSubjectSudi')
def devicesWithoutSubjectSudi():
    return Sdwan_mngrClient().devicesWithoutSubjectSudi()

@register('getManagementSystemIPInfo_1')
def getManagementSystemIPInfo_1():
    return Sdwan_mngrClient().getManagementSystemIPInfo_1()

@register('getRMACandidates')
def getRMACandidates(deviceType: str, **kwargs):
    return Sdwan_mngrClient().getRMACandidates(deviceType=deviceType, **kwargs)

@register('getRootCertStatusAll')
def getRootCertStatusAll(state: str):
    return Sdwan_mngrClient().getRootCertStatusAll(state=state)

@register('checkSelfSignedCert_1')
def checkSelfSignedCert_1():
    return Sdwan_mngrClient().checkSelfSignedCert_1()

@register('syncRootCertChain')
def syncRootCertChain():
    return Sdwan_mngrClient().syncRootCertChain()

@register('getTenantManagementSystemIPs')
def getTenantManagementSystemIPs():
    return Sdwan_mngrClient().getTenantManagementSystemIPs()

@register('getCloudDockDataBasedOnDeviceType')
def getCloudDockDataBasedOnDeviceType(deviceCategory: str):
    return Sdwan_mngrClient().getCloudDockDataBasedOnDeviceType(deviceCategory=deviceCategory)

@register('getCloudDockDefaultConfigBasedOnDeviceType')
def getCloudDockDefaultConfigBasedOnDeviceType(deviceCategory: str):
    return Sdwan_mngrClient().getCloudDockDefaultConfigBasedOnDeviceType(deviceCategory=deviceCategory)

@register('getAllUnclaimedDevices')
def getAllUnclaimedDevices():
    return Sdwan_mngrClient().getAllUnclaimedDevices()

@register('checkvEdgeDevicePresence')
def checkvEdgeDevicePresence():
    return Sdwan_mngrClient().checkvEdgeDevicePresence()

@register('getDevicesDetails')
def getDevicesDetails(deviceCategory: str, **kwargs):
    return Sdwan_mngrClient().getDevicesDetails(deviceCategory=deviceCategory, **kwargs)

@register('getReverseProxyMappings')
def getReverseProxyMappings(uuid: str):
    return Sdwan_mngrClient().getReverseProxyMappings(uuid=uuid)

@register('getCloudXStatus')
def getCloudXStatus():
    return Sdwan_mngrClient().getCloudXStatus()

@register('getAttachedClientList')
def getAttachedClientList():
    return Sdwan_mngrClient().getAttachedClientList()

@register('getAttachedDiaList')
def getAttachedDiaList():
    return Sdwan_mngrClient().getAttachedDiaList()

@register('getAttachedGatewayList')
def getAttachedGatewayList():
    return Sdwan_mngrClient().getAttachedGatewayList()

@register('getCloudXAvailableApps')
def getCloudXAvailableApps():
    return Sdwan_mngrClient().getCloudXAvailableApps()

@register('getSiteList')
def getSiteList():
    return Sdwan_mngrClient().getSiteList()

@register('getDiaList')
def getDiaList():
    return Sdwan_mngrClient().getDiaList()

@register('getGatewayList')
def getGatewayList():
    return Sdwan_mngrClient().getGatewayList()

@register('getApps')
def getApps():
    return Sdwan_mngrClient().getApps()

@register('getSigTunnelList_1')
def getSigTunnelList_1(deviceId: str):
    return Sdwan_mngrClient().getSigTunnelList_1(deviceId=deviceId)

@register('sitePerApp')
def sitePerApp(appName: str, **kwargs):
    return Sdwan_mngrClient().sitePerApp(appName=appName, **kwargs)

@register('getAttachedConfig')
def getAttachedConfig(deviceId: str, **kwargs):
    return Sdwan_mngrClient().getAttachedConfig(deviceId=deviceId, **kwargs)

@register('generateCLIModeDevices')
def generateCLIModeDevices(type: str):
    return Sdwan_mngrClient().generateCLIModeDevices(type=type)

@register('generatevManageModeDevices')
def generatevManageModeDevices(type: str):
    return Sdwan_mngrClient().generatevManageModeDevices(type=type)

@register('getDeviceDiff')
def getDeviceDiff(deviceId: str):
    return Sdwan_mngrClient().getDeviceDiff(deviceId=deviceId)

@register('getCompatibleDevices')
def getCompatibleDevices(oldDeviceId: str):
    return Sdwan_mngrClient().getCompatibleDevices(oldDeviceId=oldDeviceId)

@register('getRunningConfig')
def getRunningConfig(deviceId: str):
    return Sdwan_mngrClient().getRunningConfig(deviceId=deviceId)

@register('getVpnForDevice')
def getVpnForDevice(deviceId: str):
    return Sdwan_mngrClient().getVpnForDevice(deviceId=deviceId)

@register('getCORStatus')
def getCORStatus():
    return Sdwan_mngrClient().getCORStatus()

@register('getAmiList')
def getAmiList(accountid: str, cloudregion: str, **kwargs):
    return Sdwan_mngrClient().getAmiList(accountid=accountid, cloudregion=cloudregion, **kwargs)

@register('getCloudList')
def getCloudList():
    return Sdwan_mngrClient().getCloudList()

@register('getCloudAccounts')
def getCloudAccounts(cloudEnvironment: str, cloudtype: str):
    return Sdwan_mngrClient().getCloudAccounts(cloudEnvironment=cloudEnvironment, cloudtype=cloudtype)

@register('getCloudHostVpcAccountDetails')
def getCloudHostVpcAccountDetails():
    return Sdwan_mngrClient().getCloudHostVpcAccountDetails()

@register('getCloudMappedHostAccounts')
def getCloudMappedHostAccounts(accountid: str, cloudtype: str):
    return Sdwan_mngrClient().getCloudMappedHostAccounts(accountid=accountid, cloudtype=cloudtype)

@register('getCloudOnRampDevices')
def getCloudOnRampDevices():
    return Sdwan_mngrClient().getCloudOnRampDevices()

@register('getHostVPCs')
def getHostVPCs(devicePairId: str, transitVpcId: str):
    return Sdwan_mngrClient().getHostVPCs(devicePairId=devicePairId, transitVpcId=transitVpcId)

@register('getExternalId')
def getExternalId():
    return Sdwan_mngrClient().getExternalId()

@register('getTransitDevicePairAndHostList')
def getTransitDevicePairAndHostList(accountId: str, cloudRegion: str):
    return Sdwan_mngrClient().getTransitDevicePairAndHostList(accountId=accountId, cloudRegion=cloudRegion)

@register('getTransitVpcVpnList')
def getTransitVpcVpnList(accountId: str):
    return Sdwan_mngrClient().getTransitVpcVpnList(accountId=accountId)

@register('getCloudHostVPCs')
def getCloudHostVPCs(accountid: str, cloudregion: str, **kwargs):
    return Sdwan_mngrClient().getCloudHostVPCs(accountid=accountid, cloudregion=cloudregion, **kwargs)

@register('getMappedVPCs')
def getMappedVPCs(accountid: str, cloudregion: str):
    return Sdwan_mngrClient().getMappedVPCs(accountid=accountid, cloudregion=cloudregion)

@register('getPemKeyList')
def getPemKeyList(accountid: str, cloudregion: str, cloudtype: str):
    return Sdwan_mngrClient().getPemKeyList(accountid=accountid, cloudregion=cloudregion, cloudtype=cloudtype)

@register('getTransitVPCs')
def getTransitVPCs(accountid: str, cloudregion: str, **kwargs):
    return Sdwan_mngrClient().getTransitVPCs(accountid=accountid, cloudregion=cloudregion, **kwargs)

@register('getTransitVPCSupportedSize')
def getTransitVPCSupportedSize(cloudEnvironment: str, **kwargs):
    return Sdwan_mngrClient().getTransitVPCSupportedSize(cloudEnvironment=cloudEnvironment, **kwargs)

@register('getCortexStatus')
def getCortexStatus():
    return Sdwan_mngrClient().getCortexStatus()

@register('getMappedWanResourceGroups')
def getMappedWanResourceGroups(accountid: str, cloudregion: str):
    return Sdwan_mngrClient().getMappedWanResourceGroups(accountid=accountid, cloudregion=cloudregion)

@register('getWanResourceGroups')
def getWanResourceGroups(accountid: str):
    return Sdwan_mngrClient().getWanResourceGroups(accountid=accountid)

@register('generateMasterTemplateList')
def generateMasterTemplateList(feature: str):
    return Sdwan_mngrClient().generateMasterTemplateList(feature=feature)

@register('getAttachedDeviceList')
def getAttachedDeviceList(masterTemplateId: str):
    return Sdwan_mngrClient().getAttachedDeviceList(masterTemplateId=masterTemplateId)

@register('getAttachedConfigToDevice')
def getAttachedConfigToDevice(deviceId: str, **kwargs):
    return Sdwan_mngrClient().getAttachedConfigToDevice(deviceId=deviceId, **kwargs)

@register('getDeviceListByMasterTemplateId')
def getDeviceListByMasterTemplateId(masterTemplateId: str):
    return Sdwan_mngrClient().getDeviceListByMasterTemplateId(masterTemplateId=masterTemplateId)

@register('checkVbond')
def checkVbond():
    return Sdwan_mngrClient().checkVbond()

@register('isMigrationRequired')
def isMigrationRequired():
    return Sdwan_mngrClient().isMigrationRequired()

@register('generateTemplateForMigration')
def generateTemplateForMigration(**kwargs):
    return Sdwan_mngrClient().generateTemplateForMigration(**kwargs)

@register('migrationInfo')
def migrationInfo():
    return Sdwan_mngrClient().migrationInfo()

@register('getMasterTemplateDefinition')
def getMasterTemplateDefinition(templateId: str):
    return Sdwan_mngrClient().getMasterTemplateDefinition(templateId=templateId)

@register('getOutOfSyncTemplates')
def getOutOfSyncTemplates():
    return Sdwan_mngrClient().getOutOfSyncTemplates()

@register('getOutOfSyncDevices')
def getOutOfSyncDevices(templateId: str):
    return Sdwan_mngrClient().getOutOfSyncDevices(templateId=templateId)

@register('getAssociatedFeatureTemplatesDetails')
def getAssociatedFeatureTemplatesDetails(templateId: str):
    return Sdwan_mngrClient().getAssociatedFeatureTemplatesDetails(templateId=templateId)

@register('generateFeatureTemplateList')
def generateFeatureTemplateList(**kwargs):
    return Sdwan_mngrClient().generateFeatureTemplateList(**kwargs)

@register('getNetworkInterface')
def getNetworkInterface(deviceModel: str):
    return Sdwan_mngrClient().getNetworkInterface(deviceModel=deviceModel)

@register('getDefaultNetworks')
def getDefaultNetworks(deviceModel: str):
    return Sdwan_mngrClient().getDefaultNetworks(deviceModel=deviceModel)

@register('getTemplateDefinition')
def getTemplateDefinition(templateId: str):
    return Sdwan_mngrClient().getTemplateDefinition(templateId=templateId)

@register('getDeviceTemplatesAttachedToFeature')
def getDeviceTemplatesAttachedToFeature(templateId: str):
    return Sdwan_mngrClient().getDeviceTemplatesAttachedToFeature(templateId=templateId)

@register('listLITemplate')
def listLITemplate():
    return Sdwan_mngrClient().listLITemplate()

@register('generateMasterTemplateDefinition')
def generateMasterTemplateDefinition(type_name: str):
    return Sdwan_mngrClient().generateMasterTemplateDefinition(type_name=type_name)

@register('getTemplateForMigration')
def getTemplateForMigration():
    return Sdwan_mngrClient().getTemplateForMigration()

@register('getGeneralTemplate')
def getGeneralTemplate(templateId: str):
    return Sdwan_mngrClient().getGeneralTemplate(templateId=templateId)

@register('generateTemplateTypes')
def generateTemplateTypes(type: str):
    return Sdwan_mngrClient().generateTemplateTypes(type=type)

@register('generateTemplateTypeDefinition')
def generateTemplateTypeDefinition(type_name: str, version: str):
    return Sdwan_mngrClient().generateTemplateTypeDefinition(type_name=type_name, version=version)

@register('generateTemplateByDeviceType')
def generateTemplateByDeviceType(deviceType: str):
    return Sdwan_mngrClient().generateTemplateByDeviceType(deviceType=deviceType)

@register('previewById')
def previewById(id: str):
    return Sdwan_mngrClient().previewById(id=id)

@register('previewById_1')
def previewById_1(id: str):
    return Sdwan_mngrClient().previewById_1(id=id)

@register('previewById_2')
def previewById_2(id: str):
    return Sdwan_mngrClient().previewById_2(id=id)

@register('previewById_3')
def previewById_3(id: str):
    return Sdwan_mngrClient().previewById_3(id=id)

@register('getCloudDiscoveredApps')
def getCloudDiscoveredApps():
    return Sdwan_mngrClient().getCloudDiscoveredApps()

@register('getCustomApps')
def getCustomApps():
    return Sdwan_mngrClient().getCustomApps()

@register('getCustomAppById')
def getCustomAppById(id: str):
    return Sdwan_mngrClient().getCustomAppById(id=id)

@register('getDefinitions_8')
def getDefinitions_8():
    return Sdwan_mngrClient().getDefinitions_8()

@register('previewPolicyDefinitionById_8')
def previewPolicyDefinitionById_8(id: str):
    return Sdwan_mngrClient().previewPolicyDefinitionById_8(id=id)

@register('getPolicyDefinition_8')
def getPolicyDefinition_8(id: str):
    return Sdwan_mngrClient().getPolicyDefinition_8(id=id)

@register('getDefinitions_9')
def getDefinitions_9():
    return Sdwan_mngrClient().getDefinitions_9()

@register('previewPolicyDefinitionById_9')
def previewPolicyDefinitionById_9(id: str):
    return Sdwan_mngrClient().previewPolicyDefinitionById_9(id=id)

@register('getPolicyDefinition_9')
def getPolicyDefinition_9(id: str):
    return Sdwan_mngrClient().getPolicyDefinition_9(id=id)

@register('getDefinitions_11')
def getDefinitions_11():
    return Sdwan_mngrClient().getDefinitions_11()

@register('previewPolicyDefinitionById_11')
def previewPolicyDefinitionById_11(id: str):
    return Sdwan_mngrClient().previewPolicyDefinitionById_11(id=id)

@register('getPolicyDefinition_11')
def getPolicyDefinition_11(id: str):
    return Sdwan_mngrClient().getPolicyDefinition_11(id=id)

@register('getDefinitions_10')
def getDefinitions_10():
    return Sdwan_mngrClient().getDefinitions_10()

@register('previewPolicyDefinitionById_10')
def previewPolicyDefinitionById_10(id: str):
    return Sdwan_mngrClient().previewPolicyDefinitionById_10(id=id)

@register('getPolicyDefinition_10')
def getPolicyDefinition_10(id: str):
    return Sdwan_mngrClient().getPolicyDefinition_10(id=id)

@register('getDefinitions_12')
def getDefinitions_12():
    return Sdwan_mngrClient().getDefinitions_12()

@register('previewPolicyDefinitionById_12')
def previewPolicyDefinitionById_12(id: str):
    return Sdwan_mngrClient().previewPolicyDefinitionById_12(id=id)

@register('getPolicyDefinition_12')
def getPolicyDefinition_12(id: str):
    return Sdwan_mngrClient().getPolicyDefinition_12(id=id)

@register('getDefinitions_13')
def getDefinitions_13():
    return Sdwan_mngrClient().getDefinitions_13()

@register('previewPolicyDefinitionById_13')
def previewPolicyDefinitionById_13(id: str):
    return Sdwan_mngrClient().previewPolicyDefinitionById_13(id=id)

@register('getPolicyDefinition_13')
def getPolicyDefinition_13(id: str):
    return Sdwan_mngrClient().getPolicyDefinition_13(id=id)

@register('getDefinitions_14')
def getDefinitions_14():
    return Sdwan_mngrClient().getDefinitions_14()

@register('previewPolicyDefinitionById_14')
def previewPolicyDefinitionById_14(id: str):
    return Sdwan_mngrClient().previewPolicyDefinitionById_14(id=id)

@register('getPolicyDefinition_14')
def getPolicyDefinition_14(id: str):
    return Sdwan_mngrClient().getPolicyDefinition_14(id=id)

@register('getDefinitions_15')
def getDefinitions_15():
    return Sdwan_mngrClient().getDefinitions_15()

@register('previewPolicyDefinitionById_15')
def previewPolicyDefinitionById_15(id: str):
    return Sdwan_mngrClient().previewPolicyDefinitionById_15(id=id)

@register('getPolicyDefinition_15')
def getPolicyDefinition_15(id: str):
    return Sdwan_mngrClient().getPolicyDefinition_15(id=id)

@register('getDefinitions_16')
def getDefinitions_16():
    return Sdwan_mngrClient().getDefinitions_16()

@register('previewPolicyDefinitionById_16')
def previewPolicyDefinitionById_16(id: str):
    return Sdwan_mngrClient().previewPolicyDefinitionById_16(id=id)

@register('getPolicyDefinition_16')
def getPolicyDefinition_16(id: str):
    return Sdwan_mngrClient().getPolicyDefinition_16(id=id)

@register('getDefinitions_17')
def getDefinitions_17():
    return Sdwan_mngrClient().getDefinitions_17()

@register('previewPolicyDefinitionById_17')
def previewPolicyDefinitionById_17(id: str):
    return Sdwan_mngrClient().previewPolicyDefinitionById_17(id=id)

@register('getPolicyDefinition_17')
def getPolicyDefinition_17(id: str):
    return Sdwan_mngrClient().getPolicyDefinition_17(id=id)

@register('getDefinitions_25')
def getDefinitions_25():
    return Sdwan_mngrClient().getDefinitions_25()

@register('previewPolicyDefinitionById_25')
def previewPolicyDefinitionById_25(id: str):
    return Sdwan_mngrClient().previewPolicyDefinitionById_25(id=id)

@register('getPolicyDefinition_25')
def getPolicyDefinition_25(id: str):
    return Sdwan_mngrClient().getPolicyDefinition_25(id=id)

@register('getDefinitions')
def getDefinitions():
    return Sdwan_mngrClient().getDefinitions()

@register('previewPolicyDefinitionById')
def previewPolicyDefinitionById(id: str):
    return Sdwan_mngrClient().previewPolicyDefinitionById(id=id)

@register('getPolicyDefinition')
def getPolicyDefinition(id: str):
    return Sdwan_mngrClient().getPolicyDefinition(id=id)

@register('getDefinitions_26')
def getDefinitions_26():
    return Sdwan_mngrClient().getDefinitions_26()

@register('previewPolicyDefinitionById_26')
def previewPolicyDefinitionById_26(id: str):
    return Sdwan_mngrClient().previewPolicyDefinitionById_26(id=id)

@register('getPolicyDefinition_26')
def getPolicyDefinition_26(id: str):
    return Sdwan_mngrClient().getPolicyDefinition_26(id=id)

@register('getDefinitions_28')
def getDefinitions_28():
    return Sdwan_mngrClient().getDefinitions_28()

@register('previewPolicyDefinitionById_28')
def previewPolicyDefinitionById_28(id: str):
    return Sdwan_mngrClient().previewPolicyDefinitionById_28(id=id)

@register('getPolicyDefinition_28')
def getPolicyDefinition_28(id: str):
    return Sdwan_mngrClient().getPolicyDefinition_28(id=id)

@register('getDefinitions_27')
def getDefinitions_27():
    return Sdwan_mngrClient().getDefinitions_27()

@register('previewPolicyDefinitionById_27')
def previewPolicyDefinitionById_27(id: str):
    return Sdwan_mngrClient().previewPolicyDefinitionById_27(id=id)

@register('getPolicyDefinition_27')
def getPolicyDefinition_27(id: str):
    return Sdwan_mngrClient().getPolicyDefinition_27(id=id)

@register('getDefinitions_4')
def getDefinitions_4():
    return Sdwan_mngrClient().getDefinitions_4()

@register('previewPolicyDefinitionById_4')
def previewPolicyDefinitionById_4(id: str):
    return Sdwan_mngrClient().previewPolicyDefinitionById_4(id=id)

@register('getPolicyDefinition_4')
def getPolicyDefinition_4(id: str):
    return Sdwan_mngrClient().getPolicyDefinition_4(id=id)

@register('getDefinitions_18')
def getDefinitions_18():
    return Sdwan_mngrClient().getDefinitions_18()

@register('previewPolicyDefinitionById_18')
def previewPolicyDefinitionById_18(id: str):
    return Sdwan_mngrClient().previewPolicyDefinitionById_18(id=id)

@register('getPolicyDefinition_18')
def getPolicyDefinition_18(id: str):
    return Sdwan_mngrClient().getPolicyDefinition_18(id=id)

@register('getDefinitions_5')
def getDefinitions_5():
    return Sdwan_mngrClient().getDefinitions_5()

@register('previewPolicyDefinitionById_5')
def previewPolicyDefinitionById_5(id: str):
    return Sdwan_mngrClient().previewPolicyDefinitionById_5(id=id)

@register('getPolicyDefinition_5')
def getPolicyDefinition_5(id: str):
    return Sdwan_mngrClient().getPolicyDefinition_5(id=id)

@register('getDefinitions_29')
def getDefinitions_29():
    return Sdwan_mngrClient().getDefinitions_29()

@register('previewPolicyDefinitionById_29')
def previewPolicyDefinitionById_29(id: str):
    return Sdwan_mngrClient().previewPolicyDefinitionById_29(id=id)

@register('getPolicyDefinition_29')
def getPolicyDefinition_29(id: str):
    return Sdwan_mngrClient().getPolicyDefinition_29(id=id)

@register('getDefinitions_1')
def getDefinitions_1():
    return Sdwan_mngrClient().getDefinitions_1()

@register('previewPolicyDefinitionById_1')
def previewPolicyDefinitionById_1(id: str):
    return Sdwan_mngrClient().previewPolicyDefinitionById_1(id=id)

@register('getPolicyDefinition_1')
def getPolicyDefinition_1(id: str):
    return Sdwan_mngrClient().getPolicyDefinition_1(id=id)

@register('getDefinitions_19')
def getDefinitions_19():
    return Sdwan_mngrClient().getDefinitions_19()

@register('previewPolicyDefinitionById_19')
def previewPolicyDefinitionById_19(id: str):
    return Sdwan_mngrClient().previewPolicyDefinitionById_19(id=id)

@register('getPolicyDefinition_19')
def getPolicyDefinition_19(id: str):
    return Sdwan_mngrClient().getPolicyDefinition_19(id=id)

@register('getDefinitions_20')
def getDefinitions_20():
    return Sdwan_mngrClient().getDefinitions_20()

@register('previewPolicyDefinitionById_20')
def previewPolicyDefinitionById_20(id: str):
    return Sdwan_mngrClient().previewPolicyDefinitionById_20(id=id)

@register('getPolicyDefinition_20')
def getPolicyDefinition_20(id: str):
    return Sdwan_mngrClient().getPolicyDefinition_20(id=id)

@register('getDefinitions_21')
def getDefinitions_21():
    return Sdwan_mngrClient().getDefinitions_21()

@register('previewPolicyDefinitionById_21')
def previewPolicyDefinitionById_21(id: str):
    return Sdwan_mngrClient().previewPolicyDefinitionById_21(id=id)

@register('getPolicyDefinition_21')
def getPolicyDefinition_21(id: str):
    return Sdwan_mngrClient().getPolicyDefinition_21(id=id)

@register('getDefinitions_30')
def getDefinitions_30():
    return Sdwan_mngrClient().getDefinitions_30()

@register('previewPolicyDefinitionById_30')
def previewPolicyDefinitionById_30(id: str):
    return Sdwan_mngrClient().previewPolicyDefinitionById_30(id=id)

@register('getPolicyDefinition_30')
def getPolicyDefinition_30(id: str):
    return Sdwan_mngrClient().getPolicyDefinition_30(id=id)

@register('getDefinitions_3')
def getDefinitions_3():
    return Sdwan_mngrClient().getDefinitions_3()

@register('previewPolicyDefinitionById_3')
def previewPolicyDefinitionById_3(id: str):
    return Sdwan_mngrClient().previewPolicyDefinitionById_3(id=id)

@register('getPolicyDefinition_3')
def getPolicyDefinition_3(id: str):
    return Sdwan_mngrClient().getPolicyDefinition_3(id=id)

@register('getDefinitions_22')
def getDefinitions_22():
    return Sdwan_mngrClient().getDefinitions_22()

@register('previewPolicyDefinitionById_22')
def previewPolicyDefinitionById_22(id: str):
    return Sdwan_mngrClient().previewPolicyDefinitionById_22(id=id)

@register('getPolicyDefinition_22')
def getPolicyDefinition_22(id: str):
    return Sdwan_mngrClient().getPolicyDefinition_22(id=id)

@register('getDefinitions_23')
def getDefinitions_23():
    return Sdwan_mngrClient().getDefinitions_23()

@register('previewPolicyDefinitionById_23')
def previewPolicyDefinitionById_23(id: str):
    return Sdwan_mngrClient().previewPolicyDefinitionById_23(id=id)

@register('getPolicyDefinition_23')
def getPolicyDefinition_23(id: str):
    return Sdwan_mngrClient().getPolicyDefinition_23(id=id)

@register('getDefinitions_24')
def getDefinitions_24():
    return Sdwan_mngrClient().getDefinitions_24()

@register('previewPolicyDefinitionById_24')
def previewPolicyDefinitionById_24(id: str):
    return Sdwan_mngrClient().previewPolicyDefinitionById_24(id=id)

@register('getPolicyDefinition_24')
def getPolicyDefinition_24(id: str):
    return Sdwan_mngrClient().getPolicyDefinition_24(id=id)

@register('getDefinitions_6')
def getDefinitions_6():
    return Sdwan_mngrClient().getDefinitions_6()

@register('previewPolicyDefinitionById_6')
def previewPolicyDefinitionById_6(id: str):
    return Sdwan_mngrClient().previewPolicyDefinitionById_6(id=id)

@register('getPolicyDefinition_6')
def getPolicyDefinition_6(id: str):
    return Sdwan_mngrClient().getPolicyDefinition_6(id=id)

@register('getDefinitions_2')
def getDefinitions_2():
    return Sdwan_mngrClient().getDefinitions_2()

@register('previewPolicyDefinitionById_2')
def previewPolicyDefinitionById_2(id: str):
    return Sdwan_mngrClient().previewPolicyDefinitionById_2(id=id)

@register('getPolicyDefinition_2')
def getPolicyDefinition_2(id: str):
    return Sdwan_mngrClient().getPolicyDefinition_2(id=id)

@register('getDefinitions_7')
def getDefinitions_7():
    return Sdwan_mngrClient().getDefinitions_7()

@register('previewPolicyDefinitionById_7')
def previewPolicyDefinitionById_7(id: str):
    return Sdwan_mngrClient().previewPolicyDefinitionById_7(id=id)

@register('getPolicyDefinition_7')
def getPolicyDefinition_7(id: str):
    return Sdwan_mngrClient().getPolicyDefinition_7(id=id)

@register('getListReference')
def getListReference(listType: str):
    return Sdwan_mngrClient().getListReference(listType=listType)

@register('sgts')
def sgts():
    return Sdwan_mngrClient().sgts()

@register('getAllPolicyLists')
def getAllPolicyLists():
    return Sdwan_mngrClient().getAllPolicyLists()

@register('getPolicyLists_3')
def getPolicyLists_3():
    return Sdwan_mngrClient().getPolicyLists_3()

@register('getPolicyListsWithInfoTag_3')
def getPolicyListsWithInfoTag_3(**kwargs):
    return Sdwan_mngrClient().getPolicyListsWithInfoTag_3(**kwargs)

@register('previewPolicyListById_3')
def previewPolicyListById_3(id: str):
    return Sdwan_mngrClient().previewPolicyListById_3(id=id)

@register('getListsById_3')
def getListsById_3(id: str):
    return Sdwan_mngrClient().getListsById_3(id=id)

@register('getPolicyLists_4')
def getPolicyLists_4():
    return Sdwan_mngrClient().getPolicyLists_4()

@register('getPolicyListsWithInfoTag_4')
def getPolicyListsWithInfoTag_4(**kwargs):
    return Sdwan_mngrClient().getPolicyListsWithInfoTag_4(**kwargs)

@register('previewPolicyListById_4')
def previewPolicyListById_4(id: str):
    return Sdwan_mngrClient().previewPolicyListById_4(id=id)

@register('getListsById_4')
def getListsById_4(id: str):
    return Sdwan_mngrClient().getListsById_4(id=id)

@register('getPolicyLists_5')
def getPolicyLists_5():
    return Sdwan_mngrClient().getPolicyLists_5()

@register('getPolicyListsWithInfoTag_5')
def getPolicyListsWithInfoTag_5(**kwargs):
    return Sdwan_mngrClient().getPolicyListsWithInfoTag_5(**kwargs)

@register('previewPolicyListById_5')
def previewPolicyListById_5(id: str):
    return Sdwan_mngrClient().previewPolicyListById_5(id=id)

@register('getListsById_5')
def getListsById_5(id: str):
    return Sdwan_mngrClient().getListsById_5(id=id)

@register('getPolicyLists_13')
def getPolicyLists_13():
    return Sdwan_mngrClient().getPolicyLists_13()

@register('getPolicyListsWithInfoTag_14')
def getPolicyListsWithInfoTag_14(**kwargs):
    return Sdwan_mngrClient().getPolicyListsWithInfoTag_14(**kwargs)

@register('previewPolicyListById_14')
def previewPolicyListById_14(id: str):
    return Sdwan_mngrClient().previewPolicyListById_14(id=id)

@register('getListsById_14')
def getListsById_14(id: str):
    return Sdwan_mngrClient().getListsById_14(id=id)

@register('getPolicyLists_6')
def getPolicyLists_6():
    return Sdwan_mngrClient().getPolicyLists_6()

@register('getPolicyListsWithInfoTag_6')
def getPolicyListsWithInfoTag_6(**kwargs):
    return Sdwan_mngrClient().getPolicyListsWithInfoTag_6(**kwargs)

@register('previewPolicyListById_6')
def previewPolicyListById_6(id: str):
    return Sdwan_mngrClient().previewPolicyListById_6(id=id)

@register('getListsById_6')
def getListsById_6(id: str):
    return Sdwan_mngrClient().getListsById_6(id=id)

@register('getPolicyLists_7')
def getPolicyLists_7():
    return Sdwan_mngrClient().getPolicyLists_7()

@register('getPolicyListsWithInfoTag_7')
def getPolicyListsWithInfoTag_7(**kwargs):
    return Sdwan_mngrClient().getPolicyListsWithInfoTag_7(**kwargs)

@register('previewPolicyListById_7')
def previewPolicyListById_7(id: str):
    return Sdwan_mngrClient().previewPolicyListById_7(id=id)

@register('getListsById_7')
def getListsById_7(id: str):
    return Sdwan_mngrClient().getListsById_7(id=id)

@register('getPolicyLists_8')
def getPolicyLists_8():
    return Sdwan_mngrClient().getPolicyLists_8()

@register('getPolicyListsWithInfoTag_8')
def getPolicyListsWithInfoTag_8(**kwargs):
    return Sdwan_mngrClient().getPolicyListsWithInfoTag_8(**kwargs)

@register('previewPolicyListById_8')
def previewPolicyListById_8(id: str):
    return Sdwan_mngrClient().previewPolicyListById_8(id=id)

@register('getListsById_8')
def getListsById_8(id: str):
    return Sdwan_mngrClient().getListsById_8(id=id)

@register('getPolicyLists_9')
def getPolicyLists_9():
    return Sdwan_mngrClient().getPolicyLists_9()

@register('getPolicyListsWithInfoTag_10')
def getPolicyListsWithInfoTag_10(**kwargs):
    return Sdwan_mngrClient().getPolicyListsWithInfoTag_10(**kwargs)

@register('previewPolicyListById_10')
def previewPolicyListById_10(id: str):
    return Sdwan_mngrClient().previewPolicyListById_10(id=id)

@register('getListsById_10')
def getListsById_10(id: str):
    return Sdwan_mngrClient().getListsById_10(id=id)

@register('getListsForAllDataPrefixes')
def getListsForAllDataPrefixes():
    return Sdwan_mngrClient().getListsForAllDataPrefixes()

@register('getPolicyListsWithInfoTag_9')
def getPolicyListsWithInfoTag_9(**kwargs):
    return Sdwan_mngrClient().getPolicyListsWithInfoTag_9(**kwargs)

@register('previewPolicyListById_9')
def previewPolicyListById_9(id: str):
    return Sdwan_mngrClient().previewPolicyListById_9(id=id)

@register('getListsById_9')
def getListsById_9(id: str):
    return Sdwan_mngrClient().getListsById_9(id=id)

@register('getAllDataPrefixAndFQDNLists')
def getAllDataPrefixAndFQDNLists():
    return Sdwan_mngrClient().getAllDataPrefixAndFQDNLists()

@register('getPolicyListsWithInfoTag_15')
def getPolicyListsWithInfoTag_15(**kwargs):
    return Sdwan_mngrClient().getPolicyListsWithInfoTag_15(**kwargs)

@register('previewPolicyListById_15')
def previewPolicyListById_15(id: str):
    return Sdwan_mngrClient().previewPolicyListById_15(id=id)

@register('getListsById_15')
def getListsById_15(id: str):
    return Sdwan_mngrClient().getListsById_15(id=id)

@register('getPolicyLists_10')
def getPolicyLists_10():
    return Sdwan_mngrClient().getPolicyLists_10()

@register('getPolicyListsWithInfoTag_11')
def getPolicyListsWithInfoTag_11(**kwargs):
    return Sdwan_mngrClient().getPolicyListsWithInfoTag_11(**kwargs)

@register('previewPolicyListById_11')
def previewPolicyListById_11(id: str):
    return Sdwan_mngrClient().previewPolicyListById_11(id=id)

@register('getListsById_11')
def getListsById_11(id: str):
    return Sdwan_mngrClient().getListsById_11(id=id)

@register('getPolicyLists_11')
def getPolicyLists_11():
    return Sdwan_mngrClient().getPolicyLists_11()

@register('getPolicyListsWithInfoTag_12')
def getPolicyListsWithInfoTag_12(**kwargs):
    return Sdwan_mngrClient().getPolicyListsWithInfoTag_12(**kwargs)

@register('previewPolicyListById_12')
def previewPolicyListById_12(id: str):
    return Sdwan_mngrClient().previewPolicyListById_12(id=id)

@register('getListsById_12')
def getListsById_12(id: str):
    return Sdwan_mngrClient().getListsById_12(id=id)

@register('getPolicyLists_12')
def getPolicyLists_12():
    return Sdwan_mngrClient().getPolicyLists_12()

@register('getPolicyListsWithInfoTag_13')
def getPolicyListsWithInfoTag_13(**kwargs):
    return Sdwan_mngrClient().getPolicyListsWithInfoTag_13(**kwargs)

@register('previewPolicyListById_13')
def previewPolicyListById_13(id: str):
    return Sdwan_mngrClient().previewPolicyListById_13(id=id)

@register('getListsById_13')
def getListsById_13(id: str):
    return Sdwan_mngrClient().getListsById_13(id=id)

@register('getPolicyLists_14')
def getPolicyLists_14():
    return Sdwan_mngrClient().getPolicyLists_14()

@register('getPolicyListsWithInfoTag_16')
def getPolicyListsWithInfoTag_16(**kwargs):
    return Sdwan_mngrClient().getPolicyListsWithInfoTag_16(**kwargs)

@register('previewPolicyListById_16')
def previewPolicyListById_16(id: str):
    return Sdwan_mngrClient().previewPolicyListById_16(id=id)

@register('getListsById_16')
def getListsById_16(id: str):
    return Sdwan_mngrClient().getListsById_16(id=id)

@register('getPolicyLists_15')
def getPolicyLists_15():
    return Sdwan_mngrClient().getPolicyLists_15()

@register('getGeoLocationLists')
def getGeoLocationLists():
    return Sdwan_mngrClient().getGeoLocationLists()

@register('getPolicyListsWithInfoTag_17')
def getPolicyListsWithInfoTag_17(**kwargs):
    return Sdwan_mngrClient().getPolicyListsWithInfoTag_17(**kwargs)

@register('previewPolicyListById_17')
def previewPolicyListById_17(id: str):
    return Sdwan_mngrClient().previewPolicyListById_17(id=id)

@register('getListsById_17')
def getListsById_17(id: str):
    return Sdwan_mngrClient().getListsById_17(id=id)

@register('getPolicyLists_16')
def getPolicyLists_16():
    return Sdwan_mngrClient().getPolicyLists_16()

@register('getPolicyListsWithInfoTag_18')
def getPolicyListsWithInfoTag_18(**kwargs):
    return Sdwan_mngrClient().getPolicyListsWithInfoTag_18(**kwargs)

@register('previewPolicyListById_18')
def previewPolicyListById_18(id: str):
    return Sdwan_mngrClient().previewPolicyListById_18(id=id)

@register('getListsById_18')
def getListsById_18(id: str):
    return Sdwan_mngrClient().getListsById_18(id=id)

@register('getListsForAllPrefixes')
def getListsForAllPrefixes():
    return Sdwan_mngrClient().getListsForAllPrefixes()

@register('getPolicyListsWithInfoTag_21')
def getPolicyListsWithInfoTag_21(**kwargs):
    return Sdwan_mngrClient().getPolicyListsWithInfoTag_21(**kwargs)

@register('previewPolicyListById_21')
def previewPolicyListById_21(id: str):
    return Sdwan_mngrClient().previewPolicyListById_21(id=id)

@register('getListsById_21')
def getListsById_21(id: str):
    return Sdwan_mngrClient().getListsById_21(id=id)

@register('getPolicyLists_17')
def getPolicyLists_17():
    return Sdwan_mngrClient().getPolicyLists_17()

@register('getPolicyListsWithInfoTag_19')
def getPolicyListsWithInfoTag_19(**kwargs):
    return Sdwan_mngrClient().getPolicyListsWithInfoTag_19(**kwargs)

@register('previewPolicyListById_19')
def previewPolicyListById_19(id: str):
    return Sdwan_mngrClient().previewPolicyListById_19(id=id)

@register('getListsById_19')
def getListsById_19(id: str):
    return Sdwan_mngrClient().getListsById_19(id=id)

@register('getPolicyLists_18')
def getPolicyLists_18():
    return Sdwan_mngrClient().getPolicyLists_18()

@register('getPolicyListsWithInfoTag_20')
def getPolicyListsWithInfoTag_20(**kwargs):
    return Sdwan_mngrClient().getPolicyListsWithInfoTag_20(**kwargs)

@register('previewPolicyListById_20')
def previewPolicyListById_20(id: str):
    return Sdwan_mngrClient().previewPolicyListById_20(id=id)

@register('getListsById_20')
def getListsById_20(id: str):
    return Sdwan_mngrClient().getListsById_20(id=id)

@register('getPolicyLists_19')
def getPolicyLists_19():
    return Sdwan_mngrClient().getPolicyLists_19()

@register('getPolicyListsWithInfoTag_22')
def getPolicyListsWithInfoTag_22(**kwargs):
    return Sdwan_mngrClient().getPolicyListsWithInfoTag_22(**kwargs)

@register('previewPolicyListById_22')
def previewPolicyListById_22(id: str):
    return Sdwan_mngrClient().previewPolicyListById_22(id=id)

@register('getListsById_22')
def getListsById_22(id: str):
    return Sdwan_mngrClient().getListsById_22(id=id)

@register('getPolicyLists_20')
def getPolicyLists_20():
    return Sdwan_mngrClient().getPolicyLists_20()

@register('getPolicyListsWithInfoTag_23')
def getPolicyListsWithInfoTag_23(**kwargs):
    return Sdwan_mngrClient().getPolicyListsWithInfoTag_23(**kwargs)

@register('previewPolicyListById_23')
def previewPolicyListById_23(id: str):
    return Sdwan_mngrClient().previewPolicyListById_23(id=id)

@register('getListsById_23')
def getListsById_23(id: str):
    return Sdwan_mngrClient().getListsById_23(id=id)

@register('getPolicyLists')
def getPolicyLists():
    return Sdwan_mngrClient().getPolicyLists()

@register('getPolicyListsWithInfoTag')
def getPolicyListsWithInfoTag(**kwargs):
    return Sdwan_mngrClient().getPolicyListsWithInfoTag(**kwargs)

@register('previewPolicyListById')
def previewPolicyListById(id: str):
    return Sdwan_mngrClient().previewPolicyListById(id=id)

@register('getListsById')
def getListsById(id: str):
    return Sdwan_mngrClient().getListsById(id=id)

@register('getPolicyLists_21')
def getPolicyLists_21():
    return Sdwan_mngrClient().getPolicyLists_21()

@register('getPolicyListsWithInfoTag_24')
def getPolicyListsWithInfoTag_24(**kwargs):
    return Sdwan_mngrClient().getPolicyListsWithInfoTag_24(**kwargs)

@register('previewPolicyListById_24')
def previewPolicyListById_24(id: str):
    return Sdwan_mngrClient().previewPolicyListById_24(id=id)

@register('getListsById_24')
def getListsById_24(id: str):
    return Sdwan_mngrClient().getListsById_24(id=id)

@register('getPolicyLists_22')
def getPolicyLists_22():
    return Sdwan_mngrClient().getPolicyLists_22()

@register('getPolicyListsWithInfoTag_25')
def getPolicyListsWithInfoTag_25(**kwargs):
    return Sdwan_mngrClient().getPolicyListsWithInfoTag_25(**kwargs)

@register('previewPolicyListById_25')
def previewPolicyListById_25(id: str):
    return Sdwan_mngrClient().previewPolicyListById_25(id=id)

@register('getListsById_25')
def getListsById_25(id: str):
    return Sdwan_mngrClient().getListsById_25(id=id)

@register('getPolicyLists_23')
def getPolicyLists_23():
    return Sdwan_mngrClient().getPolicyLists_23()

@register('getPolicyListsWithInfoTag_26')
def getPolicyListsWithInfoTag_26(**kwargs):
    return Sdwan_mngrClient().getPolicyListsWithInfoTag_26(**kwargs)

@register('previewPolicyListById_26')
def previewPolicyListById_26(id: str):
    return Sdwan_mngrClient().previewPolicyListById_26(id=id)

@register('getListsById_26')
def getListsById_26(id: str):
    return Sdwan_mngrClient().getListsById_26(id=id)

@register('getPolicyLists_24')
def getPolicyLists_24():
    return Sdwan_mngrClient().getPolicyLists_24()

@register('getPolicyListsWithInfoTag_27')
def getPolicyListsWithInfoTag_27(**kwargs):
    return Sdwan_mngrClient().getPolicyListsWithInfoTag_27(**kwargs)

@register('previewPolicyListById_27')
def previewPolicyListById_27(id: str):
    return Sdwan_mngrClient().previewPolicyListById_27(id=id)

@register('getListsById_27')
def getListsById_27(id: str):
    return Sdwan_mngrClient().getListsById_27(id=id)

@register('getPolicyLists_25')
def getPolicyLists_25():
    return Sdwan_mngrClient().getPolicyLists_25()

@register('getPolicyListsWithInfoTag_28')
def getPolicyListsWithInfoTag_28(**kwargs):
    return Sdwan_mngrClient().getPolicyListsWithInfoTag_28(**kwargs)

@register('previewPolicyListById_28')
def previewPolicyListById_28(id: str):
    return Sdwan_mngrClient().previewPolicyListById_28(id=id)

@register('getListsById_28')
def getListsById_28(id: str):
    return Sdwan_mngrClient().getListsById_28(id=id)

@register('getPolicyLists_26')
def getPolicyLists_26():
    return Sdwan_mngrClient().getPolicyLists_26()

@register('getPolicyListsWithInfoTag_29')
def getPolicyListsWithInfoTag_29(**kwargs):
    return Sdwan_mngrClient().getPolicyListsWithInfoTag_29(**kwargs)

@register('previewPolicyListById_29')
def previewPolicyListById_29(id: str):
    return Sdwan_mngrClient().previewPolicyListById_29(id=id)

@register('getListsById_29')
def getListsById_29(id: str):
    return Sdwan_mngrClient().getListsById_29(id=id)

@register('getPolicyLists_27')
def getPolicyLists_27():
    return Sdwan_mngrClient().getPolicyLists_27()

@register('getPolicyListsWithInfoTag_30')
def getPolicyListsWithInfoTag_30(**kwargs):
    return Sdwan_mngrClient().getPolicyListsWithInfoTag_30(**kwargs)

@register('previewPolicyListById_30')
def previewPolicyListById_30(id: str):
    return Sdwan_mngrClient().previewPolicyListById_30(id=id)

@register('getListsById_30')
def getListsById_30(id: str):
    return Sdwan_mngrClient().getListsById_30(id=id)

@register('getPolicyLists_28')
def getPolicyLists_28():
    return Sdwan_mngrClient().getPolicyLists_28()

@register('getPolicyListsWithInfoTag_31')
def getPolicyListsWithInfoTag_31(**kwargs):
    return Sdwan_mngrClient().getPolicyListsWithInfoTag_31(**kwargs)

@register('previewPolicyListById_31')
def previewPolicyListById_31(id: str):
    return Sdwan_mngrClient().previewPolicyListById_31(id=id)

@register('getListsById_31')
def getListsById_31(id: str):
    return Sdwan_mngrClient().getListsById_31(id=id)

@register('getPolicyLists_29')
def getPolicyLists_29():
    return Sdwan_mngrClient().getPolicyLists_29()

@register('getPolicyListsWithInfoTag_32')
def getPolicyListsWithInfoTag_32(**kwargs):
    return Sdwan_mngrClient().getPolicyListsWithInfoTag_32(**kwargs)

@register('previewPolicyListById_32')
def previewPolicyListById_32(id: str):
    return Sdwan_mngrClient().previewPolicyListById_32(id=id)

@register('getListsById_32')
def getListsById_32(id: str):
    return Sdwan_mngrClient().getListsById_32(id=id)

@register('getPolicyLists_30')
def getPolicyLists_30():
    return Sdwan_mngrClient().getPolicyLists_30()

@register('getPolicyListsWithInfoTag_33')
def getPolicyListsWithInfoTag_33(**kwargs):
    return Sdwan_mngrClient().getPolicyListsWithInfoTag_33(**kwargs)

@register('previewPolicyListById_33')
def previewPolicyListById_33(id: str):
    return Sdwan_mngrClient().previewPolicyListById_33(id=id)

@register('getListsById_33')
def getListsById_33(id: str):
    return Sdwan_mngrClient().getListsById_33(id=id)

@register('getPolicyLists_31')
def getPolicyLists_31():
    return Sdwan_mngrClient().getPolicyLists_31()

@register('getPolicyListsWithInfoTag_34')
def getPolicyListsWithInfoTag_34(**kwargs):
    return Sdwan_mngrClient().getPolicyListsWithInfoTag_34(**kwargs)

@register('previewPolicyListById_34')
def previewPolicyListById_34(id: str):
    return Sdwan_mngrClient().previewPolicyListById_34(id=id)

@register('getListsById_34')
def getListsById_34(id: str):
    return Sdwan_mngrClient().getListsById_34(id=id)

@register('getPolicyLists_32')
def getPolicyLists_32():
    return Sdwan_mngrClient().getPolicyLists_32()

@register('getPolicyListsWithInfoTag_35')
def getPolicyListsWithInfoTag_35(**kwargs):
    return Sdwan_mngrClient().getPolicyListsWithInfoTag_35(**kwargs)

@register('previewPolicyListById_35')
def previewPolicyListById_35(id: str):
    return Sdwan_mngrClient().previewPolicyListById_35(id=id)

@register('getListsById_35')
def getListsById_35(id: str):
    return Sdwan_mngrClient().getListsById_35(id=id)

@register('getPolicyLists_33')
def getPolicyLists_33():
    return Sdwan_mngrClient().getPolicyLists_33()

@register('getPolicyListsWithInfoTag_36')
def getPolicyListsWithInfoTag_36(**kwargs):
    return Sdwan_mngrClient().getPolicyListsWithInfoTag_36(**kwargs)

@register('previewPolicyListById_36')
def previewPolicyListById_36(id: str):
    return Sdwan_mngrClient().previewPolicyListById_36(id=id)

@register('getListsById_36')
def getListsById_36(id: str):
    return Sdwan_mngrClient().getListsById_36(id=id)

@register('getPolicyLists_34')
def getPolicyLists_34():
    return Sdwan_mngrClient().getPolicyLists_34()

@register('getPolicyListsWithInfoTag_37')
def getPolicyListsWithInfoTag_37(**kwargs):
    return Sdwan_mngrClient().getPolicyListsWithInfoTag_37(**kwargs)

@register('previewPolicyListById_37')
def previewPolicyListById_37(id: str):
    return Sdwan_mngrClient().previewPolicyListById_37(id=id)

@register('getListsById_37')
def getListsById_37(id: str):
    return Sdwan_mngrClient().getListsById_37(id=id)

@register('getPolicyLists_1')
def getPolicyLists_1():
    return Sdwan_mngrClient().getPolicyLists_1()

@register('getPolicyListsWithInfoTag_1')
def getPolicyListsWithInfoTag_1(**kwargs):
    return Sdwan_mngrClient().getPolicyListsWithInfoTag_1(**kwargs)

@register('previewPolicyListById_1')
def previewPolicyListById_1(id: str):
    return Sdwan_mngrClient().previewPolicyListById_1(id=id)

@register('getListsById_1')
def getListsById_1(id: str):
    return Sdwan_mngrClient().getListsById_1(id=id)

@register('getPolicyLists_2')
def getPolicyLists_2():
    return Sdwan_mngrClient().getPolicyLists_2()

@register('getPolicyListsWithInfoTag_2')
def getPolicyListsWithInfoTag_2(**kwargs):
    return Sdwan_mngrClient().getPolicyListsWithInfoTag_2(**kwargs)

@register('previewPolicyListById_2')
def previewPolicyListById_2(id: str):
    return Sdwan_mngrClient().previewPolicyListById_2(id=id)

@register('getListsById_2')
def getListsById_2(id: str):
    return Sdwan_mngrClient().getListsById_2(id=id)

@register('getPolicyLists_35')
def getPolicyLists_35():
    return Sdwan_mngrClient().getPolicyLists_35()

@register('getPolicyListsWithInfoTag_38')
def getPolicyListsWithInfoTag_38(**kwargs):
    return Sdwan_mngrClient().getPolicyListsWithInfoTag_38(**kwargs)

@register('previewPolicyListById_38')
def previewPolicyListById_38(id: str):
    return Sdwan_mngrClient().previewPolicyListById_38(id=id)

@register('getListsById_38')
def getListsById_38(id: str):
    return Sdwan_mngrClient().getListsById_38(id=id)

@register('getPolicyLists_36')
def getPolicyLists_36():
    return Sdwan_mngrClient().getPolicyLists_36()

@register('getPolicyListsWithInfoTag_39')
def getPolicyListsWithInfoTag_39(**kwargs):
    return Sdwan_mngrClient().getPolicyListsWithInfoTag_39(**kwargs)

@register('previewPolicyListById_39')
def previewPolicyListById_39(id: str):
    return Sdwan_mngrClient().previewPolicyListById_39(id=id)

@register('getListsById_39')
def getListsById_39(id: str):
    return Sdwan_mngrClient().getListsById_39(id=id)

@register('getPolicyLists_37')
def getPolicyLists_37():
    return Sdwan_mngrClient().getPolicyLists_37()

@register('getPolicyListsWithInfoTag_40')
def getPolicyListsWithInfoTag_40(**kwargs):
    return Sdwan_mngrClient().getPolicyListsWithInfoTag_40(**kwargs)

@register('previewPolicyListById_40')
def previewPolicyListById_40(id: str):
    return Sdwan_mngrClient().previewPolicyListById_40(id=id)

@register('getListsById_40')
def getListsById_40(id: str):
    return Sdwan_mngrClient().getListsById_40(id=id)

@register('getPolicyLists_38')
def getPolicyLists_38():
    return Sdwan_mngrClient().getPolicyLists_38()

@register('getPolicyListsWithInfoTag_41')
def getPolicyListsWithInfoTag_41(**kwargs):
    return Sdwan_mngrClient().getPolicyListsWithInfoTag_41(**kwargs)

@register('previewPolicyListById_41')
def previewPolicyListById_41(id: str):
    return Sdwan_mngrClient().previewPolicyListById_41(id=id)

@register('getListsById_41')
def getListsById_41(id: str):
    return Sdwan_mngrClient().getListsById_41(id=id)

@register('getPolicyLists_39')
def getPolicyLists_39():
    return Sdwan_mngrClient().getPolicyLists_39()

@register('getPolicyListsWithInfoTag_42')
def getPolicyListsWithInfoTag_42(**kwargs):
    return Sdwan_mngrClient().getPolicyListsWithInfoTag_42(**kwargs)

@register('previewPolicyListById_42')
def previewPolicyListById_42(id: str):
    return Sdwan_mngrClient().previewPolicyListById_42(id=id)

@register('getListsById_42')
def getListsById_42(id: str):
    return Sdwan_mngrClient().getListsById_42(id=id)

@register('getPolicyLists_40')
def getPolicyLists_40():
    return Sdwan_mngrClient().getPolicyLists_40()

@register('getPolicyListsWithInfoTag_43')
def getPolicyListsWithInfoTag_43(**kwargs):
    return Sdwan_mngrClient().getPolicyListsWithInfoTag_43(**kwargs)

@register('previewPolicyListById_43')
def previewPolicyListById_43(id: str):
    return Sdwan_mngrClient().previewPolicyListById_43(id=id)

@register('getListsById_43')
def getListsById_43(id: str):
    return Sdwan_mngrClient().getListsById_43(id=id)

@register('generateSecurityTemplateList')
def generateSecurityTemplateList(**kwargs):
    return Sdwan_mngrClient().generateSecurityTemplateList(**kwargs)

@register('getSecurityTemplate')
def getSecurityTemplate(policyId: str):
    return Sdwan_mngrClient().getSecurityTemplate(policyId=policyId)

@register('getSecurityPolicyDeviceList_1')
def getSecurityPolicyDeviceList_1():
    return Sdwan_mngrClient().getSecurityPolicyDeviceList_1()

@register('getDeviceListById')
def getDeviceListById(policyId: str):
    return Sdwan_mngrClient().getDeviceListById(policyId=policyId)

@register('generateSecurityPolicySummary')
def generateSecurityPolicySummary():
    return Sdwan_mngrClient().generateSecurityPolicySummary()

@register('getSecurityTemplatesForDevice')
def getSecurityTemplatesForDevice(deviceModel: str):
    return Sdwan_mngrClient().getSecurityTemplatesForDevice(deviceModel=deviceModel)

@register('generatePolicyTemplateList')
def generatePolicyTemplateList():
    return Sdwan_mngrClient().generatePolicyTemplateList()

@register('getVEdgeTemplate')
def getVEdgeTemplate(policyId: str):
    return Sdwan_mngrClient().getVEdgeTemplate(policyId=policyId)

@register('getVEdgePolicyDeviceList')
def getVEdgePolicyDeviceList():
    return Sdwan_mngrClient().getVEdgePolicyDeviceList()

@register('getDeviceListByPolicy')
def getDeviceListByPolicy(policyId: str):
    return Sdwan_mngrClient().getDeviceListByPolicy(policyId=policyId)

@register('generateVoiceTemplateList')
def generateVoiceTemplateList():
    return Sdwan_mngrClient().generateVoiceTemplateList()

@register('getTemplateById')
def getTemplateById(policyId: str):
    return Sdwan_mngrClient().getTemplateById(policyId=policyId)

@register('getVoicePolicyDeviceList')
def getVoicePolicyDeviceList():
    return Sdwan_mngrClient().getVoicePolicyDeviceList()

@register('getDeviceListByPolicyId')
def getDeviceListByPolicyId(policyId: str):
    return Sdwan_mngrClient().getDeviceListByPolicyId(policyId=policyId)

@register('generateVoicePolicySummary')
def generateVoicePolicySummary():
    return Sdwan_mngrClient().generateVoicePolicySummary()

@register('getVoiceTemplatesForDevice')
def getVoiceTemplatesForDevice(deviceModel: str):
    return Sdwan_mngrClient().getVoiceTemplatesForDevice(deviceModel=deviceModel)

@register('generateVSmartPolicyTemplateList')
def generateVSmartPolicyTemplateList():
    return Sdwan_mngrClient().generateVSmartPolicyTemplateList()

@register('checkVSmartConnectivityStatus')
def checkVSmartConnectivityStatus():
    return Sdwan_mngrClient().checkVSmartConnectivityStatus()

@register('getTemplateByPolicyId')
def getTemplateByPolicyId(policyId: str):
    return Sdwan_mngrClient().getTemplateByPolicyId(policyId=policyId)

@register('QosmosNbarMigrationWarning')
def QosmosNbarMigrationWarning():
    return Sdwan_mngrClient().QosmosNbarMigrationWarning()

@register('getAllTenants')
def getAllTenants(**kwargs):
    return Sdwan_mngrClient().getAllTenants(**kwargs)

@register('getTenantvSmartMapping')
def getTenantvSmartMapping():
    return Sdwan_mngrClient().getTenantvSmartMapping()

@register('getTenantHostingCapacityOnvSmarts')
def getTenantHostingCapacityOnvSmarts():
    return Sdwan_mngrClient().getTenantHostingCapacityOnvSmarts()

@register('getTenant')
def getTenant(tenantId: str):
    return Sdwan_mngrClient().getTenant(tenantId=tenantId)

@register('downloadExistingBackupFile')
def downloadExistingBackupFile(path: str):
    return Sdwan_mngrClient().downloadExistingBackupFile(path=path)

@register('exportTenantBackup')
def exportTenantBackup():
    return Sdwan_mngrClient().exportTenantBackup()

@register('listTenantBackup')
def listTenantBackup():
    return Sdwan_mngrClient().listTenantBackup()

@register('downloadTenantData')
def downloadTenantData(path: str):
    return Sdwan_mngrClient().downloadTenantData(path=path)

@register('getMigrationToken')
def getMigrationToken(migrationId: str):
    return Sdwan_mngrClient().getMigrationToken(migrationId=migrationId)

@register('reTriggerNetworkMigration')
def reTriggerNetworkMigration():
    return Sdwan_mngrClient().reTriggerNetworkMigration()

@register('getAllTenantStatuses')
def getAllTenantStatuses():
    return Sdwan_mngrClient().getAllTenantStatuses()

@register('createFullTopology')
def createFullTopology():
    return Sdwan_mngrClient().createFullTopology()

@register('createDeviceTopology')
def createDeviceTopology(deviceId: list):
    return Sdwan_mngrClient().createDeviceTopology(deviceId=deviceId)

@register('getSiteTopology')
def getSiteTopology(siteId: str):
    return Sdwan_mngrClient().getSiteTopology(siteId=siteId)

@register('getSiteTopologyMonitorData')
def getSiteTopologyMonitorData(siteId: str):
    return Sdwan_mngrClient().getSiteTopologyMonitorData(siteId=siteId)

@register('createPhysicalTopology')
def createPhysicalTopology(deviceId: list):
    return Sdwan_mngrClient().createPhysicalTopology(deviceId=deviceId)

@register('getControlConnections')
def getControlConnections(uuid: str):
    return Sdwan_mngrClient().getControlConnections(uuid=uuid)

@register('getDeviceConfiguration')
def getDeviceConfiguration(uuid: str):
    return Sdwan_mngrClient().getDeviceConfiguration(uuid=uuid)

@register('getAllKeysFromUmbrella')
def getAllKeysFromUmbrella():
    return Sdwan_mngrClient().getAllKeysFromUmbrella()

@register('getManagementKeysFromUmbrella')
def getManagementKeysFromUmbrella():
    return Sdwan_mngrClient().getManagementKeysFromUmbrella()

@register('getNetworkKeysFromUmbrella')
def getNetworkKeysFromUmbrella():
    return Sdwan_mngrClient().getNetworkKeysFromUmbrella()

@register('getReportingKeysFromUmbrella')
def getReportingKeysFromUmbrella():
    return Sdwan_mngrClient().getReportingKeysFromUmbrella()

@register('sendMetaDataToUmbrella')
def sendMetaDataToUmbrella():
    return Sdwan_mngrClient().sendMetaDataToUmbrella()

@register('getStatus')
def getStatus():
    return Sdwan_mngrClient().getStatus()

@register('getUrlMonitor')
def getUrlMonitor():
    return Sdwan_mngrClient().getUrlMonitor()

@register('returnMetric')
def returnMetric(metricName: str, startDate: str, **kwargs):
    return Sdwan_mngrClient().returnMetric(metricName=metricName, startDate=startDate, **kwargs)

@register('returnMetricFiles')
def returnMetricFiles(metricName: str, startDate: str, **kwargs):
    return Sdwan_mngrClient().returnMetricFiles(metricName=metricName, startDate=startDate, **kwargs)

@register('getMetricsList')
def getMetricsList():
    return Sdwan_mngrClient().getMetricsList()

@register('getDBSizeOnFile')
def getDBSizeOnFile():
    return Sdwan_mngrClient().getDBSizeOnFile()

@register('listLogFileDetails')
def listLogFileDetails():
    return Sdwan_mngrClient().listLogFileDetails()

@register('listVManageServerLogLastNLines')
def listVManageServerLogLastNLines(**kwargs):
    return Sdwan_mngrClient().listVManageServerLogLastNLines(**kwargs)

@register('listConfigurations')
def listConfigurations():
    return Sdwan_mngrClient().listConfigurations()

@register('listLoggers')
def listLoggers():
    return Sdwan_mngrClient().listLoggers()

@register('getStatsMigrationRangeConfig')
def getStatsMigrationRangeConfig():
    return Sdwan_mngrClient().getStatsMigrationRangeConfig()

@register('getStatsMigrationSettings')
def getStatsMigrationSettings():
    return Sdwan_mngrClient().getStatsMigrationSettings()

@register('getStatsMigrationStatsDbInfo')
def getStatsMigrationStatsDbInfo():
    return Sdwan_mngrClient().getStatsMigrationStatsDbInfo()

@register('getStatsMigrationStatus')
def getStatsMigrationStatus():
    return Sdwan_mngrClient().getStatsMigrationStatus()

@register('getCloudOnRampSaasStatus')
def getCloudOnRampSaasStatus():
    return Sdwan_mngrClient().getCloudOnRampSaasStatus()

@register('getCloudTunnelList')
def getCloudTunnelList(deviceIp: str):
    return Sdwan_mngrClient().getCloudTunnelList(deviceIp=deviceIp)

@register('getPolicyGroupsWithCorSaasApps')
def getPolicyGroupsWithCorSaasApps():
    return Sdwan_mngrClient().getPolicyGroupsWithCorSaasApps()

@register('getCorSitesPerDevice')
def getCorSitesPerDevice():
    return Sdwan_mngrClient().getCorSitesPerDevice()

@register('getInactiveCorSaasSites')
def getInactiveCorSaasSites():
    return Sdwan_mngrClient().getInactiveCorSaasSites()

@register('getLegacyDeviceList')
def getLegacyDeviceList():
    return Sdwan_mngrClient().getLegacyDeviceList()

@register('getCorSaasStatusPerDevice')
def getCorSaasStatusPerDevice(deviceIp: str):
    return Sdwan_mngrClient().getCorSaasStatusPerDevice(deviceIp=deviceIp)

@register('getWebexSyncStatus')
def getWebexSyncStatus():
    return Sdwan_mngrClient().getWebexSyncStatus()

@register('GetConfigGroupBySolution')
def GetConfigGroupBySolution(**kwargs):
    return Sdwan_mngrClient().GetConfigGroupBySolution(**kwargs)

@register('GetConfigGroup')
def GetConfigGroup(configGroupId: str, **kwargs):
    return Sdwan_mngrClient().GetConfigGroup(configGroupId=configGroupId, **kwargs)

@register('GetConfigGroupAssociation')
def GetConfigGroupAssociation(configGroupId: str):
    return Sdwan_mngrClient().GetConfigGroupAssociation(configGroupId=configGroupId)

@register('getConfigGroupDeviceVariables')
def getConfigGroupDeviceVariables(configGroupId: str, **kwargs):
    return Sdwan_mngrClient().getConfigGroupDeviceVariables(configGroupId=configGroupId, **kwargs)

@register('getConfigGroupDeviceVariablesSchema')
def getConfigGroupDeviceVariablesSchema(configGroupId: str, **kwargs):
    return Sdwan_mngrClient().getConfigGroupDeviceVariablesSchema(configGroupId=configGroupId, **kwargs)

@register('getRuleAssociationByConfigGroupId')
def getRuleAssociationByConfigGroupId(configGroupId: str):
    return Sdwan_mngrClient().getRuleAssociationByConfigGroupId(configGroupId=configGroupId)

@register('getRunningIosCliConfig')
def getRunningIosCliConfig(deviceUUID: str):
    return Sdwan_mngrClient().getRunningIosCliConfig(deviceUUID=deviceUUID)

@register('getUnsupportedCliConfig')
def getUnsupportedCliConfig(deviceUUID: str, **kwargs):
    return Sdwan_mngrClient().getUnsupportedCliConfig(deviceUUID=deviceUUID, **kwargs)

@register('GetMobilityCliFeatureProfile')
def GetMobilityCliFeatureProfile(**kwargs):
    return Sdwan_mngrClient().GetMobilityCliFeatureProfile(**kwargs)

@register('GetMobilityCliFeatureProfileByCliId')
def GetMobilityCliFeatureProfileByCliId(cliId: str):
    return Sdwan_mngrClient().GetMobilityCliFeatureProfileByCliId(cliId=cliId)

@register('GetAllConfigFeatureForMobility')
def GetAllConfigFeatureForMobility(cliId: str):
    return Sdwan_mngrClient().GetAllConfigFeatureForMobility(cliId=cliId)

@register('GetConfigFeatureForMobilityByParcelId')
def GetConfigFeatureForMobilityByParcelId(cliId: str, configId: str):
    return Sdwan_mngrClient().GetConfigFeatureForMobilityByParcelId(cliId=cliId, configId=configId)

@register('GetMobilityGlobalFeatureProfile')
def GetMobilityGlobalFeatureProfile(**kwargs):
    return Sdwan_mngrClient().GetMobilityGlobalFeatureProfile(**kwargs)

@register('GetMobilityGlobalBasicParcelSchemaBySchemaType')
def GetMobilityGlobalBasicParcelSchemaBySchemaType(schemaType: str):
    return Sdwan_mngrClient().GetMobilityGlobalBasicParcelSchemaBySchemaType(schemaType=schemaType)

@register('GetMobilityFeatureProfileByGlobalId')
def GetMobilityFeatureProfileByGlobalId(globalId: str):
    return Sdwan_mngrClient().GetMobilityFeatureProfileByGlobalId(globalId=globalId)

@register('GetQosFeatureForGlobal')
def GetQosFeatureForGlobal(globalId: str):
    return Sdwan_mngrClient().GetQosFeatureForGlobal(globalId=globalId)

@register('GetQosFeatureByParcelIdForGlobal')
def GetQosFeatureByParcelIdForGlobal(globalId: str, qosId: str):
    return Sdwan_mngrClient().GetQosFeatureByParcelIdForGlobal(globalId=globalId, qosId=qosId)

@register('GetAaaServersProfileParcelForMobility')
def GetAaaServersProfileParcelForMobility(profileId: str):
    return Sdwan_mngrClient().GetAaaServersProfileParcelForMobility(profileId=profileId)

@register('GetAaaServersProfileParcelByParcelIdForMobility')
def GetAaaServersProfileParcelByParcelIdForMobility(aaaserversId: str, profileId: str):
    return Sdwan_mngrClient().GetAaaServersProfileParcelByParcelIdForMobility(aaaserversId=aaaserversId, profileId=profileId)

@register('GetBasicProfileParcelForMobility')
def GetBasicProfileParcelForMobility(profileId: str):
    return Sdwan_mngrClient().GetBasicProfileParcelForMobility(profileId=profileId)

@register('GetBasicProfileParcelByParcelIdForMobility')
def GetBasicProfileParcelByParcelIdForMobility(parcelId: str, profileId: str):
    return Sdwan_mngrClient().GetBasicProfileParcelByParcelIdForMobility(parcelId=parcelId, profileId=profileId)

@register('GetCellularProfileParcelListForMobility')
def GetCellularProfileParcelListForMobility(profileId: str):
    return Sdwan_mngrClient().GetCellularProfileParcelListForMobility(profileId=profileId)

@register('GetCellularProfileParcelForMobility')
def GetCellularProfileParcelForMobility(cellularId: str, profileId: str):
    return Sdwan_mngrClient().GetCellularProfileParcelForMobility(cellularId=cellularId, profileId=profileId)

@register('GetEsimCellularProfileFeatureForMobility')
def GetEsimCellularProfileFeatureForMobility(profileId: str):
    return Sdwan_mngrClient().GetEsimCellularProfileFeatureForMobility(profileId=profileId)

@register('GetEsimCellularProfileFeatureByEsimCellularIdForMobility')
def GetEsimCellularProfileFeatureByEsimCellularIdForMobility(esimCellularId: str, profileId: str):
    return Sdwan_mngrClient().GetEsimCellularProfileFeatureByEsimCellularIdForMobility(esimCellularId=esimCellularId, profileId=profileId)

@register('GetEthernetProfileParcels')
def GetEthernetProfileParcels(profileId: str):
    return Sdwan_mngrClient().GetEthernetProfileParcels(profileId=profileId)

@register('GetEthernetProfileParcel')
def GetEthernetProfileParcel(ethernetId: str, profileId: str):
    return Sdwan_mngrClient().GetEthernetProfileParcel(ethernetId=ethernetId, profileId=profileId)

@register('GetLoggingProfileFeatureForMobility')
def GetLoggingProfileFeatureForMobility(profileId: str):
    return Sdwan_mngrClient().GetLoggingProfileFeatureForMobility(profileId=profileId)

@register('GetLoggingProfileFeatureByFeatureIdForMobility')
def GetLoggingProfileFeatureByFeatureIdForMobility(loggingId: str, profileId: str):
    return Sdwan_mngrClient().GetLoggingProfileFeatureByFeatureIdForMobility(loggingId=loggingId, profileId=profileId)

@register('GetNetworkProtocolProfileParcelListForMobility')
def GetNetworkProtocolProfileParcelListForMobility(profileId: str):
    return Sdwan_mngrClient().GetNetworkProtocolProfileParcelListForMobility(profileId=profileId)

@register('GetNetworkProtocolProfileParcelForMobility')
def GetNetworkProtocolProfileParcelForMobility(networkProtocolId: str, profileId: str):
    return Sdwan_mngrClient().GetNetworkProtocolProfileParcelForMobility(networkProtocolId=networkProtocolId, profileId=profileId)

@register('GetSecurityPolicyProfileParcelListForMobility')
def GetSecurityPolicyProfileParcelListForMobility(profileId: str):
    return Sdwan_mngrClient().GetSecurityPolicyProfileParcelListForMobility(profileId=profileId)

@register('GetSecurityPolicyProfileParcelForMobility')
def GetSecurityPolicyProfileParcelForMobility(profileId: str, securityPolicyId: str):
    return Sdwan_mngrClient().GetSecurityPolicyProfileParcelForMobility(profileId=profileId, securityPolicyId=securityPolicyId)

@register('GetVpnProfileParcelForMobility')
def GetVpnProfileParcelForMobility(profileId: str):
    return Sdwan_mngrClient().GetVpnProfileParcelForMobility(profileId=profileId)

@register('GetVpnProfileParcelByParcelIdForMobility')
def GetVpnProfileParcelByParcelIdForMobility(profileId: str, vpnId: str):
    return Sdwan_mngrClient().GetVpnProfileParcelByParcelIdForMobility(profileId=profileId, vpnId=vpnId)

@register('GetWifiProfileParcelListForMobility')
def GetWifiProfileParcelListForMobility(profileId: str):
    return Sdwan_mngrClient().GetWifiProfileParcelListForMobility(profileId=profileId)

@register('GetWifiProfileParcelForMobility')
def GetWifiProfileParcelForMobility(profileId: str, wifiId: str):
    return Sdwan_mngrClient().GetWifiProfileParcelForMobility(profileId=profileId, wifiId=wifiId)

@register('GetAllNfvirtualCLIFeatureProfiles')
def GetAllNfvirtualCLIFeatureProfiles(**kwargs):
    return Sdwan_mngrClient().GetAllNfvirtualCLIFeatureProfiles(**kwargs)

@register('GetNfvirtualCLIFeatureProfileByid')
def GetNfvirtualCLIFeatureProfileByid(cliId: str):
    return Sdwan_mngrClient().GetNfvirtualCLIFeatureProfileByid(cliId=cliId)

@register('getNfvirtualCLIParcel')
def getNfvirtualCLIParcel(cliId: str, configId: str):
    return Sdwan_mngrClient().getNfvirtualCLIParcel(cliId=cliId, configId=configId)

@register('GetAllNfvirtualNetworksFeatureProfiles')
def GetAllNfvirtualNetworksFeatureProfiles(limit: int, offset: int):
    return Sdwan_mngrClient().GetAllNfvirtualNetworksFeatureProfiles(limit=limit, offset=offset)

@register('GetAllNfvirtualOvsNetworksFeatureProfileByProfileId')
def GetAllNfvirtualOvsNetworksFeatureProfileByProfileId(details: bool, networkId: str):
    return Sdwan_mngrClient().GetAllNfvirtualOvsNetworksFeatureProfileByProfileId(details=details, networkId=networkId)

@register('GetNfvirtualNetworksFeatureProfileByProfileId')
def GetNfvirtualNetworksFeatureProfileByProfileId(details: bool, networkId: str):
    return Sdwan_mngrClient().GetNfvirtualNetworksFeatureProfileByProfileId(details=details, networkId=networkId)

@register('GetNfvirtualLANParcel')
def GetNfvirtualLANParcel(lanId: str, networksId: str):
    return Sdwan_mngrClient().GetNfvirtualLANParcel(lanId=lanId, networksId=networksId)

@register('GetNfvirtualOVSNetworkParcel')
def GetNfvirtualOVSNetworkParcel(networksId: str, ovsNetworkId: str):
    return Sdwan_mngrClient().GetNfvirtualOVSNetworkParcel(networksId=networksId, ovsNetworkId=ovsNetworkId)

@register('GetNfvirtualRoutesParcel')
def GetNfvirtualRoutesParcel(networksId: str, routesId: str):
    return Sdwan_mngrClient().GetNfvirtualRoutesParcel(networksId=networksId, routesId=routesId)

@register('GetNfvirtualSwitchParcel')
def GetNfvirtualSwitchParcel(networksId: str, switchId: str):
    return Sdwan_mngrClient().GetNfvirtualSwitchParcel(networksId=networksId, switchId=switchId)

@register('GetNfvirtualVNFAttributesParcel')
def GetNfvirtualVNFAttributesParcel(networksId: str, vnfAttributesId: str):
    return Sdwan_mngrClient().GetNfvirtualVNFAttributesParcel(networksId=networksId, vnfAttributesId=vnfAttributesId)

@register('GetNfvirtualVNFParcel')
def GetNfvirtualVNFParcel(networksId: str, vnfAttributesId: str, vnfId: str):
    return Sdwan_mngrClient().GetNfvirtualVNFParcel(networksId=networksId, vnfAttributesId=vnfAttributesId, vnfId=vnfId)

@register('GetNfvirtualWANParcel')
def GetNfvirtualWANParcel(networksId: str, wanId: str):
    return Sdwan_mngrClient().GetNfvirtualWANParcel(networksId=networksId, wanId=wanId)

@register('GetAllNfvirtualSystemFeatureProfiles')
def GetAllNfvirtualSystemFeatureProfiles(**kwargs):
    return Sdwan_mngrClient().GetAllNfvirtualSystemFeatureProfiles(**kwargs)

@register('GetNfvirtualSystemFeatureProfileByProfileId')
def GetNfvirtualSystemFeatureProfileByProfileId(systemId: str):
    return Sdwan_mngrClient().GetNfvirtualSystemFeatureProfileByProfileId(systemId=systemId)

@register('GetNfvirtualAAAParcel')
def GetNfvirtualAAAParcel(aaaId: str, systemId: str):
    return Sdwan_mngrClient().GetNfvirtualAAAParcel(aaaId=aaaId, systemId=systemId)

@register('GetNfvirtualBannerParcel')
def GetNfvirtualBannerParcel(bannerId: str, systemId: str):
    return Sdwan_mngrClient().GetNfvirtualBannerParcel(bannerId=bannerId, systemId=systemId)

@register('GetNfvirtualLoggingParcel')
def GetNfvirtualLoggingParcel(loggingId: str, systemId: str):
    return Sdwan_mngrClient().GetNfvirtualLoggingParcel(loggingId=loggingId, systemId=systemId)

@register('GetNfvirtualNTPParcel')
def GetNfvirtualNTPParcel(ntpId: str, systemId: str):
    return Sdwan_mngrClient().GetNfvirtualNTPParcel(ntpId=ntpId, systemId=systemId)

@register('GetNfvirtualSNMPParcel')
def GetNfvirtualSNMPParcel(snmpId: str, systemId: str):
    return Sdwan_mngrClient().GetNfvirtualSNMPParcel(snmpId=snmpId, systemId=systemId)

@register('GetNfvirtualSystemSettingsParcel')
def GetNfvirtualSystemSettingsParcel(systemId: str, systemSettingsId: str):
    return Sdwan_mngrClient().GetNfvirtualSystemSettingsParcel(systemId=systemId, systemSettingsId=systemSettingsId)

@register('GetSdroutingFeatureProfiles')
def GetSdroutingFeatureProfiles(**kwargs):
    return Sdwan_mngrClient().GetSdroutingFeatureProfiles(**kwargs)

@register('GetSdroutingCliFeatureProfiles')
def GetSdroutingCliFeatureProfiles(**kwargs):
    return Sdwan_mngrClient().GetSdroutingCliFeatureProfiles(**kwargs)

@register('Get')
def Get(**kwargs):
    return Sdwan_mngrClient().Get(**kwargs)

@register('GetSdroutingCliFeatureProfile')
def GetSdroutingCliFeatureProfile(cliId: str):
    return Sdwan_mngrClient().GetSdroutingCliFeatureProfile(cliId=cliId)

@register('GetSdroutingCLIAddOnFeatures')
def GetSdroutingCLIAddOnFeatures(cliId: str):
    return Sdwan_mngrClient().GetSdroutingCLIAddOnFeatures(cliId=cliId)

@register('GetSdroutingCLIAddOnFeature')
def GetSdroutingCLIAddOnFeature(cliId: str, configId: str):
    return Sdwan_mngrClient().GetSdroutingCLIAddOnFeature(cliId=cliId, configId=configId)

@register('GetSdroutingCliConfigGroupFeatures')
def GetSdroutingCliConfigGroupFeatures(cliId: str):
    return Sdwan_mngrClient().GetSdroutingCliConfigGroupFeatures(cliId=cliId)

@register('GetSdroutingCliConfigGroupFeature')
def GetSdroutingCliConfigGroupFeature(cliId: str, fullConfigId: str):
    return Sdwan_mngrClient().GetSdroutingCliConfigGroupFeature(cliId=cliId, fullConfigId=fullConfigId)

@register('GetSdroutingIosCLassicCLIAddOnFeatures')
def GetSdroutingIosCLassicCLIAddOnFeatures(cliId: str):
    return Sdwan_mngrClient().GetSdroutingIosCLassicCLIAddOnFeatures(cliId=cliId)

@register('GetSdroutingIosClassicCLIAddOnFeature')
def GetSdroutingIosClassicCLIAddOnFeature(cliId: str, iosConfigId: str):
    return Sdwan_mngrClient().GetSdroutingIosClassicCLIAddOnFeature(cliId=cliId, iosConfigId=iosConfigId)

@register('GetSdRoutingEmbeddedSecurityFeatureProfiles')
def GetSdRoutingEmbeddedSecurityFeatureProfiles(**kwargs):
    return Sdwan_mngrClient().GetSdRoutingEmbeddedSecurityFeatureProfiles(**kwargs)

@register('GetSdRoutingEmbeddedSecurityFeatureProfileByProfileId')
def GetSdRoutingEmbeddedSecurityFeatureProfileByProfileId(embeddedSecurityId: str, **kwargs):
    return Sdwan_mngrClient().GetSdRoutingEmbeddedSecurityFeatureProfileByProfileId(embeddedSecurityId=embeddedSecurityId, **kwargs)

@register('GetSecurityFeature')
def GetSecurityFeature(securityId: str):
    return Sdwan_mngrClient().GetSecurityFeature(securityId=securityId)

@register('GetSecurityFeatureByFeatureId')
def GetSecurityFeatureByFeatureId(securityId: str, securityProfileParcelId: str):
    return Sdwan_mngrClient().GetSecurityFeatureByFeatureId(securityId=securityId, securityProfileParcelId=securityProfileParcelId)

@register('GetNgfirewallFeature')
def GetNgfirewallFeature(securityId: str):
    return Sdwan_mngrClient().GetNgfirewallFeature(securityId=securityId)

@register('GetNgfirewallFeatureByFeatureId')
def GetNgfirewallFeatureByFeatureId(securityId: str, securityProfileParcelId: str):
    return Sdwan_mngrClient().GetNgfirewallFeatureByFeatureId(securityId=securityId, securityProfileParcelId=securityProfileParcelId)

@register('GetCybervisionProfileFeatureForOther')
def GetCybervisionProfileFeatureForOther(otherId: str):
    return Sdwan_mngrClient().GetCybervisionProfileFeatureForOther(otherId=otherId)

@register('GetCybervisionProfileFeatureByFeatureIdForOther')
def GetCybervisionProfileFeatureByFeatureIdForOther(cybervisionId: str, otherId: str):
    return Sdwan_mngrClient().GetCybervisionProfileFeatureByFeatureIdForOther(cybervisionId=cybervisionId, otherId=otherId)

@register('GetSdroutingServiceFeatureProfiles')
def GetSdroutingServiceFeatureProfiles(**kwargs):
    return Sdwan_mngrClient().GetSdroutingServiceFeatureProfiles(**kwargs)

@register('GetSdroutingServiceFeatureProfile')
def GetSdroutingServiceFeatureProfile(serviceId: str):
    return Sdwan_mngrClient().GetSdroutingServiceFeatureProfile(serviceId=serviceId)

@register('GetSdroutingDhcpServerProfileParcels')
def GetSdroutingDhcpServerProfileParcels(serviceId: str):
    return Sdwan_mngrClient().GetSdroutingDhcpServerProfileParcels(serviceId=serviceId)

@register('GetSdroutingDhcpServerProfileParcel')
def GetSdroutingDhcpServerProfileParcel(dhcpServerId: str, serviceId: str):
    return Sdwan_mngrClient().GetSdroutingDhcpServerProfileParcel(dhcpServerId=dhcpServerId, serviceId=serviceId)

@register('GetSdroutingServiceIpsecProfileFeatures')
def GetSdroutingServiceIpsecProfileFeatures(serviceId: str):
    return Sdwan_mngrClient().GetSdroutingServiceIpsecProfileFeatures(serviceId=serviceId)

@register('GetSdroutingServiceIpsecProfileFeature')
def GetSdroutingServiceIpsecProfileFeature(ipsecProfileId: str, serviceId: str):
    return Sdwan_mngrClient().GetSdroutingServiceIpsecProfileFeature(ipsecProfileId=ipsecProfileId, serviceId=serviceId)

@register('GetSdroutingServiceIpv4AclFeatures')
def GetSdroutingServiceIpv4AclFeatures(serviceId: str):
    return Sdwan_mngrClient().GetSdroutingServiceIpv4AclFeatures(serviceId=serviceId)

@register('GetSdroutingServiceIpv4AclFeature')
def GetSdroutingServiceIpv4AclFeature(ipv4AclId: str, serviceId: str):
    return Sdwan_mngrClient().GetSdroutingServiceIpv4AclFeature(ipv4AclId=ipv4AclId, serviceId=serviceId)

@register('GetListOfProfileParcels')
def GetListOfProfileParcels(serviceId: str):
    return Sdwan_mngrClient().GetListOfProfileParcels(serviceId=serviceId)

@register('GetMultiCloudConnection')
def GetMultiCloudConnection(multiCloudConnectionId: str, serviceId: str):
    return Sdwan_mngrClient().GetMultiCloudConnection(multiCloudConnectionId=multiCloudConnectionId, serviceId=serviceId)

@register('GetSdroutingServiceObjectTrackerFeatures')
def GetSdroutingServiceObjectTrackerFeatures(serviceId: str):
    return Sdwan_mngrClient().GetSdroutingServiceObjectTrackerFeatures(serviceId=serviceId)

@register('GetSdroutingServiceObjectTrackerFeature')
def GetSdroutingServiceObjectTrackerFeature(objectTrackerId: str, serviceId: str):
    return Sdwan_mngrClient().GetSdroutingServiceObjectTrackerFeature(objectTrackerId=objectTrackerId, serviceId=serviceId)

@register('GetSdroutingServiceObjectTrackerGroupFeatures')
def GetSdroutingServiceObjectTrackerGroupFeatures(serviceId: str):
    return Sdwan_mngrClient().GetSdroutingServiceObjectTrackerGroupFeatures(serviceId=serviceId)

@register('GetSdroutingServiceObjectTrackerGroupFeature')
def GetSdroutingServiceObjectTrackerGroupFeature(objectTrackerGroupId: str, serviceId: str):
    return Sdwan_mngrClient().GetSdroutingServiceObjectTrackerGroupFeature(objectTrackerGroupId=objectTrackerGroupId, serviceId=serviceId)

@register('GetSdroutingServiceRoutePolicyFeatures')
def GetSdroutingServiceRoutePolicyFeatures(serviceId: str):
    return Sdwan_mngrClient().GetSdroutingServiceRoutePolicyFeatures(serviceId=serviceId)

@register('GetSdroutingServiceRoutePolicyFeature')
def GetSdroutingServiceRoutePolicyFeature(routePolicyId: str, serviceId: str):
    return Sdwan_mngrClient().GetSdroutingServiceRoutePolicyFeature(routePolicyId=routePolicyId, serviceId=serviceId)

@register('GetSdroutingServiceVrfOspfFeatures')
def GetSdroutingServiceVrfOspfFeatures(serviceId: str):
    return Sdwan_mngrClient().GetSdroutingServiceVrfOspfFeatures(serviceId=serviceId)

@register('GetSdroutingServiceVrfOspfFeature')
def GetSdroutingServiceVrfOspfFeature(ospfId: str, serviceId: str):
    return Sdwan_mngrClient().GetSdroutingServiceVrfOspfFeature(ospfId=ospfId, serviceId=serviceId)

@register('GetSdroutingServiceVrfOspfv3Ipv4Features')
def GetSdroutingServiceVrfOspfv3Ipv4Features(serviceId: str):
    return Sdwan_mngrClient().GetSdroutingServiceVrfOspfv3Ipv4Features(serviceId=serviceId)

@register('GetSdroutingServiceVrfOspfv3Ipv4Feature')
def GetSdroutingServiceVrfOspfv3Ipv4Feature(ospfv3Id: str, serviceId: str):
    return Sdwan_mngrClient().GetSdroutingServiceVrfOspfv3Ipv4Feature(ospfv3Id=ospfv3Id, serviceId=serviceId)

@register('GetSdroutingServiceVrfOspfv3Ipv6Features')
def GetSdroutingServiceVrfOspfv3Ipv6Features(serviceId: str):
    return Sdwan_mngrClient().GetSdroutingServiceVrfOspfv3Ipv6Features(serviceId=serviceId)

@register('GetSdroutingServiceVrfOspfv3Ipv6Feature')
def GetSdroutingServiceVrfOspfv3Ipv6Feature(ospfv3Id: str, serviceId: str):
    return Sdwan_mngrClient().GetSdroutingServiceVrfOspfv3Ipv6Feature(ospfv3Id=ospfv3Id, serviceId=serviceId)

@register('GetSdroutingServiceVRFFeatures')
def GetSdroutingServiceVRFFeatures(serviceId: str):
    return Sdwan_mngrClient().GetSdroutingServiceVRFFeatures(serviceId=serviceId)

@register('GetSdroutingServiceVrfBgpFeatures')
def GetSdroutingServiceVrfBgpFeatures(serviceId: str):
    return Sdwan_mngrClient().GetSdroutingServiceVrfBgpFeatures(serviceId=serviceId)

@register('GetSdroutingServiceVrfBgpFeature')
def GetSdroutingServiceVrfBgpFeature(bgpId: str, serviceId: str):
    return Sdwan_mngrClient().GetSdroutingServiceVrfBgpFeature(bgpId=bgpId, serviceId=serviceId)

@register('GetSdroutingServiceVrfEigrpFeatures')
def GetSdroutingServiceVrfEigrpFeatures(serviceId: str):
    return Sdwan_mngrClient().GetSdroutingServiceVrfEigrpFeatures(serviceId=serviceId)

@register('GetSdroutingServiceVrfEigrpFeature')
def GetSdroutingServiceVrfEigrpFeature(eigrpId: str, serviceId: str):
    return Sdwan_mngrClient().GetSdroutingServiceVrfEigrpFeature(eigrpId=eigrpId, serviceId=serviceId)

@register('GetSdroutingServiceVRFFeature')
def GetSdroutingServiceVRFFeature(serviceId: str, vrfId: str):
    return Sdwan_mngrClient().GetSdroutingServiceVRFFeature(serviceId=serviceId, vrfId=vrfId)

@register('GetSdroutingServiceVRFDmvpnTunnelFeatures')
def GetSdroutingServiceVRFDmvpnTunnelFeatures(serviceId: str, vrfId: str):
    return Sdwan_mngrClient().GetSdroutingServiceVRFDmvpnTunnelFeatures(serviceId=serviceId, vrfId=vrfId)

@register('GetSdroutingServiceVRFDmvpnTunnelFeature')
def GetSdroutingServiceVRFDmvpnTunnelFeature(serviceId: str, tunnelId: str, vrfId: str):
    return Sdwan_mngrClient().GetSdroutingServiceVRFDmvpnTunnelFeature(serviceId=serviceId, tunnelId=tunnelId, vrfId=vrfId)

@register('GetSdroutingServiceVrfInterfaceEthernetFeaturesForService')
def GetSdroutingServiceVrfInterfaceEthernetFeaturesForService(serviceId: str, vrfId: str):
    return Sdwan_mngrClient().GetSdroutingServiceVrfInterfaceEthernetFeaturesForService(serviceId=serviceId, vrfId=vrfId)

@register('GetSdroutingServiceVrfInterfaceEthernetFeatureByFeatureIdForService')
def GetSdroutingServiceVrfInterfaceEthernetFeatureByFeatureIdForService(ethernetId: str, serviceId: str, vrfId: str):
    return Sdwan_mngrClient().GetSdroutingServiceVrfInterfaceEthernetFeatureByFeatureIdForService(ethernetId=ethernetId, serviceId=serviceId, vrfId=vrfId)

@register('GetVrfInterfaceEthernetAssociatedDhcpServerParcelsForService')
def GetVrfInterfaceEthernetAssociatedDhcpServerParcelsForService(ethernetId: str, serviceId: str, vrfId: str):
    return Sdwan_mngrClient().GetVrfInterfaceEthernetAssociatedDhcpServerParcelsForService(ethernetId=ethernetId, serviceId=serviceId, vrfId=vrfId)

@register('GetVrfInterfaceEthernetAssociatedDhcpServerParcelByFeatureIdForService')
def GetVrfInterfaceEthernetAssociatedDhcpServerParcelByFeatureIdForService(dhcpServerId: str, ethernetId: str, serviceId: str, vrfId: str):
    return Sdwan_mngrClient().GetVrfInterfaceEthernetAssociatedDhcpServerParcelByFeatureIdForService(dhcpServerId=dhcpServerId, ethernetId=ethernetId, serviceId=serviceId, vrfId=vrfId)

@register('GetSdroutingServiceVrfInterfaceIpsecFeaturesForService')
def GetSdroutingServiceVrfInterfaceIpsecFeaturesForService(serviceId: str, vrfId: str):
    return Sdwan_mngrClient().GetSdroutingServiceVrfInterfaceIpsecFeaturesForService(serviceId=serviceId, vrfId=vrfId)

@register('GetSdroutingServiceVrfInterfaceIpsecFeatureByFeatureIdForService')
def GetSdroutingServiceVrfInterfaceIpsecFeatureByFeatureIdForService(ipsecId: str, serviceId: str, vrfId: str):
    return Sdwan_mngrClient().GetSdroutingServiceVrfInterfaceIpsecFeatureByFeatureIdForService(ipsecId=ipsecId, serviceId=serviceId, vrfId=vrfId)

@register('GetServiceVrfAssociatedRoutingBgpFeatures')
def GetServiceVrfAssociatedRoutingBgpFeatures(serviceId: str, vrfId: str):
    return Sdwan_mngrClient().GetServiceVrfAssociatedRoutingBgpFeatures(serviceId=serviceId, vrfId=vrfId)

@register('GetServiceVrfAssociatedRoutingBgpParcelByParcelId')
def GetServiceVrfAssociatedRoutingBgpParcelByParcelId(bgpId: str, serviceId: str, vrfId: str):
    return Sdwan_mngrClient().GetServiceVrfAssociatedRoutingBgpParcelByParcelId(bgpId=bgpId, serviceId=serviceId, vrfId=vrfId)

@register('GetServiceVrfAssociatedRoutingEigrpFeatures')
def GetServiceVrfAssociatedRoutingEigrpFeatures(serviceId: str, vrfId: str):
    return Sdwan_mngrClient().GetServiceVrfAssociatedRoutingEigrpFeatures(serviceId=serviceId, vrfId=vrfId)

@register('GetServiceVrfAssociatedRoutingEigrpFeatureByFeatureId')
def GetServiceVrfAssociatedRoutingEigrpFeatureByFeatureId(eigrpId: str, serviceId: str, vrfId: str):
    return Sdwan_mngrClient().GetServiceVrfAssociatedRoutingEigrpFeatureByFeatureId(eigrpId=eigrpId, serviceId=serviceId, vrfId=vrfId)

@register('GetServiceVrfAssociatedRoutingOspfFeatures')
def GetServiceVrfAssociatedRoutingOspfFeatures(serviceId: str, vrfId: str):
    return Sdwan_mngrClient().GetServiceVrfAssociatedRoutingOspfFeatures(serviceId=serviceId, vrfId=vrfId)

@register('GetServiceVrfAssociatedRoutingOspfFeatureById')
def GetServiceVrfAssociatedRoutingOspfFeatureById(ospfId: str, serviceId: str, vrfId: str):
    return Sdwan_mngrClient().GetServiceVrfAssociatedRoutingOspfFeatureById(ospfId=ospfId, serviceId=serviceId, vrfId=vrfId)

@register('GetServiceVrfAssociatedRoutingOspfv3Ipv4Features')
def GetServiceVrfAssociatedRoutingOspfv3Ipv4Features(serviceId: str, vrfId: str):
    return Sdwan_mngrClient().GetServiceVrfAssociatedRoutingOspfv3Ipv4Features(serviceId=serviceId, vrfId=vrfId)

@register('GetServiceVrfAssociatedRoutingOspfv3Ipv4FeatureById')
def GetServiceVrfAssociatedRoutingOspfv3Ipv4FeatureById(ospfv3Id: str, serviceId: str, vrfId: str):
    return Sdwan_mngrClient().GetServiceVrfAssociatedRoutingOspfv3Ipv4FeatureById(ospfv3Id=ospfv3Id, serviceId=serviceId, vrfId=vrfId)

@register('GetServiceVrfAssociatedRoutingOspfv3Ipv6Parcels')
def GetServiceVrfAssociatedRoutingOspfv3Ipv6Parcels(serviceId: str, vrfId: str):
    return Sdwan_mngrClient().GetServiceVrfAssociatedRoutingOspfv3Ipv6Parcels(serviceId=serviceId, vrfId=vrfId)

@register('GetServiceVrfAssociatedRoutingOspfv3Ipv6FeatureById')
def GetServiceVrfAssociatedRoutingOspfv3Ipv6FeatureById(ospfv3Id: str, serviceId: str, vrfId: str):
    return Sdwan_mngrClient().GetServiceVrfAssociatedRoutingOspfv3Ipv6FeatureById(ospfv3Id=ospfv3Id, serviceId=serviceId, vrfId=vrfId)

@register('GetSdRoutingSseFeatureProfiles')
def GetSdRoutingSseFeatureProfiles(**kwargs):
    return Sdwan_mngrClient().GetSdRoutingSseFeatureProfiles(**kwargs)

@register('GetSdRoutingSseFeatureProfileByProfileId')
def GetSdRoutingSseFeatureProfileByProfileId(sseId: str, **kwargs):
    return Sdwan_mngrClient().GetSdRoutingSseFeatureProfileByProfileId(sseId=sseId, **kwargs)

@register('GetCiscoSseFeatureForSse')
def GetCiscoSseFeatureForSse(sseId: str):
    return Sdwan_mngrClient().GetCiscoSseFeatureForSse(sseId=sseId)

@register('GetCiscoSseFeatureByFeatureIdForSSE')
def GetCiscoSseFeatureByFeatureIdForSSE(ciscoSseId: str, sseId: str):
    return Sdwan_mngrClient().GetCiscoSseFeatureByFeatureIdForSSE(ciscoSseId=ciscoSseId, sseId=sseId)

@register('GetSdroutingSystemFeatureProfiles')
def GetSdroutingSystemFeatureProfiles(**kwargs):
    return Sdwan_mngrClient().GetSdroutingSystemFeatureProfiles(**kwargs)

@register('GetSdroutingSystemFeatureProfile')
def GetSdroutingSystemFeatureProfile(systemId: str):
    return Sdwan_mngrClient().GetSdroutingSystemFeatureProfile(systemId=systemId)

@register('GetSdroutingAaaFeatures')
def GetSdroutingAaaFeatures(systemId: str):
    return Sdwan_mngrClient().GetSdroutingAaaFeatures(systemId=systemId)

@register('GetSdroutingAaaFeature')
def GetSdroutingAaaFeature(aaaId: str, systemId: str):
    return Sdwan_mngrClient().GetSdroutingAaaFeature(aaaId=aaaId, systemId=systemId)

@register('GetSdroutingBannerFeatures')
def GetSdroutingBannerFeatures(systemId: str):
    return Sdwan_mngrClient().GetSdroutingBannerFeatures(systemId=systemId)

@register('GetSdroutingBannerFeature')
def GetSdroutingBannerFeature(bannerId: str, systemId: str):
    return Sdwan_mngrClient().GetSdroutingBannerFeature(bannerId=bannerId, systemId=systemId)

@register('GetSdroutingCertificateFeatures')
def GetSdroutingCertificateFeatures(systemId: str):
    return Sdwan_mngrClient().GetSdroutingCertificateFeatures(systemId=systemId)

@register('GetSdroutingCertificateFeature')
def GetSdroutingCertificateFeature(certificateId: str, systemId: str):
    return Sdwan_mngrClient().GetSdroutingCertificateFeature(certificateId=certificateId, systemId=systemId)

@register('GetSdroutingFlexiblePortSpeedFeatures')
def GetSdroutingFlexiblePortSpeedFeatures(systemId: str):
    return Sdwan_mngrClient().GetSdroutingFlexiblePortSpeedFeatures(systemId=systemId)

@register('GetSdroutingFlexiblePortSpeedFeature')
def GetSdroutingFlexiblePortSpeedFeature(flexiblePortSpeedId: str, systemId: str):
    return Sdwan_mngrClient().GetSdroutingFlexiblePortSpeedFeature(flexiblePortSpeedId=flexiblePortSpeedId, systemId=systemId)

@register('GetSdroutingGlobalSettingFeatures')
def GetSdroutingGlobalSettingFeatures(systemId: str):
    return Sdwan_mngrClient().GetSdroutingGlobalSettingFeatures(systemId=systemId)

@register('GetSdroutingGlobalSettingFeature')
def GetSdroutingGlobalSettingFeature(globalId: str, systemId: str):
    return Sdwan_mngrClient().GetSdroutingGlobalSettingFeature(globalId=globalId, systemId=systemId)

@register('GetSdroutingLoggingFeatures')
def GetSdroutingLoggingFeatures(systemId: str):
    return Sdwan_mngrClient().GetSdroutingLoggingFeatures(systemId=systemId)

@register('GetSdroutingLoggingFeature')
def GetSdroutingLoggingFeature(loggingId: str, systemId: str):
    return Sdwan_mngrClient().GetSdroutingLoggingFeature(loggingId=loggingId, systemId=systemId)

@register('GetSdroutingNtpFeatures')
def GetSdroutingNtpFeatures(systemId: str):
    return Sdwan_mngrClient().GetSdroutingNtpFeatures(systemId=systemId)

@register('GetSdroutingNtpFeature')
def GetSdroutingNtpFeature(ntpId: str, systemId: str):
    return Sdwan_mngrClient().GetSdroutingNtpFeature(ntpId=ntpId, systemId=systemId)

@register('GetSdroutingSnmpFeatures')
def GetSdroutingSnmpFeatures(systemId: str):
    return Sdwan_mngrClient().GetSdroutingSnmpFeatures(systemId=systemId)

@register('GetSdroutingSnmpFeature')
def GetSdroutingSnmpFeature(snmpId: str, systemId: str):
    return Sdwan_mngrClient().GetSdroutingSnmpFeature(snmpId=snmpId, systemId=systemId)

@register('GetSdroutingTransportFeatureProfiles')
def GetSdroutingTransportFeatureProfiles(**kwargs):
    return Sdwan_mngrClient().GetSdroutingTransportFeatureProfiles(**kwargs)

@register('GetSdroutingTransportFeatureProfile')
def GetSdroutingTransportFeatureProfile(transportId: str):
    return Sdwan_mngrClient().GetSdroutingTransportFeatureProfile(transportId=transportId)

@register('GetCellularControllerProfileParcelForTransport_1')
def GetCellularControllerProfileParcelForTransport_1(transportId: str):
    return Sdwan_mngrClient().GetCellularControllerProfileParcelForTransport_1(transportId=transportId)

@register('GetCellularControllerProfileParcelByParcelIdForTransport_1')
def GetCellularControllerProfileParcelByParcelIdForTransport_1(cellularControllerId: str, transportId: str):
    return Sdwan_mngrClient().GetCellularControllerProfileParcelByParcelIdForTransport_1(cellularControllerId=cellularControllerId, transportId=transportId)

@register('GetCellularControllerAssociatedCellularProfileParcelsForTransport_1')
def GetCellularControllerAssociatedCellularProfileParcelsForTransport_1(cellularControllerId: str, transportId: str):
    return Sdwan_mngrClient().GetCellularControllerAssociatedCellularProfileParcelsForTransport_1(cellularControllerId=cellularControllerId, transportId=transportId)

@register('GetCellularControllerAssociatedCellularProfileParcelByParcelIdForTransport_1')
def GetCellularControllerAssociatedCellularProfileParcelByParcelIdForTransport_1(cellularControllerId: str, cellularProfileId: str, transportId: str):
    return Sdwan_mngrClient().GetCellularControllerAssociatedCellularProfileParcelByParcelIdForTransport_1(cellularControllerId=cellularControllerId, cellularProfileId=cellularProfileId, transportId=transportId)

@register('GetCellularControllerAssociatedGpsParcelsForTransport_1')
def GetCellularControllerAssociatedGpsParcelsForTransport_1(cellularControllerId: str, transportId: str):
    return Sdwan_mngrClient().GetCellularControllerAssociatedGpsParcelsForTransport_1(cellularControllerId=cellularControllerId, transportId=transportId)

@register('GetCellularControllerAssociatedGpsParcelByParcelIdForTransport_1')
def GetCellularControllerAssociatedGpsParcelByParcelIdForTransport_1(cellularControllerId: str, gpsId: str, transportId: str):
    return Sdwan_mngrClient().GetCellularControllerAssociatedGpsParcelByParcelIdForTransport_1(cellularControllerId=cellularControllerId, gpsId=gpsId, transportId=transportId)

@register('GetCellularProfileParcelForTransport')
def GetCellularProfileParcelForTransport(transportId: str):
    return Sdwan_mngrClient().GetCellularProfileParcelForTransport(transportId=transportId)

@register('GetCellularProfileParcelByParcelIdForTransport')
def GetCellularProfileParcelByParcelIdForTransport(cellularProfileId: str, transportId: str):
    return Sdwan_mngrClient().GetCellularProfileParcelByParcelIdForTransport(cellularProfileId=cellularProfileId, transportId=transportId)

@register('GetSdroutingTransportGlobalVRFFeatures')
def GetSdroutingTransportGlobalVRFFeatures(transportId: str):
    return Sdwan_mngrClient().GetSdroutingTransportGlobalVRFFeatures(transportId=transportId)

@register('GetSdroutingTransportGlobalVrfBgpFeatures')
def GetSdroutingTransportGlobalVrfBgpFeatures(transportId: str):
    return Sdwan_mngrClient().GetSdroutingTransportGlobalVrfBgpFeatures(transportId=transportId)

@register('GetSdroutingTransportGlobalVrfBgpFeature')
def GetSdroutingTransportGlobalVrfBgpFeature(bgpId: str, transportId: str):
    return Sdwan_mngrClient().GetSdroutingTransportGlobalVrfBgpFeature(bgpId=bgpId, transportId=transportId)

@register('GetSdroutingTransportGlobalVRFFeature')
def GetSdroutingTransportGlobalVRFFeature(transportId: str, vrfId: str):
    return Sdwan_mngrClient().GetSdroutingTransportGlobalVRFFeature(transportId=transportId, vrfId=vrfId)

@register('GetGlobalVRFInterfaceCellularParcelsForTransport')
def GetGlobalVRFInterfaceCellularParcelsForTransport(transportId: str, vrfId: str):
    return Sdwan_mngrClient().GetGlobalVRFInterfaceCellularParcelsForTransport(transportId=transportId, vrfId=vrfId)

@register('GetGlobalVRFInterfaceCellularAssociatedTrackerParcelsForTransport_1')
def GetGlobalVRFInterfaceCellularAssociatedTrackerParcelsForTransport_1(cellularId: str, transportId: str, vrfId: str):
    return Sdwan_mngrClient().GetGlobalVRFInterfaceCellularAssociatedTrackerParcelsForTransport_1(cellularId=cellularId, transportId=transportId, vrfId=vrfId)

@register('GetGlobalVRFInterfaceCellularAssociatedTrackerParcelByParcelIdForTransport_1')
def GetGlobalVRFInterfaceCellularAssociatedTrackerParcelByParcelIdForTransport_1(cellularId: str, trackerId: str, transportId: str, vrfId: str):
    return Sdwan_mngrClient().GetGlobalVRFInterfaceCellularAssociatedTrackerParcelByParcelIdForTransport_1(cellularId=cellularId, trackerId=trackerId, transportId=transportId, vrfId=vrfId)

@register('GetGlobalVRFInterfaceCellularAssociatedTrackerParcelsForTransport')
def GetGlobalVRFInterfaceCellularAssociatedTrackerParcelsForTransport(cellularId: str, transportId: str, vrfId: str):
    return Sdwan_mngrClient().GetGlobalVRFInterfaceCellularAssociatedTrackerParcelsForTransport(cellularId=cellularId, transportId=transportId, vrfId=vrfId)

@register('GetGlobalVRFInterfaceCellularAssociatedTrackerParcelByParcelIdForTransport')
def GetGlobalVRFInterfaceCellularAssociatedTrackerParcelByParcelIdForTransport(cellularId: str, trackerId: str, transportId: str, vrfId: str):
    return Sdwan_mngrClient().GetGlobalVRFInterfaceCellularAssociatedTrackerParcelByParcelIdForTransport(cellularId=cellularId, trackerId=trackerId, transportId=transportId, vrfId=vrfId)

@register('GetGlobalVRFInterfaceCellularParcelByParcelIdForTransport')
def GetGlobalVRFInterfaceCellularParcelByParcelIdForTransport(intfId: str, transportId: str, vrfId: str):
    return Sdwan_mngrClient().GetGlobalVRFInterfaceCellularParcelByParcelIdForTransport(intfId=intfId, transportId=transportId, vrfId=vrfId)

@register('GetSdroutingTransportGlobalVrfInterfaceEthernetParcelsForTransport')
def GetSdroutingTransportGlobalVrfInterfaceEthernetParcelsForTransport(transportId: str, vrfId: str):
    return Sdwan_mngrClient().GetSdroutingTransportGlobalVrfInterfaceEthernetParcelsForTransport(transportId=transportId, vrfId=vrfId)

@register('GetSdroutingTransportGlobalVrfInterfaceEthernetParcelByParcelIdForTransport')
def GetSdroutingTransportGlobalVrfInterfaceEthernetParcelByParcelIdForTransport(ethernetId: str, transportId: str, vrfId: str):
    return Sdwan_mngrClient().GetSdroutingTransportGlobalVrfInterfaceEthernetParcelByParcelIdForTransport(ethernetId=ethernetId, transportId=transportId, vrfId=vrfId)

@register('GetSdroutingTransportGlobalVrfInterfaceIpsecFeaturesForTransport')
def GetSdroutingTransportGlobalVrfInterfaceIpsecFeaturesForTransport(transportId: str, vrfId: str):
    return Sdwan_mngrClient().GetSdroutingTransportGlobalVrfInterfaceIpsecFeaturesForTransport(transportId=transportId, vrfId=vrfId)

@register('GetSdroutingTransportGlobalVrfInterfaceIpsecFeatureByFeatureIdForTransport')
def GetSdroutingTransportGlobalVrfInterfaceIpsecFeatureByFeatureIdForTransport(ipsecId: str, transportId: str, vrfId: str):
    return Sdwan_mngrClient().GetSdroutingTransportGlobalVrfInterfaceIpsecFeatureByFeatureIdForTransport(ipsecId=ipsecId, transportId=transportId, vrfId=vrfId)

@register('GetTransportVrfAssociatedRoutingBgpFeatures')
def GetTransportVrfAssociatedRoutingBgpFeatures(transportId: str, vrfId: str):
    return Sdwan_mngrClient().GetTransportVrfAssociatedRoutingBgpFeatures(transportId=transportId, vrfId=vrfId)

@register('GetVrfAssociatedRoutingBgpFeatureById')
def GetVrfAssociatedRoutingBgpFeatureById(bgpId: str, transportId: str, vrfId: str):
    return Sdwan_mngrClient().GetVrfAssociatedRoutingBgpFeatureById(bgpId=bgpId, transportId=transportId, vrfId=vrfId)

@register('GetTransportVrfAssociatedRoutingOspfFeatures')
def GetTransportVrfAssociatedRoutingOspfFeatures(transportId: str, vrfId: str):
    return Sdwan_mngrClient().GetTransportVrfAssociatedRoutingOspfFeatures(transportId=transportId, vrfId=vrfId)

@register('GetVrfAssociatedRoutingOspfParcelByFeatureId')
def GetVrfAssociatedRoutingOspfParcelByFeatureId(ospfId: str, transportId: str, vrfId: str):
    return Sdwan_mngrClient().GetVrfAssociatedRoutingOspfParcelByFeatureId(ospfId=ospfId, transportId=transportId, vrfId=vrfId)

@register('GetTransportVrfAssociatedRoutingOspfv3Ipv4Features')
def GetTransportVrfAssociatedRoutingOspfv3Ipv4Features(transportId: str, vrfId: str):
    return Sdwan_mngrClient().GetTransportVrfAssociatedRoutingOspfv3Ipv4Features(transportId=transportId, vrfId=vrfId)

@register('GetVrfAssociatedRoutingOspfv3Ipv4FeatureById')
def GetVrfAssociatedRoutingOspfv3Ipv4FeatureById(ospfv3Id: str, transportId: str, vrfId: str):
    return Sdwan_mngrClient().GetVrfAssociatedRoutingOspfv3Ipv4FeatureById(ospfv3Id=ospfv3Id, transportId=transportId, vrfId=vrfId)

@register('GetTransportVrfAssociatedRoutingOspfv3Ipv6Features')
def GetTransportVrfAssociatedRoutingOspfv3Ipv6Features(transportId: str, vrfId: str):
    return Sdwan_mngrClient().GetTransportVrfAssociatedRoutingOspfv3Ipv6Features(transportId=transportId, vrfId=vrfId)

@register('GetVrfAssociatedRoutingOspfv3Ipv6FeatureById')
def GetVrfAssociatedRoutingOspfv3Ipv6FeatureById(ospfv3Id: str, transportId: str, vrfId: str):
    return Sdwan_mngrClient().GetVrfAssociatedRoutingOspfv3Ipv6FeatureById(ospfv3Id=ospfv3Id, transportId=transportId, vrfId=vrfId)

@register('GetGPSProfileParcelForTransport')
def GetGPSProfileParcelForTransport(transportId: str):
    return Sdwan_mngrClient().GetGPSProfileParcelForTransport(transportId=transportId)

@register('GetGPSProfileParcelByParcelIdForTransport')
def GetGPSProfileParcelByParcelIdForTransport(gpsId: str, transportId: str):
    return Sdwan_mngrClient().GetGPSProfileParcelByParcelIdForTransport(gpsId=gpsId, transportId=transportId)

@register('GetSdroutingTransportIpv4AclFeatures')
def GetSdroutingTransportIpv4AclFeatures(transportId: str):
    return Sdwan_mngrClient().GetSdroutingTransportIpv4AclFeatures(transportId=transportId)

@register('GetSdroutingTransportIpv4AclFeature')
def GetSdroutingTransportIpv4AclFeature(ipv4AclId: str, transportId: str):
    return Sdwan_mngrClient().GetSdroutingTransportIpv4AclFeature(ipv4AclId=ipv4AclId, transportId=transportId)

@register('GetSdroutingManagementVRFFeatures')
def GetSdroutingManagementVRFFeatures(transportId: str):
    return Sdwan_mngrClient().GetSdroutingManagementVRFFeatures(transportId=transportId)

@register('GetSdroutingManagementVRFFeature')
def GetSdroutingManagementVRFFeature(transportId: str, vrfId: str):
    return Sdwan_mngrClient().GetSdroutingManagementVRFFeature(transportId=transportId, vrfId=vrfId)

@register('GetSdroutingManagementVrfInterfaceEthernetParcelsForTransportProfile')
def GetSdroutingManagementVrfInterfaceEthernetParcelsForTransportProfile(transportId: str, vrfId: str):
    return Sdwan_mngrClient().GetSdroutingManagementVrfInterfaceEthernetParcelsForTransportProfile(transportId=transportId, vrfId=vrfId)

@register('GetSdroutingManagementVrfInterfaceEthernetParcelByParcelIdForTransportProfile')
def GetSdroutingManagementVrfInterfaceEthernetParcelByParcelIdForTransportProfile(ethernetId: str, transportId: str, vrfId: str):
    return Sdwan_mngrClient().GetSdroutingManagementVrfInterfaceEthernetParcelByParcelIdForTransportProfile(ethernetId=ethernetId, transportId=transportId, vrfId=vrfId)

@register('GetLanVpnProfileParcelForService_1')
def GetLanVpnProfileParcelForService_1(transportId: str):
    return Sdwan_mngrClient().GetLanVpnProfileParcelForService_1(transportId=transportId)

@register('GetLanVpnProfileParcelByParcelIdForService_1')
def GetLanVpnProfileParcelByParcelIdForService_1(multiCloudConnectionId: str, transportId: str):
    return Sdwan_mngrClient().GetLanVpnProfileParcelByParcelIdForService_1(multiCloudConnectionId=multiCloudConnectionId, transportId=transportId)

@register('GetSdroutingTransportObjectTrackerFeatures')
def GetSdroutingTransportObjectTrackerFeatures(transportId: str):
    return Sdwan_mngrClient().GetSdroutingTransportObjectTrackerFeatures(transportId=transportId)

@register('GetSdroutingTransportObjectTrackerFeature')
def GetSdroutingTransportObjectTrackerFeature(objectTrackerId: str, transportId: str):
    return Sdwan_mngrClient().GetSdroutingTransportObjectTrackerFeature(objectTrackerId=objectTrackerId, transportId=transportId)

@register('GetSdroutingTransportObjectTrackerGroupFeatures')
def GetSdroutingTransportObjectTrackerGroupFeatures(transportId: str):
    return Sdwan_mngrClient().GetSdroutingTransportObjectTrackerGroupFeatures(transportId=transportId)

@register('GetSdroutingTransportObjectTrackerGroupFeature')
def GetSdroutingTransportObjectTrackerGroupFeature(objectTrackerGroupId: str, transportId: str):
    return Sdwan_mngrClient().GetSdroutingTransportObjectTrackerGroupFeature(objectTrackerGroupId=objectTrackerGroupId, transportId=transportId)

@register('GetSdroutingTransportRoutePolicyFeatures')
def GetSdroutingTransportRoutePolicyFeatures(transportId: str):
    return Sdwan_mngrClient().GetSdroutingTransportRoutePolicyFeatures(transportId=transportId)

@register('GetSdroutingTransportRoutePolicyFeature')
def GetSdroutingTransportRoutePolicyFeature(routePolicyId: str, transportId: str):
    return Sdwan_mngrClient().GetSdroutingTransportRoutePolicyFeature(routePolicyId=routePolicyId, transportId=transportId)

@register('GetSdroutingTransportRoutingOspfFeatures')
def GetSdroutingTransportRoutingOspfFeatures(transportId: str):
    return Sdwan_mngrClient().GetSdroutingTransportRoutingOspfFeatures(transportId=transportId)

@register('GetSdroutingTransportRoutingOspfFeature')
def GetSdroutingTransportRoutingOspfFeature(ospfId: str, transportId: str):
    return Sdwan_mngrClient().GetSdroutingTransportRoutingOspfFeature(ospfId=ospfId, transportId=transportId)

@register('GetSdroutingTransportRoutingOspfv3Ipv4Features')
def GetSdroutingTransportRoutingOspfv3Ipv4Features(transportId: str):
    return Sdwan_mngrClient().GetSdroutingTransportRoutingOspfv3Ipv4Features(transportId=transportId)

@register('GetSdroutingTransportRoutingOspfv3Ipv4Feature')
def GetSdroutingTransportRoutingOspfv3Ipv4Feature(ospfv3Id: str, transportId: str):
    return Sdwan_mngrClient().GetSdroutingTransportRoutingOspfv3Ipv4Feature(ospfv3Id=ospfv3Id, transportId=transportId)

@register('GetSdroutingTransportRoutingOspfv3Ipv6Features')
def GetSdroutingTransportRoutingOspfv3Ipv6Features(transportId: str):
    return Sdwan_mngrClient().GetSdroutingTransportRoutingOspfv3Ipv6Features(transportId=transportId)

@register('GetSdroutingTransportRoutingOspfv3Ipv6Feature')
def GetSdroutingTransportRoutingOspfv3Ipv6Feature(ospfv3Id: str, transportId: str):
    return Sdwan_mngrClient().GetSdroutingTransportRoutingOspfv3Ipv6Feature(ospfv3Id=ospfv3Id, transportId=transportId)

@register('GetTrackerProfileParcelForTransport_1')
def GetTrackerProfileParcelForTransport_1(transportId: str):
    return Sdwan_mngrClient().GetTrackerProfileParcelForTransport_1(transportId=transportId)

@register('GetTrackerProfileParcelByParcelIdForTransport_1')
def GetTrackerProfileParcelByParcelIdForTransport_1(trackerId: str, transportId: str):
    return Sdwan_mngrClient().GetTrackerProfileParcelByParcelIdForTransport_1(trackerId=trackerId, transportId=transportId)

@register('GetTrackerGroupProfileParcelForTransport_1')
def GetTrackerGroupProfileParcelForTransport_1(transportId: str):
    return Sdwan_mngrClient().GetTrackerGroupProfileParcelForTransport_1(transportId=transportId)

@register('GetTrackerGroupProfileParcelByParcelIdForTransport_1')
def GetTrackerGroupProfileParcelByParcelIdForTransport_1(trackergroupId: str, transportId: str):
    return Sdwan_mngrClient().GetTrackerGroupProfileParcelByParcelIdForTransport_1(trackergroupId=trackergroupId, transportId=transportId)

@register('GetSdroutingTransportVRFFeatures')
def GetSdroutingTransportVRFFeatures(transportId: str):
    return Sdwan_mngrClient().GetSdroutingTransportVRFFeatures(transportId=transportId)

@register('GetSdroutingTransportVrfBgpFeatures')
def GetSdroutingTransportVrfBgpFeatures(transportId: str):
    return Sdwan_mngrClient().GetSdroutingTransportVrfBgpFeatures(transportId=transportId)

@register('GetSdroutingTransportVrfBgpFeature')
def GetSdroutingTransportVrfBgpFeature(bgpId: str, transportId: str):
    return Sdwan_mngrClient().GetSdroutingTransportVrfBgpFeature(bgpId=bgpId, transportId=transportId)

@register('GetSdroutingTransportVRFFeature')
def GetSdroutingTransportVRFFeature(transportId: str, vrfId: str):
    return Sdwan_mngrClient().GetSdroutingTransportVRFFeature(transportId=transportId, vrfId=vrfId)

@register('GetSdroutingTransportVrfInterfaceEthernetParcelsForTransport')
def GetSdroutingTransportVrfInterfaceEthernetParcelsForTransport(transportId: str, vrfId: str):
    return Sdwan_mngrClient().GetSdroutingTransportVrfInterfaceEthernetParcelsForTransport(transportId=transportId, vrfId=vrfId)

@register('GetSdroutingTransportVrfInterfaceEthernetParcelByParcelIdForTransport')
def GetSdroutingTransportVrfInterfaceEthernetParcelByParcelIdForTransport(ethernetId: str, transportId: str, vrfId: str):
    return Sdwan_mngrClient().GetSdroutingTransportVrfInterfaceEthernetParcelByParcelIdForTransport(ethernetId=ethernetId, transportId=transportId, vrfId=vrfId)

@register('GetSdroutingTransportVrfInterfaceIpsecFeaturesForTransport')
def GetSdroutingTransportVrfInterfaceIpsecFeaturesForTransport(transportId: str, vrfId: str):
    return Sdwan_mngrClient().GetSdroutingTransportVrfInterfaceIpsecFeaturesForTransport(transportId=transportId, vrfId=vrfId)

@register('GetSdroutingTransportVrfInterfaceIpsecFeatureByFeatureIdForTransport')
def GetSdroutingTransportVrfInterfaceIpsecFeatureByFeatureIdForTransport(ipsecId: str, transportId: str, vrfId: str):
    return Sdwan_mngrClient().GetSdroutingTransportVrfInterfaceIpsecFeatureByFeatureIdForTransport(ipsecId=ipsecId, transportId=transportId, vrfId=vrfId)

@register('GetTransportVrfAssociatedRoutingBgpFeatures_1')
def GetTransportVrfAssociatedRoutingBgpFeatures_1(transportId: str, vrfId: str):
    return Sdwan_mngrClient().GetTransportVrfAssociatedRoutingBgpFeatures_1(transportId=transportId, vrfId=vrfId)

@register('GetTransportVrfAssociatedRoutingBgpById')
def GetTransportVrfAssociatedRoutingBgpById(bgpId: str, transportId: str, vrfId: str):
    return Sdwan_mngrClient().GetTransportVrfAssociatedRoutingBgpById(bgpId=bgpId, transportId=transportId, vrfId=vrfId)

@register('GetTransportVrfAssociatedRoutingOspfFeatures_1')
def GetTransportVrfAssociatedRoutingOspfFeatures_1(transportId: str, vrfId: str):
    return Sdwan_mngrClient().GetTransportVrfAssociatedRoutingOspfFeatures_1(transportId=transportId, vrfId=vrfId)

@register('GetVrfAssociatedRoutingOspfById')
def GetVrfAssociatedRoutingOspfById(ospfId: str, transportId: str, vrfId: str):
    return Sdwan_mngrClient().GetVrfAssociatedRoutingOspfById(ospfId=ospfId, transportId=transportId, vrfId=vrfId)

@register('GetTransportVrfAssociatedRoutingOspfv3Ipv4Features_1')
def GetTransportVrfAssociatedRoutingOspfv3Ipv4Features_1(transportId: str, vrfId: str):
    return Sdwan_mngrClient().GetTransportVrfAssociatedRoutingOspfv3Ipv4Features_1(transportId=transportId, vrfId=vrfId)

@register('GetVrfAssociatedRoutingOspfv3Ipv4FeatureById_1')
def GetVrfAssociatedRoutingOspfv3Ipv4FeatureById_1(ospfv3Id: str, transportId: str, vrfId: str):
    return Sdwan_mngrClient().GetVrfAssociatedRoutingOspfv3Ipv4FeatureById_1(ospfv3Id=ospfv3Id, transportId=transportId, vrfId=vrfId)

@register('GetTransportVrfAssociatedRoutingOspfv3Ipv6Features_1')
def GetTransportVrfAssociatedRoutingOspfv3Ipv6Features_1(transportId: str, vrfId: str):
    return Sdwan_mngrClient().GetTransportVrfAssociatedRoutingOspfv3Ipv6Features_1(transportId=transportId, vrfId=vrfId)

@register('GetVrfAssociatedRoutingOspfv3Ipv6FeatureById_1')
def GetVrfAssociatedRoutingOspfv3Ipv6FeatureById_1(ospfv3Id: str, transportId: str, vrfId: str):
    return Sdwan_mngrClient().GetVrfAssociatedRoutingOspfv3Ipv6FeatureById_1(ospfv3Id=ospfv3Id, transportId=transportId, vrfId=vrfId)

@register('GetSdwanFeatureProfileBySdwanFamily')
def GetSdwanFeatureProfileBySdwanFamily(**kwargs):
    return Sdwan_mngrClient().GetSdwanFeatureProfileBySdwanFamily(**kwargs)

@register('GetCloudProbeProfileParcelByParcelIdForapplication-priority')
def GetCloudProbeProfileParcelByParcelIdForapplication_priority(applicationPriorityId: str, cloudProbeId: str):
    return Sdwan_mngrClient().GetCloudProbeProfileParcelByParcelIdForapplication_priority(applicationPriorityId=applicationPriorityId, cloudProbeId=cloudProbeId)

@register('getPolicyApplicationProfileParcel')
def getPolicyApplicationProfileParcel(applicationPriorityId: str, qosPolicyId: str):
    return Sdwan_mngrClient().getPolicyApplicationProfileParcel(applicationPriorityId=applicationPriorityId, qosPolicyId=qosPolicyId)

@register('GetTrafficPolicyProfileParcelByParcelIdForapplication-priority')
def GetTrafficPolicyProfileParcelByParcelIdForapplication_priority(applicationPriorityId: str, trafficPolicyId: str):
    return Sdwan_mngrClient().GetTrafficPolicyProfileParcelByParcelIdForapplication_priority(applicationPriorityId=applicationPriorityId, trafficPolicyId=trafficPolicyId)

@register('GetSdwanFeatureProfilesByFamilyAndType_1')
def GetSdwanFeatureProfilesByFamilyAndType_1(**kwargs):
    return Sdwan_mngrClient().GetSdwanFeatureProfilesByFamilyAndType_1(**kwargs)

@register('GetSdwanCliConfigFeatureSchemaBySchemaType')
def GetSdwanCliConfigFeatureSchemaBySchemaType(schemaType: str):
    return Sdwan_mngrClient().GetSdwanCliConfigFeatureSchemaBySchemaType(schemaType=schemaType)

@register('GetSdwanFeatureProfilesByFamilyAndType')
def GetSdwanFeatureProfilesByFamilyAndType(**kwargs):
    return Sdwan_mngrClient().GetSdwanFeatureProfilesByFamilyAndType(**kwargs)

@register('GetSdwanFeatureProfileByProfileId')
def GetSdwanFeatureProfileByProfileId(cliId: str):
    return Sdwan_mngrClient().GetSdwanFeatureProfileByProfileId(cliId=cliId)

@register('GetConfigProfileParcelForCLI')
def GetConfigProfileParcelForCLI(cliId: str):
    return Sdwan_mngrClient().GetConfigProfileParcelForCLI(cliId=cliId)

@register('GetConfigProfileParcelByParcelIdForCLI')
def GetConfigProfileParcelByParcelIdForCLI(cliId: str, configId: str):
    return Sdwan_mngrClient().GetConfigProfileParcelByParcelIdForCLI(cliId=cliId, configId=configId)

@register('GetSdwanDnsSecurityFeatureProfiles')
def GetSdwanDnsSecurityFeatureProfiles(**kwargs):
    return Sdwan_mngrClient().GetSdwanDnsSecurityFeatureProfiles(**kwargs)

@register('GetSdwanDnsSecurityFeatureProfileByProfileId')
def GetSdwanDnsSecurityFeatureProfileByProfileId(dnsSecurityId: str, **kwargs):
    return Sdwan_mngrClient().GetSdwanDnsSecurityFeatureProfileByProfileId(dnsSecurityId=dnsSecurityId, **kwargs)

@register('GetSigSecurityProfileParcel')
def GetSigSecurityProfileParcel(dnsSecurityId: str):
    return Sdwan_mngrClient().GetSigSecurityProfileParcel(dnsSecurityId=dnsSecurityId)

@register('GetSigSecurityProfileParcelByParcelId')
def GetSigSecurityProfileParcelByParcelId(dnsSecurityId: str, dnsSecurityProfileParcelId: str):
    return Sdwan_mngrClient().GetSigSecurityProfileParcelByParcelId(dnsSecurityId=dnsSecurityId, dnsSecurityProfileParcelId=dnsSecurityProfileParcelId)

@register('GetSdwanSecurityFeature_1')
def GetSdwanSecurityFeature_1(securityId: str):
    return Sdwan_mngrClient().GetSdwanSecurityFeature_1(securityId=securityId)

@register('GetSdwanSecurityFeatureByFeatureId_1')
def GetSdwanSecurityFeatureByFeatureId_1(securityId: str, securityProfileParcelId: str):
    return Sdwan_mngrClient().GetSdwanSecurityFeatureByFeatureId_1(securityId=securityId, securityProfileParcelId=securityProfileParcelId)

@register('GetSdwanNgfirewallFeature')
def GetSdwanNgfirewallFeature(securityId: str):
    return Sdwan_mngrClient().GetSdwanNgfirewallFeature(securityId=securityId)

@register('GetSdwanNgfirewallFeatureByFeatureId')
def GetSdwanNgfirewallFeatureByFeatureId(securityId: str, securityProfileParcelId: str):
    return Sdwan_mngrClient().GetSdwanNgfirewallFeatureByFeatureId(securityId=securityId, securityProfileParcelId=securityProfileParcelId)

@register('GetSdwanOtherFeatureProfiles')
def GetSdwanOtherFeatureProfiles(**kwargs):
    return Sdwan_mngrClient().GetSdwanOtherFeatureProfiles(**kwargs)

@register('GetSdwanOtherThousandeyesParcelSchemaBySchemaType')
def GetSdwanOtherThousandeyesParcelSchemaBySchemaType(schemaType: str):
    return Sdwan_mngrClient().GetSdwanOtherThousandeyesParcelSchemaBySchemaType(schemaType=schemaType)

@register('GetSdwanOtherFeatureProfileByProfileId')
def GetSdwanOtherFeatureProfileByProfileId(otherId: str):
    return Sdwan_mngrClient().GetSdwanOtherFeatureProfileByProfileId(otherId=otherId)

@register('GetThousandeyesProfileParcelForOther')
def GetThousandeyesProfileParcelForOther(otherId: str):
    return Sdwan_mngrClient().GetThousandeyesProfileParcelForOther(otherId=otherId)

@register('GetThousandeyesProfileParcelByParcelIdForOther')
def GetThousandeyesProfileParcelByParcelIdForOther(otherId: str, thousandeyesId: str):
    return Sdwan_mngrClient().GetThousandeyesProfileParcelByParcelIdForOther(otherId=otherId, thousandeyesId=thousandeyesId)

@register('GetUcseProfileFeatureForOther')
def GetUcseProfileFeatureForOther(otherId: str):
    return Sdwan_mngrClient().GetUcseProfileFeatureForOther(otherId=otherId)

@register('GetUcseProfileFeatureByIdFFeatureForOther')
def GetUcseProfileFeatureByIdFFeatureForOther(otherId: str, ucseId: str):
    return Sdwan_mngrClient().GetUcseProfileFeatureByIdFFeatureForOther(otherId=otherId, ucseId=ucseId)

@register('GetSdwanSecurityFeature')
def GetSdwanSecurityFeature(policyObjectId: str, securityProfileParcelType: str, **kwargs):
    return Sdwan_mngrClient().GetSdwanSecurityFeature(policyObjectId=policyObjectId, securityProfileParcelType=securityProfileParcelType, **kwargs)

@register('GetSdwanSecurityFeatureByFeatureId')
def GetSdwanSecurityFeatureByFeatureId(policyObjectId: str, securityProfileParcelId: str, securityProfileParcelType: str, **kwargs):
    return Sdwan_mngrClient().GetSdwanSecurityFeatureByFeatureId(policyObjectId=policyObjectId, securityProfileParcelId=securityProfileParcelId, securityProfileParcelType=securityProfileParcelType, **kwargs)

@register('GetDataPrefixProfileParcelForPolicyObject')
def GetDataPrefixProfileParcelForPolicyObject(policyObjectId: str, policyObjectListType: str, **kwargs):
    return Sdwan_mngrClient().GetDataPrefixProfileParcelForPolicyObject(policyObjectId=policyObjectId, policyObjectListType=policyObjectListType, **kwargs)

@register('GetDataPrefixProfileParcelByParcelIdForPolicyObject')
def GetDataPrefixProfileParcelByParcelIdForPolicyObject(listObjectId: str, policyObjectId: str, policyObjectListType: str, **kwargs):
    return Sdwan_mngrClient().GetDataPrefixProfileParcelByParcelIdForPolicyObject(listObjectId=listObjectId, policyObjectId=policyObjectId, policyObjectListType=policyObjectListType, **kwargs)

@register('GetSdwanPolicyObjectDataPrefixParcelSchemaBySchemaType')
def GetSdwanPolicyObjectDataPrefixParcelSchemaBySchemaType(policyObjectListType: str, schemaType: str):
    return Sdwan_mngrClient().GetSdwanPolicyObjectDataPrefixParcelSchemaBySchemaType(policyObjectListType=policyObjectListType, schemaType=schemaType)

@register('GetSdwanServiceFeatureProfiles')
def GetSdwanServiceFeatureProfiles(**kwargs):
    return Sdwan_mngrClient().GetSdwanServiceFeatureProfiles(**kwargs)

@register('GetSdwanServiceDhcpServerParcelSchemaBySchemaType')
def GetSdwanServiceDhcpServerParcelSchemaBySchemaType(schemaType: str):
    return Sdwan_mngrClient().GetSdwanServiceDhcpServerParcelSchemaBySchemaType(schemaType=schemaType)

@register('GetSdwanServiceLanVpnInterfaceEthernetParcelSchemaBySchema')
def GetSdwanServiceLanVpnInterfaceEthernetParcelSchemaBySchema(schemaType: str):
    return Sdwan_mngrClient().GetSdwanServiceLanVpnInterfaceEthernetParcelSchemaBySchema(schemaType=schemaType)

@register('GetCedgeServiceLanVpnInterfaceGreSchemaBySchema')
def GetCedgeServiceLanVpnInterfaceGreSchemaBySchema(schemaType: str):
    return Sdwan_mngrClient().GetCedgeServiceLanVpnInterfaceGreSchemaBySchema(schemaType=schemaType)

@register('getSdwanProfileParcelSchema')
def getSdwanProfileParcelSchema(schemaType: str):
    return Sdwan_mngrClient().getSdwanProfileParcelSchema(schemaType=schemaType)

@register('GetCedgeServiceLanVpnInterfaceSviParcelSchemaBySchema')
def GetCedgeServiceLanVpnInterfaceSviParcelSchemaBySchema(schemaType: str):
    return Sdwan_mngrClient().GetCedgeServiceLanVpnInterfaceSviParcelSchemaBySchema(schemaType=schemaType)

@register('GetSdwanServiceLanVpnParcelSchemaBySchemaType')
def GetSdwanServiceLanVpnParcelSchemaBySchemaType(schemaType: str):
    return Sdwan_mngrClient().GetSdwanServiceLanVpnParcelSchemaBySchemaType(schemaType=schemaType)

@register('GetSdwanServiceRoutingBgpParcelSchemaBySchemaType')
def GetSdwanServiceRoutingBgpParcelSchemaBySchemaType(schemaType: str):
    return Sdwan_mngrClient().GetSdwanServiceRoutingBgpParcelSchemaBySchemaType(schemaType=schemaType)

@register('GetSdwanServiceRoutingMulticastParcelSchemaBySchemaType')
def GetSdwanServiceRoutingMulticastParcelSchemaBySchemaType(schemaType: str):
    return Sdwan_mngrClient().GetSdwanServiceRoutingMulticastParcelSchemaBySchemaType(schemaType=schemaType)

@register('GetCedgeServiceSwitchportParcelSchemaBySchemaType')
def GetCedgeServiceSwitchportParcelSchemaBySchemaType(schemaType: str):
    return Sdwan_mngrClient().GetCedgeServiceSwitchportParcelSchemaBySchemaType(schemaType=schemaType)

@register('GetSdwanServiceTrackerParcelSchemaBySchemaType')
def GetSdwanServiceTrackerParcelSchemaBySchemaType(schemaType: str):
    return Sdwan_mngrClient().GetSdwanServiceTrackerParcelSchemaBySchemaType(schemaType=schemaType)

@register('GetCedgeServiceTrackerGroupParcelSchemaBySchemaType')
def GetCedgeServiceTrackerGroupParcelSchemaBySchemaType(schemaType: str):
    return Sdwan_mngrClient().GetCedgeServiceTrackerGroupParcelSchemaBySchemaType(schemaType=schemaType)

@register('GetSdwanServiceWirelesslanParcelSchemaBySchemaType')
def GetSdwanServiceWirelesslanParcelSchemaBySchemaType(schemaType: str):
    return Sdwan_mngrClient().GetSdwanServiceWirelesslanParcelSchemaBySchemaType(schemaType=schemaType)

@register('GetSdwanServiceFeatureProfileByProfileId')
def GetSdwanServiceFeatureProfileByProfileId(serviceId: str, **kwargs):
    return Sdwan_mngrClient().GetSdwanServiceFeatureProfileByProfileId(serviceId=serviceId, **kwargs)

@register('GetAppqoeProfileParcelForService')
def GetAppqoeProfileParcelForService(serviceId: str):
    return Sdwan_mngrClient().GetAppqoeProfileParcelForService(serviceId=serviceId)

@register('GetAppqoeProfileParcelByParcelIdForService')
def GetAppqoeProfileParcelByParcelIdForService(appqoeId: str, serviceId: str):
    return Sdwan_mngrClient().GetAppqoeProfileParcelByParcelIdForService(appqoeId=appqoeId, serviceId=serviceId)

@register('GetDhcpServerProfileParcelForService')
def GetDhcpServerProfileParcelForService(serviceId: str):
    return Sdwan_mngrClient().GetDhcpServerProfileParcelForService(serviceId=serviceId)

@register('GetDhcpServerProfileParcelByParcelIdForService')
def GetDhcpServerProfileParcelByParcelIdForService(dhcpServerId: str, serviceId: str):
    return Sdwan_mngrClient().GetDhcpServerProfileParcelByParcelIdForService(dhcpServerId=dhcpServerId, serviceId=serviceId)

@register('GetLanVpnProfileParcelForService')
def GetLanVpnProfileParcelForService(serviceId: str):
    return Sdwan_mngrClient().GetLanVpnProfileParcelForService(serviceId=serviceId)

@register('GetLanVpnProfileParcelByParcelIdForService')
def GetLanVpnProfileParcelByParcelIdForService(serviceId: str, vpnId: str):
    return Sdwan_mngrClient().GetLanVpnProfileParcelByParcelIdForService(serviceId=serviceId, vpnId=vpnId)

@register('GetInterfaceEthernetParcelsForServiceLanVpn')
def GetInterfaceEthernetParcelsForServiceLanVpn(serviceId: str, vpnId: str):
    return Sdwan_mngrClient().GetInterfaceEthernetParcelsForServiceLanVpn(serviceId=serviceId, vpnId=vpnId)

@register('GetLanVpnInterfaceEthernetParcelByParcelIdForService')
def GetLanVpnInterfaceEthernetParcelByParcelIdForService(ethernetId: str, serviceId: str, vpnId: str):
    return Sdwan_mngrClient().GetLanVpnInterfaceEthernetParcelByParcelIdForService(ethernetId=ethernetId, serviceId=serviceId, vpnId=vpnId)

@register('GetLanVpnInterfaceEthernetAssociatedDhcpServerParcelsForTransport')
def GetLanVpnInterfaceEthernetAssociatedDhcpServerParcelsForTransport(ethernetId: str, serviceId: str, vpnId: str):
    return Sdwan_mngrClient().GetLanVpnInterfaceEthernetAssociatedDhcpServerParcelsForTransport(ethernetId=ethernetId, serviceId=serviceId, vpnId=vpnId)

@register('GetLanVpnInterfaceEthernetAssociatedDhcpServerParcelByParcelIdForTransport')
def GetLanVpnInterfaceEthernetAssociatedDhcpServerParcelByParcelIdForTransport(dhcpServerId: str, ethernetId: str, serviceId: str, vpnId: str):
    return Sdwan_mngrClient().GetLanVpnInterfaceEthernetAssociatedDhcpServerParcelByParcelIdForTransport(dhcpServerId=dhcpServerId, ethernetId=ethernetId, serviceId=serviceId, vpnId=vpnId)

@register('GetLanVpnInterfaceEthernetAssociatedTrackerParcelsForTransport')
def GetLanVpnInterfaceEthernetAssociatedTrackerParcelsForTransport(ethernetId: str, serviceId: str, vpnId: str):
    return Sdwan_mngrClient().GetLanVpnInterfaceEthernetAssociatedTrackerParcelsForTransport(ethernetId=ethernetId, serviceId=serviceId, vpnId=vpnId)

@register('GetLanVpnInterfaceEthernetAssociatedTrackerParcelByParcelIdForTransport')
def GetLanVpnInterfaceEthernetAssociatedTrackerParcelByParcelIdForTransport(ethernetId: str, serviceId: str, trackerId: str, vpnId: str):
    return Sdwan_mngrClient().GetLanVpnInterfaceEthernetAssociatedTrackerParcelByParcelIdForTransport(ethernetId=ethernetId, serviceId=serviceId, trackerId=trackerId, vpnId=vpnId)

@register('GetLanVpnInterfaceEthernetAssociatedTrackerGroupParcelsForTransport')
def GetLanVpnInterfaceEthernetAssociatedTrackerGroupParcelsForTransport(ethernetId: str, serviceId: str, vpnId: str):
    return Sdwan_mngrClient().GetLanVpnInterfaceEthernetAssociatedTrackerGroupParcelsForTransport(ethernetId=ethernetId, serviceId=serviceId, vpnId=vpnId)

@register('GetLanVpnInterfaceEthernetAssociatedTrackerGroupParcelByParcelIdForTransport')
def GetLanVpnInterfaceEthernetAssociatedTrackerGroupParcelByParcelIdForTransport(ethernetId: str, serviceId: str, trackergroupId: str, vpnId: str):
    return Sdwan_mngrClient().GetLanVpnInterfaceEthernetAssociatedTrackerGroupParcelByParcelIdForTransport(ethernetId=ethernetId, serviceId=serviceId, trackergroupId=trackergroupId, vpnId=vpnId)

@register('GetInterfaceGresForServiceLanVpn')
def GetInterfaceGresForServiceLanVpn(serviceId: str, vpnId: str):
    return Sdwan_mngrClient().GetInterfaceGresForServiceLanVpn(serviceId=serviceId, vpnId=vpnId)

@register('GetLanVpnInterfaceGreByIdForService')
def GetLanVpnInterfaceGreByIdForService(greId: str, serviceId: str, vpnId: str):
    return Sdwan_mngrClient().GetLanVpnInterfaceGreByIdForService(greId=greId, serviceId=serviceId, vpnId=vpnId)

@register('getListOfProfileParcels')
def getListOfProfileParcels(serviceId: str, vpnId: str):
    return Sdwan_mngrClient().getListOfProfileParcels(serviceId=serviceId, vpnId=vpnId)

@register('getProfileParcelByParcelId')
def getProfileParcelByParcelId(ipsecId: str, serviceId: str, vpnId: str):
    return Sdwan_mngrClient().getProfileParcelByParcelId(ipsecId=ipsecId, serviceId=serviceId, vpnId=vpnId)

@register('GetLanVpnInterfaceIpsecAssociatedDhcpServerParcelsForTransport')
def GetLanVpnInterfaceIpsecAssociatedDhcpServerParcelsForTransport(ipsecId: str, serviceId: str, vpnId: str):
    return Sdwan_mngrClient().GetLanVpnInterfaceIpsecAssociatedDhcpServerParcelsForTransport(ipsecId=ipsecId, serviceId=serviceId, vpnId=vpnId)

@register('GetLanVpnInterfaceIpsecAssociatedDhcpServerParcelByParcelIdForTransport')
def GetLanVpnInterfaceIpsecAssociatedDhcpServerParcelByParcelIdForTransport(dhcpServerId: str, ipsecId: str, serviceId: str, vpnId: str):
    return Sdwan_mngrClient().GetLanVpnInterfaceIpsecAssociatedDhcpServerParcelByParcelIdForTransport(dhcpServerId=dhcpServerId, ipsecId=ipsecId, serviceId=serviceId, vpnId=vpnId)

@register('GetInterfaceSviParcelsForServiceLanVpn')
def GetInterfaceSviParcelsForServiceLanVpn(serviceId: str, vpnId: str):
    return Sdwan_mngrClient().GetInterfaceSviParcelsForServiceLanVpn(serviceId=serviceId, vpnId=vpnId)

@register('GetLanVpnInterfaceSviParcelByParcelIdForService')
def GetLanVpnInterfaceSviParcelByParcelIdForService(serviceId: str, sviId: str, vpnId: str):
    return Sdwan_mngrClient().GetLanVpnInterfaceSviParcelByParcelIdForService(serviceId=serviceId, sviId=sviId, vpnId=vpnId)

@register('GetLanVpnInterfaceSviAssociatedDhcpServerParcelsForTransport')
def GetLanVpnInterfaceSviAssociatedDhcpServerParcelsForTransport(serviceId: str, sviId: str, vpnId: str):
    return Sdwan_mngrClient().GetLanVpnInterfaceSviAssociatedDhcpServerParcelsForTransport(serviceId=serviceId, sviId=sviId, vpnId=vpnId)

@register('GetLanVpnInterfaceSviAssociatedDhcpServerParcelByParcelIdForTransport')
def GetLanVpnInterfaceSviAssociatedDhcpServerParcelByParcelIdForTransport(dhcpServerId: str, serviceId: str, sviId: str, vpnId: str):
    return Sdwan_mngrClient().GetLanVpnInterfaceSviAssociatedDhcpServerParcelByParcelIdForTransport(dhcpServerId=dhcpServerId, serviceId=serviceId, sviId=sviId, vpnId=vpnId)

@register('GetLanVpnAssociatedRoutingBgpParcelsForService')
def GetLanVpnAssociatedRoutingBgpParcelsForService(serviceId: str, vpnId: str):
    return Sdwan_mngrClient().GetLanVpnAssociatedRoutingBgpParcelsForService(serviceId=serviceId, vpnId=vpnId)

@register('GetLanVpnAssociatedRoutingBgpParcelByParcelIdForService')
def GetLanVpnAssociatedRoutingBgpParcelByParcelIdForService(bgpId: str, serviceId: str, vpnId: str):
    return Sdwan_mngrClient().GetLanVpnAssociatedRoutingBgpParcelByParcelIdForService(bgpId=bgpId, serviceId=serviceId, vpnId=vpnId)

@register('GetLanVpnAssociatedRoutingEigrpParcelsForService')
def GetLanVpnAssociatedRoutingEigrpParcelsForService(serviceId: str, vpnId: str):
    return Sdwan_mngrClient().GetLanVpnAssociatedRoutingEigrpParcelsForService(serviceId=serviceId, vpnId=vpnId)

@register('GetLanVpnAssociatedRoutingEigrpParcelByParcelIdForService')
def GetLanVpnAssociatedRoutingEigrpParcelByParcelIdForService(eigrpId: str, serviceId: str, vpnId: str):
    return Sdwan_mngrClient().GetLanVpnAssociatedRoutingEigrpParcelByParcelIdForService(eigrpId=eigrpId, serviceId=serviceId, vpnId=vpnId)

@register('GetLanVpnAssociatedRoutingMulticastParcelsForService')
def GetLanVpnAssociatedRoutingMulticastParcelsForService(serviceId: str, vpnId: str):
    return Sdwan_mngrClient().GetLanVpnAssociatedRoutingMulticastParcelsForService(serviceId=serviceId, vpnId=vpnId)

@register('GetLanVpnAssociatedRoutingMulticastParcelByParcelIdForService')
def GetLanVpnAssociatedRoutingMulticastParcelByParcelIdForService(multicastId: str, serviceId: str, vpnId: str):
    return Sdwan_mngrClient().GetLanVpnAssociatedRoutingMulticastParcelByParcelIdForService(multicastId=multicastId, serviceId=serviceId, vpnId=vpnId)

@register('GetLanVpnAssociatedRoutingOspfParcelsForService')
def GetLanVpnAssociatedRoutingOspfParcelsForService(serviceId: str, vpnId: str):
    return Sdwan_mngrClient().GetLanVpnAssociatedRoutingOspfParcelsForService(serviceId=serviceId, vpnId=vpnId)

@register('GetLanVpnAssociatedRoutingOspfParcelByParcelIdForService')
def GetLanVpnAssociatedRoutingOspfParcelByParcelIdForService(ospfId: str, serviceId: str, vpnId: str):
    return Sdwan_mngrClient().GetLanVpnAssociatedRoutingOspfParcelByParcelIdForService(ospfId=ospfId, serviceId=serviceId, vpnId=vpnId)

@register('GetLanVpnAssociatedRoutingOspfv3IPv4ParcelsForService')
def GetLanVpnAssociatedRoutingOspfv3IPv4ParcelsForService(serviceId: str, vpnId: str):
    return Sdwan_mngrClient().GetLanVpnAssociatedRoutingOspfv3IPv4ParcelsForService(serviceId=serviceId, vpnId=vpnId)

@register('GetLanVpnAssociatedRoutingOspfv3IPv4ParcelByParcelIdForService')
def GetLanVpnAssociatedRoutingOspfv3IPv4ParcelByParcelIdForService(ospfv3Id: str, serviceId: str, vpnId: str):
    return Sdwan_mngrClient().GetLanVpnAssociatedRoutingOspfv3IPv4ParcelByParcelIdForService(ospfv3Id=ospfv3Id, serviceId=serviceId, vpnId=vpnId)

@register('GetLanVpnAssociatedRoutingOspfv3IPv6ParcelsForService')
def GetLanVpnAssociatedRoutingOspfv3IPv6ParcelsForService(serviceId: str, vpnId: str):
    return Sdwan_mngrClient().GetLanVpnAssociatedRoutingOspfv3IPv6ParcelsForService(serviceId=serviceId, vpnId=vpnId)

@register('GetLanVpnAssociatedRoutingOspfv3IPv6ParcelByParcelIdForService')
def GetLanVpnAssociatedRoutingOspfv3IPv6ParcelByParcelIdForService(ospfv3Id: str, serviceId: str, vpnId: str):
    return Sdwan_mngrClient().GetLanVpnAssociatedRoutingOspfv3IPv6ParcelByParcelIdForService(ospfv3Id=ospfv3Id, serviceId=serviceId, vpnId=vpnId)

@register('GetRoutingBgpProfileParcelForService')
def GetRoutingBgpProfileParcelForService(serviceId: str):
    return Sdwan_mngrClient().GetRoutingBgpProfileParcelForService(serviceId=serviceId)

@register('GetRoutingBgpProfileParcelByParcelIdForService')
def GetRoutingBgpProfileParcelByParcelIdForService(bgpId: str, serviceId: str):
    return Sdwan_mngrClient().GetRoutingBgpProfileParcelByParcelIdForService(bgpId=bgpId, serviceId=serviceId)

@register('GetRoutingEigrpProfileParcelForService')
def GetRoutingEigrpProfileParcelForService(serviceId: str):
    return Sdwan_mngrClient().GetRoutingEigrpProfileParcelForService(serviceId=serviceId)

@register('GetRoutingEigrpProfileParcelByParcelIdForService')
def GetRoutingEigrpProfileParcelByParcelIdForService(eigrpId: str, serviceId: str):
    return Sdwan_mngrClient().GetRoutingEigrpProfileParcelByParcelIdForService(eigrpId=eigrpId, serviceId=serviceId)

@register('GetRoutingMulticastProfileParcelForService')
def GetRoutingMulticastProfileParcelForService(serviceId: str):
    return Sdwan_mngrClient().GetRoutingMulticastProfileParcelForService(serviceId=serviceId)

@register('GetRoutingMulticastProfileParcelByParcelIdForService')
def GetRoutingMulticastProfileParcelByParcelIdForService(multicastId: str, serviceId: str):
    return Sdwan_mngrClient().GetRoutingMulticastProfileParcelByParcelIdForService(multicastId=multicastId, serviceId=serviceId)

@register('GetRoutingOspfProfileParcelForService')
def GetRoutingOspfProfileParcelForService(serviceId: str):
    return Sdwan_mngrClient().GetRoutingOspfProfileParcelForService(serviceId=serviceId)

@register('GetRoutingOspfProfileParcelByParcelIdForService')
def GetRoutingOspfProfileParcelByParcelIdForService(ospfId: str, serviceId: str):
    return Sdwan_mngrClient().GetRoutingOspfProfileParcelByParcelIdForService(ospfId=ospfId, serviceId=serviceId)

@register('GetRoutingOspfv3Ipv4AfProfileParcelForService')
def GetRoutingOspfv3Ipv4AfProfileParcelForService(serviceId: str):
    return Sdwan_mngrClient().GetRoutingOspfv3Ipv4AfProfileParcelForService(serviceId=serviceId)

@register('GetRoutingOspfv3IPv4AfProfileParcelByParcelIdForService')
def GetRoutingOspfv3IPv4AfProfileParcelByParcelIdForService(ospfv3Id: str, serviceId: str):
    return Sdwan_mngrClient().GetRoutingOspfv3IPv4AfProfileParcelByParcelIdForService(ospfv3Id=ospfv3Id, serviceId=serviceId)

@register('GetRoutingOspfv3Ipv6AfProfileParcelForService')
def GetRoutingOspfv3Ipv6AfProfileParcelForService(serviceId: str):
    return Sdwan_mngrClient().GetRoutingOspfv3Ipv6AfProfileParcelForService(serviceId=serviceId)

@register('GetRoutingOspfv3IPv6AfProfileParcelByParcelIdForService')
def GetRoutingOspfv3IPv6AfProfileParcelByParcelIdForService(ospfv3Id: str, serviceId: str):
    return Sdwan_mngrClient().GetRoutingOspfv3IPv6AfProfileParcelByParcelIdForService(ospfv3Id=ospfv3Id, serviceId=serviceId)

@register('GetSwitchportParcelsForService')
def GetSwitchportParcelsForService(serviceId: str):
    return Sdwan_mngrClient().GetSwitchportParcelsForService(serviceId=serviceId)

@register('GetSwitchportParcelByParcelIdForService')
def GetSwitchportParcelByParcelIdForService(serviceId: str, switchportId: str):
    return Sdwan_mngrClient().GetSwitchportParcelByParcelIdForService(serviceId=serviceId, switchportId=switchportId)

@register('GetTrackerProfileParcelForService')
def GetTrackerProfileParcelForService(serviceId: str):
    return Sdwan_mngrClient().GetTrackerProfileParcelForService(serviceId=serviceId)

@register('GetTrackerProfileParcelByParcelIdForService')
def GetTrackerProfileParcelByParcelIdForService(serviceId: str, trackerId: str):
    return Sdwan_mngrClient().GetTrackerProfileParcelByParcelIdForService(serviceId=serviceId, trackerId=trackerId)

@register('GetTrackerGroupProfileParcelForService')
def GetTrackerGroupProfileParcelForService(serviceId: str):
    return Sdwan_mngrClient().GetTrackerGroupProfileParcelForService(serviceId=serviceId)

@register('GetTrackerGroupProfileParcelByParcelIdForService')
def GetTrackerGroupProfileParcelByParcelIdForService(serviceId: str, trackergroupId: str):
    return Sdwan_mngrClient().GetTrackerGroupProfileParcelByParcelIdForService(serviceId=serviceId, trackergroupId=trackergroupId)

@register('GetWirelesslanProfileParcelForService')
def GetWirelesslanProfileParcelForService(serviceId: str):
    return Sdwan_mngrClient().GetWirelesslanProfileParcelForService(serviceId=serviceId)

@register('GetWirelesslanProfileParcelByParcelIdForService')
def GetWirelesslanProfileParcelByParcelIdForService(serviceId: str, wirelesslanId: str):
    return Sdwan_mngrClient().GetWirelesslanProfileParcelByParcelIdForService(serviceId=serviceId, wirelesslanId=wirelesslanId)

@register('GetSdwanSigSecurityFeatureProfiles')
def GetSdwanSigSecurityFeatureProfiles(**kwargs):
    return Sdwan_mngrClient().GetSdwanSigSecurityFeatureProfiles(**kwargs)

@register('GetSdwanSigSecurityFeatureProfileByProfileId')
def GetSdwanSigSecurityFeatureProfileByProfileId(sigSecurityId: str, **kwargs):
    return Sdwan_mngrClient().GetSdwanSigSecurityFeatureProfileByProfileId(sigSecurityId=sigSecurityId, **kwargs)

@register('GetSigSecurityProfileParcel_1')
def GetSigSecurityProfileParcel_1(sigSecurityId: str):
    return Sdwan_mngrClient().GetSigSecurityProfileParcel_1(sigSecurityId=sigSecurityId)

@register('GetSigSecurityProfileParcelByParcelId_1')
def GetSigSecurityProfileParcelByParcelId_1(sigSecurityId: str, sigSecurityProfileParcelId: str):
    return Sdwan_mngrClient().GetSigSecurityProfileParcelByParcelId_1(sigSecurityId=sigSecurityId, sigSecurityProfileParcelId=sigSecurityProfileParcelId)

@register('GetSdwanSystemFeatureProfiles')
def GetSdwanSystemFeatureProfiles(**kwargs):
    return Sdwan_mngrClient().GetSdwanSystemFeatureProfiles(**kwargs)

@register('GetSdwanSystemAaaParcelSchemaBySchemaType')
def GetSdwanSystemAaaParcelSchemaBySchemaType(schemaType: str):
    return Sdwan_mngrClient().GetSdwanSystemAaaParcelSchemaBySchemaType(schemaType=schemaType)

@register('GetSdwanSystemBannerParcelSchemaBySchemaType')
def GetSdwanSystemBannerParcelSchemaBySchemaType(schemaType: str):
    return Sdwan_mngrClient().GetSdwanSystemBannerParcelSchemaBySchemaType(schemaType=schemaType)

@register('GetSdwanSystemBasicFeatureSchemaBySchemaType')
def GetSdwanSystemBasicFeatureSchemaBySchemaType(schemaType: str):
    return Sdwan_mngrClient().GetSdwanSystemBasicFeatureSchemaBySchemaType(schemaType=schemaType)

@register('GetSdwanSystemBfdParcelSchemaBySchemaType')
def GetSdwanSystemBfdParcelSchemaBySchemaType(schemaType: str):
    return Sdwan_mngrClient().GetSdwanSystemBfdParcelSchemaBySchemaType(schemaType=schemaType)

@register('GetCedgeSystemGlobalParcelSchemaBySchemaType')
def GetCedgeSystemGlobalParcelSchemaBySchemaType(schemaType: str):
    return Sdwan_mngrClient().GetCedgeSystemGlobalParcelSchemaBySchemaType(schemaType=schemaType)

@register('GetSdwanSystemLoggingParcelSchemaBySchemaType')
def GetSdwanSystemLoggingParcelSchemaBySchemaType(schemaType: str):
    return Sdwan_mngrClient().GetSdwanSystemLoggingParcelSchemaBySchemaType(schemaType=schemaType)

@register('GetCedgeSystemMrfParcelSchemaBySchemaType')
def GetCedgeSystemMrfParcelSchemaBySchemaType(schemaType: str):
    return Sdwan_mngrClient().GetCedgeSystemMrfParcelSchemaBySchemaType(schemaType=schemaType)

@register('GetSdwanSystemNtpParcelSchemaBySchemaType')
def GetSdwanSystemNtpParcelSchemaBySchemaType(schemaType: str):
    return Sdwan_mngrClient().GetSdwanSystemNtpParcelSchemaBySchemaType(schemaType=schemaType)

@register('GetSdwanSystemOmpParcelSchemaBySchemaType')
def GetSdwanSystemOmpParcelSchemaBySchemaType(schemaType: str):
    return Sdwan_mngrClient().GetSdwanSystemOmpParcelSchemaBySchemaType(schemaType=schemaType)

@register('GetSdwanSystemSnmpParcelSchemaBySchemaType')
def GetSdwanSystemSnmpParcelSchemaBySchemaType(schemaType: str):
    return Sdwan_mngrClient().GetSdwanSystemSnmpParcelSchemaBySchemaType(schemaType=schemaType)

@register('GetSdwanSystemFeatureProfileByProfileId')
def GetSdwanSystemFeatureProfileByProfileId(systemId: str):
    return Sdwan_mngrClient().GetSdwanSystemFeatureProfileByProfileId(systemId=systemId)

@register('GetAaaProfileParcelForSystem')
def GetAaaProfileParcelForSystem(systemId: str):
    return Sdwan_mngrClient().GetAaaProfileParcelForSystem(systemId=systemId)

@register('GetAaaProfileParcelByParcelIdForSystem')
def GetAaaProfileParcelByParcelIdForSystem(aaaId: str, systemId: str):
    return Sdwan_mngrClient().GetAaaProfileParcelByParcelIdForSystem(aaaId=aaaId, systemId=systemId)

@register('GetBannerProfileParcelForSystem')
def GetBannerProfileParcelForSystem(systemId: str):
    return Sdwan_mngrClient().GetBannerProfileParcelForSystem(systemId=systemId)

@register('GetBannerProfileParcelByParcelIdForSystem')
def GetBannerProfileParcelByParcelIdForSystem(bannerId: str, systemId: str):
    return Sdwan_mngrClient().GetBannerProfileParcelByParcelIdForSystem(bannerId=bannerId, systemId=systemId)

@register('GetBasicProfileFeatureForSystem')
def GetBasicProfileFeatureForSystem(systemId: str):
    return Sdwan_mngrClient().GetBasicProfileFeatureForSystem(systemId=systemId)

@register('GetBasicProfileFeatureByFeatureIdForSystem')
def GetBasicProfileFeatureByFeatureIdForSystem(basicId: str, systemId: str):
    return Sdwan_mngrClient().GetBasicProfileFeatureByFeatureIdForSystem(basicId=basicId, systemId=systemId)

@register('GetBfdProfileParcelForSystem')
def GetBfdProfileParcelForSystem(systemId: str):
    return Sdwan_mngrClient().GetBfdProfileParcelForSystem(systemId=systemId)

@register('GetBfdProfileParcelByParcelIdForSystem')
def GetBfdProfileParcelByParcelIdForSystem(bfdId: str, systemId: str):
    return Sdwan_mngrClient().GetBfdProfileParcelByParcelIdForSystem(bfdId=bfdId, systemId=systemId)

@register('GetGlobalProfileParcelForSystem')
def GetGlobalProfileParcelForSystem(systemId: str):
    return Sdwan_mngrClient().GetGlobalProfileParcelForSystem(systemId=systemId)

@register('GetGlobalProfileParcelByParcelIdForSystem')
def GetGlobalProfileParcelByParcelIdForSystem(globalId: str, systemId: str):
    return Sdwan_mngrClient().GetGlobalProfileParcelByParcelIdForSystem(globalId=globalId, systemId=systemId)

@register('GetLoggingProfileParcelForSystem')
def GetLoggingProfileParcelForSystem(systemId: str):
    return Sdwan_mngrClient().GetLoggingProfileParcelForSystem(systemId=systemId)

@register('GetLoggingProfileParcelByParcelIdForSystem')
def GetLoggingProfileParcelByParcelIdForSystem(loggingId: str, systemId: str):
    return Sdwan_mngrClient().GetLoggingProfileParcelByParcelIdForSystem(loggingId=loggingId, systemId=systemId)

@register('GetMrfProfileParcelForSystem')
def GetMrfProfileParcelForSystem(systemId: str):
    return Sdwan_mngrClient().GetMrfProfileParcelForSystem(systemId=systemId)

@register('GetMrfProfileParcelByParcelIdForSystem')
def GetMrfProfileParcelByParcelIdForSystem(mrfId: str, systemId: str):
    return Sdwan_mngrClient().GetMrfProfileParcelByParcelIdForSystem(mrfId=mrfId, systemId=systemId)

@register('GetNtpProfileParcelForSystem')
def GetNtpProfileParcelForSystem(systemId: str):
    return Sdwan_mngrClient().GetNtpProfileParcelForSystem(systemId=systemId)

@register('GetNtpProfileParcelByParcelIdForSystem')
def GetNtpProfileParcelByParcelIdForSystem(ntpId: str, systemId: str):
    return Sdwan_mngrClient().GetNtpProfileParcelByParcelIdForSystem(ntpId=ntpId, systemId=systemId)

@register('GetOmpProfileParcelForSystem')
def GetOmpProfileParcelForSystem(systemId: str):
    return Sdwan_mngrClient().GetOmpProfileParcelForSystem(systemId=systemId)

@register('GetOmpProfileParcelByParcelIdForSystem')
def GetOmpProfileParcelByParcelIdForSystem(ompId: str, systemId: str):
    return Sdwan_mngrClient().GetOmpProfileParcelByParcelIdForSystem(ompId=ompId, systemId=systemId)

@register('GetSecurityForSystem')
def GetSecurityForSystem(systemId: str):
    return Sdwan_mngrClient().GetSecurityForSystem(systemId=systemId)

@register('GetSecurityBySecurityIdForSystem')
def GetSecurityBySecurityIdForSystem(securityId: str, systemId: str):
    return Sdwan_mngrClient().GetSecurityBySecurityIdForSystem(securityId=securityId, systemId=systemId)

@register('GetSnmpProfileParcelForSystem')
def GetSnmpProfileParcelForSystem(systemId: str):
    return Sdwan_mngrClient().GetSnmpProfileParcelForSystem(systemId=systemId)

@register('GetSnmpProfileParcelByParcelIdForSystem')
def GetSnmpProfileParcelByParcelIdForSystem(snmpId: str, systemId: str):
    return Sdwan_mngrClient().GetSnmpProfileParcelByParcelIdForSystem(snmpId=snmpId, systemId=systemId)

@register('GetSdwanTransportFeatureProfiles')
def GetSdwanTransportFeatureProfiles(**kwargs):
    return Sdwan_mngrClient().GetSdwanTransportFeatureProfiles(**kwargs)

@register('GetSdwanTransportCellularControllerParcelSchemaBySchemaType')
def GetSdwanTransportCellularControllerParcelSchemaBySchemaType(schemaType: str):
    return Sdwan_mngrClient().GetSdwanTransportCellularControllerParcelSchemaBySchemaType(schemaType=schemaType)

@register('GetSdwanTransportCellularProfileParcelSchemaBySchemaType')
def GetSdwanTransportCellularProfileParcelSchemaBySchemaType(schemaType: str):
    return Sdwan_mngrClient().GetSdwanTransportCellularProfileParcelSchemaBySchemaType(schemaType=schemaType)

@register('GetSdwanTransportIpv6TrackerParcelSchemaBySchemaType')
def GetSdwanTransportIpv6TrackerParcelSchemaBySchemaType(schemaType: str):
    return Sdwan_mngrClient().GetSdwanTransportIpv6TrackerParcelSchemaBySchemaType(schemaType=schemaType)

@register('GetCedgeTransportIpv6TrackerGroupParcelSchemaBySchemaType')
def GetCedgeTransportIpv6TrackerGroupParcelSchemaBySchemaType(schemaType: str):
    return Sdwan_mngrClient().GetCedgeTransportIpv6TrackerGroupParcelSchemaBySchemaType(schemaType=schemaType)

@register('GetSdwanTransportManagementVpnInterfaceEthernetParcelSchemaBySchema')
def GetSdwanTransportManagementVpnInterfaceEthernetParcelSchemaBySchema(schemaType: str):
    return Sdwan_mngrClient().GetSdwanTransportManagementVpnInterfaceEthernetParcelSchemaBySchema(schemaType=schemaType)

@register('GetSdwanTransportManagementVpnParcelSchemaBySchemaType')
def GetSdwanTransportManagementVpnParcelSchemaBySchemaType(schemaType: str):
    return Sdwan_mngrClient().GetSdwanTransportManagementVpnParcelSchemaBySchemaType(schemaType=schemaType)

@register('GetSdwanTransportRoutingBgpParcelSchemaBySchemaType')
def GetSdwanTransportRoutingBgpParcelSchemaBySchemaType(schemaType: str):
    return Sdwan_mngrClient().GetSdwanTransportRoutingBgpParcelSchemaBySchemaType(schemaType=schemaType)

@register('GetCedgeTransportT1e1controllerParcelSchemaBySchemaType')
def GetCedgeTransportT1e1controllerParcelSchemaBySchemaType(schemaType: str):
    return Sdwan_mngrClient().GetCedgeTransportT1e1controllerParcelSchemaBySchemaType(schemaType=schemaType)

@register('GetSdwanTransportTrackerParcelSchemaBySchemaType')
def GetSdwanTransportTrackerParcelSchemaBySchemaType(schemaType: str):
    return Sdwan_mngrClient().GetSdwanTransportTrackerParcelSchemaBySchemaType(schemaType=schemaType)

@register('GetCedgeTransportTrackerGroupParcelSchemaBySchemaType')
def GetCedgeTransportTrackerGroupParcelSchemaBySchemaType(schemaType: str):
    return Sdwan_mngrClient().GetCedgeTransportTrackerGroupParcelSchemaBySchemaType(schemaType=schemaType)

@register('GetSdwanTransportWanVpnCellularInterfaceParcelSchemaBySchema')
def GetSdwanTransportWanVpnCellularInterfaceParcelSchemaBySchema(schemaType: str):
    return Sdwan_mngrClient().GetSdwanTransportWanVpnCellularInterfaceParcelSchemaBySchema(schemaType=schemaType)

@register('GetSdwanTransportWanVpnInterfaceEthernetParcelSchemaBySchema')
def GetSdwanTransportWanVpnInterfaceEthernetParcelSchemaBySchema(schemaType: str):
    return Sdwan_mngrClient().GetSdwanTransportWanVpnInterfaceEthernetParcelSchemaBySchema(schemaType=schemaType)

@register('GetCedgeTransportWanVpnInterfaceGreParcelSchemaBySchema')
def GetCedgeTransportWanVpnInterfaceGreParcelSchemaBySchema(schemaType: str):
    return Sdwan_mngrClient().GetCedgeTransportWanVpnInterfaceGreParcelSchemaBySchema(schemaType=schemaType)

@register('getSdwanProfileParcelSchema_1')
def getSdwanProfileParcelSchema_1(schemaType: str):
    return Sdwan_mngrClient().getSdwanProfileParcelSchema_1(schemaType=schemaType)

@register('GetCedgeTransportWanVpnInterfaceSerialParcelSchemaBySchema')
def GetCedgeTransportWanVpnInterfaceSerialParcelSchemaBySchema(schemaType: str):
    return Sdwan_mngrClient().GetCedgeTransportWanVpnInterfaceSerialParcelSchemaBySchema(schemaType=schemaType)

@register('GetSdwanTransportWanVpnParcelSchemaBySchemaType')
def GetSdwanTransportWanVpnParcelSchemaBySchemaType(schemaType: str):
    return Sdwan_mngrClient().GetSdwanTransportWanVpnParcelSchemaBySchemaType(schemaType=schemaType)

@register('GetSdwanTransportFeatureProfileByProfileId')
def GetSdwanTransportFeatureProfileByProfileId(transportId: str):
    return Sdwan_mngrClient().GetSdwanTransportFeatureProfileByProfileId(transportId=transportId)

@register('GetCellularControllerProfileParcelForTransport')
def GetCellularControllerProfileParcelForTransport(transportId: str):
    return Sdwan_mngrClient().GetCellularControllerProfileParcelForTransport(transportId=transportId)

@register('GetCellularControllerProfileParcelByParcelIdForTransport')
def GetCellularControllerProfileParcelByParcelIdForTransport(cellularControllerId: str, transportId: str):
    return Sdwan_mngrClient().GetCellularControllerProfileParcelByParcelIdForTransport(cellularControllerId=cellularControllerId, transportId=transportId)

@register('GetCellularControllerAssociatedCellularProfileParcelsForTransport')
def GetCellularControllerAssociatedCellularProfileParcelsForTransport(cellularControllerId: str, transportId: str):
    return Sdwan_mngrClient().GetCellularControllerAssociatedCellularProfileParcelsForTransport(cellularControllerId=cellularControllerId, transportId=transportId)

@register('GetCellularControllerAssociatedCellularProfileParcelByParcelIdForTransport')
def GetCellularControllerAssociatedCellularProfileParcelByParcelIdForTransport(cellularControllerId: str, cellularProfileId: str, transportId: str):
    return Sdwan_mngrClient().GetCellularControllerAssociatedCellularProfileParcelByParcelIdForTransport(cellularControllerId=cellularControllerId, cellularProfileId=cellularProfileId, transportId=transportId)

@register('GetCellularControllerAssociatedGpsParcelsForTransport')
def GetCellularControllerAssociatedGpsParcelsForTransport(cellularControllerId: str, transportId: str):
    return Sdwan_mngrClient().GetCellularControllerAssociatedGpsParcelsForTransport(cellularControllerId=cellularControllerId, transportId=transportId)

@register('GetCellularControllerAssociatedGpsParcelByParcelIdForTransport')
def GetCellularControllerAssociatedGpsParcelByParcelIdForTransport(cellularControllerId: str, gpsId: str, transportId: str):
    return Sdwan_mngrClient().GetCellularControllerAssociatedGpsParcelByParcelIdForTransport(cellularControllerId=cellularControllerId, gpsId=gpsId, transportId=transportId)

@register('GetCellularProfileProfileParcelForTransport')
def GetCellularProfileProfileParcelForTransport(transportId: str):
    return Sdwan_mngrClient().GetCellularProfileProfileParcelForTransport(transportId=transportId)

@register('GetCellularProfileProfileParcelByParcelIdForTransport')
def GetCellularProfileProfileParcelByParcelIdForTransport(cellularProfileId: str, transportId: str):
    return Sdwan_mngrClient().GetCellularProfileProfileParcelByParcelIdForTransport(cellularProfileId=cellularProfileId, transportId=transportId)

@register('GetEsimCellularControllerProfileFeatureForTransport')
def GetEsimCellularControllerProfileFeatureForTransport(transportId: str):
    return Sdwan_mngrClient().GetEsimCellularControllerProfileFeatureForTransport(transportId=transportId)

@register('GetEsimCellularControllerProfileFeatureByFeatureIdForTransport')
def GetEsimCellularControllerProfileFeatureByFeatureIdForTransport(esimCellularControllerId: str, transportId: str):
    return Sdwan_mngrClient().GetEsimCellularControllerProfileFeatureByFeatureIdForTransport(esimCellularControllerId=esimCellularControllerId, transportId=transportId)

@register('GetEsimCellularProfileProfileFeatureForTransport')
def GetEsimCellularProfileProfileFeatureForTransport(transportId: str):
    return Sdwan_mngrClient().GetEsimCellularProfileProfileFeatureForTransport(transportId=transportId)

@register('GetEsimCellularProfileByFeatureIdForTransport')
def GetEsimCellularProfileByFeatureIdForTransport(esimCellularProfileId: str, transportId: str):
    return Sdwan_mngrClient().GetEsimCellularProfileByFeatureIdForTransport(esimCellularProfileId=esimCellularProfileId, transportId=transportId)

@register('GetGpsProfileParcelForTransport')
def GetGpsProfileParcelForTransport(transportId: str):
    return Sdwan_mngrClient().GetGpsProfileParcelForTransport(transportId=transportId)

@register('GetGpsProfileParcelByParcelIdForTransport')
def GetGpsProfileParcelByParcelIdForTransport(gpsId: str, transportId: str):
    return Sdwan_mngrClient().GetGpsProfileParcelByParcelIdForTransport(gpsId=gpsId, transportId=transportId)

@register('GetIpv6TrackerProfileParcelForTransport')
def GetIpv6TrackerProfileParcelForTransport(transportId: str):
    return Sdwan_mngrClient().GetIpv6TrackerProfileParcelForTransport(transportId=transportId)

@register('GetIpv6TrackerProfileParcelByParcelIdForTransport')
def GetIpv6TrackerProfileParcelByParcelIdForTransport(ipv6-trackerId: str, transportId: str):
    return Sdwan_mngrClient().GetIpv6TrackerProfileParcelByParcelIdForTransport(ipv6-trackerId=ipv6-trackerId, transportId=transportId)

@register('GetIpv6TrackerGroupProfileParcelForTransport')
def GetIpv6TrackerGroupProfileParcelForTransport(transportId: str):
    return Sdwan_mngrClient().GetIpv6TrackerGroupProfileParcelForTransport(transportId=transportId)

@register('GetIpv6TrackerGroupProfileParcelByParcelIdForTransport')
def GetIpv6TrackerGroupProfileParcelByParcelIdForTransport(ipv6-trackergroupId: str, transportId: str):
    return Sdwan_mngrClient().GetIpv6TrackerGroupProfileParcelByParcelIdForTransport(ipv6-trackergroupId=ipv6-trackergroupId, transportId=transportId)

@register('GetManagementVpnProfileParcelForTransport')
def GetManagementVpnProfileParcelForTransport(transportId: str):
    return Sdwan_mngrClient().GetManagementVpnProfileParcelForTransport(transportId=transportId)

@register('GetManagementVpnProfileParcelByParcelIdForTransport')
def GetManagementVpnProfileParcelByParcelIdForTransport(transportId: str, vpnId: str):
    return Sdwan_mngrClient().GetManagementVpnProfileParcelByParcelIdForTransport(transportId=transportId, vpnId=vpnId)

@register('GetInterfaceEthernetParcelsForTransportManagementVpn')
def GetInterfaceEthernetParcelsForTransportManagementVpn(transportId: str, vpnId: str):
    return Sdwan_mngrClient().GetInterfaceEthernetParcelsForTransportManagementVpn(transportId=transportId, vpnId=vpnId)

@register('GetManagementVpnInterfaceEthernetParcelByParcelIdForTransport')
def GetManagementVpnInterfaceEthernetParcelByParcelIdForTransport(ethernetId: str, transportId: str, vpnId: str):
    return Sdwan_mngrClient().GetManagementVpnInterfaceEthernetParcelByParcelIdForTransport(ethernetId=ethernetId, transportId=transportId, vpnId=vpnId)

@register('GetRoutingBgpProfileParcelForTransport')
def GetRoutingBgpProfileParcelForTransport(transportId: str):
    return Sdwan_mngrClient().GetRoutingBgpProfileParcelForTransport(transportId=transportId)

@register('GetRoutingBgpProfileParcelByParcelIdForTransport')
def GetRoutingBgpProfileParcelByParcelIdForTransport(bgpId: str, transportId: str):
    return Sdwan_mngrClient().GetRoutingBgpProfileParcelByParcelIdForTransport(bgpId=bgpId, transportId=transportId)

@register('GetRoutingOspfProfileParcelForTransport')
def GetRoutingOspfProfileParcelForTransport(transportId: str):
    return Sdwan_mngrClient().GetRoutingOspfProfileParcelForTransport(transportId=transportId)

@register('GetRoutingOspfProfileParcelByParcelIdForTransport')
def GetRoutingOspfProfileParcelByParcelIdForTransport(ospfId: str, transportId: str):
    return Sdwan_mngrClient().GetRoutingOspfProfileParcelByParcelIdForTransport(ospfId=ospfId, transportId=transportId)

@register('GetRoutingOspfv3Ipv4AfProfileParcelForTransport')
def GetRoutingOspfv3Ipv4AfProfileParcelForTransport(transportId: str):
    return Sdwan_mngrClient().GetRoutingOspfv3Ipv4AfProfileParcelForTransport(transportId=transportId)

@register('GetRoutingOspfv3Ipv4AfProfileParcelByParcelIdForTransport')
def GetRoutingOspfv3Ipv4AfProfileParcelByParcelIdForTransport(ospfv3Id: str, transportId: str):
    return Sdwan_mngrClient().GetRoutingOspfv3Ipv4AfProfileParcelByParcelIdForTransport(ospfv3Id=ospfv3Id, transportId=transportId)

@register('GetRoutingOspfv3Ipv6AfProfileParcelForTransport')
def GetRoutingOspfv3Ipv6AfProfileParcelForTransport(transportId: str):
    return Sdwan_mngrClient().GetRoutingOspfv3Ipv6AfProfileParcelForTransport(transportId=transportId)

@register('GetRoutingOspfv3Ipv6AfProfileParcelByParcelIdForTransport')
def GetRoutingOspfv3Ipv6AfProfileParcelByParcelIdForTransport(ospfv3Id: str, transportId: str):
    return Sdwan_mngrClient().GetRoutingOspfv3Ipv6AfProfileParcelByParcelIdForTransport(ospfv3Id=ospfv3Id, transportId=transportId)

@register('GetT1e1controllerProfileParcelForTransport')
def GetT1e1controllerProfileParcelForTransport(transportId: str):
    return Sdwan_mngrClient().GetT1e1controllerProfileParcelForTransport(transportId=transportId)

@register('GetT1e1controllerProfileParcelByParcelIdForTransport')
def GetT1e1controllerProfileParcelByParcelIdForTransport(t1e1controllerId: str, transportId: str):
    return Sdwan_mngrClient().GetT1e1controllerProfileParcelByParcelIdForTransport(t1e1controllerId=t1e1controllerId, transportId=transportId)

@register('GetTrackerProfileParcelForTransport')
def GetTrackerProfileParcelForTransport(transportId: str):
    return Sdwan_mngrClient().GetTrackerProfileParcelForTransport(transportId=transportId)

@register('GetTrackerProfileParcelByParcelIdForTransport')
def GetTrackerProfileParcelByParcelIdForTransport(trackerId: str, transportId: str):
    return Sdwan_mngrClient().GetTrackerProfileParcelByParcelIdForTransport(trackerId=trackerId, transportId=transportId)

@register('GetTrackerGroupProfileParcelForTransport')
def GetTrackerGroupProfileParcelForTransport(transportId: str):
    return Sdwan_mngrClient().GetTrackerGroupProfileParcelForTransport(transportId=transportId)

@register('GetTrackerGroupProfileParcelByParcelIdForTransport')
def GetTrackerGroupProfileParcelByParcelIdForTransport(trackergroupId: str, transportId: str):
    return Sdwan_mngrClient().GetTrackerGroupProfileParcelByParcelIdForTransport(trackergroupId=trackergroupId, transportId=transportId)

@register('GetWanVpnProfileParcelForTransport')
def GetWanVpnProfileParcelForTransport(transportId: str):
    return Sdwan_mngrClient().GetWanVpnProfileParcelForTransport(transportId=transportId)

@register('GetWanVpnProfileParcelByParcelIdForTransport')
def GetWanVpnProfileParcelByParcelIdForTransport(transportId: str, vpnId: str):
    return Sdwan_mngrClient().GetWanVpnProfileParcelByParcelIdForTransport(transportId=transportId, vpnId=vpnId)

@register('GetInterfaceCellularParcelsForTransportWanVpn')
def GetInterfaceCellularParcelsForTransportWanVpn(transportId: str, vpnId: str):
    return Sdwan_mngrClient().GetInterfaceCellularParcelsForTransportWanVpn(transportId=transportId, vpnId=vpnId)

@register('GetWanVpnInterfaceCellularAssociatedIpv6TrackerParcelsForTransport')
def GetWanVpnInterfaceCellularAssociatedIpv6TrackerParcelsForTransport(cellularId: str, transportId: str, vpnId: str):
    return Sdwan_mngrClient().GetWanVpnInterfaceCellularAssociatedIpv6TrackerParcelsForTransport(cellularId=cellularId, transportId=transportId, vpnId=vpnId)

@register('GetWanVpnInterfaceCellularAssociatedIpv6TrackerParcelByParcelIdForTransport')
def GetWanVpnInterfaceCellularAssociatedIpv6TrackerParcelByParcelIdForTransport(cellularId: str, ipv6-trackerId: str, transportId: str, vpnId: str):
    return Sdwan_mngrClient().GetWanVpnInterfaceCellularAssociatedIpv6TrackerParcelByParcelIdForTransport(cellularId=cellularId, ipv6-trackerId=ipv6-trackerId, transportId=transportId, vpnId=vpnId)

@register('GetWanVpnInterfaceCellularAssociatedIpv6TrackerGroupParcelsForTransport')
def GetWanVpnInterfaceCellularAssociatedIpv6TrackerGroupParcelsForTransport(cellularId: str, transportId: str, vpnId: str):
    return Sdwan_mngrClient().GetWanVpnInterfaceCellularAssociatedIpv6TrackerGroupParcelsForTransport(cellularId=cellularId, transportId=transportId, vpnId=vpnId)

@register('GetWanVpnInterfaceCellularAssociatedIpv6TrackerGroupParcelByParcelIdForTransport')
def GetWanVpnInterfaceCellularAssociatedIpv6TrackerGroupParcelByParcelIdForTransport(cellularId: str, ipv6-trackergroupId: str, transportId: str, vpnId: str):
    return Sdwan_mngrClient().GetWanVpnInterfaceCellularAssociatedIpv6TrackerGroupParcelByParcelIdForTransport(cellularId=cellularId, ipv6-trackergroupId=ipv6-trackergroupId, transportId=transportId, vpnId=vpnId)

@register('GetWanVpnInterfaceCellularAssociatedTrackerParcelsForTransport')
def GetWanVpnInterfaceCellularAssociatedTrackerParcelsForTransport(cellularId: str, transportId: str, vpnId: str):
    return Sdwan_mngrClient().GetWanVpnInterfaceCellularAssociatedTrackerParcelsForTransport(cellularId=cellularId, transportId=transportId, vpnId=vpnId)

@register('GetWanVpnInterfaceCellularAssociatedTrackerParcelByParcelIdForTransport')
def GetWanVpnInterfaceCellularAssociatedTrackerParcelByParcelIdForTransport(cellularId: str, trackerId: str, transportId: str, vpnId: str):
    return Sdwan_mngrClient().GetWanVpnInterfaceCellularAssociatedTrackerParcelByParcelIdForTransport(cellularId=cellularId, trackerId=trackerId, transportId=transportId, vpnId=vpnId)

@register('GetWanVpnInterfaceCellularAssociatedTrackerGroupParcelsForTransport')
def GetWanVpnInterfaceCellularAssociatedTrackerGroupParcelsForTransport(cellularId: str, transportId: str, vpnId: str):
    return Sdwan_mngrClient().GetWanVpnInterfaceCellularAssociatedTrackerGroupParcelsForTransport(cellularId=cellularId, transportId=transportId, vpnId=vpnId)

@register('GetWanVpnInterfaceCellularAssociatedTrackerGroupParcelByParcelIdForTransport')
def GetWanVpnInterfaceCellularAssociatedTrackerGroupParcelByParcelIdForTransport(cellularId: str, trackerGroupId: str, transportId: str, vpnId: str):
    return Sdwan_mngrClient().GetWanVpnInterfaceCellularAssociatedTrackerGroupParcelByParcelIdForTransport(cellularId=cellularId, trackerGroupId=trackerGroupId, transportId=transportId, vpnId=vpnId)

@register('GetWanVpnInterfaceCellularParcelByParcelIdForTransport')
def GetWanVpnInterfaceCellularParcelByParcelIdForTransport(intfId: str, transportId: str, vpnId: str):
    return Sdwan_mngrClient().GetWanVpnInterfaceCellularParcelByParcelIdForTransport(intfId=intfId, transportId=transportId, vpnId=vpnId)

@register('GetInterfaceEthernetParcelsForTransportWanVpn')
def GetInterfaceEthernetParcelsForTransportWanVpn(transportId: str, vpnId: str):
    return Sdwan_mngrClient().GetInterfaceEthernetParcelsForTransportWanVpn(transportId=transportId, vpnId=vpnId)

@register('GetWanVpnInterfaceEthernetParcelByParcelIdForTransport')
def GetWanVpnInterfaceEthernetParcelByParcelIdForTransport(ethernetId: str, transportId: str, vpnId: str):
    return Sdwan_mngrClient().GetWanVpnInterfaceEthernetParcelByParcelIdForTransport(ethernetId=ethernetId, transportId=transportId, vpnId=vpnId)

@register('GetWanVpnInterfaceEthernetAssociatedIpv6TrackerParcelsForTransport')
def GetWanVpnInterfaceEthernetAssociatedIpv6TrackerParcelsForTransport(ethernetId: str, transportId: str, vpnId: str):
    return Sdwan_mngrClient().GetWanVpnInterfaceEthernetAssociatedIpv6TrackerParcelsForTransport(ethernetId=ethernetId, transportId=transportId, vpnId=vpnId)

@register('GetWanVpnInterfaceEthernetAssociatedIpv6TrackerParcelByParcelIdForTransport')
def GetWanVpnInterfaceEthernetAssociatedIpv6TrackerParcelByParcelIdForTransport(ethernetId: str, ipv6-trackerId: str, transportId: str, vpnId: str):
    return Sdwan_mngrClient().GetWanVpnInterfaceEthernetAssociatedIpv6TrackerParcelByParcelIdForTransport(ethernetId=ethernetId, ipv6-trackerId=ipv6-trackerId, transportId=transportId, vpnId=vpnId)

@register('GetWanVpnInterfaceEthernetAssociatedIpv6TrackerGroupParcelsForTransport')
def GetWanVpnInterfaceEthernetAssociatedIpv6TrackerGroupParcelsForTransport(ethernetId: str, transportId: str, vpnId: str):
    return Sdwan_mngrClient().GetWanVpnInterfaceEthernetAssociatedIpv6TrackerGroupParcelsForTransport(ethernetId=ethernetId, transportId=transportId, vpnId=vpnId)

@register('GetWanVpnInterfaceEthernetAssociatedIpv6TrackerGroupParcelByParcelIdForTransport')
def GetWanVpnInterfaceEthernetAssociatedIpv6TrackerGroupParcelByParcelIdForTransport(ethernetId: str, ipv6-trackergroupId: str, transportId: str, vpnId: str):
    return Sdwan_mngrClient().GetWanVpnInterfaceEthernetAssociatedIpv6TrackerGroupParcelByParcelIdForTransport(ethernetId=ethernetId, ipv6-trackergroupId=ipv6-trackergroupId, transportId=transportId, vpnId=vpnId)

@register('GetWanVpnInterfaceEthernetAssociatedTrackerParcelsForTransport')
def GetWanVpnInterfaceEthernetAssociatedTrackerParcelsForTransport(ethernetId: str, transportId: str, vpnId: str):
    return Sdwan_mngrClient().GetWanVpnInterfaceEthernetAssociatedTrackerParcelsForTransport(ethernetId=ethernetId, transportId=transportId, vpnId=vpnId)

@register('GetWanVpnInterfaceEthernetAssociatedTrackerParcelByParcelIdForTransport')
def GetWanVpnInterfaceEthernetAssociatedTrackerParcelByParcelIdForTransport(ethernetId: str, trackerId: str, transportId: str, vpnId: str):
    return Sdwan_mngrClient().GetWanVpnInterfaceEthernetAssociatedTrackerParcelByParcelIdForTransport(ethernetId=ethernetId, trackerId=trackerId, transportId=transportId, vpnId=vpnId)

@register('GetWanVpnInterfaceEthernetAssociatedTrackerGroupParcelsForTransport')
def GetWanVpnInterfaceEthernetAssociatedTrackerGroupParcelsForTransport(ethernetId: str, transportId: str, vpnId: str):
    return Sdwan_mngrClient().GetWanVpnInterfaceEthernetAssociatedTrackerGroupParcelsForTransport(ethernetId=ethernetId, transportId=transportId, vpnId=vpnId)

@register('GetWanVpnInterfaceEthernetAssociatedTrackerGroupParcelByParcelIdForTransport')
def GetWanVpnInterfaceEthernetAssociatedTrackerGroupParcelByParcelIdForTransport(ethernetId: str, trackergroupId: str, transportId: str, vpnId: str):
    return Sdwan_mngrClient().GetWanVpnInterfaceEthernetAssociatedTrackerGroupParcelByParcelIdForTransport(ethernetId=ethernetId, trackergroupId=trackergroupId, transportId=transportId, vpnId=vpnId)

@register('GetInterfaceGreParcelsForTransportWanVpn')
def GetInterfaceGreParcelsForTransportWanVpn(transportId: str, vpnId: str):
    return Sdwan_mngrClient().GetInterfaceGreParcelsForTransportWanVpn(transportId=transportId, vpnId=vpnId)

@register('GetWanVpnInterfaceGreParcelByParcelIdForTransport')
def GetWanVpnInterfaceGreParcelByParcelIdForTransport(greId: str, transportId: str, vpnId: str):
    return Sdwan_mngrClient().GetWanVpnInterfaceGreParcelByParcelIdForTransport(greId=greId, transportId=transportId, vpnId=vpnId)

@register('GetWanVpnInterfaceGreAssociatedTrackerParcelsForTransport')
def GetWanVpnInterfaceGreAssociatedTrackerParcelsForTransport(greId: str, transportId: str, vpnId: str):
    return Sdwan_mngrClient().GetWanVpnInterfaceGreAssociatedTrackerParcelsForTransport(greId=greId, transportId=transportId, vpnId=vpnId)

@register('GetWanVpnInterfaceGreAssociatedTrackerParcelByParcelIdForTransport')
def GetWanVpnInterfaceGreAssociatedTrackerParcelByParcelIdForTransport(greId: str, trackerId: str, transportId: str, vpnId: str):
    return Sdwan_mngrClient().GetWanVpnInterfaceGreAssociatedTrackerParcelByParcelIdForTransport(greId=greId, trackerId=trackerId, transportId=transportId, vpnId=vpnId)

@register('getListOfProfileParcels_1')
def getListOfProfileParcels_1(transportId: str, vpnId: str):
    return Sdwan_mngrClient().getListOfProfileParcels_1(transportId=transportId, vpnId=vpnId)

@register('getProfileParcelByParcelId_1')
def getProfileParcelByParcelId_1(ipsecId: str, transportId: str, vpnId: str):
    return Sdwan_mngrClient().getProfileParcelByParcelId_1(ipsecId=ipsecId, transportId=transportId, vpnId=vpnId)

@register('GetWanVpnInterfaceIpsecAssociatedTrackerParcelsForTransport')
def GetWanVpnInterfaceIpsecAssociatedTrackerParcelsForTransport(ipsecId: str, transportId: str, vpnId: str):
    return Sdwan_mngrClient().GetWanVpnInterfaceIpsecAssociatedTrackerParcelsForTransport(ipsecId=ipsecId, transportId=transportId, vpnId=vpnId)

@register('GetWanVpnInterfaceIpsecAssociatedTrackerParcelByParcelIdForTransport')
def GetWanVpnInterfaceIpsecAssociatedTrackerParcelByParcelIdForTransport(ipsecId: str, trackerId: str, transportId: str, vpnId: str):
    return Sdwan_mngrClient().GetWanVpnInterfaceIpsecAssociatedTrackerParcelByParcelIdForTransport(ipsecId=ipsecId, trackerId=trackerId, transportId=transportId, vpnId=vpnId)

@register('GetInterfaceSerialParcelsForTransportWanVpn')
def GetInterfaceSerialParcelsForTransportWanVpn(transportId: str, vpnId: str):
    return Sdwan_mngrClient().GetInterfaceSerialParcelsForTransportWanVpn(transportId=transportId, vpnId=vpnId)

@register('GetWanVpnInterfaceSerialParcelByParcelIdForTransport')
def GetWanVpnInterfaceSerialParcelByParcelIdForTransport(serialId: str, transportId: str, vpnId: str):
    return Sdwan_mngrClient().GetWanVpnInterfaceSerialParcelByParcelIdForTransport(serialId=serialId, transportId=transportId, vpnId=vpnId)

@register('GetWanVpnAssociatedRoutingBgpParcelsForTransport')
def GetWanVpnAssociatedRoutingBgpParcelsForTransport(transportId: str, vpnId: str):
    return Sdwan_mngrClient().GetWanVpnAssociatedRoutingBgpParcelsForTransport(transportId=transportId, vpnId=vpnId)

@register('GetWanVpnAssociatedRoutingBgpParcelByParcelIdForTransport')
def GetWanVpnAssociatedRoutingBgpParcelByParcelIdForTransport(bgpId: str, transportId: str, vpnId: str):
    return Sdwan_mngrClient().GetWanVpnAssociatedRoutingBgpParcelByParcelIdForTransport(bgpId=bgpId, transportId=transportId, vpnId=vpnId)

@register('GetWanVpnAssociatedRoutingOspfParcelsForTransport')
def GetWanVpnAssociatedRoutingOspfParcelsForTransport(transportId: str, vpnId: str):
    return Sdwan_mngrClient().GetWanVpnAssociatedRoutingOspfParcelsForTransport(transportId=transportId, vpnId=vpnId)

@register('GetWanVpnAssociatedRoutingOspfParcelByParcelIdForTransport')
def GetWanVpnAssociatedRoutingOspfParcelByParcelIdForTransport(ospfId: str, transportId: str, vpnId: str):
    return Sdwan_mngrClient().GetWanVpnAssociatedRoutingOspfParcelByParcelIdForTransport(ospfId=ospfId, transportId=transportId, vpnId=vpnId)

@register('GetWanVpnAssociatedRoutingOspfv3IPv4AfParcelsForTransport')
def GetWanVpnAssociatedRoutingOspfv3IPv4AfParcelsForTransport(transportId: str, vpnId: str):
    return Sdwan_mngrClient().GetWanVpnAssociatedRoutingOspfv3IPv4AfParcelsForTransport(transportId=transportId, vpnId=vpnId)

@register('GetWanVpnAssociatedRoutingOspfv3IPv4AfParcelByParcelIdForTransport')
def GetWanVpnAssociatedRoutingOspfv3IPv4AfParcelByParcelIdForTransport(ospfv3Id: str, transportId: str, vpnId: str):
    return Sdwan_mngrClient().GetWanVpnAssociatedRoutingOspfv3IPv4AfParcelByParcelIdForTransport(ospfv3Id=ospfv3Id, transportId=transportId, vpnId=vpnId)

@register('GetWanVpnAssociatedRoutingOspfv3IPv6AfParcelsForTransport')
def GetWanVpnAssociatedRoutingOspfv3IPv6AfParcelsForTransport(transportId: str, vpnId: str):
    return Sdwan_mngrClient().GetWanVpnAssociatedRoutingOspfv3IPv6AfParcelsForTransport(transportId=transportId, vpnId=vpnId)

@register('GetWanVpnAssociatedRoutingOspfv3IPv6AfParcelByParcelIdForTransport')
def GetWanVpnAssociatedRoutingOspfv3IPv6AfParcelByParcelIdForTransport(ospfv3Id: str, transportId: str, vpnId: str):
    return Sdwan_mngrClient().GetWanVpnAssociatedRoutingOspfv3IPv6AfParcelByParcelIdForTransport(ospfv3Id=ospfv3Id, transportId=transportId, vpnId=vpnId)

@register('getMSLADevices')
def getMSLADevices():
    return Sdwan_mngrClient().getMSLADevices()

@register('getLicenseByUuid')
def getLicenseByUuid(uuid: str):
    return Sdwan_mngrClient().getLicenseByUuid(uuid=uuid)

@register('GetPolicyGroupBySolution')
def GetPolicyGroupBySolution(**kwargs):
    return Sdwan_mngrClient().GetPolicyGroupBySolution(**kwargs)

@register('GetPolicyGroup')
def GetPolicyGroup(policyGroupId: str):
    return Sdwan_mngrClient().GetPolicyGroup(policyGroupId=policyGroupId)

@register('GetPolicyGroupAssociation')
def GetPolicyGroupAssociation(policyGroupId: str):
    return Sdwan_mngrClient().GetPolicyGroupAssociation(policyGroupId=policyGroupId)

@register('getPolicyGroupDeviceVariables')
def getPolicyGroupDeviceVariables(policyGroupId: str, **kwargs):
    return Sdwan_mngrClient().getPolicyGroupDeviceVariables(policyGroupId=policyGroupId, **kwargs)

@register('getPolicyGroupDeviceVariablesSchema')
def getPolicyGroupDeviceVariablesSchema(policyGroupId: str):
    return Sdwan_mngrClient().getPolicyGroupDeviceVariablesSchema(policyGroupId=policyGroupId)

@register('getAllReportTemplates')
def getAllReportTemplates():
    return Sdwan_mngrClient().getAllReportTemplates()

@register('downloadReportPreviewFile')
def downloadReportPreviewFile(**kwargs):
    return Sdwan_mngrClient().downloadReportPreviewFile(**kwargs)

@register('getReportTemplateById')
def getReportTemplateById(reportId: str):
    return Sdwan_mngrClient().getReportTemplateById(reportId=reportId)

@register('getAllReportTasksByReportId')
def getAllReportTasksByReportId(reportId: str):
    return Sdwan_mngrClient().getAllReportTasksByReportId(reportId=reportId)

@register('downloadReportDataFile')
def downloadReportDataFile(reportId: str, taskId: str):
    return Sdwan_mngrClient().downloadReportDataFile(reportId=reportId, taskId=taskId)

@register('getUrlForSdoIdentityService')
def getUrlForSdoIdentityService():
    return Sdwan_mngrClient().getUrlForSdoIdentityService()

@register('getAllAccounts')
def getAllAccounts():
    return Sdwan_mngrClient().getAllAccounts()

@register('getRatePlansByAcctId')
def getRatePlansByAcctId(accountId: str):
    return Sdwan_mngrClient().getRatePlansByAcctId(accountId=accountId)

@register('getProvidersInfo')
def getProvidersInfo():
    return Sdwan_mngrClient().getProvidersInfo()

@register('getCommPlansByAcctId')
def getCommPlansByAcctId(accountId: str):
    return Sdwan_mngrClient().getCommPlansByAcctId(accountId=accountId)

@register('getProviderCredentialsByAccountId')
def getProviderCredentialsByAccountId(accountId: str):
    return Sdwan_mngrClient().getProviderCredentialsByAccountId(accountId=accountId)

@register('getDeviceDataUsage')
def getDeviceDataUsage(deviceUUID: str):
    return Sdwan_mngrClient().getDeviceDataUsage(deviceUUID=deviceUUID)

@register('serviceChainMapping')
def serviceChainMapping():
    return Sdwan_mngrClient().serviceChainMapping()

@register('getDevicesForTemplate')
def getDevicesForTemplate(**kwargs):
    return Sdwan_mngrClient().getDevicesForTemplate(**kwargs)

@register('license')
def license(licenseType: str, virtual_account_id: str):
    return Sdwan_mngrClient().license(licenseType=licenseType, virtual_account_id=virtual_account_id)

@register('getUserSettings')
def getUserSettings():
    return Sdwan_mngrClient().getUserSettings()

@register('GetTopologyGroupBySolution')
def GetTopologyGroupBySolution(**kwargs):
    return Sdwan_mngrClient().GetTopologyGroupBySolution(**kwargs)

@register('GetTopologyGroup')
def GetTopologyGroup(topologyGroupId: str):
    return Sdwan_mngrClient().GetTopologyGroup(topologyGroupId=topologyGroupId)

@register('generateDeviceInterfaceStatisticsData')
def generateDeviceInterfaceStatisticsData(**kwargs):
    return Sdwan_mngrClient().generateDeviceInterfaceStatisticsData(**kwargs)

@register('getCountWithInterfaceStatistics')
def getCountWithInterfaceStatistics(endDate: str, startDate: str, **kwargs):
    return Sdwan_mngrClient().getCountWithInterfaceStatistics(endDate=endDate, startDate=startDate, **kwargs)

@register('getStatDataFieldsByInterfaceStatistics')
def getStatDataFieldsByInterfaceStatistics():
    return Sdwan_mngrClient().getStatDataFieldsByInterfaceStatistics()

@register('getWaniRecommendations')
def getWaniRecommendations(**kwargs):
    return Sdwan_mngrClient().getWaniRecommendations(**kwargs)

@register('getAppliedWaniRecommendations')
def getAppliedWaniRecommendations():
    return Sdwan_mngrClient().getAppliedWaniRecommendations()

@register('getListActivationStatus')
def getListActivationStatus(listId: str, listType: str):
    return Sdwan_mngrClient().getListActivationStatus(listId=listId, listType=listType)

@register('getPolicyActivationStatus')
def getPolicyActivationStatus(policyId: str, policyType: str):
    return Sdwan_mngrClient().getPolicyActivationStatus(policyId=policyId, policyType=policyType)

@register('webexAccessCode')
def webexAccessCode():
    return Sdwan_mngrClient().webexAccessCode()

@register('getWebexDataCentersSyncStatus')
def getWebexDataCentersSyncStatus():
    return Sdwan_mngrClient().getWebexDataCentersSyncStatus()

@register('redirectWebexDataCenters')
def redirectWebexDataCenters(code: str):
    return Sdwan_mngrClient().redirectWebexDataCenters(code=code)
