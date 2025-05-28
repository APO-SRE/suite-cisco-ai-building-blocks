# app/llm/function_dispatcher/meraki_dispatcher.py
from app.llm.function_dispatcher import register
from app.llm.platform_clients.meraki_client import MerakiClient

@register('getAdministeredIdentitiesMe')
def getAdministeredIdentitiesMe(**kwargs):
    return MerakiClient().getAdministeredIdentitiesMe(**kwargs)

@register('getAdministeredIdentitiesMeApiKeys')
def getAdministeredIdentitiesMeApiKeys(**kwargs):
    return MerakiClient().getAdministeredIdentitiesMeApiKeys(**kwargs)

@register('getAdministeredLicensingSubscriptionEntitlements')
def getAdministeredLicensingSubscriptionEntitlements(**kwargs):
    return MerakiClient().getAdministeredLicensingSubscriptionEntitlements(**kwargs)

@register('getAdministeredLicensingSubscriptionSubscriptions')
def getAdministeredLicensingSubscriptionSubscriptions(**kwargs):
    return MerakiClient().getAdministeredLicensingSubscriptionSubscriptions(**kwargs)

@register('getAdministeredLicensingSubscriptionSubscriptionsComplianceStatuses')
def getAdministeredLicensingSubscriptionSubscriptionsComplianceStatuses(**kwargs):
    return MerakiClient().getAdministeredLicensingSubscriptionSubscriptionsComplianceStatuses(**kwargs)

@register('getDevice')
def getDevice(**kwargs):
    return MerakiClient().getDevice(**kwargs)

@register('getDeviceApplianceDhcpSubnets')
def getDeviceApplianceDhcpSubnets(**kwargs):
    return MerakiClient().getDeviceApplianceDhcpSubnets(**kwargs)

@register('getDeviceAppliancePerformance')
def getDeviceAppliancePerformance(**kwargs):
    return MerakiClient().getDeviceAppliancePerformance(**kwargs)

@register('getDeviceAppliancePrefixesDelegated')
def getDeviceAppliancePrefixesDelegated(**kwargs):
    return MerakiClient().getDeviceAppliancePrefixesDelegated(**kwargs)

@register('getDeviceAppliancePrefixesDelegatedVlanAssignments')
def getDeviceAppliancePrefixesDelegatedVlanAssignments(**kwargs):
    return MerakiClient().getDeviceAppliancePrefixesDelegatedVlanAssignments(**kwargs)

@register('getDeviceApplianceRadioSettings')
def getDeviceApplianceRadioSettings(**kwargs):
    return MerakiClient().getDeviceApplianceRadioSettings(**kwargs)

@register('getDeviceApplianceUplinksSettings')
def getDeviceApplianceUplinksSettings(**kwargs):
    return MerakiClient().getDeviceApplianceUplinksSettings(**kwargs)

@register('getDeviceCameraAnalyticsLive')
def getDeviceCameraAnalyticsLive(**kwargs):
    return MerakiClient().getDeviceCameraAnalyticsLive(**kwargs)

@register('getDeviceCameraAnalyticsOverview')
def getDeviceCameraAnalyticsOverview(**kwargs):
    return MerakiClient().getDeviceCameraAnalyticsOverview(**kwargs)

@register('getDeviceCameraAnalyticsRecent')
def getDeviceCameraAnalyticsRecent(**kwargs):
    return MerakiClient().getDeviceCameraAnalyticsRecent(**kwargs)

@register('getDeviceCameraAnalyticsZones')
def getDeviceCameraAnalyticsZones(**kwargs):
    return MerakiClient().getDeviceCameraAnalyticsZones(**kwargs)

@register('getDeviceCameraAnalyticsZoneHistory')
def getDeviceCameraAnalyticsZoneHistory(**kwargs):
    return MerakiClient().getDeviceCameraAnalyticsZoneHistory(**kwargs)

@register('getDeviceCameraCustomAnalytics')
def getDeviceCameraCustomAnalytics(**kwargs):
    return MerakiClient().getDeviceCameraCustomAnalytics(**kwargs)

@register('getDeviceCameraQualityAndRetention')
def getDeviceCameraQualityAndRetention(**kwargs):
    return MerakiClient().getDeviceCameraQualityAndRetention(**kwargs)

@register('getDeviceCameraSense')
def getDeviceCameraSense(**kwargs):
    return MerakiClient().getDeviceCameraSense(**kwargs)

@register('getDeviceCameraSenseObjectDetectionModels')
def getDeviceCameraSenseObjectDetectionModels(**kwargs):
    return MerakiClient().getDeviceCameraSenseObjectDetectionModels(**kwargs)

@register('getDeviceCameraVideoSettings')
def getDeviceCameraVideoSettings(**kwargs):
    return MerakiClient().getDeviceCameraVideoSettings(**kwargs)

@register('getDeviceCameraVideoLink')
def getDeviceCameraVideoLink(**kwargs):
    return MerakiClient().getDeviceCameraVideoLink(**kwargs)

@register('getDeviceCameraWirelessProfiles')
def getDeviceCameraWirelessProfiles(**kwargs):
    return MerakiClient().getDeviceCameraWirelessProfiles(**kwargs)

@register('getDeviceCellularSims')
def getDeviceCellularSims(**kwargs):
    return MerakiClient().getDeviceCellularSims(**kwargs)

@register('getDeviceCellularGatewayLan')
def getDeviceCellularGatewayLan(**kwargs):
    return MerakiClient().getDeviceCellularGatewayLan(**kwargs)

@register('getDeviceCellularGatewayPortForwardingRules')
def getDeviceCellularGatewayPortForwardingRules(**kwargs):
    return MerakiClient().getDeviceCellularGatewayPortForwardingRules(**kwargs)

@register('getDeviceClients')
def getDeviceClients(**kwargs):
    return MerakiClient().getDeviceClients(**kwargs)

@register('getDeviceLiveToolsArpTable')
def getDeviceLiveToolsArpTable(**kwargs):
    return MerakiClient().getDeviceLiveToolsArpTable(**kwargs)

@register('getDeviceLiveToolsCableTest')
def getDeviceLiveToolsCableTest(**kwargs):
    return MerakiClient().getDeviceLiveToolsCableTest(**kwargs)

@register('getDeviceLiveToolsLedsBlink')
def getDeviceLiveToolsLedsBlink(**kwargs):
    return MerakiClient().getDeviceLiveToolsLedsBlink(**kwargs)

@register('getDeviceLiveToolsPing')
def getDeviceLiveToolsPing(**kwargs):
    return MerakiClient().getDeviceLiveToolsPing(**kwargs)

@register('getDeviceLiveToolsPingDevice')
def getDeviceLiveToolsPingDevice(**kwargs):
    return MerakiClient().getDeviceLiveToolsPingDevice(**kwargs)

@register('getDeviceLiveToolsThroughputTest')
def getDeviceLiveToolsThroughputTest(**kwargs):
    return MerakiClient().getDeviceLiveToolsThroughputTest(**kwargs)

@register('getDeviceLiveToolsWakeOnLan')
def getDeviceLiveToolsWakeOnLan(**kwargs):
    return MerakiClient().getDeviceLiveToolsWakeOnLan(**kwargs)

@register('getDeviceLldpCdp')
def getDeviceLldpCdp(**kwargs):
    return MerakiClient().getDeviceLldpCdp(**kwargs)

@register('getDeviceLossAndLatencyHistory')
def getDeviceLossAndLatencyHistory(**kwargs):
    return MerakiClient().getDeviceLossAndLatencyHistory(**kwargs)

@register('getDeviceManagementInterface')
def getDeviceManagementInterface(**kwargs):
    return MerakiClient().getDeviceManagementInterface(**kwargs)

@register('getDeviceSensorCommands')
def getDeviceSensorCommands(**kwargs):
    return MerakiClient().getDeviceSensorCommands(**kwargs)

@register('getDeviceSensorCommand')
def getDeviceSensorCommand(**kwargs):
    return MerakiClient().getDeviceSensorCommand(**kwargs)

@register('getDeviceSensorRelationships')
def getDeviceSensorRelationships(**kwargs):
    return MerakiClient().getDeviceSensorRelationships(**kwargs)

@register('getDeviceSwitchPorts')
def getDeviceSwitchPorts(**kwargs):
    return MerakiClient().getDeviceSwitchPorts(**kwargs)

@register('getDeviceSwitchPortsStatuses')
def getDeviceSwitchPortsStatuses(**kwargs):
    return MerakiClient().getDeviceSwitchPortsStatuses(**kwargs)

@register('getDeviceSwitchPortsStatusesPackets')
def getDeviceSwitchPortsStatusesPackets(**kwargs):
    return MerakiClient().getDeviceSwitchPortsStatusesPackets(**kwargs)

@register('getDeviceSwitchPort')
def getDeviceSwitchPort(**kwargs):
    return MerakiClient().getDeviceSwitchPort(**kwargs)

@register('getDeviceSwitchRoutingInterfaces')
def getDeviceSwitchRoutingInterfaces(**kwargs):
    return MerakiClient().getDeviceSwitchRoutingInterfaces(**kwargs)

@register('getDeviceSwitchRoutingInterface')
def getDeviceSwitchRoutingInterface(**kwargs):
    return MerakiClient().getDeviceSwitchRoutingInterface(**kwargs)

@register('getDeviceSwitchRoutingInterfaceDhcp')
def getDeviceSwitchRoutingInterfaceDhcp(**kwargs):
    return MerakiClient().getDeviceSwitchRoutingInterfaceDhcp(**kwargs)

@register('getDeviceSwitchRoutingStaticRoutes')
def getDeviceSwitchRoutingStaticRoutes(**kwargs):
    return MerakiClient().getDeviceSwitchRoutingStaticRoutes(**kwargs)

@register('getDeviceSwitchRoutingStaticRoute')
def getDeviceSwitchRoutingStaticRoute(**kwargs):
    return MerakiClient().getDeviceSwitchRoutingStaticRoute(**kwargs)

@register('getDeviceSwitchWarmSpare')
def getDeviceSwitchWarmSpare(**kwargs):
    return MerakiClient().getDeviceSwitchWarmSpare(**kwargs)

@register('getDeviceWirelessBluetoothSettings')
def getDeviceWirelessBluetoothSettings(**kwargs):
    return MerakiClient().getDeviceWirelessBluetoothSettings(**kwargs)

@register('getDeviceWirelessConnectionStats')
def getDeviceWirelessConnectionStats(**kwargs):
    return MerakiClient().getDeviceWirelessConnectionStats(**kwargs)

@register('getDeviceWirelessElectronicShelfLabel')
def getDeviceWirelessElectronicShelfLabel(**kwargs):
    return MerakiClient().getDeviceWirelessElectronicShelfLabel(**kwargs)

@register('getDeviceWirelessLatencyStats')
def getDeviceWirelessLatencyStats(**kwargs):
    return MerakiClient().getDeviceWirelessLatencyStats(**kwargs)

@register('getDeviceWirelessRadioSettings')
def getDeviceWirelessRadioSettings(**kwargs):
    return MerakiClient().getDeviceWirelessRadioSettings(**kwargs)

