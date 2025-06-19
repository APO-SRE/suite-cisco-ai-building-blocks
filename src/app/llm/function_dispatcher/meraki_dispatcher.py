# app/llm/function_dispatcher/meraki_dispatcher.py
from typing import Any
from app.llm.function_dispatcher import register
from app.llm.platform_clients.meraki_client import MerakiClient

@register('getAdministeredIdentitiesMe')
def getAdministeredIdentitiesMe():
    return MerakiClient().getAdministeredIdentitiesMe(**{})

@register('getAdministeredIdentitiesMeApiKeys')
def getAdministeredIdentitiesMeApiKeys():
    return MerakiClient().getAdministeredIdentitiesMeApiKeys(**{})

@register('getAdministeredLicensingSubscriptionEntitlements')
def getAdministeredLicensingSubscriptionEntitlements(**kwargs):
    return MerakiClient().getAdministeredLicensingSubscriptionEntitlements(**{**kwargs})

@register('getAdministeredLicensingSubscriptionSubscriptions')
def getAdministeredLicensingSubscriptionSubscriptions(**kwargs):
    return MerakiClient().getAdministeredLicensingSubscriptionSubscriptions(**{**kwargs})

@register('getAdministeredLicensingSubscriptionSubscriptionsComplianceStatu')
def getAdministeredLicensingSubscriptionSubscriptionsComplianceStatu(organizationIds: list, **kwargs):
    return MerakiClient().getAdministeredLicensingSubscriptionSubscriptionsComplianceStatu(**{'organizationIds': organizationIds, **kwargs})

@register('getDevice')
def getDevice(serial: str):
    return MerakiClient().getDevice(**{'serial': serial})

@register('getDeviceApplianceDhcpSubnets')
def getDeviceApplianceDhcpSubnets(serial: str):
    return MerakiClient().getDeviceApplianceDhcpSubnets(**{'serial': serial})

@register('getDeviceAppliancePerformance')
def getDeviceAppliancePerformance(serial: str, **kwargs):
    return MerakiClient().getDeviceAppliancePerformance(**{'serial': serial, **kwargs})

@register('getDeviceAppliancePrefixesDelegated')
def getDeviceAppliancePrefixesDelegated(serial: str):
    return MerakiClient().getDeviceAppliancePrefixesDelegated(**{'serial': serial})

@register('getDeviceAppliancePrefixesDelegatedVlanAssignments')
def getDeviceAppliancePrefixesDelegatedVlanAssignments(serial: str):
    return MerakiClient().getDeviceAppliancePrefixesDelegatedVlanAssignments(**{'serial': serial})

@register('getDeviceApplianceRadioSettings')
def getDeviceApplianceRadioSettings(serial: str):
    return MerakiClient().getDeviceApplianceRadioSettings(**{'serial': serial})

@register('getDeviceApplianceUplinksSettings')
def getDeviceApplianceUplinksSettings(serial: str):
    return MerakiClient().getDeviceApplianceUplinksSettings(**{'serial': serial})

@register('getDeviceCameraAnalyticsLive')
def getDeviceCameraAnalyticsLive(serial: str):
    return MerakiClient().getDeviceCameraAnalyticsLive(**{'serial': serial})

@register('getDeviceCameraAnalyticsOverview')
def getDeviceCameraAnalyticsOverview(serial: str, **kwargs):
    return MerakiClient().getDeviceCameraAnalyticsOverview(**{'serial': serial, **kwargs})

@register('getDeviceCameraAnalyticsRecent')
def getDeviceCameraAnalyticsRecent(serial: str, **kwargs):
    return MerakiClient().getDeviceCameraAnalyticsRecent(**{'serial': serial, **kwargs})

@register('getDeviceCameraAnalyticsZones')
def getDeviceCameraAnalyticsZones(serial: str):
    return MerakiClient().getDeviceCameraAnalyticsZones(**{'serial': serial})

@register('getDeviceCameraAnalyticsZoneHistory')
def getDeviceCameraAnalyticsZoneHistory(serial: str, zoneId: str, **kwargs):
    return MerakiClient().getDeviceCameraAnalyticsZoneHistory(**{'serial': serial, 'zoneId': zoneId, **kwargs})

@register('getDeviceCameraCustomAnalytics')
def getDeviceCameraCustomAnalytics(serial: str):
    return MerakiClient().getDeviceCameraCustomAnalytics(**{'serial': serial})

@register('getDeviceCameraQualityAndRetention')
def getDeviceCameraQualityAndRetention(serial: str):
    return MerakiClient().getDeviceCameraQualityAndRetention(**{'serial': serial})

@register('getDeviceCameraSense')
def getDeviceCameraSense(serial: str):
    return MerakiClient().getDeviceCameraSense(**{'serial': serial})

@register('getDeviceCameraSenseObjectDetectionModels')
def getDeviceCameraSenseObjectDetectionModels(serial: str):
    return MerakiClient().getDeviceCameraSenseObjectDetectionModels(**{'serial': serial})

@register('getDeviceCameraVideoSettings')
def getDeviceCameraVideoSettings(serial: str):
    return MerakiClient().getDeviceCameraVideoSettings(**{'serial': serial})

@register('getDeviceCameraVideoLink')
def getDeviceCameraVideoLink(serial: str, **kwargs):
    return MerakiClient().getDeviceCameraVideoLink(**{'serial': serial, **kwargs})

@register('getDeviceCameraWirelessProfiles')
def getDeviceCameraWirelessProfiles(serial: str):
    return MerakiClient().getDeviceCameraWirelessProfiles(**{'serial': serial})

@register('getDeviceCellularSims')
def getDeviceCellularSims(serial: str):
    return MerakiClient().getDeviceCellularSims(**{'serial': serial})

@register('getDeviceCellularGatewayLan')
def getDeviceCellularGatewayLan(serial: str):
    return MerakiClient().getDeviceCellularGatewayLan(**{'serial': serial})

@register('getDeviceCellularGatewayPortForwardingRules')
def getDeviceCellularGatewayPortForwardingRules(serial: str):
    return MerakiClient().getDeviceCellularGatewayPortForwardingRules(**{'serial': serial})

@register('getDeviceClients')
def getDeviceClients(serial: str, **kwargs):
    return MerakiClient().getDeviceClients(**{'serial': serial, **kwargs})

@register('getDeviceLiveToolsArpTable')
def getDeviceLiveToolsArpTable(arpTableId: str, serial: str):
    return MerakiClient().getDeviceLiveToolsArpTable(**{'arpTableId': arpTableId, 'serial': serial})

@register('getDeviceLiveToolsCableTest')
def getDeviceLiveToolsCableTest(id: str, serial: str):
    return MerakiClient().getDeviceLiveToolsCableTest(**{'id': id, 'serial': serial})

@register('getDeviceLiveToolsLedsBlink')
def getDeviceLiveToolsLedsBlink(ledsBlinkId: str, serial: str):
    return MerakiClient().getDeviceLiveToolsLedsBlink(**{'ledsBlinkId': ledsBlinkId, 'serial': serial})

@register('getDeviceLiveToolsPing')
def getDeviceLiveToolsPing(id: str, serial: str):
    return MerakiClient().getDeviceLiveToolsPing(**{'id': id, 'serial': serial})

@register('getDeviceLiveToolsPingDevice')
def getDeviceLiveToolsPingDevice(id: str, serial: str):
    return MerakiClient().getDeviceLiveToolsPingDevice(**{'id': id, 'serial': serial})

@register('getDeviceLiveToolsThroughputTest')
def getDeviceLiveToolsThroughputTest(serial: str, throughputTestId: str):
    return MerakiClient().getDeviceLiveToolsThroughputTest(**{'serial': serial, 'throughputTestId': throughputTestId})

@register('getDeviceLiveToolsWakeOnLan')
def getDeviceLiveToolsWakeOnLan(serial: str, wakeOnLanId: str):
    return MerakiClient().getDeviceLiveToolsWakeOnLan(**{'serial': serial, 'wakeOnLanId': wakeOnLanId})

@register('getDeviceLldpCdp')
def getDeviceLldpCdp(serial: str):
    return MerakiClient().getDeviceLldpCdp(**{'serial': serial})

@register('getDeviceLossAndLatencyHistory')
def getDeviceLossAndLatencyHistory(ip: str, serial: str, **kwargs):
    return MerakiClient().getDeviceLossAndLatencyHistory(**{'ip': ip, 'serial': serial, **kwargs})

@register('getDeviceManagementInterface')
def getDeviceManagementInterface(serial: str):
    return MerakiClient().getDeviceManagementInterface(**{'serial': serial})

@register('getDeviceSensorCommands')
def getDeviceSensorCommands(serial: str, **kwargs):
    return MerakiClient().getDeviceSensorCommands(**{'serial': serial, **kwargs})

@register('getDeviceSensorCommand')
def getDeviceSensorCommand(commandId: str, serial: str):
    return MerakiClient().getDeviceSensorCommand(**{'commandId': commandId, 'serial': serial})

@register('getDeviceSensorRelationships')
def getDeviceSensorRelationships(serial: str):
    return MerakiClient().getDeviceSensorRelationships(**{'serial': serial})

@register('getDeviceSwitchPorts')
def getDeviceSwitchPorts(serial: str):
    return MerakiClient().getDeviceSwitchPorts(**{'serial': serial})

@register('getDeviceSwitchPortsStatuses')
def getDeviceSwitchPortsStatuses(serial: str, **kwargs):
    return MerakiClient().getDeviceSwitchPortsStatuses(**{'serial': serial, **kwargs})

@register('getDeviceSwitchPortsStatusesPackets')
def getDeviceSwitchPortsStatusesPackets(serial: str, **kwargs):
    return MerakiClient().getDeviceSwitchPortsStatusesPackets(**{'serial': serial, **kwargs})

@register('getDeviceSwitchPort')
def getDeviceSwitchPort(portId: str, serial: str):
    return MerakiClient().getDeviceSwitchPort(**{'portId': portId, 'serial': serial})

@register('getDeviceSwitchRoutingInterfaces')
def getDeviceSwitchRoutingInterfaces(serial: str):
    return MerakiClient().getDeviceSwitchRoutingInterfaces(**{'serial': serial})

@register('getDeviceSwitchRoutingInterface')
def getDeviceSwitchRoutingInterface(interfaceId: str, serial: str):
    return MerakiClient().getDeviceSwitchRoutingInterface(**{'interfaceId': interfaceId, 'serial': serial})

@register('getDeviceSwitchRoutingInterfaceDhcp')
def getDeviceSwitchRoutingInterfaceDhcp(interfaceId: str, serial: str):
    return MerakiClient().getDeviceSwitchRoutingInterfaceDhcp(**{'interfaceId': interfaceId, 'serial': serial})

@register('getDeviceSwitchRoutingStaticRoutes')
def getDeviceSwitchRoutingStaticRoutes(serial: str):
    return MerakiClient().getDeviceSwitchRoutingStaticRoutes(**{'serial': serial})

@register('getDeviceSwitchRoutingStaticRoute')
def getDeviceSwitchRoutingStaticRoute(serial: str, staticRouteId: str):
    return MerakiClient().getDeviceSwitchRoutingStaticRoute(**{'serial': serial, 'staticRouteId': staticRouteId})

@register('getDeviceSwitchWarmSpare')
def getDeviceSwitchWarmSpare(serial: str):
    return MerakiClient().getDeviceSwitchWarmSpare(**{'serial': serial})

@register('getDeviceWirelessBluetoothSettings')
def getDeviceWirelessBluetoothSettings(serial: str):
    return MerakiClient().getDeviceWirelessBluetoothSettings(**{'serial': serial})

