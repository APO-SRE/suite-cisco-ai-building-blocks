# app/llm/function_dispatcher/meraki_dispatcher.py
from app.llm.function_dispatcher import register
from app.llm.platform_clients.meraki_client import MerakiClient

@register('getAdministeredIdentitiesMe')
def getAdministeredIdentitiesMe(**kwargs):
    return MerakiClient().getAdministeredIdentitiesMe(**kwargs)

@register('getAdministeredIdentitiesMeApiKeys')
def getAdministeredIdentitiesMeApiKeys(**kwargs):
    return MerakiClient().getAdministeredIdentitiesMeApiKeys(**kwargs)

@register('generateAdministeredIdentitiesMeApiKeys')
def generateAdministeredIdentitiesMeApiKeys(**kwargs):
    return MerakiClient().generateAdministeredIdentitiesMeApiKeys(**kwargs)

@register('revokeAdministeredIdentitiesMeApiKeys')
def revokeAdministeredIdentitiesMeApiKeys(**kwargs):
    return MerakiClient().revokeAdministeredIdentitiesMeApiKeys(**kwargs)

@register('getAdministeredLicensingSubscriptionEntitlements')
def getAdministeredLicensingSubscriptionEntitlements(**kwargs):
    return MerakiClient().getAdministeredLicensingSubscriptionEntitlements(**kwargs)

@register('getAdministeredLicensingSubscriptionSubscriptions')
def getAdministeredLicensingSubscriptionSubscriptions(**kwargs):
    return MerakiClient().getAdministeredLicensingSubscriptionSubscriptions(**kwargs)

@register('claimAdministeredLicensingSubscriptionSubscriptions')
def claimAdministeredLicensingSubscriptionSubscriptions(**kwargs):
    return MerakiClient().claimAdministeredLicensingSubscriptionSubscriptions(**kwargs)

@register('validateAdministeredLicensingSubscriptionSubscriptionsClaimKey')
def validateAdministeredLicensingSubscriptionSubscriptionsClaimKey(**kwargs):
    return MerakiClient().validateAdministeredLicensingSubscriptionSubscriptionsClaimKey(**kwargs)

@register('getAdministeredLicensingSubscriptionSubscriptionsComplianceStatuses')
def getAdministeredLicensingSubscriptionSubscriptionsComplianceStatuses(**kwargs):
    return MerakiClient().getAdministeredLicensingSubscriptionSubscriptionsComplianceStatuses(**kwargs)

@register('bindAdministeredLicensingSubscriptionSubscription')
def bindAdministeredLicensingSubscriptionSubscription(**kwargs):
    return MerakiClient().bindAdministeredLicensingSubscriptionSubscription(**kwargs)

@register('getDevice')
def getDevice(**kwargs):
    return MerakiClient().getDevice(**kwargs)

@register('updateDevice')
def updateDevice(**kwargs):
    return MerakiClient().updateDevice(**kwargs)

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

@register('updateDeviceApplianceRadioSettings')
def updateDeviceApplianceRadioSettings(**kwargs):
    return MerakiClient().updateDeviceApplianceRadioSettings(**kwargs)

@register('getDeviceApplianceUplinksSettings')
def getDeviceApplianceUplinksSettings(**kwargs):
    return MerakiClient().getDeviceApplianceUplinksSettings(**kwargs)

@register('updateDeviceApplianceUplinksSettings')
def updateDeviceApplianceUplinksSettings(**kwargs):
    return MerakiClient().updateDeviceApplianceUplinksSettings(**kwargs)

@register('createDeviceApplianceVmxAuthenticationToken')
def createDeviceApplianceVmxAuthenticationToken(**kwargs):
    return MerakiClient().createDeviceApplianceVmxAuthenticationToken(**kwargs)

@register('blinkDeviceLeds')
def blinkDeviceLeds(**kwargs):
    return MerakiClient().blinkDeviceLeds(**kwargs)

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

@register('updateDeviceCameraCustomAnalytics')
def updateDeviceCameraCustomAnalytics(**kwargs):
    return MerakiClient().updateDeviceCameraCustomAnalytics(**kwargs)

@register('generateDeviceCameraSnapshot')
def generateDeviceCameraSnapshot(**kwargs):
    return MerakiClient().generateDeviceCameraSnapshot(**kwargs)

@register('getDeviceCameraQualityAndRetention')
def getDeviceCameraQualityAndRetention(**kwargs):
    return MerakiClient().getDeviceCameraQualityAndRetention(**kwargs)

@register('updateDeviceCameraQualityAndRetention')
def updateDeviceCameraQualityAndRetention(**kwargs):
    return MerakiClient().updateDeviceCameraQualityAndRetention(**kwargs)

@register('getDeviceCameraSense')
def getDeviceCameraSense(**kwargs):
    return MerakiClient().getDeviceCameraSense(**kwargs)

@register('updateDeviceCameraSense')
def updateDeviceCameraSense(**kwargs):
    return MerakiClient().updateDeviceCameraSense(**kwargs)

@register('getDeviceCameraSenseObjectDetectionModels')
def getDeviceCameraSenseObjectDetectionModels(**kwargs):
    return MerakiClient().getDeviceCameraSenseObjectDetectionModels(**kwargs)

@register('getDeviceCameraVideoSettings')
def getDeviceCameraVideoSettings(**kwargs):
    return MerakiClient().getDeviceCameraVideoSettings(**kwargs)

@register('updateDeviceCameraVideoSettings')
def updateDeviceCameraVideoSettings(**kwargs):
    return MerakiClient().updateDeviceCameraVideoSettings(**kwargs)

@register('getDeviceCameraVideoLink')
def getDeviceCameraVideoLink(**kwargs):
    return MerakiClient().getDeviceCameraVideoLink(**kwargs)

@register('getDeviceCameraWirelessProfiles')
def getDeviceCameraWirelessProfiles(**kwargs):
    return MerakiClient().getDeviceCameraWirelessProfiles(**kwargs)

@register('updateDeviceCameraWirelessProfiles')
def updateDeviceCameraWirelessProfiles(**kwargs):
    return MerakiClient().updateDeviceCameraWirelessProfiles(**kwargs)

@register('getDeviceCellularSims')
def getDeviceCellularSims(**kwargs):
    return MerakiClient().getDeviceCellularSims(**kwargs)

@register('updateDeviceCellularSims')
def updateDeviceCellularSims(**kwargs):
    return MerakiClient().updateDeviceCellularSims(**kwargs)

@register('getDeviceCellularGatewayLan')
def getDeviceCellularGatewayLan(**kwargs):
    return MerakiClient().getDeviceCellularGatewayLan(**kwargs)

@register('updateDeviceCellularGatewayLan')
def updateDeviceCellularGatewayLan(**kwargs):
    return MerakiClient().updateDeviceCellularGatewayLan(**kwargs)

@register('getDeviceCellularGatewayPortForwardingRules')
def getDeviceCellularGatewayPortForwardingRules(**kwargs):
    return MerakiClient().getDeviceCellularGatewayPortForwardingRules(**kwargs)

@register('updateDeviceCellularGatewayPortForwardingRules')
def updateDeviceCellularGatewayPortForwardingRules(**kwargs):
    return MerakiClient().updateDeviceCellularGatewayPortForwardingRules(**kwargs)

@register('getDeviceClients')
def getDeviceClients(**kwargs):
    return MerakiClient().getDeviceClients(**kwargs)

@register('createDeviceLiveToolsArpTable')
def createDeviceLiveToolsArpTable(**kwargs):
    return MerakiClient().createDeviceLiveToolsArpTable(**kwargs)

@register('getDeviceLiveToolsArpTable')
def getDeviceLiveToolsArpTable(**kwargs):
    return MerakiClient().getDeviceLiveToolsArpTable(**kwargs)

@register('createDeviceLiveToolsCableTest')
def createDeviceLiveToolsCableTest(**kwargs):
    return MerakiClient().createDeviceLiveToolsCableTest(**kwargs)

@register('getDeviceLiveToolsCableTest')
def getDeviceLiveToolsCableTest(**kwargs):
    return MerakiClient().getDeviceLiveToolsCableTest(**kwargs)

@register('createDeviceLiveToolsLedsBlink')
def createDeviceLiveToolsLedsBlink(**kwargs):
    return MerakiClient().createDeviceLiveToolsLedsBlink(**kwargs)

@register('getDeviceLiveToolsLedsBlink')
def getDeviceLiveToolsLedsBlink(**kwargs):
    return MerakiClient().getDeviceLiveToolsLedsBlink(**kwargs)

@register('createDeviceLiveToolsMacTable')
def createDeviceLiveToolsMacTable(**kwargs):
    return MerakiClient().createDeviceLiveToolsMacTable(**kwargs)

@register('getDeviceLiveToolsMacTable')
def getDeviceLiveToolsMacTable(**kwargs):
    return MerakiClient().getDeviceLiveToolsMacTable(**kwargs)

@register('createDeviceLiveToolsPing')
def createDeviceLiveToolsPing(**kwargs):
    return MerakiClient().createDeviceLiveToolsPing(**kwargs)

@register('getDeviceLiveToolsPing')
def getDeviceLiveToolsPing(**kwargs):
    return MerakiClient().getDeviceLiveToolsPing(**kwargs)

@register('createDeviceLiveToolsPingDevice')
def createDeviceLiveToolsPingDevice(**kwargs):
    return MerakiClient().createDeviceLiveToolsPingDevice(**kwargs)

@register('getDeviceLiveToolsPingDevice')
def getDeviceLiveToolsPingDevice(**kwargs):
    return MerakiClient().getDeviceLiveToolsPingDevice(**kwargs)

@register('createDeviceLiveToolsThroughputTest')
def createDeviceLiveToolsThroughputTest(**kwargs):
    return MerakiClient().createDeviceLiveToolsThroughputTest(**kwargs)

@register('getDeviceLiveToolsThroughputTest')
def getDeviceLiveToolsThroughputTest(**kwargs):
    return MerakiClient().getDeviceLiveToolsThroughputTest(**kwargs)

@register('createDeviceLiveToolsWakeOnLan')
def createDeviceLiveToolsWakeOnLan(**kwargs):
    return MerakiClient().createDeviceLiveToolsWakeOnLan(**kwargs)

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

@register('updateDeviceManagementInterface')
def updateDeviceManagementInterface(**kwargs):
    return MerakiClient().updateDeviceManagementInterface(**kwargs)

@register('rebootDevice')
def rebootDevice(**kwargs):
    return MerakiClient().rebootDevice(**kwargs)

@register('getDeviceSensorCommands')
def getDeviceSensorCommands(**kwargs):
    return MerakiClient().getDeviceSensorCommands(**kwargs)

@register('createDeviceSensorCommand')
def createDeviceSensorCommand(**kwargs):
    return MerakiClient().createDeviceSensorCommand(**kwargs)

@register('getDeviceSensorCommand')
def getDeviceSensorCommand(**kwargs):
    return MerakiClient().getDeviceSensorCommand(**kwargs)

@register('getDeviceSensorRelationships')
def getDeviceSensorRelationships(**kwargs):
    return MerakiClient().getDeviceSensorRelationships(**kwargs)

@register('updateDeviceSensorRelationships')
def updateDeviceSensorRelationships(**kwargs):
    return MerakiClient().updateDeviceSensorRelationships(**kwargs)

@register('getDeviceSwitchPorts')
def getDeviceSwitchPorts(**kwargs):
    return MerakiClient().getDeviceSwitchPorts(**kwargs)

@register('cycleDeviceSwitchPorts')
def cycleDeviceSwitchPorts(**kwargs):
    return MerakiClient().cycleDeviceSwitchPorts(**kwargs)

@register('getDeviceSwitchPortsStatuses')
def getDeviceSwitchPortsStatuses(**kwargs):
    return MerakiClient().getDeviceSwitchPortsStatuses(**kwargs)

@register('getDeviceSwitchPortsStatusesPackets')
def getDeviceSwitchPortsStatusesPackets(**kwargs):
    return MerakiClient().getDeviceSwitchPortsStatusesPackets(**kwargs)

@register('getDeviceSwitchPort')
def getDeviceSwitchPort(**kwargs):
    return MerakiClient().getDeviceSwitchPort(**kwargs)

@register('updateDeviceSwitchPort')
def updateDeviceSwitchPort(**kwargs):
    return MerakiClient().updateDeviceSwitchPort(**kwargs)

@register('getDeviceSwitchRoutingInterfaces')
def getDeviceSwitchRoutingInterfaces(**kwargs):
    return MerakiClient().getDeviceSwitchRoutingInterfaces(**kwargs)

@register('createDeviceSwitchRoutingInterface')
def createDeviceSwitchRoutingInterface(**kwargs):
    return MerakiClient().createDeviceSwitchRoutingInterface(**kwargs)

@register('getDeviceSwitchRoutingInterface')
def getDeviceSwitchRoutingInterface(**kwargs):
    return MerakiClient().getDeviceSwitchRoutingInterface(**kwargs)

@register('updateDeviceSwitchRoutingInterface')
def updateDeviceSwitchRoutingInterface(**kwargs):
    return MerakiClient().updateDeviceSwitchRoutingInterface(**kwargs)

@register('deleteDeviceSwitchRoutingInterface')
def deleteDeviceSwitchRoutingInterface(**kwargs):
    return MerakiClient().deleteDeviceSwitchRoutingInterface(**kwargs)

@register('getDeviceSwitchRoutingInterfaceDhcp')
def getDeviceSwitchRoutingInterfaceDhcp(**kwargs):
    return MerakiClient().getDeviceSwitchRoutingInterfaceDhcp(**kwargs)

@register('updateDeviceSwitchRoutingInterfaceDhcp')
def updateDeviceSwitchRoutingInterfaceDhcp(**kwargs):
    return MerakiClient().updateDeviceSwitchRoutingInterfaceDhcp(**kwargs)

@register('getDeviceSwitchRoutingStaticRoutes')
def getDeviceSwitchRoutingStaticRoutes(**kwargs):
    return MerakiClient().getDeviceSwitchRoutingStaticRoutes(**kwargs)

@register('createDeviceSwitchRoutingStaticRoute')
def createDeviceSwitchRoutingStaticRoute(**kwargs):
    return MerakiClient().createDeviceSwitchRoutingStaticRoute(**kwargs)

@register('getDeviceSwitchRoutingStaticRoute')
def getDeviceSwitchRoutingStaticRoute(**kwargs):
    return MerakiClient().getDeviceSwitchRoutingStaticRoute(**kwargs)

@register('updateDeviceSwitchRoutingStaticRoute')
def updateDeviceSwitchRoutingStaticRoute(**kwargs):
    return MerakiClient().updateDeviceSwitchRoutingStaticRoute(**kwargs)

@register('deleteDeviceSwitchRoutingStaticRoute')
def deleteDeviceSwitchRoutingStaticRoute(**kwargs):
    return MerakiClient().deleteDeviceSwitchRoutingStaticRoute(**kwargs)

@register('getDeviceSwitchWarmSpare')
def getDeviceSwitchWarmSpare(**kwargs):
    return MerakiClient().getDeviceSwitchWarmSpare(**kwargs)

@register('updateDeviceSwitchWarmSpare')
def updateDeviceSwitchWarmSpare(**kwargs):
    return MerakiClient().updateDeviceSwitchWarmSpare(**kwargs)

@register('updateDeviceWirelessAlternateManagementInterfaceIpv6')
def updateDeviceWirelessAlternateManagementInterfaceIpv6(**kwargs):
    return MerakiClient().updateDeviceWirelessAlternateManagementInterfaceIpv6(**kwargs)

@register('getDeviceWirelessBluetoothSettings')
def getDeviceWirelessBluetoothSettings(**kwargs):
    return MerakiClient().getDeviceWirelessBluetoothSettings(**kwargs)

@register('updateDeviceWirelessBluetoothSettings')
def updateDeviceWirelessBluetoothSettings(**kwargs):
    return MerakiClient().updateDeviceWirelessBluetoothSettings(**kwargs)

@register('getDeviceWirelessConnectionStats')
def getDeviceWirelessConnectionStats(**kwargs):
    return MerakiClient().getDeviceWirelessConnectionStats(**kwargs)

@register('getDeviceWirelessElectronicShelfLabel')
def getDeviceWirelessElectronicShelfLabel(**kwargs):
    return MerakiClient().getDeviceWirelessElectronicShelfLabel(**kwargs)

@register('updateDeviceWirelessElectronicShelfLabel')
def updateDeviceWirelessElectronicShelfLabel(**kwargs):
    return MerakiClient().updateDeviceWirelessElectronicShelfLabel(**kwargs)

@register('getDeviceWirelessLatencyStats')
def getDeviceWirelessLatencyStats(**kwargs):
    return MerakiClient().getDeviceWirelessLatencyStats(**kwargs)

@register('getDeviceWirelessRadioSettings')
def getDeviceWirelessRadioSettings(**kwargs):
    return MerakiClient().getDeviceWirelessRadioSettings(**kwargs)

@register('updateDeviceWirelessRadioSettings')
def updateDeviceWirelessRadioSettings(**kwargs):
    return MerakiClient().updateDeviceWirelessRadioSettings(**kwargs)

@register('getDeviceWirelessStatus')
def getDeviceWirelessStatus(**kwargs):
    return MerakiClient().getDeviceWirelessStatus(**kwargs)

@register('getNetwork')
def getNetwork(**kwargs):
    return MerakiClient().getNetwork(**kwargs)

@register('updateNetwork')
def updateNetwork(**kwargs):
    return MerakiClient().updateNetwork(**kwargs)