@register('getDeviceWirelessStatus')
def getDeviceWirelessStatus(**kwargs):
    return MerakiClient().getDeviceWirelessStatus(**kwargs)

@register('getNetwork')
def getNetwork(**kwargs):
    return MerakiClient().getNetwork(**kwargs)

@register('getNetworkAlertsHistory')
def getNetworkAlertsHistory(**kwargs):
    return MerakiClient().getNetworkAlertsHistory(**kwargs)

@register('getNetworkAlertsSettings')
def getNetworkAlertsSettings(**kwargs):
    return MerakiClient().getNetworkAlertsSettings(**kwargs)

@register('getNetworkApplianceClientSecurityEvents')
def getNetworkApplianceClientSecurityEvents(**kwargs):
    return MerakiClient().getNetworkApplianceClientSecurityEvents(**kwargs)

@register('getNetworkApplianceConnectivityMonitoringDestinations')
def getNetworkApplianceConnectivityMonitoringDestinations(**kwargs):
    return MerakiClient().getNetworkApplianceConnectivityMonitoringDestinations(**kwargs)

@register('getNetworkApplianceContentFiltering')
def getNetworkApplianceContentFiltering(**kwargs):
    return MerakiClient().getNetworkApplianceContentFiltering(**kwargs)

@register('getNetworkApplianceContentFilteringCategories')
def getNetworkApplianceContentFilteringCategories(**kwargs):
    return MerakiClient().getNetworkApplianceContentFilteringCategories(**kwargs)

@register('getNetworkApplianceFirewallCellularFirewallRules')
def getNetworkApplianceFirewallCellularFirewallRules(**kwargs):
    return MerakiClient().getNetworkApplianceFirewallCellularFirewallRules(**kwargs)

@register('getNetworkApplianceFirewallFirewalledServices')
def getNetworkApplianceFirewallFirewalledServices(**kwargs):
    return MerakiClient().getNetworkApplianceFirewallFirewalledServices(**kwargs)

@register('getNetworkApplianceFirewallFirewalledService')
def getNetworkApplianceFirewallFirewalledService(**kwargs):
    return MerakiClient().getNetworkApplianceFirewallFirewalledService(**kwargs)

@register('getNetworkApplianceFirewallInboundCellularFirewallRules')
def getNetworkApplianceFirewallInboundCellularFirewallRules(**kwargs):
    return MerakiClient().getNetworkApplianceFirewallInboundCellularFirewallRules(**kwargs)

@register('getNetworkApplianceFirewallInboundFirewallRules')
def getNetworkApplianceFirewallInboundFirewallRules(**kwargs):
    return MerakiClient().getNetworkApplianceFirewallInboundFirewallRules(**kwargs)

@register('getNetworkApplianceFirewallL3FirewallRules')
def getNetworkApplianceFirewallL3FirewallRules(**kwargs):
    return MerakiClient().getNetworkApplianceFirewallL3FirewallRules(**kwargs)

@register('getNetworkApplianceFirewallL7FirewallRules')
def getNetworkApplianceFirewallL7FirewallRules(**kwargs):
    return MerakiClient().getNetworkApplianceFirewallL7FirewallRules(**kwargs)

@register('getNetworkApplianceFirewallL7FirewallRulesApplicationCategories')
def getNetworkApplianceFirewallL7FirewallRulesApplicationCategories(**kwargs):
    return MerakiClient().getNetworkApplianceFirewallL7FirewallRulesApplicationCategories(**kwargs)

@register('getNetworkApplianceFirewallOneToManyNatRules')
def getNetworkApplianceFirewallOneToManyNatRules(**kwargs):
    return MerakiClient().getNetworkApplianceFirewallOneToManyNatRules(**kwargs)

@register('getNetworkApplianceFirewallOneToOneNatRules')
def getNetworkApplianceFirewallOneToOneNatRules(**kwargs):
    return MerakiClient().getNetworkApplianceFirewallOneToOneNatRules(**kwargs)

@register('getNetworkApplianceFirewallPortForwardingRules')
def getNetworkApplianceFirewallPortForwardingRules(**kwargs):
    return MerakiClient().getNetworkApplianceFirewallPortForwardingRules(**kwargs)

@register('getNetworkApplianceFirewallSettings')
def getNetworkApplianceFirewallSettings(**kwargs):
    return MerakiClient().getNetworkApplianceFirewallSettings(**kwargs)

@register('getNetworkAppliancePorts')
def getNetworkAppliancePorts(**kwargs):
    return MerakiClient().getNetworkAppliancePorts(**kwargs)

@register('getNetworkAppliancePort')
def getNetworkAppliancePort(**kwargs):
    return MerakiClient().getNetworkAppliancePort(**kwargs)

@register('getNetworkAppliancePrefixesDelegatedStatics')
def getNetworkAppliancePrefixesDelegatedStatics(**kwargs):
    return MerakiClient().getNetworkAppliancePrefixesDelegatedStatics(**kwargs)

@register('getNetworkAppliancePrefixesDelegatedStatic')
def getNetworkAppliancePrefixesDelegatedStatic(**kwargs):
    return MerakiClient().getNetworkAppliancePrefixesDelegatedStatic(**kwargs)

@register('getNetworkApplianceRfProfiles')
def getNetworkApplianceRfProfiles(**kwargs):
    return MerakiClient().getNetworkApplianceRfProfiles(**kwargs)

@register('getNetworkApplianceRfProfile')
def getNetworkApplianceRfProfile(**kwargs):
    return MerakiClient().getNetworkApplianceRfProfile(**kwargs)

@register('getNetworkApplianceSecurityEvents')
def getNetworkApplianceSecurityEvents(**kwargs):
    return MerakiClient().getNetworkApplianceSecurityEvents(**kwargs)

@register('getNetworkApplianceSecurityIntrusion')
def getNetworkApplianceSecurityIntrusion(**kwargs):
    return MerakiClient().getNetworkApplianceSecurityIntrusion(**kwargs)

@register('getNetworkApplianceSecurityMalware')
def getNetworkApplianceSecurityMalware(**kwargs):
    return MerakiClient().getNetworkApplianceSecurityMalware(**kwargs)

@register('getNetworkApplianceSettings')
def getNetworkApplianceSettings(**kwargs):
    return MerakiClient().getNetworkApplianceSettings(**kwargs)

@register('getNetworkApplianceSingleLan')
def getNetworkApplianceSingleLan(**kwargs):
    return MerakiClient().getNetworkApplianceSingleLan(**kwargs)

@register('getNetworkApplianceSsids')
def getNetworkApplianceSsids(**kwargs):
    return MerakiClient().getNetworkApplianceSsids(**kwargs)

@register('getNetworkApplianceSsid')
def getNetworkApplianceSsid(**kwargs):
    return MerakiClient().getNetworkApplianceSsid(**kwargs)

@register('getNetworkApplianceStaticRoutes')
def getNetworkApplianceStaticRoutes(**kwargs):
    return MerakiClient().getNetworkApplianceStaticRoutes(**kwargs)

@register('getNetworkApplianceStaticRoute')
def getNetworkApplianceStaticRoute(**kwargs):
    return MerakiClient().getNetworkApplianceStaticRoute(**kwargs)

@register('getNetworkApplianceTrafficShaping')
def getNetworkApplianceTrafficShaping(**kwargs):
    return MerakiClient().getNetworkApplianceTrafficShaping(**kwargs)

@register('getNetworkApplianceTrafficShapingCustomPerformanceClasses')
def getNetworkApplianceTrafficShapingCustomPerformanceClasses(**kwargs):
    return MerakiClient().getNetworkApplianceTrafficShapingCustomPerformanceClasses(**kwargs)

@register('getNetworkApplianceTrafficShapingCustomPerformanceClass')
def getNetworkApplianceTrafficShapingCustomPerformanceClass(**kwargs):
    return MerakiClient().getNetworkApplianceTrafficShapingCustomPerformanceClass(**kwargs)

@register('getNetworkApplianceTrafficShapingRules')
def getNetworkApplianceTrafficShapingRules(**kwargs):
    return MerakiClient().getNetworkApplianceTrafficShapingRules(**kwargs)

@register('getNetworkApplianceTrafficShapingUplinkBandwidth')
def getNetworkApplianceTrafficShapingUplinkBandwidth(**kwargs):
    return MerakiClient().getNetworkApplianceTrafficShapingUplinkBandwidth(**kwargs)

@register('getNetworkApplianceTrafficShapingUplinkSelection')
def getNetworkApplianceTrafficShapingUplinkSelection(**kwargs):
    return MerakiClient().getNetworkApplianceTrafficShapingUplinkSelection(**kwargs)

@register('getNetworkApplianceUplinksUsageHistory')
def getNetworkApplianceUplinksUsageHistory(**kwargs):
    return MerakiClient().getNetworkApplianceUplinksUsageHistory(**kwargs)

@register('getNetworkApplianceVlans')
def getNetworkApplianceVlans(**kwargs):
    return MerakiClient().getNetworkApplianceVlans(**kwargs)

@register('getNetworkApplianceVlansSettings')
def getNetworkApplianceVlansSettings(**kwargs):
    return MerakiClient().getNetworkApplianceVlansSettings(**kwargs)

@register('getNetworkApplianceVlan')
def getNetworkApplianceVlan(**kwargs):
    return MerakiClient().getNetworkApplianceVlan(**kwargs)

@register('getNetworkApplianceVpnBgp')
def getNetworkApplianceVpnBgp(**kwargs):
    return MerakiClient().getNetworkApplianceVpnBgp(**kwargs)

@register('getNetworkApplianceVpnSiteToSiteVpn')
def getNetworkApplianceVpnSiteToSiteVpn(**kwargs):
    return MerakiClient().getNetworkApplianceVpnSiteToSiteVpn(**kwargs)

@register('getNetworkApplianceWarmSpare')
def getNetworkApplianceWarmSpare(**kwargs):
    return MerakiClient().getNetworkApplianceWarmSpare(**kwargs)

@register('getNetworkBluetoothClients')
def getNetworkBluetoothClients(**kwargs):
    return MerakiClient().getNetworkBluetoothClients(**kwargs)

@register('getNetworkBluetoothClient')
def getNetworkBluetoothClient(**kwargs):
    return MerakiClient().getNetworkBluetoothClient(**kwargs)

@register('getNetworkCameraQualityRetentionProfiles')
def getNetworkCameraQualityRetentionProfiles(**kwargs):
    return MerakiClient().getNetworkCameraQualityRetentionProfiles(**kwargs)

@register('getNetworkCameraQualityRetentionProfile')
def getNetworkCameraQualityRetentionProfile(**kwargs):
    return MerakiClient().getNetworkCameraQualityRetentionProfile(**kwargs)

@register('getNetworkCameraSchedules')
def getNetworkCameraSchedules(**kwargs):
    return MerakiClient().getNetworkCameraSchedules(**kwargs)

@register('getNetworkCameraWirelessProfiles')
def getNetworkCameraWirelessProfiles(**kwargs):
    return MerakiClient().getNetworkCameraWirelessProfiles(**kwargs)