@register('getDeviceWirelessConnectionStats')
def getDeviceWirelessConnectionStats(serial: str, **kwargs):
    return MerakiClient().getDeviceWirelessConnectionStats(**{'serial': serial, **kwargs})

@register('getDeviceWirelessElectronicShelfLabel')
def getDeviceWirelessElectronicShelfLabel(serial: str):
    return MerakiClient().getDeviceWirelessElectronicShelfLabel(**{'serial': serial})

@register('getDeviceWirelessLatencyStats')
def getDeviceWirelessLatencyStats(serial: str, **kwargs):
    return MerakiClient().getDeviceWirelessLatencyStats(**{'serial': serial, **kwargs})

@register('getDeviceWirelessRadioSettings')
def getDeviceWirelessRadioSettings(serial: str):
    return MerakiClient().getDeviceWirelessRadioSettings(**{'serial': serial})

@register('getDeviceWirelessStatus')
def getDeviceWirelessStatus(serial: str):
    return MerakiClient().getDeviceWirelessStatus(**{'serial': serial})

@register('getNetwork')
def getNetwork(networkId: str):
    return MerakiClient().getNetwork(**{'networkId': networkId})

@register('getNetworkAlertsHistory')
def getNetworkAlertsHistory(networkId: str, **kwargs):
    return MerakiClient().getNetworkAlertsHistory(**{'networkId': networkId, **kwargs})

@register('getNetworkAlertsSettings')
def getNetworkAlertsSettings(networkId: str):
    return MerakiClient().getNetworkAlertsSettings(**{'networkId': networkId})

@register('getNetworkApplianceClientSecurityEvents')
def getNetworkApplianceClientSecurityEvents(clientId: str, networkId: str, **kwargs):
    return MerakiClient().getNetworkApplianceClientSecurityEvents(**{'clientId': clientId, 'networkId': networkId, **kwargs})

@register('getNetworkApplianceConnectivityMonitoringDestinations')
def getNetworkApplianceConnectivityMonitoringDestinations(networkId: str):
    return MerakiClient().getNetworkApplianceConnectivityMonitoringDestinations(**{'networkId': networkId})

@register('getNetworkApplianceContentFiltering')
def getNetworkApplianceContentFiltering(networkId: str):
    return MerakiClient().getNetworkApplianceContentFiltering(**{'networkId': networkId})

@register('getNetworkApplianceContentFilteringCategories')
def getNetworkApplianceContentFilteringCategories(networkId: str):
    return MerakiClient().getNetworkApplianceContentFilteringCategories(**{'networkId': networkId})

@register('getNetworkApplianceFirewallCellularFirewallRules')
def getNetworkApplianceFirewallCellularFirewallRules(networkId: str):
    return MerakiClient().getNetworkApplianceFirewallCellularFirewallRules(**{'networkId': networkId})

@register('getNetworkApplianceFirewallFirewalledServices')
def getNetworkApplianceFirewallFirewalledServices(networkId: str):
    return MerakiClient().getNetworkApplianceFirewallFirewalledServices(**{'networkId': networkId})

@register('getNetworkApplianceFirewallFirewalledService')
def getNetworkApplianceFirewallFirewalledService(networkId: str, service: str):
    return MerakiClient().getNetworkApplianceFirewallFirewalledService(**{'networkId': networkId, 'service': service})

@register('getNetworkApplianceFirewallInboundCellularFirewallRules')
def getNetworkApplianceFirewallInboundCellularFirewallRules(networkId: str):
    return MerakiClient().getNetworkApplianceFirewallInboundCellularFirewallRules(**{'networkId': networkId})

@register('getNetworkApplianceFirewallInboundFirewallRules')
def getNetworkApplianceFirewallInboundFirewallRules(networkId: str):
    return MerakiClient().getNetworkApplianceFirewallInboundFirewallRules(**{'networkId': networkId})

@register('getNetworkApplianceFirewallL3FirewallRules')
def getNetworkApplianceFirewallL3FirewallRules(networkId: str):
    return MerakiClient().getNetworkApplianceFirewallL3FirewallRules(**{'networkId': networkId})

@register('getNetworkApplianceFirewallL7FirewallRules')
def getNetworkApplianceFirewallL7FirewallRules(networkId: str):
    return MerakiClient().getNetworkApplianceFirewallL7FirewallRules(**{'networkId': networkId})

@register('getNetworkApplianceFirewallL7FirewallRulesApplicationCategories')
def getNetworkApplianceFirewallL7FirewallRulesApplicationCategories(networkId: str):
    return MerakiClient().getNetworkApplianceFirewallL7FirewallRulesApplicationCategories(**{'networkId': networkId})

@register('getNetworkApplianceFirewallOneToManyNatRules')
def getNetworkApplianceFirewallOneToManyNatRules(networkId: str):
    return MerakiClient().getNetworkApplianceFirewallOneToManyNatRules(**{'networkId': networkId})

@register('getNetworkApplianceFirewallOneToOneNatRules')
def getNetworkApplianceFirewallOneToOneNatRules(networkId: str):
    return MerakiClient().getNetworkApplianceFirewallOneToOneNatRules(**{'networkId': networkId})

@register('getNetworkApplianceFirewallPortForwardingRules')
def getNetworkApplianceFirewallPortForwardingRules(networkId: str):
    return MerakiClient().getNetworkApplianceFirewallPortForwardingRules(**{'networkId': networkId})

@register('getNetworkApplianceFirewallSettings')
def getNetworkApplianceFirewallSettings(networkId: str):
    return MerakiClient().getNetworkApplianceFirewallSettings(**{'networkId': networkId})

@register('getNetworkAppliancePorts')
def getNetworkAppliancePorts(networkId: str):
    return MerakiClient().getNetworkAppliancePorts(**{'networkId': networkId})

@register('getNetworkAppliancePort')
def getNetworkAppliancePort(networkId: str, portId: str):
    return MerakiClient().getNetworkAppliancePort(**{'networkId': networkId, 'portId': portId})

@register('getNetworkAppliancePrefixesDelegatedStatics')
def getNetworkAppliancePrefixesDelegatedStatics(networkId: str):
    return MerakiClient().getNetworkAppliancePrefixesDelegatedStatics(**{'networkId': networkId})

@register('getNetworkAppliancePrefixesDelegatedStatic')
def getNetworkAppliancePrefixesDelegatedStatic(networkId: str, staticDelegatedPrefixId: str):
    return MerakiClient().getNetworkAppliancePrefixesDelegatedStatic(**{'networkId': networkId, 'staticDelegatedPrefixId': staticDelegatedPrefixId})

@register('getNetworkApplianceRfProfiles')
def getNetworkApplianceRfProfiles(networkId: str):
    return MerakiClient().getNetworkApplianceRfProfiles(**{'networkId': networkId})

@register('getNetworkApplianceRfProfile')
def getNetworkApplianceRfProfile(networkId: str, rfProfileId: str):
    return MerakiClient().getNetworkApplianceRfProfile(**{'networkId': networkId, 'rfProfileId': rfProfileId})

@register('getNetworkApplianceSecurityEvents')
def getNetworkApplianceSecurityEvents(networkId: str, **kwargs):
    return MerakiClient().getNetworkApplianceSecurityEvents(**{'networkId': networkId, **kwargs})

@register('getNetworkApplianceSecurityIntrusion')
def getNetworkApplianceSecurityIntrusion(networkId: str):
    return MerakiClient().getNetworkApplianceSecurityIntrusion(**{'networkId': networkId})

@register('getNetworkApplianceSecurityMalware')
def getNetworkApplianceSecurityMalware(networkId: str):
    return MerakiClient().getNetworkApplianceSecurityMalware(**{'networkId': networkId})

@register('getNetworkApplianceSettings')
def getNetworkApplianceSettings(networkId: str):
    return MerakiClient().getNetworkApplianceSettings(**{'networkId': networkId})

@register('getNetworkApplianceSingleLan')
def getNetworkApplianceSingleLan(networkId: str):
    return MerakiClient().getNetworkApplianceSingleLan(**{'networkId': networkId})

@register('getNetworkApplianceSsids')
def getNetworkApplianceSsids(networkId: str):
    return MerakiClient().getNetworkApplianceSsids(**{'networkId': networkId})

@register('getNetworkApplianceSsid')
def getNetworkApplianceSsid(networkId: str, number: str):
    return MerakiClient().getNetworkApplianceSsid(**{'networkId': networkId, 'number': number})

@register('getNetworkApplianceStaticRoutes')
def getNetworkApplianceStaticRoutes(networkId: str):
    return MerakiClient().getNetworkApplianceStaticRoutes(**{'networkId': networkId})

@register('getNetworkApplianceStaticRoute')
def getNetworkApplianceStaticRoute(networkId: str, staticRouteId: str):
    return MerakiClient().getNetworkApplianceStaticRoute(**{'networkId': networkId, 'staticRouteId': staticRouteId})

@register('getNetworkApplianceTrafficShaping')
def getNetworkApplianceTrafficShaping(networkId: str):
    return MerakiClient().getNetworkApplianceTrafficShaping(**{'networkId': networkId})

@register('getNetworkApplianceTrafficShapingCustomPerformanceClasses')
def getNetworkApplianceTrafficShapingCustomPerformanceClasses(networkId: str):
    return MerakiClient().getNetworkApplianceTrafficShapingCustomPerformanceClasses(**{'networkId': networkId})

@register('getNetworkApplianceTrafficShapingCustomPerformanceClass')
def getNetworkApplianceTrafficShapingCustomPerformanceClass(customPerformanceClassId: str, networkId: str):
    return MerakiClient().getNetworkApplianceTrafficShapingCustomPerformanceClass(**{'customPerformanceClassId': customPerformanceClassId, 'networkId': networkId})

@register('getNetworkApplianceTrafficShapingRules')
def getNetworkApplianceTrafficShapingRules(networkId: str):
    return MerakiClient().getNetworkApplianceTrafficShapingRules(**{'networkId': networkId})

@register('getNetworkApplianceTrafficShapingUplinkBandwidth')
def getNetworkApplianceTrafficShapingUplinkBandwidth(networkId: str):
    return MerakiClient().getNetworkApplianceTrafficShapingUplinkBandwidth(**{'networkId': networkId})

@register('getNetworkApplianceTrafficShapingUplinkSelection')
def getNetworkApplianceTrafficShapingUplinkSelection(networkId: str):
    return MerakiClient().getNetworkApplianceTrafficShapingUplinkSelection(**{'networkId': networkId})

@register('getNetworkApplianceUplinksUsageHistory')
def getNetworkApplianceUplinksUsageHistory(networkId: str, **kwargs):
    return MerakiClient().getNetworkApplianceUplinksUsageHistory(**{'networkId': networkId, **kwargs})

@register('getNetworkApplianceVlans')
def getNetworkApplianceVlans(networkId: str):
    return MerakiClient().getNetworkApplianceVlans(**{'networkId': networkId})

@register('getNetworkApplianceVlansSettings')
def getNetworkApplianceVlansSettings(networkId: str):
    return MerakiClient().getNetworkApplianceVlansSettings(**{'networkId': networkId})

@register('getNetworkApplianceVlan')
def getNetworkApplianceVlan(networkId: str, vlanId: str):
    return MerakiClient().getNetworkApplianceVlan(**{'networkId': networkId, 'vlanId': vlanId})

@register('getNetworkApplianceVpnBgp')
def getNetworkApplianceVpnBgp(networkId: str):
    return MerakiClient().getNetworkApplianceVpnBgp(**{'networkId': networkId})

@register('getNetworkApplianceVpnSiteToSiteVpn')
def getNetworkApplianceVpnSiteToSiteVpn(networkId: str):
    return MerakiClient().getNetworkApplianceVpnSiteToSiteVpn(**{'networkId': networkId})