@register('deleteNetwork')
def deleteNetwork(**kwargs):
    return MerakiClient().deleteNetwork(**kwargs)

@register('getNetworkAlertsHistory')
def getNetworkAlertsHistory(**kwargs):
    return MerakiClient().getNetworkAlertsHistory(**kwargs)

@register('getNetworkAlertsSettings')
def getNetworkAlertsSettings(**kwargs):
    return MerakiClient().getNetworkAlertsSettings(**kwargs)

@register('updateNetworkAlertsSettings')
def updateNetworkAlertsSettings(**kwargs):
    return MerakiClient().updateNetworkAlertsSettings(**kwargs)

@register('getNetworkApplianceClientSecurityEvents')
def getNetworkApplianceClientSecurityEvents(**kwargs):
    return MerakiClient().getNetworkApplianceClientSecurityEvents(**kwargs)

@register('getNetworkApplianceConnectivityMonitoringDestinations')
def getNetworkApplianceConnectivityMonitoringDestinations(**kwargs):
    return MerakiClient().getNetworkApplianceConnectivityMonitoringDestinations(**kwargs)

@register('updateNetworkApplianceConnectivityMonitoringDestinations')
def updateNetworkApplianceConnectivityMonitoringDestinations(**kwargs):
    return MerakiClient().updateNetworkApplianceConnectivityMonitoringDestinations(**kwargs)

@register('getNetworkApplianceContentFiltering')
def getNetworkApplianceContentFiltering(**kwargs):
    return MerakiClient().getNetworkApplianceContentFiltering(**kwargs)

@register('updateNetworkApplianceContentFiltering')
def updateNetworkApplianceContentFiltering(**kwargs):
    return MerakiClient().updateNetworkApplianceContentFiltering(**kwargs)

@register('getNetworkApplianceContentFilteringCategories')
def getNetworkApplianceContentFilteringCategories(**kwargs):
    return MerakiClient().getNetworkApplianceContentFilteringCategories(**kwargs)

@register('getNetworkApplianceFirewallCellularFirewallRules')
def getNetworkApplianceFirewallCellularFirewallRules(**kwargs):
    return MerakiClient().getNetworkApplianceFirewallCellularFirewallRules(**kwargs)

@register('updateNetworkApplianceFirewallCellularFirewallRules')
def updateNetworkApplianceFirewallCellularFirewallRules(**kwargs):
    return MerakiClient().updateNetworkApplianceFirewallCellularFirewallRules(**kwargs)

@register('getNetworkApplianceFirewallFirewalledServices')
def getNetworkApplianceFirewallFirewalledServices(**kwargs):
    return MerakiClient().getNetworkApplianceFirewallFirewalledServices(**kwargs)

@register('getNetworkApplianceFirewallFirewalledService')
def getNetworkApplianceFirewallFirewalledService(**kwargs):
    return MerakiClient().getNetworkApplianceFirewallFirewalledService(**kwargs)

@register('updateNetworkApplianceFirewallFirewalledService')
def updateNetworkApplianceFirewallFirewalledService(**kwargs):
    return MerakiClient().updateNetworkApplianceFirewallFirewalledService(**kwargs)

@register('getNetworkApplianceFirewallInboundCellularFirewallRules')
def getNetworkApplianceFirewallInboundCellularFirewallRules(**kwargs):
    return MerakiClient().getNetworkApplianceFirewallInboundCellularFirewallRules(**kwargs)

@register('updateNetworkApplianceFirewallInboundCellularFirewallRules')
def updateNetworkApplianceFirewallInboundCellularFirewallRules(**kwargs):
    return MerakiClient().updateNetworkApplianceFirewallInboundCellularFirewallRules(**kwargs)

@register('getNetworkApplianceFirewallInboundFirewallRules')
def getNetworkApplianceFirewallInboundFirewallRules(**kwargs):
    return MerakiClient().getNetworkApplianceFirewallInboundFirewallRules(**kwargs)

@register('updateNetworkApplianceFirewallInboundFirewallRules')
def updateNetworkApplianceFirewallInboundFirewallRules(**kwargs):
    return MerakiClient().updateNetworkApplianceFirewallInboundFirewallRules(**kwargs)

@register('getNetworkApplianceFirewallL3FirewallRules')
def getNetworkApplianceFirewallL3FirewallRules(**kwargs):
    return MerakiClient().getNetworkApplianceFirewallL3FirewallRules(**kwargs)

@register('updateNetworkApplianceFirewallL3FirewallRules')
def updateNetworkApplianceFirewallL3FirewallRules(**kwargs):
    return MerakiClient().updateNetworkApplianceFirewallL3FirewallRules(**kwargs)

@register('getNetworkApplianceFirewallL7FirewallRules')
def getNetworkApplianceFirewallL7FirewallRules(**kwargs):
    return MerakiClient().getNetworkApplianceFirewallL7FirewallRules(**kwargs)

@register('updateNetworkApplianceFirewallL7FirewallRules')
def updateNetworkApplianceFirewallL7FirewallRules(**kwargs):
    return MerakiClient().updateNetworkApplianceFirewallL7FirewallRules(**kwargs)

@register('getNetworkApplianceFirewallL7FirewallRulesApplicationCategories')
def getNetworkApplianceFirewallL7FirewallRulesApplicationCategories(**kwargs):
    return MerakiClient().getNetworkApplianceFirewallL7FirewallRulesApplicationCategories(**kwargs)

@register('updateNetworkApplianceFirewallMulticastForwarding')
def updateNetworkApplianceFirewallMulticastForwarding(**kwargs):
    return MerakiClient().updateNetworkApplianceFirewallMulticastForwarding(**kwargs)

@register('getNetworkApplianceFirewallOneToManyNatRules')
def getNetworkApplianceFirewallOneToManyNatRules(**kwargs):
    return MerakiClient().getNetworkApplianceFirewallOneToManyNatRules(**kwargs)

@register('updateNetworkApplianceFirewallOneToManyNatRules')
def updateNetworkApplianceFirewallOneToManyNatRules(**kwargs):
    return MerakiClient().updateNetworkApplianceFirewallOneToManyNatRules(**kwargs)

@register('getNetworkApplianceFirewallOneToOneNatRules')
def getNetworkApplianceFirewallOneToOneNatRules(**kwargs):
    return MerakiClient().getNetworkApplianceFirewallOneToOneNatRules(**kwargs)

@register('updateNetworkApplianceFirewallOneToOneNatRules')
def updateNetworkApplianceFirewallOneToOneNatRules(**kwargs):
    return MerakiClient().updateNetworkApplianceFirewallOneToOneNatRules(**kwargs)

@register('getNetworkApplianceFirewallPortForwardingRules')
def getNetworkApplianceFirewallPortForwardingRules(**kwargs):
    return MerakiClient().getNetworkApplianceFirewallPortForwardingRules(**kwargs)

@register('updateNetworkApplianceFirewallPortForwardingRules')
def updateNetworkApplianceFirewallPortForwardingRules(**kwargs):
    return MerakiClient().updateNetworkApplianceFirewallPortForwardingRules(**kwargs)

@register('getNetworkApplianceFirewallSettings')
def getNetworkApplianceFirewallSettings(**kwargs):
    return MerakiClient().getNetworkApplianceFirewallSettings(**kwargs)

@register('updateNetworkApplianceFirewallSettings')
def updateNetworkApplianceFirewallSettings(**kwargs):
    return MerakiClient().updateNetworkApplianceFirewallSettings(**kwargs)

@register('getNetworkAppliancePorts')
def getNetworkAppliancePorts(**kwargs):
    return MerakiClient().getNetworkAppliancePorts(**kwargs)

@register('getNetworkAppliancePort')
def getNetworkAppliancePort(**kwargs):
    return MerakiClient().getNetworkAppliancePort(**kwargs)

@register('updateNetworkAppliancePort')
def updateNetworkAppliancePort(**kwargs):
    return MerakiClient().updateNetworkAppliancePort(**kwargs)

@register('getNetworkAppliancePrefixesDelegatedStatics')
def getNetworkAppliancePrefixesDelegatedStatics(**kwargs):
    return MerakiClient().getNetworkAppliancePrefixesDelegatedStatics(**kwargs)

@register('createNetworkAppliancePrefixesDelegatedStatic')
def createNetworkAppliancePrefixesDelegatedStatic(**kwargs):
    return MerakiClient().createNetworkAppliancePrefixesDelegatedStatic(**kwargs)

@register('getNetworkAppliancePrefixesDelegatedStatic')
def getNetworkAppliancePrefixesDelegatedStatic(**kwargs):
    return MerakiClient().getNetworkAppliancePrefixesDelegatedStatic(**kwargs)

@register('updateNetworkAppliancePrefixesDelegatedStatic')
def updateNetworkAppliancePrefixesDelegatedStatic(**kwargs):
    return MerakiClient().updateNetworkAppliancePrefixesDelegatedStatic(**kwargs)

@register('deleteNetworkAppliancePrefixesDelegatedStatic')
def deleteNetworkAppliancePrefixesDelegatedStatic(**kwargs):
    return MerakiClient().deleteNetworkAppliancePrefixesDelegatedStatic(**kwargs)

@register('getNetworkApplianceRfProfiles')
def getNetworkApplianceRfProfiles(**kwargs):
    return MerakiClient().getNetworkApplianceRfProfiles(**kwargs)

@register('createNetworkApplianceRfProfile')
def createNetworkApplianceRfProfile(**kwargs):
    return MerakiClient().createNetworkApplianceRfProfile(**kwargs)

@register('updateNetworkApplianceRfProfile')
def updateNetworkApplianceRfProfile(**kwargs):
    return MerakiClient().updateNetworkApplianceRfProfile(**kwargs)

@register('deleteNetworkApplianceRfProfile')
def deleteNetworkApplianceRfProfile(**kwargs):
    return MerakiClient().deleteNetworkApplianceRfProfile(**kwargs)

@register('getNetworkApplianceRfProfile')
def getNetworkApplianceRfProfile(**kwargs):
    return MerakiClient().getNetworkApplianceRfProfile(**kwargs)

@register('updateNetworkApplianceSdwanInternetPolicies')
def updateNetworkApplianceSdwanInternetPolicies(**kwargs):
    return MerakiClient().updateNetworkApplianceSdwanInternetPolicies(**kwargs)

@register('getNetworkApplianceSecurityEvents')
def getNetworkApplianceSecurityEvents(**kwargs):
    return MerakiClient().getNetworkApplianceSecurityEvents(**kwargs)

@register('getNetworkApplianceSecurityIntrusion')
def getNetworkApplianceSecurityIntrusion(**kwargs):
    return MerakiClient().getNetworkApplianceSecurityIntrusion(**kwargs)

@register('updateNetworkApplianceSecurityIntrusion')
def updateNetworkApplianceSecurityIntrusion(**kwargs):
    return MerakiClient().updateNetworkApplianceSecurityIntrusion(**kwargs)

@register('getNetworkApplianceSecurityMalware')
def getNetworkApplianceSecurityMalware(**kwargs):
    return MerakiClient().getNetworkApplianceSecurityMalware(**kwargs)

@register('updateNetworkApplianceSecurityMalware')
def updateNetworkApplianceSecurityMalware(**kwargs):
    return MerakiClient().updateNetworkApplianceSecurityMalware(**kwargs)

@register('getNetworkApplianceSettings')
def getNetworkApplianceSettings(**kwargs):
    return MerakiClient().getNetworkApplianceSettings(**kwargs)

@register('updateNetworkApplianceSettings')
def updateNetworkApplianceSettings(**kwargs):
    return MerakiClient().updateNetworkApplianceSettings(**kwargs)

@register('getNetworkApplianceSingleLan')
def getNetworkApplianceSingleLan(**kwargs):
    return MerakiClient().getNetworkApplianceSingleLan(**kwargs)

@register('updateNetworkApplianceSingleLan')
def updateNetworkApplianceSingleLan(**kwargs):
    return MerakiClient().updateNetworkApplianceSingleLan(**kwargs)

@register('getNetworkApplianceSsids')
def getNetworkApplianceSsids(**kwargs):
    return MerakiClient().getNetworkApplianceSsids(**kwargs)

@register('getNetworkApplianceSsid')
def getNetworkApplianceSsid(**kwargs):
    return MerakiClient().getNetworkApplianceSsid(**kwargs)

@register('updateNetworkApplianceSsid')
def updateNetworkApplianceSsid(**kwargs):
    return MerakiClient().updateNetworkApplianceSsid(**kwargs)

@register('getNetworkApplianceStaticRoutes')
def getNetworkApplianceStaticRoutes(**kwargs):
    return MerakiClient().getNetworkApplianceStaticRoutes(**kwargs)

@register('createNetworkApplianceStaticRoute')
def createNetworkApplianceStaticRoute(**kwargs):
    return MerakiClient().createNetworkApplianceStaticRoute(**kwargs)

@register('getNetworkApplianceStaticRoute')
def getNetworkApplianceStaticRoute(**kwargs):
    return MerakiClient().getNetworkApplianceStaticRoute(**kwargs)

@register('updateNetworkApplianceStaticRoute')
def updateNetworkApplianceStaticRoute(**kwargs):
    return MerakiClient().updateNetworkApplianceStaticRoute(**kwargs)

@register('deleteNetworkApplianceStaticRoute')
def deleteNetworkApplianceStaticRoute(**kwargs):
    return MerakiClient().deleteNetworkApplianceStaticRoute(**kwargs)

@register('getNetworkApplianceTrafficShaping')
def getNetworkApplianceTrafficShaping(**kwargs):
    return MerakiClient().getNetworkApplianceTrafficShaping(**kwargs)

@register('updateNetworkApplianceTrafficShaping')
def updateNetworkApplianceTrafficShaping(**kwargs):
    return MerakiClient().updateNetworkApplianceTrafficShaping(**kwargs)

@register('getNetworkApplianceTrafficShapingCustomPerformanceClasses')
def getNetworkApplianceTrafficShapingCustomPerformanceClasses(**kwargs):
    return MerakiClient().getNetworkApplianceTrafficShapingCustomPerformanceClasses(**kwargs)

@register('createNetworkApplianceTrafficShapingCustomPerformanceClass')
def createNetworkApplianceTrafficShapingCustomPerformanceClass(**kwargs):
    return MerakiClient().createNetworkApplianceTrafficShapingCustomPerformanceClass(**kwargs)

@register('getNetworkApplianceTrafficShapingCustomPerformanceClass')
def getNetworkApplianceTrafficShapingCustomPerformanceClass(**kwargs):
    return MerakiClient().getNetworkApplianceTrafficShapingCustomPerformanceClass(**kwargs)

@register('updateNetworkApplianceTrafficShapingCustomPerformanceClass')
def updateNetworkApplianceTrafficShapingCustomPerformanceClass(**kwargs):
    return MerakiClient().updateNetworkApplianceTrafficShapingCustomPerformanceClass(**kwargs)

@register('deleteNetworkApplianceTrafficShapingCustomPerformanceClass')
def deleteNetworkApplianceTrafficShapingCustomPerformanceClass(**kwargs):
    return MerakiClient().deleteNetworkApplianceTrafficShapingCustomPerformanceClass(**kwargs)

@register('updateNetworkApplianceTrafficShapingRules')
def updateNetworkApplianceTrafficShapingRules(**kwargs):
    return MerakiClient().updateNetworkApplianceTrafficShapingRules(**kwargs)

@register('getNetworkApplianceTrafficShapingRules')
def getNetworkApplianceTrafficShapingRules(**kwargs):
    return MerakiClient().getNetworkApplianceTrafficShapingRules(**kwargs)

@register('getNetworkApplianceTrafficShapingUplinkBandwidth')
def getNetworkApplianceTrafficShapingUplinkBandwidth(**kwargs):
    return MerakiClient().getNetworkApplianceTrafficShapingUplinkBandwidth(**kwargs)

@register('updateNetworkApplianceTrafficShapingUplinkBandwidth')
def updateNetworkApplianceTrafficShapingUplinkBandwidth(**kwargs):
    return MerakiClient().updateNetworkApplianceTrafficShapingUplinkBandwidth(**kwargs)

@register('getNetworkApplianceTrafficShapingUplinkSelection')
def getNetworkApplianceTrafficShapingUplinkSelection(**kwargs):
    return MerakiClient().getNetworkApplianceTrafficShapingUplinkSelection(**kwargs)

@register('updateNetworkApplianceTrafficShapingUplinkSelection')
def updateNetworkApplianceTrafficShapingUplinkSelection(**kwargs):
    return MerakiClient().updateNetworkApplianceTrafficShapingUplinkSelection(**kwargs)

@register('updateNetworkApplianceTrafficShapingVpnExclusions')
def updateNetworkApplianceTrafficShapingVpnExclusions(**kwargs):
    return MerakiClient().updateNetworkApplianceTrafficShapingVpnExclusions(**kwargs)

@register('getNetworkApplianceUplinksUsageHistory')
def getNetworkApplianceUplinksUsageHistory(**kwargs):
    return MerakiClient().getNetworkApplianceUplinksUsageHistory(**kwargs)

@register('getNetworkApplianceVlans')
def getNetworkApplianceVlans(**kwargs):
    return MerakiClient().getNetworkApplianceVlans(**kwargs)

@register('createNetworkApplianceVlan')
def createNetworkApplianceVlan(**kwargs):
    return MerakiClient().createNetworkApplianceVlan(**kwargs)

@register('getNetworkApplianceVlansSettings')
def getNetworkApplianceVlansSettings(**kwargs):
    return MerakiClient().getNetworkApplianceVlansSettings(**kwargs)