@register('getNetworkCameraWirelessProfile')
def getNetworkCameraWirelessProfile(**kwargs):
    return MerakiClient().getNetworkCameraWirelessProfile(**kwargs)

@register('getNetworkCellularGatewayConnectivityMonitoringDestinations')
def getNetworkCellularGatewayConnectivityMonitoringDestinations(**kwargs):
    return MerakiClient().getNetworkCellularGatewayConnectivityMonitoringDestinations(**kwargs)

@register('getNetworkCellularGatewayDhcp')
def getNetworkCellularGatewayDhcp(**kwargs):
    return MerakiClient().getNetworkCellularGatewayDhcp(**kwargs)

@register('getNetworkCellularGatewaySubnetPool')
def getNetworkCellularGatewaySubnetPool(**kwargs):
    return MerakiClient().getNetworkCellularGatewaySubnetPool(**kwargs)

@register('getNetworkCellularGatewayUplink')
def getNetworkCellularGatewayUplink(**kwargs):
    return MerakiClient().getNetworkCellularGatewayUplink(**kwargs)

@register('getNetworkClients')
def getNetworkClients(**kwargs):
    return MerakiClient().getNetworkClients(**kwargs)

@register('getNetworkClientsApplicationUsage')
def getNetworkClientsApplicationUsage(**kwargs):
    return MerakiClient().getNetworkClientsApplicationUsage(**kwargs)

@register('getNetworkClientsBandwidthUsageHistory')
def getNetworkClientsBandwidthUsageHistory(**kwargs):
    return MerakiClient().getNetworkClientsBandwidthUsageHistory(**kwargs)

@register('getNetworkClientsOverview')
def getNetworkClientsOverview(**kwargs):
    return MerakiClient().getNetworkClientsOverview(**kwargs)

@register('getNetworkClientsUsageHistories')
def getNetworkClientsUsageHistories(**kwargs):
    return MerakiClient().getNetworkClientsUsageHistories(**kwargs)

@register('getNetworkClient')
def getNetworkClient(**kwargs):
    return MerakiClient().getNetworkClient(**kwargs)

@register('getNetworkClientPolicy')
def getNetworkClientPolicy(**kwargs):
    return MerakiClient().getNetworkClientPolicy(**kwargs)

@register('getNetworkClientSplashAuthorizationStatus')
def getNetworkClientSplashAuthorizationStatus(**kwargs):
    return MerakiClient().getNetworkClientSplashAuthorizationStatus(**kwargs)

@register('getNetworkClientTrafficHistory')
def getNetworkClientTrafficHistory(**kwargs):
    return MerakiClient().getNetworkClientTrafficHistory(**kwargs)

@register('getNetworkClientUsageHistory')
def getNetworkClientUsageHistory(**kwargs):
    return MerakiClient().getNetworkClientUsageHistory(**kwargs)

@register('getNetworkDevices')
def getNetworkDevices(**kwargs):
    return MerakiClient().getNetworkDevices(**kwargs)

@register('getNetworkEvents')
def getNetworkEvents(**kwargs):
    return MerakiClient().getNetworkEvents(**kwargs)

@register('getNetworkEventsEventTypes')
def getNetworkEventsEventTypes(**kwargs):
    return MerakiClient().getNetworkEventsEventTypes(**kwargs)

@register('getNetworkFirmwareUpgrades')
def getNetworkFirmwareUpgrades(**kwargs):
    return MerakiClient().getNetworkFirmwareUpgrades(**kwargs)

@register('getNetworkFirmwareUpgradesStagedEvents')
def getNetworkFirmwareUpgradesStagedEvents(**kwargs):
    return MerakiClient().getNetworkFirmwareUpgradesStagedEvents(**kwargs)

@register('getNetworkFirmwareUpgradesStagedGroups')
def getNetworkFirmwareUpgradesStagedGroups(**kwargs):
    return MerakiClient().getNetworkFirmwareUpgradesStagedGroups(**kwargs)

@register('getNetworkFirmwareUpgradesStagedGroup')
def getNetworkFirmwareUpgradesStagedGroup(**kwargs):
    return MerakiClient().getNetworkFirmwareUpgradesStagedGroup(**kwargs)

@register('getNetworkFirmwareUpgradesStagedStages')
def getNetworkFirmwareUpgradesStagedStages(**kwargs):
    return MerakiClient().getNetworkFirmwareUpgradesStagedStages(**kwargs)

@register('getNetworkFloorPlans')
def getNetworkFloorPlans(**kwargs):
    return MerakiClient().getNetworkFloorPlans(**kwargs)

@register('getNetworkFloorPlan')
def getNetworkFloorPlan(**kwargs):
    return MerakiClient().getNetworkFloorPlan(**kwargs)

@register('getNetworkGroupPolicies')
def getNetworkGroupPolicies(**kwargs):
    return MerakiClient().getNetworkGroupPolicies(**kwargs)

@register('getNetworkGroupPolicy')
def getNetworkGroupPolicy(**kwargs):
    return MerakiClient().getNetworkGroupPolicy(**kwargs)

@register('getNetworkHealthAlerts')
def getNetworkHealthAlerts(**kwargs):
    return MerakiClient().getNetworkHealthAlerts(**kwargs)

@register('getNetworkInsightApplicationHealthByTime')
def getNetworkInsightApplicationHealthByTime(**kwargs):
    return MerakiClient().getNetworkInsightApplicationHealthByTime(**kwargs)

@register('getNetworkMerakiAuthUsers')
def getNetworkMerakiAuthUsers(**kwargs):
    return MerakiClient().getNetworkMerakiAuthUsers(**kwargs)

@register('getNetworkMerakiAuthUser')
def getNetworkMerakiAuthUser(**kwargs):
    return MerakiClient().getNetworkMerakiAuthUser(**kwargs)

@register('getNetworkMqttBrokers')
def getNetworkMqttBrokers(**kwargs):
    return MerakiClient().getNetworkMqttBrokers(**kwargs)

@register('getNetworkMqttBroker')
def getNetworkMqttBroker(**kwargs):
    return MerakiClient().getNetworkMqttBroker(**kwargs)

@register('getNetworkNetflow')
def getNetworkNetflow(**kwargs):
    return MerakiClient().getNetworkNetflow(**kwargs)

@register('getNetworkNetworkHealthChannelUtilization')
def getNetworkNetworkHealthChannelUtilization(**kwargs):
    return MerakiClient().getNetworkNetworkHealthChannelUtilization(**kwargs)

@register('getNetworkPiiPiiKeys')
def getNetworkPiiPiiKeys(**kwargs):
    return MerakiClient().getNetworkPiiPiiKeys(**kwargs)

@register('getNetworkPiiRequests')
def getNetworkPiiRequests(**kwargs):
    return MerakiClient().getNetworkPiiRequests(**kwargs)

@register('getNetworkPiiRequest')
def getNetworkPiiRequest(**kwargs):
    return MerakiClient().getNetworkPiiRequest(**kwargs)

@register('getNetworkPiiSmDevicesForKey')
def getNetworkPiiSmDevicesForKey(**kwargs):
    return MerakiClient().getNetworkPiiSmDevicesForKey(**kwargs)

@register('getNetworkPiiSmOwnersForKey')
def getNetworkPiiSmOwnersForKey(**kwargs):
    return MerakiClient().getNetworkPiiSmOwnersForKey(**kwargs)

@register('getNetworkPoliciesByClient')
def getNetworkPoliciesByClient(**kwargs):
    return MerakiClient().getNetworkPoliciesByClient(**kwargs)

@register('getNetworkSensorAlertsCurrentOverviewByMetric')
def getNetworkSensorAlertsCurrentOverviewByMetric(**kwargs):
    return MerakiClient().getNetworkSensorAlertsCurrentOverviewByMetric(**kwargs)

@register('getNetworkSensorAlertsOverviewByMetric')
def getNetworkSensorAlertsOverviewByMetric(**kwargs):
    return MerakiClient().getNetworkSensorAlertsOverviewByMetric(**kwargs)

@register('getNetworkSensorAlertsProfiles')
def getNetworkSensorAlertsProfiles(**kwargs):
    return MerakiClient().getNetworkSensorAlertsProfiles(**kwargs)

@register('getNetworkSensorAlertsProfile')
def getNetworkSensorAlertsProfile(**kwargs):
    return MerakiClient().getNetworkSensorAlertsProfile(**kwargs)

@register('getNetworkSensorMqttBrokers')
def getNetworkSensorMqttBrokers(**kwargs):
    return MerakiClient().getNetworkSensorMqttBrokers(**kwargs)

@register('getNetworkSensorMqttBroker')
def getNetworkSensorMqttBroker(**kwargs):
    return MerakiClient().getNetworkSensorMqttBroker(**kwargs)

@register('getNetworkSensorRelationships')
def getNetworkSensorRelationships(**kwargs):
    return MerakiClient().getNetworkSensorRelationships(**kwargs)

@register('getNetworkSettings')
def getNetworkSettings(**kwargs):
    return MerakiClient().getNetworkSettings(**kwargs)

@register('getNetworkSmBypassActivationLockAttempt')
def getNetworkSmBypassActivationLockAttempt(**kwargs):
    return MerakiClient().getNetworkSmBypassActivationLockAttempt(**kwargs)

@register('getNetworkSmDevices')
def getNetworkSmDevices(**kwargs):
    return MerakiClient().getNetworkSmDevices(**kwargs)

@register('getNetworkSmDeviceCellularUsageHistory')
def getNetworkSmDeviceCellularUsageHistory(**kwargs):
    return MerakiClient().getNetworkSmDeviceCellularUsageHistory(**kwargs)

@register('getNetworkSmDeviceCerts')
def getNetworkSmDeviceCerts(**kwargs):
    return MerakiClient().getNetworkSmDeviceCerts(**kwargs)

@register('getNetworkSmDeviceConnectivity')
def getNetworkSmDeviceConnectivity(**kwargs):
    return MerakiClient().getNetworkSmDeviceConnectivity(**kwargs)

@register('getNetworkSmDeviceDesktopLogs')
def getNetworkSmDeviceDesktopLogs(**kwargs):
    return MerakiClient().getNetworkSmDeviceDesktopLogs(**kwargs)

@register('getNetworkSmDeviceDeviceCommandLogs')
def getNetworkSmDeviceDeviceCommandLogs(**kwargs):
    return MerakiClient().getNetworkSmDeviceDeviceCommandLogs(**kwargs)

@register('getNetworkSmDeviceDeviceProfiles')
def getNetworkSmDeviceDeviceProfiles(**kwargs):
    return MerakiClient().getNetworkSmDeviceDeviceProfiles(**kwargs)

@register('getNetworkSmDeviceNetworkAdapters')
def getNetworkSmDeviceNetworkAdapters(**kwargs):
    return MerakiClient().getNetworkSmDeviceNetworkAdapters(**kwargs)

@register('getNetworkSmDevicePerformanceHistory')
def getNetworkSmDevicePerformanceHistory(**kwargs):
    return MerakiClient().getNetworkSmDevicePerformanceHistory(**kwargs)

@register('getNetworkSmDeviceRestrictions')
def getNetworkSmDeviceRestrictions(**kwargs):
    return MerakiClient().getNetworkSmDeviceRestrictions(**kwargs)