@register('getNetworkApplianceWarmSpare')
def getNetworkApplianceWarmSpare(networkId: str):
    return MerakiClient().getNetworkApplianceWarmSpare(**{'networkId': networkId})

@register('getNetworkBluetoothClients')
def getNetworkBluetoothClients(networkId: str, **kwargs):
    return MerakiClient().getNetworkBluetoothClients(**{'networkId': networkId, **kwargs})

@register('getNetworkBluetoothClient')
def getNetworkBluetoothClient(bluetoothClientId: str, networkId: str, **kwargs):
    return MerakiClient().getNetworkBluetoothClient(**{'bluetoothClientId': bluetoothClientId, 'networkId': networkId, **kwargs})

@register('getNetworkCameraQualityRetentionProfiles')
def getNetworkCameraQualityRetentionProfiles(networkId: str):
    return MerakiClient().getNetworkCameraQualityRetentionProfiles(**{'networkId': networkId})

@register('getNetworkCameraQualityRetentionProfile')
def getNetworkCameraQualityRetentionProfile(networkId: str, qualityRetentionProfileId: str):
    return MerakiClient().getNetworkCameraQualityRetentionProfile(**{'networkId': networkId, 'qualityRetentionProfileId': qualityRetentionProfileId})

@register('getNetworkCameraSchedules')
def getNetworkCameraSchedules(networkId: str):
    return MerakiClient().getNetworkCameraSchedules(**{'networkId': networkId})

@register('getNetworkCameraWirelessProfiles')
def getNetworkCameraWirelessProfiles(networkId: str):
    return MerakiClient().getNetworkCameraWirelessProfiles(**{'networkId': networkId})

@register('getNetworkCameraWirelessProfile')
def getNetworkCameraWirelessProfile(networkId: str, wirelessProfileId: str):
    return MerakiClient().getNetworkCameraWirelessProfile(**{'networkId': networkId, 'wirelessProfileId': wirelessProfileId})

@register('getNetworkCellularGatewayConnectivityMonitoringDestinations')
def getNetworkCellularGatewayConnectivityMonitoringDestinations(networkId: str):
    return MerakiClient().getNetworkCellularGatewayConnectivityMonitoringDestinations(**{'networkId': networkId})

@register('getNetworkCellularGatewayDhcp')
def getNetworkCellularGatewayDhcp(networkId: str):
    return MerakiClient().getNetworkCellularGatewayDhcp(**{'networkId': networkId})

@register('getNetworkCellularGatewaySubnetPool')
def getNetworkCellularGatewaySubnetPool(networkId: str):
    return MerakiClient().getNetworkCellularGatewaySubnetPool(**{'networkId': networkId})

@register('getNetworkCellularGatewayUplink')
def getNetworkCellularGatewayUplink(networkId: str):
    return MerakiClient().getNetworkCellularGatewayUplink(**{'networkId': networkId})

@register('getNetworkClients')
def getNetworkClients(networkId: str, **kwargs):
    return MerakiClient().getNetworkClients(**{'networkId': networkId, **kwargs})

@register('getNetworkClientsApplicationUsage')
def getNetworkClientsApplicationUsage(clients: str, networkId: str, **kwargs):
    return MerakiClient().getNetworkClientsApplicationUsage(**{'clients': clients, 'networkId': networkId, **kwargs})

@register('getNetworkClientsBandwidthUsageHistory')
def getNetworkClientsBandwidthUsageHistory(networkId: str, **kwargs):
    return MerakiClient().getNetworkClientsBandwidthUsageHistory(**{'networkId': networkId, **kwargs})

@register('getNetworkClientsOverview')
def getNetworkClientsOverview(networkId: str, **kwargs):
    return MerakiClient().getNetworkClientsOverview(**{'networkId': networkId, **kwargs})

@register('getNetworkClientsUsageHistories')
def getNetworkClientsUsageHistories(clients: str, networkId: str, **kwargs):
    return MerakiClient().getNetworkClientsUsageHistories(**{'clients': clients, 'networkId': networkId, **kwargs})

@register('getNetworkClient')
def getNetworkClient(clientId: str, networkId: str):
    return MerakiClient().getNetworkClient(**{'clientId': clientId, 'networkId': networkId})

@register('getNetworkClientPolicy')
def getNetworkClientPolicy(clientId: str, networkId: str):
    return MerakiClient().getNetworkClientPolicy(**{'clientId': clientId, 'networkId': networkId})

@register('getNetworkClientSplashAuthorizationStatus')
def getNetworkClientSplashAuthorizationStatus(clientId: str, networkId: str):
    return MerakiClient().getNetworkClientSplashAuthorizationStatus(**{'clientId': clientId, 'networkId': networkId})

@register('getNetworkClientTrafficHistory')
def getNetworkClientTrafficHistory(clientId: str, networkId: str, **kwargs):
    return MerakiClient().getNetworkClientTrafficHistory(**{'clientId': clientId, 'networkId': networkId, **kwargs})

@register('getNetworkClientUsageHistory')
def getNetworkClientUsageHistory(clientId: str, networkId: str):
    return MerakiClient().getNetworkClientUsageHistory(**{'clientId': clientId, 'networkId': networkId})

@register('getNetworkDevices')
def getNetworkDevices(networkId: str):
    return MerakiClient().getNetworkDevices(**{'networkId': networkId})

@register('getNetworkEvents')
def getNetworkEvents(networkId: str, **kwargs):
    return MerakiClient().getNetworkEvents(**{'networkId': networkId, **kwargs})

@register('getNetworkEventsEventTypes')
def getNetworkEventsEventTypes(networkId: str):
    return MerakiClient().getNetworkEventsEventTypes(**{'networkId': networkId})

@register('getNetworkFirmwareUpgrades')
def getNetworkFirmwareUpgrades(networkId: str):
    return MerakiClient().getNetworkFirmwareUpgrades(**{'networkId': networkId})

@register('getNetworkFirmwareUpgradesStagedEvents')
def getNetworkFirmwareUpgradesStagedEvents(networkId: str):
    return MerakiClient().getNetworkFirmwareUpgradesStagedEvents(**{'networkId': networkId})

@register('getNetworkFirmwareUpgradesStagedGroups')
def getNetworkFirmwareUpgradesStagedGroups(networkId: str):
    return MerakiClient().getNetworkFirmwareUpgradesStagedGroups(**{'networkId': networkId})

@register('getNetworkFirmwareUpgradesStagedGroup')
def getNetworkFirmwareUpgradesStagedGroup(groupId: str, networkId: str):
    return MerakiClient().getNetworkFirmwareUpgradesStagedGroup(**{'groupId': groupId, 'networkId': networkId})

@register('getNetworkFirmwareUpgradesStagedStages')
def getNetworkFirmwareUpgradesStagedStages(networkId: str):
    return MerakiClient().getNetworkFirmwareUpgradesStagedStages(**{'networkId': networkId})

@register('getNetworkFloorPlans')
def getNetworkFloorPlans(networkId: str):
    return MerakiClient().getNetworkFloorPlans(**{'networkId': networkId})

@register('getNetworkFloorPlan')
def getNetworkFloorPlan(floorPlanId: str, networkId: str):
    return MerakiClient().getNetworkFloorPlan(**{'floorPlanId': floorPlanId, 'networkId': networkId})

@register('getNetworkGroupPolicies')
def getNetworkGroupPolicies(networkId: str):
    return MerakiClient().getNetworkGroupPolicies(**{'networkId': networkId})

@register('getNetworkGroupPolicy')
def getNetworkGroupPolicy(groupPolicyId: str, networkId: str):
    return MerakiClient().getNetworkGroupPolicy(**{'groupPolicyId': groupPolicyId, 'networkId': networkId})

@register('getNetworkHealthAlerts')
def getNetworkHealthAlerts(networkId: str):
    return MerakiClient().getNetworkHealthAlerts(**{'networkId': networkId})

@register('getNetworkInsightApplicationHealthByTime')
def getNetworkInsightApplicationHealthByTime(applicationId: str, networkId: str, **kwargs):
    return MerakiClient().getNetworkInsightApplicationHealthByTime(**{'applicationId': applicationId, 'networkId': networkId, **kwargs})

@register('getNetworkMerakiAuthUsers')
def getNetworkMerakiAuthUsers(networkId: str):
    return MerakiClient().getNetworkMerakiAuthUsers(**{'networkId': networkId})

@register('getNetworkMerakiAuthUser')
def getNetworkMerakiAuthUser(merakiAuthUserId: str, networkId: str):
    return MerakiClient().getNetworkMerakiAuthUser(**{'merakiAuthUserId': merakiAuthUserId, 'networkId': networkId})

@register('getNetworkMqttBrokers')
def getNetworkMqttBrokers(networkId: str):
    return MerakiClient().getNetworkMqttBrokers(**{'networkId': networkId})

@register('getNetworkMqttBroker')
def getNetworkMqttBroker(mqttBrokerId: str, networkId: str):
    return MerakiClient().getNetworkMqttBroker(**{'mqttBrokerId': mqttBrokerId, 'networkId': networkId})

@register('getNetworkNetflow')
def getNetworkNetflow(networkId: str):
    return MerakiClient().getNetworkNetflow(**{'networkId': networkId})

@register('getNetworkNetworkHealthChannelUtilization')
def getNetworkNetworkHealthChannelUtilization(networkId: str, **kwargs):
    return MerakiClient().getNetworkNetworkHealthChannelUtilization(**{'networkId': networkId, **kwargs})

@register('getNetworkPiiPiiKeys')
def getNetworkPiiPiiKeys(networkId: str, **kwargs):
    return MerakiClient().getNetworkPiiPiiKeys(**{'networkId': networkId, **kwargs})

@register('getNetworkPiiRequests')
def getNetworkPiiRequests(networkId: str):
    return MerakiClient().getNetworkPiiRequests(**{'networkId': networkId})

@register('getNetworkPiiRequest')
def getNetworkPiiRequest(networkId: str, requestId: str):
    return MerakiClient().getNetworkPiiRequest(**{'networkId': networkId, 'requestId': requestId})

@register('getNetworkPiiSmDevicesForKey')
def getNetworkPiiSmDevicesForKey(networkId: str, **kwargs):
    return MerakiClient().getNetworkPiiSmDevicesForKey(**{'networkId': networkId, **kwargs})

@register('getNetworkPiiSmOwnersForKey')
def getNetworkPiiSmOwnersForKey(networkId: str, **kwargs):
    return MerakiClient().getNetworkPiiSmOwnersForKey(**{'networkId': networkId, **kwargs})

@register('getNetworkPoliciesByClient')
def getNetworkPoliciesByClient(networkId: str, **kwargs):
    return MerakiClient().getNetworkPoliciesByClient(**{'networkId': networkId, **kwargs})

@register('getNetworkSensorAlertsCurrentOverviewByMetric')
def getNetworkSensorAlertsCurrentOverviewByMetric(networkId: str):
    return MerakiClient().getNetworkSensorAlertsCurrentOverviewByMetric(**{'networkId': networkId})

@register('getNetworkSensorAlertsOverviewByMetric')
def getNetworkSensorAlertsOverviewByMetric(networkId: str, **kwargs):
    return MerakiClient().getNetworkSensorAlertsOverviewByMetric(**{'networkId': networkId, **kwargs})

@register('getNetworkSensorAlertsProfiles')
def getNetworkSensorAlertsProfiles(networkId: str):
    return MerakiClient().getNetworkSensorAlertsProfiles(**{'networkId': networkId})

@register('getNetworkSensorAlertsProfile')
def getNetworkSensorAlertsProfile(id: str, networkId: str):
    return MerakiClient().getNetworkSensorAlertsProfile(**{'id': id, 'networkId': networkId})