@register('updateNetworkApplianceVlansSettings')
def updateNetworkApplianceVlansSettings(**kwargs):
    return MerakiClient().updateNetworkApplianceVlansSettings(**kwargs)

@register('getNetworkApplianceVlan')
def getNetworkApplianceVlan(**kwargs):
    return MerakiClient().getNetworkApplianceVlan(**kwargs)

@register('updateNetworkApplianceVlan')
def updateNetworkApplianceVlan(**kwargs):
    return MerakiClient().updateNetworkApplianceVlan(**kwargs)

@register('deleteNetworkApplianceVlan')
def deleteNetworkApplianceVlan(**kwargs):
    return MerakiClient().deleteNetworkApplianceVlan(**kwargs)

@register('getNetworkApplianceVpnBgp')
def getNetworkApplianceVpnBgp(**kwargs):
    return MerakiClient().getNetworkApplianceVpnBgp(**kwargs)

@register('updateNetworkApplianceVpnBgp')
def updateNetworkApplianceVpnBgp(**kwargs):
    return MerakiClient().updateNetworkApplianceVpnBgp(**kwargs)

@register('getNetworkApplianceVpnSiteToSiteVpn')
def getNetworkApplianceVpnSiteToSiteVpn(**kwargs):
    return MerakiClient().getNetworkApplianceVpnSiteToSiteVpn(**kwargs)

@register('updateNetworkApplianceVpnSiteToSiteVpn')
def updateNetworkApplianceVpnSiteToSiteVpn(**kwargs):
    return MerakiClient().updateNetworkApplianceVpnSiteToSiteVpn(**kwargs)

@register('getNetworkApplianceWarmSpare')
def getNetworkApplianceWarmSpare(**kwargs):
    return MerakiClient().getNetworkApplianceWarmSpare(**kwargs)

@register('updateNetworkApplianceWarmSpare')
def updateNetworkApplianceWarmSpare(**kwargs):
    return MerakiClient().updateNetworkApplianceWarmSpare(**kwargs)

@register('swapNetworkApplianceWarmSpare')
def swapNetworkApplianceWarmSpare(**kwargs):
    return MerakiClient().swapNetworkApplianceWarmSpare(**kwargs)

@register('bindNetwork')
def bindNetwork(**kwargs):
    return MerakiClient().bindNetwork(**kwargs)

@register('getNetworkBluetoothClients')
def getNetworkBluetoothClients(**kwargs):
    return MerakiClient().getNetworkBluetoothClients(**kwargs)

@register('getNetworkBluetoothClient')
def getNetworkBluetoothClient(**kwargs):
    return MerakiClient().getNetworkBluetoothClient(**kwargs)

@register('getNetworkCameraQualityRetentionProfiles')
def getNetworkCameraQualityRetentionProfiles(**kwargs):
    return MerakiClient().getNetworkCameraQualityRetentionProfiles(**kwargs)

@register('createNetworkCameraQualityRetentionProfile')
def createNetworkCameraQualityRetentionProfile(**kwargs):
    return MerakiClient().createNetworkCameraQualityRetentionProfile(**kwargs)

@register('getNetworkCameraQualityRetentionProfile')
def getNetworkCameraQualityRetentionProfile(**kwargs):
    return MerakiClient().getNetworkCameraQualityRetentionProfile(**kwargs)

@register('updateNetworkCameraQualityRetentionProfile')
def updateNetworkCameraQualityRetentionProfile(**kwargs):
    return MerakiClient().updateNetworkCameraQualityRetentionProfile(**kwargs)

@register('deleteNetworkCameraQualityRetentionProfile')
def deleteNetworkCameraQualityRetentionProfile(**kwargs):
    return MerakiClient().deleteNetworkCameraQualityRetentionProfile(**kwargs)

@register('getNetworkCameraSchedules')
def getNetworkCameraSchedules(**kwargs):
    return MerakiClient().getNetworkCameraSchedules(**kwargs)

@register('createNetworkCameraWirelessProfile')
def createNetworkCameraWirelessProfile(**kwargs):
    return MerakiClient().createNetworkCameraWirelessProfile(**kwargs)

@register('getNetworkCameraWirelessProfiles')
def getNetworkCameraWirelessProfiles(**kwargs):
    return MerakiClient().getNetworkCameraWirelessProfiles(**kwargs)

@register('getNetworkCameraWirelessProfile')
def getNetworkCameraWirelessProfile(**kwargs):
    return MerakiClient().getNetworkCameraWirelessProfile(**kwargs)

@register('updateNetworkCameraWirelessProfile')
def updateNetworkCameraWirelessProfile(**kwargs):
    return MerakiClient().updateNetworkCameraWirelessProfile(**kwargs)

@register('deleteNetworkCameraWirelessProfile')
def deleteNetworkCameraWirelessProfile(**kwargs):
    return MerakiClient().deleteNetworkCameraWirelessProfile(**kwargs)

@register('getNetworkCellularGatewayConnectivityMonitoringDestinations')
def getNetworkCellularGatewayConnectivityMonitoringDestinations(**kwargs):
    return MerakiClient().getNetworkCellularGatewayConnectivityMonitoringDestinations(**kwargs)

@register('updateNetworkCellularGatewayConnectivityMonitoringDestinations')
def updateNetworkCellularGatewayConnectivityMonitoringDestinations(**kwargs):
    return MerakiClient().updateNetworkCellularGatewayConnectivityMonitoringDestinations(**kwargs)

@register('getNetworkCellularGatewayDhcp')
def getNetworkCellularGatewayDhcp(**kwargs):
    return MerakiClient().getNetworkCellularGatewayDhcp(**kwargs)

@register('updateNetworkCellularGatewayDhcp')
def updateNetworkCellularGatewayDhcp(**kwargs):
    return MerakiClient().updateNetworkCellularGatewayDhcp(**kwargs)

@register('getNetworkCellularGatewaySubnetPool')
def getNetworkCellularGatewaySubnetPool(**kwargs):
    return MerakiClient().getNetworkCellularGatewaySubnetPool(**kwargs)

@register('updateNetworkCellularGatewaySubnetPool')
def updateNetworkCellularGatewaySubnetPool(**kwargs):
    return MerakiClient().updateNetworkCellularGatewaySubnetPool(**kwargs)

@register('getNetworkCellularGatewayUplink')
def getNetworkCellularGatewayUplink(**kwargs):
    return MerakiClient().getNetworkCellularGatewayUplink(**kwargs)

@register('updateNetworkCellularGatewayUplink')
def updateNetworkCellularGatewayUplink(**kwargs):
    return MerakiClient().updateNetworkCellularGatewayUplink(**kwargs)

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

@register('provisionNetworkClients')
def provisionNetworkClients(**kwargs):
    return MerakiClient().provisionNetworkClients(**kwargs)

@register('getNetworkClientsUsageHistories')
def getNetworkClientsUsageHistories(**kwargs):
    return MerakiClient().getNetworkClientsUsageHistories(**kwargs)

@register('getNetworkClient')
def getNetworkClient(**kwargs):
    return MerakiClient().getNetworkClient(**kwargs)

@register('getNetworkClientPolicy')
def getNetworkClientPolicy(**kwargs):
    return MerakiClient().getNetworkClientPolicy(**kwargs)

@register('updateNetworkClientPolicy')
def updateNetworkClientPolicy(**kwargs):
    return MerakiClient().updateNetworkClientPolicy(**kwargs)

@register('getNetworkClientSplashAuthorizationStatus')
def getNetworkClientSplashAuthorizationStatus(**kwargs):
    return MerakiClient().getNetworkClientSplashAuthorizationStatus(**kwargs)

@register('updateNetworkClientSplashAuthorizationStatus')
def updateNetworkClientSplashAuthorizationStatus(**kwargs):
    return MerakiClient().updateNetworkClientSplashAuthorizationStatus(**kwargs)

@register('getNetworkClientTrafficHistory')
def getNetworkClientTrafficHistory(**kwargs):
    return MerakiClient().getNetworkClientTrafficHistory(**kwargs)

@register('getNetworkClientUsageHistory')
def getNetworkClientUsageHistory(**kwargs):
    return MerakiClient().getNetworkClientUsageHistory(**kwargs)

@register('getNetworkDevices')
def getNetworkDevices(**kwargs):
    return MerakiClient().getNetworkDevices(**kwargs)

@register('claimNetworkDevices')
def claimNetworkDevices(**kwargs):
    return MerakiClient().claimNetworkDevices(**kwargs)

@register('vmxNetworkDevicesClaim')
def vmxNetworkDevicesClaim(**kwargs):
    return MerakiClient().vmxNetworkDevicesClaim(**kwargs)

@register('removeNetworkDevices')
def removeNetworkDevices(**kwargs):
    return MerakiClient().removeNetworkDevices(**kwargs)

@register('getNetworkEvents')
def getNetworkEvents(**kwargs):
    return MerakiClient().getNetworkEvents(**kwargs)

@register('getNetworkEventsEventTypes')
def getNetworkEventsEventTypes(**kwargs):
    return MerakiClient().getNetworkEventsEventTypes(**kwargs)

@register('getNetworkFirmwareUpgrades')
def getNetworkFirmwareUpgrades(**kwargs):
    return MerakiClient().getNetworkFirmwareUpgrades(**kwargs)

@register('updateNetworkFirmwareUpgrades')
def updateNetworkFirmwareUpgrades(**kwargs):
    return MerakiClient().updateNetworkFirmwareUpgrades(**kwargs)

@register('createNetworkFirmwareUpgradesRollback')
def createNetworkFirmwareUpgradesRollback(**kwargs):
    return MerakiClient().createNetworkFirmwareUpgradesRollback(**kwargs)

@register('getNetworkFirmwareUpgradesStagedEvents')
def getNetworkFirmwareUpgradesStagedEvents(**kwargs):
    return MerakiClient().getNetworkFirmwareUpgradesStagedEvents(**kwargs)

@register('createNetworkFirmwareUpgradesStagedEvent')
def createNetworkFirmwareUpgradesStagedEvent(**kwargs):
    return MerakiClient().createNetworkFirmwareUpgradesStagedEvent(**kwargs)

@register('updateNetworkFirmwareUpgradesStagedEvents')
def updateNetworkFirmwareUpgradesStagedEvents(**kwargs):
    return MerakiClient().updateNetworkFirmwareUpgradesStagedEvents(**kwargs)

@register('deferNetworkFirmwareUpgradesStagedEvents')
def deferNetworkFirmwareUpgradesStagedEvents(**kwargs):
    return MerakiClient().deferNetworkFirmwareUpgradesStagedEvents(**kwargs)

@register('rollbacksNetworkFirmwareUpgradesStagedEvents')
def rollbacksNetworkFirmwareUpgradesStagedEvents(**kwargs):
    return MerakiClient().rollbacksNetworkFirmwareUpgradesStagedEvents(**kwargs)

@register('getNetworkFirmwareUpgradesStagedGroups')
def getNetworkFirmwareUpgradesStagedGroups(**kwargs):
    return MerakiClient().getNetworkFirmwareUpgradesStagedGroups(**kwargs)

@register('createNetworkFirmwareUpgradesStagedGroup')
def createNetworkFirmwareUpgradesStagedGroup(**kwargs):
    return MerakiClient().createNetworkFirmwareUpgradesStagedGroup(**kwargs)

@register('getNetworkFirmwareUpgradesStagedGroup')
def getNetworkFirmwareUpgradesStagedGroup(**kwargs):
    return MerakiClient().getNetworkFirmwareUpgradesStagedGroup(**kwargs)

@register('updateNetworkFirmwareUpgradesStagedGroup')
def updateNetworkFirmwareUpgradesStagedGroup(**kwargs):
    return MerakiClient().updateNetworkFirmwareUpgradesStagedGroup(**kwargs)

@register('deleteNetworkFirmwareUpgradesStagedGroup')
def deleteNetworkFirmwareUpgradesStagedGroup(**kwargs):
    return MerakiClient().deleteNetworkFirmwareUpgradesStagedGroup(**kwargs)

@register('getNetworkFirmwareUpgradesStagedStages')
def getNetworkFirmwareUpgradesStagedStages(**kwargs):
    return MerakiClient().getNetworkFirmwareUpgradesStagedStages(**kwargs)

@register('updateNetworkFirmwareUpgradesStagedStages')
def updateNetworkFirmwareUpgradesStagedStages(**kwargs):
    return MerakiClient().updateNetworkFirmwareUpgradesStagedStages(**kwargs)

@register('getNetworkFloorPlans')
def getNetworkFloorPlans(**kwargs):
    return MerakiClient().getNetworkFloorPlans(**kwargs)

@register('createNetworkFloorPlan')
def createNetworkFloorPlan(**kwargs):
    return MerakiClient().createNetworkFloorPlan(**kwargs)

@register('batchNetworkFloorPlansAutoLocateJobs')
def batchNetworkFloorPlansAutoLocateJobs(**kwargs):
    return MerakiClient().batchNetworkFloorPlansAutoLocateJobs(**kwargs)

@register('cancelNetworkFloorPlansAutoLocateJob')
def cancelNetworkFloorPlansAutoLocateJob(**kwargs):
    return MerakiClient().cancelNetworkFloorPlansAutoLocateJob(**kwargs)

@register('publishNetworkFloorPlansAutoLocateJob')
def publishNetworkFloorPlansAutoLocateJob(**kwargs):
    return MerakiClient().publishNetworkFloorPlansAutoLocateJob(**kwargs)

@register('recalculateNetworkFloorPlansAutoLocateJob')
def recalculateNetworkFloorPlansAutoLocateJob(**kwargs):
    return MerakiClient().recalculateNetworkFloorPlansAutoLocateJob(**kwargs)

@register('batchNetworkFloorPlansDevicesUpdate')
def batchNetworkFloorPlansDevicesUpdate(**kwargs):
    return MerakiClient().batchNetworkFloorPlansDevicesUpdate(**kwargs)

@register('getNetworkFloorPlan')
def getNetworkFloorPlan(**kwargs):
    return MerakiClient().getNetworkFloorPlan(**kwargs)

@register('updateNetworkFloorPlan')
def updateNetworkFloorPlan(**kwargs):
    return MerakiClient().updateNetworkFloorPlan(**kwargs)

@register('deleteNetworkFloorPlan')
def deleteNetworkFloorPlan(**kwargs):
    return MerakiClient().deleteNetworkFloorPlan(**kwargs)

@register('getNetworkGroupPolicies')
def getNetworkGroupPolicies(**kwargs):
    return MerakiClient().getNetworkGroupPolicies(**kwargs)

@register('createNetworkGroupPolicy')
def createNetworkGroupPolicy(**kwargs):
    return MerakiClient().createNetworkGroupPolicy(**kwargs)

@register('getNetworkGroupPolicy')
def getNetworkGroupPolicy(**kwargs):
    return MerakiClient().getNetworkGroupPolicy(**kwargs)

@register('updateNetworkGroupPolicy')
def updateNetworkGroupPolicy(**kwargs):
    return MerakiClient().updateNetworkGroupPolicy(**kwargs)

@register('deleteNetworkGroupPolicy')
def deleteNetworkGroupPolicy(**kwargs):
    return MerakiClient().deleteNetworkGroupPolicy(**kwargs)

@register('getNetworkHealthAlerts')
def getNetworkHealthAlerts(**kwargs):
    return MerakiClient().getNetworkHealthAlerts(**kwargs)

@register('getNetworkInsightApplicationHealthByTime')
def getNetworkInsightApplicationHealthByTime(**kwargs):
    return MerakiClient().getNetworkInsightApplicationHealthByTime(**kwargs)

@register('getNetworkMerakiAuthUsers')
def getNetworkMerakiAuthUsers(**kwargs):
    return MerakiClient().getNetworkMerakiAuthUsers(**kwargs)

@register('createNetworkMerakiAuthUser')
def createNetworkMerakiAuthUser(**kwargs):
    return MerakiClient().createNetworkMerakiAuthUser(**kwargs)

@register('getNetworkMerakiAuthUser')
def getNetworkMerakiAuthUser(**kwargs):
    return MerakiClient().getNetworkMerakiAuthUser(**kwargs)

@register('deleteNetworkMerakiAuthUser')
def deleteNetworkMerakiAuthUser(**kwargs):
    return MerakiClient().deleteNetworkMerakiAuthUser(**kwargs)

@register('updateNetworkMerakiAuthUser')
def updateNetworkMerakiAuthUser(**kwargs):
    return MerakiClient().updateNetworkMerakiAuthUser(**kwargs)

@register('getNetworkMqttBrokers')
def getNetworkMqttBrokers(**kwargs):
    return MerakiClient().getNetworkMqttBrokers(**kwargs)

@register('createNetworkMqttBroker')
def createNetworkMqttBroker(**kwargs):
    return MerakiClient().createNetworkMqttBroker(**kwargs)

@register('getNetworkMqttBroker')
def getNetworkMqttBroker(**kwargs):
    return MerakiClient().getNetworkMqttBroker(**kwargs)

@register('updateNetworkMqttBroker')
def updateNetworkMqttBroker(**kwargs):
    return MerakiClient().updateNetworkMqttBroker(**kwargs)

@register('deleteNetworkMqttBroker')
def deleteNetworkMqttBroker(**kwargs):
    return MerakiClient().deleteNetworkMqttBroker(**kwargs)

@register('getNetworkNetflow')
def getNetworkNetflow(**kwargs):
    return MerakiClient().getNetworkNetflow(**kwargs)

@register('updateNetworkNetflow')
def updateNetworkNetflow(**kwargs):
    return MerakiClient().updateNetworkNetflow(**kwargs)