@register('getNetworkSmDeviceSecurityCenters')
def getNetworkSmDeviceSecurityCenters(**kwargs):
    return MerakiClient().getNetworkSmDeviceSecurityCenters(**kwargs)

@register('getNetworkSmDeviceSoftwares')
def getNetworkSmDeviceSoftwares(**kwargs):
    return MerakiClient().getNetworkSmDeviceSoftwares(**kwargs)

@register('getNetworkSmDeviceWlanLists')
def getNetworkSmDeviceWlanLists(**kwargs):
    return MerakiClient().getNetworkSmDeviceWlanLists(**kwargs)

@register('getNetworkSmProfiles')
def getNetworkSmProfiles(**kwargs):
    return MerakiClient().getNetworkSmProfiles(**kwargs)

@register('getNetworkSmTargetGroups')
def getNetworkSmTargetGroups(**kwargs):
    return MerakiClient().getNetworkSmTargetGroups(**kwargs)

@register('getNetworkSmTargetGroup')
def getNetworkSmTargetGroup(**kwargs):
    return MerakiClient().getNetworkSmTargetGroup(**kwargs)

@register('getNetworkSmTrustedAccessConfigs')
def getNetworkSmTrustedAccessConfigs(**kwargs):
    return MerakiClient().getNetworkSmTrustedAccessConfigs(**kwargs)

@register('getNetworkSmUserAccessDevices')
def getNetworkSmUserAccessDevices(**kwargs):
    return MerakiClient().getNetworkSmUserAccessDevices(**kwargs)

@register('getNetworkSmUsers')
def getNetworkSmUsers(**kwargs):
    return MerakiClient().getNetworkSmUsers(**kwargs)

@register('getNetworkSmUserDeviceProfiles')
def getNetworkSmUserDeviceProfiles(**kwargs):
    return MerakiClient().getNetworkSmUserDeviceProfiles(**kwargs)

@register('getNetworkSmUserSoftwares')
def getNetworkSmUserSoftwares(**kwargs):
    return MerakiClient().getNetworkSmUserSoftwares(**kwargs)

@register('getNetworkSnmp')
def getNetworkSnmp(**kwargs):
    return MerakiClient().getNetworkSnmp(**kwargs)

@register('getNetworkSplashLoginAttempts')
def getNetworkSplashLoginAttempts(**kwargs):
    return MerakiClient().getNetworkSplashLoginAttempts(**kwargs)

@register('getNetworkSwitchAccessControlLists')
def getNetworkSwitchAccessControlLists(**kwargs):
    return MerakiClient().getNetworkSwitchAccessControlLists(**kwargs)

@register('getNetworkSwitchAccessPolicies')
def getNetworkSwitchAccessPolicies(**kwargs):
    return MerakiClient().getNetworkSwitchAccessPolicies(**kwargs)

@register('getNetworkSwitchAccessPolicy')
def getNetworkSwitchAccessPolicy(**kwargs):
    return MerakiClient().getNetworkSwitchAccessPolicy(**kwargs)

@register('getNetworkSwitchAlternateManagementInterface')
def getNetworkSwitchAlternateManagementInterface(**kwargs):
    return MerakiClient().getNetworkSwitchAlternateManagementInterface(**kwargs)

@register('getNetworkSwitchDhcpV4ServersSeen')
def getNetworkSwitchDhcpV4ServersSeen(**kwargs):
    return MerakiClient().getNetworkSwitchDhcpV4ServersSeen(**kwargs)

@register('getNetworkSwitchDhcpServerPolicy')
def getNetworkSwitchDhcpServerPolicy(**kwargs):
    return MerakiClient().getNetworkSwitchDhcpServerPolicy(**kwargs)

@register('getNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers')
def getNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers(**kwargs):
    return MerakiClient().getNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers(**kwargs)

@register('getNetworkSwitchDhcpServerPolicyArpInspectionWarningsByDevice')
def getNetworkSwitchDhcpServerPolicyArpInspectionWarningsByDevice(**kwargs):
    return MerakiClient().getNetworkSwitchDhcpServerPolicyArpInspectionWarningsByDevice(**kwargs)

@register('getNetworkSwitchDscpToCosMappings')
def getNetworkSwitchDscpToCosMappings(**kwargs):
    return MerakiClient().getNetworkSwitchDscpToCosMappings(**kwargs)

@register('getNetworkSwitchLinkAggregations')
def getNetworkSwitchLinkAggregations(**kwargs):
    return MerakiClient().getNetworkSwitchLinkAggregations(**kwargs)

@register('getNetworkSwitchMtu')
def getNetworkSwitchMtu(**kwargs):
    return MerakiClient().getNetworkSwitchMtu(**kwargs)

@register('getNetworkSwitchPortSchedules')
def getNetworkSwitchPortSchedules(**kwargs):
    return MerakiClient().getNetworkSwitchPortSchedules(**kwargs)

@register('getNetworkSwitchQosRules')
def getNetworkSwitchQosRules(**kwargs):
    return MerakiClient().getNetworkSwitchQosRules(**kwargs)

@register('getNetworkSwitchQosRulesOrder')
def getNetworkSwitchQosRulesOrder(**kwargs):
    return MerakiClient().getNetworkSwitchQosRulesOrder(**kwargs)

@register('getNetworkSwitchQosRule')
def getNetworkSwitchQosRule(**kwargs):
    return MerakiClient().getNetworkSwitchQosRule(**kwargs)

@register('getNetworkSwitchRoutingMulticast')
def getNetworkSwitchRoutingMulticast(**kwargs):
    return MerakiClient().getNetworkSwitchRoutingMulticast(**kwargs)

@register('getNetworkSwitchRoutingMulticastRendezvousPoints')
def getNetworkSwitchRoutingMulticastRendezvousPoints(**kwargs):
    return MerakiClient().getNetworkSwitchRoutingMulticastRendezvousPoints(**kwargs)

@register('getNetworkSwitchRoutingMulticastRendezvousPoint')
def getNetworkSwitchRoutingMulticastRendezvousPoint(**kwargs):
    return MerakiClient().getNetworkSwitchRoutingMulticastRendezvousPoint(**kwargs)

@register('getNetworkSwitchRoutingOspf')
def getNetworkSwitchRoutingOspf(**kwargs):
    return MerakiClient().getNetworkSwitchRoutingOspf(**kwargs)

@register('getNetworkSwitchSettings')
def getNetworkSwitchSettings(**kwargs):
    return MerakiClient().getNetworkSwitchSettings(**kwargs)

@register('getNetworkSwitchStacks')
def getNetworkSwitchStacks(**kwargs):
    return MerakiClient().getNetworkSwitchStacks(**kwargs)

@register('getNetworkSwitchStack')
def getNetworkSwitchStack(**kwargs):
    return MerakiClient().getNetworkSwitchStack(**kwargs)

@register('getNetworkSwitchStackRoutingInterfaces')
def getNetworkSwitchStackRoutingInterfaces(**kwargs):
    return MerakiClient().getNetworkSwitchStackRoutingInterfaces(**kwargs)

@register('getNetworkSwitchStackRoutingInterface')
def getNetworkSwitchStackRoutingInterface(**kwargs):
    return MerakiClient().getNetworkSwitchStackRoutingInterface(**kwargs)

@register('getNetworkSwitchStackRoutingInterfaceDhcp')
def getNetworkSwitchStackRoutingInterfaceDhcp(**kwargs):
    return MerakiClient().getNetworkSwitchStackRoutingInterfaceDhcp(**kwargs)

@register('getNetworkSwitchStackRoutingStaticRoutes')
def getNetworkSwitchStackRoutingStaticRoutes(**kwargs):
    return MerakiClient().getNetworkSwitchStackRoutingStaticRoutes(**kwargs)

@register('getNetworkSwitchStackRoutingStaticRoute')
def getNetworkSwitchStackRoutingStaticRoute(**kwargs):
    return MerakiClient().getNetworkSwitchStackRoutingStaticRoute(**kwargs)

@register('getNetworkSwitchStormControl')
def getNetworkSwitchStormControl(**kwargs):
    return MerakiClient().getNetworkSwitchStormControl(**kwargs)

@register('getNetworkSwitchStp')
def getNetworkSwitchStp(**kwargs):
    return MerakiClient().getNetworkSwitchStp(**kwargs)

@register('getNetworkSyslogServers')
def getNetworkSyslogServers(**kwargs):
    return MerakiClient().getNetworkSyslogServers(**kwargs)

@register('getNetworkTopologyLinkLayer')
def getNetworkTopologyLinkLayer(**kwargs):
    return MerakiClient().getNetworkTopologyLinkLayer(**kwargs)

@register('getNetworkTraffic')
def getNetworkTraffic(**kwargs):
    return MerakiClient().getNetworkTraffic(**kwargs)

@register('getNetworkTrafficAnalysis')
def getNetworkTrafficAnalysis(**kwargs):
    return MerakiClient().getNetworkTrafficAnalysis(**kwargs)

@register('getNetworkTrafficShapingApplicationCategories')
def getNetworkTrafficShapingApplicationCategories(**kwargs):
    return MerakiClient().getNetworkTrafficShapingApplicationCategories(**kwargs)

@register('getNetworkTrafficShapingDscpTaggingOptions')
def getNetworkTrafficShapingDscpTaggingOptions(**kwargs):
    return MerakiClient().getNetworkTrafficShapingDscpTaggingOptions(**kwargs)

@register('getNetworkVlanProfiles')
def getNetworkVlanProfiles(**kwargs):
    return MerakiClient().getNetworkVlanProfiles(**kwargs)

@register('getNetworkVlanProfilesAssignmentsByDevice')
def getNetworkVlanProfilesAssignmentsByDevice(**kwargs):
    return MerakiClient().getNetworkVlanProfilesAssignmentsByDevice(**kwargs)

@register('getNetworkVlanProfile')
def getNetworkVlanProfile(**kwargs):
    return MerakiClient().getNetworkVlanProfile(**kwargs)

@register('getNetworkWebhooksHttpServers')
def getNetworkWebhooksHttpServers(**kwargs):
    return MerakiClient().getNetworkWebhooksHttpServers(**kwargs)

@register('getNetworkWebhooksHttpServer')
def getNetworkWebhooksHttpServer(**kwargs):
    return MerakiClient().getNetworkWebhooksHttpServer(**kwargs)

@register('getNetworkWebhooksPayloadTemplates')
def getNetworkWebhooksPayloadTemplates(**kwargs):
    return MerakiClient().getNetworkWebhooksPayloadTemplates(**kwargs)

@register('getNetworkWebhooksPayloadTemplate')
def getNetworkWebhooksPayloadTemplate(**kwargs):
    return MerakiClient().getNetworkWebhooksPayloadTemplate(**kwargs)

@register('getNetworkWebhooksWebhookTest')
def getNetworkWebhooksWebhookTest(**kwargs):
    return MerakiClient().getNetworkWebhooksWebhookTest(**kwargs)

@register('getNetworkWirelessAirMarshal')
def getNetworkWirelessAirMarshal(**kwargs):
    return MerakiClient().getNetworkWirelessAirMarshal(**kwargs)