@register('getNetworkSensorMqttBrokers')
def getNetworkSensorMqttBrokers(networkId: str):
    return MerakiClient().getNetworkSensorMqttBrokers(**{'networkId': networkId})

@register('getNetworkSensorMqttBroker')
def getNetworkSensorMqttBroker(mqttBrokerId: str, networkId: str):
    return MerakiClient().getNetworkSensorMqttBroker(**{'mqttBrokerId': mqttBrokerId, 'networkId': networkId})

@register('getNetworkSensorRelationships')
def getNetworkSensorRelationships(networkId: str):
    return MerakiClient().getNetworkSensorRelationships(**{'networkId': networkId})

@register('getNetworkSettings')
def getNetworkSettings(networkId: str):
    return MerakiClient().getNetworkSettings(**{'networkId': networkId})

@register('getNetworkSmBypassActivationLockAttempt')
def getNetworkSmBypassActivationLockAttempt(attemptId: str, networkId: str):
    return MerakiClient().getNetworkSmBypassActivationLockAttempt(**{'attemptId': attemptId, 'networkId': networkId})

@register('getNetworkSmDevices')
def getNetworkSmDevices(networkId: str, **kwargs):
    return MerakiClient().getNetworkSmDevices(**{'networkId': networkId, **kwargs})

@register('getNetworkSmDeviceCellularUsageHistory')
def getNetworkSmDeviceCellularUsageHistory(deviceId: str, networkId: str):
    return MerakiClient().getNetworkSmDeviceCellularUsageHistory(**{'deviceId': deviceId, 'networkId': networkId})

@register('getNetworkSmDeviceCerts')
def getNetworkSmDeviceCerts(deviceId: str, networkId: str):
    return MerakiClient().getNetworkSmDeviceCerts(**{'deviceId': deviceId, 'networkId': networkId})

@register('getNetworkSmDeviceConnectivity')
def getNetworkSmDeviceConnectivity(deviceId: str, networkId: str, **kwargs):
    return MerakiClient().getNetworkSmDeviceConnectivity(**{'deviceId': deviceId, 'networkId': networkId, **kwargs})

@register('getNetworkSmDeviceDesktopLogs')
def getNetworkSmDeviceDesktopLogs(deviceId: str, networkId: str, **kwargs):
    return MerakiClient().getNetworkSmDeviceDesktopLogs(**{'deviceId': deviceId, 'networkId': networkId, **kwargs})

@register('getNetworkSmDeviceDeviceCommandLogs')
def getNetworkSmDeviceDeviceCommandLogs(deviceId: str, networkId: str, **kwargs):
    return MerakiClient().getNetworkSmDeviceDeviceCommandLogs(**{'deviceId': deviceId, 'networkId': networkId, **kwargs})

@register('getNetworkSmDeviceDeviceProfiles')
def getNetworkSmDeviceDeviceProfiles(deviceId: str, networkId: str):
    return MerakiClient().getNetworkSmDeviceDeviceProfiles(**{'deviceId': deviceId, 'networkId': networkId})

@register('getNetworkSmDeviceNetworkAdapters')
def getNetworkSmDeviceNetworkAdapters(deviceId: str, networkId: str):
    return MerakiClient().getNetworkSmDeviceNetworkAdapters(**{'deviceId': deviceId, 'networkId': networkId})

@register('getNetworkSmDevicePerformanceHistory')
def getNetworkSmDevicePerformanceHistory(deviceId: str, networkId: str, **kwargs):
    return MerakiClient().getNetworkSmDevicePerformanceHistory(**{'deviceId': deviceId, 'networkId': networkId, **kwargs})

@register('getNetworkSmDeviceRestrictions')
def getNetworkSmDeviceRestrictions(deviceId: str, networkId: str):
    return MerakiClient().getNetworkSmDeviceRestrictions(**{'deviceId': deviceId, 'networkId': networkId})

@register('getNetworkSmDeviceSecurityCenters')
def getNetworkSmDeviceSecurityCenters(deviceId: str, networkId: str):
    return MerakiClient().getNetworkSmDeviceSecurityCenters(**{'deviceId': deviceId, 'networkId': networkId})

@register('getNetworkSmDeviceSoftwares')
def getNetworkSmDeviceSoftwares(deviceId: str, networkId: str):
    return MerakiClient().getNetworkSmDeviceSoftwares(**{'deviceId': deviceId, 'networkId': networkId})

@register('getNetworkSmDeviceWlanLists')
def getNetworkSmDeviceWlanLists(deviceId: str, networkId: str):
    return MerakiClient().getNetworkSmDeviceWlanLists(**{'deviceId': deviceId, 'networkId': networkId})

@register('getNetworkSmProfiles')
def getNetworkSmProfiles(networkId: str, **kwargs):
    return MerakiClient().getNetworkSmProfiles(**{'networkId': networkId, **kwargs})

@register('getNetworkSmTargetGroups')
def getNetworkSmTargetGroups(networkId: str, **kwargs):
    return MerakiClient().getNetworkSmTargetGroups(**{'networkId': networkId, **kwargs})

@register('getNetworkSmTargetGroup')
def getNetworkSmTargetGroup(networkId: str, targetGroupId: str, **kwargs):
    return MerakiClient().getNetworkSmTargetGroup(**{'networkId': networkId, 'targetGroupId': targetGroupId, **kwargs})

@register('getNetworkSmTrustedAccessConfigs')
def getNetworkSmTrustedAccessConfigs(networkId: str, **kwargs):
    return MerakiClient().getNetworkSmTrustedAccessConfigs(**{'networkId': networkId, **kwargs})

@register('getNetworkSmUserAccessDevices')
def getNetworkSmUserAccessDevices(networkId: str, **kwargs):
    return MerakiClient().getNetworkSmUserAccessDevices(**{'networkId': networkId, **kwargs})

@register('getNetworkSmUsers')
def getNetworkSmUsers(networkId: str, **kwargs):
    return MerakiClient().getNetworkSmUsers(**{'networkId': networkId, **kwargs})

@register('getNetworkSmUserDeviceProfiles')
def getNetworkSmUserDeviceProfiles(networkId: str, userId: str):
    return MerakiClient().getNetworkSmUserDeviceProfiles(**{'networkId': networkId, 'userId': userId})

@register('getNetworkSmUserSoftwares')
def getNetworkSmUserSoftwares(networkId: str, userId: str):
    return MerakiClient().getNetworkSmUserSoftwares(**{'networkId': networkId, 'userId': userId})

@register('getNetworkSnmp')
def getNetworkSnmp(networkId: str):
    return MerakiClient().getNetworkSnmp(**{'networkId': networkId})

@register('getNetworkSplashLoginAttempts')
def getNetworkSplashLoginAttempts(networkId: str, **kwargs):
    return MerakiClient().getNetworkSplashLoginAttempts(**{'networkId': networkId, **kwargs})

@register('getNetworkSwitchAccessControlLists')
def getNetworkSwitchAccessControlLists(networkId: str):
    return MerakiClient().getNetworkSwitchAccessControlLists(**{'networkId': networkId})

@register('getNetworkSwitchAccessPolicies')
def getNetworkSwitchAccessPolicies(networkId: str):
    return MerakiClient().getNetworkSwitchAccessPolicies(**{'networkId': networkId})

@register('getNetworkSwitchAccessPolicy')
def getNetworkSwitchAccessPolicy(accessPolicyNumber: str, networkId: str):
    return MerakiClient().getNetworkSwitchAccessPolicy(**{'accessPolicyNumber': accessPolicyNumber, 'networkId': networkId})

@register('getNetworkSwitchAlternateManagementInterface')
def getNetworkSwitchAlternateManagementInterface(networkId: str):
    return MerakiClient().getNetworkSwitchAlternateManagementInterface(**{'networkId': networkId})

@register('getNetworkSwitchDhcpV4ServersSeen')
def getNetworkSwitchDhcpV4ServersSeen(networkId: str, **kwargs):
    return MerakiClient().getNetworkSwitchDhcpV4ServersSeen(**{'networkId': networkId, **kwargs})

@register('getNetworkSwitchDhcpServerPolicy')
def getNetworkSwitchDhcpServerPolicy(networkId: str):
    return MerakiClient().getNetworkSwitchDhcpServerPolicy(**{'networkId': networkId})

@register('getNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers')
def getNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers(networkId: str, **kwargs):
    return MerakiClient().getNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers(**{'networkId': networkId, **kwargs})

@register('getNetworkSwitchDhcpServerPolicyArpInspectionWarningsByDevice')
def getNetworkSwitchDhcpServerPolicyArpInspectionWarningsByDevice(networkId: str, **kwargs):
    return MerakiClient().getNetworkSwitchDhcpServerPolicyArpInspectionWarningsByDevice(**{'networkId': networkId, **kwargs})

@register('getNetworkSwitchDscpToCosMappings')
def getNetworkSwitchDscpToCosMappings(networkId: str):
    return MerakiClient().getNetworkSwitchDscpToCosMappings(**{'networkId': networkId})

@register('getNetworkSwitchLinkAggregations')
def getNetworkSwitchLinkAggregations(networkId: str):
    return MerakiClient().getNetworkSwitchLinkAggregations(**{'networkId': networkId})

@register('getNetworkSwitchMtu')
def getNetworkSwitchMtu(networkId: str):
    return MerakiClient().getNetworkSwitchMtu(**{'networkId': networkId})

@register('getNetworkSwitchPortSchedules')
def getNetworkSwitchPortSchedules(networkId: str):
    return MerakiClient().getNetworkSwitchPortSchedules(**{'networkId': networkId})

@register('getNetworkSwitchQosRules')
def getNetworkSwitchQosRules(networkId: str):
    return MerakiClient().getNetworkSwitchQosRules(**{'networkId': networkId})

@register('getNetworkSwitchQosRulesOrder')
def getNetworkSwitchQosRulesOrder(networkId: str):
    return MerakiClient().getNetworkSwitchQosRulesOrder(**{'networkId': networkId})

@register('getNetworkSwitchQosRule')
def getNetworkSwitchQosRule(networkId: str, qosRuleId: str):
    return MerakiClient().getNetworkSwitchQosRule(**{'networkId': networkId, 'qosRuleId': qosRuleId})

@register('getNetworkSwitchRoutingMulticast')
def getNetworkSwitchRoutingMulticast(networkId: str):
    return MerakiClient().getNetworkSwitchRoutingMulticast(**{'networkId': networkId})

@register('getNetworkSwitchRoutingMulticastRendezvousPoints')
def getNetworkSwitchRoutingMulticastRendezvousPoints(networkId: str):
    return MerakiClient().getNetworkSwitchRoutingMulticastRendezvousPoints(**{'networkId': networkId})

@register('getNetworkSwitchRoutingMulticastRendezvousPoint')
def getNetworkSwitchRoutingMulticastRendezvousPoint(networkId: str, rendezvousPointId: str):
    return MerakiClient().getNetworkSwitchRoutingMulticastRendezvousPoint(**{'networkId': networkId, 'rendezvousPointId': rendezvousPointId})

@register('getNetworkSwitchRoutingOspf')
def getNetworkSwitchRoutingOspf(networkId: str):
    return MerakiClient().getNetworkSwitchRoutingOspf(**{'networkId': networkId})

@register('getNetworkSwitchSettings')
def getNetworkSwitchSettings(networkId: str):
    return MerakiClient().getNetworkSwitchSettings(**{'networkId': networkId})

@register('getNetworkSwitchStacks')
def getNetworkSwitchStacks(networkId: str):
    return MerakiClient().getNetworkSwitchStacks(**{'networkId': networkId})

@register('getNetworkSwitchStack')
def getNetworkSwitchStack(networkId: str, switchStackId: str):
    return MerakiClient().getNetworkSwitchStack(**{'networkId': networkId, 'switchStackId': switchStackId})