@register('getNetworkNetworkHealthChannelUtilization')
def getNetworkNetworkHealthChannelUtilization(**kwargs):
    return MerakiClient().getNetworkNetworkHealthChannelUtilization(**kwargs)

@register('getNetworkPiiPiiKeys')
def getNetworkPiiPiiKeys(**kwargs):
    return MerakiClient().getNetworkPiiPiiKeys(**kwargs)

@register('getNetworkPiiRequests')
def getNetworkPiiRequests(**kwargs):
    return MerakiClient().getNetworkPiiRequests(**kwargs)

@register('createNetworkPiiRequest')
def createNetworkPiiRequest(**kwargs):
    return MerakiClient().createNetworkPiiRequest(**kwargs)

@register('getNetworkPiiRequest')
def getNetworkPiiRequest(**kwargs):
    return MerakiClient().getNetworkPiiRequest(**kwargs)

@register('deleteNetworkPiiRequest')
def deleteNetworkPiiRequest(**kwargs):
    return MerakiClient().deleteNetworkPiiRequest(**kwargs)

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

@register('createNetworkSensorAlertsProfile')
def createNetworkSensorAlertsProfile(**kwargs):
    return MerakiClient().createNetworkSensorAlertsProfile(**kwargs)

@register('getNetworkSensorAlertsProfile')
def getNetworkSensorAlertsProfile(**kwargs):
    return MerakiClient().getNetworkSensorAlertsProfile(**kwargs)

@register('updateNetworkSensorAlertsProfile')
def updateNetworkSensorAlertsProfile(**kwargs):
    return MerakiClient().updateNetworkSensorAlertsProfile(**kwargs)

@register('deleteNetworkSensorAlertsProfile')
def deleteNetworkSensorAlertsProfile(**kwargs):
    return MerakiClient().deleteNetworkSensorAlertsProfile(**kwargs)

@register('getNetworkSensorMqttBrokers')
def getNetworkSensorMqttBrokers(**kwargs):
    return MerakiClient().getNetworkSensorMqttBrokers(**kwargs)

@register('getNetworkSensorMqttBroker')
def getNetworkSensorMqttBroker(**kwargs):
    return MerakiClient().getNetworkSensorMqttBroker(**kwargs)

@register('updateNetworkSensorMqttBroker')
def updateNetworkSensorMqttBroker(**kwargs):
    return MerakiClient().updateNetworkSensorMqttBroker(**kwargs)

@register('getNetworkSensorRelationships')
def getNetworkSensorRelationships(**kwargs):
    return MerakiClient().getNetworkSensorRelationships(**kwargs)

@register('getNetworkSettings')
def getNetworkSettings(**kwargs):
    return MerakiClient().getNetworkSettings(**kwargs)

@register('updateNetworkSettings')
def updateNetworkSettings(**kwargs):
    return MerakiClient().updateNetworkSettings(**kwargs)

@register('createNetworkSmBypassActivationLockAttempt')
def createNetworkSmBypassActivationLockAttempt(**kwargs):
    return MerakiClient().createNetworkSmBypassActivationLockAttempt(**kwargs)

@register('getNetworkSmBypassActivationLockAttempt')
def getNetworkSmBypassActivationLockAttempt(**kwargs):
    return MerakiClient().getNetworkSmBypassActivationLockAttempt(**kwargs)

@register('getNetworkSmDevices')
def getNetworkSmDevices(**kwargs):
    return MerakiClient().getNetworkSmDevices(**kwargs)

@register('checkinNetworkSmDevices')
def checkinNetworkSmDevices(**kwargs):
    return MerakiClient().checkinNetworkSmDevices(**kwargs)

@register('updateNetworkSmDevicesFields')
def updateNetworkSmDevicesFields(**kwargs):
    return MerakiClient().updateNetworkSmDevicesFields(**kwargs)

@register('lockNetworkSmDevices')
def lockNetworkSmDevices(**kwargs):
    return MerakiClient().lockNetworkSmDevices(**kwargs)

@register('modifyNetworkSmDevicesTags')
def modifyNetworkSmDevicesTags(**kwargs):
    return MerakiClient().modifyNetworkSmDevicesTags(**kwargs)

@register('moveNetworkSmDevices')
def moveNetworkSmDevices(**kwargs):
    return MerakiClient().moveNetworkSmDevices(**kwargs)

@register('rebootNetworkSmDevices')
def rebootNetworkSmDevices(**kwargs):
    return MerakiClient().rebootNetworkSmDevices(**kwargs)

@register('shutdownNetworkSmDevices')
def shutdownNetworkSmDevices(**kwargs):
    return MerakiClient().shutdownNetworkSmDevices(**kwargs)

@register('wipeNetworkSmDevices')
def wipeNetworkSmDevices(**kwargs):
    return MerakiClient().wipeNetworkSmDevices(**kwargs)

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

@register('installNetworkSmDeviceApps')
def installNetworkSmDeviceApps(**kwargs):
    return MerakiClient().installNetworkSmDeviceApps(**kwargs)

@register('getNetworkSmDeviceNetworkAdapters')
def getNetworkSmDeviceNetworkAdapters(**kwargs):
    return MerakiClient().getNetworkSmDeviceNetworkAdapters(**kwargs)

@register('getNetworkSmDevicePerformanceHistory')
def getNetworkSmDevicePerformanceHistory(**kwargs):
    return MerakiClient().getNetworkSmDevicePerformanceHistory(**kwargs)

@register('refreshNetworkSmDeviceDetails')
def refreshNetworkSmDeviceDetails(**kwargs):
    return MerakiClient().refreshNetworkSmDeviceDetails(**kwargs)

@register('getNetworkSmDeviceRestrictions')
def getNetworkSmDeviceRestrictions(**kwargs):
    return MerakiClient().getNetworkSmDeviceRestrictions(**kwargs)

@register('getNetworkSmDeviceSecurityCenters')
def getNetworkSmDeviceSecurityCenters(**kwargs):
    return MerakiClient().getNetworkSmDeviceSecurityCenters(**kwargs)

@register('getNetworkSmDeviceSoftwares')
def getNetworkSmDeviceSoftwares(**kwargs):
    return MerakiClient().getNetworkSmDeviceSoftwares(**kwargs)

@register('unenrollNetworkSmDevice')
def unenrollNetworkSmDevice(**kwargs):
    return MerakiClient().unenrollNetworkSmDevice(**kwargs)

@register('uninstallNetworkSmDeviceApps')
def uninstallNetworkSmDeviceApps(**kwargs):
    return MerakiClient().uninstallNetworkSmDeviceApps(**kwargs)

@register('getNetworkSmDeviceWlanLists')
def getNetworkSmDeviceWlanLists(**kwargs):
    return MerakiClient().getNetworkSmDeviceWlanLists(**kwargs)

@register('getNetworkSmProfiles')
def getNetworkSmProfiles(**kwargs):
    return MerakiClient().getNetworkSmProfiles(**kwargs)

@register('getNetworkSmTargetGroups')
def getNetworkSmTargetGroups(**kwargs):
    return MerakiClient().getNetworkSmTargetGroups(**kwargs)

@register('createNetworkSmTargetGroup')
def createNetworkSmTargetGroup(**kwargs):
    return MerakiClient().createNetworkSmTargetGroup(**kwargs)

@register('getNetworkSmTargetGroup')
def getNetworkSmTargetGroup(**kwargs):
    return MerakiClient().getNetworkSmTargetGroup(**kwargs)

@register('updateNetworkSmTargetGroup')
def updateNetworkSmTargetGroup(**kwargs):
    return MerakiClient().updateNetworkSmTargetGroup(**kwargs)

@register('deleteNetworkSmTargetGroup')
def deleteNetworkSmTargetGroup(**kwargs):
    return MerakiClient().deleteNetworkSmTargetGroup(**kwargs)

@register('getNetworkSmTrustedAccessConfigs')
def getNetworkSmTrustedAccessConfigs(**kwargs):
    return MerakiClient().getNetworkSmTrustedAccessConfigs(**kwargs)

@register('getNetworkSmUserAccessDevices')
def getNetworkSmUserAccessDevices(**kwargs):
    return MerakiClient().getNetworkSmUserAccessDevices(**kwargs)

@register('deleteNetworkSmUserAccessDevice')
def deleteNetworkSmUserAccessDevice(**kwargs):
    return MerakiClient().deleteNetworkSmUserAccessDevice(**kwargs)

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

@register('updateNetworkSnmp')
def updateNetworkSnmp(**kwargs):
    return MerakiClient().updateNetworkSnmp(**kwargs)

@register('getNetworkSplashLoginAttempts')
def getNetworkSplashLoginAttempts(**kwargs):
    return MerakiClient().getNetworkSplashLoginAttempts(**kwargs)

@register('splitNetwork')
def splitNetwork(**kwargs):
    return MerakiClient().splitNetwork(**kwargs)

@register('getNetworkSwitchAccessControlLists')
def getNetworkSwitchAccessControlLists(**kwargs):
    return MerakiClient().getNetworkSwitchAccessControlLists(**kwargs)

@register('updateNetworkSwitchAccessControlLists')
def updateNetworkSwitchAccessControlLists(**kwargs):
    return MerakiClient().updateNetworkSwitchAccessControlLists(**kwargs)

@register('getNetworkSwitchAccessPolicies')
def getNetworkSwitchAccessPolicies(**kwargs):
    return MerakiClient().getNetworkSwitchAccessPolicies(**kwargs)

@register('createNetworkSwitchAccessPolicy')
def createNetworkSwitchAccessPolicy(**kwargs):
    return MerakiClient().createNetworkSwitchAccessPolicy(**kwargs)

@register('getNetworkSwitchAccessPolicy')
def getNetworkSwitchAccessPolicy(**kwargs):
    return MerakiClient().getNetworkSwitchAccessPolicy(**kwargs)

@register('updateNetworkSwitchAccessPolicy')
def updateNetworkSwitchAccessPolicy(**kwargs):
    return MerakiClient().updateNetworkSwitchAccessPolicy(**kwargs)

@register('deleteNetworkSwitchAccessPolicy')
def deleteNetworkSwitchAccessPolicy(**kwargs):
    return MerakiClient().deleteNetworkSwitchAccessPolicy(**kwargs)

@register('getNetworkSwitchAlternateManagementInterface')
def getNetworkSwitchAlternateManagementInterface(**kwargs):
    return MerakiClient().getNetworkSwitchAlternateManagementInterface(**kwargs)

@register('updateNetworkSwitchAlternateManagementInterface')
def updateNetworkSwitchAlternateManagementInterface(**kwargs):
    return MerakiClient().updateNetworkSwitchAlternateManagementInterface(**kwargs)

@register('getNetworkSwitchDhcpV4ServersSeen')
def getNetworkSwitchDhcpV4ServersSeen(**kwargs):
    return MerakiClient().getNetworkSwitchDhcpV4ServersSeen(**kwargs)

@register('getNetworkSwitchDhcpServerPolicy')
def getNetworkSwitchDhcpServerPolicy(**kwargs):
    return MerakiClient().getNetworkSwitchDhcpServerPolicy(**kwargs)

@register('updateNetworkSwitchDhcpServerPolicy')
def updateNetworkSwitchDhcpServerPolicy(**kwargs):
    return MerakiClient().updateNetworkSwitchDhcpServerPolicy(**kwargs)

@register('getNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers')
def getNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers(**kwargs):
    return MerakiClient().getNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers(**kwargs)

@register('createNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer')
def createNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer(**kwargs):
    return MerakiClient().createNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer(**kwargs)

@register('updateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer')
def updateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer(**kwargs):
    return MerakiClient().updateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer(**kwargs)

@register('deleteNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer')
def deleteNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer(**kwargs):
    return MerakiClient().deleteNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer(**kwargs)

@register('getNetworkSwitchDhcpServerPolicyArpInspectionWarningsByDevice')
def getNetworkSwitchDhcpServerPolicyArpInspectionWarningsByDevice(**kwargs):
    return MerakiClient().getNetworkSwitchDhcpServerPolicyArpInspectionWarningsByDevice(**kwargs)

@register('getNetworkSwitchDscpToCosMappings')
def getNetworkSwitchDscpToCosMappings(**kwargs):
    return MerakiClient().getNetworkSwitchDscpToCosMappings(**kwargs)

@register('updateNetworkSwitchDscpToCosMappings')
def updateNetworkSwitchDscpToCosMappings(**kwargs):
    return MerakiClient().updateNetworkSwitchDscpToCosMappings(**kwargs)

@register('getNetworkSwitchLinkAggregations')
def getNetworkSwitchLinkAggregations(**kwargs):
    return MerakiClient().getNetworkSwitchLinkAggregations(**kwargs)

@register('createNetworkSwitchLinkAggregation')
def createNetworkSwitchLinkAggregation(**kwargs):
    return MerakiClient().createNetworkSwitchLinkAggregation(**kwargs)

@register('updateNetworkSwitchLinkAggregation')
def updateNetworkSwitchLinkAggregation(**kwargs):
    return MerakiClient().updateNetworkSwitchLinkAggregation(**kwargs)

@register('deleteNetworkSwitchLinkAggregation')
def deleteNetworkSwitchLinkAggregation(**kwargs):
    return MerakiClient().deleteNetworkSwitchLinkAggregation(**kwargs)

@register('getNetworkSwitchMtu')
def getNetworkSwitchMtu(**kwargs):
    return MerakiClient().getNetworkSwitchMtu(**kwargs)

@register('updateNetworkSwitchMtu')
def updateNetworkSwitchMtu(**kwargs):
    return MerakiClient().updateNetworkSwitchMtu(**kwargs)

@register('getNetworkSwitchPortSchedules')
def getNetworkSwitchPortSchedules(**kwargs):
    return MerakiClient().getNetworkSwitchPortSchedules(**kwargs)

@register('createNetworkSwitchPortSchedule')
def createNetworkSwitchPortSchedule(**kwargs):
    return MerakiClient().createNetworkSwitchPortSchedule(**kwargs)

@register('deleteNetworkSwitchPortSchedule')
def deleteNetworkSwitchPortSchedule(**kwargs):
    return MerakiClient().deleteNetworkSwitchPortSchedule(**kwargs)

@register('updateNetworkSwitchPortSchedule')
def updateNetworkSwitchPortSchedule(**kwargs):
    return MerakiClient().updateNetworkSwitchPortSchedule(**kwargs)

@register('getNetworkSwitchQosRules')
def getNetworkSwitchQosRules(**kwargs):
    return MerakiClient().getNetworkSwitchQosRules(**kwargs)

@register('createNetworkSwitchQosRule')
def createNetworkSwitchQosRule(**kwargs):
    return MerakiClient().createNetworkSwitchQosRule(**kwargs)

@register('getNetworkSwitchQosRulesOrder')
def getNetworkSwitchQosRulesOrder(**kwargs):
    return MerakiClient().getNetworkSwitchQosRulesOrder(**kwargs)

@register('updateNetworkSwitchQosRulesOrder')
def updateNetworkSwitchQosRulesOrder(**kwargs):
    return MerakiClient().updateNetworkSwitchQosRulesOrder(**kwargs)

@register('getNetworkSwitchQosRule')
def getNetworkSwitchQosRule(**kwargs):
    return MerakiClient().getNetworkSwitchQosRule(**kwargs)

@register('deleteNetworkSwitchQosRule')
def deleteNetworkSwitchQosRule(**kwargs):
    return MerakiClient().deleteNetworkSwitchQosRule(**kwargs)

@register('updateNetworkSwitchQosRule')
def updateNetworkSwitchQosRule(**kwargs):
    return MerakiClient().updateNetworkSwitchQosRule(**kwargs)

@register('getNetworkSwitchRoutingMulticast')
def getNetworkSwitchRoutingMulticast(**kwargs):
    return MerakiClient().getNetworkSwitchRoutingMulticast(**kwargs)

@register('updateNetworkSwitchRoutingMulticast')
def updateNetworkSwitchRoutingMulticast(**kwargs):
    return MerakiClient().updateNetworkSwitchRoutingMulticast(**kwargs)

@register('getNetworkSwitchRoutingMulticastRendezvousPoints')
def getNetworkSwitchRoutingMulticastRendezvousPoints(**kwargs):
    return MerakiClient().getNetworkSwitchRoutingMulticastRendezvousPoints(**kwargs)

@register('createNetworkSwitchRoutingMulticastRendezvousPoint')
def createNetworkSwitchRoutingMulticastRendezvousPoint(**kwargs):
    return MerakiClient().createNetworkSwitchRoutingMulticastRendezvousPoint(**kwargs)

@register('getNetworkSwitchRoutingMulticastRendezvousPoint')
def getNetworkSwitchRoutingMulticastRendezvousPoint(**kwargs):
    return MerakiClient().getNetworkSwitchRoutingMulticastRendezvousPoint(**kwargs)

@register('deleteNetworkSwitchRoutingMulticastRendezvousPoint')
def deleteNetworkSwitchRoutingMulticastRendezvousPoint(**kwargs):
    return MerakiClient().deleteNetworkSwitchRoutingMulticastRendezvousPoint(**kwargs)

@register('updateNetworkSwitchRoutingMulticastRendezvousPoint')
def updateNetworkSwitchRoutingMulticastRendezvousPoint(**kwargs):
    return MerakiClient().updateNetworkSwitchRoutingMulticastRendezvousPoint(**kwargs)

@register('getNetworkSwitchRoutingOspf')
def getNetworkSwitchRoutingOspf(**kwargs):
    return MerakiClient().getNetworkSwitchRoutingOspf(**kwargs)