@register('getNetworkWirelessAlternateManagementInterface')
def getNetworkWirelessAlternateManagementInterface(**kwargs):
    return MerakiClient().getNetworkWirelessAlternateManagementInterface(**kwargs)

@register('getNetworkWirelessBilling')
def getNetworkWirelessBilling(**kwargs):
    return MerakiClient().getNetworkWirelessBilling(**kwargs)

@register('getNetworkWirelessBluetoothSettings')
def getNetworkWirelessBluetoothSettings(**kwargs):
    return MerakiClient().getNetworkWirelessBluetoothSettings(**kwargs)

@register('getNetworkWirelessChannelUtilizationHistory')
def getNetworkWirelessChannelUtilizationHistory(**kwargs):
    return MerakiClient().getNetworkWirelessChannelUtilizationHistory(**kwargs)

@register('getNetworkWirelessClientCountHistory')
def getNetworkWirelessClientCountHistory(**kwargs):
    return MerakiClient().getNetworkWirelessClientCountHistory(**kwargs)

@register('getNetworkWirelessClientsConnectionStats')
def getNetworkWirelessClientsConnectionStats(**kwargs):
    return MerakiClient().getNetworkWirelessClientsConnectionStats(**kwargs)

@register('getNetworkWirelessClientsLatencyStats')
def getNetworkWirelessClientsLatencyStats(**kwargs):
    return MerakiClient().getNetworkWirelessClientsLatencyStats(**kwargs)

@register('getNetworkWirelessClientConnectionStats')
def getNetworkWirelessClientConnectionStats(**kwargs):
    return MerakiClient().getNetworkWirelessClientConnectionStats(**kwargs)

@register('getNetworkWirelessClientConnectivityEvents')
def getNetworkWirelessClientConnectivityEvents(**kwargs):
    return MerakiClient().getNetworkWirelessClientConnectivityEvents(**kwargs)

@register('getNetworkWirelessClientLatencyHistory')
def getNetworkWirelessClientLatencyHistory(**kwargs):
    return MerakiClient().getNetworkWirelessClientLatencyHistory(**kwargs)

@register('getNetworkWirelessClientLatencyStats')
def getNetworkWirelessClientLatencyStats(**kwargs):
    return MerakiClient().getNetworkWirelessClientLatencyStats(**kwargs)

@register('getNetworkWirelessConnectionStats')
def getNetworkWirelessConnectionStats(**kwargs):
    return MerakiClient().getNetworkWirelessConnectionStats(**kwargs)

@register('getNetworkWirelessDataRateHistory')
def getNetworkWirelessDataRateHistory(**kwargs):
    return MerakiClient().getNetworkWirelessDataRateHistory(**kwargs)

@register('getNetworkWirelessDevicesConnectionStats')
def getNetworkWirelessDevicesConnectionStats(**kwargs):
    return MerakiClient().getNetworkWirelessDevicesConnectionStats(**kwargs)

@register('getNetworkWirelessDevicesLatencyStats')
def getNetworkWirelessDevicesLatencyStats(**kwargs):
    return MerakiClient().getNetworkWirelessDevicesLatencyStats(**kwargs)

@register('getNetworkWirelessElectronicShelfLabel')
def getNetworkWirelessElectronicShelfLabel(**kwargs):
    return MerakiClient().getNetworkWirelessElectronicShelfLabel(**kwargs)

@register('getNetworkWirelessElectronicShelfLabelConfiguredDevices')
def getNetworkWirelessElectronicShelfLabelConfiguredDevices(**kwargs):
    return MerakiClient().getNetworkWirelessElectronicShelfLabelConfiguredDevices(**kwargs)

@register('getNetworkWirelessEthernetPortsProfiles')
def getNetworkWirelessEthernetPortsProfiles(**kwargs):
    return MerakiClient().getNetworkWirelessEthernetPortsProfiles(**kwargs)

@register('getNetworkWirelessEthernetPortsProfile')
def getNetworkWirelessEthernetPortsProfile(**kwargs):
    return MerakiClient().getNetworkWirelessEthernetPortsProfile(**kwargs)

@register('getNetworkWirelessFailedConnections')
def getNetworkWirelessFailedConnections(**kwargs):
    return MerakiClient().getNetworkWirelessFailedConnections(**kwargs)

@register('getNetworkWirelessLatencyHistory')
def getNetworkWirelessLatencyHistory(**kwargs):
    return MerakiClient().getNetworkWirelessLatencyHistory(**kwargs)

@register('getNetworkWirelessLatencyStats')
def getNetworkWirelessLatencyStats(**kwargs):
    return MerakiClient().getNetworkWirelessLatencyStats(**kwargs)

@register('getNetworkWirelessMeshStatuses')
def getNetworkWirelessMeshStatuses(**kwargs):
    return MerakiClient().getNetworkWirelessMeshStatuses(**kwargs)

@register('getNetworkWirelessRfProfiles')
def getNetworkWirelessRfProfiles(**kwargs):
    return MerakiClient().getNetworkWirelessRfProfiles(**kwargs)

@register('getNetworkWirelessRfProfile')
def getNetworkWirelessRfProfile(**kwargs):
    return MerakiClient().getNetworkWirelessRfProfile(**kwargs)

@register('getNetworkWirelessSettings')
def getNetworkWirelessSettings(**kwargs):
    return MerakiClient().getNetworkWirelessSettings(**kwargs)

@register('getNetworkWirelessSignalQualityHistory')
def getNetworkWirelessSignalQualityHistory(**kwargs):
    return MerakiClient().getNetworkWirelessSignalQualityHistory(**kwargs)

@register('getNetworkWirelessSsids')
def getNetworkWirelessSsids(**kwargs):
    return MerakiClient().getNetworkWirelessSsids(**kwargs)

@register('getNetworkWirelessSsid')
def getNetworkWirelessSsid(**kwargs):
    return MerakiClient().getNetworkWirelessSsid(**kwargs)

@register('getNetworkWirelessSsidBonjourForwarding')
def getNetworkWirelessSsidBonjourForwarding(**kwargs):
    return MerakiClient().getNetworkWirelessSsidBonjourForwarding(**kwargs)

@register('getNetworkWirelessSsidDeviceTypeGroupPolicies')
def getNetworkWirelessSsidDeviceTypeGroupPolicies(**kwargs):
    return MerakiClient().getNetworkWirelessSsidDeviceTypeGroupPolicies(**kwargs)

@register('getNetworkWirelessSsidEapOverride')
def getNetworkWirelessSsidEapOverride(**kwargs):
    return MerakiClient().getNetworkWirelessSsidEapOverride(**kwargs)

@register('getNetworkWirelessSsidFirewallL3FirewallRules')
def getNetworkWirelessSsidFirewallL3FirewallRules(**kwargs):
    return MerakiClient().getNetworkWirelessSsidFirewallL3FirewallRules(**kwargs)

@register('getNetworkWirelessSsidFirewallL7FirewallRules')
def getNetworkWirelessSsidFirewallL7FirewallRules(**kwargs):
    return MerakiClient().getNetworkWirelessSsidFirewallL7FirewallRules(**kwargs)

@register('getNetworkWirelessSsidHotspot20')
def getNetworkWirelessSsidHotspot20(**kwargs):
    return MerakiClient().getNetworkWirelessSsidHotspot20(**kwargs)

@register('getNetworkWirelessSsidIdentityPsks')
def getNetworkWirelessSsidIdentityPsks(**kwargs):
    return MerakiClient().getNetworkWirelessSsidIdentityPsks(**kwargs)

@register('getNetworkWirelessSsidIdentityPsk')
def getNetworkWirelessSsidIdentityPsk(**kwargs):
    return MerakiClient().getNetworkWirelessSsidIdentityPsk(**kwargs)

@register('getNetworkWirelessSsidSchedules')
def getNetworkWirelessSsidSchedules(**kwargs):
    return MerakiClient().getNetworkWirelessSsidSchedules(**kwargs)

@register('getNetworkWirelessSsidSplashSettings')
def getNetworkWirelessSsidSplashSettings(**kwargs):
    return MerakiClient().getNetworkWirelessSsidSplashSettings(**kwargs)

@register('getNetworkWirelessSsidTrafficShapingRules')
def getNetworkWirelessSsidTrafficShapingRules(**kwargs):
    return MerakiClient().getNetworkWirelessSsidTrafficShapingRules(**kwargs)

@register('getNetworkWirelessSsidVpn')
def getNetworkWirelessSsidVpn(**kwargs):
    return MerakiClient().getNetworkWirelessSsidVpn(**kwargs)

@register('getNetworkWirelessUsageHistory')
def getNetworkWirelessUsageHistory(**kwargs):
    return MerakiClient().getNetworkWirelessUsageHistory(**kwargs)

@register('getOrganizations')
def getOrganizations(**kwargs):
    return MerakiClient().getOrganizations(**kwargs)

@register('getOrganization')
def getOrganization(**kwargs):
    return MerakiClient().getOrganization(**kwargs)

@register('getOrganizationActionBatches')
def getOrganizationActionBatches(**kwargs):
    return MerakiClient().getOrganizationActionBatches(**kwargs)

@register('getOrganizationActionBatch')
def getOrganizationActionBatch(**kwargs):
    return MerakiClient().getOrganizationActionBatch(**kwargs)

@register('getOrganizationAdaptivePolicyAcls')
def getOrganizationAdaptivePolicyAcls(**kwargs):
    return MerakiClient().getOrganizationAdaptivePolicyAcls(**kwargs)

@register('getOrganizationAdaptivePolicyAcl')
def getOrganizationAdaptivePolicyAcl(**kwargs):
    return MerakiClient().getOrganizationAdaptivePolicyAcl(**kwargs)

@register('getOrganizationAdaptivePolicyGroups')
def getOrganizationAdaptivePolicyGroups(**kwargs):
    return MerakiClient().getOrganizationAdaptivePolicyGroups(**kwargs)

@register('getOrganizationAdaptivePolicyGroup')
def getOrganizationAdaptivePolicyGroup(**kwargs):
    return MerakiClient().getOrganizationAdaptivePolicyGroup(**kwargs)

@register('getOrganizationAdaptivePolicyOverview')
def getOrganizationAdaptivePolicyOverview(**kwargs):
    return MerakiClient().getOrganizationAdaptivePolicyOverview(**kwargs)

@register('getOrganizationAdaptivePolicyPolicies')
def getOrganizationAdaptivePolicyPolicies(**kwargs):
    return MerakiClient().getOrganizationAdaptivePolicyPolicies(**kwargs)

@register('getOrganizationAdaptivePolicyPolicy')
def getOrganizationAdaptivePolicyPolicy(**kwargs):
    return MerakiClient().getOrganizationAdaptivePolicyPolicy(**kwargs)

@register('getOrganizationAdaptivePolicySettings')
def getOrganizationAdaptivePolicySettings(**kwargs):
    return MerakiClient().getOrganizationAdaptivePolicySettings(**kwargs)

@register('getOrganizationAdmins')
def getOrganizationAdmins(**kwargs):
    return MerakiClient().getOrganizationAdmins(**kwargs)