@register('getNetworkSwitchStackRoutingInterfaces')
def getNetworkSwitchStackRoutingInterfaces(networkId: str, switchStackId: str):
    return MerakiClient().getNetworkSwitchStackRoutingInterfaces(**{'networkId': networkId, 'switchStackId': switchStackId})

@register('getNetworkSwitchStackRoutingInterface')
def getNetworkSwitchStackRoutingInterface(interfaceId: str, networkId: str, switchStackId: str):
    return MerakiClient().getNetworkSwitchStackRoutingInterface(**{'interfaceId': interfaceId, 'networkId': networkId, 'switchStackId': switchStackId})

@register('getNetworkSwitchStackRoutingInterfaceDhcp')
def getNetworkSwitchStackRoutingInterfaceDhcp(interfaceId: str, networkId: str, switchStackId: str):
    return MerakiClient().getNetworkSwitchStackRoutingInterfaceDhcp(**{'interfaceId': interfaceId, 'networkId': networkId, 'switchStackId': switchStackId})

@register('getNetworkSwitchStackRoutingStaticRoutes')
def getNetworkSwitchStackRoutingStaticRoutes(networkId: str, switchStackId: str):
    return MerakiClient().getNetworkSwitchStackRoutingStaticRoutes(**{'networkId': networkId, 'switchStackId': switchStackId})

@register('getNetworkSwitchStackRoutingStaticRoute')
def getNetworkSwitchStackRoutingStaticRoute(networkId: str, staticRouteId: str, switchStackId: str):
    return MerakiClient().getNetworkSwitchStackRoutingStaticRoute(**{'networkId': networkId, 'staticRouteId': staticRouteId, 'switchStackId': switchStackId})

@register('getNetworkSwitchStormControl')
def getNetworkSwitchStormControl(networkId: str):
    return MerakiClient().getNetworkSwitchStormControl(**{'networkId': networkId})

@register('getNetworkSwitchStp')
def getNetworkSwitchStp(networkId: str):
    return MerakiClient().getNetworkSwitchStp(**{'networkId': networkId})

@register('getNetworkSyslogServers')
def getNetworkSyslogServers(networkId: str):
    return MerakiClient().getNetworkSyslogServers(**{'networkId': networkId})

@register('getNetworkTopologyLinkLayer')
def getNetworkTopologyLinkLayer(networkId: str):
    return MerakiClient().getNetworkTopologyLinkLayer(**{'networkId': networkId})

@register('getNetworkTraffic')
def getNetworkTraffic(networkId: str, **kwargs):
    return MerakiClient().getNetworkTraffic(**{'networkId': networkId, **kwargs})

@register('getNetworkTrafficAnalysis')
def getNetworkTrafficAnalysis(networkId: str):
    return MerakiClient().getNetworkTrafficAnalysis(**{'networkId': networkId})

@register('getNetworkTrafficShapingApplicationCategories')
def getNetworkTrafficShapingApplicationCategories(networkId: str):
    return MerakiClient().getNetworkTrafficShapingApplicationCategories(**{'networkId': networkId})

@register('getNetworkTrafficShapingDscpTaggingOptions')
def getNetworkTrafficShapingDscpTaggingOptions(networkId: str):
    return MerakiClient().getNetworkTrafficShapingDscpTaggingOptions(**{'networkId': networkId})

@register('getNetworkVlanProfiles')
def getNetworkVlanProfiles(networkId: str):
    return MerakiClient().getNetworkVlanProfiles(**{'networkId': networkId})

@register('getNetworkVlanProfilesAssignmentsByDevice')
def getNetworkVlanProfilesAssignmentsByDevice(networkId: str, **kwargs):
    return MerakiClient().getNetworkVlanProfilesAssignmentsByDevice(**{'networkId': networkId, **kwargs})

@register('getNetworkVlanProfile')
def getNetworkVlanProfile(iname: str, networkId: str):
    return MerakiClient().getNetworkVlanProfile(**{'iname': iname, 'networkId': networkId})

@register('getNetworkWebhooksHttpServers')
def getNetworkWebhooksHttpServers(networkId: str):
    return MerakiClient().getNetworkWebhooksHttpServers(**{'networkId': networkId})

@register('getNetworkWebhooksHttpServer')
def getNetworkWebhooksHttpServer(httpServerId: str, networkId: str):
    return MerakiClient().getNetworkWebhooksHttpServer(**{'httpServerId': httpServerId, 'networkId': networkId})

@register('getNetworkWebhooksPayloadTemplates')
def getNetworkWebhooksPayloadTemplates(networkId: str):
    return MerakiClient().getNetworkWebhooksPayloadTemplates(**{'networkId': networkId})

@register('getNetworkWebhooksPayloadTemplate')
def getNetworkWebhooksPayloadTemplate(networkId: str, payloadTemplateId: str):
    return MerakiClient().getNetworkWebhooksPayloadTemplate(**{'networkId': networkId, 'payloadTemplateId': payloadTemplateId})

@register('getNetworkWebhooksWebhookTest')
def getNetworkWebhooksWebhookTest(networkId: str, webhookTestId: str):
    return MerakiClient().getNetworkWebhooksWebhookTest(**{'networkId': networkId, 'webhookTestId': webhookTestId})

@register('getNetworkWirelessAirMarshal')
def getNetworkWirelessAirMarshal(networkId: str, **kwargs):
    return MerakiClient().getNetworkWirelessAirMarshal(**{'networkId': networkId, **kwargs})

@register('getNetworkWirelessAlternateManagementInterface')
def getNetworkWirelessAlternateManagementInterface(networkId: str):
    return MerakiClient().getNetworkWirelessAlternateManagementInterface(**{'networkId': networkId})

@register('getNetworkWirelessBilling')
def getNetworkWirelessBilling(networkId: str):
    return MerakiClient().getNetworkWirelessBilling(**{'networkId': networkId})

@register('getNetworkWirelessBluetoothSettings')
def getNetworkWirelessBluetoothSettings(networkId: str):
    return MerakiClient().getNetworkWirelessBluetoothSettings(**{'networkId': networkId})

@register('getNetworkWirelessChannelUtilizationHistory')
def getNetworkWirelessChannelUtilizationHistory(networkId: str, **kwargs):
    return MerakiClient().getNetworkWirelessChannelUtilizationHistory(**{'networkId': networkId, **kwargs})

@register('getNetworkWirelessClientCountHistory')
def getNetworkWirelessClientCountHistory(networkId: str, **kwargs):
    return MerakiClient().getNetworkWirelessClientCountHistory(**{'networkId': networkId, **kwargs})

@register('getNetworkWirelessClientsConnectionStats')
def getNetworkWirelessClientsConnectionStats(networkId: str, **kwargs):
    return MerakiClient().getNetworkWirelessClientsConnectionStats(**{'networkId': networkId, **kwargs})

@register('getNetworkWirelessClientsLatencyStats')
def getNetworkWirelessClientsLatencyStats(networkId: str, **kwargs):
    return MerakiClient().getNetworkWirelessClientsLatencyStats(**{'networkId': networkId, **kwargs})

@register('getNetworkWirelessClientConnectionStats')
def getNetworkWirelessClientConnectionStats(clientId: str, networkId: str, **kwargs):
    return MerakiClient().getNetworkWirelessClientConnectionStats(**{'clientId': clientId, 'networkId': networkId, **kwargs})

@register('getNetworkWirelessClientConnectivityEvents')
def getNetworkWirelessClientConnectivityEvents(clientId: str, networkId: str, **kwargs):
    return MerakiClient().getNetworkWirelessClientConnectivityEvents(**{'clientId': clientId, 'networkId': networkId, **kwargs})

@register('getNetworkWirelessClientLatencyHistory')
def getNetworkWirelessClientLatencyHistory(clientId: str, networkId: str, **kwargs):
    return MerakiClient().getNetworkWirelessClientLatencyHistory(**{'clientId': clientId, 'networkId': networkId, **kwargs})

@register('getNetworkWirelessClientLatencyStats')
def getNetworkWirelessClientLatencyStats(clientId: str, networkId: str, **kwargs):
    return MerakiClient().getNetworkWirelessClientLatencyStats(**{'clientId': clientId, 'networkId': networkId, **kwargs})

@register('getNetworkWirelessConnectionStats')
def getNetworkWirelessConnectionStats(networkId: str, **kwargs):
    return MerakiClient().getNetworkWirelessConnectionStats(**{'networkId': networkId, **kwargs})

@register('getNetworkWirelessDataRateHistory')
def getNetworkWirelessDataRateHistory(networkId: str, **kwargs):
    return MerakiClient().getNetworkWirelessDataRateHistory(**{'networkId': networkId, **kwargs})

@register('getNetworkWirelessDevicesConnectionStats')
def getNetworkWirelessDevicesConnectionStats(networkId: str, **kwargs):
    return MerakiClient().getNetworkWirelessDevicesConnectionStats(**{'networkId': networkId, **kwargs})

@register('getNetworkWirelessDevicesLatencyStats')
def getNetworkWirelessDevicesLatencyStats(networkId: str, **kwargs):
    return MerakiClient().getNetworkWirelessDevicesLatencyStats(**{'networkId': networkId, **kwargs})

@register('getNetworkWirelessElectronicShelfLabel')
def getNetworkWirelessElectronicShelfLabel(networkId: str):
    return MerakiClient().getNetworkWirelessElectronicShelfLabel(**{'networkId': networkId})

@register('getNetworkWirelessElectronicShelfLabelConfiguredDevices')
def getNetworkWirelessElectronicShelfLabelConfiguredDevices(networkId: str):
    return MerakiClient().getNetworkWirelessElectronicShelfLabelConfiguredDevices(**{'networkId': networkId})

@register('getNetworkWirelessEthernetPortsProfiles')
def getNetworkWirelessEthernetPortsProfiles(networkId: str):
    return MerakiClient().getNetworkWirelessEthernetPortsProfiles(**{'networkId': networkId})

@register('getNetworkWirelessEthernetPortsProfile')
def getNetworkWirelessEthernetPortsProfile(networkId: str, profileId: str):
    return MerakiClient().getNetworkWirelessEthernetPortsProfile(**{'networkId': networkId, 'profileId': profileId})

@register('getNetworkWirelessFailedConnections')
def getNetworkWirelessFailedConnections(networkId: str, **kwargs):
    return MerakiClient().getNetworkWirelessFailedConnections(**{'networkId': networkId, **kwargs})

@register('getNetworkWirelessLatencyHistory')
def getNetworkWirelessLatencyHistory(networkId: str, **kwargs):
    return MerakiClient().getNetworkWirelessLatencyHistory(**{'networkId': networkId, **kwargs})

@register('getNetworkWirelessLatencyStats')
def getNetworkWirelessLatencyStats(networkId: str, **kwargs):
    return MerakiClient().getNetworkWirelessLatencyStats(**{'networkId': networkId, **kwargs})

@register('getNetworkWirelessMeshStatuses')
def getNetworkWirelessMeshStatuses(networkId: str, **kwargs):
    return MerakiClient().getNetworkWirelessMeshStatuses(**{'networkId': networkId, **kwargs})

@register('getNetworkWirelessRfProfiles')
def getNetworkWirelessRfProfiles(networkId: str, **kwargs):
    return MerakiClient().getNetworkWirelessRfProfiles(**{'networkId': networkId, **kwargs})

@register('getNetworkWirelessRfProfile')
def getNetworkWirelessRfProfile(networkId: str, rfProfileId: str):
    return MerakiClient().getNetworkWirelessRfProfile(**{'networkId': networkId, 'rfProfileId': rfProfileId})

@register('getNetworkWirelessSettings')
def getNetworkWirelessSettings(networkId: str):
    return MerakiClient().getNetworkWirelessSettings(**{'networkId': networkId})