@register('updateNetworkSwitchRoutingOspf')
def updateNetworkSwitchRoutingOspf(**kwargs):
    return MerakiClient().updateNetworkSwitchRoutingOspf(**kwargs)

@register('getNetworkSwitchSettings')
def getNetworkSwitchSettings(**kwargs):
    return MerakiClient().getNetworkSwitchSettings(**kwargs)

@register('updateNetworkSwitchSettings')
def updateNetworkSwitchSettings(**kwargs):
    return MerakiClient().updateNetworkSwitchSettings(**kwargs)

@register('getNetworkSwitchStacks')
def getNetworkSwitchStacks(**kwargs):
    return MerakiClient().getNetworkSwitchStacks(**kwargs)

@register('createNetworkSwitchStack')
def createNetworkSwitchStack(**kwargs):
    return MerakiClient().createNetworkSwitchStack(**kwargs)

@register('getNetworkSwitchStack')
def getNetworkSwitchStack(**kwargs):
    return MerakiClient().getNetworkSwitchStack(**kwargs)

@register('deleteNetworkSwitchStack')
def deleteNetworkSwitchStack(**kwargs):
    return MerakiClient().deleteNetworkSwitchStack(**kwargs)

@register('addNetworkSwitchStack')
def addNetworkSwitchStack(**kwargs):
    return MerakiClient().addNetworkSwitchStack(**kwargs)

@register('removeNetworkSwitchStack')
def removeNetworkSwitchStack(**kwargs):
    return MerakiClient().removeNetworkSwitchStack(**kwargs)

@register('getNetworkSwitchStackRoutingInterfaces')
def getNetworkSwitchStackRoutingInterfaces(**kwargs):
    return MerakiClient().getNetworkSwitchStackRoutingInterfaces(**kwargs)

@register('createNetworkSwitchStackRoutingInterface')
def createNetworkSwitchStackRoutingInterface(**kwargs):
    return MerakiClient().createNetworkSwitchStackRoutingInterface(**kwargs)

@register('getNetworkSwitchStackRoutingInterface')
def getNetworkSwitchStackRoutingInterface(**kwargs):
    return MerakiClient().getNetworkSwitchStackRoutingInterface(**kwargs)

@register('updateNetworkSwitchStackRoutingInterface')
def updateNetworkSwitchStackRoutingInterface(**kwargs):
    return MerakiClient().updateNetworkSwitchStackRoutingInterface(**kwargs)

@register('deleteNetworkSwitchStackRoutingInterface')
def deleteNetworkSwitchStackRoutingInterface(**kwargs):
    return MerakiClient().deleteNetworkSwitchStackRoutingInterface(**kwargs)

@register('getNetworkSwitchStackRoutingInterfaceDhcp')
def getNetworkSwitchStackRoutingInterfaceDhcp(**kwargs):
    return MerakiClient().getNetworkSwitchStackRoutingInterfaceDhcp(**kwargs)

@register('updateNetworkSwitchStackRoutingInterfaceDhcp')
def updateNetworkSwitchStackRoutingInterfaceDhcp(**kwargs):
    return MerakiClient().updateNetworkSwitchStackRoutingInterfaceDhcp(**kwargs)

@register('getNetworkSwitchStackRoutingStaticRoutes')
def getNetworkSwitchStackRoutingStaticRoutes(**kwargs):
    return MerakiClient().getNetworkSwitchStackRoutingStaticRoutes(**kwargs)

@register('createNetworkSwitchStackRoutingStaticRoute')
def createNetworkSwitchStackRoutingStaticRoute(**kwargs):
    return MerakiClient().createNetworkSwitchStackRoutingStaticRoute(**kwargs)

@register('getNetworkSwitchStackRoutingStaticRoute')
def getNetworkSwitchStackRoutingStaticRoute(**kwargs):
    return MerakiClient().getNetworkSwitchStackRoutingStaticRoute(**kwargs)

@register('updateNetworkSwitchStackRoutingStaticRoute')
def updateNetworkSwitchStackRoutingStaticRoute(**kwargs):
    return MerakiClient().updateNetworkSwitchStackRoutingStaticRoute(**kwargs)

@register('deleteNetworkSwitchStackRoutingStaticRoute')
def deleteNetworkSwitchStackRoutingStaticRoute(**kwargs):
    return MerakiClient().deleteNetworkSwitchStackRoutingStaticRoute(**kwargs)

@register('getNetworkSwitchStormControl')
def getNetworkSwitchStormControl(**kwargs):
    return MerakiClient().getNetworkSwitchStormControl(**kwargs)

@register('updateNetworkSwitchStormControl')
def updateNetworkSwitchStormControl(**kwargs):
    return MerakiClient().updateNetworkSwitchStormControl(**kwargs)

@register('getNetworkSwitchStp')
def getNetworkSwitchStp(**kwargs):
    return MerakiClient().getNetworkSwitchStp(**kwargs)

@register('updateNetworkSwitchStp')
def updateNetworkSwitchStp(**kwargs):
    return MerakiClient().updateNetworkSwitchStp(**kwargs)

@register('getNetworkSyslogServers')
def getNetworkSyslogServers(**kwargs):
    return MerakiClient().getNetworkSyslogServers(**kwargs)

@register('updateNetworkSyslogServers')
def updateNetworkSyslogServers(**kwargs):
    return MerakiClient().updateNetworkSyslogServers(**kwargs)

@register('getNetworkTopologyLinkLayer')
def getNetworkTopologyLinkLayer(**kwargs):
    return MerakiClient().getNetworkTopologyLinkLayer(**kwargs)

@register('getNetworkTraffic')
def getNetworkTraffic(**kwargs):
    return MerakiClient().getNetworkTraffic(**kwargs)

@register('getNetworkTrafficAnalysis')
def getNetworkTrafficAnalysis(**kwargs):
    return MerakiClient().getNetworkTrafficAnalysis(**kwargs)

@register('updateNetworkTrafficAnalysis')
def updateNetworkTrafficAnalysis(**kwargs):
    return MerakiClient().updateNetworkTrafficAnalysis(**kwargs)

@register('getNetworkTrafficShapingApplicationCategories')
def getNetworkTrafficShapingApplicationCategories(**kwargs):
    return MerakiClient().getNetworkTrafficShapingApplicationCategories(**kwargs)

@register('getNetworkTrafficShapingDscpTaggingOptions')
def getNetworkTrafficShapingDscpTaggingOptions(**kwargs):
    return MerakiClient().getNetworkTrafficShapingDscpTaggingOptions(**kwargs)

@register('unbindNetwork')
def unbindNetwork(**kwargs):
    return MerakiClient().unbindNetwork(**kwargs)

@register('getNetworkVlanProfiles')
def getNetworkVlanProfiles(**kwargs):
    return MerakiClient().getNetworkVlanProfiles(**kwargs)

@register('createNetworkVlanProfile')
def createNetworkVlanProfile(**kwargs):
    return MerakiClient().createNetworkVlanProfile(**kwargs)

@register('getNetworkVlanProfilesAssignmentsByDevice')
def getNetworkVlanProfilesAssignmentsByDevice(**kwargs):
    return MerakiClient().getNetworkVlanProfilesAssignmentsByDevice(**kwargs)

@register('reassignNetworkVlanProfilesAssignments')
def reassignNetworkVlanProfilesAssignments(**kwargs):
    return MerakiClient().reassignNetworkVlanProfilesAssignments(**kwargs)

@register('getNetworkVlanProfile')
def getNetworkVlanProfile(**kwargs):
    return MerakiClient().getNetworkVlanProfile(**kwargs)

@register('updateNetworkVlanProfile')
def updateNetworkVlanProfile(**kwargs):
    return MerakiClient().updateNetworkVlanProfile(**kwargs)

@register('deleteNetworkVlanProfile')
def deleteNetworkVlanProfile(**kwargs):
    return MerakiClient().deleteNetworkVlanProfile(**kwargs)

@register('getNetworkWebhooksHttpServers')
def getNetworkWebhooksHttpServers(**kwargs):
    return MerakiClient().getNetworkWebhooksHttpServers(**kwargs)

@register('createNetworkWebhooksHttpServer')
def createNetworkWebhooksHttpServer(**kwargs):
    return MerakiClient().createNetworkWebhooksHttpServer(**kwargs)

@register('getNetworkWebhooksHttpServer')
def getNetworkWebhooksHttpServer(**kwargs):
    return MerakiClient().getNetworkWebhooksHttpServer(**kwargs)

@register('updateNetworkWebhooksHttpServer')
def updateNetworkWebhooksHttpServer(**kwargs):
    return MerakiClient().updateNetworkWebhooksHttpServer(**kwargs)

@register('deleteNetworkWebhooksHttpServer')
def deleteNetworkWebhooksHttpServer(**kwargs):
    return MerakiClient().deleteNetworkWebhooksHttpServer(**kwargs)

@register('getNetworkWebhooksPayloadTemplates')
def getNetworkWebhooksPayloadTemplates(**kwargs):
    return MerakiClient().getNetworkWebhooksPayloadTemplates(**kwargs)

@register('createNetworkWebhooksPayloadTemplate')
def createNetworkWebhooksPayloadTemplate(**kwargs):
    return MerakiClient().createNetworkWebhooksPayloadTemplate(**kwargs)

@register('getNetworkWebhooksPayloadTemplate')
def getNetworkWebhooksPayloadTemplate(**kwargs):
    return MerakiClient().getNetworkWebhooksPayloadTemplate(**kwargs)

@register('deleteNetworkWebhooksPayloadTemplate')
def deleteNetworkWebhooksPayloadTemplate(**kwargs):
    return MerakiClient().deleteNetworkWebhooksPayloadTemplate(**kwargs)

@register('updateNetworkWebhooksPayloadTemplate')
def updateNetworkWebhooksPayloadTemplate(**kwargs):
    return MerakiClient().updateNetworkWebhooksPayloadTemplate(**kwargs)

@register('createNetworkWebhooksWebhookTest')
def createNetworkWebhooksWebhookTest(**kwargs):
    return MerakiClient().createNetworkWebhooksWebhookTest(**kwargs)

@register('getNetworkWebhooksWebhookTest')
def getNetworkWebhooksWebhookTest(**kwargs):
    return MerakiClient().getNetworkWebhooksWebhookTest(**kwargs)

@register('getNetworkWirelessAirMarshal')
def getNetworkWirelessAirMarshal(**kwargs):
    return MerakiClient().getNetworkWirelessAirMarshal(**kwargs)

@register('createNetworkWirelessAirMarshalRule')
def createNetworkWirelessAirMarshalRule(**kwargs):
    return MerakiClient().createNetworkWirelessAirMarshalRule(**kwargs)

@register('updateNetworkWirelessAirMarshalRule')
def updateNetworkWirelessAirMarshalRule(**kwargs):
    return MerakiClient().updateNetworkWirelessAirMarshalRule(**kwargs)

@register('deleteNetworkWirelessAirMarshalRule')
def deleteNetworkWirelessAirMarshalRule(**kwargs):
    return MerakiClient().deleteNetworkWirelessAirMarshalRule(**kwargs)

@register('updateNetworkWirelessAirMarshalSettings')
def updateNetworkWirelessAirMarshalSettings(**kwargs):
    return MerakiClient().updateNetworkWirelessAirMarshalSettings(**kwargs)

@register('getNetworkWirelessAlternateManagementInterface')
def getNetworkWirelessAlternateManagementInterface(**kwargs):
    return MerakiClient().getNetworkWirelessAlternateManagementInterface(**kwargs)

@register('updateNetworkWirelessAlternateManagementInterface')
def updateNetworkWirelessAlternateManagementInterface(**kwargs):
    return MerakiClient().updateNetworkWirelessAlternateManagementInterface(**kwargs)

@register('getNetworkWirelessBilling')
def getNetworkWirelessBilling(**kwargs):
    return MerakiClient().getNetworkWirelessBilling(**kwargs)

@register('updateNetworkWirelessBilling')
def updateNetworkWirelessBilling(**kwargs):
    return MerakiClient().updateNetworkWirelessBilling(**kwargs)

@register('getNetworkWirelessBluetoothSettings')
def getNetworkWirelessBluetoothSettings(**kwargs):
    return MerakiClient().getNetworkWirelessBluetoothSettings(**kwargs)

@register('updateNetworkWirelessBluetoothSettings')
def updateNetworkWirelessBluetoothSettings(**kwargs):
    return MerakiClient().updateNetworkWirelessBluetoothSettings(**kwargs)

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

@register('updateNetworkWirelessElectronicShelfLabel')
def updateNetworkWirelessElectronicShelfLabel(**kwargs):
    return MerakiClient().updateNetworkWirelessElectronicShelfLabel(**kwargs)

@register('getNetworkWirelessElectronicShelfLabelConfiguredDevices')
def getNetworkWirelessElectronicShelfLabelConfiguredDevices(**kwargs):
    return MerakiClient().getNetworkWirelessElectronicShelfLabelConfiguredDevices(**kwargs)

@register('getNetworkWirelessEthernetPortsProfiles')
def getNetworkWirelessEthernetPortsProfiles(**kwargs):
    return MerakiClient().getNetworkWirelessEthernetPortsProfiles(**kwargs)

@register('createNetworkWirelessEthernetPortsProfile')
def createNetworkWirelessEthernetPortsProfile(**kwargs):
    return MerakiClient().createNetworkWirelessEthernetPortsProfile(**kwargs)

@register('assignNetworkWirelessEthernetPortsProfiles')
def assignNetworkWirelessEthernetPortsProfiles(**kwargs):
    return MerakiClient().assignNetworkWirelessEthernetPortsProfiles(**kwargs)

@register('setNetworkWirelessEthernetPortsProfilesDefault')
def setNetworkWirelessEthernetPortsProfilesDefault(**kwargs):
    return MerakiClient().setNetworkWirelessEthernetPortsProfilesDefault(**kwargs)

@register('getNetworkWirelessEthernetPortsProfile')
def getNetworkWirelessEthernetPortsProfile(**kwargs):
    return MerakiClient().getNetworkWirelessEthernetPortsProfile(**kwargs)

@register('updateNetworkWirelessEthernetPortsProfile')
def updateNetworkWirelessEthernetPortsProfile(**kwargs):
    return MerakiClient().updateNetworkWirelessEthernetPortsProfile(**kwargs)

@register('deleteNetworkWirelessEthernetPortsProfile')
def deleteNetworkWirelessEthernetPortsProfile(**kwargs):
    return MerakiClient().deleteNetworkWirelessEthernetPortsProfile(**kwargs)

@register('getNetworkWirelessFailedConnections')
def getNetworkWirelessFailedConnections(**kwargs):
    return MerakiClient().getNetworkWirelessFailedConnections(**kwargs)

@register('getNetworkWirelessLatencyHistory')
def getNetworkWirelessLatencyHistory(**kwargs):
    return MerakiClient().getNetworkWirelessLatencyHistory(**kwargs)

@register('getNetworkWirelessLatencyStats')
def getNetworkWirelessLatencyStats(**kwargs):
    return MerakiClient().getNetworkWirelessLatencyStats(**kwargs)

@register('updateNetworkWirelessLocationScanning')
def updateNetworkWirelessLocationScanning(**kwargs):
    return MerakiClient().updateNetworkWirelessLocationScanning(**kwargs)

@register('getNetworkWirelessMeshStatuses')
def getNetworkWirelessMeshStatuses(**kwargs):
    return MerakiClient().getNetworkWirelessMeshStatuses(**kwargs)

@register('getNetworkWirelessRfProfiles')
def getNetworkWirelessRfProfiles(**kwargs):
    return MerakiClient().getNetworkWirelessRfProfiles(**kwargs)

@register('createNetworkWirelessRfProfile')
def createNetworkWirelessRfProfile(**kwargs):
    return MerakiClient().createNetworkWirelessRfProfile(**kwargs)

@register('updateNetworkWirelessRfProfile')
def updateNetworkWirelessRfProfile(**kwargs):
    return MerakiClient().updateNetworkWirelessRfProfile(**kwargs)

@register('deleteNetworkWirelessRfProfile')
def deleteNetworkWirelessRfProfile(**kwargs):
    return MerakiClient().deleteNetworkWirelessRfProfile(**kwargs)

@register('getNetworkWirelessRfProfile')
def getNetworkWirelessRfProfile(**kwargs):
    return MerakiClient().getNetworkWirelessRfProfile(**kwargs)

@register('getNetworkWirelessSettings')
def getNetworkWirelessSettings(**kwargs):
    return MerakiClient().getNetworkWirelessSettings(**kwargs)

@register('updateNetworkWirelessSettings')
def updateNetworkWirelessSettings(**kwargs):
    return MerakiClient().updateNetworkWirelessSettings(**kwargs)

@register('getNetworkWirelessSignalQualityHistory')
def getNetworkWirelessSignalQualityHistory(**kwargs):
    return MerakiClient().getNetworkWirelessSignalQualityHistory(**kwargs)

@register('getNetworkWirelessSsids')
def getNetworkWirelessSsids(**kwargs):
    return MerakiClient().getNetworkWirelessSsids(**kwargs)

@register('getNetworkWirelessSsid')
def getNetworkWirelessSsid(**kwargs):
    return MerakiClient().getNetworkWirelessSsid(**kwargs)

@register('updateNetworkWirelessSsid')
def updateNetworkWirelessSsid(**kwargs):
    return MerakiClient().updateNetworkWirelessSsid(**kwargs)

@register('getNetworkWirelessSsidBonjourForwarding')
def getNetworkWirelessSsidBonjourForwarding(**kwargs):
    return MerakiClient().getNetworkWirelessSsidBonjourForwarding(**kwargs)