@register('getOrganizationAlertsProfiles')
def getOrganizationAlertsProfiles(**kwargs):
    return MerakiClient().getOrganizationAlertsProfiles(**kwargs)

@register('getOrganizationApiRequests')
def getOrganizationApiRequests(**kwargs):
    return MerakiClient().getOrganizationApiRequests(**kwargs)

@register('getOrganizationApiRequestsOverview')
def getOrganizationApiRequestsOverview(**kwargs):
    return MerakiClient().getOrganizationApiRequestsOverview(**kwargs)

@register('getOrganizationApiRequestsOverviewResponseCodesByInterval')
def getOrganizationApiRequestsOverviewResponseCodesByInterval(**kwargs):
    return MerakiClient().getOrganizationApiRequestsOverviewResponseCodesByInterval(**kwargs)

@register('getOrganizationApplianceSecurityEvents')
def getOrganizationApplianceSecurityEvents(**kwargs):
    return MerakiClient().getOrganizationApplianceSecurityEvents(**kwargs)

@register('getOrganizationApplianceSecurityIntrusion')
def getOrganizationApplianceSecurityIntrusion(**kwargs):
    return MerakiClient().getOrganizationApplianceSecurityIntrusion(**kwargs)

@register('getOrganizationApplianceTrafficShapingVpnExclusionsByNetwork')
def getOrganizationApplianceTrafficShapingVpnExclusionsByNetwork(**kwargs):
    return MerakiClient().getOrganizationApplianceTrafficShapingVpnExclusionsByNetwork(**kwargs)

@register('getOrganizationApplianceUplinkStatuses')
def getOrganizationApplianceUplinkStatuses(**kwargs):
    return MerakiClient().getOrganizationApplianceUplinkStatuses(**kwargs)

@register('getOrganizationApplianceUplinksStatusesOverview')
def getOrganizationApplianceUplinksStatusesOverview(**kwargs):
    return MerakiClient().getOrganizationApplianceUplinksStatusesOverview(**kwargs)

@register('getOrganizationApplianceUplinksUsageByNetwork')
def getOrganizationApplianceUplinksUsageByNetwork(**kwargs):
    return MerakiClient().getOrganizationApplianceUplinksUsageByNetwork(**kwargs)

@register('getOrganizationApplianceVpnStats')
def getOrganizationApplianceVpnStats(**kwargs):
    return MerakiClient().getOrganizationApplianceVpnStats(**kwargs)

@register('getOrganizationApplianceVpnStatuses')
def getOrganizationApplianceVpnStatuses(**kwargs):
    return MerakiClient().getOrganizationApplianceVpnStatuses(**kwargs)

@register('getOrganizationApplianceVpnThirdPartyVPNPeers')
def getOrganizationApplianceVpnThirdPartyVPNPeers(**kwargs):
    return MerakiClient().getOrganizationApplianceVpnThirdPartyVPNPeers(**kwargs)

@register('getOrganizationApplianceVpnVpnFirewallRules')
def getOrganizationApplianceVpnVpnFirewallRules(**kwargs):
    return MerakiClient().getOrganizationApplianceVpnVpnFirewallRules(**kwargs)

@register('getOrganizationAssuranceAlerts')
def getOrganizationAssuranceAlerts(**kwargs):
    return MerakiClient().getOrganizationAssuranceAlerts(**kwargs)

@register('getOrganizationAssuranceAlertsOverview')
def getOrganizationAssuranceAlertsOverview(**kwargs):
    return MerakiClient().getOrganizationAssuranceAlertsOverview(**kwargs)

@register('getOrganizationAssuranceAlertsOverviewByNetwork')
def getOrganizationAssuranceAlertsOverviewByNetwork(**kwargs):
    return MerakiClient().getOrganizationAssuranceAlertsOverviewByNetwork(**kwargs)

@register('getOrganizationAssuranceAlertsOverviewByType')
def getOrganizationAssuranceAlertsOverviewByType(**kwargs):
    return MerakiClient().getOrganizationAssuranceAlertsOverviewByType(**kwargs)

@register('getOrganizationAssuranceAlertsOverviewHistorical')
def getOrganizationAssuranceAlertsOverviewHistorical(**kwargs):
    return MerakiClient().getOrganizationAssuranceAlertsOverviewHistorical(**kwargs)

@register('getOrganizationAssuranceAlert')
def getOrganizationAssuranceAlert(**kwargs):
    return MerakiClient().getOrganizationAssuranceAlert(**kwargs)

@register('getOrganizationBrandingPolicies')
def getOrganizationBrandingPolicies(**kwargs):
    return MerakiClient().getOrganizationBrandingPolicies(**kwargs)

@register('getOrganizationBrandingPoliciesPriorities')
def getOrganizationBrandingPoliciesPriorities(**kwargs):
    return MerakiClient().getOrganizationBrandingPoliciesPriorities(**kwargs)

@register('getOrganizationBrandingPolicy')
def getOrganizationBrandingPolicy(**kwargs):
    return MerakiClient().getOrganizationBrandingPolicy(**kwargs)

@register('getOrganizationCameraBoundariesAreasByDevice')
def getOrganizationCameraBoundariesAreasByDevice(**kwargs):
    return MerakiClient().getOrganizationCameraBoundariesAreasByDevice(**kwargs)

@register('getOrganizationCameraBoundariesLinesByDevice')
def getOrganizationCameraBoundariesLinesByDevice(**kwargs):
    return MerakiClient().getOrganizationCameraBoundariesLinesByDevice(**kwargs)

@register('getOrganizationCameraCustomAnalyticsArtifacts')
def getOrganizationCameraCustomAnalyticsArtifacts(**kwargs):
    return MerakiClient().getOrganizationCameraCustomAnalyticsArtifacts(**kwargs)

@register('getOrganizationCameraCustomAnalyticsArtifact')
def getOrganizationCameraCustomAnalyticsArtifact(**kwargs):
    return MerakiClient().getOrganizationCameraCustomAnalyticsArtifact(**kwargs)

@register('getOrganizationCameraDetectionsHistoryByBoundaryByInterval')
def getOrganizationCameraDetectionsHistoryByBoundaryByInterval(**kwargs):
    return MerakiClient().getOrganizationCameraDetectionsHistoryByBoundaryByInterval(**kwargs)

@register('getOrganizationCameraOnboardingStatuses')
def getOrganizationCameraOnboardingStatuses(**kwargs):
    return MerakiClient().getOrganizationCameraOnboardingStatuses(**kwargs)

@register('getOrganizationCameraPermissions')
def getOrganizationCameraPermissions(**kwargs):
    return MerakiClient().getOrganizationCameraPermissions(**kwargs)

@register('getOrganizationCameraPermission')
def getOrganizationCameraPermission(**kwargs):
    return MerakiClient().getOrganizationCameraPermission(**kwargs)

@register('getOrganizationCameraRoles')
def getOrganizationCameraRoles(**kwargs):
    return MerakiClient().getOrganizationCameraRoles(**kwargs)

@register('getOrganizationCameraRole')
def getOrganizationCameraRole(**kwargs):
    return MerakiClient().getOrganizationCameraRole(**kwargs)

@register('getOrganizationCellularGatewayEsimsInventory')
def getOrganizationCellularGatewayEsimsInventory(**kwargs):
    return MerakiClient().getOrganizationCellularGatewayEsimsInventory(**kwargs)

@register('getOrganizationCellularGatewayEsimsServiceProviders')
def getOrganizationCellularGatewayEsimsServiceProviders(**kwargs):
    return MerakiClient().getOrganizationCellularGatewayEsimsServiceProviders(**kwargs)

@register('getOrganizationCellularGatewayEsimsServiceProvidersAccounts')
def getOrganizationCellularGatewayEsimsServiceProvidersAccounts(**kwargs):
    return MerakiClient().getOrganizationCellularGatewayEsimsServiceProvidersAccounts(**kwargs)

@register('getOrganizationCellularGatewayEsimsServiceProvidersAccountsCommunicationPlans')
def getOrganizationCellularGatewayEsimsServiceProvidersAccountsCommunicationPlans(**kwargs):
    return MerakiClient().getOrganizationCellularGatewayEsimsServiceProvidersAccountsCommunicationPlans(**kwargs)

@register('getOrganizationCellularGatewayEsimsServiceProvidersAccountsRatePlans')
def getOrganizationCellularGatewayEsimsServiceProvidersAccountsRatePlans(**kwargs):
    return MerakiClient().getOrganizationCellularGatewayEsimsServiceProvidersAccountsRatePlans(**kwargs)

@register('getOrganizationCellularGatewayUplinkStatuses')
def getOrganizationCellularGatewayUplinkStatuses(**kwargs):
    return MerakiClient().getOrganizationCellularGatewayUplinkStatuses(**kwargs)

@register('getOrganizationClientsBandwidthUsageHistory')
def getOrganizationClientsBandwidthUsageHistory(**kwargs):
    return MerakiClient().getOrganizationClientsBandwidthUsageHistory(**kwargs)

@register('getOrganizationClientsOverview')
def getOrganizationClientsOverview(**kwargs):
    return MerakiClient().getOrganizationClientsOverview(**kwargs)

@register('getOrganizationClientsSearch')
def getOrganizationClientsSearch(**kwargs):
    return MerakiClient().getOrganizationClientsSearch(**kwargs)

@register('getOrganizationConfigTemplates')
def getOrganizationConfigTemplates(**kwargs):
    return MerakiClient().getOrganizationConfigTemplates(**kwargs)

@register('getOrganizationConfigTemplate')
def getOrganizationConfigTemplate(**kwargs):
    return MerakiClient().getOrganizationConfigTemplate(**kwargs)

@register('getOrganizationConfigTemplateSwitchProfiles')
def getOrganizationConfigTemplateSwitchProfiles(**kwargs):
    return MerakiClient().getOrganizationConfigTemplateSwitchProfiles(**kwargs)

@register('getOrganizationConfigTemplateSwitchProfilePorts')
def getOrganizationConfigTemplateSwitchProfilePorts(**kwargs):
    return MerakiClient().getOrganizationConfigTemplateSwitchProfilePorts(**kwargs)

@register('getOrganizationConfigTemplateSwitchProfilePort')
def getOrganizationConfigTemplateSwitchProfilePort(**kwargs):
    return MerakiClient().getOrganizationConfigTemplateSwitchProfilePort(**kwargs)

@register('getOrganizationConfigurationChanges')
def getOrganizationConfigurationChanges(**kwargs):
    return MerakiClient().getOrganizationConfigurationChanges(**kwargs)

@register('getOrganizationDevices')
def getOrganizationDevices(**kwargs):
    return MerakiClient().getOrganizationDevices(**kwargs)

@register('getOrganizationDevicesAvailabilities')
def getOrganizationDevicesAvailabilities(**kwargs):
    return MerakiClient().getOrganizationDevicesAvailabilities(**kwargs)

@register('getOrganizationDevicesAvailabilitiesChangeHistory')
def getOrganizationDevicesAvailabilitiesChangeHistory(**kwargs):
    return MerakiClient().getOrganizationDevicesAvailabilitiesChangeHistory(**kwargs)