@register('getNetworkWirelessSignalQualityHistory')
def getNetworkWirelessSignalQualityHistory(networkId: str, **kwargs):
    return MerakiClient().getNetworkWirelessSignalQualityHistory(**{'networkId': networkId, **kwargs})

@register('getNetworkWirelessSsids')
def getNetworkWirelessSsids(networkId: str):
    return MerakiClient().getNetworkWirelessSsids(**{'networkId': networkId})

@register('getNetworkWirelessSsid')
def getNetworkWirelessSsid(networkId: str, number: str):
    return MerakiClient().getNetworkWirelessSsid(**{'networkId': networkId, 'number': number})

@register('getNetworkWirelessSsidBonjourForwarding')
def getNetworkWirelessSsidBonjourForwarding(networkId: str, number: str):
    return MerakiClient().getNetworkWirelessSsidBonjourForwarding(**{'networkId': networkId, 'number': number})

@register('getNetworkWirelessSsidDeviceTypeGroupPolicies')
def getNetworkWirelessSsidDeviceTypeGroupPolicies(networkId: str, number: str):
    return MerakiClient().getNetworkWirelessSsidDeviceTypeGroupPolicies(**{'networkId': networkId, 'number': number})

@register('getNetworkWirelessSsidEapOverride')
def getNetworkWirelessSsidEapOverride(networkId: str, number: str):
    return MerakiClient().getNetworkWirelessSsidEapOverride(**{'networkId': networkId, 'number': number})

@register('getNetworkWirelessSsidFirewallL3FirewallRules')
def getNetworkWirelessSsidFirewallL3FirewallRules(networkId: str, number: str):
    return MerakiClient().getNetworkWirelessSsidFirewallL3FirewallRules(**{'networkId': networkId, 'number': number})

@register('getNetworkWirelessSsidFirewallL7FirewallRules')
def getNetworkWirelessSsidFirewallL7FirewallRules(networkId: str, number: str):
    return MerakiClient().getNetworkWirelessSsidFirewallL7FirewallRules(**{'networkId': networkId, 'number': number})

@register('getNetworkWirelessSsidHotspot20')
def getNetworkWirelessSsidHotspot20(networkId: str, number: str):
    return MerakiClient().getNetworkWirelessSsidHotspot20(**{'networkId': networkId, 'number': number})

@register('getNetworkWirelessSsidIdentityPsks')
def getNetworkWirelessSsidIdentityPsks(networkId: str, number: str):
    return MerakiClient().getNetworkWirelessSsidIdentityPsks(**{'networkId': networkId, 'number': number})

@register('getNetworkWirelessSsidIdentityPsk')
def getNetworkWirelessSsidIdentityPsk(identityPskId: str, networkId: str, number: str):
    return MerakiClient().getNetworkWirelessSsidIdentityPsk(**{'identityPskId': identityPskId, 'networkId': networkId, 'number': number})

@register('getNetworkWirelessSsidSchedules')
def getNetworkWirelessSsidSchedules(networkId: str, number: str):
    return MerakiClient().getNetworkWirelessSsidSchedules(**{'networkId': networkId, 'number': number})

@register('getNetworkWirelessSsidSplashSettings')
def getNetworkWirelessSsidSplashSettings(networkId: str, number: str):
    return MerakiClient().getNetworkWirelessSsidSplashSettings(**{'networkId': networkId, 'number': number})

@register('getNetworkWirelessSsidTrafficShapingRules')
def getNetworkWirelessSsidTrafficShapingRules(networkId: str, number: str):
    return MerakiClient().getNetworkWirelessSsidTrafficShapingRules(**{'networkId': networkId, 'number': number})

@register('getNetworkWirelessSsidVpn')
def getNetworkWirelessSsidVpn(networkId: str, number: str):
    return MerakiClient().getNetworkWirelessSsidVpn(**{'networkId': networkId, 'number': number})

@register('getNetworkWirelessUsageHistory')
def getNetworkWirelessUsageHistory(networkId: str, **kwargs):
    return MerakiClient().getNetworkWirelessUsageHistory(**{'networkId': networkId, **kwargs})

@register('getOrganizations')
def getOrganizations(**kwargs):
    return MerakiClient().getOrganizations(**{**kwargs})

@register('getOrganization')
def getOrganization(organizationId: str):
    return MerakiClient().getOrganization(**{'organizationId': organizationId})