@register('updateNetworkWirelessSsidBonjourForwarding')
def updateNetworkWirelessSsidBonjourForwarding(**kwargs):
    return MerakiClient().updateNetworkWirelessSsidBonjourForwarding(**kwargs)

@register('getNetworkWirelessSsidDeviceTypeGroupPolicies')
def getNetworkWirelessSsidDeviceTypeGroupPolicies(**kwargs):
    return MerakiClient().getNetworkWirelessSsidDeviceTypeGroupPolicies(**kwargs)

@register('updateNetworkWirelessSsidDeviceTypeGroupPolicies')
def updateNetworkWirelessSsidDeviceTypeGroupPolicies(**kwargs):
    return MerakiClient().updateNetworkWirelessSsidDeviceTypeGroupPolicies(**kwargs)

@register('getNetworkWirelessSsidEapOverride')
def getNetworkWirelessSsidEapOverride(**kwargs):
    return MerakiClient().getNetworkWirelessSsidEapOverride(**kwargs)

@register('updateNetworkWirelessSsidEapOverride')
def updateNetworkWirelessSsidEapOverride(**kwargs):
    return MerakiClient().updateNetworkWirelessSsidEapOverride(**kwargs)

@register('getNetworkWirelessSsidFirewallL3FirewallRules')
def getNetworkWirelessSsidFirewallL3FirewallRules(**kwargs):
    return MerakiClient().getNetworkWirelessSsidFirewallL3FirewallRules(**kwargs)

@register('updateNetworkWirelessSsidFirewallL3FirewallRules')
def updateNetworkWirelessSsidFirewallL3FirewallRules(**kwargs):
    return MerakiClient().updateNetworkWirelessSsidFirewallL3FirewallRules(**kwargs)

@register('getNetworkWirelessSsidFirewallL7FirewallRules')
def getNetworkWirelessSsidFirewallL7FirewallRules(**kwargs):
    return MerakiClient().getNetworkWirelessSsidFirewallL7FirewallRules(**kwargs)

@register('updateNetworkWirelessSsidFirewallL7FirewallRules')
def updateNetworkWirelessSsidFirewallL7FirewallRules(**kwargs):
    return MerakiClient().updateNetworkWirelessSsidFirewallL7FirewallRules(**kwargs)

@register('getNetworkWirelessSsidHotspot20')
def getNetworkWirelessSsidHotspot20(**kwargs):
    return MerakiClient().getNetworkWirelessSsidHotspot20(**kwargs)

@register('updateNetworkWirelessSsidHotspot20')
def updateNetworkWirelessSsidHotspot20(**kwargs):
    return MerakiClient().updateNetworkWirelessSsidHotspot20(**kwargs)

@register('getNetworkWirelessSsidIdentityPsks')
def getNetworkWirelessSsidIdentityPsks(**kwargs):
    return MerakiClient().getNetworkWirelessSsidIdentityPsks(**kwargs)

@register('createNetworkWirelessSsidIdentityPsk')
def createNetworkWirelessSsidIdentityPsk(**kwargs):
    return MerakiClient().createNetworkWirelessSsidIdentityPsk(**kwargs)

@register('getNetworkWirelessSsidIdentityPsk')
def getNetworkWirelessSsidIdentityPsk(**kwargs):
    return MerakiClient().getNetworkWirelessSsidIdentityPsk(**kwargs)

@register('updateNetworkWirelessSsidIdentityPsk')
def updateNetworkWirelessSsidIdentityPsk(**kwargs):
    return MerakiClient().updateNetworkWirelessSsidIdentityPsk(**kwargs)

@register('deleteNetworkWirelessSsidIdentityPsk')
def deleteNetworkWirelessSsidIdentityPsk(**kwargs):
    return MerakiClient().deleteNetworkWirelessSsidIdentityPsk(**kwargs)

@register('getNetworkWirelessSsidSchedules')
def getNetworkWirelessSsidSchedules(**kwargs):
    return MerakiClient().getNetworkWirelessSsidSchedules(**kwargs)

@register('updateNetworkWirelessSsidSchedules')
def updateNetworkWirelessSsidSchedules(**kwargs):
    return MerakiClient().updateNetworkWirelessSsidSchedules(**kwargs)

@register('getNetworkWirelessSsidSplashSettings')
def getNetworkWirelessSsidSplashSettings(**kwargs):
    return MerakiClient().getNetworkWirelessSsidSplashSettings(**kwargs)

@register('updateNetworkWirelessSsidSplashSettings')
def updateNetworkWirelessSsidSplashSettings(**kwargs):
    return MerakiClient().updateNetworkWirelessSsidSplashSettings(**kwargs)

@register('updateNetworkWirelessSsidTrafficShapingRules')
def updateNetworkWirelessSsidTrafficShapingRules(**kwargs):
    return MerakiClient().updateNetworkWirelessSsidTrafficShapingRules(**kwargs)

@register('getNetworkWirelessSsidTrafficShapingRules')
def getNetworkWirelessSsidTrafficShapingRules(**kwargs):
    return MerakiClient().getNetworkWirelessSsidTrafficShapingRules(**kwargs)

@register('getNetworkWirelessSsidVpn')
def getNetworkWirelessSsidVpn(**kwargs):
    return MerakiClient().getNetworkWirelessSsidVpn(**kwargs)

@register('updateNetworkWirelessSsidVpn')
def updateNetworkWirelessSsidVpn(**kwargs):
    return MerakiClient().updateNetworkWirelessSsidVpn(**kwargs)

@register('getNetworkWirelessUsageHistory')
def getNetworkWirelessUsageHistory(**kwargs):
    return MerakiClient().getNetworkWirelessUsageHistory(**kwargs)

@register('getOrganizations')
def getOrganizations(**kwargs):
    return MerakiClient().getOrganizations(**kwargs)

@register('createOrganization')
def createOrganization(**kwargs):
    return MerakiClient().createOrganization(**kwargs)

@register('getOrganization')
def getOrganization(**kwargs):
    return MerakiClient().getOrganization(**kwargs)

@register('updateOrganization')
def updateOrganization(**kwargs):
    return MerakiClient().updateOrganization(**kwargs)

@register('deleteOrganization')
def deleteOrganization(**kwargs):
    return MerakiClient().deleteOrganization(**kwargs)

@register('createOrganizationActionBatch')
def createOrganizationActionBatch(**kwargs):
    return MerakiClient().createOrganizationActionBatch(**kwargs)

@register('getOrganizationActionBatches')
def getOrganizationActionBatches(**kwargs):
    return MerakiClient().getOrganizationActionBatches(**kwargs)

@register('getOrganizationActionBatch')
def getOrganizationActionBatch(**kwargs):
    return MerakiClient().getOrganizationActionBatch(**kwargs)

@register('deleteOrganizationActionBatch')
def deleteOrganizationActionBatch(**kwargs):
    return MerakiClient().deleteOrganizationActionBatch(**kwargs)

@register('updateOrganizationActionBatch')
def updateOrganizationActionBatch(**kwargs):
    return MerakiClient().updateOrganizationActionBatch(**kwargs)

@register('getOrganizationAdaptivePolicyAcls')
def getOrganizationAdaptivePolicyAcls(**kwargs):
    return MerakiClient().getOrganizationAdaptivePolicyAcls(**kwargs)

@register('createOrganizationAdaptivePolicyAcl')
def createOrganizationAdaptivePolicyAcl(**kwargs):
    return MerakiClient().createOrganizationAdaptivePolicyAcl(**kwargs)

@register('getOrganizationAdaptivePolicyAcl')
def getOrganizationAdaptivePolicyAcl(**kwargs):
    return MerakiClient().getOrganizationAdaptivePolicyAcl(**kwargs)

@register('updateOrganizationAdaptivePolicyAcl')
def updateOrganizationAdaptivePolicyAcl(**kwargs):
    return MerakiClient().updateOrganizationAdaptivePolicyAcl(**kwargs)

@register('deleteOrganizationAdaptivePolicyAcl')
def deleteOrganizationAdaptivePolicyAcl(**kwargs):
    return MerakiClient().deleteOrganizationAdaptivePolicyAcl(**kwargs)

@register('getOrganizationAdaptivePolicyGroups')
def getOrganizationAdaptivePolicyGroups(**kwargs):
    return MerakiClient().getOrganizationAdaptivePolicyGroups(**kwargs)

@register('createOrganizationAdaptivePolicyGroup')
def createOrganizationAdaptivePolicyGroup(**kwargs):
    return MerakiClient().createOrganizationAdaptivePolicyGroup(**kwargs)

@register('getOrganizationAdaptivePolicyGroup')
def getOrganizationAdaptivePolicyGroup(**kwargs):
    return MerakiClient().getOrganizationAdaptivePolicyGroup(**kwargs)

@register('updateOrganizationAdaptivePolicyGroup')
def updateOrganizationAdaptivePolicyGroup(**kwargs):
    return MerakiClient().updateOrganizationAdaptivePolicyGroup(**kwargs)

@register('deleteOrganizationAdaptivePolicyGroup')
def deleteOrganizationAdaptivePolicyGroup(**kwargs):
    return MerakiClient().deleteOrganizationAdaptivePolicyGroup(**kwargs)

@register('getOrganizationAdaptivePolicyOverview')
def getOrganizationAdaptivePolicyOverview(**kwargs):
    return MerakiClient().getOrganizationAdaptivePolicyOverview(**kwargs)

@register('getOrganizationAdaptivePolicyPolicies')
def getOrganizationAdaptivePolicyPolicies(**kwargs):
    return MerakiClient().getOrganizationAdaptivePolicyPolicies(**kwargs)

@register('createOrganizationAdaptivePolicyPolicy')
def createOrganizationAdaptivePolicyPolicy(**kwargs):
    return MerakiClient().createOrganizationAdaptivePolicyPolicy(**kwargs)

@register('getOrganizationAdaptivePolicyPolicy')
def getOrganizationAdaptivePolicyPolicy(**kwargs):
    return MerakiClient().getOrganizationAdaptivePolicyPolicy(**kwargs)

@register('updateOrganizationAdaptivePolicyPolicy')
def updateOrganizationAdaptivePolicyPolicy(**kwargs):
    return MerakiClient().updateOrganizationAdaptivePolicyPolicy(**kwargs)

@register('deleteOrganizationAdaptivePolicyPolicy')
def deleteOrganizationAdaptivePolicyPolicy(**kwargs):
    return MerakiClient().deleteOrganizationAdaptivePolicyPolicy(**kwargs)

@register('getOrganizationAdaptivePolicySettings')
def getOrganizationAdaptivePolicySettings(**kwargs):
    return MerakiClient().getOrganizationAdaptivePolicySettings(**kwargs)

@register('updateOrganizationAdaptivePolicySettings')
def updateOrganizationAdaptivePolicySettings(**kwargs):
    return MerakiClient().updateOrganizationAdaptivePolicySettings(**kwargs)

@register('getOrganizationAdmins')
def getOrganizationAdmins(**kwargs):
    return MerakiClient().getOrganizationAdmins(**kwargs)

@register('createOrganizationAdmin')
def createOrganizationAdmin(**kwargs):
    return MerakiClient().createOrganizationAdmin(**kwargs)

@register('updateOrganizationAdmin')
def updateOrganizationAdmin(**kwargs):
    return MerakiClient().updateOrganizationAdmin(**kwargs)

@register('deleteOrganizationAdmin')
def deleteOrganizationAdmin(**kwargs):
    return MerakiClient().deleteOrganizationAdmin(**kwargs)

@register('getOrganizationAlertsProfiles')
def getOrganizationAlertsProfiles(**kwargs):
    return MerakiClient().getOrganizationAlertsProfiles(**kwargs)

@register('createOrganizationAlertsProfile')
def createOrganizationAlertsProfile(**kwargs):
    return MerakiClient().createOrganizationAlertsProfile(**kwargs)

@register('updateOrganizationAlertsProfile')
def updateOrganizationAlertsProfile(**kwargs):
    return MerakiClient().updateOrganizationAlertsProfile(**kwargs)

@register('deleteOrganizationAlertsProfile')
def deleteOrganizationAlertsProfile(**kwargs):
    return MerakiClient().deleteOrganizationAlertsProfile(**kwargs)

@register('getOrganizationApiRequests')
def getOrganizationApiRequests(**kwargs):
    return MerakiClient().getOrganizationApiRequests(**kwargs)

@register('getOrganizationApiRequestsOverview')
def getOrganizationApiRequestsOverview(**kwargs):
    return MerakiClient().getOrganizationApiRequestsOverview(**kwargs)

@register('getOrganizationApiRequestsOverviewResponseCodesByInterval')
def getOrganizationApiRequestsOverviewResponseCodesByInterval(**kwargs):
    return MerakiClient().getOrganizationApiRequestsOverviewResponseCodesByInterval(**kwargs)

@register('getOrganizationApplianceDnsLocalProfiles')
def getOrganizationApplianceDnsLocalProfiles(**kwargs):
    return MerakiClient().getOrganizationApplianceDnsLocalProfiles(**kwargs)

@register('createOrganizationApplianceDnsLocalProfile')
def createOrganizationApplianceDnsLocalProfile(**kwargs):
    return MerakiClient().createOrganizationApplianceDnsLocalProfile(**kwargs)

@register('getOrganizationApplianceDnsLocalProfilesAssignments')
def getOrganizationApplianceDnsLocalProfilesAssignments(**kwargs):
    return MerakiClient().getOrganizationApplianceDnsLocalProfilesAssignments(**kwargs)

@register('bulkOrganizationApplianceDnsLocalProfilesAssignmentsCreate')
def bulkOrganizationApplianceDnsLocalProfilesAssignmentsCreate(**kwargs):
    return MerakiClient().bulkOrganizationApplianceDnsLocalProfilesAssignmentsCreate(**kwargs)

@register('createOrganizationApplianceDnsLocalProfilesAssignmentsBulkDelete')
def createOrganizationApplianceDnsLocalProfilesAssignmentsBulkDelete(**kwargs):
    return MerakiClient().createOrganizationApplianceDnsLocalProfilesAssignmentsBulkDelete(**kwargs)

@register('updateOrganizationApplianceDnsLocalProfile')
def updateOrganizationApplianceDnsLocalProfile(**kwargs):
    return MerakiClient().updateOrganizationApplianceDnsLocalProfile(**kwargs)

@register('deleteOrganizationApplianceDnsLocalProfile')
def deleteOrganizationApplianceDnsLocalProfile(**kwargs):
    return MerakiClient().deleteOrganizationApplianceDnsLocalProfile(**kwargs)

@register('getOrganizationApplianceDnsLocalRecords')
def getOrganizationApplianceDnsLocalRecords(**kwargs):
    return MerakiClient().getOrganizationApplianceDnsLocalRecords(**kwargs)

@register('createOrganizationApplianceDnsLocalRecord')
def createOrganizationApplianceDnsLocalRecord(**kwargs):
    return MerakiClient().createOrganizationApplianceDnsLocalRecord(**kwargs)

@register('updateOrganizationApplianceDnsLocalRecord')
def updateOrganizationApplianceDnsLocalRecord(**kwargs):
    return MerakiClient().updateOrganizationApplianceDnsLocalRecord(**kwargs)

@register('deleteOrganizationApplianceDnsLocalRecord')
def deleteOrganizationApplianceDnsLocalRecord(**kwargs):
    return MerakiClient().deleteOrganizationApplianceDnsLocalRecord(**kwargs)

@register('getOrganizationApplianceDnsSplitProfiles')
def getOrganizationApplianceDnsSplitProfiles(**kwargs):
    return MerakiClient().getOrganizationApplianceDnsSplitProfiles(**kwargs)

@register('createOrganizationApplianceDnsSplitProfile')
def createOrganizationApplianceDnsSplitProfile(**kwargs):
    return MerakiClient().createOrganizationApplianceDnsSplitProfile(**kwargs)

@register('getOrganizationApplianceDnsSplitProfilesAssignments')
def getOrganizationApplianceDnsSplitProfilesAssignments(**kwargs):
    return MerakiClient().getOrganizationApplianceDnsSplitProfilesAssignments(**kwargs)

@register('createOrganizationApplianceDnsSplitProfilesAssignmentsBulkCreate')
def createOrganizationApplianceDnsSplitProfilesAssignmentsBulkCreate(**kwargs):
    return MerakiClient().createOrganizationApplianceDnsSplitProfilesAssignmentsBulkCreate(**kwargs)

@register('createOrganizationApplianceDnsSplitProfilesAssignmentsBulkDelete')
def createOrganizationApplianceDnsSplitProfilesAssignmentsBulkDelete(**kwargs):
    return MerakiClient().createOrganizationApplianceDnsSplitProfilesAssignmentsBulkDelete(**kwargs)

@register('updateOrganizationApplianceDnsSplitProfile')
def updateOrganizationApplianceDnsSplitProfile(**kwargs):
    return MerakiClient().updateOrganizationApplianceDnsSplitProfile(**kwargs)

@register('deleteOrganizationApplianceDnsSplitProfile')
def deleteOrganizationApplianceDnsSplitProfile(**kwargs):
    return MerakiClient().deleteOrganizationApplianceDnsSplitProfile(**kwargs)

@register('getOrganizationApplianceFirewallMulticastForwardingByNetwork')
def getOrganizationApplianceFirewallMulticastForwardingByNetwork(**kwargs):
    return MerakiClient().getOrganizationApplianceFirewallMulticastForwardingByNetwork(**kwargs)

@register('getOrganizationApplianceSecurityEvents')
def getOrganizationApplianceSecurityEvents(**kwargs):
    return MerakiClient().getOrganizationApplianceSecurityEvents(**kwargs)