@register('getOrganizationDevicesOverviewByModel')
def getOrganizationDevicesOverviewByModel(**kwargs):
    return MerakiClient().getOrganizationDevicesOverviewByModel(**kwargs)

@register('getOrganizationDevicesPowerModulesStatusesByDevice')
def getOrganizationDevicesPowerModulesStatusesByDevice(**kwargs):
    return MerakiClient().getOrganizationDevicesPowerModulesStatusesByDevice(**kwargs)

@register('getOrganizationDevicesProvisioningStatuses')
def getOrganizationDevicesProvisioningStatuses(**kwargs):
    return MerakiClient().getOrganizationDevicesProvisioningStatuses(**kwargs)

@register('getOrganizationDevicesStatuses')
def getOrganizationDevicesStatuses(**kwargs):
    return MerakiClient().getOrganizationDevicesStatuses(**kwargs)

@register('getOrganizationDevicesStatusesOverview')
def getOrganizationDevicesStatusesOverview(**kwargs):
    return MerakiClient().getOrganizationDevicesStatusesOverview(**kwargs)

@register('getOrganizationDevicesUplinksAddressesByDevice')
def getOrganizationDevicesUplinksAddressesByDevice(**kwargs):
    return MerakiClient().getOrganizationDevicesUplinksAddressesByDevice(**kwargs)

@register('getOrganizationDevicesUplinksLossAndLatency')
def getOrganizationDevicesUplinksLossAndLatency(**kwargs):
    return MerakiClient().getOrganizationDevicesUplinksLossAndLatency(**kwargs)

@register('getOrganizationEarlyAccessFeatures')
def getOrganizationEarlyAccessFeatures(**kwargs):
    return MerakiClient().getOrganizationEarlyAccessFeatures(**kwargs)

@register('getOrganizationEarlyAccessFeaturesOptIns')
def getOrganizationEarlyAccessFeaturesOptIns(**kwargs):
    return MerakiClient().getOrganizationEarlyAccessFeaturesOptIns(**kwargs)

@register('getOrganizationEarlyAccessFeaturesOptIn')
def getOrganizationEarlyAccessFeaturesOptIn(**kwargs):
    return MerakiClient().getOrganizationEarlyAccessFeaturesOptIn(**kwargs)

@register('getOrganizationFirmwareUpgrades')
def getOrganizationFirmwareUpgrades(**kwargs):
    return MerakiClient().getOrganizationFirmwareUpgrades(**kwargs)

@register('getOrganizationFirmwareUpgradesByDevice')
def getOrganizationFirmwareUpgradesByDevice(**kwargs):
    return MerakiClient().getOrganizationFirmwareUpgradesByDevice(**kwargs)

@register('getOrganizationFloorPlansAutoLocateDevices')
def getOrganizationFloorPlansAutoLocateDevices(**kwargs):
    return MerakiClient().getOrganizationFloorPlansAutoLocateDevices(**kwargs)

@register('getOrganizationFloorPlansAutoLocateStatuses')
def getOrganizationFloorPlansAutoLocateStatuses(**kwargs):
    return MerakiClient().getOrganizationFloorPlansAutoLocateStatuses(**kwargs)

@register('getOrganizationInsightApplications')
def getOrganizationInsightApplications(**kwargs):
    return MerakiClient().getOrganizationInsightApplications(**kwargs)

@register('getOrganizationInsightMonitoredMediaServers')
def getOrganizationInsightMonitoredMediaServers(**kwargs):
    return MerakiClient().getOrganizationInsightMonitoredMediaServers(**kwargs)

@register('getOrganizationInsightMonitoredMediaServer')
def getOrganizationInsightMonitoredMediaServer(**kwargs):
    return MerakiClient().getOrganizationInsightMonitoredMediaServer(**kwargs)

@register('getOrganizationInventoryDevices')
def getOrganizationInventoryDevices(**kwargs):
    return MerakiClient().getOrganizationInventoryDevices(**kwargs)

@register('getOrganizationInventoryDevicesSwapsBulk')
def getOrganizationInventoryDevicesSwapsBulk(**kwargs):
    return MerakiClient().getOrganizationInventoryDevicesSwapsBulk(**kwargs)

@register('getOrganizationInventoryDevice')
def getOrganizationInventoryDevice(**kwargs):
    return MerakiClient().getOrganizationInventoryDevice(**kwargs)

@register('getOrganizationInventoryOnboardingCloudMonitoringImports')
def getOrganizationInventoryOnboardingCloudMonitoringImports(**kwargs):
    return MerakiClient().getOrganizationInventoryOnboardingCloudMonitoringImports(**kwargs)

@register('getOrganizationInventoryOnboardingCloudMonitoringNetworks')
def getOrganizationInventoryOnboardingCloudMonitoringNetworks(**kwargs):
    return MerakiClient().getOrganizationInventoryOnboardingCloudMonitoringNetworks(**kwargs)

@register('getOrganizationLicenses')
def getOrganizationLicenses(**kwargs):
    return MerakiClient().getOrganizationLicenses(**kwargs)

@register('getOrganizationLicensesOverview')
def getOrganizationLicensesOverview(**kwargs):
    return MerakiClient().getOrganizationLicensesOverview(**kwargs)

@register('getOrganizationLicense')
def getOrganizationLicense(**kwargs):
    return MerakiClient().getOrganizationLicense(**kwargs)

@register('getOrganizationLicensingCotermLicenses')
def getOrganizationLicensingCotermLicenses(**kwargs):
    return MerakiClient().getOrganizationLicensingCotermLicenses(**kwargs)

@register('getOrganizationLoginSecurity')
def getOrganizationLoginSecurity(**kwargs):
    return MerakiClient().getOrganizationLoginSecurity(**kwargs)

@register('getOrganizationNetworks')
def getOrganizationNetworks(**kwargs):
    return MerakiClient().getOrganizationNetworks(**kwargs)

@register('getOrganizationOpenapiSpec')
def getOrganizationOpenapiSpec(**kwargs):
    return MerakiClient().getOrganizationOpenapiSpec(**kwargs)

@register('getOrganizationPolicyObjects')
def getOrganizationPolicyObjects(**kwargs):
    return MerakiClient().getOrganizationPolicyObjects(**kwargs)

@register('getOrganizationPolicyObjectsGroups')
def getOrganizationPolicyObjectsGroups(**kwargs):
    return MerakiClient().getOrganizationPolicyObjectsGroups(**kwargs)

@register('getOrganizationPolicyObjectsGroup')
def getOrganizationPolicyObjectsGroup(**kwargs):
    return MerakiClient().getOrganizationPolicyObjectsGroup(**kwargs)

@register('getOrganizationPolicyObject')
def getOrganizationPolicyObject(**kwargs):
    return MerakiClient().getOrganizationPolicyObject(**kwargs)

@register('getOrganizationSaml')
def getOrganizationSaml(**kwargs):
    return MerakiClient().getOrganizationSaml(**kwargs)

@register('getOrganizationSamlIdps')
def getOrganizationSamlIdps(**kwargs):
    return MerakiClient().getOrganizationSamlIdps(**kwargs)

@register('getOrganizationSamlIdp')
def getOrganizationSamlIdp(**kwargs):
    return MerakiClient().getOrganizationSamlIdp(**kwargs)

@register('getOrganizationSamlRoles')
def getOrganizationSamlRoles(**kwargs):
    return MerakiClient().getOrganizationSamlRoles(**kwargs)

@register('getOrganizationSamlRole')
def getOrganizationSamlRole(**kwargs):
    return MerakiClient().getOrganizationSamlRole(**kwargs)

@register('getOrganizationSensorReadingsHistory')
def getOrganizationSensorReadingsHistory(**kwargs):
    return MerakiClient().getOrganizationSensorReadingsHistory(**kwargs)

@register('getOrganizationSensorReadingsLatest')
def getOrganizationSensorReadingsLatest(**kwargs):
    return MerakiClient().getOrganizationSensorReadingsLatest(**kwargs)

@register('getOrganizationSmAdminsRoles')
def getOrganizationSmAdminsRoles(**kwargs):
    return MerakiClient().getOrganizationSmAdminsRoles(**kwargs)

@register('getOrganizationSmAdminsRole')
def getOrganizationSmAdminsRole(**kwargs):
    return MerakiClient().getOrganizationSmAdminsRole(**kwargs)

@register('getOrganizationSmApnsCert')
def getOrganizationSmApnsCert(**kwargs):
    return MerakiClient().getOrganizationSmApnsCert(**kwargs)

@register('getOrganizationSmSentryPoliciesAssignmentsByNetwork')
def getOrganizationSmSentryPoliciesAssignmentsByNetwork(**kwargs):
    return MerakiClient().getOrganizationSmSentryPoliciesAssignmentsByNetwork(**kwargs)

@register('getOrganizationSmVppAccounts')
def getOrganizationSmVppAccounts(**kwargs):
    return MerakiClient().getOrganizationSmVppAccounts(**kwargs)

@register('getOrganizationSmVppAccount')
def getOrganizationSmVppAccount(**kwargs):
    return MerakiClient().getOrganizationSmVppAccount(**kwargs)

@register('getOrganizationSnmp')
def getOrganizationSnmp(**kwargs):
    return MerakiClient().getOrganizationSnmp(**kwargs)

@register('getOrganizationSplashAsset')
def getOrganizationSplashAsset(**kwargs):
    return MerakiClient().getOrganizationSplashAsset(**kwargs)

@register('getOrganizationSplashThemes')
def getOrganizationSplashThemes(**kwargs):
    return MerakiClient().getOrganizationSplashThemes(**kwargs)

@register('getOrganizationSummarySwitchPowerHistory')
def getOrganizationSummarySwitchPowerHistory(**kwargs):
    return MerakiClient().getOrganizationSummarySwitchPowerHistory(**kwargs)

@register('getOrganizationSummaryTopAppliancesByUtilization')
def getOrganizationSummaryTopAppliancesByUtilization(**kwargs):
    return MerakiClient().getOrganizationSummaryTopAppliancesByUtilization(**kwargs)

@register('getOrganizationSummaryTopApplicationsByUsage')
def getOrganizationSummaryTopApplicationsByUsage(**kwargs):
    return MerakiClient().getOrganizationSummaryTopApplicationsByUsage(**kwargs)

@register('getOrganizationSummaryTopApplicationsCategoriesByUsage')
def getOrganizationSummaryTopApplicationsCategoriesByUsage(**kwargs):
    return MerakiClient().getOrganizationSummaryTopApplicationsCategoriesByUsage(**kwargs)

@register('getOrganizationSummaryTopClientsByUsage')
def getOrganizationSummaryTopClientsByUsage(**kwargs):
    return MerakiClient().getOrganizationSummaryTopClientsByUsage(**kwargs)

@register('getOrganizationSummaryTopClientsManufacturersByUsage')
def getOrganizationSummaryTopClientsManufacturersByUsage(**kwargs):
    return MerakiClient().getOrganizationSummaryTopClientsManufacturersByUsage(**kwargs)

@register('getOrganizationSummaryTopDevicesByUsage')
def getOrganizationSummaryTopDevicesByUsage(**kwargs):
    return MerakiClient().getOrganizationSummaryTopDevicesByUsage(**kwargs)