@register('getOrganizationActionBatches')
def getOrganizationActionBatches(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationActionBatches(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationActionBatch')
def getOrganizationActionBatch(actionBatchId: str, organizationId: str):
    return MerakiClient().getOrganizationActionBatch(**{'actionBatchId': actionBatchId, 'organizationId': organizationId})

@register('getOrganizationAdaptivePolicyAcls')
def getOrganizationAdaptivePolicyAcls(organizationId: str):
    return MerakiClient().getOrganizationAdaptivePolicyAcls(**{'organizationId': organizationId})

@register('getOrganizationAdaptivePolicyAcl')
def getOrganizationAdaptivePolicyAcl(aclId: str, organizationId: str):
    return MerakiClient().getOrganizationAdaptivePolicyAcl(**{'aclId': aclId, 'organizationId': organizationId})

@register('getOrganizationAdaptivePolicyGroups')
def getOrganizationAdaptivePolicyGroups(organizationId: str):
    return MerakiClient().getOrganizationAdaptivePolicyGroups(**{'organizationId': organizationId})

@register('getOrganizationAdaptivePolicyGroup')
def getOrganizationAdaptivePolicyGroup(id: str, organizationId: str):
    return MerakiClient().getOrganizationAdaptivePolicyGroup(**{'id': id, 'organizationId': organizationId})

@register('getOrganizationAdaptivePolicyOverview')
def getOrganizationAdaptivePolicyOverview(organizationId: str):
    return MerakiClient().getOrganizationAdaptivePolicyOverview(**{'organizationId': organizationId})

@register('getOrganizationAdaptivePolicyPolicies')
def getOrganizationAdaptivePolicyPolicies(organizationId: str):
    return MerakiClient().getOrganizationAdaptivePolicyPolicies(**{'organizationId': organizationId})

@register('getOrganizationAdaptivePolicyPolicy')
def getOrganizationAdaptivePolicyPolicy(id: str, organizationId: str):
    return MerakiClient().getOrganizationAdaptivePolicyPolicy(**{'id': id, 'organizationId': organizationId})

@register('getOrganizationAdaptivePolicySettings')
def getOrganizationAdaptivePolicySettings(organizationId: str):
    return MerakiClient().getOrganizationAdaptivePolicySettings(**{'organizationId': organizationId})

@register('getOrganizationAdmins')
def getOrganizationAdmins(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationAdmins(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationAlertsProfiles')
def getOrganizationAlertsProfiles(organizationId: str):
    return MerakiClient().getOrganizationAlertsProfiles(**{'organizationId': organizationId})

@register('getOrganizationApiRequests')
def getOrganizationApiRequests(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationApiRequests(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationApiRequestsOverview')
def getOrganizationApiRequestsOverview(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationApiRequestsOverview(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationApiRequestsOverviewResponseCodesByInterval')
def getOrganizationApiRequestsOverviewResponseCodesByInterval(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationApiRequestsOverviewResponseCodesByInterval(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationApplianceSecurityEvents')
def getOrganizationApplianceSecurityEvents(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationApplianceSecurityEvents(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationApplianceSecurityIntrusion')
def getOrganizationApplianceSecurityIntrusion(organizationId: str):
    return MerakiClient().getOrganizationApplianceSecurityIntrusion(**{'organizationId': organizationId})

@register('getOrganizationApplianceTrafficShapingVpnExclusionsByNetwork')
def getOrganizationApplianceTrafficShapingVpnExclusionsByNetwork(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationApplianceTrafficShapingVpnExclusionsByNetwork(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationApplianceUplinkStatuses')
def getOrganizationApplianceUplinkStatuses(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationApplianceUplinkStatuses(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationApplianceUplinksStatusesOverview')
def getOrganizationApplianceUplinksStatusesOverview(organizationId: str):
    return MerakiClient().getOrganizationApplianceUplinksStatusesOverview(**{'organizationId': organizationId})

@register('getOrganizationApplianceUplinksUsageByNetwork')
def getOrganizationApplianceUplinksUsageByNetwork(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationApplianceUplinksUsageByNetwork(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationApplianceVpnStats')
def getOrganizationApplianceVpnStats(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationApplianceVpnStats(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationApplianceVpnStatuses')
def getOrganizationApplianceVpnStatuses(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationApplianceVpnStatuses(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationApplianceVpnThirdPartyVPNPeers')
def getOrganizationApplianceVpnThirdPartyVPNPeers(organizationId: str):
    return MerakiClient().getOrganizationApplianceVpnThirdPartyVPNPeers(**{'organizationId': organizationId})

@register('getOrganizationApplianceVpnVpnFirewallRules')
def getOrganizationApplianceVpnVpnFirewallRules(organizationId: str):
    return MerakiClient().getOrganizationApplianceVpnVpnFirewallRules(**{'organizationId': organizationId})

@register('getOrganizationAssuranceAlerts')
def getOrganizationAssuranceAlerts(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationAssuranceAlerts(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationAssuranceAlertsOverview')
def getOrganizationAssuranceAlertsOverview(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationAssuranceAlertsOverview(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationAssuranceAlertsOverviewByNetwork')
def getOrganizationAssuranceAlertsOverviewByNetwork(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationAssuranceAlertsOverviewByNetwork(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationAssuranceAlertsOverviewByType')
def getOrganizationAssuranceAlertsOverviewByType(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationAssuranceAlertsOverviewByType(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationAssuranceAlertsOverviewHistorical')
def getOrganizationAssuranceAlertsOverviewHistorical(organizationId: str, segmentDuration: int, tsStart: str, **kwargs):
    return MerakiClient().getOrganizationAssuranceAlertsOverviewHistorical(**{'organizationId': organizationId, 'segmentDuration': segmentDuration, 'tsStart': tsStart, **kwargs})

@register('getOrganizationAssuranceAlert')
def getOrganizationAssuranceAlert(id: str, organizationId: str):
    return MerakiClient().getOrganizationAssuranceAlert(**{'id': id, 'organizationId': organizationId})

@register('getOrganizationBrandingPolicies')
def getOrganizationBrandingPolicies(organizationId: str):
    return MerakiClient().getOrganizationBrandingPolicies(**{'organizationId': organizationId})

@register('getOrganizationBrandingPoliciesPriorities')
def getOrganizationBrandingPoliciesPriorities(organizationId: str):
    return MerakiClient().getOrganizationBrandingPoliciesPriorities(**{'organizationId': organizationId})

@register('getOrganizationBrandingPolicy')
def getOrganizationBrandingPolicy(brandingPolicyId: str, organizationId: str):
    return MerakiClient().getOrganizationBrandingPolicy(**{'brandingPolicyId': brandingPolicyId, 'organizationId': organizationId})

@register('getOrganizationCameraBoundariesAreasByDevice')
def getOrganizationCameraBoundariesAreasByDevice(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationCameraBoundariesAreasByDevice(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationCameraBoundariesLinesByDevice')
def getOrganizationCameraBoundariesLinesByDevice(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationCameraBoundariesLinesByDevice(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationCameraCustomAnalyticsArtifacts')
def getOrganizationCameraCustomAnalyticsArtifacts(organizationId: str):
    return MerakiClient().getOrganizationCameraCustomAnalyticsArtifacts(**{'organizationId': organizationId})

@register('getOrganizationCameraCustomAnalyticsArtifact')
def getOrganizationCameraCustomAnalyticsArtifact(artifactId: str, organizationId: str):
    return MerakiClient().getOrganizationCameraCustomAnalyticsArtifact(**{'artifactId': artifactId, 'organizationId': organizationId})

@register('getOrganizationCameraDetectionsHistoryByBoundaryByInterval')
def getOrganizationCameraDetectionsHistoryByBoundaryByInterval(boundaryIds: list, organizationId: str, ranges: list, **kwargs):
    return MerakiClient().getOrganizationCameraDetectionsHistoryByBoundaryByInterval(**{'boundaryIds': boundaryIds, 'organizationId': organizationId, 'ranges': ranges, **kwargs})

@register('getOrganizationCameraOnboardingStatuses')
def getOrganizationCameraOnboardingStatuses(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationCameraOnboardingStatuses(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationCameraPermissions')
def getOrganizationCameraPermissions(organizationId: str):
    return MerakiClient().getOrganizationCameraPermissions(**{'organizationId': organizationId})

@register('getOrganizationCameraPermission')
def getOrganizationCameraPermission(organizationId: str, permissionScopeId: str):
    return MerakiClient().getOrganizationCameraPermission(**{'organizationId': organizationId, 'permissionScopeId': permissionScopeId})

@register('getOrganizationCameraRoles')
def getOrganizationCameraRoles(organizationId: str):
    return MerakiClient().getOrganizationCameraRoles(**{'organizationId': organizationId})

@register('getOrganizationCameraRole')
def getOrganizationCameraRole(organizationId: str, roleId: str):
    return MerakiClient().getOrganizationCameraRole(**{'organizationId': organizationId, 'roleId': roleId})

@register('getOrganizationCellularGatewayEsimsInventory')
def getOrganizationCellularGatewayEsimsInventory(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationCellularGatewayEsimsInventory(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationCellularGatewayEsimsServiceProviders')
def getOrganizationCellularGatewayEsimsServiceProviders(organizationId: str):
    return MerakiClient().getOrganizationCellularGatewayEsimsServiceProviders(**{'organizationId': organizationId})

@register('getOrganizationCellularGatewayEsimsServiceProvidersAccounts')
def getOrganizationCellularGatewayEsimsServiceProvidersAccounts(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationCellularGatewayEsimsServiceProvidersAccounts(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationCellularGatewayEsimsServiceProvidersAccountsCommu')
def getOrganizationCellularGatewayEsimsServiceProvidersAccountsCommu(accountIds: list, organizationId: str):
    return MerakiClient().getOrganizationCellularGatewayEsimsServiceProvidersAccountsCommu(**{'accountIds': accountIds, 'organizationId': organizationId})

@register('getOrganizationCellularGatewayEsimsServiceProvidersAccountsRateP')
def getOrganizationCellularGatewayEsimsServiceProvidersAccountsRateP(accountIds: list, organizationId: str):
    return MerakiClient().getOrganizationCellularGatewayEsimsServiceProvidersAccountsRateP(**{'accountIds': accountIds, 'organizationId': organizationId})

@register('getOrganizationCellularGatewayUplinkStatuses')
def getOrganizationCellularGatewayUplinkStatuses(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationCellularGatewayUplinkStatuses(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationClientsBandwidthUsageHistory')
def getOrganizationClientsBandwidthUsageHistory(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationClientsBandwidthUsageHistory(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationClientsOverview')
def getOrganizationClientsOverview(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationClientsOverview(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationClientsSearch')
def getOrganizationClientsSearch(mac: str, organizationId: str, **kwargs):
    return MerakiClient().getOrganizationClientsSearch(**{'mac': mac, 'organizationId': organizationId, **kwargs})

@register('getOrganizationConfigTemplates')
def getOrganizationConfigTemplates(organizationId: str):
    return MerakiClient().getOrganizationConfigTemplates(**{'organizationId': organizationId})

@register('getOrganizationConfigTemplate')
def getOrganizationConfigTemplate(configTemplateId: str, organizationId: str):
    return MerakiClient().getOrganizationConfigTemplate(**{'configTemplateId': configTemplateId, 'organizationId': organizationId})

@register('getOrganizationConfigTemplateSwitchProfiles')
def getOrganizationConfigTemplateSwitchProfiles(configTemplateId: str, organizationId: str):
    return MerakiClient().getOrganizationConfigTemplateSwitchProfiles(**{'configTemplateId': configTemplateId, 'organizationId': organizationId})

@register('getOrganizationConfigTemplateSwitchProfilePorts')
def getOrganizationConfigTemplateSwitchProfilePorts(configTemplateId: str, organizationId: str, profileId: str):
    return MerakiClient().getOrganizationConfigTemplateSwitchProfilePorts(**{'configTemplateId': configTemplateId, 'organizationId': organizationId, 'profileId': profileId})

@register('getOrganizationConfigTemplateSwitchProfilePort')
def getOrganizationConfigTemplateSwitchProfilePort(configTemplateId: str, organizationId: str, portId: str, profileId: str):
    return MerakiClient().getOrganizationConfigTemplateSwitchProfilePort(**{'configTemplateId': configTemplateId, 'organizationId': organizationId, 'portId': portId, 'profileId': profileId})

@register('getOrganizationConfigurationChanges')
def getOrganizationConfigurationChanges(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationConfigurationChanges(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationDevices')
def getOrganizationDevices(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationDevices(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationDevicesAvailabilities')
def getOrganizationDevicesAvailabilities(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationDevicesAvailabilities(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationDevicesAvailabilitiesChangeHistory')
def getOrganizationDevicesAvailabilitiesChangeHistory(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationDevicesAvailabilitiesChangeHistory(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationDevicesOverviewByModel')
def getOrganizationDevicesOverviewByModel(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationDevicesOverviewByModel(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationDevicesPowerModulesStatusesByDevice')
def getOrganizationDevicesPowerModulesStatusesByDevice(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationDevicesPowerModulesStatusesByDevice(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationDevicesProvisioningStatuses')
def getOrganizationDevicesProvisioningStatuses(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationDevicesProvisioningStatuses(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationDevicesStatuses')
def getOrganizationDevicesStatuses(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationDevicesStatuses(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationDevicesStatusesOverview')
def getOrganizationDevicesStatusesOverview(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationDevicesStatusesOverview(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationDevicesUplinksAddressesByDevice')
def getOrganizationDevicesUplinksAddressesByDevice(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationDevicesUplinksAddressesByDevice(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationDevicesUplinksLossAndLatency')
def getOrganizationDevicesUplinksLossAndLatency(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationDevicesUplinksLossAndLatency(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationEarlyAccessFeatures')
def getOrganizationEarlyAccessFeatures(organizationId: str):
    return MerakiClient().getOrganizationEarlyAccessFeatures(**{'organizationId': organizationId})

@register('getOrganizationEarlyAccessFeaturesOptIns')
def getOrganizationEarlyAccessFeaturesOptIns(organizationId: str):
    return MerakiClient().getOrganizationEarlyAccessFeaturesOptIns(**{'organizationId': organizationId})

@register('getOrganizationEarlyAccessFeaturesOptIn')
def getOrganizationEarlyAccessFeaturesOptIn(optInId: str, organizationId: str):
    return MerakiClient().getOrganizationEarlyAccessFeaturesOptIn(**{'optInId': optInId, 'organizationId': organizationId})

@register('getOrganizationFirmwareUpgrades')
def getOrganizationFirmwareUpgrades(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationFirmwareUpgrades(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationFirmwareUpgradesByDevice')
def getOrganizationFirmwareUpgradesByDevice(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationFirmwareUpgradesByDevice(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationFloorPlansAutoLocateDevices')
def getOrganizationFloorPlansAutoLocateDevices(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationFloorPlansAutoLocateDevices(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationFloorPlansAutoLocateStatuses')
def getOrganizationFloorPlansAutoLocateStatuses(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationFloorPlansAutoLocateStatuses(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationInsightApplications')
def getOrganizationInsightApplications(organizationId: str):
    return MerakiClient().getOrganizationInsightApplications(**{'organizationId': organizationId})

@register('getOrganizationInsightMonitoredMediaServers')
def getOrganizationInsightMonitoredMediaServers(organizationId: str):
    return MerakiClient().getOrganizationInsightMonitoredMediaServers(**{'organizationId': organizationId})

@register('getOrganizationInsightMonitoredMediaServer')
def getOrganizationInsightMonitoredMediaServer(monitoredMediaServerId: str, organizationId: str):
    return MerakiClient().getOrganizationInsightMonitoredMediaServer(**{'monitoredMediaServerId': monitoredMediaServerId, 'organizationId': organizationId})

@register('getOrganizationInventoryDevices')
def getOrganizationInventoryDevices(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationInventoryDevices(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationInventoryDevicesSwapsBulk')
def getOrganizationInventoryDevicesSwapsBulk(id: str, organizationId: str):
    return MerakiClient().getOrganizationInventoryDevicesSwapsBulk(**{'id': id, 'organizationId': organizationId})

@register('getOrganizationInventoryDevice')
def getOrganizationInventoryDevice(organizationId: str, serial: str):
    return MerakiClient().getOrganizationInventoryDevice(**{'organizationId': organizationId, 'serial': serial})

@register('getOrganizationInventoryOnboardingCloudMonitoringImports')
def getOrganizationInventoryOnboardingCloudMonitoringImports(importIds: list, organizationId: str):
    return MerakiClient().getOrganizationInventoryOnboardingCloudMonitoringImports(**{'importIds': importIds, 'organizationId': organizationId})

@register('getOrganizationInventoryOnboardingCloudMonitoringNetworks')
def getOrganizationInventoryOnboardingCloudMonitoringNetworks(deviceType: str, organizationId: str, **kwargs):
    return MerakiClient().getOrganizationInventoryOnboardingCloudMonitoringNetworks(**{'deviceType': deviceType, 'organizationId': organizationId, **kwargs})

@register('getOrganizationLicenses')
def getOrganizationLicenses(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationLicenses(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationLicensesOverview')
def getOrganizationLicensesOverview(organizationId: str):
    return MerakiClient().getOrganizationLicensesOverview(**{'organizationId': organizationId})

@register('getOrganizationLicense')
def getOrganizationLicense(licenseId: str, organizationId: str):
    return MerakiClient().getOrganizationLicense(**{'licenseId': licenseId, 'organizationId': organizationId})

@register('getOrganizationLicensingCotermLicenses')
def getOrganizationLicensingCotermLicenses(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationLicensingCotermLicenses(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationLoginSecurity')
def getOrganizationLoginSecurity(organizationId: str):
    return MerakiClient().getOrganizationLoginSecurity(**{'organizationId': organizationId})

@register('getOrganizationNetworks')
def getOrganizationNetworks(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationNetworks(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationOpenapiSpec')
def getOrganizationOpenapiSpec(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationOpenapiSpec(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationPolicyObjects')
def getOrganizationPolicyObjects(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationPolicyObjects(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationPolicyObjectsGroups')
def getOrganizationPolicyObjectsGroups(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationPolicyObjectsGroups(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationPolicyObjectsGroup')
def getOrganizationPolicyObjectsGroup(organizationId: str, policyObjectGroupId: str):
    return MerakiClient().getOrganizationPolicyObjectsGroup(**{'organizationId': organizationId, 'policyObjectGroupId': policyObjectGroupId})

@register('getOrganizationPolicyObject')
def getOrganizationPolicyObject(organizationId: str, policyObjectId: str):
    return MerakiClient().getOrganizationPolicyObject(**{'organizationId': organizationId, 'policyObjectId': policyObjectId})

@register('getOrganizationSaml')
def getOrganizationSaml(organizationId: str):
    return MerakiClient().getOrganizationSaml(**{'organizationId': organizationId})

@register('getOrganizationSamlIdps')
def getOrganizationSamlIdps(organizationId: str):
    return MerakiClient().getOrganizationSamlIdps(**{'organizationId': organizationId})

@register('getOrganizationSamlIdp')
def getOrganizationSamlIdp(idpId: str, organizationId: str):
    return MerakiClient().getOrganizationSamlIdp(**{'idpId': idpId, 'organizationId': organizationId})

@register('getOrganizationSamlRoles')
def getOrganizationSamlRoles(organizationId: str):
    return MerakiClient().getOrganizationSamlRoles(**{'organizationId': organizationId})

@register('getOrganizationSamlRole')
def getOrganizationSamlRole(organizationId: str, samlRoleId: str):
    return MerakiClient().getOrganizationSamlRole(**{'organizationId': organizationId, 'samlRoleId': samlRoleId})

@register('getOrganizationSensorReadingsHistory')
def getOrganizationSensorReadingsHistory(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationSensorReadingsHistory(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationSensorReadingsLatest')
def getOrganizationSensorReadingsLatest(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationSensorReadingsLatest(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationSmAdminsRoles')
def getOrganizationSmAdminsRoles(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationSmAdminsRoles(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationSmAdminsRole')
def getOrganizationSmAdminsRole(organizationId: str, roleId: str):
    return MerakiClient().getOrganizationSmAdminsRole(**{'organizationId': organizationId, 'roleId': roleId})

@register('getOrganizationSmApnsCert')
def getOrganizationSmApnsCert(organizationId: str):
    return MerakiClient().getOrganizationSmApnsCert(**{'organizationId': organizationId})

@register('getOrganizationSmSentryPoliciesAssignmentsByNetwork')
def getOrganizationSmSentryPoliciesAssignmentsByNetwork(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationSmSentryPoliciesAssignmentsByNetwork(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationSmVppAccounts')
def getOrganizationSmVppAccounts(organizationId: str):
    return MerakiClient().getOrganizationSmVppAccounts(**{'organizationId': organizationId})

@register('getOrganizationSmVppAccount')
def getOrganizationSmVppAccount(organizationId: str, vppAccountId: str):
    return MerakiClient().getOrganizationSmVppAccount(**{'organizationId': organizationId, 'vppAccountId': vppAccountId})

@register('getOrganizationSnmp')
def getOrganizationSnmp(organizationId: str):
    return MerakiClient().getOrganizationSnmp(**{'organizationId': organizationId})

@register('getOrganizationSplashAsset')
def getOrganizationSplashAsset(id: str, organizationId: str):
    return MerakiClient().getOrganizationSplashAsset(**{'id': id, 'organizationId': organizationId})

@register('getOrganizationSplashThemes')
def getOrganizationSplashThemes(organizationId: str):
    return MerakiClient().getOrganizationSplashThemes(**{'organizationId': organizationId})

@register('getOrganizationSummarySwitchPowerHistory')
def getOrganizationSummarySwitchPowerHistory(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationSummarySwitchPowerHistory(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationSummaryTopAppliancesByUtilization')
def getOrganizationSummaryTopAppliancesByUtilization(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationSummaryTopAppliancesByUtilization(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationSummaryTopApplicationsByUsage')
def getOrganizationSummaryTopApplicationsByUsage(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationSummaryTopApplicationsByUsage(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationSummaryTopApplicationsCategoriesByUsage')
def getOrganizationSummaryTopApplicationsCategoriesByUsage(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationSummaryTopApplicationsCategoriesByUsage(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationSummaryTopClientsByUsage')
def getOrganizationSummaryTopClientsByUsage(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationSummaryTopClientsByUsage(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationSummaryTopClientsManufacturersByUsage')
def getOrganizationSummaryTopClientsManufacturersByUsage(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationSummaryTopClientsManufacturersByUsage(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationSummaryTopDevicesByUsage')
def getOrganizationSummaryTopDevicesByUsage(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationSummaryTopDevicesByUsage(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationSummaryTopDevicesModelsByUsage')
def getOrganizationSummaryTopDevicesModelsByUsage(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationSummaryTopDevicesModelsByUsage(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationSummaryTopNetworksByStatus')
def getOrganizationSummaryTopNetworksByStatus(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationSummaryTopNetworksByStatus(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationSummaryTopSsidsByUsage')
def getOrganizationSummaryTopSsidsByUsage(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationSummaryTopSsidsByUsage(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationSummaryTopSwitchesByEnergyUsage')
def getOrganizationSummaryTopSwitchesByEnergyUsage(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationSummaryTopSwitchesByEnergyUsage(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationSwitchPortsBySwitch')
def getOrganizationSwitchPortsBySwitch(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationSwitchPortsBySwitch(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationSwitchPortsClientsOverviewByDevice')
def getOrganizationSwitchPortsClientsOverviewByDevice(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationSwitchPortsClientsOverviewByDevice(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationSwitchPortsOverview')
def getOrganizationSwitchPortsOverview(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationSwitchPortsOverview(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationSwitchPortsStatusesBySwitch')
def getOrganizationSwitchPortsStatusesBySwitch(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationSwitchPortsStatusesBySwitch(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationSwitchPortsTopologyDiscoveryByDevice')
def getOrganizationSwitchPortsTopologyDiscoveryByDevice(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationSwitchPortsTopologyDiscoveryByDevice(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationUplinksStatuses')
def getOrganizationUplinksStatuses(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationUplinksStatuses(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationWebhooksAlertTypes')
def getOrganizationWebhooksAlertTypes(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationWebhooksAlertTypes(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationWebhooksCallbacksStatus')
def getOrganizationWebhooksCallbacksStatus(callbackId: str, organizationId: str):
    return MerakiClient().getOrganizationWebhooksCallbacksStatus(**{'callbackId': callbackId, 'organizationId': organizationId})

@register('getOrganizationWebhooksLogs')
def getOrganizationWebhooksLogs(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationWebhooksLogs(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationWirelessAirMarshalRules')
def getOrganizationWirelessAirMarshalRules(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationWirelessAirMarshalRules(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationWirelessAirMarshalSettingsByNetwork')
def getOrganizationWirelessAirMarshalSettingsByNetwork(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationWirelessAirMarshalSettingsByNetwork(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationWirelessClientsOverviewByDevice')
def getOrganizationWirelessClientsOverviewByDevice(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationWirelessClientsOverviewByDevice(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationWirelessDevicesChannelUtilizationByDevice')
def getOrganizationWirelessDevicesChannelUtilizationByDevice(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationWirelessDevicesChannelUtilizationByDevice(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationWirelessDevicesChannelUtilizationByNetwork')
def getOrganizationWirelessDevicesChannelUtilizationByNetwork(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationWirelessDevicesChannelUtilizationByNetwork(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationWirelessDevicesChannelUtilizationHistoryByDeviceB')
def getOrganizationWirelessDevicesChannelUtilizationHistoryByDeviceB(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationWirelessDevicesChannelUtilizationHistoryByDeviceB(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationWirelessDevicesChannelUtilizationHistoryByNetwork')
def getOrganizationWirelessDevicesChannelUtilizationHistoryByNetwork(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationWirelessDevicesChannelUtilizationHistoryByNetwork(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationWirelessDevicesEthernetStatuses')
def getOrganizationWirelessDevicesEthernetStatuses(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationWirelessDevicesEthernetStatuses(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationWirelessDevicesPacketLossByClient')
def getOrganizationWirelessDevicesPacketLossByClient(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationWirelessDevicesPacketLossByClient(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationWirelessDevicesPacketLossByDevice')
def getOrganizationWirelessDevicesPacketLossByDevice(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationWirelessDevicesPacketLossByDevice(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationWirelessDevicesPacketLossByNetwork')
def getOrganizationWirelessDevicesPacketLossByNetwork(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationWirelessDevicesPacketLossByNetwork(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationWirelessDevicesWirelessControllersByDevice')
def getOrganizationWirelessDevicesWirelessControllersByDevice(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationWirelessDevicesWirelessControllersByDevice(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationWirelessRfProfilesAssignmentsByDevice')
def getOrganizationWirelessRfProfilesAssignmentsByDevice(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationWirelessRfProfilesAssignmentsByDevice(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationWirelessSsidsStatusesByDevice')
def getOrganizationWirelessSsidsStatusesByDevice(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationWirelessSsidsStatusesByDevice(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationWirelessControllerAvailabilitiesChangeHistory')
def getOrganizationWirelessControllerAvailabilitiesChangeHistory(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationWirelessControllerAvailabilitiesChangeHistory(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationWirelessControllerClientsOverviewHistoryByDeviceB')
def getOrganizationWirelessControllerClientsOverviewHistoryByDeviceB(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationWirelessControllerClientsOverviewHistoryByDeviceB(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationWirelessControllerConnections')
def getOrganizationWirelessControllerConnections(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationWirelessControllerConnections(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationWirelessControllerDevicesInterfacesL2ByDevice')
def getOrganizationWirelessControllerDevicesInterfacesL2ByDevice(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationWirelessControllerDevicesInterfacesL2ByDevice(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationWirelessControllerDevicesInterfacesL2StatusesChan')
def getOrganizationWirelessControllerDevicesInterfacesL2StatusesChan(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationWirelessControllerDevicesInterfacesL2StatusesChan(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationWirelessControllerDevicesInterfacesL2UsageHistory')
def getOrganizationWirelessControllerDevicesInterfacesL2UsageHistory(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationWirelessControllerDevicesInterfacesL2UsageHistory(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationWirelessControllerDevicesInterfacesL3ByDevice')
def getOrganizationWirelessControllerDevicesInterfacesL3ByDevice(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationWirelessControllerDevicesInterfacesL3ByDevice(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationWirelessControllerDevicesInterfacesL3StatusesChan')
def getOrganizationWirelessControllerDevicesInterfacesL3StatusesChan(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationWirelessControllerDevicesInterfacesL3StatusesChan(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationWirelessControllerDevicesInterfacesL3UsageHistory')
def getOrganizationWirelessControllerDevicesInterfacesL3UsageHistory(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationWirelessControllerDevicesInterfacesL3UsageHistory(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationWirelessControllerDevicesInterfacesPacketsOvervie')
def getOrganizationWirelessControllerDevicesInterfacesPacketsOvervie(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationWirelessControllerDevicesInterfacesPacketsOvervie(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationWirelessControllerDevicesInterfacesUsageHistoryBy')
def getOrganizationWirelessControllerDevicesInterfacesUsageHistoryBy(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationWirelessControllerDevicesInterfacesUsageHistoryBy(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationWirelessControllerDevicesRedundancyFailoverHistor')
def getOrganizationWirelessControllerDevicesRedundancyFailoverHistor(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationWirelessControllerDevicesRedundancyFailoverHistor(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationWirelessControllerDevicesRedundancyStatuses')
def getOrganizationWirelessControllerDevicesRedundancyStatuses(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationWirelessControllerDevicesRedundancyStatuses(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationWirelessControllerDevicesSystemUtilizationHistory')
def getOrganizationWirelessControllerDevicesSystemUtilizationHistory(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationWirelessControllerDevicesSystemUtilizationHistory(**{'organizationId': organizationId, **kwargs})

@register('getOrganizationWirelessControllerOverviewByDevice')
def getOrganizationWirelessControllerOverviewByDevice(organizationId: str, **kwargs):
    return MerakiClient().getOrganizationWirelessControllerOverviewByDevice(**{'organizationId': organizationId, **kwargs})