@register('getOrganizationApplianceSecurityIntrusion')
def getOrganizationApplianceSecurityIntrusion(**kwargs):
    return MerakiClient().getOrganizationApplianceSecurityIntrusion(**kwargs)

@register('updateOrganizationApplianceSecurityIntrusion')
def updateOrganizationApplianceSecurityIntrusion(**kwargs):
    return MerakiClient().updateOrganizationApplianceSecurityIntrusion(**kwargs)

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

@register('updateOrganizationApplianceVpnThirdPartyVPNPeers')
def updateOrganizationApplianceVpnThirdPartyVPNPeers(**kwargs):
    return MerakiClient().updateOrganizationApplianceVpnThirdPartyVPNPeers(**kwargs)

@register('getOrganizationApplianceVpnVpnFirewallRules')
def getOrganizationApplianceVpnVpnFirewallRules(**kwargs):
    return MerakiClient().getOrganizationApplianceVpnVpnFirewallRules(**kwargs)

@register('updateOrganizationApplianceVpnVpnFirewallRules')
def updateOrganizationApplianceVpnVpnFirewallRules(**kwargs):
    return MerakiClient().updateOrganizationApplianceVpnVpnFirewallRules(**kwargs)

@register('getOrganizationAssuranceAlerts')
def getOrganizationAssuranceAlerts(**kwargs):
    return MerakiClient().getOrganizationAssuranceAlerts(**kwargs)

@register('dismissOrganizationAssuranceAlerts')
def dismissOrganizationAssuranceAlerts(**kwargs):
    return MerakiClient().dismissOrganizationAssuranceAlerts(**kwargs)

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

@register('restoreOrganizationAssuranceAlerts')
def restoreOrganizationAssuranceAlerts(**kwargs):
    return MerakiClient().restoreOrganizationAssuranceAlerts(**kwargs)

@register('getOrganizationAssuranceAlert')
def getOrganizationAssuranceAlert(**kwargs):
    return MerakiClient().getOrganizationAssuranceAlert(**kwargs)

@register('getOrganizationBrandingPolicies')
def getOrganizationBrandingPolicies(**kwargs):
    return MerakiClient().getOrganizationBrandingPolicies(**kwargs)

@register('createOrganizationBrandingPolicy')
def createOrganizationBrandingPolicy(**kwargs):
    return MerakiClient().createOrganizationBrandingPolicy(**kwargs)

@register('getOrganizationBrandingPoliciesPriorities')
def getOrganizationBrandingPoliciesPriorities(**kwargs):
    return MerakiClient().getOrganizationBrandingPoliciesPriorities(**kwargs)

@register('updateOrganizationBrandingPoliciesPriorities')
def updateOrganizationBrandingPoliciesPriorities(**kwargs):
    return MerakiClient().updateOrganizationBrandingPoliciesPriorities(**kwargs)

@register('getOrganizationBrandingPolicy')
def getOrganizationBrandingPolicy(**kwargs):
    return MerakiClient().getOrganizationBrandingPolicy(**kwargs)

@register('updateOrganizationBrandingPolicy')
def updateOrganizationBrandingPolicy(**kwargs):
    return MerakiClient().updateOrganizationBrandingPolicy(**kwargs)

@register('deleteOrganizationBrandingPolicy')
def deleteOrganizationBrandingPolicy(**kwargs):
    return MerakiClient().deleteOrganizationBrandingPolicy(**kwargs)

@register('getOrganizationCameraBoundariesAreasByDevice')
def getOrganizationCameraBoundariesAreasByDevice(**kwargs):
    return MerakiClient().getOrganizationCameraBoundariesAreasByDevice(**kwargs)

@register('getOrganizationCameraBoundariesLinesByDevice')
def getOrganizationCameraBoundariesLinesByDevice(**kwargs):
    return MerakiClient().getOrganizationCameraBoundariesLinesByDevice(**kwargs)

@register('getOrganizationCameraCustomAnalyticsArtifacts')
def getOrganizationCameraCustomAnalyticsArtifacts(**kwargs):
    return MerakiClient().getOrganizationCameraCustomAnalyticsArtifacts(**kwargs)

@register('createOrganizationCameraCustomAnalyticsArtifact')
def createOrganizationCameraCustomAnalyticsArtifact(**kwargs):
    return MerakiClient().createOrganizationCameraCustomAnalyticsArtifact(**kwargs)

@register('getOrganizationCameraCustomAnalyticsArtifact')
def getOrganizationCameraCustomAnalyticsArtifact(**kwargs):
    return MerakiClient().getOrganizationCameraCustomAnalyticsArtifact(**kwargs)

@register('deleteOrganizationCameraCustomAnalyticsArtifact')
def deleteOrganizationCameraCustomAnalyticsArtifact(**kwargs):
    return MerakiClient().deleteOrganizationCameraCustomAnalyticsArtifact(**kwargs)

@register('getOrganizationCameraDetectionsHistoryByBoundaryByInterval')
def getOrganizationCameraDetectionsHistoryByBoundaryByInterval(**kwargs):
    return MerakiClient().getOrganizationCameraDetectionsHistoryByBoundaryByInterval(**kwargs)

@register('getOrganizationCameraOnboardingStatuses')
def getOrganizationCameraOnboardingStatuses(**kwargs):
    return MerakiClient().getOrganizationCameraOnboardingStatuses(**kwargs)

@register('updateOrganizationCameraOnboardingStatuses')
def updateOrganizationCameraOnboardingStatuses(**kwargs):
    return MerakiClient().updateOrganizationCameraOnboardingStatuses(**kwargs)

@register('getOrganizationCameraPermissions')
def getOrganizationCameraPermissions(**kwargs):
    return MerakiClient().getOrganizationCameraPermissions(**kwargs)

@register('getOrganizationCameraPermission')
def getOrganizationCameraPermission(**kwargs):
    return MerakiClient().getOrganizationCameraPermission(**kwargs)

@register('getOrganizationCameraRoles')
def getOrganizationCameraRoles(**kwargs):
    return MerakiClient().getOrganizationCameraRoles(**kwargs)

@register('createOrganizationCameraRole')
def createOrganizationCameraRole(**kwargs):
    return MerakiClient().createOrganizationCameraRole(**kwargs)

@register('getOrganizationCameraRole')
def getOrganizationCameraRole(**kwargs):
    return MerakiClient().getOrganizationCameraRole(**kwargs)

@register('deleteOrganizationCameraRole')
def deleteOrganizationCameraRole(**kwargs):
    return MerakiClient().deleteOrganizationCameraRole(**kwargs)

@register('updateOrganizationCameraRole')
def updateOrganizationCameraRole(**kwargs):
    return MerakiClient().updateOrganizationCameraRole(**kwargs)

@register('getOrganizationCellularGatewayEsimsInventory')
def getOrganizationCellularGatewayEsimsInventory(**kwargs):
    return MerakiClient().getOrganizationCellularGatewayEsimsInventory(**kwargs)

@register('updateOrganizationCellularGatewayEsimsInventory')
def updateOrganizationCellularGatewayEsimsInventory(**kwargs):
    return MerakiClient().updateOrganizationCellularGatewayEsimsInventory(**kwargs)

@register('getOrganizationCellularGatewayEsimsServiceProviders')
def getOrganizationCellularGatewayEsimsServiceProviders(**kwargs):
    return MerakiClient().getOrganizationCellularGatewayEsimsServiceProviders(**kwargs)

@register('getOrganizationCellularGatewayEsimsServiceProvidersAccounts')
def getOrganizationCellularGatewayEsimsServiceProvidersAccounts(**kwargs):
    return MerakiClient().getOrganizationCellularGatewayEsimsServiceProvidersAccounts(**kwargs)

@register('createOrganizationCellularGatewayEsimsServiceProvidersAccount')
def createOrganizationCellularGatewayEsimsServiceProvidersAccount(**kwargs):
    return MerakiClient().createOrganizationCellularGatewayEsimsServiceProvidersAccount(**kwargs)

@register('getOrganizationCellularGatewayEsimsServiceProvidersAccountsCommunicationPlans')
def getOrganizationCellularGatewayEsimsServiceProvidersAccountsCommunicationPlans(**kwargs):
    return MerakiClient().getOrganizationCellularGatewayEsimsServiceProvidersAccountsCommunicationPlans(**kwargs)

@register('getOrganizationCellularGatewayEsimsServiceProvidersAccountsRatePlans')
def getOrganizationCellularGatewayEsimsServiceProvidersAccountsRatePlans(**kwargs):
    return MerakiClient().getOrganizationCellularGatewayEsimsServiceProvidersAccountsRatePlans(**kwargs)

@register('updateOrganizationCellularGatewayEsimsServiceProvidersAccount')
def updateOrganizationCellularGatewayEsimsServiceProvidersAccount(**kwargs):
    return MerakiClient().updateOrganizationCellularGatewayEsimsServiceProvidersAccount(**kwargs)

@register('deleteOrganizationCellularGatewayEsimsServiceProvidersAccount')
def deleteOrganizationCellularGatewayEsimsServiceProvidersAccount(**kwargs):
    return MerakiClient().deleteOrganizationCellularGatewayEsimsServiceProvidersAccount(**kwargs)

@register('createOrganizationCellularGatewayEsimsSwap')
def createOrganizationCellularGatewayEsimsSwap(**kwargs):
    return MerakiClient().createOrganizationCellularGatewayEsimsSwap(**kwargs)

@register('updateOrganizationCellularGatewayEsimsSwap')
def updateOrganizationCellularGatewayEsimsSwap(**kwargs):
    return MerakiClient().updateOrganizationCellularGatewayEsimsSwap(**kwargs)

@register('getOrganizationCellularGatewayUplinkStatuses')
def getOrganizationCellularGatewayUplinkStatuses(**kwargs):
    return MerakiClient().getOrganizationCellularGatewayUplinkStatuses(**kwargs)

@register('claimIntoOrganization')
def claimIntoOrganization(**kwargs):
    return MerakiClient().claimIntoOrganization(**kwargs)

@register('getOrganizationClientsBandwidthUsageHistory')
def getOrganizationClientsBandwidthUsageHistory(**kwargs):
    return MerakiClient().getOrganizationClientsBandwidthUsageHistory(**kwargs)

@register('getOrganizationClientsOverview')
def getOrganizationClientsOverview(**kwargs):
    return MerakiClient().getOrganizationClientsOverview(**kwargs)

@register('getOrganizationClientsSearch')
def getOrganizationClientsSearch(**kwargs):
    return MerakiClient().getOrganizationClientsSearch(**kwargs)

@register('cloneOrganization')
def cloneOrganization(**kwargs):
    return MerakiClient().cloneOrganization(**kwargs)

@register('getOrganizationConfigTemplates')
def getOrganizationConfigTemplates(**kwargs):
    return MerakiClient().getOrganizationConfigTemplates(**kwargs)

@register('createOrganizationConfigTemplate')
def createOrganizationConfigTemplate(**kwargs):
    return MerakiClient().createOrganizationConfigTemplate(**kwargs)

@register('getOrganizationConfigTemplate')
def getOrganizationConfigTemplate(**kwargs):
    return MerakiClient().getOrganizationConfigTemplate(**kwargs)

@register('updateOrganizationConfigTemplate')
def updateOrganizationConfigTemplate(**kwargs):
    return MerakiClient().updateOrganizationConfigTemplate(**kwargs)

@register('deleteOrganizationConfigTemplate')
def deleteOrganizationConfigTemplate(**kwargs):
    return MerakiClient().deleteOrganizationConfigTemplate(**kwargs)

@register('getOrganizationConfigTemplateSwitchProfiles')
def getOrganizationConfigTemplateSwitchProfiles(**kwargs):
    return MerakiClient().getOrganizationConfigTemplateSwitchProfiles(**kwargs)

@register('getOrganizationConfigTemplateSwitchProfilePorts')
def getOrganizationConfigTemplateSwitchProfilePorts(**kwargs):
    return MerakiClient().getOrganizationConfigTemplateSwitchProfilePorts(**kwargs)

@register('getOrganizationConfigTemplateSwitchProfilePort')
def getOrganizationConfigTemplateSwitchProfilePort(**kwargs):
    return MerakiClient().getOrganizationConfigTemplateSwitchProfilePort(**kwargs)

@register('updateOrganizationConfigTemplateSwitchProfilePort')
def updateOrganizationConfigTemplateSwitchProfilePort(**kwargs):
    return MerakiClient().updateOrganizationConfigTemplateSwitchProfilePort(**kwargs)

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

@register('createOrganizationDevicesControllerMigration')
def createOrganizationDevicesControllerMigration(**kwargs):
    return MerakiClient().createOrganizationDevicesControllerMigration(**kwargs)

@register('getOrganizationDevicesControllerMigrations')
def getOrganizationDevicesControllerMigrations(**kwargs):
    return MerakiClient().getOrganizationDevicesControllerMigrations(**kwargs)

@register('bulkUpdateOrganizationDevicesDetails')
def bulkUpdateOrganizationDevicesDetails(**kwargs):
    return MerakiClient().bulkUpdateOrganizationDevicesDetails(**kwargs)

@register('getOrganizationDevicesOverviewByModel')
def getOrganizationDevicesOverviewByModel(**kwargs):
    return MerakiClient().getOrganizationDevicesOverviewByModel(**kwargs)

@register('getOrganizationDevicesPacketCaptureCaptures')
def getOrganizationDevicesPacketCaptureCaptures(**kwargs):
    return MerakiClient().getOrganizationDevicesPacketCaptureCaptures(**kwargs)

@register('createOrganizationDevicesPacketCaptureCapture')
def createOrganizationDevicesPacketCaptureCapture(**kwargs):
    return MerakiClient().createOrganizationDevicesPacketCaptureCapture(**kwargs)

@register('bulkOrganizationDevicesPacketCaptureCapturesCreate')
def bulkOrganizationDevicesPacketCaptureCapturesCreate(**kwargs):
    return MerakiClient().bulkOrganizationDevicesPacketCaptureCapturesCreate(**kwargs)

@register('bulkOrganizationDevicesPacketCaptureCapturesDelete')
def bulkOrganizationDevicesPacketCaptureCapturesDelete(**kwargs):
    return MerakiClient().bulkOrganizationDevicesPacketCaptureCapturesDelete(**kwargs)

@register('deleteOrganizationDevicesPacketCaptureCapture')
def deleteOrganizationDevicesPacketCaptureCapture(**kwargs):
    return MerakiClient().deleteOrganizationDevicesPacketCaptureCapture(**kwargs)

@register('generateOrganizationDevicesPacketCaptureCaptureDownloadUrl')
def generateOrganizationDevicesPacketCaptureCaptureDownloadUrl(**kwargs):
    return MerakiClient().generateOrganizationDevicesPacketCaptureCaptureDownloadUrl(**kwargs)

@register('stopOrganizationDevicesPacketCaptureCapture')
def stopOrganizationDevicesPacketCaptureCapture(**kwargs):
    return MerakiClient().stopOrganizationDevicesPacketCaptureCapture(**kwargs)

@register('getOrganizationDevicesPacketCaptureSchedules')
def getOrganizationDevicesPacketCaptureSchedules(**kwargs):
    return MerakiClient().getOrganizationDevicesPacketCaptureSchedules(**kwargs)

@register('createOrganizationDevicesPacketCaptureSchedule')
def createOrganizationDevicesPacketCaptureSchedule(**kwargs):
    return MerakiClient().createOrganizationDevicesPacketCaptureSchedule(**kwargs)

@register('reorderOrganizationDevicesPacketCaptureSchedules')
def reorderOrganizationDevicesPacketCaptureSchedules(**kwargs):
    return MerakiClient().reorderOrganizationDevicesPacketCaptureSchedules(**kwargs)

@register('updateOrganizationDevicesPacketCaptureSchedule')
def updateOrganizationDevicesPacketCaptureSchedule(**kwargs):
    return MerakiClient().updateOrganizationDevicesPacketCaptureSchedule(**kwargs)

@register('deleteOrganizationDevicesPacketCaptureSchedule')
def deleteOrganizationDevicesPacketCaptureSchedule(**kwargs):
    return MerakiClient().deleteOrganizationDevicesPacketCaptureSchedule(**kwargs)

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

@register('getOrganizationDevicesSystemMemoryUsageHistoryByInterval')
def getOrganizationDevicesSystemMemoryUsageHistoryByInterval(**kwargs):
    return MerakiClient().getOrganizationDevicesSystemMemoryUsageHistoryByInterval(**kwargs)

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

@register('createOrganizationEarlyAccessFeaturesOptIn')
def createOrganizationEarlyAccessFeaturesOptIn(**kwargs):
    return MerakiClient().createOrganizationEarlyAccessFeaturesOptIn(**kwargs)

@register('getOrganizationEarlyAccessFeaturesOptIn')
def getOrganizationEarlyAccessFeaturesOptIn(**kwargs):
    return MerakiClient().getOrganizationEarlyAccessFeaturesOptIn(**kwargs)

@register('updateOrganizationEarlyAccessFeaturesOptIn')
def updateOrganizationEarlyAccessFeaturesOptIn(**kwargs):
    return MerakiClient().updateOrganizationEarlyAccessFeaturesOptIn(**kwargs)

@register('deleteOrganizationEarlyAccessFeaturesOptIn')
def deleteOrganizationEarlyAccessFeaturesOptIn(**kwargs):
    return MerakiClient().deleteOrganizationEarlyAccessFeaturesOptIn(**kwargs)

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