@register('getOrganizationSummaryTopDevicesModelsByUsage')
def getOrganizationSummaryTopDevicesModelsByUsage(**kwargs):
    return MerakiClient().getOrganizationSummaryTopDevicesModelsByUsage(**kwargs)

@register('getOrganizationSummaryTopNetworksByStatus')
def getOrganizationSummaryTopNetworksByStatus(**kwargs):
    return MerakiClient().getOrganizationSummaryTopNetworksByStatus(**kwargs)

@register('getOrganizationSummaryTopSsidsByUsage')
def getOrganizationSummaryTopSsidsByUsage(**kwargs):
    return MerakiClient().getOrganizationSummaryTopSsidsByUsage(**kwargs)

@register('getOrganizationSummaryTopSwitchesByEnergyUsage')
def getOrganizationSummaryTopSwitchesByEnergyUsage(**kwargs):
    return MerakiClient().getOrganizationSummaryTopSwitchesByEnergyUsage(**kwargs)

@register('getOrganizationSwitchPortsBySwitch')
def getOrganizationSwitchPortsBySwitch(**kwargs):
    return MerakiClient().getOrganizationSwitchPortsBySwitch(**kwargs)

@register('getOrganizationSwitchPortsClientsOverviewByDevice')
def getOrganizationSwitchPortsClientsOverviewByDevice(**kwargs):
    return MerakiClient().getOrganizationSwitchPortsClientsOverviewByDevice(**kwargs)

@register('getOrganizationSwitchPortsOverview')
def getOrganizationSwitchPortsOverview(**kwargs):
    return MerakiClient().getOrganizationSwitchPortsOverview(**kwargs)

@register('getOrganizationSwitchPortsStatusesBySwitch')
def getOrganizationSwitchPortsStatusesBySwitch(**kwargs):
    return MerakiClient().getOrganizationSwitchPortsStatusesBySwitch(**kwargs)

@register('getOrganizationSwitchPortsTopologyDiscoveryByDevice')
def getOrganizationSwitchPortsTopologyDiscoveryByDevice(**kwargs):
    return MerakiClient().getOrganizationSwitchPortsTopologyDiscoveryByDevice(**kwargs)

@register('getOrganizationUplinksStatuses')
def getOrganizationUplinksStatuses(**kwargs):
    return MerakiClient().getOrganizationUplinksStatuses(**kwargs)

@register('getOrganizationWebhooksAlertTypes')
def getOrganizationWebhooksAlertTypes(**kwargs):
    return MerakiClient().getOrganizationWebhooksAlertTypes(**kwargs)

@register('getOrganizationWebhooksCallbacksStatus')
def getOrganizationWebhooksCallbacksStatus(**kwargs):
    return MerakiClient().getOrganizationWebhooksCallbacksStatus(**kwargs)

@register('getOrganizationWebhooksLogs')
def getOrganizationWebhooksLogs(**kwargs):
    return MerakiClient().getOrganizationWebhooksLogs(**kwargs)

@register('getOrganizationWirelessAirMarshalRules')
def getOrganizationWirelessAirMarshalRules(**kwargs):
    return MerakiClient().getOrganizationWirelessAirMarshalRules(**kwargs)

@register('getOrganizationWirelessAirMarshalSettingsByNetwork')
def getOrganizationWirelessAirMarshalSettingsByNetwork(**kwargs):
    return MerakiClient().getOrganizationWirelessAirMarshalSettingsByNetwork(**kwargs)

@register('getOrganizationWirelessClientsOverviewByDevice')
def getOrganizationWirelessClientsOverviewByDevice(**kwargs):
    return MerakiClient().getOrganizationWirelessClientsOverviewByDevice(**kwargs)

@register('getOrganizationWirelessDevicesChannelUtilizationByDevice')
def getOrganizationWirelessDevicesChannelUtilizationByDevice(**kwargs):
    return MerakiClient().getOrganizationWirelessDevicesChannelUtilizationByDevice(**kwargs)

@register('getOrganizationWirelessDevicesChannelUtilizationByNetwork')
def getOrganizationWirelessDevicesChannelUtilizationByNetwork(**kwargs):
    return MerakiClient().getOrganizationWirelessDevicesChannelUtilizationByNetwork(**kwargs)

@register('getOrganizationWirelessDevicesChannelUtilizationHistoryByDeviceByInterval')
def getOrganizationWirelessDevicesChannelUtilizationHistoryByDeviceByInterval(**kwargs):
    return MerakiClient().getOrganizationWirelessDevicesChannelUtilizationHistoryByDeviceByInterval(**kwargs)

@register('getOrganizationWirelessDevicesChannelUtilizationHistoryByNetworkByInterval')
def getOrganizationWirelessDevicesChannelUtilizationHistoryByNetworkByInterval(**kwargs):
    return MerakiClient().getOrganizationWirelessDevicesChannelUtilizationHistoryByNetworkByInterval(**kwargs)

@register('getOrganizationWirelessDevicesEthernetStatuses')
def getOrganizationWirelessDevicesEthernetStatuses(**kwargs):
    return MerakiClient().getOrganizationWirelessDevicesEthernetStatuses(**kwargs)

@register('getOrganizationWirelessDevicesPacketLossByClient')
def getOrganizationWirelessDevicesPacketLossByClient(**kwargs):
    return MerakiClient().getOrganizationWirelessDevicesPacketLossByClient(**kwargs)

@register('getOrganizationWirelessDevicesPacketLossByDevice')
def getOrganizationWirelessDevicesPacketLossByDevice(**kwargs):
    return MerakiClient().getOrganizationWirelessDevicesPacketLossByDevice(**kwargs)

@register('getOrganizationWirelessDevicesPacketLossByNetwork')
def getOrganizationWirelessDevicesPacketLossByNetwork(**kwargs):
    return MerakiClient().getOrganizationWirelessDevicesPacketLossByNetwork(**kwargs)

@register('getOrganizationWirelessDevicesWirelessControllersByDevice')
def getOrganizationWirelessDevicesWirelessControllersByDevice(**kwargs):
    return MerakiClient().getOrganizationWirelessDevicesWirelessControllersByDevice(**kwargs)

@register('getOrganizationWirelessRfProfilesAssignmentsByDevice')
def getOrganizationWirelessRfProfilesAssignmentsByDevice(**kwargs):
    return MerakiClient().getOrganizationWirelessRfProfilesAssignmentsByDevice(**kwargs)

@register('getOrganizationWirelessSsidsStatusesByDevice')
def getOrganizationWirelessSsidsStatusesByDevice(**kwargs):
    return MerakiClient().getOrganizationWirelessSsidsStatusesByDevice(**kwargs)

@register('getOrganizationWirelessControllerAvailabilitiesChangeHistory')
def getOrganizationWirelessControllerAvailabilitiesChangeHistory(**kwargs):
    return MerakiClient().getOrganizationWirelessControllerAvailabilitiesChangeHistory(**kwargs)

@register('getOrganizationWirelessControllerClientsOverviewHistoryByDeviceByInterval')
def getOrganizationWirelessControllerClientsOverviewHistoryByDeviceByInterval(**kwargs):
    return MerakiClient().getOrganizationWirelessControllerClientsOverviewHistoryByDeviceByInterval(**kwargs)

@register('getOrganizationWirelessControllerConnections')
def getOrganizationWirelessControllerConnections(**kwargs):
    return MerakiClient().getOrganizationWirelessControllerConnections(**kwargs)

@register('getOrganizationWirelessControllerDevicesInterfacesL2ByDevice')
def getOrganizationWirelessControllerDevicesInterfacesL2ByDevice(**kwargs):
    return MerakiClient().getOrganizationWirelessControllerDevicesInterfacesL2ByDevice(**kwargs)

@register('getOrganizationWirelessControllerDevicesInterfacesL2StatusesChangeHistoryByDevice')
def getOrganizationWirelessControllerDevicesInterfacesL2StatusesChangeHistoryByDevice(**kwargs):
    return MerakiClient().getOrganizationWirelessControllerDevicesInterfacesL2StatusesChangeHistoryByDevice(**kwargs)

@register('getOrganizationWirelessControllerDevicesInterfacesL2UsageHistoryByInterval')
def getOrganizationWirelessControllerDevicesInterfacesL2UsageHistoryByInterval(**kwargs):
    return MerakiClient().getOrganizationWirelessControllerDevicesInterfacesL2UsageHistoryByInterval(**kwargs)

@register('getOrganizationWirelessControllerDevicesInterfacesL3ByDevice')
def getOrganizationWirelessControllerDevicesInterfacesL3ByDevice(**kwargs):
    return MerakiClient().getOrganizationWirelessControllerDevicesInterfacesL3ByDevice(**kwargs)

@register('getOrganizationWirelessControllerDevicesInterfacesL3StatusesChangeHistoryByDevice')
def getOrganizationWirelessControllerDevicesInterfacesL3StatusesChangeHistoryByDevice(**kwargs):
    return MerakiClient().getOrganizationWirelessControllerDevicesInterfacesL3StatusesChangeHistoryByDevice(**kwargs)

@register('getOrganizationWirelessControllerDevicesInterfacesL3UsageHistoryByInterval')
def getOrganizationWirelessControllerDevicesInterfacesL3UsageHistoryByInterval(**kwargs):
    return MerakiClient().getOrganizationWirelessControllerDevicesInterfacesL3UsageHistoryByInterval(**kwargs)

@register('getOrganizationWirelessControllerDevicesInterfacesPacketsOverviewByDevice')
def getOrganizationWirelessControllerDevicesInterfacesPacketsOverviewByDevice(**kwargs):
    return MerakiClient().getOrganizationWirelessControllerDevicesInterfacesPacketsOverviewByDevice(**kwargs)

@register('getOrganizationWirelessControllerDevicesInterfacesUsageHistoryByInterval')
def getOrganizationWirelessControllerDevicesInterfacesUsageHistoryByInterval(**kwargs):
    return MerakiClient().getOrganizationWirelessControllerDevicesInterfacesUsageHistoryByInterval(**kwargs)

@register('getOrganizationWirelessControllerDevicesRedundancyFailoverHistory')
def getOrganizationWirelessControllerDevicesRedundancyFailoverHistory(**kwargs):
    return MerakiClient().getOrganizationWirelessControllerDevicesRedundancyFailoverHistory(**kwargs)

@register('getOrganizationWirelessControllerDevicesRedundancyStatuses')
def getOrganizationWirelessControllerDevicesRedundancyStatuses(**kwargs):
    return MerakiClient().getOrganizationWirelessControllerDevicesRedundancyStatuses(**kwargs)

@register('getOrganizationWirelessControllerDevicesSystemUtilizationHistoryByInterval')
def getOrganizationWirelessControllerDevicesSystemUtilizationHistoryByInterval(**kwargs):
    return MerakiClient().getOrganizationWirelessControllerDevicesSystemUtilizationHistoryByInterval(**kwargs)

@register('getOrganizationWirelessControllerOverviewByDevice')
def getOrganizationWirelessControllerOverviewByDevice(**kwargs):
    return MerakiClient().getOrganizationWirelessControllerOverviewByDevice(**kwargs)