@register('createOrganizationInsightMonitoredMediaServer')
def createOrganizationInsightMonitoredMediaServer(**kwargs):
    return MerakiClient().createOrganizationInsightMonitoredMediaServer(**kwargs)

@register('getOrganizationInsightMonitoredMediaServer')
def getOrganizationInsightMonitoredMediaServer(**kwargs):
    return MerakiClient().getOrganizationInsightMonitoredMediaServer(**kwargs)

@register('updateOrganizationInsightMonitoredMediaServer')
def updateOrganizationInsightMonitoredMediaServer(**kwargs):
    return MerakiClient().updateOrganizationInsightMonitoredMediaServer(**kwargs)

@register('deleteOrganizationInsightMonitoredMediaServer')
def deleteOrganizationInsightMonitoredMediaServer(**kwargs):
    return MerakiClient().deleteOrganizationInsightMonitoredMediaServer(**kwargs)

@register('getOrganizationIntegrationsXdrNetworks')
def getOrganizationIntegrationsXdrNetworks(**kwargs):
    return MerakiClient().getOrganizationIntegrationsXdrNetworks(**kwargs)

@register('disableOrganizationIntegrationsXdrNetworks')
def disableOrganizationIntegrationsXdrNetworks(**kwargs):
    return MerakiClient().disableOrganizationIntegrationsXdrNetworks(**kwargs)

@register('enableOrganizationIntegrationsXdrNetworks')
def enableOrganizationIntegrationsXdrNetworks(**kwargs):
    return MerakiClient().enableOrganizationIntegrationsXdrNetworks(**kwargs)

@register('claimIntoOrganizationInventory')
def claimIntoOrganizationInventory(**kwargs):
    return MerakiClient().claimIntoOrganizationInventory(**kwargs)

@register('getOrganizationInventoryDevices')
def getOrganizationInventoryDevices(**kwargs):
    return MerakiClient().getOrganizationInventoryDevices(**kwargs)

@register('createOrganizationInventoryDevicesSwapsBulk')
def createOrganizationInventoryDevicesSwapsBulk(**kwargs):
    return MerakiClient().createOrganizationInventoryDevicesSwapsBulk(**kwargs)

@register('getOrganizationInventoryDevicesSwapsBulk')
def getOrganizationInventoryDevicesSwapsBulk(**kwargs):
    return MerakiClient().getOrganizationInventoryDevicesSwapsBulk(**kwargs)

@register('getOrganizationInventoryDevice')
def getOrganizationInventoryDevice(**kwargs):
    return MerakiClient().getOrganizationInventoryDevice(**kwargs)

@register('createOrganizationInventoryOnboardingCloudMonitoringExportEvent')
def createOrganizationInventoryOnboardingCloudMonitoringExportEvent(**kwargs):
    return MerakiClient().createOrganizationInventoryOnboardingCloudMonitoringExportEvent(**kwargs)

@register('createOrganizationInventoryOnboardingCloudMonitoringImport')
def createOrganizationInventoryOnboardingCloudMonitoringImport(**kwargs):
    return MerakiClient().createOrganizationInventoryOnboardingCloudMonitoringImport(**kwargs)

@register('getOrganizationInventoryOnboardingCloudMonitoringImports')
def getOrganizationInventoryOnboardingCloudMonitoringImports(**kwargs):
    return MerakiClient().getOrganizationInventoryOnboardingCloudMonitoringImports(**kwargs)

@register('getOrganizationInventoryOnboardingCloudMonitoringNetworks')
def getOrganizationInventoryOnboardingCloudMonitoringNetworks(**kwargs):
    return MerakiClient().getOrganizationInventoryOnboardingCloudMonitoringNetworks(**kwargs)

@register('createOrganizationInventoryOnboardingCloudMonitoringPrepare')
def createOrganizationInventoryOnboardingCloudMonitoringPrepare(**kwargs):
    return MerakiClient().createOrganizationInventoryOnboardingCloudMonitoringPrepare(**kwargs)

@register('releaseFromOrganizationInventory')
def releaseFromOrganizationInventory(**kwargs):
    return MerakiClient().releaseFromOrganizationInventory(**kwargs)

@register('getOrganizationLicenses')
def getOrganizationLicenses(**kwargs):
    return MerakiClient().getOrganizationLicenses(**kwargs)

@register('assignOrganizationLicensesSeats')
def assignOrganizationLicensesSeats(**kwargs):
    return MerakiClient().assignOrganizationLicensesSeats(**kwargs)

@register('moveOrganizationLicenses')
def moveOrganizationLicenses(**kwargs):
    return MerakiClient().moveOrganizationLicenses(**kwargs)

@register('moveOrganizationLicensesSeats')
def moveOrganizationLicensesSeats(**kwargs):
    return MerakiClient().moveOrganizationLicensesSeats(**kwargs)

@register('getOrganizationLicensesOverview')
def getOrganizationLicensesOverview(**kwargs):
    return MerakiClient().getOrganizationLicensesOverview(**kwargs)

@register('renewOrganizationLicensesSeats')
def renewOrganizationLicensesSeats(**kwargs):
    return MerakiClient().renewOrganizationLicensesSeats(**kwargs)

@register('getOrganizationLicense')
def getOrganizationLicense(**kwargs):
    return MerakiClient().getOrganizationLicense(**kwargs)

@register('updateOrganizationLicense')
def updateOrganizationLicense(**kwargs):
    return MerakiClient().updateOrganizationLicense(**kwargs)

@register('getOrganizationLicensingCotermLicenses')
def getOrganizationLicensingCotermLicenses(**kwargs):
    return MerakiClient().getOrganizationLicensingCotermLicenses(**kwargs)

@register('moveOrganizationLicensingCotermLicenses')
def moveOrganizationLicensingCotermLicenses(**kwargs):
    return MerakiClient().moveOrganizationLicensingCotermLicenses(**kwargs)

@register('getOrganizationLoginSecurity')
def getOrganizationLoginSecurity(**kwargs):
    return MerakiClient().getOrganizationLoginSecurity(**kwargs)

@register('updateOrganizationLoginSecurity')
def updateOrganizationLoginSecurity(**kwargs):
    return MerakiClient().updateOrganizationLoginSecurity(**kwargs)

@register('getOrganizationNetworks')
def getOrganizationNetworks(**kwargs):
    return MerakiClient().getOrganizationNetworks(**kwargs)

@register('createOrganizationNetwork')
def createOrganizationNetwork(**kwargs):
    return MerakiClient().createOrganizationNetwork(**kwargs)

@register('combineOrganizationNetworks')
def combineOrganizationNetworks(**kwargs):
    return MerakiClient().combineOrganizationNetworks(**kwargs)

@register('getOrganizationOpenapiSpec')
def getOrganizationOpenapiSpec(**kwargs):
    return MerakiClient().getOrganizationOpenapiSpec(**kwargs)

@register('getOrganizationPolicyObjects')
def getOrganizationPolicyObjects(**kwargs):
    return MerakiClient().getOrganizationPolicyObjects(**kwargs)

@register('createOrganizationPolicyObject')
def createOrganizationPolicyObject(**kwargs):
    return MerakiClient().createOrganizationPolicyObject(**kwargs)

@register('getOrganizationPolicyObjectsGroups')
def getOrganizationPolicyObjectsGroups(**kwargs):
    return MerakiClient().getOrganizationPolicyObjectsGroups(**kwargs)

@register('createOrganizationPolicyObjectsGroup')
def createOrganizationPolicyObjectsGroup(**kwargs):
    return MerakiClient().createOrganizationPolicyObjectsGroup(**kwargs)

@register('getOrganizationPolicyObjectsGroup')
def getOrganizationPolicyObjectsGroup(**kwargs):
    return MerakiClient().getOrganizationPolicyObjectsGroup(**kwargs)

@register('updateOrganizationPolicyObjectsGroup')
def updateOrganizationPolicyObjectsGroup(**kwargs):
    return MerakiClient().updateOrganizationPolicyObjectsGroup(**kwargs)

@register('deleteOrganizationPolicyObjectsGroup')
def deleteOrganizationPolicyObjectsGroup(**kwargs):
    return MerakiClient().deleteOrganizationPolicyObjectsGroup(**kwargs)

@register('getOrganizationPolicyObject')
def getOrganizationPolicyObject(**kwargs):
    return MerakiClient().getOrganizationPolicyObject(**kwargs)

@register('updateOrganizationPolicyObject')
def updateOrganizationPolicyObject(**kwargs):
    return MerakiClient().updateOrganizationPolicyObject(**kwargs)

@register('deleteOrganizationPolicyObject')
def deleteOrganizationPolicyObject(**kwargs):
    return MerakiClient().deleteOrganizationPolicyObject(**kwargs)

@register('getOrganizationSaml')
def getOrganizationSaml(**kwargs):
    return MerakiClient().getOrganizationSaml(**kwargs)

@register('updateOrganizationSaml')
def updateOrganizationSaml(**kwargs):
    return MerakiClient().updateOrganizationSaml(**kwargs)

@register('getOrganizationSamlIdps')
def getOrganizationSamlIdps(**kwargs):
    return MerakiClient().getOrganizationSamlIdps(**kwargs)

@register('createOrganizationSamlIdp')
def createOrganizationSamlIdp(**kwargs):
    return MerakiClient().createOrganizationSamlIdp(**kwargs)

@register('updateOrganizationSamlIdp')
def updateOrganizationSamlIdp(**kwargs):
    return MerakiClient().updateOrganizationSamlIdp(**kwargs)

@register('getOrganizationSamlIdp')
def getOrganizationSamlIdp(**kwargs):
    return MerakiClient().getOrganizationSamlIdp(**kwargs)

@register('deleteOrganizationSamlIdp')
def deleteOrganizationSamlIdp(**kwargs):
    return MerakiClient().deleteOrganizationSamlIdp(**kwargs)

@register('getOrganizationSamlRoles')
def getOrganizationSamlRoles(**kwargs):
    return MerakiClient().getOrganizationSamlRoles(**kwargs)

@register('createOrganizationSamlRole')
def createOrganizationSamlRole(**kwargs):
    return MerakiClient().createOrganizationSamlRole(**kwargs)

@register('getOrganizationSamlRole')
def getOrganizationSamlRole(**kwargs):
    return MerakiClient().getOrganizationSamlRole(**kwargs)

@register('updateOrganizationSamlRole')
def updateOrganizationSamlRole(**kwargs):
    return MerakiClient().updateOrganizationSamlRole(**kwargs)

@register('deleteOrganizationSamlRole')
def deleteOrganizationSamlRole(**kwargs):
    return MerakiClient().deleteOrganizationSamlRole(**kwargs)

@register('getOrganizationSensorReadingsHistory')
def getOrganizationSensorReadingsHistory(**kwargs):
    return MerakiClient().getOrganizationSensorReadingsHistory(**kwargs)

@register('getOrganizationSensorReadingsLatest')
def getOrganizationSensorReadingsLatest(**kwargs):
    return MerakiClient().getOrganizationSensorReadingsLatest(**kwargs)

@register('getOrganizationSmAdminsRoles')
def getOrganizationSmAdminsRoles(**kwargs):
    return MerakiClient().getOrganizationSmAdminsRoles(**kwargs)

@register('createOrganizationSmAdminsRole')
def createOrganizationSmAdminsRole(**kwargs):
    return MerakiClient().createOrganizationSmAdminsRole(**kwargs)

@register('getOrganizationSmAdminsRole')
def getOrganizationSmAdminsRole(**kwargs):
    return MerakiClient().getOrganizationSmAdminsRole(**kwargs)

@register('updateOrganizationSmAdminsRole')
def updateOrganizationSmAdminsRole(**kwargs):
    return MerakiClient().updateOrganizationSmAdminsRole(**kwargs)

@register('deleteOrganizationSmAdminsRole')
def deleteOrganizationSmAdminsRole(**kwargs):
    return MerakiClient().deleteOrganizationSmAdminsRole(**kwargs)

@register('getOrganizationSmApnsCert')
def getOrganizationSmApnsCert(**kwargs):
    return MerakiClient().getOrganizationSmApnsCert(**kwargs)

@register('updateOrganizationSmSentryPoliciesAssignments')
def updateOrganizationSmSentryPoliciesAssignments(**kwargs):
    return MerakiClient().updateOrganizationSmSentryPoliciesAssignments(**kwargs)

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

@register('updateOrganizationSnmp')
def updateOrganizationSnmp(**kwargs):
    return MerakiClient().updateOrganizationSnmp(**kwargs)

@register('getOrganizationSplashAsset')
def getOrganizationSplashAsset(**kwargs):
    return MerakiClient().getOrganizationSplashAsset(**kwargs)

@register('deleteOrganizationSplashAsset')
def deleteOrganizationSplashAsset(**kwargs):
    return MerakiClient().deleteOrganizationSplashAsset(**kwargs)

@register('getOrganizationSplashThemes')
def getOrganizationSplashThemes(**kwargs):
    return MerakiClient().getOrganizationSplashThemes(**kwargs)

@register('createOrganizationSplashTheme')
def createOrganizationSplashTheme(**kwargs):
    return MerakiClient().createOrganizationSplashTheme(**kwargs)

@register('deleteOrganizationSplashTheme')
def deleteOrganizationSplashTheme(**kwargs):
    return MerakiClient().deleteOrganizationSplashTheme(**kwargs)

@register('createOrganizationSplashThemeAsset')
def createOrganizationSplashThemeAsset(**kwargs):
    return MerakiClient().createOrganizationSplashThemeAsset(**kwargs)

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

@register('cloneOrganizationSwitchDevices')
def cloneOrganizationSwitchDevices(**kwargs):
    return MerakiClient().cloneOrganizationSwitchDevices(**kwargs)

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

@register('getOrganizationSwitchPortsUsageHistoryByDeviceByInterval')
def getOrganizationSwitchPortsUsageHistoryByDeviceByInterval(**kwargs):
    return MerakiClient().getOrganizationSwitchPortsUsageHistoryByDeviceByInterval(**kwargs)

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

@register('getOrganizationWirelessDevicesPowerModeHistory')
def getOrganizationWirelessDevicesPowerModeHistory(**kwargs):
    return MerakiClient().getOrganizationWirelessDevicesPowerModeHistory(**kwargs)

@register('getOrganizationWirelessDevicesSystemCpuLoadHistory')
def getOrganizationWirelessDevicesSystemCpuLoadHistory(**kwargs):
    return MerakiClient().getOrganizationWirelessDevicesSystemCpuLoadHistory(**kwargs)

@register('getOrganizationWirelessDevicesWirelessControllersByDevice')
def getOrganizationWirelessDevicesWirelessControllersByDevice(**kwargs):
    return MerakiClient().getOrganizationWirelessDevicesWirelessControllersByDevice(**kwargs)

@register('getOrganizationWirelessLocationScanningByNetwork')
def getOrganizationWirelessLocationScanningByNetwork(**kwargs):
    return MerakiClient().getOrganizationWirelessLocationScanningByNetwork(**kwargs)

@register('getOrganizationWirelessLocationScanningReceivers')
def getOrganizationWirelessLocationScanningReceivers(**kwargs):
    return MerakiClient().getOrganizationWirelessLocationScanningReceivers(**kwargs)

@register('createOrganizationWirelessLocationScanningReceiver')
def createOrganizationWirelessLocationScanningReceiver(**kwargs):
    return MerakiClient().createOrganizationWirelessLocationScanningReceiver(**kwargs)

@register('updateOrganizationWirelessLocationScanningReceiver')
def updateOrganizationWirelessLocationScanningReceiver(**kwargs):
    return MerakiClient().updateOrganizationWirelessLocationScanningReceiver(**kwargs)

@register('deleteOrganizationWirelessLocationScanningReceiver')
def deleteOrganizationWirelessLocationScanningReceiver(**kwargs):
    return MerakiClient().deleteOrganizationWirelessLocationScanningReceiver(**kwargs)

@register('recalculateOrganizationWirelessRadioAutoRfChannels')
def recalculateOrganizationWirelessRadioAutoRfChannels(**kwargs):
    return MerakiClient().recalculateOrganizationWirelessRadioAutoRfChannels(**kwargs)

@register('getOrganizationWirelessRfProfilesAssignmentsByDevice')
def getOrganizationWirelessRfProfilesAssignmentsByDevice(**kwargs):
    return MerakiClient().getOrganizationWirelessRfProfilesAssignmentsByDevice(**kwargs)

@register('getOrganizationWirelessSsidsFirewallIsolationAllowlistEntries')
def getOrganizationWirelessSsidsFirewallIsolationAllowlistEntries(**kwargs):
    return MerakiClient().getOrganizationWirelessSsidsFirewallIsolationAllowlistEntries(**kwargs)

@register('createOrganizationWirelessSsidsFirewallIsolationAllowlistEntry')
def createOrganizationWirelessSsidsFirewallIsolationAllowlistEntry(**kwargs):
    return MerakiClient().createOrganizationWirelessSsidsFirewallIsolationAllowlistEntry(**kwargs)

@register('deleteOrganizationWirelessSsidsFirewallIsolationAllowlistEntry')
def deleteOrganizationWirelessSsidsFirewallIsolationAllowlistEntry(**kwargs):
    return MerakiClient().deleteOrganizationWirelessSsidsFirewallIsolationAllowlistEntry(**kwargs)

@register('updateOrganizationWirelessSsidsFirewallIsolationAllowlistEntry')
def updateOrganizationWirelessSsidsFirewallIsolationAllowlistEntry(**kwargs):
    return MerakiClient().updateOrganizationWirelessSsidsFirewallIsolationAllowlistEntry(**kwargs)

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
